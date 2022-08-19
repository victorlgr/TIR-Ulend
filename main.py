from investments import investments
from installments import installments
import numpy_financial as npf


cashflows = {}


def calc_irr():
    data = []
    for amount in cashflows.values():
        data.append(amount)

    irr = round(npf.irr(data), 2)
    print("TIR:", irr)


if __name__ == "__main__":
    calc_irr()