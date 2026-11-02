import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def get_recommended_level(score):

    if score < 50:
        return ["Beginner"]

    elif score < 70:
        return ["Beginner", "Intermediate"]

    else:
        return ["Intermediate", "Advanced"]


def get_preference_match(preference, resource_style):

    preference_map = {
        "Video": "Visual",
        "Notes": "Reading",
        "Practice": "Practice",
        "Visual": "Visual"
    }

    preferred_style = preference_map.get(
        preference,
        preference
    )

    return preferred_style == resource_style


def get_duration_match(study_hours, duration):

    available_minutes = study_hours * 60

    # Short resource for limited study time
    if available_minutes <= 120:
        return duration <= 30

    # Medium resources for moderate study time
    elif available_minutes <= 180:
        return duration <= 40

    # Longer resources are suitable for more study time
    else:
        return duration >= 30


def create_text_features(student, resources):

    student_text = (
        student["Interest"] + " " +
        student["Weak_Topic"] + " " +
        student["Learning_Preference"] + " " +
        student["Difficulty_Level"]
    )

    resource_text = (
        resources["Subject"] + " " +
        resources["Topic"] + " " +
        resources["Resource_Type"] + " " +
        resources["Learning_Style"] + " " +
        resources["Difficulty_Level"]
    )

    return student_text, resource_text


def recommend_resources(student, resources, top_n=3):

    # Create text features
    student_text, resource_text = create_text_features(
        student,
        resources
    )

    # Combine student and resource text
    all_text = [student_text] + resource_text.tolist()

    # Convert text into numerical vectors
    vectorizer = CountVectorizer()

    vectors = vectorizer.fit_transform(
        all_text
    )

    # Calculate cosine similarity
    similarity_scores = cosine_similarity(
        vectors[0:1],
        vectors[1:]
    )[0]

    # Copy resource data
    recommendations = resources.copy()

    # Add similarity score
    recommendations["Similarity_Score"] = (
        similarity_scores
    )

    # Remove completed topics
    completed_topics = [
        topic.strip()
        for topic in student["Completed_Topics"].split(",")
    ]

    recommendations = recommendations[
        ~recommendations["Topic"].isin(
            completed_topics
        )
    ].copy()

    # Determine suitable difficulty
    suitable_levels = get_recommended_level(
        student["Previous_Score"]
    )

    # Difficulty bonus
    recommendations["Difficulty_Bonus"] = (
        recommendations["Difficulty_Level"]
        .isin(suitable_levels)
        .astype(int) * 0.10
    )

    # Weak topic bonus
    recommendations["Weak_Topic_Bonus"] = (
        recommendations["Topic"]
        == student["Weak_Topic"]
    ).astype(int) * 0.20

    # Learning preference bonus
    recommendations["Preference_Bonus"] = (
        recommendations.apply(
            lambda row:
            get_preference_match(
                student["Learning_Preference"],
                row["Learning_Style"]
            ),
            axis=1
        )
        .astype(int) * 0.10
    )

    # Study duration bonus
    recommendations["Duration_Bonus"] = (
        recommendations.apply(
            lambda row:
            get_duration_match(
                student["Study_Hours"],
                row["Duration_Minutes"]
            ),
            axis=1
        )
        .astype(int) * 0.05
    )

    # Calculate final recommendation score
    recommendations["Final_Score"] = (
        recommendations["Similarity_Score"]
        + recommendations["Difficulty_Bonus"]
        + recommendations["Weak_Topic_Bonus"]
        + recommendations["Preference_Bonus"]
        + recommendations["Duration_Bonus"]
    )

    # Sort recommendations by final score
    recommendations = recommendations.sort_values(
        by="Final_Score",
        ascending=False
    )

    return recommendations.head(top_n)


# Load datasets
students = pd.read_csv(
    "data/students.csv"
)

resources = pd.read_csv(
    "data/resources.csv"
)


# Select first student for testing
student = students.iloc[0]


# Generate recommendations
recommendations = recommend_resources(
    student,
    resources
)


print("\nStudent Profile")
print("-------------------------")

print(
    "Student ID:",
    student["Student_ID"]
)

print(
    "Interest:",
    student["Interest"]
)

print(
    "Learning Preference:",
    student["Learning_Preference"]
)

print(
    "Study Hours:",
    student["Study_Hours"]
)

print(
    "Weak Topic:",
    student["Weak_Topic"]
)

print(
    "Previous Score:",
    student["Previous_Score"]
)

print(
    "Difficulty Level:",
    student["Difficulty_Level"]
)


print("\nRecommended Learning Resources")
print("-------------------------")

for index, resource in recommendations.iterrows():

    score = min(
        resource["Final_Score"] * 100,
        100
    )

    print(
        resource["Resource_Name"],
        "- Match Score:",
        f"{score:.2f}%"
    )