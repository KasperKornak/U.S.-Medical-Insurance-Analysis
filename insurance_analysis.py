import csv
import numpy as np
import matplotlib.pyplot as plt


with open('insurance.csv') as csvfile:
    insurance_db = list(csv.DictReader(csvfile))

#relationship between smoking status and price
def smoking_price():
    smoker_count = 0
    smokers_charges = 0
    non_smoker_count = 0
    non_smokers_charges = 0

    for person in range(len(insurance_db)):
        temp = 0
        if insurance_db[person]['smoker'] == 'yes':
            temp = insurance_db[person]['charges']
            smokers_charges += float(temp)
            smoker_count += 1
        elif insurance_db[person]['smoker'] == 'no':
            temp = insurance_db[person]['charges']
            non_smokers_charges += float(temp)
            non_smoker_count += 1


    average_non_smoker_charge = round(non_smokers_charges/non_smoker_count,2)
    average_smoker_charge = round(smokers_charges/smoker_count,2)
    difference = round(average_smoker_charge/average_non_smoker_charge,2)
    print('Average insurance charge for non-smokers is: ' + str(average_non_smoker_charge) + ' dollars.\nAverage insurance charge for smokers is: ' + str(average_smoker_charge) + ' dollars.\nSmokers pay on average ' + str(difference) + ' times more for insurance than non-smokers')
    return ''

#relationship between person's BMI and price
def bmi_price():
    bmi_dict = {'Underweight': 18.5,
                'Normal': 24.9,
                'Overweight': 29.9,
                'Obese': 34.9}

    bmi_charges = {'Underweight': 0,
                'Normal': 0,
                'Overweight': 0,
                'Obese': 0,
                'Extremely Obese': 0}

    bmi_count = {'Underweight': 0,
                'Normal': 0,
                'Overweight': 0,
                'Obese': 0,
                'Extremely Obese': 0}

    for person in range(len(insurance_db)):
        temp = 0
        temp_charge = 0
        temp_count = 0
        temp_man = 0
        if float(insurance_db[person]['bmi']) < bmi_dict['Underweight']:
            temp_charge = bmi_charges['Underweight']
            temp = temp_charge + float(insurance_db[person]['charges'])
            bmi_charges.update({'Underweight':temp})
            temp_count = float(bmi_count['Underweight'])
            temp_man = temp_count + 1
            bmi_count.update({'Underweight': temp_man})
        elif float(insurance_db[person]['bmi']) < bmi_dict['Normal'] and float(insurance_db[person]['bmi']) >= bmi_dict['Underweight']:
            temp_charge = bmi_charges['Normal']
            temp = temp_charge + float(insurance_db[person]['charges'])
            bmi_charges.update({'Normal': temp})
            temp_count = float(bmi_count['Normal'])
            temp_man = temp_count + 1
            bmi_count.update({'Normal': temp_man})
        elif float(insurance_db[person]['bmi']) < bmi_dict['Overweight'] and float(insurance_db[person]['bmi']) >= bmi_dict['Normal']:
            temp_charge = bmi_charges['Overweight']
            temp = temp_charge + float(insurance_db[person]['charges'])
            bmi_charges.update({'Overweight': temp})
            temp_count = float(bmi_count['Overweight'])
            temp_man = temp_count + 1
            bmi_count.update({'Overweight': temp_man})
        elif float(insurance_db[person]['bmi']) < bmi_dict['Obese'] and float(insurance_db[person]['bmi']) >= bmi_dict['Overweight']:
            temp_charge = bmi_charges['Obese']
            temp = temp_charge + float(insurance_db[person]['charges'])
            bmi_charges.update({'Obese': temp})
            temp_count = float(bmi_count['Obese'])
            temp_man = temp_count + 1
            bmi_count.update({'Obese': temp_man})
        elif float(insurance_db[person]['bmi']) >= bmi_dict['Obese']:
            temp_charge = bmi_charges['Extremely Obese']
            temp = temp_charge + float(insurance_db[person]['charges'])
            bmi_charges.update({'Extremely Obese': temp})
            temp_count = float(bmi_count['Extremely Obese'])
            temp_man = temp_count + 1
            bmi_count.update({'Extremely Obese': temp_man})
    average_charge_bmi = {'Underweight': round(bmi_charges['Underweight']/bmi_count['Underweight'],2),
                          'Normal': round(bmi_charges['Normal']/bmi_count['Normal'],2),
                          'Overweight': round(bmi_charges['Overweight']/bmi_count['Overweight'],2),
                          'Obese': round(bmi_charges['Obese'] / bmi_count['Obese'],2),
                          'Extremely Obese': round(bmi_charges['Extremely Obese'] / bmi_count['Extremely Obese'],2)
                          }

    x =[]
    for person in range(len(insurance_db)):
        x.append(float(insurance_db[person]['bmi']))

    y = []
    for person in range(len(insurance_db)):
        y.append(float(insurance_db[person]['charges']))

    x_plot = []
    y_plot = []
    sorted_list = sorted(list(zip(x,y)))

    for i in range(len(sorted_list)):
        x_plot.append(sorted_list[i][0])
        y_plot.append(sorted_list[i][1])

    plt.scatter(x_plot,y_plot, s =2)
    plt.title('Scatterplot of individuals concerning BMI and insurance price',fontsize = 10)
    plt.xlabel('BMI')
    plt.ylabel('Insurance cost in USD')
    plt.show(block = False)
    plt.pause(3)
    plt.close('all')
    print('Underweight people pay on average: ' + str(average_charge_bmi['Underweight']) +  ' ,people within Normal range pay: ' + str(average_charge_bmi['Normal']) + ' ,overweight people average charge is: ', str(average_charge_bmi['Overweight']) + ' ,obese and extremely obese people pay: ' + str(average_charge_bmi['Obese']) + ' and'  + str(average_charge_bmi['Extremely Obese']) + ' dollars for insurance.')
    return ''
#average age and kids
def age_kids():
    kids = {'0 kids': 0,
            '1 kid': 0,
            '2 kids': 0,
            '3 or more': 0}

    kids_0 = 0
    kids_1 = 0
    kids_2 = 0
    kids_more = 0

    for person in range(len(insurance_db)):
        temp = 0
        temp_kid = 0
        if insurance_db[person]['children'] == '0':
            kids_0 += 1
            temp_kid = float(kids['0 kids'])
            temp = int(insurance_db[person]['age']) + temp_kid
            kids.update({'0 kids':temp})
        elif insurance_db[person]['children'] == '1':
            kids_1 += 1
            temp_kid = float(kids['1 kid'])
            temp = int(insurance_db[person]['age']) + temp_kid
            kids.update({'1 kid':temp})
        elif insurance_db[person]['children'] == '2':
            kids_2 += 1
            temp_kid = float(kids['2 kids'])
            temp = int(insurance_db[person]['age']) + temp_kid
            kids.update({'2 kids':temp})
        else:
            kids_more += 1
            temp_kid = float(kids['3 or more'])
            temp = int(insurance_db[person]['age']) + temp_kid
            kids.update({'3 or more':temp})

    x = [0, 1, 2, 3]
    y1 = round(kids['0 kids']/kids_0)
    y2 = round(kids['1 kid']/kids_1)
    y3 = round(kids['2 kids']/kids_2)
    y4 = round(kids['3 or more']/kids_more)
    y = [y1, y2, y3, y4]
    default_x_ticks = range(len(x))
    labs = ['Zero', 'One', 'Two', 'Three or more']

    plt.bar(x,y)
    plt.title('Number of children and average age of parent', fontsize=10)
    plt.xlabel('Number of children')
    plt.ylabel('Average age')
    plt.xticks(default_x_ticks, labs)
    plt.ylim(ymin=32, ymax=42)
    plt.show(block=False)
    plt.pause(3)
    plt.close('all')
    return ''

#main loop
state = 1
option = 0
while state > 0:
    print('Hi, you can see the following analysis:')
    print('1. Relationship between smoking status and price.')
    print('2. Relationship between person\'s BMI and price.')
    print('3. Average age of parents in dataset.')
    option = input('Select between 1, 2 and 3:')
    select = ''
    if option == '1':
        print(smoking_price())
        print('Do you wish to continue (y/n)?')
        select = input(select)
        if select == 'y':
            state = 1
        elif select == 'n':
            state = 0
        else:
            print('you chose bad key, continuing')
            state= 1
    elif option == '2':
        print(bmi_price())
        print('Do you wish to continue (y/n)?')
        select = input(select)
        if select == 'y':
            state = 1
        elif select == 'n':
            state = 0
        else:
            print('you chose bad key, continuing')
            state= 1
    elif option == '3':
        print(age_kids())
        print('Do you wish to continue (y/n)?')
        select = input(select)
        if select == 'y':
            state = 1
        elif select == 'n':
            state = 0
        else:
            print('you chose bad key, continuing')
            state= 1
    else:
        print('Do you want to continue? You chose bad key. Press y to continue, any other button to exit')
        select = input(select)
        if select == 'y':
            state = 1
        else:
            state = 0
