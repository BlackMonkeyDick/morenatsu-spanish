### Scene and Character Transitions

##Character

#Dissolve
# Transitions and Transformations

define slowmove = MoveTransition (1.5)
define slowermove = MoveTransition(2)
define fastmove = MoveTransition(.05)

define sleepfade = Fade(2.0, 2.0, 2.0)
define creditfade = Fade(1.0,1.0,1.0)

define vsdis = Dissolve(2.5)
define sdis = Dissolve(1.5)
define dis = Dissolve(0.4)
define qdis = Dissolve(0.1)

#define slowmove = MoveTransition(4.0)
define regmove = MoveTransition(.5)
define move1 = MoveTransition(1.0)
define move2 = MoveTransition(.2)
define move3 = MoveTransition(.1)

transform move_center(speed):
    linear speed xpos 0.5 ypos 1.01 xanchor 0.5 yanchor 1.0
    
transform move_midleft(speed):    
    linear speed xpos 0.338 xanchor 0.5
    
transform move_midright(speed):
    linear speed xpos 0.663 xanchor 0.5
    
transform move_farleft(speed):
    linear speed xpos 0.19 xanchor 0.5
    
transform move_farright(speed):
    linear speed xpos 0.81 xanchor 0.5
    
transform move_offleft(speed):
    linear speed xpos 0.0 xanchor 1.0
    
transform move_offright(speed):
    linear speed xpos 1.0 xanchor 0.0
    
transform move_offleft_far(speed):
    linear speed xpos -0.5 xanchor 0.5
    
transform move_offright_far(speed):
    linear speed xpos 1.5 xanchor 0.5
    
transform move_border_right(speed):
    linear speed xpos 1.0 xanchor 0.5
    
transform move_border_left(speed):
    linear speed xpos 0.0 xanchor 0.5
    
    
transform fireworksshow(child):
    im.MatrixColor(child, im.matrix.colorize("c40000", "f9c84a"))
    
    

transform menublur(child):    
    contains:     
        child
        xanchor .5 yanchor .5
        alpha 1.00 zoom 1.00
    contains:     
        child
        xanchor .5 yanchor .5
        alpha 0.10 zoom 1.00 xoffset 1
    contains:     
        child
        xanchor .5 yanchor .5
        alpha 0.10 zoom 1.00 xoffset -1
    contains:     
        child
        xanchor .5 yanchor .5
        alpha 0.10 zoom 1.00 yoffset 1
    contains:     
        child
        xanchor .5 yanchor .5
        alpha 0.10 zoom 1.00 yoffset -1
    contains:     
        child
        xanchor .5 yanchor .5
        alpha 0.10 zoom 1.00 xoffset 2
    contains:     
        child
        xanchor .5 yanchor .5
        alpha 0.10 zoom 1.00 xoffset -2
    contains:     
        child
        xanchor .5 yanchor .5
        alpha 0.10 zoom 1.00 yoffset 2
    contains:     
        child
        xanchor .5 yanchor .5
        alpha 0.10 zoom 1.00 yoffset -2
    contains:     
        child
        xanchor .5 yanchor .5
        alpha 0.10 zoom 1.00 xoffset 3
    contains:     
        child
        xanchor .5 yanchor .5
        alpha 0.10 zoom 1.00 xoffset -3
    contains:     
        child
        xanchor .5 yanchor .5
        alpha 0.10 zoom 1.00 yoffset 3
    contains:     
        child
        xanchor .5 yanchor .5
        alpha 0.10 zoom 1.00 yoffset -3
    contains:     
        child
        xanchor .5 yanchor .5
        alpha 0.10 zoom 1.00 xoffset 4
    contains:     
        child
        xanchor .5 yanchor .5
        alpha 0.10 zoom 1.00 xoffset -4
    contains:     
        child
        xanchor .5 yanchor .5
        alpha 0.10 zoom 1.00 yoffset 4
    contains:     
        child
        xanchor .5 yanchor .5
        alpha 0.10 zoom 1.00 yoffset -4
    contains:     
        child
        xanchor .5 yanchor .5
        alpha 0.10 zoom 1.00 xoffset 5
    contains:     
        child
        xanchor .5 yanchor .5
        alpha 0.10 zoom 1.00 xoffset -5
    contains:     
        child
        xanchor .5 yanchor .5
        alpha 0.10 zoom 1.00 yoffset 5
    contains:     
        child
        xanchor .5 yanchor .5
        alpha 0.10 zoom 1.00 yoffset -5

transform hshake:
    linear .025 xoffset -15
    linear .05 xoffset 15
    linear .05 xoffset -15
    linear .05 xoffset 15
    linear .05 xoffset -15
    linear .05 xoffset 15
    linear .025 xoffset 0
    
transform vshake:
    linear .025 yoffset -15
    linear .05 yoffset 15
    linear .05 yoffset -15
    linear .05 yoffset 15
    linear .05 yoffset -15
    linear .05 yoffset 15
    linear .025 yoffset 0

transform raining1:
    xanchor .5 yanchor 1
    xpos 100 ypos 0
    linear .3 yoffset 900
    xpos 150 ypos 0
    linear .3 yoffset 900
    xpos 200 ypos 0
    linear .3 yoffset 900
    repeat
    
transform shootingstar(x_pos, y_pos, xoff, yoff, speed, wait):
    xpos x_pos ypos y_pos
    linear speed xoffset xoff yoffset yoff
    pause wait
    
transform close_right:
        zoom 1.3
        xpos .78 ypos 1.47
    

transform menu_in:
    xoffset -250
    linear .1 xoffset 0
    
transform menu_out:
    linear .1 xoffset -250
    
transform menu_select:
    yoffset -24
    linear .1 yoffset 16
    linear .1 yoffset -12
    linear .1 yoffset 8
    linear .1 yoffset -4
    linear .1 yoffset 0

transform gallery_size:
    zoom .19

transform move_win:
    linear .2 xpos 22
    
transform move_full:
    linear .2 xpos 70
    
transform fadein:
    alpha 0.0
    linear .5 alpha 1.0

transform fadein_slow:
    alpha 0.0
    linear 1.5 alpha 1.0
    
transform fading(a, t):
    linear t alpha a
    
transform fadeout:
    linear .5 alpha 0.0

transform shrink(x, y):
    linear y zoom x

transform spinning:
    linear 0.45 xzoom -1
    linear 0.45 xzoom 1
    repeat
    
transform spinning_slow:
    linear 1.5 xzoom -1
    linear 1.5 xzoom 1
    repeat

transform fall:
    linear .3 yoffset 500
    
transform briefzoom:
    linear 0.08 zoom 1.15
    linear 0.08 zoom 1.0
    
transform bobbing:
    linear .2 yoffset 10
    linear .2 yoffset 0
    repeat
    
transform bowing:
    linear .25 yoffset 30
    linear .25 yoffset 0
    
transform sway:
    linear .5 xoffset 40
    linear .5 xoffset -40
    repeat
    
transform stagger:
    linear .10 xoffset -10
    linear .10 xoffset 10
    linear .15 xoffset -20
    linear .15 xoffset 20
    linear .15 xoffset -30
    linear .15 xoffset 30
    linear .10 xoffset -30
    linear .10 xoffset 30
    linear .15 xoffset -30
    linear .15 xoffset 30
    linear .15 xoffset -20
    linear .15 xoffset 20
    linear .10 xoffset -10
    linear .10 xoffset 10
    repeat
    
transform shivering:
    linear .017 xoffset -1 yoffset 0
    linear .017 xoffset 0 yoffset 2
    linear .017 xoffset 1 yoffset 4
    linear .017 xoffset 0 yoffset 2
    linear .017 xoffset 1 yoffset 0
    linear .017 xoffset 0 yoffset 0
    linear .017 xoffset -1 yoffset 0
    linear .017 xoffset 0 yoffset 2
    linear .017 xoffset 1 yoffset 4
    linear .017 xoffset 0 yoffset 2
    linear .017 xoffset 1 yoffset 0
    linear .017 xoffset 0 yoffset 0
    linear .017 xoffset -1 yoffset 0
    linear .017 xoffset 0 yoffset 2
    linear .017 xoffset 1 yoffset 4
    linear .017 xoffset 0 yoffset 2
    linear .017 xoffset 1 yoffset 0
    linear .017 xoffset 0 yoffset 0
    linear .017 xoffset -1 yoffset 0
    linear .017 xoffset 0 yoffset 2
    linear .017 xoffset 1 yoffset 4
    linear .017 xoffset 0 yoffset 2
    linear .017 xoffset 1 yoffset 0
    linear .017 xoffset 0 yoffset 0
    linear .017 xoffset -1 yoffset 0
    linear .017 xoffset 0 yoffset 2
    linear .017 xoffset 1 yoffset 4
    linear .017 xoffset 0 yoffset 2
    linear .017 xoffset 1 yoffset 0
    linear .017 xoffset 0 yoffset 0
    linear .017 xoffset -3 yoffset 0
    linear .017 xoffset 0 yoffset 2
    linear .017 xoffset 3 yoffset 4
    linear .017 xoffset 0 yoffset 2
    linear .017 xoffset -3 yoffset 0
    linear .017 xoffset 0 yoffset 0
    repeat
  
transform tilting:
    linear .4 rotate 13
    linear .4 rotate -13
    repeat    
transform tilting_big:
    yanchor 1.0 ypos 1.5
    linear .4 rotate 13
    linear .4 rotate -13
    repeat
    
transform tilting_big_stop:
    yanchor 1.0 ypos 1.5
    linear .4 rotate 0
    
transform shake_side:
    linear .13 xoffset -50
    linear .13 xoffset 50
    repeat
    
transform shake_side_slow:
    linear .4 xoffset -50
    linear .4 xoffset 50
    repeat
   
transform still:
    linear .1 xoffset 0 yoffset 0 xzoom 1
    
transform jump_up_big:
    linear .055 ypos 1.175
    pause .01
    linear .055 ypos 1.275
    #pause .055
    #ypos 1.275
    #pause .055
    #ypos 1.275
    
transform jumping:
    linear .055 yoffset -50
    pause .01
    linear .055 yoffset 0


#transform jump_up:
    linear .05 ypos .90
    linear .05 ypos 1.0
    
transform jump_up:
    ypos .98
    pause .01
    ypos .96
    pause .01
    ypos .94
    pause .01
    ypos .92
    pause .01
    ypos .9
    pause .02
    ypos .92
    pause .01
    ypos .94
    pause .01
    ypos .96
    pause .01
    ypos .98
    pause .01
    ypos 1.01
    
transform jump_right:
    ypos .98
    xoffset 10
    pause .01
    ypos .96
    xoffset 20
    pause .01
    ypos .94
    xoffset 30
    pause .01
    ypos .92
    xoffset 40
    pause .01
    ypos .9
    xoffset 50
    pause .02
    ypos .92
    xoffset 60
    pause .01
    ypos .94
    xoffset 70
    pause .01
    ypos .96
    xoffset 80
    pause .01
    ypos .98
    xoffset 90
    pause .01
    ypos 1.01
    
transform up:
    ypos .9
transform down:
    ypos 1.0
    
transform hit_left:
    linear .05 xoffset -50
    linear .05 xoffset 0
    
transform hit_right:
    linear .05 xoffset 50
    linear .05 xoffset 0
    
transform zoom_enlarge:
    zoom 1.05
    pause .02
    zoom 1.10
    pause .02
    zoom 1.15
    pause .02
    zoom 1.20
    pause .02
    zoom 1.25
    pause .02
    
transform hop_off:
    linear .2 xoffset -150
    linear .1 yoffset 100
    linear .2 xoffset -300
    linear .1 yoffset 200
    linear .2 xoffset -450
    linear .1 yoffset 300
    linear .2 xoffset -600
    linear .1 yoffset 400
    
    
transform zoom_normal:
    zoom 1.0
    
transform zoom_80:
    zoom .7
    
transform zoom_shrink:
    zoom .95
    pause .05
    zoom .90
    pause .05
    zoom .85
    pause .05
    zoom .80
    pause .05
    zoom .75
    pause .05
    zoom .70
    pause .05
    zoom .65
    pause .05
    zoom .60
    pause .05
    zoom .55
    pause .05
    zoom .50
    pause .05
    zoom .45
    pause .05
    zoom .40
    pause .05
    zoom .35
    pause .05
    zoom .30
    pause .05
    zoom .25
    pause .05
    

transform transparent_50:
    alpha 0.95
    pause .05
    alpha 0.90
    pause .05
    alpha 0.85
    pause .05
    alpha 0.80
    pause .05
    alpha 0.75
    pause .05
    alpha 0.70
    pause .05
    alpha 0.65
    pause .05
    alpha 0.60
    pause .05
    alpha 0.55
    pause .05
    alpha 0.50
    pause .05
    
    
    
transform bump_left:
    xanchor .5 yanchor 1.0
    xpos .6
    pause 1
    xpos .5


define up_fl = Move((.2, 1.0), (.2, .9), .05, xanchor = .5, yanchor = 1.0)
define down_fl = Move((.2, .9), (.2, 1.0), .05, xanchor = .5, yanchor = 1.0)
define up_l = Move((.25, 1.0), (.25, .9), .05, xanchor = .5, yanchor = 1.0)
define down_l = Move((.25, .9), (.25, 1.0), .05, xanchor = .5, yanchor = 1.0)
define up_ml = Move((.33, 1.0), (.33, .9), .05, xanchor = .5, yanchor = 1.0)
define down_ml = Move((.33, .9), (.33, 1.0), .05, xanchor = .5, yanchor = 1.0)
define up_c = Move((.5, 1.0), (.5, .93), .05, xanchor = .5, yanchor = 1.0)
define down_c = Move((.5, .93), (.5, 1.0), .05, xanchor = .5, yanchor = 1.0)
define up_mr = Move((.66, 1.0), (.66, .9), .05, xanchor = .5, yanchor = 1.0)
define down_mr = Move((.66, .9), (.66, 1.0), .05, xanchor = .5, yanchor = 1.0)
define up_r = Move((.8, 1.0), (.8, .9), .05, xanchor = .5, yanchor = 1.0)
define down_r = Move((.8, .9), (.8, 1.0), .05, xanchor = .5, yanchor = 1.0)
define up_fr = Move((.80, 1.0), (.80, .9), .05, xanchor = .5, yanchor = 1.0)
define down_fr = Move((.80, .9), (.80, 1.0), .05, xanchor = .5, yanchor = 1.0)

define wipe_left  = ImageDissolve("images/rule/wipe_grain.png", .4)
define wipe_right = ImageDissolve(im.Flip("images/rule/wipe_grain.png", horizontal=True), .4)
define wipe_right_fast = ImageDissolve(im.Flip("images/rule/wipe_grain.png", horizontal=True), .15)
define wipe_right_slow = ImageDissolve(im.Flip("images/rule/wipe_grain.png", horizontal=True), 1)
#define wipe_down = ImageDissolve("images/rule/wipe_down.png",.5)
#define wipe_up = ImageDissolve("images/rule/wipe_up.png",.5)
#define focus_in = ImageDissolve("images/rule/focus_in.png", 1)
#define focus_in_fast = ImageDissolve("images/rule/focus_in.png", .5)
#define focus_out = ImageDissolve("images/rule/focus_out.png", 1) 
#define focus_out_fast = ImageDissolve("images/rule/focus_out.png", .5)
#define wipe_corner = ImageDissolve("images/rule/wipe_corner.png", .5)
#define wiperightfast = CropMove(0.5, "wiperight")
#define wipeleftfast = CropMove(0.5, "wipeleft")


###These will be all the rules included in the files
define blind_diag = ImageDissolve("images/rule/blind_diag.png", 1,  reverse = True)
define blind_skinny = ImageDissolve("images/rule/blind_skinny.png", 1,  reverse = True)
define blind_vert = ImageDissolve("images/rule/blind_vert.png", 1.5,  reverse = True)
define circle_in = ImageDissolve("images/rule/circle_in.png", 1, reverse = True)
define circle_out = ImageDissolve("images/rule/circle_out.png", .4,  reverse = True)
define circle_out2 = ImageDissolve("images/rule/circle_out.png", .8,  reverse = True)
define circle_out_slow = ImageDissolve("images/rule/circle_out.png", 1.5,  reverse = True)
define cloudy = ImageDissolve("images/rule/cloudy.png", 1,  reverse = True)
define explosion = ImageDissolve("images/rule/explosion.png", .3, reverse = True)
define explosion_slow = ImageDissolve("images/rule/explosion.png", 1.2, reverse = True)
define mosaic = ImageDissolve("images/rule/mosaic.png", 1,  reverse = True)
define rotation = ImageDissolve("images/rule/rotation.png", 1,  reverse = True)
define slashing = ImageDissolve("images/rule/slashing.png", .2,  reverse = True)
define wave = ImageDissolve("images/rule/wave.png", 1,  reverse = True)
define whirlpool = ImageDissolve("images/rule/whirlpool.png", 1, reverse = True)
define wipe_corner = ImageDissolve("images/rule/wipe_corner.png", .5,  reverse = True)
define wipe_dl = ImageDissolve("images/rule/wipe_dl.png", 1,  reverse = True)
define wipe_down = ImageDissolve("images/rule/wipe_down.png", .15,  reverse = False)
define wipe_down_slow = ImageDissolve("images/rule/wipe_down.png", .75,  reverse = False)
define wipe_dr = ImageDissolve("images/rule/wipe_dr.png", .5,  reverse = True)
define wipe_dr_fast = ImageDissolve("images/rule/wipe_dr.png", .25,  reverse = True)
define wipe_dr_slow = ImageDissolve("images/rule/wipe_dr.png", 0.8,  reverse = True)
define wipeleft = ImageDissolve("images/rule/wipe.png", .4,  reverse = True)
define wipeleft_slow = ImageDissolve("images/rule/wipe.png", 1.0,  reverse = True)
define wiperight = ImageDissolve("images/rule/wipe.png", .4)
define wipe_ul = ImageDissolve("images/rule/wipe_ul.png", .25,  reverse = True)
define wipe_up = ImageDissolve("images/rule/wipe_up.png", .4,  reverse = False)
define wipe_up_fast = ImageDissolve("images/rule/wipe_up.png", .2,  reverse = False)
define wipe_up_slow = ImageDissolve("images/rule/wipe_up.png", 1,  reverse = False)
define split_open = ImageDissolve("images/rule/up_down.png", .7,  reverse = True)
define split_open_fast = ImageDissolve("images/rule/up_down.png", .25,  reverse = True)
define split_close = ImageDissolve("images/rule/up_down.png", .4)
define split_close_slow = ImageDissolve("images/rule/up_down.png", .8)

init:
    $ offleft = Position(xpos = 0.00, ypos = 1.01, xanchor='right')
    $ farleft = Position(xpos = 0.19, ypos = 1.01, xanchor='center')
    $ farleft_big = Position(xpos = 0.19, ypos = 1.275, xanchor='center')
    $ border_left_big = Position(xpos = 0, ypos = 1.275, xanchor = 0.46)
    $ left = Position(xpos = 0.25, xanchor = 'center')
    $ midleft = Position(xpos = 0.338, ypos = 1.01, xanchor = 'center')
    $ midleft_big = Position(xpos = .26, ypos = 1.275, xanchor = "center")
    $ midleft_down = Position(xpos = 0.338, ypos = .93, xanchor = 'center', yanchor = 'center')
    $ center = Position(xpos = 0.5, ypos = 1.01, xanchor='center', yanchor = 'bottom')
    $ center_big = Position(xpos = 0.5, ypos = 1.275, xanchor='center', yanchor = 'bottom')
    $ center_big_tp = Position(xpos = 0.5, ypos = 1.52, xanchor='center', yanchor = 'bottom')
    $ center_down = Position(xpos = 0.5, ypos = 1.08, xanchor='center', yanchor = 'bottom')
    $ center_bottom = Position(xpos = 0.5, ypos = 1.72, xanchor='center', yanchor = 'bottom')
    $ midright = Position(xpos = 0.663, ypos = 1.01, xanchor = 'center')
    $ midright_down = Position(xpos = 0.663, ypos = 1.75, xanchor = 'center')
    $ midright_big = Position(xpos = 0.74, ypos = 1.275, xanchor = 'center')
    $ right = Position(xpos = 0.75, ypos = 1.275, xanchor='center')
    $ farright = Position(xpos = 0.81, ypos = 1.01, xanchor='center')
    $ farright_big = Position(xpos = 0.75, ypos = 1.275, xanchor='center')
    $ offright = Position(xpos = 1.0, xanchor='left')
    $ bottomleft = Position(xpos = 0.0, ypos = 1.0, xanchor = 'right', yanchor = 'top')
    $ offleft_far = Position(xpos = -.5, ypos = 1.01, xanchor = 'center')
    $ offright_far = Position(xpos = 1.5, ypos = 1.01, xanchor = 'center')
    $ border_right = Position (xpos = 1, xanchor = 'center')
    
#####End Of Day Transition#####

label end_day:
    window hide
    show day_logo with Dissolve(.5)
    pause 1
    
    scene end_bg
    show day_logo
    with Dissolve(2)
    pause 3
    scene black with Dissolve(2)
    pause 1
    return
    
image end_day:
    config.window_hide_transition 
    day_logo
    pause 1
    
    end_bg
    day_logo
    pause 3
    black  

