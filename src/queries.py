# This is where we get information from the database about the flyers

def is_instructor(df, id):
    """
    Method that takes in a DataFrame of the flyers and an id and returns a bool indicating
    if the flyer is an instructor or not.
    
    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame containing the flyer data
    id : int
        unique identifier for the flyer
    
    Returns
    -------
    str
        A string indicating if the flyer is an instructor or not
    """
    result = df.loc[df["id"] == id, "instructor"].values[0]
    if result == 1: 
        return True
    return False

def is_current(df, id):
    """
    Method that takes in a DataFrame of flyers and an id and returns a bool indicating
    if the flyer is current or not.
    
    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame containing the flyer data
    id : int
        unique identifier for the flyer
    
    Returns
    -------
    str
        A string indicating if the flyer is current or not
    """
    result = df.loc[df["id"] == id, "current"].values[0]
    if result == 1: 
        return True
    return False

def flyer_level(df, id):
    """
    Method that takes in a DataFrame of flyers and an id and returns the level of the 
    flyer
    
    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame containing the flyer data
    id : int
        unique identifier for the flyer
    
    Returns
    -------
    str
        A string indicating what flying level the flyer is at
    """
    return df.loc[df["id"] == id, "level"].values[0]