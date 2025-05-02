import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Fully Functional Calculator")
        self.geometry("400x600")
        self.resizable(True, True)

        self.expression = ""

        self.input_text = tk.StringVar()

        # Entry Frame
        input_frame = tk.Frame(self, width=400, height=50, bd=0)
        input_frame.pack(side=tk.TOP)

        input_field = tk.Entry(
            input_frame, 
            font=('Arial', 24), 
            textvariable=self.input_text, 
            width=50, 
            bg="#eee", 
            bd=0, 
            justify=tk.RIGHT
        )
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=20)

        # Buttons Frame
        btns_frame = tk.Frame(self, bg="grey")
        btns_frame.pack(expand=True)

        # Button Layout
        buttons = [
            ['C', '/', '*', '-'],
            ['7', '8', '9', '+'],
            ['4', '5', '6', '='],
            ['1', '2', '3', '.'],
            ['0', '%']
        ]

        for r, row in enumerate(buttons):
            for c, char in enumerate(row):
                btn = tk.Button(
                    btns_frame, 
                    text=char, 
                    width=10, 
                    height=3, 
                    font=("Arial", 18),
                    fg="white" if char in ['C', '/', '*', '-', '+', '=', '%'] else "black",
                    bg="#2196F3" if char in ['/', '*', '-', '+', '='] else "#f44336" if char == 'C' else "#eee",
                    command=lambda ch=char: self.on_button_click(ch)
                )
                btn.grid(row=r, column=c, padx=5, pady=5, sticky="nsew")

        # Expand columns equally
        for i in range(4):
            btns_frame.grid_columnconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.input_text.set("")
        elif char == '=':
            try:
                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result
            except Exception:
                self.input_text.set("Error")
                self.expression = ""
        else:
            self.expression += str(char)
            self.input_text.set(self.expression)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()

