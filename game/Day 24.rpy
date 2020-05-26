###Day 24
screen hill24:
    hbox:
        add "arrow up"
        at hillbounce1
    hbox:
        add "icon_shun"
        at hillbounce2
    hbox:
        text _("Hill")
        xalign .59 yalign .56
        
screen minasatomap24():
    add "map"
    add "mapdate"
    imagebutton idle "a icon" hover "icon loop"  xpos 440 ypos 100  action Jump("shun24") hovered Show("hill24")  unhovered Hide("hill24") hover_sound "av/audio/click_008.wav" 
    hbox:
        text _("{size=+30}August 24")
        at maptime
        
##############################################
label day24:
    
    $ renpy.music.set_volume(1.0, 0.0, channel = "music")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound2")
    
    $ day = 24
    $ the_date = _("August 24")
    $ event_name = _("８月24日")
    
    if favorite == "kounosuke" or favorite == "shun" or favorite == "shin":
        window hide
        play music birds_chirping
            
        scene sky01 
        show text "{size=+130}August 24" at truecenter
        with Dissolve(.5)
        
        pause 3
        scene black with Dissolve(1)
        pause .4
        
    else:
        jump day25
        
    if favorite == "shun":
        jump map24
    else:
        $ renpy.jump (favorite + "24")
        
########################################################
label map24:

    scene hbroom with wipe_corner
    pause .2
    fn "「What should I do today? 」"

    play music "<from 2.5>av/audio/free0422.ogg"
    call screen minasatomap24    
    
########################################################
label kounosuke24:

    $ event_name = _("Checking up on him")

    play music cicada01 fadein 1.5
    $ renpy.music.set_volume(0.2, 0.0, channel = "music")
    scene kouno_house_out with wipe_right
    
    fn "「Hello. 」"
    harue "「Coming. Oh my, [fn]-chan. Welcome! 」" 
    fn "「Good afternoon, Mrs. Kuri.{p}\ \ But I'm just here to visit somebody sick. 」"
    harue "「My my, then please by all means,{p}\ \ won't you come in? 」"
    fn "「I will. 」"

    scene bedroom with sdis
    show ko 001 at center with wipeleft
    
    fn "「You have a cold? 」"
    ko "「Yeah. Thank you very much... 」"
    "I enter the room and Kounosuke,{p}raises the upper half of his body to reply."
    "This causes the ice pack,{p}on his forehead to fall with a plop."
    "I heard on the phone that Kounosuke,{p}was bedridden with an illness."
    "I was really surprised,{p}but this just looks like,{p}an ordinary Summer cold."
    "When I see him like this,{p}it doesn't seem to be all that bad."
    fn "「Don't they say that idiots can't get colds? 」"

    show ko 007 with dis
    
    ko "「...Does being an idiot have anything,{p}\ \ to do with catching a Summer cold? 」"
    fn "「No, no.{p}\ \ Anyways, is your photography going well? 」"
    
    show ko 005 with dis
    
    ko "「Huh? Uh... 」"
    fn "「Isn't the deadline approaching soon, too?{p}\ \ I can help if you'll cooperate.{p}\ \ But with the way your body is now... 」"
    ko "「Y-you know what? 」"
    fn "「Hm? What? 」"

    show ko 007 with dis
    
    ko "「I thought I'd quit and not apply. 」"
    fn "「What... Why?{p}\ \ You were so determined! 」"
    ko "「Well, you see... 」"

    stop music fadeout 5
    show ko 003 with dis
    
    ko "「Something suddenly killed,{p}\ \ my determination to do it.{p}\ \ Aha, hahaha... 」"
    fn "「...Huh? 」"
    
    show ko 002 with dis
    
    ko "「See, I'm old and useless.{p}\ \ I've got no motivation,{p}\ \ and I can't concentrate on anything."
    ko "So I'd like to see you off again. 」"
    fn "「...... 」"
    "Was that the punchline?"
    
    show ko 004 with dis
    
    ko "「Well, sorry for making you help so much. 」"
    fn "「Can you hold on a second? 」"
    
    show ko 001 with dis

    ko "「Huh? 」"
    fn "「Say what you will, but is this a joke? 」"
    "Kounosuke is usually like this,{p}when he's trying to fake,{p}so I expected this too."
    fn "「Why don't you give a more,{p}\ \ honest explanation other than,{p}\ \ I've got no motivation'?"
    fn "You know honestly,{p}you're pissing me off right now. 」"

    show ko 005 with dis
    
    ko "「S-sorry. I knew you'd be angry{p}\ \ I'll make it up to you for helping me out! 」"
    fn "「{cps=0}That's not the problem. 」"
    "I won't give a scolding,{p}to an irresponsible person,{p}if it seems like they're beyond repair."
    "With that in mind,{p}I bring out a slightly harder attitude."
    fn "「If I didn't keep every single,{p}\ \ one of your whims in check,{p}\ \ I would have never talked to you again. 」"
    
    show ko 007 with dis
    
    ko "「I-I'm really sorry.{p}\ \ But... 」"
    "He grabs on to his futon.{p}It looks like he's thinking up an excuse."
    
    if kouno_badgo == True:
        jump kounosuke24_annoyed

    menu:
        "A. Leave him and go back home":
            jump kounosuke24_annoyed
        "B. Wait for him to say something":
            jump kounosuke24_patience


    ###################################################
    label kounosuke24_annoyed:
    
        play music cicada01 fadein 3
        
        "I stand up,{p}and turn my back on Kounosuke."
        
        show ko 006 with dis
        
        ko "「Ah. 」"
        fn "「It would be bad,{p}\ \ if you gave me your cold,{p}\ \ so I'll go home for today. 」"
    
        show ko 007 with dis
        
        ko "「S-sure.{p}\ \ You're right. 」"
    
        hide ko with dis
        scene black with sdis
        scene kouno_hallway
        show yk 001 at center
        with wipe_right
        
        yk "「Ah. 」"
        fn "「Oh. 」"
        "When I exit out to the hallway,{p}I bump into Yukiharu-kun."
        yk "「You're going home already? 」"
        fn "「Yeah, well... 」"
    
        show yk 002 with dis
        
        yk "「Here's some apples for your trouble.{p}\ \ Mom peeled them for you.{p}\ \ Are you going to eat them together? 」"
        "Yukiharu-kun holds out a tray of apples,{p}and looks at me with a smiling face."
        "His carefree expression,{p}resembles that of Kounosuke's,{p}and makes me feel slightly irritated."
        "At the same time, I feel as if...{p}maybe I went a little too far."
        fn "「...Sorry. You should go give those,{p}\ \ to your brother to eat. 」"
    
        show yk 003 with dis
        
        yk "「I see. 」"
        
        $ renpy.music.set_volume(0.6, 0.0, channel = "music")
        scene kouno_house_out with wipe_right
        
        "I pass by Yukiharu-kun's side,{p}and leave Kounosuke's house behind."
        
        $ kouno_badend = True
        jump end24
    
    ##############################################################
    label kounosuke24_patience:
            
        "While silently pressuring him,{p}I wait for his words."
        
        pause 2.5
        
        ko "「It's just that I don't know why anymore. 」"
        fn "「Why what? 」"
        ko "「Why I wanted to go to the city... 」"
        "Kounosuke crawls out from his futon,{p}and pulls out a small paper bag,{p}from his desk drawer."
        
        play music melodious08
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        play sound paper00
        scene kouno_photos with sdis
        
        "Inside the bag are lots of photographs,{p}probably from when I went searching with him."
        "There's a number,{p}of familiar landscapes and scenery."
        ko "「...I was looking at these earlier,{p}\ \ thinking of how I'll be saying good bye,{p}\ \ to this village when I go to the city."
        ko "Then, for some reason,{p}I just didn't understand why anymore. 」"
        ko "「I don't like living in the country,{p}\ \ I thought that this was what I always wanted."
        ko "But there are so many things,{p}that are only here.{p}So I just don't know what to do anymore... 」"
        "Since he started talking,{p}Kounosuke's tone has gotten serious."
        "Now it looks as if,{p}he's on the verge of tears."
        fn "「Wh-what are you talking about,{p}\ \ this isn't like you. 」{w} {nw}"    
        $ renpy.music.set_volume(1.0, 0.0, channel = "sound")
        play sound bosu32
        scene bedroom
        show ko 011 at center
        extend "{w=.01}{nw}"
        show bedroom at vshake
        show ko at vshake
        
        ko "{size=+15}「I worry about things too! 」"
    
        show ko 007 with dis
        
        ko "「I can think about serious things too. 」"
        "Thought part of me thinks he might just be {p}acting."
        "I tried to cheer him up in my usual tone,{p}and he just yelled at me loudly."
        "Seeing Kounosuke like this,{p}for the first time leaves me confused."
        "A heavy silence dominates the room.{p}I really have no idea what to do."
        ko "「...I'm sorry, [fn].\n\ \ Would you go back for today? 」"
        fn "「Kounosuke... 」"
        ko "「I'm sorry... 」"
        fn "「...... 」"
        "I'm not able to say anything more.{p}Simply to escape from the silence,{p}I stand up and just leave the room..."
    
        hide ko with wipe_right
        scene black with sdis
        stop music fadeout 3
        scene kouno_hallway
        show yk 001 at center 
        with wipeleft
        
        yk "「Ah. 」"
        fn "「Oh. 」"
        "When I exit out to the hallway,{p}I bump into Yukiharu-kun."
        yk "「You're going home already? 」"
        fn "「Yeah, well... 」"
    
        show yk 002 with dis
        
        yk "「Here's some apples for your trouble.{p}\ \ Mom peeled them for you.{p}\ \ Are you going to eat them together? 」"
        "Yukiharu-kun holds out a tray of apples,{p}and looks at me with a smiling face."
        "That smile looks just like...{p}Kounosuke's usual face."
        "A twisting miserable feeling fills my chest."
    
        show yk 001 with dis
        
        yk "「Kounosuke hasn't been feeling well lately.{p}\ \ So I'm sure that you staying with him,{p}\ \ makes him feel a little better. 」"
        fn "「...Sorry. You should go...{p}\ \ give those to your brother to eat! 」"
        yk "「...I see. 」"
        "I pass by Yukiharu-kun's side,{p}and leave Kounosuke's house behind."
    
        jump end24    
    
    
########################################################
label shun24:
     
    $ event_name = _("A Boy's Hill")
    scene map
    hide screen hill24
    stop music fadeout 1.5
    scene black with wipe_dr
    play music daily03
    $ renpy.music.set_volume(0.8, 0.0, channel = "music")
    scene hill with dis
    
    "The cool wind feels pleasant on my cheek.{p}In the unseasonably refreshing air, I'm walking
    a distance farther than anybody else."
    "When I take a deep breath on a hill of Romania,{w=.2} 
    no,{w=.2} Minasato, it is a feeling 
    of Masterpiece Theatre."
    "Even though the mascot doesn't come out,\nthere is an atmosphere that an opening\nseems to be flowing from somewhere."
    su "「Lalalaaalalalalaaa. 」"
    "It has been flowing, hasn't it?{p}Waaaaaaaait?{p}Shun-kun!?"
    su "「Your letter. 」"
    "When it comes to a letter, is it John Smith?{p}Should I also burn with rivalry and hum\nthe Doughnut and Lemon Song?"
    
    show su tailwag 01 at midleft
    show ka 002 at midright
    with wipe_up_slow
    
    "In the middle of the hill, under the tree that\nlooks like it's palpitating, Kouya holds a guitar and\nShun-kun is singing happily."
    
    menu:
        "A. What are you doing?":
            jump shun24_practice
        "B. Graduation ceremonies shouldn't be held under a tree.":
            jump shun24_confusion

            
    ######################################################
    label shun24_confusion:
        
        $ event_name = _("Uncertain Palpitating")

        stop music fadeout 1
        pause 1
        play music free44
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        
        fn "「Wait a minuteeeeeee! 」"
        
        show su 015
        show ka 005
        with qdis
        
        ka "「! 」"
        su "「? 」"
        "Haah, wheeze, whew.{p}Even though the hill's ascent is slow,\nI can't help but be out of breath when I dash."
        "But I still keep running.{p}I'll never recognize the possibility\nthat those two are bound together!"
        "I pretend not to notice whether or not\nthere was an opportunity like that somewhere!"
        "They should decide that after including me\nin a 3-way... err, 3-person discussion!"
        fn "「Which one of you is confessing!? 」"
        
        show su 005
        show ka 010
        with dis
        
        ka "「? 」"
        su "「! 」"
        fn "「Generally if it's beastmen,\n\ \ a certification examination must be cleared\n\ \ before the graduation ceremony, 」"
        fn "「so you have to begin with collecting members. 」"
        su "「[fn]-san, you've got it all wrong.{p}\ \ Kouya-san and I just happened\n\ \ to meet here by chance. 」"
        fn "{size=+15}「I want to be called\n\ \ \"The 1-Year Master\"! 」"
        ka "「What's wrong, [fn]?{w} Shun? 」"
        
        show su 001 with dis
        
        su "「Please wait a minute, Kouya-san. 」"
        
        show su at move_offleft_far(1)
        scene black with rotation
        scene hill
        show su 005 at midleft
        show ka 005 at midright
        with rotation    
        pause .5
        
        fn "「Ha ha ha! {w=.2}\n\ \ We've had another misunderstanding, Shun-kun!{p}\ \ ...{w} sorry about that. 」"
        "I bow my head very deeply.{p}Kouya is taken aback and is not able to understand\nwhat happened, so I include him in my apology."
        fn "「Err, anyways. 」"
    
    ##################################################
    label shun24_practice:
            
        $ event_name = _("The Next Rhythm")

        stop music fadeout 1
        pause 1
        play music o97 
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        
        show su 001
        show ka 001
        with dis
        
        fn "「What are you doing? 」"
        
        show ka 003 with dis
        
        ka "「While I was practicing here, Shun happened\n\ \ to pass by and was happily singing.{p}\ \ So he's accompanying me for a bit. 」"
        "Dyaaaan.{p}Kouya's finger traces the string."
    
        show su tailwag 01 at jump_up
        pause .2
        
        su "「This is great, Kouya-san!{p}\ \ My song has become a proper piece of music! 」"
        "Shun-kun looks like he's in a better mood\nthan I imagined.{w} He loves singing, so adding\nin an instrument makes him really happy."
        
        show su 001 with dis
        
        su "「[fn]-san, will you listen? 」"
        
        show ka 001 with dis
        
        ka "「Only 2 phrases have been made though. 」"
        fn "「Of course I will! 」"
        "I give a strong nod, then draw near Kouya and\nShun-kun and sit down. His fingers lightly\ntouch the strings on his guitar."
        
        show ka 002 with dis
        
        su "「Lalalaaalalalalaaa~ 」"
        "The prelude overlaps the chorus,\nand the song begins."
    
        show su tailwag 01 with dis
        
        su "「Waaalk, waaalk, with the suuun.\n\ \ I am delivering your letter todaaay♪ 」"
        "Dyaan."
        
        show su 001
        show ka 003
        with dis
        
        ka "「There, that's it. 」"
        fn "「Wow, that was great! 」"
        
        show su 007 with dis
        pause .2
        
        su "「Hehee. 」"
        "Kouya plays a gentle sound.{p}Shun has a lovely boy soprano.{p}The two intertwine and become a harmony."
        "It's like a child's song,\nbut it also has a good feeling that's different."
        "When I fully immerse myself in the lingering sound,\nan impish grin appears around Kouya's mouth."
        
        show ka 009 with dis
        
        ka "「I know, [fn].{p}\ \ Try continuing the song for a bit. 」"
        fn "「Whaaat!? 」"
    
        show su 001 with dis
        pause .2
        
        su "「Wah!\n\ \ I want to hear your singing too! 」"
        "In front of others, and outside on top of that?{p}Kouya sure is bold...{w} No! It's embarrassing!"
        fn "「Th-that's kind of... 」~"
        
        show ka 002 at move_farright(0.5)
        
        ka "「The theme is what you'd expect.\n\ \ Shun is singing about delivering a letter today.\n\ \ Okay, one, two, one-two-three. 」"
    
        show su 002 at move_farleft(0.5)
        
        "Kouya has an expression of hidden laughter.\nShun-kun stands by with a carefree smile.\nAaah, I can't get out of this now!"
    
        show su tailwag 01 with dis
        
        su "「Waaalk, waaalk, with the suuun,\n\ \ I am sending your letter todaaay♪ 」"
        
        menu:
            "A. Try to sing with a hint of an enka ballad.":
                jump shun24_enka
            "B. Try to sing with a hint of idol pop music.":
                jump shun24_pop
        
    
    ##########################################################
    label shun24_enka:

        $ event_name = _("Enka-ish")
        
        stop music fadeout 1
        pause 1
        play music summer_ballad
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        
        fn "「{cps=5}Like a jaaay~{w=.2} burning~{w=.2} in the suuun~ 」"
        
        show su 004 with dis    
        stop music fadeout 1
        pause 1
        
        su "「... 」"
        "Shun-kun has an expression that says\n\"Something's wrong\"."
    
        show ka 005 with dis
        
        ka "「I don't think we heard that right... 」"
        fn "「It's for an Enka-ish feeling. 」"
        
        play music pops_006
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")    
        show ju 001 at center with sdis
        
        ju "「But why a jay? 」"
        fn "「Uwah! 」"
        
        show su tailwag 01
        show ka 010
        with dis
        
        su "「Juuichi-san! 」"
        
        show ju 002 with dis
        
        "Boing, Shun-kun jumps to him.{p}Their difference in size is plain to\nsee when they're close to each other."
        "Shun-kun is tiny. Juuichi-san is huge."
    
        show ka 005 with dis
        
        ka "「That was sudden. 」"
        ju "「So, why a jay? 」"
        "He gently pats Shun-kun on the head and asks again."
        fn "「Oh, well you see, a jay can mimic different\n\ \ kinds of sounds, right? 」"
        fn "「But the true voice of the letter,\n\ \ in other words the one who wrote it,\n\ \ can't be mimicked. 」"
        "I saw a jay birdman on TV the other day{p}and remembered he was an entertainer\nwho could mimic 7 different voices."
    
        show ka 002 with dis
        
        ka "「Hoh. 」"
        "Kouya's reaction to probing my\nbehavior scares me a little.{p}A-am I being tested!?"
        fn "「Even though I want to meet him, I can't.\n\ \ But because I have something I want to tell him,\n\ \ I deliver a letter on behalf of my voice. 」"
        fn "「It's just like the mimicking of a jay. 」"
        "I let my explanation naturally go on.{p}To be honest it didn't have such a deep reason,\nI just went off the top of my head."
        
        show su 004
        show ka 005
        with dis
        
        "Then, Juuichi-san gently lowers Shun-kun down\nand approaches me..."
    
        show ju 001 big at center_big with dis
        show hill at hshake
        
        "Wah!\nHe's grabbing my shoulders!"
        
        show ju 002 big with dis
        
        ju "「[fn]. 」"
        fn "「Yes? 」"
        "It gets swelteringly hot when he stares\nat me with those burning eyes.{p}Please let me go already, it hurts."
    
        show ju 005 big with dis
        
        ju "「I'm happy you understand me that much. 」"
        "Even though the tears overflowing\nfrom his eyes are becoming a stream,{p}I'm too embarrassed to respond."
        "Please let me go already, it hurts."
        su "「Juuichi-san... 」"
        ju "「Kodori.{w=.2} Kouya.{p}\ \ If it's alright with you, will you\n\ \ let me participate in this get-together? 」"
        
        show ju 002 big with dis
        
        ju "「And I wish to see the fate of [fn]'s soul\n\ \ with my own eyes. 」"
        
        show su 002
        show ka 002
        with dis
        
        "Even if I tell the fate of my soul,\nI'm still in Minasato.{p}Please let me go already, it hurts."
        "Kouya re-arranges the intro\ninto a more ethnic Japanese style.{p}Please stop Juuichi-san without a bitter smile."
        
        stop music fadeout 1
        pause 1
        scene black with blind_vert
        scene hill
        show ka 003 at farright
        show su 002 at farleft
        show ju 005 big at center_big
        with blind_vert
        play music summer_ballad
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")   
        show su at jump_up
        pause .2
        
        su "「Lalalaaalalalalaaa~ 」"
        su "「Waaalk, waaalk, with the suuun\n\ \ I am sending your letter todaaay♪ 」"
        fn "「{cps=5}Like a jaaay~{w=.2} burning~{w=.2} in the suuun~ 」"
        su "「It flies with a pitter-patteeer♪ 」"
        ju "「{cps=10}Never agai~n{w=.2}...{w=.2} does it come back~{w=.2}...{w=.2}\n\ \ {nw}"
        scene hill red
        show ka 003 red at farright
        show su 002 red at farleft
        show ju 005 big red at center_big
        with qdis
        extend "chasing~{w=.2} the sunset~ 」"
        fn "「{cps=5}The maaan~{w=.2} holding~ 」"
        jufn "「{cps=5}A reeed~{w=.2} teeeared~{w=.2} dreeeam~ 」" 
        
        scene black with sdis
        
        "Walking back to the village, Shun's innocent singing\nvoice begins to become sorrowful halfway there"
        "while he practices the new song,\n \"Red Teared Dream\" (title pending)."
    
        jump end24
        
    #####################################################
    label shun24_pop:
            
        $ event_name = _("Pop Idol-like")
        
        stop music fadeout 1
        pause 1
        play music shop02
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")   
        
        fn "「What if this letter does not reeeach you? 」"
        
        show su 015
        show ka 005
        with dis
        
        su "「Huh, really? 」"
        
        stop music fadeout 1
        pause 1
        
        "The accompaniment stops."
        fn "「I wrote a love letter, but I'm hesitating.\n\ \ Even though I decisively put it in the mailbox,\n\ \ my heart is pounding. 」"
        fn "「I want it to reach you,\n\ \ but I don't want it to reach you. 」"
        
        play music pops_020
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")   
        show ky 001 at center with sdis
        
        ky "「But I think it did~ 」"
        
        show su tailwag 01
        show ka 010
        with dis
        
        fn "「Uwah! 」"
        
        show ka 001 with dis
        
        ka "「Kyouji. 」"
        ky "「Hey. This looks fun. 」"
        su "「Kyouji-san! 」"
        "Boing, Shun-kun jumps to him.{p}Their differences in height are clear when he hugs him."
        "Besides, Kyouji is a soccer player\nso of course he has a toned body.{p}His arm supporting Shun is reliable."
        
        show ka 003 with dis
        
        ka "「Leave it to Kyouji when it comes to love letters,\n\ \ especially when it's about receiving them. 」"
        
        show ky 002 with dis
        
        ky "「I could say the same for you, couldn't I? 」"
        
        show ky 002 with dis
        
        "The two popular-types start bragging."
        
        show su 001 with dis
        
        su "「Were you listening to our song too, Kyouji-san? 」"
        "Shun-kun asks,\nafter being set back down on the ground."
        
        show ky 001 with dis
        
        ky "「Yes I was. Earlier your song came to me so suddenly.{p}Kouya's light guitar and Shun-kun's\n\ \ lovely singing voice. 」"
        fn "「What about me? 」"
    
        show ky 001 with dis
        
        ky "「You have a unique sense for lyrics.\n\ \ I don't think you're bad. 」"
        "His thin eyes deceive me so I can't\ntell what he's really thinking,\nbut I'll just think that he praised me."
        
        show ky 001 with dis
        
        ky "「Well, are you going to continue? 」"
        
        show su 002 with dis
        
        su "「Yes! 」"
        
        stop music fadeout 1
        pause 1
        scene black with blind_vert
        scene hill
        show ka 002 at farright
        show su tailwag 01 at farleft
        show ky 001 at center
        with blind_vert    
        play music shop02
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")   
        
        su "「Lalalaaalalalalaaa~ 」"
        su "「Waaalk, waaalk, with the suuun,\n\ \ I am delivering your letter todaaay♪ 」"
        fn "「If this letter does not rea~ch you. 」"
        ky "「But I think it did~ 」"
        fn "「To my timid self. 」"
        ky "「Let's say goodbye. 」"
        fnky "「Ｂｙｅ　Ｂｙｅ　Ｃｈｉｌｄｉｓｈ　Ｈｅａｒｔ\n\ \ I'm telling you how I feel, yay yay. 」" 
        
        show ky 001 with dis
        
        ky "「I must change. 」"
        
        show ka 009 with dis
        
        ka "「The world still remains small. 」"    
        kyka "「Ｂｙｅ　Ｂｙｅ　Ｃｈｉｌｄｉｓｈ　Ｈｅａｒｔ\n\ \ With an honest feeling, yay yay. 」"     
        fn "「To you now. 」"
        
        show ka 002 with dis
        
        kyka "「Love ☆ Letter ☆ Shoot ☆ 」"
        su "「... 」"
        
        show su 005 with dis
        
        su "「Don't reject my letter! 」"
        
        scene black with sdis
        
        "After insisting on something better,\n「Love ☆ Letter ☆ Shoot ☆\n~LOVE starting With a Kickoff 」 (title pending)"
        "Doesn't seem likely to be part\nof Shun-kun's repertoire."
        
        jump end24
    
########################################################
label shin24:
        
    $ event_name = _("Just like always...")
    
    scene shin_house_front with dis
    play music cicada01
    $ renpy.music.set_volume(0.8, 0.0, channel = "music")
    
    "I was in front of Shin-kun's house,\njust like always."
    "It's not like I came here everyday,\nbut I've gotten used to coming here."
    
    play sound tm2_chime002
    pause 1.2
    
    "That thought was on my mind when I rung the bell."
    
    play sound tm2_chair003
    pause 1
    show am 001 at center with dis
    
    am "「Ah, ln-kun. Welcome. 」"    
    fn "「Good day.{p}\ \ Is Shin-kun available? 」"
    
    show am 002 with dis
    
    am "「Yes.{p}\ \ He's in the middle of something\n\ \ in the kitchen right now. 」"
    
    show am 001 with dis
    
    am "「Oh, yes, I'll be heading out right now,\n\ \ so can I ask you two to take care of things? 」"
    fn "「Oh, okay then. 」"
    am "「Thank you.{p}\ \ {nw}"
    show am 002 with dis
    extend "Don't go too crazy.{p}\ \ See you then. 」"

    hide am with dis
    
    "Amaki-san's always so busy.{p}Even then, it's amazing how\nI can't sense that from him."
    
    stop music fadeout 1
    scene black with dis
    scene shin_house_den with sdis
    play music daily05
    show si 001 at center with dis
    
    si "「Oh, Amaki.{w=.2}\n\ \ We're almost out of wheat flour,\n\ \ so when you have time...{w} {nw}"
    show si 005 with dis
    extend "Ah-! 」"
    fn "「Good afternoon. 」"
    
    show si 011 with dis
    
    si "「G-good afternoon. 」"
    "I saw Shin-kun as he leaned\nhis head out of the kitchen."
    "Maybe it's because Shin-kun mistook me for Amaki-san,\nbut it felt kind of awkward."
    
    show si 001 with dis
    
    si "「Could you wait a moment?{p}\ \ {nw}"
    show si 009 with dis
    extend "I'm in the middle of cutting something. 」"
    fn "「Oh, sure thing.{p}\ \ Is it a cake? 」"
    
    show si 001 with dis
    
    si "「No, a pie.{p}\ \ Can you go on ahead to my room? 」"
    fn "「Mm, okay. 」"
    "I headed for Shin-kun's room as instructed.{p}So there's pie today."
    
    scene black with wipeleft
    scene shin_bedroom with wipeleft    
    pause 1.5
    play sound Door03Open
    pause 1
    show si 001 at center with dis
    
    si "「Sorry to keep you waiting. 」"
    "Shin-kun came along with a tray with some\ntea and confections."
    fn "「Is it okay if I move this? 」"
    si "「I suppose so.{w} Can you use that chair? 」"
    fn "「Okay. 」"

    hide si with wipe_right
    
    "I could smell the sweet aromatic smell of apple pie.{p}The bright look of it makes it look pretty good too.{p}The black tea smells as good as ever."
    fn "「Time to eat. 」"
    "And then I put my fork into the pie.{p}It cut in pretty easily."
    "When I put it in my mouth,\nI noticed a taste of butter and bittersweet jam."
    "The texture of the boiled apples and\nthe texture of the pie crust\nboth melded together in harmony."
    fn "「Mmm, you did pretty good today too. 」"
    
    show si 004 at center with dis
    
    si "「...{p}\ \ {nw}"
    show si 001 with dis
    extend "Well, about normal. 」"
    "Oh my...{p}He's as harsh on himself as ever.\nI even gave him a perfect score."
    
    if shin_lesson == True:
        jump shin24_baking
    else:
        jump shin24_homework

    #############################################################
    label shin24_baking:
        
        fn "「Even so, I said I'd be coming over.\n\ \ I really wanted us to make something together. 」"
        
        show si 009 with dis
        
        si "「... 」"
        fn "「Oh, that face you're making says nothing we make\n\ \ together will turn out good. 」"
        
        show si 005 with dis
        
        si "「Wha-!{p}\ \ {nw}"
        show si 012 with dis
        extend "Nobody said that! 」"
        fn "「Kidding!{p}\ \ Hahahaha!! 」"
        
        show si 009 with dis
        
        "That was surprisingly frank of him.{p}I smiled at him while I thought about\nhow much he was frowning at that joke."
    
        jump shin24_please_go
    
    ########################################################
    label shin24_homework:
        
        si "「How's your homework today? 」"
        fn "「Oh, yeah.{p}\ \ It's mostly done,\n\ \ so there won't be any problems at this rate. 」"
        
        show si 009 with dis
        
        si "「I see... 」"
        "But man, at any rate the way the tea\nand pie come together is superb yet again.{p}It's definitely better than anything from a cheap cafe."
    
    ########################################################
    label shin24_please_go:
            
        $ event_name = _("Don't Come Again")
        
        show si 001 with dis
        
        si "「...{w=.2}[fn]... 」"
        fn "「Hm? What? 」"
        
        show si 009 with dis
        
        si "「...{p}\ \ {nw}"
        show si 001 with dis
        extend "When you're done,\n\ \ would you please go home after that? 」"
        fn "「Huh?{w=.2} O-oh.{w} Are you busy? 」"
        
        show si 009 with dis
        
        si "「It's not like that... 」"
        fn "「? 」"
        
        stop music fadeout 1.5
        
        si "「...{p}\ \ I don't want you to come here anymore. 」"
        fn "「...{w} what? 」"
        "I didn't get what he just said to me,\nso after I swallowed my bite of pie,\nI repeated it in my head."
        "Don't come anymore. That's what it sounded like."
        
        show si 001 with dis
        
        si "「I said don't come here anymore. 」"
        
        play music sad03
        $ renpy.music.set_volume(1.0, 0.0, channel = "music")
        
        "Shin-kun plainly repeated it again, as if\nfollowing up with a strike after routing me.{p}This time I couldn't mistake it for anything else."
        fn "「Eh?{w} W-why? 」"
        
        show si 009 with dis
        
        si "「... 」"
        si "「...{p}\ \ {nw}"
        show si 001 with dis
        extend "Don't you get it?{p}\ \ Even I have my own circumstances. 」"
        
        show si 004 with dis
        
        si "「I want to stop giving up\n\ \ my time for your sake. 」"
        "With that attitude it can't be a joke,\nand it disturbed me to a strange degree even for me."
        fn "「No way, that's so sudden... 」"
        
        show si 001 with dis
        
        si "「I've been planning on saying it earlier,\n\ \ but I never had the chance. 」"
        fn "「... 」"
        "So then...I was always causing trouble for him?\nAll this time?"
        
        show si 009 with dis
        
        si "「... 」"
        "Shin-kun looked away from me,\nand was actively avoiding my eyes.{p}Just what did I do?"
        "And also, was he always thinking that about me?{p}I could see in that stiffening profile\nthat he was putting up with some sort of emotion."
        "The silence was getting painful.{p}Ha...hahaha...\nI could hear my dry laughing inside my head."
        "This summer I was a little anxious\nto get closer to Shin-kun,"
        "but could it be that I was the\nonly one getting excited about it?"
        "Now, I was filled with an empty, inexcusable feeling."
        "Even all those fun tea times, did Shin-kun just see\nthem as just something he had to do?\nSo I'm just a shameless friend..."
        si "「...sorry. 」"
        fn "「Eh? 」"
        
        show si 001 with dis
        
        si "「In any case I want you to stop coming. 」"
        "Shin-kun spoke quickly as if trying to\ncover up what he muttered."
        
        show si 009 with dis
        
        "Now he was looking straight at me,\nbut after a moment he couldn't bear it anymore,\nso he looked away again."
        fn "「I don't...get it. 」"
        si "「... 」"
        "What is he hiding? {p}Even I could see that something's off."
        "But what?{p}What does he really mean by not coming here anymore?{p}Why won't he tell me?"
        "I couldn't tell what his intentions were,\nand as my mind clouded over I tried\ndesperately to say something."
        fn "「Would something bad happen if I came here? 」"
        si "「... 」"
        fn "「...{w} ...{w} ...{p}\ \ T-then how about we go somewhere next time?{p}\ \ uhh...I know, how about the candy shop? 」"
        si "「...I won't go. 」"
        fn "「Oh, I-I see... 」"
        "He cut back shortly.{p}What should I do?{p}What should I do here?"
        "In front of the half-eaten pie, all words were gone.{p}Silence ruled over the room again.{p}...I've been the cause of all this."
        fn "「U-umm,{w} did I do something wrong? 」"
        si "「... 」"
        fn "「Uhh, what did you have to do?{p}\ \ If I got in the way,\n\ \ maybe I can help out to make up for it... 」"
        si "「Nothing. 」"
        fn "「... 」"
        "Ah, uh...{p}No wait, I can't accept this."
        fn "「O-okay then.\n\ \ But if there is anything feel free to- 」"
        
        play sound bosu31
        show si 012 with dis
        
        si "「I said there's nothing! 」"
        fn "「! 」"
        
        show si 005 with dis
        
        si "「Ah- 」"
        
        show si 009 with dis
        
        "Something fell out at the same time he shouted.{p}Shin-kun hid his flustered face.{p}Shin-kun's...crying?"
        "Why?\nDid I really say something that hurtful?"
        si "「In any case, I just, I don't want you coming anymore.{p}\ \ And also, I want you...to stop seeing me. 」"
        fn "「Even if you say that... 」"
        "Not see him anymore? What does he mean by that?{p}He really doesn't want to meet me anymore?{p}But why? What did I do?"
        fn "「Even if you just say that, I don't understand.\n\ \ If I could get a reason... 」"
        
        show si 001 with dis
        stop music fadeout 1.5
        play sound standup
        scene black with qdis
        
        "...{p}what?"
        
        scene shin_bedroom
        show si 001 at center
        with dis
        
        si "「...That. 」"
        "Shin-kun's face separated away.{p}The hands on my shoulders too.{p}{cps=10}Was I...{w} just{w} ...kissed?"
        "In surprise,\nI went to check the fleeting feeling on my lips,\nand unconsciously my hands touched my mouth."
        
        show si 009 with dis
        
        si "「It's disgusting isn't it?\n\ \ I won't do anything else.\n\ \ So, would you please forget this, and go home? 」"
        "The suddenness of it left me in a daze,\nbut Shin-kun's words brought me back to my senses."
        
        menu:
            "A. Clearly tell him your feelings.":
                jump shin24_confess
            "B. I can get it even if he hides it.":
                jump shin24_kiss
            "C. I...don't know what to do.":
                jump shin24_insult
            
    
    ##############################################################
    label shin24_confess:
        
        $ event_name = _("Because I'm selfish...")
        
        fn "「I-it's not disgusting at all. 」"
        
        show si 005 with dis
        
        "I unexpectedly raised my voice."
        fn "「I, I also...{w} love you Shin-kun.\n\ \ S-so, uhh... 」"
        
        show si 001 with dis
        
        si "「...so? 」"
        fn "「S-so then,{w} it was a little surprising,\n\ \ but, I guess I was a bit happy about it. 」"
        "That's right.{p}So in other words, it was a confession!{p}On top of that, it came from Shin-kun."
        "I finally understood what just happened,\nand I realized my face was flushing\nas I calmed down."
        fn "「And to think that you'd be the one to do\n\ \ this Shin-kun,{w} it makes me so happy. 」"
        
        show si 009 with dis
        
        si "「...! 」"
        si "「...{w} say that. 」"
        fn "「? 」"
        
        show si 012 with dis
        play music melodious04
        
        si "「Don't just say that! 」"
        si "「Aren't you supposed to be going soon!?{p}\ \ And... And, just what are you suggesting!?{p}\ \ That we go out even if we know you're leaving!? 」"
        fn "「Huh...? N-no.{w} I wasn't... 」"
        si "「You just simply tell someone you love them, but\n\ \ do you understand how much that can hurt people!?{p}\ \ You're happy? Stop lying to me! 」"
        fn "「I'm not lying! 」"
        si "「Then what are you saying!?{p}\ \ I, I...! 」"
        fn "「Shin-kun... 」"
    
        show si 012 big at center_big with dis
        
        si "{size=+15}「DON'T MAKE A PROMISE\n\ \ YOU CAN'T KEEP!! 」"
        fn "「!! 」"
        "When he yelled,\nI lost sight of what I was going to say."
        "What did I do?{p}This isn't like Shin-kun at all.{p}I don't understand."
    
        hide si
        show si 008 at center
        with dis
        
        si "「I beg you, I'm begging you...! 」"
        "Shin-kun was crying.{p}As he shouted, as he heaved with sobs,\nhis tears rained down."
        "I've never even once saw\nthat sort of face from him.{p}I didn't know if it was okay to say anything."
        "Shin-kun took 2, 3 big trembling breaths,\nthen tried as best he could to speak calmly."
        
        show si 009 with dis
        
        si "「Sorry.{w} I just...got mad.{p}\ \ But it's no good.{p}\ \ e can't be together. 」"
        
        show si 007 with dis
        
        si "「I realize what I'm saying is egotistical.{p}\ \ But I don't know what else to do.{p}\ \ I don't want you caught up in my selfishness. 」"
    
        show si 008 with dis
        
        si "「So, so...{w=.2}don't come anymore. 」"
        fn "「Shin-kun.. 」"
        si "「Please, [fn]... 」"
        "Slowly, his usual bracing attitude\nscattered further than I could even imagine,\nand Shin-kun continued crying."
        "I desperately tried to find words to comfort him,\nbut no matter how much I thought I couldn't come\nup with anything good."
        "Helplessly, helplessly Shin-kun was getting distant,\nand it felt like anything I say would only hurt him."
        "Still I tried desperately to come up with something,"
        "but I couldn't,\nnot one thing that could let me approach him."
        "If there was anything I could say,\nthere was just one thing."
        fn "「...sorry. 」"
        si "「... 」"
    
        scene black with sdis
        
        "As the mutual silence persisted,\nI left behind my half-eaten pie\nand left Shin-kun's house."
        "Why did Shin-kun do that?{p}Why did he tell me 'don't come'?{p}Why...did he cry?"
        "I don't get it, I don't get it Shin-kun.{p}I just...don't get it."
        
        if shin_key1 == True:
            $ shin_true = True
        else:
            $ shin_normalend = True
            
        jump end24
    
    ############################################################
    label shin24_kiss:
        
        fn "「I feel the same way about that! 」"
        
        show si 005 with dis
        
        si "「What? 」"
        
        play sound bosu29
        scene black
        show si 005 at center
        with sdis
        
        "I grabbed Shin-kun by the shoulders, and with force,\nI did to him what he did to me earlier."
        "It wasn't disgusting.{p}After all, I'm the same way."
    
        show si at shivering 
        
        si "「...! ...! 」"
        "Shin-kun struggled with my arms, but I didn't let go.\nDidn't Shin-kun start it first?\nHe shouldn't hate this."
        
        show  shin_bed behind si with sdis
        show si 005 at shivering
        with sdis
        play music wind_noise
        show si 009 at center with dis
        
        si "「Hwaah! [fn], w-what are...? 」"
        fn "「Wasn't this what you meant? 」"
        si "「No, that's... 」"
        fn "「I love you too Shin-kun. 」"
        
        show si 005 with dis
        
        si "「Nmgh! 」"
        "I went on to push Shin-kun into bed,\nand I kissed him hard one more time."
        
        scene shin_bed night
        show si 005 night at center 
        with sdis
        show si 007 night with dis
        
        si "「Mn! Nngh! 」"
        "I forcibly stuck my tongue into that mouth,\nfeeling a bit of roughness, entwined with warmth.\nI could taste the sweetness of pie."
        "I held down both of Shin-kun's\nwrists as he struggled."
        "I was pretty much riding that body,\nalmost assaulting it as I felt my breaths rose,\nand I knew my excitement was rising."
        "Shin-kun was squirming beneath me.\nHe started it, so it's weird he's so against it."
        "Until Shin-kun's resistance weakened I was determined,\nso I kept pinning down that slim body, "
        "continuing with the messy kiss,\nthen groped that little figure."
        "Almost like an animal tormenting its prey."
        si "「...! ...[fn]... 」"
        "Since his resistance broke down a bit,\nI pulled my face back,\nand there was a thread of saliva between our mouths."
        "Shin-kun was in front of my eyes.\nAs those unfixed eyes rose up to look at me,\nhis exposed chest was moving up and down."
        "I could feel the heart pounding\nthrough past the disheveled breathing."
        
        menu:
            "A. Keep going until the end.":
                jump shin24_rape
            "B. What am I doing?":
                jump shin24_regret
    
    #########################################################
    label shin24_rape:
            
        $ event_name = _("You are a HORRIBLE PERSON, you MONSTER.")
        
        stop music fadeout 1.5
        scene black with sdis
        play music sad02
        
        "As I took off Shin-kun's clothes,\nI ran my fingers through the hidden fur."
        "I twiddled the soft cat fur around my finger,\nhowever it smoothly slipped out of my hands."
        
        scene shin_bed night
        show si 207 shivering night
        with sdis
        
        si "「a...u... 」"
        "Shin-kun sometimes called out with a cracking voice,{p}and didn't resist. "
        "Whether he didn't or couldn't, I didn't care."
    
        show si 107 night at shivering with dis
        
        "In fact, I pulled off the last of Shin-kun's clothes,\nand exposed his beastly form to the air."
        "I also took off the thing hanging onto my own\nbrutish body, though I never let go of the other."
        "I've come this far,\nI just need to leave the rest to nature."

        show si 105 night at jump_up
        
        si "「Gaah,{w} {nw}"
        show si 108 night with dis
        extend " ugh,{w=.2} u... 」"
        "Countless times I took his lips, touched his body,\nforcibly pushed my way in. "
        "Past the tightness it was warm...\nIt almost felt like it was pulling me in."
        
        show si at shivering
        play sound humping loop
        
        si "「Eii,{w=.2} gyah,{w=.2} [fn], ow, ng... 」"
        "Again, I pressed our lips together.\nAs I lost myself in the movements,\nI caressed his body as much as I could."
        fn "「Whoa, this is great...!{p}\ \ It's so warm inside...Shin-kun...Shin...! 」"
        si "「Uuurgh,{w} haah,{w} guh,{w} kh... 」"
    
        scene black with dis
        
        "Shin screwed his eyes closed as he clung to me.{p}When something welled up on the end of those eyes,\nI wiped it away with my tongue."
        "Claws seized in as far as they could,\nso I shook off those hands\nand pushed them onto the bed."
        "Our bodys were glued together, and as I felt his\nfur all over me, we exchanged hot breaths.{p}I heard Shin's voice glossed over in pain."
        fn "「Ahh, Shin,{w} I can't take it anymore!{p}\ \ If you're that tight, I'll cum soon! 」"
    
        stop sound fadeout 1
        
        si "「------!!! 」"
    
        scene white with sdis
        
        "As Shin voicelessly screamed,\nI shot out all I had."
        "Doing it with the person I love\nfor the first time made my head blank out white,\nand it felt good."
    
        stop music fadeout 1.5
        scene black with sdis
        pause 2
        scene shin_bed
        show si 108 at center
        with dis
        
        "As I breathed roughly, I looked down upon him."
        "All the fluids spent got\nchilly in the air conditioning."
        "Because of the speed of it\nall my own body got cold."
        "Shin-kun was crying.\nBeneath me, he was crying while blocking out his voice."
        "Even if I understood what I did,\nmy feelings had rejected it.{p}What remained of the pleasure was in fact a lie."
        fn "「... 」"
        "I opened my mouth. No words came out.{p}What I was going to say, I don't know myself.{p}Is there anything I can say...?"
        fn "「{cps=5}I, I... 」"
        si "「Get out... 」"
        "It was a voice like a low growl.\nI desperately tried to find\nwords to explain myself with."
        si "「Shin-kun, I- 」"
    
        show si 112 with dis
        
        stop music fadeout 1
        play sound bosu35
        show shin_bed at hshake
        
        si "{size=+25}「GET OUT! 」"    
        "I was pushed away and fell off the bed.\nIt didn't hurt since I fell on a rug."
        
        play music sad01
        
        fn "「No wait, I, this wasn't- 」"
    
        show si 105 at jump_up
        
        si "「Hie! 」"
        fn "「Ah... 」"
        "I only just tried to get closer,\nand Shin-kun pulled back looking terrified,\ndrawing back on the bed."
        fn "「...sorry.\n\ \ I'm really sorry... 」"
    
        show si 108 with dis
        
        si "「{cps=5}Don't ever...come again... 」"
        fn "「Sorry... 」"
    
        scene black with dis
        
        "I couldn't say anything more than that,\nand I left Shin-kun's house."
        "There was no room for explanations.{p}I didn't mean...{w} do that to Shin-kun...{p}I just...{w} just, I..."
        "...I didn't mean for this to happen."
        
        $ shin_badend = True

        jump end24
    
    ######################################################
    label shin24_regret:
            
        $ event_name = _("I didn't mean to...")
        
        "What am I doing...?\nI came back to my senses while still\nholding Shin-kun down."
        
        stop music fadeout 1.5
        scene shin_bed
        show si 007 at center
        with sdis
        show si 009 with dis
        
        si "「...will you...get off me? 」"
        fn "「O-oh. Right... 」"
        "I removed myself just as he quietly murmured.{p}Shin-kun got back up, and as\nhe put his clothes back on,"
        
        show si 010 with dis
        play music sad03
        
        si "「You're the worst... 」"
        "He said only one thing.\nAnd yet it felt so heavy."
        fn "「S-sorry.{w} I didn't mean for... 」"
        
        show si 009 with dis
        
        si "「...go home already. 」"
        fn "「Shin-kun, I... 」"
        
        show si 012 with dis
        
        si "{size=+15}「I SAID GO HOME! 」"
        fn "「... 」"
        "I can't say anything anymore."
        
        scene black with dis
        
        "I ran away from Shin-kun's house,\nrecklessly running down Minasato's country roads.\nI didn't mean for this to happen. I didn't..."
        
        jump end24
    
    ###########################################################
    label shin24_insult:
            
        $ event_name = _("A Confession? Or...")
        
        "I don't know what to make of things\nbeing confessed to so suddenly."
        "My head was so filled with confusion,\nit was cramming up fast."
        fn "「Ah,{w} uh,{w} S-Shin-kun?{p}\ \ That was... 」"
        si "「... 」"
        fn "「No, uh, umm... 」"
        si "「... 」"
        "Right. So just now, that was a confession wasn't it?{p}On top of that, it came from Shin-kun..."
        "That was an unexpected approach.{p}I tried hiding my embarrassment by scratching my head."
        "However the flush in my face\ndidn't seem to be cooling off."
        
        play music daily05
        
        fn "「O-oh man.{p}\ \ You're surprisingly bold Shin-kun. 」"
        
        show si 001 with dis
        
        si "「What? 」"
        fn "「Uh well, I guess I like you too?{p}\ \ It's just, being confessed to by an unrequited\n\ \ love just has my head all messed up. 」"
        
        show si 009 with dis
        
        si "「What are you saying...? 」"
        fn "「Well,{w} in other words,\n\ \ wouldn't this be requited feelings? 」"
        fn "「I've always loved you since before,\n\ \ and with you loving me, isn't that okay? 」"
        
        show si 005 with dis
        
        "As I looked away while moving my hand all flustered,\nI kept talking like I was explaining things\nmore to myself than anyone."
        fn "「So,{w} well,{w} like,{w} I'm also that way? 」"
        fn "「I mean I'm surprised right now,\n\ \ but I'm kinda happy, and,\n\ \ that was a confession right? 」"
        si "「...{p}{nw}"
        show si 002 with dis
        extend "Pft,{w=.2} ahahaha!{p}\ \ you really are...{w=.2}ahahahaha! 」"
        fn "「D-don't laugh. 」"
        "When he left,\nI felt like the tense mood broke up.\nHowever, it only lasted for a second."
        
        show si 001 with dis
        
        si "「...if that's the case,{w} {nw}"
        stop music fadeout 1.5
        extend " I hate you. 」"
        fn "「Eh? 」"
        "The moment the laughing stopped,\nShin-kun proclaimed that coldly."
        
        play music melodious05
        show si 009 with dis
        pause .5
        show si 001 with dis
        
        si "「I hate you.{w} I've always hated you.{p}\ \ That optimism of yours irritates me,\n\ \ it makes me sick. 」"
        fn "「... 」"
        "He didn't seem to be joking,\nit wasn't like the casual barbed comments he made,\nit felt cold and robotic."
        "Shin-kun kept going on like that."
        
        show si 010 with dis
        
        si "「So don't make so much out of a kiss.{p}\ \ And actually,{w=.2} could you not get weird ideas?{p}\ \ {nw}"
        show si 004 with dis
        extend "I just wanted to make fun of you 」"
        fn "「That can't be...{w} that's so cruel. 」"
        
        show si 009 with dis
        pause .3
        show si 001 with dis
        
        si "「I wanted to tell you as peaceably as possible,\n\ \ but it won't get through unless I'm clear, won't it? 」"
        si "「For the second time, don't ever come again.{p}\ \ {nw}"
        show si 012 with dis
        extend "Just looking at you disgusts me! 」"
        "----!"
        "At those words, something within me just burst out."
        fn "「You, you're the worst...! 」"
    
        show si 009 with dis
        scene black with dis
        play sound step03
        
        "I yelled something at Shin-kun, and when I realized\nI had ran out of Shin-kun's house, "
        "I was already out on the familiar country road\nbreathing in the humid midsummer air."
        "Maybe it was because I had suddenly dashed out,\nbut my lungs hurt. What the hell..."
        "What the hell is his problem...!?"
    
        jump end24
    
########################################################
label end24:
    stop music fadeout 3
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

    jump day25

