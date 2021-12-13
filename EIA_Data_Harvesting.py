# installing necessary libraries
import pandas as pd
import requests
import matplotlib.pyplot as plt
import numpy as np
from datetime import date
import matplotlib.ticker as ticker

# API Key from EIA
api_key = '45fc211dc417f6b7a53609c99ab0546a'

# PADD Names to Label Columns
# Change to whatever column labels you want to use

PADD_NAMES = ['PADD 1', 'PADD 2', 'PADD 3', 'PADD 4', 'PADD 5']

# enter all your Series IDs here seperated by commas
PADD_KEY = ['PET.MCRRIP12.M', 'PET.MCRRIP22.M', 'PET.MCRRIP32.M',
            'PET.MCRRIP42.M', 'PET.MCRRIP52.M']

# initialize list - this is the final list that you will store all the data
# from the json pull. Then you will use this list to concat into a pandas df.

final_data = []

# choose start and end dates
startDate = '2000-01-01'
endDate = '2021-01-01'

# pull in data via EIA API
for i in range(len(PADD_KEY)):

    url = 'http://api.eia.gov/series/?api_key=' + api_key + '&series_id=' + \
          PADD_KEY[i]

    r = requests.get(url)
    json_data = r.json()

    if r.status_code == 200:
        print('Success!')
    else:
        print('Error :(')

    df = pd.DataFrame(json_data.get('series')[0].get('data'),
                      columns = ['Date', PADD_NAMES[i]])

    df.set_index('Date', drop = True, inplace = True)
    final_data.append(df)
