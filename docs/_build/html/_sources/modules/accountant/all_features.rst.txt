Liste des fonctionnalités
=========================

Contexte
--------
Le comptable dispose de plusieurs fonctionnalités permettant la gestion et le suivi des
opérations comptables au sein de l'application. Les principaux avantages incluent
la centralisation des opérations, une traçabilité complète, et un système optimisé de traitement des écritures comptables.


1. Opérations sur les comptes internes
---------------------------------------
- Permet de gérer les transactions liées aux comptes internes de CID
- Transferts entre comptes internes
- Suivi des soldes et historique des transactions
- Filtrage par intervalle de dates et critères de recherche

2. Prélèvement des capitaux
----------------------------
- Permet d'effectuer des virements de fonds depuis les comptes clients vers les comptes
  de capitaux internes.
- **Exemple :** Le caissier veut prélever 32 000 FCFA au compte 00002-01142-10350561-73 du client John Doe

.. video:: ../../_static/images/accountant/hint_capital_withdrawal.mp4
   :autoplay:
   :controls:

3. Système de composants de transaction (NOUVEAU)
--------------------------------------------------
- Architecture optimisée avec composants de transaction
- Une seule écriture comptable par transaction avec plusieurs lignes
- Gestion de 16 types de composants différents (Marge, TAF, Frais divers)
- Performance améliorée et traçabilité complète

4. Traitement par lots des écritures comptables (NOUVEAU)
----------------------------------------------------------
- Traitement automatique des écritures comptables par lots
- Idempotence pour éviter le double traitement
- Reprocessing intelligent des écritures existantes
- Traitement par pages de 100 transactions pour optimiser les performances

5. Génération du grand livre (NOUVEAU)
---------------------------------------
- API REST pour la génération du grand livre
- Filtrage par compte et période
- Données complètes : date, numéro, libellé, débit, crédit
- Export possible des données

6. Historique des transactions
------------------------------
- Fournit une vue complète de toutes les opérations de prélèvement.
- Offre un filtrage par plage de dates (par exemple : du 01/01/2025 au 31/01/2025).
- **Exemples :**

7. Recherche ciblée
-------------------
- Permet de retrouver une transaction spécifique à l'aide de différents critères
  (montant, nom de l'agence, date, etc.).
- **Exemple :** Rechercher toutes les transactions effectuées durant le mois de décembre 2024.

8. Reprocessing des écritures (NOUVEAU)
----------------------------------------
- Reprocessing intelligent des écritures existantes
- Gestion automatique des composants TAF et marge
- Maintien de la cohérence des données comptables
- Logs détaillés pour le suivi des opérations

9. Améliorations de performance (NOUVEAU)
------------------------------------------
- Réduction du nombre de requêtes base de données
- Optimisation de l'utilisation mémoire
- Traitement simplifié des composants
- Audit trail amélioré et cohérent

10. Journaux Comptables (NOUVEAU)
-----------------------------------
Cette fonctionnalité permet de gérer les journaux comptables qui organisent les écritures par type d'opération.

Fonctionnalités :
- **Création de journaux** : Création de journaux avec code unique (ex: "BQ", "CS", "OD")
- **Types de journaux** : STANDARD, CAISSE, BANQUE, OD
- **Gestion des séquences** : Numérotation automatique des pièces comptables
- **Activation/Désactivation** : Contrôle de l'utilisation des journaux
- **Génération de références** : Format automatique "{CODE}-{SEQUENCE}" (ex: "BQ-001")

11. Écritures Comptables Manuelles (NOUVEAU)
---------------------------------------------
Cette fonctionnalité permet de créer des écritures comptables directement depuis l'interface utilisateur.

Fonctionnalités :
- **Création manuelle** : Formulaire complet pour créer des écritures
- **Gestion des lignes** : Ajout, modification, suppression de lignes débit/crédit
- **Validation en temps réel** : Vérification automatique de l'équilibre (Débits = Crédits)
- **Association avec journaux** : Sélection d'un journal comptable lors de la création
- **Génération automatique de références** : Références de pièces comptables générées automatiquement
- **Modification** : Possibilité de modifier les écritures manuelles (si non validées)

12. Pièces Comptables (NOUVEAU)
---------------------------------
Système de références uniques pour identifier les écritures comptables.

Fonctionnalités :
- **Format standardisé** : "{CODE_JOURNAL}-{SEQUENCE}" (ex: "BQ-001", "CS-002")
- **Génération automatique** : Références créées automatiquement lors de la création d'écritures
- **Incrémentation automatique** : Séquence du journal incrémentée après chaque écriture
- **Traçabilité** : Références visibles dans tous les rapports et exports

13. Module Comptable Complet (NOUVEAU)
---------------------------------------
Le module comptable complet est une extension majeure qui fournit un système comptable complet conforme aux standards de la finance islamique.

Fonctionnalités principales :
- **Plan Comptable** : Structure hiérarchique des comptes avec types (ASSET, LIABILITY, EQUITY, REVENUE, EXPENSE)
- **Exercices Comptables** : Gestion des exercices fiscaux avec création automatique de 12 périodes mensuelles
- **Grand Livre Général** : Enregistrement de toutes les transactions comptables avec génération automatique
- **Balance de Vérification** : Calcul automatique avec validation de l'équilibre débit/crédit
- **États Financiers** : Génération automatique du bilan, compte de résultat et tableau de flux de trésorerie
- **Réconciliation Bancaire** : Pointage automatique et manuel avec gestion des écarts

Architecture :
- **Backend** : 9 entités JPA, 7 services métier, 7 controllers REST, 50+ endpoints API
- **Frontend** : 6 composants Angular, 7 services, 8 modèles TypeScript, 4 enums

Conformité :
- Support pour finance islamique (Murabaha, Ijara, Musharaka)
- Conformité AAOIFI (structure prête)
- Séparation des fonds islamiques/conventionnels
- Traçabilité complète conforme à la Sharia

Voir la documentation complète : :ref:`accounting-module`