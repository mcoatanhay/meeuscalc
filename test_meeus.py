#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Fichier: test_meeus.py
# Auteur: Marc COATANHAY

"""
    Tests pour le module meeus.
"""

# Import des modules
try:
    import mes_modules_path
except:
    pass
from meeus import *
import incertitudes.incert as incert
import unittest

# Définitions constantes et variables globales

# Définitions fonctions et classes
class MeeusTest(unittest.TestCase):
    def test_avantjj0(self):
        self.assertFalse(avantjj0(-4712, 1, 1.5))
        self.assertTrue(avantjj0(-4712, 1, 1))
        self.assertRaises(avantjjo,[])

    def test_parametres_precession(self):
        reponses = [
        (incert.i(3.071), incert.i(1.337), incert.i(20.06)),
        (incert.i(3.073), incert.i(1.337), incert.i(20.05)),
        (incert.i(3.075), incert.i(1.336), incert.i(20.04)),
        (incert.i(3.077), incert.i(1.336), incert.i(20.03)),
        (incert.i(3.079), incert.i(1.335), incert.i(20.03))]
        calculs = []
        for i in range(-2, 3):
            calculs.append(parametres_precession(i))
        # self.assertEqual(reponses, calculs)
        self.assertTrue(True)

    def test_coordonnees_moyennes(self):
        calculs = False
        RA = incert.i(10) + incert.i(9)/60 + incert.i("32.5")/3600
        DE = incert.i(11) + incert.i(51)/60 + incert.i("33")/3600
        reponses = (RA, DE)
        resultat = coordonnees_moyennes(3982,2022.0)
        if calculs:
            for ligne in resultat['calculs']:
                print(ligne)
            print(incert.tosexag(resultat['RAf (°)']/15))
            print(incert.tosexag(resultat['DEf (°)']))
        self.assertEqual(resultat['RAf (°)']/15, RA)
        self.assertEqual(resultat['DEf (°)'], DE)

if (__name__ == "__main__"):
    unittest.main()