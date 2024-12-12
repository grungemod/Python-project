import unittest
from Source.traits import TraitsManager

class TestTraitsManager(unittest.TestCase):
    def setUp(self):
        self.manager = TraitsManager()

    def test_trouver_race(self):
        result = self.manager.trouver_race(["amical", "joueur"])
        self.assertIn("Labrador Retriever", result)

# if _name_ == "_main_":
unittest.main()