import tkinter as tk
import random as rnd
import time as tm

def start_game():
    global start_time, current_text, index
    # Generate a random sentence from the list
    sentence = rnd.choice(sentences)
    current_text.set(sentence)
    index = 0
    start_time = tm.time()
    entry.config(state=tk.NORMAL)
    entry.focus_set()

def check_text():
    global index
    typed_text = entry.get()
    if typed_text == current_text.get():
        elapsed_time = tm.time() - start_time
        words_per_minute = len(typed_text.split()) / (elapsed_time / 60)
        result_text.set(f"Correct! Your speed: {words_per_minute:.2f} WPM")
    else:
        result_text.set("Incorrect! Try again.")
    entry.delete(0, tk.END)
    entry.config(state=tk.DISABLED)

# List of sentences for the typing test
sentences = [
    "the quick brown fox jumps over the lazy dog",
    "python is a versatile programming language",
    # "OpenAI's ChatGPT provides powerful language modeling capabilities",
    "i love coding and building applications",
    "i love learning new things",
    "engineering is all about learning new things and generating new skills"
]

# Create the Tkinter root window
root = tk.Tk()
root.title("Speed Typing Test")

# Create a label for displaying the current text
current_text = tk.StringVar()
text_label = tk.Label(root, textvariable=current_text, font=("Arial", 14))
text_label.pack(pady=20)

# Create an entry field for typing the text
entry = tk.Entry(root, font=("Arial", 12), width=30, state=tk.DISABLED)
entry.pack(pady=10)

# Create a button to start the test
start_button = tk.Button(root, text="Start", font=("Arial", 12), command=start_game)
start_button.pack(pady=10)

# Create a label for displaying the result
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, font=("Arial", 12))
result_label.pack(pady=20)

# Create a button to check the typed text
check_button = tk.Button(root, text="Check", font=("Arial", 12), command=check_text)
check_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
