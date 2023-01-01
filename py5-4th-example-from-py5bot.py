"""
Adapted from 4th example at
https://py5coding.org/tutorials/introduction_to_py5bot.html
to produce a random iteration of this:
https://py5coding.org/_images/introduction_to_py5bot_9_0.png 

Code modified to Module Mode.
"""

import py5

def setup():
    py5.size(200, 200)

    def draw_random_circle():
        x = py5.random_int(py5.width)
        y = py5.random_int(py5.height)
        py5.circle(x, y, py5.random_int(25))
        
    for _ in range(20):
        draw_random_circle()

py5.run_sketch()
