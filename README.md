# Hari — Expert Klaviyo

Site public : https://harishift.com/

Site vitrine bilingue, en français (`/`) et anglais (`/en/`), hébergé sur GitHub Pages depuis la branche `main` avec le domaine personnalisé `harishift.com`.

## Modifier le site

- Textes et structure : `build.py` ; galerie des emails : `media.py` ; tarifs et détails des offres FR/EN : `offers.py`.
- Styles : `assets/style.css`, `assets/fonts.css`, `assets/media.css`, `assets/refresh.css`, `assets/offers.css`.
- Interactions : `assets/app.js` ; fiches détaillées des offres : `assets/offers.js` ; réservation Calendly : `assets/booking.js`.
- Régénérer les pages avec `python3 build.py`, puis publier les fichiers modifiés sur `main`.
- Aucune installation de dépendances nécessaire. GitHub Pages sert directement les fichiers HTML générés.

Les plafonds d’emails, le nombre de flows et les campagnes par semaine sont définis dans `PLANS` (`offers.py`). Les fiches, la FAQ et les repères de « Votre croissance » réutilisent ces données. Les ressources CSS et JavaScript portent une empreinte de contenu pour éviter les anciennes mises en page en cache.

Ordre de la page : accroche et bannière, croissance et extrait d’un témoignage, offres, designs d’emails, témoignages, méthode, présentation, FAQ et contact. Le suivi, les audits réguliers, les optimisations et les A/B tests sont réservés à Growth et Scale ; Starter reste une mise en place ponctuelle.

## Identité visuelle

Sora pour les titres et DM Sans pour les textes, auto-hébergées avec leurs licences OFL. Bannière 16:9, un portrait dans À propos et deux illustrations pour Méthode et Contact. Trois modèles d’emails et trois témoignages WhatsApp avec agrandissement.

Le site utilise le domaine personnalisé `harishift.com` via GitHub Pages. Le fichier `CNAME` contient `harishift.com`, et les liens, images et métadonnées utilisent la racine du domaine. Le fichier `.nojekyll` indique que le site est statique et ne nécessite pas Jekyll. L’ancienne adresse `hari-klaviyo-expert.html` redirige vers l’accueil.

Les coordonnées sont définies dans `build.py` : `BOOKING_URL` pour l’audit gratuit de 30 minutes, `EMAIL` pour l’adresse professionnelle et `PHONE` pour WhatsApp.

Les boutons d’audit ouvrent le widget officiel Calendly en pop-up, y compris dans le menu mobile et les fiches des offres. Le lien direct reste disponible si le script externe est bloqué ou pas encore chargé. Une fiche d’offre est fermée avant d’ouvrir Calendly pour éviter la superposition des fenêtres. La réservation et les disponibilités sont gérées dans Calendly ; aucun rendez-vous n’est créé au simple clic sur le bouton.

L’adresse `hello@harishift.com` est un lien `mailto:` dans Contact. Les boutons de discussion sur les offres restent sur WhatsApp et ouvrent un message prérempli sans l’envoyer automatiquement. Le site ne charge aucun outil d’analyse d’audience ; Calendly est un service externe de réservation avec ses propres cookies et informations de confidentialité.
