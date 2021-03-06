﻿################################################################################
## Initialization
################################################################################
init python:        
    import math
    #translate_define(spanish)
    config.keymap['game_menu'] = []
    config.keymap['game_menu2'] = ['mousedown_3']
    #!#config.game_menu_action = [FileTakeScreenshot(), Show("navigation")]#, transition = menu_in)
    #config.quit_action = Quit(confirm=False)
    #config.OVERWRITE_SAVE_action = renpy.save(confirm=Fasle)
    config.has_autosave = False
    #config.default_windowed = True
    def gloabal_vars(x, y, z):
        global var0
        global var1
        global var2
        var0 = z
        var1 = x
        var2 = y
        
    

init offset = -1

################################################################################
## Styles
################################################################################
image title_select = "images/image/title_selectbar.bmp"
image title_selectbar:
    "title_select"
    linear 2.5 alpha 0.0
    linear 2.5 alpha 1.0
    repeat

image navigation_bar = "images/image/menu.png"

image title_continue = "images/image/title_continue.png"
image title_start = "images/image/title_begin.png"
image title_gallery = "images/image/title_gallery.png"
image title_options = "images/image/title_option.png"
image title_exit = "images/image/title_exit.png"
    
image config_title_idle = "images/image/config_title_normal.png"
image config_title_hover = "images/image/config_title_over.png"
image config_back_idle = "images/image/config_return_normal.png"
image config_back_hover = "images/image/config_return_over.png"
image config_default_idle = "images/image/config_default_normal.png"
image config_default_hover = "images/image/config_default_over.png"


image config_select_1 = "images/image/config_selectbar.png"
image config_select_2 = "images/image/config_selectbar.png"
image config_select_3 = "images/image/config_selectbar.png"
image config_skip_normal = "images/image/config_skip_normal.png"
image config_skip_hover = "images/image/config_skip_over.png"
image config_all_normal = "images/image/config_all_normal.png"
image config_all_hover = "images/image/config_all_over.png"
image config_fullscreen_normal = "images/image/config_fullscreen_normal.png"
image config_fullscreen_hover = "images/image/config_fullscreen_over.png"
image config_window_normal = "images/image/config_window_normal.png"
image config_window_hover = "images/image/config_window_over.png"
image config_normal_normal = "images/image/config_normal_normal.png"
image config_normal_hover = "images/image/config_normal_over.png"
image config_seen_normal = "images/image/config_seen_normal.png"
image config_seen_hover = "images/image/config_seen_over.png"
image config_select = "images/image/config_selectbar.png"


image page_1_idle = "images/image/page1_normal.png"
image page_1_hover = "images/image/page1_over.png"
image page_2_idle = "images/image/page2_normal.png"
image page_2_hover = "images/image/page2_over.png"
image page_3_idle = "images/image/page3_normal.png"
image page_3_hover = "images/image/page3_over.png"
image page_4_idle = "images/image/page4_normal.png"
image page_4_hover = "images/image/page4_over.png"
image page_5_idle = "images/image/page5_normal.png"
image page_5_hover = "images/image/page5_over.png"
image page_6_idle = "images/image/page6_normal.png"
image page_6_hover = "images/image/page6_over.png"
image page_7_idle = "images/image/page7_normal.png"
image page_7_hover = "images/image/page7_over.png"
image page_8_idle = "images/image/page8_normal.png"
image page_8_hover = "images/image/page8_over.png"
image page_9_idle = "images/image/page9_normal.png"
image page_9_hover = "images/image/page9_over.png"

image cgmode = "images/image/cgmode_base.png"
image cgmode_1_normal = "images/image/cgmode_1_normal.png"
image cgmode_1_hover =  "images/image/cgmode_1_over.png"
image cgmode_2_normal = "images/image/cgmode_2_normal.png"
image cgmode_2_hover = "images/image/cgmode_2_over.png"
image cgmode_3_normal = "images/image/cgmode_3_normal.png"
image cgmode_3_hover = "images/image/cgmode_3_over.png"
image cgmode_4_normal = "images/image/cgmode_4_normal.png"
image cgmode_4_hover = "images/image/cgmode_4_over.png"
image cg_btn_normal = "images/image/cgmode_button_normal.png"
image cg_btn_hover = "images/image/cgmode_button_over.png"

image cg_image_normal = "images/image/cgmode_thum_normal.png"
image cg_image_hover = "images/image/cgmode_thum_over.png"

image gallery_return_normal = "images/image/gallery_return_normal.png"
image gallery_return_hover = "images/image/gallery_return_over.png"
image return_normal = "images/image/return_normal.png"
image return_hover = "images/image/return_over.png"

image rpmode = "images/image/replaymode.png"
image rpmode_1_normal = "images/image/rpmode_1_normal.png"
image rpmode_1_hover = "images/image/rpmode_1_over.png"
image rpmode_2_normal = "images/image/rpmode_2_normal.png"
image rpmode_2_hover = "images/image/rpmode_2_over.png"
image rpmode_3_normal = "images/image/rpmode_3_normal.png"
image rpmode_3_hover = "images/image/rpmode_3_over.png"
image rpmode_4_normal = "images/image/rpmode_4_normal.png"
image rpmode_4_hover = "images/image/rpmode_4_over.png"
image rp_btn_normal = "images/image/replay_button_normal.png"
image rp_btn_hover = "images/image/replay_button_over.png"

image dialog_config = "images/image/dialog_config.png"
image dialog_exit = "images/image/dialog_exit.png"
image dialog_load = "images/image/dialog_load.png"
image dialog_overwrite = "images/image/dialog_overwrite.png"
image dialog_title = "images/image/dialog_title.png"
image dialog_yes_normal = "images/image/dialog_yes_normal.png"
image dialog_yes_hover = "images/image/dialog_yes_over.png"
image dialog_no_normal = "images/image/dialog_no_normal.png"
image dialog_no_hover = "images/image/dialog_no_over.png"

image menu_save = "images/image/menu_save.png"
image menu_nosave = "images/image/menu_save_disable.png"
image menu_load = "images/image/menu_load.png"
image menu_noload = "images/image/menu_load_disable.png"
image menu_title = "images/image/menu_totitle.png"
image menu_config = "images/image/menu_config.png"
image menu_char = "images/image/menu_char.png"
image menu_newchar = "images/image/menu_char_new.png"
image menu_return = "images/image/menu_return.png"
image menu_select = "images/image/menu_select.png"


screen title_selectbar1():
    hbox:
        add "title_selectbar"
        xpos 275 ypos 387
        
screen title_selectbar2():
    hbox:
        add "title_selectbar"
        xpos 275 ypos 425 
        
screen title_selectbar3():
    hbox:
        add "title_selectbar"
        xpos 275 ypos 463 
        
screen title_selectbar4():
    hbox:
        add "title_selectbar"
        xpos 275 ypos 501 
        
screen title_selectbar5():
    hbox:
        add "title_selectbar"
        xpos 275 ypos 539 


style default:
    properties gui.text_properties()
    outlines [ (absolute(3), "#000000", absolute(0), absolute(0)) ]
    language gui.language
   
style input:
    properties gui.text_properties("input", accent=True)

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

#style vscrollbar:
    #xsize gui.scrollbar_size
    #base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    #thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    
style vscrollbar:
    xsize 24
    #base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    #thumb Frame("images/image/log_bar_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb "images/image/log_bar_[prefix_]thumb.png"
style slider:
    ysize gui.slider_size
    #base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "images/image/slidebar_[prefix_]thumb.png"
    #thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                style "namebox"
                text who id "who"

        text what id "what"
        
        if _in_replay:
            hbox:
                imagebutton idle "msg_exit_normal" hover "msg_exit_over" action EndReplay(confirm=False)
                imagebutton idle "msg_log_normal" hover "msg_log_over" selected "msg_log_on"  action ShowMenu('history', 1.0)
                imagebutton idle "msg_auto_normal" hover "msg_auto_over" selected "msg_auto_on"  action Preference("auto-forward", "toggle")
                imagebutton idle "msg_skip_normal" hover "msg_skip_over" selected "msg_skip_on"  action Skip() alternate Skip(fast=True, confirm=True)
                imagebutton idle "msg_hide_normal" hover "msg_hide_over" selected "msg_hide_on"  action HideInterface()
                xalign .96
                yalign 0.0
                spacing 10
        
        else:
            hbox:
                style_prefix "quick"
    
                xalign 0.96
                yalign 0.0
                spacing 10
                
                #textbutton _("Menu") action [FileTakeScreenshot(), ShowMenu("navigation")]
                imagebutton idle "msg_log_normal" hover "msg_log_over" selected "msg_log_on"  action ShowMenu('history', 1.0)
                imagebutton idle "msg_auto_normal" hover "msg_auto_over" selected "msg_auto_on"  action Preference("auto-forward", "toggle")
                imagebutton idle "msg_skip_normal" hover "msg_skip_over" selected "msg_skip_on"  action Skip() alternate Skip(fast=True, confirm=True)
                imagebutton idle "msg_hide_normal" hover "msg_hide_over" selected "msg_hide_on"  action HideInterface()
                
    key "game_menu2" action ShowMenu('navigation')


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0
        
    use quick_menu


style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("images/image/message.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos
    line_spacing 5
    adjust_spacing True





## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## http://www.renpy.org/doc/html/screen_special.html#input

#screen input(prompt):
    #style_prefix "input"

    #window:

        #vbox:
            #xpos gui.dialogue_xpos
            #xanchor gui.dialogue_xalign
            #ypos gui.dialogue_ypos
            #xsize gui.dialogue_width

            #text prompt style "input_prompt"
            #input id "input"


#style input_prompt is say_dialogue

#style input_prompt:
    #properties gui.text_properties("input_prompt")
    #xmaximum gui.dialogue_width

#style input:
    #xmaximum gui.dialogue_width
    
    
screen input:

    window:

        #style "nvl_window"
       
        text prompt xalign 0.5 yalign 0.4
        input: 
            id "input" 
            xalign 0.5 yalign 0.6
            color "#ffffff"

    use quick_menu

## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"
    
    $ choices = items

    vbox:
        for i in items:
            textbutton i.caption action i.action
            


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

        
style choice_vbox:
    xalign 0.5
    ypos 300
    yanchor 0.5
    ymaximum 50
            
    spacing gui.choice_spacing
    

style choice_button is default:
    properties gui.button_properties("choice_button")
    hover_sound "av/audio/click_008.wav"
    activate_sound "av/audio/on03.wav"
    
style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
    ymaximum 600
    
style map_choice:
    hover_sound "av/audio/click_008.wav"
    activate_sound "av/audio/on03.wav"



## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus


screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    #if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.96
            yalign 0.76
            spacing 10

            #textbutton _("Back") action Rollback()
            #textbutton _("History") action ShowMenu('history')
            #imagebutton idle "msg_log_normal" hover "msg_log_over" selected "msg_log_on"  action ShowMenu('history')
            #imagebutton idle "msg_auto_normal" hover "msg_auto_over" selected "msg_auto_on"  action Preference("auto-forward", "toggle")
            #imagebutton idle "msg_skip_normal" hover "msg_skip_over" selected "msg_skip_on"  action Skip() alternate Skip(fast=True, confirm=True)
            #imagebutton idle "msg_hide_normal" hover "msg_hide_over" selected "msg_hide_on"  action HideInterface()
            #textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            #textbutton _("Auto") action Preference("auto-forward", "toggle")
            #textbutton _("Save") action ShowMenu('save')
            #textbutton _("Q.Save") action QuickSave()
            #textbutton _("Q.Load") action QuickLoad()
            #textbutton _("Prefs") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.

######Attempting my own personalized quick menu....########################
#screen quick_menu():
    #zorder 100
    
    #if say:
        if _in_replay:
            textbutton _("End Replay") action EndReplay(confirm=True)
    #else:            
        hbox:
            style_prefix "quick"

            xalign 0.96
            yalign 0.76
            spacing 10
            imagebutton idle "msg_log_normal" hover "msg_log_over" selected "msg_log_on"  action Show('history')
            imagebutton idle "msg_auto_normal" hover "msg_auto_over" selected "msg_auto_on"  action Preference("auto-forward", "toggle")
            imagebutton idle "msg_skip_normal" hover "msg_skip_over" selected "msg_skip_on"  action Skip() alternate Skip(fast=True, confirm=True)
            imagebutton idle "msg_hide_normal" hover "msg_hide_over" selected "msg_hide_on"  action HideInterface()
        


init python:
    config.overlay_screens.append("quick_menu")
    config.debug_sound = True
default quick_menu = True


style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen hover_save:
    add "menu_select" xpos 5 ypos 39 at menu_select
screen hover_load:
    add "menu_select" xpos 5 ypos 84 at menu_select
screen hover_title:
    add "menu_select" xpos 5 ypos 129 at menu_select
screen hover_config:
    add "menu_select" xpos 5 ypos 174 at menu_select
screen hover_char:
    add "menu_select" xpos 5 ypos 221 at menu_select
screen hover_return:
    add "menu_select" xpos 5 ypos 265 at menu_select

screen mainmenu():
    modal True
    
    add "gui/overlay/confirm.png"
    add "dialog_title"        

    imagebutton xpos 230 ypos 290 idle "dialog_yes_normal" hover "dialog_yes_hover" action ShowMenu("main_menu")
    imagebutton xpos 430 ypos 290 idle "dialog_no_normal" hover "dialog_no_hover" action Hide("mainmenu")
    
label restartgame:
    call screen main_menu
        
screen navigation():    

    modal True
    #$ screenshot = renpy.take_screenshot(scale=None, background=False)
    
    vbox:
        style_prefix "navigation"        
        
        xpos gui.navigation_xpos
        xalign 0.0
        yalign .9
        spacing 20
        #spacing gui.navigation_spacing

        if main_menu: 
    
            vbox:
                imagebutton idle "title_continue" xpos 5 hovered Show("title_selectbar1") unhovered Hide("title_selectbar1") selected Hide("title_selectbar1") action [Hide("title_selectbar1"), ShowMenu("load", 1, "yes")]
                imagebutton idle "title_start"  xpos 8 hovered Show("title_selectbar2") unhovered Hide("title_selectbar2") selected Hide("title_selectbar2") action [Hide("title_selectbar2"), Start()]
                imagebutton idle "title_gallery" xpos 13 hovered Show("title_selectbar3") unhovered Hide("title_selectbar3") selected Hide("title_selectbar3") action [Hide("title_selectbar3"),  ShowMenu("gallery", "cg", 1), Hide('main_menu', Dissolve(.5))]
                imagebutton idle "title_options"  xpos 12 hovered Show("title_selectbar4") unhovered Hide("title_selectbar4") selected Hide("title_selectbar4") action [Hide("title_selectbar4"), ShowMenu("preferences1", "yes")]
                imagebutton idle "title_exit" xpos 23 hovered Show("title_selectbar5") unhovered Hide("title_selectbar5") selected Hide("title_selectbar5") action Quit(confirm=True)#not main_menu)
                xanchor 0.5 yanchor 0.5
                xpos 360 ypos 125            
                spacing -15
                
        else:    
  
            #add FileCurrentScreenshot() xpos -40 ypos 542 at menublur
            $ menu_blur = FileCurrentScreenshot()
            add menu_blur xpos 360 ypos 894 at menublur
            textbutton ("August [day]: [event_name]")  xpos -20 ypos 520 at fadein
            add 'navigation_bar' xpos -40 ypos -50 at menu_in#ypos -40 #at fadein
            #add "navigation_bar" xpos -10 ypos -40
            vbox:
                if persistent.replay != True:
                    imagebutton idle "menu_save" xanchor .5 yanchor .5 hovered Show("hover_save") unhovered Hide("hover_save") hover_sound "av/audio/click_008.wav" activate_sound "av/audio/on03.wav" action [Hide("hover_save", qdis), Hide("navigation", dis), ShowMenu("save", 1, "yes")]
                    imagebutton idle "menu_load" xanchor .5 yanchor .5 hovered Show("hover_load") unhovered Hide("hover_load") hover_sound "av/audio/click_008.wav" activate_sound "av/audio/on03.wav" action [Hide("hover_load", qdis), Hide("navigation", dis), ShowMenu("load", 1, "yes")]
                else: 
                    imagebutton idle "menu_nosave" xanchor .5 yanchor .5
                    imagebutton idle "menu_noload" xanchor .5 yanchor .5  
                imagebutton idle "menu_title" xanchor .5 yanchor .5 hovered Show("hover_title") unhovered Hide("hover_title") hover_sound "av/audio/click_008.wav" activate_sound "av/audio/on03.wav" action MainMenu()
                imagebutton idle "menu_config" xanchor .5 yanchor .5 hovered Show("hover_config") unhovered Hide("hover_config") hover_sound "av/audio/click_008.wav" activate_sound "av/audio/on03.wav" action [Hide("hover_config", qdis), Hide("navigation", dis), ShowMenu("preferences2", "yes")] 
                imagebutton idle "menu_char" xanchor .5 yanchor .5 hovered Show("hover_char") unhovered Hide("hover_char") hover_sound "av/audio/click_008.wav" activate_sound "av/audio/on03.wav" action [Hide("hover_char", qdis), Hide("navigation", dis),  ShowMenu("characters_main", 0, 1, "yes")]
                imagebutton idle "menu_return" xanchor .5 yanchor .5 hovered Show("hover_return") unhovered Hide("hover_return") hover_sound "av/audio/click_008.wav" activate_sound "av/audio/on03.wav" action [Hide("hover_return", qdis), Return()]
                #imagebutton idle "menu_return" xanchor .5 yanchor .5 hovered Show("hover_return") unhovered Hide("hover_return") hover_sound "av/audio/click_008.wav" activate_sound "av/audio/on03.wav" action [Hide("hover_return", qdis), Hide (FileCurrentScreenshot())]
                #imagebutton idle "menu_return" xanchor .5 yanchor .5 hovered Show("hover_return") unhovered Hide("hover_return") hover_sound "av/audio/click_008.wav" activate_sound "av/audio/on03.wav" action [Hide("hover_return", qdis), Jump("hide_nav")]
                xpos 70 ypos -336
                spacing 7
                at menu_in                
                key "game_menu2" action [Hide("hover_save"), Hide("hover_load"), Hide("hover_title"), Hide("hover_config"), Hide("hover_char"), Hide("hover_return"), Return()]#, menu_out)
            
        
                
            #use quick_menu
                               
    
                
                #vbox:
                    #textbutton _("Save") text_size 37 xpos 25 ypos -340  action [Hide("navigation", qdis), ShowMenu("save", 1)]
                    #textbutton _("Load") text_size 37 xpos 23 ypos -333 action [Hide("navigation", easeoutleft), ShowMenu("load", 1)]        
                    #textbutton _("To Title") text_size 37 xpos -3 ypos -326 action MainMenu()
                    #textbutton _("Config") text_size 37 xpos 10 ypos -319 action [Hide("navigation", easeoutleft), ShowMenu("preferences", "no")]
                    #textbutton _("Character") text_size 37 xpos -15 ypos -312 action [Hide("navigation", qdis), ShowMenu("characters_main", 0, 1)]
                    #textbutton _("Return") text_size 37 xpos 10 ypos -305 action Hide("navigation", easeoutleft)
                

        #if _in_replay:

            #textbutton _("End Replay") action EndReplay(confirm=True)

        #elif not main_menu:

            #textbutton _("Main Menu") action MainMenu()

        #textbutton _("About") action ShowMenu("about")

        #if renpy.variant("pc"):

            ## Help isn't necessary or relevant to mobile devices.
            #textbutton _("Help") action ShowMenu("help")

            ## The quit button is banned on iOS and unnecessary on Android.
            #textbutton _("Quit") action Quit(confirm=not main_menu)
            
label hide_nav:
    hide menu_blur
    return
          
style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
    


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## http://www.renpy.org/doc/html/screen_special.html#main-menu
#screen opening_movie():

    
screen main_menu():       
    ## This ensures that any other menu screen is replaced.
    #$ renpy.transition(dissolve)
    tag menu
    
    

    style_prefix "main_menu"
    
    
    add gui.main_menu_background

    ## This empty frame darkens the main menu.
    frame:
        pass

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation
    #$ renpy.play("av/audio/piano3_001.ogg", channel='music2')

   # if gui.show_name:

        #vbox:
            #text "[config.name!t]":
                #style "main_menu_title"

            #text "[config.version]":
                #style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 280
    yfill True

    ##background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None):
    
    $ page = persistent.historypage

    style_prefix "game_menu"
    
    #if main_menu:
        #add gui.main_menu_background at fadein
        
    #else:
        #add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:
            

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1                        
                        yinitial page                       

                        scrollbars "vertical"
                        mousewheel True
                        
                        #$ persistent.historypage = ui.adjustment()
                        draggable True

                        #side_yfill True

                        transclude

                else:

                    transclude
        vbox:
            imagebutton idle "images/image/log_first_normal.png" hover "images/image/log_first_over.png" action [Hide('history'), ShowMenu('history', 0.0)]
            if persistent.historypage != 0:
                imagebutton idle "images/image/log_uppage_normal.png" hover "images/image/log_uppage_over.png" action [Hide('history'), ShowMenu('history', persistent.historypage - 0.01)]
            else:
                imagebutton idle "images/image/log_uppage_normal.png"
            xpos 736 ypos -55
            spacing 2
            
        vbox:
            if persistent.historypage != 1:
                imagebutton idle "images/image/log_downpage_normal.png" hover "images/image/log_downpage_over.png" action [Hide('history'), ShowMenu('history', persistent.historypage + 0.01)]
            else:
                imagebutton idle "images/image/log_downpage_normal.png"
            imagebutton idle "images/image/log_last_normal.png" hover "images/image/log_last_over.png"  action [Hide('history'), ShowMenu('history', 1.0)]           
            xpos 736 ypos 437
            spacing 2

    #use navigation

    #textbutton _("Return"):
        #style "return_button"

        #action Return()

    #label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")        

style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 85
    top_padding 80

    #background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 0
    yfill True

style game_menu_content_frame:
    left_margin 0
    right_margin 20
    top_margin 10

style game_menu_viewport:
    xsize 920

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 50
    ysize 120

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30
    
##BackTrack##################################################################
##
##At certain points in the game the player will be prompted to either try again or return to the main menu

screen backtrack():
    modal True
    add "backtrack_back"
    imagebutton idle "backtrack_yes_normal" hover "backtrack_yes_hover" xpos 80 ypos 460 action[Jump("jumpback"), Hide("backtrack", ImageDissolve("images/rule/cloudy.png", 1,  reverse = True))]
    imagebutton idle "backtrack_no_normal" hover "backtrack_no_hover" xpos 415 ypos 460 action MainMenu()
        
label jumpback():  
    stop music fadeout 2
    show backtrack_background
    hide backtrack_background with cloudy
    pause 2
    $ renpy.jump(persistent.backtrack_name)
    

## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


## This is redefined in options.rpy to add text to the about screen.
define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size




## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

#screen history():

    #tag menu

    ## Avoid predicting this screen, as it can be very large.
  #  predict False

   # use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport")):

      #  style_prefix "history"

      #  for h in _history_list:

          #  window:

                ## This lays things out properly if history_height is None.
             #   has fixed:
             #       yfit True

              #  if h.who:

                 #   label h.who:
                      #  style "history_name"

                        ## Take the color of the who text from the Character, if
                        ## set.
                      #  if "color" in h.who_args:
                           # text_color h.who_args["color"]

               # text h.what

       # if not _history_list:
            #label _("The dialogue history is empty.")
            
screen history(x):

    #tag menu
    $ persistent.historypage = x

    ## Avoid predicting this screen, as it can be very large.    
    predict 100
    add "images/image/log_base.png"
    
    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport")):

        style_prefix "history"
    
        for h in _history_list:
    
            window:
    
                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True
    
                if h.who:
    
                    label h.who:
                        #style "history_name"
                        style "history_text_size"
    
                        ## Take the color of the who text from the Character, if
                        ## set.
                        #if "color" in h.who_args:
                            #text_color h.who_args["color"]
    
                text h.what size gui.text_size
                
    if renpy.variant("touch"):
        hbox:
            #textbutton _("Return") action Return() text_size 25
            imagebutton idle "gallery_return_normal" hover "gallery_return_hover" action Return() 
            xalign 0.5
            yalign 0.975
                
    key "game_menu2" action Return() 
    
        #if not _history_list:
            #label _("The dialogue history is empty.")
            



style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_text_size:
    size gui.text_size
    xpos 20

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 15

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 8

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 250
    right_padding 20

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## http://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True
    zorder 99
    
    add "gui/overlay/confirm.png"
    
    #if message == layout.ARE_YOU_SURE:
        #add 
        
    if message == layout.OVERWRITE_SAVE:
        add "dialog_overwrite"
        
    elif message == layout.LOADING:
        add "dialog_load"
        
    elif message == layout.QUIT:
        add "dialog_exit"
        
    elif message == layout.MAIN_MENU:
        add "dialog_title"
        

    imagebutton xpos 230 ypos 290 idle "dialog_yes_normal" hover "dialog_yes_hover" action yes_action
    imagebutton xpos 430 ypos 290 idle "dialog_no_normal" hover "dialog_no_hover" action no_action


        
        
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator


define config.skip_indicator = False

#screen skip_indicator():

    #zorder 100
    #style_prefix "skip"

    #frame:

        #hbox:
            #spacing 6

            #text _("Skipping")

            #text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            #text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            #text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"
    


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 96
    style_prefix "notify"

    frame at notify_appear:
        text message

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## http://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = 6

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")
    line_spacing 5

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")


################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 450

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    #zorder 100

    hbox:
        style_prefix "quick"

        xalign 1.0
        yalign 0.98
        
        textbutton _("Menu") action ShowMenu("navigation") text_size 25 #[FileTakeScreenshot(), Show("navigation")]
        
    hbox:
        
        style_prefix "quick"

        xalign 0.875
        yalign 0.98
        
        textbutton _("Back") action Rollback() text_size 25
        
        #textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
        #textbutton _("Auto") action Preference("auto-forward", "toggle")
        #textbutton _("Menu") action Show("navigation")


#style window:
    #variant "small"
    #background "gui/phone/textbox.png"

#style nvl_window:
    #variant "small"
    #background "gui/phone/nvl.png"

#style main_menu_frame:
    #variant "small"
    #background "gui/phone/overlay/main_menu.png"

#style game_menu_outer_frame:
    #variant "small"
    #background "gui/phone/overlay/game_menu.png"

#style game_menu_navigation_frame:
    #variant "small"
    #xsize 340

#style game_menu_content_frame:
    #variant "small"
    #top_margin 0

#style pref_vbox:
    #variant "small"
    #xsize 400

#style slider_pref_vbox:
    #variant "small"
    #xsize None

#style slider_pref_slider:
    #variant "small"
    #xsize 600




