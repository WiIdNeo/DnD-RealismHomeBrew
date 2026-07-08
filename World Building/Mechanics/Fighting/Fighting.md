# Combat System for DnD Homebrew

Many aspects of DnD's standard rules feel too light, too generic, or tactically flat. The goal of this system is to make combat more realistic and tactically demanding: a bandit should feel different from a dragon — not just through more HP, but through different decisions made during the fight.

This system is inspired by *The Riddle of Steel*, but not a 1:1 copy — the stamina resource, weapon classes, and attribute weighting are adapted independently.

**Core idea:** Real physical resilience barely increases with level — a human dies from an arrow to the eye regardless of experience. What actually increases is technique and anticipation. This isn't reflected by more HP, but by better active defense.

---

If not stated differently the original DnD fighting rules are applied. Remember this is work in progress and for now only a theoretical concept and not playtested. If you notice any problem please raise an issue!

## 1. Core Mechanic: Ranged vs. Melee

| Distance | DC |
| ---------: | --------------: |
|      0,5 m |               2 |
|        5 m |               3 |
|       10 m |               4 |
|       20 m |               6 |
|       30 m |               8 |
|       40 m |              10 |
|       50 m |              12 |
|       75 m |              15 |
|      100 m |              18 |
|      125 m |              20 |

> **Exception — Called Shots:** Precise hits on small target zones (eye, throat) remain uncertain even at close range. Here the attacker rolls an additional precision check, but only as a deliberate special action, not as the default. (Details: see Attack Zones section, TBD.)
> 
> Dm decides how much harder called shoots are. Normally the smaller, the harder. Of course a called shot to Heart and you role one to low does not need to mean to not hit. It could also mean just not hitting that critical zone. But DM makes that call. Also the size difference can be hard, as a tiny human like halfling could become problem if hitting a giant into eye. So DM may increase difficulty or requires a prior Skill check. This would also fix problems about precise longshots to an eye or something.

Reactions are limited by a stamina pool (relevant only for defense — offense remains pure action economy).

---

## 2. Attributes

### STR
Harder hits → harder to parry/block, easier to break the opponent's stance. Own blocks are more resilient.

### DEX
Faster movement → higher absolute stamina, better initiative, easier parries. Arrow shots are harder to dodge. Governing stat for finesse weapons and ranged combat.

### CON
HP matters less, but CON stays relevant: increases resistance to impacts/falls and makes stamina more valuable (multiplier on the pool).

**Governing stat per weapon:** STR for most melee weapons, DEX for finesse weapons (dagger, rapier) and ranged combat. See weapon table.

---

## 3. Weapon Table

Weapons grant you different buffs and debuffs for checks and properties making the correct weapon choice quite important. As this is a really long list of all weapons and their buff there will be another markdown on this.

---

## 4. Magic

Most spells require line of sight and (for precision effects) anatomical knowledge of the target — no "popping a vein in the brain" without sight and expertise. Projectile spells work like physical ranged attacks: the defender gets a normal Dodge/Block check against them.

---

## 5. Stamina

### 5.1 Formula

Level (Prof) and Constitution are scaled **separately**, so both can be tuned independently:

$$\text{Stamina} = \text{LevelBase}(\text{Prof}) \times \text{ConMult}(\text{Con-Mod})$$

$$\text{LevelBase} = 50 + 10 \cdot (\text{Prof} - 2)$$
$$\text{ConMult} = 1 + \frac{\text{Con-Mod}}{10}$$

| Prof | LevelBase | | Con-Mod | ConMult |
|---|---|---|---|---|
| 2 (Lvl 1) | 50 | | -5 | 0.5 |
| 3 | 60 | | -3 | 0.7 |
| 4 | 70 | | 0 | 1.0 |
| 5 | 80 | | +3 | 1.3 |
| 6 (Lvl 20) | 90 | | +5 | 1.5 |

**Why separate:** Pure level scaling (at Con=0) gives 50 → 90, a factor of **1.8×** — roughly matching damage scaling (see below) and preventing experienced fighters from being able to sustain proportionally *fewer* blocks than beginners. CON remains an independent second axis: worst CON exactly halves the pool.

### 5.2 Reset

Stamina regenerates per combat, not per round — a middle ground between realism and bookkeeping.

---

## 6. Defense Options

**Success DC:**
$$DC = 10 + \text{Init-Diff-Tier} + \text{Attacker-Prof} - \text{Defender-Prof}$$

Defender rolls a plain 1d20 ≥ DC (all modifiers are already baked into the DC). At parity with no initiative difference: ~50/50. A natural 20 always succeeds, a natural 1 always fails.

**Init-Diff-Tier** (capped at max. +4, to limit stacking with stat/prof bonuses):

| Initiative Difference | Tier |
|---|---|
| 0 | 0 |
| 3 | 1 |
| 6 | 2 |
| 9 | 3 |
| 12 | 4 |
| 15 | 5|
| 18 | 6 |
| 21 | 7 |
| ... | ... |

*Replaces a separate "can I react at all" gate check — the initiative difference flows directly into the existing defense DC, no extra roll needed.*

In case you role a nat1 or nat20 that only effects your position in action queue, the Initiative for this difference is still increased/decreased according to Buffs.


### 6.1 Dodge

Fixed stamina cost of 9. Pure DEX check, scaling with distance/attacker's DEX. On success: 0 damage.

### 6.2 Block
You gain a block buff depending on your block weapon, stamina drain scales with the damage of the hit:

$$\text{Stamina-Drain} = \text{Damage} \times \left(1 + \frac{\text{Stance-Breaking}}{2}\right)$$

If the pool drops below 0, the remaining force is passed through proportionally as damage (see calculation example 8.3).

### 6.3 Parry
Requires timing (success check). On success: 0 damage + free counterattack (opportunity attack, no reaction possible from the opponent). On failure: full hit. There is a parry bonus to the check depending on your weapon.

**Cost (regardless of success):**
$$\text{Stamina-Drain} = \left(\text{Damage} \times \frac{\text{Stance-Breaking}}{2}\right) + \frac{\text{Prof-Mod}}{2}$$

### 6.4 Reference Values for Stamina Costs

| Action | Cost |
|---|---|
| Dodge | fixed ~9 |
| Parry | variable, ~2–15 (see 6.3) |
| Block | variable, ~4.5–18+ depending on weapon/damage (see 6.2) |

---

## 7. Damage

### 7.1 Formula

$$\text{Damage} = \max\left(1,\; 1d6 + \text{Prof-Mod} + \text{Stat-Mod}\right)$$

- **Prof-Mod** unchanged (+2 to +6) — carries the level curve.
- **Stat-Mod** (weapon's governing stat) full weight
- Minimum 1 damage on any hit, regardless of negative modifiers.

*So that a level-1 wizard and a level-1 barbarian with the same weapon deal different damage — not because of level, but because of build.*

### 7.2 Rounding Rule
Standard 0.5 → 1 round-up, but the base value is reduced by 0.1 beforehand (effectively rounds x.5 values down, e.g. 1d6 average 3.5 → 3.4 → 3).

---

## 8. Calculation Examples

### 8.1 Stamina Pool: Minimum and Maximum Case

| Case | Level (Prof) | Con-Mod | Stamina |
|---|---|---|---|
| Minimum | 1 (+2) | -5 | 50 × 0.5 = **25** |
| Reference (average) | 1 (+2) | 0 | 50 × 1.0 = **50** |
| Reference (average) | 20 (+6) | 0 | 90 × 1.0 = **90** |
| Maximum | 20 (+6) | +5 | 90 × 1.5 = **135** |

### 8.2 Dagger Damage: Minimum and Maximum Case

| Case | Level | Stat-Mod | 1d6 | Damage |
|---|---|---|---|---|
| Minimum | 1 (+2) | -5 | 1 | max(1, 1+2-5) = **1** |
| Minimum, avg roll | 1 (+2) | -5 | 3 | max(1, 3+2-5) = **1** |
| Maximum, avg roll | 20 (+6) | +5 | 3 | 3+6+5 = **14** |
| Maximum | 20 (+6) | +5 | 6 | 6+6+5 = **17** |

### 8.3 Core Question: Can a Maxed-Out Build Take Down a Weak Defender in 1–2 Hits?

**Setup:** Attacker: Level 20, Stat-Mod +5, Hammer (Stance-Breaking 4, multiplier ×3). Defender: Level 1, Con-Mod -5 → Stamina pool **25** (minimum case from 8.1).

| Roll | Damage (Attacker) | Block-Drain (×3) | Remaining Pool After Block |
|---|---|---|---|
| Minimum (1d6=1) | 12 | 36 | -11 |
| Average (1d6≈3) | 14 | 42 | -17 |
| Maximum (1d6=6) | 17 | 51 | -26 |

**Result:** Even the weakest possible hit from a maxed-out hammer build exceeds the entire stamina pool of a fragile defender — **the very first block already can't be fully absorbed.**

**Overflow Damage:**

$$\text{Damage Through} = \text{Damage} \times \frac{\text{Overflow}}{\text{Drain}}$$

| Roll | Overflow | Fraction | Damage Through |
|---|---|---|---|
| Minimum | 11 | 0.31 | ≈ **4** |
| Average | 17 | 0.40 | ≈ **6** |
| Maximum | 26 | 0.51 | ≈ **9** |

**Conclusion:** Not an instant kill in one hit (the wound pool is separate and larger), but stamina is fully spent after this single block — any further attack in the same round lands unhindered at full damage (12–17). This confirms that the three defense options carry real tactical weight: against a clearly superior hammer-wielder, **Dodge (fixed cost ~9) is clearly the better choice** over Block — exactly the kind of situational decision this system is meant to create.

---

## 9. AC & Initiative

### Initiative
Still determines turn order. Additionally, the difference between two combatants' initiative values flows directly into the Defensive DC as a tier (see 6.3) — no separate reaction gate roll.

### AC
No longer a binary hit/miss, but a damage modifier:

$$\text{Mod} = \frac{1}{AC/10}$$

AC 10 = neutral (×1), AC 20 = ×0.5 (half damage), AC 5 = ×2 (double damage). Full avoidance remains reserved for active reactions (Block/Parry/Dodge).

---

## 10. Attack Zones (WIP)

Base idea is to bring more realism to fights by making specific body parts more penetrating than others.
A hit to the arm or foot may is bad for movement, but damage is just normal to low. In opposite a hit to head is really dangerous and deals a lot of damage and as conclusion a hit into ear or eye is immediate death. Therefore, this system supports different body parts. Of course, you can bring a lot of rules in this for loosed arms or legs and stuff like this, but I would say that's mainly a dm topic he is deciding on the fly. As the damage in this system also is not really high, normally about 3.5+Mods the hit into a vital area may grant a further d4 to d8 depending on zone. But that's a dm choice.

---

## 11. Example Combat Sequence

- A sets a bonus-attack trigger: "when the opponent's parry fails" (A exploits the opening).
- An attack:
  - Damage roll
  - *(no precision roll in melee, see Section 1)*
- B reacts with a Parry (costs stamina, simultaneously opens B's own guard):
  - Stamina deducted from B
  - Success check against DC (see 6.3):
    - **Failure:** A hits B with full damage
    - **Success:** B hits A (free counterattack) + A's bonus trigger fires → A additionally hits B