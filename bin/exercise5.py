from string import Template

first = int(input("What's the first number? "))
second = int(input("What's the second number? "))

total = first + second
diff = first - second
product = first * second
quotient = first / second

output = Template("$first + $second = $sum\n$first - $second = $diff\n"
                  "$first * $second = $product\n$first / $second = $quotient\n")

print(output.substitute(first=first, second=second, sum=total, diff=diff, product=product, quotient=quotient))
