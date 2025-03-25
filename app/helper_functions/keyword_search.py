import re

def keyword_search(data: dict, keyword: str) -> list:
    """
    Perform a keyword search over the values in a dictionary, ignoring punctuation, spaces, and case.

    Args:
        data (dict): Dictionary with values to search.
        keyword (str): Keyword to search for.

    Returns:
        list: List of keys where the keyword is found in the corresponding value.
    """
    # Normalize the keyword by removing punctuation and spaces, and converting to lowercase
    normalized_keyword = re.sub(r'\W+', '', keyword).lower()
    
    result = []
    for key, value in data.items():
        # Normalize the value by removing punctuation and spaces, and converting to lowercase
        normalized_value = re.sub(r'\W+', '', value).lower()
        if normalized_keyword in normalized_value:
            result.append(key)
    
    return result
