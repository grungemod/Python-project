import unittest
from unittest.mock import patch, MagicMock
import sys
import os
import pytest
# Ajoute le chemin à l'arborescence
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Source.interface import Interface

class TestInterface(unittest.TestCase):
    @pytest.fixture
    def interface():
        return Interface()
    
    def test_create_interface(self):
        """Test pour vérifier que create_interface est appelée correctement."""
        with patch("Source.interface.tk.Tk") as MockTk:
             mock_tk_instance = MockTk.return_value
             self.interface = Interface()
             fenetre = self.interface.create_interface()
             self.assertEqual(fenetre, mock_tk_instance)

    # Test de la soumission avec des traits sélectionnés
    @patch('tkinter.messagebox.showinfo')
    def test_soumettre_selection_avec_traits(interface, mock_showinfo):
        # Mock des checkboxes
        checkbox_mock = {
        "force": MagicMock(get=lambda: True),
        "vitesse": MagicMock(get=lambda: False),
        }

        interface.soumettre(checkbox_mock)

        mock_showinfo.assert_called_once_with("Résultat", "Race(s) adaptée(s) : force")

    # Test sans sélectionner aucun trait
    @patch('tkinter.messagebox.showinfo')
    def test_soumettre_sans_traits_selectionnes(interface, mock_showinfo):
        checkbox_mock = {
        "force": MagicMock(get=lambda: False),
        "vitesse": MagicMock(get=lambda: False),
        }

        interface.soumettre(checkbox_mock)

        mock_showinfo.assert_called_once_with("Erreur", "Veuillez sélectionner au moins un trait !")


