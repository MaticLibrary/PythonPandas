import pandas as pd
import numpy as np
import os

r = ["S", "M", "L", "XL"]
t = ["MTB", "BMX", "DH", "CX"]
c = [1500, 3000, 5500, 8000, 14000]

rozmiary = np.random.choice(r, size = 100, replace = True)
typy = np.random.choice(t, size = 100, replace = True)
ceny = np.random.choice(c, size = 100, replace = True, p = [0.5, 0.3, 0.1, 0.08, 0.02])

rowery = pd.DataFrame(data = {
    "rozmiar": rozmiary,
    "typ": typy,
    "cena": ceny
    })


# Przykład 1
for cena in rowery["cena"].unique():
  print(os.linesep, "Cena =", cena)
  print(pd.crosstab(rowery[rowery["cena"] == cena].typ, rowery[rowery["cena"] == cena].rozmiar))

# Przykład 2
for cena in rowery.cena.unique():
  print(os.linesep, "Cena =", cena)
  print(pd.crosstab(rowery[rowery.cena == cena].typ, rowery[rowery.cena == cena].rozmiar))

# Przykład 3
for cena in pd.unique(rowery.cena):
  print(os.linesep, "Cena =", cena)
  print(pd.crosstab(rowery.loc[rowery.cena == cena].typ, rowery.loc[rowery.cena == cena].rozmiar))

# Przykład 4
for cena in rowery.drop_duplicates(subset = "cena").cena:
  print(os.linesep, "Cena =", cena)
  print(pd.crosstab(rowery.query("cena == @cena").typ, rowery.query("cena == @cena").rozmiar))

# I Oblicz łączną liczbę rowerów w poszczególnych rozmiarach, cenach oraz typach
print(
    pd.crosstab(
        [rowery["cena"], rowery["typ"]],
        rowery["rozmiar"]
    )
)


# II Oblicz łączną liczbę rowerów w poszczególnych rozmiarach, cenach oraz typach
print(os.linesep)
print(rowery.groupby(["rozmiar"]).count())

print(os.linesep)
print(rowery.groupby(["cena"]).count())

print(os.linesep)
print(rowery.groupby(["typ"]).count())
