
num_Processes = 7
time_in = [0,0,12,27,7,54,12]
time_duration = [3,10,7,21,3,5,13]





#to create the dictionary of processes for SJF and FCFS
def create_dic(process , enter , duration):
    
    dic_processes = {}
    for i in range(process):
        dic_processes[f'P{i+1}'] = [enter[i] , duration[i]]
    return dic_processes



#input to functions
process_info = create_dic(num_Processes , time_in , time_duration)


#FCFS
def FCFS(processes):
    
    waiting_flag = 0
    average_waiting = 0 
    average_turn_around = 0
    
    #for sorting 
    print("Process\t\tenter\t\tburst time\twaiting time\tturn around time")
    waiting_time = 0
    sorted_by_time_in = {key:value for key , value in sorted(processes.items() , key = lambda v : v[1][0])}
    
    
    #for calculating waiting time and turn around time
    for k,v in sorted_by_time_in.items(): 
        
        turn_around_time = v[1]
        if k != 1: 
            waiting_time += (waiting_flag) - v[0]
            
            if waiting_time < 0 :
                waiting_time = 0
            
            print(str(k) + "\t\t" + str(v[0]) + "\t\t" + str(v[1]) + "\t\t" + str(waiting_time) + "\t\t" + str(turn_around_time + waiting_time))
            average_waiting += waiting_time
            average_turn_around += turn_around_time + waiting_time
            waiting_flag = v[0] + v[1]
        else :
            waiting_flag += v[1]
            print(str(k) + "\t\t" + str(v[0]) + "\t\t" + str(v[1]) + "\t\t" + str(waiting_time) + "\t\t" + str(turn_around_time + waiting_time))
            average_waiting += waiting_time
            average_turn_around += turn_around_time + waiting_time
            
    print(f"\n\nThe average waiting time is {average_waiting/num_Processes} and the average turn around time is {average_turn_around/num_Processes}")    
        

         
#SJF
def SJF(processes):
    
    waiting_flag = 0
    average_waiting = 0 
    average_turn_around = 0
    
    
    #for sorting 
    print("Process\t\tenter\t\tburst time\twaiting time\tturn around time")
    waiting_time = 0
    temp = {}
    sorted_by_SJF = {}
    
    min_time_in = min(processes.values() , key = lambda x : x[0] , default=0)
    processes_copy = processes.copy()
    
    for k,v in processes.items() :
        
        if v[0] == min_time_in[0] :
            temp[k] = processes[k]
            del processes_copy[k]
    
    
    while len(processes_copy) > 0 or len(temp) >0 :
        
        constant_SJF = 0
        min_burst_time = min(temp.values() , key = lambda z : z[1] , default=0)
        temp_copy = temp.copy()
        
        for key,value in temp_copy.items() :
            
            waiting_time = 0
            turn_around_time = 0
            if value[1] == min_burst_time[1] :
                sorted_by_SJF[key] = temp[key]
                constant_SJF += sorted_by_SJF[key][0] + sorted_by_SJF[key][1]
                del temp[key]
              
        processes_copy1 = processes_copy.copy()
        
        for key1,value1 in processes_copy1.items() :
            
            if value1[0] <= constant_SJF :
                temp[key1] = processes[key1] 
                del processes_copy[key1]
                
        if len(temp) == 0 :
            min_emergency = min(processes_copy1.values() , key = lambda x : x[0] , default=0)
            
            for key2,value2 in processes_copy1.items():
                
                if value2[0] == min_emergency[0] :
                    temp[key2] = processes[key2]
                    del processes_copy[key2]
                    
                    
    #for calculating the waiting time and turn around time
    for key3 , value3 in sorted_by_SJF.items():
        
        turn_around_time = value3[1] 
        if key3 != 1: 
            waiting_time += waiting_flag - value3[0]
        
            if waiting_time < 0 :
                waiting_time = 0
            
            print(str(key3) + "\t\t" + str(value3[0]) + "\t\t" + str(value3[1]) + "\t\t" + str(waiting_time) + "\t\t" + str(turn_around_time + waiting_time))
            average_waiting += waiting_time
            average_turn_around += turn_around_time + waiting_time
            waiting_flag = value3[0] + value3[1]
        else :
            waiting_flag = value3[1]
            print(str(key3) + "\t\t" + str(value3[0]) + "\t\t" + str(value3[1]) + "\t\t" + str(waiting_time) + "\t\t" + str(turn_around_time + waiting_time))
            average_waiting += waiting_time
            average_turn_around += turn_around_time + waiting_time

    print(f"\n\nThe average waiting time is {average_waiting/num_Processes} and the average turn around time is {average_turn_around/num_Processes}")    
     
            
                
        
        
        
   
        
FCFS(process_info)
print("\n\n******************************************************************\n\n")
SJF(process_info)
print("\n\n******************************************************************\n\n")

