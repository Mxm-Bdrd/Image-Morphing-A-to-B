import numpy as np
import matplotlib.pyplot as plt
import matplotlib.path as mpath
from scipy.spatial import Delaunay
from scipy.interpolate import RectBivariateSpline
import os


# 1. Définir les correspondances
def charger_points(chemin_img, chemin_txt):
    img = plt.imread(chemin_img)
    h, l = img.shape[:2] # hauteur et largeur
    pts = np.loadtxt(chemin_txt) # les points
    coins = np.array([[0, 0], [l - 1, 0], [0, h - 1], [l - 1, h - 1]]) # les coins
    pts_complets = np.vstack((pts, coins)) # matrice complète
    return img, pts_complets



# 2. Calculer une triangulation
def calculer_triangulation(pts1, pts2):
    pts_moyens = (pts1 + pts2) / 2.0
    triangles = Delaunay(pts_moyens)
    return triangles



# 3. Créer la métamorphose
def calculer_matrice_affine(tri_depart, tri_arrivee):
    X = np.vstack((tri_depart.T, [1, 1, 1])) # une ligne de 1 pour coordonnées homogènes
    U = np.vstack((tri_arrivee.T, [1, 1, 1])) # une ligne de 1 pour coordonnées homogènes
    A = U @ np.linalg.inv(X)
    return A # la matrice affine

def morph(img1, img2, img1_pts, img2_pts, tri, warp_frac, dissolve_frac):
    h, w, canaux = img1.shape
    morphed_img = np.zeros((h, w, canaux), dtype=np.float64) # résultats
    inter_pts = (1 - warp_frac) * img1_pts + warp_frac * img2_pts # points moyens

    splines1 = [RectBivariateSpline(np.arange(h), np.arange(w), img1[:, :, c]) for c in range(canaux)] # interpolation des couleurs
    splines2 = [RectBivariateSpline(np.arange(h), np.arange(w), img2[:, :, c]) for c in range(canaux)]

    X_grid, Y_grid = np.meshgrid(np.arange(w), np.arange(h)) # coordonnées
    coords_pixels = np.vstack((X_grid.flatten(), Y_grid.flatten())).T

    for simplex in tri.simplices: # boucle pour chaque triangle
        t_inter = inter_pts[simplex]
        t_img1 = img1_pts[simplex]
        t_img2 = img2_pts[simplex]
        A1 = calculer_matrice_affine(t_inter, t_img1)
        A2 = calculer_matrice_affine(t_inter, t_img2)
        chemin = mpath.Path(t_inter)
        masque = chemin.contains_points(coords_pixels)
        if not np.any(masque):
            continue

        pts_dans_triangle = coords_pixels[masque] # pour coord. homogènes
        pts_homogenes = np.vstack((pts_dans_triangle.T, np.ones(pts_dans_triangle.shape[0])))

        src_pts1 = A1 @ pts_homogenes # transfo inverse
        src_pts2 = A2 @ pts_homogenes

        x1, y1 = src_pts1[0, :], src_pts1[1, :]
        x2, y2 = src_pts2[0, :], src_pts2[1, :]

        for c in range(canaux): # interpolation couleurs
            val1 = splines1[c].ev(y1, x1)
            val2 = splines2[c].ev(y2, x2)
            val_fondue = (1 - dissolve_frac) * val1 + dissolve_frac * val2
            morphed_img[pts_dans_triangle[:, 1], pts_dans_triangle[:, 0], c] = val_fondue

    return np.clip(morphed_img, 0, 255).astype(np.uint8) # verif valide



# Sauvegarde vidéo
def generer_sequence(img1_path, pts1_path, img2_path, pts2_path, dossier_sortie):
    if not os.path.exists(dossier_sortie): # creer dossier
        os.makedirs(dossier_sortie)

    img1, img1_pts = charger_points(img1_path, pts1_path) # Chargement données
    img2, img2_pts = charger_points(img2_path, pts2_path)

    if img1.max() <= 1.0: img1 = (img1 * 255).astype(np.uint8) # normalisation
    if img2.max() <= 1.0: img2 = (img2 * 255).astype(np.uint8)

    tri = calculer_triangulation(img1_pts, img2_pts) # triangulation de Delaunay
    nb_frames = 100

    print("Generating frames...")
    for i in range(nb_frames):
        frac = i / (nb_frames - 1)

        warp_frac = frac
        dissolve_frac = frac

        frame = morph(img1, img2, img1_pts, img2_pts, tri, warp_frac, dissolve_frac)
        nom_fichier = os.path.join(dossier_sortie, f"file_{i:05d}.png")
        plt.imsave(nom_fichier, frame)
        print(f"Frame {i + 1}/{nb_frames} saved.")

# lancer script
generer_sequence("Portugal_maPhoto1.png", "Portugal_maPhoto1.txt", "Portugal_maPhoto2.png", "Portugal_maPhoto2.txt", "video_25fps_4")