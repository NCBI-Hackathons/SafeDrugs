<img src="logo/logo.png"></img>

A framework for interacting with drug safety data

## Goal

- Using a standardized dataset of adverse drug reactions from the FDA (AEOLUS, see resources for link to paper), provide a web app for interacting and visualizing with this unique data source. 

## Packages required for running app

pip install:

dash==0.22.0
dash_core_components==0.26.0
dash_html_components==0.11.0
dash_table_experiments==0.6.0
plotly==3.1.0
Markdown==2.6.11
pyarrow==0.9.0
numpy==1.13.3
pandas==0.23.0

## Some Background

- See introduction in app

- There has been a lot of development by the FDA in providing tools and apps using their API to query their ADR data. 

- As is, the FDA data is not standardized and so contains redundancy and ambiguity in their data (e.g. aspirin and aspirin 81mg). Using a standardized version of their data can provide additional clarity representing ADR data. Our app would be another community tool to possibly add to their online portfolio (see OpenFDA community tools). 

## Possible tasks

- Outline and execute approaches for analyzing AEOLUS data. Make sure they are informative, concise, and can be somewhat unique to what has already been provided (use demographic information?). 

- How to host app? How to host data (it's 6.36 GBs)? 

- Will the FDA accept this app as a tool? If yes, how?

- Design the app. What is the best look and feel for the app? We can style using CSS.

- Can we query the data without having to load everything into memory? Need to make loading the app and transitioning within/between features seamless.

- Provide commenting/documenting of code. Need to explain how we are using Dash API. 

- Docker-ize so that individuals can download the app and data and spin up on their local machine without needing to download libraries. 

## Resources

Plotly/dash github repository

- https://github.com/plotly/dash

Dash User Guide

- https://dash.plot.ly/

OpenFDA

- https://open.fda.gov/

OpenFDA contact for submitting tool

- open@fda.hhs.gov

OpenFDA tools (using API)

- https://open.fda.gov/tools/

OpenFDA Community Apps

- https://open.fda.gov/community/

AEOLUS paper

- https://www.nature.com/articles/sdata201626

Unified Medical Language System Quick Start Guide

- https://www.nlm.nih.gov/research/umls/quickstart.html
