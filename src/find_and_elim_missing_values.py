def elim_missing_values(data_frame):
    check_fav_win_cond = data_frame["Favourite_Win_Condition"] == "N.A."
    check_win_probability_greater_than_100 = data_frame["Win_Probability"] > 100
    check_all = check_fav_win_cond | check_win_probability_greater_than_100
    nr_missing_values = check_all.sum()

    data_frame = data_frame[~check_all]
    return data_frame, nr_missing_values