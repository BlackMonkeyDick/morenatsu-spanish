#####Rain

###Rain Sprites
image rain_0 = "images/image/rain_0_0.png"
image rain_1 = "images/image/rain_0_1.png"
image rain_2 = "images/image/rain_0_2.png"
image rain_3 = "images/image/rain_0_3.png"


image rain_1a:    
    persistent.rain1a
    alpha 1.0
    linear .275 yoffset 700
    alpha 0
    linear 0.1 yoffset - 700
    pause .1
    repeat  
image rain_1b:
    persistent.rain1b
    alpha 1.0
    linear .215 yoffset 700
    alpha 0
    linear 0.1 yoffset - 700
    pause .1
    repeat
image rain_1c:
    persistent.rain1c
    alpha 1.0
    linear .3 yoffset 700
    alpha 0
    linear 0.1 yoffset - 700
    pause .1
    repeat
image rain_1d:
    persistent.rain1d
    alpha 1.0
    linear .325 yoffset 700
    alpha 0
    linear 0.1 yoffset - 700
    pause .1
    repeat
image rain_1e:
    persistent.rain1e
    alpha 1.0
    linear .34 yoffset 700
    alpha 0
    linear 0.1 yoffset - 700
    pause .1
    repeat
image rain_1f:
    persistent.rain1f
    alpha 1.0
    linear .31 yoffset 700
    alpha 0
    linear 0.1 yoffset - 700
    pause .1
    repeat
image rain_1g:
    persistent.rain1g
    alpha 1.0
    linear .375 yoffset 700
    alpha 0
    linear 0.1 yoffset - 700
    pause .1
    repeat
image rain_1h:
    persistent.rain1h
    alpha 1.0
    linear .285 yoffset 700
    alpha 0
    linear 0.1 yoffset - 700
    pause .1
    repeat
image rain_1i:
    persistent.rain1i
    alpha 1.0
    linear .325 yoffset 700
    alpha 0
    linear 0.1 yoffset - 700
    pause .1
    repeat
image rain_1j:
    persistent.rain1j
    alpha 1.0
    linear .32 yoffset 700
    alpha 0
    linear 0.1 yoffset - 700
    pause .1
    repeat
image rain_1k:
    persistent.rain1k
    alpha 1.0
    linear .385 yoffset 700
    alpha 0
    linear 0.1 yoffset - 700
    pause .1
    repeat
image rain_1l:
    persistent.rain1l
    alpha 1.0
    linear .265 yoffset 700
    alpha 0
    linear 0.1 yoffset - 700
    pause .1
    repeat
image rain_1m:
    persistent.rain1m
    alpha 1.0
    linear .25 yoffset 700
    alpha 0
    linear 0.1 yoffset - 700
    pause .1
    repeat
image rain_1n:
    persistent.rain1n
    alpha 1.0
    linear .28 yoffset 700
    alpha 0
    linear 0.1 yoffset - 700
    pause .1
    repeat
image rain_1o:
    persistent.rain1o
    alpha 1.0
    linear .355 yoffset 700
    alpha 0
    linear 0.1 yoffset - 700
    pause .1
    repeat
image rain_1p:
    persistent.rain1p
    alpha 1.0
    linear .345 yoffset 700
    alpha 0
    linear 0.1 yoffset - 700
    pause .1
    repeat
image rain_1q:
    persistent.rain1q
    alpha 1.0
    linear .28 yoffset 700
    alpha 0
    linear 0.1 yoffset - 700
    pause .1
    repeat
image rain_1r:
    persistent.rain1r
    alpha 1.0
    linear .38 yoffset 700
    alpha 0
    linear 0.1 yoffset - 700
    pause .1
    repeat
image rain_1s:
    persistent.rain1s
    alpha 1.0
    linear .3 yoffset 700
    alpha 0
    linear 0.1 yoffset - 700
    pause .1
    repeat
image rain_1t:
    persistent.rain1t
    alpha 1.0
    linear .325 yoffset 700
    alpha 0
    linear 0.1 yoffset - 700
    pause .1
    repeat
image rain_1u:
    persistent.rain1u
    alpha 1.0
    linear .275 yoffset 700
    alpha 0
    linear 0.1 yoffset - 700
    pause .1
    repeat
    

image raining = LiveComposite(
    (800, 600),
    (0, 650), "rain_1a",
    (40, 650), "rain_1b",
    (80, 650), "rain_1c",
    (120, 650), "rain_1d",
    (160, 650), "rain_1e",
    (200, 650), "rain_1f",
    (240, 650), "rain_1g",
    (280, 650), "rain_1h",
    (320, 650), "rain_1i", 
    (360, 650), "rain_1j",
    (400, 650), "rain_1k",
    (440, 650), "rain_1l",
    (480, 650), "rain_1m",
    (520, 650), "rain_1n",
    (560, 650), "rain_1o",
    (600, 650), "rain_1p",
    (640, 650), "rain_1q",
    (680, 650), "rain_1r",
    (720, 650), "rain_1s",
    (760, 650), "rain_1t",
    (800, 650), "rain_1u")

label rain_set:
    $ persistent.rain1a = renpy.random.choice(["rain_0","rain_1","rain_2","rain_3"])
    $ persistent.rain1b = renpy.random.choice(["rain_0","rain_1","rain_2","rain_3"])
    $ persistent.rain1c = renpy.random.choice(["rain_0","rain_1","rain_2","rain_3"])
    $ persistent.rain1d = renpy.random.choice(["rain_0","rain_1","rain_2","rain_3"])
    $ persistent.rain1e = renpy.random.choice(["rain_0","rain_1","rain_2","rain_3"])
    $ persistent.rain1f = renpy.random.choice(["rain_0","rain_1","rain_2","rain_3"])
    $ persistent.rain1g = renpy.random.choice(["rain_0","rain_1","rain_2","rain_3"])
    $ persistent.rain1h = renpy.random.choice(["rain_0","rain_1","rain_2","rain_3"])
    $ persistent.rain1i = renpy.random.choice(["rain_0","rain_1","rain_2","rain_3"])
    $ persistent.rain1j = renpy.random.choice(["rain_0","rain_1","rain_2","rain_3"])
    $ persistent.rain1k = renpy.random.choice(["rain_0","rain_1","rain_2","rain_3"])
    $ persistent.rain1l = renpy.random.choice(["rain_0","rain_1","rain_2","rain_3"])
    $ persistent.rain1m = renpy.random.choice(["rain_0","rain_1","rain_2","rain_3"])
    $ persistent.rain1n = renpy.random.choice(["rain_0","rain_1","rain_2","rain_3"])
    $ persistent.rain1o = renpy.random.choice(["rain_0","rain_1","rain_2","rain_3"])
    $ persistent.rain1p = renpy.random.choice(["rain_0","rain_1","rain_2","rain_3"])
    $ persistent.rain1q = renpy.random.choice(["rain_0","rain_1","rain_2","rain_3"])
    $ persistent.rain1r = renpy.random.choice(["rain_0","rain_1","rain_2","rain_3"])
    $ persistent.rain1s = renpy.random.choice(["rain_0","rain_1","rain_2","rain_3"])
    $ persistent.rain1t = renpy.random.choice(["rain_0","rain_1","rain_2","rain_3"])
    $ persistent.rain1u = renpy.random.choice(["rain_0","rain_1","rain_2","rain_3"])
    
    return
