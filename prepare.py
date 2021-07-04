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
    
    '''
    # convert Date to datetime object
    df.Date = pd.to_datetime(df.Date)

    







