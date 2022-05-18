import pandas as pd
from sqlalchemy import create_engine

def write_df_to_database(   df: pd.DataFrame
                            , engine_str: str
                            , table_str : str
                            , if_exists : str = 'append') -> None:
    """
    Write your pandas DataFrame into a database using supported
    SQLAlchemy connectors.

    Args:
        df (pd.DataFrame): Pandas DataFrame that you want to insert into your database
        engine_str (str): String containing SQLAlchemy format connection 
        table_str (str): Name of the table that you want to append data or create
        if_exists (str, optional): Inherited from the method pd.DataFrame().to_sql()
                                    for more information see: 
                                    https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html
                                    Defaults to 'append'
    """
    # Create SQLAlchemy engine to write your dataframe into the database
    engine = create_engine(engine_str)
    # Write your data to the desired database
    response = df.to_sql(table_str, con=engine, if_exists=if_exists, index=False)

    return(print(f"Number of rows inserted: {response}"))

