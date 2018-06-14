def issue_greeting(name):
    return 'Hello, ' + name + ', nice to meet you!'


def ask_name():
    return input('What is your name? ')


def get_length(string):
    return len(string)


def ask_for_string():
    return input('What is the input string? ')


def get_output_message(string):
    return string + ' has ' + str(get_length(string)) + ' characters'

