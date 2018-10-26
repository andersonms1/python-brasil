
switcher = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}



def extract_int(data, type):
    if type == 1:
        return int(data[:2])
    elif type == 2:
        return int(data[2:4])
    elif type == 3:
        print(int(data[4:8]))
        return int(data[4:8])
    else:
        return -1

data = input('Digite sua data de nascimento(dd/mm/aaaa)')

month = switcher[extract_int(data, 2)]
month = month + ' de '


print('Você nasceu em '+str(extract_int(data, 1))+' de '+month+str(extract_int(data, 3)))

