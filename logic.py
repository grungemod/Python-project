# src/dog_breed_suggester/logic.py

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
    """Trouve les races correspondant aux traits sélectionnés."""
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
