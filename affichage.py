def afficher_appoint(result):
    print("On est donc sûr d'avoir l'appoint pour les prix : " + str(sorted(result)))


def afficher_appoints_bonus(decomposition, systeme, nbr_de_piece_bonus, piece_bonus, appoint):
    print("Les valeurs pour lesquelles l'appoint est possible pour " + str(len(decomposition)) + " piece(s) de " + str(systeme[0]) + " et " + str(nbr_de_piece_bonus) + " piece(s) de " + str(piece_bonus) + " sont : " + str(appoint))


def afficher_appoints(decomposition, systeme, appoint):
    print("Les valeurs pour lesquelles l'appoint est possible pour " + str(len(decomposition)) + " piece(s) de " + str(systeme[0]) + " sont : " + str(appoint))


def afficher_s_primaire(is_s_primaire, systeme, monnaie):
    if is_s_primaire:
        print("Pour le système " + str(systeme) + ", le prix " + str(monnaie) + " est S-primaire.")
    else:
        print("Pour le système " + str(systeme) + ", le prix " + str(monnaie) + " n'est pas S-primaire.")