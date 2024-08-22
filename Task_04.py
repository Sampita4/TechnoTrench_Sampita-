import random

# Function to describe a location
def describe_location(location):
    descriptions = {
        "forest": "You are in a dark and eerie forest. The trees tower over you, blocking out the sunlight.",
        "cave": "You enter a cold and damp cave. The sound of dripping water echoes through the darkness.",
        "village": "You arrive at a small village. The villagers seem wary of strangers, but the place feels safe.",
        "mountain": "You find yourself at the base of a tall mountain. The path ahead looks treacherous but promising."
    }
    return descriptions.get(location, "Unknown location")

# Function to handle random events
def random_event():
    events = [
        {"event": "You find a hidden treasure chest!", "points": 10},
        {"event": "A wild animal attacks you!", "points": -5},
        {"event": "You meet a wise old man who gives you advice.", "points": 5},
        {"event": "You fall into a hidden trap!", "points": -10}
    ]
    return random.choice(events)

# Main function to run the game
def adventure_game():
    print("Welcome to the Adventure Game!")
    print("You will explore different locations and face random events.\n")
    
    score = 0
    locations = ["forest", "cave", "village", "mountain"]
    
    while True:
        print("Choose a location to explore:")
        for index, location in enumerate(locations, start=1):
            print(f"{index}. {location.capitalize()}")
        
        # Improved user input handling
        choice = input("Enter the number of your choice (or 0 to quit): ").strip()
        
        if choice == "0":
            print(f"Game over! Your final score is: {score}")
            break
        
        if choice.isdigit() and 1 <= int(choice) <= len(locations):
            choice = int(choice)
            location = locations[choice - 1]
            print(f"\nExploring the {location}...")
            print(describe_location(location))
            
            # Handle random event
            event = random_event()
            print(f"\n{event['event']}")
            score += event['points']
            print(f"Your current score: {score}\n")
        else:
            print("Invalid choice! Please choose a valid location by entering the corresponding number.")

if __name__ == "__main__":
    adventure_game()
