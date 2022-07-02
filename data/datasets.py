import pandas as pd


class Datasets:
    """
    Auxiliary data generator
    """
    @staticmethod
    def barranquilla():
        return pd.read_csv(
            'https://raw.githubusercontent.com/cosmolejo/dataRepo/master/ds4a/Barranquilla_final.csv',
            low_memory=False
        )

    @staticmethod
    def palmira():
        return pd.read_csv(
            'https://raw.githubusercontent.com/cosmolejo/dataRepo/master/ds4a/Palmira_final.csv',
            low_memory=False
        )

    @staticmethod
    def medellin():
        return pd.read_csv(
            'https://raw.githubusercontent.com/cosmolejo/dataRepo/master/ds4a/Medellin_final.csv',
            low_memory=False
        )

    @staticmethod
    def bucaramanga():
        return pd.read_csv(
            'https://raw.githubusercontent.com/cosmolejo/dataRepo/master/ds4a/Bucaramanga_final.csv',
            low_memory=False
        )

    @staticmethod
    def envigado():
        return pd.read_csv(
            'https://raw.githubusercontent.com/cosmolejo/dataRepo/master/ds4a/Envigado_final.csv',
            low_memory=False
        )

    @staticmethod
    def nacional():
        return pd.read_csv(
            'https://raw.githubusercontent.com/cosmolejo/dataRepo/master/ds4a/Nacional_final.csv',
            low_memory=False
        )

    @staticmethod
    def get_data():
        return {
            'nacional': Datasets.nacional(),
            'palmira': Datasets.palmira(),
            'barranquilla': Datasets.barranquilla(),
            'medellin': Datasets.medellin(),
            'bucaramanga': Datasets.bucaramanga(),
            'envigado': Datasets.envigado(),

        }


if __name__ == '__main__':
    print(Datasets.get_data()['nacional'].head())
