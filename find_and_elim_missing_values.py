def elim_missing_values(data_frame):
    check_fav_win_cond = data_frame["Favourite_Win_Condition"] == "N.A."
    check_play_style = data_frame["Play_Style"] == "unspecified"
    check_all = check_fav_win_cond | check_play_style
    nr_missing_values = check_all.sum()

    data_frame = data_frame[~check_all]
    return data_frame, nr_missing_values