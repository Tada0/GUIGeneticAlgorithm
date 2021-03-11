from math import ceil
from random import random


class Selection:
    def __init__(self, selection_method):
        self.__selection_method = {
            'Best': Selection.__best,
            'Roulette': Selection.__roulette,
            'Tournament': Selection.__tournament
        }[selection_method]

    def get_method(self):
        return self.__selection_method

    @staticmethod
    def __filter_chromosomes(chromosomes):
        return chromosomes if len(chromosomes) % 2 == 0 else chromosomes[:-1]

    @staticmethod
    def __best(population, selection_amount, maximization):
        chromosomes_copy = [chromosome for chromosome in population.get_chromosomes()]
        chromosomes_copy.sort(key=lambda chromosome: chromosome.get_fitness(), reverse=True if maximization else False)
        return Selection.__filter_chromosomes(chromosomes_copy[:selection_amount])

    @staticmethod
    def __roulette(population, selection_amount, maximization):
        chromosomes_copy = [chromosome for chromosome in population.get_chromosomes()]

        chosen_chromosomes = []

        for _ in range(selection_amount):

            fitness_sums = {
                True: sum([chromosome.get_fitness() for chromosome in chromosomes_copy]),
                False: sum([1 / chromosome.get_fitness() for chromosome in chromosomes_copy])
            }[maximization]

            roulette = []
            probability_sum = 0

            for chromosome in chromosomes_copy:
                adaptation = chromosome.get_fitness() if maximization else 1 / chromosome.get_fitness()
                probability_sum += adaptation / fitness_sums
                roulette.append({
                    'Chromosome': chromosome,
                    'Probability': probability_sum
                })

            chosen_number = random()
            for roulette_element in roulette:
                if chosen_number < roulette_element['Probability']:
                    chosen_chromosomes.append(roulette_element['Chromosome'])
                    chromosomes_copy.remove(roulette_element['Chromosome'])
                    break

        return Selection.__filter_chromosomes(chosen_chromosomes)

    @staticmethod
    def __tournament(population, selection_amount, maximization):
        def chunks(li, n):
            return [li[i:i + n] for i in range(0, len(li), n)]

        chromosomes_copy = [chromosome for chromosome in population.get_chromosomes()]

        return Selection.__filter_chromosomes([
            max(tournament) if maximization else min(tournament) for tournament in
            chunks(
                chromosomes_copy,
                ceil(population.get_size() / selection_amount)
            )
        ])
