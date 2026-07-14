As I already changed the way hp works we of course need some readjusting to handle DnD-Forms for calculating some stuff.

HP now means life Energy basecally so how much life is drained from you by a source.

# Fall Damage

# Exhaustion

To exhaust is in DnD a 6 Level progression resulting in death. Those are:

| Level | Effect                                         |
| ----- | ---------------------------------------------- |
| 1     | Disadvantage on ability checks                 |
| 2     | Speed halved                                   |
| 3     | Disadvantage on attack rolls and saving throws |
| 4     | Hit point maximum halved                       |
| 5     | Speed reduced to 0                             |
| 6     | Death                                          |

Exhaustion is normally reduced by **1 level only after completing a Long Rest with full provisions** (food, water, and adequate warmth). Characters who sleep hungry or while suffering from cold cannot recover Exhaustion.

This already is really realistic. Normally you start to move slower, your muscles do not react like you wish, you start to hallucinate, you can't think anymore, you sleep longer. On extreme state you just can't move anymore and not only speed, but you can't use your muscles anymore as all your energy is needed for heart and breath. So at this state someone needs to care about you already, and lastly you just die. So base list is quite good you slowly lose your body control and life power. But I personally would not change anything on this yet. Maybe later if my group faces such punishment, I will return.

# Fall Damage 

Immediately affects your HP.

# Resting

A long rest is automatically also a short rest, but only one no matter how long you actually rest.

# Travel

In some campaigns, travel is an important part of the game, but D&D mostly reduces it to a simple 8-hour travel day. This system adds meaningful differences without turning travel into bookkeeping.

# Travel System – Final Formulas

## Base Values

| Parameter       |   Value |
| --------------- | ------: |
| Base Speed      |  5 km/h |
| Base March Time | 8 hours |

## Mounts

### Horse (Riding)

* Base Speed: **6 km/h**
* Base March Time: **8 h**
* Attributes:

  * **STR** = Carrying Capacity
  * **DEX** = Speed
  * **CON** = Endurance

**Base Range:** 48 km/day

### Horse & Wagon

* Base Speed: **4 km/h**
* Base March Time: **7 h**
* Attributes:

  * **STR** = Pulling Capacity
  * **DEX** = Ignored (fixed ×1)

Replace terrain with a **Road Modifier**:

| Surface    |         Multiplier |
| ---------- | -----------------: |
| Paved Road |               ×1.1 |
| Dirt Road  |               ×1.0 |
| Firm Grass |               ×0.8 |
| Mud        |               ×0.5 |
| No Road    | Usually impossible |

**Base Range:** 28 km/day

### Dragon (Flying)

*Balanced for gameplay rather than realism.*

* Base Speed: **30 km/h**
* Base Flight Time: **5 h**
* Attributes:

  * **STR** = Carrying Capacity
  * **DEX** = Flight Speed
  * **CON** = Flight Endurance

Replace terrain with a **Wind Modifier**:

| Wind            |                  Multiplier |
| --------------- | --------------------------: |
| Strong Tailwind |                        ×1.3 |
| Light Tailwind  |                        ×1.1 |
| Calm            |                        ×1.0 |
| Headwind        |                        ×0.8 |
| Storm           | ×0.4 (or flight impossible) |

**Base Range:** 150 km/day

### Swimming Creature

* Base Speed: **5 km/h**
* Base Travel Time: **6 h**
* Attributes:

  * **STR** = Carrying Capacity
  * **DEX** = Swim Speed
  * **CON** = Endurance

Replace terrain with a **Water Modifier**:

| Condition             | Multiplier |
| --------------------- | ---------: |
| Strong Current        |       ×1.3 |
| Light Current         |       ×1.1 |
| Calm Water            |       ×1.0 |
| Light Countercurrent  |       ×0.8 |
| Strong Countercurrent |       ×0.6 |
| Storm / Heavy Waves   |       ×0.4 |

**Base Range:** 30 km/day

---

# Block A – Speed

```
Speed = Base Speed × DEX Modifier × Terrain Modifier
```

### DEX Modifier

| DEX Mod | Multiplier |
| ------- | ---------: |
| -5      |       ×0.5 |
| -4      |       ×0.6 |
| -3      |       ×0.7 |
| -2      |       ×0.8 |
| -1      |       ×0.9 |
| 0       |       ×1.0 |
| +1      |       ×1.1 |
| +2      |       ×1.2 |
| +3      |       ×1.3 |
| +4      |       ×1.4 |
| +5      |       ×1.5 |

### Terrain Modifier

| Terrain                  | Multiplier |
| ------------------------ | ---------: |
| Road                     |       ×1.1 |
| Plains                   |       ×1.0 |
| Grassland / Light Forest |       ×0.9 |
| Hills / Dense Forest     |       ×0.8 |
| Swamp / Deep Snow        |       ×0.6 |
| Mountains                |       ×0.4 |

---

# Block B – Travel Time

### 1. Effective Load

```
Effective Load = max(0%, Load% − 15% × STR Modifier)
```

### 2. Load Multiplier

| Effective Load | Multiplier |
| -------------- | ---------: |
| 0–10%          |       ×1.0 |
| 10–25%         |       ×0.9 |
| 25–50%         |       ×0.8 |
| 50–75%         |       ×0.6 |
| 75–100%        |       ×0.4 |
| >100%          |       ×0.2 |

### 3. March Hours (CON)

| CON Mod | Hours |
| ------- | ----: |
| -5      |     3 |
| -4      |     4 |
| -3      |     5 |
| -2      |     6 |
| -1      |     7 |
| 0       |     8 |
| +1      |     9 |
| +2      |    10 |
| +3      |    11 |
| +4      |    12 |
| +5      |    13 |

### 4. Travel Time

```
Travel Time = March Hours × Load Multiplier
```

---

# Final Formula

```
Daily Range = Speed × Travel Time

= (Base Speed × DEX Modifier × Terrain Modifier)
  × (March Hours × Load Multiplier)
```

Speed and travel time are calculated independently and multiplied only at the end.

---

More Mechanics in character care sheet!


