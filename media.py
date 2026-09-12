"""Bilingual marketing email gallery."""
from html import escape as e

COPY = {'fr': {'designTitle': 'Des emails<br>qui <span class="lime">donnent envie.</span>',
        'designIntro': 'Du premier regard au clic : des messages clairs, des produits mis en valeur et un '
                       'univers fidèle à la marque.',
        'designs': [('Couleur & produit',
                     'Une sélection de compositions colorées et de mises en avant produit.',
                     'design-cpg.jpeg',
                     1472),
                    ('Temps forts & campagnes',
                     'Des compositions contrastées pour les promotions et les campagnes saisonnières.',
                     'design-campaigns.jpeg',
                     1173),
                    ('Marque & lifestyle',
                     'Des univers mode, beauté, maison et lifestyle.',
                     'design-lifestyle.jpeg',
                     1472)],
        'designTag': '04 / Designs d’emails',
        'reference': 'Modèle d’email marketing',
        'enlarge': 'Agrandir le visuel'},
 'en': {'designTitle': 'Emails that<br><span class="lime">make an impression.</span>',
        'designIntro': 'From the first glance to the click: clear messaging, products in the spotlight and a '
                       'look that stays true to the brand.',
        'designs': [('Colour & product',
                     'A selection of colourful compositions and product presentations.',
                     'design-cpg.jpeg',
                     1472),
                    ('Key moments & campaigns',
                     'High-contrast compositions for promotions and seasonal campaigns.',
                     'design-campaigns.jpeg',
                     1173),
                    ('Brand & lifestyle',
                     'Fashion, beauty, home and lifestyle designs.',
                     'design-lifestyle.jpeg',
                     1472)],
        'designTag': '04 / Email designs',
        'reference': 'Marketing email design',
        'enlarge': 'Enlarge the image'}}

def media_sections(lang):
 c=COPY[lang]
 templates=[]
 def viewer(asset,title,caption,label,key,width,height,kind='wide'):
  templates.append(f'<template id="media-{key}"><h3>{e(title)}</h3><p>{e(caption)}</p></template>')
  return f'<button class="media-image" data-proof="/assets/{asset}" data-transcript="#media-{key}" data-modal-label="{e(label,quote=True)}" data-view="{kind}" aria-label="{e(c["enlarge"]+" — "+title,quote=True)}"><img src="/assets/{asset}" alt="{e(label+" — "+title,quote=True)}" width="{width}" height="{height}" loading="lazy"><span class="media-zoom">{e(c["enlarge"])} <span aria-hidden="true">↗</span></span></button>'
 designs=''
 for i,(title,text,asset,height) in enumerate(c['designs']):
  view=viewer(asset,title,text,c['reference'],'design-'+str(i),736,height,'design')
  designs+=f'<figure class="design-card reveal">{view}<figcaption><span>{c["reference"]}</span><h3>{e(title)}</h3><p>{e(text)}</p></figcaption></figure>'
 gallery=f'''<section class="designs section wrap" id="designs"><div class="section-head reveal"><div><p class="eyebrow lime">{c['designTag']}</p><h2>{c['designTitle']}</h2></div><p>{c['designIntro']}</p></div><div class="design-grid">{designs}</div></section>'''
 return gallery,''.join(templates)
