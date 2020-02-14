###########################################################
###Gallery/Replay Theater
###########################################################
    
screen gallery(page, number):
    if page == "cg":
        use gallery_cg("cg", number)
    elif page == "cg2":
        use gallery_cg2("cg2", number)
    elif page == "rp":
        use gallery_rp(number)                 
    
screen gallery_cg(mode, n):
    modal True
    add "cgmode" at fadein
    tag menu
    hbox:
        imagebutton idle "cg_btn_hover"
        imagebutton idle "rp_btn_normal" hover "rp_btn_hover" action [ShowMenu('gallery', 'rp',  1), Hide('gallery_cg', Dissolve(.5))]
        xpos 400 ypos 25
        spacing 10
        at fadein
        
    vbox:
        imagebutton idle "gallery_return_normal" hover "gallery_return_hover" action [Hide('buttons_cg_1'), Hide('buttons_cg_2'), Hide('buttons_cg_3'), Hide('buttons_cg_4'), 
        Hide('gallery1', Dissolve(.5)), Hide('gallery_cg', Dissolve(0.5)), Show('main_menu', Dissolve(0.5))]
        
        xpos 20 ypos 450
        at fadein        

    if n == 1:
        use buttons_cg_1(mode)
    elif n == 2:
        use buttons_cg_2(mode)
    elif n == 3:
        use buttons_cg_3(mode)
    elif n == 4:
        use buttons_cg_4(mode)
        
screen gallery_cg2(mode, n):
    modal True
    add "rpmode"
    add "cgmode" at fadein
    tag menu
    hbox:
        imagebutton idle "cg_btn_hover"
        imagebutton idle "rp_btn_normal" hover "rp_btn_hover" action [ShowMenu('gallery', 'rp',  1), Hide('gallery_cg', Dissolve(.5))]
        xpos 400 ypos 25
        spacing 10
        at fadein
        
    vbox:
        imagebutton idle "gallery_return_normal" hover "gallery_return_hover" action [Hide('buttons_cg_1'), Hide('buttons_cg_2'), Hide('buttons_cg_3'), Hide('buttons_cg_4'), 
        Hide('gallery1', Dissolve(.5)), Hide('gallery_cg', Dissolve(0.5)), Show('main_menu', Dissolve(0.5))]
        
        xpos 20 ypos 450
        at fadein        

    if n == 1:
        use buttons_cg_1(mode)
    elif n == 2:
        use buttons_cg_2(mode)
    elif n == 3:
        use buttons_cg_3(mode)
    elif n == 4:
        use buttons_cg_4(mode)

screen gallery_rp(n):
    modal True
    add "cgmode"
    add "rpmode" at fadein
    
    hbox:
        
        imagebutton idle "cg_btn_normal" hover "cg_btn_hover" action [ShowMenu('gallery', 'cg2', 1), Hide('gallery_rp', Dissolve(.5))]
        imagebutton idle "rp_btn_hover"          
        xpos 400 ypos 25
        spacing 10
        at fadein
        
    vbox:
        imagebutton idle "gallery_return_normal" hover "gallery_return_hover" action [Hide('buttons_rp_1'), Hide('buttons_rp_2'), Hide('buttons_rp_3'), Hide('buttons_rp_4'), 
        Hide('gallery2', Dissolve(.5)), Show('main_menu', Dissolve(0.5))]
        xpos 20 ypos 450
        at fadein 
    
    if n == 1:
        use buttons_rp_1
    elif n == 2:
        use buttons_rp_2
    elif n == 3:
        use buttons_rp_3
    elif n == 4:
        use buttons_rp_4
        
screen gallery_title1():
        textbutton ("With Tatsuki") xpos 210 ypos 530
screen gallery_title2():
        textbutton ("Night of the Meteor Shower") xpos 210 ypos 530
screen gallery_title3():
        textbutton ("Lovers' Proof") xpos 210 ypos 530
screen gallery_title4():
        textbutton ("Night of Falling Stars") xpos 210 ypos 530
screen gallery_title5():
        textbutton ("The Seventh Wonder") xpos 210 ypos 530
screen gallery_title6():
        textbutton ("Teach me ✭ First ejaculation") xpos 210 ypos 530
screen gallery_title7():
        textbutton ("Continuing from Last Time") xpos 210 ypos 530
screen gallery_title8():
        textbutton ("Sixty-nine") xpos 210 ypos 530
screen gallery_title9():
        textbutton ("Shape of Gratitude") xpos 210 ypos 530
screen gallery_title10():
        textbutton ("When Heart and Body Connect") xpos 210 ypos 530
screen gallery_title11():
        textbutton ("Heartbeats Mixed Together") xpos 210 ypos 530
screen gallery_title12():
        textbutton ("I Like You") xpos 210 ypos 530
screen gallery_title13():
        textbutton ("Goodbyes and a First Kiss") xpos 210 ypos 530
screen gallery_title14():
        textbutton ("Afterwords Part 1: Ume & Roah") xpos 210 ypos 530
screen gallery_title15():
        textbutton ("Afterwords Part 2: Hyugakuo & Yukidaruma") xpos 210 ypos 530
screen gallery_title16():
        textbutton ("Afterwords Part 3: iwak & Ruoh") xpos 210 ypos 530
screen gallery_title17():
        textbutton ("Scripts Afterword: Torainu") xpos 210 ypos 530
        

screen buttons_cg_1(mode ):
    if mode == "cg":
        vbox:
             imagebutton idle "cgmode_1_hover"   
             imagebutton idle "cgmode_2_normal"  hover "cgmode_2_hover"  action ShowMenu('gallery', 'cg', 2)
             imagebutton idle "cgmode_3_normal"  hover "cgmode_3_hover"  action ShowMenu('gallery', 'cg', 3)
             imagebutton idle "cgmode_4_normal"  hover "cgmode_4_hover"  action ShowMenu('gallery', 'cg', 4)
             at fadein
             ypos 180
             
    elif mode == "cg2":
        vbox:
             imagebutton idle "cgmode_1_hover"   
             imagebutton idle "cgmode_2_normal"  hover "cgmode_2_hover"  action ShowMenu('gallery', 'cg2', 2)
             imagebutton idle "cgmode_3_normal"  hover "cgmode_3_hover"  action ShowMenu('gallery', 'cg2', 3)
             imagebutton idle "cgmode_4_normal"  hover "cgmode_4_hover"  action ShowMenu('gallery', 'cg2', 4)
             at fadein
             ypos 180
             
    hbox:
        if persistent.event_tatsuki1 == True:
            imagebutton idle "cg_image_normal" hover "cg_image_hover" hovered Show("gallery_title1") unhovered Hide("gallery_title1") action Show('cg_tatsuki1', Dissolve(0.5))
        else:
            imagebutton idle "cg_image_normal"
        if persistent.event_tatsuki2 == True:
            imagebutton idle "cg_image_normal" hover "cg_image_hover" hovered Show("gallery_title2") unhovered Hide("gallery_title2") action Show('cg_tatsuki2', Dissolve(0.5))
        else:
            imagebutton idle "cg_image_normal"
        if persistent.event_kounosuke1 == True:
            imagebutton idle "cg_image_normal" hover "cg_image_hover" hovered Show("gallery_title3") unhovered Hide("gallery_title3") action Show('cg_kounosuke1', Dissolve(0.5))
        else:
            imagebutton idle "cg_image_normal"
        at fadein
        xpos 220 ypos 135
        spacing 27
       
    hbox:
        if persistent.event_kounosuke2 == True:
            imagebutton idle "cg_image_normal" hover "cg_image_hover" hovered Show("gallery_title4") unhovered Hide("gallery_title4") action Show('cg_kounosuke2', Dissolve(0.5))
        else:
            imagebutton idle "cg_image_normal"
        if persistent.ghost_pictures == True:
            imagebutton idle "cg_image_normal" hover "cg_image_hover" hovered Show("gallery_title5") unhovered Hide("gallery_title5") action Show('cg_ghost1', Dissolve(0.5))
        else:
            imagebutton idle "cg_image_normal"
        at fadein
        xpos 220 ypos 325
        spacing 27
       
    hbox:
        textbutton ("No.1") text_size 28
        textbutton ("No.2") text_size 28 
        textbutton ("No.3") text_size 28 
        xpos 219 ypos 137
        spacing 127
        
    hbox:
        textbutton ("No.4") text_size 28
        textbutton ("No.5") text_size 28 
        xpos 219 ypos 328
        spacing 127
        
    if persistent.event_tatsuki1 == True:   
        add "ev_tatsuki_1" at gallery_size xpos 229 ypos 177
    if persistent.event_tatsuki2 == True:
        add "ev_tatsuki_2" at gallery_size xpos 426 ypos 177
    if persistent.event_kounosuke1 == True:
        add "ev_kounosuke_1" at gallery_size xpos 623 ypos 177
    if persistent.event_kounosuke2 == True:
        add "ev_kounosuke_2" at gallery_size xpos 229 ypos 366
    if persistent.ghost_pictures == True:
        add "ghostpic_clear" at gallery_size xpos 426 ypos 366
        
        
screen buttons_cg_2(mode):
    if mode == "cg":
        vbox:
            imagebutton idle "cgmode_1_normal"  hover "cgmode_1_hover"   action ShowMenu('gallery', 'cg', 1)
            imagebutton idle "cgmode_2_hover"  
            imagebutton idle "cgmode_3_normal"  hover "cgmode_3_hover"   action ShowMenu('gallery', 'cg', 3)
            imagebutton idle "cgmode_4_normal"  hover "cgmode_4_hover"   action ShowMenu('gallery', 'cg', 4)
            at fadein
            ypos 180
            
    elif mode == "cg2":
        vbox:
            imagebutton idle "cgmode_1_normal"  hover "cgmode_1_hover"   action ShowMenu('gallery', 'cg2', 1)
            imagebutton idle "cgmode_2_hover"  
            imagebutton idle "cgmode_3_normal"  hover "cgmode_3_hover"   action ShowMenu('gallery', 'cg2', 3)
            imagebutton idle "cgmode_4_normal"  hover "cgmode_4_hover"   action ShowMenu('gallery', 'cg2', 4)
            at fadein
            ypos 180
        
    hbox:
         if  persistent.event_shun1 == True:
             imagebutton idle "cg_image_normal" hover "cg_image_hover" hovered Show("gallery_title6") unhovered Hide("gallery_title6") action Show('cg_shun1a', Dissolve(0.5))
         else:         
             imagebutton idle "cg_image_normal"
         if  persistent.event_shun2 == True:
             imagebutton idle "cg_image_normal" hover "cg_image_hover" hovered Show("gallery_title7") unhovered Hide("gallery_title7") action Show('cg_shun2a', Dissolve(0.5))
         else:         
             imagebutton idle "cg_image_normal"
         if  persistent.event_kouya1 == True:
             imagebutton idle "cg_image_normal" hover "cg_image_hover" hovered Show("gallery_title8") unhovered Hide("gallery_title8") action Show('cg_kouya1a', Dissolve(0.5))
         else:         
             imagebutton idle "cg_image_normal"
         at fadein
         xpos 220 ypos 135
         spacing 27
       
    hbox:
         if  persistent.event_kouya2 == True:
             imagebutton idle "cg_image_normal" hover "cg_image_hover" hovered Show("gallery_title9") unhovered Hide("gallery_title9") action Show('cg_kouya2a', Dissolve(0.5))
         else:         
             imagebutton idle "cg_image_normal"
         at fadein
         xpos 220 ypos 325
         spacing 27
       
    hbox:
        textbutton ("No.6") text_size 28
        textbutton ("No.7") text_size 28 
        textbutton ("No.8") text_size 28 
        xpos 219 ypos 137
        spacing 127
        
    hbox:
        textbutton ("No.9") text_size 28
        xpos 219 ypos 328
        
    if persistent.event_shun1 == True:
        add "ev_shun_1a" at gallery_size xpos 229 ypos 177
    if persistent.event_shun2 == True:
        add "ev_shun_2a" at gallery_size xpos 426 ypos 177
    if persistent.event_kouya1 == True:
        add "ev_kouya_1a" at gallery_size xpos 623 ypos 177
    if persistent.event_kouya2 == True:
        add "ev_kouya_2a" at gallery_size xpos 229 ypos 366
       

screen buttons_cg_3(mode):
    if mode == "cg":
        vbox:
            imagebutton idle "cgmode_1_normal"  hover "cgmode_1_hover"  action ShowMenu('gallery', 'cg', 1)
            imagebutton idle "cgmode_2_normal"  hover "cgmode_2_hover"  action ShowMenu('gallery', 'cg', 2)
            imagebutton idle "cgmode_3_hover"  
            imagebutton idle "cgmode_4_normal"  hover "cgmode_4_hover"  action ShowMenu('gallery', 'cg', 4)
            at fadein
            ypos 180
            
    elif mode == "cg2":
        vbox:
            imagebutton idle "cgmode_1_normal"  hover "cgmode_1_hover"  action ShowMenu('gallery', 'cg2', 1)
            imagebutton idle "cgmode_2_normal"  hover "cgmode_2_hover"  action ShowMenu('gallery', 'cg2', 2)
            imagebutton idle "cgmode_3_hover"  
            imagebutton idle "cgmode_4_normal"  hover "cgmode_4_hover"  action ShowMenu('gallery', 'cg2', 4)
            at fadein
            ypos 180
        
    hbox:
        if  persistent.event_juuichi1 == True:
            imagebutton idle "cg_image_normal" hover "cg_image_hover" hovered Show("gallery_title10") unhovered Hide("gallery_title10") action Show('cg_juuichi1a', Dissolve(0.5))
        else:         
            imagebutton idle "cg_image_normal"
        if  persistent.event_juuichi2 == True:
            imagebutton idle "cg_image_normal" hover "cg_image_hover" hovered Show("gallery_title11") unhovered Hide("gallery_title11") action Show('cg_juuichi2a', Dissolve(0.5))
        else:         
            imagebutton idle "cg_image_normal"
        if  persistent.event_shin1 == True:
            imagebutton idle "cg_image_normal" hover "cg_image_hover" hovered Show("gallery_title12") unhovered Hide("gallery_title12") action Show('cg_shin1a', Dissolve(0.5))
        else:         
             imagebutton idle "cg_image_normal"
        at fadein
        xpos 220 ypos 135
        spacing 27
       
    hbox:
        if  persistent.event_shin2 == True:
            imagebutton idle "cg_image_normal" hover "cg_image_hover" hovered Show("gallery_title13") unhovered Hide("gallery_title13") action Show('cg_shin2a', Dissolve(0.5))
        else:         
            imagebutton idle "cg_image_normal"
        at fadein
        xpos 220 ypos 325
        spacing 27
       
    hbox:
        textbutton ("No.10") text_size 28
        textbutton ("No.11") text_size 28 
        textbutton ("No.12") text_size 28 
        xpos 219 ypos 137
        spacing 111
        
    hbox:
        textbutton ("No.13") text_size 28
        xpos 219 ypos 328
        
    if persistent.event_juuichi1 == True:
        add "ev_juuichi_1a" at gallery_size xpos 229 ypos 177
    if persistent.event_juuichi2 == True:
        add "ev_juuichi_2a" at gallery_size xpos 426 ypos 177
    if persistent.event_shin1 == True:
        add "ev_shin_1a" at gallery_size xpos 623 ypos 177
    if persistent.event_shin2 == True:
        add "ev_shin_2a" at gallery_size xpos 229 ypos 366
        
screen buttons_cg_4(mode):
    if mode == "cg":
        vbox:
             imagebutton idle "cgmode_1_normal"  hover "cgmode_1_hover"   action ShowMenu('gallery', 'cg', 1)
             imagebutton idle "cgmode_2_normal"  hover "cgmode_2_hover"   action ShowMenu('gallery', 'cg', 2)
             imagebutton idle "cgmode_3_normal"  hover "cgmode_3_hover"   action ShowMenu('gallery', 'cg', 3)
             imagebutton idle "cgmode_4_hover"  
             at fadein
             ypos 180
           
    elif mode == "cg2":
        vbox:
         imagebutton idle "cgmode_1_normal"  hover "cgmode_1_hover"   action ShowMenu('gallery', 'cg2', 1)
         imagebutton idle "cgmode_2_normal"  hover "cgmode_2_hover"   action ShowMenu('gallery', 'cg2', 2)
         imagebutton idle "cgmode_3_normal"  hover "cgmode_3_hover"   action ShowMenu('gallery', 'cg2', 3)
         imagebutton idle "cgmode_4_hover"  
         at fadein
         ypos 180
        
    hbox:
        if  persistent.afterword1 == True:
            imagebutton idle "cg_image_normal" hover "cg_image_hover" hovered Show("gallery_title14") unhovered Hide("gallery_title14") action Show('cg_afterword1a', Dissolve(0.5))
        else:         
            imagebutton idle "cg_image_normal"
        if  persistent.afterword2 == True:
            imagebutton idle "cg_image_normal" hover "cg_image_hover" hovered Show("gallery_title15") unhovered Hide("gallery_title15") action Show('cg_afterword2a', Dissolve(0.5))
        else:         
            imagebutton idle "cg_image_normal"
        if  persistent.afterword3 == True:
            imagebutton idle "cg_image_normal" hover "cg_image_hover" hovered Show("gallery_title16") unhovered Hide("gallery_title16") action Show('cg_afterword3a', Dissolve(0.5))
        else:         
             imagebutton idle "cg_image_normal"
        at fadein
        xpos 220 ypos 135
        spacing 27
       
    hbox:
       if  persistent.afterword0 == True:
             imagebutton idle "cg_image_normal" hover "cg_image_hover" hovered Show("gallery_title17") unhovered Hide("gallery_title17") action Show('cg_afterword0', Dissolve(0.5))
       else:         
             imagebutton idle "cg_image_normal"     
       at fadein
       xpos 220 ypos 325
       spacing 27
       
    hbox:
        textbutton ("No.14") text_size 28
        textbutton ("No.15") text_size 28 
        textbutton ("No.16") text_size 28 
        xpos 219 ypos 137
        spacing 111
        
    hbox:
        textbutton ("No.17") text_size 28
        xpos 219 ypos 328
        
    if persistent.afterword1 == True:
        add "afterword1a" at gallery_size xpos 229 ypos 177
    if persistent.afterword2 == True:
        add "afterword2a" at gallery_size xpos 426 ypos 177
    if persistent.afterword3 == True:
        add "afterword3a" at gallery_size xpos 623 ypos 177
    if persistent.afterword0 == True:
        add "afterword0" at gallery_size xpos 229 ypos 366

########################################################
screen rp_title1():
        textbutton ("With Tatsuki") xpos 210 ypos 530
screen rp_title2():
        textbutton ("Night of the Meteor Shower") xpos 210 ypos 530
screen rp_title3():
        textbutton ("Lovers' Proof") xpos 210 ypos 530
screen rp_title4():
        textbutton ("I am a Lie") xpos 210 ypos 530
screen rp_title5():
        textbutton ("Teach me ✭ First ejaculation") xpos 210 ypos 530
screen rp_title6():
        textbutton ("Continuing from Last Time") xpos 210 ypos 530
screen rp_title7():
        textbutton ("Sixty-nine") xpos 210 ypos 530
screen rp_title8():
        textbutton ("Shape of Gratitude") xpos 210 ypos 530
screen rp_title9():
        textbutton ("When Heart and Body Connect") xpos 210 ypos 530
screen rp_title10():
        textbutton ("Heartbeats Mixed Together") xpos 210 ypos 530
screen rp_title11():
        textbutton ("I Like You") xpos 210 ypos 530

screen buttons_rp_1():    
    vbox:
        imagebutton idle "rpmode_1_hover"  
        imagebutton idle "rpmode_2_normal"  hover "rpmode_2_hover"  action ShowMenu('gallery', 'rp', 2)
        imagebutton idle "rpmode_3_normal"  hover "rpmode_3_hover"  action ShowMenu('gallery', 'rp', 3)
        imagebutton idle "rpmode_4_normal"  hover "rpmode_4_hover"  action ShowMenu('gallery', 'rp', 4)
        at fadein
        ypos 180
        
    hbox:
        if persistent.event_tatsuki1 == True:
            imagebutton idle "cg_image_normal" hover "cg_image_hover" hovered Show("rp_title1") unhovered Hide("rp_title1") action Jump('rp_tatsuki1')
        else:
            imagebutton idle "cg_image_normal"
        if persistent.event_tatsuki2 == True:
            imagebutton idle "cg_image_normal" hover "cg_image_hover" hovered Show("rp_title2") unhovered Hide("rp_title2") action Jump('rp_tatsuki2')
        else:
            imagebutton idle "cg_image_normal"
        if persistent.event_kounosuke1 == True:
            imagebutton idle "cg_image_normal" hover "cg_image_hover" hovered Show("rp_title3") unhovered Hide("rp_title3") action Jump('rp_kounosuke1')
        else:
            imagebutton idle "cg_image_normal"
        at fadein
        xpos 220 ypos 135
        spacing 27
       
    hbox:
        if persistent.ghost_pictures == True and persistent.clear_kounosuke2 == True:
            imagebutton idle "cg_image_normal" hover "cg_image_hover" hovered Show("rp_title4") unhovered Hide("rp_title4") action Jump('rp_nanafuse')
        else:
            imagebutton idle "cg_image_normal"
        at fadein
        xpos 220 ypos 325
        spacing 27
       
    hbox:
        textbutton ("No.1") text_size 28
        textbutton ("No.2") text_size 28 
        textbutton ("No.3") text_size 28 
        xpos 219 ypos 137
        spacing 127
        
    hbox:
        textbutton ("No.4") text_size 28
        xpos 219 ypos 328

    if persistent.event_tatsuki1 == True:
        add "ev_tatsuki_1" at gallery_size xpos 229 ypos 177
    if persistent.event_tatsuki2 == True:
        add "ev_tatsuki_2" at gallery_size xpos 426 ypos 177
    if persistent.event_kounosuke1 == True:
        add "ev_kounosuke_1" at gallery_size xpos 623 ypos 177
    if persistent.ghost_pictures == True and persistent.clear_kounosuke2 == True:
        add "ev_kounosuke_3" at gallery_size xpos 229 ypos 366
    
    
screen buttons_rp_2():
    vbox:
        imagebutton idle "rpmode_1_normal"  hover "rpmode_1_hover"   action ShowMenu('gallery', 'rp', 1)
        imagebutton idle "rpmode_2_hover"  
        imagebutton idle "rpmode_3_normal"  hover "rpmode_3_hover"   action ShowMenu('gallery', 'rp', 3)
        imagebutton idle "rpmode_4_normal"  hover "rpmode_4_hover"   action ShowMenu('gallery', 'rp', 4)
        at fadein
        ypos 180
        
    hbox:
        if persistent.event_shun1 == True:
            imagebutton idle "cg_image_normal" hover "cg_image_hover" hovered Show("rp_title5") unhovered Hide("rp_title5") action Jump('rp_shun1')
        else:
            imagebutton idle "cg_image_normal"
        if persistent.event_shun2 == True:
            imagebutton idle "cg_image_normal" hover "cg_image_hover" hovered Show("rp_title6") unhovered Hide("rp_title6") action Jump('rp_shun2')
        else:
            imagebutton idle "cg_image_normal"
        if persistent.event_kouya1 == True:
            imagebutton idle "cg_image_normal" hover "cg_image_hover" hovered Show("rp_title7") unhovered Hide("rp_title7") action Jump('rp_kouya1')
        else:
            imagebutton idle "cg_image_normal"
        at fadein
        xpos 220 ypos 135
        spacing 27
       
    hbox:
        if persistent.event_kouya2 == True:
            imagebutton idle "cg_image_normal" hover "cg_image_hover" hovered Show("rp_title8") unhovered Hide("rp_title8")  action Jump('rp_kouya2')
        else:
            imagebutton idle "cg_image_normal"
        at fadein
        xpos 220 ypos 325
        spacing 27  
        
    hbox:
        textbutton ("No.5") text_size 28
        textbutton ("No.6") text_size 28 
        textbutton ("No.7") text_size 28 
        xpos 219 ypos 137
        spacing 127
        
    hbox:
        textbutton ("No.8") text_size 28
        xpos 219 ypos 328

    if persistent.event_shun1 == True:                
        add "ev_shun_1a" at gallery_size xpos 229 ypos 177
    if persistent.event_shun2 == True:
        add "ev_shun_2a" at gallery_size xpos 426 ypos 177
    if persistent.event_kouya1 == True:
        add "ev_kouya_1a" at gallery_size xpos 623 ypos 177
    if persistent.event_kouya2 == True:
        add "ev_kouya_2a" at gallery_size xpos 229 ypos 366
    
screen buttons_rp_3():
    vbox:
        imagebutton idle "rpmode_1_normal"  hover "rpmode_1_hover"   action ShowMenu('gallery', 'rp', 1)
        imagebutton idle "rpmode_2_normal"  hover "rpmode_2_hover"   action ShowMenu('gallery', 'rp', 2)
        imagebutton idle "rpmode_3_hover"  
        imagebutton idle "rpmode_4_normal"  hover "rpmode_4_hover"   action ShowMenu('gallery', 'rp', 4)
        at fadein
        ypos 180
        
    hbox:
        if persistent.event_juuichi1 == True:
            imagebutton idle "cg_image_normal" hover "cg_image_hover" hovered Show("rp_title9") unhovered Hide("rp_title9") action Jump('rp_juuichi1')
        else:
            imagebutton idle "cg_image_normal"
        if persistent.event_juuichi2 == True:
            imagebutton idle "cg_image_normal" hover "cg_image_hover" hovered Show("rp_title10") unhovered Hide("rp_title10") action Jump('rp_juuichi2')
        else:
            imagebutton idle "cg_image_normal"
        if persistent.event_shin1 == True:
            imagebutton idle "cg_image_normal" hover "cg_image_hover" hovered Show("rp_title11") unhovered Hide("rp_title11") action Jump('rp_shin1')
        else:
            imagebutton idle "cg_image_normal"
        at fadein
        xpos 220 ypos 135
        spacing 27

    hbox:
        textbutton ("No.9 ") text_size 28
        xpos 219 ypos 137
    hbox:
        textbutton ("No.10") text_size 28 
        textbutton ("No.11") text_size 28 
        xpos 416 ypos 137
        spacing 111
       
    if persistent.event_juuichi1 == True:       
        add "ev_juuichi_1a" at gallery_size xpos 229 ypos 177
    if persistent.event_juuichi2 == True:
        add "ev_juuichi_2a" at gallery_size xpos 426 ypos 177
    if persistent.event_shin1 == True:
        add "ev_shin_1a" at gallery_size xpos 623 ypos 177
        
screen buttons_rp_4():
    vbox:
        imagebutton idle "rpmode_1_normal"  hover "rpmode_1_hover"   action ShowMenu('gallery', 'rp', 1)
        imagebutton idle "rpmode_2_normal"  hover "rpmode_2_hover"   action ShowMenu('gallery', 'rp', 2)
        imagebutton idle "rpmode_3_normal"  hover "rpmode_3_hover"   action ShowMenu('gallery', 'rp', 3)
        imagebutton idle "rpmode_4_hover"  
        at fadein
        ypos 180
        
    


  
#screen cg1():
    #$ cg_page =1
    #action ShowMenu('buttons_cg_')
    
#screen cg2():
    #$ cg_page =2
    #action ShowMenu('buttons_cg_')
    
#screen cg3():
    #$ cg_page =3
    #action ShowMenu('buttons_cg_')
    
#screen  cg4():
    #$ cg_page =4
    #action ShowMenu('buttons_cg_')


