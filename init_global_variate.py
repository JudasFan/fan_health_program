import fan_element_struct as fes
import copy

def init_global_variate():
    fan_tuple=copy.deepcopy(fes.fan_element_struct())
    fan_dict=copy.deepcopy(fan_tuple[0])
    return fan_dict,fan_tuple

