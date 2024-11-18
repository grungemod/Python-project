# src/dog_breed_suggester/gui.py
import tkinter as tk
from tkinter import messagebox
from dog_breed_suggester.logic import trouver_race

def lancer_application():
    """Lance l'interface graphique."""
    fenetre = tk.Tk()
    fenetre.title("Trouver la race de chien idéale")

    label = tk.Label(fenetre, text="Sélectionnez les traits de caractère désirés :", font=("Arial", 14))
    label.pack(pady=10)

    checkboxes = {}
    traits_disponibles = {"amical", "joueur", "familial", "intelligent", "protecteur",
                          "travailleur", "calme", "affectueux", "paresseux", "énergique",
                          "indépendant", "endurant", "vigilant", "courageux"}
    for trait in traits_disponibles:
        var = tk.BooleanVar()
        checkbox = tk.Checkbutton(fenetre, text=trait, variable=var, font=("Arial", 12))
        checkbox.pack(anchor="w")
        checkboxes[trait] = var

    def soumettre():
        traits_selectionnes = [trait for trait, var in checkboxes.items() if var.get()]
        if not traits_selectionnes:
            messagebox.showinfo("Erreur", "Veuillez sélectionner au moins un trait !")
            return
        races = trouver_race(traits_selectionnes)
        races_str = ", ".join(races)
        messagebox.showinfo("Résultat", f"Race(s) adaptée(s) : {races_str}")

    bouton = tk.Button(fenetre, text="Soumettre", command=soumettre, font=("Arial", 12))
    bouton.pack(pady=10)

    fenetre.mainloop()
