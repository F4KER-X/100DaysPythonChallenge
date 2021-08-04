import tkinter
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0

# ------------------------- TIMER MECHANISM ---------------------------- #


def start():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        countdown(work_sec)
        timer_label.config(text="Work", fg=GREEN)
# ------------------------- COUNTDOWN MECHANISM ---------------------------- #


def countdown(count):

    count_min = count//60
    count_sec = count % 60

    if count_sec < 10:
        count_sec = "0" + str(count_sec)

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start()
        marks = ""
        work_sessions = int(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()

window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = tkinter.PhotoImage(file=r'Day 028 - Pomodoro\tomato.png')
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill='white',
                                font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)


reset_button = tkinter.Button(
    text='Reset', command=reset, highlightthickness=0)
reset_button.grid(row=2, column=2)

start_button = tkinter.Button(
    text="Start", command=start, highlightthickness=0)
start_button.grid(row=2, column=0)

timer_label = tkinter.Label(text="Timer", fg=GREEN,
                            bg=YELLOW, font=(FONT_NAME, 50))
timer_label.grid(row=0, column=1)

check_marks = tkinter.Label(bg=YELLOW, fg=GREEN)
check_marks.grid(row=3, column=1)


window.mainloop()
