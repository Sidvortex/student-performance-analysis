#Student Performance Analysis

# Step 1: Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Load Dataset
df = pd.read_csv("StudentsPerformance.csv")

# Step 3: Basic Info
print("\n--- Dataset Info ---")
print(df.info())
print("\n--- Summary Statistics ---")
print(df.describe())

# Step 4: Rename Columns
df.columns = ['Gender', 'Race', 'Parental_Education', 'Lunch', 'Test_Prep',
              'Math_Score', 'Reading_Score', 'Writing_Score']

# Step 5: Average Scores
print("\n--- Average Scores ---")
print("Average Math Score:", df['Math_Score'].mean())
print("Average Reading Score:", df['Reading_Score'].mean())
print("Average Writing Score:", df['Writing_Score'].mean())

# Step 6: Visualizations

# Gender vs Math Score
sns.barplot(x='Gender', y='Math_Score', data=df)
plt.title("Math Score by Gender")
plt.show()

# Test Prep vs Math Score
sns.boxplot(x='Test_Prep', y='Math_Score', data=df)
plt.title("Test Preparation vs Math Score")
plt.show()

# Correlation Heatmap
sns.heatmap(df[['Math_Score','Reading_Score','Writing_Score']].corr(), annot=True, cmap='Blues')
plt.title("Subject Score Correlation")
plt.show()

# Parental Education vs Math Score
plt.figure(figsize=(8,4))
sns.barplot(x='Parental_Education', y='Math_Score', data=df)
plt.xticks(rotation=45)
plt.title("Parental Education vs Math Score")
plt.show()

# Average Scores Bar Chart
df[['Math_Score', 'Reading_Score', 'Writing_Score']].mean().plot(
    kind='bar', color=['#6A5ACD','#20B2AA','#FF7F50'])
plt.title("Average Scores by Subject")
plt.ylabel("Score")
plt.show()

# Step 7: Summary Insights
print("\n--- Key Insights ---")
print("1. Students who completed test prep scored higher in all subjects.")
print("2. Females performed better in Reading & Writing, males slightly higher in Math.")
print("3. Reading & Writing scores are strongly correlated.")
print("4. Higher parental education slightly improves performance.")
