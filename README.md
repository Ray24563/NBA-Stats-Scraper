
# NBA Stats Scraper

A stats scraper designed to gather and analyze preseason team performance data, with an intuitive interface for easy access to insights and statistics.


## Features

- Web scraping of NBA stats with Beautiful Soup.
- GUI interface using Tkinter.
- Statistical analysis with visualizations (Bar Plot).
- Switchable sections with disappearing text widget.
- Can save the data in Excel.


## Tech Stack


**Programming Language:** Python

**Libraries Used:** 
- **Beautiful Soup** - For web scraping
- **Pandas** - For data manipulation and analysis
- **Tkinter** - For creating the GUI
- **Matplotlib/Seaborn** - For data visualization

**EXE Conversion Tool:** PyInstaller


## Installation

For windows: Kindly click and install the **NBAStats.Scraper_WINDOWS_v1.0.0_setup.exe**

- When newly installed, there will be a warning message that tells you that **Running this app might put your PC at risk.** This is because the publisher is unknown. We assure you that the application is **COMPLETELY SAFE**

- After pressing **Run Anyway** it will direct you to the setup show the terms and policy and the location/path where you want to install the app.

- After configuration, you can freely explore the app.
    
## File Structure

When you install the application, the code will be included as well. It is organized into three separate files to improve clarity and structure. Here’s a brief overview of each file:

- **web_scrape.py** - This file handles the web scraping process. After collecting the data from the website, we store it in a Pandas structure called a DataFrame.

- **analysis.py** -  This file is where we perform data manipulation, such as generating new statistics based on NBA formulas and predicting the top offensive and defensive team.

- **gui.py** -  This file is responsible for creating the GUI.
## Usage

The NBA Stats Scraper displays the stats of NBA Teams in 2024-2025 NBA Pre-Season. It also has a prediction of top offensive and defensive stats for the upcoming 2024-2025 NBA Season. Here is the brief overview of the application:

    1. Home - In homepage, it has 5 buttons and will direct you 
    at its specific location

    2. Scraped Data - when you click the scraped data button, it
    will direct you to the data we scraped from the website.
    In addition, you can save the data as xlsx (Excel).

    3. About - In this section will give you a brief overview of
    the project and its developers

    4. Offensive Ratings - In this section is where you will see
    our prediction for top offensive teams for the upcoming 
    season. It also has a bar plot to visualize the data.
    In addition, you can save the top offensive team data as xlsx
    file (Excel).

    5. Defensive Ratings - In this section is where you will see
    our prediction for top defensive teams for the upcoming 
    season. It also has a bar plot to visualize the data.
    In addition, you can save the top defensive team data as xlsx
    file (Excel).

    6. Save Overall Data - Clicking this will save the Overall
    data (Scraped Data, Top Offensive Teams and Top Defensive
    Teams) as xlsx (Excel).


## Support

Thank you for trying out my application! I welcome any feedback that could help me improve my programming skills. Please feel free to reach out using the contact information provided.

**Email:** charlespalatino@gmail.com

**Github:** Ray24563
