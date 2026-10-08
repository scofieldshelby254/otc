"""A short interactive quiz for the Week 1 programming portfolio."""


# Each question stores its prompt, accepted answer, and a helpful explanation.
QUESTIONS = [
    {
        "prompt": "What is the name of the planet we live on?",
        "answer": "earth",
        "fact": "Earth is the third planet from the Sun.",
    },
    {
        "prompt": "How many sides does a triangle have?",
        "answer": "3",
        "fact": "A triangle has three sides.",
    },
    {
        "prompt": "Which ocean is the largest on Earth?",
        "answer": "pacific",
        "fact": "The Pacific Ocean is the largest ocean.",
    },
    {
        "prompt": "What is 5 multiplied by 6?",
        "answer": "30",
        "fact": "5 multiplied by 6 equals 30.",
    },
    {
        "prompt": "What gas do plants absorb from the air?",
        "answer": "carbon dioxide",
        "fact": "Plants absorb carbon dioxide during photosynthesis.",
    },
]


def get_player_name():
    """Ask for a name and keep asking until the player enters one."""
    while True:
        name = input("What is your name? ").strip()
        if name:
            return name
        print("Please enter a name so we know who is playing.")


def ask_question(question, question_number):
    """Display one question and return whether the player's answer is right."""
    print(f"\nQuestion {question_number}: {question['prompt']}")
    answer = input("Your answer: ").strip().casefold()

    if answer == question["answer"]:
        print("Correct!")
        return True

    print(f"Not quite. {question['fact']}")
    return False


def run_quiz(name):
    """Ask every question, count correct answers, and show the final result."""
    score = 0
    print(f"\nWelcome to the quiz, {name}!")

    for question_number, question in enumerate(QUESTIONS, start=1):
        if ask_question(question, question_number):
            score += 1

    print(f"\n{name}, you scored {score} out of {len(QUESTIONS)}.")
    if score == len(QUESTIONS):
        print("Perfect score! Amazing work.")
    elif score >= len(QUESTIONS) // 2:
        print("Nice job! Keep learning.")
    else:
        print("Good try! Play again to improve your score.")


def main():
    """Start the quiz by greeting the player and running the questions."""
    print("=== The Quick Knowledge Quiz ===")
    player_name = get_player_name()
    run_quiz(player_name)


# Run the quiz only when this file is started directly.
if __name__ == "__main__":
    main()