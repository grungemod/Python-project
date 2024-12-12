import unittest
from Source.traits import TraitsManager

class TestTraitsManager(unittest.TestCase):
    def setUp(self):
        self.manager = TraitsManager()

    def test_add_trait(self):
        """Test pour ajouter et récupérer un trait."""
        self.manager.add_trait("force", 10)
        self.assertEqual(self.manager.get_trait("force"), 10)

    def test_get_nonexistent_trait(self):
        """Test pour récupérer un trait inexistant."""
        self.assertIsNone(self.manager.get_trait("vitesse"))
