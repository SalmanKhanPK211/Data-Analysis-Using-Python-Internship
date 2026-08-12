import pandas as pd
import matplotlib.pyplot as plt


# Load the cleaned dataset
df = pd.read_csv("cleaned_netflix_dataset.csv")


# Display the first five rows
print(df.head())


# Display dataset shape
print("\nDataset Shape:")
print(df.shape)


# Identify unique content types
print("\nContent Types:")
print(df["type"].unique())


# Count Movies and TV Shows
content_counts = df["type"].value_counts()

print("\nContent Type Counts:")
print(content_counts)


# Calculate content proportions
content_percentages = (content_counts / len(df)) * 100

# Round percentages to two decimal places
content_percentages = content_percentages.round(2)

print("\nContent Type Percentages:")
print(content_percentages)


# Bar Chart: Number of Movies and TV Shows
content_counts.plot(kind="bar")

plt.title("Netflix Content Type Distribution")
plt.xlabel("Content Type")
plt.ylabel("Number of Titles")
plt.xticks(rotation=0)

plt.show()


# Pie Chart: Content Proportions
plt.figure(figsize=(7, 7))

plt.pie(
    content_counts,
    labels=content_counts.index,
    autopct="%1.1f%%"
)

plt.title("Netflix Movies vs TV Shows")

plt.show()


# Display final summary
print("\nKey Findings:")
print(f"Total Netflix titles: {len(df)}")
print(f"Movies: {content_counts['Movie']} ({content_percentages['Movie']}%)")
print(f"TV Shows: {content_counts['TV Show']} ({content_percentages['TV Show']}%)")