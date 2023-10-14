from data_raw.team_stats import all_countries_stats

inp_df_header = ["name", "total_matches", "runs_scored", "batting_average", "num_centuries", "num_fifties",
                 "num_wickets_taken", "bowling_average", "five_wickets_haul"]

for elem in inp_df_header:
    world_median_stats = {
        elem: round(all_countries_stats[elem].median(), 4)
    }
len_all_countries_stats = len(all_countries_stats)


def compute_stats_within(col_name, comparison_type, inp_df):
    """
    :param col_name: Column Name on which statistic has to be computed
    :param comparison_type: Logical Operator to get 'good' or 'bad' numbers
    :param inp_df: Input Dataframe
    :return: Output Value [float]
    """
    stat_median = inp_df[col_name].median()
    if comparison_type == "gte":
        rec_that_fulfill_condition = inp_df.query("{} >= {}".format(col_name, stat_median))
    else:
        rec_that_fulfill_condition = inp_df.query("{} < {}".format(col_name, stat_median))
    stats_for_col = len(rec_that_fulfill_condition) / len(inp_df)
    return round(stats_for_col, 4)


def compute_stats_world(col_name, comparison_type, inp_df):
    """
    :param col_name: Column Name on which statistic has to be computed
    :param comparison_type: Logical Operator to get 'good' or 'bad' numbers
    :param inp_df: Input Dataframe
    :return: Output Value [float]
    """
    if comparison_type == "gte":
        rec_that_fulfill_condition = inp_df.query("{} >= {}".format(col_name, world_median_stats[col_name]))
    else:
        rec_that_fulfill_condition = inp_df.query("{} < {}".format(col_name, world_median_stats[col_name]))
    stats_for_col = len(rec_that_fulfill_condition) / len_all_countries_stats
    return round(stats_for_col, 4)


def derive_summary_from_team(country_name, input_df):
    """
    :param country_name: Name of the country
    :param input_df: Team Details dataframe
    :return: Pandas dataframe with summary stats
    """
    summ = {"num_seniors": compute_stats_within("total_matches", "gte", input_df),
            "num_batsmen": compute_stats_within("batting_average", "gte", input_df),
            "num_bowlers": compute_stats_within("bowling_average", "lt", input_df),
            "num_good_batsmen": len(input_df.query("num_centuries > 0 or num_fifties > 0")) / len(input_df),
            "num_good_bowlers": max(
                float(len(input_df.query("five_wickets_haul > 0"))),
                compute_stats_within("num_wickets_taken", "gte", input_df)
            ),
            "num_seniors_vs_world": compute_stats_world("total_matches", "gte", input_df)}
    print(country_name, summ)
