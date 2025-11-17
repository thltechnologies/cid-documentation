.. _loan-index:

Prêts
=====

Le module **Prêts** est un système complet de gestion des prêts qui permet la création, l'approbation, le suivi et le remboursement des prêts accordés aux clients. Il intègre un système de tarification avancé, des échéanciers flexibles et une gestion automatisée des remboursements.

.. note::
   **Mises à jour importantes - Octobre 2025**
   
   Le module prêts a bénéficié de corrections critiques et d'améliorations majeures :
   
   - ✅ Migration complète vers le système de composants de transaction
   - ✅ Correction des calculs financiers avec protection contre les divisions par zéro
   - ✅ Amélioration de la précision des échéanciers pour tous les types d'échéances
   - ✅ Renforcement des validations et de la sécurité des données
   - ✅ Correction des rapports et exports Excel
   
   Ces améliorations garantissent une meilleure fiabilité et précision du système.

1. Création et gestion des prêts
---------------------------------

Cette section permet aux gestionnaires de prêts de créer, modifier et gérer les prêts accordés aux clients.

Procédure
~~~~~~~~~

1. Connectez-vous au logiciel.
2. Accédez au module **Prêts**.
3. Cliquez sur **Nouveau prêt** pour créer un prêt.

   \a. **Création d'un prêt**

      Dans le formulaire de création, renseignez :
         - Le type de prêt (Murabaha, Ijara, Musharaka, Qard, etc.)
         - Le client bénéficiaire
         - Le montant du prêt (prix d'achat + marge + TAF)
         - La date de livraison
         - La date du premier remboursement
         - Le type d'échéance (mensuel, trimestriel, etc.)
         - Le type de remboursement (linéaire, personnalisé)
         - Une description du prêt

   \b. **Modification d'un prêt**

      - Sélectionnez le prêt à modifier
      - Mettez à jour les informations nécessaires
      - Sauvegardez les modifications

   \c. **Mise à jour du produit de prêt**

      - Modifiez le produit associé au prêt
      - Ajustez les paramètres de tarification
      - Mettez à jour les conditions contractuelles

2. Approbation des prêts
-------------------------

Cette fonctionnalité permet aux validateurs de prêts d'approuver ou de rejeter les demandes de prêt.

Procédure
~~~~~~~~~

1. Connectez-vous au logiciel avec les droits de **LOAN_VALIDATOR**.
2. Accédez au module **Prêts**.
3. Consultez la liste des prêts en attente d'approbation.

   \a. **Processus d'approbation**

      - Examinez les détails du prêt
      - Vérifiez la solvabilité du client
      - Validez les conditions contractuelles
      - Approuvez ou rejetez la demande

   \b. **Contrôles de sécurité**

      - Vérification des autorisations
      - Validation des montants
      - Contrôle de cohérence des données

3. Gestion des remboursements
------------------------------

Cette section permet de gérer les échéances et les remboursements des prêts.

Procédure
~~~~~~~~~

1. Connectez-vous au logiciel.
2. Accédez au module **Prêts**.
3. Sélectionnez le prêt concerné.

   \a. **Création d'un remboursement**

      - Cliquez sur **Nouveau remboursement**
      - Renseignez le montant à rembourser
      - Définissez la période
      - Spécifiez la date de paiement

   \b. **Confirmation des remboursements**

      - Vérifiez les détails du remboursement
      - Confirmez le paiement
      - Le système génère automatiquement les transactions

   \c. **Remboursements personnalisés**

      - Créez des remboursements sur mesure
      - Ajustez les montants selon les besoins
      - Gérez les reports d'échéances

   \d. **Gestion des retards**

      - Identification automatique des échéances en retard
      - Calcul des pénalités
      - Suivi des remboursements en souffrance

4. Remboursement anticipé
--------------------------

Cette fonctionnalité permet aux clients de rembourser leurs prêts de manière anticipée.

Procédure
~~~~~~~~~

1. Connectez-vous au logiciel.
2. Accédez au module **Prêts**.
3. Sélectionnez le prêt à rembourser.

   \a. **Calcul du remboursement anticipé**

      - Le système calcule automatiquement le montant dû
      - Prise en compte des intérêts et frais
      - Génération du solde de tout compte

   \b. **Validation du remboursement**

      - Vérification des fonds disponibles
      - Confirmation du paiement
      - Clôture du prêt

5. Reports et exports
---------------------

Cette section permet de générer des rapports et d'exporter les données de prêts.

Procédure
~~~~~~~~~

1. Connectez-vous au logiciel.
2. Accédez au module **Prêts**.
3. Sélectionnez l'option **Rapports**.

   \a. **Export des prêts**

      - Export de la liste complète des prêts
      - Filtrage par période, client, ou statut
      - Export au format Excel

   \b. **Rapport des prêts en retard**

      - Liste des prêts en souffrance
      - Détails des échéances manquées
      - Export pour suivi de recouvrement

   \c. **Rapport de performance**

      - Statistiques de remboursement
      - Analyse des retards
      - Indicateurs de qualité du portefeuille

6. Système de tarification
---------------------------

Le système intègre un moteur de tarification sophistiqué basé sur la formule :

.. math::
   
   \text{Marge} &= \text{Prix de vente} - \text{Prix d'achat} \\
   \text{Pourcentage marge} &= \frac{\text{Marge}}{\text{Prix d'achat}} \times 100 \\
   \text{Valeur TAF} &= \text{Marge} \times \frac{\text{Pourcentage TAF}}{100} \\
   \text{Montant total} &= \text{Prix d'achat} + \text{Marge} + \text{Valeur TAF}

**Validations automatiques** :

- Prix d'achat doit être strictement supérieur à 0 (évite les divisions par zéro)
- Prix de vente doit être supérieur ou égal au prix d'achat
- Tous les calculs sont effectués avant l'enregistrement (évite les dépendances circulaires)
- Précision garantie sur tous les montants financiers

Procédure
~~~~~~~~~

1. **Configuration des paramètres**

   - Définition des pourcentages de marge
   - Configuration des taux TAF (Taxe sur Activités Financières)
   - Paramétrage des frais additionnels
   - Validation automatique de la cohérence des données

2. **Calcul automatique**

   - Le système calcule automatiquement le montant total
   - Application des règles de tarification islamique
   - Génération de l'échéancier selon le type d'échéance
   - Vérification de la cohérence des montants

3. **Types de prêts supportés**

   - **Murabaha** : Vente avec marge (financement islamique)
   - **Ijara** : Location-vente (leasing islamique)
   - **Musharaka** : Partenariat (participation islamique)
   - **Qard** : Prêt sans intérêt (prêt bienveillant)
   - **Autres types** : Prêts conventionnels

4. **Types d'échéances disponibles**

   - **MONTHLY** : Mensuel (30 jours)
   - **QUARTERLY** : Trimestriel (90 jours)
   - **FOURTH_MONTH** : Quatre mois (120 jours)
   - **FIFTH_MONTH** : Cinq mois (150 jours)
   - **SEMI_ANNUAL** : Semestriel (180 jours)
   - **ANNUAL** : Annuel (360 jours)

.. warning::
   Le calcul de l'échéancier est automatiquement mis à jour lorsque vous modifiez :
   
   - La date du premier remboursement
   - Le délai (nombre de périodes)
   - Le type d'échéance
   
   Cette mise à jour supprime les remboursements non validés et régénère l'échéancier.

Démo
~~~~

1. Le gestionnaire de prêts veut créer un prêt Murabaha de 500 000 FCFA pour le client John Doe.

2. Le validateur de prêts veut approuver une demande de prêt en attente.

3. Le gestionnaire veut confirmer un remboursement de 50 000 FCFA pour le prêt #12345.

4. Le client veut effectuer un remboursement anticipé de son prêt.
