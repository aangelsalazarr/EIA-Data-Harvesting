import eia
import pandas as pd

def retrieve_time_series(api, series_ID):
    """
    Return the time series dataframe, based on API and unique series ID
    """
    # retrieve data by series id
    series_search = api.data_by_series(series=series_ID)
    # create a pandas dataframe from the retrieved time series
    df = pd.DataFrame(series_search)
    return df

def main():
    """
    Run main script
    """
    # create EIA API using your specific API Key
    api_key = "45fc211dc417f6b7a53609c99ab0546a"
    api = eia.API(api_key)
    # declare desired series ID
    series_ID = 'EMISS.CO2-TOTV-TT-NG-TX.A'
    df = retrieve_time_series(api, series_ID)
    # print the returned dataframe
    print(df)

if __name__== "__main__":
    main()
