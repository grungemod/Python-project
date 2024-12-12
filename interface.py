import tkinter as tk
from tkinter import messagebox
from .traits import TraitsManager

class Interface:
    """Gère l'interface graphique."""

    def _init_(self):
        self.manager = TraitsManager()

    def soumettre(self, checkboxes):
        """
        Récupère les traits sélectionnés et affiche les résultats.
        """
        traits_selectionnes = [
            trait for trait, var in checkboxes.items() if var.get()
        ]

        if not traits_selectionnes:
            messagebox.showinfo("Erreur", "Veuillez sélectionner au moins un trait !")
            return

        races = self.manager.trouver_race(traits_selectionnes)
        races_str = ", ".join(races)
        messagebox.showinfo("Résultat", f"Race(s) adaptée(s) : {races_str}")

    def create_interface(self):
        """
        Crée et lance l'interface graphique.
        """
        fenetre = tk.Tk()
        fenetre.title("Trouver la race de chien idéale")

        label = tk.Label(fenetre, text="Sélectionnez les traits de caractère désirés :", font=("Arial", 14))
        label.pack(pady=10)

        checkboxes = {}
        for trait in set(trait for traits in self.manager.races.values() for trait in traits):
            var = tk.BooleanVar()
            checkbox = tk.Checkbutton(fenetre, text=trait, variable=var, font=("Arial", 12))
            checkbox.pack(anchor="w")
            checkboxes[trait] = var

        bouton = tk.Button(fenetre, text="Soumettre", command=lambda: self.soumettre(checkboxes), font=("Arial", 12))
        bouton.pack(pady=10)

        fenetre.mainloop()