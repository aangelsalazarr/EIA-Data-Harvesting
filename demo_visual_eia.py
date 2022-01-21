from eia_electricity_ids import *
import eia
import pandas as pd
import requests
import matplotlib.pyplot as plt
import numpy as np
from datetime import date
import matplotlib.ticker as ticker

# Energy Information Administration personal API KEY
api_key = "45fc211dc417f6b7a53609c99ab0546a"

# here we are referencing the api we will be using
api = eia.API(api_key)


# here is the code
def retrieve_time_series(api, series_ID):
    """
    return the time series dataframe, based on API and a unique Series ID
    """
    # retrieve data by series ID
    series_search = api.data_by_series(series=series_ID)

    # create a pandas dataframe from the retrieved time series
    df = pd.DataFrame(data=series_search)
    df.reset_index(inplace=True)
    df.columns = ['date', 'value']
    return df


# calling EIA API with specified series ID
plot1 = retrieve_time_series(api, net_gen_all_fuels_electric_us)
print(plot1.head())  # plotting first few lines of our df
print(plot1)

# here we will attempt to visualize the plot
plot1.plot(x='date', y='value', color='blue')

# adding titles and axis names
plt.title('US Electric Power, Net Generation')
plt.ylabel('thousand megawatthours (MWh)')
plt.xlabel('Date')

# showing our plot
plt.show()
