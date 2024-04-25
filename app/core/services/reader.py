import pandas as pd


def read_data_with_dtype(path_to_data, dtype=None):
    file_extension = path_to_data.split(".")[-1].lower()
    if file_extension == "json":
        if dtype is None:
            return pd.read_json(path_to_data, lines=True)
        else:
            return pd.read_json(path_to_data, lines=True, dtype=dtype)
    elif file_extension == "csv":
        if dtype is None:
            return pd.read_csv(path_to_data)
        else:
            return pd.read_csv(path_to_data, dtype=dtype)
    elif file_extension in ["xls", "xlsx"]:
        if dtype is None:
            return pd.read_excel(path_to_data)
        else:
            return pd.read_excel(path_to_data, dtype=dtype)
    elif file_extension == "snappy":
        if dtype is None:
            return pd.read_parquet(path_to_data)
        else:
            return pd.read_parquet(path_to_data, dtype=dtype)
    else:
        raise ValueError("Unsupported file format")
