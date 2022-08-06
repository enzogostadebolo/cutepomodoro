import tkinter
import threading
from time import sleep
from PIL import ImageTk, Image
from playsound import playsound
from plyer import notification


class Pomodoro:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Cute Pomodoro")
        self.window.geometry("500x200")
        self.window.resizable(width=False, height=False)

        self.pomo_counts = 0

        # Images
        self.icon_pic = tkinter.PhotoImage(file="utilities/icon.png")
        self.tomato_pic = ImageTk.PhotoImage(Image.open("utilities/cute tomato.png").resize((100, 100)))

        self.window.iconphoto(False, self.icon_pic)
        self.label_cute_tomato = tkinter.Label(image=self.tomato_pic, height=100, width=100)
        self.label_cute_tomato.pack()

        # Timer n Timer Label
        self.timer_label = tkinter.Label(text="WORK TIME!", font=("sansserif", 20))
        self.timer_label.pack(pady=10)

        self.timer_button = tkinter.Button(text="START POMO!", command=self.threaded_countdown)
        self.timer_button.pack()

        self.window.mainloop()

    def countdown(self):
        if self.pomo_counts % 2 == 0:
            time = 25 * 60  # Work
        else:
            time = 5 * 60  # Break

        while time != -1:
            mins = time // 60
            secs = time % 60
            timer = "{:02d} : {:02d}".format(mins, secs)

            self.timer_label.config(text=timer)

            time -= 1
            sleep(1)
            self.window.update()

        self.pomo_counts += 1
        self.timer_label.config(text="BREAK TIME!")

        notification.notify(
            title="Cute Pomodoro",
            message="THE TIME IS OVER!",
            app_icon="icon.ico"
        )

        playsound("song.mp3")

    def threaded_countdown(self):
        countdown_thread = threading.Thread(target=self.countdown())
        countdown_thread.start()


if __name__ == '__main__':
    Pomodoro()
