from time import gmtime
from string import Template

age = int(input("What's your age? "))
desired_retirement = int(input("What age do you want to retire at? "))

values = {
    'years_to_retirement': desired_retirement - age,
    'current_year': gmtime().tm_year
}
values['retirement_year'] = values['current_year'] + values['years_to_retirement']

if values['years_to_retirement'] > 0:
    output = Template("You have $years_to_retirement years left until you can retire.\n"
                      "It's $current_year, so you can retire in $retirement_year.\n")
else:
    output = Template("It's $current_year; you've reached your retirement age. What are you doing working??")

print(output.substitute(values))
