import pandas as pd
import matplotlib.pyplot as plt


# Load student dataset
students = pd.read_csv("data/students.csv")


# Display basic information
print("Student Dataset Information")
print("---------------------------")

print("Number of Students:", len(students))

print("\nAverage Previous Score:",
      students["Previous_Score"].mean())

print("Average Study Hours:",
      students["Study_Hours"].mean())


# -------------------------------
# Graph 1: Previous Score
# -------------------------------

plt.figure(figsize=(8, 5))

plt.hist(
    students["Previous_Score"],
    bins=5,
    edgecolor="black"
)

plt.title("Distribution of Previous Scores")
plt.xlabel("Previous Score")
plt.ylabel("Number of Students")

plt.show()


# -------------------------------
# Graph 2: Study Hours
# -------------------------------

plt.figure(figsize=(8, 5))

plt.bar(
    students["Student_ID"],
    students["Study_Hours"]
)

plt.title("Study Hours of Students")
plt.xlabel("Student ID")
plt.ylabel("Study Hours per Day")

plt.xticks(rotation=45)

plt.show()


# -------------------------------
# Graph 3: Student Interests
# -------------------------------

interest_counts = students["Interest"].value_counts()

plt.figure(figsize=(8, 5))

plt.bar(
    interest_counts.index,
    interest_counts.values
)

plt.title("Student Interests")
plt.xlabel("Subject")
plt.ylabel("Number of Students")

plt.xticks(rotation=45)

plt.show()


# -------------------------------
# Graph 4: Learning Preferences
# -------------------------------

preference_counts = students[
    "Learning_Preference"
].value_counts()

plt.figure(figsize=(8, 5))

plt.bar(
    preference_counts.index,
    preference_counts.values
)

plt.title("Learning Preferences")
plt.xlabel("Learning Preference")
plt.ylabel("Number of Students")

plt.show()

# -------------------------------
# Graph 5: Average Score by Interest
# -------------------------------

average_score = students.groupby(
    "Interest"
)["Previous_Score"].mean()

plt.figure(figsize=(8, 5))

plt.bar(
    average_score.index,
    average_score.values
)

plt.title("Average Previous Score by Interest")
plt.xlabel("Interest")
plt.ylabel("Average Score")

plt.xticks(rotation=45)

plt.show()


# -------------------------------
# Graph 6: Study Hours vs Score
# -------------------------------

plt.figure(figsize=(8, 5))

plt.scatter(
    students["Study_Hours"],
    students["Previous_Score"]
)

plt.title("Study Hours vs Previous Score")
plt.xlabel("Study Hours per Day")
plt.ylabel("Previous Score")

plt.show()


# -------------------------------
# Graph 7: Difficulty Level
# -------------------------------

difficulty_counts = students[
    "Difficulty_Level"
].value_counts()

plt.figure(figsize=(7, 7))

plt.pie(
    difficulty_counts.values,
    labels=difficulty_counts.index,
    autopct="%1.1f%%"
)

plt.title("Student Difficulty Levels")

plt.show()


# -------------------------------
# Graph 8: Weak Topics
# -------------------------------

weak_topic_counts = students[
    "Weak_Topic"
].value_counts()

plt.figure(figsize=(9, 5))

plt.bar(
    weak_topic_counts.index,
    weak_topic_counts.values
)

plt.title("Distribution of Weak Topics")
plt.xlabel("Weak Topic")
plt.ylabel("Number of Students")

plt.xticks(rotation=45)

plt.show()


# -------------------------------
# Graph 9: Study Hours by Learning Preference
# -------------------------------

average_study_hours = students.groupby(
    "Learning_Preference"
)["Study_Hours"].mean()

plt.figure(figsize=(8, 5))

plt.bar(
    average_study_hours.index,
    average_study_hours.values
)

plt.title("Average Study Hours by Learning Preference")
plt.xlabel("Learning Preference")
plt.ylabel("Average Study Hours")

plt.show()