from random import random
from model.Navire import *


class NavireDeGuerre(Navire):
    def __init__(self, nom, fabriquant, annee, longueur, puissance_moteur, kilometrage, coque, arme):
        """
        constructeur NavireDeGuerre
        :param nom:
        :param fabriquant:
        :param annee:
        :param longueur:
        :param puissance_moteur:
        :param kilometrage:
        :param coque:
        :param arme:
        """
        super().__init__(nom, fabriquant, annee, longueur, puissance_moteur, kilometrage, coque)
        self.arme = arme

    def tirer_sur(self, cible):
        if self.arme.puissance_tir > 0:
            print(self.nom, 'tire sur', cible.nom)

            # calcul des degats
            random1 = random()
            random2 = random()
            random3 = random()
            degats = round((((0.5 + random1) * self.arme.puissance_tir) - (random2 * cible.coque.resistance)) * random3)

            # La cible est 'en marche' et tir réussi
            if degats > 0 and cible.etat == 'En marche':
                print(degats, 'dégâts infligés')
                cible.subir_degats(degats)
            # la cible est deja détruite ou le tir échoué
            else:
                print('Le tir a échoué !')

            self.arme.puissance_tir = self.arme.puissance_tir - 1 if self.arme.puissance_tir > 0 else 0

            print("""Puissance {tireur} = {puissance_tir}.
    Résistance {cible} = {resistance}.
    Points de vie {cible} = {points_vie}/100.
        -------------------------""".format(tireur=self.nom, puissance_tir=self.arme.puissance_tir, cible=cible.nom,
                                            resistance=cible.coque.resistance, points_vie=cible.coque.points_vie))
        else:
            print(self.nom, 'ne peut plus tirer car il n\'a plus de puissance de tir')

    def __str__(self):
        return """[ {nom} - {fabriquant} ({annee}) ]
{longueur} mètres - {puissance_moteur} ch
{couleur} - {kilometrage} NM
Puissance de tir : {puissance_tir}
Résistance : {resistance}
Points de vie : {points_vie}/100
Etat : {etat}
------------------------- 
""".format(nom=self.nom.upper(), fabriquant=self.fabriquant.upper(), annee=self.annee, longueur=self.longueur,
           puissance_moteur=self.puissance_moteur, couleur=self.coque.couleur,
           kilometrage=self.kilometrage, puissance_tir=self.arme.puissance_tir, resistance=self.coque.resistance,
           points_vie=self.coque.points_vie, etat=self.etat)
