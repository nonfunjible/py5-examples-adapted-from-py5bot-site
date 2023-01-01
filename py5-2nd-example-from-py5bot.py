"""
Adapted from 2nd example at
https://py5coding.org/tutorials/introduction_to_py5bot.html
to produce a random iteration of this:
https://py5coding.org/_images/introduction_to_py5bot_5_0.png 

Code modified to Module Mode.
"""

import py5

def setup():
    py5.size(200, 200)
    py5.background(224)
    py5.no_stroke()
    for _ in range(250):
        py5.fill(py5.random_int(255), py5.random_int(255), py5.random_int(255))
        py5.rect(py5.random_int(py5.width), py5.random_int(py5.height), 10, 10)

py5.run_sketch()
