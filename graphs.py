import seaborn as sns
import matplotlib.pyplot as plt

def get_histogram(data_frame, choice):
    numerical_charact = ["Trophy_Count", "Current_Win_Streak", "Win_Percentage", "Average_Elixir_Cost", "Win_Condition_Level", "Win_Probability"]
    for i in numerical_charact:
        plt.figure(figsize = (10, 5))
        sns.histplot(data_frame[i], kde = True, bins = 30, color = 'blue')
        plt.title(f"{i}")
        plt.xlabel(i)
        plt.ylabel("Frequency")
        if choice == 0:
            plt.savefig(f"{i}_train.jpg")
        elif choice == 1:
            plt.savefig(f"{i}_test.jpg")
        plt.close()

def get_countplot(data_frame, choice):
    categorial_charact = ["Favourite_Win_Condition", "Play_Style"]
    for i in categorial_charact:
        plt.figure(figsize = (15, 10))
        sns.countplot(data = data_frame, x = i, hue = i, palette = 'deep', legend = True)
        plt.title(f"{i}")
        plt.ylabel("Frequency")
        plt.xticks(rotation = 30)
        if choice == 0:
            plt.savefig(f"{i}_train.png")
        elif choice == 1:
            plt.savefig(f"{i}_test.png")
        plt.tight_layout()
        plt.close()