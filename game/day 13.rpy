###Day 13

screen tatsukihouse13:
    hbox:
        add "arrow right"
        at tatsukibounce1
    hbox:
        add "icon_shun"
        at tatsukibounce2
    hbox: 
        text "Tatsuki's House"
        xalign .85 yalign .88
        
screen school13:
    hbox:
        add "arrow down"
        at schoolbounce1
    hbox:
        add "icon_tatsu"
        at schoolbounce2
    hbox:
        text "School"
        xalign .42 yalign .37
        
        
screen minasatomap13():
    add "map"
    add "mapdate"
    imagebutton idle "a icon" hover "icon loop" xpos 315 ypos 163 action Jump("tatsuki13") hovered Show("school13")  unhovered Hide("school13") hover_sound "av/audio/click_008.wav"
    imagebutton idle "a icon" hover "icon loop"  xpos 662 ypos 391  action Jump("shun13") hovered Show("tatsukihouse13")  unhovered Hide("tatsukihouse13") hover_sound "av/audio/click_008.wav"
    hbox:
        text "{size=+30}August 13"
        at maptime     

####################################################
label day13:
    
    $ renpy.music.set_volume(1.0, 0.0, channel = "music")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound2")
    
    $ day = 13
    $ focus_character = ""
    $ event_name = "８月13日"
    $ the_date = "August 13"
    
    window hide
    play music birds_chirping
    
    scene sky01 
    show text "{size=+130}August 13" at truecenter
    with Dissolve(.5)

    pause 3
    scene black with Dissolve(1)
    pause .4
    
    scene hbroom with wipe_corner
    
    fn "「I wonder what I should do today. 」"
    
    play music "<from 2.5>av/audio/free0422.ogg"
    
    call screen minasatomap13

#######################################################    
label shun13:

    $ focus_character = "shun"
    $ love_shun += 1
    $ event_name = "Hearing Strange Sounds"

    scene map
    hide screen tatsukihouse13
    stop music fadeout 1
    scene black with wipe_dr
    pause .2
    scene old_house1 with wipe_right
    play music piano2_015
    $ renpy.music.set_volume(0.8, 0.0, channel = "music")
    play sound don20
    
    su "「Wawawawawa!{w=.3} Tatsuki-san,\n\ \ You-{w=.3} you're-{w=.3} you're fast!! 」"
    ta "「Wahahahahahahahaha!! 」"
    
    play sound don20
    pause 1

    "Tatsu-nii's house{w=.3}{cps=10}... no,{w=.2}{cps=40} a little earlier.{p}I was invited to the {w=.3}{cps=10}\"Old Kodori House,\"{w=.2}{cps=40}\nwhere Shun-kun's relatives live."
    "Is Shun-kun there?{w=.3} I think he is because\nthere's the familiar sound of hearty laughter\nand a small, timid voice."
    "It seems they got here before me.\nWhat should I do?"

    menu:
        "A. Let's play together.":
            jump shun13_play
        "B. I shouldn't disturb them...":
            jump shun13_alone
        "C. Suddenly jump out and surprise them.":
            jump shun13_surprise

    #############################################
    label shun13_play:

        $ event_name = "Let's Play Together"
        $ love_shun += 1
        $ love_tatsuki += 1
        
        fn "「Heeey! 」"
        ta "「Ooh, [fn]! 」"
        "I wave my hand to both of them in the courtyard.{p}Tatsu-nii notices me at the entrance\nand lowers Shun-kun, who was riding on his shoulders."
        "It looks like one was giving the other\na piggyback ride and spinning around in place.{p}Tatsu-nii points towards me."
        ta "「Look Shun, [fn]'s there. 」"
        su "「Fuwah...[fn]-san. 」"
        "Totter totter totter. {p}Going the way Tatsu-nii pointed,\nShun-kun draws a loose curve up to me."
        "As I expected, his steps deviate to the right."
        
        show su 006 spinning at center with dis
    
        su "「Hau, the world is spinning. 」"
        
        show su at move_offright(1)
    
        fn "「Shun-kun, this way, this way! 」"
        
        hide su
        show ta 002 at offright
    
        "This is dangerous!{p}I rush through the gate and grab Shun-kun's arm\nbefore he charges into some bushes."
        
        play music pops_004 fadein 1
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        
        fn "「You alright? 」"
        su "「Hoheh,{w} [fn]-san is spinning too. 」"
        fn "「Shun-kun, what was Tatsu-nii doing to you? 」"
        
        show ta at move_midright(0.25)
        pause .25
    
        ta "「Hey! Do you want to be a living top too!? 」"
        "What?"
        fn "「A living top? 」"
    
        show ta at jump_up
        show su 006 at offright
    
        ta "「It's a challenge to see how many rotations\n\ \ a person can take, an honored New Year's event! 」"
        "...spinning a top for competition isn't\nabout how many times it goes around."
        "Doing that under this midsummer sunlight? {p}He's brimming with energy above all else.{w} {nw}"
        show su at move_midright(0.5) behind ta
        extend "{w=.6}{nw}"
        show su at move_midleft(0.75) 
    
        su "「Fuwah, the spinning is getting slower. 」"   
        ta "「Good, you're making a speedy recovery!\n\ \ Now then, it's your turn. {nw}"
        show ta at jump_up
        extend "Get over here [fn]! 」"
        fn "「I'm fine... I'll stick\n\ \ to keeping an eye on Shun-kun. 」"
        su "「I'll stay here, hanyaruun. 」"
        
        scene black with dis
        pause 1
        
        scene old_house1
        show ta 002 at midright
        show su 003 at midleft
        with dis
    
        ta "「Alright! Nice one Shun! That's a new record!\n\ \ We're a shoe in for the next tournament! 」"
        su "「{cps=10}Hawahafuru... Funururururu 」"
        "Tournament!?\nWhat did you say?!\n...Shun-kun is lurching around cutely."
        ta "「The National Carpenters\n\ \ Competitive Living Top Tournament!{p}\ \ Shun and I are entering next year! 」"
        "Tatsu-nii thrusts his arm up in a triumphant pose.{p}Shun-kun makes a lovely contrast by staggering\naround in the summer sunlight."
        fn "「But isn't it only for carpenters? 」"
        
        show ta 003 at jump_up
    
        ta "「...Haah! That's right!{p}\ \ Shun,{w=.2} become an apprentice at my house right now! 」"
    
        show su at shake_side
        
        su "「{cps=10}Hafuu, Don't... shake me... so much... Auu. 」"
        fn "「T-{w=.2}Tatsu-nii,{w} you shouldn't grab\n\ \ and shake his shoulders like that. 」"
        
        scene black with dis
        
        scene old_house1
        show ta 002 at midright
        show su 001 at midleft
        with dis
        
        jump shun13_carpenters
    
    ################################################
    label shun13_alone:

        $ event_name = "I shouldn't disturb them..."

        stop music fadeout 1.5
    
        "I don't know what they're doing,\nbut I shouldn't disturb them."
        play music free0421
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
    
        su "「N-{w=.2}no, Tatsuki-san! 」"
        ta "「You'll be fine, {p}\ \ I did it 5 times a day when I was around your height! 」"
        "I have...{w} no idea what they're doing."
        su "「P-{w=.2}please put me down already, hau, yah...\n\ \ {cps=10}{cps=+20}FWAAAAH! 」"
        ta "「Hmm?{w=.2} That as far as you can go?{p}\ \ Here. 」"
        "What...?"
        su "「Hwah, I'm dizzy,{w} I can't walk. 」"
        ta "「Gahahahaha! You gotta get used to it. 」"
        ta "「Come over to my place next time,\n\ \ I'll get everybody there to spin you real good!{p}\ \ ...alright, 1 more time. 」"
    
        menu:
            "A. UWAAAAH!":
                jump shun13_surprise
            "B. ...I'm going home":
                jump shun13_gohome
    
    ################################################
    label shun13_gohome:

        $ event_name = "From the Middle of the Day"

        play music cicada01 fadein 2
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
    
        "I didn't know they were that close.{p}\ \ ...I'm going home."
        
        jump end13
    
    ###############################################
    label shun13_surprise:

        $ event_name = "Chasing"
        $ love_shun -= 1
        $ love_tatsuki -= 1

        play music oo39_cho_ys001
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        show su 001 at offright
        show ta 001 at offright
    
        fn "{size=+20}「UWAAAAH! 」"
    
        show ta at move_midleft(0.25)
        show su at move_midright(0.25)
    
        su "「Wa- waah? 」"
        ta "「、[fn]！？ 」" #!# [emb exp= f.fname.charAt(0)]#Need to figure out how to pull first letter of inputted name
        
        stop music fadeout 1
    
        "Both of them seem to be very surprised by my voice.{p}Probably because of that, they don't approach me.{p}If that's the case, I'll go after them!"
        
        play music free0531
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
    
        fn "{size=80}「UWAAAAH! 」"
        "Chase them.{w} Chase them. {p}I'm not thinking about anything,\njust intent on pursuing them."
        
        show su 003 with dis
        show ta 004 with dis
    
        ta "「R-run away, Shun!{w} I don't really understand why,\n\ \ but he's in a strange state of mind right now! 」"
        su "「Waaan, [fn]-san, you're scaring me! 」"
        
        stop music fadeout .4
        show su at move_offleft(0.25)
        show ta at move_offleft(0.25)
    
        "{cps=10}And then we enjoyed chasing each other\nuntil the sun went down.{cps=40}"
    
        jump end13
    
    ###############################################
    label shun13_carpenters:

        $ event_name = "The Carpenters of Minasato"

        play music pops_003 fadein 1
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")        
    
        su "「Hawah, I'm still a little dizzy. 」"
        fn "「Tatsu-nii, you went too far. 」"
        ta "「Err... I'm sorry, I'm sorry! 」"
        "He takes a break from his training\nfor New Year's Day."
        "Then we sit on the porch with some\nbarley tea and enjoy the cool breeze. {p}A classic way to pass time in summer."
        fn "「This porch sure is long, isn't it? 」"
    
        show su 002 with dis
        
        su "「It is. Cleaning it is kind of hard... 」"
        "It's a shame that I'm sitting looking small\nand quiet on the end of 3 people."
        "Not to be outdone by the dignity\nof the large garden with a pond, lanterns,\nand pine trees, I spread out horizontally."
        "Come to think of it,\ndespite Tatsu-nii's huge physique as he sits,\nthe ceiling looks really high."
    
        show su 001 with dis
        
        su "「[fn]-san? 」"
    
        show ta 001 with dis
        
        ta "「What's the matter? 」"
        fn "「Oh, well. 」"
        "They noticed me looking around restlessly."
        fn "「Umm, I was thinking about how big \n\ \ your grandfather's house is, Shun-kun. 」"
    
        show su 002 at jump_up
    
        su "「Hehe♪ The Carpenters of Minasato\n\ \ built it for him. 」"
        fn "「Oh, really?{w=.2} That means Tatsu-nii did it? 」"
        ta "「No, it wasn't the Midoriya Group.{p}\ \ I specialize in shrines. 」"
        ta "「They're not in the village anymore.{p}\ \ They're an old acquaintance of my family. 」"
        su "「The master at the time was introduced\n\ \ to my grandfather's grandfather's\n\ \ grandfather's grandfather. 」"
        fn "「E-err, say that again please. 」"
        su "「It's a story of the Kodori family and the\n\ \ Minasato Group from 8 generations ago. 」"
        ta "「Their way of constructing was different from ours. 」"
        ta "「They just had long-lasting techniques and care\nover the particulars.{w} After all, that was\n\ \ the spirit of the Carpenters of Minasato. 」"
        "Ooh, Tatsu-nii has an unusually serious expression."
        "The apprentice gazes in awe at the pillars and beams.{p}Then that expression seems to change\nto pride in his occupation."
        fn "「Really? That's amazing.{p}\ \ It won't budge for 100 or even 200 years. 」"
        ta "「I know, I'll teach you all about\n\ \ the greatness of the Carpenters of Minasato! 」"
        fn "「Huh? 」"
        
        show ta 004 with dis
        play sound jap_002
        
        ta "「First!{w=.2} No matter who gets on the roof\n\ \ of their buildings, it'll never break! 」"
        su "「Woah! Is that true? 」"
    
        show ta 002 with dis
        
        ta "「Yep! Dragons, bears, \n\ \ and elephants are all safe! 」"
        "I think that's going a bit too far, but Shun-kun\nis looking at Tatsu-nii with twinkling eyes,{p}so being a wet blanket would be the same."
    
        show ta 001 with dis
        
        ta "「Hmm? [fn], you don't believe me? 」"
        fn "「Not necessarily,\n\ \ but no matter which way you cut it,\n\ \ you're exaggerating. 」"
    
        show ta 002 with dis
        
        ta "「Alright then, let's test it out! {p}\ \ Shun, go get the ladder behind the storeroom! 」"
        su "「Okay♪{w} {nw}"
        show su 004 with dis
        extend "Wait, are we climbing it? 」"
    
        show ta 004 at jump_up
    
        ta "「Yes! The dignity of the Carpenters of Minasato\n\ \ has been questioned, I'll show you exact proof! 」"
        
        scene black with Dissolve(.5)
        stop music fadeout 1
        play sound hit51
        pause .5
        play sound step06
        pause .5
        play sound step06
        pause .5
        play sound step06
        pause .5
        play sound step06
        pause 1

        $ event_name = "The Blue Sky, and the 3 in It"

        play music free02
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
    
        scene sky
        show ta 002 at midright
        show su 002 at midleft
        with Dissolve(1)
    
        "Just as he said, Shun-kun, Tatsu-nii,\nand I are standing side-by-side on the slightly\nsloping roof, viewing the distant blue sky."
        ta "「Ooh, nice view! 」"
        su "「[fn]-san! I can see the outside field! 」"
        "The field that spreads outside the premises\nis surrounded by high walls.{p}The road I took looks quite different from here."
    
        show ta at jump_up
    
        ta "「Just as I thought, high places are great! 」"
        su "「Woah! I can even kind of see the school! 」"
        "Tatsu-nii crosses his arms and nods in satisfaction.{p}Shun-kun is unable to hide his astonishment\nat the sight stretching out.{w} Yeah, yeah."
        "With the way things are going, they're going to\nforget our original purpose for being up here..."
    
        show ta 004 at jump_up
    
        ta "「Okay! Now [fn], watch. 」"
        "Tatsu-nii takes a deep breath,\nthen gently hops up with both legs."
        
        stop music fadeout .7
        play sound bosu31
        show ta at jump_up
        show sky at vshake
        pause .3
        show sky at vshake
        pause .3
        show sky at vshake
        pause .3
        show sky at vshake
        
        show su 004 at jump_up
    
        su "「Hyan! 」"
        
        show ta 002 with dis
        
        ta "「See, it's completely safe. 」"
        fn "「Y-{w=.2}Yeah, I get it,{w=.2}\n\ \ so let's stop already Tatsu-nii... 」"
        ta "「Nah, you don't sound convinced,\n\ \ so I'll do it until I'm satisfied. 」"
        "Tatsu-nii isn't satisfied!?"
        
        play sound bosu31
        show ta at jump_up
        show sky at vshake
        pause .3
        show sky at vshake
        pause .3
        show sky at vshake
        pause .3
        show sky at vshake
        pause .2
        play sound bosu31
        show ta at jump_up
        show sky at vshake
        pause .3
        show sky at vshake
        pause .3
        show sky at vshake
        pause .3
        show sky at vshake
    
        "He keeps repeatedly jumping.\nUwaaah, it's shaking beneath my feet...\nI immediately get down."
        
        scene sky with wipe_right
    
        su "「Hawawaah, I'm shaking. 」"
        
        play sound bosu26_b
        show sky at vshake
        pause .3
        show sky at vshake
        pause .3
        show sky at vshake
        pause .3
        show sky at vshake
        
        "When I look over, Shun-kun is also on all fours\nand is somehow keeping his balance. {p}B-{w=.2}but..."
    
        play sound bosu26_b
        show sky at vshake
        pause .3
        show sky at vshake
        pause .3
        show sky at vshake
        pause .3
        show sky at vshake
    
        "Shun-kun's body is so light that\nwhenever it shakes, he flies up.{p}{nw}"
        play music free27
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        extend "...he's getting closer to the edge of the roof!"
        
        play sound bosu26_b
        show sky at vshake
        pause .3
        show sky at vshake
        pause .3
        show sky at vshake
        pause .3
        show sky at vshake
        
        show su 004 at center with wipe_right
    
        su "{size=+20}「WAH,{w=.3} WAAAH! 」"
        fn "「Shun-kun! 」"
    
        play sound hit82
    
        "I catch his hand. {p}Whew, a little more and he would've fell."
        
        show su at shivering
    
        su "「Woof,{w=.2} thank you [fn]-san,\n\ \ that was scary, hauuuu. 」"
    
        play sound bosu26_b
        show sky at vshake
        pause .3
        show sky at vshake
        pause .3
        show sky at vshake
        pause .3
        show sky at vshake
    
        fn "「Thank goodness, Shun-kun... {p}\ \ Now I'll stop Tatsu-nii. 」"
    
        play sound bosu26_b
        show sky at vshake
        pause .3
        show sky at vshake
        pause .3
        show sky at vshake
        pause .3
        show sky at vshake
        
        hide su
        show ta 002 at center
        with wipe_right
        
        fn "「T-{w=.3}Tatsu-nii! Tatsu-nii, come on! 」"
    
        show ta at jump_up
    
        ta "「Heey hey hey♪ 」"
        fn "「Tatsu-niiii! 」"
    
        show ta 001 with dis
    
        ta "「Aah? 」"
    
        play sound bosu26_b
        show sky at vshake
        pause .3
        show sky at vshake
        pause .3
        show sky at vshake
        pause .3
        show sky at vshake
    
        fn "「W-waah? 」"
        "O-{w=.3}oh crap! I lost my balance! {p}I'm falling!"
        su "「[fn]-san! 」"
        
        scene black with wipe_right
        play sound bosu31
        stop music
    
        "My body is thrown into the air. {p}Woah, the scenery is really in slow-motion..."
        "Then, I close my eyes tight to brace myself\nfor the imminent pain."
        "..."
        "Huh? Huuh? {p}I'm not feeling any pain."
    
        #[EV file=大丈夫か？1 normal] #!#Don't know what this does at the moment
    
        ta "「...you alright? 」"
        su "「Ah-{w=.3} [fn]-san... 」"
        fn "「Ah. 」"
        "I look up and see Tatsu-nii's face. {p}Right when I was about to fall,\nhe caught both of my hands and saved me."
        ta "「Now, I'll pull you up. {p}\ \ {cps=10}{size=+20}...UuuooOOOHH. 」"  #!#[EV file=大丈夫か？2 normal] #Again... need to figure out what this is
        "With a spirited roar,\nhe lifts my body up perpendicularly."
        "Laying on his stomach, Tatsu-nii stretches out\nthe muscles on his arms."
        "Even though he didn't prepare his stance...\nhe's amazing."
        ta "{size=+20}「OOOOOOOH! 」"
        "He pulls me up to my elbows, {p}then I'm somehow able to crawl up on my own."
        
        scene sky
        show ta 001 at center
        show su 001 at farright
        with dis #!# check
        
        play music piano2_015 fadein 1.5
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
    
        fn "「Th-thank you, Tatsu-nii. 」"
        "Tatsu-nii gets up too, then sits\non one knee next to me."
        ta "「What, this was... originally my fault. 」"
        
        stop music fadeout 1
    
        "Err... {p}Yeah, he's right,\nthis was originally his fault, wasn't it!?"
        
        play music free44
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
    
        fn "「That's right!{w=.2}{p}\ \ This was originally your fault, wasn't it!? 」"
    
        show su 003 with dis
        
        su "「[fn]-saaan, you're okaaay, *sniffle* 」"
        "Shun-kun has already begun to sniffle."
        fn "「You overdid it! 」"
    
        show ta 005 with dis
        
        ta "「I-{w=.2}I went through all that trouble\n\ \ to save you, didn't I? 」"
        fn "「You shouldn't have been doing that to begin with! 」"
        
        play sound crash21
    
        "Thump"
        
        show ta 003 at move_offleft(1.5)
    
        su "「Ah. 」"
        fn "「Ah. 」"
        ta "「Ah? 」"
        
        hide ta with dis
        
        play sound bosu27
        #!#Shake screen for about one second
    
        "Receiving the excess force of my body blow,\nTatsu-nii falls from the roof."
        
        scene old_house1 with wipe_up
    
        su "「Tatsuki-san! 」"
        fn "「Tatsu-nii! 」"
        "Uooh, he fell off! {p}We immediately look down."
    
        #!#[辰樹 ガクガク]
    
        ta "「{cps=10}...uu{w=.3}, uoh. 」"
        su "「Tatsuki-saaan! 」"
        fn "「A-are you alright!? I'm sorry. 」"
    
        show ta 004 with dis
        
        ta "「Hitting me with a single blow... {p}\ \ Not bad, [fn]! 」"
        "Huh?"
        "Even though his body sunk into the ground,\nit didn't have any effect? {p}He's turning his shoulder?"
        
        show ta 002 at jump_up
    
        ta "「Now get down here! Game on, [fn]! 」"
    
        scene sky
        show su 002 at center
        with wipe_down
    
        su "「...that's good, Tatsuki-san is safe too. 」"
        "Shun-kun gives a sigh of relief."
        fn "「It seems I've become dangerous\n\ \ after what happened,{w} hahahahaha... 」"
        "Then, while being watched by Shun-kun,\nI was harassed by Tatsu-nii until the sun set."
        
        jump end13
    
#######################################################
label tatsuki13:

    $ event_name = "Teacher and Field Work"
    $ love_tatsuki += 1
    $ focus_character = "tatsuki"

    scene map
    hide screen school13
    play music rainfall fadein 8
    call rain_set from _call_rain_set_2
    scene school01 
    show over black
    show raining
    with wipe_corner

    "Sigh... It's been raining since morning...{p}The forecast said it's going to rain all day."
    "Botan-sensei called us today, of all days,\nto meet at school.{p}Just what are we doing?"
    fn "「Good morning. 」"
    
    show bo 001 at center behind raining with dis

    bo "「Morning, you're here bright and early.{p}\ \ Well, there's no need to be so stiff. Relax. 」"
    
    $ encounter_botan = True
    
    "As I entered the staffroom,\nI met my old teacher, Botan-sensei\n(On that note, the only teacher in the village)."
    "He's only a teacher when he's working, though."
    "Since it's Summer vacation at the moment,\nBotan-sensei's the only one here.\nEven the principal isn't around."
    fn "「Sensei, how come you called me into school today?{p}\ \ I haven't been up to any mischief or anything. 」"
    
    show bo 002 with dis

    bo "「Hahaha, you and Ooshima both got up to so many\n\ \ things, and caused so much trouble for us.{p}\ \ That was cute."
    bo "「It's not just you that I called today, though.{p}\ \ I arranged for others to come by, but... 」"
    
    show bo 001 with dis

    bo "「Oh, it looks like they're here now. 」"
    
    hide bo with wipeleft
    show ky 001 behind raining at farright
    show ta 001 behind raining at farleft
    show to 001 behind raining at center
    with wipeleft

    ky "「Good morning. 」"
    
    show to 002 with dis

    to "「Yo, Sensei! 」"
    ta "「Hmm? You came too, [fn]? 」"
    fn "「Morning! You guys got called too, then? 」"
    
    scene school01 
    show over black
    call rain_set from _call_rain_set_3
    show raining
    with wipe_right
    show bo 002 behind raining at center with wipeleft

    bo "「Right, everyone's here. Let's go, then. 」"
    fn "「Go...? Go where? 」"
    
    show bo 001 with dis

    bo "「Oh yes, I haven't told you yet, [ln].{p}\ \ We're going to one of my farmer acquaintances,\n\ \ and we should have enough people to help now. 」"
    bo "「They need assistance with some physical work,\n\ \ so they needed some strong guys to help. 」"
    "I see, that's why these guys are here.{p}Two are in sports clubs,\nand then there's Tatsu-nii..."
    "Wait, how did I end up getting called?"
    fn "「Why was I called over? 」"
    
    show bo 002 with dis

    bo "「Because you had the most free time. 」"
    bo "「And, after being in the city for so long,\n\ \ I thought you'd appreciate the countryside. 」"
    bo "「Juuichi can still do judo when it's raining,\n\ \ and isn't Kouya a little far away?{p}\ \ That's why you're the fourth one here. 」"
    "Urgh... I suppose it's true I'm free every day.{p}Of all of us, I'm the most available."
    bo "「We'll take a car over. Time to go. 」"
    "So we'll be working in the rain.{p}Man, what a drag..."
    
    hide bo with Dissolve(.6)
    scene black with Dissolve(1)
    play music free0211
    call rain_set from _call_rain_set_4    
    scene old_house1
    show over black
    show raining
    with Dissolve(.5)
    
    farmer "「Thanks, Sensei. You've finally come.{p}\ \ I'm counting on you, everyone. 」"
    
    show bo 002 at center behind raining with dis

    bo "「No no, no need for thanks.{p}\ \ It's good exercise for these guys, anyway.{p}\ \ Okay everyone. Listen carefully, and work hard. 」"
    everyone "「Yes, Sensei! 」"
    farmer "「Everyone has so much energy...{p}\ \ I have high hopes for you all. 」"
    "Mister, why do you keep looking at me?"
    farmer "「Well, boys, will you help me with the harvest? 」"
    everyone "「Yes. 」"
    farmer "「Uhh, could you pack boxes inside?{p}\ \ Outside work is tough, and it's raining. 」"
    "Uncle, you're treating me as a bonus, aren't you?{p}I suppose that's true, since I was free anyway."
    
    menu:
        "A. I can still do the physical stuff!":
            jump tatsuki13_outside
        "B. Okay, I'll work inside then.":
            jump tatsuki13_inside

    ##########################################
    label tatsuki13_outside:

        $ event_name = "Harvesting Time"
    
        fn "「I can still do the physical stuff. 」"
        "Old man, please don't make fun of me..."
        "In the old days I ran around the fields with\neveryone, and we'd keep going until we dropped.{p}Harvesting surely can't compare to that."
        "Besides, why am I the only one to get something\ndifferent?{p}I can't have that."
        farmer "「Really? Do your best, then. 」"
        fn "「Yes, I'll give it all I've got! 」"
        "Watch as I surpass the old man's expectations!"
        
        hide bo with Dissolve(.5)
        scene field1 
        show over black
        show raining
        with Dissolve(1)
    
        farmer "「To start with, can you do the plowing? 」"
        farmer "「Since there are four of you,\n\ \ you can all take one field each.{p}\ \ We'll have lunch when you finish. 」"
        farmer "「It should only take about that long.{p}\ \ We'll have a break after lunch, and then you'll\n\ \ do something else on the opposite fields. 」"
        "Hey, wait a sec. This whole area is fields.{p}The opposite fields look\nlike they're at the horizon..."
        
        show ta 001 at farleft behind raining
        show ky 001 at center behind raining
        show to 001 at farright behind raining
        with wipeleft
    
        ky "「Well, shall we get started? 」"
        to "「What a pain... Guess we just have to do it. 」"
        ta "「They're bigger than I thought.\n\ \ Let's get this done quickly. 」"
        
        hide ta
        hide ky
        hide to
        with wipe_right
        
        "Wait, what... You guys are treating this\nlike this is nothing."
        "Oh right, I've become to used to the city life,\nand I forgot how stupidly huge these fields are."
        "Maybe I should've gone with packing boxes...{p}No, I am also a man.{w} Tell me to do it,\nand I will.{w} {nw}"
        play sound freeze04 
        extend " I'll plough the hell out of this thing!"
        fn "「Hey, why don't we make this a competition?{p}\ \ Last one done treats the others to juice. 」"
    
        show to 002 at center behind raining with wipeleft
    
        to "「Oh, you're in a good mood, [fn]. 」"
        
        show ta 002 at farleft behind to with wipeleft
    
        ta "「Interesting. I won't lose. 」"
        
        show ky 001 at farright behind ta with wipeleft
    
        ky "「Sounds good, but won't it be tiring?{p}\ \ The fields are pretty big. 」"
        fn "「I'll be okay.{w} I'm gonna finish first! 」"
    
        show to 003 with dis
        
        to "「All right, let's do this! 」"
        
        hide to with wipe_right
        show ta 004 with dis
    
        ta "「Come on, let's get fired up! 」"
    
        hide ta with wipe_right
        
        ky "「Is this really going to be okay...? 」"
        
        hide ky with wipe_right
        
        "..."
        
        scene black with sdis
    
        "I totally saw it coming,\nbut I lost by a huge margin.{w} In the end,\nI even had to get the others to help out a bit..."
        
        jump tatsuki13_rest

    ############################################    
    label tatsuki13_inside:
        
        $ event_name = "Light Work"

        scene black with Dissolve(.5)
        scene farmhouse_in with Dissolve(1)
    
        ow "「Young man, can you help us\n\ \ with packing these boxes here? 」"
        fn "「Of course. I look forward to working with you. 」"
        ow "「Well then, we'll be filling the boxes with\n\ \ vegetables. When the boxes are full,\n\ \ put them over there, please. 」"
        fn "「Okay, I understand. 」"
        "This is simple enough that even I can do it.{p}It sucks that everyone else is working in the rain.{p}I wonder if I'm good enough to work out there?"
        ow "「Are you a student? 」"
        fn "「Yes, I am.{p}\ \ I grew up here, but we moved,\n\ \ and now I live in the city. 」"
        ow "「Oh, I see. So you're only here for the Summer. 」"
        fn "「Well, yeah... 」"
        farmer "「Son, that one's not full yet, so don't move it. 」"
        fn "「Oh, I'm sorry. 」"
        ow "「Is that so. You must be having fun, then.{p}\ \ It's been so long since you've seen your friends,\n\ \ and I've never left this area. 」"
        
        show bo 001 at center with dis
    
        bo "「[fn], bring me that box over there. 」"
        fn "「Here you go. 」"
        ow "「Oh, move this one too, please? 」"
        fn "「Coming. 」"
        farmer "「This one's done too. 」"
        bo "「[fn], is this box done? 」"
        ow "「Young man. 」"
        farmer "「Young man. 」"
        bo "「[fn]. 」"
        "T-{w=.2}this is..."
        "What do I dooo...?"
        
        scene black with dis
    
        "Several hours later..."
        
        scene farmhouse_in with circle_out
    
        "Whew, I was wondering how I was going to manage,\nbut I got used to it pretty quickly.{p}I did pretty well, if I say so myself."
    
        show bo 001 at center with dis
        
        "「Hey, [fn].{w} There's still more,\nso don't slow down there. 」"
        "...*sniff* I really am not cut out for this.{p}Let's do our best...{w} This isn't fun.\nMaybe I should've worked with everyone else?"
        
        jump tatsuki13_rest
    
    ##############################################
    label tatsuki13_rest:

        $ event_name = "Back to work"

        scene old_house1 
        show over black
        show raining
        with Dissolve(1)
        
        farmer "「Have you rested enough?{p}\ \ You'll need your strength back,\n\ \ or we won't be done by nightfall. 」"
        fn "「Yes, I'm much better now. 」"
        "Man, I'm so full."
        "The farmer's wife kept saying 'Eat, eat!\nNo need to hold back, eat as much as you like!'"
        "So of course I asked for seconds.\nI almost fell asleep after lunch..."
        farmer "「There's still more work to do in the afternoon,{p}\ \ So do your best. I know your sensei will say it,\n\ \ but I'm counting on you boys. 」"
        
        show bo 001 at center behind raining with dis
    
        bo "「Got that? 」"
        bo "「We're picking vegetables next.\n\ \ Just pick them, then carry them to that hut.{p}\ \ There's other work that gets done there. 」"
    
        show bo 002 with dis
        
        bo "「I won't bore you with the details, so get to it. 」"
        hide bo with wipe_right
        show ky 001 at center behind raining with wipe_right
    
        ky "「So what should we do...? 」"
        ky "「This should be simple enough.\n\ \ If we split into two groups,\n\ \ one gathering, one carrying. Right? 」"
        
        show ky at farleft
        show to 001 at center behind raining  
        with wipe_right
    
        to "「Sounds good. 」"
        
        show ta 008 at farright behind to with wipe_right
    
        ta "「No, wait a minute.\n\ \ About that... 」"
    
        show ta 001 with dis
        
        ta "「If we split up like that, our efficiency drops.{p}\ \ The pickers will probably work faster than the\n\ \ carriers, and then they'd have nothing to do. 」"
        
        show ta 002 with dis
    
        ta "「I think it'd be better if we all gather vegetables,\n\ \ then put them on the cart.\n\ \ We can carry all of them over after that. 」"
        fn "「I see. That's just like a craftsman,{p}\ \ using your head at times like these. 」"
        ta "「Hehehe, I guess. 」"
        
        show to 003 with dis
    
        to "「What? Tatsu-nii's no craftsman.\n\ \ He's still an apprentice. 」"
        
        show ta 004 with dis
    
        ta "「Say that again. 」"
        ta "「If you think so,\n\ \ why don't you sign up as an apprentice, too? 」"
        ky "「Now, stop fighting please, you two.{p}\ \ Not even a dog would get in the way of a\n\ \ lovers' quarrel. 」"
        
        show to 007
        show ta 008
        with dis
        
        tato "（...Dog?）"
        fn "「Yeah, it's definitely a cockfight,\n\ \ no matter how I look at it. 」"
    
        show ta 010 with dis
    
        ta "「Hey, [fn]...! 」"
        
        show to 003 with dis
    
        to "「That's harsh. You didn't need to go that far. 」"
        fn "「Hehe. Sorry. 」"
        "Ahh, when these three get together...\nIt always feels like this."
        "Tatsu-nii and Torahiko are always together,\nand they get on surprisingly well with Kyouji-senpai.{p}These guys would probably rock together at soccer."
        "And, if Torahiko were to pull something,\nTatsu-nii and I would get caught up in it,\nand Kyouji-senpai would try hard to stop us."
        "Same as always..."
        ky "「Well then, let's start. 」"
        fn "「Man, it's still raining. Are we gonna work like\n\ \ this all day? If it does clear up, though, it'll\n\ \ be hot as hell, so maybe it's not that bad. 」"
        to "「Yeah, it is. 」"
        
        show to 007 with dis
    
        to "「You'd be fine, even if you got wet in a raincoat,\n\ \ but do you know how heavy wet fur is?{p}\ \ Drying that out is a real pain in the ass. 」"
        ky "「That's true. It's a real pain when it's wet.{p}\ \ Plus, rain means no soccer. 」"
        
        show ta 007 with dis
    
        ta "「I'm glad it's raining.{p}\ \ It's better when there's some moisture in the air,\n\ \ and isn't it more relaxing when it's raining? 」"
        fn "「Hmm, I see what you mean about it being calming.{p}\ \ Still, rain on a day like this bothers me a bit... 」"
        ky "「That's funny... didn't you say this was all right\n\ \ just a minute ago? 」"
        
        show to 002 with dis
    
        to "「Yeah, he totally did. So which is it, [fn]? 」"
        fn "「Hmm... I don't like working in the rain,\n\ \ but it'll be bad if it clears up...{p}\ \ Wait, hmm... 」"
        
        show ta 008 with dis
        
        ta "「So, basically, the weather doesn't matter,\n\ \ to hell with manual labour. 」"
        fn "「Hwah?! 」"
        
        show to 010 with dis
    
        to "「Heh.\n\ \ Seems you got all soft and weak from\n\ \ living in the city. 」"
        fn "「You've changed too much, Torahiko.\n\ \ Did you make a deal with the Devil or something? 」"
        ky "「I don't think I've ever\n\ \ seen Ooshima as being small. 」"
        
        show ta 002 with dis
    
        ta "「If you ask me, you guys have always been small.{p}\ \ Gahaha! 」"
        
        show to 007 with dis
    
        to "「You're just too freaking big, Tatsu-nii.{p}\ \ You're the reason we have XXXL sizes... 」"
    
        show ta 001 with dis
        
        ta "「Nah, those are a bit too restrictive.\n\ \ Can't wear them. 」"
        "Then what size do you usually wear?"
        
        play music rainfall fadein 1
        scene black with wipeleft
        call rain_set from _call_rain_set_5
        scene field1
        show over black
        show raining
        with wipeleft
    
        fn "「Somehow, we're almost done. 」"
        
        show ta 001 at midright behind raining with dis
    
        ta "「Yep. We'll be done after we move this last one. 」"
        "As we worked, we talked less,\nand our concentration on the task increased."
        "The work went by quickly after that,\nand it became easy for us to handle."
        
        show to 002 at center behind raining with dis
    
        to "「All right, this will be the last lot.{p}\ \ No matter what anyone else says, we're done. 」"
        
        show ky 001 behind ta at farleft with wipeleft
    
        ky "「Yeah, I think we're done here.{p}\ \ Ooshima, can you give me a hand taking it in? 」"
        "Whew, it's finally over.{p}Today was so long...{p}We can go home after this."
        
        scene black with sdis
        scene field1
        show over black
        show ta 006 at center
        show raining
        with Dissolve(.5)
    
        ta "「Those guys are taking ages.\n\ \ What are they doing over there? 」"
        fn "「Hmm, looks like they stopped...{p}\ \ I wonder why?{p}\ \ We should go check it out. 」"
    
        scene field2
        show over black
        show ky 001 at midleft
        show to 007 at midright
        show raining
        with wipe_right
    
        ky "「Oh boy... 」"
        fn "「Kyouji-senpai, is something wrong?\n\ \ It looked like you guys were having some trouble. 」"
        ky "「Yeah, there is.{w} Take a look. 」"
        fn "「Whoa, what is this? 」"
        
        show ta 002 at center behind ky with dis
    
        ta "「It's amazing...{p}\ \ Maybe you could swim across?{p}\ \ Gahahahaha! 」"
        "So many people must have passed by on the\nrice field roads,\nthat a giant puddle had formed in the middle."
        "The road was completely underwater,\nand the puddle spread across the whole field."
        to "「This isn't a puddle, this is a small lake.{p}\ \ What's more, the road's uneven now. 」"
        to "「I mean, it totally looks like a cave is right\n\ \ underneath the surface. 」"
        
        show ta 001 with dis
    
        ta "「Well, it is big, but it's still just a puddle.\n\ \ It can't be that deep. 」"
        ta "「It might be a problem for only one or two people,\n\ \ But with the four of us,\n\ \ we should be able to do something, right? 」"
        ky "「It doesn't seem like there's any way around it.{p}\ \ I don't think it's a good idea\n\ \ to force your way through, though. 」"
        
        show to 003 with dis
    
        to "「When it comes to brute strength,\n\ \ it's Tatsu-nii's time to shine.{p}\ \ You can do something, right? 」"
        
        show ta 008 with dis
    
        ta "「Hey, it's not like I can whip\n\ \ something up just like that.{p}\ \ I dunno what to do. 」"
        
        show to 002 with dis
    
        to "「With your strength, you could probably just\n\ \ walk straight through.{w} It's not like anything\n\ \ will be a bother to you, so it should be fine. 」"
        ky "「Ooshima, isn't that a bit unreasonable...?{p}\ \ [fn], what do you think? 」"
        fn "「I... 」"
        
        menu:
            "A. Leave it to Tatsu-nii":
                jump tatsuki13_tatsuki
            "B. Get Kyouji's opinion":
                jump tatsuki13_kyouji
            "C. Go along with Torahiko":
                jump tatsuki13_torahiko
    
    ################################################
    label tatsuki13_tatsuki:

        $ event_name = "Teamwork"
    
        fn "「Uhh... 」"
        
        play music free0470
        show ta 004 with dis
    
        ta "「Hey, why do you think all four of us are here?{p}\ \ If we work together, nothing will be a problem. 」"
        "Before I could answer, Tatsu-nii started talking."
        
        show to 001 with dis
    
        to "「I guess. It's impossible for one person,\n\ \ but four people should be able to do it.\n\ \ Nothing should be able to stand in our way. 」"
        ky "「Wait, are you getting scared?{p}\ \ Nothing's impossible, if we cooperate. 」"
        "Right. If we all make an effort,\nwe can do anything."
        
        show to 006 with dis
    
        to "「That said, how are we going to cross this? 」"
        fn "「Well... Maybe we should just go straight through,\n\ \ after all? 」"
        
        show ta 002 with dis
    
        ta "「Sounds good. We'll take positions, then go.\n\ \ The rest will work out, somehow. 」"
        "Tatsu-nii took the middle,\nand we all gathered around.{p}He's so dependable at times like this."
    
        show to ray 01 with dis
    
        to "「When the chips are down, Tatsu-nii's so dependable{p}\ \ Go, craftsman! 」"
    
        show ta 008 with dis
        
        ta "「Hey... Back when we started working,\n\ \ didn't you say I was just an apprentice? 」"
        
        hide to at center
        show to 006 at midright
        with dis
    
        to "「Did I? 」"
        fn "「I think I heard something like that. 」"
        
        show to 008 with dis
    
        to "「Weird, I don't remember anything like that... 」"
        ky "「Anyway, let's give this a shot. 」"
        
        scene black with sdis
        scene field1
        show over black 
        show ta 001 at center
        show raining
        with dis
    
        ta "「I'll go in front. Kyouji, Tora,\n\ \ you take the sides.{p}\ \ [fn], bring up the rear. 」"
        fn "「Got it. I'm here, right? 」"
        
        show ky 001 at farleft behind raining with wipe_right
    
        ky "「Let's give it our best, everyone.{w} Ready? 」"
    
        show to 002 at farright behind raining with wipe_right
        
        to "「All set here. 」"
        "Looks like everyone's ready to do their part."
        "All right, with luck, we should be able to do this!"
        
        show ta 002 with dis
    
        ta "「Well then, let's go! 」{nw}"
        show ta at jump_up
        play sound bosu10_c
        extend "{w=.2}"
        "Tatsu-nii yelled out,\nand began advancing with the cart."
        
        show to 001 with dis
    
        to "「Cart wheels are pretty hard to move underwater,\n\ \ but they're not as bad as I thought they'd be. 」"
        ky "「True, but remember that the ground might not\n\ \ be level under the surface.\n\ \ That could be a problem. 」"
        fn "「It's getting harder to move it.\n\ \ Have we reached the center yet? 」"
        "Our footing is getting worse after coming this\nfar through the mud,\nand it's getting harder to advance."
        
        show ta 004 with dis
    
        ta "「Just a little more! Keep going! 」"
        
        play sound bosu34
        show to 008 at jump_up
        pause .2
    
        to "「Right.{w=.2} Wait, what!? 」"
        ky "「Ooshima, what's wrong? 」"
        fn "「Is there a rock, or something...?{p}\ \ It looks like it's stuck on something. 」"
        "Stuck in the rain, no matter how much we tried,\nthe cart wouldn't move.{w} We even tried pulling\nbackwards, but time was the only thing moving."
        
        show ta 001 with dis
    
        ta "「There's no helping it, we're stuck here.{p}\ \ But, if we push with all our strength at the same\n\ \ time, we can overcome anything. 」"
        fn "「Hm, okay.{w} Let's try that, then. 」"
        ky "「Ready?{w} Let's go.{w} One, two... 」"
        
        show ta 004 at jump_up
    
        ta "{size=+15}「Hiyaaaaaah!! 」"
        "We all pushed together at once,\nbut the cart didn't budge."
        fn "「It won't move... 」"
        ta "「Let's try again. 」"
        fn "「Hmm... It feels like something might move,\n\ \ this time. 」"
        ky "「Ooshima!{w} 　It's tilting that way. 」"
    
        show to 003 with dis
        
        to "「Got it, it'll be fine as long as it doesn't\n\ \ go too far, right? 」"
        fn "「Just a little more...! 」"
        ky "「Did it get free? 」"
        
        show to 007 with dis
    
        to "「It's fine. It's not caught on anything now. 」"
        
        show ta 002 with dis
    
        ta "「At this rate, we'll be done in no time. 」"
        
        jump tatsuki13_done
        
    ##############################################
    label tatsuki13_kyouji:

        $ event_name = "Let's take a shortcut!"

        scene field1
        show over black
        show ky 001 at center
        show raining
        with wipe_right
    
        fn "「Kyouji-senpai, what do you think we should do? 」"
        "He is a senior, after all..."
        ky"「I think we'd be better off carrying things\n\ \ separately, rather than forcing our way through. 」"
        
        show ta 008 at farright behind ky with dis
    
        ta "「Well... it's annoying, but we do have time,\n\ \ and we'd certainly get it done that way.{p}\ \ I wanna do this quickly since it's raining, though. 」"
    
        show to 006 at farleft behind raining with dis
    
        to "「It's not like we can do anything about that.{p}\ \ Isn't there a shortcut or something? 」"
        fn "「Isn't this the fastest way through already? 」"
        ky "「Now that you mention it,\n\ \ Ooshima led us this way to begin with...{p}\ \ Let's try taking a different route. 」"
        
        play music free44
        show to 005 at jump_up
        pause .2
    
        fn "「That reminds me. When we came into the fields,\n\ \ wasn't the road wider?\n\ \ It felt like a good path to walk. 」"
        ta "「Oh, Tora... when we were young you'd say 'let's\n\ \ take a shortcut', come to a crazy conclusion and\n\ \ get mad, then go with it anyway. 」"
        ta "「You haven't learned from experience, have you? 」"
        fn "「That's right. Whether it was your own garden,\n\ \ a fence we needed to climb, or even a grass field,\n\ \ you'd ford rivers and climb mountains to avoid it. 」"
        ky "「The ones who followed Torahiko in high spirits\n\ \ were Tatsuki-san and [fn], from memory... 」"
        fn "「Really? 」"
        
        show to 011 with dis
    
        to "「No, I didn't think it'd turn out like this.{p}\ \ Besides, if something did happen,\n\ \ there were the four of us... 」"
        ky "「Well, there's no helping it.\n\ \ Looks like we'll have to double back.{p}\ \ I think it's best we try a different road. 」"
        
        show ta 001 with dis
    
        ta "「With three people, we should be able to handle it,{p}\ \ but we can't do the impossible, I suppose.\n\ \ Later, Tora. 」"
        fn "「If we turn back now, we'll at least get all these\n\ \ in safely.{w} Nice job, Torahiko. 」"
    
        show to 005 with dis
    
        to "「Hey, you two. What are you leaving me alone for? 」"
        ky "「Ooshima, it's fine if they\n\ \ go ahead and take a break. 」"
        
        show to 006 with dis
    
        to "「Aw, geez.{w} Not you too, Kyouji-senpai! 」"
        ky "「Hmph,{w=.2} come help with this thing aready.{p}\ \ Or I really will leave you behind. 」"
        
        hide ky with wipe_right
        show ta 004 with dis
    
        ta "「As punishment for taking a shortcut, you don't\n\ \ get to eat today. 」"
        
        hide ta with wipe_right
    
        fn "「Because you made Mom and Dad angry, right?{p}\ \ Now stand over there and think about what you did.{p}\ \ I'll let you back in once you think it over. 」"
        
        show to 003 with dis
    
        to "「Who're you guys again?{w} Damnit, you'd better\n\ \ remember this. Next time you screw up, I'll be\n\ \ there to laugh at you guys... 」"
        ta "「Isn't the one laughing always the same guy? 」"
        fn "「Ahahahaha! You're lucky Kouya's not here today.{p}\ \ If he were, you'd be getting a verbal thrashing\n\ \ right around now. 」"
        
        show to 005 with dis
    
        to "{size=+15}「DAMNIT!! 」"
        
        jump tatsuki13_done

    ##################################################
    label tatsuki13_torahiko:

        $ event_name = "Power Game"
        $ love_torahiko -= 1
        $ love_tatsuki -= 1
        $ love_kyouji -= 1

        play music free53 fadein 1
    
        fn "「Since you move heavy things every day at work,\n\ \ won't you be fine, Tatsu-nii? 」"
        "It's overkill, maybe, but I agree with Torahiko.{p}Rather than let an amateur butt in, it'd be better\nto leave things to a professional."
        
        show to ray 01 with dis
    
        to "「Right, right.{w} If Tatsu-nii uses his giant body\n\ \ and power, moving this should be no problem. 」"
        
        show ta 007 with dis
    
        ta "「Y-{w=.2}you think?{w} Well, there's nothing I can't do.{p}\ \ {nw}"
        show ta 001 with dis
        extend "So all four of us going together is a bad plan? 」"
        ky "「If we all went together, wouldn't that mean\n\ \ that we can't leave it all to you, Tatsuki-san? 」"
        
        show ta 010 with dis
    
        ta "「Well, no, it's not like I need your help.\n\ \ I think one person should be able to do it alone. 」"
        
        show to 010 at midright with dis
    
        to "「That settles it.{p}\ \ If it's Tatsu-nii, it should be fine.\n\ \ Now let's try that out. 」"
        fn "「When it comes down to it, you get dependable.\n\ \ That's so awesome. 」"
        "If it's Tatsu-nii... if it's up to him...{p}He should be able to do it."
        
        show ta 002 with dis
    
        ta "「No way around it... right, leave it to me.{p}\ \ I'll show you what a real man is. 」"
        ky "「Is this okay...? 」"
        "Tatsu-nii's getting interested in this, and it\nreally looks like he'll be able to do it himself.{p}Too bad we aren't all helping, but oh well."
        
        scene field2
        show over black
        show ky 001 at farleft
        show to 010 at farright
        show ta 004 at center
        show raining
        with explosion
    
        ta "「All right, let's go! Uoooooo! 」"
        
        play sound bosu29
        
        "The cart's moving slowly, but it is moving forward."
        fn "「It moved! 」"
        to "「I believe Tatsu-nii could do anything for us. 」"
        
        stop music fadeout .7
        show ta 002 with dis
    
        ta "「Heheh,{w=.2} This is actually pretty easy.{p}\ \ ...Oh wait, what? 」"
        fn "「Tatsu-nii, look out! 」"
        "Tatsu-nii seems to have stumbled on something,\ntipping him off-balance and making him flail wildly."
    
        play sound bosu26_b
        show ta 003 at jump_up
        pause .2
    
        ta "「Whoa, thisisbad! 」"
        
        hide ta with wipe_down
        play sound bosu31
    
        fn "「That was a really dramatic fall, are you okay? 」"
        
        play music free0205
        show to 005 with dis
        
        to "「Crap! At this rate the cart's gonna tip over!{p}\ \ Umm??{w} 　The cart's gonna fall, because Tatsu-nii\n\ \ fell over??? 」"
        ky "「Ooshima, it's the other way round.{p}\ \ Anyway, we need to do something about that cart. 」"
        "In the moment Tatsu-nii fell over, the cart really\nlurched. It looked like it would topple sideways]nat any moment."
        "The three of us tried our hardest to right it,\nbut even with our best efforts...\nThe cart still tipped over."
        
        show to at jump_up
    
        to "「Crap, it looks like the vegetables\n\ \ are gonna be crushed! 」"
        fn "「I... can't do anymore...{w=.2} I'm at my limit... 」"
        
        show ta 008 at center behind raining with wipe_up_slow
    
        ta "「My bad. Hang on, I'll fix this. 」"
        "The fallen Tatsu-nii got up,\nthen closed his powerful hands on the cart."
        
        play sound bosu34
        pause .4
        show to at jump_up
    
        to "「Tatsu-nii, you're pushing it the wrong waaay!! 」"
        
        play music rainfall fadein 1
        show ta 003 with dis
        play sound crash21
        show field2 at hshake
    
        fn "「Aw, man. It collapsed. 」"
        
        show to 007 with dis
    
        to "「Well, if we wash the vegetables off,\n\ \ they should be all right. 」"
        ky "「It's no use.\n\ \ We're going to have to apologise for this. 」"
        
        show ta 010 with dis
    
        ta "「We came over to help out,\n\ \ but we somehow forgot that along the way... 」"
        "Sigh...{p}This plan really needed more forethought."
        
        scene black with wipe_right
    
        "In the end, we went off to apologise."
        "The farmer was pretty forgiving,\nbut Botan-sensei really gave us an earful.{p}(As the one responsible, Torahiko got it worst.)"
        
        jump end13
    
    ###################################################
    label tatsuki13_done:

        $ event_name = "Rain letting up"

        scene black with Dissolve(1)
        scene old_house1 
        show over black 
        with Dissolve(1)
        play music free0258 fadein 2
    
        fn "「We've finished. 」"
        farmer "「Thank you for your work today.{p}\ \ You've been so much help. The day's almost over,\n\ \ so come on inside and rest. 」"
        fn "「Okay. Good work, everyone. 」"
        "We were all so completely exhausted from work,\nwe accepted his invitation without second thought."
        fn "「Whew, we're finally done.{p}\ \ When we took Torahiko's 'shortcut' at the end,\n\ \ I was wondering how that would turn out. 」"
        
        show to 003 at center with dis
    
        to "「It's not my fault the weather sucks. 」"
        
        show ky 001 at farleft behind to with wipeleft
    
        ky "「Haha. At any rate,\n\ \ it's great that it all ended up with no problems. 」"
        
        show ta 008 at farright behind ky with wipeleft
    
        ta "「Even on a day off I have to do work.{p}\ \ I'm so tired... 」"
        fn "「So even you get tired.{p}\ \ I've got this image of you never getting tired. 」"
        
        show ta 010 with dis
    
        ta "「Of course I get tired, I'm not a machine.{p}\ \ For now I'm okay, but for tomorrow...{p}\ \ Tch.{w=.2} I'm jealous of you guys on Summer vacation. 」"
        ky "「The rain gave me a day off today,\n\ \ but there'll probably be club activities tomorrow.\n\ \ It's probably going to be intense, to make up. 」"
        
        show to 006 with dis
    
        to "「I have club tomorrow, too,\n\ \ so I'm jealous of the people with time to spare. 」"
        fn "「I have to guard my house, and that means\n\ \ patrolling the perimeter. Man, I'm so busy...{p}\ \ Wait,{w=.2} it's not my house. It's Grandpa's. 」"
        
        show to 002 with dis
    
        to "「What the hell is that about? 」"
        everyone "「Hahahahahaha! 」"
        "It doesn't look like we'll be able to hang out\nafter this, we're just all too tired.{p}Plus, it's started to rain again."
        "In any case, I'm glad we're done with helping out.{p}I'm probably gonna be all sore tomorrow..."
        ow "「Thank you so much for everything, boys.{p}\ \ Go take the vegetables into the kitchen to cool,\n\ \ and then make sure to eat as much as you like. 」"
        ky "「Thank you very much.{p}\ \ Sorry for intruding,\n\ \ especially after we came over to help. 」"
        ow "「It's no trouble at all. Now, go on, eat up. 」"
        fn "「Thank you very much... whoa,{w=.2} these look tasty!{p}\ \ Are they okay? They're still soaking. 」"
        "Inside the kitchen sink was a bucket of water.\nInside the bucket were a bunch of tomatoes and\ncucumbers, all floating around."
        "Water was flowing into the bucket from a tap,\nand I was feeling chilled just by looking at it."
        ow "「That water is drawn from a mountain spring, so it\n\ \ never stops flowing.{w} Sometimes it's a little\n\ \ bit dirty, but that's nothing to worry about. 」"
        
        show ta 001 with dis
    
        ta "「They're so good when they're cold. 」"
        "While I was talking with the farmer's wife,\nTatsu-nii stepped over and bit into a tomato."
        ky "「Tatsu-nii, aren't you eating a bit fast...? 」"
        ow "「Now now, don't you worry, boys.\n\ \ Eat fast or it'll all be gone.{w} I need to finish\n\ \ up some things, but go ahead and relax. 」"
        "In that case, I'll have one too."
        "...?!"
        fn "「This tomato is awesome!{p}\ \ It's so sweet, you wouldn't need to pickle it.{p}\ \ Vegetables like this are so delicious! 」"
        
        show ta 002 with dis
    
        ta "「Gahaha! You can't get fresh stuff like this\n\ \ in the city, can you? 」"
        fn "「No, you can't.\n\ \ It's like I'm eating a different food.{p}\ \ Surprising. 」"
        
        show to 010 with dis
    
        to "「It's good, but there're only cucumbers and\n\ \ tomatoes...{w} It'd be nice if there were\n\ \ some other things, too. 」"
        fn "「That would be luxury. I'm fine with just these. 」"
        ky "「Well, there are other vegetables.\n\ \ we could ask to chill some lettuce, or some\n\ \ eggplant, but you can't eat that raw. 」"
    
        show ta 008 with dis
    
        ta "「I kinda feel like watermelon... 」"
        ow "「The watermelon slices are here...! 」"
        "The farmer's wife brought out a bunch of\nwatermelon slices, cut like they would be for the\nObon Festival."
        
        show to ray 01 with dis
    
        to "「Nice timing! 」"
        ta "「Don't mind if I do...! 」"
        "Immediately, Tatsu-nii reached out and grabbed\na slice, biting right into it."
        ky "「Tatsuki-san, you're eating too fast... 」"
        ow "「Big dragon boy, you really can eat.{p}\ \ I'm so happy you came by. 」"
        
        show bo 001 at midleft behind ta with wipe_right
    
        bo "「You guys got a real treat.{p}\ \ Did you save any for me? 」"
        fn "「Ehehe, we already ate it. 」"
        "I'm tired, but doing this once in a while is fine.{p}When I'm working with everyone, it's like I'm a\nkid again, and I have a great time."
        
        scene sky with sdis
    
        ky "「Oh, it looks like the rain is clearing up. 」"
        "Before we knew it, the cloud above started to\nbreak up, and we could see a bit of blue sky\nthrough the gaps."
        to "「Hey, look over there. 」"
        "Torahiko pointed in the direction of the mountain,\nand we all looked over."
        fn "「A rainbow... it's so beautiful. 」"
        fn "「How many years has it been since I've seen a\n\ \ rainbow this big and bright? 」"
        
        scene old_house1
        show ta 002 at center 
        with Dissolve(1)
    
        ta "「It's a great scene...\n\ \ now, since we're done eating,\n\ \ Where are we going now? 」"
        "Tatsu-nii stretched, patted his stomach,\nthen turned around to speak to us."
        fn "「I'm so tired, I can't move.\n\ \ Forgive me...! 」"
        ta "「Lazybones. You coming, Tora? 」"
        
        show to 006 at farright with wipeleft
    
        to "「I'm too tired to move, too.{w} Next time. 」"
        ky "「It's not that you're tired,\n\ \ It's that you don't want to ride in his car,\n\ \ isn't it? 」"
        fn "「I can't move an inch, but it looks like Torahiko\n\ \ still has some energy left. 」"
        
        show to 001 with dis
    
        to "「I really am tired right now.{p}\ \ Even if I wasn't, I still wouldn't want\n\ \ to get in a car with Tatsu-nii driving. 」"
        
        show ta 004 at jump_up
    
        ta "「What was that? 」"
        
        show to 006 with dis
    
        to "「I said, I. {w=.2}Don't. {w=.2}Want. {w=.2}To. {w=.2}Get. {w=.2}Into. {w=.2}Your. {w=.2}Car. 」"
        ta "「Say that again! 」"
        ky "「Tatsuki-san, calm down. 」" 
    
        bo "「You guys are so energetic.\n\ \ It must be good to be young... 」"
        
        jump end13

#######################################################
label end13:
    stop music fadeout 2
    window hide
    show day_logo2 with Dissolve(.5)
    pause .5
    show day_logo with dis
    pause 1
    
    scene end_bg
    show day_logo
    with Dissolve(2)
    pause 3
    scene black with Dissolve(2)
    pause 1
    
    #jump day13
    jump day14
