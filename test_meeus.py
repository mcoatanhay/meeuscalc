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
        # self.assertRaises(avantjj0,[])

    def test_coordonnees_moyennes(self):
        afficher_calculs = False
        RA = (incert.i(10) + incert.i(9)/60 + incert.i("32.5")/3600)*15
        DE = incert.i(11) + incert.i(51)/60 + incert.i("33")/3600
        reponses = {'RAf (°)': RA, 'DEf (°)': DE}
        resultat = coordonnees_moyennes(3982, 2022.0)
        if afficher_calculs:
            print()
            print("************************************")
            print("*     test_coordonnees_moyennes    *")
            print("************************************")
            for ligne in resultat['calculs']:
                print(ligne)
            print('RAf (h) :', incert.tosexag(resultat['RAf (°)']/15))
            print('DEf (°) :', incert.tosexag(resultat['DEf (°)']))
        del resultat['calculs']
        self.assertEqual(resultat, reponses)

    def test_coordonnees_moyennes_rigoureuses(self):
        afficher_calculs = False
        RA = (incert.i(10) + incert.i(9)/60 + incert.i("32.48")/3600)*15
        DE = incert.i(11) + incert.i(51)/60 + incert.i("31.9")/3600
        reponses = {'RAf (°)': RA, 'DEf (°)': DE}
        resultat = coordonnees_moyennes_rigoureuses(3982, 2022.0)
        if afficher_calculs:
            print()
            print("*****************************************")
            print("* test_coordonnees_moyennes rigoureuses *")
            print("*****************************************")
            for ligne in resultat['calculs']:
                print(ligne)
            print('RAf (h) :', incert.tosexag(resultat['RAf (°)']/15))
            print('DEf (°) :', incert.tosexag(resultat['DEf (°)']))
        del resultat['calculs']
        self.assertEqual(resultat, reponses)

    def test_coordonnees_moyennes2(self):
        afficher_calculs = False
        RA = (incert.i(10) + incert.i(9)/60 + incert.i("32.48")/3600)*15
        DE = incert.i(11) + incert.i(51)/60 + incert.i("31.9")/3600
        reponses = {'RAf (°)': RA, 'DEf (°)': DE}
        resultat = coordonnees_moyennes2(3982,2022.0)
        if afficher_calculs:
            print()
            print("************************************")
            print("*    test_coordonnees_moyennes2    *")
            print("************************************")
            for ligne in resultat['calculs']:
                print(ligne)
            print('RAf (h) :', incert.tosexag(resultat['RAf (°)']/15))
            print('DEf (°) :', incert.tosexag(resultat['DEf (°)']))
        del resultat['calculs']
        self.assertEqual(resultat, reponses)

    def test_coordonnees_moyennes3(self):
        afficher_calculs = False
        RA = (incert.i(10) + incert.i(9)/60 + incert.i("32.47")/3600)*15
        DE = incert.i(11) + incert.i(51)/60 + incert.i("31.9")/3600
        reponses = {'RAf (°)': RA, 'DEf (°)': DE}
        resultat = coordonnees_moyennes3(3982,2022.0)
        if afficher_calculs:
            print()
            print("*************************************")
            print("*     test_coordonnees_moyennes3    *")
            print("*************************************")
            for ligne in resultat['calculs']:
                print(ligne)
            print('RAf (h) :', incert.tosexag(resultat['RAf (°)']/15))
            print('DEf (°) :', incert.tosexag(resultat['DEf (°)']))
        del resultat['calculs']
        # self.assertEqual(resultat, reponses)

    def test_coordonnnes_moyennes_comparaisons(self):
        afficher_calculs = False
        resultats = []
        resultats.append(coordonnees_moyennes(3982,2022.0))
        resultats.append(coordonnees_moyennes_rigoureuses(3982,2022.0))
        resultats.append(coordonnees_moyennes2(3982,2022.0))
        resultats.append(coordonnees_moyennes3(3982,2022.0))
        if afficher_calculs:
            print()
            print("**************************************")
            print("* test_coordonnees_moyennes_synthèse *")
            print("**************************************")
            for resultat in resultats:
                RAfh = incert.tosexag(resultat['RAf (°)']/15)
                print(RAfh.valeur, format((RAfh.incert*3).s, '>10.3f'))
            for resultat in resultats:
                DEfd = incert.tosexag(resultat['DEf (°)'])
                print(DEfd.valeur, format((DEfd.incert*3).s, '>10.3f'))
        for i in range(0, 4):
            del resultats[i]['calculs']
            if i > 0:
                self.assertEqual(resultats[0], resultats[i])

    def test_parametres_precession(self):
        afficher_calculs = False
        reponses = [
        {'m_alpha (s)': 3.071, 'n_alpha (s)': 1.337, 'n_delta (")': 20.06},
        {'m_alpha (s)': 3.073, 'n_alpha (s)': 1.337, 'n_delta (")': 20.05},
        {'m_alpha (s)': 3.075, 'n_alpha (s)': 1.336, 'n_delta (")': 20.04},
        {'m_alpha (s)': 3.077, 'n_alpha (s)': 1.336, 'n_delta (")': 20.03},
        {'m_alpha (s)': 3.079, 'n_alpha (s)': 1.335, 'n_delta (")': 20.03}]
        resultat = []
        if afficher_calculs:
            print()
            print("**************************************")
            print("*     test_parametres_precession     *")
            print("**************************************")
        for i in range(-2, 3):
            parametres_i = parametres_precession(incert.i(i))
            resultat.append(parametres_i)
            if afficher_calculs:
                print('----------- siècle :', 2000 + 100*i)
                print('m_alpha (s) :', parametres_i['m_alpha (s)'])
                print('n_alpha (s) :', parametres_i['n_alpha (s)'])
                print('n_delta (") :', parametres_i['n_delta (")'])
        self.assertEqual(reponses, resultat)

if (__name__ == "__main__"):
    unittest.main()