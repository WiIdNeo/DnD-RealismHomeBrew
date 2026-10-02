import math

# ---------- Annahmen (hier justieren) ----------
PARTY_SIZE = 4
TARGET_ROUNDS_MARSHAL = 4
TARGET_ROUNDS_MAGE = 6
HIT_CHANCE = 0.65        # Trefferchance der Marshals
CRIT_CHANCE = 0.05       # Crit = zusätzlich ein Würfelwurf
MAGE_EFFECT = 0.75       # Anteil des Spell-Schadens, der im Schnitt ankommt (Save/Halbschaden)

# Schadensbonus je Stufe (an Monster-HP gekoppelt, wie von dir vorgesehen)
DAMAGE_BONUS = [5, 8, 10, 11]
HP_TIERS = [130, 220, 310]

AVG_Health_CR = [4, 21, 43, 60, 78, 93, 108, 123, 138, 153, 168, 183, 198, 213,
                 228, 243, 258, 273, 288, 303, 318, 333, 348, 378]  # 348 -> 378: Absicht?


class Dice:
    def __init__(self, sides):
        self.sides = sides
        self.base_damage = (1 + sides) / 2


dices = [Dice(s) for s in (4, 6, 8, 10, 12)]


def damage_bonus(hp):
    for tier, bonus in zip(HP_TIERS, DAMAGE_BONUS):
        if hp < tier:
            return bonus
    return DAMAGE_BONUS[-1]


def attacks_per_round(level):
    """Extra Attack des Marshals (D&D 5e Fighter). Level = Index + 1 (Annahme)."""
    if level >= 20:
        return 4
    if level >= 11:
        return 3
    if level >= 5:
        return 2
    return 1


# ---------- Marshal ----------
def expected_attack_damage(dice, bonus):
    return HIT_CHANCE * (dice.base_damage + bonus) + CRIT_CHANCE * dice.base_damage


def marshal_needed_attacks_per_round(hp_share, dice, bonus):
    """Angriffe pro Runde, damit man in TARGET_ROUNDS_MARSHAL Runden fertig ist."""
    total_attacks = math.ceil(hp_share / expected_attack_damage(dice, bonus))
    return math.ceil(total_attacks / TARGET_ROUNDS_MARSHAL)


def marshal_actual_rounds(hp_share, dice, bonus, attacks):
    return math.ceil(hp_share / (expected_attack_damage(dice, bonus) * attacks))


# ---------- Mage ----------
def mage_needed_dice(hp_share, dice, bonus):
    """Anzahl Würfel pro Runde (Modifikator einmal), damit TARGET_ROUNDS_MAGE reichen."""
    x = 1
    while (dice.base_damage * x + bonus) * MAGE_EFFECT * TARGET_ROUNDS_MAGE < hp_share:
        x += 1
    return x


# ---------- Auswertung ----------
with open("Data.txt", "w", encoding="utf-8") as f:
    f.write("Spalten je Zeile: d4, d6, d8, d10, d12\n\n")
    for idx, hp in enumerate(AVG_Health_CR):
        level = idx + 1
        bonus = damage_bonus(hp)
        hp_share = hp / PARTY_SIZE  # jeder Spieler trägt 1/4 der HP bei
        atk = attacks_per_round(level)

        needed_atk = [marshal_needed_attacks_per_round(hp_share, d, bonus) for d in dices]
        actual = [marshal_actual_rounds(hp_share, d, bonus, atk) for d in dices]
        mage = [mage_needed_dice(hp_share, d, bonus) for d in dices]

        f.write(
            f"--- Eintrag {level} | HP {hp} | Bonus {bonus} | Angriffe/Runde {atk} ---\n"
            f"Marshal benötigte Angriffe/Runde (Ziel {TARGET_ROUNDS_MARSHAL}): {needed_atk}\n"
            f"Marshal tatsächliche Runden:                  {actual}\n"
            f"Mage benötigte Würfel/Runde (Ziel {TARGET_ROUNDS_MAGE}):        {mage}\n\n"
        )