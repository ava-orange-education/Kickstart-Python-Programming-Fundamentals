# Module for logarithmic calculations 
import math 
def natural_log(x): 
    if x > 0: 
        return math.log(x) 
    else: 
        return "Error: Logarithm not defined for non-positive values" 
def log_base_ten(x): 
    if x > 0: 
        return math.log10(x) 
    else: 
        return "Error: Logarithm not defined for non-positive values"