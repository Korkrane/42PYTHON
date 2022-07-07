class Evaluator:
    def zip_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1
        total = 0
        for coef, word in zip(coefs, words):
            total += coef * len(word)
        return total

    def enumerate_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1
        total = 0
        for i, word in enumerate(words):
            total += coefs[i] * len(word)
        return total
