#=
Author:        Rameet Gulsin
Date:          13/07/2020
Description:   Kenometrics julia sheet to introduce the basic Quandl API
=#

# If you have not already done so, import the Package manager package 'Pkg'
# and use this to import the 'HTTP' and 'CSV' package.
# import Pkg
# Pkg.add("HTTP")
# Pkg.add("CSV")

# Using required packages
using HTTP
using CSV

# Always set to your own API key
api_key = 'YOUR OWN API KEY GOES HERE'

# Filename to save your data as
file_name = "uk_gdp3.csv"

# Set country ISO
cntry = "GBR"

# Set indicator ISO
indic = "G"

# Set start date and end date
start_date = "2000-12-31"
end_date = "2019-12-31"

# create URL components
scheme = "https://"
netloc = "www.quandl.com"
path = "/api/v3/datasets/SGE/$cntry$indic/data.csv"
query = "?start_date=$start_date&end_date=$end_date&api_key=$api_key"

# concatenate strings to form full url
url = scheme * netloc * path * query

# Send the URL request and get data
response = HTTP.get(url)

# convert response from Quandl server to readable csv
data = CSV.read(IOBuffer(response.body))

# save csv to directory
CSV.write(file_name, data)
