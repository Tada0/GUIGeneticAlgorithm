from matplotlib import pyplot
from pathlib import Path


class DataVisualizer:
    def __init__(self, out_path):
        self.__graphs_path = f'{out_path}/data/graphs/'
        self.__txts_path = f'{out_path}/data/txt/'
        Path(self.__txts_path).mkdir(parents=True, exist_ok=True)
        Path(self.__graphs_path).mkdir(parents=True, exist_ok=True)

    @staticmethod
    def create_graph(xvalues, yvalues, title, xlabel, ylabel, filename, filepath):
        figure = pyplot.figure()
        pyplot.plot(xvalues, yvalues, figure=figure)
        pyplot.xlabel(xlabel, figure=figure)
        pyplot.ylabel(ylabel, figure=figure)
        pyplot.title(title, figure=figure)
        figure.savefig(f'{filepath}{filename}')
        pyplot.close(figure)

    @staticmethod
    def create_txt(values, filename, filepath):
        with open(f'{filepath}{filename}', 'w') as file:
            file.writelines([f'{idx + 1}: {value}\n' for idx, value in enumerate(values)])

    def create_mean_fitness_data_visualization(self, mean_fitness_data):
        DataVisualizer.create_graph(
            xvalues=list(range(len(mean_fitness_data))),
            yvalues=mean_fitness_data,
            title='Mean Function Value Graph',
            xlabel='Epoch',
            ylabel='Mean Function Value',
            filename='Mean_Value_Graph.png',
            filepath=self.__graphs_path
        )
        DataVisualizer.create_txt(
            values=mean_fitness_data,
            filename='Mean_Values.txt',
            filepath=self.__txts_path
        )

    def create_best_fitness_data_visualization(self, best_fitness_data):
        DataVisualizer.create_graph(
            xvalues=list(range(len(best_fitness_data))),
            yvalues=best_fitness_data,
            title='Function Value Graph',
            xlabel='Epoch',
            ylabel='Function Value',
            filename='Value_Graph.png',
            filepath=self.__graphs_path
        )
        DataVisualizer.create_txt(
            values=best_fitness_data,
            filename='Values.txt',
            filepath=self.__txts_path
        )

    def create_standard_deviation_data_visualization(self, standard_deviation_data):
        DataVisualizer.create_graph(
            xvalues=list(range(len(standard_deviation_data))),
            yvalues=standard_deviation_data,
            title='Standard Deviation Graph',
            xlabel='Epoch',
            ylabel='Standard Deviation',
            filename='Standard_Deviation_Graph.png',
            filepath=self.__graphs_path
        )
        DataVisualizer.create_txt(
            values=standard_deviation_data,
            filename='Standard_Deviations.txt',
            filepath=self.__txts_path
        )
