'''
Author:        Rameet Gulsin
Date:          13/07/2020
Description:   Kenometrics python sheet to introduce the basic Quandl API
'''

# make required package imports
import requests
from io import StringIO
import urllib.parse
import pandas as pd

'''
Example: downloading annual UK GDP time series.
'''

# Always set to your own API key
api_key = 'YOUR OWN API KEY GOES HERE'

# Filename to save your data as
file_name = 'uk_gdp.csv'

# Set country ISO
cntry = 'GBR'

# Set indicator ISO
indic = 'G'

# Set start date and end date
start = '2000-12-31'
end = '2019-12-31'

# create URL components
scheme = 'https'
netloc = 'www.quandl.com'
path = f'/api/v3/datasets/SGE/{cntry + indic}/data.csv'
params = ''
query = (
    f'start_date={start}&end_date={end}&api_key={api_key}'
)
fragment = ''

# combine all elements of URL into a tuple
url_tuple = (scheme, netloc, path, params, query, fragment)

# parse the newly created tuple as a URL
url = urllib.parse.urlunparse(url_tuple)

# Send the URL request
response = requests.get(url)

# Convert response from Quandl server to readable csv
raw_data = StringIO(response.text)

# Convert csv to pandas DataFrame
data = pd.read_csv(raw_data)

# Save your data to the directory where this python sheet is saved
data.to_csv(file_name, index=False)
