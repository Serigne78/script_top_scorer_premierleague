# Premier League Stats Scraper

Ce projet utilise BeautifulSoup, requests, pandas, et Twilio pour récupérer les statistiques actuelles des meilleurs buteurs de la Premier League et envoyer les résultats par message texte via Twilio.

## Objectif

L'objectif de ce projet est de fournir des informations actualisées sur les meilleurs buteurs de la Premier League, notamment le joueur, le club, la nationalité et le nombre de buts marqués.

## Configuration

Avant d'exécuter le script, assurez-vous d'avoir les bibliothèques Python nécessaires installées. Vous pouvez le faire en exécutant :

pip install beautifulsoup4 requests pandas twilio

Assurez-vous également d'avoir un compte Twilio et de remplir les informations d'authentification (`account_sid`, `auth_token`, `twilio_phone_number`, `your_phone_number`) dans le script.

## Utilisation

1. Exécutez le script `premierleague_stats_scraper.py`.
2. Les données seront extraites du site de la Premier League.
3. Un DataFrame Pandas sera créé avec les statistiques des meilleurs buteurs.
4. Les données seront envoyées par message texte via Twilio.

## Captures d'écran
![Capture d'écran de l'interface web](https://pbs.twimg.com/media/F_VB2AgXQAAUIb8?format=jpg&name=900x900)
## Auteur

- [Serigne Gueye]
