def graph1():
    packing = []
    collisions = []
    with open("sim1.txt", "r") as f:
        for line in f:
            line = line.strip()
            pack, collide = line.split(',')
            packing.append(float(pack))  # assuming pack is a float
            collisions.append(float(collide))  # assuming collis is a float

    from bokeh.plotting import figure, show
    import numpy as np
    from scipy.stats import linregress

    p = figure(width=400, height=400,x_axis_label = 'Packing',y_axis_label = 'Collisions',title = 'Packing vs Collisions(circle)')

    # add a circle renderer with a size, color, and alpha for every pack-collis pair
    p.circle(collisions, packing, size=5, color="navy", alpha=0.5)
    slope, intercept, rvalue, pvalue, stderr = linregress(collisions, packing)
    x_fit = np.linspace(min(collisions), max(collisions), 2)
    y_fit = slope * x_fit + intercept
    #p.line(x_fit, y_fit, line_color="red")

    # show the results
    show(p)

def graph2():
    packing = []
    collisions = []
    with open("sim2.txt", "r") as f:
        for line in f:
            line = line.strip()
            pack, collide = line.split(',')
            packing.append(float(pack))  # assuming pack is a float
            collisions.append(float(collide))  # assuming collis is a float

    from bokeh.plotting import figure, show
    import numpy as np
    from scipy.stats import linregress

    p = figure(width=400, height=400,x_axis_label = 'Packing',y_axis_label = 'Collisions',title = 'Packing vs Collisions(Square)')

    # add a circle renderer with a size, color, and alpha for every pack-collis pair
    p.circle(collisions, packing, size=5, color="navy", alpha=0.5)
    slope, intercept, rvalue, pvalue, stderr = linregress(collisions, packing)
    x_fit = np.linspace(min(collisions), max(collisions), 2)
    y_fit = slope * x_fit + intercept
    #p.line(x_fit, y_fit, line_color="red")

    # show the results
    show(p)