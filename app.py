import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
import plotly.graph_objs as go

from textwrap import dedent
from pyarrow import feather
import numpy as np
import pandas as pd
import sys
sys.path.append('./src/python')

import sd_data
import sd_plot

app = dash.Dash()
app.config.supress_callback_exceptions=True

data = sd_data.file_connector("data/aeolus_top5drugs.feather")
uniq_drugs = data.unique_values("drug_concept_name")
all_drugs = data.counts_by_feature("age_cat")

##########

app.layout = html.Div(

	children=[

		dcc.Location(id='url', refresh=True),
		html.Div(id='page-content')
		]
	)	
	
	
index_page = html.Div(
	children=[

		html.H1('Visualizing Drug Safety Data in a Web Framework: Interacting with, understanding, and communicating using Python',
			style={'text-align' : 'center','font-size' : 48}
			),

		dcc.Link('Go to ADR age relation Page', href='/age_page',
			style={'font-size' : 16,'color' : 'blue'}),

		html.Br(),

		dcc.Link('Investigate Drugs',
			href = '/feature_drugs_page',
			style={'font-size' : 16,'color' : 'blue'}),

		html.Br(),

		dcc.Link('Investigate Adverse Reactions',
			href = '/feature_outcomes_page',
			style={'font-size' : 16,'color' : 'blue'}),

		html.Br(),

		dcc.Link('Investigate ADRs',
			href = '/feature_drugs_and_outcomes_page',
			style={'font-size' : 16,'color' : 'blue'}),

		html.Br(),

		html.Hr(),

		html.H4("The Food and Drug Administration's Adverse Event Reporting System provides population-level information on drug usage and adverse reactions to drugs (ADRs). We present a standardized, processed version of this ADR data for the public."),

		html.Br(),

		html.H4("Feel free to use the Jupyter notebooks in our github repository SafeDrugs (www.github/NCBI-Hackathons/SafeDrugs) for the data wrangling and code implementation."),

		html.Br(),

		html.H4("Check out the individual fveature links to investigate frequent drugs, adverse reactions, and ADRs. Post issues on our github SafeDrugs (www.github/NCBI-Hackathons/SafeDrugs) for additional features or bugs."),

		html.Br()
		]
	)

feature_drugs_page = html.Div(

	children=[

		html.H1('Investigating Drug usage \nin ADR data',
			style={'text-align' : 'center'}),

		dcc.Link('Go to Home Page', href='/',
			style={'font-size' : 16,'color' : 'blue'}),

		html.Br(),

		dcc.Link('Investigate Adverse Reactions',
			href = '/feature_outcomes_page',
			style={'font-size' : 16,'color' : 'blue'}),

		html.Br(),

		dcc.Link('Investigate ADRs',
			href = '/feature_drugs_and_outcomes_page',
			style={'font-size' : 16,'color' : 'blue'}),

		html.Br(),

		html.Hr(),

		html.Div(
			className='col-md-6',
			style={'text-align' : 'center'},
			children=[

				html.H2('Drug Class'),

				html.H4('The Anatomical Thearapeutic Classification (ATC) is a standard vocabulary that categorizes drugs within domains such as organ system, mechanism of action, etc. Please choose the ATC class of drugs you want to view.')

			]),

		html.Div(
			className='col-md-6',
			style={'text-align' : 'center'},
			children=[

				html.H2('How many reports?'),

				dcc.Graph(id='drug-class-num-reports')

			]),

		html.Div(
			className='col-md-6',
			style={'text-align' : 'center'},
			children=[

				html.H2('Frequency across years of reporting'),

				html.H4('Reports of ADRs were given in different years, where reporting may be more or less frequent for random reasons, or because of popular events such as news and drug releases.')

			]),

		html.Div(
			className='col-md-6',
			style={'text-align' : 'center'},
			children=[

				dcc.Graph(id='drug-class-num-reports-across-report-years')

			]),

		html.Div(
			className='col-md-6',
			style={'text-align' : 'center'},
			children=[

				html.H2('Breakdown of reporting based on sex'),

				html.H4('Reporting of ADRs can be by males or females, which can vary in reporting behavior as well as have different predisposition to drug use.')

			]),

		html.Div(
			className='col-md-6',
			style={'text-align' : 'center'},
			children=[

				dcc.Graph(id='drug-class-num-reports-across-report-years-by-sex')

			]),

		html.Div(
			className='col-md-6',
			style={'text-align' : 'center'},
			children=[

				html.H2('Breakdown of reporting based on sex and age'),

				html.H4('Reporting of ADRs can be by males or females, as well as at different ages. Patient demographics can influence reporting as well as predisposition to drug use.')

			]),

		html.Div(
			className='col-md-6',
			style={'text-align' : 'center'},
			children=[

				dcc.Graph(id='drug-class-num-reports-across-report-years-by-sex-and-age')

			])
		
		]
	),

feature_outcomes_page = html.Div(

	children=[

		html.H1('Investigating Adverse Reactions from drug usage \nin ADR data',
			style={'text-align' : 'center'}),
		
		dcc.Link('Go to Home Page', href='/',
			style={'font-size' : 16,'color' : 'blue'}),

		html.Br(),

		dcc.Link('Investigate Drugs',
			href = '/feature_drugs_page',
			style={'font-size' : 16,'color' : 'blue'}),

		html.Br(),

		dcc.Link('Investigate ADRs',
			href = '/feature_drugs_and_outcomes_page',
			style={'font-size' : 16,'color' : 'blue'}),

		html.Br(),

		html.Hr(),

		html.Div(
			className='col-md-6',
			style={'text-align' : 'center'},
			children=[

				html.H2('Number of Adverse Reactions'),

				html.H4('Patients may report one or many adverse reactions to a drug, which can either be causal or anecdotal (i.e caused by many factors) as well as reported more frequently than others. Choose how many adverse reactions you want to view.')

			]),

		html.Div(
			className='col-md-6',
			style={'text-align' : 'center'},
			children=[

				html.H2('How many reports?'),

				dcc.Graph(id='outcomes-num-reports')

			]),

		html.Div(
			className='col-md-6',
			style={'text-align' : 'center'},
			children=[

				html.H2('Frequency across years of reporting'),

				html.H4('Reports of ADRs were given in different years, where reporting may be more or less frequent for random reasons, or because of popular events such as news and drug releases.')

			]),

		html.Div(
			className='col-md-6',
			style={'text-align' : 'center'},
			children=[

				dcc.Graph(id='outcomes-num-reports-across-report-years')

			]),

		html.Div(
			className='col-md-6',
			style={'text-align' : 'center'},
			children=[

				html.H2('Breakdown of reporting based on sex'),

				html.H4('Reporting of ADRs can be by males or females, which can vary in reporting behavior as well as have different predisposition to drug use.')

			]),

		html.Div(
			className='col-md-6',
			style={'text-align' : 'center'},
			children=[

				dcc.Graph(id='outcomes-num-reports-across-report-years-by-sex')

			]),

		html.Div(
			className='col-md-6',
			style={'text-align' : 'center'},
			children=[

				html.H2('Breakdown of reporting based on sex and age'),

				html.H4('Reporting of ADRs can be by males or females, as well as at different ages. Patient demographics can influence reporting as well as predisposition to drug use.')

			]),

		html.Div(
			className='col-md-6',
			style={'text-align' : 'center'},
			children=[

				dcc.Graph(id='outcomes-num-reports-across-report-years-by-sex-and-age')

			])
		]
	),

feature_drugs_and_outcomes_page = html.Div(

	children=[

		html.H1('Investigating ADRs',
			style={'text-align' : 'center'}),
		
		dcc.Link('Go to Home Page', href='/',
			style={'font-size' : 16,'color' : 'blue'}),

		html.Br(),

		dcc.Link('Investigate Drugs',
			href = '/feature_drugs_page',
			style={'font-size' : 16,'color' : 'blue'}),

		html.Br(),

		dcc.Link('Investigate Adverse Reactions',
			href = '/feature_outcomes_page',
			style={'font-size' : 16,'color' : 'blue'}),

		html.Br(),

		html.Hr(),

		html.Div(
			className='col-md-6',
			style={'text-align' : 'center'},
			children=[

				html.H2('Adverse drug reactions'),

				html.H4('ADRs that are reported may be more or less frequent in the population. Choose the number of ADRs you would like to view, with the top being the most frequent ADR in the dataset.')

			]),

		html.Div(
			className='col-md-6',
			style={'text-align' : 'center'},
			children=[

				html.H2('How many reports?'),

				dcc.Graph(id='adr-num-reports')

			]),

		html.Div(
			className='col-md-6',
			style={'text-align' : 'center'},
			children=[

				html.H2('Frequency across years of reporting'),

				html.H4('Reports of ADRs were given in different years, where reporting may be more or less frequent for random reasons, or because of popular events such as news and drug releases.')

			]),

		html.Div(
			className='col-md-6',
			style={'text-align' : 'center'},
			children=[

				dcc.Graph(id='adr-num-reports-across-report-years')

			]),

		html.Div(
			className='col-md-6',
			style={'text-align' : 'center'},
			children=[

				html.H2('Breakdown of reporting based on sex'),

				html.H4('Reporting of ADRs can be by males or females, which can vary in reporting behavior as well as have different predisposition to drug use.')

			]),

		html.Div(
			className='col-md-6',
			style={'text-align' : 'center'},
			children=[

				dcc.Graph(id='adr-num-reports-across-report-years-by-sex')

			]),

		html.Div(
			className='col-md-6',
			style={'text-align' : 'center'},
			children=[

				html.H2('Breakdown of reporting based on sex and age'),

				html.H4('Reporting of ADRs can be by males or females, as well as at different ages. Patient demographics can influence reporting as well as predisposition to drug use.')

			]),

		html.Div(
			className='col-md-6',
			style={'text-align' : 'center'},
			children=[

				dcc.Graph(id='adr-num-reports-across-report-years-by-sex-and-age')

			])
		]
	),

age_page = html.Div(

	children=[

		html.H1('ADR age relation'),

		dcc.Link('Go to Home Page', href='/',
			style={'font-size' : 16,'color' : 'blue'}),

		html.Br(),

		dcc.Link('Go to ADR table Page', href='/table_page',
			style={'font-size' : 16,'color' : 'blue'}),

		html.Hr(),

		html.Div(
			style={'class' : "col-sm-4",'border' : '2px solid black',
			'float' : 'left'},
			children=[
			
			html.H1('How many patients are taking these drugs?',
				style={'text-align' : 'center','font-size' : 18}),
			
			dcc.Dropdown(
				id='drug_count',
				options=[{'label' : i, 'value' : i} for i in uniq_drugs],
				value=uniq_drugs[0]),

			html.Div(id='drug_output',
				style={'text-align' : 'center'})

			]),

		dcc.Graph(
			id='drug-reports-at-ages',
			style={'class' : 'col-sm-4','float' : 'right'},
		)

		]
	)


# Update the index
# This callback constantly looks at the page location with id="url",
# and gives the pathname to the function immediately following the callback.
# The function then gives what it returns, which is a new layout.
# That new layout itself has a url! So the new url is displayed
# Every time we click the link, the pathname changes (href) and we get returned the 
# corresponding page. 
@app.callback(
	dash.dependencies.Output('page-content', 'children'),
			  [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
	if pathname == '/age_page':
		return age_page
	if pathname == '/feature_drugs_page':
		return feature_drugs_page
	if pathname == '/feature_outcomes_page':
		return feature_outcomes_page
	if pathname == '/feature_drugs_and_outcomes_page':
		return feature_drugs_and_outcomes_page
	else:
		return index_page


#Show number of patients taking selected drug in dataset
@app.callback(
	dash.dependencies.Output('drug_output', 'children'),
	[dash.dependencies.Input('drug_count', 'value')])
def callback_drug(value):
	return 'There are {} patients that reported taking {}'.format(
		data.count('drug_concept_name=="' + value + '"'),
		value)

#Update bar graph for drug
@app.callback(
	dash.dependencies.Output('drug-reports-at-ages','figure'),
	[dash.dependencies.Input('drug_count','value')])
def callback_drug_reports_at_ages_bars(value):
        title = 'Patients taking {} at different age intervals'.format(value)
        x_legend = "Age category"
        y_legend = "Percentage of reports"
        this_drug_title = '{}'.format(value)
        all_drugs_title = "All drugs"
        this_drug = data.counts_by_feature("age_cat", 'drug_concept_name == "' + value + '"')
        return sd_plot.bar_plot(title, x_legend, y_legend, this_drug, all_drugs, this_drug_title, all_drugs_title)

        
#enable bootstrap styling
external_css = [
					["https://bootswatch.com/3/paper/bootstrap.css"],
					["docs/custom.css"]
				]

for css in external_css:
	app.css.append_css({"external_url": css})


if __name__ == '__main__':
	app.run_server(debug=True)
