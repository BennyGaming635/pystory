import random

genres = ["Fantasy", "Horror", "Sci-Fi", "Romance", "Mystery"]
settings = ["forest", "space station", "haunted house", "castle", "desert"]
characters = ["Alice", "Bob", "Charlie", "Eve", "Megan", "John"]
adjectives = ["brave", "mysterious", "daring", "fearless", "intrepid", "curious"]
conflicts = {
    "Fantasy": ["a terrible curse", "a rival wizard", "a group of bandits", "an ancient prophecy"],
    "Horror": ["a ghostly apparition", "a terrifying monster", "a strange illness", "a series of horrifying dreams"],
    "Sci-Fi": ["a rogue AI", "an intergalactic war", "an alien invasion", "a time-travel paradox"],
    "Romance": ["unrequited love", "a misunderstanding", "a love triangle", "a long-distance relationship"],
    "Mystery": ["a missing person", "an unsolved crime", "a secret organization", "a hidden treasure"]
}

actions = {
    "Fantasy": ["fights a dragon", "casts a spell", "finds a magical artifact", "journeys to a distant land"],
    "Horror": ["is chased by a ghost", "enters a haunted house", "fights a monster", "uncovers dark secrets"],
    "Sci-Fi": ["discovers a new planet", "encounters aliens", "travels through a wormhole", "starts a robot revolution"],
    "Romance": ["meets their true love", "experiences a heartbreak", "falls in love in an unexpected place", "goes on a romantic adventure"],
    "Mystery": ["solves a crime", "unravels a conspiracy", "finds a hidden treasure", "decodes an ancient mystery"]
}

endings = ["and lives happily ever after.", "and disappears mysteriously.", "and uncovers the truth.", "and learns a life-changing lesson."]

def get_random_element(category):
    return random.choice(category)

def generate_long_story():
    # Select random parameters
    genre = get_random_element(genres)
    setting = get_random_element(settings)
    character = get_random_element(characters)
    adjective = get_random_element(adjectives)
    conflict = get_random_element(conflicts[genre])
    action = get_random_element(actions[genre])
    ending = get_random_element(endings)

    first_paragraph = (
        f"Once upon a time, in a {setting}, there was a {adjective} character named {character}. "
        f"One fateful day, they encountered {conflict}, which threatened everything they held dear. "
        f"With no time to lose, {character} embarked on a daring journey to overcome this obstacle. "
        f"Along the way, they faced numerous challenges and met strange allies. As they ventured deeper into the heart of danger, "
        f"they discovered a hidden power within themselves. But the road ahead was fraught with peril, and {character} knew they would need all their courage to survive."
    )

    second_paragraph = (
        f"At the climax of their journey, {character} {action}, confronting their greatest fear. "
        f"Amidst the chaos, unexpected twists kept them on edge, but they never wavered. With determination and quick thinking, "
        f"they managed to find a solution that no one else could have imagined. In the end, {character} emerged victorious, having "
        f"defeated the odds and restored peace. Their journey came to a close as they {ending}."
    )

    story = first_paragraph + "\n\n" + second_paragraph
    return story

def main():
    print("Welcome to PyStory!")
    while True:
        # Ask the user if they want to generate a story
        user_input = input("\nDo you want to generate a random story? (yes/no): ").strip().lower()
        if user_input == "yes":
            print("\nHere's your random story:")
            print(generate_long_story())
        elif user_input == "no":
            print("Goodbye!")
            break
        else:
            print("Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()
