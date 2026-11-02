class Student:

    def __init__(
        self,
        student_id,
        previous_score,
        study_hours,
        interest,
        learning_preference,
        completed_topics,
        weak_topic,
        difficulty_level
    ):
        self.student_id = student_id
        self.previous_score = previous_score
        self.study_hours = study_hours
        self.interest = interest
        self.learning_preference = learning_preference
        self.completed_topics = completed_topics
        self.weak_topic = weak_topic
        self.difficulty_level = difficulty_level

    def display_profile(self):

        print("\n==============================")
        print("       STUDENT PROFILE")
        print("==============================")

        print("Student ID:", self.student_id)
        print("Previous Score:", self.previous_score)
        print("Study Hours:", self.study_hours)
        print("Interest:", self.interest)
        print("Learning Preference:", self.learning_preference)
        print("Completed Topics:", self.completed_topics)
        print("Weak Topic:", self.weak_topic)
        print("Difficulty Level:", self.difficulty_level)