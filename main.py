from bs4 import BeautifulSoup
import requests
import pandas as pd
from twilio.rest import Client

url = "https://www.premierleague.com/stats/top/players/goals?se=-1"
response = requests.get(url)
content = response.text

# Vos informations d'authentification Twilio
account_sid = 'xxxxxxx'
auth_token = 'xxxxxxx'
# Votre numéro Twilio et votre numéro de téléphone
twilio_phone_number = 'xxxxxxxxx'
your_phone_number = '+xxxxxxxxx'


client = Client(account_sid, auth_token)
soup = BeautifulSoup(content, "html.parser")


def stats_table_rank():
      liste = []
      stats_table = soup.find_all(name="td", class_="stats-table__rank")
      for stats in stats_table:
            liste.append(stats.getText())
      return liste

def stats_table_player():
      liste = []
      stats_table = soup.find_all(name="a", class_="playerName")
      for stats in stats_table:
            liste.append(stats.getText().strip())
      return liste

def stats_table_team():
      liste = []
      stats_table = soup.find_all(name="a", class_="stats-table__cell-icon-align")
      for stats in stats_table:
            liste.append(stats.getText().strip())
      return liste

def stats_table_country():
      liste = []
      stats_table = soup.find_all(name="div", class_="stats-table__cell-icon-align")
      for stats in stats_table:
            liste.append(stats.getText().strip())
      return liste


def stats_table_goal():
      liste = []
      stats_table = soup.find_all(name="td", class_="stats-table__main-stat")
      for stats in stats_table:
            liste.append(stats.getText().strip())
      return liste


data = {
    'Player': stats_table_player(),
    'Club': stats_table_team(),
    'Nationality': stats_table_country(),
    'Stat':stats_table_goal()
}

df = pd.DataFrame(data)

# Modifier l'index pour commencer à 1
df.index = stats_table_rank()

print(df)

# Créez une chaîne de caractères formatée à partir du DataFrame
   # Envoyer un message avec le nombre de buts marqués
message = client.messages.create(
from_=twilio_phone_number,
body=f'{df}',
to=your_phone_number
)


print(f"Message envoyé : {message.sid}")

