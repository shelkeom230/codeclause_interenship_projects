import os
import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("MP3 Music Player")
        self.root.geometry("500x400")

        root.configure(bg='lightgreen')
        self.heading_label = tk.Label(root, text='Mp3 music player by Omkar Shelke', font=('Calibri', 25, 'bold'), background='lightgreen')
        self.heading_label.pack(pady=15)

        self.playlist = []
        self.current_index = 0
        self.paused = False

        self.current_song_label = tk.Label(root, text="Currently Playing: None", font=("Arial", 10, "italic"))
        self.current_song_label.pack(pady=10)

        self.load_button = tk.Button(root, text="Load Playlist", command=self.load_playlist)
        self.load_button.pack(pady=5)

        self.play_button = tk.Button(root, text="Play", command=self.play_music)
        self.play_button.pack(pady=5)

        self.pause_button = tk.Button(root, text="Pause", command=self.pause_music)
        self.pause_button.pack(pady=5)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_music)
        self.stop_button.pack(pady=5)

        self.next_button = tk.Button(root, text="Next", command=self.next_music)
        self.next_button.pack(pady=5)
        
        self.previous_button=tk.Button(root,text='Previous',command=self.previous_music)
        self.previous_button.pack(pady=5)

        # Initialize mixer only once
        pygame.mixer.init()

    def load_playlist(self):
        file_paths = filedialog.askopenfilenames(filetypes=[("MP3 files", "*.mp3")])

        if file_paths:
            self.playlist = list(file_paths)
            self.current_index = 0

    def play_music(self):
        if not self.playlist:
            tk.messagebox.showinfo("Error", "No playlist loaded.")
            return

        if self.paused:
            pygame.mixer.music.unpause()
            self.paused = False
        else:
            file_path = self.playlist[self.current_index]
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()
            self.update_current_song_label(file_path)

    def pause_music(self):
        pygame.mixer.music.pause()
        self.paused = True

    def stop_music(self):
        pygame.mixer.music.stop()
        self.paused = False

    def next_music(self):
        if not self.playlist:
            tk.messagebox.showinfo("Error", "No playlist loaded.")
            return

        self.current_index = (self.current_index + 1) % len(self.playlist)
        self.stop_music()
        self.play_music()

    def previous_music(self):
        if not self.playlist:
            tk.messagebox.showinfo("Error", "No playlist loaded.")
            return

        if self.current_index == 0:
            self.current_index = len(self.playlist) - 1
        else:
            self.current_index = (self.current_index - 1) % len(self.playlist)

        self.stop_music()
        self.play_music()

    def update_current_song_label(self, file_path):
        song_name = os.path.basename(file_path)
        self.current_song_label.config(text=f"Currently Playing ({self.current_index + 1}/{len(self.playlist)}): {song_name}")

    def update_current_song_label(self, file_path):
        song_name = os.path.basename(file_path)
        self.current_song_label.config(text=f"Currently Playing: {song_name}")

if __name__ == "__main__":
    root = tk.Tk()
    music_player = MusicPlayer(root)
    root.mainloop()
