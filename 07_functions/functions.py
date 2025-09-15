# Function that creates a message
def create_message(prefix, *args):
    s = str(prefix) + ": "
    for arg in args:
        s += str(arg) + " "
    print(s)

def create_mes(*args, **kwargs):
    # Find the key in kwargs
    separator = kwargs.get("separator", " ")
    prefix = kwargs.get("prefix", "Q")
    suffix = kwargs.get("suffix", 1)
    msg = prefix + separator.join(args) + suffix

    return msg

# Call a function
create_message("Status", "Temp", 25, "Degree")
create_message("Alert", "System", "is", "online")

print(create_mes("a", "b", separator = "-", prefix = "start", suffix = "end"))

# Qpy-th-on1
print(create_mes("py", "th", "on", separator = "-", prefix = "Q", suffix = "1"))