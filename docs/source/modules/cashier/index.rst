.. _cashier-index:

Caissier et Billetage
=====================

Le module **Caissier et Billetage** gère toutes les opérations de caisse et de gestion des espèces. Il permet aux caissiers d'ouvrir leur caisse, d'effectuer des opérations de dépôt et retrait, de gérer les billets et pièces, et de fermer leur caisse en fin de journée avec les contrôles de conformité appropriés.

1. Ouverture de caisse
-----------------------

Cette procédure permet au caissier d'ouvrir sa caisse au début de la journée de travail.

Procédure
~~~~~~~~~

1. Connectez-vous au système avec vos identifiants de caissier.
2. Accédez au module **Caissier et Billetage**.
3. Cliquez sur **Ouvrir la caisse**.
4. Le système vérifie qu'aucune caisse n'est déjà ouverte pour vous.
5. Sélectionnez le compte de caisse interne (box) à utiliser.
6. Confirmez l'ouverture de la caisse.

**Résultat :** Votre caisse est ouverte et prête pour les opérations de la journée.

2. Gestion des billets et espèces
----------------------------------

Cette fonctionnalité permet de gérer l'inventaire des billets et pièces en caisse.

Procédure
~~~~~~~~~

1. Accédez à la section **Gestion des billets**.
2. Consultez l'inventaire actuel des espèces :

   **Billets :**
   - 10 000 FCFA
   - 5 000 FCFA
   - 2 000 FCFA
   - 1 000 FCFA
   - 500 FCFA

   **Pièces :**
   - 250 FCFA
   - 200 FCFA
   - 100 FCFA
   - 50 FCFA
   - 25 FCFA
   - 10 FCFA
   - 5 FCFA

3. Mettez à jour les quantités selon les besoins :

   **Pour ajouter des espèces :**
   - Saisissez les quantités positives
   - Confirmez la mise à jour

   **Pour retirer des espèces :**
   - Saisissez les quantités négatives
   - Le système vérifie la disponibilité
   - Confirmez la mise à jour

**Contrôles automatiques :**
- Vérification de la disponibilité des espèces
- Calcul automatique du total en caisse
- Alerte en cas de manque d'espèces

3. Opérations de transaction
-----------------------------

Cette section permet d'effectuer les opérations de dépôt et retrait avec gestion automatique des espèces.

Procédure de dépôt
~~~~~~~~~~~~~~~~~~

1. Cliquez sur **Dépôt à l'agence**.
2. Sélectionnez le compte client destinataire.
3. Saisissez le montant à déposer.
4. Le système calcule automatiquement la répartition en billets.
5. Ajustez manuellement si nécessaire :

   **Exemple :** Dépôt de 25 000 FCFA
   - 2 × 10 000 FCFA = 20 000 FCFA
   - 1 × 5 000 FCFA = 5 000 FCFA
   - **Total :** 25 000 FCFA

6. Confirmez l'opération.
7. Le système met à jour automatiquement :
   - Le solde du compte client
   - L'inventaire des espèces en caisse
   - Les écritures comptables

Procédure de retrait
~~~~~~~~~~~~~~~~~~~~

1. Cliquez sur **Retrait à l'agence**.
2. Sélectionnez le compte client.
3. Saisissez le montant à retirer.
4. Vérifiez la disponibilité des fonds du client.
5. Le système vérifie la disponibilité des espèces en caisse.
6. Ajustez la répartition des billets si nécessaire.
7. Confirmez l'opération.
8. Le système met à jour automatiquement :
   - Le solde du compte client
   - L'inventaire des espèces en caisse
   - Les écritures comptables

**Contrôles de sécurité :**
- Vérification du solde client
- Vérification de la disponibilité des espèces
- Limites de retrait selon le produit bancaire
- Traçabilité complète des opérations

4. Fermeture de caisse
-----------------------

Cette procédure permet de fermer la caisse en fin de journée avec les contrôles de conformité.

Procédure
~~~~~~~~~

1. Accédez à la section **Fermeture de caisse**.
2. Le système affiche le récapitulatif de la journée :

   **Résumé des opérations :**
   - Nombre total de transactions
   - Montant total des dépôts
   - Montant total des retraits
   - Solde théorique de la caisse

3. Saisissez l'inventaire final des espèces :

   **Vérification manuelle :**
   - Comptez physiquement chaque type de billet/pièce
   - Saisissez les quantités réelles
   - Le système calcule le total

4. Le système effectue les contrôles de conformité :

   **Contrôles automatiques :**
   - Comparaison solde théorique vs inventaire réel
   - Vérification des écarts (excédents/déficits)
   - Validation des montants

5. En cas d'écart :

   **Excédent :**
   - Saisissez la justification
   - Enregistrez l'excédent
   - Le système génère un rapport

   **Déficit :**
   - Saisissez la justification
   - Enregistrez le déficit
   - Le système génère un rapport d'incident

6. Confirmez la fermeture de la caisse.
7. Le système génère automatiquement :
   - Rapport de fermeture de caisse
   - Écritures comptables de clôture
   - Historique des opérations

5. Rapports et contrôles
-------------------------

Cette section fournit les rapports et outils de contrôle pour la gestion de caisse.

Rapports disponibles
~~~~~~~~~~~~~~~~~~~~

**Rapport de caisse quotidien :**
- Résumé des opérations de la journée
- Détail des dépôts et retraits
- Inventaire des espèces
- Écarts et justifications

**Rapport de conformité :**
- Comparaison solde théorique vs réel
- Historique des écarts
- Tendances et analyses

**Rapport de transaction :**
- Liste détaillée des opérations
- Filtres par période, montant, type
- Export en Excel/PDF

Contrôles de sécurité
~~~~~~~~~~~~~~~~~~~~~

**Contrôles automatiques :**
- Vérification des autorisations caissier
- Validation des montants et limites
- Contrôle de cohérence des espèces
- Traçabilité complète des opérations

**Alertes et notifications :**
- Manque d'espèces en caisse
- Écarts importants détectés
- Opérations suspectes
- Rappels de fermeture de caisse

6. Gestion des autorisations
-----------------------------

Cette section couvre la gestion des droits d'accès pour les opérations de caisse.

Rôles et permissions
~~~~~~~~~~~~~~~~~~~~

**Caissier (CASHIER) :**
- Ouverture/fermeture de caisse
- Opérations de dépôt et retrait
- Gestion des espèces
- Consultation des rapports

**Superviseur de caisse :**
- Validation des fermetures de caisse
- Consultation de tous les rapports
- Gestion des autorisations
- Résolution des écarts

**Administrateur :**
- Configuration des comptes de caisse
- Gestion des utilisateurs
- Paramétrage des contrôles
- Accès à tous les rapports

Sécurité des opérations
~~~~~~~~~~~~~~~~~~~~~~~

**Authentification :**
- Connexion obligatoire avec identifiants
- Session limitée dans le temps
- Déconnexion automatique après inactivité

**Autorisation :**
- Vérification des droits pour chaque opération
- Limitation par agence
- Contrôle des montants selon le rôle

**Audit :**
- Enregistrement de toutes les actions
- Horodatage précis des opérations
- Traçabilité des modifications
- Rapports d'audit détaillés

7. Intégration avec les autres modules
---------------------------------------

Le module Caissier s'intègre parfaitement avec les autres modules du système.

Modules intégrés
~~~~~~~~~~~~~~~~

**Module Comptabilité :**
- Génération automatique des écritures
- Intégration au grand livre
- Rapports comptables de caisse

**Module Transactions :**
- Enregistrement des opérations
- Gestion des frais et commissions
- Historique des transactions

**Module Agence :**
- Gestion par agence
- Contrôles hiérarchiques
- Rapports consolidés

**Module Clients :**
- Vérification des comptes clients
- Historique des opérations
- Limites et autorisations

8. Cas d'usage et exemples
---------------------------

Cette section présente des exemples concrets d'utilisation du module.

Scénario 1 : Ouverture de caisse
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Contexte :** Caissier débutant sa journée de travail.

**Étapes :**

1. Connexion au système à 8h00
2. Ouverture de la caisse avec 50 000 FCFA d'espèces
3. Répartition initiale :
   - 4 × 10 000 FCFA = 40 000 FCFA
   - 2 × 5 000 FCFA = 10 000 FCFA
4. Confirmation de l'ouverture
5. Prêt pour les opérations de la journée

Scénario 2 : Dépôt client
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Contexte :** Client effectuant un dépôt de 75 000 FCFA.

**Étapes :**

1. Sélection du compte client #12345
2. Saisie du montant : 75 000 FCFA
3. Répartition automatique :
   - 7 × 10 000 FCFA = 70 000 FCFA
   - 1 × 5 000 FCFA = 5 000 FCFA
4. Vérification et confirmation
5. Mise à jour automatique :
   - Solde client : +75 000 FCFA
   - Espèces en caisse : +75 000 FCFA
   - Écritures comptables générées

Scénario 3 : Retrait client
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Contexte :** Client effectuant un retrait de 30 000 FCFA.

**Étapes :**

1. Sélection du compte client #67890
2. Vérification du solde disponible
3. Saisie du montant : 30 000 FCFA
4. Vérification des espèces disponibles
5. Répartition :
   - 3 × 10 000 FCFA = 30 000 FCFA
6. Confirmation et remise des espèces
7. Mise à jour automatique :
   - Solde client : -30 000 FCFA
   - Espèces en caisse : -30 000 FCFA
   - Écritures comptables générées

Scénario 4 : Fermeture de caisse
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Contexte :** Fin de journée, fermeture de caisse.

**Étapes :**

1. Accès à la fermeture de caisse à 17h00
2. Récapitulatif de la journée :
   - 25 dépôts : 1 250 000 FCFA
   - 18 retraits : 900 000 FCFA
   - Solde théorique : 400 000 FCFA
3. Inventaire physique :
   - 40 × 10 000 FCFA = 400 000 FCFA
4. Vérification : Conforme ✓
5. Confirmation de fermeture
6. Génération du rapport de caisse

9. Dépannage et support
------------------------

Cette section aide à résoudre les problèmes courants.

Problèmes fréquents
~~~~~~~~~~~~~~~~~~~

**Erreur : "Aucun billetage trouvé"**
- **Cause :** Caisse non ouverte
- **Solution :** Ouvrir la caisse avant les opérations

**Erreur : "Manque de X FCFA dans le billetage"**
- **Cause :** Espèces insuffisantes en caisse
- **Solution :** Approvisionner la caisse ou ajuster la répartition

**Erreur : "Le montant du billetage ne correspond pas"**
- **Cause :** Écart entre solde théorique et inventaire
- **Solution :** Vérifier l'inventaire et justifier les écarts

**Erreur : "Vous n'êtes pas affecté à une agence"**
- **Cause :** Caissier non assigné à une agence
- **Solution :** Contacter l'administrateur pour l'affectation

Contact support
~~~~~~~~~~~~~~~

**Support technique :**
- Email : support@thltechnologies.com
- Téléphone : +237 XXX XX XX XX
- Horaires : 8h00 - 18h00 (Lun-Ven)

**Documentation :**
- Guide utilisateur complet
- Vidéos de formation
- FAQ en ligne
- Base de connaissances

.. toctree::
   :maxdepth: 1
   :caption: 📋 Documentation détaillée

   all_features
   new_features
