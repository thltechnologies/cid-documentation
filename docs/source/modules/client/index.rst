.. _client-index:

Clients
=======

Le module **Client** est dédié à la gestion de client de CID, il est utilisé par beaucoup d'utilisateur comme le SuperAdmin, l'Admin, le Chef d'agence, ....
Ce module comprend 3 menus et 3 options(boutons) disponibles selon le rôle de l'utilisateur connecté :

1. Le menu 'Ajouter'
--------------------

Ce menu permet de rédiriger l'utilisateur vers la page d'ajout d'un client.

Procédure
~~~~~~~~~

1. Connectez-vous au logiciel.
2. Cliquez sur le module **Clients**
3. Cliquer sur le menu *Ajouter*, un formulaire d'enregistrement de client s'ouvre à vous :
   Dans le formulaire, saisissez les informations du client comme :
      - Son prénom,
      - Son nom,
      - Sa date de naissance,
      - Son lieu de naissance,
      - Son genre (Homme ou Femme),
      - Son numéro de téléphone,
      - Son adresse email (exemple: xyz@mail.com),
      - Le nom et le prénom de son père,
      - Le nom et le prénom de sa mère,
      - Son statut matrimonial (Célibataire, Marié(e), Divorcé(e), ...),
      - Son numéro Fax (optionnel),
      - Cocher Résident s'il est résident ou laissé si non,
      - Son pays de résidence,
      - Sa nationalité,
      - Son adresse (optionnel) qui est constitué de :
         * Le pays,
         * La ville,
         * Le quartier,
         * Le code postal
   Puis cliquer sur le bouton :
      - *Enregistrer* : Pour ajouter le client et rester sur le formulaire d'ajout de client,
      - *Enregistrer et continuer* : Pour ajouter le client et continuer sur la page des informations du client pour éventuellement créer son compte
      - *Annuler* : Pour réinitialiser le formulaire et récommencer à saisir les informations

Démo
~~~~

Le chef d'agence John Chef Agence veut ajouter un nouveau client :

.. list-table:: Informations du client
   :header-rows: 1

   * - Attribut
     - Valeur

   * - Prénom
     - Kélan

   * - Nom
     - Dembassy

   * - Date de naissance
     - 31/12/1995

   * - Lieu de naissance
     - Baco-Djicoroni

   * - Genre
     - Homme

   * - Numéro de téléphone
     - +223 01234567

   * - Adresse email
     - kelandembassy@gmail.com

   * - Nom et le prénom du père
     - Fadigué Dembassy

   * - Nom et le prénom de la mère
     - Sira Kourouma

   * - Statut matrimonial
     - Marié

   * - Numéro Fax
     - 91091

   * - Résident
     - Oui

   * - Pays de résidence
     - Mali

   * - Nationalité
     - Malienne

   * - Adresse
     -
         * Pays : Mali
         * Ville : Bamako
         * Quartier : Baco-djicoroni
         * Code postal : 91091

.. video:: ../../_static/videos/client/add_menu_demo.mp4
    :caption: Ajout d'un compte via le menu Ajouter


2. Le menu 'Clients de l'agence'
--------------------------------

Ce menu permet de gérer les clients de l'agence à laquelle l'utilisateur connecté est affecté

Procédure
~~~~~~~~~

1. Connectez-vous au logiciel.
2. Cliquez sur le module **Clients**
3. Cliquer sur le menu *Clients de l'agence* :
   La liste des clients de l'agence de l'utilisateur connecté seront affichés. Il y a 100 clients qui s'affichent initialement, 100 autres clients se charge quand vous atteignez la fin de la page; ainsi de suite jusqu'à afficher la liste complète des clients.
   Cette liste est présentée sous forme de tableau avec les informations du client et deux bouton *Supprimer* et *Modifier* :

    .. list-table:: Détails du tableau
       :header-rows: 1

       * - Attribut
         - Signification

       * - CIF
         - Customer Identification File (Fichier d’Identification du Client), un identifiant unique attribué à chaque client pour regrouper ses informations et faciliter la gestion de ses comptes et services.

       * - PRENOM
         - Le prénom du client.

       * - NOM
         - Le nom du client.

       * - SEXE
         - Le genre du client.

       * - TELEPHONE
         - Le numéro de téléphone du client.

       * - EMAIL
         - L'adresse e-mail du client.

       * - ADRESSE
         - Le quartier du client.

       * - AGENCE
         - Le nom de l'agence du client.

       * - COMPTE
         - Le nombre de comptes du client.

       * - ETAT
         - L'état actuel du compte : activé/désactivé, avec possibilité de changement d'état.

       * - ACTION
         - Comprend les boutons "Modifier" (pour mettre à jour les informations du client) et "Supprimer" (pour supprimer le client).



Démo
~~~~

Le chef d'agence John Chef Agence veut afficher la liste de tous les clients de son agence.

.. video:: ../../_static/videos/client/branch_clients_menu_demo.mp4
    :caption: Listes des clients d'un chef d'agence spécifique

3. Le menu 'Clients'
--------------------

Ce menu semblable à celui de 'Clients de l'agence' permet de gérer l'ensemble des clients de CID

Procédure
~~~~~~~~~

1. Connectez-vous au logiciel.
2. Cliquez sur le module **Clients**
3. Cliquer sur le menu *Clients* :
   La liste des clients de CID seront affichés. Il y a 100 clients qui s'affichent initialement, 100 autres clients se charge quand vous atteignez la fin de la page; ainsi de suite jusqu'à afficher la liste complète de tous les clients de CID.
   Cette liste est présentée sous forme de tableau avec les informations du client et deux bouton *Supprimer* et *Modifier* :

    .. list-table:: Détails du tableau
       :header-rows: 1

       * - Attribut
         - Signification

       * - CIF
         - Customer Identification File (Fichier d’Identification du Client), un identifiant unique attribué à chaque client pour regrouper ses informations et faciliter la gestion de ses comptes et services.

       * - PRENOM
         - Le prénom du client.

       * - NOM
         - Le nom du client.

       * - SEXE
         - Le genre du client.

       * - TELEPHONE
         - Le numéro de téléphone du client.

       * - EMAIL
         - L'adresse e-mail du client.

       * - ADRESSE
         - Le quartier du client.

       * - AGENCE
         - Le nom de l'agence du client.

       * - COMPTE
         - Le nombre de comptes du client.

       * - ETAT
         - L'état actuel du compte : activé/désactivé, avec possibilité de changement d'état.

       * - ACTION
         - Comprend les boutons "Modifier" (pour mettre à jour les informations du client) et "Supprimer" (pour supprimer le client).

Démo
~~~~

Le super administrateur John SuperAdmin veut afficher la liste de tous les clients de CID.

.. video:: ../../_static/videos/client/clients_menu_demo.mp4
    :caption: Listes de tous les clients de CID

4. Le bouton 'Ajouter un(e) client(e)'
--------------------------------------

Ce bouton permet de faire la même chose que le menu 'Ajouter': rédiriger l'utilisateur vers la page d'ajout d'un client.

Procédure
~~~~~~~~~

1. Connectez-vous au logiciel.
2. Cliquez sur le module **Clients**
3. Cliquer sur le menu *Clients de l'agence* ou *Clients*,
4. Cliquer sur le bouton 'Ajouter un(e) client(e)' en haut et à gauche de la page, un formulaire d'enregistrement de client s'ouvre à vous :
   Dans le formulaire, saisissez les informations du client comme :
      - Son prénom,
      - Son nom,
      - Sa date de naissance,
      - Son lieu de naissance,
      - Son genre (Homme ou Femme),
      - Son numéro de téléphone,
      - Son adresse email (exemple: xyz@mail.com),
      - Le nom et le prénom de son père,
      - Le nom et le prénom de sa mère,
      - Son statut matrimonial (Célibataire, Marié(e), Divorcé(e), ...),
      - Son numéro Fax (optionnel),
      - Cocher Résident s'il est résident ou laissé si non,
      - Son pays de résidence,
      - Sa nationalité,
      - Son adresse (optionnel) qui est constitué de :
         * Le pays,
         * La ville,
         * Le quartier,
         * Le code postal
   Puis cliquer sur le bouton :
      - *Enregistrer* : Pour ajouter le client et rester sur le formulaire d'ajout de client,
      - *Enregistrer et continuer* : Pour ajouter le client et continuer sur la page des informations du client pour éventuellement créer son compte
      - *Annuler* : Pour réinitialiser le formulaire et récommencer à saisir les informations

Démo
~~~~

Le chef d'agence John Chef Agence veut ajouter un nouveau client :

.. list-table:: Informations du client
   :header-rows: 1

   * - Attribut
     - Valeur

   * - Prénom
     - Nohan

   * - Nom
     - Falessi

   * - Date de naissance
     - 22/11/1998

   * - Lieu de naissance
     - Sikasso, Mali

   * - Genre
     - Homme

   * - Numéro de téléphone
     - +22303456789

   * - Adresse email
     - nohanfalessi@mail.com

   * - Nom et le prénom du père
     - Makan Falessi

   * - Nom et le prénom de la mère
     - Djeneba Konaté

   * - Statut matrimonial
     - Célibataire

   * - Numéro Fax
     - 22307

   * - Résident
     - Oui

   * - Pays de résidence
     - Mali

   * - Nationalité
     - Malienne

   * - Adresse
     -
         * Pays : Mali
         * Ville : Bamako
         * Quartier : Faladié
         * Code postal : 22307

.. video:: ../../_static/videos/client/add_button_demo.mp4
    :caption: Ajout d'un compte via le bouton Ajouter

5. Le bouton 'Exporter'
-----------------------

Ce bouton permet d'exporter (en excel) la liste des comptes des clients.

Procédure
~~~~~~~~~

1. Connectez-vous au logiciel.
2. Cliquez sur le module **Clients**
3. Cliquer sur le menu *Clients de l'agence* ou *Clients*,
4. Cliquer sur le bouton 'Exporter' en haut et à droite de la page et attendre que le téléchargement soit terminé.

Démo
~~~~

Le super administrateur John SuperAdmin veut exporter la liste de tous les comptes des client de CID

.. video:: ../../_static/videos/client/export_button_demo.mkv
    :caption: Exportation des comptes clients

6. Le bouton 'Importer'
--------------------------------------

Ce bouton permet d'importer / migrer les comptes de l'ancien système dans le logiciel CID (au format excel).

Procédure
~~~~~~~~~

1. Connectez-vous au logiciel.
2. Cliquez sur le module **Clients**
3. Cliquer sur le menu *Clients de l'agence* ou *Clients*,
4. Cliquer sur le bouton 'Importer' en haut de la page et à gauche du bouton 'Exporter', vous serez invité à choisir le fichier excel depuis votre explorateur de fichier :

   Notez bien que le fichier respecte bien cet format :
      - Les clients sont enregistré sur la première feuille du document
      - Cette feuille contient uniquement une entête :
            .. list-table:: Structure du fichier excel à importer
               :header-rows: 1

               * - Entête
                 - Signification

               * - N
                 - Le numéro de la ligne

               * - ACC_NUM
                 - La structure des comptes clients: 14 positions de gauche à droite:
                    * 1 positions: agence
                    * 8 positions: numéro CIF
                    * 5 positions: numéro non utilisé actuellement

               * - NOM_ACC
                 - Le nom du titulaire(client) du compte.

               * - Solde sur le relevé (a)
                 - Le solde inscrit sur le relevé.

               * - Solde confirmé par le client (b)
                 - Le solde confirmé par le client

               * - Ecart (a) - (b)
                 - Différence entre le solde du relevé et le solde confirmé par le client.

               * - SOLDE CORRIGE
                 - Le solde corrigé après résolution des écarts.

               * - EXPLICATION ECART
                 - Une explication de l'écart.

               * - TELEPHONE
                 - Numéro de téléphone du client.

               * - TYPE DE COMPTE
                 - Type de compte (ex. : Compte Courant, Compte Épargne).

               * - ETAT
                 - Statut du compte (ex. : Activé/Désactivé).

               * - NOUVEAU CIF
                 - Nouveau numéro de dossier d’information client (CIF) correspondant aux 8 positions de la deuxième colonne de la feuille après la prémiere position.

               * - CODE PRODUIT
                 - Code produit associé au compte (correspondant au Type de compte dans la 10ème colonne de la feuille).

5. Après l'importation, un bouton 'Télécharger' apparaît à gauche du bouton 'Importer' qui permet de télécharger le RIB(relevé d'identification bancaire) des comptes qui viennent d'être migrés.

Démo
~~~~

Le super administrateur John SuperAdmin veut importer une liste (télécharger la liste `ici`_) de 20 comptes clients

.. _ici: ../../_static/excel/client/accounts_to_be_migrated.xlsx


.. video:: ../../_static/videos/client/import_button_demo.mkv
    :caption: Migration des comptes clients
