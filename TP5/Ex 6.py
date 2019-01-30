from matplotlib import pyplot

abscisses = [0, 1, 2, 3, 4, 5]
ordonnees = [0, 1, 4, 9, 16, 25]

pyplot.plot(abscisses, ordonnees, 'b-', color="red", linewidth=3, linestyle="dashed")
pyplot.show()

paniers = [0, 1, 2, 3, 4]
effectifs = [12, 37, 24, 9, 3]

pyplot.bar(paniers, effectifs, color="purple", width=0.5)
pyplot.xticks(paniers, ["Insuffisant", "Passable", "Assez bien", "Bien", "Très bien"])
pyplot.show()
