"""Generate the two standalone pages using only the Python standard library."""
from pathlib import Path
from html import escape as e
from urllib.parse import quote
import re
from media import media_sections

ROOT = Path(__file__).resolve().parent
BASE_PATH = '/Expert-Klaviyo'
ORIGIN = 'https://rasoanaivo-prog.github.io' + BASE_PATH
PHONE = '261388050781'
ARROW = '<span class="arrow" aria-hidden="true">↗</span>'

CONTENT = {
 'fr': {
  'title': 'Hari — Plus de ventes grâce à votre email marketing',
  'description': 'Votre trafic mérite de convertir. Hari, expert Klaviyo indépendant, accompagne les boutiques Shopify : emails, fidélisation et optimisation continue.',
  'skip': 'Aller au contenu', 'home': 'Accueil Hari', 'nav': ['Votre croissance', 'À propos', 'La méthode', 'Accompagnement'],
  'navcta': 'Parlons croissance', 'menulabel': 'Ouvrir ou fermer le menu', 'audit': 'Demander mon diagnostic',
  'wa': 'Bonjour Hari, je souhaite un diagnostic de mon email marketing. Voici le lien de ma boutique : ',
  'eyebrow': 'Expert Klaviyo indépendant · Shopify',
  'hero': '<span>Votre trafic.</span><span>Plus de <em>ventes.</em></span>',
  'intro': 'Vous attirez les visiteurs. Je crée les emails qui les aident à passer commande, puis leur donnent envie de revenir.',
  'note': 'Un premier diagnostic gratuit. Directement avec moi.',
  'role': 'Votre expert email marketing', 'portrait': 'Portrait professionnel de Hari',
  'bottom': ['Basé à Madagascar · Clients à l’international', 'Stratégie. Création. Optimisation.'],
  'band': ['Convertir le trafic', 'Faire revenir les clients', 'Construire la croissance'],
  'impactTag': '01 / Votre croissance', 'impactTitle': 'Le prochain achat<br>se prépare <span class="lime">maintenant.</span>',
  'impactIntro': 'Un visiteur qui hésite. Un panier oublié. Un client qui ne revient pas. À chaque étape, un email peut faire avancer la relation.',
  'services': [
   ['Transformer l’intérêt<br><span class="soft">en première commande.</span>', 'Je construis un accueil qui donne envie de découvrir votre marque, rassure et accompagne vers le premier achat.', 'Inscription newsletter · Emails de bienvenue'],
   ['Récupérer les ventes<br><span class="soft">qui vous échappent.</span>', 'Je relance au bon moment, avec le bon message, les visiteurs qui ont laissé un produit dans leur panier ou interrompu leur commande.', 'Abandon de panier · Abandon de paiement, traités séparément'],
   ['Donner envie<br><span class="soft">de revenir.</span>', 'Je crée une suite à la première commande : conseils utiles, produits pertinents et campagnes qui entretiennent le lien avec votre marque.', 'Après-achat · Fidélisation · Campagnes ciblées']
  ],
  'aboutTag': '02 / Derrière les emails', 'aboutTitle': 'Hari.<br>À vos côtés.<br><span>À fond.</span>',
  'aboutLead': 'Je suis Harifetra. Vous pouvez m’appeler Hari.',
  'aboutText': 'J’accompagne les boutiques Shopify qui veulent tirer davantage de leur trafic et de leur base clients. Mon rôle : prendre en main leur email marketing, de la stratégie aux ajustements du quotidien.',
  'aboutText2': 'Après avoir géré des comptes e-commerce en agence, j’ai choisi l’accompagnement direct. Nous échangeons ensemble, je crée vos emails et je suis leur performance.',
  'aboutCta': 'Échangeons sur votre boutique', 'photoTag': 'Harifetra / Hari',
  'facts': [['En direct', 'Votre projet, un seul interlocuteur.'], ['FR / EN', 'Un accompagnement dans votre langue.']],
  'methodTag': '03 / La méthode', 'methodTitle': 'Un cap clair.<br>À chaque étape.',
  'methodIntro': 'Vous savez ce que nous faisons, pourquoi nous le faisons et ce que nous allons mesurer.',
  'steps': [
   ['Comprendre', 'J’étudie votre parcours d’achat et vos emails pour identifier les opportunités prioritaires.'],
   ['Construire', 'Je prépare la stratégie, les textes et le design, puis configure les séquences adaptées à votre boutique.'],
   ['Lancer', 'Nous validons les emails. Je vérifie les parcours et les liens avant la mise en route.'],
   ['Optimiser', 'Pour le suivi continu, j’analyse les achats, les clics et la délivrabilité afin d’ajuster la suite.']
  ],
  'offersTag': '05 / Accompagnement', 'offersTitle': 'Le bon départ.<br>La bonne suite.',
  'offersIntro': 'Nous choisissons le périmètre selon votre situation, vos priorités et votre rythme de croissance.',
  'offers': [
   ['Starter', 'Poser les bases', 'Mission ponctuelle', 'Pour commencer par vos priorités email et avancer sur une première étape bien définie.', ['Un objectif prioritaire', 'Un périmètre ciblé', 'Une base pour la suite']],
   ['Growth', 'Construire l’ensemble', 'Mise en place complète', 'Pour donner une vraie structure à votre email marketing, du premier contact à l’après-achat.', ['Une stratégie cohérente', 'Des séquences adaptées', 'Des emails à votre image']],
   ['Scale', 'Garder le rythme', 'Mise en place + suivi', 'Pour construire, suivre et faire évoluer votre email marketing avec un expert à vos côtés.', ['La base Growth', 'Un suivi dans la durée', 'Des optimisations régulières']]
  ],
  'offerCta': 'Parlons de votre besoin', 'offerNote': 'Les livrables, le calendrier et le tarif sont précisés dans votre proposition après le diagnostic.',
  'examplesTag': '06 / Témoignages clients', 'examplesTitle': 'La performance<br>se suit <span class="lime">ensemble.</span>',
  'examplesIntro': 'Les retours de mes clients sur les commandes, les séquences automatiques et la qualité des envois.',
  'disclaimer': 'Retours clients partagés par Hari.',
  'demo': 'Témoignage client · WhatsApp', 'zoom': 'Agrandir le témoignage', 'close': 'Fermer', 'transcript': 'Transcription de l’échange',
  'examples': [
   ['Des emails qui accompagnent la vente', 'Un retour sur les séquences de bienvenue et d’abandon de panier.', '2.jpg'],
   ['Un regard sur les commandes', 'Un échange autour du suivi des ventes au quotidien.', '3.jpg'],
   ['Des ajustements qui comptent', 'Un point sur la segmentation, la délivrabilité et les automatisations.', '1.jpg']
  ],
  'sourceNote': 'Échange WhatsApp en français.',
  'faqTag': '07 / Questions fréquentes', 'faqTitle': 'Tout simplement.',
  'faqs': [
   ['Je n’ai encore rien mis en place. On peut démarrer ?', 'Oui. Nous partons de votre boutique et de vos objectifs pour définir les premières actions utiles. Je peux prendre en charge la mise en place de Klaviyo et des emails qui accompagnent votre parcours client.'],
   ['Klaviyo est déjà installé. Pouvez-vous reprendre l’existant ?', 'Oui. Je commence par examiner ce qui existe, ce qui fonctionne et ce qui mérite d’être corrigé. Nous priorisons ensuite les améliorations en fonction de votre situation.'],
   ['Que comprend le premier diagnostic gratuit ?', 'Un premier regard sur votre boutique et votre parcours email, puis un échange sur les principales pistes à explorer. Si une analyse approfondie du compte est nécessaire, son périmètre est défini séparément.'],
   ['Vous vous occupez aussi des textes et du design ?', 'Oui. Je travaille la stratégie, les textes, le design et la configuration. Les livrables exacts et les validations nécessaires sont précisés dans la proposition.'],
   ['Quels résultats peut-on attendre ?', 'L’objectif est de mieux convertir et fidéliser. Les résultats dépendent notamment du trafic, de l’offre, de la base clients et de la situation de départ. Nous suivons les ventes attribuées, les clics et la qualité des envois, sans promettre un pourcentage universel.']
  ],
  'contactTag': 'La suite commence ici', 'contactTitle': 'Et si votre<br>prochaine vente<br>était <em>déjà là ?</em>',
  'contactText': 'Envoyez-moi le lien de votre boutique. Regardons ensemble ce que votre email marketing pourrait mieux faire.',
  'contactCta': 'Parlons-en sur WhatsApp', 'footerLine': 'Expert indépendant.<br>Email marketing pour Shopify.', 'footerCopyright': '© 2026 Hari · Harifetra', 'back': 'Retour en haut'
 },
 'en': {
  'title': 'Hari — Turn more of your traffic into sales',
  'description': 'Your traffic deserves to convert. Hari is an independent Klaviyo expert helping Shopify brands with email marketing, retention and ongoing optimisation.',
  'skip': 'Skip to content', 'home': 'Hari home', 'nav': ['Your growth', 'About me', 'The approach', 'Work with me'],
  'navcta': 'Let’s talk growth', 'menulabel': 'Open or close the menu', 'audit': 'Get my email review',
  'wa': 'Hi Hari, I would like an initial review of my email marketing. Here is my store link: ',
  'eyebrow': 'Independent Klaviyo expert · Shopify',
  'hero': '<span>Your traffic.</span><span>More <em>sales.</em></span>',
  'intro': 'You bring the visitors. I create the emails that help them place an order, then give them a reason to come back.',
  'note': 'A free initial review. Directly with me.', 'role': 'Your email marketing expert', 'portrait': 'Professional portrait of Hari',
  'bottom': ['Based in Madagascar · Working worldwide', 'Strategy. Creative. Optimisation.'],
  'band': ['Convert your traffic', 'Bring customers back', 'Build your growth'],
  'impactTag': '01 / Your growth', 'impactTitle': 'The next purchase<br>starts <span class="lime">right here.</span>',
  'impactIntro': 'A visitor on the fence. A forgotten cart. A customer who hasn’t returned. At every stage, an email can move the relationship forward.',
  'services': [
   ['Turn interest<br><span class="soft">into a first order.</span>', 'I build a welcome experience that introduces your brand, builds confidence and helps subscribers make their first purchase.', 'Newsletter signup · Welcome emails'],
   ['Win back sales<br><span class="soft">that slip away.</span>', 'I follow up with the right message at the right time when visitors leave products in their cart or stop before completing checkout.', 'Abandoned cart · Abandoned checkout, handled separately'],
   ['Give customers<br><span class="soft">a reason to return.</span>', 'I build on that first order with helpful advice, relevant products and campaigns that keep customers connected to your brand.', 'Post-purchase · Retention · Targeted campaigns']
  ],
  'aboutTag': '02 / Behind the emails', 'aboutTitle': 'Hari.<br>By your side.<br>All in.',
  'aboutLead': 'I’m Harifetra. You can call me Hari.',
  'aboutText': 'I help Shopify brands get more from their traffic and customer base. My role is to take ownership of their email marketing, from the initial strategy to everyday improvements.',
  'aboutText2': 'After managing e-commerce accounts in an agency, I chose to work directly with brands. You speak with me, I create your emails and I keep track of their performance.',
  'aboutCta': 'Let’s talk about your store', 'photoTag': 'Harifetra / Hari',
  'facts': [['Direct access', 'One person who knows your project.'], ['FR / EN', 'Support in your language.']],
  'methodTag': '03 / The approach', 'methodTitle': 'A clear direction.<br>Every step of the way.',
  'methodIntro': 'You know what we’re doing, why we’re doing it and what we’ll be measuring.',
  'steps': [
   ['Understand', 'I review your buying journey and emails to identify the most useful opportunities.'],
   ['Build', 'I develop the strategy, copy and design, then set up sequences that fit your store.'],
   ['Launch', 'We approve the emails together. I check the customer journeys and links before going live.'],
   ['Improve', 'With ongoing support, I review purchases, clicks and deliverability to guide the next changes.']
  ],
  'offersTag': '05 / Work with me', 'offersTitle': 'Start strong.<br>Keep moving.',
  'offersIntro': 'We choose the right scope for where your store is today, your priorities and your pace of growth.',
  'offers': [
   ['Starter', 'Lay the foundations', 'One-time project', 'Focus on your email priorities and move forward with a clearly defined first step.', ['One priority goal', 'A focused scope', 'A foundation to build on']],
   ['Growth', 'Build the whole picture', 'Complete setup', 'Give your email marketing a clear structure, from first contact to the post-purchase experience.', ['A coherent strategy', 'Sequences for your store', 'Emails that feel like your brand']],
   ['Scale', 'Keep the momentum', 'Setup + ongoing support', 'Build, track and improve your email marketing with a dedicated expert by your side.', ['The Growth foundation', 'Ongoing support', 'Regular optimisation']]
  ],
  'offerCta': 'Let’s discuss your needs', 'offerNote': 'Deliverables, timing and pricing are set out in your proposal after the initial review.',
  'examplesTag': '06 / Client testimonials', 'examplesTitle': 'Track progress.<br><span class="lime">Stay connected.</span>',
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
   ['Klaviyo is already installed. Can you improve what’s there?', 'Yes. I begin by reviewing what exists, what works and what needs attention. We then prioritise improvements based on your situation.'],
   ['What does the free initial review include?', 'An initial look at your store and email journey, followed by a conversation about the main opportunities. If an in-depth account audit is needed, we define that scope separately.'],
   ['Do you also handle copy and design?', 'Yes. I work on strategy, copy, design and setup. Your proposal specifies the exact deliverables and the approvals needed.'],
   ['What results can I expect?', 'The goal is to improve conversion and retention. Results depend on your traffic, offer, customer base and starting point. We track attributed sales, clicks and sending quality, without promising a universal percentage.']
  ],
  'contactTag': 'Your next step starts here', 'contactTitle': 'What if your<br>next sale was<br><em>already here?</em>',
  'contactText': 'Send me your store link. Let’s look at what your email marketing could be doing better.',
  'contactCta': 'Let’s talk on WhatsApp', 'footerLine': 'Independent expert.<br>Email marketing for Shopify.', 'footerCopyright': '© 2026 Hari · Harifetra', 'back': 'Back to top'
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
 base = '/' if lang == 'fr' else '/en/'
 wa = 'https://wa.me/' + PHONE + '?text=' + quote(c['wa'])
 def cta(text, cls='button', url=wa):
  return f'<a class="{cls}" href="{e(url,quote=True)}" target="_blank" rel="noopener noreferrer">{e(text)}{ARROW}</a>'
 ids = ['growth','about','designs','offers','examples']
 nav_labels = [c['nav'][0], c['nav'][1], 'Emails', c['nav'][3], 'Témoignages' if lang=='fr' else 'Testimonials']
 nav = ''.join(f'<a href="#{i}">{e(t)}</a>' for i,t in zip(ids,nav_labels))
 languages = ''.join(f'<a href="{url}" data-language="{lc}" lang="{lc}" hreflang="{lc}" aria-label="{label}"{(" aria-current=\"page\"" if lc==lang else "")}>{lc.upper()}</a>' for lc,url,label in [('fr','/','Français'),('en','/en/','English')])
 services = ''.join(f'<article class="service reveal"><span class="service-number">0{i}</span><h3>{title}</h3><div class="service-detail"><p>{e(text)}</p><small>{e(tag)}</small></div></article>' for i,(title,text,tag) in enumerate(c['services'],1))
 steps = ''.join(f'<article class="step reveal"><span class="step-index">0{i}</span><h3>{e(title)}</h3><p>{e(text)}</p></article>' for i,(title,text) in enumerate(c['steps'],1))
 offers = ''
 for i,(name,benefit,kind,text,items) in enumerate(c['offers']):
  offers += f'<article class="offer {"featured" if i==1 else ""} reveal"><div class="offer-top"><span>{e(kind)}</span><span>0{i+1}</span></div><h3>{name}</h3><p><strong>{e(benefit)}</strong></p><p>{e(text)}</p><ul>{"".join(f"<li>{e(item)}</li>" for item in items)}</ul>{cta(c["offerCta"],"text-link")}</article>'
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
<meta property="og:title" content="{e(c['title'],quote=True)}"><meta property="og:description" content="{e(c['description'],quote=True)}"><meta property="og:type" content="website"><meta property="og:url" content="{ORIGIN}{base}"><meta property="og:locale" content="{'fr_FR' if lang=='fr' else 'en_GB'}">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="/assets/style.css"><link rel="stylesheet" href="/assets/media.css"><link rel="stylesheet" href="/assets/refresh.css"><link rel="preload" as="image" href="/assets/hari-banner.webp"><script src="/assets/app.js" defer></script></head>
<body id="top"><a class="skip" href="#main">{c['skip']}</a>
<header class="header"><div class="nav-inner wrap"><a class="brand" href="{base}" aria-label="{c['home']}">HARI<span> /</span></a><nav class="desktop-nav" aria-label="{'Navigation principale' if lang=='fr' else 'Main navigation'}">{nav}</nav><div class="nav-tools"><nav class="languages" aria-label="{'Langue' if lang=='fr' else 'Language'}">{languages}</nav>{cta(c['navcta'])}<button class="menu-toggle" aria-label="{c['menulabel']}" aria-expanded="false" aria-controls="mobile-nav">Menu <span aria-hidden="true">☰</span></button></div></div><nav class="mobile-nav" id="mobile-nav" hidden aria-label="{'Navigation mobile' if lang=='fr' else 'Mobile navigation'}">{nav}<a href="#contact">{c['navcta']}</a></nav></header>
<main id="main">
<section class="hero"><div class="hero-lead wrap"><div><p class="eyebrow lime">{c['eyebrow']}</p><h1>{c['hero']}</h1></div><div class="hero-summary"><p class="hero-description">{c['intro']}</p><div class="hero-actions">{cta(c['audit'])}</div><p class="hero-note">{c['note']}</p></div></div><figure class="hero-banner"><img src="/assets/hari-banner.webp" width="1672" height="941" alt="{'Hari entouré de tableaux de bord Klaviyo en hologrammes bleus' if lang=='fr' else 'Hari surrounded by blue holographic Klaviyo dashboards'}" fetchpriority="high"></figure><div class="hero-bottom wrap"><span>{c['bottom'][0]}</span><span>{c['bottom'][1]}</span></div></section>
<div class="band">{('<i aria-hidden="true">✳</i>').join(f'<span>{e(s)}</span>' for s in c['band'])}</div>
<section class="impact section wrap" id="growth"><div class="section-head reveal"><div><p class="eyebrow lime">{c['impactTag']}</p><h2>{c['impactTitle']}</h2></div><p>{c['impactIntro']}</p></div><div class="service-list">{services}</div></section>
<section class="about section" id="about"><div class="about-grid wrap"><figure class="about-photo reveal"><img src="/assets/hari-about.webp" width="1368" height="1824" alt="{c['portrait']}" loading="lazy"><figcaption class="photo-tag">{c['photoTag']}</figcaption></figure><div class="about-copy reveal"><p class="eyebrow">{c['aboutTag']}</p><h2>{c['aboutTitle']}</h2><p class="lead">{c['aboutLead']}</p><p>{c['aboutText']}</p><p>{c['aboutText2']}</p><div class="facts">{facts}</div>{cta(c['aboutCta'],'text-link')}</div></div></section>
<section class="method section" id="approach"><div class="wrap"><div class="section-head reveal"><div><p class="eyebrow lime">{c['methodTag']}</p><h2>{c['methodTitle']}</h2></div><p>{c['methodIntro']}</p></div><div class="method-layout"><div class="method-grid">{steps}</div><figure class="method-illustration reveal"><img src="/assets/email-method-illustration.webp" width="1200" height="900" alt="{'Illustration d’une enveloppe et de messages organisés pour la stratégie email' if lang=='fr' else 'Illustration of an envelope and organised messages for email strategy'}" loading="lazy"></figure></div></div></section>
{gallery}
<section class="offers section" id="offers"><div class="wrap"><div class="section-head reveal"><div><p class="eyebrow">{c['offersTag']}</p><h2>{c['offersTitle']}</h2></div><p>{c['offersIntro']}</p></div><div class="offer-grid">{offers}</div><p class="offer-note">{c['offerNote']}</p></div></section>
<section class="examples section wrap" id="examples"><div class="section-head reveal"><div><p class="eyebrow lime">{c['examplesTag']}</p><h2>{c['examplesTitle']}</h2></div><p>{c['examplesIntro']}</p></div><div class="example-grid">{examples}</div></section>
<section class="faq section wrap" id="faq"><div class="faq-grid"><div class="reveal"><p class="eyebrow lime">{c['faqTag']}</p><h2>{c['faqTitle']}</h2></div><div>{faqs}</div></div></section>
<section class="contact section" id="contact"><div class="wrap contact-grid"><div class="reveal"><p class="eyebrow">{c['contactTag']}</p><h2>{c['contactTitle']}</h2></div><div class="contact-right"><img class="contact-illustration" src="/assets/contact-illustration.webp" width="1200" height="900" alt="{'Illustration de bulles de discussion et d’une enveloppe' if lang=='fr' else 'Illustration of chat bubbles and an envelope'}" loading="lazy"><p>{c['contactText']}</p>{cta(c['contactCta'],'button dark')}<a class="contact-number" href="https://wa.me/{PHONE}" target="_blank" rel="noopener noreferrer">WhatsApp · +261 38 80 507 81</a></div></div></section>
</main><footer class="footer wrap"><div class="footer-top"><a class="brand" href="#top" aria-label="{c['home']}">HARI<span> /</span></a><p>{c['footerLine']}</p></div><div class="footer-bottom"><span>{c['footerCopyright']}</span><a href="#top">{c['back']} ↑</a></div></footer>
<dialog class="proof-dialog" id="proof-dialog" aria-labelledby="dialog-label"><div class="dialog-header"><p id="dialog-label">{c['demo']}</p><button class="dialog-close" autofocus>{c['close']} ×</button></div><div class="dialog-body"><img alt=""><div class="transcript"></div></div></dialog>{templates}
</body></html>'''

def page(lang):
 # Keep local links inside the GitHub Pages project on both language pages.
 return re.sub(r'''(\b(?:href|src|data-proof)=["'])/(?!/)''',
               lambda match: match.group(1) + BASE_PATH + '/', _page(lang))

if __name__ == '__main__':
 for lang in ('fr','en'):
  p=ROOT/('en/index.html' if lang=='en' else 'index.html')
  p.parent.mkdir(parents=True,exist_ok=True)
  p.write_text(page(lang),encoding='utf-8')
  print('Generated',p.relative_to(ROOT))
