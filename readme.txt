Help on module meeus:

NAME
    meeus

DESCRIPTION
    Implémentation des "calculs astronomiques à l'usage des amateurs"
    de Jean MEEUS, édition 2014.

FUNCTIONS
    avantjj0(Y, M, D)
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
    
    bissextile(Y)
        Vérifie si une année Y est bissextile.
        Entrée :
            Y l’année
        Retour :
            True
            False
            Erreur si Y n’est pas convertible en entier
    
    calendrier(Y, M, D)
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
    
    conforme(Y, M, D)
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
    
    coordonnees_moyennes(HR, A)
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
    
    coordonnees_moyennes2(HR, A)
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
    
    coordonnees_moyennes3(HR, A)
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
    
    coordonnees_moyennes_rigoureuses(HR, A)
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
    
    date(JJ)
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
    
    dimanchepaques(Y)
        Calcul la date du jour de Pâques de l'année Y.
        Entrée :
            Y l’année
        Retour :
            [Y, M, D]
            Y l’année
            M le numéro du mois
            D le jour du mois
            Erreur si Y n’est pas convertible en entier
    
    jourannee(Y, M, D)
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
    
    jourjulien(Y, M, D)
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
    
    jourjulien0(Y)
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
    
    jourjulienmodif(Y, M, D)
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
    
    joursemaine(Y, M, D)
        Détermine le jour de la semaine correspondant à une date.
        Entrée :
            Y l’année
            M le numéro du mois
            D le jour du mois avec éventuellement des décimales de jour
        Retour :
            Jour de la semaine (lundi, mardi, ….)
            Erreur si (Y, M, D) n’est pas une date conforme
                - voir conforme(Y, M, D) –
    
    parametres_precession(t)
        Calcul les paramètres de la précession approximative.
        Entrée :
            t en siècles juliens à partir de l'époque 2000.0
                t = [(JJ) - (JJ)2000.0] / 36525
        Retour :
            dictionnaire:
            m_alpha (s)
            n_alpha (s)
            n_delta (")

DATA
    jours_semaine = {0: 'dimanche', 1: 'lundi', 2: 'mardi', 3: 'mercredi',...

FILE
    c:\users\mc\mu_code\_mes_modules\meeuscalc\meeus.py


