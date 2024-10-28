#Fonctionne

import os, time, shutil, random
from datetime import datetime

#Chemin vers le dossier sélectionné.
dossier = r'C:\Users\peran\OneDrive\Documents\TEST\Annaïg enfant'
chemin_dest = r'C:\Users\peran\OneDrive\Documents\TEST'

nombre = random.randint(1, 99)
nom_dossier_source = os.path.basename(dossier)
nom_dossier_apres = f"{nom_dossier_source} - Copie {nombre}"
chemin_complet_dest = os.path.join(chemin_dest, nom_dossier_apres)
print(f"chemin_complet_dest -> {chemin_complet_dest}")
#Crée une copie du dossier sélectionné, au cas où.
try:
    shutil.copytree(dossier, chemin_complet_dest, dirs_exist_ok=True, copy_function=shutil.copy2)
    print(f"Dossier copié avec succès de {dossier} vers {chemin_dest}")
except FileExistsError:
    print(f"Le dossier {chemin_dest} existe déjà.")
except FileNotFoundError:
    print(f"Le dossier source {dossier} n'existe pas.")
except Exception as e:
    print(f"Une erreur est survenue : {e}")

#Filtre les fichiers, pour ne s'occuper que des fichiers avec les extensions demandées.
extensions = ['.png', '.jpg', '.jpeg']

contenu = os.listdir(dossier)

#Liste les fichiers contenus dans le dossier sélectionné.
for fichier in os.listdir(dossier):
    chemin = os.path.join(dossier, fichier)

    #Vérifie que c'est bien un fichier avec les bonnes extensions.
    if os.path.isfile(chemin) and os.path.splitext(fichier)[1].lower() in extensions:
        infos = os.stat(chemin)

        #Affiche les dates de création et de modification des fichiers.
        date_creation = datetime.fromtimestamp(infos.st_ctime).strftime('%d.%m.%Y')
        date_modif = datetime.fromtimestamp(infos.st_mtime).strftime('%d.%m.%Y')

        #Affiche les métadonnées des fichiers contenus dans le dossier sélectionné.
        print(f"Propriétés du fichier {fichier} :")
        print(f"  - Date de création       : {date_creation}")
        print(f"  - Date de modification   : {date_modif}")
        print('-' * 40)

        #Récupère la date de création du fichier pour pouvoir créer le dossier.
        nom_dossier = date_creation
        chemin_crea_dossier = os.path.join(chemin_complet_dest,  nom_dossier)
        print(f"chemin_crea_dossier -> {chemin_crea_dossier}")
    else:
        print(f"Le fichier {fichier} n'a pas les bonnes extensions, il est donc ignoré.")

#Crée un dossier avec comme nom la date de création de l'image.
#Si un dossier avec la date de l'image existe déjà, alors il n'en crée pas un nouveau.
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