# Continue creating more lessons

lessons_part2 = [
    ('lesson4.html', 'w1_l4', 'Conditionals & Logic', '⚡', 75, 'lab2.html', '''
<div class="content-section">
    <h2>⚡ Control Flow & Conditionals</h2>
    <p>Make decisions in your game code!</p>

    <h3>If Statements</h3>
    <div class="code-block">
<pre>var health = 50

if health < 20:
    print("Critical health!")
elif health < 50:
    print("Low health")
else:
    print("Healthy")
</pre>
    </div>

    <h3>Comparison Operators</h3>
    <ul>
        <li><code>==</code> Equal to</li>
        <li><code>!=</code> Not equal to</li>
        <li><code>&lt;</code> Less than</li>
        <li><code>&gt;</code> Greater than</li>
        <li><code>&lt;=</code> Less than or equal</li>
        <li><code>&gt;=</code> Greater than or equal</li>
    </ul>

    <h3>Logical Operators</h3>
    <div class="code-block">
<pre># and, or, not (same as Python!)
if health > 0 and has_weapon:
    attack_enemy()

if is_invincible or health > 50:
    take_risk()

if not is_dead:
    keep_playing()
</pre>
    </div>

    <h3>Match Statement (like switch)</h3>
    <p>GDScript has a powerful match statement:</p>
    <div class="code-block">
<pre>var state = "running"

match state:
    "idle":
        play_idle_animation()
    "running":
        play_run_animation()
    "jumping":
        play_jump_animation()
    _:  # default case
        print("Unknown state")
</pre>
    </div>

    <h3>Ternary Operator</h3>
    <div class="code-block">
<pre># condition if true else false
var damage = 20 if has_power_up else 10
var color = Color.GREEN if health > 50 else Color.RED
</pre>
    </div>

    <h3>Game Example: Enemy AI</h3>
    <div class="code-block">
<pre>func update_enemy_ai(player_distance: float):
    if player_distance < 50:
        # Player is very close
        attack_player()
    elif player_distance < 200:
        # Player is nearby
        move_towards_player()
    else:
        # Player is far
        patrol()
</pre>
    </div>
</div>
'''),
    ('lesson5.html', 'w1_l5', 'Loops & Iteration', '🔄', 75, 'lesson6.html', '''
<div class="content-section">
    <h2>🔄 Loops in GDScript</h2>
    
    <h3>For Loops</h3>
    <div class="code-block">
<pre># Loop through range
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# Loop through range with start/end
for i in range(2, 7):
    print(i)  # 2, 3, 4, 5, 6

# Loop with step
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8
</pre>
    </div>

    <h3>While Loops</h3>
    <div class="code-block">
<pre>var count = 0
while count < 5:
    print(count)
    count += 1
</pre>
    </div>

    <h3>Loop Control</h3>
    <div class="code-block">
<pre># break - exit loop early
for i in range(10):
    if i == 5:
        break
    print(i)  # 0,1,2,3,4

# continue - skip to next iteration
for i in range(5):
    if i == 2:
        continue
    print(i)  # 0,1,3,4
</pre>
    </div>

    <h3>Looping Through Arrays</h3>
    <div class="code-block">
<pre>var enemies = ["Goblin", "Orc", "Dragon"]

# Loop through items
for enemy in enemies:
    print("Fighting ", enemy)

# Loop with index
for i in range(enemies.size()):
    print(i, ": ", enemies[i])
</pre>
    </div>

    <h3>Game Examples</h3>
    <div class="code-block">
<pre># Spawn multiple enemies
for i in range(5):
    spawn_enemy(Vector2(i * 100, 0))

# Update all enemies
for enemy in enemies:
    enemy.update_ai(delta)

# Find nearest enemy
var nearest_dist = 999999
for enemy in enemies:
    var dist = position.distance_to(enemy.position)
    if dist < nearest_dist:
        nearest_dist = dist
</pre>
    </div>
</div>
'''),
    ('lesson6.html', 'w1_l6', 'Arrays & Dictionaries', '📚', 75, 'lab3.html', '''
<div class="content-section">
    <h2>📚 Data Structures</h2>
    
    <h3>Arrays (Lists)</h3>
    <div class="code-block">
<pre># Create array
var items = ["Sword", "Shield", "Potion"]
var numbers = [1, 2, 3, 4, 5]
var mixed = [1, "text", true, Vector2(0, 0)]

# Type-hinted array
var enemies: Array[String] = ["Goblin", "Orc"]
</pre>
    </div>

    <h3>Array Methods</h3>
    <div class="code-block">
<pre>var inventory = []

# Add items
inventory.append("Sword")  # Add to end
inventory.push_back("Shield")  # Same as append
inventory.insert(0, "Potion")  # Insert at index

# Remove items
inventory.erase("Sword")  # Remove by value
inventory.pop_back()  # Remove last
inventory.pop_front()  # Remove first

# Access
print(inventory[0])  # First item
print(inventory[-1])  # Last item
print(inventory.size())  # Length

# Check if exists
if "Sword" in inventory:
    print("Has sword!")
</pre>
    </div>

    <h3>Dictionaries</h3>
    <div class="code-block">
<pre># Create dictionary
var player_stats = {
    "name": "Hero",
    "health": 100,
    "level": 5,
    "inventory": ["Sword", "Potion"]
}

# Access values
print(player_stats["name"])
print(player_stats.health)  # Also works!

# Add/modify
player_stats["mana"] = 50
player_stats.health = 80

# Check if key exists
if "name" in player_stats:
    print(player_stats["name"])

# Get keys and values
for key in player_stats.keys():
    print(key, ": ", player_stats[key])
</pre>
    </div>

    <h3>Nested Structures</h3>
    <div class="code-block">
<pre>var game_data = {
    "player": {
        "name": "Hero",
        "stats": {
            "health": 100,
            "mana": 50
        },
        "inventory": ["Sword", "Potion"]
    },
    "enemies": [
        {"name": "Goblin", "health": 30},
        {"name": "Orc", "health": 50}
    ]
}

# Access nested data
print(game_data["player"]["stats"]["health"])
print(game_data.enemies[0].name)
</pre>
    </div>

    <h3>Practical Examples</h3>
    <div class="code-block">
<pre># Inventory system
var inventory = []

func add_item(item: String):
    inventory.append(item)
    print("Added ", item)

func has_item(item: String) -> bool:
    return item in inventory

# Quest system
var quests = {
    "quest_1": {"name": "Slay Goblin", "complete": false},
    "quest_2": {"name": "Find Sword", "complete": true}
}

func complete_quest(quest_id: String):
    if quest_id in quests:
        quests[quest_id]["complete"] = true
</pre>
    </div>
</div>
''')
]

def create_lesson_html(filename, lesson_id, title, icon, xp, next_page, content):
    return f'''<!DOCTYPE html>
<html><head><meta charset="UTF-8"><title>{title}</title>
<style>*{{margin:0;padding:0;box-sizing:border-box}}body{{font-family:'Segoe UI',sans-serif;background:linear-gradient(135deg,#1e293b 0%,#0f172a 100%);color:#e2e8f0;min-height:100vh;padding:20px}}.container{{max-width:900px;margin:0 auto}}.nav-bar{{display:flex;justify-content:space-between;margin-bottom:30px}}.nav-btn{{background:rgba(255,255,255,0.1);color:white;border:2px solid rgba(255,255,255,0.3);padding:10px 20px;border-radius:20px;cursor:pointer;text-decoration:none;transition:all 0.3s ease}}.nav-btn:hover{{background:rgba(255,255,255,0.2)}}header{{background:rgba(16,185,129,0.2);border-left:5px solid #10b981;padding:30px;border-radius:10px;margin-bottom:30px}}h1{{font-size:2.5em;margin-bottom:10px}}.content-section{{background:rgba(255,255,255,0.05);border-radius:10px;padding:30px;margin:25px 0;line-height:1.8}}.content-section h2{{color:#10b981;margin-bottom:20px;font-size:1.8em}}.content-section h3{{color:#60a5fa;margin:25px 0 15px 0;font-size:1.4em}}.code-block{{background:#1e293b;border:2px solid #334155;border-radius:8px;padding:20px;margin:20px 0;font-family:'Courier New',monospace;overflow-x:auto}}ul,ol{{margin-left:25px;line-height:1.8}}li{{margin:10px 0}}code{{background:rgba(16,185,129,0.2);padding:2px 6px;border-radius:3px;color:#10b981;font-family:'Courier New',monospace}}.btn{{background:linear-gradient(135deg,#10b981 0%,#059669 100%);color:white;border:none;padding:15px 40px;border-radius:25px;font-size:1.1em;cursor:pointer;transition:all 0.3s ease}}.btn:hover{{transform:scale(1.05);box-shadow:0 10px 30px rgba(16,185,129,0.3)}}</style>
</head><body><div class="container">
<div class="nav-bar"><a href="index.html" class="nav-btn">← World 1</a><a href="{next_page}" class="nav-btn">Next →</a></div>
<header><h1>{icon} {title}</h1><p>+{xp} XP</p></header>
{content}
<div style="text-align:center;margin:40px 0"><button class="btn" onclick="complete()">✓ Mark Complete</button></div>
</div><script>function complete(){{const p=JSON.parse(localStorage.getItem('gdscript_quest_progress'))||{{xp:0,completedLessons:[],achievements:[]}};if(!p.completedLessons.includes('{lesson_id}')){{p.completedLessons.push('{lesson_id}');p.xp+={xp};localStorage.setItem('gdscript_quest_progress',JSON.stringify(p))}}window.location.href='{next_page}'}}</script></body></html>'''

for lesson_data in lessons_part2:
    html = create_lesson_html(*lesson_data)
    with open(lesson_data[0], 'w') as f:
        f.write(html)

print(f"Created {len(lessons_part2)} more lessons!")
