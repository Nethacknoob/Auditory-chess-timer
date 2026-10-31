import tkinter as tk

# -----------------------
# Timer settings
# -----------------------
START_TIME = 30 * 60  # 30 minutes in seconds

white_time = START_TIME
black_time = START_TIME

active_player = None
game_started = False
timer_job = None


# -----------------------
# Display time as MM:SS
# -----------------------
def format_time(seconds):
    minutes = seconds // 60
    secs = seconds % 60
    return f"{minutes:02}:{secs:02}"


# -----------------------
# Update timer
# -----------------------
def update_timer():
    global white_time, black_time, timer_job

    if not game_started:
        return

    if active_player == "white":
        if white_time > 0:
            white_time -= 1
            white_timer.config(text=format_time(white_time))
        else:
            white_timer.config(text="00:00")
            stop_game()
            return

    elif active_player == "black":
        if black_time > 0:
            black_time -= 1
            black_timer.config(text=format_time(black_time))
        else:
            black_timer.config(text="00:00")
            stop_game()
            return

    timer_job = root.after(1000, update_timer)


# -----------------------
# Start game
# -----------------------
def start_game():
    global game_started, active_player

    if game_started:
        return

    game_started = True
    active_player = "white"

    status_label.config(text="White's turn")

    start_button.config(state="disabled")
    switch_button.config(state="normal")

    update_timer()


# -----------------------
# Switch clocks
# -----------------------
def switch_player(event=None):
    global active_player

    if not game_started:
        return

    if active_player == "white":
        active_player = "black"
        status_label.config(text="Black's turn")

    elif active_player == "black":
        active_player = "white"
        status_label.config(text="White's turn")


# -----------------------
# Stop game
# -----------------------
def stop_game():
    global game_started, active_player

    game_started = False
    active_player = None

    status_label.config(text="Time's up!")
    switch_button.config(state="disabled")


# -----------------------
# GUI
# -----------------------
root = tk.Tk()
root.title("Chess Timer")
root.geometry("600x400")

# Title
title_label = tk.Label(
    root,
    text="Chess Timer",
    font=("Arial", 28, "bold")
)
title_label.pack(pady=20)


# Timer area
timer_frame = tk.Frame(root)
timer_frame.pack(pady=20)


# White
white_frame = tk.Frame(timer_frame)
white_frame.grid(row=0, column=0, padx=50)

white_name = tk.Label(
    white_frame,
    text="WHITE",
    font=("Arial", 18, "bold")
)
white_name.pack()

white_timer = tk.Label(
    white_frame,
    text="30:00",
    font=("Arial", 45)
)
white_timer.pack()


# Black
black_frame = tk.Frame(timer_frame)
black_frame.grid(row=0, column=1, padx=50)

black_name = tk.Label(
    black_frame,
    text="BLACK",
    font=("Arial", 18, "bold")
)
black_name.pack()

black_timer = tk.Label(
    black_frame,
    text="30:00",
    font=("Arial", 45)
)
black_timer.pack()


# Status
status_label = tk.Label(
    root,
    text="Press Start Game",
    font=("Arial", 16)
)
status_label.pack(pady=10)


# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

start_button = tk.Button(
    button_frame,
    text="Start Game",
    font=("Arial", 16),
    width=12,
    command=start_game
)
start_button.grid(row=0, column=0, padx=10)

switch_button = tk.Button(
    button_frame,
    text="Switch",
    font=("Arial", 16),
    width=12,
    command=switch_player,
    state="disabled"
)
switch_button.grid(row=0, column=1, padx=10)


# -----------------------
# Keyboard controls
# -----------------------

# Spacebar switches clocks
root.bind("<space>", switch_player)


# Start GUI
root.mainloop()