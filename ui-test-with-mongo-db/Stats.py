import numpy as numpy

def get_stats(weight_array):
    output = ""
    output += "======================================\n"
    output += "Maximaler Wert: " + numpy.max(weight_array).__str__() + " \n"
    output += "Minimaler Wert: " + numpy.min(weight_array).__str__() + " \n"
    output += "\n"
    output += "Median: " + numpy.median(weight_array).__str__() + "\n"
    output += "Arithmetisches Mittel: " + numpy.mean(weight_array).__str__() + "\n"
    output += "Varianz: " + numpy.var(weight_array).__str__() + "\n"
    output += "======================================\n"
    return output
