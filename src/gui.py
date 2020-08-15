
# Title:ferret.py
# Description:
# Development Environment:Ubuntu 18/Python 3.6.9
# Author:Guy Cole (guycole at gmail dot com)
#
import logging
import tkinter

class FerretGui:
    def __init__(self):
        self.logger = logging.getLogger()

    def execute(self):
        print("execute")
        main_window = tkinter.Tk()

        numeric_pad = tkinter.Frame(master=main_window, relief="groove", borderwidth=5)
        numeric_pad.grid()
#        tkinter.Button(self, text='7', width=5, )

        greeting = tkinter.Label(text="byteme")
        greeting.pack()
        main_window.mainloop()


print("start")

#
# argv[1] = configuration filename
#
if __name__ == "__main__":
    ferret_gui = FerretGui()
    ferret_gui.execute()

#    if len(sys.argv) > 1:
#        file_name = sys.argv[1]
#    else:
#        file_name = "config.yaml"
#
#    logging_level = logging.DEBUG
#
#    with open(file_name, "r") as infile:
#        try:
#            ferret = Ferret(logging_level, yaml.load(infile, Loader=yaml.FullLoader))
#            ferret.execute()
#        except yaml.YAMLError as exception:
#            print(exception)

print("stop")

# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***
