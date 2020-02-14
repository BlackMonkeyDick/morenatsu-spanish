###Shooting Stars


image shooting_star:
    "meteor"
    xpos persistent.star_xpos1 ypos persistent.star_ypos1
    linear .01 alpha 1.0        
    linear persistent.star_speed1 offset(persistent.star_xoff1, persistent.star_yoff1)
    linear .1 alpha 0.0
    linear .01 offset(0, 0)
    pause persistent.star_interval1    
    xpos persistent.star_xpos2 ypos persistent.star_ypos2
    linear .01 alpha 1.0    
    linear persistent.star_speed2 offset(persistent.star_xoff2, persistent.star_yoff2)
    linear .1 alpha 0.0
    linear .01 offset(0, 0)
    pause persistent.star_interval2 
    xpos persistent.star_xpos3 ypos persistent.star_ypos3
    linear .01 alpha 1.0    
    linear persistent.star_speed3 offset(persistent.star_xoff3, persistent.star_yoff3)
    linear .1 alpha 0.0
    linear .01 offset(0, 0)
    pause persistent.star_interval3
    xpos persistent.star_xpos4 ypos persistent.star_ypos4
    linear .01 alpha 1.0    
    linear persistent.star_speed4 offset(persistent.star_xoff4, persistent.star_yoff4)
    linear .1 alpha 0.0
    linear .01 offset(0, 0)
    pause persistent.star_interval4 
    xpos persistent.star_xpos5 ypos persistent.star_ypos2
    linear .01 alpha 1.0    
    linear persistent.star_speed5 offset(persistent.star_xoff5, persistent.star_yoff5)
    linear .1 alpha 0.0
    linear .01 offset(0, 0)
    pause persistent.star_interval5 
    repeat
    
    
label set_star_stats:
    $ persistent.star_xpos1 = renpy.random.randint(80, 520)
    $ persistent.star_ypos1 = renpy.random.randint(80, 320)
    $ persistent.star_xoff1 = renpy.random.randint(130, 200)
    $ persistent.star_yoff1 = renpy.random.randint(100, 150)
    $ persistent.star_speed1 = renpy.random.randint(1, 3)
    $ persistent.star_interval1 = renpy.random.randint(0, 5)
    $ persistent.star_wait1 = persistent.star_speed1 + persistent.star_interval1
    
    $ persistent.star_xpos2 = renpy.random.randint(80, 520)
    $ persistent.star_ypos2 = renpy.random.randint(80, 320)
    $ persistent.star_xoff2 = renpy.random.randint(130, 200)
    $ persistent.star_yoff2 = renpy.random.randint(100, 150)
    $ persistent.star_speed2 = renpy.random.randint(1, 3)
    $ persistent.star_interval2 = renpy.random.randint(0, 5)
    $ persistent.star_wait2 = persistent.star_speed2 + persistent.star_interval2
    
    $ persistent.star_xpos3 = renpy.random.randint(80, 520)
    $ persistent.star_ypos3 = renpy.random.randint(80, 320)
    $ persistent.star_xoff3 = renpy.random.randint(130, 200)
    $ persistent.star_yoff3 = renpy.random.randint(100, 150)
    $ persistent.star_speed3 = renpy.random.randint(1, 3)
    $ persistent.star_interval3 = renpy.random.randint(0, 5)
    $ persistent.star_wait3 = persistent.star_speed3 + persistent.star_interval3 
    
    $ persistent.star_xpos4 = renpy.random.randint(80, 520)
    $ persistent.star_ypos4 = renpy.random.randint(80, 320)
    $ persistent.star_xoff4 = renpy.random.randint(130, 200)
    $ persistent.star_yoff4 = renpy.random.randint(100, 150)
    $ persistent.star_speed4 = renpy.random.randint(1, 3)
    $ persistent.star_interval4 = renpy.random.randint(0, 5)
    $ persistent.star_wait4 = persistent.star_speed4 + persistent.star_interval4 
    
    $ persistent.star_xpos5 = renpy.random.randint(80, 520)
    $ persistent.star_ypos5 = renpy.random.randint(80, 320)
    $ persistent.star_xoff5 = renpy.random.randint(130, 200)
    $ persistent.star_yoff5 = renpy.random.randint(100, 150)
    $ persistent.star_speed5 = renpy.random.randint(1, 3)
    $ persistent.star_interval5 = renpy.random.randint(0, 5)
    $ persistent.star_wait5 = persistent.star_speed5 + persistent.star_interval5 
    
    return
    
        
        
