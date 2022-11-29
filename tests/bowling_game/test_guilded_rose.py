from approvaltests.approvals import verify

from src.gilded_rose.guilded_rose import Item, GildedRose


def test_approval():
    items = [
        Item(name='Aged Brie', sell_in=1, quality=1),
    ]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    verify(gilded_rose.items)