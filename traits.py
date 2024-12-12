class TraitsManager:
    """Gère les traits et les races associées."""

    def _init_(self):
        self.races = {
            "Labrador Retriever": ["amical", "joueur", "familial"],
            "Berger Allemand": ["intelligent", "protecteur", "travailleur"],
            "Caniche": ["intelligent", "élégant", "actif"],
            "Bulldog": ["calme", "affectueux", "paresseux"],
            "Husky Sibérien": ["énergique", "indépendant", "endurant"],
            "Chihuahua": ["vigilant", "affectueux", "courageux"],
            "Golden Retriever": ["loyal", "doux", "amical"]
        }

    def trouver_race(self, traits_selectionnes):
        """
        Trouve la ou les races correspondant le mieux aux traits sélectionnés.
        
        :param traits_selectionnes: Liste de traits sélectionnés.
        :return: Liste des races avec le meilleur score.
        """
        meilleures_races = []
        meilleur_score = 0

        for race, traits in self.races.items():
            score = len(set(traits) & set(traits_selectionnes))
            if score > meilleur_score:
                meilleures_races = [race]
                meilleur_score = score
            elif score == meilleur_score:
                meilleures_races.append(race)

        return meilleures_races