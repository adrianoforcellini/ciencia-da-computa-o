from collections import Counter

class Estatistica:
    def __init__(self, numbers2):
        self.numbers2 = numbers2

    @classmethod
    def media(cls, numbers):
        return sum(numbers) / len(numbers)

    @classmethod
    def mediana(cls, numbers):
        numbers.sort()
        index = len(numbers) // 2
        if len(numbers) % 2 == 0:
            return (numbers[index - 1] + numbers[index]) / 2

        return numbers[index]

    @classmethod
    def moda(cls, numbers):
        number, _ = Counter(numbers).most_common()[0]
        return number

    def moda2(self):
        self.numbers2, _ = Counter(self.numbers2).most_common()[0]
        return self.numbers2


print(Estatistica.media([1,2,3]))
print(Estatistica.mediana([1,2,3]))
print(Estatistica.moda([1,2,3,3]))

minha_estatistica = Estatistica([1, 2 , 2])
print(minha_estatistica.media([1,2]))
print(minha_estatistica.moda2())


### Note como a annotation @classmethod facilita a passagem dos 
### valores sem que haja necessidade do uso do self ou init.