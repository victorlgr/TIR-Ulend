from investments import investments
from installments import installments
import numpy_financial as npf


cashflows = {
    # "20190409": -14000.00,
}


def mount_investments():
    pass


def mount_installments():
    pass


def calc_irr():
    data = []
    for amount in cashflows.values():
        data.append(amount)

    irr = round(npf.irr(data), 2)
    print("TIR:", irr)


if __name__ == "__main__":
    mount_investments()
    mount_installments()
    calc_irr()