import unittest
from unittest.mock import patch
import sys
import os
# Ajoute le chemin à l'arborescence
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Source.interface import Interface

class TestInterface(unittest.TestCase):
    def test_create_interface(self):
        """Test pour vérifier que create_interface est appelée correctement."""
        with patch("Source.interface.tk.Tk") as MockTk:
             mock_tk_instance = MockTk.return_value
             self.interface = Interface()
             fenetre = self.interface.create_interface()
             self.assertEqual(fenetre, mock_tk_instance)


