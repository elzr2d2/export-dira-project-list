import pandas


def create_csv(list_to_csv):
    pandas.DataFrame(list_to_csv).to_csv("./exported_data/dira_table.csv")