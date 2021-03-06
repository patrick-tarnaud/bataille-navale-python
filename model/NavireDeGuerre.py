from random import random
from model.Navire import *
from errors.BatailleNavaleError import *
from csv import writer
import json


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
        if cible == self:
            raise BatailleNavaleError(self, self.nom + ' tire sur lui-même ! Un navire ne peut tirer sur lui-même !')
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

            if isinstance(cible, NavireDeGuerre):
                self.arme.puissance_tir = self.arme.puissance_tir - 1 if self.arme.puissance_tir > 0 else 0
            else:
                self.arme.puissance_tir = self.arme.puissance_tir - 10 if self.arme.puissance_tir > 10 else 0
                self.coque.resistance = self.coque.resistance - 10 if self.coque.resistance > 10 else 0

            print("""Puissance {tireur} = {puissance_tir}.
    Résistance {cible} = {resistance}.
    Points de vie {cible} = {points_vie}/100.
        -------------------------""".format(tireur=self.nom, puissance_tir=self.arme.puissance_tir, cible=cible.nom,
                                            resistance=cible.coque.resistance, points_vie=cible.coque.points_vie))
        else:
            raise BatailleNavaleError(self, self.nom + ' ne peut plus tirer car il n\'a plus de puissance de tir')

    def __str__(self):
        return """\
[ {nom} - {fabriquant} ({annee}) ]
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

    def save_to_cvs(self):
        with open('navire_' + self.nom + '.csv', 'w') as csvfile:
            wr = writer(csvfile, delimiter=',')

            # header
            header = list(self.__dict__.keys())
            header.remove('coque')
            header.remove('arme')
            header += list(self.coque.__dict__.keys())
            header += list(self.arme.__dict__.keys())
            wr.writerow(header)

            # row with values
            row = list(self.__dict__.values())
            row = row[:6]
            row += list(self.coque.__dict__.values())
            row += list(self.arme.__dict__.values())
            wr.writerow(row)

    def to_json(self):
        return json.dumps(self, ensure_ascii=False, default=lambda o: o.__dict__)

    def save_to_json(self):
        with open('navire_' + self.nom + '.json', 'w') as jsonfile:
            jsonfile.write(self.to_json())

    @staticmethod
    def from_json(data):
        dn = json.loads(data)
        return NavireDeGuerre(dn['nom'], dn['fabriquant'], dn['annee'], dn['longueur'], dn['puissance_moteur'],
                              dn['kilometrage'],
                              Coque(dn['coque']['resistance'], dn['coque']['couleur'], dn['coque']['matiere']),
                              Arme(dn['arme']['nom'], dn['arme']['puissance_tir'], dn['arme']['prix']))

    @staticmethod
    def load_from_json(jsonfile_name):
        with open(jsonfile_name, 'r') as jsonfile:
            data = jsonfile.read()

        return NavireDeGuerre.from_json(data)
