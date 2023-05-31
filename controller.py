from datetime import datetime
from view import View
from model import Model

class Controller:
    def __init__(self, view: View, model: Model,):
        self.model = model
        self.view = view

    def start(self):
         """Set up and start the view"""
         self.view.setup_view(self.button_click_handler)
         self.view.start_main_loop()

    def button_click_handler(self, value):
        """Redirect to the suitable handler function base on the value of the clicked button"""
        if value == "=":
            self._equal_button()
        elif value == "C":
            self._clear_button()
        else:
            self._button_pressed(value)
        

    def _button_pressed(self, num):
        """Add the value of the clicked button to the equation"""
        self.model.data += str(num)
        self.view.set_equation(self.model.data)
        
        

    def _equal_button(self):
        """Evaluate the equation and show the result"""
        total = str(eval(self.model.data))
        self.view.set_equation(total)
        self.model.data = ""
        self.file_log = open("file_log.txt", "a")
        self.time = datetime.now().strftime("%H:%M")
        self.file_log.write(f" Время: {self.time} Результат операции: {total} \n")

        
    
    def _clear_button(self):
        """Clear out the sreen of the calculator"""
        self.model.data = ""
        self.view.set_equation(self.model.data)


if __name__ == "__main__":
    controller = Controller(View(), Model())
    controller.start()


    


    