import kivy
import random

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

class MainApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"]
        ]
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None
        self.solution = TextInput(multiline=False, readonly=True, halign="right", font_size=55)
        layout.add_widget(self.solution)
        for row in buttons:
            rowLayout = BoxLayout()
            for elem in row:
                button = Button(text=elem, pos_hint={"center_x": 0.5, "center_y": 0.5}, on_press=self.on_button_press)
                rowLayout.add_widget(button)
            layout.add_widget(rowLayout)
        equalButton = Button(text="=", pos_hint={'center_x': .5, 'center_y': .5}, on_press=self.get_solution)
        layout.add_widget(equalButton)
        return layout
    
    def on_button_press(self, instance):
        state = self.solution.text
        currentBtn = instance.text

        if currentBtn == "C":
            # Clear the solution widget
            self.solution.text = ""
        else:
            if state != "" and (self.last_was_operator and currentBtn in self.operators):
                return
            elif state == "" and currentBtn in self.operators:
                return
            else:
                new_text = state + currentBtn
                self.solution.text = new_text
        self.last_button = currentBtn
        self.last_was_operator = self.last_button in self.operators
    
    def get_solution(self, instance):
        state = self.solution.text
        if state != "":
            solution = str(eval(self.solution.text))
            self.solution.text = solution



if __name__ == "__main__":
    app = MainApp()
    app.run()