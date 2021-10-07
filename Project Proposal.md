Question/need:
- What is the framing question of your analysis, or the purpose of the model/system you plan to build?
  - In recent years, California has experienced increasingly large and destructive wildfires. CAL FIRE, a state-based agency, maintains a website that lists all active wildfires, as well as a database of past incidents. However, this website can be difficult to navigate. The aim of this project is to create a user friendly dashboard with two parts:
    - Part 1: An automatically updated listing of all active wildfires in the state of California, along with a link to each fire’s incident page (which provides crucial emergency information like evacuation orders and road closures)
    - Part 2: Historical data about past wildfires in the state (2013 to present). This would take the form of visually appealing charts summarizing the major causes of wildfires, the counties most affected, and the degree of destruction - and how these trends have changed over time. It would also include a search function allowing users to search by county and year.

- Who benefits from exploring this question or building this model/system?
  - Part 1, the listing of active wildfires, would benefit citizens affected by the wildfires, family and friends watching from afar, and the media
  - Part 2, historical wildfire data, would provide insight into patterns and trends of wildfires in the state. This could help elected officials and government agencies make decisions about wildfire prevention and management. It could also inform citizens’ decisions about where they chose to live and the extent to which they prepare for wildfires.

Data Description:
- What dataset(s) do you plan to use, and how will you obtain the data?
	- I plan to scrape the CALFIRE website (fire.ca.gov). This site contains information about active wildfires in the state of California, as well as a database of past incidents dating back to 2013. For some of the active wildfires, I may also need to scrape the linked site (individual pages at inciweb.nwcg.gov) to obtain basic data about the fire 

- What is an individual sample/unit of analysis in this project? What characteristics/features do you expect to work with?
  - Each wildfire is an individual unit of analysis. There are currently 11 active wildfires. The historical database contains 2090 wildfires over a span of 9 years (2013-2021) 
  -  For the active wildfires, I plan to scrape from CAL FIRE website:
      - Fire Name
      - Date Started
      - Last Updated
      - Counties
      - Acres (if available)
      - % Containment (if available)
      - Cause
      - Lat/Long
      - External Incident Link (links to a page on inciweb.nwcg.gov)
      - Note: If acres and % containment are not listed on CAL FIRE website, I would need to scrape the linked page on inciweb.nwcg.gov
  - For the historical wildfires (2013 to present), I plan to scrape from CAL FIRE website:
    - Fire Name
    - Date Started
    - Date Contained
    - Counties
    - Acres
    - % Containment (should be 100%)
    - Cause
    - Lat/Long
    - Damages and Losses (if available):
      - Structures Damaged
      - Structures Destroyed
      - Injuries
      - Fatalities
- If modeling, what will you predict as your target? 
	- No modeling this time!

Tools:
- How do you intend to meet the tools requirement of the project?
	- After obtaining data via web scraping, I will load the data into a NoSQL database (MongoDB). I will use tools we learn in class to create a dashboard with auto-update capabilities. 
- Are you planning in advance to need or use additional tools beyond those required? 
	- I plan to use Selenium and Beautiful Soup for web scraping
	- I may use Tableau in order to highlight counties and/or plot longitude/latitude on a map

MVP Goal:
- What would a minimum viable product (MVP) look like for this project?
  - A very basic dashboard
