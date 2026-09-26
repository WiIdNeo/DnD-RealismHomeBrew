import random

def rand_die(x):
    return random.randint(1, x)

n = 100000
boni = [3, 4, 5, 6, 7]

wurf_typen = [
    "d20 (Vergleich)",
    "2d20",
    "d20+1d4", "d20+2d4",
    "d20+1d6", "d20+2d6",
    "d20+1d8", "d20+2d8",
    "d20+1d10", "d20+2d10",
    "d20+1d12", "d20+2d12",
]

for bonus in boni:
    counters = {name: 0 for name in wurf_typen}

    print(f"\n=========== Baseline: d20 + {bonus} ===========")
    header = f"{'i':>3} | {'Baseline':>10} | {'d20':>5} | {'2d20':>5}"
    for size in [4, 6, 8, 10, 12]:
        header += f" | {'d20+1d'+str(size):>9} | {'d20+2d'+str(size):>9}"
#    print(header)

    for i in range(n):
        baseline = rand_die(20) + bonus

        vergleich_d20 = rand_die(20)
        zwei_d20 = rand_die(20) + rand_die(20)

        werte = {
            "d20 (Vergleich)": vergleich_d20,
            "2d20": zwei_d20,
        }
        zeile = f"{i:>3} | {baseline:>10} | {vergleich_d20:>5} | {zwei_d20:>5}"

        for size in [4, 6, 8, 10, 12]:
            wurf_1x = rand_die(20) + rand_die(size)
            wurf_2x = rand_die(20) + rand_die(size) + rand_die(size)

            werte[f"d20+1d{size}"] = wurf_1x
            werte[f"d20+2d{size}"] = wurf_2x

            zeile += f" | {wurf_1x:>9} | {wurf_2x:>9}"

        for name, wert in werte.items():
            if wert > baseline:
                counters[name] += 1

#        print(zeile)

    print(f"\n--- Auswertung für Baseline d20+{bonus} ---")
    for name, count in counters.items():
        prozent = (count / n) * 100
        print(f"{name:<16}: {count:>3} von {n} Würfen höher ({prozent:.1f} %)")