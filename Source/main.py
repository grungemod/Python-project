import tkinter as tk
from Source.traits import TraitsManager
from Source.interface import Interface

def main():
    # Création du TraitsManager
    manager = TraitsManager()

    # Création de l'Interface en utilisant TraitsManager
    interface = Interface(manager)

    # Appel de la méthode pour créer l'interface graphique
    interface.create_interface()

# Point d'entrée du script principal
if __name__ == "__main__":
    main()
