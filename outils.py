from affichage import *


def liste_des_n(monnaie):
    list = []
    for i in range(monnaie + 1):
        list.append(i)
    return list


def choix_objets(monnaie, systeme, val, systeme_initial):
    decomposition = []
    appoint = []
    temp = []
    monnaie_initiale = monnaie
    total = 0
    precision = 10
    piece_bonus = 0
    nbr_de_piece_bonus = 0
    piece = systeme[0]

    for n in range(monnaie + 1):
        if piece * n in val:
            appoint.append(piece * n)

    while monnaie - piece >= 0:
        monnaie -= piece
        decomposition.append(piece)
        total += piece

    if total != monnaie_initiale and monnaie_initiale >= piece:
        for n in appoint:
            for j in systeme_initial:
                for i in range(precision):
                    if total + j * i == monnaie_initiale:
                        n += 1
                        temp.append(n + j - 1)
                        if i > 1:
                            for l in range(i):
                                temp.append(n + l)
                        piece_bonus = j
                        nbr_de_piece_bonus = i

        for k in set(temp):
            appoint.append(k)

        appoint.sort()
        afficher_appoints_bonus(decomposition, systeme, nbr_de_piece_bonus, piece_bonus, appoint)

    if total == monnaie_initiale:
        afficher_appoints(decomposition, systeme, appoint)

    return appoint
