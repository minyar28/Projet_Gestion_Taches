print("=== GESTION DES TACHES ===")
taches = []
while True:
    print("\n1. ajouter une tache ")
    print("2. afficher les taches")
    print("3. recherche une tache")
    print("0. quitter")
    choix = input("votre choix : ")
    if choix == "1":
        nom = input("entrez le nom de la tache : ")
        taches.append(nom)
        print("tache ajoutée avec succès !")
    elif choix == "2":
        if len(taches) == 0:
            print("aucune tache disponible.")
        else:
            for i, tache in enumerate(taches, start=1):
                print(i, "-", tache)
    elif choix =="3":
        recherche = input("entrez le nom de la tache à recherche : ")
        if recherche in taches:
            print("tache trouvée !")
        else:
            print("tache introuvable.")
    elif choix =="0":
            print("au revoir !")
            break
    else:
            print("choix invalide, réessayez.")








