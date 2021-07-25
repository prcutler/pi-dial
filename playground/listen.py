from keyboard_listener import KeyboardListener, Combo, KeyWord


def function_1(string):
    print(f"This function prints {string}")


def function_2(string):
    print(f"This function prints {string}")


combinations = {
    "function 1": Combo(["alt"], "f", function_1, "hello world"),
    # Function 1 is executed when the user presses Alt+F
    "function 2": Combo(["ctrl", "alt"], "g", function_2, "goodbye world"),
    # Function 2 is executed when the user presses Alt+G
    "function 3": Combo(["shift", "alt"], "H", function_2, "hello again world"),
    # Be mindful when setting up Combos that include 'shift'. If the Combo includes the shift key, the character must be uppercase.
}

keywords = {
    "keyword_1": KeyWord("keyword1", function_1, "hello world"),
    # Function 1 is executed when the user types 'keyword1'
    "keyword_2": KeyWord("keyword2", function_2, "goodbye world")
    # Function 2 is executed when the user types 'keyword2'
}

keyboard_listener = KeyboardListener(combinations=combinations, keywords=keywords)
keyboard_listener.run()
