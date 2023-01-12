from unittest import TestCase

import pytest
from src.gilded_rose.guilded_rose import Item, GildedRose
import unittest
from approvaltests import verify, verify_all_combinations


class TestGildedRose(unittest.TestCase):
  def test_gilded_rose(self):
    i = Item('name', 0, 0)
    self.assertEquals(i.name, 'name')

  def test_approval_gilded_rose(self):
    i = Item('name', 0, 0)
    verify(i.name)

  def test_update_quality(self):
    i = Item('test_1', 0, 0)
    j = Item('test_2', 1, 1)
    gr = GildedRose([i, j])
    self.assertEquals(gr.items[0].name, "test_1")
    self.assertEquals(gr.items[1].name, "test_2")

  def test_combo_guilded_rose(self):
    ...