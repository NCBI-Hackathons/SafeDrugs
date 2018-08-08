<img src="logo/logo.png"></img>

## <p align="center"> A framework for interacting with drug safety data </p> 

### Table of contents
* [Goal](#goal)
* [Installation](#installation)
* [Introduction](#introduction)
* [Use Cases](#use-cases)
* [Resources](#resources)

### Goal <a name="goal"></a>

- Using a standardized dataset of adverse drug reactions from the FDA (AEOLUS, see resources for link to paper), provide a web app as well as a set of Jupyter notebooks for interacting and visualizing with this unique data source. 

### Installation <a name="installation"></a>

```
git clone git@github.com:NCBI-Hackathons/SafeDrugs.git 
cd path-to-SafeDrug-directory 
pip install -r requirements.txt
```
- The app is run by python 3. If you don't have it, please install python 3 first. You can find out how to install it [here](https://www.python.org/downloads/).

### Introduction <a name="introduction"></a>

- Drugs are commonly used in the population. Often, people experience adverse reactions to these drugs (ADRs). It is important for the public to view and understand ADRs.

- The Food and Drug Administration (FDA) has collected reports of ADRs in the US population over several decades, and this data is publicly available. There has been a lot of development by the FDA and others in providing tools and apps to view and communicate their ADR data. 

- As is, the FDA data is not standardized and so contains redundancy and ambiguity in their data (e.g. aspirin and aspirin 81mg). Using a standardized version of their data, called AEOLUS, we provide additional clarity representing and communicating ADR data. Our app and Jupyter notebooks is available to the public to ad to the online portfolio for communicating adverse drug reactions in the population (see OpenFDA community tools). 

- See the manuscript and app for more information.

### Use cases <a name="use-cases"></a>

<i>SafeDrugs</i> communicates standardized ADR data through two interfaces: a set of interactive Jupyter notebooks and a Dash web app.

To interact with the data in the Jupyter notebooks, follow the installation procedure, and view the feature notebooks:=. For example, to view drug information execute:

```
jupyter notebook feature_drugs.ipynb
```

To view adverse reaction information, execute:

```
jupyter notebook feature_outcomes.ipynb
```

To view ADR information, execute:

```
jupyter notebook feature_drugs_and_outcomes.ipynb
```

You may run the code chunks sequentially in the notebooks to regenerate the plots, as well as choose options in the embedded widgets to modify what's plotted.

To run the Dash web app, execute:

```
python app.py
```

The packages in requirements.txt are required for the app to spin up a local instance, so please execute the installation procedure first.

You may then view the descriptions and dataset directly without changing code, while still defining options to modify the data to be viewed.

Any issues in running the notebooks or apps, as well as wanting to modify or add features, please start an issue to the repository. Thank you, and enjoy! 

### Resources <a name="resources"></a>

Plotly/dash github repository

- https://github.com/plotly/dash

Dash User Guide

- https://dash.plot.ly/

OpenFDA

- https://open.fda.gov/

OpenFDA tools (using API)

- https://open.fda.gov/tools/

OpenFDA Community Apps

- https://open.fda.gov/community/

AEOLUS paper

- https://www.nature.com/articles/sdata201626

Unified Medical Language System Quick Start Guide

- https://www.nlm.nih.gov/research/umls/quickstart.html
