Help on module meeus:

NAME
    meeus

DESCRIPTION
    Implémentation des "calculs astronomiques à l'usage des amateurs"
    de Jean MEEUS, édition 2014.

FUNCTIONS
    avantJJ0(Y, M, D)
        Vérifie si une date (Y, M, D) se trouve avant le jour julien 0, c'est
        à dire avant le 1er janvier - 4712 à 12H (-4712, 1, 1.5).
        Entrée :
            Y L'année
            M le numéro du mois
            D le jour du mois avec éventuellement des décimales de jour
        Retour :
            booléen : True or False
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
        Retourne le calendrier (Julien ou Grégorien) qui correspond à une date.
        Entrée :
            Y l’année
            M le numéro du mois
            D le jour du mois avec éventuellement des décimales de jour
        Retour :
            « Julien »
            « Grégorien »
            Erreur si (Y, M, D) n’est pas une date conforme
    
    conformeInt(Y, M, D)
        Vérifie la conformité de la date proposée.
        Entrée :
            Y l’année
            M le numéro du mois
            D le jour du mois avec éventuellement des décimales de jour
        Retour :
            [Y, M, D]
            Y l’année (entière)
            M le numéro du mois (entier)
            D le jour du mois avec éventuellement des décimales de jour (float)
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
            date au format [Y, M, D]
            Y l’année
            M le numéro du mois
            D le jour du mois avec éventuellement des décimales de jour
            Erreur si :
                JJ n’est pas convertible en float
                JJ < 0
    
    dateJourAnnee(Y, N)
        Détermine la date du N^iem jour de l'année Y.
        Entrée :
            Y l’année
            N numéro du jour
        Retour :
            Date au format [Y,M,D]
    
    deltaJours(date1, date2)
        Détermine le nombre de jours entre deux dates.
        Entrée
            date1, au format [Y, M, D]
            date2, au format [Y, M, D]
        Retour
            nombre de jours
            Erreur si une date est non conforme
    
    dimanchePaques(Y)
        Calcul la date du jour de Pâques de l'année Y.
        La date de Pâques est fixée au premier dimanche après la première
        pleine lune qui suit le 21 mars, donc au plus tôt le 22/03, si la
        pleine lune tombe le soir du 21, et au plus tard le 25/04.
        Entrée :
            Y l’année
        Retour :
            date au format [Y, M, D]
            Y l’année
            M le numéro du mois
            D le jour du mois
            Erreur si Y n’est pas convertible en entier
    
    intM(nombre)
        Donne le plus grand nombre entier qui ne soit pas plus grand que le
        nombre donné.
    
    jourAnnee(Y, M, D)
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
    
    jourJulien(Y, M, D)
        Détermine la valeur du jour julien qui correspond à une date donnée.
        Cette méthode est valable aussi bien pour les années positives que
        négatives, mais pas pour des jours juliens négatifs.
        Entrée :
            (Date grégorienne ou julienne)
            Y l’année
            M le numéro du mois
            D le jour du mois avec éventuellement des décimales de jour
        Retour :
            JJ jour julien
            Erreur si :
                avantjj0(Y, M, D)
                non conformeInt(Y, M, D)
        Origine (1er janvier - 4712 à 12H) :
            jourjulien(-4712,1,1.5) = 0
    
    jourJulien0(Y)
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
    
    jourJulienModif(Y, M, D)
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
    
    jourSemaine(Y, M, D)
        Détermine le jour de la semaine correspondant à une date.
        Entrée :
            Y l’année
            M le numéro du mois
            D le jour du mois avec éventuellement des décimales de jour
        Retour :
            Jour de la semaine (lundi, mardi, ….)
            Erreur si (Y, M, D) n’est pas une date conforme
    
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
    c:\users\mc\documents\python\mes_modules\meeuscalc\meeus.py


