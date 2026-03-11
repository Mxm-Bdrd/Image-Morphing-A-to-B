#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime


# =============================================================================
# CSS Styles
# =============================================================================

def obtenir_css(accent_color="#4fc3f7"):
    return f"""
        @import url('https://fonts.googleapis.com/css2?family=Source+Sans+Pro:wght@400;600;700&family=Fira+Code:wght@400;500&display=swap');
        * {{ box-sizing: border-box; }}
        body {{
            font-family: 'Source Sans Pro', -apple-system, BlinkMacSystemFont, sans-serif;
            margin: 0; padding: 0;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
            min-height: 100vh; color: #e8e8e8;
        }}
        .container {{ max-width: 1400px; margin: 0 auto; padding: 30px 20px; }}
        header {{ text-align: center; padding: 40px 0; border-bottom: 2px solid rgba(255,255,255,0.1); margin-bottom: 40px; }}
        h1 {{ font-size: 2.5em; font-weight: 700; color: #fff; margin: 0 0 15px 0; text-shadow: 0 2px 10px rgba(0,0,0,0.3); }}
        .subtitle {{ font-size: 1.2em; color: #a0a0a0; margin: 0; line-height: 1.5; }}
        .date-badge {{ display: inline-block; background: rgba(255,255,255,0.1); padding: 8px 20px; border-radius: 20px; margin-top: 20px; font-size: 0.9em; color: #b0b0b0; }}
        .image-section {{ background: rgba(255,255,255,0.05); backdrop-filter: blur(10px); border-radius: 16px; padding: 30px; margin-bottom: 40px; border: 1px solid rgba(255,255,255,0.1); box-shadow: 0 8px 32px rgba(0,0,0,0.2); }}
        .image-section h2 {{ color: {accent_color}; font-size: 1.6em; margin: 0 0 25px 0; padding-bottom: 15px; border-bottom: 2px solid {accent_color}40; }}
        h3 {{ color: #e0e1dd; font-size: 1.3em; margin: 30px 0 20px 0; }}
        h3::before {{ content: ''; display: inline-block; width: 4px; height: 24px; background: {accent_color}; margin-right: 12px; border-radius: 2px; vertical-align: middle; }}
        .algorithm-box {{ background: rgba(0,0,0,0.3); padding: 20px; border-radius: 8px; margin: 15px 0; border-left: 4px solid {accent_color}; }}
        .algorithm-box h4 {{ color: {accent_color}; margin: 0 0 10px 0; }}
        .algorithm-box p {{ margin: 5px 0; line-height: 1.6; }}

        .figure-container, .video-container {{ display: flex; flex-direction: column; align-items: center; justify-content: center; margin: 20px 0; padding: 15px; background: rgba(0,0,0,0.2); border-radius: 12px; }}
        .figure-container img, .video-container video {{ max-width: 80%; max-height: 500px; border-radius: 8px; box-shadow: 0 4px 20px rgba(0,0,0,0.3); outline: none; }}
        .figure-container img {{ cursor: zoom-in; transition: transform 0.2s; }}
        .figure-container img:hover {{ transform: scale(1.02); }}
        .figure-caption {{ margin-top: 10px; font-style: italic; color: #a0a0a0; font-size: 1em; text-align: center; }}

        .image-grid {{ display: flex; flex-wrap: wrap; justify-content: center; gap: 20px; margin: 30px 0; }}
        .image-grid-item {{ position: relative; border-radius: 12px; overflow: hidden; background: rgba(0,0,0,0.3); cursor: zoom-in; transition: transform 0.2s; flex: 0 1 400px; max-width: 100%; }}
        .image-grid-item:hover {{ transform: translateY(-5px); box-shadow: 0 8px 25px rgba(0,0,0,0.5); }}
        .image-grid-item img {{ width: 100%; height: auto; display: block; }}
        .image-grid-item .image-label {{ position: absolute; bottom: 0; left: 0; right: 0; background: linear-gradient(to top, rgba(0,0,0,0.8), transparent); color: #fff; padding: 15px 10px 10px; font-size: 0.9em; text-align: center; }}

        .lightbox {{ display: none; position: fixed; z-index: 9999; left: 0; top: 0; width: 100%; height: 100%; background-color: rgba(0,0,0,0.9); animation: fadeIn 0.3s; overflow: auto; }}
        .lightbox.active {{ display: flex; align-items: center; justify-content: center; }}
        .lightbox-content {{ margin: auto; padding: 20px; display: flex; align-items: center; justify-content: center; }}

        .lightbox-content img {{ 
            max-width: 95vw; 
            max-height: 95vh; 
            object-fit: contain; 
            border-radius: 8px; 
            box-shadow: 0 0 30px rgba(0,0,0,0.8); 
            transition: transform 0.3s ease; 
            transform: scale(1.2); 
            cursor: zoom-out; 
        }}

        .lightbox-content img.fit-screen {{ transform: scale(1); cursor: zoom-in; }}

        .lightbox-close {{ position: fixed; top: 20px; right: 40px; color: #fff; font-size: 40px; font-weight: bold; cursor: pointer; z-index: 10000; }}
        .lightbox-close:hover {{ color: {accent_color}; }}

        @keyframes fadeIn {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}
        footer {{ text-align: center; padding: 30px; color: #666; font-size: 0.9em; }}
    """


# =============================================================================
# Composants HTML
# =============================================================================

def document_html(titre, sous_titre, icone, contenu, accent_color="#4fc3f7"):
    date_str = datetime.now().strftime("%d %B %Y à %H:%M")
    css = obtenir_css(accent_color)
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{titre}</title>
    <style>{css}</style>
</head>
<body>
    <div id="lightbox" class="lightbox" onclick="closeLightbox(event)">
        <span class="lightbox-close">&times;</span>
        <div class="lightbox-content">
            <img id="lightbox-img" src="" alt="">
        </div>
    </div>

    <div class="container">
        <header>
            <h1>{icone} {titre}</h1>
            <p class="subtitle">{sous_titre}</p>
            <div class="date-badge">Généré le {date_str}</div>
        </header>

        {contenu}

        <footer></footer>
    </div>

    <script>
        function openLightbox(img) {{
            const lbImg = document.getElementById('lightbox-img');
            lbImg.src = img.src;
            lbImg.className = ''; 
            document.getElementById('lightbox').classList.add('active');
            document.body.style.overflow = 'hidden';
        }}

        function closeLightbox(event) {{
            const lightbox = document.getElementById('lightbox');
            if (event.target === lightbox || event.target.classList.contains('lightbox-close') || event.target.classList.contains('lightbox-content')) {{
                lightbox.classList.remove('active');
                document.body.style.overflow = 'auto';
            }}
        }}

        document.getElementById('lightbox-img').addEventListener('click', function(e) {{
            this.classList.toggle('fit-screen'); 
            e.stopPropagation(); 
        }});

        document.addEventListener('keydown', e => {{ 
            if (e.key === 'Escape') {{
                document.getElementById('lightbox').classList.remove('active');
                document.body.style.overflow = 'auto';
            }}
        }});
    </script>
</body>
</html>
"""


def section(titre, contenu, icone="📷"):
    return f'<div class="image-section"><h2><span class="icon">{icone}</span> {titre}</h2>{contenu}</div>'


def figure(chemin_img, legende="", alt=""):
    alt = alt or legende
    html_legende = f'<p class="figure-caption">{legende}</p>' if legende else ""
    return f'<div class="figure-container"><img src="{chemin_img}" alt="{alt}" onclick="openLightbox(this)">{html_legende}</div>'


def video_element(chemin_video, legende=""):
    """Nouveau composant pour intégrer facilement les vidéos mp4 générées par ffmpeg."""
    html_legende = f'<p class="figure-caption">{legende}</p>' if legende else ""
    # L'attribut 'controls' affiche le bouton play/pause, 'loop' fait rejouer la vidéo en boucle
    return f"""
    <div class="video-container">
        <video controls loop muted>
            <source src="{chemin_video}" type="video/mp4">
            Votre navigateur ne supporte pas la balise vidéo.
        </video>
        {html_legende}
    </div>
    """


def grille_images(images, titre=""):
    items = ""
    for img in images:
        items += f'<div class="image-grid-item" onclick="openLightbox(this.querySelector(\'img\'))"><img src="{img["src"]}" alt="{img["label"]}"><div class="image-label">{img["label"]}</div></div>'
    html_titre = f'<h3>{titre}</h3>' if titre else ""
    return f'{html_titre}<div class="image-grid">{items}</div>'


def boite_texte(titre, description):
    return f'<div class="algorithm-box"><h4>{titre}</h4><p>{description}</p></div>'


# =============================================================================
# Génération
# =============================================================================

def generer_rapport():
    contenu = ""

    # SECTION 1
    contenu_sec1 = boite_texte("Description de l'algorithme",
                               "Pour la métamorphose, la première étape de l'algorithme est de calculer une forme moyenne entre les deux visages avec une triangulation de Delaunay. Ensuite, pour chaque frame de la vidéo, une transformation affine (avec la matrice) inverse est appliquée sur chaque triangle pour trouver la position correspondante dans les images sources. Finalement, les couleurs sont interpolées pour créer le fondu selon la fraction de t (équation M = (1-t)P + tQ). Les photos servant à prduire les vidéos sont dans le dossier de remise tp3/web/images et non dans le rapport par redondance (les videos sont plus intéressantes).")

    contenu_sec1 += video_element("video1.mp4",
                                  "Métamorphose du visage d'Edwin vers le mien (100 images, 25 fps)")

    contenu_sec1 += boite_texte("Discussion du résultat",
                                "D'abord, je remarque que le résultat est globalement fluide. Les points ont bien été pris par moi et par Edwin faisant que les proportions se conserve très bien. Je remarque cependant qu'il y a une légère différence d'angle (ma faute. ma caméra de cellulaire est un peu trop haute) causant l'apparition soudaine de mon colet au fondu en couleur. Ensuite, malgré les points et leur correspondances bien placées, les différences physiques (mes cheveux et lunettes entre autres) peuvent apparaitre subitement lors du fondu. Pour y remédier, je vais modifier le fondu des prochaines vidéos (il est à noter que mes paramètres warp_frac et dissolve_frac sont égaux et linéaire). Les ressemblance physique, cependant, s'agence très bien et donne un ton réaliste à la transformation (nos moustaches).")

    contenu += section("Métamorphose de visages", contenu_sec1, icone="👤")

    # SECTION 2
    contenu_sec2 = ""

    contenu_sec2 += video_element("video2.mp4", "Métamorphose entre une objet imprimé 3D et sa modèle.")

    contenu_sec2 += boite_texte("Discussion",
                                "Pour la métamorphose d'objet ou d'animal, j'ai décider de métamorphoser un objet en animal. J'ai imprimé un modèle 3D de Ahsoka puis j'ai pris en photo les 2 têtes à un angle et luminosité similaire. Les paramètres pour l'algorithme sont (warp_frac = frac) et (dissolve_frac = 1 - frac) pour tester des combinaisons. Il est important de commencer par la modèle plastique pour avoir l'effet des 'poils qui poussent'. Il est à noter que faire tenir un chien à un angle précis pour prendre une photo n'est pas une tâche facile!")

    contenu += section("Métamorphose d'objets", contenu_sec2, icone="🍎")

    # SECTION 3
    contenu_sec3 = ""

    # Vidéo personnelle 1
    contenu_sec3 += video_element("video3.mp4", "Animation personnelle : Changement d'expression.")
    contenu_sec3 += boite_texte("Discussion",
                                "Pour ma première video personnelle, je voulais essayer un changement d'expression faciale. J'ai isoler mon visage sur deux photos (pris avec le même fond d'écran) et établi les points de correspondances selon l'expression. En d'autres mots, la plupart des points sont semblables en position mais les points qui changent selon l'expression (yeux, coins de bouche) difffèrent et vont donc donner un effet de déplacement. J'ai tweak mes paramètres warp_frac et dissolve_frac à (warp_frac = frac**0.5) et (dissolve_frac = frac**2) pour que le changement d'expression se produise rapidement (fonction racine carrée), mais que le fondu se produise initialement lentement puis rapidement à la fin (fonction quadratique). J'aime le résultat du changement d'expression, mais je trouve le changement de couleur trop brusque (surtout au niveau des dents/yeux). Je continuerai de modifier les paramètres pour trouver un sweet spot.")

    # Vidéo personnelle 2
    contenu_sec3 += video_element("video4_boomerang.mp4", "Animation personnelle 2 : Swap de personne + effet boomerang.")
    contenu_sec3 += boite_texte("Discussion",
                                "Pour ma dernière vidéo, je voulais faire un swap de personne dans un décors complexe mais similaire. Malheureusement, on comprend vite que l'angle dans un décors complexe est très important pour ne pas avoir simplement une genre de translation/ghosting du même objet (l'arche dorée en particulier...). La position de l'individu ne doit pas trop changer non plus. Dans mon cas, le déplacement des silhouettes ce fait assez bien de moi à ma copine. En lisant plus sur FFMPEG, j'ai trouver qu'on peut aussi générer une video boomerang de la métamorphose puis de la métamorphose inverse (simplement la video qui joue à l'envers).")

    contenu += section("Métamorphoses de photos personnelles", contenu_sec3, icone="📸")

    # FINALISATION
    sous_titre = "Photographie algorithmique<br> Maxime Bédard"
    html_final = document_html("<strong>Algorithme de métamorphose</strong> 🎬", sous_titre, "🎬", contenu)

    nom_fichier = "index.html"
    with open(nom_fichier, "w", encoding="utf-8") as f:
        f.write(html_final)
    print(f"Rapport généré")


if __name__ == '__main__':
    generer_rapport()