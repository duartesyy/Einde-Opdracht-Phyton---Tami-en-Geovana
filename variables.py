product1 = "brood"
product2 = "tee"
product3 = "chips"
prijsbrood = 2.00
prijstee = 2.30
prijschips = 3.00
aantalverkochtbrood = 50
aantalverkochttee = 30
aantalverkochtchips = 45
geldverdiend = (aantalverkochtbrood * prijsbrood) + (aantalverkochttee * prijstee) + (aantalverkochtchips * prijschips)

print(f"Product:{product1}, Prijs:{prijsbrood}, Aantal:{aantalverkochtbrood}")
print(f"Product:{product2}, Prijs:{prijstee}, Aantal:{aantalverkochttee}")
print(f"Product:{product3}, Prijs:{prijschips}, Aantal:{aantalverkochtchips}")
print(f"Totale omzet: {geldverdiend}")