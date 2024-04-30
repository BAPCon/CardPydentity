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

CardPydentitier.Build("SQUIRTLE - 1999 WOTC Pokemon Card 63/102 Non Holo - LP/MP")

{
    "id": "base1-63",
    "name": "Squirtle",
    "number": "63",
    "rarity": "Common",
    "set": "base1"
}
```

```python
from cardpydentity import CardPydentitier

bd = CardPydentitier()
card = bd.Build('PSA 10 Luffy Nika Gear 5 OP05-119 Parallel SEC New Era One Piece Card Japanese')
print(card)

>>> {'series': {'name': 'Booster Pack Awakening of the New Era'}, 'card': {'name': 'Monkey.D.Luffy', 'set': 'Booster Pack Awakening of the New Era', 'number': 'OP05-119', 'type': 'Character - the four emperors/straw hat crew strike'}, 'score': 60, 'match': 'OP05-119 Monkey.D.Luffy Booster Pack Awakening of the New Era'}
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
