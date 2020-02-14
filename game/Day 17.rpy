###Day 17
label day17:
    
    $ renpy.music.set_volume(1.0, 0.0, channel = "music")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound2")
    
    $ day = 17
    $ the_date = "August 17"
    $ event_name = "８月17日"
    
    if favorite == "shun" and meet_gaku != True:
        jump day18
        
    if favorite == "kounosuke" or favorite == "shun":
        window hide
        play music birds_chirping
        
        scene sky01 
        show text "{size=+130}August 17" at truecenter
        with Dissolve(.5)
    
        pause 3
        scene black with Dissolve(1)
        pause .4

    if favorite == "kounosuke":
        jump kounosuke17
    elif favorite == "shun":
        jump shun17
    else:
        jump day18

################################################################
label kounosuke17:
  
    $ event_name = "Taking pictures with Kounosuke"

    scene hbroom with sdis
    play music free0213 fadein 1.5 
    
    "Even though it's still morning,{p}it's already getting hot in the room{p}I can tell the weather is gonna be nice."

    play sound ChimeA
    pause 1
    
    "...He's arrived."
    ko "「Good afternoon! 」"
    "I hear a familiar and cheerful voice,{p}from the front door."
    
    scene black with sdis
    scene hentry
    show ko 001 at center
    with sdis
    
    fn "「I run into you first thing,{p}\ \ but it's morning now."
    fn "You should be saying 'good morning',{p}not 'good afternoon'. Okay? 」"

    show ko 002 with dis
    
    ko "「That's just a...{p}\ \ minor detail, isn't it? 」"
    "The problem here isn't the greeting,{p}it's the time."
    "You shouldn't call a friend's house,{p}until at least 10."
    "That's what we were taught,{p}in elementary school..."
    
    show ko 001 with dis
    
    ko "「So, is now alright?{p}\ \ Have you even eaten breakfast yet? 」"
    
    menu:
        "A. Not yet.":
            jump kounosuke17_notyet
        "B. I ate, but...":
            jump kounosuke17_ate
        "C. What are you talking about?":
            jump kounosuke17_what

    ################################################
    label kounosuke17_notyet:
            
        fn "「Not yet. 」"
    
        show ko 005 with dis
        
        ko "「Come on, hurry up and eat! 」"
        fn "「I mean, do you even know,{p}\ \ what time it is right now? 」"
        
        show ko 001 with dis
        
        ko "「Eh? Err... 」"
    
        show ko 006 with dis
        
        ko "「Ah! I don't have a watch.{p}\ \ What time is it? 」"
        fn "「...8:36. 」"
    
        show ko 001 with dis
        
        ko "「Huh? 」"
        fn "「And now it's 8:37. 」"
        ko "「...... 」"
    
        show ko 005 with dis
        
        ko "「S-sorry.{p}\ \ If I didn't come out before breakfast,{p}\ \ dad would've made me watch the store... 」"
        fn "「...... 」"
        
        show ko 007 with dis
        
        ko "「I'm really sorry! 」"
        "Haah.{p}Jeez, he really hasn't grown up at all."
        fn "「For now, will you wait,{p}\ \ until I'm done eating breakfast? 」"
    
        show ko 001 with dis
        
        ko "「Oh, yeah. Of course.{p}\ \ I'm truly sorry, [fn]! 」"
        fn "「It's troubling,{p}\ \ when you go that far to apologize. 」"
    
        jump kounosuke17_photography
        
    ##############################################
    label kounosuke17_ate:
        
        fn "「I ate, but... 」"
    
        show ko 002 with dis
        
        ko "「Really? Then let's hurry,{p}\ \ and get out of here! 」"
        fn "「But don't you think next time that,{p}\ \ you should pay more attention to the time? 」"
    
        show ko 005 with dis
        
        ko "「Huh? What time is it right now? 」"
        fn "「Half past 8. 」"
    
        show ko 006 at jump_up
        
        ko "「Really!? 」"
        fn "「Really. 」"
    
        show ko 005 with dis
        
        ko "「S-sorry.{p}\ \ I didn't think about the time...{p}\ \ Am I bothering you? 」"
        fn "「How many years do you think,{p}\ \ we've been friends in this village?{p}\ \ I'm used to it. 」"
    
        show ko 001 with dis
        
        ko "「Is that so?{p}\ \ But I really am sorry, [fn]! 」"
        "I hope that this situation,{p}really helps him in the future..."
        
        jump kounosuke17_photography
    
    #################################################
    label kounosuke17_what:
    
        $ kouno_badstep = "True" #Don't want to get on his badside....    
        
        fn "「What are you talking about? 」"
    
        show ko 005 with dis
        
        ko "「Damn it, don't play dumb."
        ko "Isn't this your part of the deal,{p}in exchange for me helping you,{p}with your homework? 」"
        "Tch.{p}I'm so tired and sore."
        fn "「I know, can you wait a little?{p}\ \ I still haven't eaten breakfast. 」"
    
        show ko 002 with dis
        
        ko "「Oh, yeah. Of course. 」"
        "Aah, I'll be running around the village,{p}with him in this horrible heat..."
        "Still, I wonder if saying that,{p}would be too much..."
        "The depressing heat and sunlight,{p}is already coming through the front door."
        "Ooh, in the meantime,{p}I'll just eat my breakfast slowly."
        ko "「I'll be waiting, so eat quickly! 」"
        "Says Kounosuke, with timing,{p}that makes it seem as if he read my mind."
        "Ah jeez, okay! I got it! I got it!{p}I did say I'd help him!"
        "The mouth really is,{p}\"the origin of disaster\"..."
    
        jump kounosuke17_photography
    
    ##############################################
    label kounosuke17_photography:
        
        scene black with wipe_right_slow
        play music cicada01 fadein 2
        $ renpy.music.set_volume(0.5, 0.0, channel = "music")
        pause .2
        scene bstop
        show ko 001 at center
        with wipe_right_slow
        
        ko "「What do you think about here? 」"
        "For some reason,{p}we ended up at the bus stop."
        "It might just be Kounosuke's sensibility,{p}but I'll ask just in case."
        fn "「...Just to be sure,{p}\ \ can I ask why you chose this place? 」"
        ko "「This is the only place where,{p}\ \ you can get transportation to other towns,{p}\ \ or something like that."
        
        show ko 007 with dis
        
        ko "It gives the sense of...{p}setting off on a journey... 」"
        "I think I noticed that myself,{p}while he was talking."
        "He looks away from me,{p}{nw}"
        show ko 002 with dis
        extend "and puts on a fake smile."
        fn "「Kounsouke, the theme is,{p}\ \ 'Nostalgic Scenery', right? 」"
        
        show ko 001 with dis
        
        ko "「Yeah. 」"
        fn "「This place is nostalgic? 」"
    
        show ko 003 with dis
        
        ko "「Oh, haha! 」"
        "I'd thought that maybe,{p}he'd stay on task with this,{p}but I knew this was going to happen."
    
        show ko 001 with dis
        show ky 001 at offleft
        show ju 001 at offleft
        
        ko "「L-let's move on, shall we? 」"
        "I've been deceived."
        
        show ko at move_farright(0.6)
        show ky at move_center(0.6)
        show ju at move_farleft(0.6)
        stop music fadeout 1.5
        
        ky "「Oh? What are you two doing? 」"
    
        show ko 006 at jump_up
        play music daily01
        $ renpy.music.set_volume(0.7, 0.0, channel = "music")
        
        ko "「Nyooooo!? 」"
        ju "「Why are you so surprised? 」"
        fn "「Oh, well look, senpai and senpai.{p}\ \ Good morning. 」"
        ky "「Good morning, [fn]. 」"
        ju "「Good morning. 」"
        ky "「If you're here for the bus,{p}\ \ it should be getting here."
        ky "But if you're going shopping,{p}don't you think it would be better,{p}to go to Kazenari? 」"
    
        show ko 005 with dis
        
        ko "「Oh no, that's... 」"
        fn "「We aren't going to town. 」"
        ju "「If you're not getting on the bus,{p}\ \ then what are you doing here? 」"
        fn "「It's because of Kounosuke. 」"
    
        show ko 002 with dis
        
        ko "「Th-that's right!{p}\ \ I'm showing [fn] around the village,{p}\ \ since he's been gone for so long! 」"
        
        stop music fadeout 2
        pause 2
        
        "What?"
        
        play music free22
        
        ju "「I think it's kind of late for that. 」"
    
        show ko 005 with dis
        
        ko "「Oh... 」"
        fn "「Huh? Umm, we're just taking pictures. 」"
    
        show ko 012 with dis
        
        ko "「Zip it, [ln]! 」"
        fn "「Okay... 」"
        "He desperately gives me an awful death glare,{p}so I shut my mouth."
    
        show ko 002 with dis
        
        ko "「S-so, senpai and senpai, what are you...{p}\ \ going into town for? 」"
        ju "「Us? 」"
        ky "「There's a special course,{p}\ \ for 3rd year students today.{p}\ \ We're on our way to school. 」"
        ko "「Oh, is that so?{p}\ \ We have some urgent business,{p}\ \ to take care of around here! 」"
        fn "「Eh? What? W-wait a minute! 」"
    
        show ko 001 with dis
        
        ko "「Come on [fn], quickly! 」"
        fn "「Whaaaaat!? 」"
    
        play sound step03 
        show ko at move_offright(0.6)
        show ky at move_midright(0.6)
        show ju at move_midleft(0.6)
        
        kyju"「......? 」" 
        ju "「Well, that was something. 」"
        ky "「Kounosuke's just as busy as ever... 」"
        ju "「He's gonna be a 3rd year soon.\n\ \ {nw}"
        show ju 003 with dis
        extend "...Is he gonna be alright? 」"
    
        show ky 002 with dis
        
        ky "「Hmm, I would say it's all up to him. 」"
        
        stop music fadeout 2
        scene black with sdis
        scene park
        show ko 011 at center
        with circle_out2
        play music free53 
        
        ko "「Jeez! You just went right out,{p}\ \ and publicly advertised a secret! 」"
        fn "「What? Err, I did that? 」"
        
        play sound bom26_b
        $ renpy.music.set_volume(0.8, 0.0, channel = "sound")
        show ko 012 big at center_big with explosion
        show yk 001 at offleft
        
        ko "{size=+15}「YOU DID! 」"
        "I didn't think he'd be this high-strung."
        "When he talks like this,{p}it feels like he could just lash out,{p}and bite me at any moment."
        fn "「A-alright. I'll be careful next time,{p}\ \ so please don't bear your canines... 」"
        ko "「You definitely won't next time? 」"
        who "「Heeey. 」{w} {nw}"       
        show ko 006 big with qdis
        show ko at move_offright_far(0.2)
        show yk at move_farleft(0.8) 
        extend "{w=.6}{nw}"
        hide ko        
        show ko 001 at offright
        
        yk "「Oh, I knew it was you, nii-san.{p}\ \ What are you doing here? 」"
    
        show ko at move_farright(0.5)
        
        ko "「Oh, what? Yukiharu? 」"
    
        show yk 003 with dis
        
        yk "「What are you saying what for? 」"
        fn "「Good afternoon. 」"
    
        show yk 001 at bowing
        
        yk "「Good afternoon. 」"
        "Yukiharu-kun politely bows."
        "Even though they look similar,{p}their personalities are really different.{p}It's sort of funny, actually."
    
        show yk 003 with dis
        
        yk "「What is it? 」"
        "Oh, oops.{p}It seems I was unconsciously smiling."
        "Yukiharu-kun looks at me,{p}with clearly suspicious eyes."
        fn "「N-nevermind.{p}\ \ Anyways, what are you up to? 」"
    
        show yk 001 with dis
        
        yk "「It's going to be hot today,{p}\ \ so I'm going to play in the river. 」"
        "He has a somewhat blunt attitude.{p}I wonder if he doesn't like me?"
        fn "「I see... 」"
    
        show ko 005 with dis
        
        ko "「The river can be dangerous, be careful. 」"
        yk "「You don't need to tell me,{p}\ \ I won't go where it's deep. 」"
    
        show ko 001 with dis
        
        friend "「Yukki, what's going on? 」"
    
        show na 001 at center with dis
        
        friend "「Is this your big brother? 」"
        
        yk "「Oh, yeah. That's right. 」"
        
        show ko 002 at bowing
        
        ko "「Hello! 」"
    
        show na 002 with dis
        
        friend "「Good afternoon.{p}\ \ Yukki, what are you wasting time for?{p}\ \ Let's hurry to the river! 」"
        yk "「Oh, sorry. Let's go.{p}\ \ See ya, nii-san! 」"
    
        scene park
        show ko 003 at center 
        with wipeleft
        
        ko "「Be careful in the river! 」"
        yk "「I know! 」"
    
        show ko 001 with dis
        
        ko "「Hmm, let's go to the next place then. 」"
        fn "「Wait, you're not taking any pictures here? 」"
        ko "「Huh? 」"
        "It's deserted in the park.{p}The children that were here went off somewhere,{p}There seems to be melancholy in the emptiness."
        "I had thought that this,{p}is why we came running over here."
        fn "「This is 'Nostalgic Scenery' isn't it? 」"
        ko "「...... 」"
    
        show ko 002 with qdis
        
        ko "「Oh! Nice one, [fn]! 」"
        "Kounosuke wasn't...{p}even thinking about it, was he."
    
        play sound ShutterSound
        pause 1
        play sound ShutterSound
        pause .5
        play sound ShutterSound
        pause .5
    
        ko "「Alright, now we really are,{p}\ \ going to the next spot! 」"
        fn "「Okay. 」"
        
        hide ko with dis
        scene black with blind_vert
        pause .5
        scene shrine
        show ko 001 at center
        with blind_vert
        
        ko "「I think this place is good,{p}\ \ what about you? 」"
        "Hmm, the shrine."
        fn "「You aren't going to just take pictures,{p}\ \ of stuff like birds and flowers again? 」"
    
        show ko 005 with dis
        
        ko "「Of course not. Look, at this.{p}\ \ It represents the good old days,{p}\ \ it's  almost like... the soul of our town."
        ko "Well, at least, something like that.{p}I'm not really good at explaining things,{p}but I'd say it gives a sense of history. 」"
        fn "「Aah... 」"
        "I think he's about to make,{p}the same mistake as last time,{p}but I'll consider it for the time being."
        ko "「Would you still say this is wrong? 」"
        fn "「Well, it's not that great?{p}\ \ To put it simply,{p}\ \ the problem is your sensibility 」"
    
        show ko 007 with dis
        
        ko "「Huh, aren't you being kind of cold? 」"
        fn "「That's not it, I'm saying that,{p}\ \ you need to hone your sensibilities,{p}\ \ a little more... 」"
    
        show ko 005 with dis
        
        ko "「Hmm, are you avoiding,{p}\ \ saying something nice? 」"
        "Haah...{p}I'm going through all this trouble,{p}to give adivice to this tanuki."
        fn "「...If you don't need my advice,{p}\ \ then maybe I should go back home now. 」"
    
        show ko 006 with dis
        
        ko "「I-I said I'm sorry.\n\ \ Don't be so irritable! 」"
        
        play sound ShutterSound
        pause .5
        play sound ShutterSound
        pause 1.2
        play sound ShutterSound
        pause .5
        show ko 002 with dis
        show so 001 at offright_far
        
        ko "「Oh, I know. How about we...{p}\ \ make a little prayer,{p}\ \ to take care of your troubles? 」"
        fn "「Ah, that'll be good. 」"
    
        show ko 001 with dis
        
        ko "「Alright then,{p}\ \ then I'll definitely get the grand prize! 」{w} {nw}"        
        show ko at move_farleft(0.75)
        show so at move_farright(0.75)
        show su 001 at offright
        extend "{w=.75}{nw}"
        
        so "「Huh? [ln]-senpai? 」{w} {nw}"    
        show ko 006 with dis
        show so at move_center(0.75)
        show su at move_farright(0.75)
        extend "{w=.75}{nw}"
        
        so "「Ah, I knew it.{p}\ \ And there's Kuri-senpai too.{p}\ \ Hello! 」"
    
        show su 002 with dis
        
        su "「Good afternoon to both of you. 」"
        fn "「Oh, hello. 」"
    
        show ko 002 at shivering with dis
        
        ko "「Y-yeah, hi... 」"
        
        show so 005
        show su 004
        with dis
        
        su "「Kounosuke-san, what's wrong? 」"
        so "「You're lookin' weird... 」"
        ko "「N-nothing? 」"
        fn "「What are you two doing,{p}\ \ at a place like this? 」"
    
        show so 001 with dis
        
        so "「I've got a practice game comin' up,{p}\ \ so I came to make a small bettin' prayer. 」"
    
        show su 001 with dis
        
        su "「I'm escorting him. 」"
        fn "「Hmm. 」"
        so "「Are you guys prayin' too? 」"
        fn "「Well, there's... 」"
        
        show ko 001 at still with dis
        
        ko "「Nonono, we're already done here.{p}\ \ so then, [fn],{p}\ \ let's head to our next location! 」"
    
        show ko at move_offleft_far(0.75)
        
        fn "「Eh? Huh?{p}\ \ Kounosuke, what about the prayer? 」"
    
        show ko 011 at move_farleft(0.5)
        
        ko "「Come on,{p}\ \ I don't care about that anymore! 」"
    
        play sound bosu31
        show shrine at hshake
        show ko at move_offleft_far(0.75)
        
        fn "「A-alright, don't pull on me.{p}\ \ See you later Shun-kun and Soutarou-kun,{p}\ \ maybe next tim-woah! 」"
    
        stop music fadeout 2
        show so 005
        show su 004
        with dis
    
        suso "「...What? 」" 
        
        scene black with sdis
        play music daily04
        scene market
        show ko 005 at center
        with wipe_down_slow
        
        ko "「Wh-why is it that we keep,{p}\ \ running into people on today of all days! 」"
        fn "「Th-that's just the way the world is... 」"
        ko "「This is a time where,{p}\ \ I don't want to encounter so many people.{p}\ \ We keep suddenly running into them! 」"
        fn "「Yeah, yeah... 」"
        "B-but I don't think we should,\nbe running away at full speed."
        "I'm desperately trying to fill my lungs,{p}in this humid Summer air,{p}but it's not easy to breathe."
        
        stop music fadeout 1.5
        
        "On top of that,{p}we're in the shopping district?"
        "This is a place where,{p}you're likely to encounter somebody..."
        who "「I still can't agree with you at all! 」"
        
        scene market
        show ka 001 at midright
        show to 003 at midleft
        with wipe_right
        play music free0346
        
        ka "「That's my line. 」"
        to "「So what? I guess that you of all people,{p}\ \ is supposed to be right? Over my dead body. 」"

        show ka 007 with dis
        
        ka "「We'll see. What are you doing? 」"
    
        scene market
        show ko 005 at center
        with wipe_right
        
        fn "「Ah, I knew it... 」"
        ko "「Here too, not again... 」"
        fn "「What are you two arguing about? 」"
        
        show ko 001 with dis
        show si 004 at offright_far
        
        ko "「Now? It doesn't really matter right? 」{w} {nw}"    
        show ko at move_midleft(.75)
        show si at move_midright(.75)
        extend "{w=.75}{nw}"
        si "「I agree with that. 」"
        
        show ko 006 at jump_up
        
        ko "「Uwaaaa!? 」"
    
        show si 003 with dis
        
        si "「By the way,{p}\ \ those two were arguing about how..."
        si "When you're eating toast with jam,{p}whether you should butter the bread,{p}or leave it as is. 」"
        "Butter the bread..."
        fn "「Every time they meet,\n\ \ they argue over something stupid. 」"
    
        show ko 001 with dis
        show si 001 with dis
        
        si "「I guess it means they're good enough friends,{p}\ \ good enough to argue with each other.{p}\ \ {nw}"
        show ko at move_farleft(1)
        extend "That is, if they're doing it in public. 」"
        ko "「Th-that's right! 」"
    
        show si 005 with dis
        
        si "「Oh... 」"
        
        show ko 002 with dis
        
        ko "「See ya, we have some...{p}\ \ business to take care of! 」"
        
        play sound step03
        show ko at move_offleft_far(0.5)
        
        fn "「S-see you later, Shin-kun... 」"
        
        play sound step03
        show si 001 with dis
        
        si "「...... 」"
        
        stop music fadeout 2
        show si 004 with dis
        
        si "「Hmph. The same as ever. 」"
        
        scene candystoreout
        show ko 007 at center
        with wipe_dr_slow
        play music cicada01
        $ renpy.music.set_volume(0.6, 0.0, channel = "music")
        
        fn "「Ko-Kounosuke.{p}\ \ Th-this is too much for me... 」"
        ko "「S-same here... 」"
        "We both put our hands on our knees,{p}and breathe heavily."
        "The sweat dripping off our cheeks,{p}leaves black stains on the ground."
        "But the strength of the sunlight,{p}makes them disappear in no time at all."
        "Today would definitely be a good day,{p}to hang your laundry out to dry."
        fn "「W-why are you going this...{p}\ \ far to keep a secret? 」"
        
        show ko 006 with dis
        
        ko "「Why? If everybody knew about this...{p}\ \ {nw}"
        show ko 005 with dis
        extend "and if I lost...{p}\ \ that would suck, wouldn't it? 」"
        fn "「That's why!? 」"
        "I-I'm running around at full speed,{p}in this terrible heat just for that?"
        "I don't even have the energy,{p}to get angry about something like that."
        "I've compeletly lost,{p}all the strength in my body."
        
        show ko 007 with dis
        
        ko "「And besides, even if I told everybody,{p}\ \ they'd underestimate me and doubt me.{p}\ \ I just want to prove something by winning. 」"
        fn "「Ah, I see... 」"
        "It doesn't matter anymore."
    
        show ko 001 with dis
        
        ko "「Y-you want to take a break over there? 」"
        "There?"
        
        scene candystore_flavor with dis
        
        "I raise my head and look up ahead.{p}Written on a red and white sign is,{p}\"Shaved Ice\"."
    
        play sound dream
        stop music fadeout 2
        
        fn "「I-it's the candy store. 」"
        "I see, is this why we ran over here?"
        
        play music tam_n06
        scene candystoreout
        show ko 002 at center
        with wipeleft
    
        ko "「Let's see, I'll take one...{p}\ \ strawberry milk, ma'am. 」"
        fn "「I'll have a melon soda. 」"
        
        show ko 005 with dis
        
        ko "「Huh? 」"
        fn "「Of course you're treating me. 」"
    
        show ko 002 with dis
       
        ko "「Umm, if it's at all possible,{p}\ \ could you pay for your own,{p}\ \ and be kind to my wallet, what... 」"
        
        play sound freeze04
        
        "Hohoh."
        fn "「I've been running around the village,{p}\ \ in this terrible heat, just for you,{p}\ \ and you're not gonna buy me a soda?"
        fn "Huh, oh, so that's how it is. 」"
    
        show ko 007 with dis
        
        ko "「A-alright! 」"
        fn "「While you're at it,{p}\ \ I'll take some ice cream later too. 」"
    
        show ko 005 with dis
        
        ko "「Gah...{p}\ \ You're running me dry here. 」"
        
        stop music fadeout 1.5
        scene black with sdis
        pause 1
        play music sad03 fadein 10
        scene candystoreout
        show ko 007 at center
        with sdis
        
        fn "「Now that I think of it,{p}\ \ doesn't this place give you...{p}\ \ sort of a good feeling? 」"
        "With a melon soda in one hand,{p}I talk to Kounosuke."
        ko "「What? 」"
        "With his considerably lighter wallet in hand,{p}Kounosuke looks up at me with bitter eyes.{p}D-did I get a little too carried away?"
        "By the way, today's lunch was,{p}melon soda, okonomiyaki, and some candy.{p}I've got a cola and ice cream set for later."
        "The amount for each item itself,{p}isn't really that much,{p}but when it adds up, it's moderately priced."
        fn "「W-well, for the theme of your picuture. 」"
        ko "「Hm? Oh, maybe. 」"
        "For now I'll bring up a fake subject,{p}he appears to be quite down."
        "The energy that was pulling me around,{p}not too long ago is gone,{p}and he replies in a dull voice."
        "I-I'll treat him to something,{p}as an apology next time."
        "...If I remember."
        fn "「H-hey, if you get the prize money,{p}\ \ that'll be more than enough to recover.{p}\ \ There's no use in being depressed! 」"
        
        show ko 005 with dis
        
        ko "「You're saying such a thing,{p}\ \ while eating all that? 」"
        fn "「Oh... 」"
        "His words pierce me and I can't reply."
    
        show ko 001 with dis
        
        ko "「But, you do have a point. 」"        
        ko "「Yeah.{p}\ \ {nw}"
        show ko 005 with dis
        extend "For now, let's not focus on that. 」"
        "Hoh. That's good.{p}It seems I was somehow successful,{p}in distracting Kounosuke for a moment."
        "With the way things are going,{p}I'll be glad if he forgets about today."
    
        show ta 001 at offleft_far
        play sound ShutterSound
        pause .8
        play sound ShutterSound
        pause .8
        play sound ShutterSound
        pause .5
        show ko at move_farright(0.75)
        show ta at move_midleft(0.75)
        
        ta "「What are you up to? 」"
    
        stop music
        show ko 006 with dis
        
        ko "「UoOOOO!? 」"
        fn "「Oh, Tatsu-onii. 」"
        
        play music daily05
    
        show ta 002 with dis
        
        ta "「Yo. 」"
    
        show ta 001 with dis
        
        ta "「Am I too late to get my picture taken? 」"
        
        show ko 005 with dis
        
        ko "「Eh, err, that's... 」"
        fn "「We're going around so he can...{p}\ \ take pictures for me,{p}\ \ of things to remember the village by."
        fn "Right, Kounosuke? 」"
    
        show ko 006 with dis
        
        ko "「Oh, {w=.3}{nw}"
        show ko 002 with dis
        extend "oh yeah.{p}\ \ That's right! 」"
    
        show ta 008 with dis
        
        ta "「I see. Well you will be going back home,{p}\ \ in less than half a month. 」"
    
        show ko 001 with dis
        
        ko "「What? 」"
        "That reminds me,{p}I am on the second half,{p}of my Summer vacation."
        fn "「Oh, now that you mention it,{p}\ \ it is already that far along.{p}\ \ Man, time sure does fly... 」"
        ta "「You're right. 」"
        
        show ko 007 with dis
        
        ko "「...... 」"
        fn "「Are you getting shaved ice? 」"
    
        show ta 002 with dis
        
        ta "「No, this is why I'm here. 」"
        "Tatsu-onii holds some candy in his hand."
        ta "「This goes very well with sake. 」"
        fn "「Sake, huh... 」"
    
        show ta 001 with dis
        
        ta "「But you have to be a little older for that! 」"
        fn "「What, just a little would be fine,{p}\ \ wouldn't it? Right? Right? 」"
    
        show ta 002 with dis
        
        ta "「I guess there's nothing I can do about it."
        ta "Well then, some time,{p}I'll let you have some,{p}but only just a little."
        ta "Will you come too, Kounosuke? 」"
    
        pause .5
        show ko 006 with dis
        
        ko "「Huh?{p}\ \ {nw}"
        show ko 005 with dis
        extend "What were you talking about?{p}\ \ S-sorry, I wasn't listening... 」"
    
        show ta 008 with dis
        
        ta "「Err... 」"
        fn "「Tatsu-onii's gonna let us drink sake.{p}\ \ Are you going to come too? 」"
    
        show ko 003 with dis
        
        ko "「What? Really?{p}\ \ Let's do it, let's do it! 」"
    
        show ta 001 with dis
        
        ta "「But only just a little. 」"
    
        show ko 002 at jump_up
        
        ko "「Yeah, I got it.{p}\ \ It's a promise, Tatsu-onii. 」"
    
        show ta 008 with dis
        
        ta "「Don't be so self-important,{p}\ \ for someone who wasn't listening. 」"
        fn "「Well then, Kounosuke, don't you think,{p}\ \ we should be getting to our next location? 」"
    
        show ko 001 with dis
        
        ko "「Oh, yeah. 」"
        fn "「See you again some other time, Tatsu-onii. 」"
    
        show ta 002 with qdis
        show ta at move_center(0.75)
        show ko at move_offright(0.75)
        
        ta "「Yeah! But really, only just a little... 」"
        
        scene path
        show ko 001 at center
        with wipe_right
        
        fn "「Nice follow-up back there! 」"
        
        show ko 002 with dis
        
        ko "「Yeah. Thanks, [fn]. 」"
        fn "「What's next? 」"
    
        show ko 001 with dis
        
        ko "「Umm, I think the school would be good. 」"
        fn "「Ah, that would be nice, wouldn't it.{p}\ \ Let's go! 」"
        ko "「Yeah. 」"
    
        $ event_name = "Memories at sunset"
        
        scene school01 red with wipe_up_slow
        pause .2
        
        "With the sun going down,{p}we're on the school's grounds."
        "It's the same as I remember,{p}but everything seems so small now..."
        "There's the front gate,{p}that I passed through every morning,{p}the flower bed everybody took care of..."
        "The gymnastics bar, and the swing set too."
        "I understand it in my head,{p}because I've gotten older..."
        "But the way things look the same,{p}makes me feel uncomfortable,{p}and mixes with a feeling of nostalgia."
        "It's a strange feeling."
        fn "「Everything is so small... 」"
        "Damn, it sounds a lot more cliched,{p}coming out of my mouth...{p}But still, it's true."
        
        play sound ShutterSound
        pause 1
        play sound ShutterSound
        pause .3
        play sound ShutterSound
        pause .5
        show ko 001 red at center with dis 
        
        ko "「Oh. 」"
        fn "「What's wrong? 」"
    
        show ko 005 red with dis
        
        ko "「It looks like I've used up all my film... 」"
        "Then that means..."
        fn "「So, that's it for today? 」"
    
        show ko 001 red with dis
        
        ko "「Looks like it.{p}\ \ I don't have any spare film left. 」"
        "Hooray!\nThis means we won't have to run,{p}around the village anymore."
        "We just stopped not too long ago,{p}the fatigue instantly comes,{p}when I think about it.{p}"
        "So I sit down on a fairly low swing,{p}and throw my legs up."
    
        scene dusk with wipe_down_slow
        
        "Kounosuke sits next to me on a swing as well."
        "I grab on to the swing,{p}stretch by upper body back..."
        "And the view of the deep blue sky,{p}over Minasato fills my field of vision."
        
        stop music fadeout 1.5
        
        ko "「Umm... 」"
        fn "「Hm, what? 」"
        
        play music melodious01
        show ko 007 red at center with dis  
        
        ko "「This is gonna sound strange,{p}\ \ {nw}"
        show ko 001 red with dis 
        extend "but how did you feel when you transferred? 」"
        fn "「Huh?\n\ \ I'm not sure what to say... 」"
        "While raising my body, I try to remember,{p}but since that was five years ago,{p}I won't be able to give a good explaination."
        fn "「Of course I was lonely.{p}\ \ I thought that I would...{p}\ \ never see you guys again. 」"
        "I can't express it with ordinary words,{p}but still, I really did feel that way."
        ko "「Hmm... 」"
        fn "「What's wrong all of a sudden? 」"
    
        show ko 002 red with dis 
        
        ko "「Ah, well... 」"
    
        show ko 001 red with dis 
        
        ko "「Speaking of this, I was thinking,{p}\ \ about how you're going back,{p}\ \ to the city again. 」"
        fn "「O-oh. 」"
        "I see."
        "I wasn't aware of it earlier,{p}but after Summer vacation is over,{p}I'll be leaving this village again."
    
        show ko 003 red with dis 
        
        ko "「It's like the old days all over again.{p}\ \ Feeling that we won't always be together,{p}\ \ and... it got me thinking. 」"
        fn "「Oh, that's an awfully...{p}\ \ serious thing for you to say... 」"
    
        show ko 005 red with dis 
        
        ko "「What do you think I mean by that!? 」"
        fn "「But is that it? 」"
    
        show ko 007 red with dis
        
        ko "「That's mean, you're so cruel... 」"
        fn "「Hahahaha! 」"
    
        show ko 002 red with dis 
        
        ko "「Ahaha! 」"
        "Have I made Kounosuke,{p}into a good-for-nothing comedian,{p}after a little less than half a month?"
        "As I think about that,{p}a lonely feeling starts to rise in me."
        "It seems Kounosuke was thinking the same thing.{p}Then, he suddenly says something unexpected."
    
        show ko 001 red with dis 
        
        ko "「...Hey, [fn]. 」"
        fn "「What? 」"
        ko "「Will you also help me...{p}\ \ search for a scene like today? 」"
        
        menu:
            "A. Sure.":
                jump kounosuke17_accept
            "B. Forgive me.":
                jump kounosuke17_decline
            "C. It's your turn now.":
                jump kounosuke17_reward
    
    ####################################################
    label kounosuke17_accept:
        
        fn "「Sure. 」"
    
        show ko 002 red with dis
        
        ko "「Thank you, [fn]! 」"
        
        jump kounosuke17_cooldown
    
    ####################################################
    label kounosuke17_decline:
    
        if kouno_badstep == True:
            $ kouno_badgo = True #This sets up bad ending for Kounosuke
        else:
            $ kouno_badstep = True #Warning
        
        fn "「Forgive me. 」"
    
        show ko 005 red with dis
        
        ko "「Eh, you don't need to say that... 」"
        
        jump kounosuke17_cooldown
        
    ####################################################
    label kounosuke17_reward:
        
        fn "「It's your turn now. 」"
        
        show ko 005 red with dis
        
        ko "「Huh? 」"
        fn "「You promised to help me,{p}\ \ with my homework, didn't you? 」"
    
        show ko 002 red with dis
        
        ko "「Oh, that's right... 」"
        
        jump kounosuke17_cooldown
    
    #####################################################
    label kounosuke17_cooldown:
        
        "Well, this is called a fatal connection."
        fn "「I can help you again,{p}\ \ but let's take it a little slowly this time. 」"
    
        show ko 001 red with dis
        
        ko "「Oh, yeah. Sorry about that... 」"
    
        show ko 005 red at jump_up
        
        ko "「Oh! But we did get even today,{p}\ \ in the candy store! 」"
        fn "「Oh... 」"
        "Damn it.{p}It seems I dug my own grave,{p}when I made my intentions clear."
    
        show ko 007 red with dis
        
        ko "「That reminds me, the money... 」"
        fn "「S-sorry. I'll treat you,{p}\ \ to something as an apology next time! 」"
    
        show ko 011 red with dis
        
        ko "「At that time,{p}\ \ I too shall eat as much as I want! 」"
        "Kounosuke lets out a madman laugh."
        fn "「Oh... 」"
        "With dark, fiery eyes,{p}Kounosuke emphasizes \"as much as I want\"."
        "I unintentionally flinch,{p}from the feeling of oppression."
        fn "「J-just eat as much as I did today... 」"
        "I should make sure to...{p}keep telling him that."
    
        scene dusk with Dissolve(3)
        pause .5
        
        fn "「What are we doing after this? 」"
        ko "「What should we do? 」"
        fn "「First of all,{p}\ \ I'd like to go somewhere cooler. 」"
        ko "「Oh, if that's the case,{p}\ \ why not come to my house?{p}\ \ There's an air conditioner there. 」"
        fn "「Ah, good. 」"
        "His invitation to air conditioning,{p}is like a charm.{p}I immediately reply."
        
        scene school01 red
        show ko 001 red at center
        with wipe_right
        
        fn "「So, let's hurry up,{p}\ \ and move before we get heatstroke! 」"
        ko "「Okay! 」"
        
        if kouno_badgo == True:
            jump end17
        else:
            jump kounosuke17_confession
    
    #########################################################
    label kounosuke17_confession:
    
        scene path red
        show ko 001 red at center
        with wipeleft
    
        ko "「...... 」"
        ko "「Ah, umm! [fn]... 」"
        fn "「Hm? 」"
    
        show ko 008 red with dis
        
        ko "「Is it, err, okay if we hold hands? 」"
        fn "「Huh? 」"
        "Uhh...{p}I can't answer right away,{p}to his sudden proposal."
    
        show ko 003 red with dis
        
        ko "「Aah! Sorry. After all,{p}\ \ it's strange for guys to do that,{p}\ \ isn't it? 」"
        fn "「Not really, I don't think so. Sure. 」"
    
        show ko 008 red with dis
        
        ko "「Really? 」"
        fn "「Yeah. 」"
    
        show ko 001 red with dis
        
        "Considering how reserved Kounosuke is being,{p}I grab back at his timidly outstretched hand."
        "The pads on the palm of his hand feel warm,{p}and the fur on his fingertips,{p}mildly tickle my hands."
        "But, this is still a little embarrassing.{p}I'm walking hand in hand,{p}with another guy in broad daylight..."
        "Well, it's not bad,{p}but something like this,{p}Ahh!"
        "It's hot. So very, very hot."
    
        show ko 007 red with dis
        
        ko "「Sorry, should I let go? 」"
        fn "「Huh? Oh, ah, sure. 」"
    
        show ko 001 red with dis
        
        ko "「Our hands got sticky with sweat. 」"
        fn "「Ah, you're right. 」"
        "I didn't care about it that much,{p}but now that he mentions it,{p}there are drops of sweat on my hands."
        "It's kind of a gross feeling."
        "Thinking about what just happened...{p}Why did he just randomly hold my hand?"
        "It's not really like him,{p}to do something like that."
        "It's sort of funny,{p}and I accidentally laugh about it out loud."
    
        show ko 005 red with dis
        
        ko "「What's with you all of a sudden? 」"
        fn "「N-no, it's nothing... 」"
        ko "「Eh? 」"
        "I-I wonder why such...{p}a stupid thing made me laugh."
        "Wait, why am I even thinking about this,{p}so much?"
    
        show ko 001 red with dis
        
        ko "「You're weird... 」"
    
        pause .5
        show ko 002 red with dis
        
        ko "「Ahaha! 」"
        
        scene white with Dissolve(3)
        pause .5
        
        ko "\n\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ 「...I love you, [fn]. 」"
        
        jump end17

################################################################
label shun17:

    $ event_name = "The Next Morning"

    scene shun_bedroom_day with sdis
    
    su "「Uunnnn... 」"
    "Thump.{p}Overreacting to the noise heard above me,\nI vigorously jump up."
    "This makes my left brain and right brain\ngo into full operation. In other words,\nI start self-processing afterwords."
    "I roll down and return to my futon.\nOr maybe I should say that after is irrelevant.{p}To summarize the main point, I realize what we did."
    "First, I shake my buzzing head.{p}There are no mistakes in my memory\nof that sort of thing."
    fn "「Aaaaaaaaaaaaah. 」"
    "It was just a natural course of events.\nOr maybe that book is to blame."
    "No matter how I look at it,\na great number of flags came forth."
    "It was inevitable.{p}Shun-kun was urging me as well.{p}That's right. I'm not at fault here."
    "No. It's my fault.{p}Shun-kun didn't know about ejaculation,{p}I taught him about it."
    "It's something you're supposed to to\nwith somebody you love, not a friend."
    "However, it's also the first stage of sexual\nactivity. It was written that an older person\nshould teach him how to respond to an erection..."
    "Masturbation and oral are two very different things.{p}B-but with the way it was twitching,{p}it wanted me to suck it, right?"

    show su 204 at center with wipe_up_slow
    
    su "「[fn]-san? 」"
    fn "「Waaaaaaaaaaaaaah! 」"
    "He suddenly calls my name and frightens me.{p}No, he's been there for a while.{p}Awawa, it's Shun-kun."
    
    show su 202 with dis
    
    su "「Unyuu... [fn]-san, good morning. 」"
    fn "「G-good m-morning. 」"
    "In a gesture appropriate for the mimetic word\n\"nemunemu\", Shun-kun dozes off in his bed."
    "I-I should take action from here,\nshouldn't I!?"
    "I turn towards Shun-kun, who has sat up."
    fn "「Um, Shun-kun!{w=.2} Earlier,{w=.2} not yesterday evening! 」"
    
    show su 201 with dis
    
    su "「You came over to stay over night\n\ \ Funyuu, thank you very much. 」"
    fn "「Y-yeah, don't mention it,\n\ \ You did faint after all. 」"
    
    show su 204 with dis
    
    su "「That's right, I fainted,{w=.2}\n\ \ then you came over,{w=.2}\n\ \ I ate dinner, took a bath, ...{w=.2} 」"
    
    stop music fadeout 1
    hide window
    
    show su 202 with dis
    pause .5
    show su 201 with dis
    pause .5
    show su 204 with dis
    pause .5
    show su 222 with dis
    
    play music free21 fadein 1
    $ renpy.music.set_volume(0.8, 0.0, channel = "music")
    
    "Kaaaaah."
    "Turning red,\nShun-kun is able to grasp it.{p}He remembered, didn't he."
    fn "「Y-you know, last night, there was that. 」"
    
    show su 218 with dis
    
    su "「Hauhauhau, woof. 」"
    fn "「Aaaah. 」"
    
    show su 222 with dis
    
    su "「...I'm embarrassed. 」"
    fn "「S-sorry!{w=.2} Um, I'm really sorry! 」"
    "I put my hands together in front of my face\nand bow deeply. I apologize and feel like running."
    
    show su 220 with dis
    
    su "「Uh, um, I thought you taught me\n\ \ that because I asked...{p}\ \ [fn]-san, don't apologize. 」"
    "Awawawawa.{p}For him to say something like that,\nI went too far and feel regret."
    fn "「Shun-kun...{p}\ \ But I was teaching you a little too quickly,\n\ \ or too much, actually. 」"
    fn "「I regret it, so I'll still apologize.{p}\ \ I'm sorry. 」"
    fn "「That was bad of me in more ways than one... 」"
    
    show su 222 with dis
    
    su "「[fn]-san...{w=.2} no it wasn't. 」"
    
    show su 219 with dis
    
    su "「Please teach me again, won't you...? 」"
    "Shun-kun turns red, not just on his cheeks,{p}but up to his ears."
    "His slightly moist sleepy eyes look at mine,\nand he whispers in a tiny voice."
    "Thank you for those delicious words!{p}I am rejoicing in the back of my head and\ncrushed by what seems to be feelings of guilt."
    fn "「A-again, huh...{p}\ \ Sh-Shun-kun, are you hungry? 」"
    
    show su 201 with dis
    
    su "「!{p}\ \ N-now that you mention it...{p}\ \ I'm really hungry. 」"
    fn "「Want to get something to eat? 」"
    
    show su 202 with dis
    
    su "「Yes! 」"
    "Somehow regaining my sanity, I weave my words.{p}Shun-kun answers energetically, stands from his bed,\nand starts changing his clothes..."
    
    show su 222 with dis
    
    "...intermittently looking at me."
    "Looks like he's a little hesitant.{p}We can't go back to the time when\nhe could undress with me looking, can't we?"
    fn "「Um, I'll... go out, okay? 」"
    su "「O-okay... 」"
    "I leave him with his ears and tail down,\nfeeling awkward.{p}For now I exit the room."
    "Anyways, before eating I must put away{p}the \"Kodori Family ・ Sex Guidebook\""
    
    jump end17


################################################################    
label end17:
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

    jump day18

