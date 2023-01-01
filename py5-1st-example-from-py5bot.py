"""
Adapted from 1st example at
https://py5coding.org/tutorials/introduction_to_py5bot.html
to produce this:
https://py5coding.org/_images/introduction_to_py5bot_1_0.png

Code modified to Module Mode.
"""

import py5

def setup():
    py5.size(200, 200)
    py5.background(255, 255, 0)
    py5.rect(50, 50, 100, 100)

py5.run_sketch()
