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

5. Le bouton 'Exporter'
--------------------------------------

Ce bouton permet d'exporter (en excel) la liste des comptes des clients.

Procédure
~~~~~~~~~

1. Connectez-vous au logiciel.
2. Cliquez sur le module **Clients**
3. Cliquer sur le menu *Clients de l'agence* ou *Clients*,
4. Cliquer sur le bouton 'Exporter' en haut et à droite de la page et attendre que le téléchargement soit terminé.

Démo
~~~~

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
      - Cette contient uniquement une entête :
            .. list-table:: Structure du fichier excel à importer
               :header-rows: 1

               * - Entête
                 - Signification

               * -

Démo
~~~~
