# All decimal 3 places

# Function to compute mean
def mean(first_list):
    # mean Logic 

    for i in range(len(first_list)):
        if isinstance(first_list[i], str):
            mean_value = 0
            break
    else:
        mean_value = 0
        sum = summation(first_list)
        mean_value = sum / len(first_list)
    return mean_value



# Function to compute sum. You cant use Python functions
def summation(first_list):
    # sum Logic
    for x in first_list:
        a=isinstance(x,int) or isinstance(x,float)
        summation_value=0
        if a:
            summation_value+=x
        else:
            return 0
    return summation_value
