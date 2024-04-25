from fuzzywuzzy import fuzz
from fuzzywuzzy import process


MATCHING_FUNCTION = fuzz.token_set_ratio

def dict_match_string(item: dict, keys_to_match: list[str], joined_by: str = ' ') -> str:
    '''
    Parameters:
        item: dict: Dictionary to match
        keys_to_match: list[str]: Keys in dictionary to build match option.
        joined_by: str: String to join the keys with
    '''
    return joined_by.join([str(item[key]) for key in keys_to_match])

def string_match(text: str, options: list[str], limit: int = 50) -> list[str]:
    '''
    Fuzzy matches a text with a list of strings
    Parameters:
        text: str: Text to match
        options: list[str]: List of strings to process
        limit: int: Limit of matches to return
    '''
    return process.extract(text, options, limit=limit, scorer=MATCHING_FUNCTION)

def dict_match(text: str, keys_to_match: list[str], options: list[dict], limit: int = 50, return_dicts: bool = True) -> list[dict]:
    '''
    Fuzzy matches a text with a list of dictionaries
    Parameters:
        text: str: Text to match
        keys_to_match: list[str]: Keys in dictionary to build match option.
        options: list[dict]: List of dictionaries to process
        limit: int: Limit of matches to return
        return_dicts: bool: Return as formatted dictionaries with the matches
    '''
    options_str = [dict_match_string(option, keys_to_match) for option in options]
    matches = process.extract(text, options_str, limit=limit, scorer=MATCHING_FUNCTION)
    if return_dicts:
        return [{'match': options[options_str.index(match[0])], 'score': match[1], 'as_string': match[0]} for match in matches]
    return matches


def modify_scores(matches: list[dict], modifier: callable) -> list[dict]:
    '''
    Parameters:
        matches: list[dict]: List of matches with keys 'match', 'score', 'as_string'
        modifier: Function that takes a match and returns a new score
            Parameters:
                - match: dict with keys 'match', 'score', 'as_string'
            Returns:
                - new_score: float
    Returns: list[dict]
    '''
    for match in matches:
        match['score'] = modifier(match)
    return sorted(matches, key=lambda x: x['score'], reverse=True)  # Sort by score 