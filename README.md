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

## About
Simpler, non-ML, and local version of BiDR TV's collectibles classifier. More collectible categories are planned.

#### Current Available Brands:
-   Magic: The Gathering
-   Pokemon
-   Funko (partial)

#### Planned:
- One Piece
- Yu-Gi-Oh

## TO-DO
- Threaded matching
- Grading extraction

## Issues/Info

If you have any suggestions or questions don't hestitate to open an issue.
