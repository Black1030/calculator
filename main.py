import tkinter as jh

window = jh.Tk()
window.title("calculate")
window.geometry("500x550")
window.resizable(True, True)
window.configure(bg="black")


# функция для вычисления операций
def calculate(operation):
    global formula

    if operation == "C":
        formula = ""
    elif operation == "del":
        formula = formula[:-1]
    elif operation == "x^2":
        formula = str(eval(formula) ** 2)
    elif operation == "=":
        formula = str(eval(formula))
    else:
        if formula == "0":
            formula = ""
        formula += operation
    lable_text.configure(text=formula)


# создание окна для вывода вычислений
formula = "0"
lable_text = jh.Label(text=formula, font=("Roboto", 30, "bold"), bg="black", fg="white")
lable_text.place(x=11, y=50)

buttons = ["C", "del", "*", "=", "1", "2", "3", "/", "4", "5", "6", "+", "7", "8", "9", "-", "0", "%", "x^2"]
x = 18
y = 140
for button in buttons:
    get_lbl = lambda x=button: calculate(x)
    jh.Button(text=button, bg="blue", font=("Roboto", 20), command=get_lbl).place(x=x, y=y, width=115, height=79)
    x += 117
    if x > 400:
        x = 18
        y += 81

window.mainloop()





