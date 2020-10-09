import random

class Navire:

    def __init__(self, nom, fabriquant, annee, longueur, puissance_moteur, couleur, kilometrage,
                 puissance_tir, resistance, points_vie):
        self.nom = nom
        self.fabriquant = fabriquant
        self.annee = annee
        self.longueur = longueur
        self.puissance_moteur = puissance_moteur
        self.couleur = couleur
        self.kilometrage = kilometrage
        self.puissance_tir = puissance_tir
        self.resistance = resistance
        self.points_vie = points_vie

    @property
    def etat(self):
        return "En marche" if self.points_vie > 0 else "Détruit"

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
           puissance_moteur=self.puissance_moteur, couleur=self.couleur,
           kilometrage=self.kilometrage, puissance_tir=self.puissance_tir, resistance=self.resistance,
           points_vie=self.points_vie, etat=self.etat)

    def naviguer(self, distance):
        self.kilometrage += distance
        print("""{nom} navigue.
{distance} NM parcourus.
Kilométrage actuel : {kilometrage} NM.
-------------------------""".format(nom=self.nom, distance=distance, kilometrage=self.kilometrage))

    def subir_degats(self, degats):
        # calcul des points de vie restant vis à vis des degats
        if degats < self.points_vie:
            self.points_vie -= degats
            # la cible perd 5 points de resistance à chaque tir subi, ne peut être négatif
            self.resistance = self.resistance - 5 if self.resistance > 5 else 0
            # if self.resistance >= 5:
            #     self.resistance -= 5
            # else:
            #     self.resistance = 0
        else:
            # détruit
            self.points_vie = 0

        if self.etat == 'Détruit':
            print(self.nom, 'est détruit !')

    def tirer_sur(self, cible):
        print(self.nom, 'tire sur', cible.nom)

        # calcul des degats
        random1 = random.random()
        random2 = random.random()
        random3 = random.random()
        degats = round((((0.5 + random1) * self.puissance_tir) - (random2 * cible.resistance)) * random3)

        # La cible est 'en marche' et tir réussi
        if degats > 0 and cible.etat == 'En marche':
            print(degats, 'dégâts infligés')
            cible.subir_degats(degats)
        # la cible est deja détruite ou le tir échoué
        else:
            print('Le tir a échoué !')

        # le tireur perd 1 point de puissance a chaque tir réussi ou non, ne peut etre inférieur à 0
        # if self.puissance_tir > 0:
        #     self.puissance_tir += -1
        self.puissance_tir = self.puissance_tir - 1 if self.puissance_tir > 0 else 0

        print("""Puissance {tireur} = {puissance_tir}.
Résistance {cible} = {resistance}.
Points de vie {cible} = {points_vie}/100.
-------------------------""".format(tireur=self.nom, puissance_tir=self.puissance_tir, cible=cible.nom,
                                    resistance=cible.resistance, points_vie=cible.points_vie))
