from UI.Window import Window
from UI.UIElement import Column, Text, Input, DropDownList, CheckBox, Button, Image


class App:
    def __init__(self, window):
        self.__window = window

    def run(self):
        self.__window.run()


if __name__ == '__main__':
    App(Window(title='Genetic Algorithm', layout=[
        [
            Text(_id='Null0', text='', size=(1, 2)).create(),
        ], [
            Column(layout=[
                [
                    Column(layout=[[
                        Text(_id='Desc_Text1', text='Genetic Algorithm for finding min/max', size=(27, 1)).create(),
                    ]], justification='CENTER').create()
                ], [
                    Column(layout=[[
                        Text(_id='Desc_Text2', text='In the Drop-Wave Function', size=(19, 2)).create(),
                    ]], justification='CENTER').create()
                ]
            ], justification='LEFT').create(),
            Image(_id='DNA_Image', filepath='./Resources/DNA_100.png').create()
        ], [
            Text(_id='Null1', text='', size=(1, 2)).create(),
        ], [
            Text(_id='Range_Begin_Text', text='Begin of the range (int)').create(),
            Input(_id='Range_Begin_Input').create()
        ], [
            Text(_id='Range_End_Text', text='End of the range (int)').create(),
            Input(_id='Range_End_Input').create()
        ], [
            Text(_id='Population_Size_Text', text='Population Size (int)').create(),
            Input(_id='Population_Size_Input').create()
        ], [
            Text(_id='Bits_Number_Text', text='Number Of Bits (int)').create(),
            Input(_id='Bits_Number_Input').create()
        ], [
            Text(_id='Epochs_Amount_Text', text='Epochs Amount (int)').create(),
            Input(_id='Epochs_Amount_Input').create()
        ], [
            Text(_id='Selection_Amount_Text', text='Selection Amount (int)').create(),
            Input(_id='Selection_Amount_Input').create()
        ], [
            Text(_id='Elite_Strategy_Amount_Text', text='Elite Strategy Amount (int)').create(),
            Input(_id='Elite_Strategy_Amount_Input').create()
        ], [
            Text(_id='Cross_Probability_Text', text='Cross Probability (float)').create(),
            Input(_id='Cross_Probability_Input').create()
        ], [
            Text(_id='Mutation_Probability_Text', text='Mutation Probability (float)').create(),
            Input(_id='Mutation_Probability_Input').create()
        ], [
            Text(_id='Inversion_Probability_Text', text='Inversion Probability (float)').create(),
            Input(_id='Inversion_Probability_Input').create()
        ], [
            Text(_id='Selection_Method_Text', text='Selection Method').create(),
            DropDownList(_id='Selection_Method_Input', choices=['Best', 'Roulette', 'Tournament']).create()
        ], [
            Text(_id='Cross_Method_Text', text='Cross Method').create(),
            DropDownList(_id='Cross_Method_Input', choices=[
                'One Point', 'Two Points', 'Three Points', 'Homogenetic'
            ]).create()
        ], [
            Text(_id='Mutation_Method_Text', text='Mutation Method').create(),
            DropDownList(_id='Mutation_Method_Input', choices=['Edge', 'One Point', 'Two Points']).create()
        ], [
            CheckBox(_id='Maximization_Input', text='Maximization', default_value=False).create()
        ], [
            Column(layout=[[
                Text(_id='Validation_Text', text='', size=(45, 1), justification='center').create()
            ]], justification='CENTER').create()
        ], [
            Column(layout=[[
                Text(_id='Result_Text', text='', size=(45, 1), justification='center').create()
            ]], justification='CENTER').create()
        ], [
            Column(layout=[[
                Button(_id='Start', text='Start').create(), Button(_id='Close', text='Close').create()
            ]], justification='CENTER').create()
        ]
    ])).run()

