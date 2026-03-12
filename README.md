# Algorithme de Métamorphose (Image Morphing)

Ce dépôt contient l'implémentation complète d'un algorithme de métamorphose (morphing) d'images. L'objectif de ce projet est de créer une transition fluide et naturelle entre une image A et une image B sous forme de séquence vidéo.

## Méthodologie

L'algorithme repose sur une combinaison de géométrie algorithmique et d'algèbre linéaire, et se divise en trois étapes principales :

1. **Correspondances et Triangulation :**
   - Définition manuelle de points de repère sur les deux images pour lier les caractéristiques physiques.
   - Calcul de la forme moyenne géométrique.
   - Génération d'un maillage via la **triangulation de Delaunay** (`scipy.spatial.Delaunay`) pour éviter le chevauchement des triangles lors de la déformation.

2. **Transformation Affine (Warping) :**
   - Calcul des transformations affines de manière analytique (résolution de systèmes d'équations linéaires, sans utiliser de fonctions de transformation pré-bâties).
   - Utilisation de la transformation inverse (de l'image de destination vers la source) pour garantir qu'aucun pixel ne soit laissé vide.

3. **Interpolation et Fondu (Dissolve) :**
   - Évaluation des couleurs aux coordonnées sous-pixeliques grâce à l'interpolation bilinéaire (`scipy.interpolate.RectBivariateSpline`).
   - Fondu croisé progressif (dissolve) des couleurs en fonction de la trame temporelle.

## Prérequis

Pour exécuter ce projet, vous devez avoir Python installé avec les librairies suivantes :
- `numpy`
- `scipy`
- `matplotlib`

De plus, **FFmpeg** doit être installé sur votre système et ajouté à vos variables d'environnement (`PATH`) pour la compilation des vidéos.

## Utilisation

### 1. Sélection des points de repère
Utilisez le script interactif fourni pour définir les correspondances entre les deux images. Cliquez sur les mêmes caractéristiques physiques dans le même ordre pour les deux images. N'oubliez pas de cliquer sur les bordures/coins pour stabiliser l'arrière-plan !

```bash
python selectpoints.py imageA.jpg pointsA.txt
python selectpoints.py imageB.jpg pointsB.txt
