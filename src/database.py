import pandas as pd

def load_flyers_csv(path="../data/flyers.csv"):
    """
    Method that loads flyer data from a specified .csv file and returns it as a DataFrame.
    
    Parameters
    ----------
    path : str, optional
        Path to the .csv file containing the flyer data (default is "../data/flyers.csv")
    
    Returns
    -------
    pandas.DataFrame
        DataFrame containing the flyer data
    """

    df = pd.read_csv(path)
    # df.reset_index(drop=True)
    return df
    
def save_flyers_csv(df, path="../data/flyers.csv"):
    """
    Method that takes in a DataFrame of flyers and a path and saves the DataFrame to 
    that path as a .csv file.
    
    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame containing the flyer data
    path : str
        Path to save the .csv file
    """
    df.to_csv(path, index=False)
    # df.reset_index(drop=True)
    
# TODO make sure this is correct, this is just something from LLMs make sure this is 
# using best practices