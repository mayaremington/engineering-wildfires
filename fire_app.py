import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from sqlalchemy import inspect

#To run this app, run `streamlit run fire_app.py` from inside this directory

st.write(
'''
# Wildfire Trends in California (2013-2020)
'''
)

st.write(
'''
#### Major Trends
'''
)

# connecting to SQL database
engine = create_engine('sqlite:///wildfires.db')
fire_df = pd.read_sql('SELECT * FROM cleaned_data', con=engine)
fire_df['start_date'] = pd.to_datetime(fire_df['start_date']).dt.date

def get_per_year_fig(per_year_df, ticks_y=None, y_label=None):
    '''Creates a plot based on aggregated fire data
    '''
    
    fig, ax = plt.subplots()

    x = per_year_df['year']
    y = per_year_df['total']
    ticks_y = ticks_y
    ax.plot(x, y, marker='o', color='#F25348')
    ax.set_xlabel('Year')
    ax.set_ylabel(y_label)
    ax.set_yticks(ticks_y)

    return st.pyplot(fig)

def get_top_df(per_year_df, sort_by):
    '''Gets a dataframe of top 10 based on an aggregated metric
    '''
    
    top_df = fire_df.loc[:, ['name', 'start_date', 'acres', 'destroyed', 'fatalities', 'counties', 'cause']].sort_values(by=sort_by, ascending=False).set_index('name').head(10)
    top_df['acres'] = top_df['acres'].apply(lambda x: int(x / 1000))
    
    return st.dataframe(top_df)  

options = ('Number of fires per year', 'Acres burned per year (in thousands)', 'Structures destroyed per year', 'Fatalities per year')
options_button = st.radio("Select one:", options)

if options_button == options[0]:
    fires_per_year = pd.read_sql('SELECT * FROM fires_per_year', con=engine)

    col1, col2 = st.columns([1,1.5])
    with col1:
        ticks_y = range(0, 500, 50)
        y_label = '# of wildfires'
        get_per_year_fig(fires_per_year, ticks_y=ticks_y, y_label=y_label)
        
    with col2:
        st.empty()

elif options_button == options[1]:
    acres_per_year = pd.read_sql('SELECT * FROM acres_per_year', con=engine)

    col1, col2 = st.columns([1,1.5])
    with col1:
        ticks_y = range(0, 3000, 500)
        y_label = 'Acres burned (in thousands)'
        get_per_year_fig(acres_per_year, ticks_y=ticks_y, y_label=y_label)

    with col2:
        # display df
        
        st.write(
        '''
        ##### Largest fires (in thousands of acres)
        '''
        )
        get_top_df(acres_per_year, sort_by='acres')        

elif options_button == options[2]:
    destroyed_per_year = pd.read_sql('SELECT * FROM destroyed_per_year', con=engine)

    col1, col2 = st.columns([1,1.5])
    with col1:
        ticks_y = range(0, 25000, 5000)
        y_label = 'Structures destroyed'
        get_per_year_fig(destroyed_per_year, ticks_y=ticks_y, y_label=y_label)

    with col2:
        # display df
        
        st.write(
        '''
        ##### Most destructive fires
        '''
        )
        get_top_df(destroyed_per_year, sort_by='destroyed')   

elif options_button == options[3]:
    fatalities_per_year = pd.read_sql('SELECT * FROM fatalities_per_year', con=engine)

    col1, col2 = st.columns([1,1.5])
    with col1:
        ticks_y = range(0, 100, 20)
        y_label = 'Fatalities'
        get_per_year_fig(fatalities_per_year, ticks_y=ticks_y, y_label=y_label)

    with col2:
        # display df
        
        st.write(
        '''
        ##### Deadliest fires
        '''
        )
        get_top_df(fatalities_per_year, sort_by='fatalities')        


st.write(
'''
#### Number of new wildfires (14-day rolling average)
'''
)

# importing from SQL db
fires_per_date = pd.read_sql('SELECT * FROM fires_per_date', con=engine)

# convert date to datetime format and isolate month-day
fires_per_date['date'] = pd.to_datetime(fires_per_date['date'])
fires_per_date['month-day'] = fires_per_date['date'].dt.strftime('%m-%d')

# get list of years in df
year_list = fires_per_date['date'].dt.year.unique()

# plot number of wildfires over course of the year (14-day rolling average)
for year in year_list:
    single_year = fires_per_date[fires_per_date['date'].dt.year == year]
    
    fig, ax = plt.subplots(figsize=[12, 2])
    x = single_year['month-day']
    y = single_year['avg_14d']
    ax.plot(x, y, color='#F25348')
    
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    ticks_x = np.linspace(0, 365, 12)
    ticks_y = np.linspace(0, 4, 5)

    ax.set_title(year, fontsize='18')
    #ax.set_xlabel('Months', fontsize='14')
    ax.set_ylabel('# of wildfires', fontsize='12')
    ax.set_xticks(ticks=ticks_x)
    ax.set_xticklabels(months, fontsize='12')
    ax.set_yticks(ticks_y);

    st.pyplot(fig)


    