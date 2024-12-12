import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import codecademylib3_seaborn

# Load in the data
df = pd.read_csv("mushroom_data.csv")
print(df.head())

# List of all column headers
columns = df.columns.tolist()

# Iterate over each column and print its name
for column in columns:
    print(column)
    sns.countplot(df[column])  # Plot the countplot for each column
    plt.show()  # Display the plot
    plt.clf()  # Clear the figure for the next plot

plt.xticks(rotation=30, fontsize=10)  # Rotates the x-axis labels and increases font size
plt.xlabel(column, fontsize=12)       # Increases the font size of the x-axis label


plt.title(column + " Value Counts")

sns.countplot(df[column], order=df[column].value_counts().index)


