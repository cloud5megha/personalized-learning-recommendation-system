# 🎓 Personalized Learning Recommendation System

## 📌 About the Project

The **Personalized Learning Recommendation System** is a Python-based project that recommends learning resources according to a student's learning profile.

Every student has different learning needs, strengths, weaknesses, and learning preferences. This system analyzes student information and suggests suitable learning materials to make learning more personalized.

It uses **Content-Based Filtering and Rule-Based Scoring** to generate the top 3 learning resource recommendations for each student.

## 🎯 Objectives

- Understand individual student learning needs.
- Identify students' weak topics.
- Recommend suitable learning resources.
- Avoid recommending already completed topics.
- Provide the top 3 personalized recommendations.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Pandas | Data handling and processing |
| NumPy | Numerical calculations |
| Matplotlib | Data visualization |
| Scikit-learn | Similarity calculation |
| CSV | Dataset storage |

## ⚙️ Features

- Student profile management.
- Student and resource dataset processing.
- Weak topic identification.
- Content similarity calculation using Cosine Similarity.
- Rule-based recommendation scoring.
- Completed topic filtering.
- Top 3 learning resource recommendations.
- Graphical data visualization.
- Recommendation results saved as CSV files.
- Evaluation using different performance metrics.

## 📂 Project Structure

```text
Personalized_Learning_Recommendation/
│
├── data/
│   ├── students.csv
│   └── resources.csv
│
├── output/
│   ├── S001_recommendations.csv
│   └── ...
│
├── main.py
├── student.py
├── preprocessing.py
├── recommendation.py
├── eda.py
├── evaluation.py
├── evaluation_graph.py
│
└── README.md
```

## 📊 Dataset Information

The project uses two CSV datasets:

**1. students.csv**
- Student ID
- Student learning profile
- Weak topics
- Completed topics
- Learning preferences
- Study duration
- Other student-related information

**2. resources.csv**
- Resource ID
- Topic
- Resource description
- Difficulty level
- Learning preference
- Duration
- Other resource-related information

**Dataset Size:**
- 100 student records
- 60 learning resource records

*Note: The project uses sample/synthetic dataset records for demonstration and testing.*

## 🔄 How It Works

1. The system loads student and learning resource datasets.
2. It preprocesses the data.
3. It creates a student learning profile.
4. It calculates content similarity using Cosine Similarity.
5. It applies additional rule-based scoring.
6. It filters out completed topics.
7. It ranks the available resources.
8. It displays the top 3 recommendations.
9. It saves the recommendation results in a CSV file.

## 🧮 Recommendation Method

The system uses **Cosine Similarity** to compare student profiles with learning resource descriptions.

It also applies additional scoring bonuses:

- Difficulty Match: 0.10
- Weak Topic Match: 0.20
- Learning Preference Match: 0.10
- Study Duration Match: 0.05

The final scores are used to rank the learning resources.

## 🚀 How to Run the Project

**Step 1: Clone the Repository**

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

**Step 2: Open the Project Folder**

```bash
cd Personalized_Learning_Recommendation
```

**Step 3: Install Required Libraries**

```bash
pip install pandas numpy matplotlib scikit-learn
```

**Step 4: Run the Main Program**

```bash
python main.py
```

**Step 5: Enter Student ID**

Enter a valid Student ID when prompted to generate personalized learning recommendations.

## 📈 Evaluation Metrics

The system evaluates recommendations using:

- Weak Topic Match
- Completed Topic Avoidance
- Suitable Difficulty
- Average Recommendation Score

The project also provides graphical representations of evaluation results.

## 🔮 Future Scope

- Develop a web-based application.
- Add more students and learning resources.
- Track student learning progress.
- Include student feedback.
- Improve recommendation accuracy.
- Add a user-friendly dashboard.

## 👩‍💻 Developed By

**Megha Pal**  
Department of Computational Science  
Brainware University

## 📚 References

- [Python Documentation](https://docs.python.org/3/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [NumPy Documentation](https://numpy.org/doc/)
- [Matplotlib Documentation](https://matplotlib.org/stable/)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)

---

⭐ *This project was developed as part of an academic project to demonstrate personalized learning resource recommendations using Python and Machine Learning concepts.*