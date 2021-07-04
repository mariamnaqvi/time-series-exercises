import pandas as pd

def prep_store_items(df):
    '''
    This function takes in the store and items combined dataframe and makes these changes
    # change date variable to datetime
    # set index to be datetime variable and sort the index
    # add month and day of week columns to the dataframe
    # add sales total column to df
    '''
    # convert sale date to datetime
    df.sale_date = pd.to_datetime(df.sale_date)

    # set index to be datetime variable
    df = df.set_index('sale_date').sort_index()

    # add month column to df
    df['month'] = df.index.month

    # add day column to df
    df['day_of_week'] = df.index.day_name()
    
    # add sales total column
    df['sales_total'] = df.sale_amount * df.item_price

    # return new df
    return df

def prep_energy_data(df):
    '''
    This function takes in a pandas dataframe and makes these changes
    # change date to datetime
    # set date as index and sort it
    # add month and year columns
    # fill missing values
    '''

    # convert Date to datetime object
    df.Date = pd.to_datetime(df.Date)

    # set and sort the index
    df = df.set_index('Date').sort_index()

    # add month col to df
    df['month'] = df.index.month

    # add year col to df
    df['year'] = df.index.year

    # fill missing values with 0
    df = df.fillna('0')
    
    # return prepped df
    return df











