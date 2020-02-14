###Preferences

## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences
#screen config_select_win():
    #add 'config_select_1' at move_win
    #action Return()
    
#screen config_select_full():
    #add 'config_select_1' at move_full
    #action Return()

screen preferences1(fade):
    
    $ persistent.windowmode = windowmode
    $ persistent.skipmode = skipmode
    $ persistent.skipeffect = skipeffect

    #tag menu
    modal True
    #add gui.preference_menu_background at fadein
    #add "config_select_1" xpos 22 ypos 197 at fadein
    
    if fade == "yes":
        add gui.preference_menu_background at fadein
    if fade == "no":
        add gui.preference_menu_background
    #add "config_select_1" xpos 22 ypos 197 at fadein
    
    if fade == "yes":
        if persistent.windowmode == "window":
            imagebutton idle "config_select" xpos 30 ypos 195 at fadein
        if persistent.windowmode == "fullscreen":
            imagebutton idle "config_select" xpos 220 ypos 195 at fadein
        if persistent.skipmode == "all":
            imagebutton idle "config_select" xpos 455 ypos 195 at fadein
        if persistent.skipmode == "seen":
            imagebutton idle "config_select" xpos 620 ypos 195 at fadein
        if persistent.skipeffect == "normal":
            imagebutton idle "config_select" xpos 35 ypos 527 at fadein
        if persistent.skipeffect == "skip":
            imagebutton idle "config_select" xpos 215 ypos 527 at fadein

    elif fade == "no":  
        if persistent.windowmode == "window":
            imagebutton idle "config_select" xpos 30 ypos 195
        if persistent.windowmode == "fullscreen":
            imagebutton idle "config_select" xpos 220 ypos 195
        if persistent.skipmode == "all":
            imagebutton idle "config_select" xpos 455 ypos 195
        if persistent.skipmode == "seen":
            imagebutton idle "config_select" xpos 620 ypos 195
        if persistent.skipeffect == "normal":
            imagebutton idle "config_select" xpos 35 ypos 527
        if persistent.skipeffect == "skip":
            imagebutton idle "config_select" xpos 215 ypos 527
        

    if renpy.mobile:
        $ cols = 4
    else:
        $ cols = 4

    #use game_menu(_("Config"), scroll="viewport"):

    #imagebutton idle "config_title_idle" hover "config_title_hover" action Hide('preferences', Dissolve(.5)) xpos 605 ypos 35 at fadein

        hbox:
            imagebutton idle "config_title_idle" hover "config_title_hover" action [ShowMenu('main_menu'), Hide('preferences1', Dissolve(.5))]
            #imagebutton idle "config_back_idle" hover "config_back_hover" action Hide('preferences', Dissolve(.5))
            xpos 610 ypos 35
            spacing 5
            if fade == "yes":
                at fadein
        hbox:
            imagebutton idle "config_default_idle" hover "config_default_hover" action [Preference("display", "window"), Preference("skip", "seen"), Preference("after choices", "stop"), Preference("music volume", 0.4), Preference("sound volume", 0.5), Preference("auto-forward time", 10), Preference("text speed", 40), SetVariable("windowmode", "window"), SetVariable("skipmode", "seen"), SetVariable("skipeffect", "normal")]
            xpos 540 ypos 522

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc"):

                    hbox:
                        style_prefix "radio"
                        #label _("Display")
                        imagebutton idle "config_window_normal" hover "config_window_hover"  action [Preference("display", "window"), SetVariable("windowmode", "window")]
                        imagebutton idle "config_fullscreen_normal" hover "config_fullscreen_hover"  action [Preference("display", "fullscreen"), SetVariable("windowmode", "fullscreen")]
                        if fade == "yes":
                            at fadein
                        xpos 55 ypos 200
                        spacing 65
                        #textbutton _("Window") action Preference("display", "window")
                        #textbutton _("Fullscreen") action Preference("display", "fullscreen")
                        
                else:
                    hbox:
                        style_prefix "radio"
                        #label _("Display")
                        imagebutton idle "config_window_normal" action SetVariable("windowmode", "window")
                        imagebutton idle "config_fullscreen_normal" action SetVariable("windowmode", "fullscreen")
                        if fade == "yes":
                            at fadein
                        xpos 55 ypos 200
                        spacing 65
                    

                #vbox:
                    #style_prefix "radio"
                    #label _("Rollback Side")
                    #textbutton _("Disable") action Preference("rollback side", "disable")
                    #textbutton _("Left") action Preference("rollback side", "left")
                    #textbutton _("Right") action Preference("rollback side", "right")

                hbox:
                    style_prefix "radio"
                    #xpos 10 ypos 200
                    #spacing 100
                    #style_prefix "check"
                    #label _("Skip")
                    imagebutton idle "config_all_normal" hover "config_all_hover" action [Preference("skip", "all"), SetVariable("skipmode", "all")]
                    imagebutton idle "config_seen_normal" hover "config_seen_hover" action [Preference("skip", "seen"), SetVariable("skipmode", "seen")]
                    xpos 175 ypos 198
                    spacing 55
                    if fade == "yes":
                            at fadein
                            
                hbox:
                    style_prefix "radio"
                    imagebutton idle "config_normal_normal" hover "config_normal_hover" action [Preference("after choices", "stop"), SetVariable("skipeffect", "normal")]
                    imagebutton idle "config_skip_normal" hover "config_skip_hover" action [Preference("after choices", "skip"), SetVariable("skipeffect", "skip")]
                    xpos 60 ypos 490
                    spacing 70
                    if fade == "yes":
                        at fadein
                    
                    #textbutton _("Unseen Text") action Preference("skip", "toggle")
                    #textbutton _("After Choices") action Preference("after choices", "toggle")
                    #textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:
                    
                    xpos 22 ypos 200
                    spacing 80

                    #label _("Text Speed")

                    bar value Preference("text speed")

                    #label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:
                    
                    xpos 430 ypos 60
                    spacing 80

                    if config.has_music:
                        #label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        #label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            #if config.sample_sound:
                                #textbutton _("Test") action Play("sound", config.sample_sound)


                    #if config.has_voice:
                        #label _("Voice Volume")

                        #hbox:
                            #bar value Preference("voice volume")

                            #if config.sample_voice:
                                #textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        #textbutton _("Mute All"):
                            #action Preference("all mute", "toggle")
                            #style "mute_all_button"
                            

      
  
label config_set_window1():
    $ persistent.windowmode = "window"
    call screen preferences1("no")
    
label config_set_fullscreen1():
    $ persistent.windowmode = "fullscreen"
    call screen preferences1("no")
    
label config_set_all1():
    $ persistent.skipmode = "all"
    call screen preferences1("no")
    
label config_set_seen1():
    $ persistent.skipmode = "seen"
    call screen preferences1("no")
    
label config_set_normal1():
    $ persistent.skipeffect = "normal"
    call screen preferences1("no")

label config_set_skip1():
    $ persistent.skipeffect = "skip"
    call screen preferences1("no")
    
label config_set_default1():
    $ persistent.windowmode = "window"
    $ persistent.skipmode = "seen"
    $ persistent.skipeffect = "normal"
    call screen preferences1("no")
    
    
screen preferences2(fade):
    
    $ persistent.windowmode = windowmode
    $ persistent.skipmode = skipmode
    $ persistent.skipeffect = skipeffect

    #tag menu
    modal True
    #add gui.preference_menu_background at fadein
    #add "config_select_1" xpos 22 ypos 197 at fadein
    
    if fade == "yes":
        add gui.preference_menu_background at fadein
    if fade == "no":
        add gui.preference_menu_background
    #add "config_select_1" xpos 22 ypos 197 at fadein
    
    if fade == "yes":
        if persistent.windowmode == "window":
            imagebutton idle "config_select" xpos 30 ypos 195 at fadein
        if persistent.windowmode == "fullscreen":
            imagebutton idle "config_select" xpos 220 ypos 195 at fadein
        if persistent.skipmode == "all":
            imagebutton idle "config_select" xpos 455 ypos 195 at fadein
        if persistent.skipmode == "seen":
            imagebutton idle "config_select" xpos 620 ypos 195 at fadein
        if persistent.skipeffect == "normal":
            imagebutton idle "config_select" xpos 35 ypos 527 at fadein
        if persistent.skipeffect == "skip":
            imagebutton idle "config_select" xpos 215 ypos 527 at fadein

    elif fade == "no":  
        if persistent.windowmode == "window":
            imagebutton idle "config_select" xpos 30 ypos 195
        if persistent.windowmode == "fullscreen":
            imagebutton idle "config_select" xpos 220 ypos 195
        if persistent.skipmode == "all":
            imagebutton idle "config_select" xpos 455 ypos 195
        if persistent.skipmode == "seen":
            imagebutton idle "config_select" xpos 620 ypos 195
        if persistent.skipeffect == "normal":
            imagebutton idle "config_select" xpos 35 ypos 527
        if persistent.skipeffect == "skip":
            imagebutton idle "config_select" xpos 215 ypos 527
        

    if renpy.mobile:
        $ cols = 4
    else:
        $ cols = 4

    #use game_menu(_("Config"), scroll="viewport"):

    #imagebutton idle "config_title_idle" hover "config_title_hover" action Hide('preferences', Dissolve(.5)) xpos 605 ypos 35 at fadein

        hbox:
            imagebutton idle "config_title_idle" hover "config_title_hover" action MainMenu()
            imagebutton idle "config_back_idle" hover "config_back_hover" action [Hide('preferences2', Dissolve(.5)), Show("navigation")]
            xpos 470 ypos 35
            spacing 5
            if fade == "yes":
                at fadein
        hbox:
            imagebutton idle "config_default_idle" hover "config_default_hover" action [Preference("display", "window"), Preference("skip", "seen"), Preference("after choices", "stop"), Preference("music volume", 0.4), Preference("sound volume", 0.5), Preference("auto-forward time", 10), Preference("text speed", 40), SetVariable("windowmode", "window"), SetVariable("skipmode", "seen"), SetVariable("skipeffect", "normal")]
            xpos 540 ypos 522

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc"):

                    hbox:
                        style_prefix "radio"
                        #label _("Display")
                        imagebutton idle "config_window_normal" hover "config_window_hover"  action [Preference("display", "window"), SetVariable("windowmode", "window")]
                        imagebutton idle "config_fullscreen_normal" hover "config_fullscreen_hover"  action [Preference("display", "fullscreen"), SetVariable("windowmode", "fullscreen")]
                        if fade == "yes":
                            at fadein
                        xpos 55 ypos 200
                        spacing 65
                        #textbutton _("Window") action Preference("display", "window")
                        #textbutton _("Fullscreen") action Preference("display", "fullscreen")
                        
                else:
                    hbox:
                        style_prefix "radio"
                        #label _("Display")
                        imagebutton idle "config_window_normal" action SetVariable("windowmode", "window")
                        imagebutton idle "config_fullscreen_normal" action SetVariable("windowmode", "fullscreen")
                        if fade == "yes":
                            at fadein
                        xpos 55 ypos 200
                        spacing 65

                #vbox:
                    #style_prefix "radio"
                    #label _("Rollback Side")
                    #textbutton _("Disable") action Preference("rollback side", "disable")
                    #textbutton _("Left") action Preference("rollback side", "left")
                    #textbutton _("Right") action Preference("rollback side", "right")

                hbox:
                    style_prefix "radio"
                    #xpos 10 ypos 200
                    #spacing 100
                    #style_prefix "check"
                    #label _("Skip")
                    imagebutton idle "config_all_normal" hover "config_all_hover" action [Preference("skip", "all"), SetVariable("skipmode", "all")]
                    imagebutton idle "config_seen_normal" hover "config_seen_hover" action [Preference("skip", "seen"), SetVariable("skipmode", "seen")]
                    xpos 175 ypos 198
                    spacing 55
                    if fade == "yes":
                            at fadein
                            
                hbox:
                    style_prefix "radio"
                    imagebutton idle "config_normal_normal" hover "config_normal_hover" action [Preference("after choices", "stop"), SetVariable("skipeffect", "normal")]
                    imagebutton idle "config_skip_normal" hover "config_skip_hover" action [Preference("after choices", "skip"), SetVariable("skipeffect", "skip")]
                    xpos 60 ypos 490
                    spacing 70
                    if fade == "yes":
                        at fadein
                    
                    #textbutton _("Unseen Text") action Preference("skip", "toggle")
                    #textbutton _("After Choices") action Preference("after choices", "toggle")
                    #textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:
                    
                    xpos 22 ypos 200
                    spacing 80

                    #label _("Text Speed")

                    bar value Preference("text speed")

                    #label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:
                    
                    xpos 430 ypos 60
                    spacing 80

                    if config.has_music:
                        #label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        #label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            #if config.sample_sound:
                                #textbutton _("Test") action Play("sound", config.sample_sound)


                    #if config.has_voice:
                        #label _("Voice Volume")

                        #hbox:
                            #bar value Preference("voice volume")

                            #if config.sample_voice:
                                #textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        #textbutton _("Mute All"):
                            #action Preference("all mute", "toggle")
                            #style "mute_all_button"
                            

      
  
label config_set_window2():
    $ persistent.windowmode = "window"
    call screen preferences2("no")
    
label config_set_fullscreen2():
    $ persistent.windowmode = "fullscreen"
    call screen preferences2("no")
    
label config_set_all2():
    $ persistent.skipmode = "all"
    call screen preferences2("no")
    
label config_set_seen2():
    $ persistent.skipmode = "seen"
    call screen preferences2("no")
    
label config_set_normal2():
    $ persistent.skipeffect = "normal"
    call screen preferences2("no")

label config_set_skip2():
    $ persistent.skipeffect = "skip"
    call screen preferences2("no")
    
label config_set_default2():
    $ persistent.windowmode = "window"
    $ persistent.skipmode = "seen"
    $ persistent.skipeffect = "normal"
    call screen preferences2("no")
    


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 225

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    #foreground "images/image/config_selectbar.png"
    #foreground "images/image/check_[prefix_]foreground.png"
    foreground "gui/button/check_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    xoffset - 50
    foreground "gui/button/check_[prefix_]foreground.png" 

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 350

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 450
