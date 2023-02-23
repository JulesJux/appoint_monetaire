def liste_des_n(monnaie):
    list = []
    for i in range(monnaie + 1):
        list.append(i)
    return list


def choix_objets(monnaie, systeme, val):
    decomposition = []
    appoint = []
    temp = []
    monnaie_initiale = monnaie
    total = 0
    precision = 10
    piece_bonus = 0
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
            for j in range(precision):
                if total + j == monnaie_initiale:
                    n += 1
                    temp.append(n + j - 1)
                    piece_bonus = j

        for k in temp:
            appoint.append(k)

        appoint.sort()
        print("Les valeurs pour lesquelles l'appoint est possible pour " + str(len(decomposition)) + " piece(s) de " + str(systeme[0]) + " et une piece de " + str(piece_bonus) + " sont : " + str(appoint))

    if total == monnaie_initiale:
        print("Les valeurs pour lesquelles l'appoint est possible pour " + str(len(decomposition)) + " piece(s) de " + str(systeme[0]) + " sont : " + str(appoint))

    return appoint, total, decomposition


def appoint(monnaie, systeme):
    list = []
    val = liste_des_n(monnaie)
    while systeme:
        x = choix_objets(monnaie, systeme, val)
        if x[0] != [0]:
            list.append(x[0])

        del systeme[0]

    result = set(list[0])
    for s in list[1:]:
        result.intersection_update(s)

    return "On est donc sur d'avoir l'appoint pour les prix : " + str(sorted(result))
