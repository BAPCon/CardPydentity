from typing import List, Dict
from .load import get_source
from .fuzzy import *
from .helpers import *  


class Matcher:  
    '''
    Class to match a text with a list of item options.
    '''
    
    def __init__(self, text: str, category: str = None):
        self.raw_text = text
        self.category = category if category else self.get_category()
        self.data = get_source(self.category)
        self.year_present = False

    def get_category(self):
        '''
        Function to get the category of the text.   
        '''
        simple_match = self.get_category_simple(self.raw_text)
        if simple_match:
            return simple_match
        return self.get_category_complex(self.raw_text)

    @staticmethod
    def get_category_complex(self, text: str):
        # To be implemented
        pass

    @staticmethod
    def get_category_simple(text: str):
        '''
        Function to get the category of the text based on simple keyword matching.
        '''
        if any(kword in text.lower() for kword in ['pokemon', 'pokémon']):
            return 'pokemon'
        if any(kword in text.lower() for kword in ['funko', 'funko pop', 'funko pop!', 'funko!']):
            return 'funko'
        if any(kword in text.lower() for kword in ['magic: the gathering', 'magic the gathering']) or 'mtg' in text.lower().split(' '):
            return 'magic'

    def substitute(self, text: str, substitutions: list[list[str]]) -> str:
        '''
        Function to substitute text based on a list of substitutions.
        Parameters:
            text: str: The text to substitute.
            substitutions: list[list[str]]: List of substitutions to make.
        '''
        for sub in substitutions['subs']:
            text = text.replace(sub[0], sub[1])
            text = text.replace(sub[0].replace('-', ' '), sub[1])
            text = text.replace(sub[0].replace('-', ' '), sub[1])
        for rem in substitutions['remove']:
            text = text.replace(rem, '')
        while '  ' in text:
            text = text.replace('  ', ' ')
        return text

    def format_for_matching(self):
        '''
        Function to format the text for matching.
        '''
        text = self.raw_text
        text = self.substitute(
            text,
            SUBSTITUTIONS[self.category]
        )
        self.year_present = extract_year_in_text(text)
        self.tuple_present = extract_card_tuple(text)
        self.number_present = [_ for _ in extract_numbers_in_text(text) if _ not in (
            self.tuple_present if self.tuple_present else []) and _ != (self.year_present if self.year_present else '')]
        self.grades_present = extract_grades_in_text(text)
        for grade in self.grades_present:
            for grade2 in self.grades_present:
                if grade != grade2:
                    text = text.replace(f'- {grade}/{grade2}', '')
                    text = text.replace(f'-{grade}/{grade2}', '')
                    text = text.replace(f'{grade}/{grade2}', '')
        for grade in self.grades_present:
            text = " ".join(
                [word for word in text.split(' ') if word != grade])
        included_attrs = {
            'year': self.year_present,
            'tuple': self.tuple_present,
            'grades': self.grades_present
        }
        self.included_attrs = {k: bool(v) for k, v in included_attrs.items()}
        self.sterile_text = remove_extra_spacing(text)

    def match(self):
        '''
        Matches the text with the list of options and returns the response.

        This method performs the matching process by first formatting the text for matching,
        then gathering the options to be matched against. It uses the string_match function
        to find the best matches for the text among the options. Finally, it builds the response
        based on the matches, cross-referenced options, and original options.

        Returns:
            The response containing the best matches for the given text.

        '''
        self.format_for_matching()
        cross_ref_options, options = self._gather_options()
        matches = string_match(self.sterile_text, options, limit=10)
        response = self._build_response(matches, cross_ref_options, options)
        return response

    def _gather_options(self):
        '''
        Gathers the available options for matching cards.

        This method iterates over the data and extracts the values for each card in each series.
        It then creates a list of cross-reference options and a list of options by joining the extracted values.
        
        Returns:
            cross_ref_options (list): A list of tuples representing the indices of the series and items.
            options (list): A list of strings representing the extracted values joined together.
        '''
        options = []
        cross_ref_options = []
        for series_index, series in enumerate(self.data):
            for item_index, item in enumerate(series['prints']):
                vals = self._extract_vals(series, item)
                cross_ref_options.append((series_index, item_index))
                options.append(' '.join([str(val) for val in vals]))
        return cross_ref_options, options

    def _extract_vals(self, series, item):
        '''
        Extracts attribute values from the given series and item.

        Parameters:
            series (dict): The series dictionary containing card attributes.
            item (dict): The item dictionary containing card attributes.

        Returns:
            list: A list of extracted attribute values.
        '''
        vals = []
        if self.included_attrs['year'] and series.get('year'):
            vals.append(series['year'])
        if self.included_attrs['tuple'] and item.get('number'):
            vals.append(item['number'])
        if series.get('total_cards'):
            total_cards_str = str(series.get('total_cards'))
            base_str = str(series.get('total_base', '***'))
            vals.append(
                series['total_base'] if base_str in self.tuple_present else series['total_cards'])
        for k in ['name', 'rarity']:
            if item.get(k):
                vals.append(item[k])
        vals.append(series['name'])
        return vals

    def _build_response(self, matches, cross_ref_options, options):
        '''
        Builds the response based on the matches, cross-reference options, and original options.
        Parameters:
            matches (list): A list of tuples representing the matches.
            cross_ref_options (list): A list of tuples representing the indices of the series and items.
            options (list): A list of strings representing the extracted values joined together.
        '''
        response = []
        for match in matches:
            series_idx, card_idx = cross_ref_options[options.index(match[0])]
            series_min = self.data[series_idx].copy()
            del series_min['prints']
            response.append({
                'series': series_min,
                'card': self.data[series_idx]['prints'][card_idx],
                'score': match[1]
            })
        return response


SUBSTITUTIONS = {
    "pokemon": {
        "subs": [
            ["Non-Holo", "Common"]
        ],
        "remove": ["WOTC", "Pokemon Card", "Pokemon", "Card"]
    },
    'magic': {
        'subs': [],
        'remove': ['Card', 'Magic: The Gathering', 'Magic The Gathering']
    },
    'funko': {
        'subs': [],
        'remove': ['Funko Pop!', 'Funko Pop', 'Funko', 'Pop']
    }
}
# Path: CardIdentifier/load.py