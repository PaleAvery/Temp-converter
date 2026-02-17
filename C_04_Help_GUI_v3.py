from tkinter import *
from functools import partial
import all_constants as c
from datetime import date
class Converter:
    """
    Temperature Conversion tool (C to F or F to C)
    """

    def __init__(self):
        """
        Temperature converter GUI
        """

        # self.all_calculations_list = ['10.0F is -12C','20.0F is -7C',
        #                               '30 f is -1c',' 40 f is 4 c ',
        #                               '50f is 10 c ','60 f is 16 c']

        self.all_calculations_list = ['10.0F is -12C','20.0F is -7.0C',
                                      '30.0f is -1.0C',' 40.0F is 4.0C ',
                                      '50.0F is 10.0C ','this is a test']
        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.to_history_button = Button(self.temp_frame,
                                     text="Help / Info",
                                     bg="#CC6600",
                                     fg="#FFFFFF",
                                     font=("Arial",14, "bold"), width=12,
                                     command=self.to_history)
        self.to_history_button.grid(row=1, padx=5, pady=5)

    def to_history(self):
        """
        opens help dialogue box and disables help button
        (so that users cant create multiple help boxes)
        """
        HistoryExport(self, self.all_calculations_list)

class HistoryExport:
    """
    displays help dialogue  box
    """

    def __init__(self, partner, calculations):
        # setup dialogue box and background colour

        self.history_box = Toplevel()

        # disable history button
        partner.to_history_button.config(state=DISABLED)

        #if users press cross at top closes history
        # and releases history button
        self.history_box.protocol('WM_DELETE_WINDOW',
                                  partial(self.close_history,partner))

        self.history_frame = Frame(self.history_box)
        self.history_frame.grid()

        # background colour and text for calculation area
        if len(calculations) <= c.MAX_CALCS:
            calc_back = "#D5E8D4"
            calc_amount = "all your"
        else:
            calc_back = "#ffe6cc"
            calc_amount = (f"your recent calculations - "
                           f"showing {c.MAX_CALCS} / {len(calculations)}")

        # strings for long labels
        recent_intro_txt = (f"below are {calc_amount} calculations"
                            f"(to the nearest degree)")

        # create string from calculations list (newest calculations first
        newest_first_string = ""
        newest_first_list = list(reversed(calculations))

        if len(newest_first_string) <= c.MAX_CALCS:

            for item in newest_first_list[:-1]:
                newest_first_string += item + "\n"

            newest_first_string += newest_first_list[-1]

        else:
            for item in newest_first_list[:c.MAX_CALCS-1]:
                newest_first_string += item + "\n"

            newest_first_string += newest_first_list[c.MAX_CALCS-1]

        export_instruction_txt = ("please push export to save your calculations "
                                 "in file if the filename already exists it will be ... ")

        # label list (;abel text / format / bg)
        history_labels_list = [
            ["History / Export", ("Arial", 16, "bold"), None],
            [recent_intro_txt, ("Arial", 11), None],
            [newest_first_string,("Arial", 14), calc_back],
            [export_instruction_txt, ("Arial", 11), None]
        ]

        history_label_ref = []
        for count, item in enumerate(history_labels_list):
            make_label = Label(self.history_box, text=item[0], font=item[1],
                               bg=item[2],
                               wraplength=300, justify="left", pady=10, padx=20)
            make_label.grid(row=count)

            history_label_ref.append(make_label)

        # retrieve export instructions label so that we can
        # configure it to show the filename if the user exports the file
        self.export_filename_label = history_label_ref[3]

        # make frame to hold buttons (two columns )
        self.hist_button_frame = Frame(self.history_box)
        self.hist_button_frame.grid(row=4)

        button_ref_list = []

        # button list (button text / bg color / command / row / column)
        button_detail_list = [
            ["Export", "#004C99",lambda: self.export_data(calculations), 0, 0],
            ["Close", "#666666", partial(self.close_history, partner), 0, 1],
        ]

        for btn in button_detail_list:
            self.make_button = Button(self.hist_button_frame,
                                      font=("Arial", 0 , "bold"),
                                      text=btn[0], bg=btn[1],
                                      fg="#FFFFFF", width=12,
                                      command=btn[2])
            self.make_button.grid(row=btn[3], column=btn[4], padx=10,pady=10)


    def export_data(self, calculations):
        # **** get current date for heading and filename ****
        today = date.today()

        # get day, month and year as individual strings
        day = today.strftime("%d")
        month = today.strftime("%m")
        year = today.strftime("%Y")

        file_name = f"temperatures_{year}_{month}_{day}"
        #edit label so users know that their export has been done
        success_string = ("export successful the file is called"
                          f"{file_name}.txt")
        self.export_filename_label.config(bg="#009900", text=success_string)

        write_to = f"{file_name}.txt"

        with open(write_to, "w") as text_file:
            text_file.write("****** temperature calculations ******\n")
            text_file.write(f"generated: {day}/{month}/{year}\n\n")
            text_file.write("here is your calculation history (oldest to newest)...\n")

            # write the item to file
            for item in calculations:
                text_file.write(item)
                text_file.write("\n")

    def close_history(self,partner):
        """
        Closes help dialogue box (and enables help button)
        """
        #put help button back to normal
        partner.to_history_button.config(state=NORMAL)
        self.history_box.destroy()
# main routine


if __name__ == "__main__":
    root = Tk()
    root.title("Temperature converter")
    Converter()
    root.mainloop()