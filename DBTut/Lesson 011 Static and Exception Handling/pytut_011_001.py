class Sum:

    @staticmethod
    def getsum(*args):

        summary = 0

        for i in args:
            summary += i

        return summary


def main():

    print('Sum :', Sum.getsum(1, 2, 3, 4, 5))
