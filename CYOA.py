import time

def slow_print(text, delay=0.03):
    """Prints text character by character for dramatic effect."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # Newline at the end

def game():
    """The main game function - a choose your own adventure."""

    player_name = input("Enter your name, adventurer: ")
    slow_print("\n")
    print("-" * 40)
    print(f"       CAVE OF THE WINDS!")
    print("-" * 40)
    slow_print("\n")

    # Lore - Why you shouldn't enter the Cave of the Winds
    slow_print("For centuries, the villagers of Oakhaven have warned against entering the Cave of the Winds. Legend speaks of a malevolent entity known as 'The Whisperer,' who dwells within its depths.")
    slow_print("It is said that The Whisperer feeds on memories and emotions, trapping those who enter in an endless cycle of fragmented recollections. Some claim to hear voices echoing from the cave – whispers of lost souls begging for release.")
    slow_print("The original explorers vanished without a trace, their names scrubbed from history as if they never existed.  Ancient runes carved into the entrance warn: 'Turn back, lest you become another echo in The Whisperer's symphony.'")
    slow_print("Even the bravest warriors have refused to venture near, fearing that the cave’s influence can corrupt even the strongest minds.")
    slow_print("Yet, whispers persist of a powerful artifact hidden within – 'The Orb of Clarity,' said to grant its wielder the ability to see through illusions and perceive true reality.  But is such power worth the risk?")

    slow_print("\nDespite the warnings, you find yourself drawn to the Cave of the Winds...")

    # --- Initial Scene ---
    scene1(player_name)


def scene1(player_name):
    """The first scene - Awakening in the woods."""
    slow_print("\nThe air is thick with the scent of damp earth and decaying leaves.  Sunlight struggles to penetrate the dense canopy above.")
    slow_print("You notice three distinct paths leading away from your current location:")
    slow_print("1. A narrow, overgrown trail heading deeper into the woods - it feels ancient and forgotten.")
    slow_print("2. A well-worn path that seems to lead towards a distant village – smoke curls lazily on the horizon.")
    slow_print("3.  A rocky ascent leading up a steep hill – you can hear the faint sound of rushing water from above.")

    choice = input("\nWhich path do you choose? (1, 2, or 3): ")

    if choice == "1":
        scene2_woods(player_name)
    elif choice == "2":
        scene3_village(player_name)
    elif choice == "3":
        scene4_hill(player_name)
    else:
        slow_print("Invalid choice. You stumble around confused, wasting precious time.")
        scene1(player_name)  # Return to the same scene


def scene2_woods(player_name):
    """Scene 2 - Deeper into the woods."""
    slow_print("\nYou push through tangled vines and gnarled branches. The deeper you go, the darker it becomes.")
    slow_print("You come across a clearing where an ancient stone circle stands. In the center lies a weathered pedestal with a single object: a tarnished silver locket.")
    slow_print("1. Examine the locket.")
    slow_print("2. Ignore the locket and continue deeper into the woods.")
    slow_print("3. Attempt to decipher the runes carved on the stones of the circle.")

    choice = input("\nWhat do you do? (1, 2, or 3): ")

    if choice == "1":
        scene5_locket(player_name)
    elif choice == "2":
        scene6_deeper_woods(player_name)
    elif choice == "3":
        scene7_runes(player_name)
    else:
        slow_print("You hesitate, lost in thought. The shadows seem to deepen around you.")
        scene2_woods(player_name)


def scene3_village(player_name):
    """Scene 3 - Approaching the village."""
    slow_print("\nThe path leads you towards a small village nestled in a valley.  The villagers appear wary, but not openly hostile.")
    slow_print("As you approach, a stern-looking man with a long grey beard steps forward.")
    slow_print("'You are new here,' he says. 'State your business.'")
    slow_print("1. Claim to be lost and seeking shelter.")
    slow_print("2. Ask about the history of Eldoria.")
    slow_print("3. Offer to help with a task in exchange for information or assistance.")

    choice = input("\nWhat do you say? (1, 2, or 3): ")

    if choice == "1":
        scene8_lost(player_name)
    elif choice == "2":
        scene9_history(player_name)
    elif choice == "3":
        scene10_help(player_name)
    else:
        slow_print("You stammer, unable to form a coherent sentence. The villagers exchange uneasy glances.")
        scene3_village(player_name)


def scene4_hill(player_name):
    """Scene 4 - Climbing the hill."""
    slow_print("\nThe climb is arduous, but you eventually reach the summit.  A breathtaking view of Eldoria unfolds before you – rolling hills, dense forests, and a shimmering lake in the distance.")
    slow_print("You notice a small cave entrance partially hidden by foliage.")
    slow_print("1. Explore the cave.")
    slow_print("2. Continue admiring the view and try to orient yourself.")
    slow_print("3. Search for signs of life or civilization from this vantage point.")

    choice = input("\nWhat do you do? (1, 2, or 3): ")

    if choice == "1":
        scene11_cave(player_name)
    elif choice == "2":
        scene12_view(player_name)
    elif choice == "3":
        scene13_search(player_name)
    else:
        slow_print("You lose your footing on the rocky terrain, nearly tumbling back down.")
        scene4_hill(player_name)

# --- More Scenes (Expanding the Story - Add more as needed!) ---

def scene5_locket(player_name):
    """Scene 5 - Examining the locket."""
    slow_print("\nYou carefully pick up the locket. It's cold to the touch.  You manage to pry it open, revealing a miniature portrait of a beautiful woman with sorrowful eyes.")
    slow_print("As you gaze at the portrait, a wave of memories floods your mind – fragments of a life you don’t remember living…")
    slow_print("1. Focus on the memory and try to piece together what happened.")
    slow_print("2. Dismiss the vision as a trick of the light and continue exploring.")

    choice = input("\nWhat do you do? (1 or 2): ")
    if choice == "1":
        scene14_memories(player_name)
    else:
        scene6_deeper_woods(player_name)


def scene6_deeper_woods(player_name):
    """Scene 6 - Deeper into the woods."""
    slow_print("You wander deeper, eventually getting hopelessly lost.  Exhausted and disoriented, you succumb to the elements.")
    ending1()

def scene7_runes(player_name):
    """Scene 7 - Deciphering runes."""
    slow_print("After hours of study, you decipher the runes. They warn of a corrupted guardian protecting a powerful artifact.")
    slow_print("1. Seek out the artifact anyway.")
    slow_print("2. Heed the warning and leave the circle.")

    choice = input("\nWhat do you do? (1 or 2): ")
    if choice == "1":
        scene23_guardian(player_name)
    else:
        ending5()  #Heeding the warning


def scene8_lost(player_name):
    """Scene 8 - Claiming to be lost."""
    slow_print("The villagers are sympathetic, offering you food and shelter. However, they also warn you about a growing darkness threatening Eldoria.")
    scene16_warning(player_name)

def scene9_history(player_name):
    """Scene 9 - Asking about history."""
    slow_print("The elder recounts tales of ancient wars, powerful magic, and a prophecy foretelling the return of a dark lord. He mentions a legendary sword capable of defeating him.")
    scene24_sword(player_name)

def scene10_help(player_name):
    """Scene 10 - Offering help."""
    slow_print("The villagers need help with a troublesome beast that has been terrorizing their livestock. It's said to dwell in the nearby swamp.")
    scene25_beast_swamp(player_name)

def scene11_cave(player_name):
    """Scene 11 - Exploring the cave."""
    slow_print("The cave is dark and damp. You stumble upon a hidden chamber containing an ancient artifact – a shimmering orb.")
    scene26_orb(player_name)

def scene12_view(player_name):
    """Scene 12 - Admiring the view."""
    slow_print("You spend hours admiring the view, but eventually night falls. Without shelter or supplies, you perish from exposure.")
    ending2()

def scene13_search(player_name):
    """Scene 13 - Searching for signs of life."""
    slow_print("You spot a faint trail leading towards a distant tower, partially obscured by mist.")
    scene20_tower(player_name)


def scene14_memories(player_name):
    """Scene 14 - Recalling memories."""
    slow_print("The memories flood back: you were a royal mage, betrayed and stripped of your power.  You must reclaim your birthright!")
    scene27_birthright(player_name)

def scene15_portal(player_name):
    """Scene 15 - Entering the portal."""
    slow_print("You step through the portal, never to be seen again.")
    ending4()

def scene16_warning(player_name):
    """Scene 16 - Heeding the warning."""
    slow_print("You decide to heed their warnings and leave Eldoria, never looking back.")
    ending5()

def scene17_prophecy(player_name):
    """Scene 17 - The prophecy."""
    slow_print("The prophecy speaks of a hero who will either save or destroy Eldoria.  You feel a strange pull towards destiny...")
    scene21_hero(player_name)

def scene18_beast(player_name):
    """Scene 18 - Slaying the beast."""
    slow_print("You bravely confront the beast, defeating it with your cunning and strength. The villagers hail you as a hero.")
    ending6()

def scene19_artifact(player_name):
    """Scene 19 - The artifact."""
    slow_print("The artifact grants you incredible power, but also corrupts your mind. You become obsessed with control.")
    ending7()

def scene20_tower(player_name):
    """Scene 20 - Approaching the tower."""
    slow_print("You approach the tower. It is guarded by a fearsome dragon!")
    scene22_dragon(player_name)

def scene21_hero(player_name):
    """Scene 21 - The hero's choice."""
    slow_print("Do you choose to save Eldoria or embrace the darkness?")
    ending8()

def scene22_dragon(player_name):
    """Scene 22 - Facing the dragon."""
    slow_print("You face the dragon. Do you fight, try to reason with it, or sneak past?")
    ending9()

def scene23_guardian(player_name):
    """Scene 23 - Confronting the Guardian."""
    slow_print("The corrupted guardian is a powerful spectral knight.  Do you attack head-on or attempt to find its weakness?")
    choice = input("\nWhat do you do? (1: Attack, 2: Search for Weakness): ")
    if choice == "1":
        ending10() #Direct confrontation leads to defeat
    else:
        scene28_weakness(player_name)

def scene24_sword(player_name):
    """Scene 24 - Seeking the Sword."""
    slow_print("The elder tells you of a hidden cave where the legendary sword, 'Lightbringer,' is said to be kept.  It's protected by magical traps.")
    scene29_traps(player_name)

def scene25_beast_swamp(player_name):
    """Scene 25 - The Swamp Beast."""
    slow_print("The swamp is a fetid, dangerous place. You encounter the beast – a giant crocodile with glowing red eyes.")
    ending11() #Beast defeats you

def scene26_orb(player_name):
    """Scene 26 - The Shimmering Orb."""
    slow_print("The orb pulses with energy. Touching it grants you visions of the future, but also drains your strength.")
    ending12() #Orb drains your life force

def scene27_birthright(player_name):
    """Scene 27 - Reclaiming Your Throne."""
    slow_print("You begin a quest to gather allies and reclaim your throne.  Your journey is fraught with peril...")
    ending13() #Long, complex quest – not fully implemented yet

def scene28_weakness(player_name):
    """Scene 28 - Finding the Guardian's Weakness."""
    slow_print("You discover that the guardian’s power stems from a corrupted crystal. Destroying it weakens him.")
    ending14() #Destroying the crystal defeats the guardian

def scene29_traps(player_name):
    """Scene 29 - Navigating the Traps."""
    slow_print("You carefully navigate the traps, but one proves too clever. A hidden dart poisons you.")
    ending15() #Poisoned by a trap


# --- Existing Endings (Expanded) ---

def ending1():
    """Ending 1: Lost in the Woods."""
    slow_print("\nYou wander aimlessly until your strength fails. The Whispering Woods claim another victim.")
    slow_print("GAME OVER")

def ending2():
    """Ending 2: Exposure."""
    slow_print("\nThe cold night air seeps into your bones. You succumb to the elements, a forgotten soul on the hillside.")
    slow_print("GAME OVER")

def ending3():
    """Ending 3: Revenge Fulfilled."""
    slow_print("You reclaim your throne and bring justice to those who betrayed you. Eldoria enters an era of peace and prosperity.")
    slow_print("VICTORY!")

def ending4():
    """Ending 4: Vanished Through the Portal."""
    slow_print("You step through the portal, never to be seen again. Your fate remains a mystery.")
    slow_print("GAME OVER")

def ending5():
    """Ending 5: Heeding the Warning."""
    slow_print("You decide to heed their warnings and leave Eldoria, never looking back. A wise choice.")
    slow_print("GAME OVER")

def ending6():
    """Ending 6: Hero of the Village."""
    slow_print("The villagers hail you as a hero for defeating the beast. You are welcomed with open arms and given land and title.")
    slow_print("VICTORY!")

def ending7():
    """Ending 7: Corrupted by Power."""
    slow_print("You become obsessed with power, ruling Eldoria with an iron fist. Your reign is one of fear and oppression.")
    slow_print("GAME OVER")

def ending8():
    """Ending 8: Savior or Destroyer."""
    slow_print("Your choice determines the fate of Eldoria – either a golden age of peace or a descent into darkness.")
    slow_print("THE END (Depending on your choices)")

def ending9():
    """Ending 9: Dragon's Fury."""
    slow_print("You attempt to fight the dragon, but its fiery breath overwhelms you. You are reduced to ashes.")
    slow_print("GAME OVER")

def ending10():
    """Ending 10: Guardian's Defeat (Direct Confrontation)."""
    slow_print("Your reckless attack fails against the guardian’s power.  You are swiftly defeated.")
    slow_print("GAME OVER")

def ending11():
    """Ending 11: Swamp Beast."""
    slow_print("The swamp beast is too powerful. You become another victim of its jaws.")
    slow_print("GAME OVER")

def ending12():
    """Ending 12: Orb's Drain."""
    slow_print("The orb drains your life force, leaving you a hollow shell.")
    slow_print("GAME OVER")

def ending13():
    """Ending 13: Quest for the Throne (Incomplete)."""
    slow_print("Your quest to reclaim your throne is long and arduous.  (This story arc is not yet fully implemented.)")
    slow_print("TO BE CONTINUED...")

def ending14():
    """Ending 14: Guardian Defeated."""
    slow_print("You destroy the corrupted crystal, weakening the guardian and allowing you to defeat it.")
    slow_print("VICTORY!")

def ending15():
    """Ending 15: Poisoned by Traps."""
    slow_print("The poison courses through your veins. You collapse, another victim of the ancient traps.")
    slow_print("GAME OVER")


def play_again():
    choice = input("\nWould you like to play again? (yes/no): ")
    if choice.lower() == "yes":
        game()
    else:
        print("Thank you for playing!")

# --- Main Function ---
def main():
    """Main function to start the game."""
    game()

if __name__ == "__main__":
    main()
