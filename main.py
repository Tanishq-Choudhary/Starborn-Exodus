#Code By Tanishq-Choudhary @ Github

import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import pygame

pygame.mixer.init()
def play():
    pygame.mixer.music.load("assets/bgm.mp3")
    pygame.mixer.music.play(loops=99)

play()

class Player:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.level = 1
        self.xp = 0
        self.max_health = 100
        self.health = self.max_health
        self.attack = 5 if gender == "Male" else 3  
        self.stealth = 3 if gender == "Male" else 5  
        self.morality = 0  
        self.relationship = {}
        self.inventory = {"Potion": 3, "Gold": 500} 
        self.gear_level = 1  

    def gain_xp(self, xp):
        self.xp += xp
        if self.xp >= 100:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.max_health += 10
        self.attack += 2 if self.gender == "Male" else 1
        self.stealth += 1 if self.gender == "Female" else 0
        self.health = self.max_health
        self.xp = 0
        messagebox.showinfo("Level Up", f"Congratulations! You've reached Level {self.level}.")

    def heal(self):
        if "Potion" in self.inventory and self.health < self.max_health:
            self.health = min(self.health + 20, self.max_health)
            self.inventory["Potion"] -= 1
            messagebox.showinfo("Healing", "You used a Potion to heal yourself.")
        else:
            messagebox.showwarning("No Potion", "You don't have any Potions left.")


class Monster:
    def __init__(self, name, health, attack, reward_xp, reward_gold):
        self.name = name
        self.health = health
        self.attack = attack
        self.reward_xp = reward_xp
        self.reward_gold = reward_gold

    def is_defeated(self):
        return self.health <= 0

    def take_damage(self, damage):
        self.health -= damage


class GameApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Starborn Exodus: Legend of The Godslayer OOPS Project : 23FE10CSE00664")
        self.geometry("900x600")
        self.resizable(False, False)

        self.player = None
        self.current_location = "Bar"
        self.betrayer_god_health = 100  
        self.places_to_travel = {
            "Bar": ["Temple", "Village", "Ruins"],
            "Temple": ["Bar"],
            "Village": ["Bar"],
            "Ruins": ["Bar"]
        }

        self.create_widgets()

    def create_widgets(self):
       
        welcome_message = (
            "Welcome to Starborn Exodus, the tale of vengeance and rebirth.\n\n"
            "You are the last of the starborn, once a god amongst mortals. Disgraced and betrayed by those you trusted most.\n"
            "You have lost everything—your power, your title, your very identity.\n"
            "Now, you are but a shadow of what you once were, cast out of the celestial realms, exiled by the gods themselves.\n\n"
            "But your story does not end in ruin. You rise from the ashes of betrayal, seeking vengeance against those who abandoned you.\n"
            "The world trembles at the thought of your wrath. Your journey will not be easy, but it will be legendary.\n\n"
            "In this game, your choices will define your path. Will you rise as a Hero, gaining the strength to challenge gods themselves?\n"
            "Or will you embrace the shadows, becoming a Rogue, gaining speed and cunning in your quest for retribution?\n\n"
            "Your alignment will shape your fate. Your strength, morality, and relationships will guide you, but in the end, vengeance will be your only master.\n\n"
            "This game is not just about the story. It is a journey through the power of Object-Oriented Programming (OOP).\n"
            "- *Encapsulation*: Your stats, items, and decisions are hidden within objects, giving structure and clarity to your journey.\n"
            "- *Inheritance*: Characters like you, the Hero and the Rogue, inherit traits of the starborn, with unique abilities and powers.\n"
            "- *Polymorphism*: Your choices in how you live your life—whether as a Hero or Rogue—will shape how you engage with the world around you.\n"
            "- *Abstraction*: The complex mechanics of your revenge, your relationships, and your destiny are hidden, giving you only the choices that matter.\n\n"
            "Prepare yourself, for you are about to embark on an epic journey that will echo through the ages.\n"
            "You will fight gods, change the fate of the world, and restore what was lost. Your destiny awaits.\n\n"
            "Press Enter to begin your exodus..."
        )

       
        self.lbl_info = tk.Label(self, text=welcome_message, justify=tk.LEFT, font=("Garamond", 11), width=120, height=25, wraplength=1000)
        self.lbl_info.pack(padx=0, pady=0)

        
        self.start_button = tk.Button(self, text="Start Game", command=self.start_game)
        self.start_button.pack(pady=10)

    def start_game(self):

        self.lbl_info.config(text="Game Starting...") 

        self.btn_start = tk.Button(self, text="Click here to start", command=self.start_adventure)
        self.btn_start.pack()

    def start_adventure(self):
        self.clear_widgets()
        self.create_player()

    def clear_widgets(self):
        for widget in self.winfo_children():
            widget.destroy()

    def create_player(self):
        self.lbl_class = tk.Label(self, text="Choose your gender:")
        self.lbl_class.pack()

        gender_options = ["Male", "Female"]
        for gender in gender_options:
            btn_gender = tk.Button(self, text=gender, command=lambda g=gender: self.select_class(g))
            btn_gender.pack()

    def select_class(self, gender):
        player_name = simpledialog.askstring("Player Name", "Enter your name:")
        if player_name:
            self.player = Player(player_name, gender)
            self.show_stats()

    def count_consonants(self, name):
        vowels = "AEIOUaeiou"
        consonants = 0
        for char in name:
            if char.isalpha() and char not in vowels:
                consonants += 1
        return consonants

    def show_stats(self):
        self.clear_widgets()
        
        consonants_count = self.count_consonants(self.player.name)
        
        stats_text = (
            f"Player: {self.player.name} (Consonants: {consonants_count})\n"
            f"Gender: {self.player.gender}\n"
            f"Level: {self.player.level}\n"
            f"XP: {self.player.xp}/100\n"
            f"Health: {self.player.health}/{self.player.max_health}\n"
            f"Attack: {self.player.attack}\n"
            f"Stealth: {self.player.stealth}\n"
            f"Morality: {self.player.morality}\n\n"
            f"Inventory:\n"
        )
        
        for item, quantity in self.player.inventory.items():
            stats_text += f"{item}: {quantity}\n"
        
        stats_text += f"\nCurrent Location: {self.current_location}"
        
        self.lbl_stats = tk.Label(self, text=stats_text)
        self.lbl_stats.pack()

        self.btn_activity = tk.Button(self, text="Choose Activity", command=self.choose_activity)
        self.btn_activity.pack()

    def choose_activity(self):
        self.clear_widgets()
        self.lbl_activity = tk.Label(self, text="Choose an activity:")
        self.lbl_activity.pack()

        activities = ["View Stats", "Travel", "Shop", "Quest", "Confrontation"]
        for activity in activities:
            btn_activity = tk.Button(self, text=activity, command=lambda a=activity: self.handle_activity(a))
            btn_activity.pack()

        lbl_location = tk.Label(self, text=f"Current Location: {self.current_location}")
        lbl_location.pack()

    def handle_activity(self, activity):
        if activity == "View Stats":
            self.show_stats()
        elif activity == "Travel":
            self.travel()
        elif activity == "Shop":
            self.shop()
        elif activity == "Quest":
            self.quest()
        elif activity == "Confrontation":
            self.confrontation()

    def confrontation(self):
    
        messagebox.showinfo("Confrontation", (
            "You stand at the foot of an ancient, crumbling temple. The air is thick with dark magic.\n\n"
            "This is where your journey began, where you were betrayed by the one you trusted most.\n"
            "Now, before you, stands Malakoth, the Fallen King.\n\n"
            f"'You've come back for more, {self.player.name}?' Malakoth's voice echoes, a deep, haunting growl.\n"
            "'Foolish. You think you can undo the consequences of your defiance?'\n\n"
            "Malakoth, once a mighty ruler of the gods, now stands before you as a corrupted being of unimaginable power."
        ))
        
        
        self.confrontation_stage_one()

    def confrontation_stage_one(self):
        
        messagebox.showinfo("Malakoth's Taunt", (
            f"'You've always been weak, {self.player.name}. You could never understand the true weight of power.'\n\n"
            "'But now, you have come for vengeance? A laughable notion.'\n\n"
            "He spreads his arms, and the very air around you seems to crackle with darkness."
        ))

        player_choice = messagebox.askyesno(
            "First Move",
            "Will you charge forward with all your might, or wait and watch for an opening?\n\n"
            "Yes: Charge with full force\nNo: Wait and observe"
        )

        if player_choice:
            self.attack_first()
        else:
            self.wait_and_counter()

    def attack_first(self):
        
        if self.player.attack >= 20:
            damage_dealt = random.randint(40, 60)
            self.betrayer_god_health -= damage_dealt
            messagebox.showinfo("Fierce Strike", (
                f"With a primal scream, you charge at Malakoth. Your strike lands with the force of a thunderstorm!\n"
                f"You deal {damage_dealt} damage to the Fallen King.\n\n"
                f"'You’re a fool, {self.player.name}!' Malakoth laughs as he slowly heals the wound.\n"
                "'I have lived for millennia... Your strength is meaningless.'"
            ))
        else:
            damage_taken = random.randint(30, 50)
            self.player.health -= damage_taken
            messagebox.showinfo("Failed Attack", (
                "You charge recklessly, but Malakoth barely flinches.\n"
                f"He counters with devastating speed, and you take {damage_taken} damage in return.\n\n"
                "'You are nothing compared to me!' Malakoth scoffs, his eyes glowing with malevolent power."
            ))
        self.confrontation_stage_two()

    def wait_and_counter(self):
        
        if random.randint(1, 10) > 4:
            damage_dealt = random.randint(40, 60)
            self.betrayer_god_health -= damage_dealt
            messagebox.showinfo("Perfect Counter", (
                "You study Malakoth’s movements carefully. Just as he lunges, you sidestep and strike at his exposed side.\n"
                f"You deal {damage_dealt} damage to the Fallen King.\n\n"
                "'You may be swift, but you’re still no match for me!' Malakoth growls, clearly enraged."
            ))
        else:
            damage_taken = random.randint(30, 50)
            self.player.health -= damage_taken
            messagebox.showinfo("Mistimed Counter", (
                "Your timing falters, and Malakoth’s massive fist crashes into you.\n"
                f"You take {damage_taken} damage as you’re sent flying back.\n\n"
                "'Pathetic. You can’t even dodge me.'"
            ))
        self.confrontation_stage_two()

    def confrontation_stage_two(self):
        
        messagebox.showinfo("Malakoth's Power", (
            f"'You’ve barely scratched the surface of my power, {self.player.name}.' Malakoth says, a cruel smile spreading across his face.\n\n"
            "'I gave you a chance, but it seems you prefer to die slowly.'\n\n"
            "The very ground beneath your feet cracks as Malakoth summons an army of shadow creatures from the void."
        ))

        player_choice = messagebox.askyesno(
            "Second Move",
            "Do you attempt to fight through his shadow army with sheer will, or find a way to break the connection he has with them?\n\n"
            "Yes: Fight through the shadows\nNo: Break the connection"
        )

        if player_choice:
            self.fight_through_shadows()
        else:
            self.break_the_connection()

    def fight_through_shadows(self):
        if self.player.attack >= 25:
            damage_dealt = random.randint(50, 70)
            self.betrayer_god_health -= damage_dealt
            messagebox.showinfo("Fury Unleashed", (
                "You fight through the swarm of dark creatures, cutting them down with relentless fury.\n"
                f"You deal {damage_dealt} damage to Malakoth himself as he momentarily falters.\n\n"
                "'You have no idea what you’re dealing with!' Malakoth roars, fury in his voice."
            ))
        else:
            damage_taken = random.randint(40, 60)
            self.player.health -= damage_taken
            messagebox.showinfo("Swarmed", (
                "You’re overwhelmed by the tide of shadows. Each creature seems to drain your strength.\n"
                f"You take {damage_taken} damage as you’re trapped in the swarm.\n\n"
                f"'This is the end for you, {self.player.name}!' Malakoth cackles maniacally."
            ))
        self.confrontation_stage_three()

    def break_the_connection(self):
        if random.randint(1, 10) > 5:
            damage_dealt = random.randint(60, 80)
            self.betrayer_god_health -= damage_dealt
            messagebox.showinfo("Connection Severed", (
                "You focus your mind, finding the weak link in Malakoth’s dark magic. With a surge of willpower, you sever his connection to the shadows.\n"
                f"You deal {damage_dealt} damage to him as his connection weakens.\n\n"
                "'No! You... you cannot stop me!' Malakoth roars, the shadows retreating into the void."
            ))
        else:
            damage_taken = random.randint(35, 50)
            self.player.health -= damage_taken
            messagebox.showinfo("Failed Attempt", (
                "You try to disrupt the flow of dark magic, but it’s too powerful.\n"
                f"You take {damage_taken} damage as Malakoth’s wrath is unleashed upon you.\n\n"
                "'You are not worthy to face me, mortal.'"
            ))
        self.confrontation_stage_three()

    def confrontation_stage_three(self):
         
        messagebox.showinfo("Malakoth's Final Form", (
            "'Enough of this... Time to end it all!' Malakoth bellows.\n\n"
            "He rises into the air, his form growing massive. Dark energy swirls around him, bending the very space around you.\n\n"
           f"'This is your last chance, {self.player.name}. Will you cower before me, or face your inevitable doom?'\n\n"
            "The temple shudders as the final confrontation begins."
        ))

        player_choice = messagebox.askyesno(
            "Final Choice",
            "Do you charge forward, risking everything, or prepare yourself for the ultimate defense?\n\n"
            "Yes: Charge with everything\nNo: Defend and wait for an opening"
        )

        if player_choice:
            self.final_charge()
        else:
            self.final_defense()

    def final_charge(self):
        
        if self.player.attack >= 30:
            damage_dealt = random.randint(80, 100)
            self.betrayer_god_health -= damage_dealt
            messagebox.showinfo("Final Strike", (
                "You gather all your strength, charging at Malakoth with a final, desperate attack.\n"
                f"You deal {damage_dealt} damage to the Fallen King as his body begins to crack and burn.\n\n"
                "'This... this is impossible!' Malakoth screams as he begins to fall apart."
            ))
        else:
            damage_taken = random.randint(50, 70)
            self.player.health -= damage_taken
            messagebox.showinfo("Final Reckoning", (
                "You charge recklessly, but Malakoth easily counters.\n"
                f"You take {damage_taken} damage as the energy of his power overwhelms you.\n\n"
                "'Fool... You were always too weak to win.'"
            ))
        self.final_battle_outcome()

    def final_defense(self):
        
        if random.randint(1, 10) > 5:
            damage_dealt = random.randint(90, 120)
            self.betrayer_god_health -= damage_dealt
            messagebox.showinfo("Defense and Counter", (
                "You hold your ground, waiting for the perfect moment. When Malakoth strikes, you parry and land a deadly counterattack.\n"
                f"You deal {damage_dealt} damage, and the Fallen King staggers.\n\n"
                "'No... I cannot lose... not like this!' Malakoth gasps."
            ))
        else:
            damage_taken = random.randint(60, 80)
            self.player.health -= damage_taken
            messagebox.showinfo("Unavoidable End", (
                "Malakoth’s power overwhelms your defense. You barely manage to hold on as his energy breaks through.\n"
                f"You take {damage_taken} damage as his final blow lands.\n\n"
                f"'Your end is inevitable, {self.player.name}.'"
            ))
        self.final_battle_outcome()

    def final_battle_outcome(self):
        if self.player.health <= 0:
            messagebox.showinfo("Defeat", (
                "The battle is over. Malakoth stands triumphant, his voice echoing as you fall to your knees.\n\n"
                "'You were never worthy to face me.'"
            ))
            self.destroy()
        elif self.betrayer_god_health <= 0:
            messagebox.showinfo("Victory", (
                "With one final, powerful strike, you destroy Malakoth, his dark form shattering into nothingness.\n\n"
                "'This is the end... You will never rule again.'\n"
                "The temple crumbles, and you stand victorious, your vengeance complete."
            ))
            self.destroy()
        else:
            
            self.show_stats()


    def travel(self):
        self.clear_widgets()
        travel_options = self.places_to_travel[self.current_location]
        self.lbl_travel = tk.Label(self, text="Choose a location to travel to:")
        self.lbl_travel.pack()

        for location in travel_options:
            btn_location = tk.Button(self, text=location, command=lambda loc=location: self.travel_to(loc))
            btn_location.pack()

    def travel_to(self, location):
        self.current_location = location
        self.show_stats()

    def shop(self):
        
        self.clear_widgets()
        
        
        lbl_shop = tk.Label(self, text="Welcome to the Shop!")
        lbl_shop.pack()

        
        lbl_money = tk.Label(self, text=f"Gold: {self.player.inventory.get('Gold', 0)}")
        lbl_money.pack()

        
        btn_buy_potion = tk.Button(self, text="Buy Potion (10 Gold)", command=self.buy_potion)
        btn_buy_potion.pack()

        btn_sell_potion = tk.Button(self, text="Sell Potion (5 Gold)", command=self.sell_potion)
        btn_sell_potion.pack()

        
        btn_leave = tk.Button(self, text="Back to Activities", command=self.choose_activity)
        btn_leave.pack()

    def buy_potion(self):
        
        if self.player.inventory.get("Gold", 0) >= 10:
            self.player.inventory["Gold"] -= 10
            self.player.inventory["Potion"] = self.player.inventory.get("Potion", 0) + 1
            messagebox.showinfo("Purchase Successful", "You bought a Potion.")
        else:
            messagebox.showwarning("Not Enough Gold", "You don't have enough gold to buy a Potion.")
        
        
        self.shop()

    def sell_potion(self):
        
        if self.player.inventory.get("Potion", 0) > 0:
            self.player.inventory["Gold"] += 5
            self.player.inventory["Potion"] -= 1
            messagebox.showinfo("Sale Successful", "You sold a Potion.")
        else:
            messagebox.showwarning("No Potions", "You don't have any Potions to sell.")
        
        
        self.shop()


    def quest(self):
    
        if self.current_location == "Bar":
            self.bar_quest()
        elif self.current_location == "Temple":
            self.temple_quest()
        elif self.current_location == "Ruins":
            self.ruins_quest()
        elif self.current_location == "Village":
            self.village_quest()
        else:
            self.default_quest()
    
    def bar_quest(self):
        
        quest_text = (
            "You sit at a rickety wooden table in the dimly lit corner of the bar. "
            "The noise of drunken revelers and clinking mugs fills the air. But you're not here to relax. "
            "You're here for something far more important, something that calls to you in the quiet of your soul.\n\n"
            "A shadow looms over your table. You glance up slowly. An old man, grizzled and broken, his eyes dull with age, stands before you. "
            "His weathered face twitches as he studies you, sizing you up.\n\n"
            "'I've been watching you...'\n\n"
            "The man leans in closer, his voice dropping to a whisper.\n\n"
            "'I know who you are... The last of the Starborn. The one who once ruled the heavens.'\n\n"
            "You don’t flinch. The world has tried to break you, but you’re still standing.\n\n"
            "'The village just outside this town has been terrorized by thieves. They're worse than beasts. "
            "And the guards... worthless. But you... you could be the reckoning they fear. What do you say? Will you help us?'"
        )
        messagebox.showinfo("Quest: The Thieves of the Village", quest_text)

        
        accept_quest = messagebox.askyesno(
            "Quest Offered",
            "Will you help the villagers by dealing with the thieves? You can either strike them down or show mercy."
        )

        if accept_quest:
            
            self.start_thieves_encounter()  
        else:
            
            messagebox.showinfo("Refused",  
                            "The villagers’ pleas fall on deaf ears. The old man shakes his head in disappointment. "
                            "'I thought you were more than this... but perhaps you’re just another broken soul.'"
                            "\n\nThe thieves strike again, and the villagers are left to fend for themselves. "
                            "You hear their screams in the distance, but you do nothing. The world is a little darker now.")
            self.show_stats()

    def start_thieves_encounter(self):
       
        quest_text = (
            "You arrive at the village under the cover of night. The thieves are gathered around a campfire, laughing and celebrating. "
            "Their leader, a burly man with a scar running across his cheek, looks up as you approach.\n\n"
            "'Well, well, what do we have here?' he sneers, clearly unimpressed. 'Another hero looking to save the day?'"
            "He stands, drawing his blade with a mocking flourish.\n\n"
            "'You should’ve stayed in the bar, fool.'\n\n"
            "You let out a low, dangerous chuckle. The air grows heavy with anticipation."
        )
        messagebox.showinfo("Thieves Encounter", quest_text)

        
        fight_choice = messagebox.askyesno(
            "Fight or Mercy",
            "Do you choose to fight the thieves, or do you offer them mercy and walk away?"
        )

        if fight_choice:
            
            messagebox.showinfo("Epic Battle", "You charge forward with the fury of a god, your strength overwhelming the thieves. "
                                            "Each strike leaves a trail of destruction. The leader is the last to fall, his eyes wide with fear. "
                                            "'You were nothing,' you mutter as you deliver the final blow.")
            reward = random.randint(30, 50)
            self.player.gain_xp(reward)
            messagebox.showinfo("Victory", f"You have defeated the thieves and gained {reward} XP. The village is safe once more.")
        else:
            
            messagebox.showinfo("Mercy Given", 
                                "You step forward, your presence overwhelming. 'You can leave now,' you say coldly. 'But know this: "
                                "if I ever hear of you again, you won't get another chance.'\n\n"
                                "The thieves look at each other nervously before fleeing into the night. The village is safe, for now.")
            reward = random.randint(10, 20)
            self.player.gain_xp(reward)
            messagebox.showinfo("Mercy Reward", f"You spared their lives and earned {reward} XP. The village is grateful, but the thieves live to terrorize another day.")

        self.show_stats()

    def failed_negotiation(self):
        
        messagebox.showinfo("Failed Negotiation", 
                            "The villagers’ pleas fall on deaf ears. The old man shakes his head in disappointment. "
                            "'I thought you were more than this... but perhaps you’re just another broken soul.'"
                            "\n\nThe thieves strike again, and the villagers are left to fend for themselves. "
                            "You hear their screams in the distance, but you do nothing. The world is a little darker now.")
        self.show_stats()
    def ruins_quest(self):
    
        quest_intro = (
            "You step into the ruins, the remnants of a once-thriving city now reduced to dust. The wind howls through "
            "broken stone pillars, carrying whispers of a forgotten past. The air is thick with the scent of decay and old magic. "
            "Suddenly, the ground beneath your feet trembles. The earth shakes with a low rumble, as if the ruins themselves "
            "are warning you.\n\n"
            "In the distance, a figure emerges from the shadows. Clad in dark robes, their face hidden beneath a hood, "
            "the figure raises a hand, and an ominous voice calls out to you:\n"
            "'So, the Starborn has come to the ruins... I have waited long for this moment.'"
        )
        messagebox.showinfo("Ruins Quest", quest_intro)

        
        messagebox.showinfo("Ruins Quest", "'You may not remember me, but I was once your most trusted ally. I followed you, "
                                        "believed in your vision... until I saw the truth. The gods betrayed us, yes, but "
                                        "so did you. You were the first to abandon us to the darkness. And now, you dare come here, "
                                        "seeking redemption? You will find none.'")

        
        player_choice = messagebox.askyesno(
            "Ruins Quest Decision",
            "Do you want to challenge your old ally in battle, or attempt to negotiate for peace?"
        )

        if player_choice:  
            self.fight_in_ruins()
        else:  
            self.negotiate_in_ruins()

    def fight_in_ruins(self):
        
        messagebox.showinfo("Fight Begins", "'Very well... I had hoped for more words, but you seek to spill blood, then blood you shall have!'")
        messagebox.showinfo("Ruins Quest", "The former ally draws their weapon, a blade forged from the very ruins of this place, "
                                        "its edge glowing with dark energy. They charge at you with a speed that betrays their age, "
                                        "ready to strike down the Starborn.")

        
        messagebox.showinfo("Battle Victory", f"You strike with incredible force, dealing damage to your former ally.")
            
              
        self.end_fight_success()
        
        
        self.show_stats()

    def end_fight_success(self):
        
        messagebox.showinfo("Ruins Quest", "Your former ally crumbles to the ground, defeated. Their weapon falls, "
                                        "the dark energy fading with their last breath. The ruins grow still once more.")
        reward = random.randint(20, 40)
        self.player.gain_xp(reward)
        messagebox.showinfo("Victory", f"You have gained {reward} XP for your victory.")
        self.show_stats()

    def negotiate_in_ruins(self):
        
        messagebox.showinfo("Negotiation", "'You still think you can talk your way out of this? It's too late for that. "
                                            "The ruin is already sealed... by my hand!'")
        messagebox.showinfo("Ruins Quest", "Your former ally summons a barrier of dark energy, the ruins trembling with its power. "
                                        "You stand there, trying to reach them with words, but there is only fury in their eyes.")

        
        if self.player.xp >= 50:  
            self.end_negotiation_success()
        else:  
            self.end_negotiation_failure()

    def end_negotiation_success(self):
        
        messagebox.showinfo("Negotiation Success", "'...Perhaps you are right. Perhaps I have been blind in my hatred. "
                                                "The gods may have betrayed us, but so did we betray each other. I will stand down.'")
        reward = random.randint(10, 30)
        self.player.gain_xp(reward)
        messagebox.showinfo("Ruins Quest", f"You have gained {reward} XP for your successful negotiation.")
        self.show_stats()  

    def end_negotiation_failure(self):
        
        messagebox.showinfo("Negotiation Failure", "'No. Your words are hollow. You are nothing but a shadow of your former self!'")
        self.fight_in_ruins()  
    
    def temple_quest(self):
    
        quest_intro = (
            "You walk through the hallowed halls of the Temple, the stone walls echoing with the ancient chants of monks past. "
            "The air is thick with the scent of incense and age-old books, the wisdom of countless generations drifting in the stillness.\n\n"
            "At the center of the vast hall, you find a young monk, kneeling in meditation. His face is calm, but his eyes, when they open, are filled with an ancient knowing—"
            "a quiet yet resolute presence that seems to pierce through the veils of time.\n\n"
            "'The Temple has been waiting for you, Starborn. Not many walk this path, but you... You were called here.'"
        )
        messagebox.showinfo("Temple Quest", quest_intro)

        
        messagebox.showinfo("Temple Quest", "'Please, sit with me. The world is a tempest, and within it, we search for meaning. "
                                        "But sometimes, in the stillness, we find answers that the noise of battle cannot provide.'")

        messagebox.showinfo("Temple Quest", "'You have suffered, Starborn. The gods cast you aside like a broken vessel, leaving you to drown in your own despair. "
                                        "Do you think you were forgotten? No, not forgotten—betrayed. But the question is, what will you do with that betrayal?'")

        
        messagebox.showinfo("Temple Quest", "'Betrayal is a hard thing to bear. We expect loyalty from those we trust, and when it is shattered, we feel the weight of it on our soul. "
                                        "It is a wound that cuts deeper than any sword. But it also opens us to something greater—a revelation. What does betrayal teach you?'")

        messagebox.showinfo("Temple Quest", "'The gods betrayed you not because you were weak, but because you were strong. You were something beyond them—"
                                        "a being who could rise above the confines of their realm. They feared your potential. Fear can be more dangerous than hatred.'")

        messagebox.showinfo("Temple Quest", "'What does it mean to be a god? The gods once ruled with absolute authority, controlling the fates of mortals and immortals alike. "
                                        "But even they are bound by their limitations—prisoners of their own making. They cannot see beyond their own eternity, their own rules.'")

        messagebox.showinfo("Temple Quest", "'You are different. You were born with a power they could not understand. And it is that power that caused their downfall.'")

        messagebox.showinfo("Temple Quest", "'But power, Starborn... it is a double-edged sword. To wield it without wisdom is to risk becoming what you despise.'")

        
        messagebox.showinfo("Temple Quest", "'I see the fire in your eyes. You carry the anger of the betrayed, the weight of those who wronged you. But listen closely—"
                                        "the path of vengeance is seductive. It calls to you, whispers promises of retribution, of restoring what was taken from you.'")

        messagebox.showinfo("Temple Quest", "'But vengeance is not justice. It is an endless cycle of destruction that consumes all in its path, even the one who seeks it.'")

        messagebox.showinfo("Temple Quest", "'You must ask yourself—what is your true purpose? To destroy the gods who abandoned you? To prove to them that you are still worthy?'")

        messagebox.showinfo("Temple Quest", "'Or is there something more? A deeper understanding of your own existence? A way to transcend the hatred and find balance in the chaos?'")

        
        messagebox.showinfo("Temple Quest", "'Look around you. This temple was once a place of great power and wisdom. But now, the halls are empty. The gods who once frequented it are gone, "
                                        "leaving only their broken promises behind.'")

        messagebox.showinfo("Temple Quest", "'The world is like this temple—ancient, crumbling, and yet, there is still life within it. There is still hope. We must learn from the mistakes of the past, "
                                        "so that we do not repeat them. What will you learn from your pain, Starborn? How will you move forward?'")

        messagebox.showinfo("Temple Quest", "'Your journey does not end with vengeance, though that may be part of it. It is a journey of self-discovery, of finding balance in a world torn apart by gods and mortals alike.'")

        
        messagebox.showinfo("Temple Quest", "'The greatest battle is not fought with sword or fire, but with the self. What you face within yourself will determine the world around you.'")

        messagebox.showinfo("Temple Quest", "'The gods may have abandoned you, but you have not abandoned yourself. You are still the Starborn, the last of your kind, with power untold. But that power is yours to control, not to be controlled by.'")

        messagebox.showinfo("Temple Quest", "'What you do next, Starborn, is yours to choose. Will you let the gods’ betrayal define you, or will you rise above it? The world is waiting for you to make that choice.'")

        
        messagebox.showinfo("Temple Quest", "'There is no true victory without wisdom. To conquer the world, you must first conquer yourself. Only then will you have the strength to shape the future.'")

        messagebox.showinfo("Temple Quest", "'You will face many trials ahead, but remember this—no matter how dark the road may seem, there is always light to be found. Even in the shadows of betrayal, there is the possibility of redemption.'")

        
        messagebox.showinfo("Temple Quest", "'Go now, Starborn. The gods may have cast you down, but you still have the power to rise. Remember, true strength comes not from anger or revenge, but from understanding and balance.'")

        
        reward_xp = random.randint(30, 50)
        self.player.gain_xp(reward_xp)
        messagebox.showinfo("Temple Quest", f"You have gained {reward_xp} XP for reflecting on the teachings of the monk and gaining wisdom in your journey.")
        
        
        self.show_stats()
        
    def village_quest(self):
    
        quest_intro = (
            "You arrive in a quaint little village, the scent of freshly baked bread mixing with the sounds of chickens clucking and people laughing. "
            "The villagers seem to be going about their daily business, but one particular individual catches your eye—a portly, grinning man with a surprisingly loud voice. "
            "He’s standing by a cart full of *questionable* goods, shouting at the passing villagers.\n\n"
            "'Hey there, mighty Starborn! I’ve got a proposition for ya!'"
        )
        messagebox.showinfo("Village Quest", quest_intro)

        
        messagebox.showinfo("Village Quest", "'I know what you’re thinking, ‘Who’s this strange fellow?’ Well, let me introduce myself. I'm Grubbins! Not exactly a name that'll strike fear into your enemies, huh?'")
        messagebox.showinfo("Village Quest", "'Anyway, enough about my charmingly ridiculous name. I've got a little *problem*, and I think you’re the one to solve it!'")

        
        messagebox.showinfo("Village Quest", "'Here’s the deal, Starborn. I’ve got a stash of *precious* goods, and by precious, I mean stuff I ‘borrowed’ from some very *unfortunate* travelers. "
                                        "But here’s the thing—I’m missing a very important item to complete my “collection”. No biggie, just a little *human* foot, nothing strange about that, right?'")

        
        messagebox.showinfo("Village Quest", "'You see, I’ve been trying to get my hands on a *genuine* foot from a human. Not just any foot! A foot from someone who’s tall, dashing, heroic-looking, maybe even... I dunno... a little Starborn-y?'")
        
        messagebox.showinfo("Village Quest", "'The thing is, there’s this *elderly* fellow in the village, blind as a bat, who *happens* to have a foot I’ve been eyeing. "
                                        "But you know, I can’t exactly waltz in there and ask him for it. That’d be... well, *awkward*. And I do like to keep my reputation intact, thank you very much.'")

        
        messagebox.showinfo("Village Quest", "'So, here’s where you come in. I need you to go to old man Crusty’s house and *“borrow”* that foot for me. Don’t worry, he won’t miss it. "
                                        "And, hey, you’ll be doing him a favor. I mean, how much use can a blind, elderly man really have for a foot, right? Pfft!'")

        messagebox.showinfo("Village Quest", "'If you’re successful, I’ll reward you handsomely with, uh... a *mystery item*. Could be something useful, could be something completely absurd. "
                                        "But hey, you can’t say I don’t know how to treat my guests!'")

        
        accept_quest = messagebox.askyesno("Quest Acceptance", "'So, what do you say, Starborn? Ready to do a little *dirty work* for a weird, little man like me? Trust me, you won’t regret it... probably.'")

        if accept_quest:
            messagebox.showinfo("Village Quest", "'Ha! I knew I could count on you! I can already tell you’re going to be a great asset to my *collection*.'")

            
            messagebox.showinfo("Village Quest", "'Alright, go on then. Don’t be shy, knock on old man Crusty’s door. But remember—*no* kicking, no *weird* foot-related comments, just grab and go!'")
            messagebox.showinfo("Village Quest", "'I’ll be here, waiting with *great anticipation* for that foot. You better not disappoint me!'")

            
            messagebox.showinfo("Village Quest", "'You approach old man Crusty’s house, but you can hear him muttering to himself inside, his voice frail and shaky. "
                                            "It seems like he's having one of his old-man rants. Oh, this should be good... What will you do?'")

            
            player_choice = messagebox.askyesno(
                "Sneak or Ask?",
                "'Do you sneak in quietly and try to *steal* the foot? Or do you knock on the door, with all the subtlety of a bull in a china shop?'"
            )

            if player_choice:  
                messagebox.showinfo("Village Quest", "'You sneak around the back, trying your best to be as stealthy as possible. But you can’t help but think—this is a really weird thing to be doing.'")
                messagebox.showinfo("Village Quest", "'You manage to make it to Crusty’s bedroom, where the foot is tucked away in a little cabinet. As you gently grab it... CRASH! You step on a rusty old tin can!'")
                messagebox.showinfo("Village Quest", "'Old man Crusty stirs in his sleep. You freeze. He mumbles something about ‘bloody kids’ and ‘spells with chickens’ but doesn’t wake up. Phew!'")

                
                messagebox.showinfo("Village Quest", "'You get the foot! It’s not as glamorous as you thought, but hey, it’s *a foot*. Now, all that’s left is to bring it back to Grubbins.'")
            else:  
                messagebox.showinfo("Village Quest", "'You knock on the door. Crusty opens, blinking up at you with a confused look. You greet him with a cheerful ‘Hey, mind if I borrow your foot?’'")
                messagebox.showinfo("Village Quest", "'Old man Crusty just stares at you, blinking slowly. ‘Well, that’s the weirdest thing anyone’s ever said to me...’ he says. Well, at least you didn’t sneak around!'")

                messagebox.showinfo("Village Quest", "'After a long, uncomfortable silence, he sighs and says, ‘Alright, take the darn foot, just don’t make a mess of my house.’")
                messagebox.showinfo("Village Quest", "'You’ve got the foot. A little easier than expected, but now, what’s next?'")

            
            messagebox.showinfo("Village Quest", "'You return to Grubbins, who’s grinning like a Cheshire cat. He’s practically drooling as you hand over the foot.'")
            messagebox.showinfo("Village Quest", "'Ah, the *perfect foot*! Now, let’s see what’s behind door number one, shall we?'")

            
            reward_item = random.choice(["A rusty sword", "A bag of mysterious beans", "A strange amulet", "A weirdly ornate boot"])
            messagebox.showinfo("Village Quest", f"'You get your reward: {reward_item}. Not exactly what you expected, but hey, it’s better than nothing!'")

            
            messagebox.showinfo("Village Quest", "'Well, that was certainly an adventure. I’ll be here, *probably causing chaos* until next time. Thanks for the foot, Starborn!'")

            
            reward_xp = random.randint(15, 30)
            self.player.gain_xp(reward_xp)
            messagebox.showinfo("Village Quest", f"You have gained {reward_xp} XP for completing the village quest. Well done... weirdo.")

            
            self.show_stats()

        else:
            messagebox.showinfo("Village Quest", "'Pfft, what’s the matter? Too good for a little foot theft? Fine, go off and be all heroic somewhere else then.'")

            
            self.show_stats()

if __name__ == "__main__":
    app = GameApp()
    app.mainloop()
    
    #Code By Tanishq-Choudhary @ Github
