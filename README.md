# World Bank Data - Web App
Heroku free plan was discontinued. Web app to be migrated to another hosting platform.

_Find the web app: https://worldbankdata-fertility-app.herokuapp.com/_

## Table of Contents
1. [Installation](#installation)
2. [Objective](#objective)
3. [File Descriptions](#file-descriptions)
4. [Licensing, Authors, Acknowledgements](#licensing-authors-acknowledgements)

## Installation
The code was developed using Python 3.7.9 on Windows 10. Necessary packages beyond the Python Standard Library are:

- Flask=1.1.2
- gunicorn=20.0.4
- pandas=1.1.5
- plotly=4.14.1
- requests=2.25.1

The environment can be installed using [requirements.txt](https://github.com/MareikeHeller/worldbankdata-web-app/blob/main/requirements.txt).

## Objective

This web app displays a data dashboard on fertility rates as births per woman in selected European countries.
Data is loaded from the [World Bank APIs](https://datahelpdesk.worldbank.org/knowledgebase/articles/889386-developer-information-overview)
and prepared (pandas) for visualization (plotly). The application is created using Flask and was deployed on Heroku.

Heroku free plan was discontinued. Web app to be migrated to another hosting platform.

_You can access the app here: https://worldbankdata-fertility-app.herokuapp.com/_

## File Descriptions
The **folder** [wrangling_scripts](https://github.com/MareikeHeller/worldbankdata-web-app/tree/main/wrangling_scripts) contains the file [wrangle_data.py](https://github.com/MareikeHeller/worldbankdata-web-app/blob/main/wrangling_scripts/wrangle_data.py) that
(a.) loads data from the World Bank APIs,
(b.) provides data wrangling for visualization purposes and
(c.) returns the plotly figures (data+layout). 

- a. function load_api_data
- b. function cleandata
- c. function return_figures

The **folder** [worldbank_fertility_app](https://github.com/MareikeHeller/worldbankdata-web-app/tree/main/worldbank_fertility_app) contains the [web template (index.html)](https://github.com/MareikeHeller/worldbankdata-web-app/blob/main/worldbank_fertility_app/templates/index.html), [images](https://github.com/MareikeHeller/worldbankdata-web-app/tree/main/worldbank_fertility_app/static/img) and [integration of plotly figures (routes.py)](https://github.com/MareikeHeller/worldbankdata-web-app/blob/main/worldbank_fertility_app/routes.py).

The file [requirements.txt](https://github.com/MareikeHeller/worldbankdata-web-app/blob/main/requirements.txt) is used to install the python environment.

The [Procfile](https://github.com/MareikeHeller/worldbankdata-web-app/blob/main/Procfile) is used for deployment with Heroku.

## Licensing, Authors, Acknowledgements
This web app was developed during an exercise related to the [Udacity Data Science Nanodegree](https://www.udacity.com/course/data-scientist-nanodegree--nd025).

The data used in this project is publicly available on [data.worldbank.org](https://data.worldbank.org/) (Creative Commons Attribution 4.0 International License).
