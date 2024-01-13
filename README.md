# Football Vision App

## Ce projet s'inscrit dans le cadre des matières suivantes:
- Médias sociaux et big data
- Architecture des applications

## Table des matières

- [Introduction](#Introduction)
- [Technologies](#Technologies Utilisées)
- [Fonctionnalités](#Fonctionnalités)
- [Installation](#Installation)
- [Utilisation](#Utilisation)

## Introduction

Football Vision App est une application de vision par ordinateur basée sur le travail de Jac99 (https://github.com/jac99/FootAndBall). Elle utilise Pytorch et OpenCV pour effectuer la détection d'objets dans des vidéos. Notre projet vise à étendre les fonctionnalités de cette application et à l'intégrer à une interface web via un cadre architectural, en utilisant Django.

<img src="https://cdn.discordapp.com/attachments/1183508687923453956/1193901735861829713/homepage.png?ex=65ae66a3&is=659bf1a3&hm=8c8cd34d4ff13ff30957fef89cfe21f6db9d5c6734e1a46966cd440ded5d1a26&" alt="homepage">

## Technologies Utilisées

- Django 
- Pytorch
- OpenCV

## Fonctionnalités

L'application FootAndBall permet de détecter les joueurs et le ballon de football dans une vidéo, par exemple un replay de match. Le résultat est une vidéo annotée avec des boîtes indiquant l'emplacement des objets détectés. Football Vision App offre une interface web permettant aux utilisateurs de se connecter à leur tableau de bord et d'envoyer une vidéo pour traitement par FootAndBall, cela sans avoir à installer l'application de base sur la machine.

## Installation

### Prérequis : Python 3.7 et Django doivent être installés sur votre machine pour faire fonctionner cette application localement.

Pour installer le site web sur votre machine, suivez ces étapes :

Sur Windows :

```bash
python3.7 -m venv myenv
```

```bash
myenv/scripts/activate
```

Installez les packages nécessaires :

```bash
pip install -r requirements.txt
```

Il est possible que certains packages ne s'installent pas via la commande au dessus.
Selon le message d'erreur, veuillez installer le package manquant via pip (dans votre environnement virtuel).

Ensuite, lancer les commandes suivantes :

```bash
cd footballVision
python manage.py runserver
python manage.py migrate #will create the db.sqlite3
python manage.py createsuperuser  # If needed
```

Cette application utilise Pytorch. Bien qu'il soit possible d'entraîner le modèle soi-même, il est recommandé d'utiliser les poids déjà existants pour des raisons de temps et de performance.

## Utilisation

Une fois votre serveur démarré, inscrivez-vous via la page /register pour pouvoir vous connecter à l'application.

<img alt="register" src="https://cdn.discordapp.com/attachments/1183508687923453956/1193901736264478740/register.png?ex=65ae66a3&is=659bf1a3&hm=17c4a9c09cc888d4e8388cc120d74f8c018523d0b3da5defb8ad8be357f3edc7&">

Passé cette étape, vous pourrez vous connecter et accéder à votre tableau de bord ainsi qu'à l'interface pour utiliser FootballVisionApp.

<img src="https://cdn.discordapp.com/attachments/1183508687923453956/1193901735454969936/footballvision.png?ex=65ae66a3&is=659bf1a3&hm=b26726df6dd6382d2a7ef7fb46392bf76cd3dd42937e89e8e1b4f58183c4f29b&" alt="footballVisionApp">

### **Il est important d'autoriser le téléchargement via le site web afin que le résultat du process soit déposé sur votre machine.**