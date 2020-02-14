###Endings

label endings:
    $ persistent.clear_game = True
    
    if favorite == "tatsuki":
        jump tatsuki_ending
    elif favorite == "kounosuke":
        jump kounosuke_ending
    elif favorite == "shun":
        jump shun_ending
    elif favorite == "kouya":
        jump kouya_ending
    elif favorite == "juuichi":
        jump juuichi_ending
    elif favorite == "shin":
        jump shin_ending
        
#################################################        
label tatsuki_ending:
    show ending1t
    if persistent.clear_tatsuki != True:
        $ renpy.pause(60, hard=True)
    else:
        pause 60
    $ persistent.clear_tatsuki = True
    
    jump ending_message    
    
#################################################
label kounosuke_ending:
    show ending1k
    if persistent.clear_kounosuke != True:
        $ renpy.pause(60, hard=True)
    else:
        pause 60
    $ persistent.clear_kounosuke = True
    
    if kouno_badend == True:
        jump kounosuke_end_bad
    else:
        jump kounosuke_end_good
        
    label kounosuke_end_good:
        scene black with dis
        play music bus_idling
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        scene bus with sdis
        
        "Hm?{w} Wait, didn't he give me two pictures earlier?{p}What's on the other one...?"
        
        scene candystoreout
        show ko 002
        with sdis
        
        "The other photograph is a picture of Kounosuke and I.{p}Ah, this is from when we were looking for scenery.{p}Wait. Something is written on the back."
        
        play sound paper00
        
        "「{i}This doesn't mean that promise is gone.{p}Make sure you keep it for the next time we meet.{p}So, don't forget it.{w} Ever! 」"
    
        scene bus with sdis
        
        "Hahaha, that's Kounosuke, all right."
        
        window hide dis
        scene sky_clear with sdis
        
        "Sitting in the bus, I gaze at the two pictures.\nNostalgia swells inside me,\nand I can't stop myself from smiling bitterly."        
        
        $ persistent.clear_kounosuke2 = True
        
        jump kounosuke_done
    
    ###################################################
    label kounosuke_end_bad:
        scene bstop with sdis
        show ko 002 with dis
        play music melodious08
        $ renpy.music.set_volume(0.75, 0.0, channel = "music")
        
        ko "「... 」"
        
        show ko 007 with dis
        
        ko "「... 」"
        
        show to 002 at midright behind ko with wipeleft
        
        to "「What are you so down for? This is unusual. 」"
        
        show ko 005 with dis
        
        ko "「I-{w=.3}it's nothing. 」"
        
        show ko 007 with dis
        
        ko "「... 」"
    
        show to 001 with dis
        
        to "「...Well, it's okay that you're feeling lonely,\nso cheer up.{w} Right? 」"
        ko "「...Yeah. 」"
        
        jump kounosuke_done
    
    ####################################################
    label kounosuke_done:
        $ config_skipping = False
        window hide dis
        stop music fadeout 4
        scene black with sdis
        pause 4
        
        jump ending_message
        
#################################################
label shun_ending:
    show ending2
    if persistent.clear_shun != True and persistent.clear_kouya != True:
        $ renpy.pause(178, hard=True)
    else:
        pause 178
    $ persistent.clear_shun = True
    
    jump ending_message
    
#################################################
label kouya_ending:
    show ending2
    if persistent.clear_shun != True and persistent.clear_kouya != True:
        $ renpy.pause(178, hard=True)
    else:
        pause 178
    $ persistent.clear_kouya = True
    
    jump ending_message
    
#################################################
label juuichi_ending:
    show ending3
    if persistent.clear_juuichi != True and persistent.clear_shin != True:
        $ renpy.pause(101, hard=True)
    else:
        pause 101
    $ persistent.clear_juuichi = True
    
    jump ending_message
    
#################################################
label shin_ending:
    show ending3
    if persistent.clear_juuichi != True and persistent.clear_shin != True:
        $ renpy.pause(101, hard=True)
    else:
        pause 101
    $ persistent.clear_shin = True
    
    if shin_normalend == True:
        jump shin_end_normal
    elif shin_trueend == True:
        jump shin_end_true
    else:
        jump shin_done
        
    #################################################
    label shin_end_normal:
        #その日が来るまで
        scene black with sdis
        pause 1
        scene shin_house_den with dis
        show am 001
        with sdis
        play music free60
        play sound DoorCloseB
        pause 1.5
        
        si "「I'm home. 」"
        
        show am 002 with dis
        
        am "「Welcome back, Shin-kun. 」"
        si "「... 」"
        
        show am 001 with dis
        
        am "「...I see.{w=.3} You saw him off properly. 」"
        si "「... 」"
        am "「...{w} {nw}"
        show am 005 with dis
        extend "Have you...{w=.3}\nCome to a decision? 」"
        si "「I... 」"
        am "「... 」"
        si "「I... Want to stay here.\nI want to stay with everyone, always.\nIf possible, I want to live here. 」"
        
        show am 001 with dis
    
        am "「...I see. 」"
        si "「I'm sorry.{p}I'm sorry, for my selfishness... 」"
        
        show am 002 with dis
        
        am "「It's okay, you did your best.{p}So, it's okay. 」"
        
        window hide dis
        scene black with sdis
        play sound bosu34
        pause 1
        
        am "「You decided it by yourself.{p}So, everything will be okay. 」"
        si "「Ama...ki... 」"
        am "「It's fine.{p}Whatever you choose, I will always support you.\nI'll go discuss things with the Master. 」"
        si "「I'm...sorry... 」"
        am "「It's okay.{w} I know.{p}So when you're with just me,\nyou don't need to pretend to be tough. 」"
        si "「... 」"
        si "「...! 」"
        si "「...*sniff*...*sniff*... 」"
        si "{size=+15}「WAAAAAH! 」"
        
        show am 004 with dis
        
        am "(It's all right... Until you can stand alone,\nI'll be there to support you.)"
        am "(Until the day the one\nwho can stand with you comes...)"
        
        jump shin_done
        
    #################################################
    label shin_end_true:
        #物語はまだ、これから
        scene black with sdis
        pause 1
        play music piano3_015
        scene hhome with sdis
        play sound fantasy_017
        pause 3
        play sound fantasy_017
        pause 1
        
        "Oh, a text from Shin-kun.{p}Once I checked the notification sound,\nI opened up my cell phone."
    
        play sound open_cell
    
        si "「Good evening. I wonder how texts it's been now?\n\ \ I never thought I'd be using this,\n\ \ but now I really need to thank my father. 」"
        si "「By the way, next time I'm going over there,\n\ \ but if it's no trouble I'd like to\n\ \ go to your home if that's alright. 」"
        si "「I want to see you again. 」"
        "Even after getting back,\nI'm always exchanging texts with Shin."
        "Since signals can't reach Minasato Village,\nit seems he has to go all the way to Kazenari Town."
        "So I can't carelessly let things slip\nand pay close attention to when something happens."
        "Whenever something comes in\nit's usually a holiday."
        "Still, even with the distance\nwe're connected this way."
        "Even with a connection like this,\nI always feel a big warmth inside me."
        fn "「It's no trouble at all! When are you coming?\n\ \ My room's pretty messy so I'll have to clean it.\n\ \ I'm so excited! 」"
        "I smiled unintentionally as I typed out my reply,\nthen pressed the send button."
    
        play sound close_cell
        pause 1
        
        "Our relationship has only just started."
        
        $ persistent.clear_shin2 = True
        
        jump shin_done
        
    #################################################
    label shin_done:
        $ config.skipping = False
        stop music fadeout 1.5
        scene black with sdis
        pause 2
        
        jump ending_message
        
#################################################
label ending_message:
    
    if persistent.afterword0 != True and persistent.clear_game == True:
        $ afterword = 0
        jump new_afterword
    elif persistent.afterword1 != True and persistent.clear_tatsuki == True and persistent.clear_kounosuke == True and persistent.clear_kounosuke2 == True:
        $ afterword = 1
        jump new_afterword
    elif persistent.afterword2 != True and persistent.clear_shun == True and persistent.clear_kouya == True:
        $ afterword = 2
        jump new_afterword
    elif persistent.afterword3 != True and persistent.clear_juuichi == True and persistent.clear_shin == True and persistent.clear_shin2 == True:
        $ afterword = 3
        jump new_afterword
    else:
        jump fin
 
  
    label new_afterword:
        play sound jap_002
        pause .2
        play sound jap_002
        scene sky_clear with dis
        
        "New afterword available.\nCheck out the gallery!"
        
        if afterword == 0:
            $ persistent.afterword0 = True
            jump fin
        elif afterword == 1:
            $persistent.afterword1 = True
            jump fin
        elif afterword == 2:
            $ persistent.afterword2 = True
            jump fin
        elif afterword == 3:
            $ persistent.afterword3 = True
            jump fin
            
    label fin:
        scene black with dis
        pause 2
        $ renpy.full_restart()

    

    
    
        
