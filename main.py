from tkinter import *

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 100
WINDOW_TITLE = "Miles to Kilometer Converter"
MILES_TEXT = "Miles"
EQUAL_LABEL_TEXT = "is equal to"
WINDOW_PADX = 20
WINDOW_PADY = 20
MILES_INPUT_WIDTH = 7
MILES_INPUT_COLUMN = 1
MILES_INPUT_ROW = 0
MILES_LABEL_COLUMN = 2
MILES_LABEL_ROW = 0
IS_EQUAL_LABEL_COLUMN = 0
IS_EQUAL_LABEL_ROW = 1
KILOMETER_RESULT_LABEL_TEXT = "0"
KILOMETER_RESULT_LABEL_COLUMN = 1
KILOMETER_RESULT_LABEL_ROW = 1
KILOMETER_LABEL_TEXT = "Km"
KILOMETER_LABEL_COLUMN = 2
KILOMETER_LABEL_ROW = 1
CALCULATE_BUTTON_TEXT = "Calculate"
CALCULATE_BUTTON_COLUMN = 1
CALCULATE_BUTTON_ROW = 2
CONVERSION_RATE = 1.609


def miles_to_kilometer():
    miles = float(miles_input.get())
    km = miles * CONVERSION_RATE
    kilometer_result_label.config(text=f"{km}")


window = Tk()
window.title(WINDOW_TITLE)
window.minsize(WINDOW_WIDTH, WINDOW_HEIGHT)
window.config(padx=WINDOW_PADX, pady=WINDOW_PADY)
miles_input = Entry(width=MILES_INPUT_WIDTH)
miles_input.grid(column=MILES_INPUT_COLUMN, row=MILES_INPUT_ROW)

miles_label = Label(text=MILES_TEXT)
miles_label.grid(column=MILES_LABEL_COLUMN, row=MILES_LABEL_ROW)

is_equal_label = Label(text=EQUAL_LABEL_TEXT)
is_equal_label.grid(column=IS_EQUAL_LABEL_COLUMN, row=IS_EQUAL_LABEL_ROW)

kilometer_result_label = Label(text=KILOMETER_RESULT_LABEL_TEXT)
kilometer_result_label.grid(column=KILOMETER_RESULT_LABEL_COLUMN, row=KILOMETER_RESULT_LABEL_ROW)

kilometer_label = Label(text=KILOMETER_LABEL_TEXT)
kilometer_label.grid(column=KILOMETER_LABEL_COLUMN, row=KILOMETER_LABEL_ROW)

calculate_button = Button(text=CALCULATE_BUTTON_TEXT, command=miles_to_kilometer)
calculate_button.grid(column=CALCULATE_BUTTON_COLUMN, row=CALCULATE_BUTTON_ROW)

window.mainloop()
