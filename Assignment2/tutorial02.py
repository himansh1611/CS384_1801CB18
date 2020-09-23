# All decimal 3 places

# Function to compute Pearson correlation coefficient. You cant use Python functions
def pcc(first_list, second_list):
    # nse Logic
    mean_x = mean(first_list)
    mean_y = mean(second_list)
    xy, x, y = [], [], []
    if len(first_list) == len(second_list):
        for i in range(len(first_list)):
            if isinstance(first_list[i], (int, float)) and isinstance(second_list[i], (int, float)):
                xy.append((first_list[i] - mean_x) * (second_list[i] - mean_y))
                x.append((first_list[i] - mean_x) ** 2)
                y.append((second_list[i] - mean_y) ** 2)
            else:
                return 0

    else:
        return 0
    xy_sum, x_sum, y_sum = summation(xy), summation(x), summation(y)
    pcc_value = 0
    if x_sum == 0 or y_sum == 0:
        return 0
    else:
        pcc_value = xy_sum / (sqrt(x_sum * y_sum))
    return pcc_value

# Function to compute NSE. You cant use Python functions
def nse(first_list, second_list):
    # nse Logic
    for i in range(len(first_list)):
        if isinstance(first_list[i], str):
            return 0
    for i in range(len(second_list)):
        if isinstance(second_list[i], str):
            return 0
    if len(first_list) != len(second_list):
        return 0
    else:
        x = []
        y = []
        mean_x = mean(first_list)
        for i in range(len(first_list)):
            x.append((first_list[i] - second_list[i]) ** 2)
            y.append((first_list[i] - mean_x) ** 2)
        nse_value = (1 - (summation(x) / summation(y)))
    return nse_value

# Function to compute RMSE. You cant use Python functions
def rmse(first_list, second_list):
    # RMSE Logic
    rmse_value = sqrt(mse(first_list, second_list))
    return rmse_value

# Function to compute mse. You cant use Python functions
def mse(first_list, second_list):
    # mse Logic
    for i in range(len(first_list)):
        if isinstance(first_list[i], str):
            return 0
    for i in range(len(second_list)):
        if isinstance(second_list[i], str):
            return 0
    if len(first_list) != len(second_list):
        return 0
    else:
        x = []
        for i in range(len(first_list)):
            x.append((first_list[i] - second_list[i]) ** 2)
        mse_value = (summation(x) / len(first_list))
    return mse_value

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
