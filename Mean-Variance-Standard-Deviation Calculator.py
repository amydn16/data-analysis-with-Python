import numpy as np

# Define calculate function to take list of no fewer than 9 elements
def calculate(a_list):
    
    if len(a_list) < 9: # Raise ValueError 
        raise ValueError("List must contain nine numbers.")
    
    elif len(a_list) == 9:
        
        # Convert list into 3x3 Numpy array
        # Use nparray.tolist() to convert Numpy array to list
        array = np.reshape(a_list, (3,3))

        # Form dictionary to hold lists of mean, var, std, max, min, sum
        the_dict = {}
        for item in ['mean', 'variance', 'standard deviation', 'max', 'min', 'sum']:
            the_dict[item] = []

        # Compute values over axis = 0, axis = 1, axis = None (flattened)
        for item in [0, 1, None]:
            the_axis = item # Set axis

            # Calculate the mean along an axis
            the_mean = np.mean(array, axis = the_axis)
            mean_list = the_mean.tolist() 
            the_dict['mean'] = the_dict['mean'] + [mean_list]

            # Calculate the variance along an axis
            the_var = np.var(array, axis = the_axis)
            var_list = the_var.tolist()
            the_dict['variance'] = the_dict['variance'] + [var_list]

            # Calculate the standard deviation along an axis
            the_std = np.std(array, axis = the_axis)
            std_list = the_std.tolist()
            the_dict['standard deviation'] = the_dict['standard deviation'] + [std_list]
            
            # Calculate the maximum value along an axis
            the_max = np.max(array, axis = the_axis)
            max_list = the_max.tolist()
            the_dict['max'] = the_dict['max'] + [max_list]

            # Calculate the minimum value along an axis
            the_min = np.min(array, axis = the_axis)
            min_list = the_min.tolist()
            the_dict['min'] = the_dict['min'] + [min_list]

            # Calculate the sum of all values along an axis
            the_sum = np.sum(array, axis = the_axis)
            sum_list = the_sum.tolist()
            the_dict['sum'] = the_dict['sum'] + [sum_list]

        return(the_dict)
