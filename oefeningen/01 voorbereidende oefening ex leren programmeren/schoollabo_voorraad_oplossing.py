# schoollabo_voorraad_oplossing.py
VOORRAAD = {
    "pipetten": 100,
    "handschoenen": 200,
    "reagentia": 50,
    "bekerglazen": 75,
    "testbuizen": 150,
    "overig": 0
}

VERBRUIK = [
    ("10", "pipetten"),
    ("30", "handschoenen"),
    ("5", "reagentia"),
    ("7", "bekers"),
    ("abc", "pipetten"),
    ("25", "Testbuizen"),
    ("300", "handschoenen"),
    ("2", "pipet")
]

# verbruik verwerken
for aantal_str, cat in VERBRUIK:
    cat = cat.lower().strip()
    try:
        aantal = int(aantal_str)
    except ValueError:
        print(f"Ongeldig aantal '{aantal_str}', transactie wordt overgeslagen.")
        continue

    if cat not in VOORRAAD:
        print(f"Onbekende categorie '{cat}', wordt toegevoegd aan 'overig'.")
        cat = "overig"

    beschikbaar = VOORRAAD[cat]
    if aantal > beschikbaar:
        print(f"Niet genoeg voorraad van {cat} (probeerde {aantal} te gebruiken, nog {beschikbaar} beschikbaar).")
        VOORRAAD[cat] = 0
    else:
        VOORRAAD[cat] = beschikbaar - aantal

# extra input
while True:
    aantal_str = input("Aantal (of 'stop'): ").strip()
    if aantal_str.lower() == "stop":
        break
    try:
        aantal = int(aantal_str)
    except ValueError:
        print("Ongeldig aantal, probeer opnieuw.")
        continue

    cat = input("Categorie: ").lower().strip()
    if cat not in VOORRAAD:
        print(f"Onbekende categorie '{cat}', wordt toegevoegd aan 'overig'.")
        cat = "overig"

    beschikbaar = VOORRAAD[cat]
    if aantal > beschikbaar:
        print(f"Niet genoeg voorraad van {cat} (probeerde {aantal} te gebruiken, nog {beschikbaar} beschikbaar).")
        VOORRAAD[cat] = 0
    else:
        VOORRAAD[cat] = beschikbaar - aantal

print("\nOverzicht voorraad:\n")
totaal = 0
for cat in ["pipetten", "handschoenen", "reagentia", "bekerglazen", "testbuizen", "overig"]:
    rest = VOORRAAD[cat]
    print(f"{cat:15} nog {rest:4d} stuks")
    # {cat:15} : Als het woord korter is dan 15 tekens, worden spaties toegevoegd achteraan om alles netjes uit te lijnen.
    # {rest:4d} : rest is een geheel getal (het aantal stuks dat nog overblijft).
    # De :4d betekent: 4 → gebruik minstens 4 posities
                     # d → formatteer als integer (decimal)
                     # Zo zorgt Python ervoor dat getallen ook netjes rechts uitgelijnd staan.
    totaal += rest
print("-" * 28)
print(f"totaal resterend: {totaal}")
