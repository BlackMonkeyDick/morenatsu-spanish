###Day 28
label day28:
    
    $ renpy.music.set_volume(1.0, 0.0, channel = "music")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound2")
    
    $ day = 28
    $ the_date = "August 28"
    $ event_name = "８月28日"
    
    if favorite == "tatsuki" or favorite == "shun" or favorite == "kouya":
        window hide
        play music birds_chirping
            
        scene sky01 
        show text "{size=+130}August 28" at truecenter
        with Dissolve(.5)
        
        pause 3
        scene black with Dissolve(1)
        pause .4
        
    else:
        jump day29
        
    $ renpy.jump(favorite + "28")
    

########################################################
label tatsuki28:
    
    $ event_name = "I can't do it"

    play music cicada01
    $ renpy.music.set_volume(0.4, 0.0, channel = "music")
    scene tatsuki_bedroom with wipe_corner
    
    "The work on the table has gone on for two days already,\nbut it seems we still haven't gotten anywhere."
    "It should be a simple job, but Tatsu-nii became more\nworried about it."

    show ta 004 at center with dis
    
    ta "「Daaah, I don't get this.{p}\ \ It's carved beautifully, so why won't it go in? 」"
    fn "「Is a carpenter even able to fix furniture? 」"
    
    show ta 008 with dis
    
    ta "「In the old days, when building temples, they'd get\n\ \ a whole bunch of carpenters in. Sometimes, though,\n\ \ they'd have too many carpenters for the job. 」"
    ta "「It seems that some of them became furniture crafters.{p}\ \ They say that even the woodcrafters from Hakone had\n\ \ roots in temple building. 」"
    ta "「That's why the classic style won't work all the time,\n\ \ but it should be able to service things.\n\ \ We feel the same lumber being used after all. 」"
    
    show ta 006 with dis
    
    ta "「Still, I feel relieved... 」"
    fn "「Let's take it easy and not rush it.\n\ \ The mayor said it'd be all right\n\ \ to bring it back whenever. 」"
    
    show ta 005 with dis
    
    ta "「Yeah. After all, I'm just a humble apprentice.\n\ \ I can't even fix one little table. 」"
    fn "It's your first time, it happens. 」"
    ta "「I'm a useless man.\n\ \ I'm all talk.\n\ \ I can't even keep a childhood promise. 」"
    ta "「The plane was doomed from the start.\n\ \ I can't fix the table, only make mistakes.\n\ \ I can't do anything... I'm worthless. 」"
    fn "「...Do you-{w=.2} do you really think that? 」"
    
    show ta 010 with dis
    
    ta "「Yeah. Nothing can be done about me,\n\ \ I only just saw that. My dream, of becoming\n\ \ Japan's best craftsman? Laughable. 」"
    
    menu:
        "A. You dumbass!":
            jump tatsuki28_dumbass
        "B. That's not true...":
            jump tatsuki28_goodbye
        "C. What the...":
            jump tatsuki28_shutdown

    ##############################################################    
    label tatsuki28_goodbye:

        $ event_name = "Goodbye"
            
        fn "「If it's you, you can do it. 」"
        "「There's just a little left, let's do our best. 」"
        
        show ta 006 with dis
        
        ta "「This is all I got for doing my best... 」"
        fn "「No way... You can't give up. 」"
        ta "「... 」"
        fn "「You can do it, definitely. 」"
        
        show ta 005 with dis
        
        ta "「It's hopeless... 」"
        fn "「Tatsu-nii, hang in there...{p}\ \ You're just in a slump right now. 」"
        ta "「It's over. I can't do anything... 」"
        "Did he run out of willpower or something?"
        "Tatsu-nii continued to hang his head in silence."
        "His bright and cheery demeanor was nowhere to be found."
    
        show ta 008 with dis
        
        ta "「Sorry, could you go home for the day? 」"
        fn "「Eh? 」"
        
        show ta 005 with dis
        
        ta "「I want to be alone for a bit... 」"
        fn "「But... 」"
        "I wanted to do something, but I couldn't\ndo anything..."
        "In times like this, what's the best thing\nto do...?"
        fn "「Okay... I'll go. 」"
        ta "「Yeah. 」"
        fn "「See you tomorrow. 」"
        
        stop music fadeout 1
        scene black with sdis
        
        "The next day, Tatsu-nii's slump continued.{p}I still couldn't do anything,\nand time passed awkwardly."
        "For a little while,\nall we could accomplish was\nincreasing the gap between us."
        "Gradually, it became harder to go the Midoriya\nGroup's place, and along with that, it got harder to\nsee Tatsu-nii's face."
        
        play music melodious05
        $ renpy.music.set_volume(0.9, 0.0, channel = "music")
        play sound bus_idling loop
        scene bus with wipe_corner
        
        "After that, the day that I would\nreturn to the city crept up on me."
        "I still hung out with everyone,\nbut I can't really remember much."
        "The only thing I could understand was\nthat my mood would never clear up,\nand that Summer had passed by uneventfully."
        "Even when everyone saw me off at the bus stop,\nthe farewells as I got on were reasonable.\nI never saw Tatsu-nii there, in the end."
        "I think he was afraid to make eye contact with me.\nOur relationship clearly fell apart."
        "It also feels like it broke\nour ties with everyone else..."
        "I probably can't go back to that time I\ncould laugh innocently with them all.\nAll because I felt guilty about not doing anything."
        "After that, I never returned to Waterford Village."
        "Ah, if only I could fly in the sky..."
        "It'd be great if I could go back to that time."
        "Fin."
        
        stop sound fadeout 1.5
        stop music fadeout 1.5
        scene black with sdis
        pause 5
        scene old_house1 with sdis
        pause 1.5

        $ event_name = "Grandpa Shigure's Diary"

        play sound rainstorm
        pause 1.5
        play music free60
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
    
        show sg 002 at midright with dis
        show cu 005 at offright_far
        
        sg "「Hohoho! I'd like to thank all you players\n\ \ out there for your hard work. 」"
        sg "「You've already noticed by now,\n\ \ but this is a bad end. 」"
        cu "「Emergency, emergency! 」{w} {nw}"        
        show cu at move_offleft_far(1)
        extend "{w=1}{nw}"
        show cu at offright_far
        extend "{w=.01}{nw}"
        show cu at move_midleft(1)
        extend "{w=1}{nw}"
        show cu at jump_up
        
        cu "「Emergencyyy! 」"
        
        show sg 001 with dis
        
        sg "「Why so noisy? 」"
        
        show cu 008 with dis
        
        cu "「This is bad! Even though we're\n\ \ in the middle o' the game,\n\ \ it's finished, even though it's incomplete... 」"
        sg "「...That's because this is a bad ending. 」"
        
        show cu 006 with dis
        
        cu "「F'real!? 」"
        sg "「We're talking here because it is a bad end. 」"
        
        show cu 008 with dis
        
        cu "「I didn't know... 」"
        sg "「And because this is a bad end,\n\ \ that wasn't the right choice earlier. 」"
        cu "「Hmm, but Aniki comforted him though. 」"
        sg "「You should probably have tried confronting him. 」"
        sg "「When your friend is feeling down,\n\ \ sometimes kind words fail,\n\ \ and so you need to be harsh. 」"
        
        show cu 005 with dis
        
        cu "「I see! As expected!\n\ \ Then next time should go okay! 」"
        sg "「By the way... 」"
        
        show cu 001 with dis
        
        cu "「By the way? 」"
        sg "「You were made to think this was a bad\n\ \ end, but now it's a new development. 」"
        sg "「His next flight failed again and he\n\ \ lost his life. 」"
        
        show cu 005 with dis
        
        cu "「Whoa, really? 」"
        sg "「After [fn]-kun returned home,\n\ \ Tatsuki-kun somehow regained his footing,\n\ \ but his next flight failed, and he lost his life. 」"
        
        show cu 006 with dis
        
        cu "「Seriously!? 」"
        sg "「[fn]-kun found out about that and\n\ \ returned, and he stood in front of\n\ \ Tatsuki-kun's grave. 」"
        sg "「There, one of us sub-characters from\n\ \ Tatsuki's story appeared, and while expressing\n\ \ their condolences, it led to a dramatic love scene... 」"
        
        show cu 008 with dis
        
        cu "「Owowowow... 」"
        sg "「Does it hurt? 」"
        
        show cu 004 with dis
        
        cu "「It hurts... 」"
        
        show sg 002 with dis
        
        sg "「Well, the author thought about that,\n\ \ since they spent all night writing about it. 」"
        sg "「The next day, it seems they remembered the\n\ \ developments and collapsed. 」"
        
        show cu 006 at briefzoom
        pause .2
        
        cu "「I'll collapse it. 」"
        
        show cu 008 with dis
        
        cu "「To start with, the story was too light hearted... 」"
        
        show sg 001 with dis
        
        sg "「Oh, is it that time already?\n\ \ We don't have any time left, it seems. 」"
        
        show cu 001 with dis
        
        cu "「We haveta hurry on back. 」"
        sg "「So it would seem. 」"
        
        show sg 002 with dis
        
        sg "「Our talk has gotten off track, but an\n\ \ occasional scolding is a mark of true friendship. 」"
        
        show cu 008 with dis
        
        cu "「Crap, we gotta go. 」"
        sg "「Hum. So busy... Oh yes, next time on Tatsuki's Route\n\ \ Talk Corner, a new character's scenario\n\ \ will be introduced, so look forward to that. 」"
        
        show cu 005 with dis
        
        cu "「F'real? Who is it, who's the new character? 」"
        sg "「That's still a secret. 」"
        sg "「Now then, may we meet again.{p}\ \ Head for the proper ending this time. 」"
        
        show cu 002 with dis
        
        cu "「Buh-bye! 」"
        
        scene old_house1 with sdis
        pause 1
        
        $ persistent.backtrack_name = "tatsuki28"
        play music awkward
        call screen backtrack

##########################################################        
    label tatsuki28_shutdown:

        $ event_name = "A Button between Tatsuki's Eyebrows..."
        
        "What the...? There's a button in the middle\nof Tatsu-nii's forehead."
        "I never noticed until now."
        
        show ta 005 with dis
        
        ta "「No matter what I do it ends in failure.{p}\ \ I'm no good. 」"
        "I have a different meaning of no good.{p}I can't concentrate with that button there."
        
        show ta 006 with dis
        
        ta "「*sigh* Why am I doing this...? 」"
        "What happens if I push it...?\nScrew it, press the button!"
        
        show ta 005 with dis
        
        ta "「I'm...{p}\ \ {nw}"
        show ta 003 at jump_up
        extend "Hey,{w=.2} what are you doing.{w=.2} Stop! 」"
        fn "「Tatsu-nii, I'm sorry.\n\ \ I couldn't resist. 」"
        "Beep!{nw}"
        stop music 
        play sound pyoro45_a
        pause
        
        play sound puu56
        show ta at shivering
        
        ta "「UIIII,{w=.2} GAGAGA,{w=.2} PII- *Sputter* 」{nw}"
        hide ta with wipe_down
        extend ""
        
        fn "「W-{w=.2}what, this is... 」"
        "What is this...{p}Tatsu-nii is a robot!"
        "I must have pressed his power switch,\nfor sure."
        who "「Well, this certainly puts a damper on things... 」"
    
        play sound bosu34
        scene tatsukihouse_inside
        show sg 001 at center
        with wipeleft
        
        "I turned to face where the voice came from,\nand there stood Shigure-san."
        
        show sg 002 with dis
        
        sg "「I didn't think you'd notice. 」"
        fn "「Shigure-san, do you know something about this? 」"
        
        play music sad01 
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        
        sg "「Of course I do. That is my biggest masterpiece. 」"
        fn "「Biggest masterpiece? 」"
        
        show sg 001 with dis
        
        sg "「Yes. An android capable of deciding things\n\ \ by itself, is like other people, and is able\n\ \ to have an independant daily life... 」"
        sg "「That is Tatsuki Midoriya's true form. 」"
        fn "「That can't be... 」"
        sg "「He's different from a bug-riddled prototype,\n\ \ and he should be perfect, but...{p}\ \ somehow this one has a bug in it now, too. 」"
        
        show sg 002 with dis
        
        sg "「And the cause of that is you, [fn]-kun. 」"
        fn "「A prototype with bugs? You don't mean... 」"
        
        show sg 001 with dis
        
        sg "「Yes.{w=.2} The Master is also an android I created. 」"
        "I don't understand anymore."
        "Everything I believed in before my eyes\nwas crumbling to pieces."
        sg "「Now,{w=.2} do you know why I told you my secrets? 」"
        fn "「... 」"
        
        stop music
        play sound load_gun
        scene evil_mayor
        pause .5
        
        sg "「[fn]-kun... You're in the way.{p}\ \ Will you disappear? 」"
        "Shigure-san pulled out a gun from his breast pocket,\nand turned to face me."
        ta "「...S{w=.2}...S{w=.2}...oP{w=.2}...... 」{w=.2}"
        sg "「Hm,{w=.2} did you say something? 」"
        fn "「Kuh...! 」"
        "This is a desperate spot. What do I do?"
        sg "「This is the end. You'll move on to\n\ \ the next world... 」"
        
        play music melodious06 
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        scene tatsukihouse_ceiling
        
        ta "{size=+15}「ST-OP! 」"
        sg "「W-{w=.2}what!? 」"
        
        scene tatsukihouse_ceiling with dis
        scene android_tatsuki with sdis
        
        "Tatsu-nii stood up, even though he should have\nbeen cut off from power,\nand he jumped out in front of me."
        sg "「You shouldn't be able to move without your\n\ \ power on... 」"
        ta "「I WON'T AL-LOW A-NY-ONE TO HURT [fn] 」"
        sg "「Such impudence. If you keep on like this, then\n\ \ I'll have to erase you. 」"
        "At this rate they'll kill each other.{p}Still, I have to get out of here."
        fn "「Tatsu-nii, let's get away from here! 」"
        ta "「THANKS. WE'LL AL-WAYS,{w=.2} BE FRIENDS? 」"
        "It was like I saw Tatsu-nii laughing\nuntil the very end."
        fn "「Tatsu-nii? 」"
        "Tatsu-nii shoved me out of the way,\nand ran straight at Shigure-san."
        
        play sound  bosu31
        scene tatsukihouse_ceiling
        pause .2
        
        sg "「Stop, don't come here! 」{w}{nw}"        
        play sound gunshot
        extend "{w=.5}{nw}"
        
        "He pulled the gun's trigger, and the bullet pierced through\nTatsu-nii's body."
        sg "「Uwoooh! Don't come- don't come over here! 」{w}{nw}"        
        play sound gunshot
        extend "{w=.4}{nw}"
        play sound gunshot
        extend "{w=.255}{nw}"
        play sound gunshot
        extend "{w=.4}{nw}"
        
        "So many bullets blasted into Tatsu-nii's body,\nyet he never fell."
        "He can't see anything besides Shigure-san anymore.{p}He can't stop. He just plowed through."
        sg "「Impossible? You plan on self-destructing!? 」"
        
        $ renpy.music.set_volume(1.0, 0.0, channel = "music")
        
        ta "「{cps=5}MY PRE-CIOUS FRIENDS{w=.2}...{w=.2}...THANKS YOU GUYS. 」"
        fn "「Tatsu-niiii! 」"
        
        play sound bom19_b
        stop music fadeout 2
        scene white with explosion_slow
        
        "Tatsu-nii's body gave off a flash,\nand flames rolled up."
        "The explosion destroyed everything close by,\nand set fire to the things that weren't."
        "Shigure-san and the Midoriya Group all went up in flames."
        
        play music burning_wood fadein 2.5
        scene tatsukihouse_fire with sdis
        
        "Somehow, I escaped, and could only watch as\nthe flames spread across the whole building."
        fn "「How could this have happened... 」"
    
        show to 005 at center with wipe_right
        
        to "「[fn], what is all this?\n\ \ Tatsu-nii's house is on fire! 」"
        fn "「Torahiko...{w=.2} ... Tatsu-nii,\n\ \ he sacrificed himself,\n\ \ and he protected me. 」"
        to "「Calm down,{w=.2} all right?\n\ \ I'm here so you can relax.{p}\ \ Because I... 」"
        
        scene android_torahiko
    
        to "「{cps=10}I'M YOUR,{w=.2} PRE-CIOUS FRIEND RIGHT? 」"
        "Fin."
        
        $ event_name = "Grandpa Shigure's Diary"

        scene android_torahiko with dis
        scene black with sdis
        pause 5
        play sound rainstorm
        pause 1.5
        scene old_house1 with sdis
        play music free60
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        
        show sg 002 at midright
        show cu 008 at midleft
        with dis
        
        sg "「Wow, what a nice story.{p}\ \ Don't you think so too, Chuukichi-kun? 」"
    
        show cu 006 at hit_left
        pause .2
        
        cu "「What was? 」"
        
        show sg 001 with dis
        
        sg "「A robot sacrificed himself to save his friend.{p}\ \ Didn't you think that was touching? 」"
        
        show cu 004 with dis
        
        cu "「Well this kinda story, it feels kinda cliched.{p}\ \ There's a whole buncha them.{p}\ \ DoXXeXXn's BuXXX-chan's a famous one, right? 」"
        sg "「... 」"
        sg "「I don't know. I'm going back. 」"
    
        hide sg with dis
        show cu 006 at hit_left
        
        cu "「Aah, please wait a li'l. 」"
        
        scene old_house1 with sdis
        pause 1 
        
        $ persistent.backtrack_name = "tatsuki28"
        play music awkward
        call screen backtrack
    
    ####################################################
    label tatsuki28_dumbass:
            
        $ event_name = "YOU DUMBASS!"

        stop music
        
        fn "「Tatsu-nii, you dumbass!{p}\ \ I don't want to hear you say that! 」"
        fn "「How long are you going to drag your failure out?\n\ \ you're a disgrace as a man! 」"
    
        show ta 006 with dis
        
        play music free10 fadein 1
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        
        ta "「[fn]... 」"
        fn "「The ability to face others with enthusiasm,\n\ \ the depth of a carpenter, the pride in hard work,\n\ \ how to treat people with duty and kindness. 」"
        fn "「To uphold a childhood promise,\n\ \ the strength to accomplish it,\n\ \ no matter how many years it would take. 」"
        fn "「All of that, ALL of it, was taught to me by you.{p}\ \ You taught me so much. 」"
        fn "「When you fall, you get right back up. 」"
        fn "「No matter how many times you mess up,\n\ \ the one who taught me to never give up\n\ \ was you, Tatsu-nii. 」"
        fn "「That's the Tatsu-nii I fell in love with. 」"
        fn "「I don't want to see a Tatsu-nii\n\ \ moping around like this. 」"
        fn "「Isn't it all right to keep on going and\n\ \ never give up no matter how many failures you have? 」"
        fn "「It doesn't matter how long it takes. 」"
        fn "「Why don't you get that?\n\ \ You're not saying everything until\n\ \ now was a lie, are you? 」"
        fn "「So the plane falls, then you fall into despair. 」"
        fn "「That's not how Japan's best is supposed to be. 」"
        fn "「How can you not believe in yourself?{p}\ \ You idiot. 」"
        fn "「Stupid.{w=.2} Stupid STUPID.{w=.2}\n\ \ So stupid.{w=.2} You really are a\n\ \ gigantic moron. 」"
        "..."
        
        stop music fadeout 2
        show ta 008 with dis
        
        ta "「Well, that worked... Your words, I mean. 」"
        fn "「... 」"
        
        show ta 002 with dis
        
        ta "「Man, you can be so mean.{p}\ \ I'm facing such an overwhelming guy. 」"
        
        show ta 001 with dis
        play music free31
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        
        ta "「Gahaha! But thanks to you, I've opened my eyes. 」"
        
        show ta 004 with dis
        
        ta "「I won't give up a second time. 」"
        ta "「I swear it, I won't give up ever again. 」"
        ta "「Not on becoming the best in Japan,\n\ \ nor to fly in the sky. 」"
        fn "「Tatsu-nii- 」"
        
        show ta 002 with dis
        
        ta "「Thanks. I really was being an idiot there. 」"
        fn "「Yep, totally. A beautifully gigantic moron. 」"
        
        show ta 001 with dis
        
        ta "「All right then, first off is this table. 」"
        ta "「What's wrong with it...{p}\ \ Well, in any case I'll start over\n\ \ from the beginning, and take it slowly. 」"
        fn "「Yeah. Let's not rush it. 」"
        
        show ta 008 with dis
        
        ta "「Did I miss something...?\n\ \ What would I do if I was making\n\ \ one from scratch? 」"
        ta "「[fn], do you have anything to\n\ \ write with? 」"
        fn "「Oh, here. 」"
    
        show ta 001 with dis
        
        "It's like the Tatsu-nii from the time\nwe worked on the plane came back."
        "His eyes are shining again.\nThis feels a bit like a dream."
        
        show ta 003 with dis
        
        ta "「...Oh, I see.{p}\ \ {nw}"
        show ta 008 with dis
        extend "I've been careless.\n\ \ How could I have missed something so simple? 」"
        
        show ta 001 with dis
        
        ta "「This was never possible to begin with. 」"
        fn "「Did you get something? 」"
        
        show ta 002 with dis
        
        ta "「Yeah, it's well put together.\n\ \ It feels old if you touch the underside,\n\ \ but if you keep touching it, it feels glassy. 」"
        ta "「A skilled craftsman wouldn't\n\ \ make something like this. 」"
        ta "「In that case, what would a craftsman make? 」"
        ta "「He might make it for fun,\n\ \ but here and there there's some good work on it. 」"
        
        show ta 001 with dis
        
        ta "「I think it's made from Japanese cypress.{p}\ \ One of the best kinds of lumber. 」"
        
        show ta 008 with dis
        
        ta "「Easy to cut, and strong against water.{p}\ \ On top of that, it lasts for about a thousand years. 」"
        ta "「Pine and cedar last for about\n\ \ six hundred years, by comparison. 」"
        fn "「I see then. But six hundred years is still amazing. 」"
        
        show ta 006 with dis
        
        ta "「That's why you'd use the wrong timber for convenience.{p}\ \ This is done in Japanese cedar. 」"
        fn "「What are you doing? 」"
        
        show ta 008 with dis
        
        ta "「I don't know that much,\n\ \ but cedar should also be easy\n\ \ to cut and easy to handle. 」"
        ta "「It was made with cedar, but fixed with cypress.{p}\ \ I hate that kind of tree. 」"
        fn "「You hate it? 」"
        
        show ta 001 with dis
        
        ta "「Yeah, trees are alive. 」"
        ta "「The humidity and moisture are\n\ \ flexible, and they also warp\n\ \ when dry. 」"
        ta "「Craftsmen who go against the\n\ \ trees' feelings can't work like that. 」"
        ta "「It's not as simple as glueing it together. 」"
        ta "「But, we don't use that. 」"
        ta "「Well, we do use those things occasionally,\n\ \ but really we only use lumber. 」"
        
        show ta 009 with dis
        
        ta "「That's why we make our buildings\n\ \ to last for at least a thousand years.{p}\ \ That's the work of a craftsman. 」"
        
        show ta 008 with dis
        
        ta "「Seeing the trees, listening to their voices,\n\ \ and thinking about their feelings. 」"
        
        show ta 005 with dis
        
        ta "「Seeing the trees...{p}\ \ I forgot something so obvious. 」"
        fn "「You'll be fine, now that you've remembered. 」"
        fn "「The stuff you taught me is easy to forget,\n\ \ but it's always possible to remember them. 」"
        
        show ta 006 with dis
        
        ta "「I've been ignoring the voice of the table.{p}\ \ Even though it's been signaling 'no, that's\n\ \ not it,' it's my fault for sulking so much. 」"
        
        show ta 005 with dis
        
        ta "「It's the same with the plane.\n\ \ I put in the latest parts for the most horsepower,\n\ \ and switched the fuselage out for lighter materials. 」"
        ta "「I thought it didn't matter what I put in. 」"
        ta "「But it's old, so it isn't a very efficient design.{p}\ \ That means that the engine basically destroyed itself,\n\ \ trying to propel the plane. 」"
        
        show ta 001 with dis
        
        ta "「I was wrong, I ignored the voice\n\ \ saying 'I don't want this'... 」"
        ta "「When fixing old buildings,\n\ \ there usually aren't many blueprints still around. 」"
        
        show ta 002 with dis
        
        ta "「That's why we have to disassemble it first ? to get a\n\ \ feel for how it was built. 」"
        ta "「If we do that, we can hear all sorts of voices. 」"
        
        show ta 008 with dis
        
        ta "「The reason the structure was built, how old the\n\ \ lumber is, when it was built, and what\n\ \ the climate and environment was like. 」"
        ta "「There aren't any illustrations for the plane,\neither, so we have to listen closely while we\n\ \ work, instead of forcing my own ideas onto it. 」{nw}"
        show ta 001 with dis
        extend ""
        
        ta "「You have to carefully understand,{nw}"
        show ta 002 at jump_up
        extend "{w=.2}\n\ \ listening to the what, why, and how of things.{p}\ \ That way you can't say you don't know how to do it. 」"
        ta "「Geez, it's gotten so busy...{p}\ \ Come on, let's go. 」"
        fn "「Huh, where? 」"
        
        show ta 008 with dis
        
        ta "「Isn't it obvious?\n\ \ The table's fixed, so we gotta return it to Uncle. 」"
        
        show ta 001 with dis
        
        ta "「And then we'll go take a look at the plane.{p}\ \ We don't have time to waste. 」"
        fn "「That was fast.{p}\ \ You already fixed it? 」"
        
        show ta 002 with dis
        
        ta "「Of course I did. This much is nothing. 」"
        fn "「Even though you spent two days on it...? 」"
        
        play sound bosu29
        show ta 009 big at center_big with explosion
        
        ta "「What was that?{p}\ \ You say something? 」"
        fn "「Ahahahaha! Stop, don't tickle meee! 」"
        
        show ta 007 big with dis
        
        ta "「Huh? Stop, you say?\n\ \ {nw}"
        show ta 002 big with dis
        extend "How about I go lower? 」"
        
        play sound puu75
        
        fn "「No, already! We can't do that in the\n\ \ middle of broad daylight. 」"
        
        show ta 007 big with dis
        
        ta "「W-well... Let's do it tonight then, after so long... 」"
        ta "「You're feeling full, right?\n\ \ Shoot it all in me.{p}\ \ Or else I'll be the one topping you. 」"
        fn "「Yeah... Let's do it.{p}\ \ I'll do my best! 」"
    
        hide ta
        show ta 302 at center 
        with dis
        
        ta "「Gahaha! We should hurry to\n\ \ Uncle's place, then. 」"
    
        hide ta with wipe_right
        
        "Seems like he's made a complete revival.{p}I'm so glad I can see Tatsu-nii's smile again."
        
        stop music fadeout 3
        
        "And it looks like tonight will be fun too..."
        
        scene tatsuki_bedroom with dis
        scene black with sdis  
  
        $ event_name = "To Shigure's House"

        scene old_house1 with sdis
        play music free02
    
        show ta 002 at center with dis
        
        ta "「Uncle, we brought it back! 」{w} {nw}"        
        show ta at move_midright(0.5)
        extend "{w=.5}{nw}"
        show sg 001 at midleft with dis
        
        sg "「I thought I told you?{p}\ \ You need to be more gentle with that gate. 」"
        ta "「Uncle, you got no complaints about this, do you? 」"
        
        play sound step06
        pause .5
        show sg 002 with dis
        
        sg "「Hum. You've had it longer than I expected,\n\ \ but it looks perfectly fine. 」"
        
        show sg 001 with dis
        
        sg "「The thing itself has been used for\n\ \ a hundred years, and then one day,\n\ \ it gets knocked over, and breaks. 」"
        
        show ta 003 with dis
        
        ta "「It can't be, the guy who knocked it over is... 」"
        sg "「Mm well there is that guy, but the\n\ \ first one to handle this would be\n\ \ the one who made it. 」"
        
        show sg 002 with dis
        
        sg "「Your grandfather was first. 」"
        sg "「Immediately after its completion,\n\ \ he'd knock it over if he liked it. 」"
        
        show ta 006 with dis
        
        ta "「Then Granpa Teppei... 」"
        fn "「Is it that badly made? 」"
        sg "「No, it seems to have been knocked\n\ \ over for some reason or other. 」"
        sg "「When he'd be especially proud,\n\ \ he would also knock his rice bowl and\n\ \ chopsticks into the air too. 」"
        
        show ta 008 with dis
        
        ta "「If anyone would do that, it'd be Grandpa Teppei... 」"
        "Someone who's even more\nawe-inspiring than Tappei-san..."
        
        show sg 001 with dis
        
        sg "「Whenever your grandfather was worried about something,\n\ \ he'd make this, and other tables like it,\n\ \ or so it seems. 」"
        sg "「In leaving this to you.\n\ \ The Master probably wanted to\n\ \ cheer you up in his own way. 」"
        
        show ta 003 with dis
        
        ta "「No way, then Pa... 」"
        
        show sg 002 with dis
        
        sg "「Hohohoh! I don't know about that\n\ \ much. 」"
        
        show ta 007 with dis
        
        ta "「Well then, no one's gonna do anything,\n\ \ but say thanks to that guy for me. 」"
        sg "「All right. I'll keep that mind. 」"
        
        show ta 002 with dis
        
        ta "「All right, [fn], let's go. 」"
        fn "「Yeah 」"
        ta "「Later Uncle. You take it easy now. 」"
        
        show sg 001 with dis
        
        sg "「Wait, are you going to the plane's\n\ \ crash site after that? 」"
        
        show ta 001 with dis
        
        ta "「Uncle, how do you know about that? 」"
        sg "「No one was watching, but that's\n\ \ near my plot of land. 」"
        sg "「The plane was mine in the beginning, anyway. 」"
        sg "「You coming to return the table today\n\ \ is great timing, it's about the right\n\ \ time, so head to the airfield. 」"
        
        show ta 008 with dis
        
        ta "「What's going on? 」"
        
        show sg 002 with dis
        
        sg "「Just head over there. 」"
        ta "「All right, I get it.{p}\ \ {nw}"
        show ta 001 with dis
        extend "We'll go there now. 」"
        sg "「Yes, yes, that's a good boy. 」"
        
        show ta 002 with dis
        
        ta "「Later Uncle. 」"
        fn "「Sorry to hold you up! 」"
        sg "「Hohohoh! Be careful now.{p}\ \ Make sure you don't run intoany trouble. 」"
        
        stop music fadeout 1.5
        scene black with sdis

        $ event_name = "The Midoriya Family"

        play music daily03

        scene prairie with sdis
        show ta 008 at center with dis
        
        ta "「What's over here at this hour? 」"
        fn "「Who's that...? Someone's here. 」"
    
        show tp 401 at farright with dis
        
        tp "「You're here rather late.{p}\ \ I was getting worried that you wouldn't\n\ \ get here before [fn] had to leave. 」"
        
        show cu 002 at farleft with dis
        
        cu "「But, it's great that we managed to\n\ \ finish the work here before ya guys got here. 」"
        
        show ta 006 with dis
        
        ta "「Why are you here, Pa?\n\ \ And the rest of you, for that matter... 」"
    
        hide tp with wipe_right
        show ni 005 at farright with wipeleft
        
        ni "「You are so slow, just like always. 」"
        fn "「Tatsu-nii, look at that. 」"
        
        show ta 003 with dis
        
        ta "「That's... It should still be in the forest.{p}\ \ Why's it here? 」"
        "Looking out inside the old air shelter\nwas a red fuselage."
        "It's hard to make out from far away,\nbut it's unmistakeable."
        "It's definitely the plane we spent\nthe Summer working on."
        
        show cu 007 with dis
        
        cu "「(With sumthin' that red,\n\ \ it's like it was made for Char...) 」"
        
        show cu 002 with dis
        
        cu "「(*snicker snicker* Young Master's no\n\ \ Char, but Aniki might be.) 」"
        
        show cu 005 with dis
        
        cu "「(So that means Young Master would be Amuro.) 」"
        
        show cu 008 with dis
        
        cu "「(The truck would be White Base,\n\ \ so if there's the White Devil...) 」"
        
        show cu 002 with dis
        
        cu "「(Psh, a masterpiece!) 」"
        
        hide ni with dis
        show tp 403 at farright with dis
        
        tp "「Why are you smiling by yourself? 」"
        
        play sound hit_p07
        show cu 009 at hit_right
        $ chuu_beat += 1
        pause .3
        hide cu with wipe_down
        show prairie at vshake
        
        cu " {size=+15}「Dom-!! 」"
        "..."
        
        show tp 401 with dis
        
        tp "「For something like this,\n\ \ it's no problem for us to take down and transport. 」"
        
        show te 001 at farleft with wipe_right
        
        te "「Truthfully, this was a secret operation,\n\ \ and somehow we managed to bring it here today. 」"
        
        show ta 008 with dis
        
        tp "「God, you're an annoying little brat.{p}\ \ A terrible son who brings so much grief,\n\ \ and a total good-for-nothing. 」"
        
        show ta 007 with dis
        
        ta "「Pa...{p}\ \ thanks for everything. 」"
        
        show tp 402 with dis
        
        tp "「Huh? Don't misunderstand.{p}\ \ It's just a loan.{p}\ \ I'm taking it out of your salary, you know. 」"
        
        show ta 006 with dis
        
        ta "「That's practically the same as me paying for it... 」"
        
        show tp 403 with dis
        
        tp "「Be happy when you're given something!! 」"
    
        show tp 401 with dis
        
        tp "「Anyway, this is all we're doing for you.{p}\ \ After this, you gotta finish yourself. 」"
        tp "「Hey, we're heading back.{p}\ \ We had to do some stupid stuff, and now we're behind. 」"
        
        play sound step13b
        hide tp with dis
        hide te with dis
        show ta 007 with dis
        
        ta "「Hehe. Oh Pa... 」"
        fn "「Let's go. The plane's been brought\n\ \ back, so we have to hurry. 」"
        
        show ta 002 with dis
        
        ta "「Right. Let's do it. 」"
        fn "「It's covered in scratches, but nothing\n\ \ that really stands out. 」"
        fn "「It must've been protected by the trees\n\ \ like you were, Tatsu-nii. 」"
        ta "「If it's like this, then we can do something about it.{p}\ \ It's a miracle it wasn't smashed to bits. 」"
        fn "「Then it can still move.{p}\ \ We'll make it fly. 」"
        
        show ta 001 with dis
        
        ta "「Last time we added on too many useless things. 」"
        ta "「The balance was thrown off,\n\ \ and it was all too heavy. 」"
        ta "「That's why this time I think we should\n\ \ strengthen the original parts. 」"
        ta "「I'll take off the extras as best as I can,\n\ \ and lighten up the fuselage by making it out of wood. 」"
        
        show ta 002 with dis
        
        ta "「I'll bring this back to life with\n\ \ my knowledge and technique. 」"
        ta "「I'll also try to make it as close to\n\ \ it's original state as I can. 」"
        ta "「It's a stunt that no one but a craftsman can try. 」{w} {nw}"        
        show ta at move_midright(0.5)
        extend "{w=.5}{nw}"
        show ni 001 at midleft with dis
        
        ni "「In that case, this project is something to\n\ \ be approached with care.{p}\ \ A small change may have large effects. 」"
        
        show ta 003 with dis
        
        ta "「...Why are you here? 」"
        
        show ni 005 with dis
        
        ni "「'Why?' You'll need help don't you? 」"
        
        show ni 003 with dis
        
        ni "「Besides, you two working on an airplane by\n\ \ yourselves won't be good for my mental state.{p}\ \ I'll help however you want. 」"
        
        show ta 004 with dis
        
        ta "「Nikaidou! Asshole, don't touch it as you please! 」"
        fn "「Hahaha! 」"
        "Those two really get along..."
        "From friends to family, even lovers, we'll\nalways be tied together by our bonds."
        
        show ni 001 with dis
        
        ni "「I'm jealous of you. 」"
        ni "「You have a nice background and friends,\n\ \ along with a wonderful family, and you\n\ \ head straight for your dreams. 」"
        
        show ni 004 with dis
        
        ni "「Father never recognized me...{p}\ \ He never even looked at me. 」"
        
        show ta 008
        show ni 005
        with dis
        
        ni "「Despite the boss being violent,\n\ \ he'll face off against anything.{p}\ \ You'll also face off against anything. 」"
        
        show ni 001 with dis
        
        ni "「I myself have nothing. 」"
        ni "「If I were to build a building,\n\ \ I want it to be a warm and peaceful place. 」"
        
        show ni 005 with dis
        
        ni "「However, the things Father requested,\n\ \ they were all produced with a cold feel to them. 」"
        ni "「I've wondered why the things the boss made\n\ \ felt so warm, and I started to understand when\n\ \ working under him. 」"
        
        show ni 003 with dis
        
        ni "「This work doesn't use the flow of time\n\ \ or common knowledge, but the makers'\n\ \ feelings are so warm. 」"
        ni "「You're an enviable one. 」"
        ni "「I have nothing, and you have much.{p}\ \ That's why all your moping about worried me. 」"
        
        show ni 001 with dis
        
        ni "「Looking at you irritates me. 」"
        ni "「Even though you're in an environment\n\ \ rich in skill, your conduct and methods\n\ \ are quite clumsy. 」"
        ni "「The boss told you, it's okay if\n\ \ craftsmen lack ability. 」"
        ni "「If you don't have that and don't run,\n\ \ you can overcome anything.{p}\ \ Just don't be reckless, like he said. 」"
        ni "「That surely applies to someone like you. 」"
        
        show ta 001 with dis
        
        ta "「I don't really get it, but don't talk\n\ \ like that about your parents. 」"
        ta "「If you can't get your parents to recognize you,\n\ \ you won't be able to face off against anything. 」"
        
        show ta 009 with dis
        
        ta "「Besides, have some more pride in yourself.{p}\ \ You're a capable guy, you'll be crushed\n\ \ if you think you're no good. 」"
        
        show ta 008 with dis
        
        ta "「Someone important drilled that into me. 」"
        ta "「Besides, a home isn't made by a house.{p}\ \ If you want\n\ \ to make a house with warmth, then move out. 」"
        
        show ni 003 with dis
        
        ni "「...of course I know that. 」"
        
        show ta 002 with dis
        
        ta "「One more thing. I've been thinking\n\ \ about it, and the only clumsy guy\n\ \ here is you. 」"
        
        show ta 001 with dis
        
        ta "「You suck so bad that you're constantly\n\ \ making people angry, so stop arguing about every\n\ \ little thing and just leap blindly some more. 」"
        
        show ni 005 with dis
        
        ni "「Shut up. Seems like I've talked a bit too much. 」"
        
        show ta 002 with dis
        
        ta "「Since you're gonna help, I'm working you hard. 」"
        
        show ni 003 with dis
        
        ni "「Hmph. It's okay to brag,\n\ \ but don't mess up this time. 」"
        
        show ta 004 with dis
        
        ta "「What was that!? 」"
        fn "「Hmm, it really does suit the two\n\ \ of you when you guys fight. 」"
    
        show ta at jump_up
        
        ta "「Hey, you made fun of me! 」"
        
        show ni 005 with dis
        
        ni "「This isn't a show. 」"
        
        hide ni with wipeleft
        show cu 008 at center with wipe_right
        
        cu "「I'm always an outcast,\n\ \ but please include me from time to time... 」"
        fn "「Thanks. You came to help too, Chuukichi-kun? 」"
        
        scene prairie
        show ni 001 at farleft
        show ta 004 at farright
        show cu 008 at center 
        with wipe_right
        
        ni "「All right, let's start our all-night\n\ \ project at once.{p}\ \ We don't have much time, after all. 」"
        
        show ta 006 with dis
        
        ta "「Whaaat, but tonight... 」"
        
        show ni 005 with dis
        
        ni "「Do you have some task more\n\ \ important than this? 」"
        ta "「Well, it's important, but I can't\n\ \ say it's *that* important... 」"
        
        show ni 004 with dis
        
        ni "「Spit it out.{p}\ \ If you can't say what it is,\n\ \ it's not necessary. 」"
        
        show ta 005 with dis
        
        ta "「And I was looking forward to it too. 」"
        "Me too..."
        
        show ni 003 with dis
        
        ni "「Now let's do this. If we don't get\n\ \ moving, it won't get done no matter\n\ \ how long we take. 」"
        
        show ta 008 with dis
        
        ta "「How are you the most eager person here? 」"
        
        show cu 002 with dis
        
        cu "「I know, right? 」"
        
        show ni 004 with dis
        
        ni "「Why are you dragging your feet?\n\ \ Aren't you up for it?\n\ \ There's no time to waste! 」"
    
        show ta 002 with dis
        "「Okaaay. 」"
        
        jump end28
    
########################################################
label shun28:
    
    $ event_name = "Falling Into Nothing"

    stop music fadeout 1.5    
    scene black with wipe_dr  
    scene prairie with dis    
    play music daily01
    $ renpy.music.set_volume(1.0, 0.0, channel = "music")
    show su 001 at offright_far
    
    "I've noticed that summer in Minasato\nis more relaxing than in the city,{w=.2}\nthere's no dirty air and noise."
    "The unpleasant sensation of heat\nis connected with other negative factors\nand turns worse like a spiral."
    "The steam bath-like humidity and the noise\nthroughout the whole city put me into a lifestyle\nwhere I didn't want to leave my computer."
    "From that perspective, it's easier\nto put up with the heat in this village."
    "A pastoral landscape is spread out before me.{p}I can hear the smooth sounds of wind and water."

    show su at move_center(1)
    
    su "「[fn]-saaaan. 」"
    "And coming towards me is the childhood friend\nI've reunited with after 5 years."
    "He has soft, light brown fur\nand a cute tail attached to him."
    "His midsummer hugging attack brings me what I'd\nlike to think is the pleasure of ecstasy that's far\nfrom unpleasant,{w=.2} and moderately steams my brain."
    
    show su 002 with dis
    
    "Now, come and dive into my chest!"
    
    show su 016 with dis
    
    su "「Wah. 」"
    
    show su 003 with dis
    
    su "「H-hanya. 」"
    
    stop music fadeout 1
    pause 1
    play music free0205
    $ renpy.music.set_volume(0.8, 0.0, channel = "music")
    
    "!?{p}Did the Earth become obsessed with Shun-kun's charm?{p}It entangled his leg to draw him closer to itself."
    "In short, he is about to fall on an empty spot."
    "At this moment the only one\nwho can protect Shun-kun is me!"
    
    play sound metalhit001
    "{size=+25}Let me explain!"    
    "When [fn] [ln] thinks about the beastman he loves,\nhe sees the {cps=20}surrounding area {cps=10}in slow motion{cps=5},\n{cps=40}and his brain {nw}"
    play sound don20 
    extend "turns at unimaginable speeds!"    
    "Immediately, I pick up on the\nappropriate options for this situation."
    "Option 1.{p}I catch him in my arms."
    "A somewhat clever-handed technique is required,\nbut it's the most picturesque."
    "Option 2.{p}I become a cushion."
    "If I slip between him and the ground and become\nshock-buffering material, I'll be able to reduce\nthe amount of pain Shun-kun feels."
    "It's easier than the 1st,\nbut it involves the risk of dirty clothes."
    "Option 3.{p}Hope that Shun-kun's tail is strong."
    "In other words,{w=.2}\nsit on the sidelines and \"do nothing\"."
    "Now, what should I do?"
    
    menu:
        "A. Catch him in my arms.":
            jump shun28_catch
        "B. Become a cushion.":
            jump shun28_cushion
        "C. Hope that Shun-kun's tail is strong":
            jump shun28_tail
    

    ####################################################
    label shun28_catch:
            
        $ event_name = "Trying to Carry Him Under My Arm"
        
        stop music fadeout 1
        pause 1
        play music battle01
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        
        "Catching my falling partner, that is to say,\nquickly reacting to the situation, is going\nto require a considerable amount of dexterity."
        "I ascertain the moment when his body loses\nit's center of gravity to a hair's breadth.\nI must hold out my arms and become his support."
        "And I will not be against common courtesy.{p}It's important that I choose an area\nhe won't mind being touched."
        "Once his weight has bent over my arms,\nI'll soften his momentum, and support him\nto reduce the impact if possible."
        "Then I'll lovingly settle my companion\nin my arms without delay,"
        "lift him up (in a way\ncommonly called a \"princess carry\"),\nand transport him to somewhere safe."
        "I'll gently lower his body, kneel, say\n{w=.2}{cps=10}「I'm glad you're not hurt 」,{cps=40}{w=.2} and show my\nloyalty with a kiss to the back of his hand."
        "Yep, that's perfect. I'm not given any time\nat all to do the aforementioned simulation,\nand awkwardly stretch out my arms."
        
        stop music fadeout 1
        pause 1
        hide su with wipe_down_slow    
        play sound puu79_a
        
        "Clunk."
        "I miscalculate the distance and our heads collide."
    
        scene black with circle_out
        
        jump shun28_recover
        
    ######################################################
    label shun28_cushion:
        
        $ event_name = "Cushion Experience"
        
        "Zuzaaa.{p}In the blink of an eye,\nI slide underneath Shun-kun."
        "As I expected, hanging his tail down when he loses\nhis balance doesn't break his fall.{w} That's okay,\nit seems he won't crash into the ground."
    
        hide su with wipe_down_slow
        
        "The next moment.{w=.2}{nw}"
        play sound bosu35
        extend "{p}My body which isn't particularly strong\ncatches the wolf whose weight,"
        "relative to the rest of this village,\nwould go into the light category."
        "My consciousness is knocked away by the pain.{p}Guh, {w=.2}I don't hear his elbow...{cps=10}\nthrusting into...{cps=5} me..."
        
        stop music fadeout 1
        pause 1
        scene black with wipe_up_slow
        scene sky with sdis    
        play music free04 fadein 1
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        
        fn "「Nn, mmmm... 」"
    
        show su 004 at center with wipe_up_slow
        pause .2
        
        su "「[fn]-san,{w=.2} [fn]-san. 」"
        "With the blue sky as a background,\nShun-kun's face is looking into mine.{p}I see a few tears."
        "Aah, I must take to task the guy who made him cry."
        
        show su 003 at briefzoom
        pause .2
        
        su "「[fn]-san, are you okay? 」"
        "Of course I am.{p}Actually, who was the guy\nwho did mean things to Shun-kun?"
        su "「I didn't hurt you, did I?{w=.2}\n\ \ I'm sorry, it's my fault. 」"
        "Now that he mentions it,\nthere is a dull pain remaining on my body.{p}Did I get hit somewhere?"
        
        show su 016 with dis
        
        su "「[fn]-san, if you can hear me,{p}\ \ please say something. 」"
        fn "「Huuh? 」"
        
        show su 003 with dis
        
        su "「! 」"
        fn "「Shun-kun? Why are you crying? 」"
        
        show su at shivering
        pause .2
        
        su "「Hic, even though you weren't moving,{p}\ \ you opened your eyes. 」"
        "Aaah."
        "I remember.{w} I got hit with Shun-kun's falling attack,{p}laid down on the poor ground,{p}and it seems I lost consciousness."
        "Then I opened my eyes wide to Shun-kun's voice,{p}and it doesn't look like I'm able to move."
        
        show su 010 at still with dis
        
        su "「I'm really glad, [fn]-san.{p}\ \ I wanted to call for somebody,\n\ \ but I couldn't leave you. 」"
        su "「I'm glad it didn't take you too long to wake up... 」"
        fn "「S-sorry, Shun-kun. It hurts, though. 」"
        
        show su 003 with dis
        
        su "「!{p}\ \ [fn]-saaan. 」"
        "My body creaks.{p}It does that a lot when I lean forward."
        fn "「Don't worry, it's not that bad.{p}\ \ Ah. 」"
        "I manage to stand up.{w} When I see the place\nwhere it hurts for the first time, I notice\nthat my shirt and pants are covered with dirt."
        fn "「I'm going home for today.{p}\ \ Sorry, even though I was going to play with you. 」"
        
        show su 004 with dis
        
        su "「No, don't worry about it.{p}\ \ I shouldn't have been running around like that. 」"
        "No, no.{p}It's a quality of Shun-kun to jump\nwithout thinking of anybody else."
        "「Anybody else 」 being the appropriate place to fix,{p}I want that to just me be."
        
        show su 005 with dis
        
        su "「I'll take you home. 」"
        "Taking me home seems like a brave thing to do.{p}That's because I want him to give a good explanation\nto my grandparents about why my clothes are dirty."
    
        show su at move_offleft_far(1)
        
        "And so my gentlemanly escort and I\nwalk down the road to my house."
        
        stop music fadeout 1
        pause 1

        jump end28
        
    #####################################################
    label shun28_tail:
        
        $ event_name = "Overcome it with Tail Power"
        
        "He wags his tail energetically when he's happy,\nand droops it down when he's sad."
        "If he uses it for his center of gravity,\nhe'll be able to regain his balance when he falls!"
        "I watch him with hope and confidence,\njust like a commanding officer."
        "He's still going..."
    
        hide su with wipe_down_slow
        stop music fadeout 1
        pause 1
        play sound pyoro45_a
        
        su "「Po-pe. 」"
        "He was drawn to the ground."
        fn "「A-are you alright?{w=.2} Shun-kun? 」"
        su "「Howaaaan... 」"
        
        scene black with sdis
        
    ##########################################################
    label shun28_recover:
        
        $ event_name = "Nursing Under the Shade of a Tree"
        
        play music free0258 fadein 1
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        scene prairie with sdis
        
        su "「Nn, uuuunn... 」"
        fn "「Are you okay?{w=.2} Shun-kun. 」"
    
        show su 015 at center with wipe_up_slow
        
        su "「[fn]-san?{w=.2} Huh, I- 」"
        fn "「You fainted earlier. 」"
        
        show su 003 with dis
        
        su "「I-{w=.2}I'm sorry. I'm feeling a little dizzy. 」"
        
        show su 004 with dis
        
        su "「I couldn't eat that much for breakfast. 」"
        fn "「You didn't have an appetite? 」"
        
        show su 001 with dis
        
        su "「Yes, I didn't ask for much. 」"
        fn "「Really?{p}\ \ Why did you go outside even though you\n\ \ should have been taking it easy at home? 」"
        "I ask him in a soft tone\nwhile gently stroking his head."
        
        show su 002 with dis
        
        su "「Because the weather is nice,\n\ \ the wind feels good, and, 」"
        "Then, he smiles while looking at my face."
        
        show su tailwag 01 with dis
        
        su "「because I felt like seeing you.{p}\ \ That's why I came out 」"
        "Th-this is awkward.{p}That honest, brand-new feeling\nof his is embarrassing for me."
        fn "「I-I see, thank you.{p}\ \ I'm happy I got to see you too.{p}\ \ But you should be at home when you don't feel good. 」"
        "Feeling embarrassed,\nI can't look at this transparent eyes,\nand tell him while looking away."
        
        show su 010 with dis
        
        su "「Kyuun. 」"
        fn "「Can you stand? 」"
        su "「Y-yeah, I think I'm okay... Hwaah. 」"
        
        show su 010 big at center_big with dis
        
        "Thump.{p}He isn't able to stand on his unsteady legs\nand leans his body on me."
        fn "「Let's rest here for a bit.{p}I want to feel the wind for a while. 」"
        
        show su 001 big with dis
        
        su "「Okay. 」"
        "Both of us sit side-by-side under the tree's shade."
        "While listening to the gentle sound\nof the wind through the grass,\nwe enjoy the cool breeze for a little while."
        
        stop music fadeout 1

        jump end28
    
########################################################
label kouya28:
    
    $ event_name = "Noisy Atmosphere"

    scene concert with wipe_right
    play music shop02
    
    "An overwhelming heat.{p}It filled the air, and wrapped up the room."
    "It's a bit different from direct enthusiasm."
    "It's more like the tension and expectations\nbefore a big show, mixed with a bunch\nof other emotions to make something complex."
    "At least, that's what I think."
    "In a certain neighborhood here in Kazenari,{w=.2}\na certain hall was set as the stage\nfor Kouya and the others."
    "We'd already registered, and now we were waiting\nfor our turn on the stage."
    "This contest is held only once a year,\nand in the neighboring cities it's fairly big."
    "It's organized by big-name label companies,\nand since it's used as a means for scouting out\ntalent,{w=.2} it's a pretty serious event."
    "Applications were all picked out by several\norganizations, and it'll all be decided\nby live concerts here."
    "It seems that they'll have everyone perform\ntheir songs, evaluate them, and pick the best two."
    "Basically, every group that's come here\nhas already passed the initial evaluation."
    "When I thought that, my palms started sweating,\neven though I'm not going on stage."
    "Once I heard the muffled stirring\nfrom the hall itself, I went into overdrive."
    "If you could get somewhere here,\nyou'd be on the way to your debut.{p}It's a total do-or-die situation."
    
    show ka 001 at center with dis
    
    ka "「Man, it's packed.{p}\ \ There are even more people here than usual. 」"
    fn "「Yeah, it's amazing.{p}\ \ Still, I can't understand why I'm so nervous. 」"
    ka "「It's understandable since it's your first.{p}\ \ I was bad with this too, when I first started. 」"
    fn "「Wow, that's surprising.{p}\ \ I thought you'd never feel like that. 」"
    
    show ka 003 with dis
    
    ka "「Everyone feels this, at first.{p}\ \ But since I'm thinking I can do this,\n\ \ it becomes fun instead. 」"
    ka "「When you get used to it,\n\ \ being on stage feels really great.{p}\ \ It's a kind of thing you don't feel anywhere else. 」"
    fn "「I guess that's true,{w=.2}\n\ \ and I think I get what you mean. 」"
    "Kouya's expression looked happy as he talked,\nwhich got the idea over well enough."
    "It's just that I won't be standing on the stage.\nSince I'm here as the band's manager,\nthis is one of the perks."
    "Before their turn comes up, I'll have to take a seat."
    "I don't know what kind of world Kouya's talking\nabout.{w=.2} I can't know. I can only guess how it feels\nlike in my mind.{w} It's a little sad."
    
    show ka 001 with dis
    
    ka "「Don't worry,{w=.2} I'll give you a taste of what it\n\ \ feels like with a high-energy performance.{p}\ \ Look forward to it. 」"
    fn "「Okay,{w=.2} I'm counting on you. 」"
    ka "「Yeah,{w=.2} leave it to me. 」"

    hide ka with wipe_right
    
    "Our talk ended there."
    "I covered up my silence by looking at the clock.{p}The time was drawing close."
    "They'll be performing soon.{w} I have to get going.{p}I turned to face everyone and spoke up."

    show ka 001 at midleft
    show ke 001 at midright
    show yu 001 at farleft
    show jn 001 at farright
    with dis
    
    fn "「...It's almost time.{p}\ \ I'll be out there, watching you guys. 」"

    show ke 004 with dis
    
    ke "「Oh,{w=.2} already? 」"
    yk "「Seems like it.{w=.2}I see.{w} {nw}"
    show yu 002 with dis
    extend " Well, see you later then, [fn]-kun.\n\ \ We'll bring back good news, so keep your hopes up. 」"
    jn "「... 」"
    fn "「I'll be expecting something for real then.{p}\ \ Don't disappoint me now, mkay? 」"
    
    show ke 001 with dis
    
    ke "「You said it.{p}\ \ All right,{w=.2} leave it to us.{p}\ \ {nw}"
    show ke 006 with dis
    extend "Big Bro never lies! 」"
    
    show yu 001 with dis
    
    yk "「Yes, yes, we get it.{p}\ \ Now are you going to hold onto it until April 1st\n\ \ next year? 」"
    
    show ke 004 with dis
    
    ke "「Hmm, are you treating me like that on the very\n\ \ day of the performance?{w} But I'm the leader for now.\n\ \ Isn't there anything else to say?{w=.2} Hey, come on! 」"
    
    show yu 003 with dis
    
    yk "「Nope,{w=.2} impossible. 」"

    show ke at jump_up
    
    ke "「What!?{w} And you said that so fast! 」"
    "Thus began the usual repartee.{p}These two never change, no matter where or when.{p}It's charming to just watch them."
    "When they start arguing,{w=.2} it's like they go into\ntheir own little world.{w} But that's also the same\nas usual, with the rest of us on the sidelines."
    "As I saw that little spectacle from a bit away,\nmy good mood kept up,{w=.2}{nw}"
    show ka 002 with dis
    extend " and I saw Kouya smiling\nat the edge of my field of vision."
    "Somehow, Kouya seemed to notice,\nand looked back at me.{p}Our eyes met."

    scene concert with wipe_right
    show ka 001 at center with wipe_right
    
    fn "「...At long last, huh. 」"
    ka "「Yeah,{w=.2} definitely. 」"
    fn "「I'll be waiting for good news. 」"
    
    show ka 002 with dis
    
    ka "「I'll bring some back.{p}\ \ Just you wait. 」"
    "Kouya laughed as he gently ruffled my hair.{p}I couldn't say anything to that smile.{p}「Just believe in me, 」 it said."
    fn "「...All right,{w=.2} later then. 」"
    
    show ka 003 with dis
    
    ka "「Right. 」"

    hide ka with wipe_right
    
    "I turned around and walked out."

    scene black with wipeleft
    scene concert with wipeleft
    
    "I left the waiting area by the stage,{w=.2}\nand went over to where everyone else was\nwaiting for the show to start."
    "Now that I'm actually out here, it looks even\nmore packed than when I looked out from backstage."
    "Seems like the seats are completely sold out."
    "Naturally, I can't get close to the stage\nwith a crowd that big.{w} It's sad, but the\nonly thing I can do is watch from the back."
    "That's still fine, though."
    
    stop music fadeout 7.5
    scene concert night with sdis
    
    "I was drifting off into daydreams,{w=.2}\nwhen the lights started flicking off, one by one."
    "Finally, it's starting."
    
    play music free0456
    
    "In the complete darkness,\nsome easy-to-get-into music started playing.{p}The MC walked onstage, greeted by applause."
    "There, he started off with the typical spiel.{p}{nw}"
    play sound cheering1
    extend "Everyone started cheering in their seats."
    "This exchange was making me feel a bit impatient.{p}Maybe it's because I'm here with one of the bands,{w=.2}\nbut I couldn't sit still, and wanted things to start."
    "I started looking at the stage\nobjectively and coolly.{p}Like I was seizing it up."
    "I felt like a terrible audience member.{p}I guess it's all right, since I'm in the back."
    "Soon the MC changed places with the first group.{p}If I remember right, Kouya's group is the fifth\nof nine sets.{w} Still a while to go."
    "As I kept looking at the stage as before, my ears\npicked up the frantic, steadily increasing sounds.{p}My mind carefully separated each sound from the other."
    "Every group participating was different.{p}Some were all beastmen like Kouya's group,\nand some were all humans."
    "There were even some all-girl groups."
    "After listening to some different songs,\nI was having listening to all the variety."
    "No matter which kind of group, no matter what style\nof music,{w=.2} each and every performance resonated in my\nheart.{w} That was the one point they all had in common."
    "I honestly thought they were all pretty good.{p}They did as well as Kouya's practice from yesterday."
    "If I had to pick out the best after listening to\nthem all, I wouldn't be able to do it."
    "The poetic lyrics and the sounds of the instruments,\ncombined with the determination coming from them all,\nmoved me to the core."
    "Music really is amazing.{w} I felt that if there were\nany feelings needed to be given to someone, they'd\nbe carried on through the sounds to that person."
    "It happens a lot when I listen to a CD.{w} I'd get my\nfeelings synced up with the ones bundled up in the\nsongs, and I'd feel sadness, or I'd feel happiness."
    "In those few minutes, it felt like I was living the\nmusic.{w} Like they say in movies and novels,\nlosing is not an option."
    "You could possibly say they all transcended language.{p}After listening to the fourth song, I felt that\nsensation again."
    "The fifth one was next.{p}Finally the time has come for Kouya's-{w} 『Musikus'』\nperformance."
    "Being only halfway was enough. Everyone around had\ntheir own idea of who should be the champions.{p}It's going to be a stiff competition."
    "Still, I felt strangely calm.{w} There was an unusual\nconviction inside my heart, and that kept me cool.{p}I'm pretty sure...{w=.2}it's faith."
    "It filled me to the brim with certain thoughts.{w=.2}\nThoughts that said that if it's Kouya's group, they\ncould do it."
    "Thoughts that expressed my desire for them to win."
    "It's true that everyone else also has a shot at it.{p}However, there's no way they'll lose."
    "So many things have happened,\neven only in the few days I've been here.{p}There were people suffering, worrying."
    "There were people willing to\nshoulder that pain together."
    "That surpassed everything.{p}They really did see what they wanted to do,\nand they took it back."
    "I was around for only a little bit,{w=.2}\nbut I witnessed that alongside everyone."
    "Looking at any other group,\nI don't think they had anything like that."
    "But in all honesty, this experience became\na source of strength for them.{p}I'm sure that's the final key."
    "If there's no definitive difference in the art\nthen the decider of music's relative merits is the\nheart.{w=.2} That's what I believe."
    "I looked over at the stage attentively.{p}I told myself one more time,{w=.2} 「it'll be okay. 」"
    "At long last, the MC announced the name Musikus.{p}Everyone came out in response."
    
    stop music fadeout 7.5
    
    "I was far away, but I could see the confidence in\ntheir faces.{w} More than anything, they looked like\nthey were having fun."
    "They were shining with hope,{w=.2}\nout through their radiant smiles."
    "Yuuki-san gave a brief word as he took the mike into\nhis hand,{w=.2} and then the song started."
    
    play music free0451
    
    "It's an upbeat and catchy tune."
    "It was written about a month before I came back\nto Minasato."
    "I've heard this melody played several times during\npractice,{w=.2} but hearing it here gives off a\ndifferent sensation."
    "I can't describe it all that well,{w=.2}\nbut it reached even deeper into my chest than before."
    "It felt like I was reliving the excitement from the\ntime I decided to come back.{p}I felt my face relax."
    
    stop music fadeout 3
    
    "The performance ended with a lingering note,\n{nw}"
    play sound cheering1
    extend "and the crowd broke out into cheers."
    "It was amazing during the other groups' times,{w=.2}\nbut this one was seriously loud."
    "Yuuki-san responded to everyone's cheers\nwith his words of thanks."
    "「Thank you, I'm glad you all liked the song.{p}The next one will be our last,\nbut let's enjoy ourselves. 」"
    "The band smoothly transferred into the next song\non the program.{w} It was different to the song\nthey'd just played:{w=.2} A heart-rending ballad."
    
    play music free0352
    pause 5
    
    fn "「This song... 」"
    "I spoke without realizing."
    "I first heard this song yesterday."
    "Well, I say this based on the first few seconds.\nSince I was on my way to get drinks,{w=.2}\nI guess today is my first time hearing it properly."
    "The songs were mostly written by Yuuki-san,\nbut this one song is one I could say Kouya made."
    "The peaceful tune gave me the feeling of parting\nwith someone."
    "But within, there were some other messages\nweaved in, with an uplifting\n'let's walk together' part."
    "As I listened, my chest started hurting a little.{p}It's kind of nostalgic, but all these miserable\nfeelings were filling up inside my heart."
    "Goosebumps started rising. My eyes started feeling{p}hot for some reason. Something felt like it was {p}crawling up my spine,{w=.2} and a shudder came through."
    "My body was wrapped in chills.{p}I was completely overwhelmed. Overwhelmed by the\nintertwined lyrics, and from the thrumming notes."
    "As time passed, the song steadily grew in strength.{p}And once it reached the echoing climax,\nit gently went into the resolution."

    stop music fadeout 3
    
    "Then it was the end.{p}{nw}"
    play sound cheering1
    extend "The hall burst into applause."
    "It was even louder than after the first song,{p}and I thought space would crack for a bit.\nI clapped my hands until they hurt."
    "Kouya and the others smiled and waved as they\nwent back behind the curtains."
    "During all that racket, I slipped out of\nthe hall without knowing if anyone noticed."

    scene black with wipe_right
    
    "I went to find somewhere out of the way,\nwith no people around. Right now it doesn't\nseem like I'd be meeting anyone."
    "More accurately, I didn't want to be seen by anyone."
    "At any moment, the dam would break, and all\nmy emotions would flood out of my eyes.\nMy vision is blurred already."
    "I ran like I was escaping from something, quickly\nrushing into the restroom as I hid my eyes."
    
    play music melodious06
    
    "The song Kouya made.{p}I knew what was inside the lyrics."
    "That was...{w=.2} the state Kouya's been in,\never since I'd left Minasato."
    "「It's okay. We can meet again. 」{p}That's what his heart said, ever since we parted.{p}All of it was in there."
    "It said it was lonely to say goodbye.{p}But, it also said to keep going until our paths\ncrossed again."
    "It said it was difficult to be on the other side.{p}But, it also said that he wanted to go with me,\nno matter what."
    "「I'll show you I can definitely climb over any wall,\nso I want you to watch over me.{p}We can meet up, smiling like always. 」"
    "It shouldn't have been able to reach me,\neven though it was made for telling me that."
    "As if my trembling heart called to them,\nvarious memories from this dark world started\nflying by."
    "Things from back then, things from now.{p}Everything I remember came back like a flood."

    scene white with sdis
    
    fn "「Kouya... 」"
    
    show ka 002 at center with dis
    
    "Kouya was the only one in front of me."
    "「Where there's a will, there's a way, 」{w=.2}\nhis smiling self said."
    
    show ka 008 with dis
    
    "「I don't want to make anyone worry, 」{w=.2}\nhis crying self said."
    
    show ka 003 with dis
    
    "「I'll definitely win, 」{w=.2}\nhis determined self said."
    "I automatically called out to that form.{p}「I'll be waiting for good news. 」"
    "「I'll bring some back.{p}Just you wait. 」\nThat's what Kouya had said to me."
    "Little by little, the smiling image disappeared."

    hide ka with sdis
    
    "「...Okay, it's almost time. 」{p}That's what it felt like his fading form said."
    
    stop music fadeout 7.5
    
    "My sealed memories slowly returned to the\ndarkness, and my senses came back to reality.{p}And then I realized something."
    "I can't hear any music.{p}All I can hear is someone speaking."
    "It seems as if all the songs have finished,\nand they're now awarding the prizes."
    fn "「I'll be right there. 」"
    "This time I spoke clearly."
    
    scene black with sdis
    pause 4
    scene concert with sdis
    play music piano3_014
    
    "I didn't feel the passage of time,{w=.2}\nbut it seems I was out of it for quite a while."
    "When I got back to the hall, they were already\nstarting the awards ceremony."
    "And right now they're acknowledging which\ngroups are Grand Prix level.{w=.2} If that's the case,\nthen only the winners left to announce."
    "It's already at the most exciting part of the show."
    "Up on stage, all nine groups have been lined up."
    "There were already people acting like they've won,\nand also people who were crying.\nKouya's group is... still empty-handed."
    "This is a situation where the potential to join\nthe Grand Prix together with a harsh reality\nlie in wait.{w} Everyone was still there."
    mc "「Okay!{w} At long last, we have reached\n\ \ the announcements for the Grand Prix! 」"  
    mc "「Just who is it the honors belong to?{p}\ \ Chief Judge, your rulings please! 」"
    "Finally, he reached that part of the speech.{p}The Chief Judge and spoke up, right on cue."
    
    stop music fadeout 4
    
    judge "「I will now announce the winners.{p}\ \ For this year's Grand Prix- 」" 
    "It was as though my ears had stopped working.{p}Whatever he said, my head couldn't process it."
    "It felt like the world had frozen over,{w=.2}\nand everyone was just a hallucination."
    "I couldn't understand a thing."
    "The only thing I knew was that\nall the emotions I'd bottled up earlier\ncame running out of my eyes in a flood."

    jump end28
    
    
########################################################
label end28:
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

    jump day29
