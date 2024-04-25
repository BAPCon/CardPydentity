from pathlib import Path
from appdirs import *
import requests
import json
import os


SOURCES = {}

def register_source(name, source: callable, args: dict = {}) -> None:
    '''
    Registers a source to the SOURCES dictionary
    Parameters:
        name: str: Name of the source
        source: callable: Function that takes a string and returns a list of dictionaries
    '''
    SOURCES[name] = {
        'function': source,
        'data': None,
        'args': args
    }

def get_source(name: str) -> list[dict]:
    '''
    Returns the data from a source
    Parameters:
        name: str: Name of the source
    '''
    if not SOURCES.get(name):
        raise ValueError(f"Source {name} not found.")
    if not SOURCES[name]['data']:
        SOURCES[name]['data'] = SOURCES[name]['function'](**SOURCES[name]['args'])
    return SOURCES.get(name)['data']

def local_source(path: str) -> list[dict]:
    '''
    Mocks a source with the given data
    Parameters:
        name: str: Name of the source
        data: list[dict]: Data to mock the source with
    '''
    print(f"Loading source from {path}")
    with open(path, 'r') as f:
        return json.load(f)
    
def get_app_path(app_name: str, file_name: str, storage_name: str = 'data') -> str:
    '''
    Returns the path to a file in the user's data directory
    '''
    return os.path.join(user_data_dir(app_name), storage_name, file_name)
    
def try_fetch_data(url: str, data_path: str | Path)     -> None:
    '''
    Downloads data from a URL if it doesn't exist
    '''
    if not os.path.exists(data_path):
        print("Downloading required data...", data_path)
        os.makedirs(os.path.dirname(data_path), exist_ok=True)
        response = requests.get(url)
        with open(data_path, 'wb') as data_file:
            data_file.write(response.content)