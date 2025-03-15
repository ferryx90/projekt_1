# """
# projekt_1.py: první projekt do Engeto Online Python Akademie
# author: Tomáš Ferko
# email: t.ferry@seznam.cz
# """
texts = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]
registered_users = {
    "bob": "123", 
    "ann": "pas123", 
    "mike": "pasword", 
    "liz": "pas123"
}
user = input("Zadej své jméno: ")
if user not in registered_users:
    print("Uživatel není registrován. Program se ukonci.")
    quit()
password = input("Zadej své heslo: ")
if registered_users.get(user) == password:
    print("Přístup povolen.")
else:
    print("Špatné heslo. Program se ukonci")
    quit()
print("Username:", user) 
print("Password:", password)
print("-" * 40)
print("Vitej", user)
print("Zadanim cisla od 1 do 3 vyber, jaky text chces analyzovat:")
odstavec = input()
if odstavec.isalpha() or int(odstavec) >= 4:
    print("Musis zadat cislo od 1 do 3, program se ukonci.")
    quit()
print("-" * 40)
text = texts[abs(int(odstavec) - 1)]
odst = []
for slova in text.split():
    odst.append(slova)
vysledek = {"velka" : 0, "mala" :0, "vsechna_velka" : 0, "numera" : 0}
for slovo in odst:
    if slovo.istitle():
        vysledek["velka"] = vysledek["velka"] + 1
    elif slovo.islower():
        vysledek["mala"] = vysledek["mala"] + 1
    elif slovo.isupper():
        vysledek["vsechna_velka"] = vysledek["vsechna_velka"] + 1
    elif slovo.isnumeric():
        vysledek["numera"] = vysledek["numera"] + 1
suma = 0
for slovo in odst:
    if slovo.isdigit():
        suma = suma + (int(slovo))
print("Pocet slov v textu je:", len(odst))
print("V textu je", vysledek["mala"], "lowercase slov.")
print("V textu je", vysledek["velka"], "titlecase slov.")
print("V textu je", vysledek["vsechna_velka"], "uppercase slov.")
print("V textu je", vysledek["numera"], "cisel.")
print("Soucet vsech cisel v textu je:", suma)
print("-" * 40)
bez_interp = [slovo.replace(",", "").replace(".", "") for slovo in odst]
delky_slov = []
for slovo in bez_interp:
    delky_slov.append(len(slovo))
vyskyt = {}
for delka in delky_slov:
 vyskyt[delka] = vyskyt.get(delka, 0) + 1
serazene = sorted(vyskyt.items())
print("LEN|", " " , "OCCURENCES", " " * 3, "|NR." )
print("-" * 40)
for delka, pocet in serazene:
    print(f"{delka:<3}|{'*' * pocet:<17} |{pocet}")
print("-" * 40)
print("Analyza dokoncena.")
print("-" * 40)    







