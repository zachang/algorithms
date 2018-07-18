from functools import reduce

class SelfPower:
    """
    Algorithm to retrieve last ten digits of the summation of self 
    power series of natural numbers less than or equal to 1000
    """

    @staticmethod
    def self_power_first(value):
        """First implementation of the algorithm"""
        summation = 0
        for val in range(1, value):
            summation += val ** val
        return {"summation": summation, "last_ten_digits": str(summation)[-10:]}

    @staticmethod
    def self_power_second(value):
        """Second implementation of the algorithm using sum, map and lambda functions"""
        value_list = list(range(1, value))
        summation = sum(map(lambda x: x ** x, value_list))
        return dict(summation=summation, last_ten_digits=str(summation)[-10:])


if __name__ == "__main__":
    self_power = SelfPower
    print(self_power.self_power_first(11))
    print(self_power.self_power_second(11))