import requests
from bs4 import BeautifulSoup
import pandas as pd

def nba_teams_preseason_stats ():
    url = 'https://basketball.realgm.com/nba/team-stats/2025/Averages/Team_Totals/Preseason?pace_adjustment='
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    # This code find the table in the provided URL
    table = soup.find('table', class_ = 'tablesaw')

    # This code extract all the header/category in the table (Keywords, HTML elements are removed)
    headers = [header.text.strip() for header in table.find_all('th')] 

    df = pd.DataFrame(columns = headers)

    # This code finds all the 'tr' element or row in the URL (Not organized, HTML elements are included)
    rows = table.find_all('tr')

    for row in rows[1:]:
        
        # This code finds all the 'td' element or data in the 'tr' element or row
        cols = row.find_all('td')

        # This code extract all the data in the row (Keywords, HTML elements are removed)
        data = [col.text.strip() for col in cols]
        df.loc[len(df)] = data

    return df
