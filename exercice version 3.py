import os, time, shutil, random
from datetime import datetime

while True:
    dossier_photos = input(f"Bonjour ! Pour ranger vos photos par date de prise de vue dans des dossiers, veuillez écrire le chemin complet vers le dossier en question : \n-> ")
    if os.path.isdir(dossier_photos):
        print(f"Le chemin '{dossier_photos}' est un dossier valide.")
        break
    else:
        print("Le chemin saisi n'est pas valide. Veuillez réessayer.")

while True:
    lieu_copie = input(f"Une copie de votre dossier {dossier_photos} va également être effectuée, veuillez écrire le chemin complet vers la destination voulue pour la copie : \n-> ")
    if os.path.isdir(lieu_copie):
        print(f"Le chemin '{lieu_copie}' est un dossier valide.")
        break
    else:
        print("Le chemin saisi n'est pas valide. Veuillez réessayer.")

dossier = dossier_photos
chemin_dest = lieu_copie

nombre = random.randint(1, 99)
nom_dossier_source = os.path.basename(dossier)
nom_dossier_apres = f"{nom_dossier_source} - Copie {nombre}"
chemin_complet_dest = os.path.join(chemin_dest, nom_dossier_apres)
try:
    shutil.copytree(dossier, chemin_complet_dest, dirs_exist_ok=True, copy_function=shutil.copy2)
    print(f"Dossier copié avec succès de {dossier} vers {chemin_dest}")
except FileExistsError:
    print(f"Le dossier {chemin_dest} existe déjà.")
except FileNotFoundError:
    print(f"Le dossier source {dossier} n'existe pas.")
except Exception as e:
    print(f"Une erreur est survenue : {e}")

extensions = ['.png', '.jpg', '.jpeg']

for fichier in os.listdir(dossier):
    chemin = os.path.join(dossier, fichier)

    if os.path.isfile(chemin) and os.path.splitext(fichier)[1].lower() in extensions:
        infos = os.stat(chemin)

        date_creation = datetime.fromtimestamp(infos.st_ctime).strftime('%d.%m.%Y')
        date_modif = datetime.fromtimestamp(infos.st_mtime).strftime('%d.%m.%Y')

        print(f"Propriétés du fichier {fichier} :")
        print(f"  - Date de création       : {date_creation}")
        print(f"  - Date de modification   : {date_modif}")
        print('-' * 40)

        nom_dossier = date_creation
        chemin_crea_dossier = os.path.join(chemin_complet_dest,  nom_dossier)
    else:
        print(f"Le fichier {fichier} n'a pas les bonnes extensions, il est donc ignoré.")

for fichier in os.listdir(dossier):
    if os.path.isfile(chemin) and os.path.splitext(fichier)[1].lower() in extensions:
        try:
            os.makedirs(chemin_crea_dossier, exist_ok=False)
            print(f"Dossier créé : {chemin_crea_dossier}")
        except FileExistsError:
            print(f"Le dossier {dossier} existe déjà.")
        except OSError as e:
            print(f"Erreur : {e}")
                
        destination = rf'{chemin_dest}\{nom_dossier_apres}'
        fichier = rf'{chemin_dest}\{nom_dossier_apres}\{fichier}'
        print(f"fichier -> {fichier}")
        nouveau_dossier = os.path.join(destination, os.path.basename(dossier))
        try:
            shutil.move(fichier, chemin_crea_dossier)
            print(f"Fichier {fichier} déplacé avec succès vers : {nouveau_dossier}")
        except FileNotFoundError:
            print(f"Le fichier ou le dossier {fichier} destination n'existe pas.")
        except PermissionError:
            print(f"Permission refusée pour le fichier {fichier}.")
        except Exception as e:
            print(f"Une erreur est survenue : {e}")
    else:
        print(f"Le fichier {fichier} n'a pas les bonnes extensions, il est donc ignoré.")