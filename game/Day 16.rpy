## Day 16
screen candystore16:
    hbox:
        add "arrow down"
        at marketbounce1
    hbox:
        add "icon_kouya"
        at marketbounce2
    hbox:
        text _("Candy Store")
        xalign .5 yalign .52
        
screen tatsukihouse16:
    hbox:
        add "arrow right"
        at tatsukibounce1
    hbox:
        add "icon_tatsu"
        at tatsukibounce2
    hbox: 
        text _("Tatsuki's House")
        xalign .85 yalign .88
        
screen minasatomap16():
    add "map"
    add "mapdate"
    if favorite == "kouya":
        imagebutton idle "a icon" hover "icon loop"  xpos 372 ypos 249  action Jump("kouya16") hovered Show("candystore16")  unhovered Hide("candystore16") hover_sound "av/audio/click_008.wav"    
    elif favorite == "tatsuki":
        imagebutton idle "a icon" hover "icon loop"  xpos 662 ypos 391  action Jump("tatsuki16") hovered Show("tatsukihouse16")  unhovered Hide("tatsukihouse16") hover_sound "av/audio/click_008.wav"
    hbox:
        text _("{size=+30}August 16")
        at maptime

#####################################################
label day16:
    
    $ renpy.music.set_volume(1.0, 0.0, channel = "music")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound2")
    
    $ day = 16
    $ the_date = _("August 16")    
    $ event_name = _("８月16日")
    
    if favorite == "shun" and meet_gaku != True:
        jump day17

    if favorite == "tatsuki" or favorite == "kounosuke" or favorite == "shun" or favorite == "kouya" or favorite == "shin":
        window hide
        play music birds_chirping
        
        scene sky01 
        show text "{size=+130}August 16" at truecenter
        with Dissolve(.5)
    
        pause 3
        scene black with Dissolve(1)
        pause .4

    if favorite == "tatsuki":
        jump map16
    elif favorite == "kounosuke":
        jump kounosuke16
    elif favorite == "shun":
        jump shun16
    elif favorite == "kouya":
        jump map16
    elif favorite == "shin":
        jump shin16
    else:
        jump day17
        
######################################################
label map16:
    
    scene hbroom with wipe_corner
    pause .2
    fn "「What should I do today? 」"

    play music "<from 2.5>av/audio/free0422.ogg"
    call screen minasatomap16
        

#######################################################
label kounosuke16:    
    
    $ event_name = _("Call from Kounosuke")
    
    scene hbroom with wipeleft
    play music cicada01
    $ renpy.music.set_volume(0.4, 0.0, channel = "music")
    
    "The weather in Minasato is nice today."
    "Now then, I've eaten breakfast,{p}so what should I do today?"
    gm "「[fn]-chan.{p}\ \ Kounosuke-kun's on the phone. 」"
    fn "「Oh, I got it. 」"
    "Kounosuke?{p}I wonder what he wants."
    "I head towards the front door to get the phone."

    play sound step03
    scene hentry with wipe_right
    
    fn "「Hello? 」"
    ko "「Ah, hello [fn]?{p}\ \ Can we meet up today? 」"
    fn "「Today? That should be alright. 」"
    ko "「Really?{p}\ \ Then why don't you come over to my house now?"
    ko "Ah, of course I could...{p}head over your way if that's better. 」"
    fn "「Right now? 」"
    ko "「Oh, yeah.{p}\ \ Is that not okay? 」"
    fn "「No, it's okay, but... 」"
    ko "「Then hurry up, I'll be waiting! 」"
    fn "Ah, wait Kouno... 」"
    
    play sound call00
    pause 1
    play sound call00
    pause 1
    play sound call00
    
    "Boop boop boop."
    "Although he understood,{p}he completely failed to hear the information."
    "He's as careless as ever.{p}Well, I didn't have anything planned,{p}so I should go."
    
    if encounter_yukiharu == True:
        jump kounosuke16_yukiharu_yes
    else:
        jump kounosuke16_yukiharu_no

    ################################################################
    label kounosuke16_yukiharu_yes:
        
        $ event_name = _("Kuri's Appliance Store")
        
        scene black with Dissolve(1)
        scene kouno_house_out with wipe_right
        play music free02
        $ renpy.music.set_volume(0.7, 0.0, channel = "music")
        
        "I finish getting dressed and go on over."
        
        scene kouno_house_in with wipe_right
        play sound tm2_slidedoor000
        show yk 001 at center with wipeleft
        
        yk "「Oh, hello. 」"
        "As soon as I enter the store,{p}I bump into Yukiharu-kun.{p}Seems like he was leaving just now."
        fn "「Ah, hello.{p}\ \ Are you leaving now? 」"
        yk "「Yeah, see ya! 」"     
        
        show yk at move_midright(0.5)
        show ko 001 at midleft with wipeleft
    
        ko "「Yukiharu, are you going somewhere? 」"
        "Kounosuke enters at just the right time."
        fn "「Yo. 」"
    
        show ko 002 with dis
        
        ko "「Ah, I was waiting for you.\n\ \ Hurry and come in, come in. 」"
        "As usual,{p}Kounosuke quickly moves his head back and forth,{p}between Yukiharu-kun and I."
        "He makes a small bitter smile at the same time."
    
        show ko 001 with dis
        
        yk "「Alright, I'm going.{p}\ \ You aren't going to slack off watching the store,{p}\ \ just because your friend is here, are you?"
        yk "See you later! 」"
        
        play sound step03
        show yk at move_offright(0.5)
        show ko at move_center(0.5)
    
        ko "「...... 」"
        fn "「Take care! 」"
        "I cheerfully see Yukiharu-kun off.{p}When I turn around,{p}{nw}"
        show ko 007 with dis
        extend "Kounosuke's shoulders are slightly slumped."
        fn "「What's wrong? 」"
        ko "「Oh, {nw}"
        show ko 006 with dis
        pause .5
        extend "no, {nw}"
        show ko 005 with dis
        extend "it's nothing. 」"
        
        show ko 002 with dis
        
        "I guess even Kounosuke can be damaged by,{p}the things his little brother says?"
        
        scene black with sdis
        
        jump kounosuke16_bedroom
    
    #####################################################
    label kounosuke16_yukiharu_no:
        
        $ event_name = _("Little Tanuki")
        
        scene black with Dissolve(1)
        scene kouno_house_out with wipe_right
        
        play music free02
        
        "I finish getting dressed and go on over."
        
        scene kouno_house_in with wipe_right
        play sound tm2_slidedoor000
        show yk 001 at center with dis
        $ encounter_yukiharu = True
        
        yk "「Oh. Welcome. 」"
        "As soon as I enter the store,{p}I run into a tanuki,{p}that's like a smaller version of Kounosuke."
        "It seems like he's just about to leave."
        fn "「Hello. 」"      
        
        show yk at move_midright(0.5)
        show ko 001 at midleft with wipeleft
        
        ko "「Yukiharu, are you going somewhere? 」"
        "Kounosuke enters at just the right time."
        fn "「Yo. 」"
    
        show ko 002 with dis
        
        ko "「Ah, I was waiting for you.{p}\ \ Hurry and come in, come in. 」"
        yk "「Are you my big brother's friend? 」"
    
        show ko 001 with dis
        
        ko "「What, you don't remember?{p}\ \ See, this is [fn]-onii-chan.{p}\ \ We used to play together. Remember? 」"
    
        show yk 003 with dis
        
        yk "「...... 」"
        "For a short time,{p}Yukiharu-kun looks at me confused,{p}then he says..."
    
        show yk 001 with dis
        
        yk "「I kind of remember. 」"
        "Well it has been 5 years.{p}In those days, Yukiharu-kun was really small.{p}Of course he'd be like that."
        "Once he's finished observing me,{p}he turns around."
        yk "「Oh, nii-san.{p}\ \ I'm telling you just to make sure,{p}\ \ but even though there's nobody here..."
        yk "That doesn't mean you can slack off,{p}watching the store, okay?{p}Alright, I'll see you later! 」"
    
        play sound step03
        show yk at move_offright(0.5) 
        show ko at move_center(0.5) 
        
        ko "「...... 」"
        fn "「Take care! 」"
        "He purposely gives his reminder, then leaves.{p}I cheerfully see Yukiharu-kun off."
        "When I turn around,{p}{nw}"
        show ko 007 with dis
        extend "Kounosuke's shoulders are slightly slumped."
        fn "「What's wrong? 」"
        ko "「Oh, {nw}"
        show ko 006 with dis
        pause .5
        extend "no, {nw}"
        show ko 005 with dis
        extend "it's nothing. 」"
        
        show ko 002 with dis
        
        "I guess even Kounosuke can be damaged by,{p}the things his little brother says?"
        
        scene black with sdis
        jump kounosuke16_bedroom
        
    
    ###########################################################
    label kounosuke16_bedroom:
        
        $ event_name = _("Kounosuke's Ambition")
        
        show bedroom with Dissolve(1)
        
        "I'm shown to a room,{p}and given a floor cushion to relax on.{p}Kounosuke returns with some barley tea."
    
        show ko 001 at center with wipe_right
        
        fn "「Looks like Yukiharu-kun has really grown.{p}\ \ He looks a lot like you did. 」"
        "While saying that, I take a sip of tea."
        ko "「Oh, yeah.{p}\ \ {nw}"
        show ko 004 with dis
        extend "He's already in the upper grades,{p}\ \ of elementary school. 」"
        fn "「I see. He's already that far... 」"
        "The Yukiharu-kun I knew,{p}was always staying close behind Kounosuke,{p}but his older brother was just as shy."
        "He would usually cry,{p}when Torahiko teased him."
        "Whenever that happened,{p}Kounosuke would get seriously angry,{p}and try to catch Torahiko."
        "Yukiharu-kun also constantly,{p}got caught up in Kounosuke's clumsiness."
        "Kounosuke would desperately have to calm,{p}Yukiharu's crying and screaming."
        "But that was when he was small,{p}he really has grown up."
        fn "「Not to worry you or anything,{p}\ \ but sooner or later you know..."
        fn "People are gonna have a hard time,{p}telling who's the older and younger brother. 」"
    
        show ko 005 with dis
        
        ko "「They already have. 」"
        fn "「Oh. 」"
        "Seriously.{p}If he's being compared to an elementary kid..."
        "Then I definitely would expect him,{p}to be a little worried."
    
        show ko 004 with dis
        
        ko "「Well, more and more now,{p}\ \ he's beginning to distance himself away from me."
        ko "Back then, he'd always wanted to be like me.{p}But now he says things like,{p}'I'm not like my big brother!' 」"
        fn "「Are... you lonely? 」"
    
        show ko 006 with dis
        
        ko "「Huh? 」"
    
        show ko 005 with dis
        
        ko "「I wonder... if I am...{p}\ \ But Yukiharu is Yukiharu{p}\ \ As his big brother, I guess..."
        ko "I guess I should say I'm glad,{p}that I'm glad he's growing up. 」"
        "Wow...{p}That's a really mature way to think.{p}Surprising coming out of Kounosuke..."
    
        show ko 001 with dis
        
        ko "「Well, whatever. I think we should...{p}\ \ move on to the main subject. 」"
    
        if kouno_busy == True:
            jump kounosuke16_photos_yes
        else:
            jump kounosuke16_photos_no
    
    #########################################################
    label kounosuke16_photos_yes:
        
        $ event_name = _("Kounosuke's photos")
        show ko 003 with dis
        
        ko "「Ta-da! 」"
        "He presents a large quantity of photographs.{p}Wait a moment, are these bills of money?{p}Is he thinking about putting an end to my poverty?"
    
        show ko 001 with dis
        
        ko "「These are examples of pictures to be submitted,{p}\ \ or rather some material that I gathered."
        ko "But to get the grand prize,{p}I want to hear the opinion of a genuine person 」"
        "Examples?{p}Oh. It's what he was talking about before."
        "If I remember correctly,{p}he needs to have a poem,{p}to go along with his picture."
    
        show ko 005 with dis
        
        ko "「So, what do you think? 」"
        fn "「Hmm... 」"
        "With all these pictures,{p}suddenly being shown to me,{p}I'm not sure what I should say..."
        "I start off by scanning over the photos."
        "Each and every one of them,{p}is nothing but nature scenery.{p}Scenery of things like animals and insects."
        fn "「Err... what was the theme...{p}\ \ of the photos supposed to be? 」"
    
        show ko 002 with dis
        
        ko "「Nostalgic scenery. 」"
        fn "「I wonder if these are nostalgic? 」"

        jump kounosuke16_plan
    
    #######################################################
    label kounosuke16_photos_no:
        
        $ event_name = _("Kounosuke's grand plan")
        show ko 003 with dis
        
        ko "「Ta-da! 」"
        "He pulls out a magazine.{p}Judging from the front cover,{p}it's an arts and literature magazine? "
        "Seems like it.{p}Looks like something an old man would read."
        fn "「What is this? 」"
        
        show ko 001 with dis
        
        ko "「I just happened to find it,{p}\ \ at the bookstore the other day.{p}\ \ Here, look at this. 」"
        "Printed on the open page is an article,{p}about recruiting for reader's contributions."
    
        scene black with Dissolve(1)
        
        "~Mass Recruitment for Reader Contributions~{p}This month's theme is \"Nostalgic Scenery\"."
        "A photo accompanied by a short article,{p}for this (Omission)"
        "Not only will the winner be used in this magazine,{p}the wonderful, sparkling grand prize,{p}is a monetary award of 100 million yen..."
        "And the latest digital camera as a present."
    
        scene bedroom
        show ko 001 at center
        with Dissolve(1)
        
        "Looking closely,{p}there's a small simplification,{p}on the cover of the magazine."
        fn "「This is it...? 」"
        ko "「Yep, that's it. 」"
        fn "「Have you thought about applying? 」"
    
        show ko 002 with dis
        
        ko "「Of course! 」"
    
        show ko 001 with dis
        
        ko "「I'm saving money for the city,{p}but it's not easy to gather.{w} But, I could get the grand prize. 」"
        
        show ko 002 with dis
        
        ko "「The prize money could be used,{p}\ \ for my city-dweller aspirations."
        ko "Not only that,{p}\ \ I could also get a digital camera? 」"
        fn "「Oh, I see... 」"
        "I don't think it's as simple as that.{p}First of all, in the recruitment there's,{p}\"a poem must accompany the picture.\""
        "I'm pretty sure I remember Kounosuke,{p}didn't have the best grades in Japanese..."
    
        show ko 001 with dis
        
        ko "「So, if I'm aiming to get the grand prize,{p}\ \ I thought that I should also hear,{p}\ \ the opinion of a genuine person 」"
        "A genuine person...{p}what nationality am I?"
        "Without a good understanding,{p}I'm presented with some photos.{p}I start off by scanning over them."
        "In the photographs there's mostly scenery,{p}of the forest on the outskirts of the village."
        "Things like small animals, plants,{p}and insects are the main subjects."
        "Looks like things from a picture book,{p}or the front cover of a notebook."
        "The theme of the pictures seems to be,{p}\"cherish nature\" as opposed to...{p}nostalgic scenery."
        
        show ko 005 with dis
        
        ko "「What do you think? 」"
        fn "「U-umm...\n\ \ This is nostalgic? 」"
    
        jump kounosuke16_plan
    
    #################################################
    label kounosuke16_plan:
        
        $ event_name = _("Unextraordinary Tanuki")
        show ko 007 with dis
        
        ko "「Hmm, they're not any good, are they... 」"
        fn "「Well, that's my opinion.{p}\ \ By the way, which one do you think is good? 」"
    
        show ko 006 with dis
        
        ko "「Huh? 」"
    
        show ko 001 with dis
        
        ko "「Even though you ask that,{p}\ \ there's nothing... 」"
        fn "「Hey! 」"
        "I don't think that's good."
    
        show ko 005 with dis
        
        ko "「Well, I only took so many pictures,{p}\ \ if only there was one more thing,{p}\ \ that I could've photographed... 」"
        fn "「...But do you think that,{p}\ \ what you have here says 'nostalgia'? 」"
    
        show ko 006 with dis
        
        ko "「Hm?{p}\ \ {nw}"
        show ko 005 with dis
        extend "{w=.5}I really do think that,{p}\ \ the countryside full of nature says that. 」"
        fn "「It's supposed to be scenery,{p}\ \ but these are mostly just pictures,{p}\ \ of bugs and animals, aren't they? 」"
    
        show ko 002 with dis
        
        ko "「There's also lots of flowers! 」"
        fn "「That's not the point. 」"
        fn "「Even if you do have animals and flowers,{p}\ \ Don't you think that they're just...{p}\ \ usually just 'cute' or 'beautiful'? 」"
        ko "「What? {nw}"
        show ko 006 with dis
        extend "Oh...{p}\ \ {nw}"
        show ko 005 with dis 
        pause .5
        extend "Yeah, I see that too... 」"
        fn "「Don't you yourself have a place,{p}\ \ that you think is 'nostalgic', for example? 」"
        ko "「Hm?{nw}"
        show ko 001 with dis
        extend " Yeah, why? 」"
        fn "「Didn't you think that you should've...{p}\ \ taken a picture of that place? 」"
    
        show ko 005 with dis
        
        ko "「What? How is what you're saying relevant? 」"
        "He's so rude."
        fn "「...I'm going through all this trouble,{p}\ \ to have a serious discussion,{p}\ \ with this tanuki and yet... 」"
    
        show ko 006 with dis
        
        ko "「Oh, sorry. 」"
    
        show ko 005 with dis
        
        ko "「But I wonder if that...{p}\ \ could get me the grand prize? 」"
        fn "「Even if you aim for your opponents,{p}\ \ having poor favorability,{p}\ \ I don't think your results will be good. 」"
    
        show ko 001 with dis
        
        ko "「I see!{p}\ \ You're right. 」"
    
        show ko 003 with dis
        
        ko "「Thanks, [fn]. You're very helpful. 」"
        fn "「Don't mention it. 」"
    
        show ko 002 with dis
        
        ko "「Well then, let's go right now! 」"
        show ko at move_offright(0.25)
        fn "「Huh? 」"
        
        "Kounosuke suddenly stands up,{p}grabs the camera sitting on his desk,{p}and puts it around his neck."
        "He rushes out to the hallway."
        fn "「W-wait a sec Kounosuke,{p}\ \ where are you going? 」"
        ko "「I'm searching for scenery now, of course! 」"
        fn "「Wait! 」"
        ko "「We need to strike while the iron's hot!{p}\ \ Let's seize the day! 」"
        "No, he doesn't understand."
    
        scene kouno_house_out with wipe_right
        
        fn "「Aren't you supposed to,{p}\ \ be watching the store!? 」"
    
        show ko 006 at center with wipe_right
        
        ko "「Oh... 」"
        "Kounosuke stops in the middle,{p}of putting on his shoes."
        "He had already forgotten,{p}what Yukiharu-kun said just a short while ago."
    
        show ko 005 with dis
        
        ko "「I've got something I'd...{p}\ \ like to ask of you instead... 」"
        fn "「Do you think this is my house? 」"
    
        show ko 007 with dis
        
        ko "「Oh... I guess I can't...{p}\ \ do anything about it today. 」"
        "He is visibly disappointed,{p}and slumps his shoulders,{p}perhaps looking a bit pathetic."
        "But in Kounosuke's case,{p}I think it's good that he remembered,{p}to calm down a little. Yeah."
        fn "「If you want to, how about we go out,{p}\ \ and look for scenery some other time? 」"
    
        show ko 001 with dis
        
        ko "「What? Really? Is that alright? 」"
        fn "「Well, it is Summer vacation. 」"
    
        show ko 002 with dis
        
        ko "「Seriously!? Really!? Thank you.{p}\ \ As I thought, this is what...{p}\ \ best friends are for! 」"
        "Kounosuke grabs my hand,{p}with both of his and grins."
        fn "「In exchange, are you going to help me,{p}\ \ with my homework? 」"
    
        show ko 003 with dis
        
        ko "「Of course.{p}\ \ Something like that is definitely okay! 」"
        "Yes!{p}Just as planned."
        "I should be able,{p}to get through math with this."
        "As a matter of fact,{p}it seems math was a subject,{p}that Kounosuke was strong in."
        "Although I'm talking about elementary school,{p}he was amazingly fast,{p}at doing math in his head."
        "His math scores were always,{p}equal to or better than Shin-kun's."
        "Well, I can't expect much,{p}from him in other subjects..."
        "But his mental calculating,{p}should be plenty of help."
        "Those cryptic numbers and symbols,{p}are like fighting through Hell."
        "If he thinks that he's just,{p}keeping his end of the bargain,{p}this should be easy."
    
        show ko 002 with dis
        
        ko "「Well then we'll go,{p}\ \ right away tomorrow, please remember! 」"
        fn "「Huh? 」"
    
        show ko 001 with dis
        
        ko "「Alright.{p}\ \ I'll make sure not to put it off,{p}\ \ since I won't have to watch the store."
        ko "I've got my eye on the prize! 」"
        fn "「Wa-wait a minute Kounosuke? Hello? 」"
        "He said tomorrow,{p}I thought he was planning on,{p}doing it a about day or two later..."
        "Suddenly it's tomorrow?"
        ko "「I'll try my best,{p}\ \ not to dissapoint you, [fn]! 」"
        fn "「Oh, uhh, yeah... 」"
        "Staring straight ahead,{p}with my hand able to be caught,{p}I have no choice but to answer."
        "......"
        "H-hmm.{p}I think I really stepped in it this time."
        "But I should be fine as long,{p}as we're not causing any trouble..."
        
        jump end16
        
#######################################################
label tatsuki16:
    
    $ event_name = _("Unexpected!")

    scene map
    hide screen tatsukihouse16
    pause .01
    scene workplace2 with sdis
    play music free0258
    show ta 001 at center with dis
    
    ta "「Do,{w=.2} dodo,{w=.2} dododo... 」"
    "The sun's rays are strong today,\neven though the days are supposed to get shorter now.{p}The sun burned me as it slowly crossed the sky."
    
    show ta at move_midright(0.5)
    show ni 001 at midleft with dis
    
    ni "「If you're humming while you work,\n\ \ it's going to distract me. 」"
    
    show ta 002 with dis
    
    ta "「There we go. 」"
    
    show ni 004 with dis
    
    ni "「Hey. Are you listening?{p}\ \ I said stop humming that ear-damaging song. 」"
    
    show ta 008 with dis
    
    ta "「And why shouldn't I sing at work?{p}\ \ It's fine, so you shouldn't care. 」"
    
    show ni 001 with dis
    
    ni "「I want to do my work seriously.{p}\ \ Isn't that obvious? 」"
    
    show ta 003 with dis
    
    ta "「What was that?{p}\ \ {w=.2}{nw}"
    show ta 004 with dis
    extend "It sounded like you said I don't do my work seriously. 」"
    
    show ni 002 with dis
    
    ni "「That's not what it sounded like.{w=.2} That *is* what I'm saying. 」"
    
    show ta 008 with dis
    show cu 004 at offright behind ta
    
    ta "「They used to sing at work even in the old days.{p}\ \ {w=.2}Sea shanties and counting songs got popular enough to\n\ \ become folk songs. 」"
    ta "「So while you're working with your hands,\n\ \ of course you'd sing! 」{nw}"
    show ni 004 with dis
    extend ""
    ni "「That doesn't make sense at all! 」"
    cu "「Okay okay, excuse me.{p}\ \ {w=.2}{nw}"    
    show cu at move_offleft(3)   
    extend "Passing through, coming up from behind.{p}\ \ {w=.2}Excuse me, coming through. 」"
    "Why is everyone so calm?"
    fn "「So hot...{w=.2} I can't think anymore. 」"
    "There's no pool, is there?{p}The river then. Let's go to the river.{p}Let's go swim in the river."
    "Yay! I'm gonna jump in!{p}...This river is crunchy."
    
    scene workplace2 with dis
    show tp 401 at farright with dis
    
    tp "「All right, that's enough for today. I'm closing up. 」"
    
    $ encounter_tappei = True 
    
    show cu 002 at midleft with dis
    
    cu "「Good work. Let's finish up quick 'n easy! 」"
    
    show ni 001 at midright with dis
    
    ni "「Thanks for all your hard work, everyone. 」"
    tp "「Except for that one guy singing. 」"
    
    show ta 003 at farleft behind cu with dis
    
    ta "「...! 」"
    
    show ta 010 with dis
    
    ta "「It was Chuukichi. 」"
    
    hide tp
    show tp 403 behind cu
    with wipeleft 
    
    tp "「Little bastard! 」"
    
    show tp at hit_left
    pause .2
    play sound hit_p07
    show cu 009 at hit_right
    $ chuu_beat += 1
    
    cu "{size=+15}「Bwoh-! 」"
    "..."
    
    show ta 008 with dis
    
    ta "「Geez, gimme a break.{p}\ \ For a guy to sing in the middle of work... 」"
    
    show tp 401 with dis
    
    tp "「Yeah, those guys are unreliable.{p}\ \ Gotta punish them. 」"
    
    hide tp
    show tp 403 at center
    with explosion
    
    tp "{size=+15}「Hey.{w=.2} Did you think you could trick\n\ \ me, you rotten little braaat!! 」"
    
    play sound hit_p09
    show ta 003 at jump_up
    
    ta "{size=+15}「Guhooo-! 」"
    
    hide ta
    hide cu
    with wipe_right
    
    tp "「I'll lead you by the nose, dumbass! 」"
    "Pool,{w=.2} pool,{w=.2} a pool of sand."
    
    scene workplace2
    show tp 403 at farleft
    show ni 001 at midright
    with wipe_right
    show cu 008 at midleft with dis
    
    cu "「So...{w=.2} Why was I hit? 」"
    
    show tp 401 with dis
    
    tp "「Oh, that. I just hit you without\n\ \ really thinking about it. 」"
    
    show cu 006 with dis
    
    cu "「That's retarded. 」"
    
    show cu 004 with dis
    
    cu "「Gaack...! 」"
    
    hide cu with wipe_right
    show tp 402 with dis
    
    tp "「For the rest of you still moving,\n\ \ let's finish up already. 」"
    
    show ni 003 with dis
    
    ni "「Okay, understood. 」"
    tp "「Now, maybe I'll take a quick break. 」"
    
    stop music fadeout 2
    pause 2
    play music free0205
    $ renpy.music.set_volume(0.8, 0.0, channel = "music")
    
    yukino "「{cps=0}Boss, it's an emergency! 」"
    
    $ encounter_yukino = True 
    
    show ni 001
    show tp 401
    with dis
    
    tp "「What is it? Why are you making that face? 」"
    yukino "「It seems Tetsuya-san got into some sort of accident!{p}\ \ You have to go look right now! 」"
    
    show tp 403 with dis
    
    tp "「What!? This isn't anything to laugh about.{p}\ \ Okay, I'll go over there now.\n\ \ I'm leaving the rest to you. 」"
    
    play sound step03
    show tp at move_offright(0.5) 
    
    yukino "「You'd better hurry and finish up the work.{p}\ \ Even if you can't help worrying,\n\ \ in times like this the only thing to do is wait. 」"
    
    stop music fadeout 2
    show ni 004 with dis
    
    ni "「Understood. 」"
    yukino "「Dear me...{w=.2} even though you\n\ \ all wake up at the same time, Tetsuya is the only one\n\ \ to have fallen flat on his face? 」"
    yukino "「Was he still half asleep? 」"
    
    show ni 005 with dis
    
    ni "「It's because of the song. 」"
    yukino "「Song? 」"
    
    scene black with sdis
    scene old_house_inside with sdis
    play music cicada01 fadein 3
    $ renpy.music.set_volume(0.3, 0.0, channel = "music")
    
    $ event_name = "A Replacement"
    
    show cu 008 at center with dis
    
    cu "「Wonder if Tetsu-san's all right... 」"
    fn "「Yeah. Hopefully it's nothing serious. 」"
    
    hide cu with dis
    show tp 401 at farright with dis
    
    tp "「We're going home. 」"
    
    show te 003 at center with dis
    
    te "「Forgive me.{w=.2} I'm sorry to\n\ \ have caused you all to worry. 」"
    
    show ta 006 at farleft behind te with dis
    
    ta "「Tetsu-san, are you all right? 」"
    
    show te 001 with dis
    
    te "「Yes. I was in an accident, but since it happened after\n\ \ I delivered goods to a client, it was all right. 」"
    
    hide ta with dis
    show cu 008 at farleft behind te with dis
    
    cu "「It's not that, are you hurt, Tetsu-san?{p}\ \ There's some bandages, but it's not bad, is it...? 」"
    
    hide cu with dis
    show ta 006 at farleft behind te with dis
    
    ta "「That's right, we could just make the stuff again.{p}\ \ But if your body gets hurt, and it can't get fixed,\n\ \ there's nothing we could do. 」"
    
    show te 003 with dis
    
    te "「Just as it looks, the doctor made\n\ \ a real show of the treatment\n\ \ but there really is nothing to it. 」"
    te "「I should be fine with\n\ \ a bit of rest. 」"
    fn "「That's a relief,{w=.2} it seems like we can relax then. 」"
    
    show tp 403 with dis
    
    tp "「Keh! For a worker to get hurt in\n\ \ such a trivial accident... 」"
    tp "「The body is the foundation of everything,\n\ \ and you need to concentrate more. 」"
    te "「Chief, I cannot apologize enough.{p}\ \ For me to have blundered outside the workplace... 」"
    tp "「Ah?{w=.2} Just look at this mess ?{w=.2} I can't stand it,\n\ \ so you'd better prepare yourself.{p}\ \ {nw}"
    show tp 401 with dis
    extend "Now, how're you holding up? Here, let me see. 」"
    
    show te at briefzoom
    
    te "「Chief...{w=.2} Owowowow! 」"
    ta "「I thought as much.{p}\ \ {nw}"
    show tp 403 with dis
    extend "Did you really think I'd buy an answer like that? 」"
    tp "「My eyes are too good to be fooled\n\ \ by a lie about your endurance. 」"
    
    hide ta with dis
    show ni 005 at farleft behind te with dis
    
    ni "「His endurance? So Tetsu-san's\n\ \ condition isn't good, after all. 」"
    te "「No, this is no problem.{p}\ \ Look, I can move like so with no... {nw}"
    show te at hit_right
    extend "{w=.2}urgh... 」"
    
    hide ni with dis
    show ta 005 at farleft behind te with dis
    
    ta "「Tetsu-san. 」"
    tp "「Dumbass. I don't have enough time to\n\ \ be giving work to an injured man. 」"
    
    show tp 406 with dis
    
    ta "「Just rest for a while.{p}\ \ Go visit your family, or something.{p}\ \ If you understand, then I don't need to say anything. 」"
    
    show te 001 with dis
    
    te "「Chief... 」"
    
    show tp 403 with dis
    
    ta "「Listen up! Starting tomorrow,\n\ \ I'm not letting you put one foot in the workplace.{p}\ \ Come back after you've healed up. 」"
    ta "「And now this talk is over.{p}\ \ I'm taking the first bath. 」"
    
    hide tp with dis
    
    "Tappei-san finished speaking,\nthen turned on his heel and left."
    
    show te 003 with dis
    
    te "「I am sorry, Chief.{w=.2} I will get better quickly,\n\ \ and come back soon.{w} I have troubled everyone by this,\n\ \ but I will counting on you all while I am away. 」"
    
    show cu 002 at farright behind te with dis
    
    cu "「Yes, 'course!{p}\ \ Please get well soon. 」"
    
    show ta 002 with dis
    
    ta "「Just leave it to me, Tetsu-san.{p}\ \ I'm here, after all. 」"
    
    hide cu with dis
    show ni 005 at farright behind te with dis
    
    ni "「I find that the most worrisome thing here. 」"
    
    show te 001 with dis
    
    te "「Well then, excuse me. Be careful everyone. 」"
    fn "「Take care of yourself! 」"
    
    hide te with wipe_right
    show cu 008 with dis
    
    cu "「He left. 」"
    
    show ta 008 with dis
    
    ta "「Haah, did Tetsu-san fall from there?{p}\ \ It must've hurt... 」"
    ni "「There's no helping it, we all have to do our best. 」"
    
    show cu 004 with dis
    
    cu "「*Sigh* Terrible... 」"
    "He's an apprentice too,\nbut not having a veteran around makes a difference.{p}Whatever Tetsu-san said was always reliable."
    
    scene old_house_inside with wipe_right
    
    tp "「[fn], you got a moment? 」"
    fn "「Yes. 」"
    "What's going on?{p}Tappei-san calling me over like this\nis making my heart pound."
    
    scene black with sdis
    play music daily04
    $ renpy.music.set_volume(0.7, 0.0, channel = "music")
    scene tatsukihouse_inside with sdis
    show tp 401 with dis
    
    tp "「Sorry about this, but could you come\n\ \ with me to the spot he fell?{p}\ \ I want you to fill in for him for a little bit. 」"
    fn "「Eeehhh!? 」"
    tp "「I told Tetsu to rest,\n\ \ but without him around,\n\ \ things will be tough. 」"
    fn "「But am I okay for this? 」"
    tp "「I'm not saying you need to climb up somewhere high.{p}\ \ If you help me as you have been,\n\ \ it'd really help me out a lot. 」"
    
    show tp 402 at center with dis
    
    tp "「Seems like I'm remembering a lot of things too. 」"
    fn "「Well...{w=.2} Okay.{p}\ \ If it helps everyone,\n\ \ I can't really refuse. 」"
    tp "「Thanks. I wasn't expecting this,\n\ \ but you'll be a huge help. 」"
    fn "「It's all right.\n\ \ I'm a member of the Midoriya Group, after all. 」"
    fn "「I've been having most of meals here lately,\n\ \ and it's not that much of a leap to staying over. 」"
    
    show tp 401 with dis
    
    tp "「I'm really sorry about this,\n\ \ making you come along when things are like this.{p}\ \ {w=.2}Well, get changed and get ready so you can stay over. 」"
    fn "「Eh!?{w} starting today? 」"
    
    show tp 406 with dis
    
    tp "「Of course. It's best to work there in the morning,\n\ \ which means it's best for you to stay over at my house.{p}\ \ If it's going to be a problem, then leave things as is. 」"
    fn "「...I'll go grab some things. 」"
    tp "「Come over when it's time to eat. 」"

    hide tp with wipe_right
    
    "Something amazing just happened...\nI'd better take advantage of this."
    
    stop music fadeout 1.5
    scene black with sdis
    play sound door_slide
    scene hentry with sdis
    
    fn "「I'm home. 」"
    gp "「Welcome back, [fn]. 」"
    gm "「Welcome home. Will you be eating dinner here today? 」"
    "The usual scene greeted me as I got back:{p}Grandpa is reading a newspaper on the porch, and\nGrandma is preparing to make the evening meal."
    fn "「Hey, there's something I need to talk about. 」"
    gp "「Did something happen? 」"
    gm "「Yes, yes, just a moment. 」"
    fn "「The thing is,{w=.2} I've taken a\n\ \ part-time job at Tatsu-nii's house. 」"
    gm "「Oh, Midoriya-san's home? 」"
    fn "「Yeah, that's right...{w} Is it all right if I stay\n\ \ overnight and work over there for a little bit?{p}\ \ One of the usual workers there had an accident. 」"
    gm "「Oh my. 」"
    gp "「Is that so? I don't mind, do what you like.{p}\ \ It'll be a good experience. 」"
    gp "「Also, if you're a man and you become needed at work\n\ \ that's something to be proud of.{w} Do your best. 」"
    gm "「Yes, we're supporting you. 」"
    fn "「Eh?{w=.2} it's okay? 」"
    "It's surprising how easily they gave me permission.{p}They could've listened a little more."
    gm "「It's okay, you don't need to worry about us.{p}\ \ We're all adults now. "
    gm "「While you're at it, I've been wondering if there was\n\ \ someone you liked... 」"
    gp "「Be sure to introduce us if you do. 」"
    fn "「I said I was only going for work!{p}\ \ Well, if that's settled, I'll be off. 」"
    gm "「Oh my, starting today? So sudden. 」"
    fn "「They said that since I'm on-site tomorrow,\n\ \ it'd be best to go today. 」"
    gm "「Is that so? That means you won't need dinner, right? 」"
    gp "「Oh well, we'll just eat by ourselves. 」"
    fn "「Sorry!{w=.2} It's just for a little bit. I'll be back. 」"

    scene black with sdis

    $ event_name = _("Curry for Dinner")

    play music daily02
    $ renpy.music.set_volume(0.7, 0.0, channel = "music")
    scene old_house_inside with sdis
    
    "I returned to the Midoriya Group's to find both a room\nprepared for me and dinner ready.\nI went and sat down with everyone in the living room."
    fn "「I'm back. 」"

    show ta 002 at center with dis
    
    ta "「You're late. 」"
    "It hadn't been that long since the accident,\nbut everyone had calmed down somewhat."

    hide ta with dis
    show tp 201 at center with dis
    
    "Tappei-san was smoking his favorite pipe,\nand seemed to be watching baseball on the TV."
    tp "「Oh, you're back? 」"
    tp "「Food's almost ready, so wash your hands and sit down. 」"
    "He turned his neck to face me while he spoke."
    fn "「Um... About my baggage... 」"
    tp "「Just set it down over there.\n\ \ It's no big deal,\n\ \ since you'll just be changing clothes. 」"
    fn "「O-{w=.2}okay. 」"

    scene black with sdis
    scene old_house_inside with sdis
    
    fn "「Whew. Done washing. 」"

    show tp 201 at center with dis
    
    tp "「Oh, all done? 」"
    "Tatsu-nii's house specializes in temple construction,\nso the workers both live and work here\n(Tetsuya-san is an exception, since he commutes)."
    "So, at mealtimes, everyone gathers\naround the low table to eat."
    tp "「We were waiting for you, so if your hands are washed,\n\ \ sit down already. I want an evening drink already. 」"
    "Tappei-san has his own low table.{p}In his case, it's probably for him to hold his sake..."
    "Incidentally, aside from when he's smoking his pipe,\nthat table gets a lot of use."

    hide tp with dis
    show ta 002 at midleft with dis
    
    ta "「There's space next to me that's open, so sit there. 」"

    show ni 005 at midright with dis
    
    ni "「It's not so much that it's open,\n\ \ it's that the table is so big.{p}\ \ So he could sit wherever he likes. 」"
    
    show ta 004 with dis
    
    ta "「Shut up! You got a problem or something? 」"
    ni "「Not really... It was just on my mind.{p}\ \ I don't really care where everyone sits. 」"
    fn "「Hmm. Well since Tatsu-nii invited me to,\n\ \ I'll go sit there after all. 」"
    
    show ta 002 with dis
    
    ta "「Look, [fn] really does get it.{p}\ \ The complaining egghead was wrong. 」"
    ni "「Hmph... 」"
    "There really is no helping these two, is there.{p}Looks like today's meal is going to be pretty busy too."

    hide ni with dis
    show cu 004 at midright with dis
    
    cu "「My stomach's eatin' itself. 」"
    yukino "「Sorry to keep you waiting.{p}\ \ We're having curry today. 」"
    
    show cu 002 at jump_up
    
    cu "「F'real!? Oh man, I love curry! 」"
    "Yukino-san came out of the kitchen\nwith a large pot, and carried\nit out to the living room."
    "Wow...{w=.2} That much food could probably feed thirty."
    yukino "「I'll serve the rice like always,\n\ \ so dish as much sauce as you like and eat. 」"
    
    show ta 008 with dis
    
    ta "「Curry...? I had nothing but that at camp. 」"
    yukino "「What? If you don't want it, you don't have to eat it. 」"
    
    show ta 005 with dis
    
    ta "「No, it's not that I don't want any... No way. 」"
    
    show cu 005 with dis
    
    cu "「Thanks for the food! 」"

    hide cu with dis
    show ni 001 at midright with dis
    
    ni "「Thank you for the food. 」"
    
    show ta 004 with dis
    
    ta "「Hey, don't start eating so fast. 」"
    
    show ni 003 with dis
    
    ni "「But you're not eating. 」"
    ni "「We'll take it all, so you don't need to worry. 」"

    show ta at jump_up
    pause .2
    
    ta "「Huh? What'd you say!? I'm not gonna lose!!{p}\ \ Ma, gimme some food. I want a large serving. 」"
    yukino "「Oh, a large serving? 」"

    hide ta
    hide ni
    with wipe_right
    
    "She passed over Tatsu-nii's regular bowl, filled with\nseveral times the usual amount of rice.\nIt was like a mountain of rice."
    "That's not a a large serving,\nthat's a super-size mega serving..."
    yukino "「Here you are. [fn]-kun, do you want a\n\ \ regular-sized serve?{w} Everyone eats a lot here,\n\ \ so I don't know how much you want. 」"
    yukino "「Is this much all right? 」"
    fn "「Yes, that's fine. 」"
    "It was probably caution on my part,\nbut that's still quite a bit."
    "If I didn't work so hard during the day,\nit'd be more than I could eat."

    show ta 001 at midleft with dis
    
    ta "「Okay, let's eat.{p}\ \ {w=.2}[fn], you don't need to hold back,\n\ \ so just dig in. 」"
    fn "「'kay. I'll eat my fill, then. 」"
    ta "「Now, we eat!{w=.2}{nw}"
    show ta 004 with dis
    extend " I'm not gonna lose to Horseface! 」"
    
    show ni 004 at center with dis #!#Check position
    
    ni "「I don't know what this losing business is...{p}\ \ But I have no intention of failing any challenge!{p}\ \ I'll win against you! 」"

    hide ni with dis
    show cu 001 at midright with dis
    
    cu "「*shovel shovel*!{w=.2} *snarf snarf*!{w=.2} *chew chew*! 」"

    hide cu with dis
    show ni 004 at midright with dis    
    show ni 003 with dis
    
    ni "「If dinner is curry, then...{p}\ \ I should have an advantage if\n\ \ I put furikake on my rice! 」"
    fn "「Furikake? 」"
    
    show ta 006 with dis
    
    ta "「Ugh... 」"

    hide ni with dis
    show cu 002 at midright with dis
    
    cu "「Delicious,{w=.2} this is delicious! 」"
    yukino "「Chuu-chan, there's seconds if you want any,\n\ \ so be sure to eat a lot.\n\ \ If you don't, you won't get any bigger. 」"
    
    show cu 001 with dis
    
    cu "「'kay! 」"
    "What kind of challenge was it in the first place...?"

    hide cu with dis
    show ni 004 at midright with dis
    
    ni "「What's this 'Ugh' business. Rude! 」"
    
    show ni 001 with dis
    
    ni "「When the meal is curry, isn't the rice portion rather\n\ \ plain?{w} That's why the whole dish becomes more\n\ \ interesting if you put furikake on the rice. 」"
    
    show ni 003 with dis
    
    ni "「Isn't that how it is? 」"
    
    show ta 008 with dis
    
    ta "「You know, I always thought you were some\n\ \ showy know-it-all,{w=.2} but you're just a random idiot... 」"
    
    show ni 004 with dis
    
    ni "「What do you mean by idiocy?\n\ \ I don't want to hear that from you! 」"
    
    show ta 010 with dis
    
    ta "「Could it be that you've been carrying\n\ \ around furikake until there was curry served? 」"
    
    show ni 001 with dis
    
    ni "「That isn't the case. Haven't I always had some on me?{p}\ \ You really are slow to have not noticed until now. 」"
    
    show ta 005 with dis
    
    ta "「Gross... It makes the food terrible... 」"
    
    show ni 002 with dis
    
    ni "「Hmph. It seems a guy with low\n\ \ standards can't understand. 」"

    hide ni with dis
    show cu 001 at midright with dis
    
    cu "「*Chomp chomp*{w=.2} so tasty...! 」"
    yukino "「'The wise lord prepares his own exclusive furikake,'\n\ \ isn't it? 」"
    
    show ta 006 with dis
    
    ta "「Ma, are you really okay with strange\n\ \ stuff being done to the food you made? 」"
    yukino "「I don't really mind.{p}\ \ It's enough for me if people eat it happily.{p}\ \ Meals are times when you shouldn't hold yourself back. 」"

    hide cu with dis
    show ni 003 at midright with dis
    
    ni "「There's still many people in the world who don't know\n\ \ this, but at any place that serves curry they'll\n\ \ definitely have furikake to go with it. 」"
    ni "「In specialty shops and cafes, and soba stores.{p}\ \ Even the beef bowl shops... 」"
    
    show ta 004 with dis
    
    ta "「No way... 」"
    
    show ta 008 with dis
    
    ta "「Besides, we're eating at home,\n\ \ so can't we just finish this\n\ \ by putting all the rice into the sauce? 」"
    
    show ni 005 with dis
    
    ni "「Geez... you really are a blockhead.{p}\ \ {nw}"
    show ni 003 with dis
    extend "It can't be helped.\n\ \ I'll give you some of my special sprinkles. 」"
    
    show ni at move_center(0.25) 
    show ta 003 at jump_up
    
    ta "「Quit that, don't put that on! 」"
    "Before Tatsu-nii could do anything,\nhis rice was covered with furikake."
    
    show ta 004 with dis
    
    ta "「Bastard!! What the hell did you just do!? 」"
    
    show ni 001 with dis
    
    ni "「There's no problem.\n\ \ The rice's flavor isn't so plain now. 」"
    "It didn't show on his face, but when he'd\nsprinkled the furikake to his satisfaction,\nNikaidou-kun had a triumphant tone in his voice."

    show ta at jump_up
    pause .2
    
    ta "「...don't screw with me, jackass!{p}\ \ Who told you to put it on!?{p}\ \ I can't eat it like this! 」"
    
    show ni 002 with dis
    
    ni "「What are you getting mad about? You should thank me.{p}\ \ There shouldn't be any reason to shout.{p}\ \ And never mind that, just try it. 」"
    
    show ta 008 with dis
    
    ta "「Huh? Eat it? {nw}"
    show ta 004 with dis
    extend "{size=+15}Don't you take that tone to\n\ me, you ass!! 」"
    "The furious Tatsu-nii violently grabbed\nChuukichi-kun's head with a lot of force."

    hide ni with dis
    show cu 006 at midright with dis
    play sound puu75
    show cu at move_center(0.5)
    
    cu "「Huh? 」"
    ta "{size=+15}「DIE, DAMNIT!! 」"
    
    play sound don20
    show cu at move_offright_far(0.25)
    $ chuu_beat += 1
    
    "Tatsu-nii lifted Chuukichi-kun with one hand,\nthen threw him at Nikaidou-kun with all his strength."
    
    scene black with wipe_right
    scene old_house_inside with wipe_right
    show ni 004 with wipe_right
    show cu 006 at offleft
    
    ni "「What the!? 」"
    
    play sound swing30_c
    hide ni with wipe_right
    show cu at move_offright_far(0.5)
    
    "Almost as if he knew what was coming,\nNikaidou-kun smoothly dodged the flying Chuukichi-kun."
    
    scene black
    show cu 006 at offleft
    with wipe_right
    show cu at move_offright_far(0.5)

    cu "「Uwaaaahhhhh!! 」"
    
    scene black with wipe_right
    scene old_house_inside with wipe_right
    show tp 201 at center with wipe_right
    show cu 006 at offleft_far
    
    "Chuukichi-kun flew past Nikaidou-kun,\nto where Tappei-san was sitting...{w} {nw}"    
    show cu at move_center(0.25)
    extend "{w=.25}{nw}"
    show tp 203 at jump_up
    show cu at jump_up
    extend "{w=.1}{nw}"
    show cu at move_midright(0.25) 
    
    tp "{size=+15}「Why you!! 」"
    "With a dull crash, Chuukichi-kun\ntumbled onto the tatami mats."

    hide cu with wipe_right
    
    ta "「Oh, crap. 」"
    tp "「... 」"

    stop music fadeout 3
    play sound dishes
    
    "Tappei-san put down his pipe,\nand sat silently without turning around."
    "The silence was heavy as it fell upon us."
    "It's sort of like the calm before the storm.{p}A strange silence where even cicadas are quiet."
    fn "「...Are you all right? 」"
    "Since Tappei-san was being unusually quiet,\nI spoke to him automatically."
    yukino "「Ah, it's dangerous to talk to him. Go over there. 」"
    "That was careless. A cold shiver ran down my spine."
    tp "「Haven't you been taught to be quiet at mealtimes? 」"
    "Finally, Tappei-san turned around and spoke quietly.{p}This quiet was so much worse than his usual violence..."
    tp "「Who made noise while we were eating,\n\ \ and said it was okay to throw things around?\n\ \ Speak up. Who said that? 」"
    cu "「U-uuungh. My head's all spinning 'round... 」"
    "As Tappei-san's anger increased,\nChuukichi-kun finally got up."
    tp "「No one's saying anything... Why'd you guys make\n\ \ such a fuss? 」"
    
    show tp 203 at shivering
    
    "His body shook with rage,\nand his face darkened before our eyes."
    tp "「... 」"

    play sound don08
    
    tp "「When you eat, you eat without making a sound!!!{p}\ \ I'll beat the hell out of you all!!! 」"
    
    show cu 006 at midright with dis
    
    cu "「Eh? 」"
    
    play sound tm2_hit002
    show cu at move_center(0.25)
    
    "I don't know if it was unconscious or not,\nbut Tappei-san firmly grasped Chuukichi-kun's head."
    tp "{size=+15}「DIE! 」"

    play sound standup
    
    "Tappei-san stood on one leg, twisted his body so that\nhis back was towards us, and brandished him wildly."
    
    play sound freeze04
    
    fn "{size=+15}「To-{w=.7}{cps=0}Tornado Pitcher!! 」"
    "Chuukichi-kun was thrown with the pitching\nform of the great Hideo Nomo."

    $ chuu_beat += 1
    
    play sound gun09_r
    show cu at move_offleft_far(0.25)
    scene black with wipe_right

    scene old_house_inside
    show ta 003 at center
    with wipe_right
    show cu 006 at offright
    
    ta "「Look out! 」"
    
    play sound swing40_a
    hide ta with wipe_right
    show cu at move_offleft_far(0.25)
    
    "In an instant, Tatsu-nii crouched,\ndodging Chuukichi-kun's speeding form."
    
    scene black with wipe_right
    scene old_house_inside
    show cu 006 at offright
    with wipe_right
    show cu at move_offleft_far(0.25)
    
    cu "{size=+15}「Hiiiiiii!! 」"

    scene black with wipe_right
    scene old_house_inside with wipe_right
    show cu 006 at offright
    
    "Chuukichi-kun sped through the air, towards Yukino-san."
    fn "{size=+15}「Watch out!! 」"
    yukino "「What? 」"
    
    play sound swing30_c
    show cu at move_offleft_far(0.25) 
    
    "Yukino-san nimbly avoided Chuukichi-kun, then returned\nto her spot as if nothing had happened."
    
    scene black with wipe_right
    scene old_house_inside
    show cu 006 at offright
    with wipe_right 
    
    cu "「Currryyy...! 」"
    "He kept going, straight through the sliding door,\n{nw}"
    play sound fuurin
    pause 2
    extend "and disappeared into the big blue sky...{w=1}"
    
    show tp 206 at center with dis
    
    tp "「Now shut it and eat!!{p}\ \ I'm going into the bath.{p}\ \ Keh, this is disgusting. 」"

    hide tp with wipe_right
    
    fn "「... 」"
    
    show ni 001 at midright with dis
    
    ni "「Well, shall we hurry and finish up? 」"
    "At the dining table that was so noisy a minute ago,\nno one spoke a word."
    
    show ta 006 at midleft behind ni with dis
    
    ta "「Can't be helped, let's eat... 」"
    "And so Tatsu-nii hesitantly brought some of the\nfurikake-covered rice to his mouth."
    
    scene black with sdis
    scene old_house_inside
    show ta 008 at midleft
    show ni 001 at midright
    with sdis
    play music free51
    $ renpy.music.set_volume(1.0, 0.0, channel = "music")
    
    ta "「...Not as bad as I thought.{p}{w=.2}Never thought I'd try it. 」"
    fn "「Can I get a little bit? 」"
    "I took a little bit of his rice."
    fn "「...Good enough. 」"
    
    show ni 003 with dis
    
    ni "「See? Just as I said.{w=.2} Sheesh...{p}\ \ You guys need to be less adamant about these things. 」"
    ni "「It's not just fixing old things.{p}\ \ Isn't it part of a carpenter's job to\n\ \ pick up new things? 」"
    
    show ta 010 with dis
    
    ta "「It was still better as it was before. 」"
    fn "「Yeah, it's not like it needed anything extra... 」"
    
    show ni 005 with dis
    
    ni "「You guys don't understand a thing.{p}\ \ {nw}"
    show ni 004 with dis
    "Rice is the only thing worth eating to you guys!! 」"
    
    show ni 001 with dis
    
    ni "「It's a little improper... But try having an eating\n\ \ contest with me. We'll try with both the rice portion\n\ \ and the rice-with-furikake portion!! 」"
    
    show ta 004 with dis
    
    ta "{size=+15}「I don't want it, asshole! 」"
    
    show ni 004 with dis
    
    ni "「Even though I was saying that out of kindness,\n\ \ what kind of attitude is that!! 」"
    ta "「A great big help!! 」"
    ni "「You're always like this... 」"
    
    show ta 008 with dis
    
    ta "「Heh, and you... 」"
    
    hide window
    show ni 003 with dis
    show ta 003 with dis
    show ta 004 with dis
    show ni 005 with dis
    show ni 004 with dis
    show ta 006 with dis
    show ta 004 with dis
    
    yukino "「You had better eat it all up.\n\ \ You'll make the Boss mad again. 」"

    scene black with sdis
    scene old_house_inside with sdis
    show ta 002 at midright with dis
    
    ta "「Maan, I'm full. 」"

    show cu 002 at midleft with dis
    
    cu "「My stomach's so big. 」"
    "We finished our meal, and now we're\njust relaxing in the living room."
    yukino "「Everyone, if you're finished eating,\n\ \ then you should hurry and take a bath. 」"
    
    show cu 001 with dis
    
    cu "「'Kay. 」"
    
    show ta 001 with dis
    
    ta "「Into the bath then, huh? 」"
    fn "「It's been so long since I've been in your bath...{p}\ \ It was so big we could all get in. 」"
    ta "「Oh yeah. Tora went in a whole bunch of times,\n\ \ I seem to remember... 」"
    
    show cu 002 with dis
    
    cu "「Starting today, we'll all be going in, huh? 」"
    fn "「Ahaha. That's true. 」"
    "I glance at the happy-looking Chuukichi-kun,\nand I can't help but smile too."

    hide cu with dis
    show ni 001 at midleft with dis
    
    ni "「Sorry, but I'm going in last, like always. 」"
    ni "「It is big, but that's no reason for us to\n\ \ all bathe at once. 」"
    
    show ta 004 with dis
    
    ta "「Neat freak... Are you that against being seen naked? 」"
    
    show ni 003 with dis
    
    ni "「It's not that. My beautiful body is something\n\ \ that all of you should see more.{p}\ \ No, I just want to bathe and relax alone. 」"
    ta "「Can't you read the atmosphere, you insensitive jerk? 」"
    
    show ni 002 with dis
    
    ni "「Hmph. I'm already tired today.{p}\ \ If I want to get into the bath, it's all right if I go\n\ \ at my own convenience, isn't it? 」"

    hide ni with dis
    
    ta "「Bastard... 」"
    fn "「Come on, like Nikaidou-kun's saying,\n\ \ aren't there times when you just want to be alone?{p}\ \ Let's go wash up and get refreshed. 」"
    
    show ta 001 with dis
    
    ta "「Well, yeah...{w} Let's do it. 」"
    
    show cu 002 at midleft with dis
    
    cu "「Let's go then! 」"
    fn "「Oh yeah, what do I do with my luggage...? 」"
    
    show cu 008 with dis
    
    cu "「The room Nikaidou-san and I use is big,{w=.2}\n\ \ and it can still fit some more people,\n\ \ so how about you put it 'n there? 」"
    cu "「There should be 'nother futon\n\ \ {nw}"
    show cu 002 with dis
    extend "so it's totally okay! 」"
    fn "「I guess so... 」"
    
    show ta 004 with dis
    play sound bosu35
    show old_house_inside at vshake 
    ta "{size=+15}「No!!{w=.25}{nw}"
    play sound bosu35
    show old_house_inside at hshake
    extend " Totally not okay!! 」 "    
    fn "「Eeh!? 」"
    ta "「[fn]'s staying in my room. 」"
    fn "「Your room is pretty big with just you,\n\ \ but with me there too it'd probably be a bit small... 」"
    
    show ta 006 with dis
    
    ta "「Y-{w=.2}you're staying.{w=.2}{nw}"
    show ta 008 with dis
    extend " It's an event.{w=.2}{nw}"
    show ta 003 with dis
    extend " You are, aren't you?{p}{nw}"
    show ta 006 with dis
    extend "Right? It's okay, you'll come to my room, yeah? 」"
    fn "「Well, all right... I'll do that then. 」"
    
    show ta 007 with dis
    
    ta "「Hehehe, you wanted to stay in my room that much?{p}\ \ I give up... 」"
    "So pushy... I'm the one giving up here."
    
    show ta 001 with dis
    
    ta "「You've brought a towel to change with, right?{p}\ \ Just take out the stuff you need and go on ahead.{p}\ \ I'll take your stuff to my room. 」"
    fn "「Y-{w=.2}yeah... Tatsu-nii? 」"
    
    show ta 008 with dis
    
    ta "「Yeah? 」"
    fn "「Don't go through it. 」"
    
    show ta 003 at briefzoom
    
    ta "「D-dumbass, I won't do that.{p}\ \ Don't you trust me? 」"
    
    show cu 004 with dis
    
    "Tatsu-nii seems a little fidgety, and that bothers me.{p}I'm happy that I get to stay with him though."
    
    show cu 001 with dis
    
    cu "「Aniki, you can go in first.{p}\ \ I have to go up and pick up my change of clothes too. 」"
    fn "「OK. I'm going in then. 」"
    
    stop music fadeout 1
    scene black with sdis
    play music daily04
    $ renpy.music.set_volume(0.7, 0.0, channel = "music")
    
    "I take my clothes off outside the bathroom,\npull open the glass door, and go in."
    
    play sound tm2_slidedoor000
    scene tatsukihouse_bath1 with blind_skinny
    
    "It's about as big as I remember it.\nA bunch of buff workers could easily fit in here."
    fn "「It's nice. 」"
    
    play sound mizu07
    scene tatsukihouse_bath2 with dis
    
    "Inside is an excellently-made cypress bathtub,\nfilled to the brim with hot water."
    fn "「I guess I'll start off with a wash then. 」"
    "I saw the corner of the bathroom where I could wash up."
    fn "「Let's see, Skael Oyal Loshun?{p}\ \ Oh, that must be Yukino-san's treatment.{p}\ \ The others are... 」"
    "Among the beastman lotions,\nthere's some beastman body shampoo."
    "If I remember right... Using improper ones for hair\nand fur would hurt the fur?"
    "My head would be fine, but I probably \ncan't wash my body with that."
    "This flashy golden bottle is... Huh.{p}Extra-Rich Golden Beast Moisture?{p}Must be Nikaidou-kun's."
    "I'd better stop, since I'm making so much noise.{p}Can't use it on my body anyway."
    "Umm, what's over here?"
    fn "「Oh there it is, the body soap. 」"
    "Yep, it has body soap written on it.{p}Let's see now..."
    "Body Soap Dragon Screw!!"
    "「Mochu Guerrila Oil guarantees smooth scales.\nYou too can have scales as smooth and glossy as glass!\nSay goodbye to dryness today! 」"
    fn "「What is this!? 」"
    "I obviously can't use this.{p}No matter how I look at it, it's for dragonmen.{p}Also, what's Mochu Guerrila Oil?"
    "It's something ButagoXXra would pronounce like...{p}I'll stop."
    fn "「Huh, could it be there isn't any body soap? 」"
    "What should I do...?"
    "Well first off, I'll wash my head.{p}There's shampoo and rinse at least."
    "Whew, I'm tired today too..."

    scene tatsukihouse_bath1 with qdis
    
    ta "「Bath time, bath time. 」"
    cu "「'm so sweaty, I wanna wash it off. 」"
    
    scene tatsukihouse_bath2 with sdis
    
    "As I was washing my head with the beastmen shampoo,\nI could hear their voices coming in from the other\nside of the glass door."

    play sound standup
    
    ta "「Okay then...{w=.2} W-what? 」"
    cu "「Young Master, have you been gettin' bigger again? 」"
    ta "「Really? Maybe I'm not done growing or something... 」"
    cu "「Can't be, yer not a kid anymore.{p}\ \ Please stop, if you get any bigger,\n\ \ I jus' can't think of what might happen. 」"
    cu "「If you end up being around three metres,\n\ \ gimme a little bit of that height please.{p}\ \ It'll bother me if I can't measure up. 」"
    ta "「Gahahaha! Well, if I do break that height,\n\ \ I'll give you some.{p}\ \ Either way, I'm not gonna get that big. 」"
    cu "「There's still a chance, though your\n\ \ stomach is much more likely to get bigger. 」"
    ta "「Shut up. Now hurry up,\n\ \ take off your clothes, and get in. 」"

    play sound standup
    
    cu "「Ah...{p}\ \ I forgot I tossed my toothbrush\n\ \ away for bein' worn out. 」"
    ta "「It won't kill you if you don't brush for one day. 」"
    cu "「No way, there's stuff livin' in dirty teeth. 」"
    ta "「So you have dirty teeth...? 」"
    cu "「The general store's still open,\n\ \ I should make it if I go by bike. 」"
    ta "「You can use mine... 」"
    cu "「That's no good either!{p}\ \ ...I'll go buy one now. 」"
    ta "「Oh well, no helping it. Be careful going. 」"
    cu "「Got it. 」"
    
    play sound tm2_slidedoor000
    show ta 102 at center with dis
    
    ta "「[fn], I'm coming iiin. 」"
    fn "「I'd say 'Okaaay', but aren't you supposed\n\ \ to say that before you get in? 」"
    "I have shampoo in my eyes, so I can't confirm it,\nbut I heard the door open and footsteps come in."
    
    show ta 108 with dis
    
    ta "「Don't sweat it, I brought you something nice, look.{p}\ \ Soap is fine, right? 」"
    fn "「Whoa, thanks! 」"
    
    show ta 101 with dis
    
    ta "「We've only got shampoo and rinse for beastmen,\n\ \ but you don't mind, do you?\n\ \ Everyone uses it, anyway. 」"
    fn "「Not at all.{p}\ \ If everyone's used it so much,\n\ \ I don't think there'll be a problem. 」"
    
    show ta 102 with dis
    
    ta "「Okay. Here, I'll scrub your back. 」"

    hide ta with wipe_right
        
    "Saying that, Tatsu-nii got behind me and started\nrummaging around."
    fn "「Eh!? I'll be fine washing it by myself. 」"
    ta "「Don't be shy. 」"
    "Since I can't open my eyes,\nmaybe I'll just let it happen."
    ta "「Here I go. 」"
    
    play sound hit_s06_r
    show tatsukihouse_bath2 at hshake
    "{size=+15}*Grind*"    
    fn "「Nyaaa-! 」"
    "After a soft feeling,\nsomething sharp dug into my back..."
    fn "「Owowow! Hey, Tatsu-nii!{w=.2} I'm human, remember!{p}\ \ Treat me more gently. 」"
    ta "「Sorry, sorry, accidentally used a claw.\n\ \ Next time will be okay. 」"
    "Washing my head quickly sounds like a good plan..."
    ta "「Now, doesn't that feel good? 」"
    fn "「Your fingers are pretty skilled, so yeah. 」"
    "He made a mistake in the beginning,\nbut after that he confidently\nscrubbed my back with deft hands."
    "It's like he's giving me a massage as he's washing me."
    fn "「By the way, where's Chuukichi-kun? 」"
    "Before, I could only hear Tatsu-nii's voice.{p}It doesn't feel like anyone else is here,\nand it's strange that Chuukichi-kun isn't talking."
    fn "「He did say he didn't have his toothbrush. 」"
    ta "「Yeah, he wanted to get a kebab or something.\n\ \ He went to go buy one. 」"
    fn "「A kebab??? 」"
    ta "「You grill a lump of meat, slice it up,\n\ \ then eat it like a sandwich. 」"
    fn "「There's nothing like that in Minasato.\n\ \ Maybe in Kazenari, but that sounds suspicious. 」"
    ta "「Yep.{w=.2} They probably don't sell it. 」"
    fn "「You're telling me one thing,\n\ \ but I could hear you earlier.{p}\ \ Didn't he go out to buy a toothbrush? 」"
    ta "「What, you knew?{p}\ \ I thought you were just keeping quiet. 」"
    fn "「Even if I didn't know, I wasn't being quiet... 」"
    "So what is a kebab...?"
    fn "「Let me wash my head. 」"
    ta "「Sure, leave it to me. 」"
    
    play sound water01_c
    pause 1
    
    "In the next moment, hot water poured\ndown from above like a waterfall."
    fn "「Tatsu-nii, I wasn't asking you to\n\ \ wash my head for me... 」"
    fn "「Besides, the normal time to wash your head is when you\n\ \ have a small bucket or something to wash your face.\n\ \ How many times has it been? 」"
    "I know."
    "When Tatsu-nii gets into the bath,\nhe gets into the giant tub\nand washes up in one sitting..."

    show ta 108 at center with dis
    
    ta "「Oh yeah, it's like that? Next is rinsing, right?{p}\ \ I'll pour it on for you. 」"
    fn "「It's fine, I can do it myself. 」"
    "I'm thankful for Tatsu-nii's full bath service,\nbut at this rate I don't think I will survive."
    
    show ta 102 with dis
    
    ta "「I said don't be shy, didn't I?\n\ \ We're just two naked guys hanging out. 」"
    fn "「Oh yeah. Now it's my turn to wash your back. 」"
    
    show ta 107 with dis
    
    ta "「Eh?{w=.2} No thanks, I'm fine. 」"
    "It seems like the scrubber didn't\nthink of getting scrubbed,\nas Tatsu-nii was all confused."
    fn "「Oh? Being shy now, are you? 」"
    
    show ta 105 with dis
    
    ta "「It's not like that... 」"
    "Is it embarrasing to let yourself be scrubbed?{p}Tatsu-nii's bewilderment showed through."
    "It's cute how he's fidgeting like that."
    fn "「Okay then. 」"
    "This time I forced Tatsu-nii to sit down,\nand I began working on his back."
    
    stop music fadeout 1.5
    hide ta with dis
    
    fn "「Tatsu-nii, your back is so huuuge. 」"
    "Now that I think about it,\never since Tatsu-nii came in,\nthis is the first time I've properly looked at him."
    "All because I had my eyes closed during all that time."
    "The wet scales shone,\nand it felt a little sexy somehow."
    ta "「Stop that, you're tickling me. 」"
    "Do I just suck or something?"
    "Or is he just naturally ticklish?{p}Tatsu-nii was bearing with it and not moving."
    "I briskly wash the reluctant Tatsu-nii's back."
    fn "「Since you're a dragonman,\n\ \ is it okay if I put more force into it? 」"
    ta "「Don't mess around. 」"
    fn "「Come to think of it,\n\ \ you've got some small wings on your back. 」"
    
    play music free58
    
    "On his broad back, there are some tiny wings."
    ta "「Oh, them. 」"
    ta "「You remember? When we were little kids,\n\ \ you guys saw them and were totally convinced I could\n\ \ fly in the sky with them. 」"
    ta "「You'd all beg me to take you guys up,\n\ \ and when it didn't happen you'd all cry...{p}\ \ It was a huge pain... 」"
    fn "「Haha. That happened? 」"
    ta "「Yeah, it did. 」"
    ta "「I couldn't do anything about it,\n\ \ so I had to make a promise. 」"
    ta "「I said I couldn't do anything then,\n\ \ but I'd take you up someday,\n\ \ even though I couldn't fly. 」"
    fn "「Ohh, I just remembered! When you made that promise,\n\ \ I was so happy about it... 」"
    ta "「As I thought, you totally forgot about it.{p}\ \ That's why I'm fixing the airplane to begin with. 」"
    fn "「Eeh, really!? I was just a kid...{p}\ \ and that promise was from so long ago. 」"
    ta "「Gahahaha, you idiot. You asking if we had\n\ \ any other kiddy promises from back then? 」"
    "He's laughing for my sake."
    "Even after I forgot about that promise."
    fn "「Sorry, I forgot about it.{p}\ \ It's cruel of me to have forgotten about that... 」"
    ta "「Don't apologize. 」"
    ta "「Normally, it'd be impossible for\n\ \ you to remember something that old, anyway. 」"
    ta "「Besides, didn't you say so before?{p}\ \ That feeling of wanting to fly\n\ \ might be a dragonman's instinct."
    ta "「With that promise, you may have triggered it all. 」"
    fn "「I... 」"
    ta "「Don't sweat it.{w=.2} There's the promise and all that,\n\ \ but now I want to fly for my own sake too.{p}\ \ That's why if I do fly, I'll take you along. 」"
    fn "「Thanks, Tatsu-nii. 」"
    "Tatsu-nii's back seems even bigger than I remember."
    "As far as I'm concerned, it's huge."
    
    show ta 102 with dis
    
    ta "「All right, if we're done scrubbing,\n\ \ let's get into the tub. 」"

    scene black with sdis
    
    $ event_name = _("Ready for bed?")

    stop music fadeout 1.5
    scene old_house_inside with sdis
    play music shop03
    
    yukino "「You can watch TV for a bit,\n\ \ but get to bed soon. 」"

    show ta 004 at center with dis
    
    ta "「But this is the good part! 」"

    hide ta with dis
    
    "Souichirou" "「Sachiko-san... I love you. 」"        #!#Check for error
    "Sachiko" "「No, Souichirou-san...{p}\ \ If Mother finds out about that, I... 」"
    "Lately, Tatsu-nii and everyone else have\nbeen getting into this serial drama.{p}If I remember, it's titled The Madam of Karuizawa."
    "The original work was set in Karuizawa,\nand it seems to be written about the\nlady's love life."
    "Even though it's broadcast in a primetime slot, it's\nunfolding as a regular daytime muddled love/hate drama."
    
    show ta 003 at center with dis
    
    ta "「Aaah, Souichirou-san! What are you doing?{p}\ \ You have a wife, don't you? 」"

    show cu 006 at farleft with dis
    
    cu "「That's bad, yer gonna get busted if you do that... 」"

    hide ta
    hide cu
    with dis
    
    "Souichirou" "「Sachiko-san!! 」"
    "Sachiko" "「Nooo! 」"
    "The couple in the TV are totally having an affair."

    show ni 005 at farright with dis
    
    ni "「...This is stupid. 」"

    show ta 004 at center behind ni with dis
    
    ta "「What was that? Stop watching it, then. 」"
    
    show ni 003 with dis
    
    ni "「It's none of your business what I do with my time. 」"
    "He wants to watch, doesn't he..."

    hide ta
    hide ni
    with dis
    
    "Narration" "「Thus, the Madam of Karuizawa,\n\ \ overthrown by Souichirou, who was protecting Sachiko,\n\ \ snuck out of his estate, and ran into the forest... 」"
    "Narration" "「To be continued. 」"

    show ta 007 at center with dis
    
    ta "「Wait, it's over? 」"

    show cu 002 at farleft with dis
    
    cu "「Things are really lookin' bad... 」"
    "That was stupid..."

    show cu 001 with dis
    
    cu "「Well, show's over. 」"

    show ta 001 with dis
    
    ta "「Guess we should get to bed, then. 」"
    fn "「I guess. 」"
    
    show cu 002 with dis
    
    cu "「G'night! 」"

    hide cu with wipe_right
    
    fn "「Good night! 」"
    
    show ta 007 with dis
    
    ta "「All right, let's head upstairs. 」"
    
    stop music fadeout 1.5
    scene black with sdis
    play music night_insects
    $ renpy.music.set_volume(0.4, 0.0, channel = "music")
    scene tatsuki_bedroom with sdis
    show ta 001 at center with dis
    
    ta "「Okay, time to go to sleep. 」"

    hide ta with wipe_right
    
    "We went up to Tastu-nii's room,\nand it was the same as ever."
    "Tatsu-nii went from his bold\npersonality to his neat one,\nbut there was only one futon laid out."

    play sound standup
    
    fn "「You said sleep... But where should I sleep? 」"

    show ta 201 at center with dis
    
    ta "「With me, right? 」"
    
    show ta 202 with dis
    
    ta "「You're small, so I can sleep in there just fine. 」"
    fn "「That's not the problem.{p}\ \ Also, why are you taking off your clothes? 」"
    
    show ta 208 with dis
    
    ta "「You've got a set of fundoshi to wear to sleep,\n\ \ don't you?{w=.2} It's a time to be naked.{p}\ \ But since you're here I'll let you off on that. 」"
    "He says that so naturally."
    
    show ta 202 with dis
    
    ta "「Right, bedtime.{w=.2} I'm turning off the lights. 」"
    fn "「*Sigh*... 」"
    "I gave up and got into the futon."
    
    play sound on03
    pause .5
    play sound on03
    scene black with dis
    
    "Tatsu-nii's futon was as big as him,\nwhich is to say it was huge. It shouldn't be a problem\nfor me to get in together with him."
    fn "「Oh yeah, where are the pillows? 」"
    ta "「Want to use my arm? 」"
    fn "「Uhh, that's a little... 」"
    ta "「No go, huh... I'll do this, then. 」"
    "Tatsu-nii grabbed me from behind,{nw}"
    play sound puu75
    extend " hugging me against him."
    fn "「Tatsu-nii!? 」"
    ta "「How about that? 」"
    fn "「Uh, even though I don't have my pillow,\n\ \ I've been turned into a pillow myself... 」"
    ta "「Gahaha! Come on, it was a joke.{p}\ \ We've got tomorrow coming up, so go to sleep. 」"
    "I removed myself with my hand, {nw}"
    play sound standup
    extend "and laid myself facing{p}the opposite direction."
    fn "「Yeah. 」"
    "..."
    ta "「My bad. I was so happy that you were staying here that\n\ \ I got too excited about it. 」"
    fn "「It's fine, no worries.{p}\ \ I could understand from looking at you. 」"
    fn "「Hey, Tatsu-nii. 」"
    ta "「Yeah? 」"
    fn "「I know the futon's thin, since we're in the\n\ \ countryside and in the shadow of the mountain,\n\ \ but I'm feeling a little cold..."
    fn "「Would you mind being a body pillow? 」"
    ta "「You're so spoiled. Well, it can't be helped.{p}\ \ If you put it that way, I'll do you a favour.{p}\ \ Only for today, though. 」"

    play sound standup
    pause 2
    
    "Once again, I was embraced by thick, burly arms,\nand settled on top of Tatsu-nii's warm breast."
    fn "「Goodnight, Tatsu-nii. 」"
    ta "「Night, [fn]. 」"
    "It's hot enough now that I feel I might sweat,\nbut the warmth feels good.{p}I'll never forget this feeling."

    scene black with dis

    jump end16

#######################################################
label shun16:

    stop music fadeout 1.5
    scene hbroom with dis
    play music cicada01
    
    "The warmth from the earth rises up and flows\ninto the air this early afternoon."
    "I lie down in only my shirt and underwear\non the tatami mat, and give in to the\nlanguidness and heat."
    "Suddenly, I was hit with fatigue from camping.{p}I don't want to move even a single millimeter..."
    
    play sound phone_ring loop fadein 1.5
    
    "...then the phone rings at a time like this.{p}And I'm the only one in the house.{p}There's nothing I can do but go get it."
    
    scene hentry with wipeleft
    stop sound
    play sound phone_pickup
    
    fn "「Yes, this is [ln]. 」"
    
    scene black with dis    
    stop music fadeout 1
    
    "The mainly apologetic voice was Shun-kun's mom's.{p}I don't remember what came after that very well.{p}I answered 「I'm going 」, and flew out of the house."
    "It seems Shun-kun fainted."
    
    scene shun_house_door with sdis
    pause 1.5
    play sound doorbell1
    pause 3
    
    "Bing-bong. "
    "I push the intercom button,\nwhich is unusual to have in this village.{p}Based on the situation, Shun-kun should be alone."
    door  "「... 」"
    door  "「(stomp stomp stomp stomp) 」"
    su "「Yes, who is it? 」"
    fn "「Shun-kun!?{w=.2} A-are you alright?! 」"
    su "「Funyuu, yaay, [fn]-san♪{p}\ \ You came over for me? I'm opening up now♪ 」"
    door  "「(Clunk) 」"
    fn "「Wha- Shun-kun!? 」"
    "Did he hurt himself!?"
    su "「...Funyuu, please wait a minute. 」"

    play sound KeyA
    pause .5
    scene shun_house_entry
    show su 002 at center 
    with dis
    
    play music pops_003
    $ renpy.music.set_volume(0.8, 0.0, channel = "music")
    
    su "「Hehee, good afternoon [fn]-san♪ 」"
    fn "「G-Good afternoon,\n\ \ are you well enough to be out of bed? 」"
    
    show su 015 with dis
    
    su "「Umm, were we supposed to meet up today? 」"
    fn "「I got a phone call from your mom. 」"
    
    show su 002 with dis
    
    su "「Hehee, well I'm glad, please come up. 」"
    fn "「No no no, sorry, that's not it. 」"
    
    show su 015 with dis
    
    su "「Umm, were we supposed to meet up today? 」"
    "Aaahh, in addition to looping,\nthis conversation isn't connecting."
    "For now, we need to get\na mutual understanding of the situation..."
    
    play sound cellphone loop    
    show su 001 with dis
    
    su "「Ah, excuse me [fn]-san. 」"
    
    hide su with dis
    play sound phone_pickup
    
    su "「Yes, this is Kodori. 」"
    phone  "「... 」"
    su "「Mother! 」"
    phone  "「... 」"
    su "「To [fn]-san?{w=.2} Got it. 」"
    "Push. "
    "Shun-kun presses the hold button and covers the\nmouthpiece of the phone with his hand.{p}He's so diligent."
    
    show su 001 at center with dis
    
    su "「[fn]-san, my mother wants to talk to you. 」"
    fn "「To me?{w=.2} S-Sure. 」"
    
    show su 002 with dis
    
    su "「Please take it♪ 」"
    "I'm handed the receiver."
    "Did she wait until I got here to call?{p}Including what I ignored earlier,\nI'm filled in on what's going on."
    
    scene black with sdis
    scene kodori_house with blind_vert
    stop music fadeout 1
    play music free0258 fadein 1
    $ renpy.music.set_volume(0.8, 0.0, channel = "music")
    
    "Shun-kun and his parents went\nto his grandfather's house this morning."
    
    show su 001 at center with dis
    
    "While they were preparing for the Bon Festival,{p}{nw}"
    show su 006 with dis
    extend "Shun-kun seemed to have fainted."
    
    hide su with wipe_down
    pause .2
    
    "Pohette. "
    "It wasn't bad enough to call a doctor,\nbut he said he felt tired."
    "Although they were going to come back and help him,{p}his dad and mom have their hands full\nwith the ceremonial bonfire."
    "It seems there's nobody who was able to tend to him,{p}so Shun-kun said that he asked\nfor his close friend [fn]-san."
    "A feeling of concern is transmitted\nfrom the sad voice on the receiver."
    "She repeats that they won't be able to come home{p}this evening and that they are truly sorry."
    "I respond 「I understand, please leave it to me. 」{p}and hung up the phone."
    
    scene shun_house_entry with blind_vert
    
    "In any case,{p}I'll make sure Shun-kun behaves himself."
    
    show su 001 at center with dis
    
    su "「[fn]-san, I brought some tea. 」"
    "Awawawawa.{p}This isn't a situation where\nhe should be giving me a warm welcome."
    
    scene black with dis
    scene shun_bedroom_day
    show su 001 at center
    with dis
    
    "Upstairs on the second floor."
    "Shun-kun's room.\nThis is the first time I've been in here.{p}My first impression is that it's relatively clean."
    "...my room is a mess,{p}does that mean something?"
    fn "「No, you collapsed,{p}\ \ so you should be taking it easy. 」"
    
    show su 002 with dis
    
    su "「I'm already feeling better♪ 」"
    fn "「Hey!{w=.2} Earlier you weren't steady on your feet.{p}\ \ You bumped your head on the front door,\n\ \ didn't you!? 」"
    
    show su 003 at briefzoom
    pause .2
    
    su "「Hanyu, how did you know that!? 」"
    fn "「Heheheheheh, onii-san knows everything. 」"
    
    show su 001 with dis
    
    su "「...amazing. 」"
    "A look of respect."
    fn "「So listen to what I say, lay down now. 」"
    "Then, I press him by pointing to his bed."
    su "「...okay.{p}\ \ {nw}"
    show su 010 with dis
    extend "But even though I'm with you, {w=.2}it's boring. 」"
    fn "「How about you get some sleep? 」"
    su "「I'm not sleepy... *woof* 」"
    
    hide su with wipe_down_slow
    pause .2
    
    "Shun-kun reluctantly lays on his bed.\nI sit next to him on his desk chair.{p}Something like this should be taken seriously."
    "However, he's completely bored\nand continues to appeal to me."
    "He dives his head under the thin covers\nand squirms around.{w} But I can't allow him\nto act like a spoiled child now."
    "Sometimes it's necessary to be strict,\neven if I think he's cute.{w} Hmm."
    "I thump him with my hand while he's rolled up\ninto a ball, then looked around the room."
    
    $ event_name = _("Well-ordered Room")
    
    "This desk seems easy to use,\nthere's dictionaries lined up within reach."
    "Writing tools are fit properly into the pen stand.{p}I can't even see any eraser pieces on it."
    "The 2 barley teas Shun-kun\npoured earlier stand cold on the tray."
    "Shun-kun is seriously obedient,{w=.2} he even seems\nto diligently do his summer homework every day."
    "...Huh, me?{p}W-Well, I'm in the middle of my homecoming now..."
    "A box is furnished on the opposite side of the room.{p}The top is decorated with family photos."
    "There's him with his parents,{p}then his grandfather and grandmother."
    "Of course everybody is short.{p}That's strange. Is the Kodori family\nsuffering from sorcery that makes them small?"
    "The box is separated into 3 stages,\nwith gaming magazines on the lowest."
    "Strategy guides are in the middle,{p}and on the upper part is a box with\na sticker that says \"Peripherals\"."
    "I don't see a TV or PC."
    "He goes down to the living room when he plays\nvideo games. A well-balanced kid who strictly\nabides by one hour a day.{w} Hmph."
    "...huh, me?{p}Every once in a while I start up an eroge."
    "When I aim for completing the gallery,{w=.2}\nit takes until morning, doesn't it?"
    su "「[fn]-san,\nplease talk to me about something. 」"
    fn "「Huh? 」"
    
    show su 016 at center with sdis
    
    "Getting tired of being bored,\nthe futon ball... er, I mean Shun-kun,\nlooks at me from an opening in the sheets."
    fn "「Hmmm... talk, you say... 」"
    
    show su 004 with dis
    
    "His eyes are full of anticipation.{p}Ooh, at times like this I why can't\nI ever think of anything...?"
    
    $ event_name = _("The Whole Story")
    
    fn "「B-by the way, why the heck did you faint? 」"
    
    show su 016 with dis
    
    su "「Myuu, I can't remember very well... 」"
    su "「They said I was lying in the corner of the hallway\n\ \ when I came to, and then I went home. 」"
    fn "「Did you come back alone? 」"
    
    show su 001 with dis
    
    "He shakes his head."
    su "「No, father took me home. 」"
    fn "「But he wasn't here when I arrived, was he? 」"
    su "「He had to go back because he's busy. 」"
    "A child has collapsed,\nand yet his parent isn't nearby.{p}That's kind of hard to believe."
    "...but, in this day and age,{w=.2}\nis \"child\" even the same as it used to be?"
    
    show su 002 with dis
    
    su "「But that's okay because you came over. 」"
    "Shun-kun probably really wishes\nhe could be with his parents..."
    "With the way he's acting, it seems he's on the verge\nof saying something he can't and is holding back.\nHis strained smile is even more painful."
    fn "「Preparing for the Bon Festival is hard,\n\ \ that's why you collapsed. 」"
    fn "「And yet neither your mom nor dad\n\ \ are going to be coming back tonight. 」"
    su "「Umm, that's because this is usually how it is,{p}\ \ except I'm house-watching this time. 」"
    
    show su 005 with dis
    
    $ encounter_iwao = True
    
    su "「But, Iwao-sama is- 」"
    "Shun-kun is acting like there's something\nreally bothering him. This is rare."
    fn "「Iwao-sama? 」"
    
    show su 001 with dis
    
    su "「My grandfather, father's father. 」"
    "His father's father."
    "That reminds me, Shun-kun\nuses \"sama\" for his relatives.{p}That's something of an old custom."
    su "「I didn't really want to go{p}\ \ because it's the day after we went camping, 」"
    su "「But when I got up this morning father\n\ \ and mother were getting ready... 」"
    su "「I thought \"I have to do my best\"{p}\ \ and \"I have to help\",{p}\ \ but it was still extremely hard... 」"
    
    show su 010 with dis
    
    su "「When I collapsed and woke up,\n\ \ Iwao-sama was there. 」"
    su "「He said I didn't have enough discipline\n\ \ and I should be more devoted.{p}\ \ Even though I was... *sniffle* 」"
    "I see."
    "He seems to be feeling down about\nhis grandfather's criticism.{p}Shun-kun speaks sadly."    
    fn "「Did you know you were going to be helping\n\ \ your family with the Bon Festival? 」"
    su "「...it's something we do every year. 」"
    fn "「Really?{p}\ \ So it's something you've known about since\n\ \ the beginning of summer break,{w=.2} isn't it? 」"
    fn "「Did I make you do too much\n\ \ with my plan to go camping? 」"
    
    show su 005 at briefzoom
    
    su "「Th-that's not it!{p}\ \ I wanted to go too! 」"
    fn "「But with something like this\n\ \ happening as a result?{p}\ \ I should've adjusted the schedule. 」"
    
    show su 010 with dis
    
    su "「...[fn]-san, would it have been better\n\ \ if I hadn't gone camping...? 」"
    fn "「!{w=.2} No!{w=.2}\n\ \ That's not it... 」"
    
    menu:
        "A. Should he have changed his plans for camping?":
            jump shun16_plans_camping
        "B. Maybe if he'd changed his plans for the Festival?":
            jump shun16_plans_festival
        "C. He should have talked about it beforehand.":
            jump shun16_plans_discuss
    
    ####################################################
    label shun16_plans_camping:

        $ event_name = _("Things in Particular")
        
        fn "「Don't you think that if you had told everybody\n\ \ about Bon Festival and gone camping another day,\n\ \ you wouldn't have had this burden placed on you? 」"
        su "「I-I'm sorry...{p}\ \ Because you said camping,\n\ \ I cleared out my plans for that day. 」"
        su "「I was so glad that I'd get to go with everybody,{p}\ \ I didn't think about the next day... 」"
        fn "「Really? 」"
        su "「...actually, Shin-san spoke to me later.{p}\ \ He said, {w=.2}\"Don't you usually have business\n\ \ with the Bon Festival around this time?\" 」"
        su "「So I got permission from Iwao-sama.{p}\ \ I said that I'll do the cleaning,{p}\ \ but I ended up fainting... 」"
        "Getting permission is a bit much.{p}He shouldn't need to do something so strict\njust to go out and play during his summer break."
        su "「If I was stronger I wouldn't\n\ \ be bothering you like this...{p}\ \ I'm sorry. 」"
        fn "「Umm, I don't think you're bothering me. 」"
        fn "「But if this keeps continuing,\n\ \ your body won't last, will it?{p}\ \ So try to be careful. 」"
        su "「Okay... 」"
        "Shun-kun gives a response,\nbut in a weak voice. I feel relieved.{p}Just a few points weren't very well received."
        
        jump shun16_evening
        
    #####################################################
    label shun16_plans_festival:
        
        $ event_name = _("Things in Particular")
        
        fn "「You should have changed your\n\ \ plans for the Bon Festival. 」"
        fn "「If you said the right things about camping,{p}\ \ even someone from your family would understand. 」"
        
        show su 015 with dis
        
        su "「Um, [fn]-san?{p}\ \ Do you know what the Bon Festival is...? 」"
        fn "「Of course!{p}\ \ It's when our ancestors in the afterlife{p}\ \ come back to this world, isn't it? 」"
        fn "「It's once a year. 」"
        
        show su 001 with dis
        
        su "「That's right. 」"
        su "「The bonfire for welcoming back\n\ \ the spirits is on August 13th,{p}\ \ and the bonfire for seeing them off is on the 16th. 」"
        
        stop music fadeout 1
        play music oo39_cho_ys001
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        
        fn "「Something like that should be done earlier! 」"
        fn "「If you did the farewell bonfire before\n\ \ going camping, you wouldn't have had any\n\ \ problems with going out to play. 」"
        
        show su 005 with dis
        
        su "「...That's something{p}\ \ you kind of can't do, isn't it? 」"
        fn "「Huh?{w=.2} You can't? 」"
        su "「No, It only happens once a year!{p}\ \ Even though they come in the morning,\n\ \ sending them back in the evening is too much! 」"
        "Oof, I'm being scolded by Shun-kun."
        fn "「B-but, if they can plan to come back\n\ \ at a particular time,{p}\ \ they can come back at any time, can't they? 」"
        fn "「Our ancestors know their own families. 」"
        su "「Then at that time when the iron pot\n\ \ of Hell will open!{p}\ \ It's not that easy! 」"
        "Oof, I'm being scolded again."
    
        hide su with wipe_right
        pause .2
        
        "With a considerable amount\nof pouting and bit of contempt,\nShun-kun lies in bed facing away from me."
        "...But everybody's ancestors will fall to Hell?{p}Really?"
        
        jump shun16_evening
        
    #######################################################
    label shun16_plans_discuss:
        
        $ event_name = _("Things in Particular")
        
        fn "「You should have talked about it.{p}\ \ If you would've said something we could\n\ \ have decided when we were going camping afterwards. 」"
        su "「B-but that would have caused trouble for everybody,\n\ \ we went through all that trouble to decide when,\n\ \ what to do, what to bring, I was excited. 」"
        su "「Doing it on another day,\n\ \ just for my own convenience... 」"
        fn "「Don't worry about that so much, it's okay.\n\ \ We're all friends, right? 」"
        fn "「They'd say \"Is that so?\n\ \ Well then, when should we do it?\" 」"
        fn "「Torahiko or Tatsu-nii will take care\n\ \ of the house work around here,\n\ \ and we would decide when to go again. 」"
        su "「...okay. 」"
        fn "「Do you think we would cut our childhood bonds\n\ \ over something so small? 」"
        "That was a kind of cool and nice thing to say.{p}Still,{w=.2} \"bonds\" is embarrassing."
        "However, Shun-kun asks me a question\nin a tiny voice."
        
        show su 004 with dis
        
        su "「Are you getting bored too...? 」"
        fn "「No way!{p}\ \ But isn't it sadder that you aren't enjoying\n\ \ this with all you can? 」"
        fn "「See?{w=.2} Whenever you want to talk,{p}\ \ I'll always listen. 」"
        fn "「Do have something that's too hard to talk about? 」"
        fn "「If you have something to say that you can't\n\ \ to your parents or teachers, you can talk to me. 」"
        fn "「I want to help you with your problems, because\n\ \ I like you and wouldn't make light of them. 」"
        
        show su 016 with dis
        
        su "「...[fn]-san... 」"
        "Wh-whoa, his eyes are big and round.{p}Again? He's doing that again?{p}I didn't do anything to make him cry. Did I?"
        
        stop music fadeout 1
        play music melodious06
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        
        show su 003 at briefzoom
        pause .2
        
        su "「Uwaan!{w=.2} [fn]-san! 」"
    
        hide su with dis
        
        "The futon ball hangs over.{p}No, Shun-kun, who has gotten\ninto tears mode, starts to fall."
        "He buries his head into my chest,{p}and begins to talk as if a dam\ninside him had burst."
        
        show su 003 big at center_big with sdis
        pause .2
        
        su "「I haven't been able to play with everybody\n\ \ very much this summer break. 」"
        su "「There's been so much I've had to do at Iwao-sama's{p}\ \ ...but then you also came back.\n\ \ So I decided that I absolutely had to go camping. 」"
        su "「Because I had been waiting so long for that chance,{p}\ \ I wanted to be near you as much as I could,{p}\ \ but,{w=.2} but... things didn't turn out very well. 」"
        "Shun-kun continues to talk while crumpling up.{p}I see. He wanted to come with us at any cost."
        "It's scary that he hurt himself by his own will.{p}He must have been lonely.{w} While gently stroking\nhis head, I speak to him softly."
        fn "「It's alright, there's still half of summer break left.{p}I still want to play with you some more.{p}...Even if you don't want to, will you go with me? 」"
        
        show su 016 big with dis
        
        su "「P-please, let me go with you... *sniff* 」"
        fn "「Hehe, you aren't about to faint, are you?{p}\ \ So!{w=.2} Take it easy tonight and recover! 」"
        "I wipe his tears with my fingertip."
    
        hide su
        show su tailwag 01 at center
        with dis
        
        su "「...hafu, got it! 」"
        "Alright, he's feeling better.\nI give Shun-kun a hug while he wags his tail.\nHe's so cute."
    
    ###############################################################    
    label shun16_evening:
            
        $ event_name = _("Evening time")

        stop music fadeout 1
        scene black with sdis
        scene shun_bedroom_day red with sdis
        
        "...the sun is going down in Minasato."
        "I watch over Shun-kun, who is sleeping\nwith peaceful long breaths.{p}He was tired after all."
        "At first he said in his tantrum that he\nwasn't sleepy. I wonder why he wanted\nto act like a spoiled kid to me?"
        "I think of various things about the house\nand the inside of my head starts spinning.{p}Heheheh, I might be a little mentally immature."
        "He has an expression of relief with his eyes closed\nand it somehow looks as if he seems to be smiling."
        "Good, good."
        
        stop sound
        play sound KeyA
        pause .5
        
        "!{p}The sound of a lock opening."
        "If I remember correctly,\nthat's the sound I heard when I got here."
        "The front door opened!{p}His parents should be out today.{p}If I assume somebody else is here..."
        "A relative?{w=.2} That's a possibility.{p}Maybe they came to check on Shun-kun.{p}But it's weird that they didn't ring the doorbell."
        
        play music ambient_015 fadein 1
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        
        "This is feeling dangerous. I look around\nfor something I could use as a weapon.{p}Tch, I can't find anything."
        "Just punching might\nhave enough attack power."
        "There is a bazooka-type game controller,\nbut I hold back from that because\nit might make Shun-kun angry or cry."
        "I can secure a frying pan if I go around\nto the kitchen, but the stairs are right\nin front of the entrance."
        "There's nothing else I can do."
        "I leave the room,{p}and cautiously descend the staircase."
        
        scene shun_house_entry red with wipeleft 
        
        "Just as I thought.{p}Light from outside comes through\nthe other side of the door."
        "There aren't any signs of life.{p}It seems like they might still be outside.{p}Making a tightly clenched fist, I..."
        
        stop music fadeout 1
        
        fn "「Wh-who is it? Hyaa!! 」"
        "He's been turned inside oooooooooout!"
        who "「It's Gaku Kodori. 」"
        fn "「Huh!? 」"
        "Kodori.{p}The turned-inside-out owner\nof the voice gives his name."
        "He moves the door, which was about half open,{p}to where only a small crack remains."
        "It doesn't seem like he plans on coming inside."
        fn "「Wh-who? 」"
        "I finish going down the stairs\nand approach the entranceway."
        fn "「Wh-who? Are you an acquaintance\n\ \ of the Kodori family? 」"
        gk "「[fn]-san, it's Gaku Kodori. 」"
        fn "「Oh!{p}\ \ From Kazenari! 」"
        
        play music shop02 fadein 1
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        
        "With the appearance of a vertically-stretched\nShun-kun, it's the clerk from the\nneighboring town's game store."
        "Feeling relief at finding his true identity,\npower quickly leaves my shoulders."
        fn "「Y-You surprised me.{p}\ \ You opened the door without ringing the doorbell. 」"
        fn "「Do you have a duplicate key? 」"
        gk "「I thought that Shun might be sleeping. 」"
        "A through-the-door conversation."
        fn "「Th-thank you.\n\ \ Are you here to visit him?{w=.2} Err...\n\ \ would you also like to come up? 」"
        "If I remember correctly,{p}isn't Gaku-san is Shun-kun's second cousin?"
        "I can let him in since he's a relative.{p}So I decide to put my shoes on and open the door."
        fn "「Going out of your way to come here... 」"
        "Squeeze.{p}The doorknob won't move even if I push or pull it.{p}It seems like it's being held from outside."
        fn "「Uh, um?{w=.2} Gaku-san? 」"
        
        show gk 003 red at farright with dis
        
        gk "「...this is troublesome.{p}\ \ Here. 」"
        "Then, an arm stretches out from the door\nand holds a plastic bag with stuff inside it.{p}...Am I supposed to take it?"
        fn "「Oh, please come in... 」"
        
        show gk 002 red with dis
        
        gk "「I just came to deliver this.\n\ \ You can take over from here. 」"
        gk "「Tell Shun I said hello.{p}\ \ Well then, I should get back back to Kazenari. 」"
        fn "「O-Okay, thank you very much... 」"
    
        hide gk with dis
        
        "Click."
        "As soon as I let go of the doorknob\nand take the bag,{w} Gaku-san retracts his arm\nand closes the door with a soft sound."
        fn "「...was he busy? 」"
        "But even then he was awfully blunt."
        
        show su 001 red at center with wipe_down_slow
        pause .2
        
        su "「Funyuu, [fn]-san. 」"
        fn "「Ah, Shun-kun! 」"
        "Shun-kun comes down the stairs.\nDid that wake him up after all?"
        
        stop music fadeout 1
        play music free0213 fadein 1
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        scene shun_house_living
        show su 001 at center 
        with wipeleft    
        show su 002 with dis
        
        su "「Did Gaku-san come over? I wanted to see him. 」"
        fn "「Yeah, I guess he was busy with something?{p}\ \ He gave this to me and suddenly left. 」"
        "Summer daylight hours are long.{p}It's still bright outside\neven though it's dinner time."
        "At the first floor dining table, Shun-kun and I\nransack the plastic bag Gaku-san gave me earlier..."
        "Wait-{w=.2} that's not it, we're just checking it."
        "There's ready-made food that can be cooked\nwith a microwave or boiling,\na PET bottle of tea, and a sports drink."
        "They can cut out the time it would take to cook,{p}but these supplies don't seem like\nthey would be good for the body."
        
        show su 001 with dis
        
        su "「Hehe, that was nice of him.{p}\ \ I didn't know what we were going to eat tonight.{p}\ \ [fn]-san, can you make that into curry? 」"
        fn "「Yeah, that should be simple to make. 」"
        "Shun-kun doesn't seem to be very\ngood at cooking if he's asking that."
        "Or rather, he has never done it would be correct?{p}It looks like Gaku-san expected that\nwhen he sent this."
        "I should be thankful for this.{p}Even the bug in my stomach is urging me,{p}and I assume it will gratefully take part in dinner."
    
        scene black with sdis
        scene shun_house_living with sdis 
   
        $ event_name = _("Gaku-san's Supplies")
        
        "Finished with our hashed meat\nand chicken on rice, we took a rest."
        "Then, Shun-kun boiled me in the bath.{p}\"Guests take a bath before anybody else♪\"{w=.2} he said."    
        "Now I'm waiting for him to get out.\nShould I take a look at the rest\nof Gaku-san's supplies?"
        "Because my appetite got the better of me earlier,\nI stopped looking through it halfway"
        "Rustle rustle."
        "Something like a book is in there.{p}Did he also get a game magazine to stave off\nShun-kun's boredom? It looks worn."
        "I turn it to the front cover."
        "\ \ \ \ \ 『Kodori Family ・{size=+15} Sex {size=-15}Guidebook』"
        fn "「... 」"
        
        stop music fadeout 1
        play music free0428
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        
        "Judging by the word next\nto the dot in the middle,\nit's that kind of book?"
        "I look around me.{p}Okay, nobody there."
        "I turn through the pages."
        "There are what health textbooks call\nsecond stage sex characteristics and... um,\nthe the way sex is handled...{w=.2} for men."
        "Wh-{w=.2}What was that stuck in there\nright before chapter two!?"
        note  "「Do this up to here{w} -Gaku 」"
        fn "「Aaaaaaaaaaaaaaaaaah! 」"
    
        show su 201 at center with dis 
        
        su "「[fn]-san,{w=.2} what's wrong? 」"
        fn "「Aaaaaaaaaaaaaaaaaah! 」"
        "Before I realize it, Shun-kun\nis standing there, just out of the bath."
        "After forcefully closing the book,{p}I toss it into the bag I got it from\nwhile I tie a knot with my mouth about five times."
        fn "「Nothing! {w=.2} Nothing at all! {w=.2} Yeah! 」"
    
        show su 204 with dis 
        
        su "「[fn]-san?{w=.2}\n\ \ You're really flustered.{w=.2} Are you okay? 」"
        fn "「Awawawawa, I'm fine! It's nothing! 」"
        su "「...really?{p}\ \ You're making me worry, [fn]-san. 」"
        fn "「Yeah!{w=.2} Really!{w=.2} It's really nothing 」"
        "I draw back my foot and hit it on the table,\nturn over, and fall on my backside."
        "...Th-this isn't something I\nshould be freaking out about, right?{p}I calm down a bit."
        "Okay. Calm down. Let's calm down."
        
        show su 203 with dis 
        
        su "「[fn]-san!{w=.2} A-Are you alright?! 」"
        fn "「...yeah. I seemed to have calmed down a little. 」"
        
        show su 204 with dis 
        
        su "「Hwaa, I was scared.{p}\ \ Does it hurt where you bumped your foot...? 」"
        "For now I squirm around and stand up."
        fn "「Yeah, but there's no wound so I'm okay.{p}\ \ Shun-kun, why don't you go back to your\n\ \ room so you don't get cold? 」"
        fn "「I'll be there later. 」"
        su "「O-okay... 」"
    
        hide su with dis
        
        "And then Shun-kun returns to his room.{p}At the side of his bed a futon is laid out.{p}That's mine."
        "I took out the guest futon earlier.{p}It's Shun-kun's wish that we sleep\nin the same room together."
        "And, it's Gaku-san's wish{w=.2}\nthat I take care of Shun-kun."
        
        stop music fadeout 1
        scene black with sdis  
        
    ################################################
    label shun16_sex:
        if persistent.replay == True:
            $ first = persistent.name_first
            $ last = persistent.name_last
            $ day = 16
            
        $ event_name = _("Muffled Sensation")

        play music free51
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        scene shun_bedroom_night with dis
        
        fn "「Sorry to keep you waiting. 」"
    
        show su 004 at center with dis
        
        su "「[fn]-san!{w=.2} Are you alright...? 」"
        fn "「Yeah, I'm completely fine. 」"
        fn "「Sorry, it's been so long since\n\ \ I've stayed over night somewhere\n\ \ that I guess I got a little nervous? 」"
        "Then I give a deceiving laugh. Having done that,{p}{nw}"
        show su 002 with dis
        extend "Shun-kun laughs as well with relief.{p}Good, good."
    
        hide su with dis
        
        fn "「I'm turning off the light. 」"
        su "「Okay♪ 」"
        
        scene shun_bedroom_night night with qdis
        
        "Click."
        "After making sure Shun-kun has crawled\ninto his bed, I turn out the light."
        "I lay down as well and use a cotton blanket\nso that my stomach isn't the only cool part of me.\nNow this is a satisfactory summer night."
        su "「I'm glad I get to sleep together\n\ \ with you like this again♪ 」"
        fn "「I know right?{w=.2} Camping was fun, wasn't it? 」"
        su "「It was♪ 」"
        "We reminisce about the other day, half-asleep.{p}The number of words exchanged between us\ngradually decreases."
        "After a short while,\nShun-kun seems to have fallen asleep.\nIn the darkness, I think about that book."
        "It seems to say that Gaku-san is teaching me a...\nmethod to comfort Shun-kun."
        "No, I am too. Just a short while ago I was thinking\nof taking advantage of this opportunity!"
        "I'll have to carefully read\nchapter 1 about 3 more times!"
        "Certainly Shun-kun is my cherished childhood\nfriend, and I do think he is considerably cute."
        "No, he is extremely cute.{p}I want him to \"funyuu\" some more."
        "I also thought that I should teach\nhim those things while josting him!"
        "But, in this way if I got to see him change into\nhis pajamas and happily sleep together with me,{p}I can't be doing that kind of promiscuous behavior."
        "Yeah, I'll let the matter drop for this evening.\nI couldn't bring myself to do indecent things\nto him just because it was written in a book."
        "That's right."
        "That's the sort of thing you do after\nyou have a deeper relationship.{p}I understand that, don't I?"
        "I'll even return that thing to Gaku-san tomorrow."
        "It's the Kodori family's instruction book,{p}so it wouldn't be favorable for an outsider\nlike me to undertake that."
        "If I remember correctly,{w} 「whatchacallit depends on\nthe correct guidance of an older family member 」{p}was written in it. "
        "So that means if I don't initiate Shun-kun,{p}then..."
        
        stop music fadeout 1
        
        "Gaku-san will!?"
        "「This is troublesome. 」"
        "Although it seemed like he was exaggerating,{p}Gaku-san's slender fingers were going\nto get involved with Shun-kun's important place."
        "Around two or three times, his tiny body trembles\nwith nervousness and in that hand is hot semen..."
        su "「[fn]-san? 」"
        fn "「Wah!{w=.2} Shun-kun? 」"
        "A small voice calls to me from the side\nand breaks into my delusion."
        "My eyes open.{p}Shun-kun pokes his head out from his bed\nand seems to be looking at me."
        "My eyes still haven't adjusted to the darkness,\nso I can't see the expression on his face."
        su "「Um... 」"
        "Somehow I manage to drive away those thoughts\nfrom earlier into the back of my head."
        fn "「Y-yeah, what's wrong? 」"
        su "「C-Can you come here...? 」"
        
        play music melodious02
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        
        "!{p}I-{w=.2}Is this an invitation?{w=.2} An invitation!?{p}Whoa, did my heart rate just go up!?"
        "No, no,{w=.2} wait, wait.\nIt's still not necessarily that kind of invitation."
        "He might be around the age where he{p}just wants to share his bed."
        "It's probably because I was thinking about dirty\nthings earlier that I would consider anything\nto be a flag."
        "This isn't that, this isn't that."
        su "「I-If you don't want to...\n\ \ that's okay. 」"
        "His voice is smaller than it was before."
        fn "「I will!{w=.2} I will right now! 」"
        "Can I do what I'm hoping for?{p}Hm?"
        fn "「What's wrong, Shun-kun? 」"
        su "「Th-There's something...{p}\ \ I want to talk about... {cps=10}um... 」"
        "Huh?"
        "He wants to talk about something?{p}While sliding myself onto his bed,\nI listen to him talk."
        su "「[fn]-san, don't tell anybody about this.{p}\ \ ...it's embarrassing. 」"
        "Shun-kun raises the upper half of his body\nfrom a face-up position while talking{p}and nestles next to me."
        "His adorable, tiny hands grasp the bed covers.{p}His body and breath are still warm from the bath."
        "My vision finally adjusts and I can see Shun-kun's{p}head turn away in embarrassment."
        "Judging from the tone of the conversation,{p}his cheeks are probably turning red."
        "A discussion? {w=.2} This is a little different{p}from the invitation I was expecting."
        "Oh well, that's okay because he's so small and cute.{p}I give him a reassuring smile."
        fn "「Don't tell anybody?{w=.2}\n\ \ This is your secret discussion.{w} It's okay, tell me.{p}\ \ I should be able to help you. 」"
        su "「Um, there's.... 」"
        "The scent of body soap tickes my nose."
        "I used it myself when I was in the bath earlier,\nbut the amount of scent that lingers\nis different on fur."
        "Under his thin undershirt-like pajamas,{p}I realized that Shun-kun is feeling\na dizziness in his chest."
        "I quietly put my hand on his tiny chest gently{p}to try to ease his nerves."
        "The Shun-kun, who seems to have been letting\nhis gaze swim turns towards me and timidly continues\ntalking with his eyes turned up at me."
        
        stop music
        
        su "「{cps=10}[fn]-san...{w=.2}\n\ \ My penis is weird... 」"
        "Sukon."
        "That felt like it was the sound of something\ncrashing in my brain. "
        "This wolf and childhood friend just said that\nit was weird."
        "That is the so-called proof of a man."
        "Somehow, an expression of embarrassment has\nbegun to spin out.{w} Shun-kun looks down\nand droops his ears with a \"henyan\"."
        "His little hands grasping his covers\nmakes my heart beat even faster."
        "The words that come out of my mouth from surprise{p}are quickly swallowed back into my throat.{p}This is cruel. Too cruel."
        "「What's weird? 」...  I didn't think it was\npossible for Shun-kun to act any more embarrassed.{p}I make a bold decision."
        "I read it earlier.{p}Is this thanks to the book's example?"
        "「With an adolescent boy, you should check\nhis state of development by the use of love\nwith extreme care so as not to scare him. 」"
        fn "「...can you tell me what it does?{p}\ \ I doubt it's something weird,\n\ \ it's proof that you're maturing. 」"
        su "「[fn]-san... um, I'm sorry for asking\n\ \ something like this... but it's embarrassing,{p}\ \ so I can't talk about it with other people. 」"
        fn "「That's okay. Can you tell me?{p}\ \ I won't tell anybody. I promise. 」"
        "I soften my voice as much as possible,\nand speak in a whisper."
        "My eyes have gotten used to the darkness and I\ncatch a glimpse of the blush on Shun-kun's face."
        "I thought that the moonlight shining\nthrough the curtains was kind of radiant."
        su "「Okay, um... It was normal until a while ago,\n\ \ but then it suddenly got hard\n\ \ and it won't go back easily... 」"
        su "「I can't sleep when it's like this... 」"
        fn "「Even now? 」"
        su "「Yes... my body does this and\n\ \ it won't settle down...{w=.2} is that weird? 」"
        fn "「That's not weird, Shun-kun. 」"
        su "「? 」"
        fn "「You're feeling aroused there,\n\ \ it gets hard when it's stimulated.\n\ \ It happens to all men, so you're not weird. 」"
        su "「...you too? 」 "
        fn "「That's right, so you can relax. 」"
        su "「...that's good. 」"
        "And with that, Shun-kun is finally relieved.\nHe entwines both his arms around my left,{p}and snuggles up to me."
        "His muzzle hits my shoulder\nand the fur on his head tickles me."
        "The border separating the colors of fur\non his neck seem awfully charming."
        su "「...that's good, I'm not weird.{p}\ \ I was worrying about what to do if I was sick,\n\ \ but I couldn't tell anybody... 」"
        "Back to his normal self,\nhe continues to talk casually,\nshowing an expression of relief."
        fn "「That's right Shun-kun, it happens to all men.{p}\ \ Even if it gets hard, it'll go back,\n\ \ so you don't need to worry. 」"
        su "「B-But it doesn't go back right away. 」"
        su "「Before I go to bed it's okay,{p}\ \ but it's frustrating before I go\n\ \ to school or when I'm in class... 」"
        "It seems he has experienced\nseveral erections so far."
        "He stares at me with anxious eyes.{p}What should I do?{p}It feels like he's asking me \"that\"."
        "His small body is glued to my arm.{p}The smell of body soap rises from his soft fur,\nmixed with a smell peculiar to beasts."
        "Stimulated by the scent, my blood boils.{p}I'm not usually so deeply aware of the\ndifferences in our heights and maturity."
        fn "「Shun-kun, is your penis doing that now? 」"
        "Shun-kun is a male too."
        su "「Hawah... this is embarrassing\n\ \ ...p-please don't look. 」"
        "While clinging to me, Shun-kun comes out\nfrom the covers up to his knees."
        "On his lower abdomen, a small bump\nis subtly pushing up on his pajamas."
        su "「D-don't! 」"
        "Quickly becoming embarrassed,{p}he separates himself from my arm\nand lays on his side facing away from me."
        "Then he takes the opportunity to pull the covers,\nexposing my body to the summer night air."
        "For quite some time now, I have felt mine\npushing up between the legs of my pants."
        "...I am a male, after all."
        fn "「Shun-kun, this can put it back to normal...{p}\ \ without having to wait for it to settle down. 」"
        su "「...huh? 」"
        fn "「Worried about it before going to school?{p}\ \ I can teach you. 」"
        fn "「And when you know how to fix it,{p}\ \ the sudden hardness will go away. 」"
        su "「P-Please teach me! 」"
        "He quickly rises up, faces towards me,\nand gets on all fours.{w} At the same time,\nthe covers fly up and fall by the side of the bed."
        su "「[fn]-san! 」"
        "His wagging tail urges me on.{p}...is this okay?{w=.2} It's for education, right?"
        "If I don't teach him,\nwouldn't he have a lot to worry about?"
        fn "「...alright then, can you take off your clothes? 」"
        
        scene black with blind_skinny
        scene shun_bedroom_night night with blind_skinny
        show su 111 night at center with wipe_down_slow
        
        su "「W-will this do...? 」"
        "Shun-kun looks down bashfully.{p}Both the flesh and frame of his\nstark-naked body are delicate."
        "Does only 1 or 2 years really make him\nthat different from me and the others?"
        fn "「I know it's uncomfortable,{p}\ \ but can you show me...? 」"
        
        show su 119 night with dis
        
        su "「O-okay... 」"
        "I encourage him to open his legs from\na sitting position on the bed.{p}He folds his knees a little."
        "Young as it is, in the center his male organ\ntwitches and stands up hard, asserting itself."
        "...somehow, I'm getting a feeling of immorality\nfor keeping company with a kid,{p}even if I'm only looking."
        "But I am aroused. That's alright, isn't it?"
        fn "「Um, by the way Shun-kun,{p}\ \ ...when you get hard, what does it feel like? 」"
        
        show su 122 night with dis
        
        su "「Wh-what does it feel like...?\n\ \ I feel restless... 」"
        su "「And when I'm wearing underwear,\n\ \ it hurts when it rubs against it. 」"
        "It seems like Shun-kun still has yet\nto realize pleasure from there."
        "Despite his embarrassment,he obediently responds to\nmy questions because I'm going to teach him the\nbodily function he has been wondering about so far."
        "At present, his curiosity and thirst for knowledge\nseems to have overtaken his embarrassment\nof exposing his body to somebody."
        "...this doesn't mean\nI'm trying to deceive him, does it?"
        "This is sex education.{w=.2} Yeah.{w=.2}\nIsn't that right?"
        
        show su 117 night with dis
        
        su "「Looking like this is embarrassing...{p}\ \ Please teach me how to quickly fix it, [fn]-san. 」"
        fn "「S-sorry, sorry. 」"
        "How to quickly fix it.{p}It's already obvious for doing it yourself.{p}You move your hand up and down, right?"
        fn "「Alright then, will you tell me if it hurts? 」"
        "After telling him that,\nI lay on my stomach between his legs."
        "This is the best posture to clearly see it.{p}Then, I reach my hand out to the part in question."
        
        show su 118 night with dis
        
        su "「W-wait!{w=.2} [fn]-san!? 」"
        
        scene black with dis
        scene ev_shun_1a with sdis
        
        "From Shun-kun's perspective,{p}he can see this from a considerable{p}short distance."
        "His face turning bright red from{p}embarrassment is lovely."
        fn "「So cute... 」"
        "His quivering tip is still pink.{p}The foreskin wrapped covering his shaft is\na beige color that continues up his stomach fur."
        "A soft looking bag waits at his crotch.{p}...th-this is for observation purposes."
        "An older person must make sure that Shun-kun's\nimportant place is growing correctly."
        su "「D-Don't look at it so much... Hafu!? 」"
        "I gently grasp the shaft and tightly squeeze it.{p}As I expected, Shun-kun pants in a weak voice.{p}I continue to slowly massage him."
        su "「Nn, haah, haau... 」"
        fn "「How does it feel? 」"
        su "「Huff, I-I don't know... Aahn. 」"
        "I look up. "
        "While enduring his first experience,\nhis eyes are closed tight and\nhis body writhes and cries out."
        "Just as I thought,\nhe has never done this to himself."
        fn "「When you touch it like this...{p}\ \ it makes a person squirm. 」"
        su "「Nn... [fn]-sa-... unng. 」"
        fn "「If you do this, it'll go back to normal. 」"
        "This time I gently move it up and down.\nThe skin moves smoothly,\nand the pink portion spreads out."
        fn "「Here... have you pulled it down before? 」"
        su "「Nnn, In the bath, to clean it... Aaahn! 」"
        "It seems he has thorough hygienic guidance."
        "Even though I thought it was going to catch\nand stop halfway, his aroused foreskin goes\ndown smoothly, exposing its fresh contents."
        fn "「Here, please try to look...{p}\ \ This is your penis. 」"
        su "「Ya-yaah, this is embarrassing... 」"
        "Is this because he's embarrassed\nor because it feels good?{p}Or maybe both?"
        "His eyes have gotten kind of watery."
        fn "「Don't you always see it in the bath?{p}\ \ You're keeping it clean, that's great. 」"
        "I praise him by adding more stimulation."
        su "「Hyan! 」"
        "Ooze.{p}A clear, thick liquid flows out\nof the opening at the tip."
        "It makes a line down his convulsing shaft,\nverifiying his pleasure."
        fn "「Here... 」"
        "I take it up with my finger\nand extend my arm up to his chest."
        "Breathing roughly and blushing,\nhe looks at it."
        su "「Ah, ahn... that's... I'm sorry. 」"
        "The way he apologizes\nwithout understanding why is so cute."
        fn "「When your penis feels good, that comes out.{p}\ \ The color is different too,\n\ \ and it oozes down.{w=.2} ...Touch it. 」"
        "With the remaining drop of his first\nexperience of this physiological phenomenon,\nShun-kun timidly stretches out a finger."
        "I also touch it with the longest of my fingers."
        "Seen through the slick and shiny mucus\nis the face of my childhood friend,{p}half surprised, half embarrassed."
        "...that reminds me, from what I saw earlier,{p}Shun-kun is approaching the\nsecond stage sex characteristics."
        "I continue talking with that assumption."
        fn "「...is this the first time this has come out? 」"
        "I check, just in case."
        su "「Y-yes, this is the first time...{w=.2} Nnnn. 」"
        "Occasionally he shudders,{w} enchanted\nfrom the muffled sensation on his lower abdomen.\nIt's probably the natural reaction of his body."
        "A silver thread streams down.{p}I separate my finger and touch\nhis sensitive part again."
        fn "「This comes out clear at first\n\ \ when you touch it like this.\n\ \ ...after that, white comes out. 」"
        su "「Nn, Nnnn... 」"
        fn "「Then the hardness goes away, okay? 」"
        "Even with the firey lust in my head,\nit seems I remember that I have to teach him.{p}I warn him about the series of symptoms."
        su "「Hya, Hyau... O-okay...[fn]-san. 」"
        "With small, timid jolts, he responds the\ncaressing between his legs and it seems like he's\ntrying to give me some kind of reply."
        "I see him push out his waist."
        "He is embarrassed, and yet his body\nis trying to find more pleasure.{p}Is that an instinct?"
        "And there's my instincts as well..."
        su "「Hyaah!{w=.2} [fn]-sa... nn! 」"
        "I submerge my face and creep my tongue along him.{p}With the tip in my mouth,{w=.2} I carefully lick\naround the seam of his skin."
        "It tastes salty, yet slightly sweet.{p}I catch a sight of the area around\nShun-kun's navel."
        "Body soap and sweat tickle my nose.{p}Beyond that is the smell of a beast's body."
        "Then, the small volume dances in my mouth.{p}The sucking sound pleasantly stimulates my ears."
        "My fingers involuntarily massage the lower{p}part of his sack."
        su "「Yah!{w=.2} Yaah!{w=.2} [fn]-san! 」"
        "Shun-kun forces out a scream and leans\nhis body back.{w} At the same time,\nthe rod of meat in my mouth jolts."
        "I lick it so that the tip of my tongue\nblocks the opening."
        su "「...!{w=.2} Haaahnn! 」"
        "In order to check the backside of the shaft,\nI stimulate with my tongue to roll him around."
        "Then I realize that he is hastily\ndripping into my mouth."
        "Taking care not to hit his shaft with my teeth,{p}I release my head. A thread quickly follows along."
        "While enjoying the aftertaste on my lips,\nI look up at Shun-kun's face.{p}He has an intoxicated expression, ears drooped."
        "With a sense of relief at getting a break in his\nfirst intense feeling of pleasure, desire irritates\nthe part of him that waits impatiently for the climax."
        su "「Nn... [fn]-san... 」"
        "It seems that he can't hold\nback distorting his face.{p}His cheeks redden. He lets out a sigh."
        "His eyes are drunk in pleasure,\nasking for more stimulation."
        "His shaft twitches in a way that makes it seem\nas if it could reach that moment at any time."
        "While I could also greedily wolf it down\nat any time, I somehow keep myself controlled."
        "I check with Shun-kun, who is unable to stand\nthe heat coming from between his thighs."
        fn "「More...? 」"
        su "「...more, [fn]-san, please... 」"
        "He urges me.{w=.2} That crude language shows that\nhe has become straightforward in his pleasure.{p}I immediately start sucking."
        su "「Haan!{w=.2} Yaah!{w=.2} [fn]-san! 」"
        "I suck it noisily.{p}I move my lips move up and down his shaft\nand hastily lick it with my tongue."
        "I taste all of it in my mouth,\nstirring up Shun-kun's lust."
        su "「Haah, I- I can't...! 」"
    
        scene white with qdis
        scene ev_shun_1b with sdis
        pause 1.7
        
        "In an instant the tip touches my upper jaw because\nShun-kun swings his waist. His shaft jolts\nand begins to vigorously shoot hot liquid."
        su "「Nn!{w=.2} Haah!{w=.2} ...ah. 」"
        "His warmth pumps into my mouth and fills it up.\nI sound my throat and swallow it."
        "I was concerned about how it would taste,{p}but I excitedly accept the young male's\nstill-thin torrent."
        "That part of the wolf that released what\nI collected convulses 2, 3 times, and\nslowly loses strength on my tongue."
        
        scene black with sdis
        pause .2
        scene shun_bedroom_night night with sdis
        play music musi2 fadein 1
        
        "His navel twitches up and down\nto adjust his turbulent breathing.{p}He's so cute."
        "I lick up the overflowing mucus,\nand take him out of my mouth.{p}His pink fruit tasted its first release."
        "When it shrinks down, the majority\nof the shaft is wrapped in skin.{p}The wet tip peeking out is cute."
        fn "「Now then... 」"
        "After a while I feel my normal voice come out.{p}I was a little puzzled at my throat being tangled."
        "Anyways, I want to do something\nabout myself not getting settled."
        "My weapon pushes up my underwear and pants,\nfirmly standing tall and aching.{p}It's damp around the cloth it's sticking to."
        "How dare I start stroking it while doing that,\nI think. {w=.2}Good going, me."
        "As long as I remembered that common saying,{p}I didn't give myself a reward."
        "I want Shun-kun, who is sleeping pleasantly\nsleeping, to feel good."
        "Wait, whaaaaaat!?"
        "When I get up and look at Shun-kun,\nhe's stretched out on his sheets,\nhaving used up all his strength."
        "Even though it looks like he fainted,{p}I can hear the sound of his healthy breathing.\nThe redness on his cheeks remain."
        "There are traces of saliva around the edges\nof his lips. The sheets are freshly disordered."
        "The part of him that was in my mouth earlier\nis slightly wet."
        "In the faint moonlight shining through\nthe curtains, is proof our actions."
        "...is this a postponement?"
        "Although I thought of instantly thrusting in,{p}the sight of him sleeping soundly\nclears away evil intentions like that."
        "If possible, I wanted to blow away this\nmuffled heat of mine together."
        "My head is full of lust, but to be kind to Shun-kun,\nmy hand pulls up his underwear before I realize it.{p}I tenderly pull the covers up to his chest."
        su "「[fn]-san... 」"
        "Looks like he's sleep-talking."
        "For some reason,{p}I am suddenly no longer able to endure it\nand lick up the trace of saliva on his muzzle."
        "That reminds me, we didn't even kiss once."
        "...{p}May I get a tissue?"
        
        if persistent.replay == True:
            scene black with dis
            pause 1
            $ renpy.end_replay()#!#Check if this is needed or a return
            
        $ persistent.event_shun1 = True
        
        stop music fadeout 1

        $ event_name = _("Muzzle Sense")

        jump end16    
    
#######################################################
label kouya16:    
    
    $ event_name = _("Ticket Riots")
    scene map
    hide screen candystore16

    scene candystoreout with sdis
    play music daily05
    
    "On that day near the middle of the month,{w=.2}\nKouya called me and told me\nto come over to the sweets store."
    "『There's something I want to give you. 』{p}That's all he said."
    "During this summer, the times Kouya has called me\nare few and far between,{w=.2}\nso I'm a little excited about it."
    "What is this thing he wants to give me?"
    "While I was thinking about this and that,{w=.2}\nI faced the shop at the promised time.{p}The entrance was right in front of me now."
    "I walked inside, and there was..."
    
    play sound tm2_slidedoor000
    scene candystorein
    show ta 001 at farright
    show ka 001 at farleft
    show ky 001 at center
    with wipe_right
    
    fn "「Good afternoon!{w} ...Wait,{w=.2} what? 」"
    "All my childhood friends were there.{p}Three of them were standing by the door,{p}and everyone else was looking for suitable snacks."
    "One, two, three...{w=.2} Yep, looks like it's all-{p}No wait, scratch that.{p}Someone's missing. That tanuki."

    show ta 008 with dis
    
    ta "「Ahh,{w=.2} so [fn] came in first after all. 」"
    
    show ky 002 with dis
    
    ky "「Well, if we're comparing with Kounosuke,\n\ \ it probably would turn out like that. 」"
    
    show ka 005 with dis
    
    ka "「Good grief.{w} Just by comparing, [fn]'s worse. 」"
    fn "「Umm...{w=.2}what's going on? 」"
    "I don't get it, so I asked."
    "In this not-particularly-large shop interior,{w=.2}\nthere were nine guys, including me."
    "It's a business obstruction,{w=.2}\nand right now it can't really be helped.{p}Things are densely packed either way."
    
    show ka 002 with dis
    
    ka "「I called everyone over.{p}\ \ I said the same thing to you,{w=.2}\n\ \ that I had something I wanted to give you. 」"
    fn "「Hm,{w=.2} you did say that... 」"
    "I wasn't expecting so many people to show up."

    show ta 010 with dis
    
    ta "「Every time Kouya has something to hand out,\n\ \ it's always here.{w} We've all gotten used to it,{w=.2}\n\ \ but it is suprising the first time around. 」"
    
    show ky 001 with dis
    
    ky "「That's true,{w=.2} what with the\n\ \ location and number of people. 」"
    fn "「Eh...?{w} Wha...? 」"

    scene candystorein with wipe_right
    
    "I still don't get what's going on."
    "For now,{w=.2} I do understand that\nKouya's gathered everyone together."
    "And that's because he has something\nhe wants to hand out, I think.\nJust what is this thing he's handing out?"

    show ka 002 with dis
    
    ka "「Well,{w=.2} I'll hand out the stuff now then.{p}\ \ Stop making those curious faces. 」"
    "When he said that,{w=.2}\neveryone around the store looked over,\nand gathered around."
    
    show ka 001 with dis
    
    ka "「Now,{w=.2} I think you all know why I called\n\ \ you all here, but the reason we're here\n\ \ is because there's nowhere else. 」"
    ka "「I was thinking of passing out the tickets,{w=.2}\n\ \ since the show will be a few days later. 」"
    fn "「Eh,{w=.2} live concert? 」"
    ka "「Yeah,{w=.2} I'm in a band now.{p}\ \ That's what the concert's about.{p}\ \ Didn't I mention it before? 」"
    fn "「Oh yeah,{w=.2} I do remember that. 」"
    "Now that I can't remember without being reminded,\nmy memory really is failing.{p}This is so sad,{w=.2} really..."
    ka "「Well anyway,{w=.2} every time there's a live concert,\n\ \ I pass out tickets like this.{p}\ \ {nw}"
    show ka 003 with dis
    extend "Since you're here, I wanted you to see it. 」"
    fn "「I see then. 」"
    
    hide ka with wipe_right
    show to 001 at farleft
    show su 001 at farright
    show ju 001 at center
    with wipe_right
    
    ju "「Yeah,{w=.2} in the beginning it was us\n\ \ who said we wanted tickets anyway.{p}\ \ And before we knew it, this became standard practice. 」"
    
    show su 002 with dis
    
    su "「Yes, that's right!{w} When we all said we wanted\n\ \ to go see Kouya-san's first performance,{w=.2}\n\ \ we also asked for tickets then. 」"
    su "「And then,{w=.2} every time\n\ \ since then he would call us over\n\ \ and we would all gather around like this! 」"

    show to 003 at jump_up
    
    to "「Yeah,{w=.2} music shows aren't bad.{p}\ \ It's a good way to waste some time, [fn]. 」"

    show ju 003 with dis
    show ka 001 at offright behind su
    
    ju "「Why...{w=.2} why are you always\n\ \ saying such thoughtless things? 」{w} {nw}"
    show ju at shivering
    show ka at move_farright(2)
    show su 015 with dis    
    extend "{w=2.5}{nw}"
    play sound don08    
    show ka at move_offright_far(0.75)
    show su at move_offright_far(0.75)
    show ju 006 with explosion
    
    ju "「Can't you say things a bit more tactfully? 」"

    show to 005 at jump_up
    
    to "「Wait, Juuichi-san,{p}{nw}"
    show to 007 at jump_up
    extend "\ \ if you get all violent in a small shop... 」"

    show to 005 at jump_up
    
    to "「No! Juuichi-san, I was just joking,\n\ \ just some light sarcasm! Wait, if-if you use a fist\n\ \ in judo,{nw}"
    show ju at hit_right
    play sound bom26_b
    show to at move_offleft_far(0.25)
    extend " isn't that a violaaAGH! 」"
    
    show ju 001 with dis
    
    ju "「Honestly... 」"
    to "「I-{w=.2}I can't feel my body anymore...{p}\ \ S-{w=.2}so terrible... 」"
    fn "「Ahahaha. 」"

    scene candystorein with wipe_right
    
    "I've gotten used to the pair's exchanges,{w=.2}\nand while watching them I laughed in a dry voice."
    "...That one hit seemed pretty serious."

    show ka 001 at midleft
    show su 001 at midright
    with wipe_right
    
    ka "「...Anyway,{w=.2} how about we leave it at that,\n\ \ and move on.{w} Time for today's subject.\n\ \ I'm counting on you, Shun. 」"
    
    show su 002 with dis
    
    su "「Okay, I understand. 」"
    
    play sound step03
    hide su with wipe_right
    
    "With a neat reply, Shun-kun ran over\nto the counter of the candy shop,\nand brought back chopsticks and a wooden tube."

    show su 001 at midright with wipe_right
    
    "The tube was like a cup and the chopsticks\nwere inside sitting in the bottom."
    "The container was cut in half,\ngiving me the image of omikuji,\nthose fortune-telling strips in shrines."
    su "「Okay,{w=.2} time to draw! 」"

    scene candystorein with wipe_right
    
    "The jangling of the chopsticks\nbeing shuffled around filled the store."
    "It seems like it's for picking out the subject,{w=.2}\nbut just what were we picking a subject for?"

    show ka 001 at center with dis
    
    fn "「Hey Kouya,{w=.2} what's the subject for? 」"
    
    show ka 005 with dis
    
    ka "「Right, I haven't explained it to you before.{p}\ \ {nw}"
    show ka 001 with dis
    extend "It's like this,{w=.2} we're picking a subject\n\ \ to deal with the cost of tickets. 」"
    ka "「I'll say I'm fine if it's me however many times,{w=.2}\n\ \ but the tickets aren't that cheap,\n\ \ so this is a compromise we all came up with. 」"
    ka "「I'm up for this challenge,{w=.2}\n\ \ and if I lose I pay for the tickets.\n\ \ That's how it is. 」"
    fn "「Ah,{w=.2} I see. 」"

    hide ka with wipe_right
    
    "So in other words, all the chopstick-shaking\nShun-kun is doing right now is a game of some kind."
    "And in this game, there is a loser."

    show su 001 at center with dis
    
    su "「Okay!{w} Here is today's subject! 」"
    "With a loud declaration,\nShun-kun pulled out one of the chopsticks,{p}reading out the text written on it."
    
    show su 002 with dis
    
    su "「Today's subject is decided by rock-paper-scissors! 」"

    hide su with wipe_right
    
    "Oh,{w=.2} that's a good one."
    "Yep,{w=.2} last time at poker Kouya won hands-down.{p}He beat eight people."
    "That reminds me.{p}Wouldn't this be a better method?"
    "After the subject was announced,\neveryone said what they thought it would be."
    "...Hey, isn't winning against\neveryone in poker flat-out amazing?"
    "And if I were to say something,{w=.2} back then\nI was pretty good at these kinds of games.{p}But then,{w=.2} if it's video games then Shun-kun is king."
    fn "「So,{w=.2} since losing is gonna be painful.\n\ \ I'm going to try my best.{p}\ \ Go easy on me, Kou- 」"
    "I stopped abruptly.{p}For some reason,{w=.2}\nKouya seemed so crestfallen."
    
    show ka 005 at center with dis
    
    ka "「...It's that,{w=.2} huh... 」"
    fn "「Kouya?{w} What's wrong? 」"
    ka "「...No, it's nothing.{w} Nothing at all. 」"
    "He said it twice.{p}But it's obvious there's something wrong.{p}I wonder what happened?"
    
    hide ka with wipe_right
    show ta 001 at midright
    show ka 001 at midleft
    with wipe_right
    
    ta "「Now,{w=.2} how about we start already?{p}\ \ Fine if I go first, Kouya? 」"
    ka "「...I understand.{w=.2} Let's start.{p}\ \ Rock, paper- 」"
    
    stop music fadeout 3
    scene black with sdis  
  
    $ event_name = _("Weak Point in the Three-way Deadlock")

    scene candystorein
    show ka 014 at center
    with sdis
    play music sad02
    
    ka "「I...{w=.2} I am never playing\n\ \ rock-paper-scissors ever again... 」"
    "Kouya's quiet mutterings disappeared\ninto the silence of the shop."
    "Just from those words,\nit's clear how the game turned out."
    "That is to say,{w=.2}\na complete and epic fail on Kouya's part...{p}The opposite to before: Eight straight losses."
    "Well, at least it's impossible to get any worse.{p}Ummm, how does the formula go again..."
    "...Well, having a concrete number would be nice,\nbut relatively speaking, it's pretty unlikely!"
    "However,{w=.2} not one person so much as tied.{p}Most didn't laugh.{w=.2} And everyone looked worried."
    "It's so hard to describe this atmosphere,{w=.2}\nand even Torahiko stayed quiet.\nHe probably gets how serious this is."
    fn "「Ah, Kouya...{w} This is just... A{w=.2}-a coincidence.{p}\ \ It's just how the odds played out.{p}\ \ Don't worry about it too much. 」"
    "They felt kind of hollow,{w=.2} those words of comfort.{p}Maybe I shouldn't have opened my mouth.\nI regret it a little."

    show ka 013 with dis
    
    ka "「Yeah...{w} that's right.{p}Rock-paper-scissors is all about luck. 」"
    
    show ka 014 with dis
    
    ka "「But with a record of over 200 straight losses,{w=.2}\n\ \ that's probably impossible, seriously... 」"
    fn "「Yeah,{w=.2} that's ri-... Huh?{w=.2} Wait, what? 」"
    ka "「I said I just lost more than 200 times in a row.{p}\ \ That last one was on your turn. 」"
    "I don't get the significance of the number 200.{p}So 200...{w} is 200?"
    fn "「A-again and again...{p}\ \ I guess you really aren't trying to fool me. 」"
    
    show ka 013 with dis
    
    ka "「Well, yeah,{w=.2} but before you changed schools,\n\ \ do you remember ever losing to me at this game? 」"
    fn "「N-{w=.2}no,{w=.2} but I can't remember\n\ \ something that trivial... 」"
    ka "「In that case,{w=.2} do you have any strong memories\n\ \ of me being it during hide-and-seek? 」"
    fn "「Oh, I do have a lot of those.{p}\ \ You're better than anyone in the group,{w=.2}\n\ \ but when it came to being it... 」"
    "I was taken aback by what I was saying.{p}When I look into my memories for Kouya being \"it\",{w=.2}\nit feels like it's turning up quite often."
    "So that means..."
    fn "「B-but there were times when you weren't it, Kouya! 」"
    
    show ka 014 with dis
    
    ka "「You mean every time after the second person that day?{p}\ \ Doesn't the first to get caught become \"it\"? 」"
    fn "「Uu... 」"
    "Ohh, what did I just say.{p}So, it really is 200 consecutive losses."
    "It's been so long since I've played\nrock-paper-scissors with him that I forgot."
    "From everyone behind me,{w=.2}\nI could hear them whispering the same thing."
    "Gradually, I saw it the way Kouya said it was."
    ka "「After the losses piled up,\n\ \ I noticed and started counting.\n\ \ 200 already? 」"
    ka "「I'm used to losing,\n\ \ but losing 8 in a row with no ties is a first...{p}\ \ Ahhh,{w=.2} this is just depressing. 」"
    "Nobody really knew what to say,{w=.2}\nnot to Kouya in such a rarely-seen funk.{p}The place was awash in silence."
    "And then, with the mother of all timing,\nin came the guy who was late."

    hide ka with wipe_right
    show ko 001 at center with dis
    
    ko "「Afternoon! ...Oh,{w} {nw}"
    show ko 005 with dis
    extend " I'm last again?{p}\ \ You guys are all early as usual. 」"
    "You're just late.{p}None of us bothered with that routine reply."
    "He seemed to get how delicate the mood was,{w=.2}\njust as he always did."

    show ko 007 with dis
    
    ko "「What happened? 」"
    fn "「Oh,{w=.2} no, it's just that\n\ \ Kouya's in his depressed mode. 」"

    show ko 006 at briefzoom
    
    ko "「Eh?{w} That's pretty unusual.{p}\ \ {nw}"
    show ko 005 with dis
    extend "What's wrong? 」"
    ka "「I'm in the middle of eight straight losses.{w=.2}\n\ \ Seems the damage to my soul's huge... 」"
    ko "「Hmm, is that so.{w} {nw}"
    show ko 001 with dis
    extend " Well, whatever.{p}\ \ So I guess the eight losses is about\n\ \ today's ticket distributing. What was the subject? 」"
    fn "「...Rock-paper-scissors. 」"

    show ko 002 with dis
    
    ko "「Oh, then this time we can have a real contest!{p}\ \ Last time,{w=.2} I was done in without putting up a fight. 」"
    ko "「And with that streak, I can probably win. 」"
    
    hide ko with wipe_right
    show ka 005 at midleft
    show ko 001 at midright
    with wipe_right
    
    ko "「And so,{w=.2} let's do this, Kouya! 」"
    ka "「Yeah,{w=.2} let's get this over with. 」"
    "It feels like he's been amazingly\ncasual before the contest.{p}And Kouya's been like this before too..."
    ko "「Let's go!{w} Rock-paper-{w} {nw}"
    show ko at jump_up
    show ka at jump_up
    extend "scissors! 」"
    ko "「Oh,{w=.2} that sucks, Kouya.{w} Now it's nine losses. 」"
    
    show ka 014 with dis
    
    ka "「...I'm never,{w=.2} ever going to play this again. 」"
    "Once more, he muttered quietly.{p}This is getting painful to watch."
    
    show ko 005 with dis
    
    ko "「Come on, it's not that bad.{w=.2}\n\ \ It's just a loss in rock-paper-scissors. 」"
    ko "「It's not like your life is riding on this.{p}\ \ You hesitate too much. 」"
    ko "「Besides, since you put your default strength\n\ \ into other kinds of gambling,{w=.2}\n\ \ it's okay to be bad at this one. 」"
    "Wow, it's unusual for Kounosuke\nto say something so serious."
    "I can't tell if this will\ncheer him up or finish him off,{w=.2}\nbut this is a big chance."
    fn "「Yeah,{w=.2} everyone has a weak point.{w} I mean,\n\ \ look at how many things you succeed at.{p}\ \ It's not something as little as Torahiko's swimming. 」"
    
    scene candystorein with wipe_right
    show ka 014 at farleft
    show to 003 at farright
    show ko 001 at center 
    with wipe_right
    stop music fadeout 3
    
    to "「Hey, wait a minute, [fn].{p}\ \ Why are you using me as a comparison? 」"
    
    show ka 001 with dis
    play music piano3_014
    
    ka "「...Yeah.{w=.2} Yeah, that's right.{p}\ \ It's just rock-paper-scissors,\n\ \ I'm thinking too much about it. 」"
    fn "「Uh-huh.{w} Even though you've\n\ \ lost each game up until now,{w=.2}\n\ \ it doesn't mean the next one is decided for sure. 」"
    fn "「This isn't something to be down about. 」"
    
    show to 006 with dis
    
    to "「Hey, if you're gonna ignore me I'll start again.{p}\ \ Weren't you all sad?{w} If that's how it is,\n\ \ then take responsibility and deal with it. 」"
    
    show ka 002 with dis
    
    ka "「Sorry for all the awkwardness there, everyone.{p}\ \ I've got no excuses.{p}\ \ [fn], is there anything you want? 」"
    fn "「Eh, me?{p}\ \ Hmm,{w=.2} let me see... 」"

    show ko at jump_up
    
    ko "「Hey, wait Kouya.{w=.2}\n\ \ I want my ticket before that, please.{p}\ \ Seems like you might forget at this rate. 」"

    show to 007 with dis
    
    to "「...Ah,{w=.2} no one called?{p}\ \ Well that can't be helped.{w=.2} Yep, nothing to it... 」"
    
    show to at move_offright_far(2)
    show ka 001 with dis
    
    ka "「Right, sorry, sorry.{p}\ \ Let's see, yours is...{p}\ \ {nw}"
    stop music
    show ka 005 with dis
    extend "Huh?{w=.2} Where is it? 」"
    
    show ko 005 with dis
    
    ko "「Hey, hey, Kouya...{w=.2} that gag's not funny. 」"
    ka "「No...{w=.2} I had it for real earlier.{p}\ \ It should have been here before... 」"
    fn "「It's gone? 」"
    ka "「...Looks like it. 」"
    "Well, if it was there earlier,{w=.2}\nmaybe it dropped into the shop somewhere."

    scene candystorein with wipe_right
    show si 001 at farright
    show ta 001 at center
    show su 001 at farleft
    with wipe_right
    play music oo39_cho_ys001
    
    fn "「Hey,{w=.2} didn't Kounosuke's ticket\n\ \ drop somewhere over there? 」"
    
    show ta 006 with dis
    
    ta "「...Nope.{w=.2} Not here. 」"
    
    show su 004 with dis
    show to 001 at offright_far
    
    su "「I don't see it either. 」"
    si "「Me neither.{w=.2} It's not here. 」"

    show to at move_border_right(0.5) #!#Create this
    
    to "「Not over here, either. 」"

    show to at move_offright_far(0.5)
    pause .5
    scene candystorein with wipe_right
    
    "W-{w=.2}whaaa...{p}Then where did it go?"
    
    show ka 005 at midleft
    show ko 005 at midright
    with wipe_right
    
    ko "「Huh?{w=.2} So it really is gone? 」"
    ka "「My bad,{w=.2} Kounosuke...{p}\ \ Next time I'll keep it on me,\n\ \ so please let me go on it. 」"
    ko "「Well,{w=.2} if it's like that\n\ \ then I don't really mind... 」"
    
    show ko 001 with dis
    
    ko "「But it's weird,{w=.2}\n\ \ disappearing in the shop like that. 」"
    fn "「Yeah,{w=.2} it's not like\n\ \ someone else has it... 」"

    show ko 006 at jump_up
    
    ko "「...Ah, I get it!{p}\ \ That's it, [fn]! 」"
    fn "「...What is? 」"
    "I feel like I just heard something incredibly stupid,{w=.2}\nbut with all that waving around,\nI can't not ask again..."

    show ko 002 with dis
    stop music
    
    ko "「It's that!{w} The 11th presence\n\ \ still unnoticed by anyone! 」"

    play sound metalic
    
    "...Yeah, earlier there was a strange feeling.{p}Primarily a feeling of 'talk about it\nand it will be on your mind'."
    
    show ko 001 with dis
    play music daily02
    
    ko "「Huh?{w=.2} That wasn't a good\n\ \ response from any of you. 」"
    "What kind of response were you looking for?"
    "Everyone stared at Kounosuke.{p}If you were seeing this from outside,\nit probably looked amazing."
    
    show ko 005 with dis
    
    ko "「W-{w=.2}what?{w} It's not like it's impossible. 」"
    
    show ka 013 with dis
    
    ka "「No,{w=.2} it is. 」"
    "Kouya spoke what the rest of us were thinking.{p}It's so refreshing to so definitively put it down."
    "Nice, Kouya.{p}If you didn't do it, none of us would have."

    show ka 006 with dis
    
    ko "「Guh!{w=.2}{nw}"
    show ko 007 with dis
    extend " And now you're back to your usual self... 」"
    shopkeep  "「What's wrong, everyone?{p}\ \ You're making such scary faces. 」"

    show ka 001
    show ko 001
    with dis
    
    "And with that,{w=.2} the shopkeeper\nof the candy store suddenly spoke up."
    "...I guess to someone outside this scene,\nit is a scary matter."
    fn "「Oh,{w=.2} it's just that a friend\n\ \ that should have a ticket seems to have lost it. 」"
    fn "「The tanuki over there is\n\ \ saying that a spirit\n\ \ might have taken it. 」"
    shopkeep  "「A ticket?{p}\ \ You lost it in this store? 」"
    fn "「Yes.{w=.2} It seems we did have it until then... 」"
    shopkeep  "「I see...{p}\ \ In that case,{w=.2} maybe a spirit really did take it. 」"
    
    stop music fadeout 7.5
    
    "「EH!? 」{p}Everyone said the same thing,\nwith their voices rising all at once."

    show ko 002 at jump_up
    
    ko "「I knew it! 」"
    "I don't know about this 『I knew it』 business,{w=.2}\nbut I'm a little interested."
    ka "「What is that... 」"
    shopkeep  "「Yes,{w=.2} it was a story from my childhood... 」"
    "So as to not miss a single word,{w=.2}\neveryone leaned forward a little."
    "Then the shopkeeper went on,\ntelling the story disinterestedly."

    scene black with sdis  
  
    $ event_name = _("I'll Take It... ")
  
    play music ambience01
    
    "It seems to be a very old story."
    "In Minasato's elementary school,\nthere was a certain boy."
    "He wasn't from a rare species, just an ordinary boy.{p}He wasn't unhealthy, just a normal boy in every way."
    "However, he was from an especially\npoor family in Minasato Village."
    "Perhaps because of that, despite his normality,{w=.2}\nhe had a certain particular habit.{p}Rather than an action, it was more of a catchphrase."
    "「Can I take that? 」"
    "Despite how young he was,\nhe seemed to understand how poor his household was."
    "He would never ask that of things\nthat were important to others."
    "But for unneeded things that were still usable,\nhe would often say that."
    "Friends,{w=.2} teachers,{w=.2} the adult villagers.{p}Anyone, really."
    "The boy was always kind to everyone."
    "To the ones he asked, they'd often\nalready thought about tossing it away."
    "With no special reason to refuse him,\nthey would give it to him."
    "After some point,{w=.2} it seemed as if everyone\nbegan asking the boy if\nhe wanted everything they threw away."
    "In a way, it was a version of modern day recycling.{p}No one was unhappy about it,\nand it was a simple relationship."
    "However, with such a strangely projected-on person,{w=.2}\nthere was a certain seed of inevitability."
    "Amongst that boy's classmates,{w=.2}\nthere seemed to be such a child."
    "Thus, several of those unpleasant boys gathered,{w=.2}\nand several instances of bullying occurred."
    "In this boy's case,{w=.2} he was placed\nunder that unfortunate circumstance."
    "The boy was exposed to many forms of bullying.{p}However, the boy just endured it,\nnever crying, even for a moment."
    "When any onlookers saw this state of affairs,{w=.2}\nit seemed as though they\nthought it couldn't be helped."
    "That was considered the wise decision.{p}And yet, the consequences were far from ideal."
    "As the boy showed no reaction to the bullying,{w=.2}\nthe other children began to steadily\nescalate their actions."
    "That may be where it all began,{w=.2}\nThe shopkeeper said."
    "The bullying became much more direct,{w=.2}\nand at last the boy was dealt a serious injury."
    "From his right eye down his cheek,\nthere was a great big gash."
    "With such a deep wound,{w=.2} the boy lost his right eye,\nand was left with an enormous scar.{p}It seems that's what the doctor said."
    "However, the medical treatment required money."
    "The boy's family was especially poor in the village.{p}Yet they still had something saved up."
    "The boy's parents would use those savings,{w=.2}\nand one way or another the\nboy's wound would be healed."
    "It was the silver lining in the cloud."
    "...Yes, that was what anyone who saw the boy thought.{p}He had lost his right eye,{w=.2}\nbut he still had his life."
    "However the boy did not join in\nwith everyone's happiness around him,{w=.2}\nand he fully embraced the unhappiness within himself."
    "It wasn't even a few days after the cut was stitched{w=.2}\nbefore the boy collapsed due to a high fever."
    "The doctor examined him,{w=.2} only to realize that\nthe gash had become a dangerous weapon of sorts:\nBacteria had entered through it."
    "The boy's parents cried as they asked the doctor.{p}「Isn't there anything you can do? 」"
    "To that, the doctor replied slowly and calmly.{p}「There is a way. For this infection,{w=.2}\nthere is an effective medicine. 」"
    "「Then, our boy will- 」"
    "「Please be calm.{w=.2}\nTo be sure, I have found that medicine.{p}However... 」"
    "However,{w} the medicine was expensively priced,{p}as the doctor calmy and cruelly informed the parents."
    "The boy's family was the poorest in the village.{p}Yet they still had something saved up.{p}But now, it was no longer enough."
    "They frantically did what they could to gather money.{p}They worked from sun up to sun down,{w=.2}\nas well as asking their acquaintances."
    "Still, even that wasn't enough.{p}Time waits for no one,{w=.2}\nand it brings all to the same end."
    "And then, on the third day after the boy's collapse,\nhe departed from this world."
    "At his side as he laid face up,{w=.2} the boy's\napologetic parents only said, 「we can't do anything\nabout it, 」 and then it was as if he went to sleep."
    "This family was the poorest in all the village.{p}As such, the funeral service was carried out quietly."
    "But according to that family,\nall of the villagers attended and offered incense.{p}"
    "Among them, there was one\nchild who cried in front of the deceased."
    "It was that child,{w=.2}\nthe one who had given him the injury."
    "While the boy was alive, when asked about the wound\nhe would say 「I fell by myself. 」"
    "But such a wound could not be sustained from falling.{w=.2}\nWhen pressed, the parents, the doctor, and the boy\nall insisted that it was a fall until the end."
    "The poor boy died, and though\nthe bully realized the weight of his actions,{p}no one had the courage to speak to him about them."
    "So he could only cry before the boy's grave,{p}all the while apologizing desperately from his heart."
    "Even after the service ended,\nthe bully kept crying.{p}The soul-crushing weight never disappeared."
    "On the contrary, it kept piling up.{p}If he spoke to anyone he would have been comforted.{p}Sadly, he never found the courage."
    "「What if I just died? 」{p}Before he knew it, he was thinking about it."
    "Then one day, the bully saw the boy in a dream."
    "The distance between them was great,\nand it was also dark,\nso it was difficult to see the face."
    "But the gash down his face was visible,{w=.2}\nand it appeared that was all the boy thought about."
    "「Why are you making such a pained face? 」"
    "The boy asked, in the same kind\ntone he used with everyone.{p}"
    "Maybe it was because it was a dream,\nor maybe because it was the one he wronged."
    "Either way,\nthe bully let out everything that\nhe had been bottling up."
    "「I'm sorry that I killed you.{p}But I never told that to anyone.{p}I thought about dying too, and it hurts. 」"
    "「I see... 」"
    "The boy whispered quietly, then continued on like so."
    "「Do you still want to die? 」"
    "「Yeah, if it makes me feel better,\nthen dying is okay.{p}I don't want my life anymore! 」"
    "「Really. In that case... 」"
    "Then, the boy who was far away\nwas up close in an instant."
    "And the thing that was reflected\nin the bully's raised eye,{w=.2}\nalong with sinister laughter, was his left eye."
    
    stop music
    play sound attack00
    scene android_torahiko with qdis
    scene red with slashing
    scene black with sdis
    play sound taken
    
    "「Can I take that life and right eye? 」"
    
    scene black with sdis
    
    $ event_name = _("\"I'll Take It\" Ghost")
    scene candystorein with sdis
    show ka 001 at midleft
    show ko 005 at midright
    with wipe_right
    play music cicada01 fadein 3
    $ renpy.music.set_volume(0.3, 0.0, channel = "music")
    
    shopkeep "「...Well, you can say the bully woke up there,\n\ \ opened up to his parents about everything,\n\ \ and lived without further problems. 」"
    shopkeep "「But from then on, that boy would\n\ \ often appear in dreams and ask,\n\ \ 『Can I take that?』 and disappear. 」"
    shopkeep "「Then you would wake up and something in reality\n\ \ would actually have disappeared. 」"
    shopkeep "「And that is the story of the village's\n\ \ \"I'll take it\" ghost. 」"
    "The end,{w=.2} as the shopkeeper smiled and laughed."
    ko "「Meaning,{w=.2} that ghost is the\n\ \ one who took my ticket? 」"
    fn "「I see then...{p}\ \ I didn't know we had that kind of story. 」"
    ko "「It's the first I've heard of it too.\n\ \ And I've looked so much, too...{p}{nw}"
    show ko 001 with dis
    extend "Have you heard of it Kouya? 」"
    ka "「No, me neither.{p}\ \ ...But in this case,{w=.2}\n\ \ that can't possibly be it can it? 」"
    ka "「I've never seen anyone like\n\ \ that in my dreams,{w=.2} ever. 」"
    shopkeep "「Mhm.{w} Well, I don't know if this story\n\ \ is a true story or not,{w=.2} but it sounds like a story\n\ \ telling you to treat everything with care. 」"
    shopkeep "「And so,{w=.2} here you are. 」"
    fn "「Ah,{w=.2} isn't this a ticket!? 」"
    shopkeep "「It must have been picked up by the wind,{w=.2}\n\ \ and blown over to where I was. 」"
    shopkeep "「If this is something important,\n\ \ keep a better hold of it. 」"
    
    show ka 005 with dis
    
    ka "「I'm sorry. Thank you very much. 」"
    "Saying that, the shopkeeper went back to the counter.{p}So,{w=.2} basically..."
    
    play music daily02
    $ renpy.music.set_volume(0.8, 0.0, channel = "music")
    
    fn "「We were made fun of, weren't we? 」"
    ka "「...Maybe,{w=.2} but isn't it all right,\n\ \ since it's a good lesson? 」"
    fn "「Hmm,{w=.2} I guess so. 」"
    
    show ka 001 with dis
    
    ka "「Anyway, we got the ticket back,\n\ \ so it's a follow up from before."
    ka "「I'll treat you to whatever,\n\ \ so pick whatever you want. 」"
    fn "「Ahh,{w=.2} now that you mention it... 」"
    
    hide ka
    hide ko
    with wipe_right
    show to 007 at center with wipe_right
    show to at shivering
    
    fn "「Torahiko,{w=.2} what do you think...{p}\ \ Why are you shaking? 」{w} {nw}"
    show to at briefzoom
    extend "{w=.16}{nw}"
    show to at shivering
    
    to "「D-d-d-d-don't be stupid.{p}\ \ I-I-I-I-I'm not shaking at al-GAH!? 」"
    
    play sound crash21
    show to at still
    show to 005 at jump_up
    
    to "「Agh agh, I...{w=.2} I bit my tongue! 」"
    fn "「...What's up with you, seriously? 」"

    scene black with dis
    
    "One way and another, another day ended."
    "Even so,{w=.2} is that daytime ghost story the real thing?"
    "...{p}No way,{w=.2} right?"
    
    jump end16



#######################################################
label shin16:
    
    $ event_name = _("Let's go hang out at Shin-kun's!")

    play music free0211
    $ renpy.music.set_volume(0.8, 0.0, channel = "music")    
    scene shin_house_front with wipeleft    
    pause 1
    play sound tm2_chime002 
    pause 3
    
    fn "「Hello, this is [ln]. 」"
    "...{p}Huh? There's no answer.{p}I wonder what's up? Is he out?"
    who "「Yes, who might this be? 」"
    
    show shin_house_front at hshake
    
    fn "「Whoa!? 」"

    show am 002 at center with dis
    
    who "「Oh, it's you. 」"
    "That was a surprise...{p}When did he get behind me?"
    
    if shin_key1 == True:
        jump shin16_amaki_recent
    else:
        jump shin16_amaki_past

    ##############################################################
    label shin16_amaki_recent:
        
        who "「Welcome.{w} What business do you have today? 」"
        
        $ encounter_amaki = True 
        
        "This person is Amaki-san.{p}A servant in Shin-kun's house."
        "He's also Shin-kun's acting guardian,\nand before, when I met Shin-kun in the forest,\nhe was the one to treat me to lunch."
        fn "「Thank you for the food the other day.{p}I came to visit Shin-kun, is he here? 」"
    
        jump shin16_garden
    
    ###########################################################
    label shin16_amaki_past:    
    
        show am 001 with dis
        who "「[fn] [ln]-kun, right? 」"
        fn "「Oh,{w=.2} yes.{w} That's right.{p}Uh...Amaki-san? 」"
        
        $ encounter_amaki = True
    
        show am 002 with dis
        
        am "「Yes. You remember well. 」"
        "I somehow remember.{p}He's a servant in Shin-kun's house."
        fn "「Well, I came to visit Shin-kun... 」"
    
    ############################################################    
    label shin16_garden:
        
        show am 001 with dis
        
        am "「There's no one inside right now. 」"
        "Oh, so he is out..."
        
        show am 003 with dis
        
        am "「Well, maybe... 」"
        "Amaki-san started looking toward the garden\nas if searching for something."
        "I looked towards that way myself,\nbut I didn't notice anyone."
        
        show am 002 with dis
        
        am "「Come along. 」"
        "Even so, Amaki-san smiled widely\nand guided me in."
        
        scene black with wipe_right
        scene shin_house_garden with wipe_right
        show am 001 at farleft with dis
        
        "It's a beautifully maintained garden.{p}The lawn's uniformly cut,\nand the flower bed has so many colors."
        "Do they have a home garden elsewhere?\nTomatoes would be nice."
        "I wonder if Amaki-san takes care of the garden?\nWith how wide it is,\nit must count as heavy labor..."
        "There should be others who cook and clean."
        "I'm sure I remember other people\npainting the walls before."
        "Everything couldn't possibly\nbe done by one person, can it?"
        "That reminds me, I haven't seen any servants\nbesides Amaki-san."
        "But one person taking care of everything here?\n...what kind of person is he?"
        "In front of us,\nI stared at the somewhat small back.\nIt wasn't the back of just any catman though."
        
        scene forest_tree
        show am 001 at farleft
        with wipe_right
        
        "I was taken to the one tree in the garden."
        am "「Shin-kuuun, you have a guest. 」"
        fn "「Eh? 」"
        
        play sound si_gasa03
        pause 2
        
        "I didn't get what he was saying for a second,\nbut a branch up above rustled as if answering.\nAnd then..."
        
        play sound step01 
        show forest_tree at vshake
        
        fn "「Wah! 」"
        "Something suddenly jumped from out of the tree."
    
        show si 010 at center with dis
        
        fn "「S-Shin-kun? 」"
        si "「... 」"
        "Shin-kun was looking around without focusing\nhis eyes on anything,\nthen faced towards Amaki-san."
        si "「...Amaki, what is it? 」"
        
        show am 002 with dis
        
        am "「A friend came.{w} [ln]-kun. 」"
        si "「[ln]? 」"
        
        show am 001 with dis
        
        "At Amaki-san's words, he looked around again.\nSoon those eyes were focusing on me."
    
        show si 005 with dis
        
        si "「! [fn]!? 」"
        fn "「H-hi...good afternoon. 」"
        "As if out of consideration of things until now,\nShin-kun's surprised eyes became calm."
        "I was a bit awkward knowing I was treated\nlike an outsider, so I raised my hand as I spoke."
    
        show si 011 with dis
        
        si "「Good day. 」"
        fn "「What were you doing up in this tree? 」"
        
        show si 001 with dis
        
        si "「...reading.{p}\ \ You can tell by looking at this, right? 」"
        "Shin-kun held up what he was holding in his hands"
        "It was a fairly thick book that had a title written\nin a language I wasn't quite sure of.{p}French?"
        
        show am 002 with dis
        
        am "「This tree is Shin-kun's special seat.\n\ \ He always climbed this tree back then,\n\ \ giving me and the master such a fright. 」"
        
        show si 010 with dis
        
        si "「You're talking about the past again. 」"
        am "「Oh, sorry. 」"
        fn "「Is that so?{p}\ \ But I get it, what with a place like that. 」"
        "The shadow of the leaves look like an entrance,\nbut even with me standing directly underneath,\nI wouldn't know personally."
        
        show am 001 with dis
        
        am "「Well I did see you climbing earlier.{p}\ \ I thought you were still there since\n\ \ I didn't see you get down. 」"
        fn "「I see then. 」"
        
        show si 001 with dis
        
        si "「So, what did you come here for? 」"
        fn "「Well nothing in particular.{p}\ \ If there was something,\n\ \ I just wanted to see you, I guess? 」"
        
        show si 010 with dis
        
        si "「... 」"
        fn "「A... haha... 」"
        "Maybe I should called up ahead of time.{p}Shin-kun seemed to be in a bad mood\nas he silently gave me a polite smile."
        
        $ renpy.music.set_volume(0.6, 0.0, channel = "sound")
        play sound explosive
        pause .2
        play sound explosive
        $ renpy.music.set_volume(1.0, 0.0, channel = "sound")
        
        show am 002 with dis
        
        am "「Yes, yes.{p}\ \ How about we stop talking while standing there,\n\ \ and continue on inside since it's hot, okay? 」"
        
        show si 001 with dis
        
        si "「Oh, yes. 」"
        fn "「I'm sorry, for intruding so suddenly. 」"
        
        show am 001 with dis
        
        am "「It's fine. You don't need to hold back so much.{p}\ \ {nw}"
        show am 002 with dis
        extend "Shin-kun's happy too. 」"
        "I wonder...?"
        
        show si 010 with dis
        
        si "「Amaki. 」"
        "Shin-kun narrowed his eyes in displeasure,\nand Amaki-san kept smiling as he replied."
        "How do I put this?\nThese two feel less like master and servant\nand more like close relatives."
        "Almost like...{w=.2} family?"
        
        scene black with wipeleft    
        stop music fadeout 1 
        scene shin_bedroom with wipeleft
        pause 1    
        play music piano3_015
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")    
        show si 001 at center with dis
        
        si "「Wait for a moment.\n\ \ I'll go get some tea. 」"
        fn "「Okay. No need to fuss over me. 」"
        
        show si 004 with dis
        
        si "「Even if I don't I shouldn't be a bad host.{p}\ \ {nw}"
        show si 001 with dis
        extend "I'll be right back, so make yourself at home. 」"
        fn "「Oh, okay. Thanks. 」"
    
        hide si with dis
        pause .2
        
        play sound DoorCloseB
        
        "So this is Shin-kun's room.{p}Haven't been here since I was a kid."
        "I looked around restlessly,\nand partly unconsciously\nI started rummaging through."
        "The bed...{w} it's amazingly soft,\nand beautifully made like one from a hotel.{p}Does Shin-kun always sleep in it?"
        "A bookcase...\nthere's enough books to bury a wall lined up."
        "There aren't just Japanese books, there's English,\nand what seems to be French books mixed in too."
        "I thought it was strange there were some with\nsimilar spines lined up, so when I pulled them out\nthey seemed to be an original and a translated copy."
        "Why does he have two copies of the same book?{p}Is he comparing them side by side?"
        "I put the books back,\nthen went back to looking around."
        "I mean seriously now, this room is big.\nMy own room could fit in here."
        "The trash can... is clean and empty.\nAnd I really shouldn't open up his closet."
        "On another shelf on the bookcase,\nthere seem to be small containers."
        "Souvenirs from somewhere?\nThose along with some strange feeling\nornaments and animal figures were nicely arranged."
        "Oh, that rough black cat ornament.\nIt was a present Torahiko gave to Shin-kun.\nHe still has it."
        "It was supposed to replace the broken one from before,\nand it was made from Papier-mache with all his effort.\nShin-kun didn't look very happy about it though."
        "But he placed it over there,\nso maybe he does treasure it?{p}It really does bring back memories."
        "Enough with the shelf,\nI'm looking for something new now."
        "A desk...{p}does Shin-kun read and do his homework on it?"
        "Maybe I'm imagining it, but it kind of feels\nlike it was made from top quality lumber,\nand it has a solid atmoshpere."
        
        menu:
            "A. The top of the desk interests me.":
                jump shin16_desk_top
            "B. Maybe I'll peek inside.":
                jump shin16_desk_inside
    
    ########################################################
    label shin16_desk_top:
            
        $ event_name = _("Secret Diary")
        
        "Next to the desks is another shelf, and it looks like\nthere are even more books placed there.{p}There are dictionaries and reference books."
        "...?{p}However, among them there's one with no title,\nand it obviously looks different from the rest."
        "What kind of book is it?{p}I casually picked it up."
        "D...{w=.2}I...{w=.2}A...{w} 'diary'?\nSo it's a journal?\nShin-kun keeps a journal. I didn't know that."
        "I knew it was wrong of me,\nbut I still had this excitment bubbling up."
        
        stop music fadeout 1
        pause 1
        
        fn "「T-this is...! 」"
        "Amazing...{w} Unexpectedly, no wait,\nexpectedly after long consideration,\nI steeled myself and looked at the written words."
        
        play music free0428
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        
        "...it's hopeless.{w} I give up.{p}It seems it's all written in French,\nand I can't read a single word of it."
        "At least in English I can understand a few words.{p}It sucks, but I should put it back for now."
        
        play sound Door03Open 
        pause 1
        
        si "「Sorry to keep you waiting. 」"
        "The door opened up,\nand Shin-kun returned with a platter of tea and treats."
        
        show si 001 at center with dis
        
        si "「So. What are you doing over there? 」"
        fn "「N-nothing? 」"
        "I tried to feign calmness, but..."
        
        show si 002 with dis
        
        si "「Unfortunately, I haven't written anything\n\ \ I wouldn't want anyone to see. 」"
        fn "「Um... 」"
        "I was caught."
        fn "「I-it was a sudden impulse... 」"
        
        show si 001 with dis
        
        si "「Not a very polite one, no? 」"
        "Then, Shin-kun put the platter on the desk."
        fn "「Sorry. 」"
        
        show si 004 with dis
        
        si "「It's fine, you don't need to apologize.{p}\ \ {nw}"
        show si 001 with dis
        extend "Even if you were a ruder fellow,\n\ \ there are still others. I'm used to it. 」"
        "So he says, but I'm sure my standing dropped.\nDohoho..."
        si "「So then, what were you looking at? 」"
        fn "「T-this... 」"
        "I pointed at the leather bound book\nI just put back a moment ago."
        si "「Oh, the journal. 」"
        fn "「Sorry for picking it up. 」"
        
        show si 002 with dis
        
        si "「You probably couldn't read it anyway, right? 」"
        fn "「...yes. 」"
        
        show si 001 with dis
        
        si "「Even if you could,\n\ \ nothing important was written there.{p}\ \ It's just for practice. 」"
        "But isn't that a trick\nto prevent people from reading it?"
        
        show si 004 with dis
        
        si "「It's also an aid to learn French. 」"
        fn "「Eh? Really? 」"
        "What?\nDid I say that out loud?"
        
        show si 001 with dis
        
        si "「I normally don't use it,\n\ \ so I figured I'd do so so I won't forget.{p}\ \ {nw}"
        show si 010 with dis
        extend "It's my mother's native tongue after all 」"
        fn "「Your mom's? 」"
        
        show si 001 with dis
        
        si "「She's French.{p}\ \ On top of that, she's fluent in Japanese and English. 」"
        fn "「Oh. 」"
        "So she's bilingual...{p}No wait, wasn't that three languages?{p}So then the word is... trilingual?"
        "Either way, Shin-kun really is amazing.{p}He was reading English even back then,\nand now he can read French too."
        si "「Oh, I never did mention where she was from did I? 」"
        fn "「Nope.{p}\ \ I always saw the English books,\n\ \ so I figured she was American. 」"
        
        show si 003 with dis
        
        si "「So simple.\n\ \ Still, you should use some French and English though. 」"
        fn "「No, that's...{w} just a hobby or something. 」"
        
        show si 010 with dis
        
        si "「A... hobby. 」"
        "Shin-kun hung his head,\nlooking a bit lonely as he muttered to himself.{p}Uh, did I just say something wrong?"
    
        jump shin16_sit
    
    ###########################################################
    label shin16_desk_inside:
            
        $ event_name = _("Cell Phone")
        
        "There's a key to the drawer on the desk,\nbut the key went in without a hitch.{p}I really am starting to want to know what's inside."
        
        stop music fadeout 1
        pause 1
        play music free0421
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        
        fn "「(Shin-kun can be careless too...) 」"
        "I felt like a sneering evil magistrate\nwhen I had my hand on the drawer,\nwondering what I'd find inside."
        "No wait wait wait. This isn't carelessness,\nthis is just plain wrong barging in and peeking.{p}...still, not like I'll get another chance, right?"
        "He'd hide more private stuff somewhere else,\nand won't this give good insight\nto Shin-kun's life style?"
        "But when I looked inside..."
        
        play sound hit81
        
        "I don't have time to be conflicted about that!{p}Score one victory for childish curiosity."
        
        play sound tm2_slidedoor000 
        pause 1
        stop music fadeout 1.5
        
        "Huh?{w} Isn't this...a cell?{p}Inside the drawer was one simple cell phone.{p}And surprisingly it's a newer model than mine."
        "But, I thought cell phones don't work in this village?{p}Oh wait, maybe that's why it's in here."
        "Maybe we should exchange numbers and\nall since we're here.{p}No wait, if we do that, he'll know I looked."
        "Hmm...I wonder if I could just\nfind a chance to suggest it."
        "Since there wasn't anything else, I put it back."
        
        play sound Door03Open 
        pause 1
        
        si "「Sorry to keep you waiting. 」"
        "The door opened up,\nand Shin-kun returned with a platter of tea and treats."
        
        show si 001 at center with dis
        
        si "「So. What are you doing over there? 」"
        
        play music free0428
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        
        fn "「N-nothing? 」"
        "I tried to feign calmness, but..."
        
        show si 002 with dis
        
        si "「Unfortunately, I haven't placed anything I wouldn't\n\ \ want anyone to see there. 」"
        fn "「U-uh... 」"
        "I was caught."
        fn "「I-it was a sudden impulse... 」"
        
        show si 001 with dis
        
        si "「Not a very polite one, no? 」"
        "Then, Shin-kun put the platter on the desk."
        fn "「Sorry. 」"
        
        show si 004 with dis
        
        si "It's fine, you don't need to apologize.{p}\ \ {nw}"
        show si 001 with dis
        extend "Even if you were a ruder fellow,\n\ \ there are still others. I'm used to it. 」"
        "So he says, but I'm sure my standing dropped.\nDohoho..."
        si "「So then, what were you looking at? 」"
        fn "「... 」"
        "There's no way I can say it.{p}But I have no other option.{p}God please don't let Shin-kun be mad!"
        fn "「Inside the desk for a bit... 」"
        si "「... 」"
        
        show si 003 with dis
        
        si "「So you just opened it up and went on in? 」"
        fn "「S-sorry.{p}\ \ Only the first one. 」"
        
        show si 001 with dis
        
        si "「... 」"
        
        play sound tm2_slidedoor000
        pause 1
        
        "Shin-kun walked by me in silence,\nthen opened up the topmost drawer I touched."
        
        show si 010 with dis
        
        si "「This? 」"
        fn "「I didn't know you had a cell phone too. 」"
        
        show si 001 with dis
        
        si "「Well, kind of.{p}\ \ Not many chances to use it though. 」"
        fn "「This village is out of range and all, yeah. 」"
        "There's not much that can be done\nif the signal can't reach."
        fn "「Oh, how about we exchange numbers?{p}\ \ Even if we can't call in the village,\n\ \ we should be able to in Kazenari. 」"
        
        show si 005 with dis
        
        si "「What? 」"
        
        show si 010 with dis
        
        si "「...I'll consider it. 」"
        "I was rejected.{p}Maybe I overdid it."
        
        show si 001 with dis
        
        si "「Since I don't use it, I haven't touched it. 」"
        fn "「Really? 」"
        si "「If it's the same model as\n\ \ before I may as well keep it.{p}\ \ {nw}"
        show si 010 with dis
        extend "Not like I use either... 」"
        "Before... must mean that model he's had for so long.{p}But still, there's no signal here,\nso why does he have it?"
        "It doesn't seem like he'd use it\nfor other functions like music."
        fn "「Why did you buy it? 」"
        
        show si 001 with dis
        
        si "「If I say it's broken,\n\ \ I just get sent a new one.{p}\ \ Never mind that I don't use it. 」"
        fn "「Who sends it? 」"
        
        show si 009 with dis
        
        si "「...my father. 」"
        "Shin-kun sighed as he cast his eyes down.\nMaybe I shouldn't have asked that."
        
        $ shin_key2 = True 
    
    ##############################################################
    label shin16_sit:
        
        $ event_name = _("Where should we eat?")
        
        stop music fadeout 1
        
        fn "「Uh, anyways, let's eat.\n\ \ It'll get cold if we leave it alone. 」"
        
        show si 001 with dis
        
        si "「Oh,{w=.2}{nw}"
        show si 002 with dis
        extend " yes. That's true. 」"
        
        play music daily03
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        
        "The topic changed indirectly as Shin put away\nwhat he was holding and returned to the platter."
        "Oh wait,\nmaybe I should be calling it a tray instead.{p}Different feel and all."
        "On top of the tray were two chocolate cakes,\ntwo tea cups and one tea pot,\nand even a small dish with a pyramid of sugar cubes."
        
        show si 001 with dis
        
        si "「Put in as much sugar as you like. 」"
        fn "「Okay. 」"
        "As he said so, Shin-kun poured the tea.{p}As the black tea filled the cups, the steam rose\nand its aroma gently filled the room."
        
        show si 005 with dis
        
        si "「Ah. 」"
        fn "「Huh? What? 」"
        
        show si 010 with dis
        
        si "「I don't have two chairs ready. 」"
        "Oh yeah, there's only one chair in this room.\nWell if we're using something else as a chair..."
        
        menu:
            "A. Sitting on the bed should be fine.":
                jump shin16_sit_bed
            "B. How about sitting on the floor?":
                jump shin16_sit_floor
    
    ###################################################
    label shin16_sit_bed:
                
        fn "「What if you brought it to the bed? 」"
        "If Shin-kun sits on the bed,\nand the tray is set on a side table,\nthat should solve the seating problem."
        
        show si 002 with dis
        
        si "「Oh, I suppose so. Why don't we then? 」"
    
        jump shin16_snacks
    
    ####################################################
    label shin16_sit_floor:
        
        fn "「How about we eat on the floor? 」"
        
        show si 005 with dis
        
        si "「Eh? 」"
        "Ah crap.\nJust one word from Shin-kun and I knew he was looking up.\n\"That's disgraceful!\" coming in {w=.2}3, {w=.2}2, {w=.2}1..."
        
        show si 001 with dis
        
        si "「The floor...?\n{nw}"
        show si 002 with dis
        extend "I guess it's okay once in a while... 」"
        fn "「Yeah that was disgraceful wasn't it...{p}\ \ ...{w=.2}what? 」"
        "Wait, what now?"
        
        show si 001 with dis
        
        si "「So today we'll be eating on the floor? 」"
        fn "「Whaaat!? 」"
        
        show si 005 with dis
        
        si "「W-why are you shouting all of a sudden? 」"
        fn "「Nononono, Shin-kun, you can't eat on the floor,\n\ \ absolutely not, you need to eat ELEGANTLY. 」"
        
        show si 010 with dis
        
        si "「But didn't you suggest it? 」"
        fn "「Yeah, but... 」"
        "But if Shin-kun eats on the floor my image of him..."
        
        show si 002 with dis
        
        si "「It's true that isn't refined,\n\ \ but I think it's okay sometimes.{p}\ \ {nw}"
        show si 001 with dis
        "There's probably people who do that always though. 」"
        "He's probably talking about that guy.{p}No, maybe it's that other guy?{p}...or rather there's no one else but them."
        
        show si 002 with dis
        
        si "「Well then, does that seem spacious enough? 」"
        
        $ shin_step2 = True
    
    ################################################################
    label shin16_snacks:
            
        $ event_name = _("Snack Time")

        hide si with sdis
        
        "We moved ourselves to new positions,\nand Shin-kun sat opposite of me."
        "I don't normally do this,\nbut somehow the mood and our hands held\nout in front of our chests all fit together."
        fn "「Time to eat. 」"
        
        show si 002 at center with dis
        
        si "「Bon appetit. 」"
        "Shin-kun giggled.{p}Am I really that laughable?"
        "As I got a bit more embarrassed,\nI put my fork into the soft spongy cake.{p}Inside the thick chocolate brimmed over."
        fn "「Whoa. 」"
        "Could it be that the batter wasn't baked?"
        
        show si 001 with dis
        
        si "「What is it? 」"
        fn "「Oh uh, is this raw? 」"
        
        show si 004 with dis
        
        si "「Yes, that's the kind of cake it is. 」"
        fn "「Really? 」"
        
        show si 001 with dis
        
        si "「It's a chocolate fondant.\n\ \ Is this your first time with one? 」"
        fn "「Y-yeah. 」"
        "Shin-kun's calm gaze hurts...{p}You don't have to look at me like that."
        si "「It tastes great while the inside is syrupy.\n\ \ You should eat it before it gets cold. 」"
        fn "「O-okay. 」"
        "Once again I put my fork into the fondant.{p}Is it okay to eat it while the chocolate's all mixed?{p}Oh man, it's just pouring out like, whoa."
        "Whatever, I'm gonna just dive in.{w} I took a\nmouthful of the partly broken cake into my mouth,\nand the fragrant aroma of cocoa filled me up."
        "The sweet fragrant flavor cut through to my nose.{p}Barely even a moment later,\nand I already wanted the next bite."
        fn "「This is great! 」"
        
        show si 004 with dis
        
        si "「...{p}\ \ {nw}"
        show si 002 with dis
        extend "Yes, it does seem to be baked well. 」"
        fn "「Amaki-san's cooking is as great as ever. 」"
    
        show si 001 with qdis
        
        si "「... 」"
        "H-huh?{p}I say one word and Shin-kun's face stiffens.{p}Did I say something bad?"
        
        show si 010 with dis
        
        si "「...well, it is a recipe from Amaki. 」"
        fn "「Eh? 」"
        
        show si 001 with dis
        
        si "「I was the one that made this. 」"
        fn "{size=+15}「WHAT!? 」"
        
        show si 010 with dis
        
        si "「... 」"
        fn "「No, wait, that's not what I meant. 」"
        si "「And what *does* that mean? 」"
        "I thought I smoothed things over for a second,\n\ \ but he cut back right away."
        fn "「It's just, I didn't know you could cook. 」"
        
        show si 001 with dis
        
        si "「And that's so surprising it makes you yell out? 」"
        fn "「...I'm so sorry. 」"
        
        show si 005 with dis
        
        si "「Huh? 」"
        
        show si 010 with dis
        
        si "「Even if you apologize it's kind of a problem, no? 」"
        fn "「Well, uh... 」"
        "I couldn't get the words out, and silence fell over.{p}{nw}"
        show si 003 with dis
        extend "The thing that broke it was a sigh from Shin-kun."
        
        show si 009 with dis
        
        si "「..sorry.\n\ \ We were having tea and I ruined the mood. 」"
        fn "「No, I didn't have to shout like that, I'm sorry. 」"
        
        show si 001 with dis
        
        si "「Well even if I can cook,\n\ \ I can't make anything grand.{p}\ \ I only know how to make sweets. 」"
        fn "「I see then. But, aren't you amazing\n\ \ for being able to make sweets?\n\ \ They taste so good and all. 」"
        
        show si 005 with dis
        pause .3
        show si 011 with dis
        
        si "「T-thank you...{p}\ \ {nw}"
        show si 001 with dis
        extend "It was fun while Amaki was helping me.\n\ \ Right now it's more like a hobby I suppose. 」"
        fn "「Is that so? 」"
        "Shin-kun put his silver fork in the cake,\nthen put a piece into his mouth."
        
        show si 002 with dis
        
        "As soon as he tasted it, I felt like\nI saw a smile on that normally moody-looking face."
        "I repented for souring the mood earlier,\nand I took another bite of the cake myself."
        "The sweetness melted in my mouth\nas the aroma spread out."
        "This really is an incredible cake.\nI'd have believed him if he said\nit was bought somewhere."
        "I didn't know Shin-kun had hobbies aside from reading,\nbut he has so much talent at it.{p}Mindblowing..."
        "...huh?{p}Wait a second.{p}Doesn't that mean I'm eating his handmade sweets?"
        
        play sound freeze04
        
        "As soon as I thought that,\na switch flipped on inside me.\nShin-kun made sweets for my sake...!"
        "A-and of course he'd be wearing an apron right?"
        "Two supple arms over a fluttery white apron.{p}An eggbeater for a meringue in one hand,\na smile over the shoulders."
        "At the end of the mouth,\na glimpse of a white tooth."
        "{cps=5}{size=+15}T H E  U L T I M A T E ! ! !"
        "Of course there should be a royal kachusha on\nlike a maid,{w} no wait, I can keep my unadorned\nimage of Shin-kun and,"
        "no, no, maybe even the forbidden naked apron...!"
        
        show si 001 with dis
        
        si "「...[fn]? 」"
        fn "「YEEES!?\nI mean, yeah? 」"
        si "「You've been making a creepy face for a while now,\n\ \ so what are you thinking of? 」"
        fn "「Nothing, nothing at all! 」"
        
        show si 010 with dis
        
        si "「Uh huh. 」"
        
        show si 002 with dis
        
        si "「Are you thinking of someone you like? 」"
        fn "{size=+15}「What!? 」"
        
        show si 001 with dis
        
        si "「I'm kidding. 」"
        "That was horrible for a joke...\nHe was right though. And now I feel all guilty."
        
        show si 004 with dis
        
        si "「...it didn't seem possible,\n\ \ but was I actually right? 」"
        fn "「N-no, no way. I don't have anyone I like anyway. 」"
        
        show si 001 with dis
        
        si "「But didn't you say there was someone? Back at camp. 」"
        fn "「Eh? Oh, I was just mouthing off\n\ \ because of the mood then. 」"
        "When I thought about what I said to Shin-kun,\nright after there was one thing that came to mind."
        si "「...it's one-sided? 」"
        fn "「W-who can say?\nMaybe so? 」"
        "Either way, that person is sitting opposite me\noffering me handmade snacks."
        "However, I feel a bit uncomfortable\ngoing so far as to say it's love right now.{p}Why is that? Is it fine to leave it one-sided?"
        "When I thought about it for now,\nI couldn't get an answer.\nAt least, 'like' doesn't seem to be wrong..."
        fn "「Is... it maybe?\n\ \ I don't really know myself. 」"
        si "「... 」"
        
        show si 002 with dis
        
        si "「What if I helped you? 」"
        fn "「Huh? 」"
        
        show si 001 with dis
        
        si "「Here. 」"
        fn "「 ?  」"
        "Shin-kun brought his fork to his plate and...\nthe cake? That's what he's pointing at."
        
        show si 002 with dis
        
        si "「I think girls would accept sweet things,\n\ \ so what if I taught you someting simple? 」"
        fn "「Uhh... 」"
        "Uh, well, sorry Shin-kun.\nThe one I like...isn't a girl..."
        "I know he's doing it as a favor for me,\nbut it hurts so much to see how different\nfrom normal those pure eyes are."
        "What should I do?"
        
        menu:
            "A. Well he's offering and all.":
                jump shin16_lesson_accept
            "B. But even with the suddent offer...":
                jump shin16_lesson_decline
    
    ##########################################################
    label shin16_lesson_accept:
        
        $ shin_lesson = True
        
        "Huh?\nBut isn't this a chance to get closer to Shin-kun？"
        fn "「Well, maybe I will ask for your help then. 」"
        "I gave two answers to Shin-kun's offer."
        si "「I can't teach you anything grand though.{p}\ \ {nw}"
        show si 001 with dis
        extend "If I had to say,\n\ \ this is about how much I can help. 」"
        "Shin-kun put his fork down with a clink.{p}Suddenly the cake on top of my plate was gone."
        "I felt a little unsatisfied,\nbut Shin-kun and I picked up our tea."
        "Inside my mouth, it was awash with the scent of black\ntea with some sugar and the refreshing bitterness.{p}Did Shin-kun brew this tea too?"
        fn "「You say only this much, but it's still very good.\n\ \ Good enough to be sold in stores. 」"
        
        show si 004 with dis
        
        si "「Is that flattery? 」"
        fn "「I'm serious.\n\ \ It looks beautiful too. 」"
        
        show si 001 with dis
        
        si "「I just follow the recipe.{w} It will look right\n\ \ just from that, but it's still nothing that can\n\ \ bring in money, isn't it? 」"
        "Hmm, I think it would sell well enough though."
        fn "「I dunno. 」"
        
        show si 004 with dis
        
        si "「If you do as I say, then anyone can make it.{p}\ \ If you want to get money for it,\n\ \ that's your own determination, 」"
        si "「and if you don't use any techniques,\n\ \ there's no meaning. 」"
        "Even if it's about himself, Shin-kun resolutely\ndeclared so just like we used to be talked to.\nHe really is harsh on himself too."
        
        show si 002 with dis
        
        si "「Besides, it's a hobby\n\ \ so there is a question on if I can continue.{p}\ \ {nw}"
        show si 001 with dis
        extend "And so, I'd like to leave things as they are. 」"
        fn "「I see. 」"
        "If that's the case, am I only going to get a\ndisagreeable response if I unexpectedly flatter him?"
        "No wait,\neven if I don't say anything it's genuinely good."
        
        show si 004 with dis
        
        "I tried not to be noticed as I stared again\nat the moody-looking composed face\nof my childhood friend as he sipped his tea."
        fn "「So can we start with things tomorrow? 」"
        
        show si 001 with dis
        
        si "「Doesn't matter to me. 」"
        "Yes!{p}I can get closer to him like this.{p}I have no regrets, I have to make so many memories."
    
        jump end16
    
    #####################################################
    label shin16_lesson_decline:
        
        $ shin_lesson = False        
        
        fn "「...sorry.{p}\ \ I don't think I can really make treats. 」"
        "I declined Shin-kun's offer."
        
        show si 001 with dis
        
        si "「Too meddlesome? 」"
        fn "「Of course not! It's just...\n\ \ How do I say this. 」"
        si "「... 」"
        fn "「I guess I'm still not sure about my own feelings.\n\ \ I do want to hang out with this person,\n\ \ but I'm not confident enough to consider confessing. 」"
        fn "「There's no mistaking that I like them,\n\ \ but I still can't imagine going out with them,\n\ \ or what I'd want to do with them before that. 」"
        fn "「I'm happy for your feelings Shin-kun,\n\ \ but with the way I am now, \n\ \ I don't know what best to do. 」"
        si "「I'm surprised. 」"
        fn "「R-really? 」"
        
        show si 002 with dis
        
        si "「I thought of you as more of the\n\ \ type to rush in without thinking.{p}\ \ {nw}"
        show si 001 with dis
        extend "I didn't think you'd think that hard about it. 」"
        fn "「You never hold back do you... 」"
        
        show si 002 with dis
        
        si "「Hmhm, sorry.{p}\ \ {nw}"
        show si 001 with dis
        extend "Compared to back then, you really calmed down. 」"
        fn "「5 years have passed and all. 」"
        "The fork hit the plate with a ding.{p}When I looked down thinking that was weird,\nI realized that the cake was all gone."
        "There's nothing left anymore...\nIt sucks, but I didn't ask for seconds,\nso I put the fork down and reached for the tea."
        fn "「But, your feelings honestly make me happy.\n\ \ If you make a cake this delicious,\n\ \ I'll always end up wanting to eat it. 」"
        
        show si 004 with dis
        
        si "「Is that flattery? 」"
        fn "「You break my heart!\n\ \ I was being serious. 」"
        
        si "「I see.{w} {nw}"
        show si 002 with dis
        extend " Well, thank you. 」"
        "Shin-kun smiled sweetly.\nIt surprised me so much that my heart skipped a beat.\nThis is cheating!"
        "Oh, but I really did it now.\nWhen I really think about it,\nthat was a huge chance to get closer to Shin-kun."
        fn "「Oh, instead of studying on cooking,\n\ \ can I ask for your help with studying in general? 」"
        "I only just noticed the chance dangling in front of me,\nso I tried asking for something else\nin a moment's thought."
        
        show si 001 with dis
        
        si "「Your summer vacation homework? 」"
        fn "「Oh, you knew? 」"
        
        show si 002 with dis
        
        si "「I'm feeling a bit more relaxed now that\n\ \ that shrewd part of you stayed the same. 」"
        fn "「...are you saying I'm simplistic? 」"
        si "「Who can say? 」"
        fn "「You're mean! 」"
        "As he laughed while pricking me with that joke,\nit looks like he didn't change that part of him either.\nI made a mental note of it."
        
        show si 001 with dis
        
        si "「I don't mind. I have time during the day.\n\ \ It's just, could you call up beforehand\n\ \ out of consideration? 」"
        si "「It's possible we might just pass each other. 」"
        fn "「Okay, got it.{p}\ \ In that case, can we start tomorrow? 」"
        
        show si 002 with dis
        
        si "「You're so abrupt, just like always.{p}\ \ {nw}"
        show si 001 with dis
        extend "I don't mind. 」"
        "Alright!{p}Now I can spend this summer together with Shin-kun.{p}I have no regrets, I have to make so many memories."
        fn "「Alright, I'll be in your care. 」"
        
        show si 004 with dis
        
        si "「Yes, yes. 」"
        
        jump end16
    
#######################################################   
label end16:
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

    jump day17


    
