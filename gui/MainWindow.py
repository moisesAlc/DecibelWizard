import tkinter as tk
import tkinter.ttk as ttk
from gui.gui_utils import get_style, get_file_gui, get_save_destination_gui
from video.utils import get_duration


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        # region Input and Output Properties
        self.input_file_duration = None
        self.input_file = None
        self.output_file = None
        # endregion

        # region Constants
        self.APP_NAME = "Decibel Wizard"
        self.WIDTH = "600"
        self.HEIGHT = "350"
        self.ICON_URL = r'.\\img\\icone.ico'
        self.LOGO_URL = r'.\\logo20px.png'
        self.WIDGET_WIDTH = 20
        self.FOREGROUND_COLOR = '#FFFFFF'
        self.FONT_FAMILY = 'Helvetica'
        self.FONT_SIZE_BODY = 18
        self.PADY = 15
        # endregion

        # region App Configuration
        self.title(self.APP_NAME)
        self.resizable(True, True)
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        # self.iconbitmap(self.ICON_URL)
        self.logo = tk.PhotoImage(file=self.LOGO_URL)
        style = get_style(self)
        style.configure('my.TButton', font=(self.FONT_FAMILY, self.FONT_SIZE_BODY))

        # endregion

        self.output_begin_time = tk.DoubleVar()
        self.output_end_time = tk.DoubleVar()

        # region Upper Frame Config

        self.frame_upper = ttk.Frame(self)

        self.logo = ttk.Label(
            self.frame_upper,
            anchor="w",
            image=self.logo)

        self.lbl_app_name = ttk.Label(
            self.frame_upper,
            text=self.APP_NAME,
            font=(self.FONT_FAMILY, 30),
            anchor="e")

        self.logo.pack(side="left")
        self.lbl_app_name.pack(side="right", padx=15)
        self.frame_upper.pack(pady=self.PADY + 10)

        # endregion

        self.frame_main = ttk.Frame(self)

        self.input_file_button = ttk.Button(
            self.frame_main,
            text="Input File",
            width=self.WIDGET_WIDTH,
            command=lambda: self.input_file_click()
        )

        self.input_file_label = ttk.Label(
            self.frame_main,
            text='',
            wraplength=self.WIDGET_WIDTH * 15,
            foreground=self.FOREGROUND_COLOR,
            justify="center",
        )

        self.output_file_button = ttk.Button(
            self.frame_main,
            text="Output File",
            width=self.WIDGET_WIDTH,
            command=lambda: self.output_file_click()
        )

        self.output_file_label = ttk.Label(
            self.frame_main,
            text='',
            wraplength=self.WIDGET_WIDTH * 15,
            foreground=self.FOREGROUND_COLOR,
            justify="center",
        )

        self.begin_timespan_label = ttk.Label(
            self.frame_main,
            text='Begin of Time Span',
            foreground=self.FOREGROUND_COLOR,
            justify="center",
        )

        self.begin_timespan_scale = ttk.Scale(
            self.frame_main,
        )

        self.end_timespan_label = ttk.Label(
            self.frame_main,
            text='Enf of Time Span',
            foreground=self.FOREGROUND_COLOR,
            justify="center",
        )

        self.end_timespan_scale = ttk.Scale(
            self.frame_main,
        )

        self.input_file_button.grid(row=0, column=0, padx=10, pady=self.PADY)
        self.input_file_label.grid(row=0, column=1, padx=10, pady=self.PADY)
        self.output_file_button.grid(row=1, column=0, padx=10, pady=self.PADY)
        self.output_file_label.grid(row=1, column=1, padx=10, pady=self.PADY)

        self.frame_main.pack()

    def input_file_click(self):
        self.input_file = get_file_gui()
        self.input_file_label.configure(text=self.input_file)
        self.input_file_duration = get_duration(self.input_file)
        self.cursor_arrow()

    def output_file_click(self):
        self.output_file = get_save_destination_gui().name
        self.output_file_label.configure(text=self.output_file)

        self.begin_timespan_scale.configure(
            from_=0.0,
            to=float(self.input_file_duration)
        )

        # Makes the scale section visible

        self.begin_timespan_label.grid(row=2, column=0, padx=10, pady=self.PADY)
        self.end_timespan_label.grid(row=3, column=0, padx=10, pady=self.PADY)

        self.output_end_time = self.input_file_duration

        self.begin_timespan_scale = ttk.Scale(
            self.frame_main,
            from_=self.output_begin_time.get(),
            to=self.output_end_time,
            variable=self.output_begin_time,
            command=self.slider_changed
        )
        self.begin_timespan_scale.grid(row=2, column=1, padx=10, pady=self.PADY)

        self.end_timespan_scale = ttk.Scale(
            # This is pointing to the same as the other scale. Might create bugs! Watch out!
            self.frame_main,
            from_=self.output_begin_time.get(),
            to=self.output_end_time,
            variable=self.output_end_time,
            command=self.slider_changed
        )
        self.end_timespan_scale.grid(row=3, column=1, padx=10, pady=self.PADY)

        self.frame_main.pack()

    def slider_changed(self, event):
        print(self.begin_timespan_scale.get())
        print(self.end_timespan_scale.get())
        self.begin_timespan_label.configure(text=self.get_scale_begin_value())
        self.end_timespan_label.configure(text=self.get_scale_end_value())

    def get_scale_begin_value(self):
        return 'Corte começando em {: .2f} segundos'.format(self.begin_timespan_scale.get())

    def get_scale_end_value(self):
        return 'e terminando em {: .2f} segundos.'.format(self.end_timespan_scale.get())

    def cursor_hourglass(self):
        self.config(cursor="watch")

    def cursor_arrow(self):
        pass
        self.config(cursor="arrow")


if __name__ == '__main__':
    MainWindow().mainloop()
