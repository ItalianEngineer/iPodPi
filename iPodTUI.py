import curses
import subprocess
import threading
import os

# Define the path to the click binary in the same directory
CLICK_BINARY_PATH = os.path.join(os.path.dirname(__file__), 'clicky')

# Define the menu options
menu = ['Music', 'Shuffle', 'About', 'Shutdown']
current_option = 0
wheel_positions = 47  # Total positions in the wheel
sensitivity_threshold = wheel_positions // 6  # Scroll down every 1/6th of wheel positions

# Function to handle input from the click script
def handle_input(stdscr):
    global current_option
    process = subprocess.Popen(['sudo', CLICK_BINARY_PATH], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    try:
        while True:
            output = process.stdout.readline()
            if output:
                output = output.strip()
                if 'position' in output:
                    position = int(output.split()[1])
                    if position % sensitivity_threshold == 0 and position != 0:
                        current_option = (current_option + 1) % len(menu)
                        draw_menu(stdscr)
            if process.poll() is not None:
                break
    except KeyboardInterrupt:
        print("Exiting")
    finally:
        process.terminate()

# Function to draw the menu
def draw_menu(stdscr):
    global current_option
    curses.curs_set(0)  # Hide the cursor
    stdscr.clear()
    height, width = stdscr.getmaxyx()
    margin = 2

    for idx, row in enumerate(menu):
        x = margin
        y = height // 2 - len(menu) // 2 + idx
        if idx == current_option:
            stdscr.attron(curses.color_pair(1) | curses.A_BOLD)
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1) | curses.A_BOLD)
            stdscr.attron(curses.color_pair(2))
            stdscr.addstr(y, x + len(row), ' ' * (width - len(row) - margin))
            stdscr.attroff(curses.color_pair(2))
        else:
            stdscr.addstr(y, x, row)

    stdscr.refresh()

def main(stdscr):
    # Initialize color pairs
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)  # Highlight color
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLUE)   # Background color for the bar

    # Start the thread to handle input from the click script
    input_thread = threading.Thread(target=handle_input, args=(stdscr,), daemon=True)
    input_thread.start()

    # Initial draw of the menu
    draw_menu(stdscr)

    # Keep the main thread running to maintain the curses display
    while True:
        stdscr.getch()

curses.wrapper(main)
