import pandas as pd


class Datasets:
    """
    Auxiliary data generator
    """

    def barranquilla():
        return pd.read_csv(
            'https://raw.githubusercontent.com/cosmolejo/dataRepo/master/ds4a/Barranquilla_final.csv'
        )

if __name__ == '__main__':
    print(Datasets.barranquilla().head())