import sys
from mathematical_library import delenie, nasobenie, odcitanie, scitanie, odmocnina

def smerodajna_odchylka(data):
    if len(data) < 2:
        raise ValueError("Na výpočet smerodajnej odchylky je potrebné aspoň dve hodnoty.")
    priemer = delenie(sum_data(data), len(data))
    # Konvertujeme generátor na zoznam pred volaním sum_data
    variancia = delenie(sum_data([nasobenie(odcitanie(x, priemer), odcitanie(x, priemer)) for x in data]), len(data))
    return odmocnina(variancia, 2)

def sum_data(items):
    total = items[0]
    for item in items[1:]:
        total = scitanie(total, item)
    return total

def main():
    try:
        # Žiadame používateľa, aby zadal čísla oddelené medzerami
        print("Zadajte čísla oddelené medzerami:")
        data = [float(num) for num in input().strip().split()]

        # Výpočet a výpis smerodajnej odchylky
        print("Smerodajná odchylka:", smerodajna_odchylka(data))
    except Exception as e:
        print(f"Chyba: {e}")

if __name__ == "__main__":
    main()
