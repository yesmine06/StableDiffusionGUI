# StableDiffusionGUI
Description
Ce projet utilise un modèle de génération d'images à partir de descriptions textuelles, permettant aux utilisateurs de saisir des invites sous forme de texte, puis de générer des images correspondantes. L'application utilise des technologies modernes telles que PyTorch, Torchvision, et Torchaudio pour exécuter des modèles de deep learning, tout en offrant une interface utilisateur simple et intuitive pour une utilisation facile.

Fonctionnalités principales :
Génération d'images à partir de descriptions textuelles
Interface utilisateur conviviale
Personnalisation de l'interface avec des icônes et des polices
Affichage d'une barre de progression pendant la génération de l'image
Options pour sauvegarder et générer des images
Utilisation des dernières technologies de machine learning avec PyTorch et d'autres bibliothèques
Prérequis
Avant d'exécuter ce projet, assurez-vous d'avoir installé Python et les dépendances suivantes :

Python 3.12+ (ou version compatible)
Pip (gestionnaire de packages Python)

Installation
1. Cloner le dépôt
Clonez ce dépôt sur votre machine locale en utilisant Git :

bash
git clone https://github.com/votre-utilisateur/text-to-image.git
cd text-to-image
2. Créer un environnement virtuel
Il est recommandé de créer un environnement virtuel pour éviter les conflits de dépendances avec d'autres projets.

bash

python -m venv venv
Activez l'environnement virtuel :

Sur Windows :
.\venv\Scripts\activate


3. Installer les dépendances
Une fois l'environnement virtuel activé, installez les dépendances nécessaires à l'aide de pip :
pip install -r requirements.txt

5. Télécharger les modèles pré-entraînés
Si nécessaire, téléchargez les modèles pré-entraînés pour la génération d'images. Vous pouvez les placer dans le répertoire approprié ou les télécharger directement depuis un service cloud selon la configuration du projet.

Utilisation
1. Exécuter l'application
Une fois les dépendances installées, vous pouvez lancer l'application à partir du terminal :

python app.py
Cela démarrera l'interface graphique où vous pourrez entrer des descriptions textuelles et générer des images correspondantes.

2. Interface Utilisateur
Entrée Textuelle : Saisissez la description de l'image que vous souhaitez générer.
Générer l'Image : Appuyez sur le bouton "Générer" pour créer l'image à partir du texte.
Barre de Progression : Une barre de progression s'affichera pendant la génération de l'image.
Sauvegarder l'Image : Vous pouvez sauvegarder l'image générée sur votre machine.

Dépendances

Ce projet utilise les bibliothèques suivantes :

torch : Framework de machine learning pour le calcul numérique et le deep learning.
torchvision : Bibliothèque pour la vision par ordinateur.
torchaudio : Bibliothèque pour le traitement audio (utile pour certains modèles multimodaux).
Pillow : Traitement d'images.
customtkinter : Interface graphique avec des widgets personnalisables.
requests : Pour effectuer des requêtes HTTP.
Vous pouvez installer toutes les dépendances via :
pip install -r requirements.txt
