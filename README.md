# Hari — Expert Klaviyo

Site public : https://hari.klaviyo.expert/

Site vitrine bilingue, en français (`/`) et anglais (`/en/`), hébergé sur GitHub Pages depuis la branche `main`, à la racine du dépôt.

## Modifier le site

- Textes et structure : `build.py` ; galerie des emails : `media.py`.
- Styles : `assets/style.css`, `assets/fonts.css`, `assets/media.css`, `assets/refresh.css`.
- Interactions : `assets/app.js`.
- Régénérer les pages avec `python3 build.py`, puis publier les fichiers modifiés sur `main`.
- Aucune installation de dépendances nécessaire. GitHub Pages sert directement les fichiers HTML générés.

## Identité visuelle

Sora pour les titres et DM Sans pour les textes, auto-hébergées avec leurs licences OFL. Bannière 16:9, un portrait dans À propos et deux illustrations pour Méthode et Contact. Trois modèles d’emails et trois témoignages WhatsApp avec agrandissement.

Le fichier `CNAME` conserve le domaine personnalisé existant. Le fichier `.nojekyll` indique que le site est statique et ne nécessite pas Jekyll. L’ancienne adresse `hari-klaviyo-expert.html` redirige vers l’accueil.

Le site n’utilise aucun outil de suivi ni formulaire externe. Les boutons WhatsApp ouvrent un message prérempli sans l’envoyer automatiquement.
