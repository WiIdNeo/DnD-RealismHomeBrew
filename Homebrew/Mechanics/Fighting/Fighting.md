# Combat System for DnD Homebrew

Many aspects of DnD's standard rules feel too light, too generic, or
tactically flat. The goal of this system is to make combat more realistic and
tactically demanding: a bandit should feel different from a dragon — not just
through more HP, but through different decisions made during the fight.

**Core idea:** Real physical resilience barely increases with level — a human
dies from an arrow to the eye regardless of experience. What actually
increases is technique and anticipation. This isn't reflected by more HP, but
by better active defense — now fueled by a shared, **Token
pool**.

If not stated differently, the original DnD fighting rules apply. This is a
theoretical concept, not yet playtested. Raise an issue if you spot a problem!

---

## 1. Core Mechanic: Range

| Distance | Mod |
| ---------: | --------------: |
|      0.5 m |               0 |
| 3 m| 1 |
|        5 m |               2 |
|       10 m |               4 |
|       20 m |               6 |
|       30 m |               8 |
|       40 m |              10 |
|       50 m |              12 |
|       75 m |              15 |
|      100 m |              18 |
|      125 m |              20 |

If in melee this is is always 0.

> **Exception — Called Shots:** Precise hits on small target zones (eye,
> throat) remain uncertain even at close range. The attacker rolls an
> additional precision check, only as a deliberate special action. DM decides
> how much harder called shots are — smaller zone = harder, and size
> differences between combatants (e.g. a halfling aiming for a giant's eye)
> may raise the difficulty or require a prior skill check.

---

## 2. Attributes

### STR
Harder hits → harder to parry/block, easier to break the opponent's stance.
Own blocks are more resilient.

### DEX
Faster movement → higher initiative, better parries. Arrow shots are easier
to dodge. Governing stat for finesse weapons and ranged combat.

### CON
Increases HP, and decreases stamina drain in longer fights. 

**Governing stat per weapon:** STR for most melee weapons, DEX for finesse
weapons (dagger, rapier) and ranged combat.

---

## 3. Defense Options

You got 3 defensive options:

- Dodging
- Blocking
- Parrying

### Form

You throw 1d20. If you get higher than the attacker you win, else you loose.

In addition you can throw up to Stat-Mod times an additional d20 (you need to declare before throw)

Parry and Dodge scale on DEX

Blocking Scales on CON

```
This means if your DEX-Mod is +4 you can buff up to 4 DEX-Defenses. You can not buff 4 parries and 4 dodges!
```

### Blocking 

Blocking means you absorb the hit with your weapon, best a shield. The shilding will absorb all the damage, but it can be overcome or your poise can be broken.

This will highly refer to the weapons' kinds. If your blocking weapon got higher Tier than the attackers weapon your block throw is increased by the tiers and your poise can't be broken. But if the attacker still wins the check he will overcome your block doing normal Damage. In case your attacker's weapon tier is higher or equal to yours it is about poise breaking. If the attacker wins the check he will breake your stance sending you to ground and on dms flavor may throw yoou back little bit. Here no tier difference is applied.

If your enemy is larger category than you he gets +x² on the poise check, while x is the size tiers between you and the enemy.

### Parrying

To parry means you redirect your opponents attack to expose him. But to fail it means to expose yourself to the enemy's attack.

If you get the check you can freely attack without rolling a d20 and just the damage.

If you fail the check your enemy can add it's Prof-Mod to it's attack.

The checks are also influenced by die Parry Bonuses of the weapons, but not py size, as parrying does not get much harder on different size.

### Dodging

Dodging is just evading the enemy's attack and therefore it does not have a penality resulting in damage, but it consumes some movement you got for the round and you can't do it anymore if you do not have the needed Movement left.

---

## 4. Damage

$$\text{Damage} = \max\left(1,\ \text{Weapon-Roll} + \text{Prof-Mod} + \text{Stat-Mod}\right)$$

### Rounding Rule
Standard 0.5 → round up, but reduce the base value by 0.07 first (so x.5
averages effectively round down, e.g. 1d6 average 3.5 → 3.43 → 3).

---

## 9. AC & Initiative

### Initiative
Still determines turn order.

### AC
Not binary hit/miss, but a damage modifier:

$$\text{Mod} = \frac{1}{AC/10}$$

AC 10 = neutral (×1), AC 20 = ×0.5 (half damage), AC 5 = ×2 (double damage).
Full avoidance remains reserved for active reactions (Block/Parry/Dodge).

---

## 10. Attack Zones

Base idea: specific body parts are more penetrating than others. A hit to
the arm or foot hampers movement but deals normal-to-low damage; a hit to
the head is dangerous, and a hit to ear/eye can be immediate death. 

---

## 11. Buffs

Most buffs are covered in the separate `Buffs.md`.

### Advantage and Disadvantage
If a target is blinded, it isn't easier for you to aim —
it's harder for *them* to notice the attack. So Advantage/Disadvantage come
from specific Buffs/Debuffs and typically mean "best of two" on the damage
die, or disadvantage on a saving throw. So even if something tells advantage/disadvantege for you,
your dm may makes the call it is instead the opposite for your opponent.

---

## 12. Dying

Reducing a creature's HP to 0 doesn't kill it immediately — it goes
unconscious. Wound severity then determines whether it starts dying and
needs care, or simply wakes up later. While down, a creature is helpless;
attacking an unconscious target allows an undefended finishing blow.

---

## 13. Opportunity Attacks

Opportunity Attacks will be mostly removed from game to make skirmishing and tactic actually work.

---

## 14. Disarming

**How to disarm:** either the foe critically fails (nat1) their
parry/block and drops the weapon, or you declare a disarm attempt — on a
hit, the foe makes the normal defensive throw against you. Losing the save drops the called-out weapon. Two-handed weapons
grant advantage on this save.

