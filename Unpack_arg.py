def health_calculator(age, chicks_ate, cigs_smoked) :

    answer = (100 - age) + (chicks_ate * 3) - (cigs_smoked *2)

    print(answer)

Jisans_data = [22, 500, 125]

health_calculator(Jisans_data[0], Jisans_data[1], Jisans_data[2])

print('')

health_calculator(*Jisans_data)