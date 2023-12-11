# Write a function to calculate simple interest which takes amount, year and rate
# as input and throws an exception if interest rate is greater than 100.


class SimpleInterest:
    def __init__(self, amount, year, rate):
        if rate > 100:
            raise ValueError("Interest can not be greater than 100")
        self.amount = amount
        self.year = year
        self.rate = rate

    def calculate_interest(self):
        print(f"Simple Interest: {self.amount * self.year * self.rate:.3f}")


si = SimpleInterest(420, 6, 9)
si.calculate_interest()
