As stated in Fighting.md (3) the weapons all gain different buffs and debuffs making builds more relevant, but also flavored.

Those buffs got a scaling from range about 5 points. But I will immediately calculate it to the actual mod. For this the baseline is just the normal sword in DnD called Long Sword.

## Buffs
### Parry DC Buff
This is indicator about how hard it is to actually get the parry done. This is mainly influenced by the weapons size and attack angle.

### Parry Buff
This is the Buff of your parry weapon you can add to your Role and buffs on a parry. This is mainly influenced by the weapons properties, so size mainly.

### Stance-Breaking Damage
This is the Damage buff applied if you hit someone want to parry/block you. This is based on weight of the weapon. This does only affect the stamina drain not the actual damage if you hit the opponent!

### Block Buff
This is the Buff of your block weapon you can add to your Role and buffs on a block. This is mainly influenced by the weapons properties, so size and resistance mainly.

### Initiative-Buff
If your weapon is really heavy it is likely to slow you down. To simulate that you get a buff or debuff depending on your weapons size and weight. So clunky weapons like staffs even than slow you down if they are more light weight.

## Overview

| Waffe               | Wield  | Init | Parry DC | Parry | Block | Stance Dmg |
| ------------------- | ------ | ---: | -------: | ----: | ----: | ---------: | 
| Keule               | single |   -1 |       -1 |    -1 |     0 |         +1 | 
| Dolch               | single |   +3 |       +1 |    -2 |    -2 |         -2 | 
| Handaxt             | single |   +1 |       -1 |    -1 |     0 |         +1 | 
| Wurfspeer           | single |   +1 |       +2 |     0 |    -1 |          0 | 
| Leichter Hammer     | single |    0 |       -2 |    -1 |    +1 |         +1 |
| Streitkolben        | single |   -1 |       -2 |    -2 |    +2 |         +2 |
| Sichel              | single |   +2 |       -2 |    -2 |    -2 |         -1 |
| Wurfpfeil           | single |   +3 |       -3 |    -3 |    -3 |         -3 |
| Schleuder           | single |   +3 |       -3 |    -3 |    -3 |         -3 |
| Dreschflegel        | single |   -1 |       -3 |    -3 |    -2 |         +2 |
| Morgenstern         | single |   -2 |       -3 |    -2 |     0 |         +3 |
| Rapier              | single |   +2 |       +3 |    +3 |    -2 |         -2 |
| Krummsäbel          | single |   +2 |       +1 |    +1 |     0 |          0 |
| Kurzschwert         | single |   +2 |       +2 |    +1 |     0 |          0 |
| Kriegshacke         | single |    0 |       -2 |    -1 |     0 |         +2 |
| Peitsche            | single |   +3 |       -3 |    -3 |    -3 |         -3 |
| Blasrohr            | single |   +3 |       -3 |    -3 |    -3 |         -3 |
| Handarmbrust        | single |    0 |       -3 |    -3 |    -3 |         -3 |
| Netz                | single |    0 |       -3 |    -3 |    -3 |         -3 |
| Kampfstab           | single |    0 |       +2 |    +2 |    +2 |          0 |
| Kampfstab           | double |   -1 |       +3 |    +3 |    +3 |         +1 |
| Speer               | single |   +1 |       +2 |    +1 |     0 |          0 |
| Speer               | double |    0 |       +3 |    +2 |    +1 |         +1 |
| Streitaxt           | single |   -1 |       -1 |     0 |    +1 |         +2 |
| Streitaxt           | double |   -2 |        0 |    +1 |    +2 |         +3 |
| Langschwert         | single |    0 |        0 |     0 |     0 |          0 |
| Langschwert         | double |   -1 |       +1 |    +2 |    +2 |         +1 |
| Dreizack            | single |    0 |       +1 |     0 |     0 |          0 |
| Dreizack            | double |   -1 |       +2 |    +1 |    +1 |         +1 |
| Kriegshammer        | single |   -2 |       -1 |     0 |    +2 |         +3 |
| Kriegshammer        | double |   -3 |        0 |    +1 |    +3 |         +3 |
| Großer Knüppel      | double |   -2 |       -1 |     0 |    +2 |         +2 |
| Leichte Armbrust    | double |   -2 |       -3 |    -3 |    -3 |         -3 |
| Glefe               | double |   -2 |       +2 |    +2 |    +2 |         +2 |
| Großaxt             | double |   -3 |       -2 |    -1 |    +2 |         +3 |
| Großschwert         | double |   -2 |       +2 |    +3 |    +3 |         +2 |
| Hellebarde          | double |   -3 |       +1 |    +2 |    +2 |         +3 |
| Streithammer (Maul) | double |   -3 |       -2 |     0 |    +3 |         +3 |
| Pike                | double |   -3 |       +3 |    +2 |    +1 |         +1 |
| Schwere Armbrust    | double |   -3 |       -3 |    -3 |    -3 |         -3 |
| Langbogen           | double |    0 |       -3 |    -3 |    -3 |         -3 |

| Waffe               | Angriff   | Radiant |  Länge | Speed               |
| ------------------- | --------- | ------: | -----: | ------------------- |
| Keule               | Hieb      |    100° |  80 cm | normal              |
| Dolch               | Stich     |     10° |  20 cm | fast                |
| Dolch               | Hieb      |     80° |  20 cm | fast                |
| Handaxt             | Hieb      |    100° |  40 cm | normal              |
| Wurfspeer           | Wurf      |      5° | 180 cm | normal              |
| Leichter Hammer     | Hieb      |    100° |  40 cm | normal              |
| Streitkolben        | Hieb      |    100° |  70 cm | normal              |
| Sichel              | Hieb      |    110° |  45 cm | fast                |
| Wurfpfeil           | Wurf      |      3° |  15 cm | fast                |
| Schleuder           | Projektil |      2° |      – | fast                |
| Dreschflegel        | Hieb      |    130° |  90 cm | normal              |
| Morgenstern         | Hieb      |    120° |  80 cm | normal              |
| Rapier              | Stich     |      8° | 110 cm | fast                |
| Rapier              | Hieb      |     60° | 110 cm | fast                |
| Krummsäbel          | Hieb      |    120° |  95 cm | fast                |
| Kurzschwert         | Stich     |     10° |  70 cm | fast                |
| Kurzschwert         | Hieb      |    100° |  70 cm | normal              |
| Kriegshacke         | Hieb      |     95° |  75 cm | normal              |
| Peitsche            | Schnalzen |     40° | 250 cm | normal                |
| Blasrohr            | Projektil |      2° | 150 cm | fast                |
| Handarmbrust        | Bolzen    |      2° |      – | fast                |
| Netz                | Wurf      |     - | - | langsames Projektil |
| Kampfstab (1H)      | Stoß      |     10° | 170 cm | normal              |
| Kampfstab (1H)      | Hieb      |    120° | 170 cm | normal              |
| Kampfstab (2H)      | Stoß      |     10° | 180 cm | normal              |
| Kampfstab (2H)      | Hieb      |    140° | 180 cm | normal              |
| Speer (1H)          | Stoß      |      8° | 230 cm | normal                |
| Speer (1H)          | Hieb      |     90° | 230 cm | normal              |
| Speer (2H)          | Stoß      |      8° | 260 cm | normal                |
| Speer (2H)          | Hieb      |    100° | 260 cm | normal              |
| Streitaxt (1H)      | Hieb      |    110° |  80 cm | normal              |
| Streitaxt (2H)      | Hieb      |    120° | 120 cm | normal              |
| Langschwert (1H)    | Stich     |      8° | 110 cm | normal                |
| Langschwert (1H)    | Hieb      |    110° | 110 cm | normal              |
| Langschwert (2H)    | Stich     |      8° | 120 cm | normal                |
| Langschwert (2H)    | Hieb      |    120° | 120 cm | normal              |
| Dreizack (1H)       | Stich     |     12° | 220 cm | normal                |
| Dreizack (2H)       | Stich     |     12° | 240 cm | normal                |
| Kriegshammer (1H)   | Hieb      |     90° |  75 cm | normal              |
| Kriegshammer (2H)   | Hieb      |    100° | 120 cm | normal              |
| Großer Knüppel      | Hieb      |    110° | 150 cm | normal              |
| Leichte Armbrust    | Bolzen    |      2° |      – | fast                |
| Glefe               | Hieb      |    130° | 220 cm | normal              |
| Glefe               | Stich     |     10° | 220 cm | fast                |
| Großaxt             | Hieb      |    130° | 160 cm | normal              |
| Großschwert         | Stich     |      8° | 170 cm | normal                |
| Großschwert         | Hieb      |    130° | 170 cm | normal              |
| Hellebarde          | Stich     |     10° | 240 cm | normal                |
| Hellebarde          | Hieb      |    130° | 240 cm | normal              |
| Streithammer (Maul) | Hieb      |    100° | 170 cm | normal              |
| Pike                | Stich     |      5° | 450 cm | normal                |
| Schwere Armbrust    | Bolzen    |      2° |      – | fast                |
| Langbogen           | Pfeil     |      2° |      – | fast                |


| Weapon                | Damage Risky | Damage Save| Reason                                                   |
| --------------------- | -----: | -----:|--------------------------------------------------- |
| Club                  |    1d8 | 2d4 |Low penetration, but blunt trauma can still incapacitate |
| Dagger                |    1d8 | 2d4|Very lethal, but highly dependent on exact hit location  |
| Handaxe               |    1d8 | 2d4|Strong cutting force, enough mass                        |
| Javelin               |    1d10 | 1d6+1d4|Deep penetration, momentum from thrust/throw             |
| Light Hammer          |    1d8 | 2d4|Small mass, localized impact                             |
| Mace                  |    1d10 | 1d6+1d4|Heavy impact, strong against bone and armor              |
| Sickle                |    1d8 | 2d4|Cutting weapon, but limited penetration                  |
| Dart                  |    1d6 | - |Small projectile, limited wound channel                  |
| Sling                 |    1d8 | 2d4|Small projectile but high velocity                       |
| Flail                 |    1d10 | 1d6+1d4|Heavy impact, unpredictable strikes                      |
| Morningstar           |    1d10 | 1d6+1d4|Similar to mace, spikes increase trauma                  |
| Rapier                |    1d8 | 2d4|Extremely dangerous thrust, but narrow wound             |
| Scimitar              |    1d10 | 1d6+1d4|Strong cutting weapon                                    |
| Shortsword            |    1d10 | 1d6+1d4|Balanced cutting/stabbing weapon                         |
| War Pick              |   1d12 | 2d6|Concentrated force, armor penetration                    |
| Whip                  |    1d6 | -|Painful but limited deep trauma                          |
| Blowgun               |    1d6 | -|Minimal physical damage                                  |
| Hand Crossbow         |    1d10 | 1d6+1d4|Strong penetration                                       |
| Net                   |      0 | -|No damage                                                |
| Quarterstaff (single) |    1d8 | 2d4|Blunt weapon, moderate mass                              |
| Quarterstaff (double) |    1d10 | 1d6+1d4|More leverage                                            |
| Spear (single)        |    1d10 | 1d6+1d4|Excellent penetration                                    |
| Spear (double)        |    1d10 | 1d6+1d4|More control, not much more wound damage                 |
| Battleaxe (single)    |   1d12 |2d6 |Heavy cutting edge                                       |
| Battleaxe (double)    |   1d12 | 2d6|More leverage, same injury potential                     |
| Longsword (single)    |    1d10 | 1d6+1d4|Baseline                                                 |
| Longsword (double)    |   1d12 | 2d6 |Two-handed leverage increases impact                     |
| Trident               |    1d10 |1d6+1d4 |Similar to spear                                         |
| Warhammer             |   1d12 |2d6 |Heavy concentrated impact                                |
| Greatclub             |   1d12 | 2d6|Massive blunt trauma                                     |
| Light Crossbow        |    1d10 |1d6+1d4 |High penetration                                         |
| Glaive                |   1d12 |2d6 |Heavy blade + leverage                                   |
| Great Axe             |   2d8 |2d6+1d4 |Maximum cutting trauma                                   |
| Greatsword            |   1d12 |2d6 |Less concentrated than axe but huge cuts                 |
| Halberd               |   1d12 | 2d6|Similar to poleaxe                                       |
| Maul                  |   2d8 | 2d4|Maximum blunt trauma                                     |
| Pike                  |    1d10 |1d6+1d4 |Deep penetration, but less mass                          |
| Heavy Crossbow        |   1d12 |2d6 |Very high penetration                                    |
| Longbow               |    1d10 |1d6+1d4 |Strong penetration, lower mass than crossbow             |

**If your Prof Bonus is 5 or higher, and you got profession with your weapon, you can choose to go for Save or Risky Damage, before you always go risky!**

## Special Weapons
### Shield

A shield does not deal any damage on Attack! Therefore your Target needs to do an STR-Check $\text{DC} = 10 + \text{Your STR-Mod} - \text{enenies STR-Mod} + \text{Your Prof-Mod} - \text{enenies Prof-Mod}$. If it fails that check it falls to the ground and so gets the on-the-ground-mod what will be discussed in Buffs and debuffs Markdown as soon I wrote that! In case your Enemy tries to parry or block that attack, throw a normal 1d6 for Block or Parry Energy drain!

| Schild           | Typ     | Init | Parry DC | Parry | Block | Stance Damage |
| ---------------- | ------- | ---: | -------: | ----: | ----: | ------------: |
| Buckler          | Special |   +1 |       +1 |    +1 |     0 |             0 |
| Leichter Schild  | Special |    0 |       +2 |    +2 |    +1 |            +1 |
| Mittlerer Schild | Special |   -1 |       +2 |    +2 |    +2 |            +2 |
| Turmschild       | Special |   -3 |       +3 |    +1 |    +3 |            +2 |


### Natural Weapons

As your movement is not blocked or slowed in any way all checks whatfore figners or arms are useful the DC becomes 1 lower. This also applies to dodges.

The weapons themself you find in Classes and Races markdowns