import pandas as pd
from sklearn.model_selection import train_test_split
from determine_win import gen_win
from find_and_elim_missing_values import elim_missing_values
from plots import get_histogram, get_countplot, get_outliers, get_heatmap, get_violin_plot
from sklearn.ensemble import RandomForestRegressor

# Generez aleatoriu 1000 de numere pt cele 10 coloane
win = []
for i in range(1000):
    win.append(gen_win())

data_frame = pd.DataFrame(win)
train, test = train_test_split(data_frame, train_size = 700, test_size = 300, random_state = 42, shuffle = True)
train.to_csv("Clash_Royale_train.csv", index = False)
test.to_csv("Clash_Royale_test.csv", index = False)
train_data_frame = pd.read_csv("Clash_Royale_train.csv")
test_data_frame = pd.read_csv("Clash_Royale_test.csv")


m, n = train_data_frame.shape
p, q = test_data_frame.shape
train_data_frame, missing1 = elim_missing_values(train_data_frame)
test_data_frame, missing2 = elim_missing_values(test_data_frame)
print("Valorile lipsa din dataframe-ul de training sunt in numar de", missing1, ",ceea ce reprezinta", round(missing1 * 100 / m, 2), "% din totalul de", m)
print("Valorile lipsa din dataframe-ul de testing sunt in numar de", missing2, ",ceea ce reprezinta", round(missing2 * 100 / p, 2), "% din totalul de", p)


train_data_frame.to_csv("Clash_Royale_Train_Removed_Missing_Values.csv", index = False)
test_data_frame.to_csv("Clash_Royale_Test_Removed_Missing_Values.csv", index = False)
train_data_frame = pd.read_csv("Clash_Royale_Train_Removed_Missing_Values.csv")
test_data_frame = pd.read_csv("Clash_Royale_Test_Removed_Missing_Values.csv")

print("\nStatistici descriptive:")
print(train_data_frame.describe(include = [float, int, 'category']))
print("\n")
print(test_data_frame.describe(include = [float, int, 'category']))
print("\n")

# 0 pentru train si 1 pentru test; jpg pentru histograma si png pentru countplot

# Histograma pentru caracteristici numerice
get_histogram(train_data_frame, 0)
get_histogram(test_data_frame, 1)

# Countplot pentru variabilele categorice
get_countplot(train_data_frame, 0)
get_countplot(test_data_frame, 1)

# Boxplot pentru valorile aberante
get_outliers(train_data_frame, 0)
get_outliers(test_data_frame, 1)

# Heatmap pentru variabilele numerice
get_heatmap(train_data_frame, 0)
get_heatmap(test_data_frame, 1)

# Violinplot pentru win si variabilele de care depinde
get_violin_plot(train_data_frame, 0)
get_violin_plot(test_data_frame, 1)

# Random Forest cu One-Hot Encoding pentru variabilele categorice
X_train, y_train = train_data_frame.drop(columns = ["Win"]), train_data_frame["Win"]
X_test, y_test = test_data_frame.drop(columns = ["Win"]), test_data_frame["Win"]
X_train, X_test = pd.get_dummies(X_train), pd.get_dummies(X_test)
rand_forest = RandomForestRegressor(random_state = 42)
rand_forest.fit(X_train, y_train)
y_predict = rand_forest.predict(X_test)