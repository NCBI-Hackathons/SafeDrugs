import dash
import dash_core_components as dcc
import dash_html_components as html
from src.python import sd_data, sd_plot

app = dash.Dash()
app.config.supress_callback_exceptions = True

data = sd_data.file_connector("data/aeolus_top5drugs.feather")

uniq_drugs = data.unique_values("drug_concept_name")
uniq_drugs_list = []
for d in uniq_drugs:
    tmp = {'label': d, 'value': d}
    uniq_drugs_list.append(tmp)

drug_classes = [col for col in data.data.columns if 'atc' in col]
drug_classes.append('atc_5th')
drug_classes_list = []
for d in drug_classes:
    tmp = {'label': d, 'value': d}
    if d == 'atc_5th':
        tmp = {'label': d, 'value': 'drug_concept_name'}
    drug_classes_list.append(tmp)

drugs_in_drug_classes = {}
for i in range(len(drug_classes_list)):
    col = drug_classes_list[i]['value']
    drugs_in_drug_classes[col] = data.data[col].unique()

all_drugs = data.counts_by_feature("age_cat")

app.layout = html.Div(children=[
    dcc.Location(id='url', refresh=True),
    html.Div(id='page-content')
])

index_page = html.Div(children=[
    html.H1(
        'Visualizing Drug Safety Data in a Web Framework: Interacting with, understanding, and communicating using Python',
        className='text-center'),
    html.Div(children=[
        dcc.Link(
        'Go to ADR-age relation Page',
        href='/age_page',
        style={
            'font-size': 16,
            'color': 'blue'
        }),
        html.Br(),
        dcc.Link(
            'Investigate Drugs',
            href='/feature_drugs_page',
            style={
                'font-size': 16,
                'color': 'blue'
            }),
        html.Br(),
        dcc.Link(
            'Investigate Adverse Reactions',
            href='/feature_outcomes_page',
            style={
                'font-size': 16,
                'color': 'blue'
            }),
        html.Br(),
        dcc.Link(
            'Investigate ADRs',
            href='/feature_drugs_and_outcomes_page',
            style={
                'font-size': 16,
                'color': 'blue'
            }),
        html.Br()
    ], className='text-center'),
    html.Hr(),
    html.Div([
        html.P("The Food and Drug Administration's Adverse Event Reporting System provides population-level information on drug usage and adverse reactions to drugs (ADRs). We present a standardized, processed version of this ADR data for the public."),
        html.P("Feel free to use the Jupyter notebooks in our github repository SafeDrugs (www.github/NCBI-Hackathons/SafeDrugs) for the data wrangling and code implementation."),
        html.P("Check out the individual fveature links to investigate frequent drugs, adverse reactions, and ADRs. Post issues on our github SafeDrugs (www.github/NCBI-Hackathons/SafeDrugs) for additional features or bugs.")
    ])
], className='container')

feature_drugs_page = html.Div(children=[
    html.H1(
        'Investigating Drug usage \nin ADR data',
        style={'text-align': 'center'}),
    dcc.Link(
        'Go to Home Page', href='/', style={
            'font-size': 16,
            'color': 'blue'
        }),
    html.Br(),
    dcc.Link(
        'Investigate Adverse Reactions',
        href='/feature_outcomes_page',
        style={
            'font-size': 16,
            'color': 'blue'
        }),
    html.Br(),
    dcc.Link(
        'Investigate ADRs',
        href='/feature_drugs_and_outcomes_page',
        style={
            'font-size': 16,
            'color': 'blue'
        }),
    html.Br(),
    html.Hr(),
    html.Div(
        className='col-md-6',
        style={'text-align': 'center'},
        children=[
            html.H2('Drug Class'),
            html.
            H4('The Anatomical Thearapeutic Classification (ATC) is a standard vocabulary that categorizes drugs within domains such as organ system, mechanism of action, etc. Please choose the ATC class of drugs you want to view.'
               ),
            dcc.Dropdown(
                id="chosen-drug-class-input",
                options=drug_classes_list,
                value=drug_classes_list[0]['label'],
                clearable=False),
            html.Br(),
            dcc.Dropdown(id='chosen-drug-class-output', multi=True)
        ]),
    html.Div(
        className='col-md-6',
        style={'text-align': 'center'},
        children=[
            html.H2('How many reports?'),
            dcc.Graph(id='drug-class-num-reports')
        ]),
    html.Div(
        className='col-md-6',
        style={'text-align': 'center'},
        children=[
            html.H2('Frequency across years of reporting'),
            html.
            H4('Reports of ADRs were given in different years, where reporting may be more or less frequent for random reasons, or because of popular events such as news and drug releases.'
               )
        ]),
    html.Div(
        className='col-md-6',
        style={'text-align': 'center'},
        children=[dcc.Graph(id='drug-class-num-reports-across-report-years')]),
    html.Div(
        className='col-md-6',
        style={'text-align': 'center'},
        children=[
            html.H2('Breakdown of reporting based on sex'),
            html.
            H4('Reporting of ADRs can be by males or females, which can vary in reporting behavior as well as have different predisposition to drug use.'
               )
        ]),
    html.Div(
        className='col-md-6',
        style={'text-align': 'center'},
        children=[
            dcc.Graph(id='drug-class-num-reports-across-report-years-by-sex')
        ]),
    html.Div(
        className='col-md-6',
        style={'text-align': 'center'},
        children=[
            html.H2('Breakdown of reporting based on sex and age'),
            html.
            H4('Reporting of ADRs can be by males or females, as well as at different ages. Patient demographics can influence reporting as well as predisposition to drug use.'
               )
        ]),
    html.Div(
        className='col-md-6',
        style={'text-align': 'center'},
        children=[
            dcc.Graph(
                id='drug-class-num-reports-across-report-years-by-sex-and-age')
        ])
]),

feature_outcomes_page = html.Div(children=[
    html.H1(
        'Investigating Adverse Reactions from drug usage \nin ADR data',
        style={'text-align': 'center'}),
    dcc.Link(
        'Go to Home Page', href='/', style={
            'font-size': 16,
            'color': 'blue'
        }),
    html.Br(),
    dcc.Link(
        'Investigate Drugs',
        href='/feature_drugs_page',
        style={
            'font-size': 16,
            'color': 'blue'
        }),
    html.Br(),
    dcc.Link(
        'Investigate ADRs',
        href='/feature_drugs_and_outcomes_page',
        style={
            'font-size': 16,
            'color': 'blue'
        }),
    html.Br(),
    html.Hr(),
    html.Div(
        className='col-md-6',
        style={'text-align': 'center'},
        children=[
            html.H2('Number of Adverse Reactions'),
            html.
            H4('Patients may report one or many adverse reactions to a drug, which can either be causal or anecdotal (i.e caused by many factors) as well as reported more frequently than others. Choose how many adverse reactions you want to view.'
               )
        ]),
    html.Div(
        className='col-md-6',
        style={'text-align': 'center'},
        children=[
            html.H2('How many reports?'),
            dcc.Graph(id='outcomes-num-reports')
        ]),
    html.Div(
        className='col-md-6',
        style={'text-align': 'center'},
        children=[
            html.H2('Frequency across years of reporting'),
            html.
            H4('Reports of ADRs were given in different years, where reporting may be more or less frequent for random reasons, or because of popular events such as news and drug releases.'
               )
        ]),
    html.Div(
        className='col-md-6',
        style={'text-align': 'center'},
        children=[dcc.Graph(id='outcomes-num-reports-across-report-years')]),
    html.Div(
        className='col-md-6',
        style={'text-align': 'center'},
        children=[
            html.H2('Breakdown of reporting based on sex'),
            html.
            H4('Reporting of ADRs can be by males or females, which can vary in reporting behavior as well as have different predisposition to drug use.'
               )
        ]),
    html.Div(
        className='col-md-6',
        style={'text-align': 'center'},
        children=[
            dcc.Graph(id='outcomes-num-reports-across-report-years-by-sex')
        ]),
    html.Div(
        className='col-md-6',
        style={'text-align': 'center'},
        children=[
            html.H2('Breakdown of reporting based on sex and age'),
            html.
            H4('Reporting of ADRs can be by males or females, as well as at different ages. Patient demographics can influence reporting as well as predisposition to drug use.'
               )
        ]),
    html.Div(
        className='col-md-6',
        style={'text-align': 'center'},
        children=[
            dcc.Graph(
                id='outcomes-num-reports-across-report-years-by-sex-and-age')
        ])
]),

feature_drugs_and_outcomes_page = html.Div(children=[
    html.H1('Investigating ADRs', style={'text-align': 'center'}),
    dcc.Link(
        'Go to Home Page', href='/', style={
            'font-size': 16,
            'color': 'blue'
        }),
    html.Br(),
    dcc.Link(
        'Investigate Drugs',
        href='/feature_drugs_page',
        style={
            'font-size': 16,
            'color': 'blue'
        }),
    html.Br(),
    dcc.Link(
        'Investigate Adverse Reactions',
        href='/feature_outcomes_page',
        style={
            'font-size': 16,
            'color': 'blue'
        }),
    html.Br(),
    html.Hr(),
    html.Div(
        className='col-md-6',
        style={'text-align': 'center'},
        children=[
            html.H2('Adverse drug reactions'),
            html.
            H4('ADRs that are reported may be more or less frequent in the population. Choose the number of ADRs you would like to view, with the top being the most frequent ADR in the dataset.'
               )
        ]),
    html.Div(
        className='col-md-6',
        style={'text-align': 'center'},
        children=[
            html.H2('How many reports?'),
            dcc.Graph(id='adr-num-reports')
        ]),
    html.Div(
        className='col-md-6',
        style={'text-align': 'center'},
        children=[
            html.H2('Frequency across years of reporting'),
            html.
            H4('Reports of ADRs were given in different years, where reporting may be more or less frequent for random reasons, or because of popular events such as news and drug releases.'
               )
        ]),
    html.Div(
        className='col-md-6',
        style={'text-align': 'center'},
        children=[dcc.Graph(id='adr-num-reports-across-report-years')]),
    html.Div(
        className='col-md-6',
        style={'text-align': 'center'},
        children=[
            html.H2('Breakdown of reporting based on sex'),
            html.
            H4('Reporting of ADRs can be by males or females, which can vary in reporting behavior as well as have different predisposition to drug use.'
               )
        ]),
    html.Div(
        className='col-md-6',
        style={'text-align': 'center'},
        children=[dcc.Graph(id='adr-num-reports-across-report-years-by-sex')]),
    html.Div(
        className='col-md-6',
        style={'text-align': 'center'},
        children=[
            html.H2('Breakdown of reporting based on sex and age'),
            html.
            H4('Reporting of ADRs can be by males or females, as well as at different ages. Patient demographics can influence reporting as well as predisposition to drug use.'
               )
        ]),
    html.Div(
        className='col-md-6',
        style={'text-align': 'center'},
        children=[
            dcc.Graph(id='adr-num-reports-across-report-years-by-sex-and-age')
        ])
]),

age_page = html.Div(children=[
    html.H1('ADR age relation'),
    dcc.Link(
        'Go to Home Page', href='/', style={
            'font-size': 16,
            'color': 'blue'
        }),
    html.Br(),
    dcc.Link(
        'Go to ADR table Page',
        href='/table_page',
        style={
            'font-size': 16,
            'color': 'blue'
        }),
    html.Hr(),
    html.Div(
        style={
            'class': "col-sm-4",
            'border': '2px solid black',
            'float': 'left'
        },
        children=[
            html.H1(
                'How many patients are taking these drugs?',
                style={
                    'text-align': 'center',
                    'font-size': 18
                }),
            dcc.Dropdown(
                id='drug_count',
                options=[{
                    'label': i,
                    'value': i
                } for i in uniq_drugs],
                value=uniq_drugs[0]),
            html.Div(id='drug_output', style={'text-align': 'center'})
        ]),
    dcc.Graph(
        id='drug-reports-at-ages',
        style={
            'class': 'col-sm-4',
            'float': 'right'
        },
    )
])


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


# get list of drugs or drug categories based on drug class chosen
@app.callback(
    dash.dependencies.Output('chosen-drug-class-output', 'options'),
    [dash.dependencies.Input('chosen-drug-class-input', 'value')])
def set_chosen_drug_class_options(value):
    return [{'label': c, 'value': c} for c in drugs_in_drug_classes[value]]


# get list of drugs or drug categories based on drug class chosen
@app.callback(
    dash.dependencies.Output('chosen-drug-class-output', 'value'),
    [dash.dependencies.Input('chosen-drug-class-input', 'value')])
def set_chosen_drug_class_value(available_options):
    return available_options


@app.callback(
    dash.dependencies.Output('drug-class-num-reports', 'options'), [
        dash.dependencies.Input('chosen-drug-class-input', 'value'),
        dash.dependencies.Input('chosen-drug-class-output', 'value')
    ])
def plot_drug_class_num_reports(col, classes):
    title = ''
    x_legend = "classes"
    y_legend = "Number of reports"
    dat = data.counts_by_feature("report_year", '{0} in {1}'.format(
        col, classes))
    return sd_plot.bar_plot(
        title,
        x_legend,
        y_legend,
        trace1=dat,
        t1name="Drugs",
        trace2=False,
        t2name=False)


#Show number of patients taking selected drug in dataset
@app.callback(
    dash.dependencies.Output('drug_output', 'children'), [
        dash.dependencies.Input('drug_count', 'value'),
    ])
def callback_drug(value):
    return 'There are {} patients that reported taking {}'.format(
        data.count('drug_concept_name=="' + value + '"'), value)


#Update bar graph for drug
@app.callback(
    dash.dependencies.Output('drug-reports-at-ages', 'figure'),
    [dash.dependencies.Input('drug_count', 'value')])
def callback_drug_reports_at_ages_bars(value):
    title = 'Patients taking {} at different age intervals'.format(value)
    x_legend = "Age category"
    y_legend = "Percentage of reports"
    this_drug_title = '{}'.format(value)
    all_drugs_title = "All drugs"
    this_drug = data.counts_by_feature("age_cat",
                                       'drug_concept_name == "' + value + '"')
    return sd_plot.bar_plot(title, x_legend, y_legend, this_drug, all_drugs,
                            this_drug_title, all_drugs_title)

# enable bootstrap styling
external_css = [["https://bootswatch.com/3/paper/bootstrap.css"],
                ["docs/custom.css"]]

for css in external_css:
    app.css.append_css({"external_url": css})

if __name__ == '__main__':
    app.run_server(debug=True)
