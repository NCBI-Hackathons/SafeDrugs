"""

Helper functions for data wrangling and plotting for SafeDrugs

"""




def plot_settings(style='seaborn-whitegrid'):
	"""
	Common rcParams for plot styling
	"""
	import matplotlib as mpl
	
	mpl.style.use(style)
	mpl.rcParams['font.weight']= 'bold'
	mpl.rcParams['font.size']= 16



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
	
	tmp = data.query('{0}==@label'.format(x))
	
	return freqXbyY(tmp,y,z)



def plot(series,kind):
	"""
	helper for plotting
	"""
	
	series.plot(kind=kind)


