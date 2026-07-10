I personally do not like those standard-Arrays or Dicings for character stats, as this is only in parts lets you make your character fullfill their story. So my Homebrew follows the idea of buying skills.

# System

Every Ability point costs something. This is increasing for height. As this system is focusing more on those Stats but also wants you to have this real leveling experience, you will gain some Point-Pfunds to buy more abilty points furing level process.

Once you spend your points they are fix. You can't lower later on anymore, unless Dm allows, so think about it carefully.

## How to start?

You start with all your Stats being 1

```
1 - 1 - 1 - 1 - 1 - 1
```

The base cost of you skills is 1, but it increases if your current value reaches 3. 

$$\text{cost of next point on this abillity} = \text{current height of that ability} / 3 +0.5$$

Following the rounding system of x.5 rounding down you get following values:

| Current value |      Cost | Cost rounded (actual Pfunds you spend) |
| ------------: | --------: | -------------------------------------: |
|             1 |  0.833333 |                                      1 |
|             2 |  1.166667 |                                      1 |
|             3 |  1.5 |                                      1 |
|             4 |  1.833333 |                                      2 |
|             5 |  2.166667 |                                      2 |
|             6 |  2.5 |                                      2 |
|             7 |  2.833333 |                                      3 |
|             8 |  3.166667 |                                      3 |
|             9 |  3.5 |                                      3 |
|            10 |  3.833333 |                                      4 |
|            11 |  4.166667 |                                      4 |
|            12 |  4.5 |                                      4 |
|            13 |  4.833333 |                                      5 |
|            14 |  5.166667 |                                      5 |
|            15 |  5.5 |                                      5 |
|            16 |  5.833333 |                                      6 |
|            17 |  6.166667 |                                      6 |
|            18 |  6.5 |                                      6 |
|            19 |  6.833333 |                                      7 |
|            20 |  7.166667 |                                      7 |
|            21 |  7.5 |                                      7 |
|            22 |  7.833333 |                                      8 |
|            23 |  8.166667 |                                      8 |
|            24 |  8.5 |                                      8 |
|            25 |  8.833333 |                                      9 |
|            26 |  9.166667 |                                      9 |
|            27 |  9.5 |                                      9 |
|            28 |  9.833333 |                                     10 |
|            29 | 10.166667 |                                     10 |


Cost to specific levels are:

| Abillity Value | Cost |
| --------: | -----------: |
|         1 |            0 |
|         2 |            1 |
|         3 |            2 |
|         4 |            3 |
|         5 |            5 |
|         6 |            7 |
|         7 |            9 |
|         8 |           12 |
|         9 |           15 |
|        10 |           18 |
|        11 |           22 |
|        12 |           26 |
|        13 |           30 |
|        14 |           35 |
|        15 |           40 |
|        16 |           45 |
|        17 |           51 |
|        18 |           57 |
|        19 |           63 |
|        20 |           70 |
|        21 |           77 |
|        22 |           84 |
|        23 |           92 |
|        24 |          100 |
|        25 |          108 |
|        26 |          117 |
|        27 |          126 |
|        28 |          135 |
|        29 |          145 |
|        30 |          155 |

From level 10 are:

| Level to reach | Cost |
| ------------: | -----------------: |
|            11 |                  4 |
|            12 |                  8 |
|            13 |                 12 |
|            14 |                 17 |
|            15 |                 22 |
|            16 |                 27 |
|            17 |                 33 |
|            18 |                 39 |
|            19 |                 45 |
|            20 |                 52 |
|            21 |                 59 |
|            22 |                 66 |
|            23 |                 74 |
|            24 |                 82 |
|            25 |                 90 |
|            26 |                 99 |
|            27 |                108 |
|            28 |                117 |
|            29 |                127 |
|            30 |                137 |


But know the real question: What values do you start with? As you gain on level up always some to increase later one, you know do not get to many Pfunds. 
```
min = 18 * 6 = 108
max = 35 * 6 = 210
~~> 180?
    Most classes specify on 2 Attributes:
        max for just those is 22 (84) and you got 14 left:
            So you could all let reach 4 (3) and got two more left, so one reaches 5. 
                This would mean -3 on everthing except for two main stats being +6
                    Too high!
~~> 150?
    max in two:
        20 (70), ten left:
            3 in rest
                -3 on all, +5 in mains
    all 0 plus main:
        10 x 6 = 60
            two main stats:
                19: +4
                    Too high!
~~> 130?
    10 x 6 = 60 --> 70
        17, 4 left
            one more to 11
                0 on all
                    +3 on max
                        would be +6 
                            Standerd-array is -1, 0, +1, +1, +2, +2 => +5
                                seams fair
```

## Leveling

You gain per level your Professiency Bonus in Pfunds. So to level 20 you gain 78. Your Background grands you 3 free Level ups, in any way you want, but +2 max. The ASIs grant you additionally 5 to 7 two free level ups of your choice. (for fairness I may fix the number of feasts for each class, I will see during PHB rework and playtesting), which means between 10 and 14 free levels.

```
Think you are an fighter. Your background is you are a guardian of the forests, so your main attribut may be DEX and you got two off attributes: WIS and CON
You go for good alrounder having everything to 10. You spend 108 of your 130 into your stats. Than you increase DEX twice and WIS and COn both once. Resulting in 13 in DEX, 12 in WIS and 11 in CON. Than your background grants you two DEX and one WIS. So your stats in the beginning look like:
STR: 10
DEX: 15
CON: 11
INT: 10
WIS: 13
CHA: 10

You gain Feats lvl 4, 8, 12, 16, 19 (base) + 6, 14 (fighter)

Prof Bonus:
| Lvl | Bonus |
| 1 - 4| 2
| 5 - 8| 3
| 9 - 12 | 4
| 13 - 16 | 5
| 17+ | 6

Level 4: 6 Pfunds => +1 DEX, 1 Pfund Keeped
On such a low level you may also go for ASI instead of Feat and therefore go +2 DEX, as it is the most expensive

DEX: 18

Level 6: 1+6 Pfunds
You spend 4 for +1 in CON, 3 left
The ASI you spend for a half feat: +1 in a stat +prof in all Attribut conected Checks
You gof or DEX

STR: 10
DEX: 19
CON: 12
INT: 10
WIS: 13
CHA: 10

Lvl 8: 6+3 Pfunds
You go for a full Feat this time
You spend one in each CON and WIS for 9 cost combinded
STR: 10
DEX: 19
CON: 13
INT: 10
WIS: 14
CHA: 10

Level 12: 16 Pfunds
Also this time you go for a full feat
May spend 1 Upgrade in DEX go get +5 Bonus and another in Wis (cost: 12)

Level 14: 10+4 Pfunds
Spend 10 Pfunds for two levels of CON
ASI: two in CON
STR: 10
DEX: 20
CON: 17
INT: 10
WIS: 15
CHA: 10

Level 16: 10+4 Pfunds
13: One in Dex one in WIS
ASI into feat

Level 19: 17+1
2 in WIS, 1 to CON (18)
WIS-Half Feat
STR: 10
DEX: 20
CON: 18
INT: 10
WIS: 18
CHA: 10

Level 20: 6 Pfunds
One to Con:
STR: 10
DEX: 20
CON: 19
INT: 10
WIS: 18
CHA: 10

```