# Python File to consolidate all useful functions
import os
from tkinter import *
from tkinter import ttk

import pygame
from PIL import Image, ImageTk


def create_new_window(frame_destroy: Frame = None) -> Frame:
    """Destroys passed frame, and creates new one

    :param frame_destroy: Previous frame to destroy
    :type frame_destroy: Frame, default value: None
    :return: New frame
    :rtype: Frame
    """

    # Destroy previous frame
    if frame_destroy is not None:
        frame_destroy.destroy()

    # Set up new frame
    new_frame = Frame(width=650, height=500, bg="midnight blue")
    new_frame.pack(fill="both", expand=True)

    # Setting the padding between columns
    for i in range(3):
        new_frame.columnconfigure(i, weight=10)

    return new_frame


# Play different sounds
def play_sound(audio_path: str) -> None:
    """Play sound according to passed parameter

    :param audio_path: sound file location in project
    :type audio_path: str
    :return: None
    """

    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play(loops=0)


# Load image into variable (image: name, width, height)
def load_image(image_path: str, width: int, height: int) -> PhotoImage:
    """Gets image file location & size, returns the image as PhotoImage

    :param image_path: image file location in project
    :type image_path: str
    :param width: image width to set
    :type width: int
    :param height: image height to set
    :type height: int
    :return: Loaded image
    :rtype: PhotoImage
    """

    image = Image.open(image_path).resize((width, height))
    image_tk = ImageTk.PhotoImage(image)
    return image_tk


# Render restart button for results frame
def render_restart_button(frame: Frame, row: int, column_span: int) -> None:
    """Renders restart button to screen

    :param frame: Frame to render button on, and then destroy
    :type frame: Frame
    :param row: Render button in grid row
    :type row: int
    :param column_span: horizontal space for button to occupy
    :type column_span: int
    :return: None, renders restart button to screen
    """

    ttk.Button(
        frame,
        text="Restart",
        style="TButton",
        command=lambda: restart_program(frame),
    ).grid(column=0, row=row, columnspan=column_span, pady=20)


def restart_program(frame_to_destroy: Frame) -> None:
    """Stops music if playing, destroys frame and restarts program

    :param frame_to_destroy: Frame to destroy before restart
    :type frame_to_destroy: Frame
    :return: None
    """

    pygame.mixer.music.stop()
    frame_to_destroy.master.destroy()
    os.system("python main.py")
