from datetime import datetime
import math
import numpy as np
import pandas as pd

def convert_birthday_to_age(   df: pd.DataFrame() 
                                , column: str
                                , keep_birthday_column: bool = False) -> pd.DataFrame():
    """
    This function is in charge of converting a birthday column into a
    column with the age
    Args:
        df (pd.DataFrame): pandas dataframe that will be transformed
        column (str): name of the birthday column

    Returns:
        df(pd.DataFrame): Dataframe with the "age" column
    """

    # Create a datetime birthday column
    df['datetime_birthday'] = pd.to_datetime(df[column])

    # Create a column with a datetime object with the value of the time that is been executing
    df['loadtime'] = datetime.now()

    # Create a column with deltatime as float in years
    df['float_age'] = (df.loadtime - df.datetime_birthday)/np.timedelta64(1,'Y')

    # Create the desired column 'age' by applying the function floor
    df['age'] = df['float_age'].apply(lambda row: math.floor(row)).astype(int)

    # Drop the columns created just for the calculations
    transformed_df = df.drop(columns = ['datetime_birthday','float_age'])

    # Removing 'birthday' column accordingly to the user's choice
    if keep_birthday_column == False: transformed_df = transformed_df.drop(columns=column)

    return transformed_df


def convert_age_to_age_groups(   df: pd.DataFrame() 
                                , column: str
                                , keep_age_column: bool = False) -> pd.DataFrame():
    """
    This function is in charge of dividing an age column into categories
    of '10 years age group' (i.e someone with 31 years old must be categorized in [30-40] age group category).
    

    Args:
        df (pd.DataFrame): pandas dataframe that will be transformed
        column (str): name of the age column
        keep_age_column (bool): Set this parameter to True if you want to keep the column
                                    used in this transformation
                                    
    Returns:
        df(pd.DataFrame): Dataframe with the "age_group" column
    """

    # Gets the maximum value of the column
    max_age = df[column].max()

    # Here I had to add + 11, (1) to include the max number in the interval
    # (10) to create one more category from (max range) to (max range + 9)
    # If max_age = 60, for example, we will have a category 60-69
    bins = [i for i in range(0, max_age+11, 10)]
    
    # Dividing labels using bins
    labels = [f'{i} - {i+9}' for i in bins[:-1]]

    # Using pd.cut to determine the categories using the 'age' column
    df['age_groups'] = pd.cut(  df[column]
                                , bins = bins
                                , labels = labels
                                ,right=False)
    
    # Removing 'age' column accordingly to the user's choice
    if keep_age_column == False: df = df.drop(columns=column)
    
    return(df)
