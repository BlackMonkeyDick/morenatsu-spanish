## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load
#$ page = 1

image sl_win_normal = "images/image/sl_win_base.png"
image sl_win_hover = "images/image/save_win_over.png"

image sl_kounosuke = "images/image/sl_kounosuke.png"
image sl_tatsuki = "images/image/sl_tatsuki.png"
image sl_shun = "images/image/sl_shun.png"
image sl_kouya = "images/image/sl_kouya.png"
image sl_shin = "images/image/sl_shin.png"
image sl_juuichi = "images/image/sl_juuichi.png"
image sl_kyouji = "images/image/sl_kyouji.png"
image sl_soutarou = "images/image/sl_soutarou.png"
image sl_torahiko = "images/image/sl_torahiko.png"
image sl_none = "images/image/sl_none.png"

image newdata = "images/image/newdata.png"

screen save(p, fade):  
    
    modal True
    
    
    #action Hide('navigation', easeoutleft)
    
    #tag menu    
    if fade == "yes":
        add gui.save_menu_background at fadein
    else:
        add gui.save_menu_background
    
    #use file_slots(_("Save"), p)
    use file_slots(_("Save"), "save", p, fade)  

screen load(p, fade):

    #tag menu
    modal True
    if fade == "yes":
        add gui.load_menu_background at fadein
    else:
        add gui.load_menu_background 

    #use file_slots(_("Load"), p)
    use file_slots(_("Load"), "load", p, fade)
    
screen load2(p, fade):  
    
    modal True
    
    #action Hide('navigation', easeoutleft)
    
    #tag menu    
    if fade == "yes":
        add gui.load_menu_background at fadein
    else:
        add gui.load_menu_background
    
    #use file_slots(_("Save"), p)
    use file_slots(_("Load"), "load2", p, fade)
    

screen file_slots(slot, type, page, fade):
    
    $ persistent.newsave
    
    $ persistent.save_1_1 = [route11, event11, date11] 
    $ persistent.save_1_2 = [route12, event12, date12]
    $ persistent.save_1_3 = [route13, event13, date13] 
    $ persistent.save_1_4 = [route14, event14, date14] 
    
    $ persistent.save_2_1 = [route21, event21, date21] 
    $ persistent.save_2_2 = [route22, event22, date22]
    $ persistent.save_2_3 = [route23, event23, date23] 
    $ persistent.save_2_4 = [route24, event24, date24] 

    $ persistent.save_3_1 = [route31, event31, date31] 
    $ persistent.save_3_2 = [route32, event32, date32]
    $ persistent.save_3_3 = [route33, event33, date33] 
    $ persistent.save_3_4 = [route34, event34, date34] 
     
    $ persistent.save_4_1 = [route41, event41, date41] 
    $ persistent.save_4_2 = [route42, event42, date42]
    $ persistent.save_4_3 = [route43, event43, date43] 
    $ persistent.save_4_4 = [route44, event44, date44] 
    
    $ persistent.save_5_1 = [route51, event51, date51] 
    $ persistent.save_5_2 = [route52, event52, date52]
    $ persistent.save_5_3 = [route53, event53, date53] 
    $ persistent.save_5_4 = [route54, event54, date54] 
     
    $ persistent.save_6_1 = [route61, event61, date61] 
    $ persistent.save_6_2 = [route62, event62, date62]
    $ persistent.save_6_3 = [route63, event63, date63] 
    $ persistent.save_6_4 = [route64, event64, date64] 
     
    $ persistent.save_7_1 = [route71, event71, date71] 
    $ persistent.save_7_2 = [route72, event72, date72]
    $ persistent.save_7_3 = [route73, event73, date73] 
    $ persistent.save_7_4 = [route74, event74, date74] 
     
    $ persistent.save_8_1 = [route81, event81, date81] 
    $ persistent.save_8_2 = [route82, event82, date82]
    $ persistent.save_8_3 = [route83, event83, date83] 
    $ persistent.save_8_4 = [route84, event84, date84] 
    
    $ persistent.save_9_1 = [route91, event91, date91] 
    $ persistent.save_9_2 = [route92, event92, date92]
    $ persistent.save_9_3 = [route93, event93, date93] 
    $ persistent.save_9_4 = [route94, event94, date94] 
    
    #$ persistent.save_1_1 = [route_lock, event_name, the_date]
    
    $ one = 1
    $ two = 2
    $ three = 3
    $ four = 4
    
    $ slot_1 = page * four - three
    $ slot_2 = page * four - two
    $ slot_3 = page * four - one
    $ slot_4 = page * four
    
    $ change = renpy.newest_slot(regexp=None)
    
    if persistent.startedgame != True:
        $ route_lock = "none"
        
    #$ persistent.save_route = route_lock
    
    if slot == _("Save"):
        $ persistent.slotkey = "S"
    elif slot == _("Load"):
        $ persistent.slotkey = "L"
    
    #$ persistent.newsave = renpy.newest_slot(regexp=None)
    
    
    
    #$ save_picture = save_[route_lock]    
    #default page_name_value = FilePageNameInputValue(pattern=_("Page {}"))
    #default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    #use game_menu(title):
        
    use filepage(page, type, fade)

    fixed:

        ## This ensures the input will get the enter event before any of the
        ## buttons do.
        
        if fade == "yes":
            textbutton ("No.[slot_1]") text_size 25 xpos 245 ypos 40 at fadein
            textbutton ("No.[slot_2]") text_size 25 xpos 245 ypos 180 at fadein
            textbutton ("No.[slot_3]") text_size 25 xpos 245 ypos 320 at fadein
            textbutton ("No.[slot_4]") text_size 25 xpos 245 ypos 460 at fadein
        else:
            textbutton ("No.[slot_1]") text_size 25 xpos 245 ypos 40
            textbutton ("No.[slot_2]") text_size 25 xpos 245 ypos 180
            textbutton ("No.[slot_3]") text_size 25 xpos 245 ypos 320
            textbutton ("No.[slot_4]") text_size 25 xpos 245 ypos 460 
        
        if page == 1:
            if fade == "yes":
                vbox:
                    add "sl_[persistent.save_1_1[0]]"  at fadein
                    add "sl_[persistent.save_1_2[0]]"  at fadein
                    add "sl_[persistent.save_1_3[0]]"  at fadein
                    add "sl_[persistent.save_1_4[0]]"  at fadein
                    xpos 397 ypos 39
                    spacing 12
                    
                vbox:
                    textbutton ("[persistent.save_1_1[1]]") text_size 25 xpos 245 ypos 102 at fadein
                    textbutton ("[persistent.save_1_2[1]]") text_size 25 xpos 245 ypos 102 at fadein
                    textbutton ("[persistent.save_1_3[1]]") text_size 25 xpos 245 ypos 102 at fadein
                    textbutton ("[persistent.save_1_4[1]]") text_size 25 xpos 245 ypos 102 at fadein
                    spacing 103
                    
                vbox:
                    textbutton ("[persistent.save_1_1[2]]") text_size 25 xpos 245 ypos 70 at fadein
                    textbutton ("[persistent.save_1_2[2]]") text_size 25 xpos 245 ypos 70 at fadein
                    textbutton ("[persistent.save_1_3[2]]") text_size 25 xpos 245 ypos 70 at fadein
                    textbutton ("[persistent.save_1_4[2]]") text_size 25 xpos 245 ypos 70 at fadein
                    spacing 103
                    
                if persistent.newsave == 11:
                    add "newdata" xpos 325 ypos 42 at fadein
                if persistent.newsave == 12:
                    add "newdata" xpos 325 ypos 182 at fadein
                if persistent.newsave == 13:
                    add "newdata" xpos 325 ypos 320 at fadein
                if persistent.newsave == 14:
                    add "newdata" xpos 325 ypos 460 at fadein
                    
            else:
                vbox:
                    add "sl_[persistent.save_1_1[0]]" 
                    add "sl_[persistent.save_1_2[0]]" 
                    add "sl_[persistent.save_1_3[0]]" 
                    add "sl_[persistent.save_1_4[0]]" 
                    xpos 397 ypos 39
                    spacing 12
                    
                vbox:
                    textbutton ("[persistent.save_1_1[1]]") text_size 25 xpos 245 ypos 102
                    textbutton ("[persistent.save_1_2[1]]") text_size 25 xpos 245 ypos 102
                    textbutton ("[persistent.save_1_3[1]]") text_size 25 xpos 245 ypos 102
                    textbutton ("[persistent.save_1_4[1]]") text_size 25 xpos 245 ypos 102
                    spacing 103
                    
                vbox:
                    textbutton ("[persistent.save_1_1[2]]") text_size 25 xpos 245 ypos 70
                    textbutton ("[persistent.save_1_2[2]]") text_size 25 xpos 245 ypos 70
                    textbutton ("[persistent.save_1_3[2]]") text_size 25 xpos 245 ypos 70
                    textbutton ("[persistent.save_1_4[2]]") text_size 25 xpos 245 ypos 70
                    spacing 103
                    
                if persistent.newsave == 11:
                    add "newdata" xpos 325 ypos 42
                if persistent.newsave == 12:
                    add "newdata" xpos 325 ypos 182
                if persistent.newsave == 13:
                    add "newdata" xpos 325 ypos 320
                if persistent.newsave == 14:
                    add "newdata" xpos 325 ypos 460
                
                
        if page == 2:
            vbox:
                add "sl_[persistent.save_2_1[0]]" 
                add "sl_[persistent.save_2_2[0]]" 
                add "sl_[persistent.save_2_3[0]]" 
                add "sl_[persistent.save_2_4[0]]" 
                xpos 397 ypos 39
                spacing 12
                
            vbox:
                textbutton ("[persistent.save_2_1[1]]") text_size 25 xpos 245 ypos 102
                textbutton ("[persistent.save_2_2[1]]") text_size 25 xpos 245 ypos 102
                textbutton ("[persistent.save_2_3[1]]") text_size 25 xpos 245 ypos 102
                textbutton ("[persistent.save_2_4[1]]") text_size 25 xpos 245 ypos 102
                spacing 103
                
            vbox:
                textbutton ("[persistent.save_2_1[2]]") text_size 25 xpos 245 ypos 70
                textbutton ("[persistent.save_2_2[2]]") text_size 25 xpos 245 ypos 70
                textbutton ("[persistent.save_2_3[2]]") text_size 25 xpos 245 ypos 70
                textbutton ("[persistent.save_2_4[2]]") text_size 25 xpos 245 ypos 70
                spacing 103
                
            if persistent.newsave == 21:
                add "newdata" xpos 325 ypos 42
            if persistent.newsave == 22:
                add "newdata" xpos 325 ypos 182
            if persistent.newsave == 23:
                add "newdata" xpos 325 ypos 320
            if persistent.newsave == 24:
                add "newdata" xpos 325 ypos 460
                
        if page == 3:
            vbox:
                add "sl_[persistent.save_3_1[0]]" 
                add "sl_[persistent.save_3_2[0]]" 
                add "sl_[persistent.save_3_3[0]]" 
                add "sl_[persistent.save_3_4[0]]" 
                xpos 397 ypos 39
                spacing 12
                
            vbox:
                textbutton ("[persistent.save_3_1[1]]") text_size 25 xpos 245 ypos 102
                textbutton ("[persistent.save_3_2[1]]") text_size 25 xpos 245 ypos 102
                textbutton ("[persistent.save_3_3[1]]") text_size 25 xpos 245 ypos 102
                textbutton ("[persistent.save_3_4[1]]") text_size 25 xpos 245 ypos 102
                spacing 103
                
            vbox:
                textbutton ("[persistent.save_3_1[2]]") text_size 25 xpos 245 ypos 70
                textbutton ("[persistent.save_3_2[2]]") text_size 25 xpos 245 ypos 70
                textbutton ("[persistent.save_3_3[2]]") text_size 25 xpos 245 ypos 70
                textbutton ("[persistent.save_3_4[2]]") text_size 25 xpos 245 ypos 70
                spacing 103
                
            if persistent.newsave == 31:
                add "newdata" xpos 325 ypos 42
            if persistent.newsave == 32:
                add "newdata" xpos 325 ypos 182
            if persistent.newsave == 33:
                add "newdata" xpos 325 ypos 320
            if persistent.newsave == 34:
                add "newdata" xpos 325 ypos 460
                
        if page == 4:
            vbox:
                add "sl_[persistent.save_4_1[0]]" 
                add "sl_[persistent.save_4_2[0]]" 
                add "sl_[persistent.save_4_3[0]]" 
                add "sl_[persistent.save_4_4[0]]" 
                xpos 397 ypos 39
                spacing 12
                
            vbox:
                textbutton ("[persistent.save_4_1[1]]") text_size 25 xpos 245 ypos 102
                textbutton ("[persistent.save_4_2[1]]") text_size 25 xpos 245 ypos 102
                textbutton ("[persistent.save_4_3[1]]") text_size 25 xpos 245 ypos 102
                textbutton ("[persistent.save_4_4[1]]") text_size 25 xpos 245 ypos 102
                spacing 103
                
            vbox:
                textbutton ("[persistent.save_4_1[2]]") text_size 25 xpos 245 ypos 70
                textbutton ("[persistent.save_4_2[2]]") text_size 25 xpos 245 ypos 70
                textbutton ("[persistent.save_4_3[2]]") text_size 25 xpos 245 ypos 70
                textbutton ("[persistent.save_4_4[2]]") text_size 25 xpos 245 ypos 70
                spacing 103
                
            if persistent.newsave == 41:
                add "newdata" xpos 325 ypos 42
            if persistent.newsave == 42:
                add "newdata" xpos 325 ypos 182
            if persistent.newsave == 43:
                add "newdata" xpos 325 ypos 320
            if persistent.newsave == 44:
                add "newdata" xpos 325 ypos 460
                
        if page == 5:
            vbox:
                add "sl_[persistent.save_5_1[0]]" 
                add "sl_[persistent.save_5_2[0]]" 
                add "sl_[persistent.save_5_3[0]]" 
                add "sl_[persistent.save_5_4[0]]" 
                xpos 397 ypos 39
                spacing 12
                
            vbox:
                textbutton ("[persistent.save_5_1[1]]") text_size 25 xpos 245 ypos 102
                textbutton ("[persistent.save_5_2[1]]") text_size 25 xpos 245 ypos 102
                textbutton ("[persistent.save_5_3[1]]") text_size 25 xpos 245 ypos 102
                textbutton ("[persistent.save_5_4[1]]") text_size 25 xpos 245 ypos 102
                spacing 103
                
            vbox:
                textbutton ("[persistent.save_5_1[2]]") text_size 25 xpos 245 ypos 70
                textbutton ("[persistent.save_5_2[2]]") text_size 25 xpos 245 ypos 70
                textbutton ("[persistent.save_5_3[2]]") text_size 25 xpos 245 ypos 70
                textbutton ("[persistent.save_5_4[2]]") text_size 25 xpos 245 ypos 70
                spacing 103
                
            if persistent.newsave == 51:
                add "newdata" xpos 325 ypos 42
            if persistent.newsave == 52:
                add "newdata" xpos 325 ypos 182
            if persistent.newsave == 53:
                add "newdata" xpos 325 ypos 320
            if persistent.newsave == 54:
                add "newdata" xpos 325 ypos 460
                
        if page == 6:
            vbox:
                add "sl_[persistent.save_6_1[0]]" 
                add "sl_[persistent.save_6_2[0]]" 
                add "sl_[persistent.save_6_3[0]]" 
                add "sl_[persistent.save_6_4[0]]" 
                xpos 397 ypos 39
                spacing 12
                
            vbox:
                textbutton ("[persistent.save_6_1[1]]") text_size 25 xpos 245 ypos 102
                textbutton ("[persistent.save_6_2[1]]") text_size 25 xpos 245 ypos 102
                textbutton ("[persistent.save_6_3[1]]") text_size 25 xpos 245 ypos 102
                textbutton ("[persistent.save_6_4[1]]") text_size 25 xpos 245 ypos 102
                spacing 103
                
            vbox:
                textbutton ("[persistent.save_6_1[2]]") text_size 25 xpos 245 ypos 70
                textbutton ("[persistent.save_6_2[2]]") text_size 25 xpos 245 ypos 70
                textbutton ("[persistent.save_6_3[2]]") text_size 25 xpos 245 ypos 70
                textbutton ("[persistent.save_6_4[2]]") text_size 25 xpos 245 ypos 70
                spacing 103
                
            if persistent.newsave == 61:
                add "newdata" xpos 325 ypos 42
            if persistent.newsave == 62:
                add "newdata" xpos 325 ypos 182
            if persistent.newsave == 63:
                add "newdata" xpos 325 ypos 320
            if persistent.newsave == 64:
                add "newdata" xpos 325 ypos 460
                
        if page == 7:
            vbox:
                add "sl_[persistent.save_7_1[0]]" 
                add "sl_[persistent.save_7_2[0]]" 
                add "sl_[persistent.save_7_3[0]]" 
                add "sl_[persistent.save_7_4[0]]" 
                xpos 397 ypos 39
                spacing 12
                
            vbox:
                textbutton ("[persistent.save_7_1[1]]") text_size 25 xpos 245 ypos 102
                textbutton ("[persistent.save_7_2[1]]") text_size 25 xpos 245 ypos 102
                textbutton ("[persistent.save_7_3[1]]") text_size 25 xpos 245 ypos 102
                textbutton ("[persistent.save_7_4[1]]") text_size 25 xpos 245 ypos 102
                spacing 103
                
            vbox:
                textbutton ("[persistent.save_7_1[2]]") text_size 25 xpos 245 ypos 70
                textbutton ("[persistent.save_7_2[2]]") text_size 25 xpos 245 ypos 70
                textbutton ("[persistent.save_7_3[2]]") text_size 25 xpos 245 ypos 70
                textbutton ("[persistent.save_7_4[2]]") text_size 25 xpos 245 ypos 70
                spacing 103
                
            if persistent.newsave == 71:
                add "newdata" xpos 325 ypos 42
            if persistent.newsave == 72:
                add "newdata" xpos 325 ypos 182
            if persistent.newsave == 73:
                add "newdata" xpos 325 ypos 320
            if persistent.newsave == 74:
                add "newdata" xpos 325 ypos 460
                
        if page == 8:
            vbox:
                add "sl_[persistent.save_8_1[0]]" 
                add "sl_[persistent.save_8_2[0]]" 
                add "sl_[persistent.save_8_3[0]]" 
                add "sl_[persistent.save_8_4[0]]" 
                xpos 397 ypos 39
                spacing 12
                
            vbox:
                textbutton ("[persistent.save_8_1[1]]") text_size 25 xpos 245 ypos 102
                textbutton ("[persistent.save_8_2[1]]") text_size 25 xpos 245 ypos 102
                textbutton ("[persistent.save_8_3[1]]") text_size 25 xpos 245 ypos 102
                textbutton ("[persistent.save_8_4[1]]") text_size 25 xpos 245 ypos 102
                spacing 103
                
            vbox:
                textbutton ("[persistent.save_8_1[2]]") text_size 25 xpos 245 ypos 70
                textbutton ("[persistent.save_8_2[2]]") text_size 25 xpos 245 ypos 70
                textbutton ("[persistent.save_8_3[2]]") text_size 25 xpos 245 ypos 70
                textbutton ("[persistent.save_8_4[2]]") text_size 25 xpos 245 ypos 70
                spacing 103
                
            if persistent.newsave == 81:
                add "newdata" xpos 325 ypos 42
            if persistent.newsave == 82:
                add "newdata" xpos 325 ypos 182
            if persistent.newsave == 83:
                add "newdata" xpos 325 ypos 320
            if persistent.newsave == 84:
                add "newdata" xpos 325 ypos 460
                
        if page == 9:
            vbox:
                add "sl_[persistent.save_9_1[0]]" 
                add "sl_[persistent.save_9_2[0]]" 
                add "sl_[persistent.save_9_3[0]]" 
                add "sl_[persistent.save_9_4[0]]" 
                xpos 397 ypos 39
                spacing 12
                
            vbox:
                textbutton ("[persistent.save_9_1[1]]") text_size 25 xpos 245 ypos 102
                textbutton ("[persistent.save_9_2[1]]") text_size 25 xpos 245 ypos 102
                textbutton ("[persistent.save_9_3[1]]") text_size 25 xpos 245 ypos 102
                textbutton ("[persistent.save_9_4[1]]") text_size 25 xpos 245 ypos 102
                spacing 103
                
            vbox:
                textbutton ("[persistent.save_9_1[2]]") text_size 25 xpos 245 ypos 70
                textbutton ("[persistent.save_9_2[2]]") text_size 25 xpos 245 ypos 70
                textbutton ("[persistent.save_9_3[2]]") text_size 25 xpos 245 ypos 70
                textbutton ("[persistent.save_9_4[2]]") text_size 25 xpos 245 ypos 70
                spacing 103
                
            if persistent.newsave == 91:
                add "newdata" xpos 325 ypos 42
            if persistent.newsave == 92:
                add "newdata" xpos 325 ypos 182
            if persistent.newsave == 93:
                add "newdata" xpos 325 ypos 320
            if persistent.newsave == 94:
                add "newdata" xpos 325 ypos 460

                

screen filepage(p, t, f): 
    use filepage_arrows(p, t, f)
    use filepage_0(p, t, f)
    use fileslots(p, t, f)
    #use slot_number(p
    
    
        
screen filepage_arrows(page, type, fade):
    if page == 1:
        if fade == "yes":
            vbox:                
                imagebutton idle "sl_up_normal" at fadein
                imagebutton idle "sl_down_normal" hover "sl_down_over"  action [ShowMenu(type, 2, "no"), FilePage(2)] at fadein
                xpos 772 ypos 40
                spacing 440
        else:
            vbox:                
                imagebutton idle "sl_up_normal"
                imagebutton idle "sl_down_normal" hover "sl_down_over"  action [ShowMenu(type, 2, "no"), FilePage(2)]
                xpos 772 ypos 40
                spacing 440
    elif page > 1 and page < 9:
        vbox:                
            imagebutton idle "sl_up_normal"hover "sl_up_over"  action [ShowMenu(type, page-1, "no"), FilePagePrevious()]
            imagebutton idle "sl_down_normal" hover "sl_down_over"  action [ShowMenu(type, page+1, "no"), FilePageNext()]
            xpos 772 ypos 40
            spacing 440
    elif page == 9:
        vbox:                
            imagebutton idle "sl_up_normal" hover "sl_up_over"  action [ShowMenu(type, 8, "no"), FilePage(8)]
            imagebutton idle "sl_down_normal" 
            xpos 772 ypos 40
            spacing 440    
        

screen filepage_0(page, type, fade):
    if fade == "yes":
        vbox:
            imagebutton idle "return_normal" hover "return_hover" action [Hide("save", Dissolve(0.5)), Hide("load", Dissolve(0.5)), Hide("load2", Dissolve(0.5)), Show("navigation")] at fadein
            xpos 55 ypos 420
    else:
        vbox:
            imagebutton idle "return_normal" hover "return_hover" action [Hide("save", Dissolve(0.5)), Hide("load", Dissolve(0.5)), Hide("load2", Dissolve(0.5)), Show("navigation")]
            xpos 55 ypos 420
    
    if fade == "yes":
        hbox:
            xpos 15 ypos 280
            if page == 1:
                imagebutton idle "page_1_hover" at fadein
            else:
                imagebutton idle "page_1_idle" hover "page_1_hover" action [ShowMenu(type, 1, "no"), FilePage(1)] at fadein
            if page == 2:
                imagebutton idle "page_2_hover" 
            else:
                imagebutton idle "page_2_idle" hover "page_2_hover" action [ShowMenu(type, 2, "no"), FilePage(2)] at fadein
            if page == 3:
                imagebutton idle "page_3_hover" 
            else:
                imagebutton idle "page_3_idle" hover "page_3_hover" action [ShowMenu(type, 3, "no"), FilePage(3)] at fadein
            if page == 4:
                imagebutton idle "page_4_hover" 
            else:
                imagebutton idle "page_4_idle" hover "page_4_hover" action [ShowMenu(type, 4, "no"), FilePage(4)] at fadein
            if page == 5:
                imagebutton idle "page_5_hover" 
            else:
                imagebutton idle "page_5_idle" hover "page_5_hover" action [ShowMenu(type, 5, "no"), FilePage(5)] at fadein
                
        hbox:        
            xpos 15 ypos 340
            if page == 6:
                imagebutton idle "page_6_hover" 
            else:
                imagebutton idle "page_6_idle" hover "page_6_hover" action [ShowMenu(type, 6, "no"), FilePage(6)] at fadein
            if page == 7:
                imagebutton idle "page_7_hover" 
            else:
                imagebutton idle "page_7_idle" hover "page_7_hover" action [ShowMenu(type, 7, "no"), FilePage(7)] at fadein
            if page == 8:
                imagebutton idle "page_8_hover" 
            else:
                imagebutton idle "page_8_idle" hover "page_8_hover" action [ShowMenu(type, 8, "no"), FilePage(8)] at fadein
            if page == 9:
                imagebutton idle "page_9_hover" 
            else:
                imagebutton idle "page_9_idle" hover "page_9_hover" action [ShowMenu(type, 9, "no"), FilePage(9)] at fadein
                
    else:
        hbox:
            xpos 15 ypos 280
            if page == 1:
                imagebutton idle "page_1_hover" 
            else:
                imagebutton idle "page_1_idle" hover "page_1_hover" action [ShowMenu(type, 1, "no"), FilePage(1)]
            if page == 2:
                imagebutton idle "page_2_hover" 
            else:
                imagebutton idle "page_2_idle" hover "page_2_hover" action [ShowMenu(type, 2, "no"), FilePage(2)]
            if page == 3:
                imagebutton idle "page_3_hover" 
            else:
                imagebutton idle "page_3_idle" hover "page_3_hover" action [ShowMenu(type, 3, "no"), FilePage(3)]
            if page == 4:
                imagebutton idle "page_4_hover" 
            else:
                imagebutton idle "page_4_idle" hover "page_4_hover" action [ShowMenu(type, 4, "no"), FilePage(4)]
            if page == 5:
                imagebutton idle "page_5_hover" 
            else:
                imagebutton idle "page_5_idle" hover "page_5_hover" action [ShowMenu(type, 5, "no"), FilePage(5)]
                
        hbox:        
            xpos 15 ypos 340
            if page == 6:
                imagebutton idle "page_6_hover" 
            else:
                imagebutton idle "page_6_idle" hover "page_6_hover" action [ShowMenu(type, 6, "no"), FilePage(6)]
            if page == 7:
                imagebutton idle "page_7_hover" 
            else:
                imagebutton idle "page_7_idle" hover "page_7_hover" action [ShowMenu(type, 7, "no"), FilePage(7)]
            if page == 8:
                imagebutton idle "page_8_hover" 
            else:
                imagebutton idle "page_8_idle" hover "page_8_hover" action [ShowMenu(type, 8, "no"), FilePage(8)]
            if page == 9:
                imagebutton idle "page_9_hover" 
            else:
                imagebutton idle "page_9_idle" hover "page_9_hover" action [ShowMenu(type, 9, "no"), FilePage(9)]

#screen filepage_1(page, type): #Saving this incase I need it for later reference
        #hbox:

                #xpos 15 ypos 280
                                    
                #imagebutton idle "page_1_idle" hover "page_1_hover" action [ShowMenu(type, 1), FilePage(1)]
                #imagebutton idle "page_2_idle" hover "page_2_hover" action [ShowMenu(type, 2), FilePage(2)]
                #imagebutton idle "page_3_idle" hover "page_3_hover" action [ShowMenu(type, 3), FilePage(3)]
                #imagebutton idle "page_4_idle" hover "page_4_hover" action [ShowMenu(type, 4), FilePage(4)]
                #imagebutton idle "page_5_idle" hover "page_5_hover" action [ShowMenu(type, 5), FilePage(5)]
        
        #hbox:

                #xpos 15 ypos 340
                                    
                #imagebutton idle "page_6_idle" hover "page_6_hover" action [ShowMenu(type, 6), FilePage(6)]
                #imagebutton idle "page_7_idle" hover "page_7_hover" action [ShowMenu(type, 7), FilePage(7)]
                #imagebutton idle "page_8_idle" hover "page_8_hover" action [ShowMenu(type, 8), FilePage(8)]
                #imagebutton idle "page_9_idle" hover "page_9_hover" action [ShowMenu(type, 9), FilePage(9)]


            
screen fileslots(page, type, fade):
    #order_reverse True
    $ text_variable = [1, 2, 3, 4]

    if page == 1:
        if fade == "yes":
            #grid gui.file_slot_cols gui.file_slot_rows:
            vbox:
                xpos 240 ypos 35
                spacing 4            
                grid 1 1:
                        style_prefix "slot" at fadein    
                        button:
                            if persistent.slotkey == "S":
                                action [FileAction(1), SetVariable("var0", 11), SetVariable("route11", route_lock), SetVariable("event11", event_name), SetVariable("date11", the_date)]
                                text FileTime(1, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                    style "slot_time_text" xpos 55 ypos 110 at fadein
                            else:
                                action FileAction(1)
                                text FileTime(1, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                    style "slot_time_text" xpos 55 ypos 110 at fadein
                            key "save_delete" action FileDelete(1)
                                    
                grid 1 1:
                        style_prefix "slot" at fadein 
                        button:   
                            if persistent.slotkey == "S":
                                action [FileAction(2) , SetVariable("var0", 12), SetVariable("route12", route_lock), SetVariable("event12", event_name), SetVariable("date12", the_date)]
                                text FileTime(2, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                    style "slot_time_text" xpos 55 ypos 110 at fadein
                            else:
                                action FileAction(2)
                                text FileTime(2, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                    style "slot_time_text" xpos 55 ypos 110 at fadein
                            #key "save_delete" action FileDelete(2)
                                
                grid 1 1:
                        style_prefix "slot" at fadein
                        button:   
                            if persistent.slotkey == "S":
                                action [FileAction(3) , SetVariable("var0", 13), SetVariable("route11", route_lock), SetVariable("event13", event_name), SetVariable("date13", the_date)]
                                text FileTime(3, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                    style "slot_time_text" xpos 55 ypos 110 at fadein
                            else:
                                action FileAction(3)
                                text FileTime(3, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                    style "slot_time_text" xpos 55 ypos 110 at fadein
                            #key "save_delete" action FileDelete(3)
                                    
                grid 1 1:
                        style_prefix "slot" at fadein   
                        button:   
                            if persistent.slotkey == "S":
                                action [FileAction(4) , SetVariable("var0", 14), SetVariable("route14", route_lock), SetVariable("event14", event_name), SetVariable("date14", the_date)]  ###ShowMenu('save_character14')]
                                text FileTime(4, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                    style "slot_time_text" xpos 55 ypos 110 at fadein
                            else:
                                action FileAction(4)
                                text FileTime(4, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                    style "slot_time_text" xpos 55 ypos 110 at fadein
                            #key "save_delete" action FileDelete(4)
                            
        else:
            #grid gui.file_slot_cols gui.file_slot_rows:
            vbox:
                xpos 240 ypos 35
                spacing 4            
                grid 1 1:
                        style_prefix "slot"    
                        button:
                            if persistent.slotkey == "S":
                                action [FileAction(1) , SetVariable("var0", 11), SetVariable("route11", route_lock), SetVariable("event11", event_name), SetVariable("date11", the_date)]
                                text FileTime(1, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                    style "slot_time_text" xpos 55 ypos 110
                            else:
                                action FileAction(1)
                                text FileTime(1, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                    style "slot_time_text" xpos 55 ypos 110
                            #key "save_delete" action FileDelete(1)
                                     
                grid 1 1:
                        style_prefix "slot"    
                        button:   
                            if persistent.slotkey == "S":
                                action [FileAction(2) , SetVariable("var0", 12), SetVariable("route12", route_lock), SetVariable("event12", event_name), SetVariable("date12", the_date)]
                                text FileTime(2, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                    style "slot_time_text" xpos 55 ypos 110
                            else:
                                action FileAction(2)
                                text FileTime(2, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                    style "slot_time_text" xpos 55 ypos 110
                            #key "save_delete" action FileDelete(2)
                              
                grid 1 1:
                        style_prefix "slot"    
                        button:   
                            if persistent.slotkey == "S":
                                action [FileAction(3) , SetVariable("var0", 13), SetVariable("route13", route_lock), SetVariable("event13", event_name), SetVariable("date13", the_date)]
                                text FileTime(3, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                    style "slot_time_text" xpos 55 ypos 110
                            else:
                                action FileAction(3)
                                text FileTime(3, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                    style "slot_time_text" xpos 55 ypos 110
                            #key "save_delete" action FileDelete(3)
                           
                grid 1 1:
                        style_prefix "slot"    
                        button:   
                            if persistent.slotkey == "S":
                                action [FileAction(4) , SetVariable("var0", 14), SetVariable("route14", route_lock), SetVariable("event14", event_name), SetVariable("date14", the_date)]
                                text FileTime(4, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                    style "slot_time_text" xpos 55 ypos 110
                            else:
                                action FileAction(4)
                                text FileTime(4, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                    style "slot_time_text" xpos 55 ypos 110
                            #key "save_delete" action FileDelete(4)
                            
    elif page == 2:
        #grid gui.file_slot_cols gui.file_slot_rows:
        vbox:
            xpos 240 ypos 35
            spacing 4            
            grid 1 1:
                    style_prefix "slot"                         
                    button: 
                        if persistent.slotkey == "S":
                            action [FileAction(5) , SetVariable("var0", 21), SetVariable("route21", route_lock), SetVariable("event21", event_name), SetVariable("date21", the_date)]
                            text FileTime(5, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                        else:
                            action FileAction(5)
                            text FileTime(5, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                        #key "save_delete" action FileDelete(5)
                                
            grid 1 1:
                    style_prefix "slot"    
                    button: 
                        if persistent.slotkey == "S":
                            action [FileAction(6) , SetVariable("var0", 22), SetVariable("route22", route_lock), SetVariable("event22", event_name), SetVariable("date22", the_date)]
                            text FileTime(6, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                        else:
                            action FileAction(6)
                            text FileTime(6, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                        #key "save_delete" action FileDelete(6)
                            
            grid 1 1:
                    style_prefix "slot"                         
                    button:   
                        if persistent.slotkey == "S":
                            action [FileAction(7) , SetVariable("var0", 23), SetVariable("route23", route_lock), SetVariable("event23", event_name), SetVariable("date23", the_date)]
                            text FileTime(7, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                        else:
                            action FileAction(7)
                            text FileTime(7, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                        #key "save_delete" action FileDelete(7)
                                
            grid 1 1:
                    style_prefix "slot"    
                    button:   
                        if persistent.slotkey == "S":
                            action [FileAction(8) , SetVariable("var0", 24), SetVariable("route24", route_lock), SetVariable("event24", event_name), SetVariable("date24", the_date)]
                            text FileTime(8, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                        else:
                            action FileAction(8)
                            text FileTime(8, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                        #key "save_delete" action FileDelete(8)
                        
    elif page == 3:
        #grid gui.file_slot_cols gui.file_slot_rows:
        vbox:
            xpos 240 ypos 35
            spacing 4            
            grid 1 1:
                    style_prefix "slot"                         
                    button: 
                        if persistent.slotkey == "S":
                            action [FileAction(9) , SetVariable("var0", 31), SetVariable("route31", route_lock), SetVariable("event31", event_name), SetVariable("date31", the_date)]
                            text FileTime(9, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                        else:
                            action FileAction(9)
                            text FileTime(9, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                        #key "save_delete" action FileDelete(9)
                                
            grid 1 1:
                    style_prefix "slot"    
                    button: 
                        if persistent.slotkey == "S":
                            action [FileAction(10) , SetVariable("var0", 32), SetVariable("route32", route_lock), SetVariable("event32", event_name), SetVariable("date32", the_date)]
                            text FileTime(10, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                        else:
                            action FileAction(10)
                            text FileTime(10, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                        #key "save_delete" action FileDelete(10)
                            
            grid 1 1:
                    style_prefix "slot"                         
                    button:   
                        if persistent.slotkey == "S":
                            action [FileAction(11) , SetVariable("var0", 33), SetVariable("route33", route_lock), SetVariable("event33", event_name), SetVariable("date33", the_date)]
                            text FileTime(11, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                        else:
                            action FileAction(11)
                            text FileTime(11, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                        #key "save_delete" action FileDelete(11)
                                
            grid 1 1:
                    style_prefix "slot"    
                    button:   
                        if persistent.slotkey == "S":
                            action [FileAction(12) , SetVariable("var0", 34), SetVariable("route34", route_lock), SetVariable("event34", event_name), SetVariable("date34", the_date)]
                            text FileTime(12, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                        else:
                            action FileAction(12)
                            text FileTime(12, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                        #key "save_delete" action FileDelete(12)
                            
    elif page == 4:
        #grid gui.file_slot_cols gui.file_slot_rows:
        vbox:
            xpos 240 ypos 35
            spacing 4            
            grid 1 1:
                    style_prefix "slot"                         
                    button: 
                        if persistent.slotkey == "S":
                            action [FileAction(13) , SetVariable("var0", 41), SetVariable("route41", route_lock), SetVariable("event41", event_name), SetVariable("date41", the_date)]
                            text FileTime(13, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                        else:
                            action FileAction(13)
                            text FileTime(13, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                        #key "save_delete" action FileDelete(13)
                                
            grid 1 1:
                    style_prefix "slot"    
                    button: 
                        if persistent.slotkey == "S":
                            action [FileAction(14) , SetVariable("var0", 42), SetVariable("route42", route_lock), SetVariable("event42", event_name), SetVariable("date42", the_date)]
                            text FileTime(14, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                        else:
                            action FileAction(14)
                            text FileTime(14, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                            
            grid 1 1:
                    style_prefix "slot"                         
                    button:   
                        if persistent.slotkey == "S":
                            action [FileAction(15) , SetVariable("var0", 43), SetVariable("route43", route_lock), SetVariable("event43", event_name), SetVariable("date43", the_date)]
                            text FileTime(15, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                        else:
                            action FileAction(15)
                            text FileTime(15, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                                
            grid 1 1:
                    style_prefix "slot"    
                    button:   
                        if persistent.slotkey == "S":
                            action [FileAction(16) , SetVariable("var0", 44), SetVariable("route44", route_lock), SetVariable("event44", event_name), SetVariable("date44", the_date)]
                            text FileTime(16, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                        else:
                            action FileAction(16)
                            text FileTime(16, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                           
    elif page == 5:
        #grid gui.file_slot_cols gui.file_slot_rows:
        vbox:
            xpos 240 ypos 35
            spacing 4            
            grid 1 1:
                    style_prefix "slot"                         
                    button: 
                        if persistent.slotkey == "S":
                            action [FileAction(17) , SetVariable("var0", 51), SetVariable("route51", route_lock), SetVariable("event51", event_name), SetVariable("date51", the_date)]
                            text FileTime(17, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                        else:
                            action FileAction(17)
                            text FileTime(17, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                                
            grid 1 1:
                    style_prefix "slot"    
                    button: 
                        if persistent.slotkey == "S":
                            action [FileAction(18) , SetVariable("var0", 52), SetVariable("route52", route_lock), SetVariable("event52", event_name), SetVariable("date52", the_date)]
                            text FileTime(18, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                        else:
                            action FileAction(18)
                            text FileTime(18, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                            
            grid 1 1:
                    style_prefix "slot"                         
                    button:   
                        if persistent.slotkey == "S":
                            action [FileAction(19) , SetVariable("var0", 53), SetVariable("route53", route_lock), SetVariable("event53", event_name), SetVariable("date53", the_date)]
                            text FileTime(19, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                        else:
                            action FileAction(19)
                            text FileTime(19, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                                
            grid 1 1:
                    style_prefix "slot"    
                    button:   
                        if persistent.slotkey == "S":
                            action [FileAction(20) , SetVariable("var0", 54), SetVariable("route54", route_lock), SetVariable("event54", event_name), SetVariable("date54", the_date)]
                            text FileTime(20, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                        else:
                            action FileAction(20)
                            text FileTime(20, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                            
    elif page == 6:
        #grid gui.file_slot_cols gui.file_slot_rows:
        vbox:
            xpos 240 ypos 35
            spacing 4            
            grid 1 1:
                    style_prefix "slot"                         
                    button: 
                        if persistent.slotkey == "S":
                            action [FileAction(21) , SetVariable("var0", 61), SetVariable("route61", route_lock), SetVariable("event61", event_name), SetVariable("date61", the_date)]
                            text FileTime(21, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                        else:
                            action FileAction(21)
                            text FileTime(21, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                                
            grid 1 1:
                    style_prefix "slot"    
                    button: 
                        if persistent.slotkey == "S":
                            action [FileAction(22) , SetVariable("var0", 62), SetVariable("route62", route_lock), SetVariable("event62", event_name), SetVariable("date62", the_date)]
                            text FileTime(22, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                        else:
                            action FileAction(22)
                            text FileTime(22, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                            
            grid 1 1:
                    style_prefix "slot"                         
                    button:   
                        if persistent.slotkey == "S":
                            action [FileAction(23) , SetVariable("var0", 63), SetVariable("route63", route_lock), SetVariable("event63", event_name), SetVariable("date63", the_date)]
                            text FileTime(23, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                        else:
                            action FileAction(23)
                            text FileTime(23, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                                
            grid 1 1:
                    style_prefix "slot"    
                    button:   
                        if persistent.slotkey == "S":
                            action [FileAction(24) , SetVariable("var0", 64), SetVariable("route64", route_lock), SetVariable("event64", event_name), SetVariable("date64", the_date)]
                            text FileTime(24, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                        else:
                            action FileAction(24)
                            text FileTime(24, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                            
    elif page == 7:
        #grid gui.file_slot_cols gui.file_slot_rows:
        vbox:
            xpos 240 ypos 35
            spacing 4            
            grid 1 1:
                    style_prefix "slot"                         
                    button: 
                        if persistent.slotkey == "S":
                            action [FileAction(25) , SetVariable("var0", 71), SetVariable("route71", route_lock), SetVariable("event71", event_name), SetVariable("date71", the_date)]
                            text FileTime(25, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                        else:
                            action FileAction(25)
                            text FileTime(25, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                                
            grid 1 1:
                    style_prefix "slot"    
                    button: 
                        if persistent.slotkey == "S":
                            action [FileAction(26) , SetVariable("var0", 72), SetVariable("route72", route_lock), SetVariable("event72", event_name), SetVariable("date72", the_date)]
                            text FileTime(26, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                        else:
                            action FileAction(26)
                            text FileTime(26, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                            
            grid 1 1:
                    style_prefix "slot"                         
                    button:   
                        if persistent.slotkey == "S":
                            action [FileAction(27) , SetVariable("var0", 73), SetVariable("route73", route_lock), SetVariable("event73", event_name), SetVariable("date73", the_date)]
                            text FileTime(27, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                        else:
                            action FileAction(27)
                            text FileTime(27, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                                
            grid 1 1:
                    style_prefix "slot"    
                    button:   
                        if persistent.slotkey == "S":
                            action [FileAction(28) , SetVariable("var0", 74), SetVariable("route74", route_lock), SetVariable("event74", event_name), SetVariable("date74", the_date)]
                            text FileTime(28, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                        else:
                            action FileAction(28)
                            text FileTime(28, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                            
    elif page == 8:
        #grid gui.file_slot_cols gui.file_slot_rows:
        vbox:
            xpos 240 ypos 35
            spacing 4            
            grid 1 1:
                    style_prefix "slot"                         
                    button: 
                        if persistent.slotkey == "S":
                            action [FileAction(29) , SetVariable("var0", 81), SetVariable("route81", route_lock), SetVariable("event81", event_name), SetVariable("date81", the_date)]
                            text FileTime(29, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                        else:
                            action FileAction(29)
                            text FileTime(29, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                                
            grid 1 1:
                    style_prefix "slot"    
                    button: 
                        if persistent.slotkey == "S":
                            action [FileAction(30) , SetVariable("var0", 82), SetVariable("route82", route_lock), SetVariable("event82", event_name), SetVariable("date82", the_date)]
                            text FileTime(1, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                        else:
                            action FileAction(30)
                            text FileTime(30, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                            
            grid 1 1:
                    style_prefix "slot"                         
                    button:   
                        if persistent.slotkey == "S":
                            action [FileAction(31) , SetVariable("var0", 83), SetVariable("route83", route_lock), SetVariable("event83", event_name), SetVariable("date83", the_date)]
                            text FileTime(31, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                        else:
                            action FileAction(31)
                            text FileTime(31, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                                
            grid 1 1:
                    style_prefix "slot"    
                    button:   
                        if persistent.slotkey == "S":
                            action [FileAction(32) , SetVariable("var0", 84), SetVariable("route84", route_lock), SetVariable("event84", event_name), SetVariable("date84", the_date)]
                            text FileTime(32, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                        else:
                            action FileAction(32)
                            text FileTime(32, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                            
    elif page == 9:
        #grid gui.file_slot_cols gui.file_slot_rows:
        vbox:
            xpos 240 ypos 35
            spacing 4            
            grid 1 1:
                    style_prefix "slot"                         
                    button: 
                        if persistent.slotkey == "S":
                            action [FileAction(33) , SetVariable("var0", 91), SetVariable("route91", route_lock), SetVariable("event91", event_name), SetVariable("date91", the_date)]
                            text FileTime(33, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                        else:
                            action FileAction(33)
                            text FileTime(33, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                        #key "save_delete" action FileDelete(33)
                                
            grid 1 1:
                    style_prefix "slot"    
                    button: 
                        if persistent.slotkey == "S":
                            action [FileAction(34) , SetVariable("var0", 92), SetVariable("route92", route_lock), SetVariable("event92", event_name), SetVariable("date92", the_date)]
                            text FileTime(34, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                        else:
                            action FileAction(34)
                            text FileTime(34, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                        #key "save_delete" action FileDelete(34)
                            
            grid 1 1:
                    style_prefix "slot"                         
                    button:   
                        if persistent.slotkey == "S":
                            action [FileAction(35) , SetVariable("var0", 93), SetVariable("route93", route_lock), SetVariable("event93", event_name), SetVariable("date93", the_date)]
                            text FileTime(35, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                        else:
                            action FileAction(35)
                            text FileTime(35, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                        #key "save_delete" action FileDelete(35)
                                
            grid 1 1:
                    style_prefix "slot"    
                    button:   
                        if persistent.slotkey == "S":
                            action [FileAction(36) , SetVariable("var0", 94), SetVariable("route94", route_lock), SetVariable("event94", event_name), SetVariable("date94", the_date)]
                            text FileTime(36, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                        else:
                            action FileAction(36)
                            text FileTime(36, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S"), empty=_("NO DATA")):   
                                style "slot_time_text" xpos 55 ypos 110
                        #key "save_delete" action FileDelete(36)
                        
            

                        
                        
                            
#screen file_change(slot):       
        #text FileTime(slot, format=_("August [the_date]")) xpos 10 ypos 38
        #text FileTime(slot, format=_("[event_name]")) xpos 10 ypos 68
        #text FileTime(slot, format=_("Save Time:{#file_time} %Y/%m/%d %H:%M:%S")):   
            #style "slot_time_text" xpos 55 ypos 110            
                            

#for i in range(1 * 1):                    
                    #$ new_page = page - 1
                    #$ slot = i + 1
                    #$ this = new_page * 4 + slot                            

    #if page == 1:
        #add "sl_[persistent.save_1_1_route]"
        #add "sl_[persistent.save_1_2_route]" ypos 100
        #add "sl_[persistent.save_1_3_route]" ypos 200

    #if page == 2:
        #vbox:
            #imagebutton idle "sl_win_normal" hover "sl_win_hover"
            #imagebutton idle "sl_win_normal" hover "sl_win_hover"
            #imagebutton idle "sl_win_normal" hover "sl_win_hover"
            #imagebutton idle "sl_win_normal" hover "sl_win_hover"
            #xpos 240 ypos 35
            #spacing 4
            


          
    


            
                
style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 50
    ypadding 3

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")
    
