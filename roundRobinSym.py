#defining processes (processName, arrivalTime, execTime, first time being executed)
#need waiting time
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

# Sort the queue based on the first value of each tuple
queue = sorted(queue, key=lambda x: x[1])

#flag variable
completion = 0

#defines the time in wich the simulation will occur
#all the time units are seconds
time = 0
overhead = 1
quantum = 2
n = 0

while completion != 5:
    
    #gives the reponse time comparing the current Time - arrivalTime(queue[n][1]). 
    #queue[n][3]works as a flag to see if the process has entered the simulation before
    if queue[n][3] == 0: 
        queue[n][3] = 1
        responseTime.append([queue[n][0], time-queue[n][1]])

    #checking if the execTime in less than the quantum (but still more than 0),
    #it than, subtracts the execTime by itself, and adds to completion
    #also the return time is calculated (Final execTime - arrivalTime)
    if  0<queue[n][2]<quantum:
        queue[n][2] -= queue[n][2]
        time += queue[n][2]
        time += overhead
        completion += 1
        returnTime.append([queue[n][0], time-queue[n][1]])

    elif queue[n][2]>= quantum:
        queue[n][2] -=quantum 
        time += quantum
        time += overhead

        #when the execTime becomes 0, the return time is calculated (Final execTime - arrivalTime)
        # it also increasses the flag variable in 1
        if queue[n][2] == 0:
            completion += 1
            returnTime.append([queue[n][0], time-queue[n][1]])

    n+=1
    if n >=5:
        n = 0


#calculates the waitingTime of each program by compairing the returnTime and the responseTime
#also calculates the avarage for each return and response times
sumResponse = 0
sumReturn = 0


for x in range(len(responseTime)):
    waitingTime.append([queue[x][0], returnTime[x][1] - responseTime[x][1]])
    sumResponse += responseTime[x][1]
    sumReturn += returnTime[x][1]

averageResponse = sumResponse/5
averageReturn = sumReturn/5


print("Resultados para o Round Robin: ")
print(f"A ordem de atendimento foi: {queue[0][0]}->{queue[1][0]}->{queue[2][0]}->{queue[3][0]}->{queue[4][0]};")
print(f"Os tempos de resposta foram: {responseTime[0]}, {responseTime[1]}, {responseTime[3]}, {responseTime[2]}, {responseTime[4]}")
print(f"Os tempos de retorno foram: {returnTime[0]}, {returnTime[1]}, {returnTime[3]}, {returnTime[2]}, {returnTime[4]}")
print(f"A média dos tempos de resposta foi: {averageResponse}")
print(f"A media dos tempo de retorno é de: {averageReturn}")