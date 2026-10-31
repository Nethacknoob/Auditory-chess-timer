import tkinter as tk

# Starting times: 30 minutes each
time1 = 30 * 60.0
time2 = 30 * 60.0

running = False
active_player = 1


def format_time(seconds):
    minutes = int(seconds // 60)
    remaining_seconds = seconds % 60

    return f"{minutes:02}:{remaining_seconds:05.2f}"


def update_timer():
    global time1, time2

    if running:

        if active_player == 1:
            if time1 > 0:
                time1 -= 0.01

        elif active_player == 2:
            if time2 > 0:
                time2 -= 0.01

        timer1_label.config(text=format_time(time1))
        timer2_label.config(text=format_time(time2))

        # Update every 10 milliseconds
        window.after(10, update_timer)


def start_timer():
    global running

    if not running:
        running = True
        update_timer()


def switch_timer():
    global active_player

    if running:
        if active_player == 1:
            active_player = 2
        else:
            active_player = 1


# ---------------- GUI ----------------

window = tk.Tk()
window.title("Chess Timer")
window.geometry("600x400")


player1_label = tk.Label(
    window,
    text="Player 1",
    font=("Arial", 20)
)
player1_label.pack()

timer1_label = tk.Label(
    window,
    text="30:00.00",
    font=("Arial", 50)
)
timer1_label.pack(pady=10)


player2_label = tk.Label(
    window,
    text="Player 2",
    font=("Arial", 20)
)
player2_label.pack()

timer2_label = tk.Label(
    window,
    text="30:00.00",
    font=("Arial", 50)
)
timer2_label.pack(pady=10)


start_button = tk.Button(
    window,
    text="Start",
    font=("Arial", 18),
    command=start_timer
)
start_button.pack(pady=10)


switch_button = tk.Button(
    window,
    text="Switch",
    font=("Arial", 18),
    command=switch_timer
)
switch_button.pack(pady=10)


window.mainloop()