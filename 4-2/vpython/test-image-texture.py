from vpython import *

scene.range = 1
scene.forward = vector(-1,-.5,-1)
box(texture="https://s3.amazonaws.com/glowscript/textures/flower_texture.jpg")
#box(texture="https://commons.wikimedia.org/wiki/Main_Page#/media/File:Lycidae-Kadavoor-2017-05-22-001.jpg")
scene.caption = "Control-drag to rotate"