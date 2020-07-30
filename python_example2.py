'''
Author:        Rameet Gulsin
Date:          13/07/2020
Description:   Kenometrics python sheet to introduce the Quandl python package
'''

# If you have not already done so, install the quandl package with your preferred
# choice of package manager e.g. pip install quandl, conda install quandl

# import the quandl packaage
import quandl

# import package for plotting
import matplotlib.pyplot as plt

'''
Example: downloading annual UK GDP time series.
'''

# authenticate your account
quandl.ApiConfig.api_key = 'YOUR OWN API KEY GOES HERE'

# Filename to save your data as
file_name = 'uk_gdp2.csv'

# Set start date and end date
start = '2000-12-31'
end = '2019-12-31'

# get data
# data = quandl.get('SGE/GBRG', start_date=start, end_date=end)

# now we can start doing much more interesting things
countries = ['SGE/GBRG', 'SGE/COLG', 'SGE/DEUG', 'SGE/HKGG', 'SGE/IRQG', 'SGE/USAG']
names = ['UK', 'Colombia', 'Germany', 'Hong Kong', 'Iraq', 'USA']

# get data from Quandl
gdp_data = quandl.get(countries, start_date=start, end_date=end)

# plot data on line chart
uk, col, ger, hk, irq, usa = plt.plot(gdp_data)
plt.legend((uk, col, ger, hk, irq, usa), names) # label plots and turn on legend
plt.grid()  # turn gridlines on
plt.show()  # show the graph
