

class Flowers:
    def __init__(self, color , price, dew, stem_length,lifespan):
        self.color = color
        self.price = price
        self.dew = dew
        self.stem_length = stem_length
        self.lifespan = lifespan



class Rose(Flowers):
    pass

class Tulip(Flowers):
    pass

class Peonies(Flowers):
    pass

class Chamomile(Flowers):
    pass


class Bouquet:
    def __init__(self, flowers):
        self.flowers = flowers

    def total_price(self):
        total = 0

        for flower in self.flowers:
            total += flower.price

        return total

    def average_lifetime(self):
        if not self.flowers:
            return 0

        total = 0

        for flower in self.flowers:
            total += flower.lifespan - flower.dew

        return total / len(self.flowers)

    def sort_by_price(self):
        self.flowers.sort(key=lambda flower: flower.price)
        return self.flowers


    def sort_by_color(self):
        self.flowers.sort(key=lambda flower: flower.color)
        return self.flowers


    def sort_by_stem_length(self):
        self.flowers.sort(key=lambda flower: flower.stem_length)
        return self.flowers

    def sort_by_stem_life(self):
        self.flowers.sort(
            key=lambda flower: flower.lifespan - flower.dew,
            reverse=True)
        return self.flowers

    def find_by_price(self):
        found = []
        for flower in self.flowers:
            if flower.price < 400:
                found.append(flower)
        return found


    def find_by_lifetime(self):
        found = []

        for flower in self.flowers:
            if flower.lifespan - flower.dew > 5:
                found.append(flower)

        return found




rose = Rose('red', 500,2, 40, 10)##время жизни  на 0 и - отрабатывает
tulip = Tulip('yellow', 200, 4, 30,10)
peony = Peonies('pink', 400, 5, 35,10)
chamomile = Chamomile('white', 100, 5, 20,10)



bouquet = Bouquet([rose, tulip, peony, chamomile])

print("Стоимость букета:", bouquet.total_price())
print("Среднее оставшееся время жизни:", bouquet.average_lifetime())

print("\nСортировка по цене:")
for flower in bouquet.sort_by_price():
    print(flower.color, flower.price)

print("\nСортировка по цвету:")
for flower in bouquet.sort_by_color():
    print(flower.color)

print("\nСортировка по длине стебля:")
for flower in bouquet.sort_by_stem_length():
    print(flower.color, flower.stem_length)

print("\nСортировка по оставшимся дням жизни:")
for flower in bouquet.sort_by_stem_life():
    print(flower.color, flower.lifespan - flower.dew)

print("\nЦветы дешевле 400:")
for flower in bouquet.find_by_price():
    print(flower.color)

print("\nЦветы, которым осталось меньше(нету )(больше) 5 дней:")
for flower in bouquet.find_by_lifetime():
    print(flower.color)