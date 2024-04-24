import sys
from mathematical_library import delenie, nasobenie, odcitanie, scitanie, odmocnina
import numpy as np
import cProfile
import pstats

def smerodajna_odchylka(data):
    if len(data) < 2:
        raise ValueError("Na výpočet smerodajnej odchylky je potrebné aspoň dve hodnoty.")
    priemer = delenie(sum_data(data), len(data))
    variancia = delenie(sum_data([nasobenie(odcitanie(x, priemer), odcitanie(x, priemer)) for x in data]), len(data))
    return odmocnina(variancia, 2)


def sum_data(items):
    total = items[0]
    for item in items[1:]:
        total = scitanie(total, item)
    return total

def profile_with_inputs(input_sizes):
    for size in input_sizes:
        data = np.random.standard_normal(size).tolist()
        profiler = cProfile.Profile()
        profiler.enable()
        print(f"Smerodajna odchylka pre {size} prvkov: {smerodajna_odchylka(data)}")
        profiler.disable()
        stats = pstats.Stats(profiler).sort_stats('cumulative')
        stats.print_stats()
        print("\n\n")

if __name__ == "__main__":
    input_sizes = [10, 1000, 1000000]  # Velkosti vstupov ako bolo požadované
    profile_with_inputs(input_sizes)
    input("Press Enter to end...")
