#!/usr/bin/python3
"""
This module contains unit tests for the Amenity class.
"""

from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """
    This class contains unit tests for the Amenity class.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a test instance of the Amenity class.
        """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """
        Test case to check the type of the 'name' attribute of a new Amenity instance.
        """
        new = self.value()
        self.assertEqual(type(new.name), str)
