#defining processes (processName, arrivalTime, ramainingExecTime, first time being executed)

p1 = ['p1', 0, 1, 0]
p2 = ['p2', 0, 2, 0]
p3 = ['p3', 1, 1, 0]
p4 = ['p4', 0, 15, 0]
p5 = ['p5', 2, 10, 0]

waitingTime = []
responseTime = []
returnTime = []

#queue generation
queue = [p1, p2, p3, p4, p5]

#Sort the queue based on the first value of each tuple
queue = sorted(queue, key=lambda x: x[1])

#flag variable
completed = 0

#defines the time in wich the simulation will occur
#all the time units are seconds
time = 0
overhead = 1
quantum = 2
n = 0

while completed != 5:

    #check the flag value in queue[*][3], p1 to p5, if it's 0 it adds the process to the response time list
    #response time is then calculated like time subtracted by the arrival time of the proccess in the cpu 
    if queue[n][3] == 0:
        responseTime.append([queue[n][0], time - queue[n][1]])
        queue[n][3] = 1

    #if a process execTime is less than the quantum, than this is added to the chronological time and the execTime becomes 0
    #also it generates an overhead since the cpu has to switch proccesses
    if 0 < queue[n][2] < quantum:
        time += queue[n][2]
        queue[n][2] = 0
        completed += 1

        #as soon as the process finishes,  a return time is generated, by subtracting the time by the proccess arrival time
        returnTime.append([queue[n][0], time - queue[n][1]])

        time += overhead
    
    #if a procces remainingExecTime is more than the quantum, or equal to it, we will subtract the quantum from that remainingExecTime
    #and add the quantum to the time, since it's equal to the amount of time the proccess expent on the cpu
    #we will also check if the proccess has concluded
    elif queue[n][2] >= quantum:
        time += quantum
        queue[n][2] -= quantum

        if queue[n][2] == 0:
            completed += 1

            #as soon as the process finishes,  a return time is generated, by subtracting the time by the proccess arrival time
            returnTime.append([queue[n][0], time - queue[n][1]])
        
        time += overhead

    n+=1
    if n >= 5:
        n = 0


sumResponse = 0 
sumReturn = 0 
for n in range(len(responseTime)):
    waitingTime.append([queue[n][0], returnTime[n][1] - responseTime[n][1]])
    
    sumResponse+=responseTime[n][1]
    sumReturn+=returnTime[n][1]

responseAverage = sumResponse/len(responseTime)
returnAverage = sumReturn/len(returnTime)


print("p1->p2->p4->p3->p5")
print(f'''Os tempos de resposta foram: {responseTime}''')
print(f'''Os tempos de retorno foram: {returnTime}''')
print(f'''Os tempos de espera foram: {waitingTime}''')
print(f'''A média dos tempos de resposta foi: {responseAverage}''')
print(f'''A média dos tempos de retorno foi: {returnAverage}''' )
      