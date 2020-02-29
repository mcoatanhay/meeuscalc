#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Fichier: meeus.py
# Auteur: Marc COATANHAY

"""
    Implémentation des "calculs astronomiques à l'usage des amateurs"
    de Jean MEEUS, édition 2014.
"""

# Import des modules
try:
    import mes_modules_path
except:
    pass
import coordonnees.coord as coord
import etoilescat.etoiles as etoiles
import incertitudes.incert as incert

# Définitions constantes et variables globales
jours_semaine = {
    0: "dimanche", 1: "lundi", 2: "mardi", 3: "mercredi",
    4: "jeudi", 5: "vendredi", 6: "samedi"}

# Définitions fonctions et classes
def avantjj0(Y, M, D):
    """
        Vérifie si une date (Y, M, D) se trouve avant le jour julien 0, c'est
        à dire avant le 1er janvier - 4712 à 12H (-4712, 1, 1.5).
        Entrée :
            Y L'année
            M le numéro du mois
            D le jour du mois avec éventuellement des décimales de jour
        Retour :
            booleen : True or False
            erreur : si (Y, M, D) n'est pas une date conforme
                - voir conforme(Y, M, D) -
    """
    [Y, M, D] = conforme(Y, M, D)
    if(Y < -4712):
        return True
    elif(Y == -4712):
        return ((M == 1) and (D < 1.5))
    else:
        return False

def bissextile(Y):
    """
        Vérifie si une année Y est bissextile.
        Entrée :
            Y l’année
        Retour :
            True
            False
            Erreur si Y n’est pas convertible en entier
    """
    Y = int(Y)
    if(Y <= 1582):
        return ((Y % 4) == 0)
    else:
        return (
            ((Y % 4) == 0)
            and
            (((Y % 100) != 0) or ((Y % 400) == 0))
            )

def calendrier(Y, M, D):
    """
        Retourne le calendrier (Julien ou Gregorien) qui correspond à une date.
        Entrée :
            Y l’année
            M le numéro du mois
            D le jour du mois avec éventuellement des décimales de jour
        Retour :
            « Julien »
            « Grégorien »
            Erreur si (Y, M, D) n’est pas une date conforme
                - voir conforme(Y, M, D) -
    """
    [Y, M, D] = conforme(Y, M, D)
    if(Y > 1582):
        return "Grégorien"
    elif (Y == 1582):
        if(M > 10):
            return "Grégorien"
        elif(M == 10):
            if(D < 5):
                return "Julien"
            else:
                return "Grégorien"
        else:
            return "Julien"
    else:
        return "Julien"

def conforme(Y, M, D):
    """
        Vérifie la conformité de la date proposée.
        Entrée :
            Y l’année
            M le numéro du mois
            D le jour du mois avec éventuellement des décimales de jour
        Retour :
            [Y, M, D]
            Y l’année
            M le numéro du mois
            D le jour du mois avec éventuellement des décimales de jour
            Erreur si :
                le mois n’est pas compris entre 1 et 12
                le nombre de jours n’est pas correct pour le mois et l’année.
                si la date correspond à un jour perdu lors que changement de
                calendrier Julien vers Grégorien
    """
    # Vérification du format de Y, M et D
    Y = int(Y)
    M = int(M)
    D = float(D)
    # Vérification du mois M et calcul du nbr max de jours
    if M in [1, 3, 5, 7, 8, 10, 12]:
        nbjours = 31
    elif M in [4, 6, 9, 11]:
        nbjours = 30
    elif (M == 2):
        if bissextile(Y):
            nbjours = 29
        else:
            nbjours = 28
    else:
        message = "Le mois doit être compris entre 1 et 12 inclus"
        raise ValueError(message)
    # Vérification du jour D
    if((int(D) > nbjours) or (D < 0)):
        message = "Le nombre de jours du mois {}/{}"
        message += " doit être compris entre 1 et {}"
        message = message.format(M, Y, nbjours)
        raise ValueError(message)
    # Elimination des jours perdus lors du changement de calendrier Julien
    # à Grégorien.
    if((Y == 1582) and (M == 10) and (D >= 5) and (D < 15)):
        message = "Les jours du 5 au 14 novembre 1582 inclus"
        message += " n'appartiennent à aucun calendrier"
        raise ValueError(message)
    return [Y, M, D]

def coordonnees_moyennes(HR, A):
    """
        Calcul approximatif des coordonnées moyennes de l'étoile:
            en ascenscion droite
            et en déclinaison de
        pour l'année A.
        Entrée :
            HR = numéro de l'étoile
            A = Année
        Sortie :
            dictionnaire :
            'calculs' = calculs intermédiaires pour débogage
            'RAf (°)' = ascension droite (°) de 0 à 360°
            'DEf (°)' = déclinaison (°) de -90 à +90°
    """
    calculs = []
    resultat = {}
    data = etoiles.etoile_data(HR)
    calculs.append({'pmRA (mas/y)': data.pmRA})
    pmRA = incert.i(data.pmRA)/(15*1000)
    calculs.append({'pmRA (s/y)': pmRA})
    calculs.append({'pmDE (mas/y)': data.pmDE})
    pmDE = incert.i(data.pmDE)/1000
    calculs.append({'pmDE ("s/y)': pmDE})
    alpha = int(data.RAh) + incert.i(int(data.RAm))/60
    alpha += incert.i(data.RAs)/3600
    alpha *= 15
    calculs.append({'RA0 (°)': alpha})
    delta = int(data.DEsgn + data.DEd) + incert.i(int(data.DEm))/60
    delta += incert.i(data.DEs)/3600
    calculs.append({'DEC0 (°)': delta})
    deltaA = incert.it(A - 2000, 0)
    calculs.append({'DeltaA (année)': deltaA})
    S = deltaA/100
    calculs.append({'S (siècle) ': S})
    parametres = parametres_precession(S)
    m_alpha = parametres['m_alpha (s)']
    n_alpha = parametres['n_alpha (s)']
    n_delta = parametres['n_delta (")']
    calculs.append({'m_alpha (s)': m_alpha})
    calculs.append({'n_alpha (s)':  n_alpha})
    calculs.append({'n_delta (")': n_delta})
    precRA = n_alpha*incert.sin(incert.pi*alpha/180)
    precRA *= incert.tan(incert.pi*delta/180)
    precRA += m_alpha
    calculs.append({'precRA (s)': precRA})
    precDE = n_delta*incert.cos(incert.pi*alpha/180)
    calculs.append({'precDE (")': precDE})
    varRA = precRA + pmRA
    calculs.append({'varRA (s)': varRA})
    varDE = precDE + pmDE
    calculs.append({'varDE (")': varDE})
    calculs.append({'delta A (an)': deltaA})
    varRAtot = varRA*deltaA
    calculs.append({'varRAtot (s)': varRAtot})
    varDEtot = varDE*deltaA
    calculs.append({'varDEtot (")': varDEtot})
    RAf = alpha + varRAtot*15/3600
    calculs.append({'RAf (°)': RAf})
    DEf = delta + varDEtot/3600
    calculs.append({'DEf (°)': DEf})
    resultat['calculs'] = calculs
    resultat['RAf (°)'] = RAf
    resultat['DEf (°)'] = DEf
    return resultat

def coordonnees_moyennes_rigoureuses(HR, A):
    """
        Calcul rigoureux des coordonnées moyennes de l'étoile:
            en ascenscion droite
            et en déclinaison de
        pour l'année A.
        Entrée :
            HR = numéro de l'étoile
            A = Année
        Sortie :
            dictionnaire :
            'calculs' = calculs intermédiaires pour débogage
            'RAf (°)' = ascension droite (°) de 0 à 360°
            'DEf (°)' = déclinaison (°) de -90 à +90°
    """
    calculs = []
    resultat = {}
    data = etoiles.etoile_data(HR)
    pmRA = incert.it(data.pmRA, 0)/1000
    calculs.append({'pmRA (as/y)': pmRA})
    pmDE = incert.it(data.pmDE, 0)/1000
    calculs.append({'pmDE (as/y)': pmDE})
    alpha = int(data.RAh) + incert.i(int(data.RAm))/60
    alpha += incert.i(data.RAs)/3600
    alpha *= 15
    calculs.append({'RA0 (°)': alpha})
    delta = int(data.DEsgn + data.DEd) + incert.i(int(data.DEm))/60
    delta += incert.i(data.DEs)/3600
    calculs.append({'DEC0 (°)': delta})
    deltaA = incert.it(A - 2000, 0)
    calculs.append({'DeltaA (année)': deltaA})
    alpha1 = (alpha + pmRA*deltaA/3600)*incert.pi/180
    calculs.append({'alpha1 (°)': alpha1})
    delta1 = (delta + pmDE*deltaA/3600)*incert.pi/180
    calculs.append({'delta1 (°)': delta1})
    t = deltaA/100
    calculs.append({'t (siècle)': t})
    dzeta = (("2306.2181"*t + "0.30188"*t**2 + "0.017998"*t**3)/3600)*incert.pi/180
    zed = (("2306.2181"*t + "1.09468"*t**2 + "0.018203"*t**3)/3600)*incert.pi/180
    theta = (("2004.3109"*t + "0.42665"*t**2 + "0.041833"*t**3)/3600)*incert.pi/180
    A = incert.cos(delta1)*incert.sin(alpha1 + dzeta)
    B = incert.cos(theta)*incert.cos(delta1)*incert.cos(alpha1 + dzeta) \
        - incert.sin(theta)*incert.sin(delta1)
    C = incert.sin(theta)*incert.cos(delta1)*incert.cos(alpha1 + dzeta) \
        + incert.cos(theta)*incert.sin(delta1)
    delta = incert.asin(C)
    calculs.append({'delta (°)': delta})
    alpha = incert.atan2(A, B) + zed
    if(alpha.valeur < 0):
        alpha += 2*incert.pi
    calculs.append({'alpha (°)': alpha})
    resultat['calculs'] = calculs
    resultat['RAf (°)'] = alpha*180/incert.pi
    resultat['DEf (°)'] = delta*180/incert.pi
    return resultat

def coordonnees_moyennes2(HR, A):
    """
        Calcul les coordonnées moyennes de l'étoile:
            en ascenscion droite
            et en déclinaison de
        pour l'année A première méthode matricielle.
        Entrée :
            HR = numéro de l'étoile
            A = Année
        Sortie :
            dictionnaire :
            'calculs' = calculs intermédiaires pour débogage
            'RAf (°)' = ascension droite (°) de 0 à 360°
            'DEf (°)' = déclinaison (°) de -90 à +90°
    """
    calculs = []
    resultat = {}
    data = etoiles.etoile_data(HR)
    pmRA = incert.it(data.pmRA, 0)/1000
    calculs.append({'pmRA (as/y)': pmRA})
    pmDE = incert.it(data.pmDE, 0)/1000
    calculs.append({'pmDE (as/y)': pmDE})
    alpha = int(data.RAh) + incert.i(int(data.RAm))/60
    alpha += incert.i(data.RAs)/3600
    alpha *= 15
    calculs.append({'RA0 (°)': alpha})
    delta = int(data.DEsgn + data.DEd) + incert.i(int(data.DEm))/60
    delta += incert.i(data.DEs)/3600
    calculs.append({'DEC0 (°)': delta})
    deltaA = incert.it(A - 2000, 0)
    calculs.append({'DeltaA (année)': deltaA})
    S = deltaA/100
    calculs.append({'S (siècle)': S})
    DS = deltaA/1000
    calculs.append({'DS (deca siècle)': DS})
    RA1 = alpha + pmRA*deltaA/3600
    calculs.append({'RA1 (°)': RA1})
    DE1 = delta + pmDE*deltaA/3600
    calculs.append({'DE1 (°)': DE1})
    psi1 = RA1*incert.pi/180
    phi1 = DE1*incert.pi/180
    U1 = coord.xyzdepolaire(psi1, phi1, incert.un)
    calculs.append({'U1 (m)': U1})
    parametres = coord.parametres_precession(DS)
    calculs += parametres['calculs']
    U2 = coord.rotation3(-(parametres['zeta (")']/3600)*(incert.pi/180), U1)
    U3 = coord.rotation2((parametres['theta (")']/3600)*(incert.pi/180), U2)
    Uf = coord.rotation3(-(parametres['z (")']/3600)*(incert.pi/180), U3)
    (psif, phif, rf) = coord.polairedexyz(Uf)
    if(psif.valeur < 0):
        psif += incert.pi*2
    resultat['calculs'] = calculs
    resultat['RAf (°)'] = psif*180/incert.pi
    resultat['DEf (°)'] = phif*180/incert.pi
    return resultat

def coordonnees_moyennes3(HR, A):
    """
        Calcul les coordonnées moyennes de l'étoile:
            en ascenscion droite
            et en déclinaison de
        pour l'année A deuxième méthode matricielle.
        Entrée :
            HR = numéro de l'étoile
            A = Année
        Sortie :
            dictionnaire :
            'calculs' = calculs intermédiaires pour débogage
            'RAf (°)' = ascension droite (°) de 0 à 360°
            'DEf (°)' = déclinaison (°) de -90 à +90°
    """
    calculs = []
    resultat = {}
    data = etoiles.etoile_data(HR)
    pmRA = incert.it(data.pmRA, 0)/1000
    calculs.append({'pmRA (as/y)': pmRA})
    pmDE = incert.it(data.pmDE, 0)/1000
    calculs.append({'pmDE (as/y)': pmDE})
    alpha = int(data.RAh) + incert.i(int(data.RAm))/60
    alpha += incert.i(data.RAs)/3600
    alpha *= 15
    calculs.append({'RA0 (°)': alpha})
    delta = int(data.DEsgn + data.DEd) + incert.i(int(data.DEm))/60
    delta += incert.i(data.DEs)/3600
    calculs.append({'DEC0 (°)': delta})
    deltaA = incert.it(A - 2000, 0)
    calculs.append({'DeltaA (année)': deltaA})
    S = deltaA/100
    calculs.append({'S (siècle)': S})
    DS = deltaA/1000
    calculs.append({'DS (deca siècle)': DS})
    RA1 = alpha + pmRA*deltaA/3600
    calculs.append({'RA1 (°)': RA1})
    DE1 = delta + pmDE*deltaA/3600
    calculs.append({'DE1 (°)': DE1})
    # psi1 = (incert.i(360) - RA1)*incert.pi/180
    psi1 = RA1*incert.pi/180
    phi1 = DE1*incert.pi/180
    U1 = coord.xyzdepolaire(psi1, phi1, incert.un)
    calculs.append({'U1 (m)': U1})
    parametres = coord.parametres_precession(DS)
    epsilon0 = incert.i(coord.precession_uai2000_coef['epsilon (")'][0])
    calculs += parametres['calculs']
    U2 = coord.rotation1((epsilon0/3600)*(incert.pi/180), U1)
    U3 = coord.rotation3(-(parametres['psi (")']/3600)*(incert.pi/180), U2)
    U4 = coord.rotation1(-(parametres['omega (")']/3600)*(incert.pi/180), U3)
    Uf = coord.rotation3((parametres['khi (")']/3600)*(incert.pi/180), U4)
    (psif, phif, rf) = coord.polairedexyz(Uf)
    if(psif.valeur < 0):
        psif += incert.pi*2
    resultat['calculs'] = calculs
    # resultat['RAf (°)'] = incert.i(360) - psif*180/incert.pi
    resultat['RAf (°)'] = psif*180/incert.pi
    resultat['DEf (°)'] = phif*180/incert.pi
    return resultat

def date(JJ):
    """
        Détermine la date du calendrier à partir du jour julien.
        La méthode suivante est valable pour les années positives aussi bien
        que négatives, mais non pour les jours juliens négatifs.
        Entrée :
            JJ le jour julien
        Retour :
            [Y, M, D]
            Y l’année
            M le numéro du mois
            D le jour du mois avec éventuellement des décimales de jour
            Erreur si :
                JJ n’est pas convertible en float
                JJ < 0
    """
    JJ = float(JJ)
    if(JJ < 0):
        message = "Cette méthode n'est pas valable pour les jours juliens"
        message += " négatifs"
        raise ValueError(message)
    JJ += 0.5
    Z = int(JJ)
    F = JJ - int(JJ)
    if (Z < 2299161):
        A = Z
    else:
        alpha = int((Z-1867216.25)/36524.25)
        A = Z + 1 + alpha - int(alpha/4)
    B = A + 1524
    C = int((B-122.1)/365.25)
    D = int(365.25*C)
    E = int((B - D)/30.6001)
    D = B - D - int(30.6001*E) + F
    if (E < 14):
        M = E - 1
    else:
        M = E - 13
    if (M > 2):
        Y = C - 4716
    else:
        Y = C - 4715
    return [Y, M, D]

def dimanchepaques(Y):
    """
        Calcul la date du jour de Pâques de l'année Y.
        Entrée :
            Y l’année
        Retour :
            [Y, M, D]
            Y l’année
            M le numéro du mois
            D le jour du mois
            Erreur si Y n’est pas convertible en entier
    """
    Y = int(Y)
    if(Y > 1582):
        a = Y % 19
        b = Y//100
        c = Y % 100
        d = b//4
        e = b % 4
        f = (b + 8)//25
        g = (b - f + 1)//3
        h = (19*a + b - d - g + 15) % 30
        i = c//4
        k = c % 4
        L = (32 + 2*e + 2*i - h - k) % 7
        m = (a + 11*h + 22*L)//451
        n = (h + L - 7*m + 114)//31
        p = (h + L - 7*m + 114) % 31
        return [Y, n, p+1]
    else:
        a = Y % 4
        b = Y % 7
        c = Y % 19
        d = (19*c + 15) % 30
        e = (2*a + 4*b - d + 34) % 7
        f = (d + e + 114) // 31
        g = (d + e + 114) % 31
        return [Y, f, g+1]

def jourannee(Y, M, D):
    """
        Détermine le numéro de jour de l'année correspondant à une date.
        Entrée :
            Y l’année
            M le numéro du mois
            D le jour du mois avec éventuellement des décimales de jour
        Retour :
            N numéro du jour de l’année
            Entre 1 et 365 pour une année régulière
            Entre 1 et 366 pour une année bissextile
            Erreur si (Y, M, D) n’est pas une date conforme
                - voir conforme(Y, M, D) -
    """
    [Y, M, D] = conforme(Y, M, D)
    if(bissextile(Y)):
        K = 1
    else:
        K = 2
    N = int(275*M/9) - K*int((M+9)/12) + int(D) - 30
    return N

def jourjulien(Y, M, D):
    """
        Détermine la valeur du jour julien qui correspond à une date donnée.
        Cette méthode est valable aussi bien pour les années positives que
        négatives, mais pas pour des jours juliens négatifs.
        Entrée :
            Y l’année
            M le numéro du mois
            D le jour du mois avec éventuellement des décimales de jour
        Retour :
            JJ jour julien
            Erreur si :
                avantjj0(Y, M, D)
                (Y, M, D) n’est pas une date conforme
                    - voir conforme(Y, M, D) –
    """
    if avantjj0(Y, M, D):
        message = "Méthode non valable pour les jours juliens négatifs"
        raise ValueError(message)
    calend = calendrier(Y, M, D)
    if(M <= 2):
        Y -= 1
        M += 12
    if(calend == "Grégorien"):
        A = int(Y/100)
        B = 2 - A + int(A/4)
    else:
        B = 0
    return int(365.25*(Y+4716))+int(30.6001*(M+1)) + D + B - 1524.5

def jourjulien0(Y):
    """
        Détermine le jour julien correspondant au 0.0 janvier de l'année Y.
        Cette méthode est valable aussi bien pour les années positives que
        négatives, mais pas pour des jours juliens négatifs.
        Entrée :
            Y l’année
        Retour :
            JJ jour julien
            Erreur si :
                Y n’est pas convertible en entier
                Y < -4711
    """
    Y = int(Y)
    return jourjulien(Y-1, 12, 31)

def jourjulienmodif(Y, M, D):
    """
        Détermine la valeur du jour julien modifié (MDJ) qui correspond
        à une date donnée.
        MDJ = JJ - 2 400 000,5
        L'origine de cette échelle est le 17 novembre 1858 à 0h.
        Cette méthode est valable aussi bien pour les années positives que
        négatives, mais pas pour des jours juliens négatifs.
        Entrée :
            Y l’année
            M le numéro du mois
            D le jour du mois avec éventuellement des décimales de jour
        Retour :
            JJ jour julien
            Erreur si :
                avantjj0(Y, M, D)
                (Y, M, D) n’est pas une date conforme
                    - voir conforme(Y, M, D) –
    """
    return jourjulien(Y, M, D) - 2400000.5

def joursemaine(Y, M, D):
    """
        Détermine le jour de la semaine correspondant à une date.
        Entrée :
            Y l’année
            M le numéro du mois
            D le jour du mois avec éventuellement des décimales de jour
        Retour :
            Jour de la semaine (lundi, mardi, ….)
            Erreur si (Y, M, D) n’est pas une date conforme
                - voir conforme(Y, M, D) –
    """
    [Y, M, D] = conforme(Y, M, D)
    JJ = jourjulien(Y, M, int(D))
    return jours_semaine[int(JJ+1.5) % 7]

def parametres_precession(t):
    """
        Calcul les paramètres de la précession approximative.
        Entrée :
            t en siècles juliens à partir de l'époque 2000.0
                t = [(JJ) - (JJ)2000.0] / 36525
        Retour :
            dictionnaire:
            m_alpha (s)
            n_alpha (s)
            n_delta (")
    """
    resultat = {}
    resultat['m_alpha (s)'] = "3.07496" + "0.00186"*t
    resultat['n_alpha (s)'] = "1.33621" - "0.00057"*t
    resultat['n_delta (")'] = "20.0431" - "0.0085"*t
    return resultat



