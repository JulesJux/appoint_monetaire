def liste_des_n(monnaie):
    list = []
    for i in range(monnaie+1):
        list.append(i)
    return list



def choix_objets (monnaie, systeme, val):

    DEBUG_decomposition = []
    appoint = []
    i=0
    DEBUG_total=0

    while i < len(systeme) and monnaie != 0:
        piece = systeme[i]

        for n in range(monnaie+1):
            if piece*n in val:
                appoint.append(piece*n)

        while monnaie - piece >= 0:
            monnaie -= piece
            DEBUG_decomposition.append(piece)
            DEBUG_total += piece

        i += 1
    print("total:" + str(DEBUG_total) + "decomposition:" + str(DEBUG_decomposition))
    return appoint, DEBUG_total, DEBUG_decomposition

def appoint(monnaie, systeme):
    list = []
    val = liste_des_n(monnaie)
    while systeme:
        x = choix_objets(monnaie, systeme, val)
        list.append(x[0])
        del systeme[0]
        """ if x[1] != 10:
      while sum(x[2]) != 10:
          for i in systeme:
              x[2].append(i)

          for n in range(monnaie+1):
              for j in range(len(x[2])):
                  if x[2][j]*n in val:
                      x[0].append(x[2][j]*n)
"""

    result = set(list[0])
    for s in list[1:]:
        result.intersection_update(s)

    return sorted(result)
