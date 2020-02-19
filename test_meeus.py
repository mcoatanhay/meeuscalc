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
import incertitudes.incert as incert
from meeus import *
import unittest

# Définitions constantes et variables globales

# Définitions fonctions et classes
class MeeusTest(unittest.TestCase):
    def test_mnn_precession(self):
        reponses = [
        (incert.i(3.071), incert.i(1.337), incert.i(20.06)),
        (incert.i(3.073), incert.i(1.337), incert.i(20.05)),
        (incert.i(3.075), incert.i(1.336), incert.i(20.04)),
        (incert.i(3.077), incert.i(1.336), incert.i(20.03)),
        (incert.i(3.079), incert.i(1.335), incert.i(20.03))]
        calculs = []
        for i in range(-2, 3):
            calculs.append(mnn_precession(i))
        self.assertEqual(reponses, calculs)

if (__name__ == "__main__"):
    unittest.main()