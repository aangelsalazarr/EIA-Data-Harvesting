import pandas as pd
from pandas_datareader import wb
import matplotlib.pyplot as plt
from functools import reduce

# want to grab electricity access data
electricity_access = "EG.ELC.ACCS.ZS"
renewable_electricity_excluding_hydro = "EG.ELC.RNWX.KH"
renewable_energy_consumption = "EG.FEC.RNEW.ZS"

countries = ["USA"]

# creating a dataframe on electricity access
df1 = wb.download(indicator=electricity_access, country=countries, start=2010,
                  end=2018)
# print(df1)

# creating a dataframe on renewable electricity excluding hydro
df2 = wb.download(indicator=renewable_electricity_excluding_hydro, country=countries,
                  start=2010, end=2018)
# print(df2)

# creating a dataframe on renewable energy consumption (%)
df3 = wb.download(indicator=renewable_energy_consumption, country=countries,
                  start=2010, end=2018)
# print(df3)

# putting all dataframes in to a list
data_frames = [df1, df2, df3]

# merging our dataframes into one df
df_merged = reduce(lambda left, right: pd.merge(left, right, on=['country'],
                                                how="outer"), data_frames)

# renaming our col names
df_merged.columns = ["Electricity Access (%)", "Renewable Electricity Excluding Hydro (kWh)",
                     "Renewable Energy Consumption (%)"]

print(df_merged)

# now we want to visualize some data
df_merged.plot(x="Electricity Access (%)", y="Renewable Energy Consumption (%)", kind="scatter")
plt.show()
