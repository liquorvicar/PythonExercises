from string import Template

FT_TO_METRES = 0.09290304

values = {
    'length': int(input('Length in feet: ')),
    'width': int(input('Width in feet: '))
}

values['area_in_feet'] = values['length'] * values['width']
values['area_in_metres'] = round(values['area_in_feet'] * FT_TO_METRES, 3)

output = Template("You entered dimensions of $width feet by $length feet\n"
                  "The area is\n"
                  "$area_in_feet square feet\n"
                  "$area_in_metres square metres\n")

print(output.substitute(values))
