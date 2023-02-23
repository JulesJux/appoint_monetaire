from outils import *
from affichage import *


def appoint(monnaie, systeme):
    list = []
    val = liste_des_n(monnaie)
    systeme_initial = tuple(systeme)
    while systeme:
        x = choix_objets(monnaie, systeme, val, systeme_initial)
        if x != [0]:
            list.append(x)

        del systeme[0]

    result = set(list[0])
    for s in list[1:]:
        result.intersection_update(s)
    # print(str(sorted(result)))
    return afficher_appoint(result)


def s_primaire(monnaie, systeme):
    is_s_primaire = False
    if len(systeme) == 2 and systeme[1] >= 2:
        if monnaie == systeme[1] or monnaie == 1:
            is_s_primaire = True
    return afficher_s_primaire(is_s_primaire, systeme, monnaie)
