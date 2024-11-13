
---

# Starborn Exodus: Legend of The Godslayer - Mini Project Submission - 23FE10CSE00664

## Introduction

The **Starborn Exodus: Legend of The Godslayer** is a **text-based RPG** built using **Object-Oriented Programming (OOP)** principles in Python. The game follows the journey of a fallen god, known as the *starborn*, seeking revenge against those who betrayed them. The player takes on the role of this god as they travel across different locations, complete quests, and make decisions that affect the storyline.

In this documentation, I will detail the use of **Encapsulation**, **Inheritance**, **Polymorphism**, and **Abstraction** in the design and implementation of the game, as well as explain the core mechanics that power the game’s progression.

## Game Overview

The game revolves around a protagonist, the last of the *starborn*, who was cast out and betrayed by the gods. The player’s journey is one of vengeance and self-discovery, exploring locations, completing quests, and engaging in battles with enemies. The game features different locations such as the **Bar**, **Temple**, **Ruins**, and **Village**, each offering unique quests and challenges. 

### Core Gameplay Features:
- **Dynamic quests**: Players embark on various quests, each with its own story and outcome.
- **Combat system**: Players engage in turn-based combat against enemies.
- **Morality system**: Players' decisions influence their morality, shaping their path and interactions.
- **Exploration**: Players can explore different locations that lead to different encounters and quests.

## OOP Concepts Used

### 1. **Encapsulation**

Encapsulation refers to the bundling of data (attributes) and methods (functions) that operate on the data within one class. This allows for better organization and protection of the data. In my project, the **Player** class encapsulates all player-related data (such as health, strength, and experience points) and the methods used to interact with that data (like leveling up, gaining XP, and managing inventory).

For example, the player’s stats are stored as attributes within the `Player` class:

```python
class Player:
    def __init__(self, name, gender, level, xp, health, strength, stealth, morality):
        self.name = name
        self.gender = gender
        self.level = level
        self.xp = xp
        self.health = health
        self.max_health = health
        self.strength = strength
        self.stealth = stealth
        self.morality = morality
        self.inventory = {}
```

In this example, the player’s **name**, **health**, **strength**, and **inventory** are encapsulated within the `Player` class. This ensures that all related methods (such as `gain_xp()` and `level_up()`) can safely access and modify these attributes.

### 2. **Inheritance**

Inheritance is a mechanism that allows one class to inherit attributes and methods from another class. This promotes code reuse and extends functionality without modifying the original class. In the game, classes like **Player** and **Villager** inherit common attributes and methods from a generic `Character` class (for example, methods for taking damage).

For instance, the **Player** class inherits the basic functionalities of a **Character** class:

```python
class Character:
    def __init__(self, name, health, strength, stealth):
        self.name = name
        self.health = health
        self.strength = strength
        self.stealth = stealth

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.die()

    def die(self):
        print(f"{self.name} has perished!")
```

The **Player** class inherits the `take_damage()` method from **Character** to reduce code duplication. Other classes can be built in the same way, maintaining a DRY (Don't Repeat Yourself) approach.

### 3. **Polymorphism**

Polymorphism allows different classes to implement the same method in different ways. It’s particularly useful for methods that have the same name but differ in behavior based on the class instance. In the context of the game, combat actions, like taking damage or dying, may be implemented differently for the player and other characters.

For example:

```python
class Villager(Character):
    def __init__(self, name, health, strength, stealth):
        super().__init__(name, health, strength, stealth)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has been defeated.")
```

In this case, the **Villager** class inherits from **Character** and overrides the `take_damage()` method to provide specific dialogue when they die. This is an example of polymorphism in action, allowing the same method (`take_damage()`) to have different behaviors based on the object’s class.

### 4. **Abstraction**

Abstraction simplifies complex systems by hiding implementation details and showing only essential features. In the context of this game, abstraction is used in handling quests and combat. For example, when the player encounters a quest, they do not need to know the internal logic of how the quest is managed—just the high-level interaction and result are presented.

For instance, quests are abstracted into specific quest classes:

```python
class Quest:
    def start(self):
        raise NotImplementedError("Subclasses should implement this method")

class BarQuest(Quest):
    def start(self):
        print("Starting the Bar Quest...")
```

Here, the `Quest` class defines a blueprint for quests, and subclasses like `BarQuest` implement specific behaviors. The player interacts with quests at a high level, without worrying about how each quest’s logic is structured internally.

## Key Game Mechanics

### **Player Class**

The **Player** class holds essential player information, including attributes (e.g., name, health, strength) and methods for managing experience, leveling up, and interacting with the game world. Methods like `gain_xp()` allow the player to gain experience for completing tasks and quests.

```python
def gain_xp(self, amount):
    self.xp += amount
    if self.xp >= 100:
        self.level_up()

def level_up(self):
    self.level += 1
    self.xp = 0
    self.max_health += 10
    self.strength += 5
```

### **Villager and NPC Interactions**

The **Villager** class (and other NPCs) serves as an example of how characters are structured. They interact with the player, either providing quests or affecting the player’s morality based on the choices made during encounters.

### **Combat System**

Combat is turn-based, with the player using their strength or stealth to defeat enemies. The player can choose to fight or avoid conflict depending on their attributes. This is managed through methods that check the player’s attributes (like **strength**) and determine success or failure.

```python
def attack_enemy(self, enemy):
    damage_dealt = self.strength * random.randint(1, 3)
    enemy.take_damage(damage_dealt)
```

### **Quest System**

The **Quest** system is broken down into different types, each representing a unique experience. For example, the **BarQuest** might involve negotiation and combat, while the **TempleQuest** might focus on introspection and moral choices.

```python
class BarQuest(Quest):
    def start(self):
        print("You meet a shady figure in the bar who needs your help.")
        self.handle_quest()
```

### **XP and Leveling**

Players gain **XP** by completing quests and defeating enemies. Once enough XP is accumulated, the player **levels up**, gaining additional strength and health.

```python
def gain_xp(self, amount):
    self.xp += amount
    if self.xp >= 100:
        self.level_up()
```

### **Inventory System**

The **inventory** is managed through a dictionary, where items are stored and their quantities are tracked. Players can interact with their inventory during their journey.

```python
def add_item_to_inventory(self, item, quantity):
    if item in self.inventory:
        self.inventory[item] += quantity
    else:
        self.inventory[item] = quantity
```

## Conclusion

In this project, I demonstrated the use of **Encapsulation**, **Inheritance**, **Polymorphism**, and **Abstraction** in the context of a text-based RPG. Through careful design, I structured the game around these core OOP principles, ensuring modularity, reusability, and ease of future expansion. The game's dynamic quests, combat system, and character progression highlight the power of object-oriented design and provide an engaging experience for the player.

---
