# Toril Cosmology: Biomes, Realmspaces & Relationships

```mermaid
flowchart TB

  FarRealm["Far Realm<br/>incomprehensible, outside"]

  subgraph Multiversum["Multiverse"]

    subgraph Material["Material Plane"]

      subgraph SonnenSys["Solar System"]

        AndereWelten["Other Planets/Moons<br/>own Crystal Spheres"]

        subgraph Toril["Toril"]

          subgraph Chaos["Elemental Chaos"]

            Kern["Planetary Core<br/>Origin, unstructured"]

          end

          subgraph ElemBiome["Elemental Biomes"]

            Wasser["Water Biome<br/>Ocean, Marid"]

            Luft["Air Biome<br/>Sky, Djinn"]

            Erde["Earth Biome<br/>Rock, Dao, Xorn"]

            Feuer["Fire Biome<br/>Mantle, Efreet"]

            Underdark["Underdark<br/>Absence of Stone"]

          end

          subgraph Grenz["Para-Elemental Border Zones"]

            Eis["Ice: Water+Air"]

            Ooze["Ooze: Earth+Water"]

            Rauch["Smoke: Fire+Air"]

            Magma["Magma: Fire+Earth"]

          end

          subgraph HimmelBiom["Sky Biome (High Mountains)"]

            Celestia["Mount Celestia<br/>Good Gods, Devas"]

          end

          subgraph Riss["The Rift (Hellmouth)"]

            Hoellen["Nine Hells<br/>Baatezu, near the surface"]

            Limbo["Limbo<br/>Slaadi"]

            Pandemonium["Pandemonium<br/>Madness"]

            Abyss["Abyss<br/>Tanar'ri, deepest layer"]

          end

          Gehenna["Gehenna<br/>Yugoloth Mercenary Zone"]

          Carceri["Carceri<br/>Prison Island"]

          Acheron["Acheron<br/>Cursed Battlefield"]

          subgraph FeyBiom["Feywild Biome"]

            Beastlands["Beastlands Region<br/>Beast Totems"]

            Arborea["Arborea Forest<br/>Eladrin, Elven Court"]

          end

          Utopie["Arcadia Biome<br/>Bytopia+Elysium+Arcadia<br/>Archons"]

          Riesen["Ysgard Giants<br/>Real Threat"]

          Mechanus["Mechanus Ruined City<br/>Modrons, possibly abandoned"]

        end

      end

      FugueHades["Fugue Plane / Hades<br/>Soul Gathering Point, Wall of the Faithless"]

    end

    subgraph NexusZone["Outlands / Sigil"]

      SigilStadt["Sigil<br/>Lady of Pain"]

      Weisheit["Realmspace of a<br/>Goddess of Wisdom"]

    end

    subgraph Realmspaces["Realmspaces (Portal Enclaves)"]

      Corellon["Corellon"]

      Malar["Malar"]

      Walhalla["Valhalla<br/>Ysgard Afterlife"]

    end

    Astral["Astral Plane<br/>connects everything"]

    Ather["Ethereal Plane<br/>Adhesive Layer"]

  end

  %% Containment/Environment

  FarRealm -. surrounds .-> Multiversum

  %% Elemental Chaos manifests

  Kern -. breaks through .-> Eis

  Kern -. breaks through .-> Ooze

  Kern -. breaks through .-> Rauch

  Kern -. breaks through .-> Magma

  %% Conflict

  Hoellen <-. Blood War .-> Abyss

  %% Soul Journey

  Toril -. Death .-> FugueHades

  FugueHades -. Believers .-> Celestia

  FugueHades -. Fallen Warriors .-> Walhalla

  %% Portal Enclaves

  Arborea -. Portal .-> Corellon

  Beastlands -. Portal .-> Malar

  %% Sigil as Nexus

  Riss -. Portal .-> SigilStadt

  Celestia -. Portal .-> SigilStadt

  Toril -. Portal .-> SigilStadt

  SigilStadt -. houses .-> Weisheit

  %% Astral Plane connects Realmspaces

  Astral -. connects .-> Realmspaces

  Astral -. connects .-> NexusZone

  Astral -. connects .-> FugueHades

  %% Travel Between Worlds

  Toril <-. Astral Plane/Spheres .-> AndereWelten

  %% Ethereal Plane as Adjacent Layer

  Ather -. adjacent .-> Toril

  %% Subgraph Styling

  style FarRealm fill:#1a1a2e,color:#eee,stroke:#000

  style Multiversum fill:#0d0d0d,color:#eee,stroke:#444

  style Material fill:#12121f,color:#eee,stroke:#555

  style SonnenSys fill:#161629,color:#eee,stroke:#666

  style Toril fill:#1c2b1c,color:#eee,stroke:#4a7a4a

  style Chaos fill:#3a1c1c,color:#eee,stroke:#a83232

  style ElemBiome fill:#1c3a3a,color:#eee,stroke:#2fa8a8

  style Grenz fill:#2a2a1c,color:#eee,stroke:#a89b32

  style HimmelBiom fill:#3a3a1c,color:#eee,stroke:#e0d060

  style Riss fill:#3a1414,color:#eee,stroke:#c02020

  style FeyBiom fill:#1c3a20,color:#eee,stroke:#3fbf5f

  style NexusZone fill:#2a1c3a,color:#eee,stroke:#9a4fc0

  style Realmspaces fill:#1c2a3a,color:#eee,stroke:#4f8fc0

  style Kern fill:#a83232,color:#fff,stroke:#000

  style Celestia fill:#e0d060,color:#000,stroke:#000

  style Hoellen fill:#c02020,color:#fff,stroke:#000

  style Abyss fill:#6a0dad,color:#fff,stroke:#000

  style Limbo fill:#8a3fc0,color:#fff,stroke:#000

  style Pandemonium fill:#7a2fa0,color:#fff,stroke:#000

  style SigilStadt fill:#9a4fc0,color:#fff,stroke:#000

  style FugueHades fill:#555555,color:#fff,stroke:#000

  style Gehenna fill:#a05a1c,color:#fff,stroke:#000

  style Carceri fill:#444444,color:#fff,stroke:#000

  style Acheron fill:#5a2a1c,color:#fff,stroke:#000

  style Riesen fill:#2f4f6f,color:#fff,stroke:#000

  style Mechanus fill:#3a3a3a,color:#eee,stroke:#888

  style Utopie fill:#3fbf5f,color:#000,stroke:#000

  style Wasser fill:#1f6fa8,color:#fff,stroke:#000

  style Luft fill:#a8d0e0,color:#000,stroke:#000

  style Erde fill:#6f4f2f,color:#fff,stroke:#000

  style Feuer fill:#c04020,color:#fff,stroke:#000

  style Underdark fill:#2a2a3a,color:#eee,stroke:#555

  style Astral fill:#4f4fa8,color:#fff,stroke:#000

  style Ather fill:#7f7faf,color:#fff,stroke:#000
```

## Key

* **Full border (subgraph)** = Containment: X is physically/structurally within Y
* **Dotted arrows** = Relationship, travel route, or conflict between locations that are not contained within one another
* **Rift** = Combined Limbo/Pandemonium/Abyss/Nine Hells structure, layered according to depth


## Ideas

### Mechanus

- Mechanus becomes a big city, an old empire or something. Of course the size will reduce drastically.

**Tasks**

- Ruin or still active city?

### Archadia

- This will become a biome class, without bound to fix types. Basically this appears if a land is completly dominated, by fairies or any power all animals  become calm and friendly and it becomes cultivated.
- Due to the factor of cultivation this is where many population settle.

### Celestia

- Celestia will become a realmspace on a high mountain. On ascending the mountain in the material world you enter the realmspace and you exceed the mountains actual hight in the material plane.
  
### Bytopia

- Becuase I like the idea of this scene, this biome is born during spell pleague (I did not found any timeline for any event on bytopia, so this should be fine). The spell pleague bend the mountains to overhang far, creating another ground to stay on, just in the sky. 
- Also the pleague did create an phenomina similar to *Faerzress*, creating a surrounding spell you can't resist, casting some kind of levitate on everone and everything make you stick to the skyborn ground in a way gravity would.

### Elysium

- A vast forested plateau (Amoria) under the normal sun, cut by a deep canyon whose terraced walls and waterfalls form Eronia. The canyon floor holds mist-shrouded marshes with mesa-islands (Belierin), and far below lies a bioluminescent freshwater sea with the Isles of the Blessed (Thalasia).
- The river Oceanus works as a closed water cycle. It rises from artesian springs out of the underground sea, braids across the plateau, cascades down the walls, and drains back through karst sinkholes. The draining keeps the sea fresh, and the cave openings double as portals.
- The mineral-rich, calming springs and thermal pools explain the "troubles wash away" effect, while geysers host the phoenixes and terraced walls grow the famous pears.

### Beastlands

* A vast, densely forested mountain range in a fey-touched wilderness, where nearly every natural animal (and giant variants) can speak and reason. Legend holds that the Spellplague awakened them, and the forest's mycelial network and Yggdrasil turned that surge into something benevolent.
- The three layers are stacked by elevation. **Krigala** is the sunlit highland and plateau forest with no shade, so it feels like endless noon. **Brux** is the deep valleys in permanent dusk, lit by low red light from both valley ends and reflected off the cliffs. **Karasuthra** is the cave network inside the mountains, an eternal night sky of glowworms and drifting luminous spores whose random movement defies mapping, with underground forests of giant fungi and root curtains.
- Weather is regional, as in real mountains, so desert can sit beside snow through rain shadows and altitude. The mortai are sentient cloud-spirits born from orographic clouds, who guard their local weather with help from the birds. Hollow trees and cave mouths serve as portals, and the Oceanus runs straight across the high plateau.

### Arborea

- A vast, larger-than-life region of the Fey where emotion shapes the land itself. The nature spirits of every forest, mountain, stream, and cloud mirror the moods of those who enter, taking on their likeness, so joy makes the land bloom and rage brings storms of lightning and hail. Pollen, fruit, and music on the wind make visitors passionate, reckless, and reluctant to leave, and staying too long can leave a lasting craving. Spirits and courts also enforce oaths, and magic requires small offerings to them.
- The land splits into three regions. **Arvandor** is a redwood-scale forest and mountain realm of glades, orchards, and firefly constellations, ruled by Fey courts and led by the Faerie Queen's ever-moving Court of Stars. **Aquallor** is an emerald sea, only ankle-to-knee deep for miles, broken by sudden blue holes leading to sunken courts. **Mithardir** is a cool white desert of gypsum dust and lightning-charged storms, the ruins of a dead Fey court whose emotions faded, making it the Fell-touched echo of the vibrant Fey above.

### Ysgard

- The Norse realms become real places in the far north, as in the myths.
- **Asgard** remains as the divine realm of the Norse pantheon and serves as the afterlife, with Valhalla as its hall of fallen heroes. It is reached via the **Bifrost**, seen in the world as the aurora borealis.


### Abyss

- The Abyss will be a giant rift opening to a big realm even under the underdark. It is home to two fractions of celestials: The Demons and the Devils. Since the very beginning the devils make contracts with humanoids. This intelligence based idea is not liked by all celestials like the demons who prefer the direct force to get their will. So there is a war inside the abyss resulting in different fractions and teretories. The Devils got a few top levels, they call the Hells, while the rest of the abyss belongs to the demons. Between Hell and True Abyss you find all the other Evil Planes you find between Nine Hells and Abyss in great wheel.

### Limbo

### Pandemonium

As Pandemonium is the same core idea as the abyssal planes just on another usecase, it will be dropped completly. If you really want to force it to be a specific place it could be just another layer in abyss

### Acheron

Acheron basically is the idea of fighting for fun as a complete plane what is little over the top. So I drop it completly, but if some campaignes need the idea of an endless war I would call some kingdoms an material plane to are engaged in an endless war noone knows the reason for anymore. And due to the Spell Pleague the wast land they fight on, make your wound heal as soon as you are lethally hittet.

### Outlands

The Outlands will be a city or a kingdom on the material plane where many Ley lines conflict and therefore the magic for traveling is really potent there.

### Fey Wilds

The Fey will remain like it is and additional some bioms including the Shadowfell.

