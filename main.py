import pandas as pd
from sklearn.model_selection import train_test_split
from determine_win import gen_win_probability as get_win

win = []
for i in range(1000):
    win.append(get_win())

data_frame = pd.DataFrame(win)

train, test = train_test_split(data_frame, train_size = 700, test_size = 300, random_state = 42, shuffle = True)

train.to_csv("Clash_Royale_train_csv", index = False)
test.to_csv("Clash_Royale_test_csv", index = False)