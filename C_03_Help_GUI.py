from tkinter import *


class Converter:
    """
    Temperature Conversion tool (C to F or F to C)
    """

    def __init__(self):
        """
        Temperature converter GUI
        """

        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.to_help_button = Button(self.temp_frame,
                                     text="Help / Info",
                                     bg="#CC6600",
                                     fg="#FFFFFF",
                                     font=("Arial",14, "bold"), width=12,
                                     command=self.to_help)
        self.to_help_button.grid(row=1, padx=5, pady=5)


    def to_help(self):
        DisplayHelp()


class DisplayHelp:

    def __init__(self):

        # setup dialogue box and background color
        background = "#ffe6cc"
        self.help_box = Toplevel()

        self.help_frame = Frame(self.help_box, width=300,
                                height=200)
        self.help_frame.grid()

        self.help_heading_label = Label(self.help_frame,
                                        text="Help / Info",
                                        font=("Arial",14,"bold"))
        self.help_heading_label.grid(row=0)

        help_text = ("to use the program simply enter the temp you wish to convert"
                     " and then choose to convert to either celsius (centigrad or fahrenheit.."
                     " note that -273 degrees C (-459 F) is absolute zero the coldezt possible "
                     "temp if you try to convert less than that "
                     "you will receive an error to see your calculation history"
                     " please click the history / export button) ")

        self.help_text_label = Label(self.help_frame,
                                     text=help_text, wraplength=350,
                                     justify="left")
        self.help_text_label.grid(row=1, padx=10)

        self.dismiss_button = Button(self.help_frame,
                                     font=("Arial",12,"bold"),
                                     text="Dismiss", bg="#CC6600",
                                     fg="#FFFFFF", command=self.close_help)
        self.dismiss_button.grid(row=2, padx=10,pady=10)

        # list and loop to set the background clour on
        # everything except the buttons.

        recolour_list = [self.help_frame, self.help_heading_label,
                         self.help_text_label]

        for item in recolour_list:
            item.config(bg=background)

    def close_help(self):
        self.help_box.destroy()
# main routine


if __name__ == "__main__":
    root = Tk()
    root.title("Temperature converter")
    Converter()
    root.mainloop()