HAND_OF_RAGNAROS = "Sulfuras, Hand of Ragnaros"
TAFKAL_ETC_CONCERT = "Backstage passes to a TAFKAL80ETC concert"
AGED_BRIE = "Aged Brie"


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name in {AGED_BRIE, TAFKAL_ETC_CONCERT}:
                self.increment_quality_when_below_50(item)
                if item.name == TAFKAL_ETC_CONCERT and item.quality < 50:
                    if item.sell_in < 11:
                        self.increment_quality_when_below_50(item)
                    if item.sell_in < 6:
                        self.increment_quality_when_below_50(item)
            elif item.name != HAND_OF_RAGNAROS and item.quality > 0:
                self.decrement_quality(item)

            if item.name != HAND_OF_RAGNAROS:
                self.decrement_sell_in(item)

            if item.sell_in < 0:
                if item.name == AGED_BRIE:
                    self.increment_quality_when_below_50(item)
                elif item.name == TAFKAL_ETC_CONCERT:
                    self.reset_quality(item)
                elif item.name != HAND_OF_RAGNAROS and item.quality > 0:
                    self.decrement_quality(item)


    def reset_quality(self, item):
        item.quality = 0

    def decrement_sell_in(self, item):
        item.sell_in = item.sell_in - 1

    def decrement_quality(self, item):
        item.quality = item.quality - 1

    def increment_quality_when_below_50(self, item):
        if item.quality < 50:
            item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
