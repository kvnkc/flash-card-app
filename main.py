import tkinter

BACKGROUND_COLOR = "#B1DDC6"

# Flash Card UI
window = tkinter.Tk()
window.title('Flashy')
window.minsize(width=900, height=700)
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
canvas = tkinter.Canvas(width=800, height=526,
                        highlightthickness=0, background=BACKGROUND_COLOR)
card_front = tkinter.PhotoImage(file='./images/card_front.png')
canvas.create_image(400, 263, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)

right_button_image = tkinter.PhotoImage(file='./images/right.png')
wrong_button_image = tkinter.PhotoImage(file='./images/wrong.png')
right_button = tkinter.Button(image=right_button_image, highlightthickness=0)
wrong_button = tkinter.Button(image=wrong_button_image, highlightthickness=0)
right_button.grid(row=1, column=0)
wrong_button.grid(row=1, column=1)

window.mainloop()
