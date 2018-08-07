"""

Helper functions for data wrangling and plotting for SafeDrugs

"""




def plot_settings(style='seaborn-whitegrid'):
	"""
	Common rcParams for plot styling
	"""
	import matplotlib as mpl
	
	mpl.style.use(style)
	mpl.rcParams['font.weight']='bold'
	mpl.rcParams['font.size']=16



def clean_gender(data):
	"""
	Only use M and F in gender_code
	"""
	
	return data.query('gender_code in ["M","F"]')


 
def dropdown(arr,layout=None):
	"""
	Helper for pywidget dropdown
	
	Takes in array
	"""
	
	import ipywidgets as w

	if layout is None:
		layout = w.Layout(width='30%', display='flex')
	
	return w.Dropdown(options = arr,layout=layout)


def data_column_dropdown(data,layout=None):
	"""
	Helper for pywidget dropdown
	
	Takes in series
	"""
	
	import ipywidgets as w
	
	arr = data.columns.values

	return dropdown(arr)


def data_column_dropdown_multiple_tabs(data,t = ['x', 'y', 'y2', 'z']):
	"""
	 
	Helper function for putting together multiple data column dropdowns in tab format
	"""
	from ipywidgets import Tab
	 
	if t is None:
		t = ['x', 'y', 'y2', 'z']
	tab_contents = t
	children = [data_column_dropdown(data) for name in tab_contents]
	tab = Tab()
	tab.children = children
	tab_dict = {}
	for i,var in enumerate(tab_contents):
		tab.set_title(i, var)
		tab_dict[var] = tab.children[i]

	return tab_dict, tab


def freqXbyY(data,x = 'drug_concept_id',y = 'report_year'):
	"""
	helper groupby x and count y method
	"""
	
	return data.groupby(x)[y].count()


def filtXfreqYbyZ(data,label,x,y,z):
	"""
	filter by the label in x within the dataframe
	
	use freqXbyY helper method
	"""
	
	tmp=data.query("{0}==@label".format(x))

	return freqXbyY(tmp,y,z)



def plot(series,kind):
	"""
	helper for plotting
	"""


	g = series.plot(kind=kind)

	return g


