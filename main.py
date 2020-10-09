from random import randint
from model.NavireDeGuerre import *
from model.NavireCivil import *
from model.Coque import *
from model.Arme import *


def fabriquer_navires_de_guerre():
    la_fayette = NavireDeGuerre('Frégate La Fayette', 'NavCompany', 2000, 20, 3000, 100000,
                                Coque(50, 'acier', 'bleu'),
                                Arme('Canon leger', 20, 100))

    le_narval = NavireDeGuerre('Porte Avion Le Narval', 'Dassault', 1980, 100, 30000, 500000,
                               Coque(100, 'titane', 'gris'),
                               Arme('Canon lourd', 100, 10000))

    le_destructeur = NavireDeGuerre('Destroyer Le Destructeur', 'XRay', 2010, 40, 10000, 200000,
                                    Coque(75, 'acier blindé', 'bleu'),
                                    Arme('Canon', 75, 5000))

    return la_fayette, le_narval, le_destructeur


def jouer_navires_de_guerre(la_fayette: NavireDeGuerre, le_narval: NavireDeGuerre, le_destructeur: NavireDeGuerre):
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
    le_destructeur.tirer_sur(la_fayette)

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

    print(la_fayette.nom, la_fayette.etat)
    print(le_narval.nom, le_narval.etat)
    print(le_destructeur.nom, le_destructeur.etat)
    print('-------------------------------------------')
    print('-------------------------------------------')

    le_narval.tirer_sur(le_narval)

def fabriquer_navires_civil():
    paquebot_lotus = NavireCivil('Paquebot Lotus', 'Jeanneau', 2000, 150, 3000, 5000, Coque(20, 'acier', 'orange'), 0,
                                 500, ['Malte', 'Iles Canaries'])

    paquebot_tulipe = NavireCivil('Paquebot Tulipe', 'Jeanneau', 1980, 200, 4500, 10000, Coque(50, 'acier', 'rouge'), 0,
                                  250)

    paquebot_pivoine = NavireCivil('Paquebot Pivoine', 'Robert & Cie', 2019, 200, 4500, 10000,
                                   Coque(70, 'acier', 'bleu'), 0,
                                   600)
    return [paquebot_lotus, paquebot_tulipe, paquebot_pivoine]


def jouer_navires_civils(navires_civils: [NavireCivil], nb_tours):
    for tour in range(nb_tours):
        for nav in navires_civils:
            nav.prendre_passagers(randint(0, 5000))

    for nav in navires_civils:
        print(nav)


if __name__ == '__main__':
    try:
        navires_de_guerre = fabriquer_navires_de_guerre()
        jouer_navires_de_guerre(*navires_de_guerre)
        navires_civils = fabriquer_navires_civil()
        jouer_navires_civils(navires_civils, 5)
    except BatailleNavaleError as e:
        print('BatailleNavaleError !')
        print('Navire en cause :', e.navire.nom)
        print('Message :', e.msg)
    except Exception as e:
        print('Exception !')
        print(e)

    navires_de_guerre[0].saveToCSV()
