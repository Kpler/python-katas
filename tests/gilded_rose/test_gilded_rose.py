from approvaltests.approvals import verify

from src.gilded_rose.guilded_rose import Item, GildedRose
from itertools import chain

NAMES = ("Aged Brie",
         "Backstage passes to a TAFKAL80ETC concert",
         "Sulfuras, Hand of Ragnaros",
         "",
         "Fake Name"
         )
def test_update_quality():
    items=[]
    for name in NAMES:
        for i in range(-10, 60):
            for j in range(-10, 60):
                items.append(Item(name, i, j))
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    verify(items)

