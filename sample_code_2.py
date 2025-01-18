import matplotlib.pyplot as plt

class SimpleDebtSimulation:

    def __init__(self):
        self.debt = 10000
        self.monthlyInterest = 1
        self.result = []
        self.monthlyPayment = 0
        self.t = 0
        self.timeSteps = []

    def initialize(self, monthlyPayment, monthlyInterest):
        self.monthlyPayment = monthlyPayment
        self.monthlyInterest = monthlyInterest
        self.result = [self.debt]
        self.timeSteps = [self.t]

    def observe(self):
        self.result.append(self.debt)
        self.timeSteps.append(self.t)

    def update(self):
        self.debt -= self.monthlyPayment
        if self.debt > 0:
            self.debt += self.debt * (self.monthlyInterest / 12)
        self.t += 1

    def runsim(self, monthlyPayment, monthlyInterest):
        self.initialize(monthlyPayment, monthlyInterest)
        while self.t < 60:
            self.update()
            self.observe()

        plt.plot(self.timeSteps, self.result)
        plt.show()
        print(self.result)


if __name__ == '__main__':
    sim = SimpleDebtSimulation()
    sim.runsim(200, 0.04, )