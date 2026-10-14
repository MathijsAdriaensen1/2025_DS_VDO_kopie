# budgetplanner_start.py

# 1. Vaste categorieën - deze mogen NIET veranderd worden door de gebruiker
VASTE_CATEGORIEEN = ["voeding", "vervoer", "wonen", "ontspanning", "gezondheid", "overig"]

# 2. Maak hier een dictionary met alle categorieën op 0.0
budget = {}
for cat in VASTE_CATEGORIEEN:
    budget[cat] = 0.0

# 3. Voorbeeldtransacties die sowieso moeten verwerkt worden
voorbeeld_transacties = [
    ("23.50", "voeding"),
    ("15", "VERVOER"),
    ("49.99", "wonen"),
    ("12.0", "sport"),        # bestaat niet -> moet naar 'overig'
    ("abc", "voeding"),       # bedrag ongeldig -> negeren
    ("8.75", "Ontspanning"),
    ("19.90", "gezondheid"),
    ("5", "koffie")           # bestaat niet -> naar 'overig'
]

# TODO 1: verwerk eerst de voorbeeldtransacties

# TODO 2: laat gebruiker extra uitgaven ingeven

# TODO 3: toon overzicht

