import pandas as pd
import numpy as np

from recommendation import recommend_resources


def evaluate_recommendations(students, resources):

    total_students = len(students)

    weak_topic_matches = 0
    completed_topic_errors = 0
    suitable_difficulty = 0

    all_scores = []

    for index, student in students.iterrows():

        recommendations = recommend_resources(
            student,
            resources
        )

        # Check weak topic
        if any(
            recommendations["Topic"] == student["Weak_Topic"]
        ):
            weak_topic_matches += 1

        # Check completed topics
        completed_topics = [
            topic.strip()
            for topic in student["Completed_Topics"].split(",")
        ]

        for topic in recommendations["Topic"]:

            if topic in completed_topics:
                completed_topic_errors += 1

        # Check suitable difficulty
        score = student["Previous_Score"]

        if score < 50:
            suitable_levels = ["Beginner"]

        elif score < 70:
            suitable_levels = [
                "Beginner",
                "Intermediate"
            ]

        else:
            suitable_levels = [
                "Intermediate",
                "Advanced"
            ]

        for level in recommendations["Difficulty_Level"]:

            if level in suitable_levels:
                suitable_difficulty += 1

        # Store recommendation scores
        for final_score in recommendations["Final_Score"]:

            # Keep score between 0 and 1
            final_score = min(final_score, 1.0)

            all_scores.append(final_score)

    total_recommendations = len(all_scores)

    # Calculate evaluation percentages
    weak_topic_percentage = (
        weak_topic_matches / total_students
    ) * 100

    completed_topic_percentage = (
        1 -
        (
            completed_topic_errors /
            total_recommendations
        )
    ) * 100

    difficulty_percentage = (
        suitable_difficulty /
        total_recommendations
    ) * 100

    # Use NumPy to calculate average
    average_score = np.mean(all_scores) * 100

    print("\n======================================")
    print("       RECOMMENDATION EVALUATION")
    print("======================================")

    print(
        "\nWeak Topic Match:",
        f"{weak_topic_percentage:.2f}%"
    )

    print(
        "Completed Topic Avoidance:",
        f"{completed_topic_percentage:.2f}%"
    )

    print(
        "Suitable Difficulty:",
        f"{difficulty_percentage:.2f}%"
    )

    print(
        "Average Recommendation Score:",
        f"{average_score:.2f}%"
    )


# Load datasets
students = pd.read_csv("data/students.csv")
resources = pd.read_csv("data/resources.csv")


# Evaluate recommendation system
evaluate_recommendations(
    students,
    resources
)