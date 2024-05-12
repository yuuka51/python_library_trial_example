from datetime import datetime
from pathlib import Path

import pandas as pd
import yaml


def concat_dataframe(input_df):
    data2 = {
        "id": [4, 5, 6],
        "sub_id": [400, 500, 600],
        "update_time": [datetime(2023, 1, 4), datetime(2023, 1, 5), datetime(2023, 1, 6)],
    }
    df2 = pd.DataFrame(data2)

    # DataFrameを結合させる
    concat_df = pd.concat([input_df, df2])
    return concat_df


def main():
    # cwd() = current working directory
    input_file_path = Path.cwd() / "pandas"/ "input" / "year=2023" / "month=08" / "input.yml"

    # Read the input YAML file
    with open(input_file_path, "r") as file:
        input_data = yaml.safe_load(file)

    input_df = pd.DataFrame(input_data)
    print(input_df)

    concat_df = concat_dataframe(input_df)
    print(concat_df)


if __name__ == "__main__":
    main()
