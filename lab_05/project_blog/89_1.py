import requests

tab = '\t'
line_break = '\n'
categories = requests.get("https://api.chucknorris.io/jokes/categories").json()

print(f"""Dostepne kategorie zartow:{line_break}""")

for i, c in enumerate(categories):
    print(f"""Indeks: {i}{tab}Nazwa:  {c}""")

category = input(f"Wybierz i wpisz jedna z kategorii{line_break}")
joke = requests.get(f"https://api.chucknorris.io/jokes/random?category={category}").json()

for k, v in joke.items():
    if k == 'value':
        print(f"{v}{line_break}")
