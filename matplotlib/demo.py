import matplotlib.pyplot as plt 
import numpy as np

x = np.arange(0,11)
y = 3*x
plt.figure(facecolor="beige")
plt.axes(facecolor="lightcyan")
plt.bar(x,y, color="darkblue")
print(x)
print(y)

plt.plot(x,y, label="grapique", color="#009933")
plt.xlabel("Titres des abscisses", color="#ff3300")
plt.ylabel("Titre des ordonnées", color="#99ffcc")
#début et fin des axes
plt.xlim(left=3)
plt.ylim(bottom=2)
plt.xlim(left=0)
plt.title("Titre", color="#660066")
plt.legend(loc=4)



plt.grid(color="yellow")
plt.xticks(color="forestgreen")
plt.yticks(color="red")
plt.savefig("./matplotlib/beau-graphique.jpg")

plt.show()