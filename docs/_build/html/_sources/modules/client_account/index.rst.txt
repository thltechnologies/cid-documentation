.. _client_account-index:

Comptes clients
===============

Le module **Comptes clients** est un système complet de gestion des comptes bancaires des clients qui permet la création, la gestion, le suivi et la maintenance des comptes. Il intègre la gestion des propriétaires, des soldes, des frais mensuels et des relations avec les produits bancaires.

1. Création et gestion des comptes
-----------------------------------

Cette section permet aux employés de créer, modifier et gérer les comptes bancaires des clients.

Procédure
~~~~~~~~~

1. Connectez-vous au logiciel.
2. Accédez au module **Comptes clients**.
3. Cliquez sur **Nouveau compte** pour créer un compte.

   \a. **Création d'un compte**

      Dans le formulaire de création, renseignez :
         - Le client propriétaire du compte
         - Le produit bancaire (épargne, courant, etc.)
         - Le solde initial du compte
         - L'agence d'ouverture
         - Les paramètres de retrait mensuel
         - Une description optionnelle

   \b. **Modification d'un compte**

      - Sélectionnez le compte à modifier
      - Mettez à jour les informations nécessaires
      - Sauvegardez les modifications

   \c. **Mise à jour du solde initial**

      - Ajustez le solde initial du compte
      - Le système recalcule automatiquement les soldes
      - Historique des modifications conservé

2. Gestion des propriétaires de comptes
----------------------------------------

Cette fonctionnalité permet de gérer les propriétaires multiples d'un compte bancaire.

Procédure
~~~~~~~~~

1. Connectez-vous au logiciel avec les droits appropriés.
2. Accédez au module **Comptes clients**.
3. Sélectionnez le compte concerné.

   \a. **Ajout d'un propriétaire**

      - Cliquez sur **Ajouter propriétaire**
      - Sélectionnez le client à ajouter
      - Validez l'ajout du propriétaire
      - Le client devient co-propriétaire du compte

   \b. **Suppression d'un propriétaire**

      - Sélectionnez le propriétaire à supprimer
      - Confirmez la suppression
      - Vérifiez que le compte reste valide

   \c. **Gestion des droits**

      - Définissez les droits de chaque propriétaire
      - Contrôlez les autorisations de retrait
      - Gérez les signatures multiples

3. Gestion des soldes
----------------------

Cette section permet de gérer et de suivre les soldes des comptes clients.

Procédure
~~~~~~~~~

1. Connectez-vous au logiciel.
2. Accédez au module **Comptes clients**.
3. Sélectionnez le compte concerné.

   \a. **Consultation du solde**

      - Affichage du solde actuel
      - Historique des mouvements
      - Détail des transactions

   \b. **Modification du solde**

      - Ajustement manuel du solde (avec autorisation)
      - Justification obligatoire des modifications
      - Traçabilité complète des changements

   \c. **Suivi des soldes**

      - Alertes de solde faible
      - Notifications de découvert
      - Rapports de solde

4. Frais mensuels et déductions
--------------------------------

Cette fonctionnalité gère les frais mensuels et les déductions automatiques.

Procédure
~~~~~~~~~

1. Connectez-vous au logiciel.
2. Accédez au module **Comptes clients**.
3. Configurez les paramètres de frais.

   \a. **Configuration des frais**

      - Définition des montants de frais
      - Paramétrage des dates de déduction
      - Configuration par type de compte

   \b. **Déduction automatique**

      - Traitement automatique des frais mensuels
      - Vérification des fonds disponibles
      - Gestion des comptes insuffisamment approvisionnés

   \c. **Gestion des retraits mensuels**

      - Activation/désactivation des retraits mensuels
      - Limitation des montants
      - Contrôles de sécurité

5. Gestion des comptes employés
--------------------------------

Cette section permet de gérer les comptes associés aux employés.

Procédure
~~~~~~~~~

1. Connectez-vous au logiciel avec les droits de **BRANCH_MANAGER**.
2. Accédez au module **Comptes clients**.
3. Sélectionnez l'option **Comptes employés**.

   \a. **Association de comptes**

      - Liaison d'un compte client avec un compte employé
      - Définition des relations
      - Gestion des autorisations

   \b. **Désassociation de comptes**

      - Suppression des liaisons
      - Vérification des impacts
      - Mise à jour des autorisations

6. États et statuts des comptes
--------------------------------

Cette fonctionnalité gère les différents états et statuts des comptes.

Procédure
~~~~~~~~~

1. Connectez-vous au logiciel.
2. Accédez au module **Comptes clients**.
3. Consultez la liste des comptes par état.

   \a. **États des comptes**

      - **ACTIVATED** : Compte actif et opérationnel
      - **SUSPENDED** : Compte suspendu temporairement
      - **CLOSED** : Compte fermé définitivement
      - **DELETED** : Compte supprimé du système

   \b. **Changement d'état**

      - Suspension temporaire d'un compte
      - Réactivation d'un compte suspendu
      - Fermeture définitive d'un compte
      - Justification obligatoire des changements

7. Rapports et exports
-----------------------

Cette section permet de générer des rapports et d'exporter les données des comptes.

Procédure
~~~~~~~~~

1. Connectez-vous au logiciel.
2. Accédez au module **Comptes clients**.
3. Sélectionnez l'option **Rapports**.

   \a. **Rapport de comptes par client**

      - Liste des comptes d'un client
      - Détail des soldes et transactions
      - Historique des mouvements

   \b. **Rapport de comptes par agence**

      - Comptes ouverts dans une agence
      - Statistiques de performance
      - Analyse des tendances

   \c. **Export des données**

      - Export au format Excel
      - Filtrage par critères
      - Données personnalisables

8. Intégration avec les produits bancaires
-------------------------------------------

Cette fonctionnalité gère l'intégration des comptes avec les produits bancaires.

Procédure
~~~~~~~~~

1. **Association produit-compte**

   - Liaison d'un compte avec un produit bancaire
   - Application des règles du produit
   - Configuration des paramètres

2. **Gestion des règles**

   - Application des conditions du produit
   - Calcul des intérêts et frais
   - Respect des limites et plafonds

3. **Types de produits supportés**

   - Comptes d'épargne
   - Comptes courants
   - Comptes à terme
   - Comptes spécialisés

Démo
~~~~

1. Le caissier veut créer un compte d'épargne pour le client John Doe avec un solde initial de 100 000 FCFA.

2. Le gestionnaire d'agence veut ajouter un co-propriétaire au compte #12345.

3. L'employé veut consulter le solde et l'historique du compte #67890.

4. Le système effectue automatiquement la déduction des frais mensuels sur tous les comptes éligibles.
