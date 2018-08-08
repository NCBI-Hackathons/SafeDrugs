import plotly.graph_objs as go


# TODO Figure out how to display a title for this thing
def bar_plot(title, x_legend, y_legend, trace1, trace2, t1name, t2name):
    """
    inputs:
        title: duh, title
        x_legend: string to be displayed as the x-axis legend
        y_legend: ditto
        trace1: hash of format {series: array, x: array, y: array, y_norm: array, name: string}
        trace2 (optional): second series for overlapping plot
    returns: Plotly Bar Plot
    """
    
    bar1 = go.Bar(
        x=trace1['x'],
        y=trace1['y_norm'],
        name=t1name,
        text=['{} reports'.format(i) for i in trace1['y']],
        marker=go.Marker(
            color='rgb(55, 83, 109)'
        )
    )
    data = [bar1]
    
    if trace2:
        bar2 = go.Bar(
            x=trace2['x'],
            y=trace2['y_norm'],
            name=t2name,
            text=['{} reports'.format(i) for i in trace2['y']],
            marker=go.Marker(
                color='rgb(180,180,180)'
            )
        )
        data.append(bar2)
    
    return {
        'data' : data,
        'layout' : go.Layout(
            title=title,
            showlegend=True,
            yaxis = dict(
                title=y_legend,
                type='-'
            ),
            xaxis = dict(
                title=x_legend
            ),
            legend=go.layout.Legend(
                x=0,
                y=1.0
            ),
            margin=go.layout.Margin(l=40, r=20, t=40, b=100)
        )
    }
