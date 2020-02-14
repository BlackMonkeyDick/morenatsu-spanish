###Flags
##Variables to check if conditions have been met

#image movie = Movie(size=(800, 600))
image opening = Movie(channel="opening", play="opp.ogv")
image ending1t = Movie(channel="ending1t", play="end1t.ogv")
image ending1k = Movie(channel="ending1k", play="end1k.ogv")
image ending2 = Movie(channel="ending2", play="end2.ogv")
image ending3 = Movie(channel="ending3", play="end3.ogv")

label splashscreen:
    scene black
    scene thankyou with sdis
    pause 5
    scene black with sdis
    scene notice_en1 with sdis
    pause 5
    scene black with sdis
    $ config.skipping = False
    show opening
    pause 6.6
    hide opening
    pause 2
    
label splashscreen2:
    
    $ persistent.replay = False
    $ renpy.change_language("None")    
    
    if persistent.startedgame != True:
        
        $ var0 = 0
        
        $ route11, event11, date11 = "none", "", ""
        $ route12, event12, date12 = "none", "", ""
        $ route13, event13, date13 = "none", "", ""
        $ route14, event14, date14 = "none", "", ""
        
        $ route21, event21, date21 = "none", "", ""
        $ route22, event22, date22 = "none", "", ""
        $ route23, event23, date23 = "none", "", ""
        $ route24, event24, date24 = "none", "", ""
        
        $ route31, event31, date31 = "none", "", ""
        $ route32, event32, date32 = "none", "", ""
        $ route33, event33, date33 = "none", "", ""
        $ route34, event34, date34 = "none", "", ""
        
        $ route41, event41, date41 = "none", "", ""
        $ route42, event42, date42 = "none", "", ""
        $ route43, event43, date43 = "none", "", ""
        $ route44, event44, date44 = "none", "", ""
        
        $ route51, event51, date51 = "none", "", ""
        $ route52, event52, date52 = "none", "", ""
        $ route53, event53, date53 = "none", "", ""
        $ route54, event54, date54 = "none", "", ""
        
        $ route61, event61, date61 = "none", "", ""
        $ route62, event62, date62 = "none", "", ""
        $ route63, event63, date63 = "none", "", ""
        $ route64, event64, date64 = "none", "", ""
        
        $ route71, event71, date71 = "none", "", ""
        $ route72, event72, date72 = "none", "", ""
        $ route73, event73, date73 = "none", "", ""
        $ route74, event74, date74 = "none", "", ""
        
        $ route81, event81, date81 = "none", "", ""
        $ route82, event82, date82 = "none", "", ""
        $ route83, event83, date83 = "none", "", ""
        $ route84, event84, date84 = "none", "", ""
        
        $ route91, event91, date91 = "none", "", ""
        $ route92, event92, date92 = "none", "", ""
        $ route93, event93, date93 = "none", "", ""
        $ route94, event94, date94 = "none", "", ""
        
        $ route_lock = "none"
        $ event_name = ""
        $ the_date = ""
        
        
        $ persistent.save_1_1 = ["none", "", ""]       
        $ persistent.save_1_2 = ["none", "", ""]
        $ persistent.save_1_3 = ["none", "", ""]
        $ persistent.save_1_4 = ["none", "", ""]
        $ persistent.save_2_1 = ["none", "", ""]
        $ persistent.save_2_2 = ["none", "", ""]
        $ persistent.save_2_3 = ["none", "", ""]
        $ persistent.save_2_4 = ["none", "", ""]
        $ persistent.save_3_1 = ["none", "", ""]
        $ persistent.save_3_2 = ["none", "", ""]
        $ persistent.save_3_3 = ["none", "", ""]
        $ persistent.save_3_4 = ["none", "", ""]
        $ persistent.save_4_1 = ["none", "", ""]
        $ persistent.save_4_2 = ["none", "", ""]
        $ persistent.save_4_3 = ["none", "", ""]
        $ persistent.save_4_4 = ["none", "", ""]
        $ persistent.save_5_1 = ["none", "", ""]
        $ persistent.save_5_2 = ["none", "", ""]
        $ persistent.save_5_3 = ["none", "", ""]
        $ persistent.save_5_4 = ["none", "", ""]
        $ persistent.save_6_1 = ["none", "", ""]
        $ persistent.save_6_2 = ["none", "", ""]
        $ persistent.save_6_3 = ["none", "", ""]
        $ persistent.save_6_4 = ["none", "", ""]
        $ persistent.save_7_1 = ["none", "", ""]
        $ persistent.save_7_2 = ["none", "", ""]
        $ persistent.save_7_3 = ["none", "", ""]
        $ persistent.save_7_4 = ["none", "", ""]
        $ persistent.save_8_1 = ["none", "", ""]
        $ persistent.save_8_2 = ["none", "", ""]
        $ persistent.save_8_3 = ["none", "", ""]
        $ persistent.save_8_4 = ["none", "", ""]
        $ persistent.save_9_1 = ["none", "", ""]
        $ persistent.save_9_2 = ["none", "", ""]
        $ persistent.save_9_3 = ["none", "", ""]
        $ persistent.save_9_4 = ["none", "", ""]
        
        $ persistent.newsave = 0
        $ persistent.testing_var = "0"
        
        $ persistent.windowmode = "window"
        $ persistent.skipmode = "seen"
        $ persistent.skipeffect = "normal"
        
        $ windowmode = "window"
        $ skipmode = "seen"
        $ skipeffect = "normal"
        
        $ persistent.clear_tatsuki = False
        $ persistent.clear_kounosuke = False
        $ persistent.clear_kounosuke2 = False
        $ persistent.clear_shun = False
        $ persistent.clear_kouya = False
        $ persistent.clear_juuichi = False
        $ persistent.clear_shin = False
        $ persistent.clear_shin2 = False
        
        $ persistent.event_tatsuki1 = False
        $ persistent.event_tatsuki2 = False
        $ persistent.event_kounosuke1 = False
        $ persistent.event_kounosuke2 = False
        $ persistent.event_shun1 = False
        $ persistent.event_shun2 = False
        $ persistent.event_kouya1 = False
        $ persistent.event_kouya2 = False
        $ persistent.event_juuichi1 = False
        $ persistent.event_juuichi2 = False
        $ persistent.event_shin1 = False
        $ persistent.event_shin2 = False
        $ comple_kounosuke = False
        $ complete_tatsuki = False
        $ complete_shun = False
        $ complete_kouya = False
        $ complete_shin = False
        $ complete_juuichi = False 
        $ persistent.ghost_pictures = False
        $ persistent.afterword0 = False
        $ persistent.afterword1 = False
        $ persistent.afterword2 = False
        $ persistent.afterword3 = False
        
    else:
        
        $ windowmode = persistent.windowmode
        $ skipmode = persistent.skipmode
        $ skipeffect = persistent.skipeffect
        
        $ var0 = persistent.newsave
        
        $ route_lock = "none"
        $ event_name = ""
        $ the_date = ""
        
        $ route11, event11, date11 = persistent.save_1_1[0], persistent.save_1_1[1], persistent.save_1_1[2]
        $ route12, event12, date12 = persistent.save_1_2[0], persistent.save_1_2[1], persistent.save_1_2[2]
        $ route13, event13, date13 = persistent.save_1_3[0], persistent.save_1_3[1], persistent.save_1_3[2]
        $ route14, event14, date14 = persistent.save_1_4[0], persistent.save_1_4[1], persistent.save_1_4[2]
        
        $ route21, event21, date21 = persistent.save_2_1[0], persistent.save_2_1[1], persistent.save_2_1[2]
        $ route22, event22, date22 = persistent.save_2_2[0], persistent.save_2_2[1], persistent.save_2_2[2]
        $ route23, event23, date23 = persistent.save_2_3[0], persistent.save_2_3[1], persistent.save_2_3[2]
        $ route24, event24, date24 = persistent.save_2_4[0], persistent.save_2_4[1], persistent.save_2_4[2]
        
        $ route31, event31, date31 = persistent.save_3_1[0], persistent.save_3_1[1], persistent.save_3_1[2]
        $ route32, event32, date32 = persistent.save_3_2[0], persistent.save_3_2[1], persistent.save_3_2[2]
        $ route33, event33, date33 = persistent.save_3_3[0], persistent.save_3_3[1], persistent.save_3_3[2]
        $ route34, event34, date34 = persistent.save_3_4[0], persistent.save_3_4[1], persistent.save_3_4[2]
        
        $ route41, event41, date41 = persistent.save_4_1[0], persistent.save_4_1[1], persistent.save_4_1[2]
        $ route42, event42, date42 = persistent.save_4_2[0], persistent.save_4_2[1], persistent.save_4_2[2]
        $ route43, event43, date43 = persistent.save_4_3[0], persistent.save_4_3[1], persistent.save_4_3[2]
        $ route44, event44, date44 = persistent.save_4_4[0], persistent.save_4_4[1], persistent.save_4_4[2]
        
        $ route51, event51, date51 = persistent.save_4_1[0], persistent.save_4_1[1], persistent.save_4_1[2]
        $ route52, event52, date52 = persistent.save_4_2[0], persistent.save_4_2[1], persistent.save_4_2[2]
        $ route53, event53, date53 = persistent.save_4_3[0], persistent.save_4_3[1], persistent.save_4_3[2]
        $ route54, event54, date54 = persistent.save_4_4[0], persistent.save_4_4[1], persistent.save_4_4[2]
        
        $ route61, event61, date61 = persistent.save_4_1[0], persistent.save_4_1[1], persistent.save_4_1[2]
        $ route62, event62, date62 = persistent.save_4_2[0], persistent.save_4_2[1], persistent.save_4_2[2]
        $ route63, event63, date63 = persistent.save_4_3[0], persistent.save_4_3[1], persistent.save_4_3[2]
        $ route64, event64, date64 = persistent.save_4_4[0], persistent.save_4_4[1], persistent.save_4_4[2]
        
        $ route71, event71, date71 = persistent.save_4_1[0], persistent.save_4_1[1], persistent.save_4_1[2]
        $ route72, event72, date72 = persistent.save_4_2[0], persistent.save_4_2[1], persistent.save_4_2[2]
        $ route73, event73, date73 = persistent.save_4_3[0], persistent.save_4_3[1], persistent.save_4_3[2]
        $ route74, event74, date74 = persistent.save_4_4[0], persistent.save_4_4[1], persistent.save_4_4[2]
        
        $ route81, event81, date81 = persistent.save_4_1[0], persistent.save_4_1[1], persistent.save_4_1[2]
        $ route82, event82, date82 = persistent.save_4_2[0], persistent.save_4_2[1], persistent.save_4_2[2]
        $ route83, event83, date83 = persistent.save_4_3[0], persistent.save_4_3[1], persistent.save_4_3[2]
        $ route84, event84, date84 = persistent.save_4_4[0], persistent.save_4_4[1], persistent.save_4_4[2]
        
        $ route91, event91, date91 = persistent.save_4_1[0], persistent.save_4_1[1], persistent.save_4_1[2]
        $ route92, event92, date92 = persistent.save_4_2[0], persistent.save_4_2[1], persistent.save_4_2[2]
        $ route93, event93, date93 = persistent.save_4_3[0], persistent.save_4_3[1], persistent.save_4_3[2]
        $ route94, event94, date94 = persistent.save_4_4[0], persistent.save_4_4[1], persistent.save_4_4[2]
    
    return

label start:
    
    $ persistent.blur_on = True
    
    $ change = 0
    
    
    ##The following event variables will nee to be moved to another section to that it's global to the whole game rather than to the save    
    
    $ meet_yukiharu = False #Becomes True if you meet Yukiharu before locking into Kounosuke's route
    $ kouno_magazine = False #Becomes True if you go to the Market on Day 2 to witness Kounosuke purchasing something from store.  Comes up on Day 10
    $ kouno_busy = False #Becomes True if you spent time with Kounosuke on Day 10
    $ kounosuke_test = False #Becomes true if you take test of courage
    $ ghost_encounter = 0 #Value will change depending on who joins you during test of courage
    $ kouno_badstep = False #Can become True if you mess with Kounosuke/be a jerk
    $ kouno_badgo = False #Will become True if you are mean to Kounosuke two times, will lead to bad ending
    $ kouno_yakitori = False #Will become True if you propose eating Yakitori on Day 22
    $ kouno_festival_ghost = False #Will become True if you hear the story from Kounosuke on Day 22
    $ kouno_badend = False #Will become True if leave Kounosuke on Day 24
    
    
    $ part_time = False #Becomes True if you spend time with Tatsuki on Day 2; you accept offer to work with him
    $ chuu_beat = 0 #Increase when is beaten by any character in the game
    $ chuu_hit = 0 #Increase when you punch him at the festival, you sadist
    
    
    $ meet_gaku = False #Becomes True if you accept Shun's invitation on Day 10
    $ shun_play = False #Become True if you accept Shun's invitation on Day 20
    
    $ meet_band = False #Becomes True if you meet Kouya's bandmates on Day 12

    
    $ juuichi_fireflies01 = False #Becomes True if you spend time with Juuichi on day 4
    $ juuichi_fireflies02 = False #Becomes True if you spend time with Juuichi on day 5
    $ juuichi_hate = False #Becomes True if you spend time with Juuichi on day 4, but not day 5
    $ borrow_jacket = False #Becomes True if you borrow Juuichi's jacket on Day 9
    $ meet_ten = False #Becomes True if you spend time with Juuichi on Day 10
    
    $ shin_lesson = False #Become True if you accept his offer to be taught some baking on day 16
    $ shin_step1 = False #Become True if you call Shin Familial on Day 4    
    $ shin_step2  = False #Become True if you sit on the floor on Day 16
    $ shin_key1 = False #Become True if you try to revive Shin on Day 9
    $ shin_key2 = False #Becomes True if you search inside Shin's desk on Day 16
    $ shin_key3 = False #Becomes True on Day 22 if both shin_step1 and shin_step2 are True
    $ shin_true = False #Becomes True on Day 24 if you confess your feelings to Shin AND shin_key1 = True     
    $ shin_normalend = False #Becomes True on Day 24 if confess your feelings to Shin AND shin_key1 = False
    $ shin_badend = False #Becomes True if you rape Shin on Day 24
    $ shin_trueend = False #Becomes True if the following are True: shin_true, shin_key2, shin_key3
    
    $ meteor_shower = False #When True, will simulate shooting stars
    $ star_x_pos = 0
    $ star_y_pos = 0
    $ star_x_off = 0
    $ star_y_off = 0
    $ star_speed = 0
    $ star_interval = 0
    $ star_wait = 0
    
    $ day = 1 # Used for displaying date on quick menu
    $ the_date = "August 1"  #Used for saving files
    $ event_name = ""  #Used for save files and menu
    $ route_lock = "none"
    
    ###Character Introuction #Will become True when you meet a character for the first time
    
    ##Main Characters
    $ encounter_kounosuke = False
    $ encounter_tatsuki = False
    $ encounter_kouya = False
    $ encounter_torahiko = False
    $ encounter_shin = False
    $ encounter_shun = False
    $ encounter_kyouji = False
    $ encounter_soutarou = False
    $ encounter_juuichi = False
    
    ##Side Characters
    $ encounter_tappei = False
    $ encounter_yukino = False
    $ encounter_akira = False
    $ encounter_chuukichi = False
    $ encounter_tetsuya = False
    $ encounter_shigure = False
    $ encounter_botan1 = False
    $ encounter_yukiharu = False
    $ encounter_harue = False
    $ encounter_nanafuse = False
    $ encounter_botan2 = False
    $ encounter_gaku = False
    $ encounter_iwao = False
    $ encounter_mitsuhisa = False
    $ encounter_kazumi = False
    $ encounter_yuuki = False
    $ encounter_jun = False
    $ encounter_keisuke = False
    $ encounter_ten = False
    $ encounter_amaki = False
    
    $ focus_character = "" #Will change depending on the event you choose everyday and which route you're locked into


    ##Character Admirations
   
    $ love_juuichi = 0
    $ love_kounosuke = 0
    $ love_kouya = 0
    $ love_kyouji = 0
    $ love_shin = 0
    $ love_shun = 0
    $ love_soutarou = 0
    $ love_tatsuki = 0
    $ love_torahiko = 0
    
    $ persistent.startedgame = True
    
    
    $ var0 = 0
        
    $ route11, event11, date11 = "none", "", ""
    $ route12, event12, date12 = "none", "", ""
    $ route13, event13, date13 = "none", "", ""
    $ route14, event14, date14 = "none", "", ""
    
    $ route21, event21, date21 = "none", "", ""
    $ route22, event22, date22 = "none", "", ""
    $ route23, event23, date23 = "none", "", ""
    $ route24, event24, date24 = "none", "", ""
    
    $ route31, event31, date31 = "none", "", ""
    $ route32, event32, date32 = "none", "", ""
    $ route33, event33, date33 = "none", "", ""
    $ route34, event34, date34 = "none", "", ""
    
    $ route41, event41, date41 = "none", "", ""
    $ route42, event42, date42 = "none", "", ""
    $ route43, event43, date43 = "none", "", ""
    $ route44, event44, date44 = "none", "", ""
    
    $ route51, event51, date51 = "none", "", ""
    $ route52, event52, date52 = "none", "", ""
    $ route53, event53, date53 = "none", "", ""
    $ route54, event54, date54 = "none", "", ""
    
    $ route61, event61, date61 = "none", "", ""
    $ route62, event62, date62 = "none", "", ""
    $ route63, event63, date63 = "none", "", ""
    $ route64, event64, date64 = "none", "", ""
    
    $ route71, event71, date71 = "none", "", ""
    $ route72, event72, date72 = "none", "", ""
    $ route73, event73, date73 = "none", "", ""
    $ route74, event74, date74 = "none", "", ""
    
    $ route81, event81, date81 = "none", "", ""
    $ route82, event82, date82 = "none", "", ""
    $ route83, event83, date83 = "none", "", ""
    $ route84, event84, date84 = "none", "", ""
    
    $ route91, event91, date91 = "none", "", ""
    $ route92, event92, date92 = "none", "", ""
    $ route93, event93, date93 = "none", "", ""
    $ route94, event94, date94 = "none", "", ""
    
    $ route_lock = "none"
    $ event_name = ""
    $ the_date = ""
    
    jump name_input
