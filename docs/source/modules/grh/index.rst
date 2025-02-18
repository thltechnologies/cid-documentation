.. _grh-index:

GRH
===

Le module GRH est dédié à la gestion des ressources humaines au sein de CID. Il est divisé en deux sous-modules : *GRH* utilisé par le SuperAdmin et *EMPLOYES* utilisé par l'Admin.
Ce module comprend 7 menus et 5 boutons en tout :

1. Le menu 'Ajouter'
--------------------

Ce menu permet de rédiriger l'utilisateur vers la page d'ajout d'un employé.

Procédure
~~~~~~~~~

1. Connectez-vous au logiciel.
2. Cliquez sur le module **GRH**
3. Cliquer sur le menu *Ajouter*, un formulaire d'enregistrement d'employé s'ouvre à vous :

   Dans le formulaire, saisissez les informations de l'employé :
      - Prénom,
      - Nom,
      - Date de naissance,
      - Lieu de naissance,
      - Sexe (Homme ou Femme),
      - Numéro de téléphone,
      - Adresse email (exemple: xyz@mail.com),
      - Adresse (optionnel) qui est constitué de :
         * Le pays,
         * La ville,
         * Le quartier,
         * Le code postal
      - Agence
         * Nom de l'agence
         * Poste
   Puis cliquer sur le bouton :
      - *Enregistrer* : Pour ajouter l'employé et rester sur le formulaire d'ajout d'employé,
      - *Enregistrer et continuer* : Pour ajouter l'employé et continuer sur la page des informations de l'employé pour voir/modifier les informations et éventuellement attribuer les rôles et l'agence de l'employé
      - *Annuler* : Pour réinitialiser le formulaire et récommencer à saisir les informations

Démo
~~~~

Le super administrateur John SuperAdmin veut ajouter un nouvel employé :

.. list-table:: Informations de l'employé
   :header-rows: 1

   * - Attribut
     - Valeur

   * - Prénom
     - John

   * - Nom
     - Chef Opération

   * - Date de naissance
     - 31/12/1998

   * - Lieu de naissance
     - Banconi

   * - Genre
     - Homme

   * - Numéro de téléphone
     - +223 07654321

   * - Adresse email
     - john.chef-operation@gmail.com

   * - Adresse
     -
         * Pays : Mali
         * Ville : Bamako
         * Quartier : Hamdallaye ACI
         * Code postal : 91091

   * - Agence
     -
         * Nom : Agence 02
         * Poste : Non défini

.. video:: ../../_static/videos/grh/add_menu_demo.mp4
    :caption: Ajout d'un employé via le menu Ajouter


2. Le menu 'Employés'
---------------------

Ce menu permet de gérer l'ensemble des employés de CID

Procédure
~~~~~~~~~

1. Connectez-vous au logiciel.
2. Cliquez sur le module **GRH** ou **EMPLOYES** (selon les rôles).
3. Cliquer sur le menu *Employés* :
   La liste de tous les employés de CID seront affichés pour le super administrateur et seulement la liste de employés de son agence pour le chef d'agence.
   Cette liste est présentée sous forme de tableau avec les informations des employés et un bouton *Modifier* :

    .. list-table:: Détails du tableau
       :header-rows: 1

       * - Attribut
         - Signification

       * - PRENOM
         - Le prénom de l'employé.

       * - NOM
         - Le nom de l'employé.

       * - POSTE
         - Le poste occupé par l'employé.

       * - TELEPHONE
         - Le numéro de téléphone de l'employé.

       * - EMAIL
         - L'adresse e-mail de l'employé.

       * - AGENCE
         - Le nom de l'agence à laquelle l'employé est affecté.

       * - ROLES
         - Liste des rôles exercés par l'employé :

            Il y a environ 16 roles :
               * **Super administrateur**
               * **Chef des opérations**
               * **Opération**
               * **Chef d'agence**
               * **Administrateur**
               * **Employé**
               * **Caissier**
               * **Chargé clientèle**
               * **Chargé de crédit (prêt)**
               * **Commité de validation**
               * **Comptable**
               * **Gestionnaire de collecte CID**
               * **Admin Collecteur**
               * **Gestionnaire de collecte**
               * **Collecteur**

       * - ETAT
         - L'état actuel de l'employé : activé/désactivé, avec possibilité de changement d'état.

       * - ACTION
         - Comprend un bouton "Modifier" pour mettre à jour les informations de l'employé.

Démo
~~~~

1. Le super administrateur John SuperAdmin veut afficher la liste de tous les employés de CID.

    .. video:: ../../_static/videos/grh/all_employees_demo.mp4
        :caption: Listes de tous les employés de CID

2. L'administrateur John Admin veut afficher la liste de tous les employés de son agence.

    .. video:: ../../_static/videos/grh/branch_employees_demo.mp4
        :caption: Listes des employés d'une agence spécifique

3. Le bouton 'Ajouter un(e) employé(e)'
---------------------------------------

Ce bouton permet de faire la même chose que le menu 'Ajouter': rédiriger l'utilisateur vers la page d'ajout d'un employé.

Procédure
~~~~~~~~~

1. Connectez-vous au logiciel.
2. Cliquez sur le module **GRH**
3. Cliquer sur le menu *Employés*
4. Cliquer sur le bouton *Ajouter un(e) employé(e)*, un formulaire d'enregistrement d'employé s'ouvre à vous :

   Dans le formulaire, saisissez les informations de l'employé :
      - Prénom,
      - Nom,
      - Date de naissance,
      - Lieu de naissance,
      - Sexe (Homme ou Femme),
      - Numéro de téléphone,
      - Adresse email (exemple: xyz@mail.com),
      - Adresse (optionnel) qui est constitué de :
         * Le pays,
         * La ville,
         * Le quartier,
         * Le code postal
      - Agence
         * Nom de l'agence
         * Poste
   Puis cliquer sur le bouton :
      - *Enregistrer* : Pour ajouter l'employé et rester sur le formulaire d'ajout d'employé,
      - *Enregistrer et continuer* : Pour ajouter l'employé et continuer sur la page des informations de l'employé pour voir/modifier les informations et éventuellement attribuer les rôles et l'agence de l'employé
      - *Annuler* : Pour réinitialiser le formulaire et récommencer à saisir les informations

Démo
~~~~

Le super administrateur John SuperAdmin veut ajouter un nouvel employé :

.. list-table:: Informations de l'employé
   :header-rows: 1

   * - Attribut
     - Valeur

   * - Prénom
     - John

   * - Nom
     - Chargé Clientèle

   * - Date de naissance
     - 31/12/2000

   * - Lieu de naissance
     - Fadjiguila

   * - Genre
     - Femme

   * - Numéro de téléphone
     - +223 09876543

   * - Adresse email
     - john.charge-clientele@gmail.com

   * - Adresse
     -
         * Pays : Mali
         * Ville : Bamako
         * Quartier : Hamdallaye ACI
         * Code postal : 91091

   * - Agence
     -
         * Nom : Agence 02
         * Poste : Non défini

.. video:: ../../_static/videos/grh/add_button_demo.mp4
    :caption: Ajout d'un employé via le bouton Ajouter

4. Le menu 'Direction'
----------------------

Ce menu permet d'afficher la liste de toutes les directions de CID.

Procédure
~~~~~~~~~

1. Connectez-vous au logiciel.
2. Cliquez sur le module **GRH**
3. Cliquer sur le menu *Direction*

   La liste de toutes les directions de CID seront affichés.
   Cette liste est présentée sous forme de tableau avec les informations des directions et un bouton de configuration ⚙️ :

    .. list-table:: Détails du tableau
       :header-rows: 1

       * - Attribut
         - Signification

       * - DIRECTION
         - Le nom de la direction.

       * - ACTION
         - Comprend un bouton de configuration ⚙️ qui ouvre deux boutons : "Modifier" pour modifier la direction et "Supprimer" pour supprimer la direction.

Démo
~~~~

Le super administrateur John SuperAdmin veut afficher la liste de toutes les directions de CID :

.. video:: ../../_static/videos/grh/all_directions_demo.mp4
    :caption: Liste des directions de CID

5. Le bouton 'Créer une direction'
----------------------------------

Ce bouton permet d'ajouter une nouvelle direction à la liste des directions.

Procédure
~~~~~~~~~

1. Connectez-vous au logiciel.
2. Cliquez sur le module **GRH**
3. Cliquer sur le menu *Direction*,
4. Cliquer sur le bouton 'Créer une direction', un formulaire d'enregistrement de direction s'ouvre en haut de la page :

   Dans le formulaire, saisissez le nom de la direction puis cliquer sur le bouton 'Créer une direction' pour l'enregistrer ou sur 'Annuler' pour fermer le formulaire.

Démo
~~~~

Le super administrateur John SuperAdmin veut ajouter une nouvelle direction 'Direction 001' à CID

.. video:: ../../_static/videos/grh/add_direction_button_demo.mp4
    :caption: Ajout d'une nouvelle direction

6. Le menu 'Département'
------------------------

Ce menu permet d'afficher la liste de tous les départements de CID.

Procédure
~~~~~~~~~

1. Connectez-vous au logiciel.
2. Cliquez sur le module **GRH**
3. Cliquer sur le menu *Département*

   La liste de tous les département de CID seront affichés.
   Cette liste est présentée sous forme de tableau avec les informations des départements et un bouton de configuration ⚙️ :

    .. list-table:: Détails du tableau
       :header-rows: 1

       * - Attribut
         - Signification

       * - Départements
         - Le nom du département.

       * - Directions
         - Le nom de la direction à la quelle ce département est inclut.

       * - ACTION
         - Comprend un bouton de configuration ⚙️ qui ouvre deux boutons : "Modifier" pour modifier le département et "Supprimer" pour le supprimer.

Démo
~~~~

Le super administrateur John SuperAdmin veut afficher la liste de tous les départements de CID :

.. video:: ../../_static/videos/grh/all_departments_demo.mkv
    :caption: Liste des départements de CID

7. Le bouton 'Créer un département'
-----------------------------------

Ce bouton permet d'ajouter un nouveau département à la liste des départements.

Procédure
~~~~~~~~~

1. Connectez-vous au logiciel.
2. Cliquez sur le module **GRH**
3. Cliquer sur le menu *Département*,
4. Cliquer sur le bouton 'Créer un département', un formulaire d'enregistrement de département s'ouvre en haut de la page :

   Dans le formulaire, saisissez :
      - Le nom du département
      - La direction à laquelle il appartient
   Puis cliquer sur le bouton :
      - 'Créer le département' pour l'enregistrer
      - 'Annuler' pour fermer le formulaire.

Démo
~~~~

Le super administrateur John SuperAdmin veut ajouter un nouveau département 'Département 001' appartenant à la direction 'Direction 003' à CID.

.. video:: ../../_static/videos/grh/add_department_button_demo.mp4
    :caption: Ajout d'un nouveau département

8. Le menu 'Service'
--------------------

Ce menu permet d'afficher la liste de tous les services de CID.

Procédure
~~~~~~~~~

1. Connectez-vous au logiciel.
2. Cliquez sur le module **GRH**
3. Cliquer sur le menu *Service*

   La liste de tous les services de CID seront affichés.
   Cette liste est présentée sous forme de tableau avec les informations des services et un bouton de configuration ⚙️ :

    .. list-table:: Détails du tableau
       :header-rows: 1

       * - Attribut
         - Signification

       * - Services
         - Le nom du service.

       * - Départements
         - Le nom du département auquel ce service est inclut.

       * - ACTION
         - Comprend un bouton de configuration ⚙️ qui ouvre deux boutons : "Modifier" pour modifier le service et "Supprimer" pour supprimer le service.

Démo
~~~~

Le super administrateur John SuperAdmin veut afficher la liste de tous les services de CID :

.. video:: ../../_static/videos/grh/all_services_demo.mkv
    :caption: Liste des services de CID

9. Le bouton 'Créer un service'
-------------------------------

Ce bouton permet d'ajouter un nouveau service à la liste des services.

Procédure
~~~~~~~~~

1. Connectez-vous au logiciel.
2. Cliquez sur le module **GRH**
3. Cliquer sur le menu *Service*,
4. Cliquer sur le bouton 'Créer un service', un formulaire d'enregistrement de service s'ouvre en haut de la page :

   Dans le formulaire, saisissez :
      - Le nom du service
      - Le département auquel le service appartient
   Puis cliquer sur le bouton :
      - 'Créer le service' pour l'enregistrer
      - 'Annuler' pour fermer le formulaire.

Démo
~~~~

Le super administrateur John SuperAdmin veut ajouter un nouveau service 'Service 003' appartenant au département 'Département 002' à CID.

.. video:: ../../_static/videos/grh/add_service_button_demo.mkv
    :caption: Ajout d'un nouveau service

10. Le menu 'Poste'
-------------------

Ce menu permet d'afficher la liste de tous les postes de CID.

Procédure
~~~~~~~~~

1. Connectez-vous au logiciel.
2. Cliquez sur le module **GRH**
3. Cliquer sur le menu *Poste* pour le déplier,
4. Cliquer sur le sous-menu *Poste*

   La liste de tous les postes de CID seront affichés.
   Cette liste est présentée sous forme de tableau avec les informations des postes et un bouton de configuration ⚙️ :

    .. list-table:: Détails du tableau
       :header-rows: 1

       * - Attribut
         - Signification

       * - Postes
         - Le nom du poste.

       * - Services
         - Le nom du service auquel ce poste appartient.

       * - ACTION
         - Comprend un bouton de configuration ⚙️ qui ouvre deux boutons : "Modifier" pour modifier le poste et "Supprimer" pour supprimer le poste.

Démo
~~~~

Le super administrateur John SuperAdmin veut afficher la liste de tous les postes de CID :

.. video:: ../../_static/videos/grh/all_jobs_demo.mp4
    :caption: Liste des postes de CID

11. Le bouton 'Créer un poste'
------------------------------

Ce bouton permet d'ajouter un nouveau poste à la liste des postes.

Procédure
~~~~~~~~~

1. Connectez-vous au logiciel.
2. Cliquez sur le module **GRH**
3. Cliquer sur le menu *Poste* pour le déplier,
4. Cliquer sur le sous-menu *Poste*
5. Cliquer sur le bouton 'Créer un poste', un formulaire d'enregistrement de poste s'ouvre en haut de la page :

   Dans le formulaire, saisissez :
      - Le nom du poste
      - Le service auquel le poste appartient
   Puis cliquer sur le bouton :
      - 'Créer le poste' pour l'enregistrer
      - 'Annuler' pour fermer le formulaire.

Démo
~~~~

Le super administrateur John SuperAdmin veut ajouter un nouveau poste 'Poste 004' appartenant au service 'Service 001' à CID.

.. video:: ../../_static/videos/grh/add_job_button_demo.mp4
    :caption: Ajout d'un nouveau poste
