"""Generate the two standalone pages using only the Python standard library."""
from pathlib import Path
from html import escape as e
from urllib.parse import quote
from hashlib import sha256
import re
from media import media_sections
from offers import FLOWS, PLANS, campaigns_faq, offers_section

ROOT = Path(__file__).resolve().parent
BASE_PATH = ''
ORIGIN = 'https://harishift.com'
PHONE = '261388050781'
EMAIL = 'hello@harishift.com'
BOOKING_URL = 'https://calendly.com/hello-harishift/30min'
ARROW = '<span class="arrow" aria-hidden="true">↗</span>'

CONTENT = {
 'fr': {
  'title': 'Hari — Plus de ventes grâce à votre email marketing',
  'description': 'Votre trafic mérite de convertir. Hari, expert Klaviyo indépendant, accompagne les boutiques Shopify : emails, fidélisation et optimisation continue.',
  'skip': 'Aller au contenu', 'home': 'Accueil Hari', 'nav': ['Votre croissance', 'À propos', 'La méthode', 'Offres & tarifs'],
  'viewOffers': 'Voir les offres',
  'navcta': 'Audit gratuit · 30 min', 'menulabel': 'Ouvrir ou fermer le menu', 'audit': 'Réserver mon audit gratuit',
  'wa': 'Bonjour Hari, je souhaite échanger avec vous au sujet de ma boutique et de vos offres Klaviyo. Voici le lien de ma boutique : ',
  'eyebrow': 'Expert Klaviyo indépendant · Shopify',
  'hero': '<span>Votre trafic.</span><span>Plus de <em>ventes.</em></span>',
  'intro': 'Vous attirez les visiteurs. Je crée les flows et les campagnes email qui les aident à passer commande, puis leur donnent envie de revenir.',
  'note': '30 minutes offertes pour identifier vos priorités. Directement avec moi, sans engagement.',
  'role': 'Votre expert email marketing', 'portrait': 'Portrait professionnel de Hari',
  'bottom': ['Basé à Madagascar · Clients à l’international', 'Stratégie. Création. Optimisation.'],
  'band': ['Convertir le trafic', 'Faire revenir les clients', 'Construire la croissance'],
  'impactTag': '01 / Votre croissance', 'impactTitle': 'Le prochain achat<br>se prépare <span class="lime">maintenant.</span>',
  'impactIntro': 'De l’inscription au réachat, vos flows accompagnent le parcours client. Growth et Scale ajoutent des campagnes et un pilotage régulier.',
  'serviceLabels': ['Les bases · dès Starter', 'Le suivi régulier · dès Growth', 'La cadence renforcée · Scale'],
  'services': [
   ['Accueillir.<br>Récupérer les ventes.', 'Une pop-up pour développer votre base, un accueil pour vos nouveaux inscrits et deux relances distinctes pour les abandons de cart et de checkout.', 'Ces trois flows et la pop-up sont inclus dans toutes les offres.'],
   ['Relancer l’intérêt.<br>Fidéliser.', 'Relancez les visiteurs identifiés après une visite du site ou d’une fiche produit, puis accompagnez vos clients après leur achat.', f'Growth : {PLANS["growth"]["campaigns"]} campagnes par semaine, suivi, audits et optimisation des flows.'],
   ['Réactiver.<br>Garder une base engagée.', 'Réactivez les anciens clients et entretenez une base engagée, avec une dernière relance avant d’écarter les contacts inactifs des envois.', f'Scale : {PLANS["scale"]["campaigns"]} campagnes par semaine, ou {PLANS["scale-plus"]["campaigns"]} avec le rythme renforcé.']
  ],
  'proofQuote': 'Ça se voit direct : plus de CA, moins de galères de délivrabilité…',
  'proofCaption': 'Retour client · Suivi et optimisation', 'proofCta': 'Lire l’échange WhatsApp',
  'aboutTag': '06 / Derrière les emails', 'aboutTitle': 'Hari.<br>À vos côtés.<br><span>À fond.</span>',
  'aboutLead': 'Je suis Harifetra. Vous pouvez m’appeler Hari.',
  'aboutText': 'J’accompagne les boutiques Shopify qui veulent tirer davantage de leur trafic et de leur base clients. Mon rôle : prendre en main leur email marketing, de la stratégie aux ajustements du quotidien.',
  'aboutText2': 'Après avoir géré des comptes e-commerce en agence, j’ai choisi l’accompagnement direct. Nous échangeons ensemble, je crée vos emails et je suis leur performance.',
  'aboutCta': 'Échangeons sur votre boutique', 'photoTag': 'Harifetra / Hari',
  'facts': [['En direct', 'Votre projet, un seul interlocuteur.'], ['FR / EN', 'Un accompagnement dans votre langue.']],
  'methodTag': '05 / La méthode', 'methodTitle': 'Un cap clair.<br>À chaque étape.',
  'methodIntro': 'Vous savez ce que nous faisons, pourquoi nous le faisons et ce que nous allons mesurer.',
  'steps': [
   ['Comprendre', 'J’étudie votre parcours d’achat et vos emails pour identifier les opportunités prioritaires.'],
   ['Construire', 'Je prépare la stratégie, les textes, le design et les flows prévus dans votre offre. Avec Growth et Scale, j’organise aussi le calendrier des campagnes.'],
   ['Lancer', 'Nous validons les emails. Je vérifie les parcours et les liens avant la mise en route.'],
   ['Optimiser', 'Avec Growth et Scale, je suis les performances, réalise des audits réguliers et optimise les flows. Les A/B tests avancent selon les données disponibles.']
  ],
  'examplesTag': '04 / Témoignages clients', 'examplesTitle': 'La performance<br>se suit <span class="lime">ensemble.</span>',
  'examplesIntro': 'Les retours de mes clients sur les commandes, les flows et la qualité des envois.',
  'disclaimer': 'Retours clients partagés par Hari.',
  'demo': 'Témoignage client · WhatsApp', 'zoom': 'Agrandir le témoignage', 'close': 'Fermer', 'transcript': 'Transcription de l’échange',
  'examples': [
   ['Des emails qui accompagnent la vente', 'Un retour sur les flows Welcome et Abandoned Cart.', '2.jpg'],
   ['Un regard sur les commandes', 'Un échange autour du suivi des ventes au quotidien.', '3.jpg'],
   ['Des ajustements qui comptent', 'Un point sur la segmentation, la délivrabilité et les automatisations.', '1.jpg']
  ],
  'sourceNote': 'Échange WhatsApp en français.',
  'faqTag': '07 / Questions fréquentes', 'faqTitle': 'Tout simplement.',
  'faqs': [
   ['Je n’ai encore rien mis en place. On peut démarrer ?', 'Oui. Nous partons de votre boutique et de vos objectifs pour définir les premières actions utiles. Je peux prendre en charge la mise en place de Klaviyo et des emails qui accompagnent votre parcours client.'],
   ['Klaviyo est déjà installé. Pouvez-vous reprendre l’existant ?', 'Oui. Je commence par examiner ce qui existe, ce qui fonctionne et ce qui mérite d’être corrigé. Nous priorisons ensuite les améliorations en fonction de votre situation.'],
   ['Que comprend l’audit gratuit de 30 minutes ?', 'Nous échangeons pendant 30 minutes sur votre boutique, vos flows, vos campagnes et votre délivrabilité pour identifier les priorités et les prochaines actions. Cet audit est gratuit et sans engagement. Les audits réguliers et les optimisations font ensuite partie de l’accompagnement Growth ou Scale.'],
   ['Vous vous occupez aussi des textes et du design ?', 'Oui. Je travaille la stratégie, les textes, le design et la configuration. Les livrables exacts et les validations nécessaires sont précisés dans la proposition.'],
   ['Gérez-vous aussi les campagnes marketing ?', campaigns_faq('fr')],
   ['Quel suivi est inclus après la mise en place ?', 'Growth et Scale comprennent le suivi des performances et de la délivrabilité, des audits réguliers, des optimisations des flows selon leur efficacité et des A/B tests lorsque les données permettent de comparer les résultats. Un bilan mensuel fixe les prochaines priorités. Starter est une mission ponctuelle, sans suivi ni optimisation récurrents.'],
   ['Quels résultats peut-on attendre ?', 'L’objectif est de mieux convertir et fidéliser. Les résultats dépendent notamment du trafic, de l’offre, de la base clients et de la situation de départ. Nous suivons les ventes attribuées, les clics et la qualité des envois, sans promettre un pourcentage universel.']
  ],
  'contactTag': 'La suite commence ici', 'contactTitle': 'Et si votre<br>prochaine vente<br>était <em>déjà là ?</em>',
  'contactText': 'Réservez votre audit gratuit de 30 minutes. Nous faisons le point sur vos flows et vos campagnes pour identifier vos prochaines opportunités de croissance.',
  'contactCta': 'Réserver mes 30 minutes gratuites', 'footerLine': 'Expert indépendant.<br>Email marketing pour Shopify.', 'footerCopyright': '© 2026 Hari · Harifetra', 'back': 'Retour en haut'
 },
 'en': {
  'title': 'Hari — Turn more of your traffic into sales',
  'description': 'Your traffic deserves to convert. Hari is an independent Klaviyo expert helping Shopify brands with email marketing, retention and ongoing optimization.',
  'skip': 'Skip to content', 'home': 'Hari home', 'nav': ['Your growth', 'About me', 'The approach', 'Plans & pricing'],
  'viewOffers': 'View plans',
  'navcta': 'Free audit · 30 min', 'menulabel': 'Open or close the menu', 'audit': 'Book my free audit',
  'wa': 'Hi Hari, I’d like to discuss my store and your Klaviyo services. Here is my store link: ',
  'eyebrow': 'Independent Klaviyo expert · Shopify',
  'hero': '<span>Your traffic.</span><span>More <em>sales.</em></span>',
  'intro': 'You bring the visitors. I create the flows and email campaigns that help them place an order, then give them a reason to come back.',
  'note': '30 minutes to identify your priorities. Directly with me, with no obligation.', 'role': 'Your email marketing expert', 'portrait': 'Professional portrait of Hari',
  'bottom': ['Based in Madagascar · Working worldwide', 'Strategy. Creative. Optimization.'],
  'band': ['Convert your traffic', 'Bring customers back', 'Build your growth'],
  'impactTag': '01 / Your growth', 'impactTitle': 'The next purchase<br>starts <span class="lime">right here.</span>',
  'impactIntro': 'From signup to repeat purchase, your flows support the customer journey. Growth and Scale add regular campaigns and ongoing management.',
  'serviceLabels': ['The foundation · from Starter', 'Ongoing support · from Growth', 'More campaigns · Scale'],
  'services': [
   ['Welcome subscribers.<br>Recover lost sales.', 'Grow your list with a pop-up, welcome new subscribers and follow up separately on abandoned carts and abandoned checkouts.', 'These three flows and the pop-up are included in every plan.'],
   ['Follow up.<br>Bring customers back.', 'Reconnect with identified visitors after a site or product-page visit, then support customers after their purchase.', f'Growth: {PLANS["growth"]["campaigns"]} campaigns per week, ongoing support, audits and flow optimization.'],
   ['Re-engage.<br>Keep your list healthy.', 'Reconnect with past customers and give inactive subscribers one last chance to engage before excluding them from future sends.', f'Scale: {PLANS["scale"]["campaigns"]} campaigns per week, or {PLANS["scale-plus"]["campaigns"]} with Scale Plus.']
  ],
  'proofQuote': 'It shows straight away: more revenue, fewer deliverability headaches…',
  'proofCaption': 'Client feedback · Ongoing support and optimization', 'proofCta': 'Read the WhatsApp exchange',
  'aboutTag': '06 / Behind the emails', 'aboutTitle': 'Hari.<br>By your side.<br>All in.',
  'aboutLead': 'I’m Harifetra. You can call me Hari.',
  'aboutText': 'I help Shopify brands get more from their traffic and customer base. My role is to take ownership of their email marketing, from the initial strategy to everyday improvements.',
  'aboutText2': 'After managing e-commerce accounts in an agency, I chose to work directly with brands. You speak with me, I create your emails and I keep track of their performance.',
  'aboutCta': 'Let’s talk about your store', 'photoTag': 'Harifetra / Hari',
  'facts': [['Direct access', 'One person who knows your project.'], ['FR / EN', 'Support in your language.']],
  'methodTag': '05 / The approach', 'methodTitle': 'A clear direction.<br>Every step of the way.',
  'methodIntro': 'You know what we’re doing, why we’re doing it and what we’ll be measuring.',
  'steps': [
   ['Understand', 'I review your buying journey and emails to identify the most useful opportunities.'],
   ['Build', 'I create the strategy, copy, design and flows included in your plan. With Growth and Scale, I also build your campaign calendar.'],
   ['Launch', 'We approve the emails together. I check the customer journeys and links before going live.'],
   ['Improve', 'With Growth and Scale, I monitor performance, run regular audits and optimize your flows. A/B testing progresses as enough data becomes available.']
  ],
  'examplesTag': '04 / Client testimonials', 'examplesTitle': 'Track progress.<br><span class="lime">Stay connected.</span>',
  'examplesIntro': 'Client feedback on orders, automated email sequences and sending quality.',
  'disclaimer': 'Client feedback shared by Hari.',
  'demo': 'Client testimonial · WhatsApp', 'zoom': 'Enlarge the testimonial', 'close': 'Close', 'transcript': 'English translation of the conversation',
  'examples': [
   ['Emails that support the sale', 'Feedback on welcome and abandoned-cart sequences.', '2.jpg'],
   ['Keeping an eye on orders', 'A conversation about tracking sales day to day.', '3.jpg'],
   ['The details worth improving', 'An update on segmentation, deliverability and automations.', '1.jpg']
  ],
  'sourceNote': 'Conversation in French. Open for the English translation.',
  'faqTag': '07 / Common questions', 'faqTitle': 'Let’s keep it simple.',
  'faqs': [
   ['I haven’t set anything up yet. Can we start from scratch?', 'Yes. We start with your store and your goals to work out the most useful first steps. I can set up Klaviyo and the emails that support your customer journey.'],
   ['Klaviyo is already installed. Can you improve what’s there?', 'Yes. I begin by reviewing what exists, what works and what needs attention. We then prioritize improvements based on your situation.'],
   ['What does the free 30-minute audit include?', 'We spend 30 minutes discussing your store, flows, campaigns and deliverability to identify priorities and practical next steps. The audit is free, with no obligation. Regular audits and optimization are then included in ongoing Growth or Scale support.'],
   ['Do you also handle copy and design?', 'Yes. I work on strategy, copy, design and setup. Your proposal specifies the exact deliverables and the approvals needed.'],
   ['Do you also manage marketing campaigns?', campaigns_faq('en')],
   ['What support is included after setup?', 'Growth and Scale include performance and deliverability monitoring, regular audits, improvements to flows based on their performance, and A/B testing when there is enough data to compare results. A monthly review sets the next priorities. Starter is a one-time setup project without ongoing support or optimization.'],
   ['What results can I expect?', 'The goal is to improve conversion and retention. Results depend on your traffic, offer, customer base and starting point. We track attributed sales, clicks and sending quality, without promising a universal percentage.']
  ],
  'contactTag': 'Your next step starts here', 'contactTitle': 'What if your<br>next sale was<br><em>already here?</em>',
  'contactText': 'Book your free 30-minute audit. We’ll review your flows and campaigns to identify your next growth opportunities.',
  'contactCta': 'Book my free 30 minutes', 'footerLine': 'Independent expert.<br>Email marketing for Shopify.', 'footerCopyright': '© 2026 Hari · Harifetra', 'back': 'Back to top'
 }
}

TRANSCRIPTS = {
 'fr': [
  ['Franchement, les flows que t’as mis en place… c’est une dinguerie 😭🔥', 'Ahah, ça commence à bien tourner ?', 'De fou ! Même quand on lance aucune campagne, ça continue de ramener des commandes. Le Welcome et l’abandon de panier font clairement le taf tout seuls.', 'Trop bien 🔥 Je vais continuer à optimiser les séquences pour pousser ça encore plus loin.'],
  ['Frérot, je comprends rien à Klaviyo 😭 Mais là je regarde le CA tous les jours et ça monte en flèche 🔥', 'Ahah, c’est exactement le but ! Les flows bossent en arrière-plan et récupèrent des ventes automatiquement.', 'Bah écoute, je sais pas ce que t’as touché mais continue 😂 Chaque matin je vois les revenus grimper, c’est une folie !', 'On garde le rythme 💪 Je surveille les résultats et j’optimise encore tout ce qui peut l’être.'],
  ['Salut Hari, je viens de checker les résultats de la semaine… ça a grave repris depuis les changements 🔥', 'Trop bien ! J’ai surtout retravaillé la segmentation et retiré les profils moins engagés.', 'Ça se voit direct : plus de CA, moins de galères de délivrabilité… et les flows font clairement leurs preuves aussi 🙌', 'Top, merci pour ton retour ! Je garde un œil dessus et j’ajuste la suite 👌']
 ],
 'en': [
  ['Honestly, the flows you set up… they’re wild 😭🔥', 'Haha, are they starting to work well?', 'Absolutely! Even when we don’t launch a campaign, orders keep coming in. The welcome and abandoned-cart flows are clearly doing their thing on their own.', 'Love that 🔥 I’ll keep optimising the sequences to take this further.'],
  ['Mate, I don’t understand Klaviyo at all 😭 But I check revenue every day now and it’s shooting up 🔥', 'Haha, that’s exactly the idea! The flows work in the background and recover sales automatically.', 'Well, I don’t know what you changed, but keep going 😂 Every morning I see revenue climbing. It’s crazy!', 'Let’s keep it going 💪 I’m watching the results and continuing to optimise everything I can.'],
  ['Hi Hari, I just checked this week’s results… things have really picked up since the changes 🔥', 'Great! I mainly reworked the segmentation and removed less-engaged profiles.', 'It shows straight away: more revenue, fewer deliverability headaches… and the flows are really proving themselves too 🙌', 'Great, thanks for the feedback! I’m keeping an eye on it and adjusting the next steps 👌']
 ]
}

def _page(lang):
 c = CONTENT[lang]
 offers_version = sha256((ROOT / 'assets/offers.css').read_bytes() + (ROOT / 'assets/offers.js').read_bytes()).hexdigest()[:10]
 ui_version = sha256(b''.join((ROOT / ('assets/' + file)).read_bytes() for file in ('style.css', 'media.css', 'refresh.css', 'app.js'))).hexdigest()[:10]
 booking_version = sha256((ROOT / 'assets/booking.js').read_bytes()).hexdigest()[:10]
 base = '/' if lang == 'fr' else '/en/'
 wa = 'https://wa.me/' + PHONE + '?text=' + quote(c['wa'])
 def cta(text, cls='button', url=BOOKING_URL):
  booking = ' data-calendly aria-haspopup="dialog"' if url == BOOKING_URL else ''
  return f'<a class="{cls}" href="{e(url,quote=True)}" target="_blank" rel="noopener noreferrer"{booking}>{e(text)}{ARROW}</a>'
 ids = ['growth','offers','designs','examples','about']
 nav_labels = [c['nav'][0], c['nav'][3], 'Emails', 'Témoignages' if lang=='fr' else 'Testimonials', c['nav'][1]]
 nav = ''.join(f'<a href="#{i}">{e(t)}</a>' for i,t in zip(ids,nav_labels))
 languages = ''.join(f'<a href="{url}" data-language="{lc}" lang="{lc}" hreflang="{lc}" aria-label="{label}"{(" aria-current=\"page\"" if lc==lang else "")}>{lc.upper()}</a>' for lc,url,label in [('fr','/','Français'),('en','/en/','English')])
 flow_groups = (FLOWS[:PLANS['starter']['flows']], FLOWS[PLANS['starter']['flows']:PLANS['growth']['flows']], FLOWS[PLANS['growth']['flows']:PLANS['scale']['flows']])
 services = ''.join(f'<article class="growth-service reveal"><p class="growth-service-label">{e(c["serviceLabels"][i])}</p><h3>{title}</h3><p class="growth-service-description">{e(text)}</p><ul class="growth-flow-tags">{"".join(f"<li>{e(flow)}</li>" for flow in flow_groups[i])}</ul><p class="growth-service-scope">{e(tag)}</p></article>' for i,(title,text,tag) in enumerate(c['services']))
 proof_teaser = f'<figure class="growth-proof"><div><blockquote>« {e(c["proofQuote"])} »</blockquote><figcaption>{e(c["proofCaption"])}</figcaption></div><button class="text-link" type="button" data-proof="/assets/example-1.jpg" data-proof-alt="{e(c["examples"][2][0],quote=True)}" data-transcript="#transcript-2">{e(c["proofCta"])}{ARROW}</button></figure>'
 steps = ''.join(f'<article class="step reveal"><span class="step-index">0{i}</span><h3>{e(title)}</h3><p>{e(text)}</p></article>' for i,(title,text) in enumerate(c['steps'],1))
 offers = offers_section(lang, PHONE, BOOKING_URL)
 examples = ''
 templates = ''
 for i,(title,text,asset) in enumerate(c['examples']):
  examples += f'<figure class="example-card reveal"><button class="example-image" data-proof="/assets/example-{asset}" data-transcript="#transcript-{i}" aria-label="{e(c["zoom"]+": "+title,quote=True)}"><img src="/assets/example-{asset}" alt="{e(c["demo"]+" — "+title,quote=True)}" width="774" height="1200" loading="lazy"><span class="demo-label">{e(c["demo"])}</span><span class="zoom-label" aria-hidden="true">↗</span></button><figcaption><strong>{e(title)}</strong><p>{e(text)}</p><span class="example-source">{e(c["sourceNote"])}</span></figcaption></figure>'
  role = 'Client' if lang=='fr' else 'Client'
  transcript = ''.join(f'<p><strong>{role if j%2==0 else "Hari"} :</strong> {e(line)}</p>' for j,line in enumerate(TRANSCRIPTS[lang][i]))
  templates += f'<template id="transcript-{i}"><h3>{e(c["transcript"])}</h3>{transcript}</template>'
 faqs=''.join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q,a in c['faqs'])
 facts=''.join(f'<div><strong>{e(a)}</strong><span>{e(b)}</span></div>' for a,b in c['facts'])
 gallery,media_templates = media_sections(lang)
 templates += media_templates
 return f'''<!doctype html>
<html lang="{lang}">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#141614">
<title>{e(c['title'])}</title><meta name="description" content="{e(c['description'],quote=True)}">
<link rel="canonical" href="{ORIGIN}{base}"><link rel="alternate" hreflang="fr" href="{ORIGIN}/"><link rel="alternate" hreflang="en" href="{ORIGIN}/en/"><link rel="alternate" hreflang="x-default" href="{ORIGIN}/">
<meta property="og:title" content="{e(c['title'],quote=True)}"><meta property="og:description" content="{e(c['description'],quote=True)}"><meta property="og:type" content="website"><meta property="og:url" content="{ORIGIN}{base}"><meta property="og:locale" content="{'fr_FR' if lang=='fr' else 'en_US'}">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="/assets/style.css?v={ui_version}"><link rel="stylesheet" href="/assets/media.css?v={ui_version}"><link rel="stylesheet" href="/assets/refresh.css?v={ui_version}"><link rel="stylesheet" href="/assets/offers.css?v={offers_version}"><link rel="preload" as="image" href="/assets/hari-banner.webp"><script src="/assets/app.js?v={ui_version}" defer></script><script src="/assets/offers.js?v={offers_version}" defer></script><link rel="stylesheet" href="https://assets.calendly.com/assets/external/widget.css"><script src="https://assets.calendly.com/assets/external/widget.js" async></script><script src="/assets/booking.js?v={booking_version}" defer></script></head>
<body id="top"><a class="skip" href="#main">{c['skip']}</a>
<header class="header"><div class="nav-inner wrap"><a class="brand" href="{base}" aria-label="{c['home']}">HARI<span> /</span></a><nav class="desktop-nav" aria-label="{'Navigation principale' if lang=='fr' else 'Main navigation'}">{nav}</nav><div class="nav-tools"><nav class="languages" aria-label="{'Langue' if lang=='fr' else 'Language'}">{languages}</nav>{cta(c['navcta'])}<button class="menu-toggle" aria-label="{c['menulabel']}" aria-expanded="false" aria-controls="mobile-nav">Menu <span aria-hidden="true">☰</span></button></div></div><nav class="mobile-nav" id="mobile-nav" hidden aria-label="{'Navigation mobile' if lang=='fr' else 'Mobile navigation'}">{nav}{cta(c['navcta'])}</nav></header>
<main id="main">
<section class="hero"><div class="hero-lead wrap"><div><p class="eyebrow lime">{c['eyebrow']}</p><h1>{c['hero']}</h1></div><div class="hero-summary"><p class="hero-description">{c['intro']}</p><div class="hero-actions">{cta(c['audit'])}<a class="button button-outline" href="#offers">{e(c['viewOffers'])}</a></div><p class="hero-note">{c['note']}</p></div></div><figure class="hero-banner"><img src="/assets/hari-banner.webp" width="1672" height="941" alt="{'Hari entouré de tableaux de bord Klaviyo en hologrammes bleus' if lang=='fr' else 'Hari surrounded by blue holographic Klaviyo dashboards'}" fetchpriority="high"></figure><div class="hero-bottom wrap"><span>{c['bottom'][0]}</span><span>{c['bottom'][1]}</span></div></section>
<div class="band">{('<i aria-hidden="true">✳</i>').join(f'<span>{e(s)}</span>' for s in c['band'])}</div>
<section class="impact section wrap" id="growth"><div class="section-head reveal"><div><p class="eyebrow lime">{c['impactTag']}</p><h2>{c['impactTitle']}</h2></div><p>{c['impactIntro']}</p></div><div class="growth-services">{services}</div>{proof_teaser}</section>
{offers}
{gallery}
<section class="examples section wrap" id="examples"><div class="section-head reveal"><div><p class="eyebrow lime">{c['examplesTag']}</p><h2>{c['examplesTitle']}</h2></div><p>{c['examplesIntro']}</p></div><div class="example-grid">{examples}</div></section>
<section class="method section" id="approach"><div class="wrap"><div class="section-head reveal"><div><p class="eyebrow lime">{c['methodTag']}</p><h2>{c['methodTitle']}</h2></div><p>{c['methodIntro']}</p></div><div class="method-layout"><div class="method-grid">{steps}</div><figure class="method-illustration reveal"><img src="/assets/email-method-illustration.webp" width="1200" height="900" alt="{'Illustration d’une enveloppe et de messages organisés pour la stratégie email' if lang=='fr' else 'Illustration of an envelope and organised messages for email strategy'}" loading="lazy"></figure></div></div></section>
<section class="about section" id="about"><div class="about-grid wrap"><figure class="about-photo reveal"><img src="/assets/hari-about.webp" width="1368" height="1824" alt="{c['portrait']}" loading="lazy"><figcaption class="photo-tag">{c['photoTag']}</figcaption></figure><div class="about-copy reveal"><p class="eyebrow">{c['aboutTag']}</p><h2>{c['aboutTitle']}</h2><p class="lead">{c['aboutLead']}</p><p>{c['aboutText']}</p><p>{c['aboutText2']}</p><div class="facts">{facts}</div>{cta(c['aboutCta'],'text-link',wa)}</div></div></section>
<section class="faq section wrap" id="faq"><div class="faq-grid"><div class="reveal"><p class="eyebrow lime">{c['faqTag']}</p><h2>{c['faqTitle']}</h2></div><div>{faqs}</div></div></section>
<section class="contact section" id="contact"><div class="wrap contact-grid"><div class="reveal"><p class="eyebrow">{c['contactTag']}</p><h2>{c['contactTitle']}</h2></div><div class="contact-right"><img class="contact-illustration" src="/assets/contact-illustration.webp" width="1200" height="900" alt="{'Illustration de bulles de discussion et d’une enveloppe' if lang=='fr' else 'Illustration of chat bubbles and an envelope'}" loading="lazy"><p>{c['contactText']}</p>{cta(c['contactCta'],'button dark')}<a class="contact-number" href="https://wa.me/{PHONE}" target="_blank" rel="noopener noreferrer">WhatsApp · +261 38 80 507 81</a><a class="contact-email" href="mailto:{e(EMAIL,quote=True)}">{e(EMAIL)}</a></div></div></section>
</main><footer class="footer wrap"><div class="footer-top"><a class="brand" href="#top" aria-label="{c['home']}">HARI<span> /</span></a><p>{c['footerLine']}</p></div><div class="footer-bottom"><span>{c['footerCopyright']}</span><a href="#top">{c['back']} ↑</a></div></footer>
<dialog class="proof-dialog" id="proof-dialog" aria-labelledby="dialog-label"><div class="dialog-header"><p id="dialog-label">{c['demo']}</p><button class="dialog-close" autofocus>{c['close']} ×</button></div><div class="dialog-body"><img alt=""><div class="transcript"></div></div></dialog>{templates}
</body></html>'''

def page(lang):
 # Keep local links rooted at the custom domain on both language pages.
 return re.sub(r'''(\b(?:href|src|data-proof)=["'])/(?!/)''',
               lambda match: match.group(1) + BASE_PATH + '/', _page(lang))

if __name__ == '__main__':
 for lang in ('fr','en'):
  p=ROOT/('en/index.html' if lang=='en' else 'index.html')
  p.parent.mkdir(parents=True,exist_ok=True)
  p.write_text(page(lang),encoding='utf-8')
  print('Generated',p.relative_to(ROOT))
