# Z1
def functionZad1(a_list, b_list):
    result = []
    for i in range(len(a_list)):
        if i % 2 == 1:
            result.append(a_list[i])
    for i in range(len(b_list)):
        if i % 2 == 0:
            result.append(b_list[i])
    return result

print(functionZad1([1,2,3,4,5], [7,8,9,10]))
    
# Z2
def functionZad2(data_text):
    result = {}
    result['length'] = len(data_text)
    result['letters'] = set(data_text)
    result['big_letters'] = data_text.upper()
    result['small_letters'] = data_text.lower()
    return result

print(functionZad2("Geeks"))

# Z3
def functionZad3(text, letter):
    result = text.replace(letter, "")
    return result

print(functionZad3("Ala ma kota", 'a'))

# Z4
def functionZad4(celsiusTemperature, temperature_type):
    if temperature_type == "Fahrenheit":
        result = celsiusTemperature * 1.8 + 32
    elif temperature_type == "Rankine":
        result = (celsiusTemperature + 273.15) * 1.8
    elif temperature_type == "Kelvin":
        result = celsiusTemperature + 273.15
    else:
        print("Unknown temperature type")
        result = 0
    return result

print(functionZad4(50, "Rankine"))

# Z5
class Calculatr:
    def add(a, b):
        return a + b
    def difference(a, b):
        return a - b
    def multiply(a, b):
        return a * b
    def divide(a, b):
        return a / b

# Z6
class ScienceCalculator(Calculatr):
    def power(a,b):
        return a ** b
    
# Z7
def functionZad7(text):
    return (text[-1:-len(text)-1:-1])

print(functionZad7("koteł"))
