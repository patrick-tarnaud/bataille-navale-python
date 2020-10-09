from model.Navire import *


class NavireCivil(Navire):
    def __init__(self, nom, fabriquant, annee, longueur, puissance_moteur, kilometrage, coque, nb_passagers,
                 capacite_max_passagers, destinations=[]):
        """
        constructeur NavireCivil

        :param nom:
        :param fabriquant:
        :param annee:
        :param longueur:
        :param puissance_moteur:
        :param kilometrage:
        :param coque:
        :param nb_passagers:
        :param capacite_max_passagers:
        :param destinations:
        """
        super().__init__(nom, fabriquant, annee, longueur, puissance_moteur, kilometrage, coque)
        self.nb_passagers = nb_passagers
        self.capacite_max_passagers = capacite_max_passagers
        self.destinations = destinations

    def deposer_passagers(self, nb):
        self.nb_passagers = self.nb_passagers - nb if self.nb_passagers > nb else 0

    def prendre_passagers(self, nb):
        self.nb_passagers = self.nb_passagers + nb if self.nb_passagers + nb <= self.capacite_max_passagers else self.capacite_max_passagers

    def __str__(self):
        return """[ {nom} - {fabriquant} ({annee}) ]
{longueur} mètres - {puissance_moteur} ch
{couleur} - {kilometrage} NM
Résistance : {resistance}
Points de vie : {points_vie}/100
Etat : {etat}
Nombre de passagers : {nb_passagers}/{capacite}
Destinations : {destinations}
------------------------- 
""".format(nom=self.nom.upper(), fabriquant=self.fabriquant.upper(), annee=self.annee, longueur=self.longueur,
           puissance_moteur=self.puissance_moteur, couleur=self.coque.couleur,
           kilometrage=self.kilometrage, resistance=self.coque.resistance,
           points_vie=self.coque.points_vie, etat=self.etat, nb_passagers=self.nb_passagers,
           capacite=self.capacite_max_passagers, destinations=self.destinations)
