import pandas as pd
from sklearn.model_selection import train_test_split
from src.determine_win import gen_win
from src.find_and_elim_missing_values import elim_missing_values
from src.plots import *
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Randomly generating 1000 numbers for the 10 columns
win = []
for i in range(1000):
    win.append(gen_win())

# Creating the initial dataframe
data_frame = pd.DataFrame(win)
train, test = train_test_split(data_frame, train_size = 700, test_size = 300, random_state = 42, shuffle = True)
train.to_csv("Clash_Royale_train.csv", index = False)
test.to_csv("Clash_Royale_test.csv", index = False)
train_data_frame = pd.read_csv("Clash_Royale_train.csv")
test_data_frame = pd.read_csv("Clash_Royale_test.csv")

# Eliminating the missing values
m, n = train_data_frame.shape
p, q = test_data_frame.shape
train_data_frame, missing1 = elim_missing_values(train_data_frame)
test_data_frame, missing2 = elim_missing_values(test_data_frame)
print("Valorile lipsa din dataframe-ul de training sunt in numar de", missing1, ",ceea ce reprezinta", round(missing1 * 100 / m, 2), "% din totalul de", m)
print("Valorile lipsa din dataframe-ul de testing sunt in numar de", missing2, ",ceea ce reprezinta", round(missing2 * 100 / p, 2), "% din totalul de", p)


# Placing the values in new CSVs
train_data_frame.to_csv("Clash_Royale_Train_Removed_Missing_Values.csv", index = False)
test_data_frame.to_csv("Clash_Royale_Test_Removed_Missing_Values.csv", index = False)
train_data_frame = pd.read_csv("Clash_Royale_Train_Removed_Missing_Values.csv")
test_data_frame = pd.read_csv("Clash_Royale_Test_Removed_Missing_Values.csv")

# Determining the descriptive statistics
print("\nStatistici descriptive:")
print(train_data_frame.describe(include = [float, int, 'category']))
print("\n")
print(test_data_frame.describe(include = [float, int, 'category']))
print("\n")

# I used 0 for training & 1 for testing

# Histogram for the numerical characteristics
get_histogram(train_data_frame, 0)
get_histogram(test_data_frame, 1)

# Countplot for the categorial variables
get_countplot(train_data_frame, 0)
get_countplot(test_data_frame, 1)

# Boxplot for the outliers
get_outliers(train_data_frame, 0)
get_outliers(test_data_frame, 1)

# Heatmap for the numerical variables
get_heatmap(train_data_frame, 0)
get_heatmap(test_data_frame, 1)

# Violinplot for the win and the variables it is depended on
get_violin_plot(train_data_frame, 0)
get_violin_plot(test_data_frame, 1)

# Random Forest with One-Hot Encoding for the categorial variables
X_train, y_train = train_data_frame.drop(columns = ["Win"]), train_data_frame["Win"]
X_test, y_test = test_data_frame.drop(columns = ["Win"]), test_data_frame["Win"]
X_train, X_test = pd.get_dummies(X_train), pd.get_dummies(X_test)
rand_forest = RandomForestClassifier(random_state = 42)
rand_forest.fit(X_train, y_train)
y_predict = rand_forest.predict(X_test)

# Determining accuracy
accuracy = accuracy_score(y_test, y_predict)
accuracy = 100 * accuracy
accuracy = round(accuracy, 2)
print(f"The accuracy of the model is: {accuracy}%")

# Determining the confusion matrix and the heatmap
cm = confusion_matrix(y_test, y_predict)
plt.figure(figsize = (10, 5))
sns.heatmap(cm, annot = True, fmt = 'd', cmap = 'Blues', xticklabels = ["Lose", "Win"], yticklabels = ["Lose", "Win"])
plt.title("Confusion Matrix (MNIST)")
plt.xlabel("Predicted Label")
plt.ylabel("Real Label")
plt.tight_layout()
plt.savefig("Confusion Matrix.jpg")
