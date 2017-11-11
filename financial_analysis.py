
"""
class financial analysis
sub class daily percentage change
method calculate
method plot??

"""
import statsmodels.api as sm


class daily_pct_change(object):
 	"""docstring for daily_pct_change"""
 	def __init__(self, data):
 		self.data = data
 		self.daily_percentage_change()


 	def daily_percentage_change(self):
		self.daily_close = self.data[['C']] 	# Assign `Adj Close` to `daily_close`
		self.daily_pct_change = daily_close.pct_change() # Daily returns
		self.daily_pct_change.fillna(0, inplace=True) # Replace NA values with 0


	def daily_log_returns(self):
		self.daily_log_returns = np.log(daily_close.pct_change()+1)


	def plot_daily_pct_change(self):
		# Plot the distribution of `daily_pct_c`
		daily_pct_change.hist(bins=50)

		# Show the plot
		plt.show()

		# Pull up summary statistics
		print(daily_pct_change.describe())

	def cum_daily_return(self):
		# Calculate the cumulative daily returns
		cum_daily_return = (1 + daily_pct_change).cumprod()

	def plot_cum_daily_return(self):
		# Plot the cumulative daily returns
		cum_daily_return.plot(figsize=(12,8))
		# Show the plot
		plt.show()


	def multi_plot(self):
		# Isolate the `Adj Close` values and transform the DataFrame
		daily_close_px = all_data[['C']].reset_index().pivot('Date', 'Ticker', 'C')

		# Calculate the daily percentage change for `daily_close_px`
		daily_pct_change = daily_close_px.pct_change()

		# Plot the distributions
		daily_pct_change.hist(bins=50, sharex=True, figsize=(12,8))

		# Show the resulting plot
		plt.show()

class moving_avg(object): #falta
	def __init__(self, data):
		self.data = data

	def moving_average(self):
		self.adj_close_px = self.data['C']

		# Calculate the moving average
		moving_avg = adj_close_px.rolling(window=40).mean()


	def ():
		pass

