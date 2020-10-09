from model.Navire import *


def main():
    # nom, fabriquant, annee, longueur, puissance_moteur, couleur, kilometrage, puissance_tir, resistance, points_vie
    la_fayette = Navire('Frégate La Fayette', 'NavCompany', 2000, 20, 3000, 'bleu', 100000, 100, 50, 100)
    le_narval = Navire('Porte Avion Le Narval', 'Dassault', 1980, 100, 30000, 'gris/bleu', 500000, 300, 100, 100)
    le_destructeur = Navire('Destroyer Le Destructeur', 'XRay', 2010, 40, 10000, 'vert', 200000, 200, 75, 100)
    print(la_fayette)
    print(le_narval)
    print(le_destructeur)
    la_fayette.naviguer(100)
    la_fayette.tirer_sur(le_narval)


if __name__ == '__main__':
    main()
