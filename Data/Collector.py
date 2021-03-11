class DataCollector:
    def __init__(self, maximization):
        self.__maximization = maximization
        self.__start_time = None
        self.__end_time = None
        self.__best_chromosome = None
        self.__best_fitness = []
        self.__mean_fitness = []
        self.__standard_deviation = []

    def get_best_fitnesses(self):
        return self.__best_fitness

    def get_mean_fitnesses(self):
        return self.__mean_fitness

    def get_standard_deviations(self):
        return self.__standard_deviation

    def __add_best_fitness(self, population):
        all_fitnesses = [chromosome.get_fitness() for chromosome in population.get_chromosomes()]
        best_fitness = max(all_fitnesses) if self.__maximization else min(all_fitnesses)
        self.__best_fitness.append(best_fitness)

    def __add_mean_fitness(self, population):
        all_fitnesses = [chromosome.get_fitness() for chromosome in population.get_chromosomes()]
        mean_fitness = sum(all_fitnesses) / len(population.get_chromosomes())
        self.__mean_fitness.append(mean_fitness)

    def __add_standard_deviation(self, population):
        all_fitnesses = [chromosome.get_fitness() for chromosome in population.get_chromosomes()]
        mean_fitness = sum(all_fitnesses) / len(population.get_chromosomes())
        nominator = 0
        for chromosome in population.get_chromosomes():
            nominator += (chromosome.get_fitness() - mean_fitness) ** 2
        standard_deviation = (nominator / len(population.get_chromosomes())) ** 0.5
        self.__standard_deviation.append(standard_deviation)

    def __save_best_chromosome(self, population):
        chromosomes_copy = [chromosome for chromosome in population.get_chromosomes()]
        chromosomes_copy.sort(key=lambda chromosome: chromosome.get_fitness(), reverse=self.__maximization)
        self.__best_chromosome = chromosomes_copy[0]

    def collect_new_algorithm_data(self, population):
        self.__add_best_fitness(population)
        self.__add_mean_fitness(population)
        self.__add_standard_deviation(population)
        self.__save_best_chromosome(population)

    def start_timer(self, time):
        self.__start_time = time

    def stop_timer(self, time):
        self.__end_time = time

    def get_elapsed_time(self):
        return self.__end_time - self.__start_time

    def get_best_point(self):
        return {
            'x1': self.__best_chromosome.get_gene_x_decimal(),
            'x2': self.__best_chromosome.get_gene_y_decimal()
        }

    def get_best_value(self):
        return self.__best_chromosome.get_fitness()
