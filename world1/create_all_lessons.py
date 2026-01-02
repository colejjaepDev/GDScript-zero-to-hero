#!/usr/bin/env python3
import os

# Base template for all lessons
def create_lesson(filename, lesson_id, title, icon, xp, next_page, content):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - GDScript Quest</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
            color: #e2e8f0;
            min-height: 100vh;
            padding: 20px;
        }}
        .container {{ max-width: 900px; margin: 0 auto; }}
        .nav-bar {{ display: flex; justify-content: space-between; margin-bottom: 30px; }}
        .nav-btn {{
            background: rgba(255,255,255,0.1);
            color: white;
            border: 2px solid rgba(255,255,255,0.3);
            padding: 10px 20px;
            border-radius: 20px;
            cursor: pointer;
            text-decoration: none;
            transition: all 0.3s ease;
        }}
        .nav-btn:hover {{ background: rgba(255,255,255,0.2); }}
        header {{
            background: rgba(16,185,129,0.2);
            border-left: 5px solid #10b981;
            padding: 30px;
            border-radius: 10px;
            margin-bottom: 30px;
        }}
        h1 {{ font-size: 2.5em; margin-bottom: 10px; }}
        .meta {{ display: flex; gap: 15px; margin-top: 15px; }}
        .badge {{
            background: rgba(0,0,0,0.3);
            padding: 8px 15px;
            border-radius: 20px;
            font-size: 0.9em;
        }}
        .content-section {{
            background: rgba(255,255,255,0.05);
            border-radius: 10px;
            padding: 30px;
            margin: 25px 0;
            line-height: 1.8;
        }}
        .content-section h2 {{ color: #10b981; margin-bottom: 20px; font-size: 1.8em; }}
        .content-section h3 {{ color: #60a5fa; margin: 25px 0 15px 0; font-size: 1.4em; }}
        .code-block {{
            background: #1e293b;
            border: 2px solid #334155;
            border-radius: 8px;
            padding: 20px;
            margin: 20px 0;
            font-family: 'Courier New', monospace;
            overflow-x: auto;
        }}
        ul, ol {{ margin-left: 25px; line-height: 1.8; }}
        li {{ margin: 10px 0; }}
        code {{
            background: rgba(16,185,129,0.2);
            padding: 2px 6px;
            border-radius: 3px;
            color: #10b981;
            font-family: 'Courier New', monospace;
        }}
        .tip-box {{
            background: rgba(251,191,36,0.2);
            border-left: 4px solid #fbbf24;
            padding: 20px;
            margin: 25px 0;
            border-radius: 5px;
        }}
        .info-box {{
            background: rgba(59,130,246,0.2);
            border-left: 4px solid #3b82f6;
            padding: 20px;
            margin: 25px 0;
            border-radius: 5px;
        }}
        .btn {{
            background: linear-gradient(135deg, #10b981 0%, #059669 100%);
            color: white;
            border: none;
            padding: 15px 40px;
            border-radius: 25px;
            font-size: 1.1em;
            cursor: pointer;
            transition: all 0.3s ease;
        }}
        .btn:hover {{ transform: scale(1.05); box-shadow: 0 10px 30px rgba(16,185,129,0.3); }}
    </style>
</head>
<body>
    <div class="container">
        <div class="nav-bar">
            <a href="index.html" class="nav-btn">← Back to World 1</a>
            <a href="{next_page}" class="nav-btn" id="nextBtn">Next →</a>
        </div>
        <header>
            <h1>{icon} {title}</h1>
            <div class="meta">
                <span class="badge">⭐ +{xp} XP</span>
                <span class="badge">📖 Lesson</span>
            </div>
        </header>
        {content}
        <div style="text-align: center; margin: 40px 0;">
            <button class="btn" onclick="complete()">✓ Mark Complete & Continue</button>
        </div>
    </div>
    <script>
        function complete() {{
            const progress = JSON.parse(localStorage.getItem('gdscript_quest_progress')) || {{
                xp: 0, completedLessons: [], achievements: []
            }};
            if (!progress.completedLessons.includes('{lesson_id}')) {{
                progress.completedLessons.push('{lesson_id}');
                progress.xp += {xp};
                if ('{lesson_id}' === 'w1_l1' && !progress.achievements.includes('first_steps')) {{
                    progress.achievements.push('first_steps');
                    alert('🎉 Achievement Unlocked: First Steps!');
                }}
                localStorage.setItem('gdscript_quest_progress', JSON.stringify(progress));
            }}
            window.location.href = '{next_page}';
        }}
    </script>
</body>
</html>'''

# Content for all lessons
lessons = [
    {
        'filename': 'lesson1.html',
        'lesson_id': 'w1_l1',
        'title': 'Welcome to GDScript',
        'icon': '🎯',
        'xp': 50,
        'next': 'lesson2.html',
        'content': '''
<div class="content-section">
    <h2>🎮 What is GDScript?</h2>
    <p>Welcome! Since you know Python, you're going to LOVE GDScript. It was designed to look and feel similar to Python, but optimized for game development!</p>
    
    <h3>Python vs GDScript - Quick Comparison</h3>
    <div class="code-block">
<pre># Python
health = 100
def attack(damage):
    return damage * 2

# GDScript
var health = 100
func attack(damage):
    return damage * 2
</pre>
    </div>

    <div class="info-box">
        <strong>💡 Key Difference:</strong> GDScript requires <code>var</code> for variables and <code>func</code> for functions. Everything else feels like Python!
    </div>

    <h3>Your First GDScript Code</h3>
    <div class="code-block">
<pre>extends Node

# This runs once when the node enters the scene
func _ready():
    print("Hello, Godot!")
    var player_name = "Hero"
    print("Welcome, ", player_name, "!")
</pre>
    </div>

    <h3>Key Concepts</h3>
    <ul>
        <li><code>extends Node</code> - Inherit from Godot's Node class</li>
        <li><code>func _ready():</code> - Runs once at start (like __init__ in Python)</li>
        <li><code>func _process(delta):</code> - Runs every frame (60 times/second!)</li>
        <li><code>var</code> - Declare variables (required in GDScript)</li>
    </ul>

    <div class="tip-box">
        <strong>🎯 Game Dev Tip:</strong> The <code>delta</code> parameter in _process() represents time since last frame. Use it for smooth, frame-rate independent movement: <code>position += velocity * delta</code>
    </div>

    <h3>Built-in Game Types</h3>
    <p>GDScript has special types for game development:</p>
    <ul>
        <li><strong>Vector2:</strong> 2D positions/directions <code>Vector2(x, y)</code></li>
        <li><strong>Vector3:</strong> 3D positions/directions <code>Vector3(x, y, z)</code></li>
        <li><strong>Color:</strong> Colors <code>Color(r, g, b, a)</code></li>
    </ul>

    <div class="code-block">
<pre>var player_position = Vector2(100, 200)
var velocity = Vector2(5, 0)
var color = Color(1.0, 0.5, 0.0)  # Orange
</pre>
    </div>
</div>
'''
    },
    {
        'filename': 'lesson2.html',
        'lesson_id': 'w1_l2',
        'title': 'Variables & Data Types',
        'icon': '📦',
        'xp': 75,
        'next': 'lab1.html',
        'content': '''
<div class="content-section">
    <h2>📦 Variables in GDScript</h2>
    <p>You MUST use <code>var</code> or <code>const</code> to declare variables in GDScript.</p>

    <div class="code-block">
<pre># Basic variable
var health = 100

# Type-hinted variable (recommended!)
var health: int = 100
var speed: float = 5.5
var name: String = "Hero"

# Constant (cannot change)
const MAX_HEALTH: int = 100
const GRAVITY: float = 980.0
</pre>
    </div>

    <h3>Basic Data Types</h3>
    <ul>
        <li><strong>int:</strong> Whole numbers <code>1, 42, -10</code></li>
        <li><strong>float:</strong> Decimals <code>3.14, -0.5, 2.0</code></li>
        <li><strong>String:</strong> Text <code>"Hello", 'World'</code></li>
        <li><strong>bool:</strong> <code>true</code> or <code>false</code> (lowercase!)</li>
    </ul>

    <div class="info-box">
        <strong>⚠️ Python Note:</strong> In GDScript, booleans are <code>true</code> and <code>false</code> (lowercase), not <code>True</code> and <code>False</code>.
    </div>

    <h3>Game-Specific Types</h3>
    <div class="code-block">
<pre># 2D vector for positions, directions
var position: Vector2 = Vector2(100, 200)
var velocity: Vector2 = Vector2(5, -3)

# 3D vector
var position_3d: Vector3 = Vector3(10, 0, 20)

# Colors (RGBA, values 0.0 to 1.0)
var player_color: Color = Color(1.0, 0.0, 0.0)  # Red
var transparent_blue: Color = Color(0.0, 0.0, 1.0, 0.5)
</pre>
    </div>

    <h3>Type Conversion</h3>
    <div class="code-block">
<pre>var num_string = "42"
var num = int(num_string)  # Convert to int

var pi = 3.14
var pi_int = int(pi)  # 3 (truncates)

var score = 100
var score_text = str(score)  # "100"
</pre>
    </div>

    <h3>Variable Scope</h3>
    <div class="code-block">
<pre>extends Node

# Class-level variable (accessible everywhere in script)
var health: int = 100

func take_damage(amount: int):
    # Local variable (only in this function)
    var damage_multiplier = 1.5
    health -= int(amount * damage_multiplier)
    
func _ready():
    print(health)  # Works
    # print(damage_multiplier)  # ERROR - not in scope
</pre>
    </div>

    <div class="tip-box">
        <strong>🎯 Best Practice:</strong> Always use type hints! They help catch errors early and make your code more readable: <code>var speed: float = 5.0</code>
    </div>
</div>
'''
    },
    {
        'filename': 'lesson3.html',
        'lesson_id': 'w1_l3',
        'title': 'Functions & Methods',
        'icon': '🎮',
        'xp': 75,
        'next': 'lesson4.html',
        'content': '''
<div class="content-section">
    <h2>🎮 Functions in GDScript</h2>
    <p>Functions in GDScript use <code>func</code> instead of Python's <code>def</code>.</p>

    <h3>Basic Function Syntax</h3>
    <div class="code-block">
<pre># Simple function
func say_hello():
    print("Hello!")

# Function with parameters
func greet_player(name: String):
    print("Welcome, ", name, "!")

# Function that returns a value
func add(a: int, b: int) -> int:
    return a + b

# Function with default parameters
func heal(amount: int = 10):
    health += amount
</pre>
    </div>

    <h3>Godot's Built-in Functions</h3>
    <p>Godot provides special functions that run automatically:</p>

    <div class="code-block">
<pre>extends Node

# Runs ONCE when node enters the scene tree
func _ready():
    print("Node is ready!")
    setup_game()

# Runs EVERY FRAME (60 times per second)
func _process(delta: float):
    # delta = time since last frame (usually ~0.016)
    update_game(delta)

# Runs at FIXED intervals (good for physics)
func _physics_process(delta: float):
    # Use this for movement and physics
    move_player(delta)
</pre>
    </div>

    <div class="info-box">
        <strong>💡 Understanding Delta:</strong> <code>delta</code> is the time (in seconds) since the last frame. Use it to make movement frame-rate independent:<br>
        <code>position += velocity * delta</code>
    </div>

    <h3>Real Game Example</h3>
    <div class="code-block">
<pre>extends CharacterBody2D

var health: int = 100
var speed: float = 200.0

func _ready():
    print("Player spawned with ", health, " HP")

func _process(delta: float):
    handle_movement(delta)
    check_health()

func handle_movement(delta: float):
    var direction = Vector2.ZERO
    
    if Input.is_action_pressed("move_right"):
        direction.x += 1
    if Input.is_action_pressed("move_left"):
        direction.x -= 1
    
    velocity = direction * speed
    move_and_slide()

func take_damage(amount: int):
    health -= amount
    print("Ouch! Health: ", health)
    
    if health <= 0:
        die()

func die():
    print("Game Over!")
    queue_free()  # Remove this node from scene

func heal(amount: int) -> int:
    var old_health = health
    health = min(health + amount, 100)  # Cap at 100
    return health - old_health  # Return actual amount healed
</pre>
    </div>

    <h3>Function Return Types</h3>
    <div class="code-block">
<pre># Explicit return type
func calculate_damage(base: int, multiplier: float) -> int:
    return int(base * multiplier)

# Returns Vector2
func get_direction() -> Vector2:
    return Vector2(1, 0)

# No return value (void)
func print_score():
    print("Score: ", score)
</pre>
    </div>

    <div class="tip-box">
        <strong>🎯 Best Practice:</strong> Use type hints for parameters and return values. It prevents bugs and makes your code self-documenting!
    </div>
</div>
'''
    }
]

# Create all lesson files
for lesson in lessons:
    html = create_lesson(
        lesson['filename'],
        lesson['lesson_id'],
        lesson['title'],
        lesson['icon'],
        lesson['xp'],
        lesson['next'],
        lesson['content']
    )
    with open(f'/home/claude/gdscript-quest/world1/{lesson["filename"]}', 'w') as f:
        f.write(html)

print("Created 3 comprehensive lessons!")
