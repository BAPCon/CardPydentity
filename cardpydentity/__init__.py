import json
from .load import get_app_path, register_source, try_fetch_data
from .matcher import Matcher

APP_NAME = 'CardIdentifier'
__version__ = "0.1.0"

JSON_FILES = (
    ('pokemon', 'https://bidrpublicfiles.s3.amazonaws.com/pokemon.json'),
    ('magic',   'https://bidrpublicfiles.s3.amazonaws.com/mtg.json')
)

SOURCES_REGISTERED = False

class CardPydentitier:
    '''
    The CardPydentitier class is responsible for identifying cards based on given text and category.

    It provides a `Build` method that takes a text and an optional category as input and returns a Matcher object.

    Attributes: 
        None

    Methods:
        __init__(): Initializes the CardPydentitier object and registers the sources if not already registered.
        __register_sources__(): Registers the sources by calling the `register_source` function for each JSON file.
        __load_app_data__(url: str, file_name: str): Loads the app data from the given URL and file name.
        Build(text: str, category: str = None): Builds a Matcher object based on the given text and category.

    Example usage:
        card_identifier = CardPydentitier()
        matcher = card_identifier.Build("Some text", "Some category")
    '''

    def __init__(self):
        global SOURCES_REGISTERED
        if not SOURCES_REGISTERED:
            self.__register_sources__()
            SOURCES_REGISTERED = True

    def __register_sources__(self):
            '''
            Register the sources by calling the `register_source` function for each JSON file.
            '''
            for name, url in JSON_FILES:
                register_source(
                    name, 
                    CardPydentitier.__load_app_data__, 
                    {'url': url, 'file_name': f"{name}.json"}
                )

    def __load_app_data__(url: str, file_name: str):
        '''
        Load the app data from the given URL and file name.
        '''
        global APP_NAME
        data_path = get_app_path(APP_NAME, file_name, 'data')
        try_fetch_data(url, data_path)
        response = open(data_path, 'rb').read().decode('utf-8')
        if file_name.endswith('.json'):
            return json.loads(response)
        return response
            
    def Build(self, text: str, category: str = None) -> dict:
        '''
        Builds a matcher object and performs matching on the given text.

        Args:
            text (str): The text to be matched.
            category (str, optional): The category of the text. Defaults to None.

        Returns:
            dict: The matched result.
        '''
        matcher = Matcher(text, category)
        matcher.format_for_matching()
        return matcher.match()[0]