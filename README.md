# CardPydentity

![PyPI - Version](https://img.shields.io/pypi/v/cardpydentity)

Python package for identifying Pokemon/MTG cards from auction titles.   

## Installing

```
pip install cardpydentity
```

## Use

```python   
from cardpydentity import CardPydentitier

card = CardPydentitier().Build("SQUIRTLE - 1999 WOTC Pokemon Card 63/102 Non Holo - PSA 9.5)"
>>> {'series': {'id': 'base1', 'name': 'Base', 'series': 'Base', 'year': '1999', 'total_cards': 102, 'total_base': 102}, 'card': {'id': 'base1-63', 'name': 'Squirtle', 'number': '63', 'rarity': 'Common', 'set': 'base1'}, 'score': 92, 'match': '1999 63 102 Squirtle Common Base', 'grading': {'grade': 9.5, 'type': 'PSA'}}


card = CardPydentitier().Build("Yugioh x1 Dark Magician TN23-EN001 Quarter Century Secret Rare Lim Ed(Near Mint))"
>>> {'series': {'name': '25th Anniversary Tin: Dueling Heroes', 'abbrv': ['TN23']}, 'card': {'name': 'Dark Magician (Quarter Century Secret Rare)', 'set_name': '25th Anniversary Tin: Dueling Heroes', 'rarity': 'Quarter Century Secret Rare', 'number': 'EN001', 'abbrv': 'TN23'}, 'score': 84, 'match': 'EN001 Dark Magician (Quarter Century Secret Rare) Quarter Century Secret Rare TN23 25th Anniversary Tin: Dueling Heroes', 'grading': {'grade': "Near Mint", 'type': None}}


card = CardPydentitier().Build("PSA 10 Luffy Nika Gear 5 OP05-119 Parallel SEC New Era One Piece Card Japanese)"
>>> {'series': {'name': 'Booster Pack Awakening of the New Era'}, 'card': {'name': 'Monkey.D.Luffy', 'set': 'Booster Pack Awakening of the New Era', 'number': 'OP05-119', 'type': 'Character - the four emperors/straw hat crew strike'}, 'score': 60, 'match': 'OP05-119 Monkey.D.Luffy Booster Pack Awakening of the New Era', 'grading': {'grade': 10, 'type': 'PSA'}}

```

## About
Simpler, non-ML, and local version of collectibles classifier. More collectible categories are planned. 

A Python package that allows collectibles and trading cards to be identified and parsed from the title of a listing on eBay or any other retailers. Currently uses [fuzzymatching](https://en.wikipedia.org/wiki/Approximate_string_matching) and a master list of over 135,000 Pokemon and Magic: The Gathering cards.

#### Current Available Brands:
-   Magic: The Gathering
-   Pokemon
-   One Piece
-   Yu-Gi-Oh

#### Planned:
- Funko Pop!

## TO-DO
- Threaded matching
- Grading extraction

## Issues/Info

If you have any suggestions or questions don't hestitate to open an issue.
