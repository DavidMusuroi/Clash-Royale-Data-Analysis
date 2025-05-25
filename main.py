import pandas as pd
from sklearn.model_selection import train_test_split
from determine_win import gen_win
from find_and_elim_missing_values import elim_missing_values

win = []
for i in range(1000):
    win.append(gen_win())

data_frame = pd.DataFrame(win)
train, test = train_test_split(data_frame, train_size = 700, test_size = 300, random_state = 42, shuffle = True)
train.to_csv("Clash_Royale_train.csv", index = False)
test.to_csv("Clash_Royale_test.csv", index = False)

train_data_frame = pd.read_csv("Clash_Royale_train.csv")
train_data_frame, missing1 = elim_missing_values(train_data_frame)

test_data_frame = pd.read_csv("Clash_Royale_test.csv")
test_data_frame, missing2 = elim_missing_values(test_data_frame)

m, n = train_data_frame.shape
p, q = test_data_frame.shape

print("Valorile lipsa din dataframe-ul de training sunt in numar de", missing1, ",ceea ce reprezinta", round(missing1 * 100 / m, 2), "% din totalul de", m)
print("Valorile lipsa din dataframe-ul de testing sunt in numar de", missing2, ",ceea ce reprezinta", round(missing2 * 100 / p, 2), "% din totalul de", p)



#print(train_data_frame.describe)
#print(test.describe(include = 'all'))