#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Fichier: test_meeus-chap3.py
# Auteur: Marc COATANHAY

"""
    Tests pour le module meeus.
    Chapitre 3
"""

# Import des modules
try:
    import mes_modules_path
except:
    pass
from meeus import *
import unittest

# Définitions constantes et variables globales

# Définitions fonctions et classes
class MeeusTest(unittest.TestCase):

    def test_dimanchePaques(self):
        self.assertEqual(dimanchePaques(477),[477,4,17])
        self.assertEqual(dimanchePaques(1009),[1009,4,17])
        self.assertEqual(dimanchePaques(1541),[1541,4,17])
        self.assertEqual(dimanchePaques(2021),[2021,4,4])


if (__name__ == "__main__"):
    unittest.main()