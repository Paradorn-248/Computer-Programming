estimate_time = int(input('Estimated time : '))

rec_phys = rec_weight = rec_fitness = 2.5 * estimate_time

sum_phys = sum_weight = sum_fitness = 0
#print(rec_phys,rec_weight,rec_fitness)
for i in range(estimate_time // 8) :
    print(f'Week{i+1}')
    phys = int(input('Physical therapy : '))
    weight = int(input('Weight training : '))
    fitness = int(input('Fitness training : '))

    sum_phys += phys
    sum_weight += weight
    sum_fitness += fitness
    if sum_phys >= rec_phys and sum_weight >= rec_weight and sum_fitness >= rec_fitness :
        print('Buzzy has recovered in time.')
        exit()

#print(sum_phys,sum_weight,sum_fitness)
if sum_phys < rec_phys or sum_weight < rec_weight or sum_fitness < rec_fitness :
    print('Buzzy has not recovered in time.')