# Python File to consolidate all useful functions
import os
from tkinter import *

import pygame
from PIL import Image, ImageTk


# Create new frame
def create_new_window(frame_destroy: Frame = None) -> Frame:
    # Destroy previous frame
    if frame_destroy is not None:
        frame_destroy.destroy()
    new_frame = Frame(width=650, height=500, bg="midnight blue")
    new_frame.pack(fill="both", expand=True)

    # Setting the padding between columns
    for i in range(3):
        new_frame.columnconfigure(i, weight=10)

    return new_frame


# Play different sounds
def play_sound(audio_path: str) -> None:
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play(loops=0)


# Load image into variable (image: name, width, height)
def load_image(image_path: str, width: int, height: int) -> PhotoImage:
    image = Image.open(image_path).resize((width, height))
    image_tk = ImageTk.PhotoImage(image)
    return image_tk


def restart_program(frame_to_destroy: Frame) -> None:
    frame_to_destroy.master.destroy()
    os.system("python main.py")
