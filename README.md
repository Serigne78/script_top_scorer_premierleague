# Premier League Stats Scraper

Ce projet utilise BeautifulSoup, requests, pandas, et Twilio pour récupérer les statistiques actuelles des meilleurs buteurs de la Premier League et envoyer les résultats par message texte via Twilio.

## Objectif

L'objectif de ce projet est de fournir des informations actualisées sur les meilleurs buteurs de la Premier League, notamment le joueur, le club, la nationalité et le nombre de buts marqués.

## Configuration

Avant d'exécuter le script, assurez-vous d'avoir les bibliothèques Python nécessaires installées. Vous pouvez le faire en exécutant :

```bash
pip install beautifulsoup4 requests pandas twilio

Assurez-vous également d'avoir un compte Twilio et de remplir les informations d'authentification (`account_sid`, `auth_token`, `twilio_phone_number`, `your_phone_number`) dans le script.

## Utilisation

1. Exécutez le script `premierleague_stats_scraper.py`.
2. Les données seront extraites du site de la Premier League.
3. Un DataFrame Pandas sera créé avec les statistiques des meilleurs buteurs.
4. Les données seront envoyées par message texte via Twilio.

![Capture d'écran de l'interface web](https://ci3.googleusercontent.com/mail-img-att/AM67uINKIVQwq34hwVQNnHB8zeTtgB7VPlWJchiSrX0CX6Sn5vSBwMT3HiOpH_N-xxmISTQrKaYi09mfUxby6qSHcRDPrUEHYMb5L3BEu25cqAOeb2iDqUv5wHuHHMGoleOmZ7QjoBFRxIRJoxbl3LKQhtjbKeSFtMR3c9_PF7IwKPPivZQ25fsw3stxJ5mkogkRj1oFb9LuG7KJq3ZWMphuuy9wIdOvpPv8gZdVruU2K9PG-O8BuFajTFxnYZLeLXG3jRnVGsiV8qQXp7Q32fwd5OKKUGJjPRP5erG0mHRPD7wrNdr5QRpxGlbpP9hlRd4Td9e2a45Yvp6C8Nn3b539BuWeNACBi3aKjD5ro0IQDbJlLAcmdYDvSz2HiCZqLbjVAX6YoYshGb5fjuSuYGd7AfhWngLghqPo9bP4ArHhRpKkh3JaKaPxVSb3-fWYV-RjV5Yf5tkhlbc0MA0a6b1MgbaoMtYrNpL4uKGQ14Et_G6fjt8UkD2AJUt-pBcctjiaLOwPODGlO6xZW2FsANTMqAtt3C-EXa-5NLk-zaiIMTnis4q0lTCs9kK-GU4uEXBPNRuKNgTggNcIeuKOCppu_7COUmEtjNRZ1P9m5OIWXOmcusRfyf3jOoA04NuxrCnCs0vJFUhYpUGIC0lo5n_r9m25OisDdccTG31GGF2cHxF0VCuCrFBKNdw1sVwoTXX3_WKsM_NQETBJzGQp0pTLAnNQvu7URgwz19Z5bCAsoYAa2yzgd4gUW8AjznDbSwUrXlw5PIMBWJ7OQdW0-VgQNP_S_LDSwJ5TNQt_q0JkoMMPpqUS-GJU4a2oMORCYbSfjCS2vrAtLQwlN94SI_Ln4xsJYXPCCxrMgcWbUkl497wQ08r_aHMzbN89IJIlMfgpEMKeRWjAtmiW-ep9AiVxvFkbTkw2QibINs2mvjS6Z83z738Tv-5OQo2ULjBzXfsZXIVdspfXUJzjG3UCpu8cbYcLygxK-bHkxLCXi41J0bh9gG4NmouL1aaouGqJ5VQ1HyV27OvCCk22Xu3kKRg=s0-l75-ft)
## Auteur

- [Votre Nom]
