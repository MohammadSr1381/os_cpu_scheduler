
num_Processes = 7
time_in = [0,0,12,27,7,54,12]
time_duration = [3,10,7,21,3,5,13]
quantum = 2



#to create the dictionary of processes for RR
def create_dic_RR(process , enter , duration):
    
    dic_processes = {}
    for i in range(process):
        completion_time = 0
        remaining_duration = duration
        dic_processes[f'P{i+1}'] = [enter[i] , duration[i] , completion_time , 0 , remaining_duration[i]]
    return dic_processes



#input to functions
process_info_RR = create_dic_RR(num_Processes , time_in , time_duration)



#RR
def round_robin(processes , quantum):
    
    average_waiting = 0 
    average_turn_around = 0
    clock = 0
    
    
    print("Process\t\tenter\t\tburst time\twaiting time\tturn around time")
    
    
    sorted_by_time_in = {key:value for key , value in sorted(processes.items() , key = lambda v : v[1][0])}
    
    
    #if u want to see the starting step
    """
    for k ,v in sorted_by_time_in.items():
        print(str(k) + "\t\t" + str(v[0]) + "\t\t" + str(v[1]) + "\t\t" + "not yet" + "\t\t" + "not yet")
    """
      
      
    #for quantum reduction and calculating waiting time and turn around    
    while any(value[1] > 0 for value in sorted_by_time_in.values()):
        
        
        
        for k,v in sorted_by_time_in.items() : 
            
            
            if v[0] > clock :
                continue
            
             
            if v[1] > 0 :
                v[1] = v[1] - quantum
                clock += quantum
                
         
            if v[1] <= 0 :
                clock += v[1]
                v[1] = 0
                v[2] = v[2] + clock
            
                
            if sorted_by_time_in[k][1] != 0 :
                print(str(k) + "\t\t" + str(v[0]) + "\t\t" + str(v[1]) + "\t\t" + "not yet" + "\t\t" + "not yet")
            
             
            else :
                if sorted_by_time_in[k][3] == 0 :
                    
                    print(str(k) + "\t\t" + str(v[0]) + "\t\t" + str(v[1]) + "\t\t" + str(v[2] - v[4]) + "\t\t" + str(v[2]))
                    sorted_by_time_in[k][3] = 1
                    average_turn_around += v[2] - v[0]
                    average_waiting += v[2] - v[0] - v[4]
    
    print(f"\n\nThe average waiting time is {average_waiting/num_Processes} and the average turn around time is {average_turn_around/num_Processes}")    

            
            
                
        
        
round_robin(process_info_RR , quantum)


