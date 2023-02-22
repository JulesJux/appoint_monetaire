def appoint(systeme, monnaie):
    val = []
    appoint_ = []
    appoint1 = []
    appoint2 = []
    appoint3 = []
    appoint4 = []
    for i in range(len(systeme)):
        for x in range(monnaie+1):
            val.append(x)
            piece = systeme[i]
            tot = x * piece

            if piece == 1:
                for n in range(monnaie+1):
                    if piece*n in val:
                        appoint1.append(piece * n)
                            #print("1" + str(appoint1))

            if piece == 3:
                for n in range(monnaie+1):
                    if piece*n in val:
                        appoint2.append(piece * n)
                        print("2" + str(appoint2))

            if piece == 10:
                for n in range(monnaie+1):
                    if piece*n in val:
                        appoint3.append(piece * n)
                         #print("3" + str(appoint3))

            """if tot < 10:
                for n in range(monnaie+1):
                    for i in systeme:
                        if n*i == 10:
                            print(i, n)
                        if n*i+1 == 10:
                            print(i, n)
                            appoint4.append(n*i)
                        if n*i+2 == 10:
                            print(i, n)"""



            appoint_ = set(appoint1) & set(appoint3) #& set(appoint2)
    return appoint_