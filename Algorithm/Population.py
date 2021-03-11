from Algorithm.Chromosome import Chromosome


class Population:
    def __init__(self, size, gene_length, chromosome_min_value, chromosome_max_value):
        self.__size = size
        self.__chromosomes = [
            Chromosome(gene_length, chromosome_min_value, chromosome_max_value) for _ in range(self.__size)
        ]
        self.calculate_fitness()

    def get_size(self):
        return self.__size

    def get_chromosomes(self):
        return self.__chromosomes

    def calculate_fitness(self):
        for chromosome in self.__chromosomes:
            chromosome.calculate_fitness()
