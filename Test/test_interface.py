import unittest
from unittest.mock import patch
from Source.interface import Interface

class TestInterface(unittest.TestCase):
    def test_create_interface(self):
        """Test pour vérifier que create_interface est appelée correctement."""
        with patch("Source.interface.tk.Tk") as MockTk:
            mock_tk_instance = MockTk.return_value
            self.interface = Interface()
            fenetre = self.interface.create_interface()
            self.assertEqual(fenetre, mock_tk_instance)
