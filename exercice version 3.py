import os, time, shutil, random, asyncio
from datetime import datetime

nombre = random.randint(1, 99)
copie = f"- Copie {nombre}"

message = {"exit" : "Le processus a été arrêté avec succès."}
extensions_photos = ['.png', '.jpg', '.jpeg']

def contient_photos(dossier):
    for fichier in os.listdir(dossier):
        if os.path.splitext(fichier)[1].lower() in extensions_photos:
            return True
    return False

print('-' * 40)

chemin_dossier = input("Bonjour, vous souhaitez ranger vos photos dans des dossiers par date de prise de vue ?\nAlors vous êtes au bon endroit !\n Veuillez entrer le chemin complet vers le dossier en question : \n-> ")
if os.path.isdir(chemin_dossier):
    print(f"Le chemin '{chemin_dossier}' est un dossier valide.")
    if contient_photos(chemin_dossier):
        print(f"Vous avez choisi le chemin '{chemin_dossier}'")
        reponse = input(f"Est-ce que le chemin est correct ? (o / n) : \n-> ")
        if reponse == "o" or reponse == "oui" or reponse == "y" or reponse == "yes":
            print(f"Chemin '{chemin_dossier}' confirmé.")
                
            nom_dossier_source = os.path.basename(chemin_dossier)
            nom_copie = f"{nom_dossier_source} {copie}"
            print(f"Une copie du dossier '{nom_dossier_source}' va être effectuée sous le nom '{nom_copie}'.")
            chemin_copie = input("Où souhaitez-vous mettre cette copie ? \n-> ")
            if os.path.isdir(chemin_copie):
                print(f"Le chemin '{chemin_copie}' est un dossier valide.")
                reponse = input(f"Est-ce que le chemin est correct ? (o / n) : \n-> ")
                if reponse == "o" or reponse == "oui" or reponse == "y" or reponse == "yes":
                    print(f"Chemin '{chemin_dossier}' confirmé.")