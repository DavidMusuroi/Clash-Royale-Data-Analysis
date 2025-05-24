import random
import numpy as np

random.seed(1)
np.random.seed(1)

def gen_win_probability():
    win_prob = 0
    trophy_count = np.random.randint(1000, 9001)
    crt_win_streak = np.random.randint(0, 21)
    win_cons = ["Lava Hound", "Golem", "P.E.K.K.A", "Mega Knight", "Royal Giant", "X-Bow", "Hog Rider", "Wall Breakers", "Goblin Barrel", "Graveyard", "Royal Hogs", "Elixir Golem", "Royal Recruits", "Giant Skeleton", "Goblin Drill"]
    crt_fav_win_con = random.choice(win_cons)
    play_style = ["passive", "aggressive", "balanced"]
    crt_play_style = random.choice(play_style)
    has_evo_unlocked = random.choice([True, False])
    win_percentage = round(np.random.uniform(40.0, 70.0), 2)
    avg_elixir_cost = round(np.random.uniform(2.0, 7.0), 1)
    