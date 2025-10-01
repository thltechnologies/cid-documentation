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