#import unittest
#from Source.interface import Interface

#class TestInterface(unittest.TestCase):
 #   def setUp(self):
  #      """Initialisation avant chaque test."""
   #     self.interface = Interface()

    #def test_create_interface(self):
     #   """Test pour s'assurer que l'interface est créée correctement."""
      #  try:
       #     self.interface.create_interface()
        #except Exception as e:
          #  self.fail(f"create_interface() a levé une exception : {e}")

    #def test_interface_type(self):
     #   """Test pour vérifier que l'interface est de type attendu."""
      #  self.assertIsInstance(self.interface, Interface)

# if _name_ == "_main_":
#unittest.main()
import unittest
from unittest.mock import patch
from Source.interface import Interface

class TestInterface(unittest.TestCase):
    def test_create_interface(self):
        """Test pour s'assurer que l'interface est créée correctement."""
        with patch("Source.interface.tk.Tk") as MockTk:
            # Créer une instance simulée de Tk
            mock_tk_instance = MockTk.return_value
            mock_tk_instance.mainloop = lambda: None  # Simule la méthode mainloop() sans la faire tourner

            # Appeler la méthode create_interface() sans réellement créer la fenêtre
            self.interface = Interface()
            self.interface.create_interface()

            # Vérifier que Tk() a bien été appelé
            MockTk.assert_called_once()
