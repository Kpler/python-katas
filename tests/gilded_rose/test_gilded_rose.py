from approvaltests.approvals import verify

from src.gilded_rose.guilded_rose import Item, GildedRose


def test_update_quality():
    item = Item("TestItem1", 0, 0)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    verify(item)

