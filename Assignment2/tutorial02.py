# All decimal 3 places





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
