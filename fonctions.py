from outils import *
from affichage import *


def appoint(monnaie, systeme):
    list_result = []
    val = liste_des_n(monnaie)
    systeme_initial = tuple(systeme)
    while systeme:
        x = choix_objets(monnaie, systeme, val, systeme_initial)
        if x != [0]:
            list_result.append(x)

        del systeme[0]

    result = set(list_result[0])
    for s in list_result[1:]:
        result.intersection_update(s)

    afficher_appoint(result)
    return list(result)


def s_primaire(monnaie, systeme):
    systeme_initial = tuple(systeme)
    is_s_primaire = False
    appoints = appoint(monnaie, systeme)
    if monnaie == appoints[1] and len(appoints) == 2:
            is_s_primaire = True
    return afficher_s_primaire(is_s_primaire, systeme_initial, monnaie)
