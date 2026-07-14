input_datei = "./World Building/Mechanics/skills and traits/Spell.md"
output_datei = "./World Building/Mechanics/skills and traits/Spells.md"

with open(input_datei, "r", encoding="utf-8") as infile, \
     open(output_datei, "w", encoding="utf-8") as outfile:

    for zeile in infile:
        outfile.write(zeile)
        outfile.write("\n")