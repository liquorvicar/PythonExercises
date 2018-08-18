from string import Template
from math import floor

values = {
    'people': int(input('How many people? ')),
    'pizzas': int(input('How many pizzas are there? '))
}

SLICES_PER_PIZZA = 8
values['slices_each'] = floor(values['pizzas'] * SLICES_PER_PIZZA / values['people'])
values['slices_left'] = values['pizzas'] * SLICES_PER_PIZZA % values['people']

output = Template("$people people with $pizzas pizzas\n"
                  "Each person gets $slices_each slices\n"
                  "With $slices_left left over")
print(output.substitute(values))
