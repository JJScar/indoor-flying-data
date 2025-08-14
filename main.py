import pandas as pd
from pathlib import Path
from src.database import load_flyers_csv, save_flyers_csv

def add_flyer(flyers: pd.DataFrame, new_flyer_data: dict) -> pd.DataFrame:
    """
    Method that takes in a dict of a new flyer's data and adds that flyer to the database
    
    Parameters
    ----------
    new_flyer_data : dict
        Dictionary containing the new flyer's data. The keys should be the columns in the 
        database and the values should be the values for those columns, except the id which 
        is calculated within the function
        
    Returns
    -------
    pandas.DataFrame
        DataFrame containing the updated flyers data
    """
    
    # TODO add some checks to make sure that the data is valid:
        # 1. Format and types are good 
        # 2. Check if flyer exists already
    
    last_id = flyers['id'].max() if not flyers.empty else 0
    id_dict = {'id': last_id + 1}
    new_flyer_data_with_id = dict(id_dict, **new_flyer_data)
    
    new_flyer_row = pd.DataFrame([new_flyer_data_with_id])
    
    flyers = pd.concat([flyers, new_flyer_row], ignore_index=True)
    
    return flyers

def remove_flyer(flyers: pd.DataFrame, id: int) -> pd.DataFrame:
    """
    Method that takes in a DataFrame of flyers and an id and removes the flyer with 
    that id from the database
    
    Parameters
    ----------
    flyers : pandas.DataFrame
        DataFrame containing the flyers data
    id : int
        unique identifier for the flyer
    
    Returns
    -------
    pandas.DataFrame
        DataFrame containing the updated flyers data
    """
    
    # TODO add some checks to make sure that the data is valid:
        # 1. that id actually exists if not throw error
        # 2. Maybe something else?
        
    flyers = flyers.drop(flyers[flyers['id'] == id].index)
    return flyers

new_data = {
    'name': "Josh",
    'age': 23,
    'level': 2,
    'total_time': 55,
    'current': 0,
    'instructor': 0
}

file_path = Path("./data/flyers.csv")

# Adding a new flyer 
print("========>Adding flyer output<========")
flyers = load_flyers_csv(file_path)
flyers = add_flyer(flyers, new_data)
save_flyers_csv(flyers, file_path)
print(flyers)
print("-------------------------------------------------")

# Removing a flyer
print("========>Removing flyer output<========")
id_to_remove = int(input("Enter the id of the flyer to remove: "))
flyers = remove_flyer(flyers, id_to_remove)
save_flyers_csv(flyers, file_path)

# Result after all operations
print(flyers)