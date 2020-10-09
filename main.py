from random import randint
from model.Navire import *
from model.Coque import *
from model.Arme import *


def fabriquer():
    # nom, fabriquant, annee, longueur, puissance_moteur, kilometrage, coque, arme
    la_fayette = Navire('Frégate La Fayette', 'NavCompany', 2000, 20, 3000, 100000,
                        Coque(50, 'acier', 'bleu'),
                        Arme('Canon leger', 50, 100))

    le_narval = Navire('Porte Avion Le Narval', 'Dassault', 1980, 100, 30000, 500000,
                       Coque(100, 'titane', 'gris'),
                       Arme('Canon lourd', 100, 10000))

    le_destructeur = Navire('Destroyer Le Destructeur', 'XRay', 2010, 40, 10000, 200000,
                            Coque(75, 'acier blindé', 'bleu'),
                            Arme('Canon', 75, 5000))
    # print(la_fayette)
    # print(le_narval)
    # print(le_destructeur)
    return la_fayette, le_narval, le_destructeur


def jouer(la_fayette: Navire, le_narval : Navire, le_destructeur: Navire):
    # tour 1
    la_fayette.naviguer(1000)
    la_fayette.tirer_sur(le_narval)

    le_narval.naviguer(1000)
    le_narval.tirer_sur(le_destructeur)

    le_destructeur.naviguer(1000)
    le_destructeur.tirer_sur(la_fayette)

    # tour 2
    la_fayette.naviguer(1000)
    la_fayette.tirer_sur(le_destructeur)

    le_narval.naviguer(1000)
    le_narval.tirer_sur(la_fayette)

    le_destructeur.naviguer(1000)
    le_destructeur.tirer_sur(le_destructeur)

    # tour 3
    la_fayette.naviguer(1000)
    la_fayette.tirer_sur(le_narval)

    le_narval.naviguer(1000)
    le_narval.tirer_sur(la_fayette)

    le_destructeur.naviguer(1000)
    le_destructeur.tirer_sur(la_fayette)

    # resultat
    print(la_fayette)
    print(le_narval)
    print(le_destructeur)


if __name__ == '__main__':
    navires = fabriquer()
    jouer(*navires)
