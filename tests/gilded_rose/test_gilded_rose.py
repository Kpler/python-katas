from approvaltests.approvals import verify

from src.gilded_rose.guilded_rose import Item, GildedRose


def test_update_quality():
    items=[]
    for i in range(60):
        for j in range(60):
            items.append(Item("Aged Brie", i, j))
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    verify(items)

