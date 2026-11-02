import pandas as pd


def load_data():
    students = pd.read_csv("data/students.csv")
    resources = pd.read_csv("data/resources.csv")

    return students, resources


def clean_data(students, resources):

    # Check for missing values
    print("\nMissing values in Students Dataset:")
    print(students.isnull().sum())

    print("\nMissing values in Resources Dataset:")
    print(resources.isnull().sum())

    # Remove duplicate rows
    students = students.drop_duplicates()
    resources = resources.drop_duplicates()

    return students, resources


def encode_data(students, resources):

    # Convert categorical student columns into numerical values
    student_encoded = pd.get_dummies(
        students,
        columns=[
            "Interest",
            "Learning_Preference",
            "Difficulty_Level"
        ]
    )

    # Convert categorical resource columns into numerical values
    resource_encoded = pd.get_dummies(
        resources,
        columns=[
            "Subject",
            "Resource_Type",
            "Difficulty_Level",
            "Learning_Style"
        ]
    )

    return student_encoded, resource_encoded

def create_features(students, resources):

    student_features = pd.DataFrame()

    student_features["Subject"] = students["Interest"]
    student_features["Topic"] = students["Weak_Topic"]
    student_features["Learning_Style"] = students["Learning_Preference"]
    student_features["Difficulty"] = students["Difficulty_Level"]

    resource_features = pd.DataFrame()

    resource_features["Subject"] = resources["Subject"]
    resource_features["Topic"] = resources["Topic"]
    resource_features["Learning_Style"] = resources["Learning_Style"]
    resource_features["Difficulty"] = resources["Difficulty_Level"]

    return student_features, resource_features

# Load datasets
students, resources = load_data()

# Clean datasets
students, resources = clean_data(students, resources)

# Encode categorical data
student_encoded, resource_encoded = encode_data(
    students, resources
)

print("\nEncoded Student Dataset:")
print(student_encoded)

print("\nEncoded Resource Dataset:")
print(resource_encoded)

# Create common features
student_features, resource_features = create_features(
    students, resources
)

print("\nStudent Features:")
print(student_features)

print("\nResource Features:")
print(resource_features)