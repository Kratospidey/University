class Interest:
    def __init__(self, amount, year, rate):
        try:
            if rate > 100:
                raise ValueError(rate)
            self.amount = amount
            self.year = year
            self.rate = rate

        except ValueError:
            print("Rate cannot be greater than 100")

    def calculate(self):
        return (self.amount * self.year * self.rate) / 100


def main():
    amo = int(input("Amount: "))
    yrs = int(input("Time: "))
    rte = int(input("Rate: "))

    intrst = Interest(amo, yrs, rte)

    print(f"Simple Interest: {intrst.calculate()}")


main()
