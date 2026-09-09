As already hovered on, the levels in my system are representation of skill and might. Because of this the levels mean actual progress in experience, so fighting always the same or unskilled entities grant you less XP. 

So normal XP you find in Monster Manual you split for each group member based on how active they were in fight (if all are about the same: $\frac{1}{\text{Number of Players}^{0.75}}$)

This means:

|Number of Players | XP granted to each player (mult)|
|-|-|
2 | 0.6
3 | 0.4
4 | 0.35
5 | 0.3
6 | 0.26

---

This is multiplied again with the knowledge of each character

## XP Multiplier

| Frequency ↓ / Time since last encounter → | Immediate | Short | Medium | Long  | Very long |
| ----------------------------------------- | --------- | ----- | ------ | ----- | --------- |
| **First encounter** (1×)                  | 1.2×      | 1.2×  | 1.2×   | 1.2×  | 1.2×      |
| **Rare** (2–5×)                           | 1.0×      | 1.0×  | 1.0×   | 1.0×  | 1.0×      |
| **Repeated** (6–15×)                      | 0.80×     | 0.85× | 0.95×  | 1.0×  | 1.0×      |
| **Regular** (16–50×)                      | 0.50×     | 0.60× | 0.75×  | 0.90× | 1.0×      |
| **Farmed** (50×+)                         | 0.15×     | 0.20× | 0.35×  | 0.60× | 0.85×     |

---

This now sounds like a lot of work, but actually it's not as most members are pretty similar.

# Levels

$$XP_{total}(n) = 9.22 \cdot 100 \cdot \dfrac{1.28^{,n-1}-1}{1.28-1}$$

| Level | Tier         | Cumulative XP (total) | XP Delta (to next level) |
| ----- | ------------ | --------------------: | -----------------------: |
| 1     | Beginner     |                     0 |                        922 |
| 2     | Beginner     |                   922 |                   1,180    |
| 3     | Beginner     |                 2,102 |                   1,511  |
| 4     | Beginner     |                 3,613 |                   1,933  |
| 5     | Beginner     |                 5,546 |                   2,472  |
| 6     | Intermediate |                 8,018 |                   3,161  |
| 7     | Intermediate |                11,179 |                   4,052  |
| 8     | Intermediate |                15,231 |                   5,187  |
| 9     | Intermediate |                20,418 |                   6,639  |
| 10    | Intermediate |                27,057 |                    8,497 |
| 11    | Advanced     |                35,554 |                   10,876  |
| 12    | Advanced     |                46,430 |                   13,924 |
| 13    | Advanced     |                60,354 |                   17,821 |
| 14    | Advanced     |                78,175 |                   22,810 |
| 15    | Advanced     |               100,985 |                   29,198 |
| 16    | Expert       |               130,183 |                   37,373 |
| 17    | Expert       |               167,556 |                   47,839 |
| 18    | Expert       |               215,395 |                   61,232 |
| 19    | Expert       |               276,627 |                   78,373 |
| 20    | Master       |               355,000 |                    - |
