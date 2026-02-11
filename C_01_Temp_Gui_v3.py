from tkinter import *
import all_constants as c 

class Converter():
    """
    Temperature conversion tool (C to F or F to C )
    """

    def __init__(self):
        """
        Temperature converter gui
        """

        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.temp_heading = Label(self.temp_frame,
                                  text ="Temperature Converter",
                                  font=("Arial", "16", "bold")
                                  )
        self.temp_heading.grid(row=0)

        instructions = ("Please enter a temperature below and then press one of the "
                        "buttons to convert ut from centrigrade "
                        "to farenheit.")
        self.temp_instructions = Label(self.temp_frame,
                                       text=instructions,
                                       wraplength=150, width=40,
                                       justify="left")
        self.temp_instructions.grid(row=1)

        self.temp_entry = Entry(self.temp_frame,
                                font=("Arail","14")
                                )
        self.temp_entry.grid(row=2, padx=10,pady=10)

        error = "please enter a number "
        self.answer_error = Label(self.temp_frame, text=error,
                                  fg="#004C99", )
        self.answer_error.grid(row=3)

        # conversion help and history / export buttons
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)

        #button list button text/bg colour / command / row / column)
        button_details_lists = [
            ["to celsius","#990099", lambda:self.check_temp(c.ABS_ZERO_FAHRENHEIT),0,0],
            ["to fahrenheit","#009900",lambda:self.check_temp(c.ABS_ZERO_CELSIUS),0,1],
            ["Help / Info","#CC6600","",1,0],
            [" History / Export","#004C99","",1,1]

        ]

        #list to hold buttons once they have been made
        self.button_ref_list = []

        for item in button_details_lists:
            self.make_button = Button(self.button_frame,
                                      text=item[0], bg=item[1],
                                      fg="#FFFFFF", font=("Arial","12","bold"),
                                      width=12, command=item[2])
            self.make_button.grid(row=item[3], column=item[4], padx=5,pady=5)

            self.button_ref_list.append(self.make_button)
        #retrieve history / export button AND disable it at the start
        self.to_history_button = self.button_ref_list[3].config(state=DISABLED)


    def check_temp(self,min_temp):
        """
        checks temp is valid and
        either invokes calculation function or shows an custom error
        """
        print("Min temp:", min_temp)

        # retiriece temperqture to be converted
        to_convert = self.temp_entry.get()
        print("to convert", to_convert)

        # reset label and entry box (if we had an error)
        self.answer_error.config(fg="#004C99")
        self.temp_entry.config(bg="#FFFFFF")

        # checks that amo8nt to e converted is a number above absolute zero
        try:
            to_convert = float(to_convert)
            if to_convert >= min_temp:
               error = ""
               self.convert(min_temp)
            else:
                error = "Too Low "

        except ValueError:
            error = "please enter a number "

        # display the error if necessary
        if error != "":
            self.answer_error.config(text=error, fg="#9C0000")
            self.temp_entry.config(bg="#F4CCCC")
            self.temp_entry.delete(0,END)

    def convert(self,min_temp):

        if min_temp == c.ABS_ZERO_CELSIUS:
            self.answer_error.config(text="Converting to F")
        else:
            self.answer_error.config(text="Converting to C")


# main routine


if __name__ == "__main__":
    root = Tk()
    root.title("Temperature converter")
    Converter()
    root.mainloop()