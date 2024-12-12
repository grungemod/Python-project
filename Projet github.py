import tkinter as tk
from tkinter import messagebox

# Données des races et leurs traits
RACES = {
    "Labrador Retriever": ["amical", "joueur", "familial"],
    "Berger Allemand": ["intelligent", "protecteur", "travailleur"],
    "Caniche": ["intelligent", "élégant", "actif"],
    "Bulldog": ["calme", "affectueux", "paresseux"],
    "Husky Sibérien": ["énergique", "indépendant", "endurant"],
    "Chihuahua": ["vigilant", "affectueux", "courageux"],
    "Golden Retriever": ["loyal", "doux", "amical"]
}

def trouver_race(traits_selectionnes):
    """
    Trouve la ou les races correspondant le mieux aux traits sélectionnés.
    
    :param traits_selectionnes: Liste de traits sélectionnés par l'utilisateur.
    :return: Liste des races avec le meilleur score.
    """
    meilleures_races = []
    meilleur_score = 0
    
    for race, traits in RACES.items():
        score = len(set(traits) & set(traits_selectionnes))
        if score > meilleur_score:
            meilleures_races = [race]
            meilleur_score = score
        elif score == meilleur_score:
            meilleures_races.append(race)
    
    return meilleures_races

def soumettre(checkboxes):
    """
    Récupère les traits sélectionnés et affiche les résultats dans une boîte de dialogue.
    """
    traits_selectionnes = [
        trait for trait, var in checkboxes.items() if var.get()
    ]
    
    if not traits_selectionnes:
        messagebox.showinfo("Erreur", "Veuillez sélectionner au moins un trait !")
        return
    
    races = trouver_race(traits_selectionnes)
    races_str = ", ".join(races)
    messagebox.showinfo("Résultat", f"Race(s) adaptée(s) : {races_str}")

def create_interface():
    """
    Crée et lance l'interface graphique pour sélectionner les traits et afficher les résultats.
    """
    fenetre = tk.Tk()
    fenetre.title("Trouver la race de chien idéale")

    label = tk.Label(fenetre, text="Sélectionnez les traits de caractère désirés :", font=("Arial", 14))
    label.pack(pady=10)

    checkboxes = {}
    for trait in set(trait for traits in RACES.values() for trait in traits):
        var = tk.BooleanVar()
        checkbox = tk.Checkbutton(fenetre, text=trait, variable=var, font=("Arial", 12))
        checkbox.pack(anchor="w")
        checkboxes[trait] = var

    bouton = tk.Button(fenetre, text="Soumettre", command=lambda: soumettre(checkboxes), font=("Arial", 12))
    bouton.pack(pady=10)

    fenetre.mainloop()

# Lancement de l'application
# if _name_ == "_main_":
create_interface()