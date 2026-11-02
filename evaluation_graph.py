import matplotlib.pyplot as plt


# Evaluation results
metrics = [
    "Weak Topic Match",
    "Completed Topic Avoidance",
    "Suitable Difficulty",
    "Average Recommendation Score"
]

scores = [
    97.00,
    100.00,
    83.33,
    85.36
]


# Create bar chart
plt.figure(figsize=(9, 5))

plt.bar(metrics, scores)

plt.title("Recommendation System Evaluation")
plt.xlabel("Evaluation Metrics")
plt.ylabel("Percentage (%)")

plt.ylim(0, 110)

plt.xticks(rotation=20)

# Display values above bars
for i, score in enumerate(scores):
    plt.text(
        i,
        score + 2,
        f"{score:.2f}%",
        ha="center"
    )

plt.tight_layout()
plt.show()