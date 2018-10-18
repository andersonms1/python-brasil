country_a = 80000 
country_b = 200000 

while country_b > country_a:
    print()
    print('cA -> ' + str(country_a))
    print('cB -> ' + str(country_b))

    country_a  = country_a + (country_a * 3/100)
    country_b = country_b + (country_b * 1.5/100)

print()
print('cA -> ' + str(country_a))
print('cB -> ' + str(country_b))