import random
import numpy as np

def gen_win_probability():
    # Cele 9 coloane
    win_prob = 0
    trophy_count = np.random.randint(1000, 9001)
    crt_win_streak = np.random.randint(0, 21)
    win_cons = ["Lava Hound", "Golem", "P.E.K.K.A", "Mega Knight", "Royal Giant", "X-Bow", "Hog Rider", "Wall Breakers", "Goblin Barrel", "Graveyard", "Royal Hogs", "Elixir Golem", "Royal Recruits", "Giant Skeleton", "Goblin Drill"]
    crt_fav_win_con = random.choice(win_cons)
    play_style = ["aggressive", "passive", "balanced"]
    crt_play_style = random.choice(play_style)
    has_evo_unlocked = random.choice([True, False])
    win_percentage = round(np.random.uniform(40.0, 60.0), 2)
    avg_elixir_cost = round(np.random.uniform(2.0, 7.0), 1)
    win_con_level = np.random.randint(11, 16)
    win_prob += 0.005 * trophy_count
    win_prob += 2 * crt_win_streak
    if crt_play_style == "aggressive" or crt_play_style == "defensive":
        win_prob += 10
    elif crt_play_style == "balanced":
        win_prob += 20
    if has_evo_unlocked:
        win_prob += 20
    else:
        win_prob -= 5
    if avg_elixir_cost <= 4.0:
        win_prob += 20
    elif avg_elixir_cost > 4.0:
        win_prob -= 5
    win_prob -= (15 - win_con_level) * 5
    win_prob += (win_percentage - 50) * 5
    win = np.random.randint(0, 101)
    if win < win_prob:
        win = 0
    else:
        win = 1

    win = {
        "Trophy_Count" : trophy_count,
        "Current_Win_Streak" : crt_win_streak,
        "Favourite_Win_Condition" : crt_fav_win_con,
        "Play_Style" : crt_play_style,
        "Evolution" : has_evo_unlocked,
        "Win_Percentage" : win_percentage,
        "Average_Elixir_Cost" : avg_elixir_cost,
        "Win_Condition_Level" : win_con_level,
        "Win_Probability" : win_prob,
        "Win": win
    }
    return win