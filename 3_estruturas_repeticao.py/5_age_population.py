country_a = int(input('Digite a população do primeiro pais')) 
up_rate_ca = float(input('Digite a taxa de crescimento do primeiro pais')) 

country_b = int(input('Digite a população do segundo pais')) 
up_rate_cb = float(input('Digite a taxa de crescimento do segundo pais'))

while country_b > country_a:
    print()
    print('cA -> ' + str(country_a))
    print('cB -> ' + str(country_b))

    country_a  = country_a + (country_a * up_rate_ca/100)
    country_b = country_b + (country_b * up_rate_cb/100)

print()
print('cA -> ' + str(country_a))
print('cB -> ' + str(country_b))