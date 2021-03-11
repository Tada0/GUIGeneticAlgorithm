from Algorithm.Algorithm import Algorithm
from Thread.CallbackThread import CallbackThread
from Data.Visualizer import DataVisualizer
import PySimpleGUI
import re


class ValidationError(Exception):
    def __init__(self, message):
        self.message = message


class Window:
    def __init__(self, title, layout):
        self.__layout = layout
        self.__title = title
        self.__window = PySimpleGUI.Window(self.__title, self.__layout).Finalize()

    def __getitem__(self, item):
        return self.__window.__getitem__(item)

    def __window_queue_event(self, event, value):
        self.__window.write_event_value(event, value)

    def __validate_types(self, values):
        try:
            if not re.match(r"^([+-]?[1-9]\d*|0)$", values['Range_Begin_Input']):
                raise ValidationError('Range Begin must be an Integer.')
            if not re.match(r"^([+-]?[1-9]\d*|0)$", values['Range_End_Input']):
                raise ValidationError('Range End must be an Integer.')
            if not re.match(r"^([+-]?[1-9]\d*|0)$", values['Population_Size_Input']):
                raise ValidationError('Population Size must be an Integer.')
            if not re.match(r"^([+-]?[1-9]\d*|0)$", values['Bits_Number_Input']):
                raise ValidationError('Number of Bits must be an Integer.')
            if not re.match(r"^([+-]?[1-9]\d*|0)$", values['Epochs_Amount_Input']):
                raise ValidationError('Epochs Amount must be an Integer.')
            if not re.match(r"^([+-]?[1-9]\d*|0)$", values['Selection_Amount_Input']):
                raise ValidationError('Chromosome Selection Amount must be an Integer.')
            if not re.match(r"^([+-]?[1-9]\d*|0)$", values['Elite_Strategy_Amount_Input']):
                raise ValidationError('Elite Strategy Amount must be an Integer.')
            if not re.match(r'^-?\d+(?:\.\d+)$', values['Cross_Probability_Input']):
                raise ValidationError('Cross Probability must be a Float.')
            if not re.match(r'^-?\d+(?:\.\d+)$', values['Mutation_Probability_Input']):
                raise ValidationError('Mutation Probability must be a Float.')
            if not re.match(r'^-?\d+(?:\.\d+)$', values['Inversion_Probability_Input']):
                raise ValidationError('Inversion Probability must be a Float.')
        except ValidationError as error:
            self.__window['Validation_Text'].update(value=error.message, text_color='RED4', visible=True)
            return False
        return True

    def run(self):
        while True:
            event, values = self.__window.read()

            if event == PySimpleGUI.WINDOW_CLOSED or event == 'Close':
                break

            if event == 'Start':
                self.__window['Validation_Text'].update(value='')
                self.__window['Result_Text'].update(value='')
                if not self.__validate_types(values):
                    continue

                algorithm = Algorithm(
                    range_begin=values['Range_Begin_Input'],
                    range_end=values['Range_End_Input'],
                    population_size=values['Population_Size_Input'],
                    bits_number=values['Bits_Number_Input'],
                    epochs_amount=values['Epochs_Amount_Input'],
                    selection_chromosome_amount=values['Selection_Amount_Input'],
                    elite_strategy_amount=values['Elite_Strategy_Amount_Input'],
                    cross_probability=values['Cross_Probability_Input'],
                    mutation_probability=values['Mutation_Probability_Input'],
                    inversion_probability=values['Inversion_Probability_Input'],
                    selection_method=values['Selection_Method_Input'],
                    cross_method=values['Cross_Method_Input'],
                    mutation_method=values['Mutation_Method_Input'],
                    maximization=values['Maximization_Input']
                )

                validation_result, validation_message = algorithm.validate_data()

                if validation_result == 'SUCCESS':
                    self.__window['Validation_Text'].update(value="Working...", text_color='LIME GREEN')
                    self.__window['Start'].update(disabled=True)

                    CallbackThread(
                        target=algorithm.start,
                        callback=self.__window_queue_event,
                        callback_args=("ALGORITHM_FINISHED",),
                        add_result_to_callback=True,
                        daemon=True
                    ).start()

                else:
                    self.__window['Validation_Text'].update(value=validation_message, text_color='RED4')

            if event == 'ALGORITHM_FINISHED':

                data_collector = values['ALGORITHM_FINISHED']

                data_visualizer = DataVisualizer(out_path='./out')
                data_visualizer.create_best_fitness_data_visualization(data_collector.get_best_fitnesses())
                data_visualizer.create_mean_fitness_data_visualization(data_collector.get_mean_fitnesses())
                data_visualizer.create_standard_deviation_data_visualization(data_collector.get_standard_deviations())

                self.__window['Validation_Text'].update(
                    value=f"Elapsed_time - {'%.3f' % data_collector.get_elapsed_time()}s",
                    text_color='LIME GREEN',
                )

                x1 = '%.5f' % data_collector.get_best_point()['x1']
                x2 = '%.5f' % data_collector.get_best_point()['x2']
                value = '%.5f' % data_collector.get_best_value()

                self.__window['Result_Text'].update(
                    value=f"(x1, x2) = ({x1}, {x2}) -> {value}",
                    text_color='LIME GREEN',
                )

                self.__window['Start'].update(disabled=False)

        self.__window.close()
