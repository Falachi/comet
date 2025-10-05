from pathlib import Path
import pygame
import tkinter as tk
import sys, os

root = tk.Tk()
root.title("The Real Comet Browser")


def resource_path(filename: str) -> str:
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, filename)
    return str(Path(__file__).parent / "assets" / filename)

gif_path = resource_path("comet.gif")
sound_path = resource_path("click.mp3")
total_frames = 75

pygame.mixer.init()
click_sound = pygame.mixer.Sound(sound_path)

gif_frames = [tk.PhotoImage(file=gif_path, format=f'gif -index {i}') for i in range(1,total_frames)]
label = tk.Label(image=gif_frames[0])

def next_frame(index: int) -> None:
  frame = gif_frames[index]
  index = (index + 1) % (total_frames - 1)
  label.config(image=frame)
  label.image = frame
  root.after(40, next_frame, index)

button = tk.Button(root, text='Click for instant stimuli!', command=lambda: click_sound.play())

label.pack()
button.pack(padx=20, pady=20)

root.after(0, next_frame, 0)

root.mainloop()