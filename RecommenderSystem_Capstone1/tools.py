import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

#### METHODS ####

def create_hists(df, cols, xlog=False, ylog=False):

    """
    ----------------------------------------------------------
    Description:
        Wrapper function for automating histogram plotting for 
    columns of a dataframe.
    
    Inputs:
        df - Dataframe containing data to plot.
        cols - List of columns to plot.
        xlog, ylog - Boolean denoting a logarithmic scale.
    Outputs:
        Plotly histogram for every column specified.
    ----------------------------------------------------------
    """
    
    for i in range(len(cols)):
        
        trace = go.Histogram(
                    name = cols[i],
                    x=df[cols[i]])
        
        if xlog:
            xlog='log'
        else:
            xlog='linear'
        if ylog:
            ylog='log'
        else:
            ylog='linear'
        
        layout = go.Layout(
                    title='%s Histogram' % cols[i],
                    titlefont = dict(size=20),
                    xaxis=dict(
                        type=xlog,
                        autorange=True,
                        title='%s' % cols[i],
                        titlefont=dict(
                            size=18
                        )
                    ),
                    yaxis=dict(
                        type=ylog,
                        autorange=True,
                        title='Count',
                        titlefont=dict(
                            size=18
                        )
                    )
                )
        
        fig = go.Figure(data=[trace], layout=layout)

        iplot(fig, filename='%s Histogram' % cols[i])



def highlight(s, threshold=0.9):

    """
    ----------------------------------------------------------
    Description:
        Function to pass to pandas dataframe or series style 
    method. Highlights cell if value is greater than threshold
    but not equal to 1.
    
    Inputs:
        s - Pandas series containing data to highlight.
        threshold - Float value specifying highlight treshold.
    Outputs:
        List of styling arguments for each cell in the series.
    ----------------------------------------------------------
    """

    is_90 = (abs(s) > threshold) & (s != 1) 

    return ['background-color: red' if v else '' for v in is_90]