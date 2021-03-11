from Algorithm.Population import Population
from Algorithm.Selection import Selection
from Algorithm.Mutation import Mutation
from Algorithm.Cross import Cross
from Algorithm.Inversion import Inversion
from Data.Collector import DataCollector
from time import time


class Algorithm:
    def __init__(self, range_begin, range_end, population_size, bits_number, epochs_amount,
                 selection_chromosome_amount, elite_strategy_amount, cross_probability,
                 mutation_probability, inversion_probability, selection_method, cross_method,
                 mutation_method, maximization):
        self.__data_collector = DataCollector(maximization=maximization)
        self.__range_begin = int(range_begin)
        self.__range_end = int(range_end)
        self.__population_size = int(population_size)
        self.__gene_length = int(bits_number)
        self.__epochs_amount = int(epochs_amount)
        self.__selection_chromosome_amount = int(selection_chromosome_amount)
        self.__elite_strategy_amount = int(elite_strategy_amount)
        self.__cross_probability = float(cross_probability)
        self.__mutation_probability = float(mutation_probability)
        self.__inversion_probability = float(inversion_probability)
        self.__selection_method = Selection(selection_method=selection_method).get_method()
        self.__cross_method = Cross(cross_method=cross_method).get_method()
        self.__mutation_method = Mutation(mutation_method=mutation_method).get_method()
        self.__inversion_method = Inversion().get_method()
        self.__maximization = maximization
        self.__population = Population(
            size=self.__population_size,
            gene_length=self.__gene_length,
            chromosome_min_value=self.__range_begin,
            chromosome_max_value=self.__range_end
        )

    def validate_data(self):
        if self.__range_begin >= self.__range_end:
            return 'FAILURE', 'Incorrect Range'
        if 0 > self.__population_size > 10000:
            return 'FAILURE', 'Incorrect Population Size'
        if 0 > self.__gene_length > 500:
            return 'FAILURE', 'Incorrect Bits Number'
        if 0 > self.__epochs_amount > 10000:
            return 'FAILURE', 'Incorrect Epochs Amount'
        if not 0.001 < self.__cross_probability < 0.999:
            return 'FAILURE', 'Incorrect Cross Probability'
        if not 0.001 < self.__mutation_probability < 0.999:
            return 'FAILURE', 'Incorrect Mutation Probability'
        if not 0.001 < self.__inversion_probability < 0.999:
            return 'FAILURE', 'Incorrect Inversion Probability'
        return 'SUCCESS', ''

    def start(self):
        return self.__run()

    def __run(self):

        self.__data_collector.start_timer(time())

        for epoch in range(self.__epochs_amount):

            # pick elites
            chromosomes_copy = [chromosome for chromosome in self.__population.get_chromosomes()]
            chromosomes_copy.sort(key=lambda chromosome: chromosome.get_fitness(), reverse=self.__maximization)
            elite_chromosomes = chromosomes_copy[:self.__elite_strategy_amount]

            # selection
            selected_chromosomes = self.__selection_method(
                selection_amount=self.__selection_chromosome_amount,
                population=self.__population,
                maximization=self.__maximization
            )

            # crossing
            crossed_chromosomes = self.__cross_method(
                chromosomes_for_crossing=selected_chromosomes,
                crossing_probability=self.__cross_probability
            )

            # swap crossed for selected
            for chromosome in selected_chromosomes:
                self.__population.get_chromosomes().remove(chromosome)
            self.__population.get_chromosomes().extend(crossed_chromosomes)

            # mutation
            self.__mutation_method(
                population=self.__population,
                probability=self.__mutation_probability
            )

            # inversion
            self.__inversion_method(
                population=self.__population,
                probability=self.__inversion_probability
            )

            # swap elites for the worst ones
            chromosomes_copy = [chromosome for chromosome in self.__population.get_chromosomes()]
            chromosomes_copy.sort(key=lambda chromosome: chromosome.get_fitness(), reverse=not self.__maximization)
            worst_chromosomes = chromosomes_copy[:self.__elite_strategy_amount]
            for chromosome in worst_chromosomes:
                self.__population.get_chromosomes().remove(chromosome)
            self.__population.get_chromosomes().extend(elite_chromosomes)

            # evaluate
            self.__population.calculate_fitness()

            # collect data
            self.__data_collector.collect_new_algorithm_data(self.__population)

        self.__data_collector.stop_timer(time())

        return self.__data_collector
