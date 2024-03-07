# Scraping_HuggingFace

## Description

Le projet consiste à extraire les données du site web https://huggingface.co/models, stocker ces données dans une base de données MongoDB, et fournir une interface utilisateur interactive pour explorer ces données à l'aide de Dash.

## Structure du Projet

Le projet est organisé en trois dossiers principaux, ayant chacun son DockerFile correspondant au service qu'il peut délivrer, déployés dans des conteneurs Docker distincts :

- **MongoDB** : Contient les fichiers nécessaires pour construire l'image Docker de MongoDB, notre base de données.
- **Scrapy** : Contient les fichiers nécessaires pour construire l'image Docker de Scrapy, notre service de scraping.
- **Application** : Contient les fichiers nécessaires pour construire l'image Docker de l'application, notre application web.


## Utilisation

1. Clonez le dépôt sur votre machine locale :

   ```bash
   git clone https://github.com/Projet-ESIEE/Scraping_HuggingFace
   cd .\Scraping_HuggingFace
    ```
   
2. Lancez le projet avec la commande suivante :

   ```bash
   docker-compose up
   ```
3. Ouvrez votre navigateur et accédez à l'adresse suivante donnant sur l'application : http://localhost:8050

   
## Auteurs

- [**Benoit Marchadier**](https://github.com/bebe0106/) 

