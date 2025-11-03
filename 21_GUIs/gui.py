from nicegui import ui

ui.label("Welcome to NiceGUI!").style("color: purple; font-size: 40px")

# Create a greeting

def greet():
    name = input_field.value.strip()
    msg = f"Hello, {name or "stranger"}"
    ui.notify(msg) # creates a popup

input_field = ui.input("Enter your name")
ui.button("Greet Me!", color="purple", on_click=greet)

# Create a counter
class State:
    count = 0

count_label = ui.label("Count: 0")

def add_one():
    State.count += 1
    count_label.text = f"Count: {State.count}"

ui.button("Add one", color="green", on_click=add_one)

# TODO
# Create a Reset button that resets the count to 0
def reset_count():
    State.count = 0
    count_label.text = f"Count: {State.count}"
ui.button("Reset", color="red", on_click=reset_count)

ui.run(title="Intro to nicegui")