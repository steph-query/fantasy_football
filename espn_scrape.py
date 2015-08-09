from bs4 import BeautifulSoup
import pandas as pd
import requests
import pdb


urls = []

base_url = 'http://games.espn.go.com/ffl/tools/projections?'
url_ext = '&startIndex='
urls.append(base_url)
batches = [40, 80, 120, 160, 200, 240, 280, 320]

master_table = []
columns = ['name',
 'c/a',
 'pass_yards',
 'pass_tds',
 'pass_int',
 'rush_att',
 'rush_yards',
 'rush_tds',
 'receptions',
 'rec_yards',
 'rec_tds',
 'total_points']


for batch in batches:
  urls.append(base_url + url_ext + str(batch))

for url in urls:  
  r = requests.get(url)

  soup = BeautifulSoup(r.content)

  table1 = soup.find_all('tr', attrs={'class': 'pncPlayerRow playerTableBgRow0'})
  table2 = soup.find_all('tr', attrs={'class': 'pncPlayerRow playerTableBgRow1'})

  full_table = []
  for row in table1:
    full_table.append(row)
  for row in table2:
    full_table.append(row)

  stats_table = []

  for row in full_table:
    stat_line = []
    stat_line.append(row.find_all('td', attrs={'class': 'playertablePlayerName'})[0].text.split(',')[0])
    for stat in row.find_all('td', attrs={'class': 'playertableStat'}):
      stat_line.append(stat.text)
    stats_table.append(stat_line)

  for stat_line in stats_table:
    master_table.append(stat_line)

# pdb.set_trace()

stats_dataframe = pd.DataFrame(master_table, columns=columns)

stats_dataframe = stats_dataframe.drop('c/a', axis=1).drop('rush_att', axis=1).drop('total_points', axis=1)

stats_dataframe.to_csv('projected_stats.csv', index=False)




