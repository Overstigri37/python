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
boucle = True
while boucle:
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

                        chemin_complet_copie = os.path.join(chemin_copie, nom_copie)
                        print(chemin_complet_copie)
                        print("Copie du dossier en cours...")
                        time.sleep(3)
                        try:
                            shutil.copytree(chemin_dossier, chemin_complet_copie, dirs_exist_ok=True, copy_function=shutil.copy2)
                            print(f"Dossier copié avec succès de {chemin_dossier} vers {chemin_complet_copie}")
                        except FileExistsError:
                            print(f"Le dossier {chemin_copie} existe déjà.")
                        except FileNotFoundError:
                            print(f"Le dossier source {chemin_copie} n'existe pas.")
                        except Exception as e:
                            print(f"Une erreur est survenue : {e}")

                        print("Le script va maintenant analyser les métadonnées des fichiers contenus dans le dossier pour récupérer les dates de prise de vue des photos.")
                        pret = input("Etes-vous toujours prêt ? (o / n) \n-> ")
                        if pret == "o" or pret == "oui" or pret == "y" or pret == "yes":
                            print(f"Parfait, le processus va pouvoir commencer...")

                            for fichier in os.listdir(chemin_dossier):
                                chemin_fichier = os.path.join(chemin_dossier, fichier)

                                if os.path.isfile(chemin_fichier) and os.path.splitext(fichier)[1].lower() in extensions_photos:
                                    infos = os.stat(chemin_fichier)
                                    date_creation = datetime.fromtimestamp(infos.st_ctime).strftime('%d.%m.%Y')
                                    date_modif = datetime.fromtimestamp(infos.st_mtime).strftime('%d.%m.%Y')

                                else:
                                    print(f"Le fichier {fichier} n'a pas les bonnes extensions, il est donc ignoré.")
                            time.sleep(3)
                            print("Analyse terminée.")
                            time.sleep(2)
                            print(f"Maintenant, des dossiers vont être créés en fonction des dates de prise de vue des photos contenues dans le dossier.")
                            partant = input(f"Toujours partant ? (o / n) : \n-> ")

                            if partant == "o" or partant == "oui" or partant == "y" or partant == "yes":
                                print("C'est ce que j'attendais ! Création des dossiers en cours...")
                                nom_dossier = date_creation
                                chemin_crea_dossier = os.path.join(chemin_dossier,  nom_dossier)

                                try:
                                    os.makedirs(chemin_crea_dossier, exist_ok=False)
                                    print(f"Dossier créé : {chemin_crea_dossier}")
                                except OSError as e:
                                    print(f"Erreur : {e}")
                                                
                                time.sleep(3)
                                print("Dernière étape ! Il ne reste plus qu'à déplacer les photos dans leurs dossiers de date de prise de vue respectifs.")
                                continuer = input("Continuer ? (o / n) : \n-> ")

                                if continuer == "o" or continuer == "oui" or continuer == "y" or continuer == "yes":
                                    print("C'est parti ! Déplacement des fichiers en cours...")
                                    fichier = os.path.join(chemin_dossier, fichier)

                                    nouveau_dossier = os.path.join(chemin_dossier, os.path.basename(chemin_dossier))
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

                                elif continuer == "exit":
                                    print(message["exit"])
                                    boucle = False
                                else:
                                    print(message["exit"])
                                    boucle = False
                            elif partant == "exit":
                                print(message["exit"])
                                boucle = False
                            else:
                                print(message["exit"])
                                boucle = False
                        elif pret == "exit":
                            print(message["exit"])
                            boucle = False
                        else:
                            print(message["exit"])
                            boucle = False
                    elif pret == "exit":
                        print(message["exit"])
                        boucle = False
                    else:
                        print("Réessayez...")
                elif chemin_copie == "exit":
                    print(message["exit"])
                    boucle = False
                else:
                    print("Le chemin saisi n'est past valide. Veuillez réessayer.")
            elif reponse == "exit":
                print(message["exit"])
                boucle = False
            else:
                print("Réessayez...")
        else:
            print(f"Le dossier '{chemin_dossier}' ne contient pas de photos, veuillez réessayer.")
    elif chemin_dossier == "exit":
        print(message["exit"])
        boucle = False
    else:
        print("Le chemin saisi n'est pas valide. Veuillez réessayer.")
boucle = False