from datetime import datetime
import numpy as np
import pandas as pd
from typing import List
import os

from faker.ingest.pandas import write_df_to_database
from faker.request.pandas import request_data_as_df
from faker.transform.datamask import MaskColumn
from faker.transform.date import convert_age_to_age_groups, convert_birthday_to_age
from faker.transform.rename import rename_columns


def faker_api_workflow( desired_number_of_rows: int
                        , columns_to_mask_by_len: List = ['firstname','lastname','address.buildingNumber']
                        , unwanted_columns: List = ["address.id", "id"]
                        , if_exists: str = 'append'
                        , database_str: str = 'taxfix-challenge'
                        , table_str: str = 'FAKER_API'):
    """
    This is a generic workflow to get data from the
    API: https://fakerapi.it/api/v1/ and ingest into SQLite database that
    will be created in your work directory.
    The data will be transformed using some functions that you can find
    in the package "faker".

    Args:
        desired_number_of_rows (int): The number of rows that you want to request
        columns_to_mask_by_len (List, optional): List of columns that you want to use MaskColumn().bylen
                                                Default: ['firstname','lastname','address.buildingNumber']
        unwanted_columns (List, optional): List containing the name of unwanted columns. Defaults to 'address.id'.
        if_exists (str, optional): Inherited from the method pd.DataFrame().to_sql()
                                    for more information see: 
                                    https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html
                                    Defaults to 'append' 
        database_str (str, optional):   Name of the database that you want to access or create
                                        Defaults to 'taxfix-challenge'.
        table_str (str, optional):  Name of the table that you want to create or append your data 
                                     Defaults to 'FAKER_API'.
    """
    # Use the function request_data_as_df to acquire data as a pandas dataframe
    request_df =  request_data_as_df(desired_number_of_rows = desired_number_of_rows)

    # Remove unwanted columns in your dataframe
    cleaned_df = request_df.drop(columns=unwanted_columns)

    # Transform birthday column into 'age' column
    transformed_df = convert_birthday_to_age(df=cleaned_df,column='birthday')
    # Categorizes ages into predetermined range of values
    transformed_df = convert_age_to_age_groups(df=transformed_df, column='age', keep_age_column=True)
    # Convert the column 'email' into a 'domain' column by removing everything before '@'
    transformed_df['domain'] = transformed_df['email'].apply(lambda row: row.split("@")[-1])

    # Mask columns using the class MaskColumn (to see how this works please, see docs)
    masked_transformed_df = MaskColumn(transformed_df).by_len(list_of_columns = columns_to_mask_by_len)

    masked_transformed_df = MaskColumn(transformed_df).before_a_character(list_of_columns = \
                                ['email'], character = '@')

    masked_transformed_df = MaskColumn(transformed_df).before_a_character(list_of_columns = \
                                ['address.zipcode'], character = '-')

    masked_transformed_df = MaskColumn(transformed_df).after_a_character(list_of_columns =\
                                ['address.latitude', 'address.longitude'], character = '.')

    masked_transformed_df = MaskColumn(transformed_df).keep_first(list_of_columns =\
                                ['phone'], length=4)

    # Renaming columns name to remove unwanted characters
    renamed_columns_df = rename_columns(masked_transformed_df)

    # Use the function to write the data acquired and transformed in the previous steps into
    # the desired database/table and condition of choice ('append' or 'replace')
    write_df_to_database(   df = renamed_columns_df
                            , engine_str = f'''sqlite:///{os.path.join(os.getcwd(),f'{database_str}.db')}'''
                            , table_str = table_str
                            , if_exists = if_exists)

unwanted_columns = ["address.id", "id", "image", "website"]

faker_api_workflow( desired_number_of_rows= 10000,
                    unwanted_columns=unwanted_columns)
