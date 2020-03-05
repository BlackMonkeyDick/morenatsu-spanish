##User Inputs Name Here

screen showfirst(first):
    #text "[first]" xpos 400 ypos 275 size 50 at fadein
    textbutton ("[first]") xpos 400 ypos 275 text_size 50 at fadein
screen showlast(last):
    textbutton ("[last]") xpos 400 ypos 365 text_size 50 at fadein
    
screen rightname(first, last):
    add "confirm" xpos 400 ypos 270 xanchor .5 yanchor .5 at fadein
    textbutton (_("Your name is {color=#e8892d}[first] [last]{/color}?")) xpos 400 ypos 220 xanchor .5 yanchor .5at fadein
    imagebutton xpos 230 ypos 290 idle "dialog_yes_normal" hover "dialog_yes_hover" action [Hide("showfirst", Dissolve(2)), Hide("showlast", Dissolve(2)), Jump("ready")]  at fadein
    imagebutton xpos 430 ypos 290 idle "dialog_no_normal" hover "dialog_no_hover" action [Hide("showfirst"), Hide("showlast"), Jump("yourname")]  at fadein

label name_input:

    $ event_name = "My name is..."
    
    $ renpy.music.set_volume(0.5, 0.0, channel = "sound")
    play sound jingle_001
    scene black with Dissolve(2)
    play music piano_006 fadeout 2
    scene nameinput with Dissolve(2)
    
label yourname:
    
    $ first = renpy.input(_("What is your first name?"), default = "Hiroyuki", length = 10)
    $ first = first.strip()
    if first == "" or first == Null:
        $ first = "Hiroyuki"
        
    #$ renpy.transition(wipe_right)
    show screen showfirst(first) 
        
    $ last = renpy.input(_("What is your last name?"), default = "Nishimura", length = 10)
    $ last = last.strip()
    if last == "" or last == Null:
        $ last = "Nishimura"
        
    #$ renpy.transition(wipe_right)
    show screen showlast(last)
    
    pause .3
    
    call screen rightname(first, last)
    
label ready:

    define fn = Character(_("[first]"), color = "#ffffff")
    define ln = Character(_("[last]"), color = "#ffffff") 
    
    #These two lines will store the most recent names inputted by the player to be used for replays
    $ persistent.name_first = first
    $ persistent.name_last = last

        
    play sound se_006
    stop music fadeout 2
    hide screen showfirst
    hide screen showlast
    scene black with Dissolve(2)
    scene notice_en2 with Dissolve(1)
    pause 5
    scene black with Dissolve(2)
    pause 3
    
    jump begin
    
