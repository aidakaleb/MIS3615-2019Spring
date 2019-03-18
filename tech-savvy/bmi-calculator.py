import webbrowser

def calculate_bmi(weight, height):
    bmi = 703 * weight / (height * height)
    if bmi <= 18.5:
        webbrowser.open('https://www.mcdonalds.com/us/en-us.html')
        return "your bmi is {:.1f}. You are underweighted.".format(bmi)
    elif bmi <= 25:
        return "your bmi is {:.1f}. You are normal-weighted.".format(bmi) 
    elif bmi < 30:
        return "your bmi is {:.1f}. You are overweighted.".format(bmi) 
    else:
        return "your bmi is {:.1f}. You are obese.".format(bmi) 


weight = input('Enter your weight: ')
height = input('Enter your height: ')
weight = float(weight)
height = float(height)



print(calculate_bmi(weight, height))
