try:
    n = int(input("Saisir la taille des deux tableaux"))

    M1 = [[int(input("Tableau 1 =")) for x in range(n)], [int(input("Tableau 1 =")) for x in range(n)]]
    M2 = [[int(input("Tableau 2 =")) for x in range(n)], [int(input("Tableau 2 =")) for x in range(n)]]
    M3 = [[0] * n, [0] * n]

    for i in range(len(M1)):
        for j in range(len(M1[0])):
            M3[i][j] = M1[i][j] + M2[i][j]

    print("M1 =", M1)
    print("M2 =", M2)
    print("M1 + M2 = :", M3)

except ValueError:
    print("saisie non valide")
