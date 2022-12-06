# Import here
from support import txt_to_string
# Write Code here
def output():
    data_stream = txt_to_string()
    result = Tuning_Trouble(data_stream)
    print(result)

#function here
def Tuning_Trouble(data_stream):
    start_of_packet = []
    marker_char = 0
    marker = False
    for j,section  in enumerate(data_stream):
        start_of_packet = data_stream[j:14+j]
        print(start_of_packet)
        packet = {}
        
        for i in start_of_packet:
            if packet.get(i) == None:
                packet[i] = 1
            else:
                packet[i] += 1
            if packet[i] >= 2:
                marker = False
                break
            else:
                marker = True
        if marker:
            break

        marker_char += 1


    return marker_char + 14


# output function
output()