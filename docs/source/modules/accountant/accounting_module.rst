.. _accounting-module:

Module Comptable Complet
========================

Le **Module Comptable Complet** est une extension majeure du système de comptabilité de CID Core Banking. Il fournit un système comptable complet conforme aux standards de la finance islamique, avec toutes les fonctionnalités nécessaires pour la gestion comptable d'une institution financière.

Vue d'ensemble
--------------

Le module comptable complet comprend :

- **Plan Comptable** : Structure hiérarchique des comptes
- **Exercices Comptables** : Gestion des exercices fiscaux avec périodes mensuelles
- **Grand Livre Général** : Enregistrement de toutes les transactions comptables
- **Balance de Vérification** : Vérification de l'équilibre comptable
- **États Financiers** : Génération automatique des états financiers
- **Réconciliation Bancaire** : Pointage et réconciliation des comptes bancaires

Architecture
------------

Le module est structuré en deux parties principales :

**Backend (Java/Spring Boot)**
  - 9 entités JPA pour la persistance des données
  - 7 services métier avec logique complète
  - 7 controllers REST avec 50+ endpoints API
  - DTOs et mappings pour la transformation des données

**Frontend (Angular)**
  - 6 composants UI avec interfaces PrimeNG
  - 7 services Angular pour l'intégration API
  - 8 modèles TypeScript avec FormGroups
  - 4 enums avec fonctions de traduction

1. Plan Comptable
------------------

Le plan comptable permet de définir la structure hiérarchique de tous les comptes utilisés dans le système comptable.

Fonctionnalités
~~~~~~~~~~~~~~~

- **Structure hiérarchique** : Comptes parent/enfant pour organisation
- **Types de comptes** : ASSET, LIABILITY, EQUITY, REVENUE, EXPENSE
- **Intégration avec classes comptables** : Liaison avec les classes existantes
- **Comptes système** : Protection des comptes système contre modification
- **Recherche et filtrage** : Recherche par code, libellé, type

Procédure
~~~~~~~~~

1. Connectez-vous au logiciel avec les droits comptable.
2. Accédez au module **Comptabilité** > **Plan Comptable**.

   a. **Créer un compte**

      - Cliquez sur **Nouveau Compte**
      - Remplissez les informations :
        - Code du compte (ex: 1000, 1100)
        - Libellé du compte
        - Type de compte (Actif, Passif, etc.)
        - Compte parent (optionnel)
        - Classe comptable (optionnel)
        - Description
      - Cliquez sur **Enregistrer**

   b. **Modifier un compte**

      - Sélectionnez le compte dans la liste
      - Cliquez sur l'icône **Modifier**
      - Modifiez les informations nécessaires
      - Cliquez sur **Enregistrer**

   c. **Rechercher un compte**

      - Utilisez la barre de recherche en haut
      - Recherchez par code, libellé ou description
      - Les résultats sont filtrés automatiquement

Structure hiérarchique
~~~~~~~~~~~~~~~~~~~~~~

Le plan comptable supporte une structure hiérarchique :

::

   1000 - Actifs
   ├── 1100 - Actifs courants
   │   ├── 1110 - Caisse
   │   ├── 1120 - Banques
   │   └── 1130 - Clients
   └── 1200 - Actifs non courants
        ├── 1210 - Immobilisations
        └── 1220 - Investissements

2. Exercices Comptables
------------------------

Les exercices comptables permettent de définir les périodes fiscales et de gérer les clôtures comptables.

Fonctionnalités
~~~~~~~~~~~~~~~

- **Création d'exercices** : Définition des exercices avec dates de début/fin
- **Création automatique de périodes** : Génération automatique de 12 périodes mensuelles
- **Activation/désactivation** : Gestion de l'exercice actif
- **Clôture d'exercice** : Clôture avec validation de toutes les périodes

Procédure
~~~~~~~~~

1. Connectez-vous au logiciel.
2. Accédez au module **Comptabilité** > **Exercices Comptables**.

   a. **Créer un exercice**

      - Cliquez sur **Nouvel Exercice**
      - Remplissez les informations :
        - Nom de l'exercice (ex: FY2025)
        - Date de début (ex: 01/01/2025)
        - Date de fin (ex: 31/12/2025)
        - Notes (optionnel)
      - Cliquez sur **Enregistrer**
      - Le système crée automatiquement 12 périodes mensuelles

   b. **Activer un exercice**

      - Sélectionnez l'exercice dans la liste
      - Cliquez sur l'icône **Activer**
      - L'exercice précédent est automatiquement désactivé

   c. **Clôturer un exercice**

      - Vérifiez que toutes les périodes sont clôturées
      - Sélectionnez l'exercice
      - Cliquez sur l'icône **Clôturer**
      - L'exercice est clôturé et ne peut plus être modifié

Périodes mensuelles
~~~~~~~~~~~~~~~~~~~

Lors de la création d'un exercice, le système génère automatiquement 12 périodes mensuelles :

- Janvier 2025 (Période 1)
- Février 2025 (Période 2)
- ...
- Décembre 2025 (Période 12)

Chaque période peut être clôturée individuellement.

3. Grand Livre Général
----------------------

Le grand livre général enregistre toutes les transactions comptables et permet de suivre l'évolution de chaque compte.

Fonctionnalités
~~~~~~~~~~~~~~~

- **Génération automatique** : Création depuis les écritures comptables
- **Consultation par compte** : Filtrage par compte spécifique
- **Consultation par période** : Filtrage par période comptable
- **Consultation par date** : Filtrage par plage de dates
- **Calcul des soldes** : Calcul automatique du solde de chaque compte

Procédure
~~~~~~~~~

1. Connectez-vous au logiciel.
2. Accédez au module **Comptabilité** > **Grand Livre**.

   a. **Consulter le grand livre**

      - Sélectionnez un compte (optionnel)
      - Sélectionnez une période (optionnel)
      - Définissez une plage de dates
      - Cliquez sur **Rechercher**
      - Le grand livre s'affiche avec toutes les transactions

   b. **Générer le grand livre pour une période**

      - Sélectionnez une période
      - Cliquez sur **Générer**
      - Le système génère automatiquement toutes les entrées depuis les écritures comptables

Structure du grand livre
~~~~~~~~~~~~~~~~~~~~~~~~

Chaque ligne du grand livre contient :

- **Date** : Date de la transaction
- **Compte** : Code et libellé du compte
- **Référence** : Référence de l'écriture comptable
- **Description** : Description de la transaction
- **Débit** : Montant débité
- **Crédit** : Montant crédité
- **Solde** : Solde cumulé du compte

4. Balance de Vérification
---------------------------

La balance de vérification permet de vérifier l'équilibre comptable et de préparer les états financiers.

Fonctionnalités
~~~~~~~~~~~~~~~

- **Calcul automatique** : Calcul basé sur le grand livre
- **Soldes d'ouverture** : Récupération depuis la période précédente
- **Soldes de période** : Calcul des mouvements de la période
- **Soldes de clôture** : Calcul des soldes finaux
- **Validation équilibre** : Vérification que débit = crédit

Procédure
~~~~~~~~~

1. Connectez-vous au logiciel.
2. Accédez au module **Comptabilité** > **Balance de Vérification**.

   a. **Calculer la balance**

      - Sélectionnez une période comptable
      - Cliquez sur **Calculer**
      - Le système calcule automatiquement :
        - Soldes d'ouverture
        - Mouvements de la période (débit/crédit)
        - Soldes de clôture
        - Solde net de chaque compte

   b. **Vérifier l'équilibre**

      - Le système vérifie automatiquement que :
        - Total débit = Total crédit
      - Un indicateur visuel affiche si la balance est équilibrée

Structure de la balance
~~~~~~~~~~~~~~~~~~~~~~~~

La balance affiche pour chaque compte :

- **Code et libellé** : Identification du compte
- **Débit ouverture** : Solde débiteur au début de la période
- **Crédit ouverture** : Solde créditeur au début de la période
- **Débit période** : Total des débits de la période
- **Crédit période** : Total des crédits de la période
- **Débit clôture** : Solde débiteur à la fin de la période
- **Crédit clôture** : Solde créditeur à la fin de la période
- **Solde net** : Solde net (débit - crédit)

5. États Financiers
--------------------

Les états financiers permettent de générer automatiquement les documents comptables officiels.

Fonctionnalités
~~~~~~~~~~~~~~~

- **Bilan** : État de la situation financière
- **Compte de résultat** : Résultat d'exploitation
- **Tableau de flux de trésorerie** : Mouvements de trésorerie
- **Approbation** : Workflow d'approbation
- **Finalisation** : Verrouillage des états approuvés

Procédure
~~~~~~~~~

1. Connectez-vous au logiciel.
2. Accédez au module **Comptabilité** > **États Financiers**.

   a. **Générer un bilan**

      - Sélectionnez un exercice comptable
      - Sélectionnez une période (optionnel, pour bilan intermédiaire)
      - Cliquez sur **Générer Bilan**
      - Le système génère automatiquement le bilan avec :
        - Actifs (courants et non courants)
        - Passifs (courants et non courants)
        - Capitaux propres

   b. **Générer un compte de résultat**

      - Sélectionnez un exercice comptable
      - Sélectionnez une période (optionnel)
      - Cliquez sur **Générer Compte de Résultat**
      - Le système génère automatiquement :
        - Produits d'exploitation
        - Charges d'exploitation
        - Résultat net

   c. **Générer un tableau de flux de trésorerie**

      - Sélectionnez un exercice comptable
      - Sélectionnez une période (optionnel)
      - Cliquez sur **Générer Flux de Trésorerie**
      - Le système génère automatiquement :
        - Flux d'exploitation
        - Flux d'investissement
        - Flux de financement

   d. **Approuver un état financier**

      - Sélectionnez l'état financier dans la liste
      - Cliquez sur l'icône **Approuver**
      - L'état est marqué comme approuvé

   e. **Finaliser un état financier**

      - L'état doit être approuvé au préalable
      - Cliquez sur l'icône **Finaliser**
      - L'état est verrouillé et ne peut plus être modifié

Types d'états financiers
~~~~~~~~~~~~~~~~~~~~~~~~~

**Bilan (Balance Sheet)**
  - Actifs = Passifs + Capitaux propres
  - Vue instantanée de la situation financière

**Compte de Résultat (Income Statement)**
  - Produits - Charges = Résultat net
  - Performance sur une période

**Tableau de Flux de Trésorerie (Cash Flow Statement)**
  - Flux d'exploitation
  - Flux d'investissement
  - Flux de financement

6. Réconciliation Bancaire
---------------------------

La réconciliation bancaire permet de comparer les relevés bancaires avec les enregistrements comptables.

Fonctionnalités
~~~~~~~~~~~~~~~

- **Création de réconciliations** : Pour chaque compte bancaire et période
- **Pointage automatique** : Correspondance automatique des transactions
- **Pointage manuel** : Pointage manuel des transactions non correspondantes
- **Calcul des écarts** : Calcul automatique des différences
- **Validation** : Finalisation de la réconciliation

Procédure
~~~~~~~~~

1. Connectez-vous au logiciel.
2. Accédez au module **Comptabilité** > **Réconciliation Bancaire**.

   a. **Créer une réconciliation**

      - Cliquez sur **Nouvelle Réconciliation**
      - Sélectionnez le compte bancaire
      - Sélectionnez la période comptable
      - Entrez la date du relevé bancaire
      - Entrez le solde du relevé bancaire
      - Cliquez sur **Enregistrer**

   b. **Pointage automatique**

      - Sélectionnez la réconciliation
      - Cliquez sur **Pointage Automatique**
      - Le système compare automatiquement :
        - Les transactions bancaires avec les écritures comptables
        - Les montants et dates
        - Les références

   c. **Pointage manuel**

      - Pour chaque transaction non pointée :
        - Vérifiez la correspondance
        - Cliquez sur **Pointer** si correspondance trouvée
        - Ajoutez des notes si nécessaire

   d. **Finaliser la réconciliation**

      - Vérifiez que tous les écarts sont expliqués
      - Vérifiez que le solde réconcilié correspond
      - Cliquez sur **Finaliser**
      - La réconciliation est verrouillée

Types d'écarts
~~~~~~~~~~~~~~

**Dépôts en transit**
  - Dépôts enregistrés en comptabilité mais pas encore au relevé bancaire

**Chèques en circulation**
  - Chèques émis mais pas encore encaissés

**Erreurs bancaires**
  - Erreurs dans le relevé bancaire

**Erreurs comptables**
  - Erreurs dans les enregistrements comptables

**Intérêts et frais**
  - Intérêts créditeurs
  - Frais bancaires

Conformité Finance Islamique
-----------------------------

Le module comptable est conçu pour supporter les spécificités de la finance islamique :

- **Séparation des fonds** : Comptes séparés pour fonds islamiques et conventionnels
- **Comptabilisation spécifique** : Support pour Murabaha, Ijara, Musharaka
- **Conformité AAOIFI** : Structure prête pour conformité Accounting and Auditing Organization for Islamic Financial Institutions
- **Traçabilité complète** : Traçabilité de toutes les opérations conformes à la Sharia

API REST
--------

Le module expose 50+ endpoints API REST pour toutes les fonctionnalités :

**Plan Comptable**
  - ``POST /chart-of-accounts`` - Créer un compte
  - ``PUT /chart-of-accounts/{id}`` - Modifier un compte
  - ``GET /chart-of-accounts`` - Lister tous les comptes
  - ``GET /chart-of-accounts/{id}`` - Obtenir un compte

**Exercices Comptables**
  - ``POST /fiscal-years`` - Créer un exercice
  - ``POST /fiscal-years/{id}/activate`` - Activer un exercice
  - ``POST /fiscal-years/{id}/close`` - Clôturer un exercice

**Grand Livre**
  - ``GET /general-ledger/account/{accountId}`` - Grand livre par compte
  - ``GET /general-ledger/period/{periodId}`` - Grand livre par période
  - ``POST /general-ledger/period/{periodId}/generate`` - Générer le grand livre

**Balance de Vérification**
  - ``POST /trial-balance/period/{periodId}/calculate`` - Calculer la balance
  - ``GET /trial-balance/period/{periodId}`` - Obtenir la balance

**États Financiers**
  - ``POST /financial-statements/balance-sheet/fiscal-year/{fiscalYearId}`` - Générer le bilan
  - ``POST /financial-statements/income-statement/fiscal-year/{fiscalYearId}`` - Générer le compte de résultat
  - ``POST /financial-statements/{id}/approve`` - Approuver un état

**Réconciliation Bancaire**
  - ``POST /bank-reconciliations`` - Créer une réconciliation
  - ``POST /bank-reconciliations/{id}/auto-match`` - Pointage automatique
  - ``POST /bank-reconciliations/{id}/reconcile`` - Finaliser la réconciliation

Statistiques
------------

**Backend**
  - 9 entités JPA
  - 7 services métier
  - 7 controllers REST
  - 50+ endpoints API
  - ~5000+ lignes de code Java

**Frontend**
  - 6 composants Angular
  - 7 services Angular
  - 8 modèles TypeScript
  - 4 enums TypeScript
  - ~2000+ lignes de code TypeScript

**Total**
  - ~75 fichiers créés
  - ~7000+ lignes de code
  - Module comptable complet et opérationnel

