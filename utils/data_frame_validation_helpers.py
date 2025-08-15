from typing import Dict, Any, List
import pandas as pd

def validate_data_frame(df: pd.DataFrame, existing_df: pd.DataFrame) -> Dict[str, Any]:
    """
    Method that takes in a DataFrame of flyers and a DataFrame of existing flyers and 
    performs multiple checks on the DataFrame to ensure it is valid. The checks are 
    as follows:
    1. The DataFrame has the correct structure and columns
    2. The DataFrame has the correct data types
    
    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame containing the flyer data
    existing_df : pandas.DataFrame
        DataFrame containing the existing flyer data
    
    Returns
    -------
    dict
        A dictionary containing the result of the checks. The dictionary will have 
        the following keys:
        - is_valid (bool): True if the DataFrame is valid, False otherwise
        - errors (list): A list of strings containing the errors found
    """
    expected_columns = ['id', 'name', 'age', 'level', 'total_time', 'current', 'instructor']
    
    overall_result = {
        'is_valid': True,
        'errors': [],
    }
    
    result_structure = validate_data_frame_structure(df, expected_columns)
    if result_structure['is_valid'] == False:
        if result_structure['errors']:
            overall_result['is_valid'] = False
            overall_result['errors'].append(result_structure['errors'])
    
    result_types = validate_data_frame_types(df)
    if result_types['is_valid'] == False:
        if result_types['errors']:
            overall_result['is_valid'] = False
            overall_result['errors'].append(result_types['errors'])
        
    result_ranges = validate_data_frame_ranges(df)
    if result_ranges['is_valid'] == False:
        if result_ranges['errors']:
            overall_result['is_valid'] = False
            overall_result['errors'].append(result_ranges['errors'])
        
    return overall_result

def validate_data_frame_structure(df: pd.DataFrame, expected_columns: List[str]) -> Dict[str, Any]:
    """
    Method that takes in a DataFrame of flyers and a list of the expected columns structure and 
    performs checks on the DataFrame to ensure it's structure is valid.
    
    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame containing the flyer data
    expected_columns : List[str]
        List of expected column names.
    
    Returns
    -------
    dict
        A dictionary containing the result of the checks. The dictionary will have 
        the following keys:
        - is_valid (bool): True if the DataFrame is valid, False otherwise
        - errors (list): A list of strings containing the errors found
    """
    
    result = {
        'is_valid': True,
        'errors': []
    }
    
    # Check if the DataFrame is empty
    if df.empty:
        result['is_valid'] = False
        result['errors'].append("DataFrame is empty.")
    
    # Check it has the necessary amount of columns
    if len(df.columns) != len(expected_columns):
        result['is_valid'] = False
        result['errors'].append(f"{len(df.columns)} is an incorrect number of columns. Expected: {len(expected_columns)}")
    
    # Iterating over to see what columns are missing and what are unneeded
    missing_columns = [col for col in expected_columns if col not in df.columns]
    extra_columns = [col for col in df.columns if col not in expected_columns]
    
    if missing_columns:
        result['is_valid'] = False
        result['errors'].append(f"Missing columns: {missing_columns}")
        
    if extra_columns:
        result['is_valid'] = False
        result['errors'].append(f"Invalid columns: {extra_columns}")
    
    return result

# TODO finish fixing
def validate_data_frame_types(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Method that takes in the DataFrame dtypes and checks if they match the expected dtypes.
    
    Parameters
    ----------
    df : pandas.DataFrame
        The DataFrame to validate.
    
    Returns
    -------
    dict
        A dictionary containing the result of the checks. The dictionary will have 
        the following keys:
        - is_valid (bool): True if the dtypes are valid, False otherwise
        - errors (list): A list of strings containing the errors found
    """
    expected_dtypes = {
        'id': int,
        'first_name': str,
        'surname': str,
        'age': int,
        'level': int,
        'total_time': int,
        'current': int,
        'instructor': int,
    }
    
    result = {
        'is_valid': True,
        'errors': []
    }
    
    for col_name, expected_type in expected_dtypes.items():
        # TODO make sure this is not done in the validate structure def
        if col_name not in df.columns:
            result['is_valid'] = False
            result['errors'].append(f"{col_name} is missing.")
            continue
        
        type_to_check = df[col_name].dtype
        
        

    return result

# TODO
def validate_data_frame_ranges(df: pd.DataFrame) -> Dict[str, Any]:
    # Making sure that all elements make sense
        
    result = {
        'is_valid': True,
        'errors': []
    }    
    
    value_constraints = {
        'id': {'min': 1, 'not_null': True},
        'first_name': {'not_null': True},
        'surname': {'not_null': True},
        'age': {'min': 0, 'max': 120, 'not_null': True},
        'level': {'min': 1, 'max': 5, 'not_null': True},
        'total_time': {'min': 0, 'not_null': True},
        'current': {'allowed_values': [0, 1], 'not_null': True},
        'instructor': {'allowed_values': [0, 1], 'not_null': True}
    }
    
    for column, rule in value_constraints.items():
        # Checking if value is null
        if rule.get('not_null', False):
            if df[column].isnull().any():
                result['is_valid'] = False
                result['errors'].append(f"{column} cannot be null")
        
        # Checking if the columns are above the necessary min value
        if 'min' in rule:
            min_val = rule['min']
            if (df[column] < min_val).any():
                result['is_valid'] = False
                result['errors'].append(f"The {column} cannot be less than {min_val}")
        
        # Checking if the columns are less than the necessary max value
        if 'max' in rule:
            max_val = rule['max']
            if (df[column] > max_val).any():
                result['is_valid'] = False
                result['errors'].append(f"The {column} cannot be more than {max_val}")  
                
        # Checking if the columns that need to have specific values comply
        if 'allowed_values' in rule:
            allowed = rule['allowed_values']
            invalid_values = df[~df[column].isin(allowed)][column].unique()
            if len(invalid_values) > 0:
                result['is_valid'] = False
                result['errors'].append(
                    f"Column '{column}' has invalid values: {list(invalid_values)}. "
                    f"Allowed values: {allowed}"
                )
                
    return result