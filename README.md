# dst-crypto-bot
<div align="center">
<h1 align="center">Projet Data Engineering Datascientest</h1>


<details>
  <summary>Sommaire</summary>
  <ol>
    <li>
      <a href="#overview">Overview</a>
      <ul>
        <li><a href="#tools">Tools</a></li>
      </ul>
    </li>
    <li>
      <a href="#commencer">Commencer</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

# Overview #
Dans le cadre de notre formation de Data Engineer avec DataScientest, nous avons comme projet de fin d'études de réaliser un Bot de trading de Cryptomonnaie.

### Tools


## Commencer

### Prerequisites

### Installation

1. Cloner le repo

   ```sh
   git clone git@github.com:tawounfouet/dst-crypto-bot.git
   ```

2. Copier le fichier contennant les variables d'environement

   ```sh
   cp env.example .env
   ```

3. Lancer `docker-compose`

   ```sh
   docker-compose -f docker-compose.yml --profile dev up
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Usage

### Architecture des composants


├── requirements.txt <----- Fichier contennant les librairies python à installer
├── env.example <----------------- Fichier contennant les variables d'environement.