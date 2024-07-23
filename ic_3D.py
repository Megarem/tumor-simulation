import numpy as np
import csv

def generate_points(alpha, beta, num_points):
    points = []
    while len(points) < num_points:
        x = np.random.uniform(-alpha, alpha)
        y = np.random.uniform(-alpha, alpha)
        z = np.random.uniform(-alpha, alpha)
        
        if x**2 + y**2 + z**2 <= (alpha - beta)**2:
            points.append((x, y, z))
    
    return np.array(points)

# Paramètres
alpha = 70.0  # Rayon de la grande boule
beta = 8.4    # Rayon des petits points
num_points = 300  # Nombre de points à générer

# Générer les points
points = generate_points(alpha, beta, num_points)

# Créer le fichier CSV
with open('./config/points.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    
    # Écrire l'en-tête
    csvwriter.writerow(['x', 'y', 'z', 'type', 'volume', 'cycle entry', 'custom:GFP', 'custom:sample'])
    
    # Écrire les données pour chaque point
    for point in points:
        x, y, z = point
        row = [
            f"{x:.6f}",
            f"{y:.6f}",
            f"{z:.6f}",
            'cancer',
            '',  # volume (laissé vide)
            '',  # cycle entry (laissé vide)
            '',  # custom:GFP (laissé vide)
            ''   # custom:sample (laissé vide)
        ]
        csvwriter.writerow(row)

print(f"Fichier CSV 'points.csv' généré avec {num_points} points.")