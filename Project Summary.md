Abstract

The aim of this project is to engineer a data pipeline to create a user-friendly dashboard of wildfires in the state of California from 2013-2020. I obtained my data by web scraping the CalFire site. This yielded a total of 1891 fires over the 8 year period. The data demonstrate that California’s fires are increasing in size and number. It also shows that 2018 was particularly destructive and deadly as a result of a single fire.

Design 

The aim of this project is to engineer a data pipeline to create a user-friendly dashboard of wildfires in the state of California from 2013-2020. Data was stored in a SQL database and imported into python pandas.

Data  
Data was obtained by scraping the CALFIRE website (fire.ca.gov). This yielded a total of 1891 fires over the 8 year period.

Algorithms 

I stored the data in a SQLite database through use of SQLAlchemy. There were several back and forths between the SQL database (used for storage) and pandas dataframes (used for cleaning and aggregation). In order to create the web app, multiple SQL tables were accessed from within a streamlit script.  


Tools

I scraped the web using selenium and beautiful soup. I used streamit for web app creation.

Communication

Looking forward to the presentation!
