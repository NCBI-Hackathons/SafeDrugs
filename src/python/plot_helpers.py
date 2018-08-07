def pyplot(x, y, title = "plot", x_title = None, y_title = None, chart_type = "bar", tickangle = -45, plot_out = False):
    """
    plotly plot based on the labels in x and data in y.
    arguments:
        x - labels of the data
        y - values
        title - figure title
        x_title - title of x axis
        y_title - title of y axis
        chart_type - type of the chart
        tickangle - angle of x tick labels
        plot_out - bool type decides if the function plot out the figure
    
    return:
        the handler of the plotly figure
    """
    trace = {
        "x": x,
        "y": y, 
        "type": chart_type
    }
    
    data = [trace]
    
        
    layout = go.Layout(
            title = title,
            xaxis=dict(title = x_title,
                       tickangle=tickangle),
            yaxis=dict(title = y_title)
            )
    
    fig = go.Figure(data=data, layout=layout)
    
    if plot_out:
        py.iplot(fig, filename="bar_fig", show_link = False)
    
    return fig
