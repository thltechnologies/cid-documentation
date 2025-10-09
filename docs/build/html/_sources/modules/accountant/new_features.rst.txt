Nouvelles fonctionnalités
=========================

1. Système de composants de transaction
---------------------------------------
- **Architecture optimisée** : Remplacement des objets Transaction séparés par un système de composants
- **Performance améliorée** : Une seule écriture comptable par transaction avec plusieurs lignes
- **Traçabilité complète** : Tous les composants liés à la transaction principale
- **Flexibilité** : Facile d'ajouter de nouveaux types de composants

Types de composants supportés :
- Marge (MARGIN)
- TAF (Taxe sur les Activités Financières)
- Frais de communication (COMMUNICATION_FEE)
- Frais de transport (TRANSPORT_FEE)
- Frais administratifs (ADMINISTRATIVE_FEE)
- Frais d'assurance (INSURANCE_FEE)
- Frais d'enregistrement (REGISTRATION_FEE)
- Frais de notaire (NOTARY_FEE)
- Frais de dossier (APPLICATION_FEE)
- Frais commerciaux (COMMERCIAL_FEE)
- Frais d'expertise (SURVEYOR_FEE)
- Dépôt de garantie (GUARANTEE_DEPOSIT)
- Dépôt de bonne foi (GOOD_FAITH_DEPOSIT)
- Frais mensuels (MONTHLY_FEE)
- Frais d'ouverture (OPENING_FEE)
- Frais de visite et évaluation (VISIT_AND_EVALUATION_FEE)

2. Traitement par lots optimisé
-------------------------------
- **Traitement automatique** : Les écritures comptables sont traitées automatiquement par lots
- **Idempotence** : Évite le double traitement des transactions
- **Reprocessing** : Possibilité de reprocesser les écritures existantes
- **Performance** : Traitement par pages de 100 transactions pour optimiser les performances

Fonctionnalités du traitement par lots :
- Détection automatique des transactions non traitées
- Création d'écritures comptables optimisées
- Gestion des composants TAF et marge
- Logs détaillés pour le suivi des opérations

3. Génération du grand livre
----------------------------
- **API REST** : Endpoint `/account/{accountId}/general-ledger`
- **Filtrage par période** : Du 01/01/2025 au 31/01/2025
- **Données complètes** : Date, numéro, libellé, débit, crédit
- **Performance** : Requêtes optimisées avec indexation

Exemple d'utilisation :
- Sélection du compte concerné
- Définition de la période de consultation
- Génération automatique du grand livre
- Export possible des données

4. Reprocessing des écritures
-----------------------------
- **Reprocessing intelligent** : Mise à jour des écritures existantes
- **Gestion des composants** : Ajout automatique des composants TAF et marge
- **Cohérence des données** : Maintien de l'intégrité comptable
- **Logs de suivi** : Traçabilité complète des opérations

Fonctionnalités du reprocessing :
- Suppression des anciennes écritures
- Création de nouvelles écritures avec composants
- Gestion des transactions TAF multiples
- Marquage des transactions traitées

5. Améliorations de performance
-------------------------------
- **Requêtes optimisées** : Réduction du nombre de requêtes base de données
- **Mémoire optimisée** : Un seul objet Transaction avec collection de composants
- **Traitement simplifié** : Accès direct aux composants
- **Audit trail amélioré** : Tous les composants liés à la transaction principale

Avant l'optimisation :
- 3+ requêtes par transaction (principale + marge + TAF)
- 3+ écritures comptables séparées
- Gestion complexe des relations
- Traçabilité fragmentée

Après l'optimisation :
- 1 requête pour la transaction principale + composants
- 1 écriture comptable avec plusieurs lignes
- Accès direct aux composants
- Traçabilité complète et cohérente