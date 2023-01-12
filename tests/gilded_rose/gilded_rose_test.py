from unittest import TestCase

import pytest
from src.gilded_rose.guilded_rose import Item
import unittest
from approvaltests import verify


class TestGildedRose(unittest.TestCase):
  def test_gilded_rose(self):
    i = Item('name', 0, 0)
    self.assertEquals(i.name, 'something')

  def test_approval_gilded_rose(self):
    i = Item('name', 0, 0)
    verify(i.name)

  def test_update_quality(self):
    i = Item('test_1', 0, 0)
    j = Item('test_2', 1, 1)

