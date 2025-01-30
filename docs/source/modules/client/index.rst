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


1. Le menu 'Clients de l'agence'
--------------------------------

Ce menu permet de gérer les clients de l'agence à laquelle l'utilisateur connecté est affecté

Procédure
~~~~~~~~~

1. Connectez-vous au logiciel.
2. Cliquez sur le module **Clients**
3. Cliquer sur le menu *Clients de l'agence* :
   La liste des clients de l'agence de l'utilisateur connecté seront affichés. Il y a 100 clients qui s'affichent initialement, 100 autres clients se charge quand vous atteignez la fin de la page; ainsi de suite jusqu'à afficher la liste complète des clients.
   Cette liste est présentée sous forme de tableau avec les information du client et deux bouton *Supprimer* et *Modifier* :

.. list-table:: Liste des clients de l'agence
   :header-rows: 1

   * - CIF
     - PRENOM
     - NOM
     - SEXE
     - TELEPHONE
     - EMAIL
     - ADRESSE
     - AGENCE
     - COMPTE
     - ETAT
     - ACTION
   * - 01234567
     - John
     - Doe
     - Homme
     - 70707070
     - jean.doe@gmail.com
     - Baco Djicoroni
     - Agence 01
     - 2
     - Actif
     - Modifier/Supprimer

Démo
~~~~
