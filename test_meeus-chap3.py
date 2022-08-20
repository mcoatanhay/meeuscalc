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
    def test_intM(self):
        self.assertEqual(intM(7/4), 1)
        self.assertEqual(intM(5.9999), 5)
        self.assertEqual(intM(-5.84), -6)

    def test_jourJulien(self):
        self.assertEqual(jourJulien(1957,10,4.81),2436116.31)
        self.assertEqual(jourJulien(333,1,27.5),1842713.0)
        self.assertEqual(jourJulien(-4712,1,1.5),0)
        self.assertEqual(jourJulien(1858,11,17.0),2400000.5)

    def test_jourJulienModif(self):
        self.assertEqual(jourJulienModif(1858,11,17.0),0)

    def test_conformeInt(self):
        for i in range (10):
            self.assertRaises(ValueError,conformeInt,1582,10,5 + i)

    def test_avantJJ0(self):
        self.assertFalse(avantJJ0(-4712, 1, 1.5))

    def test_calendrier(self):
        self.assertEqual(calendrier(1582,10,4),"Julien")
        self.assertEqual(calendrier(1582,10,15),"Grégorien")

    def test_jourJulien0(self):
        self.assertEqual(jourJulien0(2000),jourJulien(1999,12,31))

    def test_bissextile(self):
        # bissextile quand le millésime est divisible par 4
        self.assertTrue(bissextile(900))
        self.assertTrue(bissextile(1236))
        # non bissextile quand le millésime n'est pas divisible par 4
        self.assertFalse(bissextile(750))
        self.assertFalse(bissextile(1429))
        # Exceptions pour le calendrier Grégorien
        # ---------------------------------------
        # Les années séculaires sont communes lorsque leur millésime n'est pas
        # divisible par 400.
        self.assertFalse(bissextile(1700))
        self.assertFalse(bissextile(1800))
        self.assertFalse(bissextile(1900))
        # Les années séculaires sont bissextiles lorsque leur millésime est
        # multiple de 400.
        self.assertTrue(bissextile(1600))
        self.assertTrue(bissextile(2000))
        self.assertTrue(bissextile(2400))

    def test_date(self):
        self.assertEqual(date(0),[-4712,1,1.5])
        self.assertEqual(date(2436116.31)[0],1957)
        self.assertEqual(date(2436116.31)[1],10)
        self.assertEqual(round(date(2436116.31)[2],2),4.81)

    def test_deltaJours(self):
        # Vie de Camille Flammarion
        naissanceCF = [1842,2,26]
        mortCF = [1925,6,3]
        self.assertEqual(deltaJours(naissanceCF, mortCF),30412)
        # 10 000 jours après le 30/06/1954
        date1 = [1954,6,30]
        JJ1 = jourJulien(1954,6,30)
        JJ2 = JJ1 + 10000
        date2 = date(JJ2)
        self.assertEqual(deltaJours(date1, date2),10000)

    def test_jourSemaine(self):
        # Prochaine éclipse solaire en france
        self.assertEqual(jourSemaine(2059,11,5),"mercredi")
        self.assertEqual(jourSemaine(2020,3,20),"vendredi")

    def test_jourAnnee(self):
        self.assertEqual(jourAnnee(2014,11,14),318)
        self.assertEqual(jourAnnee(2016,4,22),113)
        self.assertEqual(jourAnnee(2000,12,31),366)

    def test_dateJourAnnee(self):
        self.assertEqual(dateJourAnnee(2014,318),[2014,11,14])
        self.assertEqual(dateJourAnnee(2016,113),[2016,4,22])
        self.assertEqual(dateJourAnnee(2000,366),[2000,12,31])


if (__name__ == "__main__"):
    unittest.main()