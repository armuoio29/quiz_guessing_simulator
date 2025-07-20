"""
Random Guessing Quiz Simulator
Simualtes students guessing answers on a multiple-choice quiz,
records the results, and analyzes passing probabilities.
"""

import random
import csv

# Class for a single quiz question


class QuizQuestion:
    """Represents one multiple-choice quiz questions with a random correct answer"""

    def __init__(self):
        self.correct_answer = random.choice(["A", "B", "C", "D"])

    def check_answer(self, guessed_answer):
        """
        Check if the guessed answer matches the correct answer.

        Args:
            guessed_answer (str): The answer guessed, "A", "B", "C", "D".

        Returns:
            bool: True if the guess is correct, False otherwise.
        """
        return guessed_answer == self.correct_answer

# Class to simulate a quiz with multiple questions


class QuizSimulator:
    """
    Simulates a multiple-choice quiz where each question has a random correct answer,
    and the quiz-taker randomly guesses answers.
    """

    def __init__(self, num_questions=5):
        """
        Initialize the quiz simulator with a specified number of questions.

        Args:
            num_questions (int, optional): The number of questions in the quiz. Defaults to 5.
        """
        self.num_questions = num_questions
        self.questions = [QuizQuestion() for _ in range(self.num_questions)]

    def take_quiz(self):
        """
        Simulate taking the quiz by randomly guessing answers to all questions.

        Returns:
            int: The total number of correct guesses (score).
        """
        score = 0
        for question in self.questions:
            guess = random.choice(["A", "B", "C", "D"])  # Random guess
            if question.check_answer(guess):
                score += 1
        return score

# Function to simulate multiple quiz attempts


def simulate_many_quizzes(num_simulations=1000, passing_score=3):
    """
    Simulate a number of multiple-choice quizzes and analyze how 
    often a random guessing strategy results in passing.

    Args:
        num_simulations (int, optional): The number of quiz attempts 
        to simulate. Defualts to 1000.
        passing_score (int, optional): The minimum number of correct 
        guesses required to pass. Defaults to 3.

    Returns
        list[int]: A list of scores frmo each simulated quiz.
    """
    results = []
    passes = 0

    # Simulate a number of quizzes, each with randomly guessed numbers
    for _ in range(num_simulations):
        # Create a new quiz with a random set of correct answers
        simulator = QuizSimulator()
        score = simulator.take_quiz()
        results.append(score)
        if score >= passing_score:      # Check for a passing score
            passes += 1                 # Increase the count of passed quizzes

    # Calculate the percentage of quizzes that were passed
    pass_rate = passes / num_simulations

    # Display simulation summary
    print(f"Simulated {num_simulations} quizzes")
    print(f"Pass rate (score >= {passing_score}): {pass_rate: .2%}")
    return results

# Save results to CSV file


def save_results_to_csv(scores, filename="quiz_results.csv"):
    """
    Save the quiz results to a CSV file.

    Each row in the CSV will contain the quiz attempt number and the
    corresponding score (quiz attempt,score).

    Args:
        scores (list[int]): A list of quiz scores, one per simulated attempt.
        filename (str, optional): The name of the CSV file to write to.
        Defaults to "quiz_results.csv".

    Returns:
        None
    """
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Quiz Attempt", "Score"])
        for i, score in enumerate(scores):
            writer.writerow([i+1, score])


if __name__ == "__main__":
    results = simulate_many_quizzes(num_simulations=1000)
    save_results_to_csv(results)
