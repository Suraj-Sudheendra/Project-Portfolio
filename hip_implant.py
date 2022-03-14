import math

#Gianluca
def func1(canal_diameter, body_weight, ult_ten_strength):

    min_stem_dia = 13
    app_tens_stress = 0
    new_list= []    
    femoral_head_offset=29                                
    print("Nyota's Body Weight is:", "\t", '\t', '\t','\t', round(body_weight,1),"N")                                
    #print Nyota's body weight
    print("The Inner Diameter of Nyota's Femur is:", '\t', '\t', round(canal_diameter,1), "mm",)            
    #print the canal diameter of Nyota's femur
    print("The Ultimate Tensile Strength of Carbon Fibre is:", '\t', round(ult_ten_strength,1), "MPa")      
    #print the ultimate tensile strength of PEEK Carbon Fiber
    while app_tens_stress < ult_ten_strength:                                                               
      #loop to calculate the minimum stem diameter of the implace, determined by when the ATS is just less than UTS
        min_stem_dia -= 1/100000                                                                            
        #subtracting a small amount from Nyota's canal diameter until diameter of implant value just equals UTS when plugged into ATS equation
        app_tens_stress = (((-13*(body_weight))/(math.pi*(min_stem_dia**2))) + ((104*(body_weight)*femoral_head_offset)/(math.pi*(min_stem_dia**3)))) 
        #equation to calculate ABS
        new_list.append(app_tens_stress)                                                                    
        #add calculated to ATS values to new_list 
    print("The minimum stem diameter of the implant is:", '\t','\t', round(min_stem_dia,1) , "mm")          
    #print the minimum stem diameter of the implant rounded to one decimal place
    app_tens_stress = new_list[-2]                                                                          
    #equate the 2nd last item in new_list to ABS because last item in list exceeds UTS and instructions say it must be less than or equal to UTS
    print("Applied Tensile Strengh is:", '\t','\t','\t','\t',(round(app_tens_stress,1)), "MPa")             
    #print the ABS strength that the minimum diameter occurs at rounded to one decimal place

#Troy 
def func2(file_name, body_weight, team_number, stem_dia):

    stress_amplitude = []
    cycles_to_failure = []
    stress_conc_factor_list = []
    sigma_adj_list = []
    stress_fail = 0
    cycles_fail = 0
    
    file = open(file_name, 'r')
    data = file.read()
    file.close()
    values = data.split()
    
    increment = 0
    for i in values:
        if increment%2 == 0:
            stress_amplitude.append(float(i))
        else:
            cycles_to_failure.append(float(i))
        increment += 1
        
    Fpos = 12 * body_weight
    Fneg = -12 * body_weight
    A = (stem_dia / 2)**2 * math.pi
    sigma_max = Fpos / A
    sigma_min = Fneg / A
    sigma_amp = (sigma_max - sigma_min) / 2

    for N in cycles_to_failure:
        stress_conc_factor = 8.5 + math.log(N,10)**(0.7*team_number/40)
        stress_conc_factor_list.append(stress_conc_factor)
        
    for x in stress_conc_factor_list:
        sigma_adj = x * sigma_amp
        sigma_adj_list.append(sigma_adj)
        
    increment2 = 0
    sigma_adj_list_len = len(sigma_adj_list) - 1
    for y in sigma_adj_list:
        if sigma_adj_list.index(y) == sigma_adj_list_len:
            print("The implant will not fail under the maximum cyclical load")
            break
        elif y < (stress_amplitude[increment2]):
            increment2 += 1
        elif y > (stress_amplitude[increment2]):
            stress_fail = y
            cycles_fail = (cycles_to_failure[increment2])
            print("The implant will fail after", int(cycles_fail), "cycles.")
            print("The implant is overstressed and fails at", round(stress_fail,1), "MPa.")
            break
        
#Suraj
def func3(BW,modulus_implant,modulus_bone,outer_dia,canal_diameter):
    E_ratio=(modulus_implant/modulus_bone)**(1/2)
    stress_reduc=30*BW/((math.pi/4)*(outer_dia**2-canal_diameter**2))*(3*modulus_bone/(modulus_implant+modulus_bone))**(1/3)
    yrs_fail=0
    print("Year \t Compressive Strength")  
    while True:
        comp_strength=round(0.0015*yrs_fail**2-3.752*yrs_fail*E_ratio+168.54,1)
        print(yrs_fail, '\t',comp_strength )
        if comp_strength<stress_reduc:
            stress_fail=comp_strength
            print("The value of stress fail,", stress_fail,", occurs after", yrs_fail,"years.")
            break
        yrs_fail+=1

#Troy
def main():
    
    body_weight = 59*9.81
    team_number = 15
    outer_dia = 24
    canal_diameter = 13
    canal_offset = 29
    stem_dia = 20
    modulus_implant = 110
    modulus_bone = 17
    ult_ten_strength = 260

    print("Hello there! What would you like to know about today? \n")
    print('Input "1" if you would like to know',"Nyota's patient info, the minimum stem diameter and the applied tensile strength that corresponds to this diameter.\n") 
    print('Input "2" if you would like to know',"at what point the implant becomes overtstressed and fails and after how many cycles the implant fails.\n")
    print('Input "3" if you would like to know',"the stress-fail that corresponds to each year after implantation.\n")
    print('Input "q" if you would like to exit the program.\n')

    while True:
        user_input = input("Please make a selection: ")
        print ('\n')
        if user_input == "1":
            func1(canal_diameter, body_weight, ult_ten_strength)
            print('\n')
        elif user_input == "2":
            func2("SN Data - Sample Ceramic.txt", body_weight, team_number, stem_dia)
            print ('\n')

        elif user_input == "3":
            func3(body_weight, modulus_implant, modulus_bone, outer_dia, canal_diameter)
            print ('\n')
        
        elif user_input == "q":
            print("Thank you for your time, have a great day!")
            break
        
        else:
            print('That is not a valid input, please input either "1", "2", "3", or "q"\n')
        


main()
