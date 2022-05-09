import pandas as pd

def rename_columns(df: pd.DataFrame()) -> pd.DataFrame():

    """
    Fix dataframe columns name so it can't cause a conflict into
    the database

    Args:
        df(pd.DataFrame): DataFrame to be fixed with the function

    Returns:
        df(pd.DataFrame): DataFrame with fixed columns name
    """

    columns_to_be_renamed = df.columns

    # removes undesired characters
    renamed_columns = [i.upper().replace(' ','_').replace('.','_')
                        for i in columns_to_be_renamed]

    # Creates a dict to be parsed into pd.Dataframe().rename()
    dict_sourcecol_targetcol = dict(zip(columns_to_be_renamed, renamed_columns))

    # Renaming columns
    transformed_df = df.rename(columns=dict_sourcecol_targetcol)

    return transformed_df

