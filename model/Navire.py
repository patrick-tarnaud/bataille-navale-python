from model.Coque import *
from model.Arme import *


class Navire:

    def __init__(self, nom, fabriquant, annee, longueur, puissance_moteur, kilometrage, coque):
        self.nom = nom
        self.fabriquant = fabriquant
        self.annee = annee
        self.longueur = longueur
        self.puissance_moteur = puissance_moteur
        self.kilometrage = kilometrage

        self.coque = coque

    @property
    def etat(self):
        return "En marche" if self.coque.points_vie > 0 else "Détruit"



    def naviguer(self, distance):
        if self.etat == 'En marche':
            self.kilometrage += distance
            print("""{nom} navigue.
{distance} NM parcourus.
Kilométrage actuel : {kilometrage} NM.
    -------------------------""".format(nom=self.nom, distance=distance, kilometrage=self.kilometrage))
        else:
            print(self.nom, 'ne peut plus naviguer car il est détruit')

    def subir_degats(self, degats):
        if self.etat == 'En marche':
            # calcul des points de vie restant vis à vis des degats
            if degats < self.coque.points_vie:
                self.coque.points_vie -= degats
                # la cible perd 5 points de resistance à chaque tir subi, ne peut être négatif
                self.coque.resistance = self.coque.resistance - 5 if self.coque.resistance > 5 else 0
            else:
                # détruit
                self.coque.points_vie = 0

            if self.etat == 'Détruit':
                print(self.nom, 'est détruit !')
        else:
            print(self.nom, 'ne peut plus subir de dégâts car il est déjà détruit')

