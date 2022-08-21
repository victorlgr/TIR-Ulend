import numpy_financial as npf
import pandas as pd

from investments import investments
from installments import installments


def process_data(investments, installments):
    date = []
    amount = []

    for investment in investments:
        date.append(investment['created_at'])
        amount.append(-float(investment['amount']))

    for installment in installments:
        date.append(installment['due_date'])
        amount.append(float(installment['amount']))

    dict_values = {
        'date': date,
        'amount': amount
    }

    return dict_values


def process_df(dict_values):
    df = pd.DataFrame(dict_values)
    df['date'] = pd.to_datetime(df['date'])
    all_dates = pd.date_range(df['date'].min(), df['date'].max(), freq='d')
    df_base = pd.DataFrame({'date': all_dates})
    df_base = df_base.merge(df, on='date', how='left').fillna(0)
    df_base = df_base.groupby('date').sum().reset_index()
    df_base['cumulative'] = df_base['amount'].cumsum()
    return df_base


def export_data(df):
    df.to_csv('data.csv', index=False, sep=';', decimal=',')


def calc_irr(df):
    irr = round(100 * npf.irr(df['amount']), 2)
    print(f"TIR: {irr}%")


def main():
    dict_values = process_data(investments, installments)
    df = process_df(dict_values)
    calc_irr(df)
    export_data(df)


if __name__ == "__main__":
    main()
