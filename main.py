
import pandas as pd
import matplotlib.pyplot as plt

from recommendation import recommend_resources
from student import Student


# Display recommendations in Shell
def display_recommendations(student, recommendations):

    print("\n==============================")
    print("  PERSONALIZED RECOMMENDATIONS")
    print("==============================")

    for number, (index, resource) in enumerate(
        recommendations.iterrows(), start=1
    ):

        score = min(resource["Final_Score"] * 100, 100)

        print(f"\n{number}. {resource['Resource_Name']}")
        print("   Subject:", resource["Subject"])
        print("   Topic:", resource["Topic"])
        print("   Type:", resource["Resource_Type"])
        print("   Difficulty:", resource["Difficulty_Level"])
        print(f"   Match Score: {score:.2f}%")

        if resource["Topic"] == student.weak_topic:
            print("   Reason: Matches your weak topic.")

        elif resource["Subject"] == student.interest:
            print("   Reason: Matches your area of interest.")

        else:
            print("   Reason: Matches your learning profile.")



# Display recommendations in Graph format
def display_recommendation_graph(recommendations):

    # Get resource names
    resource_names = recommendations["Resource_Name"]

    # Calculate match scores
    match_scores = (
        recommendations["Final_Score"] * 100
    ).clip(upper=100)

    # Create figure with two sections
    fig, (ax1, ax2) = plt.subplots(
        2, 1,
        figsize=(12, 9),
        gridspec_kw={"height_ratios": [2, 1]}
    )

    # -------------------------------
    # BAR GRAPH
    # -------------------------------

    bars = ax1.bar(
        resource_names,
        match_scores
    )

    ax1.set_title(
        "Top 3 Personalized Learning Recommendations",
        fontsize=14,
        fontweight="bold"
    )

    ax1.set_xlabel("Learning Resources")
    ax1.set_ylabel("Match Score (%)")

    ax1.set_ylim(0, 115)

    ax1.tick_params(
        axis="x",
        rotation=15
    )

    # Display percentage above bars
    for bar, score in zip(bars, match_scores):

        ax1.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 2,
            f"{score:.2f}%",
            ha="center",
            fontsize=10
        )

    # -------------------------------
    # RESOURCE DETAILS TABLE
    # -------------------------------

    table_data = []

    for number, (index, resource) in enumerate(
        recommendations.iterrows(), start=1
    ):

        table_data.append([
            number,
            resource["Resource_Name"],
            resource["Topic"],
            resource["Difficulty_Level"],
            resource["Learning_Style"],
            f"{min(resource['Final_Score'] * 100, 100):.2f}%"
        ])

    columns = [
        "Rank",
        "Resource Name",
        "Topic",
        "Difficulty",
        "Learning Style",
        "Match Score"
    ]

    ax2.axis("off")

    ax2.set_title(
        "Recommended Resource Details",
        fontsize=12,
        fontweight="bold",
        pad=12
    )

    table = ax2.table(
        cellText=table_data,
        colLabels=columns,
        cellLoc="center",
        loc="center"
    )

    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1, 2)

    # Adjust layout
    plt.tight_layout()

    # Display graph and table
    plt.show()


# Save recommendations in CSV file
def save_recommendations(student, recommendations):

    output_data = []

    for number, (index, resource) in enumerate(
        recommendations.iterrows(), start=1
    ):

        score = min(resource["Final_Score"] * 100, 100)

        output_data.append({
            "Student_ID": student.student_id,
            "Recommendation_Rank": number,
            "Resource_Name": resource["Resource_Name"],
            "Subject": resource["Subject"],
            "Topic": resource["Topic"],
            "Resource_Type": resource["Resource_Type"],
            "Difficulty_Level": resource["Difficulty_Level"],
            "Match_Score": round(score, 2)
        })

    output_df = pd.DataFrame(output_data)

    filename = (
        "output/"
        + student.student_id
        + "_recommendations.csv"
    )

    output_df.to_csv(filename, index=False)

    print("\nRecommendations saved to:", filename)


# Main function
def main():

    try:

        # Load datasets
        students = pd.read_csv("data/students.csv")
        resources = pd.read_csv("data/resources.csv")

        print("======================================")
        print(" PERSONALIZED LEARNING RECOMMENDATION")
        print("======================================")

        print("\nAvailable Student IDs:")

        for student_id in students["Student_ID"]:
            print(student_id)

        student_id = input(
            "\nEnter Student ID: "
        ).strip().upper()

        student_data = students[
            students["Student_ID"] == student_id
        ]

        if student_data.empty:

            print("\nStudent ID not found.")

            return

        data = student_data.iloc[0]

        # Create Student object
        student = Student(
            data["Student_ID"],
            data["Previous_Score"],
            data["Study_Hours"],
            data["Interest"],
            data["Learning_Preference"],
            data["Completed_Topics"],
            data["Weak_Topic"],
            data["Difficulty_Level"]
        )

        # Display student profile
        student.display_profile()

        # Generate recommendations
        recommendations = recommend_resources(
            data,
            resources
        )

        if recommendations.empty:
            print("\nNo suitable recommendations found.")
            return

        # Display recommendations in Shell
        display_recommendations(
            student,
            recommendations
        )

        # Display recommendations in Graph
        display_recommendation_graph(
            recommendations
        )

        # Save recommendations
        save_recommendations(
            student,
            recommendations
        )

    except FileNotFoundError:

        print("\nError: Required dataset file was not found.")

    except KeyError as error:

        print("\nError: Required column is missing:", error)

    except Exception as error:

        print("\nAn unexpected error occurred:", error)


# Run main function
main()
