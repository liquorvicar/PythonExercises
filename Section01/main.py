from string import Template

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


def get_quote_string(quote, author):
    assert len(quote) > 0
    assert len(author) > 0
    return author + " says \"" + quote + "\""


def mad_libs(noun, verb, adjective, adverb):
    mad_lib = Template('Do you $verb your $adjective $noun $adverb? So do I!')
    return mad_lib.substitute(noun=noun, verb=verb, adjective=adjective, adverb=adverb)
