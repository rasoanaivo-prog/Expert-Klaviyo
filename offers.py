"""Bilingual, scoped offers with Growth as the recommended starting point."""
from html import escape
from urllib.parse import quote


FLOWS = [
    'Welcome', 'Abandoned Checkout', 'Abandoned Cart', 'Post-purchase',
    'Browse Abandonment', 'Site Abandonment', 'Winback', 'Sunset',
]
PLANS = {
    'starter': {'name': 'Starter', 'setup': 790, 'monthly': 0, 'flows': 3, 'emails': 15, 'campaigns': 0},
    'growth': {'name': 'Growth', 'setup': 1490, 'monthly': 550, 'flows': 6, 'emails': 20, 'campaigns': 2},
    'scale': {'name': 'Scale', 'setup': 1790, 'monthly': 800, 'flows': 8, 'emails': 26, 'campaigns': 3},
    'scale-plus': {'name': 'Scale', 'setup': 1790, 'monthly': 1000, 'flows': 8, 'emails': 26, 'campaigns': 4},
}
COPY = {
    'fr': {
        'tag': '02 / Offres & tarifs',
        'title': 'Votre email marketing.<br>Un vrai rythme de croissance.',
        'intro': 'Les bases avec Starter. Votre email marketing pris en main avec Growth. Une cadence renforcée avec Scale. Choisissez l’accompagnement adapté à votre boutique.',
        'recommended': 'Recommandé',
        'once': 'une seule fois', 'month': '/ mois', 'setup': 'Mise en place',
        'ongoing': 'Gestion mensuelle', 'close': 'Fermer',
        'base': 'Mission ponctuelle', 'managed': 'Mise en place + accompagnement',
        'full': 'Tout le détail de l’offre', 'flowsTitle': 'Vos flows à la mise en place',
        'setupTitle': 'Une base prête à fonctionner', 'monthlyTitle': 'Chaque mois, à vos côtés',
        'scopeTitle': 'Un périmètre clair', 'nextTitle': 'Commençons par votre boutique.',
        'nextText': 'Envoyez-moi son lien sur WhatsApp. Nous vérifierons ensemble si cette offre correspond à vos priorités.',
        'contact': 'Discuter de {name}', 'audit': 'Demander l’audit gratuit de 30 minutes',
        'common': 'Stratégie, copywriting, design et configuration inclus. Vous travaillez directement avec moi.',
        'note': 'Une boutique, une langue. Abonnement Klaviyo non inclus. Les frais de mise en place sont facturés une seule fois.',
        'existing': 'Klaviyo est déjà en place ? La reprise est chiffrée après l’audit, selon les ajustements nécessaires.',
        'setupItems': ['Configuration Klaviyo et intégration Shopify', 'Une pop-up reliée au Welcome flow', 'Segmentation adaptée à votre boutique', 'Copywriting, design, configuration et vérifications avant activation'],
        'monthlyItems': ['Calendrier marketing, segmentation, copywriting, design et programmation des campagnes', 'Suivi des performances et de la délivrabilité, avec audits réguliers du compte et des flows', 'Optimisation des flows existants selon leur efficacité et les priorités identifiées', 'A/B tests sur les objets, les contenus ou les timings, selon le volume de données disponible', 'Un bilan mensuel pour partager les résultats et les prochaines actions'],
        'scopeItems': ['Une boutique et une langue : français ou anglais', 'Deux séries de corrections regroupées par livrable', 'Mise en place : 50 % au démarrage, 50 % à la livraison', 'L’abonnement Klaviyo reste à votre charge'],
        'recurringNote': 'La mensualité commence au démarrage de la gestion des campagnes. Les nouveaux flows, les langues supplémentaires et les grosses opérations commerciales, comme Black Friday, font l’objet d’un devis distinct.',
        'starterNote': 'Cette mission ponctuelle couvre la mise en place des flows et de la pop-up. Les campagnes, le suivi, les audits récurrents et les optimisations avec A/B tests sont inclus uniquement dans Growth et Scale.',
        'cap': 'Jusqu’à {count} emails automatisés au total. Le nombre de messages de chaque flow est adapté à votre parcours client.',
        'wa': 'Bonjour Hari, l’offre {name} m’intéresse. Je souhaite en discuter avec vous. Voici le lien de ma boutique : ',
        'waAudit': 'Bonjour Hari, je souhaite un audit gratuit de 30 minutes pour savoir si l’offre {name} convient à ma boutique. Voici son lien : ',
        'plans': {
            'starter': {
                'benefit': 'Activez vos premières relances.',
                'description': 'Pour installer vos {flows} flows prioritaires, puis piloter votre email marketing en autonomie.',
                'items': ['{flows} flows essentiels · jusqu’à {emails} emails', '1 pop-up reliée au Welcome flow', 'Segmentation, copywriting et design', 'Configuration et vérifications avant activation', 'Aucune campagne incluse', 'Mission ponctuelle, sans suivi régulier'],
                'cta': 'Voir Starter',
            },
            'growth': {
                'benefit': 'Votre email marketing, pris en main.',
                'description': '{campaigns} campagnes chaque semaine et un expert à vos côtés, de la stratégie à l’optimisation des flows.',
                'items': ['{campaigns} campagnes marketing par semaine', '{flows} flows · jusqu’à {emails} emails', '1 pop-up et une segmentation adaptée', 'Suivi et audits réguliers', 'Optimisation des flows et A/B tests', 'Bilan mensuel et délivrabilité'],
                'cta': 'Découvrir Growth',
                'campaigns': '{campaigns} campagnes marketing par semaine.',
            },
            'scale': {
                'benefit': 'Accélérez votre cadence.',
                'description': 'Le suivi de Growth, avec {campaigns} campagnes par semaine, Winback et Sunset pour un parcours plus complet.',
                'items': ['{campaigns} campagnes marketing par semaine', '{flows} flows · jusqu’à {emails} emails', 'Winback, Sunset, pop-up et segmentation', 'Suivi et audits réguliers', 'Optimisation des flows et A/B tests', 'Bilan mensuel et délivrabilité'],
                'cta': 'Voir Scale',
                'campaigns': '{campaigns} campagnes marketing par semaine.',
            },
            'scale-plus': {
                'name': 'Scale renforcé', 'benefit': 'Un rythme de campagnes plus soutenu.',
                'description': 'La même base de {flows} flows et le même suivi que Scale, avec {campaigns} campagnes marketing par semaine.',
                'campaigns': '{campaigns} campagnes marketing par semaine, hors grosses opérations commerciales chiffrées séparément.',
                'cta': 'Rythme renforcé : 1 000 €/mois',
            },
        },
    },
    'en': {
        'tag': '02 / Plans & pricing',
        'title': 'Your email marketing.<br>Built for steady growth.',
        'intro': 'Build your foundation with Starter. Put your email marketing in expert hands with Growth. Increase your campaign frequency with Scale. Choose the support your store needs.',
        'recommended': 'Recommended',
        'once': 'one-time', 'month': '/ month', 'setup': 'Setup',
        'ongoing': 'Monthly management', 'close': 'Close',
        'base': 'One-time project', 'managed': 'Setup + ongoing support',
        'full': 'What’s included', 'flowsTitle': 'Your flows at setup',
        'setupTitle': 'A foundation ready to go', 'monthlyTitle': 'Ongoing support, every month',
        'scopeTitle': 'A clear scope', 'nextTitle': 'Let’s start with your store.',
        'nextText': 'Send me your store link on WhatsApp. We’ll check whether this plan fits your priorities.',
        'contact': 'Let’s talk about {name}', 'audit': 'Request a free 30-minute audit',
        'common': 'Strategy, copy, design and setup included. You work directly with me.',
        'note': 'One store, one language. Your Klaviyo subscription is separate. Setup is billed only once.',
        'existing': 'Already using Klaviyo? After the audit, I’ll quote the changes your account actually needs.',
        'setupItems': ['Klaviyo configuration and Shopify integration', 'One pop-up connected to your Welcome flow', 'Segmentation tailored to your store', 'Copy, design, setup and checks before activation'],
        'monthlyItems': ['Marketing calendar, segmentation, copy, design and campaign scheduling', 'Performance and deliverability monitoring, with regular account and flow audits', 'Ongoing improvements to existing flows, prioritized by performance', 'A/B testing of subject lines, content or timing, based on the available data', 'A monthly review of results and next steps'],
        'scopeItems': ['One store and one language: English or French', 'Two consolidated rounds of revisions per deliverable', 'Setup: 50% upfront and 50% on delivery', 'Your Klaviyo subscription is paid separately'],
        'recurringNote': 'Monthly billing starts when campaign management begins. Additional flows, extra languages and major sales events such as Black Friday are quoted separately.',
        'starterNote': 'This one-time project covers flow and pop-up setup. Campaigns, ongoing support, regular audits and optimization with A/B testing are included only in Growth and Scale.',
        'cap': 'Up to {count} automated emails in total. The number of messages in each flow is tailored to your customer journey.',
        'wa': 'Hi Hari, I’m interested in {name} and would like to discuss the plan. Here is my store link: ',
        'waAudit': 'Hi Hari, I would like a free 30-minute audit to see whether {name} is right for my store. Here is my store link: ',
        'plans': {
            'starter': {
                'benefit': 'Get your first follow-ups running.',
                'description': 'Set up your {flows} priority flows, then take the lead on your ongoing email marketing.',
                'items': ['{flows} core flows · up to {emails} emails', '1 pop-up connected to your Welcome flow', 'Segmentation, copy and design', 'Setup and checks before activation', 'No marketing campaigns included', 'One-time project, no ongoing support'],
                'cta': 'Explore Starter',
            },
            'growth': {
                'benefit': 'Your email marketing, taken care of.',
                'description': '{campaigns} campaigns every week and an expert by your side, from strategy to ongoing flow optimization.',
                'items': ['{campaigns} marketing campaigns per week', '{flows} flows · up to {emails} emails', '1 pop-up and tailored segmentation', 'Ongoing support and regular audits', 'Flow optimization and A/B testing', 'Monthly review and deliverability monitoring'],
                'cta': 'Explore Growth',
                'campaigns': '{campaigns} marketing campaigns per week.',
            },
            'scale': {
                'benefit': 'Make room for more campaigns.',
                'description': 'The same ongoing support as Growth, with {campaigns} weekly campaigns, Winback and Sunset for a broader customer journey.',
                'items': ['{campaigns} marketing campaigns per week', '{flows} flows · up to {emails} emails', 'Winback, Sunset, pop-up and segmentation', 'Ongoing support and regular audits', 'Flow optimization and A/B testing', 'Monthly review and deliverability monitoring'],
                'cta': 'Explore Scale',
                'campaigns': '{campaigns} marketing campaigns per week.',
            },
            'scale-plus': {
                'name': 'Scale Plus', 'benefit': 'A higher campaign frequency.',
                'description': 'The same {flows}-flow foundation and ongoing support as Scale, with {campaigns} marketing campaigns per week.',
                'campaigns': '{campaigns} marketing campaigns per week. Major sales events are scoped and quoted separately.',
                'cta': 'Higher frequency: €1,000/month',
            },
        },
    },
}


def money(value, lang):
    return f'{value:,}'.replace(',', '\u202f') + '\u00a0€' if lang == 'fr' else f'€{value:,}'


def bullet_list(items, css=''):
    return f'<ul class="{css}">' + ''.join(f'<li>{escape(item)}</li>' for item in items) + '</ul>'


def campaigns_faq(lang):
    growth, scale, plus = (PLANS[key]['campaigns'] for key in ('growth', 'scale', 'scale-plus'))
    if lang == 'fr':
        return f'Oui. Growth comprend {growth} campagnes par semaine, Scale {scale}, et Scale renforcé {plus}. Je prends en charge le calendrier marketing, la segmentation, le copywriting, le design et la programmation. Starter couvre uniquement la mise en place des flows et de la pop-up. Les grosses opérations commerciales, comme Black Friday, font l’objet d’un devis distinct.'
    return f'Yes. Growth includes {growth} campaigns per week, Scale {scale}, and Scale Plus {plus}. I handle the marketing calendar, segmentation, copy, design and scheduling. Starter covers flow and pop-up setup only. Major sales events such as Black Friday are quoted separately.'


def offers_section(lang, phone):
    c = COPY[lang]

    def name(key):
        return c['plans'][key].get('name', PLANS[key]['name'])

    def whatsapp(key, audit=False):
        return 'https://wa.me/' + phone + '?text=' + quote(c['waAudit' if audit else 'wa'].format(name=name(key)))

    def price(key):
        plan = PLANS[key]
        main = plan['monthly'] or plan['setup']
        unit = c['month'] if plan['monthly'] else c['once']
        setup = (f'<p class="plan-setup">{escape(c["setup"])}{":" if lang == "en" else " :"} '
                 f'<strong>{money(plan["setup"], lang)}</strong> · {escape(c["once"])}</p>') if plan['monthly'] else ''
        return f'<div class="plan-pricing"><p class="plan-price"><strong>{money(main, lang)}</strong><span>{escape(unit)}</span></p>{setup}</div>'

    cards = []
    # Growth comes first for screen readers and on mobile; desktop uses named grid areas.
    for key in ('growth', 'starter', 'scale'):
        p, copy = PLANS[key], c['plans'][key]
        featured = key == 'growth'
        badge = f'<span class="plan-badge">{escape(c["recommended"])}</span>' if featured else ''
        extra = ''
        if key == 'scale':
            extra = f'<button type="button" class="plan-upgrade" data-open-offer="offer-scale-plus" aria-haspopup="dialog">{escape(c["plans"]["scale-plus"]["cta"])}</button>'
        cards.append(f'''<article class="plan-card plan-{key}{' plan-featured' if featured else ''}" aria-labelledby="plan-{key}-title">
<div class="plan-label"><span>{escape(c['base'] if key == 'starter' else c['managed'])}</span>{badge}</div>
<h3 id="plan-{key}-title">{escape(name(key))}</h3>
<p class="plan-benefit">{escape(copy['benefit'])}</p>
<p class="plan-description">{escape(copy['description'].format(**p))}</p>
{price(key)}{bullet_list([item.format(**p) for item in copy['items']], 'plan-features')}
<div class="plan-actions"><button type="button" class="plan-button{' plan-button-primary' if featured else ''}" data-open-offer="offer-{key}" aria-haspopup="dialog">{escape(copy['cta'])}</button>{extra}</div>
</article>''')

    dialogs = []
    for key, plan in PLANS.items():
        copy = c['plans'][key]
        flows = bullet_list(FLOWS[:plan['flows']], 'plan-flow-list')
        monthly = ''
        if plan['monthly']:
            monthly = f'<section class="plan-detail-section"><h3>{escape(c["monthlyTitle"])}</h3><p class="plan-campaign-cadence">{escape(copy["campaigns"].format(**plan))}</p>{bullet_list(c["monthlyItems"])}</section>'
        extra_note = c['recurringNote'] if plan['monthly'] else c['starterNote']
        dialogs.append(f'''<dialog id="offer-{key}" class="offer-dialog" aria-labelledby="offer-{key}-title" aria-describedby="offer-{key}-intro">
<div class="offer-dialog-header"><span>{escape(c['full'])}</span><button class="offer-dialog-close" type="button" data-close-offer autofocus>{escape(c['close'])} <span aria-hidden="true">×</span></button></div>
<div class="offer-dialog-body"><div class="plan-detail-intro"><p class="plan-detail-kicker">{escape(c['base'] if key == 'starter' else c['managed'])}</p><h2 id="offer-{key}-title">{escape(name(key))}</h2><p id="offer-{key}-intro">{escape(copy['description'].format(**plan))}</p>{price(key)}</div>
<section class="plan-detail-section"><h3>{escape(c['flowsTitle'])}</h3>{flows}<p>{escape(c['cap'].format(count=plan['emails']))}</p></section>
<section class="plan-detail-section"><h3>{escape(c['setupTitle'])}</h3>{bullet_list(c['setupItems'])}</section>
{monthly}
<section class="plan-detail-section"><h3>{escape(c['scopeTitle'])}</h3>{bullet_list(c['scopeItems'])}<p>{escape(extra_note)}</p></section>
<div class="plan-next"><h3>{escape(c['nextTitle'])}</h3><p>{escape(c['nextText'])}</p><a class="plan-button plan-button-primary" href="{escape(whatsapp(key), quote=True)}" target="_blank" rel="noopener noreferrer">{escape(c['contact'].format(name=name(key)))}</a><a class="plan-audit-link" href="{escape(whatsapp(key, True), quote=True)}" target="_blank" rel="noopener noreferrer">{escape(c['audit'])}</a></div>
</div></dialog>''')

    return f'''<section class="offers offers-v2 section" id="offers"><div class="wrap">
<div class="section-head"><div><p class="eyebrow">{escape(c['tag'])}</p><h2>{c['title']}</h2></div><p>{escape(c['intro'])}</p></div>
<p class="plans-common">{escape(c['common'])}</p>
<div class="plans-grid">{''.join(cards)}</div>
<div class="plans-notes"><p>{escape(c['note'])}</p><p>{escape(c['existing'])}</p></div>
</div>{''.join(dialogs)}</section>'''
