.. _accountant-index:

Comptabilité
============

Le module **Comptabilité** regroupe les différentes options destinées aux comptables, notamment :

1. Opérations sur les comptes internes
--------------------------------------

Cette section permet de gérer les transactions liées aux comptes internes de CID, telles que les transferts entre comptes ou le suivi des soldes. Elle offre aux comptables les outils nécessaires pour une gestion efficace des flux financiers internes.

Procédure
~~~~~~~~~

1. Connectez-vous au logiciel.
2. Cliquez sur le module **Comptabilité** : vous serez automatiquement redirigé vers l’option **Opérations sur les comptes internes**.

   \a. **Transfert d’argent entre deux comptes internes**

      Dans le formulaire en haut de la page, sélectionnez :
        - Le compte interne source (depuis lequel l’argent sera débité)
        - Le compte interne cible (vers lequel l’argent sera transféré)
        - Le montant à transférer
        - Vous pouvez ajouter une description (optionnelle) à la transaction, puis cliquez sur le bouton **Enregistrer**.

   \b. **Historique des transactions**

      Sur la page des opérations sur les comptes internes, vous trouverez l’historique des transactions. Il est possible de :
        - Trier les transactions par intervalle de dates
        - Rechercher une transaction par montant, nom de l’agence, etc.

Démo
~~~~

1. Le comptable John Comptable veut transférer 2 500 FCFA du compte interne des frais de l'agence 02 vers le compte interne des frais de l'agence 01.

.. video:: ../../_static/videos/accountant/accountant_demo.mp4
    :autoplay:
    :caption: Opérations sur les comptes internes

2. Le comptable John Comptable veut afficher l'historique des transactions des comptes internes qui ont lieu le mois de Janvier 2025.

.. video:: ../../_static/videos/accountant/accountant_history.mp4
    :autoplay:
    :caption: Historiques des opérations sur les comptes internes


2. Prélèvement des capitaux
---------------------------

Cette fonctionnalité est dédiée à la gestion des opérations de prélèvement et d’investissement de capitaux. Elle permet de suivre et d’enregistrer les mouvements financiers liés aux parts sociales, aux actions ou à tout autre type de capital détenu par les parties prenantes de CID.

Procédure
~~~~~~~~~

1. Connectez-vous au logiciel.
2. Cliquez sur le module **Comptabilité**.
3. Cliquez sur le menu **Prélèvement des capitaux**.

   \a. **Transfert de capitaux**

      Cliquez sur le bouton **Prélever** (en haut, à gauche de la page). Dans le formulaire qui s’affiche, saisissez :
         - Le code KYC du client
         - Le compte interne des capitaux concerné
         - Le montant à prélever
         - Une description de la transaction (optionnelle)
         - Cliquez sur le bouton **Prélever** pour finaliser l’opération de prélèvement.

   \b. **Historique des transactions**

      Sur la page **Prélèvements des capitaux**, vous trouverez l’historique des transactions. Il est possible de :
         - Trier les transactions par intervalle de dates
         - Rechercher une transaction par montant, nom de l’agence, etc.

Démo
~~~~

1. Le comptable John Comptable veut prélever 200 000 FCFA au compte client (kyc: 00001-01234-01234567-08) pour le compte des capitaux 01 de l'agence 01.

.. video:: ../../_static/videos/accountant/capital_withdrawal_demo.mp4
    :autoplay:
    :caption: Prélèvement des capitaux

2. Le comptable John Comptable veut afficher l'historique des transactions de prélèvement de capitaux du mois de Janvier 2025 dont le montant est 200 000  FCFA.

.. video:: ../../_static/videos/accountant/capital_withdrawal_history.mp4
    :autoplay:
    :caption: Historiques des prélèvements de capitaux


3. Traitement des écritures comptables
---------------------------------------

Cette fonctionnalité permet la gestion automatisée et optimisée des écritures comptables avec un nouveau système de composants de transaction. Elle améliore significativement les performances et la traçabilité des opérations comptables.

Procédure
~~~~~~~~~

1. Connectez-vous au logiciel.
2. Accédez au module **Comptabilité**.
3. Le système traite automatiquement les écritures comptables via le nouveau système de composants.

   \a. **Traitement par lots des écritures**

      Le système utilise un traitement par lots optimisé qui :
         - Traite les transactions non encore comptabilisées
         - Crée une seule écriture comptable par transaction avec plusieurs lignes
         - Améliore les performances de traitement
         - Assure la traçabilité complète

   \b. **Reprocessing des écritures**

      En cas de besoin, le système permet de :
         - Reprocesser les écritures existantes
         - Mettre à jour les composants de transaction
         - Maintenir la cohérence des données comptables

   \c. **Composants de transaction**

      Le nouveau système gère différents types de composants :
         - Marge (MARGIN)
         - TAF (Taxe sur les Activités Financières)
         - Frais de communication
         - Frais de transport
         - Frais administratifs
         - Frais d'assurance
         - Et autres frais spécialisés

4. Génération du grand livre
-----------------------------

Cette fonctionnalité permet de générer et consulter le grand livre des comptes avec des filtres avancés.

Procédure
~~~~~~~~~

1. Connectez-vous au logiciel.
2. Accédez au module **Comptabilité**.
3. Sélectionnez **Grand livre** dans le menu.

   \a. **Consultation du grand livre**

      - Sélectionnez le compte concerné
      - Définissez la période (date de début et de fin)
      - Le système génère automatiquement le grand livre

   \b. **Filtres disponibles**

      - Filtrage par compte spécifique
      - Filtrage par période
      - Filtrage par type de transaction
      - Export des données au format Excel

5. Module Comptable Complet
----------------------------

Le module comptable complet fournit un système comptable complet avec toutes les fonctionnalités nécessaires pour la gestion comptable d'une institution financière.

5. Guide Utilisateur Complet (A-Z)
-----------------------------------

Pour une documentation complète de A à Z sur l'utilisation du module comptable, consultez le guide utilisateur complet qui couvre toutes les fonctionnalités étape par étape.

.. toctree::
   :maxdepth: 2
   :caption: Documentation Complète

   user_guide
   accounting_module