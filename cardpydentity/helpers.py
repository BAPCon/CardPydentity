
import re
from typing import Union


def extract_card_tuple(text: str) -> Union[tuple[int, int], bool]:
    ''' 
    Use regex to search for patterns of the form "number/number"
    '''
    match = re.search(r'(\d+)\s*/\s*(\d+)', text)
    if match:
        # If found, return the numbers as a tuple of integers
        return (match.group(1), match.group(2))
    else:
        # If no pattern is found, return False
        return False

def extract_year_in_text(text: str) -> Union[int, bool]:
    '''
    Use regex to search for years in the range 1992-2025
    '''
    present_years = []
    for year in range(1992, 2026):      
        if str(year) in text:
            present_years.append(str(year))
    return present_years[0] if present_years else False

def extract_numbers_in_text(text: str) -> list[str]:
    return re.findall(r'\d+', text)

def tuple_padding(num_tuple: tuple[str, str]) -> list[tuple[str, str]]:
    _ = []
    for l0 in range (0, 4):
        for r0 in range(0, 4):
            for l1 in range(0, 4):
                for r1 in range(0, 4):
                    _.append((' ' * l0 + num_tuple[0] + ' ' * r0, ' ' * l1 + num_tuple[1] + ' ' * r1))
    return _

def remove_extra_spacing(text: str) -> str: 
    while '  ' in text:
        text = text.replace('  ', ' ')
    return text.strip()

def extract_grades_in_text(text: str) -> list[str]: 
    '''
    Extracts grades from a string. 
    '''
    grades = ['NM', 'M', 'LP', 'MP', 'HP']
    response = []
    for word in text.split(' '):
        for grade in grades:
            if word == grade:
                response.append(grade)
                continue
            if any(word.replace(' ', '') == f'{grade}/{grade2}' or word.replace(' ', '') == f'{grade2}/{grade}' for grade2 in grades):
                response.append(grade)
    return response
