# Function that creates a message
def create_message(prefix, *args):
    s = str(prefix) + ": "
    for arg in args:
        s += str(arg) + " "
    print(s)

def create_mes(*args, **kwargs):
    # Find the key in kwargs
    separator = kwargs.get("separator", " ")
    s = ""
    for arg in args:
        s += str(arg) + separator
    
    return s[:-1]

# Call a function
create_message("Status", "Temp", 25, "Degree")
create_message("Alert", "System", "is", "online")

print(create_mes("a", "b", separator = "-"))