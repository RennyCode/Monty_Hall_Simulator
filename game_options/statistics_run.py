from tkinter import ttk
from tkinter import *

from utils.algo_setup import statistics_calculate
from utils.functions import create_new_window, render_restart_button


def statistics(main_frame: Frame) -> None:
    """Creates first statistics window with combobox, containing different options for times to run the algorithm

    :param main_frame: Previous frame to destroy
    :type main_frame: Frame
    :return: None
    """

    # Create new frame for 'PC Multi-Run'
    pc_multirun_frame = create_new_window(main_frame)

    # Set spacings between components on screen
    for i in range(3):
        pc_multirun_frame.grid_rowconfigure(i, weight=1)
        pc_multirun_frame.grid_columnconfigure(i, weight=1)

    # Instructions label for statistics screen
    ttk.Label(pc_multirun_frame, text="Times to Run:", style="ST.Label").grid(
        column=0, row=0, columnspan=3, pady=(100, 0)
    )

    # 'Times to run' combobox set up
    times_to_run = ttk.Combobox(
        pc_multirun_frame,
        width=20,
        state="readonly",
        justify=CENTER,
        font=("Arial", "12"),
    )
    times_to_run["values"] = (
        100,
        500,
        1000,
        2500,
        5000,
        10000,
        25000,
        100000,
        500000,
        1000000,
    )
    times_to_run.set(100)
    times_to_run.grid(column=1, row=1)

    # Select button
    ttk.Button(
        pc_multirun_frame,
        text="Select",
        style="TButton",
        command=lambda: statistics_res(pc_multirun_frame, int(times_to_run.get())),
    ).grid(column=0, row=2, columnspan=3, pady=(0, 100))

    mainloop()


def statistics_res(pc_multirun_frame: Frame, n: int) -> None:
    """Creates 2nd statistics screen, presenting results of n-times running the algorithm: \n
    * Number of games \n
    * Number of wins \n
    * Number of losses \n
    * Wins / Losses ratio \n
    PC always changes his choice

    :param pc_multirun_frame: Previous frame to destroy
    :type pc_multirun_frame: Frame
    :param n: Times to run
    :type n: int
    :return: None
    """

    # Create new frame for displaying the results
    pc_multirun_frame_res = create_new_window(pc_multirun_frame)

    # Set spacings between components on screen
    for i in range(6):
        pc_multirun_frame_res.grid_rowconfigure(i, weight=1)
    for i in range(4):
        pc_multirun_frame_res.grid_columnconfigure(i, weight=1)

    # Run the Monty Hall algorithm
    condition_bool, n, wins, losses = statistics_calculate(n)

    # Number of games text
    stats_row(pc_multirun_frame_res, "Number of games: ", str(n), 0, True)

    # Wins text
    stats_row(pc_multirun_frame_res, "Number of wins: ", str(wins), 1)

    # Losses text
    stats_row(pc_multirun_frame_res, "Number of losses: ", str(losses), 2)

    # Ratio text
    stats_row(
        pc_multirun_frame_res,
        "Wins / Losses ratio: ",
        "{:.2f}".format(wins / losses),
        3,
    )

    # Restart button
    render_restart_button(pc_multirun_frame_res, 4, 4)

    mainloop()


def stats_row(
    frame: Frame, first_text: str, second_text: str, row: int, pad: bool = False
) -> None:
    """Renders single stats row to screen, depends on parameters passed

    :param frame: Frame to render on
    :type frame: Frame
    :param first_text: Description of row
    :type first_text: str
    :param second_text: Final result of what is said in the description
    :type second_text: str
    :param row: Render text to grid row
    :type row: int
    :param pad: variable to determine padding between rows
    :type pad: bool
    :return: None
    """

    # Render first text
    Label(
        frame,
        text=first_text,
        bg="midnight blue",
        fg="gray70",
        font=("Arial", 11, "bold"),
    ).grid(column=1, row=row, pady=(40, 0) if pad else None, sticky=W)

    # Render second text
    ttk.Label(frame, text=second_text, style="PN.Label").grid(
        column=2, row=row, pady=(40, 0) if pad else None, sticky=E
    )
