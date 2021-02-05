import json
import random

def create_program(number):
    """
    Création de la liste de projet
    """
    programs = [{"nom": f'Programme {i}', 'actif': random.choice([True, False])} for i in range(number)]
    return programs

def create_appartments(programs, number):
    """
    Création des appartements pour chaque projets dans la liste 'programs'
    """
    appartments = []
    caracteristiques = ["piscine", "balcon", "parking", "rez-de-jardin", "station ski"]

    for program in programs:
        for i in range(number):
            appartment = {
                    "surface": random.randint(15, 75),
                    "prix": random.randint(80000, 300000),
                    "nb_piece": random.randint(1,4),
                    "projet" : program['nom'],
                    "characteristiques" : [random.choice(caracteristiques),
                                            random.choice(caracteristiques)]
                }
            appartments.append(appartment)
    
    return appartments


if __name__ == '__main__':
    """
    Génération automatique de 20 projets immobilier et de 10 appartements pour chaque
    Les données obtenues sont sauvegardées dans le fichier sample.json
    """
    programs = create_program(10)
    appartments = create_appartments(programs, 20)

    data = {"projets" : programs, "appartements" : appartments}

    with open("sample.json", "w") as file:
        json.dump(data, file)
