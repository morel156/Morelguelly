import matplotlib.pyplot as plt
import numpy as np

def dessiner_cercle():
    try:
        
        rayon = float(input("Entrez le rayon du cercle : "))
        if rayon <= 0:
            print("Le rayon doit être un nombre positif.")
            return
        
        
        theta = np.linspace(0, 2 * np.pi, 500)
        x = rayon * np.cos(theta)
        y = rayon * np.sin(theta)
        
        
        plt.figure(figsize=(6, 6))
        plt.plot(x, y, label=f"Cercle de rayon {rayon}")
        plt.gca().set_aspect('equal', adjustable='box')
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.title("Représentation d'un cercle")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend()
        plt.grid(True)
        plt.show()
    except ValueError:
        print("Veuillez entrer un nombre valide pour le rayon.")


dessiner_cercle()
