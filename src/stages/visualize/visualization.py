from typing import Tuple, Union
import pandas as pd


def prep_visualization(df: pd.DataFrame) -> Tuple:
    """Prepare data.

    Parameters
    ----------
    df: Pandas.Dataframe
    """
    # saldo
    df["lucro"] = df["revenue"] - df["budget"]
    df["saldo"] = df["lucro"].apply(calcular_saldo)
    df_saldo = df["saldo"].value_counts().reset_index()

    # genero
    lista_strings = df["genres"].tolist()
    lista_valores = [
        valor for string in lista_strings for valor in eval(string)
    ]
    df_genres = pd.DataFrame(lista_valores).value_counts().reset_index()
    df_genres.rename(columns={0: "genres"}, inplace=True)

    return df_saldo, df_genres


def calcular_saldo(x: Union[float, int]):
    """Function to calculate saldo.

    Parameters
    ----------
    x: Float
    """
    if x > 0:
        return "LUCRO"
    elif x == 0:
        return "SE PAGOU"
    else:
        return "PREJUIZO"
