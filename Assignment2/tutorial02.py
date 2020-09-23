# All decimal 3 places

def sorting(first_list):
    # Sorting Logic
    for i in range(len(first_list)):
        if isinstance(first_list[i], str):
            return 0
    else:
        sorted_list=[]
        for passnum in range(len(first_list) - 1, 0, -1):
            for i in range(passnum):
                if first_list[i] > first_list[i + 1]:
                    temp = first_list[i]
                    first_list[i] = first_list[i + 1]
                    first_list[i + 1] = temp
        sorted_list=first_list
        return sorted_list

# Function to compute Kurtosis. You cant use Python functions
def kurtosis(first_list):
    # Kurtosis Logic
    for i in range(len(first_list)):
        if isinstance(first_list[i], str):
            return 0
    else:

        sigma = standard_deviation(first_list)

        mean = mean(first_list)
        kurtosis_sum = 0
        for x in first_list:
            kurtosis_sum += ((x - mean) / sigma) ** 4

        kurtosis_value = kurtosis_sum / len(first_list)

        return kurtosis_value

# Function to compute Skewness. You cant use Python functions
def skewness(first_list):
    # Skewness Logic
    for i in range(len(first_list)):
        if isinstance(first_list[i], str):
            return 0
    else:
        sigma = standard_deviation(first_list)
        mean = mean(first_list)
        skew_sum = 0
        for x in first_list:
            skew_sum += ((x - mean) / sigma) ** 3
        skewness_value = skew_sum / len(first_list)

        return skewness_value

# Function to compute Standard deviation. You cant use Python functions
def standard_deviation(first_list):
    # Standard deviation Logic

    for i in range(len(first_list)):
        if isinstance(first_list[i], str):
            return 0
    else:
        mean_for_stdv = mean(first_list)
        stdv_sum = 0
        for x in first_list:
            stdv_sum += (x - mean_for_stdv) ** 2

        stdv = stdv_sum / len(first_list)

        standard_deviation_value = sqrt(stdv)
        return standard_deviation_value

# Function to compute variance. You cant use Python functions
def variance(first_list):
    # variance Logic

    for i in range(len(first_list)):
        if isinstance(first_list[i], str):
            return 0
    else:
        mean_for_var = mean(first_list)
        var_sum = 0
        for x in first_list:
            var_sum += (x - mean_for_var) ** 2
        variance_value = var_sum / len(first_list)
        return variance_value

def median(first_list):
    # median Logic

    for i in range(n):
        if isinstance(sorted_list[i], str):
            return 0
    else:
        sorted_list = sorting(first_list)
        n = len(sorted_list)
        if len(sorted_list) % 2 == 1:
            median_value = sorted_list[len(sorted_list) // 2]
        else:
            median_value = (sorted_list[len(sorted_list) // 2] + sorted_list[len(sorted_list) // 2 - 1]) / 2
        return median_value

def mae(first_list, second_list):
    # mae Logic
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
            x.append(abs(first_list[i] - second_list[i]))
        mae_value = (summation(x) / len(first_list))
    return mae_value

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
