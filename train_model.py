import os
import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report, accuracy_score

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(BASE_DIR, "data", "training_dataset.csv")

# Load dataset
df = pd.read_csv(data_path)

X = df[["skills", "years_experience"]]
y = df["department"]

# Train/Test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        ("text", TfidfVectorizer(
            ngram_range=(1,2),
            max_features=500
        ), "skills"),
        ("num", StandardScaler(), ["years_experience"]),
    ]
)

# Stronger classifier
model_pipeline = Pipeline(
    steps=[
        ("preprocessing", preprocessor),
        ("classifier", LinearSVC())
    ]
)

# Train
model_pipeline.fit(X_train, y_train)

# Evaluate
y_pred = model_pipeline.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# Save trained pipeline
model_path = os.path.join(BASE_DIR, "model.pkl")
pickle.dump(model_pipeline, open(model_path, "wb"))

print("\nImproved model trained and saved successfully.")