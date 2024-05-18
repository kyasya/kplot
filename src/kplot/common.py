#%%
"""kplot.common

* The base class of all graph and histograms.

"""
import matplotlib
import matplotlib.pyplot as plt

class common:
    """kplot.common
    
    The base class of all graphs and histograms. This class manages parameters and function for graphs or histograms that involve generating the canvas.
    
    """
    
    # Paras 
    Fig = None
    Ax = None
    
    # function
    def __init__(self) -> None:
        pass