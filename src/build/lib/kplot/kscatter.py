#%%
"""kplot.scatter3

* The 2D histogram/graph with histograms of each axis component using Matplotlib.
It's beta version. We will add the ability to manage common parameters.

"""
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from . import pltstyle

class scatter3:
    """kplot.scatter3 class
    
    Create a one or two dimension graph/histogram.
    
    """
    Fig = None
    Ax  = []
    HistXRange=None
    HistYRange=None
    PadMin = 0.1
    PadMax = 0.2
    wSpace = (0.12, 0.14)
    
    Mode = 'hist'
    valX = None
    valY = None

    def __init__(self, xBin=None, xMin=None, xMax=None, yBin=None, yMin=None, yMax=None, ratio=0.6, figsize=(8.27, 8.27)) -> None:
        """default constructor
        
        default constructor
        
        Args:
            xBim (int): Bin for x-axis.
            xMin (float): Minimum of graph/histogram for x-axis.
            xMaz (float): Maximum of graph/histogram for x-axis.
            yBim (int): Bin for y-axis.
            yMin (float): Minimum of graph/histogram for y-axis.
            yMaz (float): Maximum of graph/histogram for y-axis.
            ratio (float): division ratio for graph and histograms in canvas.
            figsize (float): canvas size in inch.
        """
        plt.rcParams["font.size"] = 9
        self.SetRatio(ratio, figsize)

        if self.HistXRange is not None: self.HistXRange = None
        if self.HistYRange is not None: self.HistYRange = None

        if xBin is not None:
            self.HistXRange=(xBin, xMin, xMax)
        if yBin is not None:
            self.HistYRange=(yBin, yMin, yMax)

    def SetRatio(self, ratio=0.6, figsize=(8.27, 8.27)):
        """SetRatio
        
        Set a canvas size and a division ratio and for graph and histograms in canvas.

        Args:
            ratio (float): division ratio for graph and histograms in canvas.
            figsize (float): canvas size in inch.
        
        Returns:
            self.Ax: axis object of matplotlib
        """
        if self.Fig is not None: self.Fig = None
        self.Fig = plt.figure(figsize=figsize)

        if len(self.Ax)>0: self.Ax.clear()

        Min = self.PadMin
        Max = self.PadMax
        wSpace= self.wSpace

        wScatter   = (Min, Min, ratio, ratio)
        wHistUpper = (Min, ratio+wSpace[0], ratio, Max)
        wHistSide  = (ratio+wSpace[1], Min, Max, ratio)

        self.Ax.append(plt.axes(wScatter))
        self.Ax.append(plt.axes(wHistUpper))
        self.Ax.append(plt.axes(wHistSide))

        self.Ax[1].set_xticklabels([])
        self.Ax[2].set_yticklabels([])

        return self.Ax
    def GetFig(self):
        """GetFig

        Get the figure object.
        
        Returns:
            self.Fig: figure object of matplotlib
        """
        return self.Fig

    def GetAxis(self):
        """GetAxis

        Get the axis object.
        
        Returns:
            self.Ax: axis object of matplotlib
        """
        return self.Ax

    def SetxLimit(self, x_min: float=None, x_max: float=None, x_range: tuple = None):
        """SetxLabel

        Set the x-axis limit for histograms and graphs. There are two methods to set limits.
        The primary method uses parameters `x_mix` and `x_max` . The secondary method sets the range of the x-axis limit using a tuple `x_range`.

        Args:
            x_min (float): lower limit.
            x_max (float): upper limit.
            x_range (tuple): limit range `(x_min, x_max)`
        
        Note:
            If all parameters is set, use the value of `x_range`.
    
        """
        Val = None
        if x_min is not None and x_max is not None:
            Val = (x_min, x_max)
        if x_range is not None:
            Val = x_range

        self.Ax[0].set_xlim(Val[0], Val[1])
        self.Ax[1].set_xlim(Val[0], Val[1])

    def SetyLimit(self, y_min: float=None, y_max: float=None, y_range: tuple = None):
        Val = None
        if y_min is not None and y_max is not None:
            Val = (y_min, y_max)
        if y_range is not None:
            Val = y_range

        self.Ax[0].set_ylim(Val[0], Val[1])
        self.Ax[2].set_ylim(Val[0], Val[1])

    def SetxLabel(self, title):
        """SetxLabel

        Set the x-axis label for main histograms/graph pad.

        Args:
            title (str): label title.
        """
        self.Ax[0].set_xlabel(title, loc='right')

    def SetyLabel(self, title):
        """SetyLabel

        Set the y-axis label for main histograms/graph pad.

        Args:
            title (str): label title.
        """
        self.Ax[0].set_ylabel(title, loc='top')
        pass

    def SetHistLabel(self, title='Events', axis='all'):
        """SetHistLabel

        Set the labels for x-/y- axis histograms.

        Args:
            title (str): label title.
            axis (str): Tag for the histogram index. default: 'all', set y-axis labels for all axis histograms with a common title. you can use 'upper' or 'lower' paras.
        """
        if axis == 'all' or axis == 'upper':
            self.Ax[1].set_ylabel(title, loc='top')
        if axis == 'all' or axis == 'side':
            self.Ax[2].set_xlabel(title, loc='right')

    def Draw(self, x, y, mode=None, marker_labels: list=None, norm=None):
        """Draw

        Draw the graphs.

        Args:
            x (array): value of data for x-axis hist/graph.
            y (array): value of data for y-axis hist/graph.
            mode (str): plot mode. you can used 'scatter' or 'hist'
            marker_labels (str list): Marker labels. Only valid in scatter mode.
            norm (str or obj): enable log scaling for z-axis. Only valid in hist mode.
        """
        if mode is not None: self.Mode = mode
        Znorm = norm
        
        self.valX = x
        self.valY = y
        # print(x)
        # print(self.valX)
        # print(y)
        # print(self.valY)
        
        if self.Mode == 'scatter':
            self.Ax[0].scatter(x, y, color='black', marker='o')
            if marker_labels is not None:
                for i, txt in enumerate(marker_labels):
                    Text = self.Ax[0].annotate(txt, (x[i], y[i]), fontsize=plt.rcParams["font.size"]*0.8, textcoords='offset points', xytext=(-4, 5))
        elif self.Mode == 'hist':
                # ZScale = None
                # if z_scale: ZScale = colors.LogNorm()
                if norm == 'log' or norm == True:
                    Znorm = colors.LogNorm()
                    # print('log scale')

                self.Ax[0].hist2d(x, y, bins=(self.HistXRange[0], self.HistYRange[0]), range=(self.HistXRange[1:], self.HistYRange[1:]), norm=Znorm)

        self.Ax[1].hist(x, bins=self.HistXRange[0], range=self.HistXRange[1:], color='black', histtype='step')
        self.Ax[2].hist(y, bins=self.HistYRange[0], range=self.HistYRange[1:], color='black', histtype='step', orientation='horizontal')

        self.SetHistLabel()
        self.Fig.align_labels(axs=self.Ax)

        return self.Ax
    
    def SetLogz(self, flag=True):
        """SetLogz

        Set or unset the log scale for z-axis.

        Args:
            flag (bool): Enable log scaling.
        """
        Znorm = None
        if self.Mode == 'hist':
            if flag: Znorm = colors.LogNorm()
            self.Ax[0].cla()
            self.Draw(self.valX, self.valY, norm=Znorm)

    def Print(self, path='./scatter.pdf', dpi=350, pad_inches=0.5):
        """Print

        Save the graph.

        Args:
            path (str): path to file.
            dpi (int): DPI.
            pad_inches (float): pad inches.
        """
        plt.savefig(path, dpi=dpi, bbox_inches='tight', pad_inches=pad_inches)

    def Clear():
        """Clear

        Clear the pad.
        """
        plt.cla()
        plt.clf()