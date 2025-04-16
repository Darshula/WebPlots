# Examples

1. Python
    1. Plotly
        1. 2D
            ```python
            import plotly.graph_objects as go
            import numpy as np

            N = 30     # Number of boxes

            # generate an array of rainbow colors by fixing the saturation and lightness of the HSL
            # representation of colour and marching around the hue.
            # Plotly accepts any CSS color format, see e.g. http://www.w3schools.com/cssref/css_colors_legal.asp.
            c = ['hsl('+str(h)+',50%'+',50%)' for h in np.linspace(0, 360, N)]

            # Each box is represented by a dict that contains the data, the type, and the colour.
            # Use list comprehension to describe N boxes, each with a different colour and with different randomly generated data:
            fig = go.Figure(data=[go.Box(
                y=3.5 * np.sin(np.pi * i/N) + i/N + (1.5 + 0.5 * np.cos(np.pi*i/N)) * np.random.rand(10),
                marker_color=c[i]
                ) for i in range(int(N))])

            # format the layout
            fig.update_layout(
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(zeroline=False, gridcolor='white'),
                paper_bgcolor='rgb(233,233,233)',
                plot_bgcolor='rgb(233,233,233)',
            )

            fig.show()
            ```

        2. 3D
            ```python
            import plotly.graph_objects as go

            import pandas as pd

            z_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')

            fig = go.Figure(data=[go.Surface(z=z_data.values)])

            fig.update_layout(title=dict(text='Mt Bruno Elevation'), autosize=False,
                            width=500, height=500,
                            margin=dict(l=65, r=50, b=65, t=90))

            fig.show()
            ```
    2. Matplotlib
        1. 2D
            ```python
            import matplotlib.pyplot as plt
            import numpy as np

            species = ("Adelie", "Chinstrap", "Gentoo")
            penguin_means = {
                'Bill Depth': (18.35, 18.43, 14.98),
                'Bill Length': (38.79, 48.83, 47.50),
                'Flipper Length': (189.95, 195.82, 217.19),
            }

            x = np.arange(len(species))  # the label locations
            width = 0.25  # the width of the bars
            multiplier = 0

            fig, ax = plt.subplots(layout='constrained')

            for attribute, measurement in penguin_means.items():
                offset = width * multiplier
                rects = ax.bar(x + offset, measurement, width, label=attribute)
                ax.bar_label(rects, padding=3)
                multiplier += 1

            # Add some text for labels, title and custom x-axis tick labels, etc.
            ax.set_ylabel('Length (mm)')
            ax.set_title('Penguin attributes by species')
            ax.set_xticks(x + width, species)
            ax.legend(loc='upper left', ncols=3)
            ax.set_ylim(0, 250)

            plt.show()

            ```
2. R
    1. Plotly
        1. 2D
            ```R
            library(plotly)

            fig <- plot_ly(
            x = c("giraffes", "orangutans", "monkeys"),
            y = c(20, 14, 23),
            name = "SF Zoo",
            type = "bar"
            )

            fig
            ```
        2. 3D
            ```R
            # Library
            library(plotly)

            # Data: volcano is provided by plotly

            # Plot
            fig <- plot_ly(z = volcano, type = "surface")
            ```

    2. GGPlot2
        1. 2D
            ```R
            library(ggplot2)
            library(plotly)
            library(gapminder)

            p <- gapminder %>%
            filter(year==1977) %>%
            ggplot( aes(gdpPercap, lifeExp, size = pop, color=continent)) +
            geom_point() +
            theme_bw()

            fig <- ggplotly(p)
            ```
        2. 3D
            ```R
            install.packages("devtools")  # so we can install from github
            library("devtools")
            install_github("ropensci/plotly")  # plotly is part of ropensci
            library(plotly)

            py <- plotly(username="r_user_guide", key="mw5isa4yqp")  # open plotly connection

            pp <- function (n,r=4) {
                x <- seq(-r*pi, r*pi, len=n)
                df <- expand.grid(x=x, y=x)
                df$r <- sqrt(df$x^2 + df$y^2)
                df$z <- cos(df$r^2)*exp(-df$r/6)
                df
            }
            p <- ggplot(pp(20), aes(x=x,y=y))

            p <- p + geom_tile(aes(fill=z))

            py$ggplotly(p)
            ```
