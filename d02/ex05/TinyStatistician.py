import math
import numpy


class TinyStatistician:
    def mean(self, x):
        res = 0
        if x and isinstance(x, list):
            for i in x:
                res += i
            return float(res / len(x))
        return None

    # https://www.delftstack.com/fr/howto/python/find-median-in-python/
    def median(self, x):
        if x and isinstance(x, list):
            half = len(x) // 2
            x.sort()
            if not len(x) % 2:
                return float((x[half - 1] + x[half]) / 2.0)
            return float(x[half])
        return None

    # https://www.delftstack.com/howto/python/python-percentile/
    def quartiles(self, x):
        res = []
        if x and isinstance(x, list):
            first = float(sorted(x)[int(math.ceil((len(x) * 25) / 100)) - 1])
            third = float(sorted(x)[int(math.ceil((len(x) * 75) / 100)) - 1])
            res.append(first)
            res.append(third)
            return res
        return None

    # https://www.delftstack.com/howto/python/variance-in-python/
    def var(self, x):
        if x and isinstance(x, list):
            average = sum(x) / len(x)
            var = sum((i-average)**2 for i in x) / len(x)
            return float(var)
        return None

    # https://www.delftstack.com/howto/python/standard-deviation-of-a-list-in-python/
    def std(self, x):
        if x and isinstance(x, list):
            mean = sum(x) / len(x)
            var = sum((i-mean)**2 for i in x) / len(x)
            st_dev = math.sqrt(var)
            return float(st_dev)
        return None


tstat = TinyStatistician()
a = [1, 42, 300, 10, 59]
print(tstat.mean(a))
print(tstat.median(a))
print(tstat.quartiles(a))
print(tstat.var(a))
print(tstat.std(a))
