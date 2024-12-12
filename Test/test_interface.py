import unittest
from Source.interface import Interface

class TestInterface(unittest.TestCase):
    def setUp(self):
        """Initialisation avant chaque test."""
        self.interface = Interface()

    def test_create_interface(self):
        """Test pour s'assurer que l'interface est créée correctement."""
        try:
            self.interface.create_interface()
        except Exception as e:
            self.fail(f"create_interface() a levé une exception : {e}")

    def test_interface_type(self):
        """Test pour vérifier que l'interface est de type attendu."""
        self.assertIsInstance(self.interface, Interface)

# if _name_ == "_main_":
#unittest.main()
