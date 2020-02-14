###Day 22
label day22:
    
    $ renpy.music.set_volume(1.0, 0.0, channel = "music")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound2")
    
    $ day = 22
    $ the_date = "August 22"
    $ event_name = "８月22日"
    
    window hide
    play music birds_chirping
        
    scene sky01 
    show text "{size=+130}August 22" at truecenter
    with Dissolve(.5)
    
    pause 3
    scene black with Dissolve(1)
    pause .4
        
    $ renpy.jump (favorite + "22")
    
    
######################################################        
label kounosuke22:
    $ event_name = "Kounosuke, Summer Festival"

    play music festa01 fadein 1
    scene festival_stands with sdis
    
    "The crowds of people, the smells, the sights...{p}it's just like how it was back then."
    "A sweet aroma and the scent of smoke,{p}mingle with each other.{p}The festival music goes on merrily in the background."
    "Minasato itself has faded quite a bit,{p}but I'm glad to see that this hasn't one bit.{p}It's still the same from when I was a child."

    show ko 003 at center with wipeleft
    
    ko "「Here you go, [fn]. 」"
    fn "「Thanks. 」"
    "I receive some cotton candy from Kounosuke,{p}and we escape to eat somewhere less crowded."
    
    show ko 001 with dis
    
    ko "「It's sorta weird how I can eat so much... 」"
    fn "「Well, yeah. 」"
    "First there were crepes, fried soba,{p}takoyaki, a chocolate banana, shaved ice,{p}a frankfurt, and then cotton candy."
    "I've eaten so much,{p}but there's still room in my stomach."
    
    show ko 005 with dis
    
    ko "「Maybe all that exercise made us hungry? 」"
    fn "「What exercise? We just walked. 」"

    show ko 002 with dis
    
    ko "「Hey! Walking is considered exercise. 」"
    "Well I wouldn't go as far,{p}to say that walking is exercise."
    "But thinking about the way my stomach is,{p}maybe walking around and trying different foods,{p}is a form of exercise too?"
    "Nope."

    show ko 001 with dis
    
    ko "「What should we do after we eat? 」"
    "Kounosuke asks while excitedly biting,{p}at the cotton candy with his huge mouth.{p}That's right."
    
    menu:
        "A. Why not eat some yakitori?":
            jump kounosuke22_eat
        "B. Why don't we play some target shooting?":
            jump kounosuke22_game

    ###############################################################
    label kounosuke22_eat:
    
        $ kouno_yakitori = True
        
        fn "「Ah, why not eat some yakitori? 」"
        "With the alluring scent,{p}of chicken grilling over charcoal,{p}I point towards the yakitori stall."
        
        show ko 005 with dis
        
        ko "「You still want to eat?{p}\ \ I think we should go target shooting soon. 」"
        "Hmm,{w=.2}he does have a point."
        fn "「Then we can just eat until we're full. 」"
    
        show ko 002 with dis
        
        ko "「Heh, alright! 」"
        
        jump kounosuke22_shooting
    
    #################################################################
    label kounosuke22_game:
        
        fn "「How about some target shooting? 」"
        "We're about done eating,{p}so I'd like to play a little."
    
        show ko 003 with dis
        
        ko "「Ah, sounds good. 」"
        fn "「Well then, let's go over,{p}\ \ once we're done eating. 」"
    
        show ko 001 with dis
        
        ko "「Sure. Oh, hey, do you know where the trash is? 」"
        "Wow, he's already done eating.{p}He's faster than me, but a messy eater."
        "Uh-oh, there's a piece of cotton candy,{p}stuck near his mouth."
        "I noticed it when his mouth was moving.{p}He sticks out his tongue,{p}and licks around his mouth."
    
        show ko 003 with dis
        
        ko "「Hey [fn], hurry up and eat.{p}\ \ Let's get going soon! 」"
        "Kounosuke impatiently tugs at my arm.{p}He really is a little kid, isn't he..."
        
        jump kounosuke22_shooting
    
    #################################################################  
    label kounosuke22_shooting:
        
        stop music fadeout 2
        scene black with sdis
        pause .1
        scene festival_stands with sdis
        play music free0421 fadein 1.5
        $ renpy.music.set_volume(0.7, 0.0, channel = "music")
        play sound puu79_a
        pause 1
        play sound puu79_a
        pause .45
        play sound puu79_b
        
        show ko 005 at center with wipeleft
        
        ko "「Agh, damn. I missed again... 」"
        fn "「Shouldn't you be giving up soon?{p}\ \ It looks like you spent a lot of money... 」"
        
        show ko 004 with dis
        
        ko "「No! Men never give up, [fn]! 」"
        fn "「You aren't much of a man to begin with. 」"
        ko "「No one asked you. 」"
        fn "「So you're just going to blow,{p}\ \ all of your cash here? 」"
        
        show ko 005 with dis
        
        ko "「Shut it, [fn]. 」"
        fn "「What? You don't need me now? 」"
    
        show ko 001 with dis
        
        ko "「Huh? 」"
        
        scene festival_stands
        show ko 001 at midleft
        show yk 001 at midright
        with wipe_right
        
        ko "「Oh? Yukiharu? 」"
        yk "「Well, dad told me to tell you that...{p}\ \ you shouldn't waste too much time,{p}\ \ getting wrapped up in games.' 」"
    
        show ko 007 with dis
        
        ko "「Oh... 」"
        fn "「Oh, hey. 」"
    
        show yk 002 with dis
        show yk at bowing
        
        yk "「Hi. 」"
        "As always, Yukiharu-kun bows politely.{p}He really is the exact opposite of Kounosuke."
    
        show ko 005 with dis
        
        ko "「What's wrong? 」"
        "Kounosuke notices me comparing him to Yukiharu,{p}and has a disagreeable look on his face."
        fn "「Everything... 」"
        "In essence, he's a teacher by bad example."
        "If I had a brother like him,{p}I'd raise my self in the opposite direction,{p}seeing what he's done."
    
        show ko 001 with dis
        
        ko "「Anyways, are you alone?{p}\ \ You're not with dad? 」"
    
        show yk 001 with dis
        
        yk "「He's helping out with a stall.{p}\ \ I was with my friends,{p}\ \ but I got separated from them a little bit ago."
        yk "I'm just looking... 」"
        fn "「HIYAAA!? {nw}"
        play sound hit81
        show festival_stands at hshake
        extend "{w=.2} 」"
        "Suddenly, something cold hits the back of my neck,{p}and I scream bloody murder."
        
        scene festival_stands with wipe_right
        show na 002 at center with dis
        
        who "「Ahaha! Me one, you zero! 」"
        "I turn around in surprise and in front of me,{p}is a single child laughing,{p}with a bouncing water ballon."
        fn "「Th-that's... 」"
        who "「What? Unexpected? 」"
    
        scene festival_stands
        show na 002 at midleft
        show yk 001 at midright
        with wipe_right
        
        yk "「Oh, Nana-kun. Where were you?{p}\ \ I was looking all over the place for you... 」"
    
        show na 001 with dis
    
        ykfr "「I didn't know where you were,{p}\ \ so I was looking around here too. 」"
    
        scene festival_stands
        show ko 001 at farleft
        show na 001 at center 
        show yk 001 at farright
        with wipe_right
        
        ko "「Both of you were lost.{p}\ \ {nw}"
        show ko 002 with dis
        extend "And then you meet up here... 」"
    
        show na 002 with dis
    
        ykfr "「Yep. I'm already back with Yuki. 」"
    
        show yk 003 with dis
        
        yk "「But that doesn't mean I was lo... 」"
        fn "「You, have we met somewhere before? 」"
        "I know I'm interrupting him,{p}but something has been bothering me for a while."
        "Without thinking about it,{p}I question Yukiharu's friend."
    
        show na 001 with dis
    
        ykfr "「Huh? 」"
    
        show ko 005 with dis
        
        ko "「Yukiharu was with him when he was...{p}\ \ talking about going to the river the other day.{p}\ \ You forgot already? 」"
        "The river?{p}Umm... oh, this was the kid,{p}from when we were searching for scenery."
        fn "「Ah! Now that you mention that,{p}\ \ I remember, I remember. 」"
    
        show na 002 with dis
    
        ykfr "「Onii-chan, could you be so forgetful? 」"
    
        show ko 004 with dis
        
        ko "「If you don't use your head enough,{p}\ \ you'll start having the brain of an old man. 」"
        fn "「Sh-shut up.{p}\ \ I only just met him recently.{p}\ \ Don't blame me if I forget. 」"
        "It's gotten to the point,{p}where Kounosuke is telling me these things.{p}Kounosuke is supposed to be the dumb one."
    
        show yk 002 with dis
        
        yk "「Well then, we're going.{p}\ \ Don't use up the rest of your money, okay?{p}\ \ You're always running out of it. 」"
    
        show ko 005 with dis
        
        ko "「I-I know... 」"
        fn "「Be careful. 」"
    
        show yk 001 with dis
        
        yk "「Okay! 」"
        
        scene festival_stands with wipe_right
        show ko 007 at center with wipeleft
        
        "The self-satisfied face Kounosuke had,{p}suddenly becomes depressed.{p}Good job, Yukiharu-kun."
        
        show ko 001 with dis
        
        "Yukiharu-kun slips back into the crowd.{p}Kounosuke forgets all of what just had happened,{p}and he readies his gun once again."
    
        play sound puu79_a
        pause 1
        play sound puu79_a
        pause .45
        play sound puu79_b    
        show ko 005 with dis
        
        ko "「Ah shit, again!{p}\ \ Sir, is the barrel of this gun bent? 」"
        attendant "「That's not it at all. You're bad at aiming.{p}\ \ Let me see, hmm... 」"
        "The man comes out of the stall,{p}puts a pellet into Kounosuke's gun,{p}easily takes his aim..."
        
        play sound kachi09
        
        "And quickly hits the target."
        attendant "「See? 」"
    
        show ko 007 with dis
        
        ko "「Oh. 」"
        "As expected, Kounosuke says nothing.{p}It looks like he finally gave up."
        fn "「So, what should we do next? 」"
        ko "「...... 」"
        fn "「Don't cry over spilled milk, man.{p}\ \ It's not like there were any good prizes. 」"
        
        stop music fadeout 3
        
        ko "「That's not it. 」"
        fn "「What is it, then? 」"
        ko "「It looks like I just now ran out of money! 」"
        
        play sound shock1
        
        fn "「Gah, seriously dude? 」"
        "It's just as Yukiharu said not too long ago..."
    
        play music festival_ambience fadein 1.5
        show ko 003 with dis
        
        ko "Wait, I know. You could treat me! 」"
        fn "「Uhh, let me think for a sec, okay?{p}\ \ Hmm... and the answer is no. 」"
    
        show ko 005 with dis
        
        ko "「Alright, alright, I get it.\n\ \ Geez, no need to be so harsh. 」"
        fn "「I can't even afford to.{p}\ \ You're getting what you deserve. 」"
    
        show ko 002 with dis
        
        ko "「Ah, but that reminds me,{p}\ \ didn't you promise to treat me last time? 」"
        fn "「When the hell was that!? 」"
    
        show ko 005 with dis
        
        ko "「During that fiasco at the candy store. 」"
        fn "「Oh... 」"
        "Shit. I did say that, didn't I..."
    
        show ko 003 with dis
        
        ko "「Well then, today I will be eating,{p}\ \ 'as much as I want.' 」"
        "Kounosuke wears a bold smile.{p}I'm getting what I deserve too, aren't I..."
    
        if kouno_yakitori == True:
            jump kounosuke22_fireworks
         
        $ kouno_festival_ghost = True
    
        show ko 001 with dis
        
        ko "「By the way, did you know about this?{p}\ \ When the children play at the festival,{p}\ \ an unknown person will join them. 」"
        fn "「Isn't that how it usually is,{p}\ \ with these kinds of ghost stories?{p}\ \ Like a child spirit. 」"
        
        show ko 002 with dis
        
        ko "「That's right. Well, I don't know,{p}\ \ if it's a child spirit or not,{p}\ \ but it really seems to have been here! 」"
        fn "「Lies... 」"
    
        show ko 005 with dis
        
        ko "「Yes, it really is.{p}\ \ Every year the kids are playing.{p}\ \ Some random child joins them."
        ko "And once the festival is gone, so is the child. 」"
        
        show ko 001 with dis
        
        ko "「It could just be a made-up story,{p}\ \ but isn't it strange that the same story,{p}\ \ turns up every year again and again?"
        ko "I'm not even sure of where it came from... 」"
        fn "「I wonder. Is there a kid like that?{p}\ \ This is just a silly ghost story."
        fn "Weren't these the type of tall tales,{p}that we'd talk about as kids? 」"
    
        show ko 003 with dis
        
        ko "「I'm not making it up, [fn].{p}\ \ Maybe we've even met it before?{p}\ \ That ghost... 」"
        fn "「Yeah, yeah. 」"
    
    #########################################################
    label kounosuke22_fireworks:
    
        play sound rocket_scream
        pause 3.5
        show fireworks
        pause 2
        show ko 001 with dis
        
        ko "「Oh, fireworks! 」"
        fn "「Ooh, they're beautiful.{p}\ \ Just like flowers blooming in the night sky. 」"
        ko "「When did you become such the poet, huh.{p}\ \ Hm. Taking photos of fireworks are hard. 」"
        
        play sound rocket_scream
        pause .6
        play sound2 rocket_scream
        pause 3
        show fireworks
        
        "He sets up his shutter as he says that."
        fn "「Oh! 」"
        ko "「What is it? 」"
        fn "「Isn't this festival 'nostalgic scenery'? 」"
    
        show ko 005 with dis
        
        ko "「...... 」"
        fn "「What? It's not? 」"
        
        show ko 004 with dis
        
        ko "「It's not that I don't think it is, but...{p}\ \ saying something like that ruins the mood. 」"
        fn "「S-sorry... 」"
    
        show ko 001 with dis
        
        ko "「But it also worries me if you apologize. 」"
    
        show ko 008 big at center_big with sdis
        
        ko "「...Hey, [fn]. 」"
        fn "「Yeah? 」"
        
        stop music
        
        ko "「Could... we kiss? 」"
        fn "「Huh? 」"
        
        show ko 001 big with dis
        
        ko "「Well, that kind of thing makes sense,{p}\ \ romantic fireworks and all... 」"
        fn "「Wh-what's with you all of a sudden? 」"
        
        play music free58 fadein 5
        
        "Saying something so crazy makes my heart race.{p}I welcome the proposal itself."
        "But on the other hand,{p}I'd be doing it with him right here."
        
        show ko 003 big with dis
        
        ko "「It's alright, it's alright.{p}\ \ Even if two guys kiss, it's nothing serious. 」"
        "I guess it isn't.{p}Well, it is but it isn't..."
    
        show ko 008 big with dis
        
        "Ah..."
        "While being confused on how I should answer,{p}my mouth is closed up."
        "Kounosuke is right in my face.{p}His fur tickles my cheeks."
        "Then, the heat from Kounosuke's lips,{p}is transfered to mine."
    
        hide ko
        show ko 003 at center
        with dis
        
        ko "「I did it! 」"
        "Kounosuke's face is like that of a child,{p}who has pulled off a successful prank.{p}My mind feels slow and numb."
        fn "「Oh, uhh. Yeah. 」"
        "I finally give a vague response."
    
        stop music fadeout 5
        scene black with sdis
        
        "After that I was in a daze for a while,{p}and don't remember the rest very well."
        "Only one simple fact remained.{p}When I checked my wallet when I got back home,{p}it had become considerably lighter..."
    
        jump end22
    
    
######################################################
label tatsuki22:

    $ event_name = "Festival"
    scene black with sdis
    play music cicada01 fadein 2
    $ renpy.music.set_volume(0.3, 0.0, channel = "music")
    pause 2
    
    "Umm... Nyup nyup."
    who "「Wake up. 」"
    "Hmm?"
    who "「Wake up, [fn]! 」"
    fn "「Five more minutes. 」"
    ta "「Ah, no helping it. Just a little bit...{p}\ \ {nw}"
    play sound bom35
    $ renpy.music.set_volume(0.6, 0.0, channel = "sound")
    #!#window show at vshake
    extend "Like hell I'd say that!!{p}\ \ I said get up, already!! 」"
    
    scene white with dis
    scene tatsukihouse inside
    show tp 401 at center
    with wipe_corner
    
    fn "「Ehh, Tatsu-nii? 」"
    
    show tp 406 with dis
    
    tp "「Who're you calling Tatsu-nii? Don't sleep in. 」"
    fn "「T-Tappei-san!? 」"
    fn "「Good morning... 」"
    
    show tp 402 with dis
    
    tp "「Yeah, morning. 」"
    "As I woke up (by getting hit with the futon),\nI could see it wasn't Tatsu-nii standing there,\nbut Tappei-san."
    
    show tp 403 with dis
    
    tp "「Stop sleeping in. You're late, late! 」"
    fn "「Ehh!?{w} I'm sorry.{p}\ \ I'll get ready now... huh?{p}\ \ I thought today was a holiday for the festival... 」"
    
    show tp 401 with dis
    
    tp "「Yep, we're taking a break from normal work today,\n\ \ because we have to help prepare the festival. 」"
    fn "「Oh yeah, ever since I was a kid,\n\ \ you've been on staff for the festival. 」"    
    tp "「Of course.{p}\ \ Livening things up with the festival\n\ \ is the duty of men, after all. 」"
    fn "「So you're on again this year? 」"
    tp "「You're doing it. 」"
    fn "「Huh? 」"
    
    show tp 404 with dis
    
    tp "「I'm not saying it twice.\n\ \ You're going to go in my place to help out. 」"
    fn "「What are you saying?\n\ \ This is so unreasonable, so early in the morning.{p}\ \ Wait, are you drunk...? I smell sake... 」"
    
    play music free0428 fadein 2
    $ renpy.music.set_volume(0.7, 0.0, channel = "music")
    
    "Finally, I am awake.{p}Tappei-san reeks of sake, and his face is red.{p}He's totally drunk."
    "Why is he drunk so early in the day...?"
    fn "「It's so early.{p}\ \ Is it okay to be drinking already? 」"
    
    show tp 405 with dis
    
    tp "「What day is it today? 」"
    fn "「The festival day. 」"
    tp "「And what do you do on the festival day? 」"
    fn "「The only thing to do is drink... 」"
    
    show tp 406 with dis
    
    tp "「Good, you get it after all. 」"
    "It's no good, I can't go against him..."
    fn "「But how come I'm substituting for you\n\ \ in the festival preparations? 」"
    
    show tp 401 with dis
    
    tp "「You're not gonna make me work my ass off drunk,\n\ \ are you? 」"
    "So why do I...\nAre you saying you'd be fine if you weren't drunk?"
    
    show tp 403 with dis
    
    tp "「You say something? 」"
    fn "「Nonono, nothing at all! 」"
    tp "「Are you... 」"
    tp "「...saying that you can't hear me? 」"
    fn "「That's not true! 」"
    tp "「Get this into your head!{p}\ \ My word is law in the Midoriya Group!!{p}\ \ Don't question me, just follow my orders!!! 」"
    tp "「You're 100 years to early to talk back to me!!! 」"
    "But I wasn't..."
    tp "「Got it?{w} 　If you get it, then answer me! 」"
    fn "「Yes! 」"
    tp "「Don't talk back to me!{p}\ \ My word is absoulte!{p}\ \ {nw}"
    show tp 405 at jump_up
    extend "*Hic-!*{w=.2} 」"
    fn "「Understood! 」"
    
    show tp 405 with dis
    
    tp "「Then it's all right. If you get it, it's all right. 」"
    "Tappei-san said that, and gently stroked my face."
    "His hand is so rough..."
    tp "「Okay, I'm counting on you. 」"

    hide tp with wipe_right
    
    "With that, Tappei-san thumped out of the room."
    fn "「Haah... today's going to be tough. 」"

    stop music fadeout 2
    scene black with sdis 
      
    $ event_name = "The start of a busy day"

    scene tatsukihouse inside with sdis   
    play music free02
    show ta 501 at center with dis
    
    ta "「Hey, you're finally awake?{p}\ \ It's almost noon. 」"
    "I went downstairs,\nto find Tatsu-nii waiting around.\nHe'd already changed into a happi coat."
    fn "「Tatsu-nii, you're already in a happi coat?{p}\ \ Isn't it early? 」"

    show ta 502 with dis
    
    ta "「You moron, what day is it?{p}\ \ You know what comes next. Gahahahaha! 」"
    "Tatsu-nii had a smile spread across his whole face\nas he posed with his large biceps."
    "As expected of family...\nThe apple really doesn't fall far from the tree."
    
    show ta 501 with dis
    
    ta "「We've got your yukata ready, [fn],\n\ \ so you don't need to worry. 」"
    fn "「Eh!?{w} 　You got me a yukata?{p}\ \ I'm human... there isn't a tail hole, is there? 」"
    
    show ta 508 with dis
    
    ta "「No, there isn't.{w} We made this just for you.{p}I think Pa brought it in from somewhere. 」"
    fn "「I see, thanks a lot. 」"
    
    show ta 502 with dis
    
    ta "「Gahaha, don't sweat it. 」"
    ta "「It's probably one of Pa's whims,\n\ \ and he probably got overcharged for it.{p}\ \ Anyway, we'll get going once we eat. 」"
    fn "「Where are we going? 」"
    
    show ta 501 with dis
    
    ta "「Pa's sending you to represent the group, right?{p}\ \ He's making me go, too. 」"
    ta "「He said 'You two are half a man each,\n\ \ so it balances out if I send you both.' 」"
    fn "「I see. I'm glad I'm with you, Tatsu-nii.\n\ \ I don't know if I could manage by myself. 」"
    
    show ta 502 with dis
    
    ta "「Yeah, no worries.{p}\ \ Leave it all to me. 」"
    fn "「I'll be relying on you.{p}\ \ We might stand a chance,\n\ \ if there's someone with experience. 」"
    
    show ta 510 with dis
    
    ta "「Oh, it's my first time, too. 」"
    fn "「Cool, your first time doing this...{p}\ \ Wait, this is your first time too!? 」"
    
    show ta 508 with dis
    
    ta "「It's nothing serious.{p}\ \ We'll be just fine, it'll all work out. 」"
    "Just like Tatsu-nii... is this really okay?{p}He's not all that reassuring."
    
    show ta 501 with dis
    
    ta "「First off, we should go to the shrine.\n\ \ That seems like the best thing to do. 」"
    fn "「That's where the festival will be. 」"
    fn "「If that's the case, we'd better hurry... 」"
    
    show ta 509 with dis
    
    ta "「Yep.{w} C'mon, hurry up and get ready.{p}\ \ You haven't had breakfast yet, have you?{p}\ \ Well, it's almost lunch anyway.{w} {nw}"
    show ta 502 with dis
    extend " Gahaha! 」"
    fn "「Yeah, just wait a bit. 」"
    
    show ta 501 with dis
    
    ta "「I don't want to wait, hurry it up.{p}\ \ I'll get you some food while you wash up. 」"
    fn "「Thaaanks, but put it in a rice bowl,\n\ \ not a porcelain one. 」"
    
    show ta 508 with dis
    
    ta "「I got it, a rice bowl it is. 」"
    ta "「Do you still have something against the size\n\ \ of the porcelain bowls?{p}\ \ Damn, you're so picky... 」"
    fn "「Y'know, you should think about our bodies' sizes. 」"
    
    show ta 501 with dis
    
    ta "「You just aren't big because you don't eat much.\n\ \ When sumo wrestlers bulk up their bodies,\n\ \ they eat a lot while training. 」"
    
    show ta 508 with dis
    
    ta "「Chuukichi eats about as much as we do, too. 」"
    fn "「I get the feeling Chuukichi-kun gets force-fed... 」"
    fn "「Like last time... 」"
    fn "「Chuukichi-kun said 'I can't eat anymore'.\n\ \ Didn't Tappei-san force even more into his mouth\n\ \ after that? 」"
    
    show ta 510 with dis
    
    ta "「Well, if I leave anything unfinished,\n\ \ Pa threatens to impale me like a sausage.{p}\ \ Besides, we can't afford to waste food. 」"
    "If he said 'eat, eat!' that much,\nit'd be more than I could handle..."
    "I can never tell if Tappei-san's serious or not,\nso I'll just act like I didn't hear."
    
    show ta 502 with dis
    
    ta "「You want me to heat up the side dishes? 」"
    fn "「Yes, please. 」"
    "Anyway, I'll go wash my face, brush my teeth,\nthen go eat."

    $ event_name = "At the Shrine"
    
    play music cicada01 fadein .5
    scene black with sdis
    scene shrine_court with sdis
    
    "On the way up to the shrine grounds,\nwe pass the workers constructing the float,"
    "the people putting up the paper lanterns,"
    "the people working on the stage for the Bon dance,"
    "and so many other people,\nbusy bustling around before everything is ready."
    fn "「The festival hasn't started yet,\n\ \ but it's so crowded and hectic here. 」"
    fn "「This is my first time coming to the shrine\n\ \ while the set-up is going on.\n\ \ It feels a little fresh. 」"

    show ta 501 at center with dis
    
    ta "「We've never had a reason to go this early, before. 」"
    "Today, I'm not here to participate.\nRather, I'm here to help entertain..."

    show cu 002 at midright with dis
    
    cu "「Heey!{w} 　Good mornin'! 」"
    "Chuukichi-kun walked over to us,\nand greeted us cheerfully."
    
    show cu 001 with dis
    
    cu "「So Aniki and Young Master came after all. 」"
    
    show ta 502 with dis
    
    ta "「Does that mean Pa ordered you to come, too? 」"

    show ni 001 at farright behind ta with wipeleft
    
    ni "「That's correct. 」"
    ni "「Since carpentry is our forte,\n\ \ that's probably where we should be doing work.{p}\ \ We haven't been called on yet, which is strange. 」"
    
    show cu 002 with dis
    
    cu "「Yeah. 」"
    
    show ni 003 with dis
    
    ni "「So I thought it'd appropriate for us to be on\n\ \ fatigue duty.{w} However, I think the question\n\ \ remains about why the boss isn't here... 」"
    "Right now, that person is drinking..."
    
    stop music fadeout .4
    scene tatsukihouse inside
    show tp 404 at center
    with wipe_right
    play sound jap_002
    pause .25
    
    tp "「Kaaah! I can'ts shtand this!! 」"
    
    play music cicada01
    scene shrine_court
    show ni 001 at farright
    show ta 504 at center
    show cu 001 at farleft
    with wipe_right
    
    ta "「That damned old man. 」"
    "But does that mean up until now,\nTappei-san was responsible for everything?"
    "Plus, it looks like he's never borrowed anything\nfor the festival preparations..."
    ni "「Well, we have work to do,\n\ \ so we'll be getting back to it. 」"
    
    show cu 002 with dis
    
    cu "「Yeah.{w} Let's do our best. 」"
    
    hide ni with wipe_right
    hide cu with wipe_right
    show ta 001 with dis
    
    ta "「Let's go, too. 」"
    fn "「Yeah, let's. 」"
    
    scene shrine with wipeleft 
    $ encounter_shigure = True
    show sg 001 at center with dis
    
    sg "「You're even later than I thought you'd be. 」"

    show ta 501 at farright behind sg with dis
    
    ta "「Well... sorry about that, Uncle. 」"
    fn "「I'm sorry, we were late because I was so slow. 」"
    
    show sg 002 with dis
    
    sg "「No, it's fine.{w} At any rate,\n\ \ you boys must've been forced over here\n\ \ by the Chief's unreasonable demands. 」"
    
    show ta 508 with dis
    
    ta "「Well, that's kinda true. 」"
    ta "「All of a sudden,\n\ \ he goes 'you're representing us'.\n\ \ Bastard. 」"
    
    show sg 001 with dis
    
    sg "「What is the Chief doing at the moment? 」"
    "Right now, that person is drinking..."
    
    stop music fadeout .4
    scene tatsukihouse inside
    show tp 404 at center 
    with wipe_right
    
    yukino "「What are you doing, drinking in broad daylight?\n\ \ The sun hasn't even set yet. 」"
    
    play sound jap_002
    show tp 406 with dis
    
    tp "「Idiot!!{p}\ \ You think that'd stop me from drinking!? 」"
    
    play music cicada01
    scene shrine
    show tp 501 at midright
    show sg 001 at midleft
    with wipe_right
    
    sg "「...{w} Well, he must be up to something stupid.{p}\ \ More importantly, the work I'll have you two do\n\ \ will perhaps be cleaning almost everything... 」"
    
    show ta 508 with dis
    
    ta "「Anything is fine!{p}\ \ We'll do whatever you want us to. 」"
    sg "「What to do... 」"
    "Fiddling with his neat beard,\nShigure-san looked up into the sky,\nand thought for a short while."
    
    show sg 002 with dis
    
    sg "「I know. Can I ask you to run some errands? 」"
    
    show ta 502 with dis
    
    ta "「Okay, something like that should be super easy. 」"
    fn "「If it's that, then even I shouldn't have a problem. 」"
    sg "「Well then, can you go get some\n\ \ Indian millet from the school? 」"
    
    show ta 501 with dis
    
    ta "「Indian millet? Is that sweet sorghum? 」"
    sg "「That's the one. 」"
    
    show sg 001 with dis
    
    sg "「It's only a little, but I thought our food cart\n\ \ should have some local produce. 」"
    sg "「Thankfully, the school fields produce millet,\n\ \ which should be a good addition. 」"
    
    show ta 502 with dis
    
    ta "「What about grilled corn? 」"
    sg "「Well, the other villagers are running carts, too,\n\ \ and I got the idea after seeing them. 」"
    sg "「I'll likely lose to the dedicated stall-keepers,\n\ \ but it is a nice bonus for acquaintences. 」"
    fn "「Oh, so that's how Minasato gets its earnings. 」"
    
    show ta 501 with dis
    
    ta "「Before, the village guys also left,\n\ \ but that was the Village Restoration Project. 」"
    
    show sg 002 with dis
    
    sg "「No, that was actually my hobby.{p}\ \ Of course, I used any earnings for the village. 」"
    "...I think I see why Tappei-san gets along with him."
    
    show ta 508 with dis
    
    ta "「Geez, are we being made to help with your hobby? 」"
    sg "「Hohoho, don't be so discouraged.{p}\ \ Everyone in the village is working together,\n\ \ so this food cart should do well. 」"
    
    show sg 001 with dis
    
    sg "「Isn't that wonderful? 」"
    ta "「I guess...{p}\ \ {nw}"
    show ta 501 with dis 
    extend "Hm, yeah, it is. 」"
    sg "「That's how it is. Well, I'm relying on you. 」"
    
    show ta 509 with dis
    
    ta "「Leave it to us!{w} 　Come on, [fn], let's go. 」"

    hide ta with wipe_right
    
    fn "「Ah- yeah.{w} We'll be going now. 」"
    "Hmm, one way or another,\nI feel like something was skillfully avoided..."
    
    show ta 509 at midright behind sg with wipe_right
    
    ta "「Hey hey, time's wasting. Let's go! 」"
    
    show sg 002 with dis
    
    sg "「Be careful, now. 」"

    ###########################################
    label tatsuki22_school:

        $ event_name = "Won't you join in?"
        
        #stop music fadeout 1
        scene school01 with sdis
        play music free0211
        $ renpy.music.set_volume(0.7, 0.0, channel = "music")
        scene school entryway with wipeleft
        
        fn "「Excuse me...! 」"
    
        show ta 501 at center with dis
        
        ta "「Anyone here? 」"
        fn "「I wonder if Botan-sensei is around... 」"
        
        show ta 508 with dis
        
        ta "「Did he go out?{p}\ \ If we wait here, he'll come by sooner or later. 」"
        fn "「Yeah, let's stay here for now,\n\ \ in case he comes looking for us. 」"
        "..."
        
        hide ta with wipe_right
        scene school office with wipe_right
        show ta 508 at center with wipe_right
        
        ta "「Such good cooling here. 」"
        fn "「Tatsu-nii, this is wrong. 」"
        
        show ta 509 with dis
        
        ta "「This temperature is the best!!{p}\ \ {nw}"
        show ta 508 with dis
        extend "Wait, what is this?\n\ \ It won't go down further than 18 degrees? 」"
        
        fn "「I know no one's here,\n\ \ but we shouldn't be in the teachers' lounge. 」"
        
        show ta 510 with dis
        
        ta "「Don't worry, we'll be fine. 」"
        fn "「Even so, we shouldn't! 」"
        
        show ta 501 with dis
        
        ta "「For such an old school to have so many coolers...{p}\ \ Maybe the number of students\n\ \ has something to do with it? 」"
        ta "「We only have electric fans at home.\n\ \ It's so luxurious here. 」"
        fn "「Isn't this an air conditioner, not a cooler? 」"
        
        show ta 508 with dis
        
        ta "「Men don't sweat the small stuff. 」"
        
        show ta 509 with dis
        
        ta "「We're graduates from this school,{p}\ \ which means we're entitled to priveleges here! 」"
        fn "「I moved away before graduating, though.... 」"
        
        show ta 502 with dis
        
        ta "「Hey, there's manjuu in the cupboard. 」"
        fn "「If you take any, we'll definitely be found out!{p}\ \ There aren't any other visitors here,\n\ \ so if something goes missing, it'll get noticed! 」"
        
        show ta 501 with dis
        
        ta "「When we were kids, you used to say that\n\ \ 'the perfect prank leaves no evidence!'{p}\ \ {nw}"
        show ta 508 with dis
        extend "Don't worry, we'll be gone by the time it's noticed. 」"
        fn "「That's not the point,\n\ \ and we're not kids anymore. 」"
        
        show ta 501 with dis
        
        ta "「What, do you want to take it outside?\n\ \ We're gonna eat it, anyway. 」"
        "Tatsu-nii unwrapped the manjuu and held it out."
        fn "「Hmm... 」"
        "Man, now I've done it.{p}I just accepted it."
        
        show ta 502 with dis
        
        ta "「You want tea, or coffee? 」"
        fn "「If it's manjuu, then it's got to be tea.{p}\ \ Make it strong, please. 」"
        
        stop music fadeout 1
        scene black with sdis
        
        "30 minutes later..."
        
        play sound puu56
        show black at hshake
        
        "*Gurglegurglegurglegurgle*"    
        
        play music oo39_cho_ys001
        $ renpy.music.set_volume(0.7, 0.0, channel = "music")
        scene school office
        show ta 503 at center
        with wipe_right
    
        ta "「My stomach...{w} {nw}"
        show ta at jump_up
        extend " {w=.2}Oohh. 」"
        
        play sound puu56
        show school office at hshake
        
        "*Rumblerumble*"    
        fn "「It hurts... 」"
        
        show ta 509 with dis
        
        ta "「Guooooh!{w} The manjuu, was the manjuu spoiled? 」"
        fn "「That's why I tried stopping you. 」"
        
        show ta 508 with dis
        
        ta "「Damn it, nobody told us that before we ate two,\n\ \ and had tea afterwards. 」"
        fn "「Tatsu-nii, how many times did I say not to do it?{p}\ \ There's almost nothing left. 」"
        ta "「What the...{w} {nw}"
        show ta 503 at jump_up
        extend " Haahh!!! 」"
        fn "「...Anyway, let's get to the bathrooms. 」"
        "Now's not really the time to talk."
        "We've gotta get to the bathroom, and quickly."
    
        hide ta with wipe_right
        scene school hallway 1 with wipe_right
        show ta 506 at center with wipe_right
        
        ta "「[fn]... this is as far as I go.{p}\ \ I don't think I can move another step. 」"
        fn "「That can't be, we're so close! 」"
        
        show ta 508 with dis
        
        ta "「There's a brown spot on my fundoshi,\n\ \ but I can pass it off as curry... 」"
        fn "「How's that a good idea?{p}\ \ It won't work, Tatsu-nii.{p}\ \ Just walk a little further... 」"
        
        show ta 503 at jump_up
        pause .2
        
        ta "「A-{nw}"
        show ta at jump_up
        extend " {w=.2}ahh...{w} I can't... hold it... 」"
        fn "「Hang on, we're almost there. 」"
        
        show ta 510 with dis
        
        ta "「Sorry, looks like this is the end for me. 」"
        fn "「No, don't say that. 」"
        
        show ta 503 with dis
        
        ta "「Later. I'll give them a good punch for you... 」"
        fn "「Tatsu-niiiiiiii!!! 」"
        
        stop music fadeout 2
        scene toilet_in with wipeleft
        play sound toilet_flush
        
        fn "「Haaah... We made it! 」"
        "The restoom is so calming... I wonder why.{p}It's great that Tatsu and I got here in time."
        ta "「Uoooooooooh!! 」"
        "It seems Tatsu-nii's still in a bit of a pinch."
        fn "「Tatsu-nii, are you okay? 」"
        "And he ate so much, too..."
        who "「Whew, this is terrible. 」"
        "Huh? Someone's come in."
        who "「Really terrible. 」"
        
        play sound toilet_door
        
        "The owner of the voice rushed into\nthe restroom that we were in."
        "Judging by the sound of it, it's Botan-sensei."
    
        show toilet_in at vshake
        play sound bom19_b
        "{size=+15}PBBTTTHH!!!"    
        bo "「Hmumu, no good!!{w} 　So much gas!!!{p}\ \ What should I do??? 」"
        "Is there no normal adult nearby?"
        bo "「No, there's no toilet paper!{p}\ \ How did this happen!? 」"
        "What do I do...?"
        
        menu:
            "A. Prank him.":
                jump tatsuki22_prank
            "B. Help him.":
                jump tatsuki22_help
            "C. Throw him the cardboard tube.":
                jump tatsuki22_god
        
    #######################################################
    label tatsuki22_prank:

        $ event_name = "Mischief"
        
        play music oo39_cho_ys001
        scene toilet_out1 with wipe_right
        
        fn "「Eww, poop! 」"
    
        play sound crash21
        show toilet_out1 at hshake
        pause .25
        play sound crash21
        show toilet_out1 at vshake
        pause .25
        play sound crash21
        show toilet_out1 at hshake
        pause .25
        scene  toilet_out1
        
        "I wiped my butt, gathered up my pants,\ntook a mop from the corner,\nand yelled as I banged on the door."
        bo "「Who is it!?{w} What's going on! 」"
    
        play sound water_pour
        pause .3
        
        "I flinched at Sensei's angry voice,\nthen pulled a hose from the supply closet,\nthrew it over the door, and turned it on."
        bo "「So cold!!{w} I won't forgive this.{p}\ \ What did I do to deserve this? 」"
        
        play sound crash21
        show toilet_out1 at hshake
        pause .25
        play sound crash21
        show toilet_out1 at vshake
        pause .25
        play sound crash21
        show toilet_out1 at hshake
        pause .25
        scene toilet_out1
        
        fn "「Pooping～, pooping～♪ 」"
    
        show ta 501 at center with dis
        
        ta "「Hey, what are you doing? 」"
        "While I was caught up in my prank,\nTatsu-nii finished his business, and came out."
        fn "「Tatsu-nii, let's run!! 」"
        
        show ta 503 with dis
        
        ta "「H-hey, what is this? 」"
    
        hide ta with wipe_right
        play sound door_force
        pause .3
        show bo 003 at center with wipe_right
    
        bo "「Whozzat!!{w} Wait!!! 」"
    
        hide bo with wipe_right
        scene black with wipe_right
        
        "I pulled on Tatsu-nii's hand as I ran.{p}He followed, not really understanding what happened."
        "In the end, we went back to the shrine grounds,\nas that was the only thing we could do."
        "Somehow or other, that night\nTatsu-nii and I were tied up,\nbut that's another story."
    
        jump end22
    
    #######################################################
    label tatsuki22_help:
        
        $ event_name = "Miracle of God"

        scene toilet_out1 with wipe_right
            
        fn "「Botan-sensei?{w} Shall I get you some toilet paper? 」"
        bo "「[ln]?{w} Sorry, I need assistance. 」"
        ta "「We'll help, sensei! 」"
        "Uhh, is it in the supply closet?"
        fn "「Oh, there it is. 」"
        fn "「I'm throwing it over the top-! 」"
        ta "「Ah, ah... 」"
        
        play sound toilet_flush
        show bo 002 at center with dis
        
        $ encounter_botan = True
        
        bo "「Whew, you saved me. 」"
        fn "「Oh no, I didn't do anything special. 」"
        
        show bo 001 with dis
        
        bo "「What are you saying?{w} I should thank you. 」"
        
        show bo 002 with dis
        
        bo "「Truly, thank you.{w} You are a god. 」"
        "After Botan-sensei said that,\nhe caught me in big hug."
        "Pinned as I was,\nI couldn't move at all."
    
        show ta 501 at farright behind bo with dis
        
        ta "「Wheeew, that was terrible. 」"
        ta "「I feel better now that's outta my system... 」"
        
        play music free44
        $ renpy.music.set_volume(0.7, 0.0, channel = "music")
        show ta 503 at jump_up
        pause .2
        
        ta "「What the!?{w} Sensei, what are you doing with my [fn]? 」" 
        
        show ta 509 with dis
        
        ta "「He's mine!{w} I'll never hand him over!! 」"
        
        show ta at midright with move2
        play sound bosu34
        show bo 004 big at center_big with explosion    
        
        bo "「Wha-!?{w} 　What are you doing? 」"
        ta "「Oooh, don't get close to my [fn]-!! 」"
        "In his agitation, Tatsu-nii grabbed me from behind,\nwhich pushed me into Sensei's stomach."
        fn "「Wawawa, Tatsu-nii! 」"
        "Caught as I was, I was sandwiched between the two,\nand my face was pressed harder into Sensei's belly."
        fn "「I-{w=.2}it hurts... 」"
        "I can't breathe."
        "Also, my nostrils are full of that teacher smell.{p}It's a bit overpowering."
        bo "「Ow, no need to be violent.{p}\ \ If you keep holding me that tightly, I... 」"
        "Sensei?"
        
        scene toilet_out2
        show ta 508 at midright
        show bo 004 at midleft
        with wipe_right
        
        ta "「What's up with that reaction, Sensei?{p}\ \ You don't look so great. 」"
        "When Tatsu-nii spoke, he loosened his grip,\nand I could finally break free."
        fn "「Haah, that was rough.{p}\ \ Don't be so rash like that. 」"
        fn "「You have to be a bit more careful, Tatsu-nii,\n\ \ since you're bigger and stronger than normal.{p}\ \ Could you try to be more gentle? 」"
        
        show ta 506 with dis
        
        ta "「But, Sensei was holding you, and...{p}\ \ My bad. 」"
        
        show bo 002 with dis
        
        bo "「I'm sorry, too.{p}\ \ Hugging you all of a sudden like that. 」"
        fn "「I'm fine with you two hugging me,\n\ \ but did you wash your hands first? 」"
        bo "「Ah-! 」"
        
        show ta 510 with dis
        
        ta "「Whoops. 」"
        "It's fine, I'm not sure I mind..."
        
        play music cicada01 fadein 1.5
        $ renpy.music.set_volume(0.3, 0.0, channel = "music")
        show bo 001 with dis
        
        bo "「Oh yes, did you two come to the school to pick up\n\ \ the vegetables I harvested?{p}\ \ They're ready. 」"
        bo "「Growing them is mostly a hobby, but it's rewarding.{p}\ \ Besides, everyone else here is a farmer,\n\ \ so this is a taste of what life here's like. 」"
        fn "「Thank you very much. 」"
        
        show ta 508 with dis
        
        ta "「Anyway... where were you, Sensei?\n\ \ We were looking for you. 」"
        
        show bo 002 with dis
        
        bo "「Ah. I was in the field out back,\n\ \ when my stomach started to hurt,\n\ \ and the outdoor restroom is out of order. 」"
        bo "「I was in a real hurry,\n\ \ so that's why I burst in here like I did. 」"
        
        show ta 501 with dis
        
        ta "「Sensei also getting sudden stomach aches...\n\ \ Terrible, huh. 」"
        bo "「What, you two did, too? 」"
        "Huh?{w} 　Sensei also had sudden stomach problems?{p}Coincidence?"
        fn "「Sensei... 」"
        bo "「What? 」"
        fn "「You ate them too, didn't you... 」"
    
        show bo at jump_up
        pause .2
        
        bo "(Gurk-!)"
        
        show bo 001 with dis
        
        bo "「No way... I'm a teacher.{p}\ \ Well... maybe I did eat some of the snacks...{p}\ \ Wait, it's not like I ate them all! 」"
        "What should I do?\nIs it all right to come clean...?"
        
        show bo 002 with dis
        
        bo "「In any case, you two also had some, right?{p}\ \ Otherwise, I don't really understand.{p}\ \ If you did, then we're alike that way. 」"
        "Is there really no normal adult\nanywhere near me...?"
        
        show ta 508 with dis
        
        ta "「Is that okay, Sensei? 」"
        ta "「I mean, what'd happen if we spread a rumor...{p}\ \ If I said something to the principal, or Pa? 」"
        bo "「Midoriya, forgive me at least that much. 」"
        
        show ta 502 with dis
        
        ta "「Gahahaha, I'm joking, Sensei.{p}\ \ I couldn't do anything like that to you. 」"
    
        show bo 004 with dis
        
        bo "「You are... A god... 」"
        "Why is Sensei such good friends with Tappei-san?\nSomehow, I think I know."
        "It's almost definitely not\na question of personality..."
        
        show bo 001 with dis
        
        bo "「Anyway, I heard you two were representatives,\n\ \ but what is the boss doing now? 」"
        "Right now, that person is drinking..."
        
        stop music
        scene tatsukihouse inside
        show tp 404 at center
        with wipe_right
        play sound jap_002
        
        tp "「HEEEEEeeeeyyyy!!! 」"
        yukino "「Oh, stop it, you.{p}\ \ Don't you know you have to get moving for tonight?{p}\ \ I have to tidy up, so be good. 」"
        
        play music cicada01
        $ renpy.music.set_volume(0.3, 0.0, channel = "music")
        scene toilet_out1
        show ta 501 at midright
        show bo 001 at midleft
        with wipe_right
        
        bo "「Well, I haven't heard anything.{p}\ \ If it's the boss,\n\ \ you can guess, one way or another. 」"
        "Yes, I think it's just as you're imagining..."
        
        show bo 002 with dis
        
        bo "「Now, let's go. 」"
        
        jump tatsuki22_delivery
    
    
    #####################################################
    label tatsuki22_god:
        
        $ event_name = "The Importance of Paper?"
        
        "I took the toilet paper,\nand violently pulled it off the roll."
        bo "「Is someone in the next stall over?{p}\ \ Excuse me, but can you give me some toilet paper? 」"
        "The toilet paper formed a small pile on the floor,\nand all that was left was the tube from the middle."
        fn "「Here, use this! 」"
        play sound puu79_a
        "I tossed the tube into the next stall."
        bo "「Uh, excuse me...!?{w} {nw}"
        play sound bosu35
        show toilet_in at hshake
        extend " What is this!?{p}\ \ Only the tube... what is the meaning of this!?{p}\ \ Why was there lots of rattling in the next stall!? 」"
        "What do I do, all the soft bits are useless...{p}Is there any other paper around?{p}{nw}"
        play sound freeze04
        extend "...I know,{w=.2} there's this!!"
        fn "「Sensei. 」"
        bo "「What?{w} Wh-why won't you give me any toilet paper!? 」"
        fn "「As of right now, this is all that's in stock,\n\ \ so please forgive me. 」"
        
        play sound paper00
        
        bo "「Thank you...{w} Wait,\n\ \ isn't this the wrapper of the manjuu I had earlier?{p}\ \ I'm supposed to use this? 」"
        "This isn't good, either..."
    
        play sound bom35
        pause .5
        play sound unari00
        show toilet_in at vshake
        
        fn "「Whoa! 」"
        
        play music free27
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        
        "That was unexpected."
        "That tremor, along with the jolt to the building,\nfelt like some terrible warcry from a wild beast."
        "Just what the hell happened?{p}I don't think that was an earthquake..."
        bo "「Is this...{w} No way, that's way too fast! 」"
        fn "「Sensei? 」"
        
        play sound bom35
        show toilet_in at vshake
        pause .3
        scene school01 with sdis
        show ta 503 at center with dis
        
        ta "「Uwaaaahhhh, help!! 」"
        cu "「Fufufufu...{w=.2}-ssu. 」"
    
        scene toilet_out1 with sdis
        
        fn "「Ah,{w=.2} that's Chuukichi...kun? 」"
        "A giant Chuukichi-kun crossed the school grounds\nlike they were nothing, broke into the restroom,\nand grabbed Tatsu-nii."
        
        stop music fadeout 1.5
        scene toilet_out2 with sdis
        play music free0506 fadein 1
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        
        bo "「[fn], you're there, right?{p}\ \ We don't have time to waste.{p}\ \ What I'm about to say is important, so listen up. 」"
        bo "「Chuukichi...{w} Is no mortal.{p}\ \ He's a demon. 」"
        fn "「Chuukichi-kun's a demon? What are you saying? 」"
        bo "「There's an old legend, here in Minasato.{p}\ \ It's about the village's history,\n\ \ and there are many different versions of it. 」"
        bo "「Amongst them, there's this one. 」"
        bo "「In the Heian Era,\n\ \ there was an evil that\n\ \ threatened to destroy the world. 」"
        bo "「This demon used the power of chimimouryou,\n\ \ and the world descended into darkness. 」"
        bo "「Everywhere, cruelty was pushed to extremes,\n\ \ until finally the imperial capital was destroyed. 」"
        bo "「However, one person was able to hold this demon\n\ \ in check, and that was a master onmyouji. 」"
        bo "「The battle between them was extremely fierce,\n\ \ and it went on for three straight days. 」"
        bo "「One by one, the master's comerades fell,\n\ \ until there was only one other remaining,\n\ \ but somehow, they repelled the demon. 」"
        bo "「The master met with a nearby family of carpenters.\n\ \ With their help, he used the last of his strength,\n\ \ and sealed the evil demon within the land. 」"
        fn "「And Minasato Village is\n\ \ where this sealed land is. 」"
        bo "「Correct. 」"
        bo "「That's where the legend ends.{p}\ \ If that was it, there'd be no problem. 」"
        bo "「However, the seal isn't perfect.\n\ \ It only holds for one thousand years. 」"
        bo "「After a thousand years, the seal will break,\n\ \ and the world will be destroyed.{p}\ \ However, in preparation for that event... 」"
        bo "「There is a contingency.{p}\ \ A chosen one, to fight the evil demon. 」"
        bo "「[fn], you are the descendent of that onmyouji.{p}\ \ You are the chosen one. Only you can fight this! 」"
        fn "「Eeehh? Me!? 」"
        bo "「Your return to Minasato,\n\ \ and your assistance at the Midoryia Group...{p}\ \ This is no coincidence. Everything was planned. 」"
        fn "「No way, that's... 」"
        bo "「This is no trick.{w} There's no time,\n\ \ if you are to defeat him, you must do so, now. 」"
        bo "「If he completely awakens,\n\ \ there will be no hope of victory. 」"
        bo "「If that happens, he will leave Minasato,\n\ \ and the world will fall to ruin. 」"
        fn "「I...{w} It's so sudden, to be told to fight.{p}\ \ On top of that, it's Chuukichi-kun... 」"
        bo "「I understand your feelings.{p}\ \ But he's no longer a person. 」"
        fn "「B-{w=.2}but... 」"
        bo "「In truth, I wanted to tell you after the festival,\n\ \ But for the seal to break today...{p}\ \ There was supposed to be more time! 」"
        ta "「[fn]...! Run away!{p}\ \ I'll do something about this. 」"
        "Tatsu-nii"
        fn "「Damn it... I'll go.{p}\ \ I don't know what I can do,\n\ \ But I won't leave Tatsu-nii behind. 」"
        bo "「I'm sorry, forcing it all on you like this. 」"
        fn "「Well, here goes nothing. 」"
        bo "「[fn], take this with you. 」"
    
        play sound iron_pipe
        pause .8
        
        "He pulled a plane-spear from somewhere,\nand laid it at my feet."
        "Past the handle, this weapon has a leaf-like blade.\nOverall, it looks like its name:{p}A spear-like wood plane."
        "If it hits, it looks like it'll hurt."
        fn "「What's this? 」"
        bo "「A sacred plane-spear.{p}\ \ You'll need it to send him back to oblivion. 」"
        bo "「If it's you, and you've studied with the boss,\n\ \ you should be able to master it...{p}\ \ Here, take it. 」"
        bo "「Since there's no toilet paper, I can't leave.{p}\ \ You'll have to go it alone.{p}\ \ Come back safely. 」"
        fn "「Sensei... 」"
        "I tightly grasped the plane-spear,\nthen jumped out into the schoolyard."
    
        scene black with sdis
        play music free0630 fadein 3
        
        cu "「I've been waitin', Aniki... 」"
        fn "「Chuukichi-kun, what did you do with Tatsu-nii!? 」"
        cu "「I got tired o' holdin' him in my hand,\n\ \ so I made him go home. 」"
        fn "「No way... 」"
        cu "「Aniki... before we fight, I gotta say somethin'.\n\ \ I guess Botan-sensei said that you need that\n\ \ plane-spear to beat me... 」"
        cu "「Th' thing is, other things could work. 」"
        cu "「Another thing. The plane you and Young Master are\n\ \ working on? You guys won't fix it.{p}\ \ The mayor's gone and deliberately junked it. 」"
        fn "「Chuukichi-kun, you lie! 」"
        cu "「'm serious. 」"
        fn "「Damn it... there's nothing to do but fight.{p}\ \ But before that, I have to say something. 」"
        fn "「I thought I liked beastmen and dragonmen,\n\ \ but that's not true.{p}\ \ {nw}"
        play sound bom26_b
        show black at hshake 
        extend "I like human girls! 」"    
        fn "「I like things this way.\n\ \ I've turned back into a\n\ \ really normal high schooler. 」"
        cu "「A-aniki, I love you. 」"
        
        #!#[cancelskip]
        
        fn "「We fight, Chuukichi-kun! 」"
        cu "「Come...\n\ \ I'll strike you down,\n\ \ with all my power!! 」"
        
        play music "<from 279>av/audio/free0630.ogg"
            
        fn "{size=+15}「Uoooooooh!!! 」"
        "My Summer vacation is just beginning!"
        "The end."
        
        stop music fadeout 5
        scene black with sdis

        $ event_name = "Tatsuki Bad Ending 001"

        play sound rainstorm
        pause 1.5
    
        "Uncle Shigure's porch"
        
        play music free60
        scene old_house2
        show cu 001 at midleft
        show sg 001 at midright
        with wipe_right
            
        sg "「Good afternoon.{w} Welcome to my home's porch.{p}\ \ It seems you made a mistake, somewhere. 」"
        
        show sg 002 with dis
        
        sg "「That's no good, throwing a used-up roll to the\n\ \ neighbouring stall.{p}\ \ And Chuukichi becoming a giant made so much chaos. 」"
        
        show sg 001 with dis
        
        sg "「And that's the path you chose, even though\n\ \ you knew picking it would cause a stink. 」"
        
        show cu 004 with dis
        
        cu "「Yeah, an' then I became this giant monster...{p}\ \ {nw}"
        show cu 006 with dis
        extend "Hey, why did I become that thing, anyway!? 」"
        sg "「My condolences.{w} Here, drink some tea. 」"
        
        show cu 002 with dis
        
        cu "「Thank you kindly.{p}\ \ ...Whew, that's good.{w} {nw}"
        show cu 006 at hit_right
        extend " {w=.2}\n\ \ No, wait, hey! 」"
        
        show cu 004 with dis
        
        cu "「I wasn't sealed f'r a thousand years,\n\ \ the end was far from chaotic,\n\ \ and you're definitely no sword master. 」"
        sg "「This is a bad end,\n\ \ so you can have a hint. 」"
        
        show cu 005 with dis
        
        cu "「This ain't an end to a weekly manga release.{p}\ \ Besides, Aniki's no zen master. 」"
        
        show sg 002 with dis
        
        sg "「Now, now, don't get so angry.{p}\ \ Didn't you have fun,\n\ \ one way or another? 」"
        
        show cu 010 with dis
        
        cu "「Well, yeah... 」"
        sg "「Hohoho, then everything's all right, no? 」"
        
        show cu 005 with dis
        
        cu "「Really?{w} 　Hmm, it feels like I've been had... 」"
        sg "「Well, let's talk about it inside, then. 」"
        
        show cu 002 with dis
        
        cu "「Oh yeah, let's do that. 」"
        sg "「If anything else happens, we'll talk then. 」"
    
        hide cu with wipe_right
        show sg at center with wipe_right
        
        sg "「Oh no, wait... That's right, I forgot your hint.{p}\ \ Listen, if you see someone in need of help,\n\ \ think about the best thing to do in that situation. 」"
        sg "「Don't make mistakes, and bad things won't happen. 」"
        
        show sg 001 with dis
        
        sg "「Fuhn, well then, goodbye. 」"
        hide sg with sdis
        pause 2
        
        $ persistent.backtrack_name = "tatsuki22_school"
        play music awkward
        call screen backtrack

    
    ###############################################
    label tatsuki22_delivery:
        
        $ renpy.music.set_volume(0.6, 1.5, channel = "music")
        scene black with sdis
        scene shrine with sdis
        show sg 002 at center with dis
        
        sg "「Thanks for your work. 」"
        "That was for fetching Botan-sensei's vegetables.{p}Tatsu-nii and I pulled it back,\nand somehow we made it to the shrine."
        "(Though to be honest,\nTatsu-nii did most of the work...)"
        
        show sg 001 with dis
        
        sg "「You're back later than expected.{p}\ \ What happened? 」"
        
        scene shrine
        show ta 502 at midright
        show sg 001 at midleft
        with wipe_right
        
        ta "「Gahaha, we needed to take a crap. 」"
        "Well, that's not all that happened..."
        sg "「How crude.{p}\ \ Is the Indian millet all right? 」"
        fn "「It's fine, we made sure to wash our hands.{p}\ \ We got a whole lot of other things, too. 」"
        
        show sg 002 with dis
        
        sg "「I see, I see. That's good. 」"
        fn "「I didn't think we'd be getting so much.{p}\ \ That trailer's just packed with stuff.{p}\ \ If not for Tatsu-nii, I'd have never made it back. 」"
        
        show ta 509 with dis
        
        ta "「If it's physical work, leave it to me!!{p}\ \ I can handle it, no sweat!! 」"
        sg "「Hohoho, so full of energy.{p}\ \ Well then, how about I have you\n\ \ start the next task immediately? 」"
        ta "「Eeh? 」"
        
        show sg 001 with dis
        
        sg "「You can still move around, no?{p}\ \ That job was 'no sweat' to you, wasn't it? 」"
        fn "「Eeh? 」"
        sg "「You don't need both of you for this, do you? 」"
        
        show ta 502 with dis
        
        ta "「Aah, I suppose it's true I'd be fine by myself. 」"
        fn "「Well, if you don't need me, I'm going home. 」"
        
        show ta 506 with dis
        
        ta "「Hey, wait a sec-!{w} 　I was kidding, kidding. 」"
        "As I jokingly made to leave,\nTatsu-nii stopped me in a panic."
        
        show ta 508 with dis
        
        ta "「If you aren't here, there's no way the prep work\n\ \ will get done.{p}\ \ C-{w=.2}come on, we'll do whatever you want afterwards. 」"
        fn "「Oh, really? 」"
        fn "「Maybe I'll get you to buy me something expensive. 」"
        
        show sg 002 with dis
        
        sg "「I'd want a big bag of baby castella. 」"
        
        show ta 509 with dis
        
        ta "「Ah, you tricked me, you bastard.{p}\ \ And Uncle, don't put ideas in his head. 」"
        fn "「I'm just joking.{p}\ \ A little payback, for earlier. 」"
        
        show ta 508 with dis
        
        ta "「Geez, you had me completely fooled...{p}\ \ You're some evil fraud genius.{p}\ \ I'll have you arrested, next time! 」"
        sg "「Only someone like you would fall for this.{p}\ \ If you ever go to the city,\n\ \ you'd be a sucker for anything. 」"
        
        scene shrine with wipe_right
        show ni 001 at midright
        show cu 001 at midleft
        with wipe_right
        
        ni "「What are you guys doing? 」"
        
        show cu 005 with dis
        
        cu "「The stage construction's finished. 」"
        "While the three of us were messing around,\nNikaidou and Chuukichi came over to report."
        
        show ni 002 with dis
        
        ni "「You really are hopeless.\n\ \ You aren't any different than usual in public. 」"
    
        show ta 509 at farright behind ni with wipeleft
        
        ta "「What did you say, Nikaidou-!! 」"
    
        show sg 001 at farleft behind cu with wipeleft
        
        sg "「Now, now, calm down, you two.{p}\ \ If the stage is done,\n\ \ we need to get the Taiko drums."
        sg "「It's your turn now, you two. 」"
        
        show ni 003 with dis
        
        ni "「Hmph, it's perfect for a talentless twit like you.{p}\ \ You'd better do your best, now. 」"
        ta "「Heh, better than a guy who's\n\ \ only good with his mouth. 」"
        
        show cu 004 with dis
        
        cu "「Fuhahaha, like 'm not your enemy!! 」"
        
        show ni 005 with dis
        
        ni "「... 」"
        
        show ta 508 with dis
        
        ta "「... 」"
        
        show sg 002 with dis
        
        sg "「Hey now, let's not interrupt these two. 」"
        
        show cu 013 with dis
        
        cu "「'm sorry. I wanted to try sayin' somethin', too. 」"
        "Chuukichi-kun..."
        
        show sg 001 with dis
        
        sg "「Now then, hurry over to the storehouse,\n\ \ Or else we can't have the Bon dance...{p}\ \ Oh? That's strange. 」"
        fn "「Is something wrong? 」"
        sg "「Well, I don't seem to have\n\ \ the key to the storehouse with me.{p}\ \ Where could it be? Did I leave it at home? 」"
        
        show ta 508 with dis
        
        ta "「Uncle, you're finally playing the stupid one? 」"
        sg "「Hm, no.{p}\ \ This is a problem...{p}\ \ I'd be grateful if someone could go check for me. 」"
        ta "「Anyone with time on their hands could do it. 」"
        
        show sg 002 with dis
        
        sg "「Oh, you're going?{p}\ \ The festival begins at 5, so you'd better hurry. 」"
        
        show ta 510 with dis
        
        ta "「Why me? Can't someone else do it? 」"
        
        show ni 003 with dis
        
        ni "「We still have work to do. 」"
        
        show cu 002 with dis
        
        cu "「Tha's right. 」"
        sg "「So there you have it.\n\ \ I'm counting on you. 」"
        fn "「Do your best. 」"
        
        show ta 509 at jump_up
        pause .2
        
        ta "「You're coming too, damn it. 」"
    
        hide ta with wipe_right
        
        "Tatsu-nii grabbed me by the hand and pulled,\ndragging me along with him."
        fn "「I'm being kidnapped!{w} Help! 」"    
        sg "「The Bon dance is at night,\n\ \ but be back before dark. 」"
        sg "「With you two, I didn't think you'd go willingly,\n\ \ so I added some time to when I thought you'd\n\ \ be back, just in case. 」"
        ta "「Shaddup! 」"
        "Tatsu-nii yelled back over\nhis shoulder as he walked."
        
        show sg 001 with dis
        
        sg "「If it's at home,\n\ \ I think it'll be near the entrance! 」"
        ta "「You knew it was there, didn't you, ya geezer! 」"
        sg "「You won't make it,\n\ \ if you keep that pace up!{w} Run!! 」"
        ta "「God damn it! Adults!! 」"
        "I was dragged along with Tatsu-nii,\nas we broke out into a run."
    
        $ event_name = "Dash!"
        
        scene shrine with wipe_right
        pause .2
        scene path with wipe_right
        pause .6
        scene old_house2 with wipe_right
        pause .6
        scene path with wipe_right
        pause .6
        show ta 506 at center with dis
        
        ta "「Haah, haah...{p}\ \ What's this about about it being near the entrance?{p}\ \ It was sitting in the living room. 」"
        fn "「It would have been faster to take a bike... haah. 」"
        
        show ta 505 with dis
        
        ta "「Haah, no way we could've done that.\n\ \ The way was too crowded. 」"
        "*Thump, thump, thump*"
        fn "「You're so slow, Tatsu-nii... 」"
        
        show ta 509 with dis
        
        ta "「Shut uuup!! 」"
    
        hide ta with wipe_right
        scene shrine_court with wipe_right
        show sg 002 at midleft with dis
    
        sg "「Oh, you're back.\n\ \ Faster than I thought, this time. 」"
    
        show ta 506 at midright with wipe_right
        
        ta "「Haah, haah, look, we got the key. 」"
        
        show sg 001 with dis
        
        sg "「Oh, about that, turns out I had a spare on me.{p}\ \ Sorry for putting you through all that. 」"
        fn "「Haah, haah, that can't be... 」"
        sg "「I feel bad asking you this after you just got back,\n\ \ but can you do another thing for me?{p}\ \ You did come back so fast. 」"
        
        show ta 508 with dis
        
        ta "「You're pulling that again!? 」"
    
        $ event_name = "At the Night Stalls"
        
        play music higurasi
        scene path red with sdis
        show ta 508 red at center with dis
        
        ta "「And now it's actually time. 」"
        fn "「Good thing there was still time to change clothes. 」"
        "Shigure had us running errands all afternoon,\nand we were released when it got dark."
        fn "「It seems like all the adults still have work to do.{p}\ \ Administration and management must be hard. 」"
        
        show ta 506 red with dis
        
        ta "「Huh. If I wasn't free to have fun\n\ \ during the festival, I don't think I could do it. 」"
        fn "「Since you work for the Midoriya Group,\n\ \ and you had to help out, does this mean that\n\ \ this year's festival is your last one? 」"
        
        show ta 509 red with dis
        
        ta "「I'd hate that.{p}\ \ Even when I'm an old man, I'll make time for fun.{p}\ \ I'll just do the work at the beginning!! 」"
        fn "「Well, since it is your last, let's go have fun. 」"
        
        show ta 503 red at jump_up
        pause .2
        
        ta "「I'm not letting this be my last. 」"
        
        hide ta with wipe_right
        play music festival_ambience 
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        scene festival_stands with wipeleft
        
        "Tatsu-nii and I walked along,\npast the rows of stalls."
        "The orange light from the stage was glowing\nfaintly in the dark,"
        "while the wind carried the scents of the trees,\nas well as all the other savoury smells from the\nfood stalls."
        "The voices of people enjoying themselves were\nall around us."
        "Even the mountain looked different to usual,\nin the atmosphere of the festival."
        fn "「There are so many people around.\n\ \ Has it always been like this? 」"
        "Normally this place isn't this crowded,\nbut tonight it's completely packed,\nfull of people holding fans and wearing kimonos."
        "As usual for Minasato's festival,\nthere are few humans around.\nMost of the people here are beastmen."
    
        show ta 501 with dis #!#Night time shading
        
        ta "「Hmm, has it?{w} 　I come every year, so I don't know.{p}\ \ People from Kazenari are here, too,\n\ \ so maybe there are more. 」"
        "Does the festival change a bit every time he goes?"
        fn "「Oh, goldfish scooping.{w} That was my specialty.{p}\ \ I caught so many I couldn't keep them,\n\ \ and had to hand them out at school. 」"
        
        show ta 502 with dis
        
        ta "「That black popeyed goldfish\n\ \ at home was one that you gave us. 」"
        fn "「Eh, really? 」"
        
        show ta 501 with dis
        
        ta "「Yeah, they live for a while.{p}\ \ Ma loves it.{p}\ \ I take turns caring for it, too. 」"
        ta "「We call it when it's time for food,\n\ \ and it comes straight away. 」"
        "It's amazing that it's still alive.\nIt's more amazing that Tatsu-nii still cares for it."
        fn "「Wow, I see.{p}\ \ I totally forgot that that goldfish was still alive.{p}\ \ You must really look after it. 」"
        
        show ta 502 with dis
        
        ta "「Hey, that takoyaki looks good.{p}\ \ I'll buy some. 」"
    
        hide ta with wipe_right
        
        "Tatsu-nii hurredly placed an order,\nchanging the subject."
        ta "「Two orders of takoyaki, please. 」"
        om "「Here. 」"
        "Tending the stall was a nicely built old bullman,\nwho was grilling the takoyaki in the cramped space."
        "His large fingers moved unimaginably smoothly,\nas he turned the dumplings over."
        
        show ta 502 with wipe_right
        
        ta "「Sorry to keep you waiting like that.{p}\ \ Come on, let's eat.{p}\ \ These should be good. 」"
        "Tatsu-nii presented me with one of the boxes\nthat he just bought."
        fn "「Is that okay? 」"
        
        show ta 501 with dis
        
        ta "「Didn't I say I'd get you something? 」"
        fn "「Thanks, Tatsu-nii 」"
        
        show ta 508 with dis
        
        ta "「Hehehm it's cool.{p}\ \ Let's find somewhere to sit so we can eat. 」"
        "Tatsu-nii seemed embarrassed,\nputting an arm around my shoulders as he spoke."
        fn "「Yeah. 」"
    
        scene shrine_stairs night with sdis
        
        "We left the stalls,\nand found a place with fewer people around\nso we could sit down."
    
        show ta 502 night with dis
        
        ta "「Tasty. 」"
        
        show ta 507 night with dis
        
        ta "「Crispy on the outside, juicy on the inside...{p}\ \ Just the way takoyaki should be. 」"
        fn "「It's delicious.{p}\ \ Eating outside makes it that much better. 」"
        
        show ta 501 night with dis
        
        ta "「Yeah, this kind of mood really fits the festival.{p}\ \ It's so exciting... do you feel it? 」"
        fn "「Yep, it's always been fun.{p}\ \ I've been to festivals in the city,\n\ \ but they just aren't like this. 」"
        fn "「Minasato's festival is special to me. 」"
        fn "「It kinda sucks that we couldn't\n\ \ come with everyone, though. 」"
        
        show ta 502 night with dis
        
        ta "「I know, right? I wonder where everyone is. 」"
        fn "「We couldn't contact anyone, either. 」"
        
        show ta 501 night with dis
        
        ta "「Well, how about we look for them after eating?{p}\ \ They definitely should've come,\n\ \ so we might be able to find them. 」"
        fn "「All right, let's go look. 」"
    
        hide ta with wipe_right
        scene festival_stands with wipeleft
    
        fn "「It doesn't look like they're here... 」"
    
        show ta 508 at center with wipeleft
        
        ta "「There are so many people here, though. 」"
        fn "「Well, being alone with you isn't bad.{p}\ \ Since it's the festival and all,\n\ \ let's have fun while we look. 」"
        
        show ta 507 with dis
        
        ta "「Y-yeah, let's.{p}\ \ I'm gonna buy some more food. 」"
    
        hide ta with wipe_right
        
        "He really can eat a lot..."
        
        show ta 502 with wipe_right
        
        ta "「Sorry to keep you waiting. 」"
        "Tatsu-nii came back with a nicely barbequed\npiece of corn in his hand."
        
        show ta 507 with dis
        
        ta "「What are you looking at? I'm not giving you this.{p}\ \ You want one, buy it yourself. 」"
        fn "「I get it, I get it. 」"
        "We started walking around again."
        fn "「Whoa, a superball! That brings back memories.{p}\ \ They used to sell these at the candy store. 」"
        
        show ta 502 with dis
        
        ta "「Yakisoba with fried squid, and a candied apple.{p}\ \ Oh, and one fried ring, please! 」"
        fn "「Hey, yo-yo tricks. Maybe I should try them... 」"
        
        show ta 509 with dis
        
        ta "「Look, there's a stall selling chocolate bananas,\n\ \ maybe they have chocolate pineapples, too.{p}\ \ I love those, I'm gonna buy some. 」"
        fn "「Geez, you've done nothing but eat, Tatsu-nii. 」"
        
        show ta 502 with dis
        
        ta "「For me, the best thing at festivals is the food.{p}\ \ This is dessert for me, so give me a break.{p}\ \ Though I'm still up for some sake afterwards. 」"
        fn "「You really are a glutton. 」"
        
        show ta 501 with dis
        
        ta "「One order, please...{w} {nw}"
        show ta 503 with dis
        extend " Wait, there aren't any?{p}\ \ {nw}"
        show ta 504 with dis
        extend "Damn it, there're only chocolate bananas here.{p}\ \ How come there aren't any pineapples here!? 」"
        ta "「Are bananas that good!? 」"
        om "「Sorry, those weren't popular,\n\ \ so I stopped selling them.{p}\ \ Bananas aren't sour, so they sell better. 」"
        
        show ta 505 with dis
        
        ta "「Damn it, why...?{p}\ \ The sweet-and-sourness of it was the best...{p}\ \ There're only bananas... 」"
        om "「Sorry, Kid. Didn't know there was someone who\n\ \ liked them that much.{p}\ \ Maybe I'll bring them back next year... 」"
        om "「Well, if bananas are all right,\n\ \ how about buying one? 」"
        
        show ta 509 with dis
        
        ta "「Get me a big, fat one!! 」"
        fn "「Wait, Tatsu-nii!? 」"
        
        show ta 502 with dis
        
        ta "「What, you want one too? 」"
        fn "「Not that. What were you just saying? 」"
        
        show ta 508 with dis
        
        ta "「There are only bananas here. 」"
        fn "「Weren't there some weird words after that? 」"
        
        show ta 507 with dis
        
        ta "「Oh, I want a big one... 」"
        om "「You guys are funny, I like you.{p}\ \ Here, on the house. 」"
        "The stall vendor handed over two chocolate bananas."
        
        show ta 502 with dis
        
        ta "「Is that okay, Pops? 」"
        om "「We're pros. 」"
        om "「Seeing the customers' happy faces is better\n\ \ than making money. 」"
        
        show ta 501 with dis
        
        ta "「Pops... 」"
        om "「In return, you have to buy from me next year,\n\ \ as I'll have some pineapple ready.{p}\ \ You too, boy. 」"
        fn "「Okay! 」"
        "..."
        
        show ta 502 with dis
        
        ta "「Wow, what a nice guy.{p}\ \ A real man definitely should be generous. 」"
        fn "「Pineapples are sour, so I don't really like... 」"
        
        show ta 509 big at center_big with explosion
        
        ta "「What was that. 」"
        fn "「Whoa, Tatsu-nii.\n\ \ Unless you want a 'big, fat one' of those, too? 」"
        
        show ta 507 big with dis
        
        ta "「Shut it!{w} 　Stop bringing that up already!! 」"
    
        show ka 001 at farright behind ta with dis
        
        ka "「What are you two guys doing...? 」"
        "Kouya looked at us with cold eyes as he walked over."
        
        show ta 510 big with dis
        
        ta "「Kouya, help me out.\n\ \ Hold [fn]'s arms back, would you? 」"
        ka "「Pass... 」"
        
        show ta 502 big with dis
        
        ta "「What, don't be like that. Gahaha! 」"
        fn "「Kouya, it's just you?\n\ \ You aren't with anyone else? 」"   
        ka "「I haven't got time off work,\n\ \ so I'm only swinging by for a little bit.{p}\ \ I haven't met with anyone. 」"
        fn "「Oh, I see. So you're heading back to your work? 」"
    
        show ka 002 with dis
        
        ka "「Yeah. If you see everyone, tell 'em I said hi. 」"
        
        show ta 501 big with dis
        
        ta "「Sure, if it's work, you gotta go.{w} Later, then. 」"
    
        show ka 003 with dis
        
        ka "「Seeya, you two.{w} Play nice. 」"
        
        scene festival_stands
        show ta 501 at center 
        with wipe_right
    
        fn "「He left. 」"
        fn "「Well, what do we do now?\n\ \ Kouya didn't meet with anyone else,\n\ \ and I'm kinda tired of searching. 」"
        
        show ta 502 with dis
        
        ta "「Well, we can't really help it.{p}\ \ Let's go have fun. 」"
        fn "「Yeah, sure. 」"
        "It's a bit sad that no one else is here,\nbut that can't be helped.{p}Being alone with Tatsu-nii isn't bad, anyway."
        
        show ta 501 with dis
        
        ta "「What are you smiling like that for? 」"
        fn "「Oh, uh, nothing. Nothing at all. 」"
        "Festivals are really fun."
        
        stop music fadeout .5
        
        who "「Hey, you over there.\n\ \ Want to play some ring tossing? 」"
        fn "「Ah- 」"
        
        scene festival_stands
        show sg 001 at midleft
        show ta 001 at midright
        play music free22
        
        sg "「How about it, some rign tossing? 」"
        "While we were walking along,\nwe were called over to the ring-tossing\nstall by Shigure-san."
        ta "「Uncle, what are you doing? 」"
        
        show sg 002 with dis
        
        sg "「You understand, if you looked. I'm tossing rings.{p}\ \ I changed places with the stallkeeper here earlier. 」"
        "While Tatsu-nii asked his question awkwardly,\nShigure-san answered back completely naturally."
        fn "「So you aren't peddling sorghum.\n\ \ I totally thought you would be. 」"
        
        show sg 001 with dis
        
        sg "「I just wanted some target practice,\n\ \ but then some adult circumstances happened,\n\ \ and I wound up here. 」"
        
        show ta 502 with dis
        
        ta "「What prizes are there? 」"
        
        show sg 002 with dis
        
        sg "「First place gets a pair of tickets for an\n\ \ extravagant stay at a Japanese inn. 」"
        
        show ta 508 with dis
        
        ta "「That's for Tora's place, isn't it? 」"
        
        show sg 001 with dis
        
        sg "「The second prize is a folding bicycle. 」"
        
        show ta 509 with dis
        
        ta "「Don't ignore me. 」"
        "I could use a folding bike..."
        sg "「Third prize is some fresh-picked vegetables,\n\ \ fourth is a stuffed toy,\n\ \ and fifth is the consolation prize candy. 」"
        
        show ta 508 with dis
        
        ta "「Those vegetables that you're talking about...\n\ \ They're the ones we brought over earlier,\n\ \ aren't they. 」"
        sg "「What is it, you are so full of complaints.\n\ \ To think, this is the next generation. Scary. 」"
        
        show ta 506 with dis
        
        ta "「Hey. 」"
        ta "「Haah, whatever.{w} I'm no match for you, Uncle... 」"
        "Looks like he's a step above Tappei-san after all."
    
        show cu 005 at farright with wipe_right
        
        cu "「Huh? Whatcha guys doin'? 」"
        "As we were talking in front of the ring-toss,\nChuukichi-kun showed up out of nowhere."
        fn "「Hey, Chuukichi-kun, the two of us were just\n\ \ walking around.{w} Helping out took so long,\n\ \ our friends went off to do other things. 」"
        cu "「That so? 」"
        
        show cu 002 with dis
        
        cu "「I was wit' Nikaidou-san up until a while ago,\n\ \ But I lost him.{p}\ \ Can I come along wit' you guys? 」"
        
        show ta 502 with dis
        
        ta "「Sure, let's go have some fun!! 」"
        
        show sg 002 with dis
        
        sg "「So the three of you will be ring tossing? 」"
        
        show ta 501 with dis
        
        ta "「I guess. We may as well. 」"
        
        show sg 001 with dis
        
        sg "「Yes, that's a good attitude to have.{p}\ \ That will be 500 yen for three attempts. 」"
        fn "「Well then, here. 」"
        "I handed over a 500 yen coin to Shigure-san."
        ta "「Here. 」"
        
        show cu 001 with dis
        
        cu "「Thanks. 」"
        
        show sg 002 with dis
        
        sg "「Hmm, perfect. 」"
        fn "「I guess I'll start off, then? 」"
        
        show ta 502 with dis
        
        ta "「It's been a while, so let's make it a contest. 」"
        
        show cu 002 with dis
        
        cu "「Sounds good. 」"
        
        scene festival_stands
        show ta 502 at midleft
        show cu 002 at midright
        with wipe_right
    
        "Whenever everyone was gathered together,\nif either Torahiko or Tatsu-nii were there,"
        "it became tradition for one of them\nto make a contest out of everything."
        "Whenever I hear anything like a challenge,\nI get pumped up myself,\nso I can't refuse this."
        fn "「What kind of contest? 」"
        
        show ta 501 with dis
        
        ta "「Let's see... How about whoever gets\n\ \ the first place prize is the winner?{p}\ \ If no one gets it, then whoever gets closest wins. 」"
        fn "「And if there's a tie for first place? 」"
        
        show ta 502 with dis
        
        ta "「That probably won't happen,\n\ \ but we'll have a tie-breaker if it does. 」"
        
        show cu 013 with dis
        
        cu "「Sounds fun. I'm not gonna lose! 」"
        
        show ta 509 with dis
        
        ta "「What, you think you can win against me?{p}\ \ Sorry, but I'm going to be the victor here. 」"
        fn "「I don't plan on losing either. 」"
        "Everyone's fired up."
        "I'll definitely get the win."
        fn "「So, who's going first? 」"
        
        show cu 001 with dis
        
        cu "「You can go, Aniki. 」"
        
        stop music 
        
        fn "「Huh, I'm up first? 」"
        
        play music festival_ambience fadein 4
        show ta 501 with dis
        
        ta "「I want you to start it off, too. 」"
        fn "「Tch. I'm the one testing it out, aren't I? 」"
    
        show sg 002 at farright behind ta with wipeleft
        
        sg "「You have three tries.\n\ \ Aim carefully. 」"
        "Shigure-san handed me three rings."    
        
    #######################################################
    label tatsuki22_ringtoss:
        
        $ event_name = "At the Night Stands"
        
        "Now, where should I aim?"
        
        menu:
            "A. Aim for first place":
                jump tatsuki22_first
            "B. Aim for an easy shot":
                jump tatsuki22_easy
            "C. Throw all the rings at once!":
                jump tatsuki22_triple
            "D. Toss it at full power!":
                jump tatsuki22_power
            "E. Hit Chuukichi-kun.":
                jump tatsuki22_masochist 
    
    #######################################################
    label tatsuki22_first:

        $ event_name = "Aiming for Victory"
        
        show ta 502 with dis
        
        ta "「Where are you aiming? 」"
        fn "「For the first prize.{p}\ \ Isn't that what everyone is going for?{p}\ \ Since it's a contest, I have to go for the top. 」"
        
        show cu 002 with dis
        
        cu "「Just like you, Aniki. So cool! 」"
        
        show sg 001 with dis
        
        sg "「Now, let's see if it's that simple. 」"
        "The stake for first place is the furthest away,\nso I guess I should aim for the centre,\nbut put a bit more force behind my throw."
        
        play sound metal24
        show ta 502 with dis
        
        ta "「What was thaaat. Aim a bit better. 」"
        "That was a bit too strong,\nso this time I'll try aiming a bit closer."
        
        play sound metal24
        
        "My second ring flew, bounced off the stake,\nand landed on the ground."
        
        show cu 001 with dis
        
        cu "「Aww, so close. 」"
        
        show sg 002 with dis
        
        sg "「Just a little more, and it'd have gone in.\n\ \ Take your time. 」"
        "This is the last one..."
        "However, I got the feel of it last time,\nso this one will definitely make it!!"
        sg "「Fight! 」"
        
        show cu 005 with dis
        
        cu "「You can do it! 」"
        "Relax, breathe,{w=.2} concentrate."
        "How's this!?"
        
        show ta 503 with dis
        
        ta "「Aaachooooooo-!!! 」"
        "!!"
        
        play sound metal24
        show ta 502 with dis
        
        ta "「Gahahahaha, whoops!{p}\ \ I was trying to keep quiet,\n\ \ but then my nose got all itchy. 」"
        
        show cu 002 with dis
        
        cu "「Whoa... 」"
        fn "「I got it in. 」"
        
        show ta 509 with dis
        
        ta "「Whaaat!? 」"
        sg "「Yep, it's in. 」"
        "That sneeze surprised me,\nmaking me throw the ring hard,\nbut because of that, I won."
        fn "「Yes! 」"
        
        show sg 001 with dis
        
        sg "「Amazing, you actually got it\n\ \ onto the first-place stake. 」"
        "I guess that settles it."
        
        show cu 004 with dis
        
        cu "「Anyway, I didn't think Young Master would\n\ \ try pullin' somethin' like that.{p}\ \ I thought you were cooler than that. 」"
        
        show ta 510 with dis
        
        ta "「You're wrong.{p}\ \ Stuff like that happens sometimes. 」"
        sg "「It's great that [fn]-kun got first place,\n\ \ but trying that in a serious contest is unfair.{p}\ \ What would the Master say if he heard about that? 」"
        
        show ta 506 with dis
        
        ta "「I just said it wasn't on purpose.{p}\ \ I wasn't planning on doing something like that. 」"
        sg "「If [fn]-kun had lost,\n\ \ you'd have taken your turn like nothing happened.{p}\ \ The audacity. 」"
        cu "「Disappointin'.{w} Give it up, Midoriya-san. 」"
        
        show ta 505 with dis
        
        ta "「But my nose really was itching...{p}\ \ I couldn't take it... 」"
        sg "「Using that excuse is shameful.\n\ \ You're a disgrace to all men. 」"
        
        show cu at hit_left
        pause .2
        
        cu "「Grow a pair, pansy!!{w} 　Ptuh!!! 」"
        
        show ta 504 with dis
        
        ta "「Why, you two... 」"
        "They're really laying into him,\nand I didn't even mind that much.{p}He looks so pitiful... I guess I should step in."
        fn "「Well, I got first place, so no harm done.{p}\ \ Who's up next? 」"
        
        show sg 002 with dis
        
        sg "「I suppose it can't be helped.\n\ \ We'll let him off the hook for now. 」"
        
        show cu 002 with dis
        
        cu "「If Aniki says so, there's nothing else ya can do. 」"
        
        show ta 508 with dis
        
        ta "「Damn it, ok, I'm a coward.{p}\ \ Happy now?{w} If [fn] hadn't won,\n\ \ it would've been me winning this!! 」"
        "Tatsu-nii pouted,\nand he picked up the rings."
        
        show sg 001 with dis
        
        sg "「If you're that agitated,\n\ \ you won't be able to get them in. 」"
        
        play sound metal24
        show ta 509 at hit_right
        pause .2
        
        ta "「Ha! It's in!!! 」"
        sg "「... 」"
        
        show cu 005 with dis
        
        cu "「Serious!?{w} 　I'm not gonna lose, either!! 」"
        
        play sound metal24
        show cu 002 with dis
        
        cu "「Yes! I got it in!!! 」"
        
        show ta 510 with dis
        
        ta "「Well, aren't you on fire. 」"
        sg "「...Are you monsters? 」"
        
        show ta 509 with dis
        
        ta "「Okay, seems like we all won. 」"
        
        show cu 013 with dis
        
        cu "「Sweet. 」"
        "...Isn't that a bit weird?"
        fn "「Then this isn't really a contest any more... 」"
        
        show ta 502 with dis
        
        ta "「What are you saying!?{p}\ \ Hurry up and be happy about it, now!! 」"
        fn "「Huh-oh, right.{w} Yay! 」"
        
        show cu 007 with dis
        
        cu "「We all did it! 」"
        sg "「It's good that you're all happy,\n\ \ but there's only one first place prize. 」"
        
        show ta 502 with dis
        
        ta "「Festivals are the best!! 」"
        cu "「The best!! 」"
        
        scene festival_stands with sdis
        
        "None of us really wanted a stay at Torahiko's\nthat much, so we gave back the prize."
    
        jump tatsuki22_drums
        
    ##########################################################
    label tatsuki22_easy:

        $ event_name = "Being Methodical"
        
        "If I know Tatsu-nii, he'll be aiming for first.{p}Chuukichi-kun doesn't seem that cautious either,\nso there's a good chance neither will win at all."
        "So if I go for a shot I can make,\nI should be able to win!{p}I shouldn't be the one at the bottom!"
        fn "「All right! 」"
        
        show sg 001 with dis
        
        sg "「He seems confident. 」"
        "..."
        
        show ta 501 with dis
        
        ta "「Come on, what're you gonna\n\ \ do if you win the vegetables? 」"
        
        show cu 002 with dis
        
        cu "「That sucks. 」"
        "Heheheh, first place is impossible,\nbut I should be able to get third place..."
        "Just as planned!!"
        
        show ta 509 with dis
        
        ta "「Well, I'm up next. 」"
        
        play sound metal24
        show ta 506 with dis
        
        ta "「Damn, so close to making first. 」"
        
        show sg 002 with dis
        
        sg "「Well, it happens. 」"
        
        show ta 508 with dis
        
        ta "「A folding bike? We have one at home. 」"
        "Huh?"
        
        show cu 005 with dis
        
        cu "「Well, ain't that good? You got second place. 」"
        sg "「How about it? You did win it,\n\ \ so how about a test ride? 」"
        ta "「I can't ride here, with so many people around. 」"
        "While Tatsu-nii voiced his dissatisfaction,\nhe straddled the bike."
        
        show ta 510 with dis
        
        ta "「How does it look? 」"
        
        show cu 007 with dis
        
        cu "「Pfft, if you rode around on that,\n\ \ ya'd look like one o' those circus bears. 」"
        
        show ta 509 with dis
        
        ta "「Say what. Tell that to Juuichi sometime. 」"
        sg "「If you don't like it,\n\ \ you don't have to take it. 」"
        
        show ta 508 with dis
        
        ta "「This all looks like second-hand stuff.\n\ \ This is all junk you've collected over the years,\n\ \ isn't it, Uncle? 」"
        
        show sg 002 with dis
        
        sg "「Such a narrow-minded young man. 」"    
        "Second place... it's surprising.{p}Well, Chuukichi-kun probably won't win."
        
        show cu 001 with dis
        
        cu "「Guess 'm up, then. 」"
        
        play sound metal24
        show sg at jump_up
        pause .2
        
        sg "「We have a winner!{p}\ \ Here's a pair of tickets to the Ooshima inn! 」"
        
        show cu 002 with dis
        
        cu "「Yeah! I won the contest! 」"
        "So it was Torahiko's place..."
        "Wait, hang on, Chuukichi won!?{p}So I came last?"
        
        show cu 007 with dis
        
        cu "「A-{w=.2}aniki...{w} It's a pair of tickets,{p}\ \ S-{w=.2}so... 」"
        cu "「If it's all right with you,\n\ \ how about we go together,\n\ \ and deepen our friendship...? 」"
        
        show ta 509 with dis
        
        ta "「Bastard, do you realise who you're talking to!? 」"
        
        show cu 006 at hit_right
        
        cu "「Hee!{w} It's a joke, just fooling around! 」"
    
        hide cu with wipe_right
        
        "Tatsu-nii glared at Chuukichi-kun,\nwho was hiding behind Shigure-san."
        sg "「Now, now, it's wrong to bully the weak. 」"
        
        show ta 508 with dis
        
        ta "「Just where are you hiding? 」"
        
        show ta 501 with dis
        
        ta "「If you can't find a use for it, give it to Pa.\n\ \ He'll be happy with the sake, and he'll go with Ma.{p}\ \ They get along well with Torahiko's old man. 」"
        
        show cu 004 at midright with dis
        
        cu "(Stayin' over with Master...)"
        
        show cu 011 at jump_up
        pause .2
        
        cu "「N-no way, that can't work,\n\ \ that'd be too...{p}\ \ And I...{w} {nw}"
        show cu 007 with dis
        extend " B-{w=.2}but,{w=.2} maybe a little... 」"
        
        show sg 002 with dis
        
        sg "「Hohoho! Having an imagination is good,\n\ \ but your thoughts betray you. 」"
        
        show ta 508 with dis
        
        ta "「What are you imagining?{p}\ \ If anyone's going, it's Ma and Pa. 」"
        sg "「Well then, maybe this time the Master will\n\ \ come along when it's time to drink? 」"
        
        show ta 510 with dis
        
        ta "「Don't invite him. 」"
        
        show cu 006 with dis
        
        cu "「Eeehhh!? 」"
        
        show ta 509 with dis
        
        ta "「Listen, you're not going! 」"
        
        show sg 001 with dis
        
        sg "「He's right.{w} More importantly,\n\ \ how about doing a penalty game? 」"
        
        show ta 502 with dis
        
        ta "「Oh yeah, I forgot about that.\n\ \ Everyone who didn't win has to do a penalty game. 」"
        fn "「Huh? You never said anything about this! 」"
        
        show cu 004 with dis
        
        cu "「Aniki, he's kidding again. 」"
        ta "「So, what shall we do? 」"
        
        show sg 002 with dis
        
        sg "「How about second and third place kiss each other? 」"
        "Second place?"
        
        show ta 509 with dis
        
        ta "「I'll take that! 」"
        fn "「Hey, when did this happen? 」"
        
        show ta 507 with dis
        
        ta "「Shut it!{w} 　Pipe down and kiss already. 」"
        fn "「Wait, the victor doesn't get anything.{p}\ \ Is that okay? 」"
        sg "「Well, you can't do anything about a kiss, no? 」"
        
        show cu 007 with dis
        
        cu "「A kiss can't be helped. 」"
        
        show ta 507 big at midleft_big with explosion 
        
        ta "「Now, kiss already... 」"
        "Tatsu-nii caught me,\nand drew me close with both hands.{p}This is exactly like last time..."
        
        show cu 012 big at midright_big with explosion 
    
        cu "「Kiss me, too... 」"
        "Chuukichi-kun drew close, like Tatsu-nii."
        "Why!?"
        fn "「Why?{w} 　Just why? 」"
        "I ran in circles around the stall,\ngetting chased by a big zombie and a small zombie."
        ta "「Kiiiss... 」"
        
        show cu 010 big with dis
        
        cu "「Kiiiss... 」"
        sg "「Well, aren't you guys having fun. 」"
    
        jump tatsuki22_drums
        
    #############################################################
    label tatsuki22_triple:
        
        $ event_name = "What I Desire"
        
        "Well, throwing these normally would be boring."
        fn "「Right then, I'm doing it this way. 」"
        "And so I went to throw all three rings at once."
        
        show ta 508 with dis
        
        ta "「What, you're gonna toss them all together?{p}\ \ You won't get any in like that. 」"
        
        show cu 008 with dis
        
        cu "「That's not gonna work, Aniki.{p}\ \ Surprisin', though. 」"
        "I brandished the rings in the air,\nfaced the stakes,\nthen flung the rings at them."
        
        play sound metal24
        
        "The thrown rings sailed through the air,\nand all arced towards Shigure-san."
        
        play music oo39_cho_ys001
        show sg 002 with dis
        
        sg "「...Do you want me that badly? 」"
        fn "「I'm sorry!{w} 　That was an accident! 」"
        
        show sg 001 with dis
        
        sg "「This is a bit of a problem.\n\ \ It's true that I'm unmarried right now...{p}\ \ But you're young enough to be my grandson... 」"
        fn "「I-I just said I didn't mean to do that! 」"
        
        show sg 002 with dis
        
        sg "「If you want me that much... I can't help it.\n\ \ How about I make myself a special prize?{p}\ \ Will you accept this old grandpa? 」"
        
        show ta 510 with dis
        
        ta "「Isn't that great, [fn]?{p}\ \ According to Pa, Uncle taking off\n\ \ his clothes is something amazing. 」"
        
        show cu 006 with dis
        
        cu "「That's so like you, Aniki,\n\ \ doing somethin' like that. 」"
        fn "「Uh-{w=.2}uh, no- 」"
        sg "「Well, shall we leave at once?{p}\ \ Stay at my home this evening, we'll get takeout.{p}\ \ I'm counting on you two to manage the stall. 」"
        
        show ta 509 with dis
        
        ta "「Yeah, leave it to me! 」"
        
        show cu 002 with dis
        
        cu "「Sure! 」"
        fn "「Hey, why are you two so into this...? 」"
        
        show sg 002 with dis
        
        sg "「Can we hold hands on the way home?{p}\ \ Mine are so wrinkled... I hope you don't mind.{p}\ \ Ahh, it's just as if I've had a grandchild. 」"
        "Shigure-san pulled on my hand, and made to leave.{p}Tatsu-nii and Chuukichi-kun both watched fondly."
        sg "「You're curious, no? 」"
        fn "「Hey, please wait-!! 」"
    
        jump tatsuki22_drums
        
    #######################################################
    label tatsuki22_power:
        
        $ event_name = "Max Power Boy!"
        
        play music oo39_cho_ys001 fadein 5
        
        "I wind up to throw the rings\nlike a highschool Kyuuji Fujikawa."
        fn "「How's this!!! 」"
        
        show sg 001 with dis
        
        sg "「What the!? 」"
        
        show cu 006 with dis
        
        cu "「Anikiii!! 」"
        "All of the rings got caught in Tatsu-nii's horns!!!"
        "They're caught in his horns...{p}Damnit, what does that mean?!"
        
        show ta 508 with dis
        
        ta "「Hm? What's up? 」"
        "Why...{p}What do I do...?"
        
        show ta 501 with dis
        
        ta "「What, did I do something funny? 」"
        "He didn't notice!?"
        "It looks like he's getting used to them..."
        "Even though he doesn't have ears,\nit looks like he's got earrings!!"
        
        show ta 507 with dis
        
        ta "「Man, my head feels kinda heavy.{p}\ \ Maybe I should cut my horns?{p}\ \ It's good for them to be trimmed sometimes... 」"
        fn "「Huh? But they look good on you. 」"
        "Tatsu-nii should've noticed the rings on his horns,\nBut he's gone back to the game!"
        ta "「Yeah, but they get in the way of things. 」"
        fn "「But they've grown so well,\n\ \ cutting them would be such a shame.{p}\ \ Let me feel them. 」"
        "Yes!!{w} 　Just a little more!!"
        
        show sg 002 with dis
        
        sg "「As expected, [fn]-kun.{p}\ \ You have your sights set on different things.{p}\ \ This will certainly net you a special prize. 」"
        
        show ta 501 with dis
        
        ta "「Wait, you already threw them?\n\ \ What'd you get? 」"
        "Crap."
        sg "「What did he get? That would be you. 」"
        
        show ta 507 with dis
        
        ta "「Eh? Me? 」"
        "This is bad, at this rate..."
        sg "「On your head. 」"
        
        show cu 008 with dis
        
        cu "「Oh, what's that? 」"
        
        show ta 508 with dis
        
        ta "「What is it? 」"
        "Thanks, Chuukichi-kun.{p}I knew I could count on you."
        "I can go!!"
        
        show ta 503 at hit_right
        pause .2
        
        ta "「Owowow! What are you doing?{p}\ \ Pulling on my horns...{p}\ \ Oh, is there something stuck in my horns? 」"
        
        pause .2
        
        show fireworks
        play sound fireworks_explosion
        "{size=+25}{cps=0}\ \ \ \ \ \ \ \ \  ＼(＾o＾)／" 
        
        show ta 504 with dis
        
        ta "「Hey, how'd these rings get on my head?\n\ \ What's the meaning of this!? 」"
        fn "「Chuukichi-kun put them there. 」"
        
        show cu 006 with dis
        
        cu "「Eh? 」"
        ta "「You bastaaard! 」"
        
        play sound hit_p07
        show cu 009 at hit_left
        $ chuu_beat += 1
        pause .2
    
        cu "「Oof! 」"
    
        show ta at jump_up
        pause .2
        
        ta "「...Wait, [fn], it was you!!! 」"
        fn "「Eheh. 」"
        
        show ta at jump_up
        pause .2
        
        ta "「Don't you 'eheh' me!! 」"
    
        jump tatsuki22_drums
        
    #######################################################
    label tatsuki22_masochist:
        
        $ event_name = "PUNCH!!!"
            
        fn "{size=+15}「YOU IDIOT!!! 」" 
        "I struck Chuukichi-kun for no reason."
        
        play sound mouse_squeak
        
        if chuu_hit < 5:
            show cu 009 at hit_right
            pause .2
            cu "{size=+15}「Guhaw! 」"
            $ chuu_hit += 1
            $ chuu_beat += 1
        elif chuu_hit < 10:
            show cu 015 at hit_right
            pause .2
            cu "{size=+15}「OH!! 」"
            $ chuu_hit += 1
            $ chuu_beat += 1
        elif chuu_hit < 15:
            show cu 016 at hit_right
            cu "{size=+15}「YES!! 」"
            pause .2
            $ chuu_hit += 1
            $ chuu_beat += 1
        elif chuu_hit < 16:
            show cu 109 at hit_right
            pause .2
            cu "{size=+15}「MAICCHING! 」"
            show cu 107 with dis
            cu "「So painful...!{w=.2}　But... I can feel it!{w=.2}\n\ \ *shiver shiver* 」"
            $ chuu_hit += 1
            $ chuu_beat += 1
        else:
            show cu 109 at hit_right
            cu "「So painful...!{w=.2}　But... I can feel it!{w=.2}\n\ \ *shiver shiver* 」"
            $ chuu_hit += 1
            $ chuu_beat += 1
        
        jump tatsuki22_ringtoss
    
    ####################################################
    label tatsuki22_drums:
        
        $ event_name = "Beat of the Drum"

        play music festival_ambience fadein 2
        scene black with sdis
        scene shrine_court night with dis
        show cu 002 night at midright with dis
        
        cu "「That was awesome! 」"
        fn "「Yeah, it really was. 」"
    
        show ta 508 night at midleft with dis
        
        ta "「Still, never thought it'd end like that. 」"
        "We finished our contest, then hung around,\nand talked about it for a while."
        
        show sg 002 night at farright behind cu with dis
        
        sg "「The festival's only just begun,\n\ \ so go enjoy yourselves. 」"
        fn "「Okay, we won't hold back! 」"
    
        scene shrine_court night
        show ta 501 night at midright
        show cu 001 night at midleft
        with wipe_right
        
        "Today is a special day indeed.{p}\ \ I don't want it to finish yet."
        
        show cu 005 night with dis
        
        cu "「There're gonna be fireworks today, right? 」"
        
        show ta 502 night with dis
        
        ta "「Yeah, they have them this year, too.{p}\ \ They're the festival's final event, after all.{p}\ \ You can't have a festival without fireworks. 」"
        fn "「Everyone will be watching from the bank, huh. 」"
        
        show ta 501 night with dis
        
        ta "「When they start the fireworks,\n\ \ we'll probably run into everyone there. 」"
        fn "「Yeah, you're right. 」"
        "All this talking is nice,\nbut it's making me thirsty.\nMaybe I'll go buy a soda..."
    
        show ni 004 night at farright with wipe_right
        
        ni "「Mayor, there's an emergency.{p}\ \ Oh, you're all here, can you all come with me? 」"
        "Nikaidou-kun walked quickly over to us.{p}He seems more agitated than usual..."
        
        scene shrine_court night with wipe_right
        show sg 001 night with wipe_right
    
        sg "「Hm, what's wrong? 」"
    
        show ni 001 night at farright with wipe_right
        
        ni "「I'll explain while we walk.{p}\ \ Someone is coming to watch over the stand,\n\ \ so there's no problem here. 」"
        sg "「Oh ho, so busy. 」"
    
        scene shrine_court night with wipe_right
        
        "Shigure-san was reluctantly led off by Nikaidou-kun."
        fn "「Let's go too. 」"
    
        show ta 509 night at center with wipe_right
        
        ta "「Sure. 」"
        
        hide ta with wipe_right
        show tp 403 night at center with wipe_right
        
        tp "「ZZZZZ 」"
        
        hide tp with wipe_right
        show ni 005 night at farleft with wipe_right
        
        ni "「I found him like this. 」"
        "Inside the administration tent,\nTappei-san was passed out amongst\nempty beer cans and sake bottles."
    
        hide ni with wipe_right
        show ta 508 night at center with wipeleft
        
        ta "「Pa... 」"
    
        show ni 001 night at farright with wipeleft
        
        ni "「As I just said,\n\ \ the boss seems to have drunk all this by himself.\n\ \ Now he's like this. 」"
    
        show sg 001 night at farleft behind ta with wipe_right
        
        sg "「My, my...{w} Well, we can't use this area, now.\n\ \ Whatever shall we do? 」"
        "Shigure-san went quiet,\nas he stroked his beard."
        
        show ta 506 night with dis
        
        ta "「What do we do? The Bon dance has already started.{p}\ \ Who's gonna play the taiko? 」"
        
        show sg 002 night with dis
        
        sg "「...Well, you're here. 」"
        
        show ta 501 night with dis
        
        ta "「Eh? Me!? 」"
        
        show sg 001 night with dis
        
        sg "「Haven't you been trained in the basics of taiko? 」"
        
        show ta 508 night with dis
        
        ta "「When I was a kid, I'd watch from the side,\n\ \ and follow along with the beats.{p}\ \ I've never actually done it in public before... 」"
        sg "「No matter.{p}\ \ You're the Master's son, there's no need to worry.{p}\ \ Since you two are related, I can leave you to it. 」"
    
        show cu 001 night at midright with wipeleft
        
        cu "「Young Master, haven't you always been around\n\ \ when Master practises every year?{p}\ \ I like your taiko beats. 」"
        
        show ni 003 night with dis
        
        ni "「There's no one else who can do it,\n\ \ so can you make your mind up quickly? 」"
        
        show ta 506 night  with dis
        
        ta "「So I need to do it because I'm the only one left? 」"
        fn "「You've been learning all this time, right?{p}\ \ If it's you, Tatsu-nii, you can do it. 」"
        
        show ta 507 night with dis
        
        ta "「I used to think that too, but... 」"
        fn "「I've never heard you play the taiko,\n\ \ so I want to hear you do it. 」"
        fn "「Also, aren't you aiming to be\n\ \ Japan's best craftsman?{w} Why are you\n\ \ hesitating at a festival, of all places? 」"
        "Tatsu-nii thought for a short while,\nthen answered with a serious expression."
        
        show ta 509 night with dis
        
        ta "「...Got it. I'll do it.{p}\ \ I'll show you my beat judgements. 」"
        
        show sg 002 night with dis
        
        sg "「Hmm... now, can you get to the stage at once? 」"
        
        show ta 501 night with dis
        
        ta "「Right, I'm off. 」"
        
        hide sg
        hide ta 
        with wipe_right
        show ni 001 night with dis
        
        ni "「Now, how about we go watch and learn? 」"
        
        show cu 002 night with dis
        
        cu "「Yeah. 」"
        fn "「Tatsu-nii!! Good luuuck!! 」"
        
        stop music fadeout 1
        scene black with sdis
        scene festival_stands with sdis
        
        "Soon, there was a crowd gathered around the stage."
        "Looking up at Tatsu-nii,\nhe appears to be adjusting the taiko,\nand it looks like everything is going well."
        ta "「Sshhaaa, it's showtime!! 」"
        
        play sound jap_002
        pause .2
        play sound jap_002
        pause .5
        
        ta "「Hah!! 」"
        
        play music festival_drum
        scene shrine_court night
        show su 002 night at center
        show ju 001 night at farleft
        show si 001 night at farright
        with sdis
        
        su "「Oh, the taiko drumming. 」"
        si "「Looks like the Bon dance has begun. 」"
    
        show ju 006 with dis
        
        ju "「Hey, Kodori!{p}\ \ Don't run around like that,\n\ \ or you'll trip and fall. 」"
        
        scene festival_stands
        show to 001 at center
        show so 001 at farleft
        show ky 001 at farright
        with sdis
    
        ta "「Yo-!! 」"
        
        show to 002 with dis
        
        to "「Oh, it's started. 」"
        ky "「Ooshima looks happy. 」"
    
        show so 003 with dis
        
        so "「But festivals do feel great. 」"
    
        scene festival_stands with wipe_right
        show ko 001 at center with wipe_right
        
        ko "「Tatsu-nii would be the happiest about this.\n\ \ Where is he? 」"
        
        scene music_shop
        show ka 001 at center
        with wipe_right
        
        ka "「...Is this the part where it swells up? 」"
    
        scene shrine_court night with sdis
        
        ta "「Ha-!! 」"
        "The sound of Tatsu-nii striking the taiko\nfilled the air.{w} Then, the sound of flutes\nentered everyone's hearts."
        "The music was carried onto the wind,\nwhich spread the sound throughout the village."
    
    ##############################################################
    label tatsuki22_sex():
        if persistent.replay == True:
            $ first = persistent.name_first
            $ last = persistent.name_last
            $ day = 22
        
        $ event_name = "I Love Ya!"

        stop music fadeout 1
        scene black with sdis
        play music festival_ambience
        scene shrine_court night
        show ta 601 night at midright
        show sg 001 night at midleft        
        with wipe_right
        
        ta "「Gahahahaha.{w} Today was the best! 」"
        
        show sg 002 night with dis
        
        sg "「You did very well. 」"
        sg "「With that, it'll be all right\n\ \ to leave it to you next year, too. 」"
        "The Bon dance was just like every other year,\nand Tatsu-nii performed very well on the taiko.\nNow he's finishing up with some sake."
        fn "「Tatsu-nii, your drumming was amazing. 」"
        
        show ta 602 night with dis
        
        ta "「Dumbass, I'm always amazing. 」"
        ta "「I'm good-looking, too! 」"
        "As he said that, he grabbed another bottle of sake."
    
        show ni 002 night at farleft with wipeleft
        
        ni "「Tch... 」"
        ni "「If you're talking about good-looking men,\n\ \ that's something I should be nominated for. 」"
        ni "「At the very least,\n\ \ it shouldn't be your moronic mug... 」"
        
        show ta 604 night with dis
        
        ta "「What was that, bastard!!{p}\ \ Who's got a sauce-face!? 」"
        "He didn't say that..."
        
        show sg 001 night with dis
        
        sg "「Now, now, how about we all calm down?{p}\ \ Today's the festival.\n\ \ You'll anger the gods if you aren't having fun. 」"
        
        show cu 001 night at farright with wipe_right
        
        cu "「Yeah, and in a little bit,\n\ \ the fireworks 'll start up. 」"
        
        show ta 601 night with dis
        
        ta "「Oh, the fireworks?{w} The sky was so quiet,\n\ \ I thought everything was over,\n\ \ and that it was time for sake. 」"
        "Come to think of it,\nwhy haven't the fireworks started yet?"
        "We definitely started at 7,\nso they should have started by now."
        
        show cu 005 night with dis
        
        cu "「Oh Aniki,\n\ \ you're makin' that\n\ \ 'why're fireworks happening' face. 」"
        cu "「Seems like there was a bit of trouble,\n\ \ and the beginnin' got delayed. 」"
        fn "「Oh, so that's how it is.{p}\ \ Well, let's wait until they start, then. 」"
        
        show ni 001 night with dis
        
        ni "「Looks like they've started. 」"
        fn "「Eh? 」"
        
        play sound fireworks_explosion
        show fireworks
        
        "Up in the sky, there was a small glint,\nthen a thunderous roar."
        "Looking up, I see the spread of the\nfireworks sparkle, then fade away."
        
        show sg 002 night with dis
        
        sg "「Hrm, this year was splendid, too. 」"
        fn "「It's so beautiful.\n\ \ The sky's pretty,\n\ \ but fireworks are something else. 」"
        
        show cu 013 night with dis
        
        cu "「But now this year's festival is over... 」"
        
        show ni 005 night with dis
        
        ni "「But if it never ends,\n\ \ wouldn't that be a problem, too? 」"
        
        show cu 008 night with dis
        
        cu "「No way. 」"
        cu "「Nikaidou-san, don't you understand my sufferin'?{p}\ \ Hey Aniki, what do you... whoa, what? Please stop! 」"
        "Tatsu-nii stood in front of Chuukichi-kun,\nwhere he slowly slid his fundoshi off and..."
        
        show ta 608 night with dis
        
        ta "「Woo! Under my stomach it's all smooooth.{p}\ \ Gotta piss, gotta piss. 」"
        sg "「Hohoho, Chuukichi-kun isn't a living toilet,\nyou know. 」"
        
        show cu 006 night at hit_right
        pause .2
        
        cu "（L-{w=.2}living toilet!?）"
        fn "「Hey, Tatsu-nii!!{p}\ \ I'm sorry, Shigure-san,\n\ \ I'm taking Tatsu-nii to the restroom. 」"
        
        show ta 602 night with dis
        
        ta "「Whaat?{w} 　[fn], you gotta piss too?{p}\ \ Pissing together, yeah? 」"
        fn "「Hey, if you get it, then don't take it out here. 」"
    
        show cu at stagger
        
        cu "「Hawawawawa! 」"
        fn "「Okay, off we go. 」"
        
        #[cancelskip]
        scene shrine_court night with wipe_right
        scene black with sdis
        scene shrine_stairs night with wipe_right
    
        fn "「Now, just where is that bathroom? Close by? 」"
        "I pulled Tatsu-nii by the arm,\nand we walked across the dark grounds."
    
        show ta 608 night at center with dis
        
        ta "「What are you planning,\n\ \ taking me to the bathroom like this... 」"
        fn "「Huh? It's not here? 」"
        ta "「3... 2... 1... 」"
        fn "「Huh? What's this countdown for? 」"
        
        show ta 609 night at jump_up
        pause .2
        
        ta "「O!! Fire!!! 」"
        fn "「It can't be!? 」"
    
        hide ta with wipe_right
        
        "Tatsu-nii grabbed me on both sides,\nthen lifted me easily into the air."
        ta "「'Kay, I'm going now. 」"
        fn "「Going where!? 」"
        "Tatsu-nii placed me over his shoulder,\nthen walked over into the middle of a thicket."
        
        scene path night with wipeleft
        show ta 601 night at center with dis
        
        ta "「This spot should be okay. 」"
        "Tatsu-nii finally set me down,\nin a spot that seems to be quite\nsome distance from other people."
        
        show ta 608 night with dis
        
        ta "What are you doing,\n\ \ bringing me over to a place like this? 」"
        "Tatsu-nii shifted around bashfully."
        fn "「Tatsu-nii, you brought me over here. 」"
        
        show ta 602 night with dis
        
        ta "「Gahahahaha!{p}\ \ Well...{w=.2} Maybe. 」"
        ta "「But hey, aren't we alone together, now? 」"
        fn "「Eh-? 」"
        
        show ta 607 big night at center_big with dis
                
        ta "「Hey, it's cool, yeah? 」"
        "Tatsu-nii's eyes glittered as he drew closer."
        fn "「What do you mean, 'cool'? 」"
        
        show ta 602 big night with dis
        
        ta "「Gahahaha, I think you get it. 」"
        
        show ta 610 big night with dis
        
        ta "「I didn't need to piss.\n\ \ Something else's been building up. 」"
        fn "「Geez, you get so perverted when you're drunk.{p}\ \ It's wrong to joke about things like that. 」"
        
        show ta 607 big night with dis
        
        ta "「...I'm not joking. 」"
        
        show ta 609 big night with dis
        
        ta "「There's stuff you can't say when sober. 」"
        
        show ta 608 big night with dis
        
        ta "「[fn]. 」"
        "Tatsu-nii placed his hand on my shoulder,\nthen calmly opened his mouth."
        
        show ta 607 big night with dis
        
        ta "「I love you. 」"
        
        play sound fireworks_explosion
        show fireworks
        
        "After the confession, Tatsu-nii pulled me close,\nand his muzzle brushed against my lips."
        "He smelled a little of sake,\nbut the kiss was more than enough for me.\nThe sound of fireworks faded into the distance."
        fn "「...Ng. 」"
        
        show ta 609 big night with dis
        
        ta "「I don't need to hear an answer. 」"
        ta "「Even if you hate me, I still love you!!{p}\ \ I won't let you go, and if you run,\n\ \ I'll come get you, so get yourself ready!!! 」"
        "He's getting his words all jumbled,\nbut this confession is just like him."
        fn "「Geez, you're so selfish sometimes. 」"
        fn "「It's okay, I won't run.{p}\ \ After all, there's no one who'd run away\n\ \ from someone that they like. 」"
        "Yeah, I've liked him for a while now."
        "I love him."
        
        show ta 610 big night with dis
        
        ta "「Hehehe, then you know what comes next... 」"
        fn "「Yeah. 」"
        "Thinking about the difference in our body size\nmakes me slightly uneasy, but if it's Tatsu-nii,\nI'll be all right."
        "That's how I feel."
        
        show ta 608 big night with dis
        
        ta "「Okay, let's do this, and,{w=.2} uh...{p}\ \ You're,{w=.2} you're...{w=.2} Mine. 」"
        "I wonder what the matter is?\nIt looks like he has something hard to say..."
        ta "「I want you, [fn]... 」"
        "Tatsu-nii wrapped his tail around himself in\nembarrassment as he confessed,\nthen he bashfully looked away."
        fn "「Eeeh-!? 」"
        
        show ta 609 big night at jump_up_big #!#
        pause .2
        
        ta "「I'm not telling you again!!{p}\ \ You're going to drive into me with all you've got!! 」"
        fn "「Y-{w=.2}yeah, I got it.{p}\ \ But what's a good way...? 」"
        
        show ta 608 big night with dis
        
        ta "「Can't you put it in my asshole?{p}\ \ There's a hole underneath my sheath,\n\ \ and it's aching... 」"
        
        scene ev_tatsuki_1 with sdis
        
        "Tatsu-nii's stiff member was hanging out."
        "At its base, I see a slit-shaped crack where the\ncock came out from.\nIt looks like something could fit into that crack."
        ta "「Don't just stand there looking at it.\n\ \ You go in here. 」"
        "Tatsu-nii slipped two fingers in and widened it up."
        "Inside, it was a glossy moist pink.\nA sweet-and-sour odour particular to\ndragonmen hung in the air."
        "I tried slowly inserting a finger.{p}It was hot inside, and resisted my finger's entry,\nclamping down tightly."
        ta "「Haaa...! 」"
        "I started moving my finger in and out,\nand a clear, sticky fluid flowed out."
        fn "「Wow... 」"
        "Using my other hand, I gently pinched Tatsu-nii's\nnipple, and gently caressed it."
        "Moving on from his nipple, I felt his chest,\nhis stomach, and inner thigh,\nenjoying the smoothness of dragonman."
        ta "「Haaa...{w=.2} [fn].{p}\ \ I can't take it any more, put it in... 」"
        "Tatsu-nii shifted his body a little bit.{p}Leaning over, bracing his hands against a nearby tree,\nhe pushed his butt out towards me."
        "My stomach is tying itself into knots."
        "In this position, somehow the size difference between\nus is even more noticeable than usual, and makes me a\nlittle hesitant at what we're about to do."
        fn "「Okay... 」"
        "Tatsu-nii shifted,\nand I caught a glimpse of the penis inside his slit."
        "Tatsu-nii's cock hung out of it,\nsticky precum dripping from its tip."
        fn "「Well, here goes. 」"
        ta "「Be gentle, it's my first time... 」"
        "I gently inserted myself into him, going slowly."
        ta "「Guh-! 」"
        fn "「Are you all right? 」"
        ta "「Aa-{w=.2}amazing, [fn]... 」"
        ta "「It's nothing. I'm all right, so don't stop. 」"
        "Turning his head, his expression was filled with lust,\nwhich stimulated me even more."
        ta "「Gu-{w=.2}kuh, haaa...! 」"
        "It's time for me to move my hips."
        "Just like when I was using a finger earlier,\nI pressed my member in firmly."
        fn "「Tatsu-nii, you're all warm and slippery inside. 」"
        ta "「W-what is... Aah...! 」"
        "I moved myself deeper inside Tatsu-nii,\nfeeling his warmth around me.\nMore precum leaked onto the ground from his slit."
        "Holding onto Tatsu-nii's tail,\nI began to thrust my hips."
        "Tatsu-nii's reaction to this spread through his body,\nand he began moaning with pleasure."
        ta "「O-{w=.2}oooh- 」"
        "I gradually got into a smooth rhythm\nas our movements became more relaxed."
        "I was almost hilting myself in Tatsu-nii now.{p}Our movements were getting faster,\nmaking dry smacking sounds."
        fn "「Haah, haah, Tatsu-nii... 」"
        "My hot member was rubbing inside Tatsu-nii,\nand his slit sucked it in, tightening around it."
        ta "「Kuuuh, that's good. I can't take much more...! 」"
        "The scales all over his disciplined\nbody were covered in sweat."
        "Using my tongue, I began tracing along the\nwell-defined muscles on his lower back."
        "From there, I moved upwards, towards his neck, taking\nin as much of Tatsu-nii as I could."
        ta "「A-ah, that tickles, sto... 」"
        "I ran my hands around his belly,\nholding myself closer to that meaty body.\nI rested my upper body across his back."
        ta "「Fwaaah... Haah...! 」"
        "I drove myself against those\nhips that I was practically glued to."
        "The scent of sweat mixed together with that\nbittersweet smell of dragonman,\nfilling my nose."
        ta "「Oo-{w=.2}ooh, [fn], I-I'm going to...! 」"
        "Tatsu-nii's inner walls convulsed,\nsqueezing my cock tightly."
        fn "「Me too... I... 」"
        ta "「Uoooooh- 」"
        "Tatsu-nii's innards clamped down around me,\nhis shaft pumping out copious amounts of semen\nwhich formed cloudy puddles on the ground. "
        "That was enough to push me over the edge.\nMy body responding in kind,\nI climaxed inside Tatsu-nii."
        ta "「...[fn]. After this, the two of us are together. 」"
        fn "「Yeah... 」"
    
        scene black with sdis
        
        "The two of us lay down on the ground,\nstill half-naked."
        "Up in the night sky,\nthe fireworks continued their brilliant display."
        
        if persistent.replay == True:
            pause 1
            $ renpy.end_replay()
            
        $ persistent.event_tatsuki1 = True
        
        jump end22
    
######################################################
label shun22:

    stop music fadeout 1.5
    play music festival_ambience fadein 1
    $ renpy.music.set_volume(0.8, 0.0, channel = "music")
    
    if meet_gaku == True:
        jump shun22_proceed
    else:
        jump shun22_badend

    ##############################################
    label shun22_proceed:
        
        $ event_name = "Rendezvous"
        
        scene shrine_stairs red with sdis
        
        "When I hear festival music,\nis getting my heart excited for no\nparticular reason part of human nature?"
        "Even though it's the first time I've been to\nMinasato's festival in 5 years,"
        "It's as if there's an illusion that I've come\nhere last summer and the summer before that.{p}That tickles my nostalgia."
        "The sweet fragrance of the burning sugar in\ncotton candy.{w} The voices of playing children.{p}The time for the festival to start is near."
        "Today I'm waiting to meet Shun-kun here."
        "My summer vacation is approaching its final stage\nso I thought I would make some extraordinary\nmemories and invite Shun-kun to the festival."
        "Furthermore, not together with everybody else,{p}but just the two of us."
        "So when I talked to Shun-kun about it,\nhe looked surprised,{w} but gave me a happy\nalbeit confused reply."
        "Hmm, his smile looked a little awkward.{p}I wonder if the other day is still on his mind."
        "The other day when I stayed overnight\nat Shun-kun's house."
        "Or perhaps I should say when I helped him with\nthe lower half of his body?{w} I guided him\nin his first time, so to speak."
        "He was so cute.{p}It felt so light and silky."
        "...yes, I'm reflecting on it.{p}That conversation we had afterwards also went well."
        
        stop music fadeout 1
        scene black with sdis #!#Replace with unique transition labeled うねうね    
        play music pops_003 fadein 2.5
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        pause 2.5
        show su 002 at center with wipe_right
        
        su "「[fn]-san, thank you very much. 」"
        "Although he seemed embarrassed, he smiled.\nWhen he said that, I couldn't stand it\nand wanted to run away."
        "My reason was that I was teaching him what\nto do when down there won't calm down."
        "He was really embarrassed and couldn't talk to\nanybody about it, so I became affectionate and\nguided him.{w} He was happy for that."
        
        show su 007 with wipe_right
        
        su "「...it was because of [fn]-san. 」"
        "He mutters my name with a deep red face."
    
        hide su with wipe_right
        
        "That's right, it was for the healthy growth\nof my important childhood friend, what I taught\nhim was something seriously indispensable!"
        "I decide to think of it that way. For now."
        "Making use of the few opportunities I have,\nI slowly and carefuly savored\nsomething I rarely get to eat."
        "Then, we engaged in an act known to lovers,\nand I guided him to the climax."
        
        stop music fadeout 2.5
        pause 2.5
        scene shrine_stairs red with sdis #!#Need to figure out transition うねうね
        play music festival_ambience fadein 1
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        
        "That said, inside me there's still a lingering\nfeeling that I did something I shouldn't have."
        "That's why I hope Shun-kun can fully\nenjoy himself at today's festival."
        "Target shooting, masks, cotton candy,\nand baked rice crackers.\nWe'll go around the food stalls together."
        "Making his eyes shine, going around twice\nwith my childhood friend standing on tip-toe\nwhile ransacking the night fair."
        "That would be lovely."
        "After a while, I'll ask if he wants to take a\nbreak because he's tired.{w} I'll look for a place\nto sit together with pure-hearted Shun-kun."
        "Then I'll suddenly want to eat a baby sponge cake."
        "I'll wait at our spot while Shun-kun looks for a\nfood stall.{w} He'll bring a paper bag containing\nother sweets as well.{w} Then I'll gently ask,"
        fn "「What was the stall's name? 」"
        "Then his head will go down in embarrassment,"
        "{size=-10}「F-Fried Penis... 」" 
        "He'll answer in a voice I won't be able to hear."
        "Because of that, I'll go around and check whether\nor not it corresponds to any of the stalls opened\nin the last 30 minutes, and also the decided route."
        "Then, I'll be sure not to forget to buy\nchocolate covered bananas, frankfurters,\nand other long and thick foods."
        "...my love might be distorted."
        
        scene black with sdis

        $ event_name = "To Some Other Place"

        scene shrine_stairs red with sdis
        
        "Even though I've been standing around,\nShun-kun hasn't arrived.{p}Our meeting time was 3 minutes ago."
        "Hmm, so far he has never shown up at\nthe last minute until now."
    
        show su 003 red at center 
        pause .01
        show su at briefzoom
        
        su "「[fn]-san! 」"
        fn "「Shun-kun!{w} Good evening. Isn't this rare?{p}\ \ You're usually earlier than this. 」"
        
        show su 016 red with dis
        
        su "「I'm sorry, d-did I keep you waiting...? 」"
        fn "「You don't need to apologize,\n\ \ I just got here too.{w} It's not usually\n\ \ like this though, so I was surprised. 」"
        su "「Uu... 」"
        fn "「Now then, should we get going? 」"
        "I turn towards the shrine and start walking,{p}but Shun-kun doesn't move his feet."
        
        show su 004 red with dis
        
        su "「Uh, um, [fn]-san... 」"
        fn "「Hm? What's wrong? 」"
        "He keeps fidgeting, and his tail swings restlessly."
        su "「Um, I want to go over there for a little bit... 」"
        "Then he indicates with a sidelong glance,\nin the opposite direction of the shrine."
        fn "「Huh?{w} Why?{p}\ \ We came here for the festival today, right? 」"
        
        show su 010 red at jump_up
        pause .2
        
        "*Biku*"
        su "「I-I'm sorry... 」"
        "He stiffens up as if he had been scolded.{p}Doesn't it seems like something is bothering him?"
        fn "「Oh, I see.{p}\ \ Shun-kun, are you perhaps... 」"
        
        show su 015 red with dis
        
        su "「...? 」"
        fn "「Worrying about not having a yukata? 」"
        "He's in his familiar blue and white hoodie."
        "Everybody around here is wearing festival\nclothing, so he must be hesitant to get\ninto a crowd of people dressed the way he is."
        
        show su 004 red with dis
        
        su "「Y-yeah... 」"
        fn "「You shouldn't worry about something like that. 」"
        fn "「You're cute even in your usual outfit,\n\ \ so why don't we go have fun at the festival\n\ \ we've been waiting so long for, hm? 」"
        "I place both my hands on his tiny shoulders and\nlook down at him.{w} I would say \"Let's go together\",\nbut Shun-kun doesn't make eye contact."
    
        show su 013 red big at center_big with dis
        
        su "「Hauhau... U-um, I can't. 」"
        fn "「Do you still want a yukata? 」"
        su "「That's not it, um,{p}\ \ {cps=10}{size=-10}I don't want to go to the festival. 」"
        "Towards the end was in a faint voice that\nI couldn't hear very well.{p}He bows his head down sadly."
        "His small body that would probably\nbe swallowed up by the hustle and bustle\nechoing from the inner part of the shrine grounds,"
        "tightly grasps the hem of his shirt\nto endure something."
        fn "「Hm... Shun-kun?{p}\ \ Is something wrong?{p}\ \ Why are you making that painful expression? 」"
        "I bend my knees on the spot and continue\ntalking while looking up a little.{p}He's still acting strange."
        su "「I'm sorry, [fn]-san...{p}\ \ You've been looking forward to the festival,\n\ \ but I-I... 」"
        "His eyes begin to moisten.{p}For now, it would be good to move away from here."
        fn "「I understand.\n\ \ Anyways, we should go over there, right? 」"
        su "「I'm sorry, I'm sorry... 」"
        
        stop music fadeout 1
        pause 1
        scene black with wipeleft  
  
        $ event_name = "In the Opposite Direction"

        play sound night_insects loop fadein 1
        scene path red with wipeleft
        
        "We go off the path that leads to the shrine,\nto where even the light of the paper\nlanterns doesn't reach."
        "The sun is setting in Minasato at the usual time."
    
        show su 013 red at center with wipe_right
        
        "Shun-kun is still looking down.{p}I can only feel his weak grasp in my palm."
        "We push forward silently, and the festival music\ngradually disappears behind us."
        "On the other hand, even the insects\nare having a party this evening."
        fn "「Are you not feeling well? 」"
        su "「I'm okay... 」"
        "That tone of voice doesn't seem at all okay."
        "Rather than ask him why he\ndoesn't want to go to the festival,\nthe first thing I'll do is calm him down."
        fn "「Here. 」"
        "I sit down on one knee\nand turn my back to him."
        
        show su 015 red with dis
        
        su "「? 」"
        fn "「I'll carry you on my back. 」"
        
        show su 005 red with dis
        
        su "「I-I'm not a kid... 」"
        fn "「I just wanted to carry you all of a sudden,\n\ \ it's no more than that. 」"
        fn "「Nobody's watching too, right? 」"
        
        show su 010 red with dis
        
        su "「...no. 」"
    
        hide su with wipe_down_slow
        
        "He gets on relatively obediently."
        "I'm strangely conscious of the slenderness\nof his arms around my neck.{p}I attach both hands to his butt and lift up."
        "When we're this close together,\nI want him to be as comfortable as possible."
        fn "「How is it? {w=.2}Is it hurting your legs? 」"
        su "「No... 」"
        fn "「You can cry too, okay? 」"
        "I say no more and start walking.{p}A short time later, he squeezes his arms.\nI can hear him sniffling and weeping."
        "Because Shun-kun says nothing,{p}I don't say anything either."
        "There's just the sound of his crying,\nthe insects, and the distant festival."
        "Without passing by anybody,{w} we arrive at the river."
        
        stop sound fadeout 1
        scene river night with wipeleft
        play sound water03 loop fadein 1
        
        "The flow of the cool water alleviates the heated air."
        fn "「Is around here okay? 」"
        su "「Yes... 」"
        "It seems he has already calmed down considerably.{p}Oomph.{w} I gently set my childhood friend down."
    
        show su 012 night at center with wipe_up_slow
        
        fn "「When you want to cry,\n\ \ it's better to do it comfortably, isn't it? 」"
        su "「[fn]-san, sorry... I got your shirt wet. 」"
        "Since earlier, Shun-kun has been apologizing.{p}Now that he mentions it, it is a\nbit damp around my shoulders."
        "We sit side-by-side."
        fn "「That's enough of that. More importantly,\n\ \ your face is all messy. 」"
        
        show su 016 night with dis
        
        "I take out a handkerchief and wipe away\nthe traces of tears."
        "His fur doesn't return to its disordered state,\nbut there nothing I can do about that.{p}I guess it'll be better if it stays wet."
        
        show su 002 night with dis
        
        su "「Thank you... woof. 」"
        "His slightly strained smile is sad."
        fn "「Did you not want to go to the festival with me? 」"
        "I say aloud a question I've been\nthinking since a little while ago."
        "After all, what we did that night has been done."
        "Even if I make some kind of excuse or no matter\nhow much I talk about it, there's a very high\nchance he could be afraid and changed his mind."
        
        show su 005 night with dis
        
        su "「Th-that's not it!{p}\ \ I was really happy to go with you!{p}\ \ But- but... 」"
        
        show su 010 night with dis
        
        fn "「But? 」"
        "Shun-kun slowly tells me the whole story."
        
        stop sound fadeout 1
        
        $ event_name = "The Kodori family's ceremony"
        
        play music melodious01
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        
        su "「...It's about the other day.\n\ \ Iwao-sama told me about the Kodori family's\n\ \ role in the festival. The role of a miko. 」"
        fn "「The role of a miko? 」"
        su "「Yes.{w} For generations the Kodori have served\n\ \ as the miko for the festival.{p}\ \ This year it's my turn. 」"
        su "「But then I wouldn't have been able to go\n\ \ to the festival with you.{p}\ \ Even though I was looking forward to it. 」"
        su "「That's why... I said I didn't want to. 」"
        su "「...then Iwao-sama got very angry at me. 」"
        su "「\"You don't understand the importance\n\ \ of the ceremony. Only thinking and acting\n\ \ for yourself, it's absurd,\" he said. 」"
        fn "「Really...? 」"
        su "「After that he told me that I wasn't even able to\n\ \ help with the preparations for the Bon Festival.{p}\ \ He said I'm a shameful heir to the Kodori family. 」"
        fn "「You were exhausted at the time,\n\ \ it's not your fault. 」"
        
        show su 012 night with dis
        
        su "「It is my fault.{p}\ \ I'm a burden for you too.{p}\ \ I only think of myself... 」"
        "Large tears drop like rain, and stream down\nhis half-dry cheeks. I once again present\nto him my handkerchief from earlier."
        fn "「I don't think you're a burden.{p}\ \ It was really fun when I stayed\n\ \ overnight with you. 」"
        "There are no lies in my heart."
        su "「Thank you... *sniffle* 」"
        
        show su 010 night with dis
        
        su "「To smooth things over with Iwao-sama and I,\n\ \ a relative came between us.{p}\ \ He said \"Do I have to be the miko?\" 」"
        su "「...then Iwao-sama got extremely angry. 」"
        fn "「Huh? {w=.2}Why? 」"
        su "「...I think Gaku-san popped into his head.{p}\ \ Before the ceremony, he suddenly\n\ \ appeared in Minasato. 」"
        su "「Iwao-sama doesn't recognize Gaku-san as a Kodori. 」"
        su "「Then he said, {w=.2}\"Don't talk about him!\" {w=.2}\n\ \ After that he got worked up.{p}\ \ He was angry for a while. 」"
        su "「My uncle and aunt somehow managed\n\ \ to calm him down. 」"
        su "「They told me, \"Please go home for now\",\n\ \ and I went back to my house. 」"
        su "「After that... I got a call from Gaku-san.{p}\ \ He said he's going to be the miko this time. 」"
        su "「So I can go and play with you\n\ \ without having to worry about it. 」"
        su "「He said I should enjoy myself because I worked so\n\ \ hard around the time of the Bon Festival.{w} But... 」"
        fn "「But? 」"
        su "「Gaku-san also hates Iwao-sama. 」"
        fn "「What? 」"
        su "「He also hates our old-fashioned customs and the\n\ \ way of life for the heir to the Kodori family.{p}\ \ That's why Gaku-san left Minasato. 」"
        su "「I think he's putting up with all that\n\ \ and taking over for me as this year's miko. 」"
        su "「So when I thought about that,\n\ \ I'm nothing but trouble to Gaku-san\n\ \ and everybody else... {nw}"
        show su 012 night with dis
        extend "I think... 」"
        "I couldn't hear that last part.{p}Tears are soaking his face."
        su "「*sniffle*...{w} Then I went to the shrine,\n\ \ but it got really painful.{p}\ \ You were waiting for me, but... 」"
        su "「...even though you've been waiting\n\ \ for this festival...{p}\ \ I'm sorry, [fn]-san. 」"
        su "「It's your first time at the festival in 5 years,\n\ \ but... things ended up this way. 」"
        fn "「I'm okay with that.\n\ \ More importantly, don't cry anymore.{p}\ \ I know it's not your fault. 」"
        su "「Uuun, it's all my fault. 」"
        su "「I made Iwao-sama angry, I'm troubling Gaku-san,\n\ \ and I ruined your festival. 」"
        su "「I was supposed to be the one in the ceremony. 」"
        
        show su 013 night at shivering
        pause .2
        
        "He squeezes out no more words than that,\ngrasps his knees, and begins to shake and tremble."
        "He really was looking forward\nto going to the festival with me.{p}So, he tried to go one way or another."
        "It all backfired and didn't turn out well for him."
    
        hide su with wipe_right

        su "「...[fn]-san... 」"
        "I hold Shun-kun's huddled up\nbody close from the side.{p}I don't want to make him sad anymore."
        "Not wanting him to shed any more tears,\nI increase the strength in my arms."
        "Then..."
        
        stop music fadeout 2
        pause 2
        
        $ event_name = "A Pair Watching Fireworks"
        
        play sound fireworks_explosion
        show fireworks 
        
        fn "「The fireworks are beautiful, aren't they? 」"
        su "「...Y-yeah... 」"
        fn "「To be able to watch the fireworks with you,{p}\ \ that alone makes me happy. 」"
        su "「Uu... 」"
        fn "「Even though eating stuff at a stall\n\ \ and making a lot of noise is fun,{p}\ \ being together with you like this is the best. 」"
        su "「{cps=5}Hic...{cps=40}\n\ \ Uwaaaaan!{p}\ \ [fn]-san! 」"
        
        pause 1
        play music free21
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        
        "I catch Shun-kun, who jumped at me head-on.{p}The body heat I felt from behind\nearlier is now up front."
    
        show su 014 big night at center_big with dis
        
        su "「I thought we wouldn't be able to be together!{p}\ \ I've been thinking that I could see you again\n\ \ after 5 years... only for this summer. 」"
        su "「But I couldn't see you during those 5 years. 」"
        su "「So... 」"
        fn "「Thank you. 」"
        su "「! 」"
        fn "「I'm really happy you want to be with me.{p}\ \ I feel the same way. 」"
    
        show su 018 big night with dis
        
        su "「Hau...{w=.2} [fn]-saaan. 」"
        fn "「There will be a festival next year,\n\ \ and the year after that.{p}\ \ I'll come back to see you. 」"
        fn "「Then we'll meet up again, right? 」"
        su "「Fuwaaan...{w=.2} hic, hic...{w=.2} Yeah... 」"
        fn "「Target shooting, masks, cotton candy,\n\ \ and baked rice crackers.{p}\ \ I like stuff like katanuki too. 」"
        fn "「And after that, peppermint flutes.{p}\ \ Oh, but I'm not very good at the Bon dance,\n\ \ so you'll have to teach me. 」"
    
        hide fireworks
        show su 014 big night with dis
        
        su "「Yeah...{w=.2} I will...{w=.2}\n\ \ I want to do that with you, *sniffle* 」"
        fn "「Next year, the year after that...{w=.2}\n\ \ and this summer too.{p}\ \ Let's do more together, okay? 」"
        su "「...Hic,{w=.2} okay,{w=.2} [fn]-san... 」"
        
        #[msgoff]
        play sound fireworks_explosion
        show fireworks 
        
        "The fireworks I haven't seen in Minasato\nfor 5 years were beautiful, and I got\nto watch them with Shun-kun."
        "For me, the time I got to spend with\nhim is irreplaceable."
        "I don't want to make him cry anymore."
    
        jump end22
        
    ######################################################################
    label shun22_badend:
        
        $ event_name = "3 Tails"
        
        scene shrine_court red with sdis
        play music festival_ambience fadein 1
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")        
        
        fn "「Heeey! 」"
        "I was walking around Minasato shrine's grounds,\nlured in by the festival music."
        "When I call out to those 3 familiar tails,\n6 ears twitch and they all turn around together."
        
        show so 001 red at farright    
        show si 001 red at farleft
        show su 001 red at center 
        with wipe_right
        
        "Aahn.{p}The sight of them looking back is lovely.{p}I stare at them for a while."
        
        show so 005 red with dis
        
        so "「A-are you okay? 」"
        "Yeah, I'm fine."
        "Because Soutarou-kun has an image that says\nhe's always energetically running around\nin the sunlight,"
        "His tail swinging around in the light of dusk\nis an immoral and tantalizing gesture."
        
        show si 004 red with dis
        
        si "「When you want to call out to us,\n\ \ you grin without a greeting.{p}\ \ You're thinking of something devious, are you? 」"
        "I already am.{p}When I see the black scruff and collarbone\npeeking out from Shin-kun's clothes,"
        "An impulse that is likely to make me take a wrong\nstep is carelessly shown on my face."
        
        show su 002 red with dis
        
        su "「[fn]-san, good evening! 」"
        
        show su 001 red with dis
        
        "Shun-kun plays with the strings of his hood\nto find an outlet for his excitement."
        "He probably can't help but look forward\nto the festival."
        "I'm getting the feeling that I'll\nteach him other fun things with\ngreat detail and care."
        
        show si 001 red 
        show su tailwag 01 red 
        show so 001 red 
        with dis
        
        "Surrounded by a combination\nof such short beastmen, I,"
        "[fn] [ln],\nam experiencing an enjoyment that doesn't seem\nlike something of this world. "
        "Ahh summer, summer in Minasato.{p}I've come a long way for this moment."
        "Let's be thankful for the invention\nof the postal system and the wheel."
        fn "「First of all I want to go buy a baby sponge\n\ \ cake right now! Let's go! 」"
        
        show si 004 red with dis
        
        si "「Is food what you think about\n\ \ when you open your mouth?\n\ \ fn, you have no hint of emotion, do you? 」"
        
        show so 005 red with dis
        
        so "「I'll eat just a little sweets for dinner.\n\ \ For today. 」"
        
        show su 004 red with dis
        
        su "「There's somewhere we have to go.\n\ \ Even though you invited us, I'm sorry. 」"
        "Huh?"
        fn "「Shun-kun, do you have some business to take care of?\n\ \ You didn't come here to play this evening? 」"
        
        show su 002 red with dis
        
        su "「Yes, I'm appearing in the festival's ceremony. 」"
        "This is the first time I've heard that.{p}He notices my blank stare and hurriedly adds,"
        
        show su 015 red with dis
        
        su "「Err,{nw}"
        show su 003 red with dis
        extend "\n\ \ looks like I forgot to tell you about that. 」"
        
        stop music fadeout 1
        pause 1    
        play sound shock1
        play music free0428
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        
        "I've already been in Minasato for a little\nover 20 days, and yet I haven't been informed\nof my childhood friend's big moment?"
        "That said, I'm not waiting to meet somebody\nor anything like that either, I just came here\nfor the summer festival."
        "Does something like this mean\nthat our relationship has weakened?"
        fn "「Do both of you have something to do\n\ \ with Shun-kun? 」"
        
        show so 003 red with dis
        
        so "「Yeah, I'm goin' to help him. 」"
        
        show si 001 red with dis
        
        si "「I am as well. 」"
        fn "「Aaaaaaaaaaaah! 」"
        "Our encounter from earlier wasn't fate!?{p}But I thought the 4 of us would thoroughly enjoy\nthe night fair and Bon dance!"
        
        show su 004 red with dis
        
        su "「Sorry, [fn]-san.{p}\ \ {nw}"
        show su 005 red with dis
        "This is an important ceremony.\nI must do my best. 」"
        
        show so 001 red with dis
        
        so "「Two other people of the same height\n\ \ are needed for it. 」"
        "It's going to be that kind of ceremony, isn't it?"
        "With the three of them tangled together,\na difference in height would cause problems,\nwouldn't it? Aah, fantasies."
        "I plop down, heartbroken."
        
        show si 003 red with dis
        
        si "「Hey, don't collapse, stand up. 」"
        "He just talks, doesn't lend me a hand,\nand puts up with my behavior.{p}I feebly get up."
        
        show si 001 red with dis
        
        si "「It's almost time, isn't it? 」"
        
        hide si with dis
        pause .5
        
        so "「That's right, see you later [fn]-san,\n\ \ some other time. 」"
        
        hide so with dis    
        show su 002 red with dis
        
        su "「See you tomorrow! 」"
        
        hide su with dis
        
        "While I stand there stunned,\nthe 3 tails go away.{p}It's too late for me to shed tears."
        "When I chase after Shun-kun... er, rather\nact like a groupie, he doesn't listen to a word\nI say even though there was no need to!"
        
        stop music fadeout 1
        pause 1
        scene black with sdis
        
        $ renpy.full_restart()
        
        
######################################################
label kouya22:
    
    $ event_name = "Crossing of Fate--Front to Back"

    play music melodious08
    scene bedroom with dis
    show ka 002 at center with dis
    
    
    ka "「All right,{w=.2} I'm heading out. 」"
    "The following day, the two of us\nwere standing in the entryway\njust like yesterday."
    "It was close to noon.{p}In fact, it's 12 on the dot right now."
    "In the sky there were clouds out,\nand it was humid and unpleasant."
    fn "「Okay,{w=.2} take care. 」"
    ka "「Yeah,{w=.2}\nI'm counting on you to look after the place. 」"

    hide ka with dis
    pause .4
    play sound door_close
    
    "With a faint smile,\nKouya disappeared out the door.{p}It was the same as yesterday.{w} And then I was alone."
    "I went back into the living room and laid down.{p}Today, I've decided to sit and wait patiently."
    "Kouya went out to go see Kazumi.{p}It's his response to yesterday's letter."
    "I wonder just what kind of talk it's going to be?"
    "It has nothing to do with me,{w=.2}\nbut I'm still fidgety about it."
    "If I'm just guessing,\nI can think of a lot of things."
    "But whichever it turns out to be,\nI wonder how it'll end up?{p}I still don't know."
    "Maybe it's because of how awful the weather is.{p}For some reason, I'm feeling really anxious."
    "And more than anything..."
    fn "「Kouya... 」"
    "I was worried about Kouya."
    "In my chest, things felt so noisy.{p}What could Kouya be feeling right now?{p}I can't even imagine that."
    "The only thing I do understand\nis that it won't be all that quiet.{p}Maybe that's why it's so painful for me to just wait."
    "But that's my role in this right now.{p}When Kouya comes back,{w=.2}\nI'll say 'welcome back' to him."
    "It's just a small thing,\nbut it's very important."
    "For that reason, I'll stay here.{p}Those were my feelings on things."
    fn "「Yeah, that's it. 」"
    "When I think like that, I calm down a bit."
    "As I laid on the floor,\nI turned to look out the window."
    "The sun still wasn't going\nto show its face anytime soon."
    "But even in that oppressive sky,{w=.2}\nI could see it changing, just for a moment."
    
    stop music fadeout 3
    scene black with sdis 
   
    $ event_name = "Crossing of Fate--Left to Right"

    play music cicada01 fadein 3
    scene kouya_house_out with sdis
    
    ka "「Whew... 」"
    "Maybe it's because of the clouds,\nbut it's strangely humid outside."
    "It was uncomfortable, as if sweat\nwas curling all around me.{p}I sighed, though there wasn't a reason for it."
    "When I raised my head,{w=.2} I could see\nthe color of lead covering the whole sky.{p}Seems like it'll rain soon."
    "Underneath that sky, there I was.{p}In front of a single house."
    "I know this house well.{p}Of course I should.{p}...This is my parents' house."
    "I guess this is why I sighed.{p}If I had my way, I wouldn't be anywhere\nnear this house."
    "The house I ran away from,{w=.2}\nafter I fought with my father."
    "I don't regret anything I've done.{p}However, I don't know if it was the right thing."
    "So I never come near here."
    "But even if I don't regret it,{w=.2}\nthat might be a mistake in itself.{p}Somewhere, I was thinking that."
    "If I came here,{w=.2}\nI was afraid that feeling would intensify."
    "Actually, I'm also afraid right now."
    "However, I'm here of my own free will.\nSo I have to keep going."
    ka "「... 」"
    "I tread on the ground until I was\nin front of the door.\nThen I extended my hand to the doorknob,"
    "Warm from the summer air.\nAt that point, my heartbeats reached\nall the way to my ears."
    "It feels a little bit like stage fright.{p}However, there's nothing to play."
    "I put my strength into my arm, and opened the door."
    
    play sound door04
    
    "What opened out in front of me\nwas nostalgic scenery."
    "Things haven't changed much\nsince the time I was still here.{p}It feels like an illusion where time had stopped."
    "And over there was the person who was waiting for me."
    kz "「...Welcome home. 」"
    
    stop music fadeout 3
    scene black with sdis
    
    $ event_name = "Talks of Various Things"

    scene kouya_house_in with sdis    
    play music piano4_001
    
    kz "「When the doorknob turns and the door opens,\n\ \ it makes a sound, doesn't it?{p}\ \ That's why I thought I would wait here. 」"
    kz "「It truly has been a long time.{w=.2}\n\ \ You've come home. 」"
    "We sat facing each other,\nacross the table in the living room."
    "Was she happy that I came back?{w=.2}\nShe was smiling the whole time."
    ka "「Yeah, I have. 」"
    "However, I couldn't look her in the eye."
    "I had feelings inside my heart\nI didn't really understand,{w=.2}\nand they stopped me from raising my head."
    kz "「It's been about a year since you've left.{p}\ \ Somehow, it feels like its been ages. 」"
    kz "「...For a while,{w=.2} I thought I'd\n\ \ never be able to talk to you again.{p}\ \ But now I'm happy, you've come today. 」"
    ka "「...I'm sorry,{p}\ \ for not keeping in contact. 」"
    kz "「It's okay.{p}\ \ Because now I know that you're doing well. 」"
    kz "「How are things?{w} Is your band doing okay?{p}\ \ I've heard that there will be a contest soon. 」"
    ka "「Well enough.{w} Everyone's working hard. 」"
    kz "「Next week, was it?{w} If you come out on top,\n\ \ you might be able to make your debut.{p}\ \ Do your best,{w=.2} I'll be cheering you on. 」"
    "Mom kept making small talk\nas if to fill in on all the lost time."
    "But...{w=.2} this is wrong."
    "Was that why she called me over?{p}It couldn't be just that.{p}There has to be something else."
    "If it was the case,{w=.2} there'd be no reason for her\nto bring a letter to my door all by herself."
    "And if that weren't the case,\nthis wouldn't have happened."
    "She must have a mountain of questions.{p}However,{w=.2} that shouldn't be it right now."
    "That...{w=.2} That can come later."
    ka "「...Did... 」"
    kz "「Eh? 」"
    ka "「Did you call me over to ask me about that?{p}\ \ Isn't there...{w=.2} something else you wanted to discuss? 」"
    "When I pointed it out,\nshe seemed to hold her breath.{p}I could see a bit of sadness through that smile."
    ka "「...Sorry.{p}\ \ That wasn't a good way of putting things. 」"
    kz "「No, it's okay.{p}\ \ What you said is true, after all. 」"
    "She suddenly looked serious."
    "Here on out is the main issue.{p}I think I know what it's about, though."
    kz "「Kouya.{w} It's about time you came home. 」"
    ka "「{cps=5}. . . 」"
    "I thought it'd be that."
    kz "「It's been so long since you've left.{p}\ \ Isn't it all right to return now? 」"
    ka "「But,{w=.2} I... 」"
    kz "「Let me guess,{w=.2} it's too awkward? 」"
    "I silently nodded my head."
    "Now,{w=.2} it's too late for me to come back.{p}And besides..."
    kz "「Is this about your father? 」"
    "I nodded one more time."
    "I fought with my dad.{p}That's why I left."
    "I couldn't ask about anything,{w=.2}\nand right now, I can't come home."
    kz "「...Kouya.{p}\ \ Do you...{w=.2}\n\ \ understand why your father was so strict? 」"
    ka "「...If I got some other job,\n\ \ I wouldn't be missing meals.{p}\ \ And I'd be living a more normal life, right? 」"
    ka "「I wouldn't be too concerned about my future. 」"
    "But what I'm doing isn't like that.{p}It's like I'm desperately trying to light\na fire, with myself as the match."
    "It's possible I might never make that spark.{p}Also,{w=.2} I might break before that happens."
    kz "「Yes. That's correct.{p}\ \ However, there's one more reason{w=.2}\n\ \ for why he was so strict. 」"
    kz "「I think you were too young at the time to remember.{p}\ \ It was{w=.2} when we first started living here. 」"
    "Mom cut her words off there for a moment.{p}A pained expression crossed her face\nas she looked at me."
    "After a short pause,{w=.2} she continued."
    kz "「Your father...{w=.2} left his job at the company\n\ \ just before you turned one. 」"
    ka "「Eh...? 」"
    "I didn't believe those words, and my eyes widened."
    kz "「Officially, it was a voluntary resignation,{w=.2}\n\ \ but he was actually laid off due to downsizing.{p}\ \ It was a large company too. 」"
    kz "「Fortunately, he found reemployment right away,{w=.2}\n\ \ and that was the opportunity to move here. 」"
    kz "「That's the reason.{p}\ \ Because he went through it himself,{w=.2} I believe\n\ \ he didn't want you to have to live through that. 」"
    kz "「He wanted you to live your life without\n\ \ going through the same hardships he did.{p}\ \ Not being able to work is surprisingly harsh. 」"
    kz "「But your father isn't the\n\ \ best at expressing himself.{p}\ \ He's incredibly stubborn, too. 」"
    kz "「That's why, when it was time to decide a career,\n\ \ he couldn't express his feelings properly. 」"
    kz "「So at least,{w=.2} please understand that much. 」"
    ka "「{cps=5}. . . 」"
    "It was a surprise.{p}I never,{w=.2} ever saw things that way."
    "He's stubborn, and a bad communicator,\nbut my father was always dignified."
    "I never thought he'd have a past like that."
    kz "「To tell you the truth,{w=.2} your father has always been\n\ \ more worried about you than I have. 」"
    kz "「He would always secretly\n\ \ go attend your live concerts. 」"
    kz "「He made me check what days they were on.{p}\ \ Honestly, he could have done it himself. 」"
    "After saying that, she laughed a little,{w=.2}\nas though saying 「it's okay to come back. 」"
    ka "「But... 」"
    "I can't sort things out that easily."
    "I get my father's feelings.{p}I get what he's thinking.{p}I plan on understanding it."
    "But, I have a reason I can't make it so clear-cut."
    "Over this past year, so many things have changed.{p}I've gained new things,{w=.2} and lost others.{w=.2}\nBoth of those happened a lot."
    "If I returned home now,{w=.2} I'd have to be prepared\nto throw everything that happened away."
    ka "「I can't sort it out that easily.{p}\ \ I've given it my all up until now,\n\ \ and I've done so much. 」"
    ka "「...That's why,{w=.2} I can't just come back. 」"
    kz "「*sigh*...{w=.2}\n\ \ The apple doesn't fall far from the tree, does it?{p}\ \ You two are so similar like that... 」"
    kz "「But Kouya.{w} Have you considered whether\n\ \ it's okay to leave things as they are? 」"
    ka "「I... 」"
    kz "「It's okay to think about it later.{p}\ \ I think this is a good opportunity. 」"
    kz "「Come back here one more time,{w=.2}\n\ \ and try talking to your father once more. 」"
    kz "「Everything you've done your best to accomplish,{w=.2}\n\ \ you don't have to throw it away.{p}\ \ Therefore, I have a condition for you. 」"
    ka "「A condition? 」"
    "Mom nodded.{p}Then she explained what it was."
    kz "「If nothing comes from the next contest,{w=.2}\n\ \ please talk to your father one more time.{p}\ \ That's it,{w=.2} that's my wish. 」"
    
    stop music fadeout 3
    scene black with sdis 
  
    $ event_name = "Words of Determination"

    scene bedroom with sdis
    play music free10
    
    "From the slight chill, my eyes got cold.{p}There I was, an old childhood friend\nfreeloading in the rented place."
    "After lying down on the floor,\nit seems like I fell asleep."
    "When I looked at the clock, it was about 2.{p}So it turned into an afternoon nap."
    "As I thought about it, I suddenly looked around."
    fn "「Kouya's... 」"
    "Not back yet, it seems."
    "Maybe their talks dragged on.{p}It feels kind of late."
    "However,\nit looks like it was unnecessary worrying."
    
    play sound door04
    
    "Click."
    "I heard the sound of someone opening the door."
    "I moved before I could think about it.{p}I jumped to my feet and quickly ran\nto the entry hall."
    "Over there was the person I had waited for."
    "He seemed to have a slightly\nmore serious mood than usual."
    "When I saw his face and confirmed he was back,{w=.2}\nI was a bit relieved."
    "At that same time, a single word from inside\nme rose to the surface."
    "I've decided, this is my role.{p}And this word is the one to fulfill that role."
    fn "「Kouya. 」"
    
    show ka 001 at center with dis
    
    "I called his name,\nand he looked at me again."
    fn "「Welcome back! 」"
    
    stop music fadeout 3
    scene black with sdis
    
    $ event_name = "His Story"

    scene bedroom with sdis
    play music melodious05
    
    "After Kouya came back,{w=.2} he told me about\neverything that had happened in his parents' home."
    "「I've made you worry, haven't I? 」 he said.{p}「It's pretty obvious. 」"
    "He laughed after saying that."
    "The subject of the conversation was very simple."
    "「If the next contest is no good,{w=.2}\ncome back here. 」"
    "For Kouya, for me...{p}No, for anyone, it wasn't much of a surprise."
    "But still,{w=.2} what's important is what comes after.{p}If I had to make a conclusion, up until now\nnothing changed.{w} So I asked him."
    "In the end,{w=.2} Kouya..."
    
    show ka 001 at center with dis
    
    fn "「Kouya, what will you do? 」"
    ka "「I... 」"
    ka "「I think...{w=.2} I'll go back.{p}\ \ I've already promised to. 」"
    ka "「I thought, 『just like Mom says.』{p}\ \ It's true that I don't think leaving\n\ \ things like this will be good. 」"
    ka "「Some day,{w=.2} I'll have to set it all straight. 」"
    ka "「It's the duty of the guy\n\ \ who ran away from home, after all. 」"
    "He smiled bitterly."
    ka "「I've been thinking about everything\n\ \ up until now. 」"
    ka "「Besides, for me and dad,{w=.2}\n\ \ I get the feeling that we both have\n\ \ something we want to say but couldn't. 」"
    ka "「So, I think I want to take a chance.{p}\ \ This really is a good opportunity, for sure. 」"
    ka "「Besides, even if I do return home,{w=.2}\n\ \ I feel that I want to keep playing the guitar.{p}\ \ I've come so far, after all. 」"
    ka "「Before that, I want to say\n\ \ what my real intentions are once.{p}\ \ About me.{w=.2} About everything until now. 」"
    ka "「I'm sure on that path, I can keep going further.{p}\ \ That's what I think. 」"
    "I nodded."
    "That is likely, to be sure."
    "Even when people don't understand, they can do\nanything.{w} And yet, the ones who do understand\nare probably the ones who can put in the effort."
    "But getting people to understand\nis easier said than done."
    "However, Kouya is determined to do it.{p}In all honesty, I thought that was amazing."
    fn "「...Like I thought,{w=.2} you really are strong. 」"
    
    show ka 006 with dis
    
    ka "「No, I'm not.{p}\ \ I would never have thought of this alone.{p}\ \ ...It's thanks to you,{w=.2} [fn]. 」"
    fn "「Eh? 」"
    
    show ka 001 with dis
    
    ka "「You came looking for me yesterday.{w=.2}\n\ \ And now I can think things through like this.{p}\ \ Thanks,{w=.2} seriously. 」"
    fn "「No way, I didn't do anything.{p}\ \ You keep saying the things I want to say,{w=.2}\n\ \ and I honestly thought I screwed things up there. 」"
    "I laughed a bit to hide my awkwardness.{p}If I were to say anything about yesterday,{w=.2}\nit was a little embarrassing."
    ka "「And I'm saying you didn't.{p}\ \ Hey,{w=.2} [fn]. 」"
    fn "「Hm? 」"
    "Kouya caught me with a pointed look.{p}From its earnestness, I also became serious."
    ka "「Whatever happens later, I still don't know yet.{p}\ \ But- no,{w} because of that,{w=.2} I think I\n\ \ have to work even harder than before. 」"
    
    show ka 013 with dis
    
    ka "「So, umm.{p}\ \ {nw}"
    show ka 005 with dis
    extend "Will you... keep on supporting me?{w=.2}\n\ \ Like you have been? 」"
    "Kouya asked me that question{w=.2}\nas a slightly worried expression painted his face."
    "It's kind of funny.{p}He didn't have to ask."
    fn "「Seriously...{w=.2} What are you saying Kouya? 」"
    "So I said that.{p}Even if I didn't smile,\nmy face naturally relaxed."
    fn "「Of course I will.{w=.2}\n\ \ Even if you didn't ask me to,\n\ \ I'd still be cheering you on. 」"
    
    show ka 003 with dis
    
    "Kouya smiled at my assertion."
    ka "「Thanks, [fn].{w} ...All right!{p}\ \ Then the only thing left to do is move forward.{p}\ \ How about we throw ourselves into it? 」"
    fn "「Yeah!{w} Full speed ahead! 」"
    
    show ka 002 with dis
    stop music fadeout 1
    
    ka "「Okay then, this day's been going on long enough,\n\ \ so let's end the talk right here.{p}\ \ {nw}"
    play music free02
    extend "Let's go out in a bit. 」"
    fn "「Uwooh!? 」"

    play sound standup
    
    "Kouya spoke over his shoulder as he stood up.{p}The abruptness made me raise my voice in surprise."
    "You sure are quick to change the subject, Kouya."
    fn "「Go out... where? 」"
    
    show ka 005 with dis
    
    ka "「Mm?{w} What are you saying?\n\ \ Today's the Summer Festival. 」"
    ka "「You came all this way here,\n\ \ so what are you going to do if you don't go? 」"
    
    show ka 001 with dis
    
    ka "「...Wait,{w=.2} did I not tell you? 」"
    fn "「Nope, haven't heard a thing. 」"
    
    show ka 013 with dis
    
    ka "「...oh, my bad.{p}\ \ A-{w=.2}anyway, you're going, right?{p}\ \ {nw}"
    show ka 005 with dis
    extend "Everyone else arranged to meet up too. 」"
    fn "「No,{w=.2} I'll go, but...{p}\ \ could you tell me these things a bit earlier? 」"
    
    show ka 013 with dis
    
    ka "「Yeah, sorry... 」"
    "Kouya scratched his cheek apologetically."
    "With his job from yesterday and everything,{w=.2}\nKouya's surprisingly forgetful and temperamental.{p}And I saw him as so on top of things, too."
    "No, maybe that's wrong.{p}He doesn't use that many words.{p}Maybe he's bad at communicating?"
    fn "「Well, it's okay.{w} Ready to go then?{p}\ \ Everyone's waiting, after all. 」"
    
    stop music fadeout 3
    scene black with dis   
 
    $ event_name = "Kouya and the Festival"

    scene rice red with dis
    play music festival_ambience
    
    "The two of us got ready\nand headed off towards the festival."
    "The sun was quite low in the sky,{w=.2}\nso it seemed like a good time to go."
    "Minasato Village,\na place that is usually so peaceful.{p}Today, though, that's a little different."
    "As we got closer to the shrine,{w=.2} I could feel a\nsense of tingling energy mixing in with the air.{p}It felt like the whole village was here partying."
    "Once my skin started to feel it,\nI started shivering all of a sudden."
    "Kouya looked the same as ever,{w=.2} but every so often\nhis tail will wag slowly from left to right.{p}It's kind of fun to watch."
    "Its movements seemed to be impulsive,{w=.2}\nand whenever Kouya noticed it happening,\nthe wagging stopped as if he just got pissed off."
    
    show ka 001 red at center with dis
    
    ka "「Say,{w=.2} have you ever been to\n\ \ any of the festivals over where you are? 」"
    "Maybe it was because he noticed me\nlooking aside at his tail,{w=.2}\nbut Kouya suddenly asked me that."
    fn "「Well, sometimes.{p}\ \ With so many people around,\n\ \ they're huge events. 」"
    fn "「In any case,\n\ \ I did go see the fireworks a lot. 」"
    
    show ka 003 red with dis
    
    ka "「Oh, that?{w} With a girlfriend? 」"
    fn "「No no, nothing like that.{p}\ \ With friends.{w=.2}\n\ \ F-R-I-E-N-D friends,{w=.2} you hear me. 」"
    
    show ka 009 red with dis
    
    ka "「Uh-huuuh. 」"
    fn "「Hey,{w=.2} what's with that weird doubting look?{p}\ \ It's true. 」"
    ka "「In that case,{w=.2}\n\ \ let's just leave it there. 」"
    "Kouya teased me,{w=.2}\npossibly as revenge for the thing with the tail."
    "It's a bit aggravating being done in like this.{p}I have to try and get him back."
    fn "「Now that you mention it, how about you, Kouya? 」"
    fn "「You were always popular back then,{w=.2}\n\ \ so have you ever gone to the festival\n\ \ with a girl while I was gone? 」"
    ka "「Oh yeah.{p}\ \ You've grown up too, haven't you, [fn]? 」"
    "He didn't hear a thing."
    fn "「Like I said... 」"

    hide ka with wipe_right
    
    "「That's not it, 」{w=.2} or so I would have explained\nwhen a voice from far away called to us,\nwhich wiped away the thought."
    "When I looked, all my other childhood\nfriends had grouped up over there.{p}Seems like everyone but us was already there."
    "...Even Kounosuke isn't late this time.{p}The power of the festival is just awesome."

    show to 001 red at midleft
    show ky 001 red at midright
    show si 001 red at farleft
    show ka 001 red at farright
    with wipe_right
    show to 002 red with dis
    
    to "「You guys are late!{p}\ \ Get over here already! 」"
    "At that remark, Kouya and I exchanged glances.{p}With just that we were able to understand each other."
    "The two of us moved in double time\nand joined up with the rest."
    
    show to 001 red with dis
    
    to "「Finally, you're both here.{p}\ \ You guys are late. 」"
    fn "「Sorry, sorry.{w} ...Hey, wait,\n\ \ you're all here too early.{w} Isn't there still\n\ \ some time left before the time we said we'd meet? 」"
    si "「We just got here ourselves. 」"
    fn "「Huh, really? 」"
    
    show ky 002 red with dis
    
    ky "「Well, Torahiko was itching to get here earlier.{p}\ \ All that time he was going{w=.2}\n\ \ 'we're late, we're late.' 」"
    
    show to 005 red with dis
    
    to "「W-what?{w} Is that so wrong? 」"
    ka "「Calm down already.{p}\ \ You aren't a ki-{w} {nw}"
    show ka 013 red with dis
    extend "wait, never mind. 」"
    
    show to 003 red with dis
    
    to "「Hey, hold up a minute.{p}\ \ What's with that unnatural stop?{p}\ \ You wanna say I'm a kid? 」"
    
    show ka 001 red with dis
    
    ka "「Not much gets by you, does it, Sherlock? 」"

    show to at jump_up
    
    to "「What-?! 」"

    scene rice red with wipe_right
    show ta 501 red with wipe_right
    
    ta "「Hey, come on, just leave things there.{p}\ \ It's our annual festival, after all.{p}\ \ No need to be so hasty. 」"
    
    show ta 502 red with dis
    
    ta "「Now,{w=.2} let's get a move on.{p}\ \ We're gonna have a party, yeah? 」"

    hide ta with wipe_right
    
    "At Tatsu-nii's insistence,\nthe ten of us started walking."
    "As we went along,{w=.2}\nwe started talking about the small stuff,"
    "Like if there were this many shops last year,{w=.2}\nor if things were cheaper at this stall than another."
    "Even though it was so trivial,\neveryone seemed to be having fun.{p}I guess everyone was looking forward to today."
    "Even though we haven't reached our destination,{w=.2}\nit was already quite crowded,\nbut I enjoyed myself well enough."
    "That was probably why our ten man march{w=.2}\nmade so much noise, and we finally made\nit through in the blink of an eye."
    
    stop music fadeout 3
    scene black with wipe_right
    scene festival_stands with wipe_right
    play music festa01
    
    "Minasato Shrine.{w} The old assembly hall\nwhere people made offerings to the water god."
    "The food stall tents lined up around the borders\nof the grounds,{w=.2} and decorative paper lanterns\nhung from the sky."
    "And so many people were here,{w=.2}\nfilling up the area with so much heat."    
    fn "「Whoa... 」"
    "The scene just overwhelmed me.\nUnintentionally, I let out a sigh of wonder."
    "I'm sure that in my mind,{w=.2}\nI can remember past festivals\nthat were just as lively and amazing as this one."
    "But seeing it again like this\nmade it so magnificent."
    "Even after I started walking among the crowds,{w=.2}\nmy eyes kept flicking from here to there."

    show ka 002 at center with dis
    
    ka "「What are you looking around so restlessly for? 」"
    "Kouya noticed the expression on my face,\nand asked me about it."
    fn "「Oh,{w=.2}\n\ \ I was just thinking about how amazing it all is.{p}\ \ The festival, I mean. 」"
    
    show ka 001 with dis
    
    ka "「Hm?{w} It's the same as it is every year.{p}It's not like it's changed much\nsince the time you lived here. 」"
    fn "「Really? 」"
    ka "「Yeah, really.{p}Aren't you just feeling that way{w=.2}\nsince it's been so long since you've seen it? 」"
    fn "「Hmm.{w} That could be it. 」"
    
    show ka 002 with dis
    
    ka "「Right?{w} You left so long ago, so it makes sense.{p}\ \ Come on,{w=.2} don't just look around,\n\ \ let's go do something. 」"
    ka "「Anything in particular you wanna do? 」"
    fn "「Let's see.{w=.2} Well, since it's been so long... 」"
    "This time I took another look around the place\nto see if there was anything that stood out."
    "There's the standard goldfish\nscooping and target practice,\nthe stands that sell vinyl balloons and neon sticks,"
    "and all the other various things\nyou could think to find at a festival."
    "There truly is a lot o-"
    fn "「...huh? 」"
    "There I felt a sense of discontent.{p}Something's not right."
    "Stalls were set up on both sides of the path.{p}After looking to the right,{w=.2}\nI carefully shifted my line of sight to the left."
    "With that movement,\nI figured out what was bugging me."
    fn "「Hey,{w=.2} Kouya. 」"
    
    show ka 001 with dis
    
    ka "「What's wrong? 」"
    fn "「...Where's everyone else? 」"
    "Kouya's ear twitched a little.\nIt was an indication of an unvoiced 「Huh? 」"
    "As if to check for himself,{w=.2} Kouya slowly\nturned his own eyes towards where I was looking.{p}Then he spoke."
    
    show ka 005 with dis
    
    ka "「Seriously. 」"
    "There should have been\neight people walking in front of us.{p}And somehow, we lost track of all of them."
    "Tatsu-nii's so tall,{w=.2}\nhe shouldn't be this easy to miss."
    "An unpleasant wind blew in the space between us."
    "So, simply put..."
    fn "「We got separated? 」"
    
    show ka 001 with dis
    
    ka "「Huh... Seems that way. 」"
    fn "「...What do we do? 」"
    "We stood together, looking worried."
    ka "「Ahh,{w=.2} first off let's try looking for them.{p}\ \ {nw}"
    show ka 013 with dis
    extend "But even if I say that,{w=.2}\n\ \ the chances of us finding them are... 」"
    "Kouya made a bitter face as he scratched his head."
    fn "「Yeah... They might have circled around\n\ \ the other side too. 」"
    ka "「I'd like to find them soon if possible.{p}\ \ The fireworks are soon... 」"
    
    show ka 003 with dis
    
    ka "「Oh well,{w=.2} not like I mind\n\ \ the two of us being alone together. 」"
    fn "「Wha-!? 」"
    "My heart skipped a beat at his line.{p}It's true, now that I think about it.\nKouya and I are alone together right now."
    "Realizing it again made me a little embarrassed.{p}I could tell my own face was red."
    fn "「Oh come on,{w=.2} that's not what I'm saying.{p}\ \ We came here with everyone else. 」"
    "I talked quickly to cover it up."
    "But I do think it's nice that we're alone."
    
    show ka 001 with dis
    
    ka "「Yeah, that's true.{p}\ \ ...All right,{w=.2} let's get going, [fn]. 」"
    fn "「Yeah,{w=.2} we have to find everyone soon. 」"
    ka "「Right. 」"

    hide ka with wipe_right
    
    "With that thought spurring us on,{w=.2}\nthe two of us headed into the crowd."
    "However,{w=.2} since it felt like a waste\nto go around to only look for the others,{w=.2}\nwe also looked at a few carts and stalls."
    "We started with the goldfish scooping,{w=.2}\nand then competing over who got the bigger one."
    "But in the end we couldn't even get one,\nwhich was irksome to both of us."
    "We also did the target practice.{p}It was another contest as revenge from before."
    "Kouya lost and ended up with a box of caramel,{w=.2}\nbut the two of us shared the nostalgic taste."
    "Cotton candy and crepes came later.{w} 「It'll get\nstuck to the sides of your mouth, 」 Kouya teased.{p}It was a bit embarrassing, but also fun."
    "That mood kept up as we made\nour rounds through the crowd."
    "Here I am, together with Kouya at the festival.{p}Maybe it's because I've never been to one with\nsomeone before,{w=.2} but I felt strangely awkward."
    "But, I was happy.{p}So, so much.{w} Like I've never been before."
    "We weren't able to find Torahiko and the others.{p}It's already late in the day,{w=.2} and any minute\nnow the fireworks would begin launching."
    "At this rate, we'll have to give up on looking."
    "After reaching that conclusion we felt tired\nfrom walking,{w=.2} so we separated from the crowd\nand sat at the stone steps beneath the shrine."

    scene black with wipe_right
    $ renpy.music.set_volume(0.3, 0.4, channel = "music")
    scene shrine_stairs night with wipe_right
    
    "Now's about the time for the Bon Dance,\nand we heard the customary music."
    "Dancing in the ring made me shy,\nso I opted out of it.{p}We couldn't see any of the others there anyway."
    "While we looked at the commotion on the other end,\nwe took a breath."
    
    show ka 001 night with dis
    
    fn "「Whew...{w} Somehow,\n\ \ we went around so many times. 」"
    ka "「Yeah.{w} {nw}"
    show ka 005 night with dis
    extend " And no one there seems to be tired.{p}\ \ And hey,{w=.2} isn't this everyone in the village? 」"
    fn "「Hahaha,{w=.2} wouldn't that be an overstatement?{p}\ \ But there does seem to be way too many people.{p}\ \ And this is usually an unseen village. 」"
    
    show ka 001 night with dis
    
    ka "「I know, right?{p}\ \ Seriously,{w=.2} thanks to that\n\ \ we can't really search for anyone like this. 」"
    fn "「In the end,{w=.2} we couldn't find Torahiko\n\ \ or anyone else.{w} But with this many people\n\ \ I guess it can't be helped. 」"
    ka "「...Sorry, [fn].{w} About being separated\nfrom everyone,{w=.2} and being with me.{p}\ \ It've been better with everyone together, right? 」"
    "Kouya spoke casually to me as he felt\nsome responsibility for it all{w=.2}\nand apologized to me."
    "Since I didn't feel that way myself,{w=.2}\nI became a little apologetic."
    "I do think it would have been fun if we could\nall walk around together.{w} But, I had plenty\nof fun with just being with Kouya."
    "If we weren't here with them to start with,{w=.2}\npart of me thinks I'd have had even more fun.{p}...That's mean to the other eight guys though."
    "So I spoke about the other\nparts that I was thinking."
    fn "「No,{w=.2} that's not true.{p}\ \ I had fun being with you. 」"
    "After saying so,{w=.2}\nit felt kind of embarrassing.{p}Without thinking about it, I turned away."

    hide ka with wipe_right
    
    ka "「...[fn]... 」"
    "I thought I heard Kouya's voice,{w=.2}\nand then I felt something warm\ntouch my hand on the stone steps."
    "It caught my hand,{w=.2}\nthen gently wrapped around it."
    "It was Kouya's hand.{p}{nw}"
    play sound heartbeat
    extend "The instant I realized it,\nmy heart leapt in my chest."

    show ka 001 big night at center_big with wipe_right
    
    "I turned around,{w=.2}\nand there in front of me was Kouya's face.{p}His always-sharp eyes looked straight into me."
    
    stop music fadeout 3
    
    "The distant sounds of the\nhustle and bustle faded away."
    "I could feel heartbeats next to my held hand.{p}Were they mine?{w=.2} Or were they Kouya's?\nI couldn't tell."
    "All I knew for sure was that my blood was pumping."
    "All of a sudden, I was very confused.{p}My hand felt as hot as it could be,\nwhile my face turned white."
    "I lost all comprehension about my own situation."
    fn "「Kou...{w=.2}ya...? 」"
    ka "「[fn]... 」"
    "Kouya put a bit more force into his hand.{p}It hurt a little,{w=.2} but I didn't really\nhave the time to think much of it."
    "Just how did things end up this way?{p}Did something happen?{p}Those thoughts kept whirling in my head."
    ka "「...You know,{w=.2} when you came back for the summer,\n\ \ I felt like something changed within me. 」"
    fn "「Yeah...? 」"
    ka "「This time it's special,{w=.2} and it might\n\ \ be because so many things are happening.{p}\ \ But I'm really glad that you're here. 」"
    fn "「Okay... 」"
    
    show ka 006 big night with dis
    
    ka "「How do I put this...{p}\ \ I can't really say it right,{w=.2}\n\ \ but that's what I'm thinking. 」"
    fn "「Mmhhmm... 」"
    "I've nodded earlier,\nbut whatever Kouya's trying to say,{w=.2}\nright now I can't really process it."
    "I mean, isn't this-"
    
    show ka 001 big night with dis
    
    ka "「[fn]...{w=.2} I- 」"
    "Each time one of those syllables hit my ears,{w=.2}\nI felt my heart race faster."
    "I've now forgotten how to blink.{p}My senses are all over the place."
    "My chest felt oddly painful.{p}At this point,{w=.2}\nI can't tell what's going to happen."
    "While I was in that state,\nKouya opened his mouth to keep going."
    "But just before he could voice his thoughts,{w=.2}\na call from somewhere else broke the spell."
    
    play music festa01
    $ renpy.music.set_volume(0.8, 0.0, channel = "music")
    
    who "「Finally, found you!{p}\ \ Heeey,{w=.2} what are you guys doing over there!? 」"
    
    show ka 012 big night at jump_up_big
    pause .1
    show ka at center_big
    pause .01
    hide ka
    show ka 012 night at center
    with dis
    
    "Both Kouya and I jumped up{w=.2}\nand put some distance between us\nlike children caught in the middle of a prank."
    "And just like the evening,\nthere was Torahiko's voice.{p}And behind him,{w=.2} there was everyone else."
    "After seeing that, the mood felt like it collapsed.{p}On one hand I felt relieved,{w=.2}\nbut on the other I felt like it was a pity."
    "...I kind of wish they'd come a little later."

    hide ka with wipe_right
    show to 001 night at midleft
    show ka 006 night at midright
    with wipe_right
    
    to "「You disappeared as soon as we stopped\n\ \ paying attention. 」"
    to "「Can't you guys not act like lost\n\ \ little kids at that ag-{p}\ \ {nw}"
    show to 003 night with dis
    pause .2
    extend "your faces are red.{w=.2} Did something happen? 」 "
    fn "「Ah! No, nothing!{p}\ \ Absolutely nothing!{p}\ \ Right,{w=.2} Kouya? 」"
    
    show ka 001 night with dis
    
    ka "「Yeah, nothing happened.{p}\ \ Why,{w=.2} were you worried about us? 」"
    
    show to 006 night with dis
    
    to "「Not you, I'm worried about [fn].{w} ...Well,\n\ \ if nothing happened, then okay.{p}\ \ {nw}"
    show to 001 night with dis
    extend "Anyway, the fireworks are about to start,{w=.2} let's g- 」"
    
    play sound fireworks_explosion 
    scene shrine_stairs night with wipe_right
    show fireworks
    
    "The sound of an explosion cut him off.{p}Up in the sky, a great big flower was blooming."
    "The fireworks have started."

    show to 006 night at farleft
    show ta 501 night at farright
    show si 001 night at center
    with wipe_right
    
    to "「Aww, we didn't make it in time.{p}\ \ If we go over there,{w=.2}\n\ \ I think we can get closer. 」"
    ta "「But we can see them fine right here.{p}\ \ There aren't many people around,\n\ \ so it's a nice secret spot. 」"
    si "「That's true.{w} I don't think anyone\n\ \ really wants to move around any more,{w=.2}\n\ \ so isn't it fine to just stay here? 」"
    
    show to 002 night with dis
    
    to "「I guess.{w=.2} Let's do that, then! 」"

    scene shrine_stairs night with wipe_right
    play sound fireworks_explosion
    show fireworks
    
    "After that discussion,\nthe second lot of fireworks lit up in the sky."
    "Everyone else sat on the steps\njust like Kouya and I were,{w=.2}\nand looked up into the sky."
    "Each and every time,\nthe fireworks would blast up there,{w=.2}\nthen fade away."
    
    play sound fireworks_explosion
    show fireworks
    
    "Pheeeew... Boom...{p}{nw}"
    play sound2 fireworks_explosion
    show fireworks
    extend "Pheeeew... Boom..."
    "And after each and every one of those times,\nthe sounds would resound in the night sky."
    fn "「It's beautiful... 」"
    "I murmured,{w=.2}\nwithout addressing anyone in particular."
    "That was my honest thought.{w} And possibly,{w=.2}\nI think it might even be more beautiful\nthan any other fireworks I've seen until now."
    "However, more than that,"
    
    stop music fadeout 3
    scene black with dis
    show ka 001 big at center_big with dis
    
    ka "「[fn]...{w=.2} I- 」"
    "Whatever Kouya was going to say after that,{w=.2}\nit slowly faded into the memory\nof how warm his hand was."

    scene black with dis

    jump end22
    
######################################################
label shin22:
    
    $ event_name = "Nervous? First Date"

    play music festival_ambience fadein 1
    $ renpy.music.set_volume(0.8, 0.0, channel = "music")
    scene shrine_stairs red with sdis
    
    "The shrine ground.{p}Today is the day of this village's festival."
    "I can hear the festival band,\nand my emotions beat fast to their rhythm,{p}because..."
    
    stop music fadeout 1
    pause 1
    scene hentry with wipeleft
    play music free02
    $ renpy.music.set_volume(0.8, 0.0, channel = "music")
    
    am "「Yes, hello.{w=.2} Kuroi Residence. 」"
    fn "「Oh, hello.{p}\ \ This is [ln]. Would Shin-kun be available? 」"
    am "「Yes,{w=.2} just a moment.{p}\ \ {size=-10}Shin-kun, [ln]-kun is calling!{size=+10} 」"
    "{cps=10}. . . "
    si "「Hello. 」"
    fn "「Yes, hello Shin-kun?{p}\ \ Sorry for asking so suddenly,\n\ \ but are you free tomorrow evening? 」"
    si "「That really is sudden.{p}\ \ I have no plans, but why do you ask? 」"
    fn "「How about we go to the festival together then? 」"
    si "「The festival? 」"
    fn "「Yeah.{p}\ \ I'm sure it's tomorrow. 」"
    si "「Now that you mention it,\n\ \ yes it is. 」"
    fn "「So,{w=.2} let's go then. 」"
    si "「...what shall I do? 」"
    fn "「Oh, can't make it after all? 」"
    si "「No, not like that...{p}\ \ Just don't keep your expectations high. 」"
    fn "「Expectations? Of what? 」"
    si "「If you go with me,{w=.2}\n\ \ things probably won't be very fun.{p}\ \ Wouldn't it be better to go with someone else? 」"
    fn "「You don't need to worry about that.{p}\ \ We can just wander around together. 」"
    si "「If you say so then...{w} alright.{w=.2}\n\ \ 5PM tomorrow is fine, yes? 」"
    fn "「Okay then. 」"
    
    stop music fadeout 1
    pause 1
    scene black with wipeleft
    play music festival_ambience fadein 1
    $ renpy.music.set_volume(0.8, 0.0, channel = "music")
    pause 1
    scene shrine_stairs red with sdis
    
    "And so, I'm now waiting to meet with Shin-kun.{p}I guess you could call it a date."
    "Now that I think about it,\nthe thumping of my chest got increasingly bigger."
    "I got here earlier than planned,\nbut this is Shin-kun so he shouldn't be too...{p}Oh there he is."

    show si 411 red at center with sdis
    
    si "「Oh...{w} {nw}"
    show si 401 red with dis
    extend " good evening, [fn]. 」"
    fn "「Good evening.{w} What's wrong? 」"

    show si 411 red with dis
    
    si "「Oh, nothing. I just spent some time getting ready.{p}\ \ Amaki helped me out with a lot,{w=.2}\n\ \ {nw}"
    show si 401 red with dis
    extend "but did I keep you waiting? 」"
    fn "「No. {w=.2}I just got here myself.{p}\ \ And actually, we're a bit earlier than expected.{p}\ \ That aside... 」"
    
    menu:
        "A. You look beautiful.":
            jump shin22_beautiful
        "B. You look cute.":
            jump shin22_cute

    ####################################################
    label shin22_beautiful:
        
        fn "「You look beautiful today. 」"
        
        show si 404 red with dis
        
        si "「That's because a lot of things\n\ \ were carefully prepared.{w} 'It's your first date,\n\ \ so you have to dress up,' or so I'm told. 」"
        
        show si 410 red with dis
        
        si "「Ugh, he could take it easy with the teasing.{p}\ \ He knows who I'm going with. 」"
    
        jump shin22_festival
    
    ####################################################
    label shin22_cute:
        
        fn "「You look cute today. 」"
        
        show si 411 red with dis
        
        si "「Do you really mean that? 」"
        fn "「Yep. 」"
        
        show si 401 red with dis
        
        si "「That's something you say to girls.{p}\ \ {nw}"
        show si 403 red with dis
        extend "Amaki, you. What is everyone thinking? 」"
    
    #####################################################
    label shin22_festival:
        
        show si 401 red with dis
        
        si "「But anyways, what shall we do today? 」"
        si "「Right now it looks they'll shoot\n\ \ the fireworks after dark, but there doesn't\n\ \ seem to be any events besides that... 」"
        fn "「Then how about we check\n\ \ the food carts until then? 」"
        si "「Okay.{p}\ \ {nw}"
        show si 409 red with dis
        extend "Sorry, {w=.2}guess things really aren't that fun. 」"
        fn "「That's not true at all. 」"
        "I mean, things aren't exciting\nuntil they get there."
        "As I smiled at the unexcited Shin-kun,\nthe two of us walked into the festival's bustling."
        
        scene black with dis
        stop music fadeout 1
        pause 1
        
        "One hour later..."
        
        $ event_name = "Everywhere I go it's sweet...."
        
        scene festival_stands with dis
        play music free0421
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        
        "I tried to push down the sensations welling up,\nforcing myself to eat the last mouthful as\nmy tongue tried to reject all sensations."
        "I managed to conquer the sweet lethal weapon, and\nmy eyes clouded over as I won the bitter fight while\nlooking at the smiling profile of the one next to me."
        
        show si 402 with dis
        
        "It was such a beautiful face.{p}Supreme bliss."
        "If I had to express his sentiments in words,\nthose would probably be the most appropriate."
        "If he really was that happy\nor somehow really in pain, I had no idea.{p}No clue at all anymore."
        "I tried to drown out the chill\nrunning through my mouth somehow,\nand pointed at one cart near us."
        fn "「Look Shin-kun, takoyaki... 」"
        
        show si 401 with dis
        
        si "「Oh, another crepe stand.{p}\ \ {nw}"
        show si 402 with dis
        extend "Want to try comparing them to the ones before? 」"
        "At that moment,\nI knew all my efforts came to nothing."
        fn "「N-no... 」"
        "I was hoping that the smile I gave in the\ndim lighting would really hide my thoughts."
        "My stomach still had some room left.\nBut now I can't anymore."
        
        show si 401 with dis
        
        si "「What's wrong?{p}\ \ {nw}"
        show si 402 with dis
        extend "Did you eat too much? 」"
        fn "「No,{w} well,{w=.2} a little. 」"
        "I smiled as best I could at Shin-kun, who was\nin such a good mood, as I gave a vague answer."
        
        show si 401 with dis
        
        si "「I see.{p}\ \ Then I suppose it's fine\n\ \ that I just buy one for myself? 」"
        fn "「Sure.{w=.2} Take care. 」"
    
        hide si with wipe_right
        
        "As I watched Shin-kun walk over to the cart,\na single tear fell out of my eye."
        "It's the summer festival,{w=.2} where you spend time\nwith the one you like and but the same things,\nand eat while walking."
        "That's the simple happy time it's supposed to be.{p}No wait, it was good after the very beginning."
        "We bought crepes together, looked at the\ncandy animals, passed up goldfish scooping\nsince we had no goldfish bowl..."
        "After the beginning Shin-kun wasn't that excited,\nand he was the same as usual,{w=.2} though he did\nseem to be in a better mood than normal."
        "As that unconscious smile hung on his face,\nI could just see a little bit\nof enjoyment out of him."
        "Still...{p}{nw}"
        play sound hit81
        extend "Please let me eat something salty once in a while!"
        "If I had to list out everything\nwe ate up to this point,"
        "we had a crepe, {w=.2}strawberry candies,\n{w=.2}ningyoyaki,{w=.2} cotton candy,{w=.2}\nanother crepe,{w=.2} a chocolate banana..."
        "I've tried countless times to indirectly\nsteer us towards takoyaki or yakisoba,\nbut Shin-kun only has a taste for sweets..."
        "I'm almost about to die of sugar overload.{p}I had no idea he was this much of a sweet tooth."
    
        show si 401 with wipe_right
        
        si "「Sorry to keep you waiting. 」"
        fn "「Welcome back. 」"
        "Shin-kun came back with the crepe he bought.{p}When I saw how much sugar was in his hands,{w=.2}\nI couldn't hold back the cramp in my smile."
        
        show si 404 with dis
        
        si "「... 」"
        
        show si 401 with dis
        
        si "「The cream isn't done very well.{p}\ \ But it's been baked the best\n\ \ compared to the other ones. 」"
        fn "「I-I see... 」"
        
        show si 402 with dis
        
        "After that little bite,\nShin-kun smiled even more as he stuffed\nhis cheeks with the 'third' crepe."
        "As I looked at that smile from the side, I felt\nlike there was more sugar welling inside my mouth,\nand I desperately tried to push it down."
        "I don't want to look at anything sweet now..."
        fn "「Oh, Shin-kun,{p}\ \ Do you want to eat a hot dog? 」"
        "I pointed at a nearby cart,\nand spontaneously tried to lead Shin-kun.{p}{nw}"
        play sound bom19_b
        extend "Please, {w=.2}let me have some salt!！"
        
        show si 401 with dis
        
        si "「Aren't you full? 」"
        fn "「Uh, well... 」"
        "Sob.{p}Crap,{w=.2} did I dig my own grave?"
        
        show si 402 with dis
        
        si "「Could it be that your wallet is tight?{p}\ \ How about I treat you in that case?{p}\ \ Amaki gave me quite a bit today... 」"
        fn "「T-that's not it,{w=.2}\n\ \ but, okay. 」"
        "Good, he didn't notice."
        
        show si 401 with dis
        
        si "「? 」"
        fn "「I-it's fine.{p}\ \ Come on. 」"
        
        show si 402 with dis
        
        si "「Oh, there's chocolate bananas again. 」"
        fn "「... 」"
        si "「I like those better than hot dogs. 」"
        
        play sound don08
        
        "{cps=5}He's hopeless...{cps=40}{w=.2}I have to do something...{p}There was something good right there,\nbut it was carried away in a moment."
        "If I could somehow shift Shin-kun's tastes\naway from sweets,{w=.2} he'll break through\nthe limits at the very worst at this rate."
        "In other words, a reversal crisis...!"
        "I-if I push too hard\nI might cause withdrawal symptoms!"
        fn "「H-hey, are you feeling thirsty? 」"
        
        show si 401 with dis
        
        si "「Hm...{w} {nw}"
        show si 410 with dis
        extend "well I guess I am.{p}\ \ {nw}"
        show si 402 with dis
        extend "Do you want some kaki ice cream then? 」"
        fn "「...{p}\ \ No, I'm fine with tea... 」"
        "Food's a no-go.{p}After this maybe we'll just toss rings\nor do target practice..."
        
        scene black with sdis
        
        if shin_step2 == True:
            jump shin22_parents
        else:
            jump shin22_fireworks
    
    ##########################################################
    label shin22_parents:
            
        $ event_name = "The Bon Dance"
        
        stop music fadeout 1
        play music festival_ambience fadein 1
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        scene festival_stands with dis
        show si 401 with dis
        
        fn "「S-since we're probably full by now,\n\ \ how about a game of ring tossing? 」"
        "I was saved from the sweet food mine field\nby a bottle of oolong tea, so I decided\nto steer Shin-kun towards anything else."
        si "「Really?{w} There are stands\n\ \ we haven't eaten from though. 」"
        "I'm pretty sure he was referring to crepes.{p}Please spare me from the sugar overlords!{w=.2}\nI beg you!"
        "I hung around with a hesitant Shin-kun\nas my heart cried out."
        fn "「W-we've done nothing but eat,\n\ \ and we're at the festival and all,\n\ \ so it'd be sad if we didn't do anything else. 」"
        
        show si 410 with dis
        
        si "「I suppose so...{p}\ \ {nw}"
        show si 402 with dis
        extend "Where should we go next then? 」"
        "Yes...!{p}I can escape the infinite hell of sugar here!"
        fn "「Hmm.{p}\ \ Well how about that way for now? 」"
        "I stuck a smile on my face,\nand as my heart cried in victory, I lead\nthe way to somewhere with fewer sweet stands."
        "Ring toss,{w=.2} shooting galleries,{w=.2} smart balls...{p}I wonder what'd be good first?"
        
        show si 401 with dis
        
        si "「Isn't that...? 」"
        "Shin-kun quietly uttered one word\nas he froze with a start.{w} I stiffly\nswung my neck around I could hear a creak,"
        "and I saw a stream of people\ngoing towards where I looked. I was relieved\nit wasn't more sweets at first,"
        "and when I looked at where people were going to,\nthere was a wooden stage.{p}They were all gathering together around it."
        "I can't see for sure since we were a ways apart,\nbut there seems to be a dragonman\nwith the taiko drum onstage."
        "I wonder if that's Tatsu-nii?"
        
        stop music fadeout 1
        pause 1
        play music free12 fadein 1
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        
        "A short time later, the drum's vigorous sounds\nand the Japanese music was carried by the wind\nall the way over to where we were."
        fn "「Oh, the Bon Festival dance.{p}\ \ That takes me back. 」"
        si "「The Bon Festival dance? 」"
        fn "「Yeah.{p}\ \ ...you really don't know? 」"
        
        show si 411 with dis
        
        si "「I-{w=.2}I know that much at least.{p}\ \ {size=-10}I've never danced though... 」"
        fn "「Huuuh. 」"
        "Shin-kun looked away as his voice got quiet.{p}{nw}"
        play sound freeze04
        extend "Tee hee.{p}This is my chance!"
        fn "「How about we dance together then? 」"
        
        show si 405 with dis
        
        si "「What!? 」"
        fn "「Come on then. 」"
        si "「W-wait, [fn]! 」"
        "I grabbed Shin-kun's arm forcibly dragging\nhim along until we joined everyone else\nand walked towards the stage."
        
        scene shrine_court night with wipeleft    
        show si 411 night at center with dis
        
        fn "「Yes, like that.{p}\ \ You don't need to be that stiff, just do what\n\ \ everyone else is doing and you'll be fine. 」"
        si "「R-really?{p}\ \ I'm not looking strange? 」"
        fn "「You're fine, just fine. 」"
        "Shin-kun was moving, if awkwardly,\nand frequently repeated that question.{p}He could have just relaxed his shoulders more."
        fn "「Hey, your shoulders are stiffening up again. 」"
        
        show si 406 night with dis
        pause .5
        show si 411 night with dis
        
        si "「... 」"
        fn "「You're just too nervous.{p}\ \ Come on,{w=.2} lighten up. 」"
        si "「R-right. 」"
        "But Shin-kun stiffened up again,\nand he's being clumsy all over."
        "It wasn't like he usually was,\nand I tried not to think about the jerkiness\nas I moved along with the music next to him."
    
        show si 406 big night at center_big with dis
        play sound bosu32
        
        si "「Ah. 」"
        fn "「Oh-{w} Are you okay? 」"
        "Suddenly Shin-kun tripped,\nand he fell in front of me."
        
        show si 411 big night with dis
        
        si "「S-sorry.{p}\ \ I tripped over my feet.{w} {nw}"
        hide si
        show si 401 night at center
        with dis
        extend " I'm okay. 」"
        "Shin-kun got back up in a flash,\nthen got back to his awkward movements\nas he tried to mimic everyone else's moves."
        fn "「Your shoulders are stiffening up again. 」"
        
        show si 406 night with dis
        pause .5
        show si 411 night with dis
        
        si "「It's probably because there's so many people.{p}\ \ It makes me kind of nervous. 」"
        fn "「Come on, relax more. 」"
        si "「O-okay. 」"
        "And he goes back to awkward and clumsy.{p}This is so unlike him.\nHe hesitantly looked around,"
        "frantically trying to imitate the movements\nas he feigned calmness, and for a little\nwhile I danced together with and aside him."
    
        scene black with sdis
        scene festival_stands
        show si 410 at center 
        with sdis
        
        si "「Whew... 」"
        fn "「You did well Shin-kun. 」"
        
        show si 401 with dis
        
        si "「Yeah.{p}\ \ {nw}"
        show si 409 with dis
        extend "...I really did look odd, didn't I? 」"
        fn "「You did good.{p}Wait, it wasn't even a competition anyways. 」"
        
        show si 401 with dis
        
        si "「... 」"
        
        show si 409 with dis
        
        si "「... 」"
        "He didn't really fall that often."
        fn "「It's just the Bon Festival dance.{p}No need to take it so seriously, just relax.{p}Come on, {w=.2}looser,{w} {cps=5}looser. 」"
        "I acted like an octopus, flopping around\nas I relaxed every muscle in my body."
        
        show si 401 with dis
        
        si "「... 」"
        
        show si 402 with dis
        
        si "「What is that,{p}\ \ I feel strange when I'm with you? 」"
        
        show si 401 with dis
        
        si "「If you try to encourage with a face like that,\n\ \ won't I look idiotic? 」"
        "...{w} he's so casually mean."
        
        show si 402 with dis
        
        si "「I really do look like an idiot.{p}\ \ Back when... 」"
        
        pause .5
        show si 409 with dis
        
        "Shin-kun trailed off there."
        fn "「Shin-kun? 」"
        
        stop music fadeout 1
        pause 1
        
        show si 401 with dis
        
        si "「Oh, sorry.{p}\ \ I was thinking about when I was young. 」"
    
        play music piano4_001 fadein 1
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        
        fn "「The time you moved here? 」"
        
        show si 410 with dis
        
        si "「A bit more on after that, I guess.{p}\ \ {nw}"
        show si 409 with dis
        extend "The time my mother and father came to visit. 」"
        fn "「Oh.{p}\ \ What happened? 」"
        
        show si 401 with dis
        
        si "「You want to know? 」"
        fn "「Yeah. 」"
        
        show si 410 with dis
        
        si "「I said it was when I was young,\n\ \ but my parents work somewhere a bit bigger.{p}\ \ {nw}"
        show si 401 with dis
        extend "A zaibatsu, {w=.2}a combine, {w=.2}something like that. 」"
        si "「They're the CEOs of it.{p}\ \ {nw}"
        show si 410 with dis
        extend "Simply put, {w=.2}they're big shots of the rich.{p}\ \ {nw}"
        show si 409 with dis
        extend "Because of that, they seldom ever come here. 」"
        
        show si 401 with dis
        
        si "「Even so, back then they came\n\ \ to visit me sometimes.{p}\ \ {nw}"
        show si 409 with dis
        extend "They used a short vacation. 」"
        fn "「Huh. 」"
        "That reminds me,\nI vaguely remember seeing a big black car\nin front of his house a few times."
        "I can't remember who rode it,\nbut it's probably that time."
        si "「...{w=.2}{nw}"
        show si 401 with dis
        extend "that day was the first day\n\ \ I baked a cookie all by myself.{p}\ \ All starting from making the dough onwards. 」"
        
        show si 402 with dis
        
        si "「I wanted to surprise them by saying{w=.2}\n\ \ 'I did it all by myself.' 」"
        
        show si 401 with dis
        
        si "「It was a success.{p}\ \ Both of them thought Amaki made it.{p}\ \ {nw}"
        show si 409 with dis
        extend "...{w=.2}it made me happy. 」"
        
        show si 401 with dis
        
        si "「They said it was good.{p}\ \ {nw}"
        show si 402 with dis
        extend "They enjoyed something I did.{p}\ \ {nw}"
        show si 409 with dis
        extend "Even so, I failed at the very end. 」"
        fn "「You failed? How? 」"
        
        show si 401 with dis
        
        si "「...{w} {nw}"
        show si 410 with dis
        extend "because I was a child.{p}\ \ {nw}"
        show si 409 with dis
        extend "It became night, and in front of them as {w=.2}\n\ \ they turned to leave, I cried. 」"
        si "「I should have been able to see them off,{w=.2}\n\ \ I should have understood that in my head,{w=.2}\n\ \ and I thought hard about what I'd say. 」"
        si "「But why didn't the tears stop?{p}\ \ I ended up bothering them. 」"
        fn "「... 」"
        si "「I should have known it in my head,\n\ \ but I didn't, not very well.{p}\ \ Somehow, I'm comparing that time to now. 」"
        "I...{w=.2} see.{p}I wonder, has Shin-kun\nnever depended on his parents?"
        "No wait,{w=.2} even if he did, he probably couldn't."
        "He's always aloof by himself, almost as if\nhe's saying he can do anything himself,\nbut maybe that's the cause of it."
        
        stop music fadeout 1
        pause 1
        play music festival_ambience fadein 1
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")    
        show si 401 with dis
        
        si "「...why did I tell you something like this?{p}\ \ {nw}"
        show si 403 with dis
        extend "Sorry for the stupid story. 」"
        fn "「No...{w} um. 」"
        
        show si 401 with dis
        
        si "「Would you please keep that story a secret?{p}\ \ {nw}"
        show si 410 with dis
        extend "Really, why did I tell you that? 」"
        
        show si 401 with dis
        
        si "「Sorry for putting a damper on things.{p}\ \ Instead, {w=.2}{nw}"
        show si 402 with dis
        extend "shall we enjoy the festival?{p}\ \ There's still some food carts we haven't visited. 」"
        "Food carts...{w} wait what!?{w} Oh crap!{p}The mood was so solemn until now,\nbut going around the food carts again is..."
        
        play sound bom35
        
        fn "{size=+15}「Give me a break on the sweets! 」"
        
        show si 401 with dis
        
        si "「? 」"
        fn "「Oh, uh. 」"
        "Dammit!{p}I just said what was on my mind aloud!"
        
        show si 410 with dis
        
        si "「Now that you mention it,\n\ \ everything we had until now was sweet.{p}\ \ {nw}"
        show si 401 with dis
        extend "Sorry, was that hard on you? 」"
        fn "「{cps=5}Uhhhhhhh, no? {cps=40}{w} Ahaha... 」"
        
        show si 410 with dis
        
        "I tried to force myself to laugh,\nbut I guess that won't work anymore."
        si "「Why didn't you just tell me? 」"
        fn "「I didn't want to ruin the mood.{p}\ \ It's the summer and all. 」"
        
        show si 401 with dis
        
        si "「If you forced yourself,\n\ \ wouldn't your priorities be wrong? 」"
        
        show si 403 with dis
        
        si "「How come you use consideration\n\ \ in the strangest places? 」"
        fn "「Sorry. 」"
        
        show si 410 with dis
        
        si "「You aren't to blame.{w} {nw}"
        show si 404 with dis
        extend "{p}{nw}"
        show si 401 with dis
        extend "You could've just spoken shamelessly like always. 」"
        "Shameless he says?{p}Is that how I'm always seen?{p}That's kind of depressing."
        
        show si 402 with dis
        
        si "「Since before, you and everyone else would\n\ \ always speak to me without restraint or care.{p}\ \ I like the you that doesn't mince manners. 」"
        fn "「What? 」"
        
        show si 401 with dis
        
        si "「?{p}\ \ {nw}"
        show si 406 with dis
        extend "Eh- {w=.2}N-no.{w} Not like that.{p}\ \ {nw}"
        show si 411 with dis
        extend "I don't get it,{w} today's been so strange. 」"
    
        hide si with wipe_right
        
        fn "「Ah, hey, Shin-kun,{w=.2} wait! 」"
        "Shin-kun ran off as his face was completely red,\nand I ran off after him a second later\nin confusion."
    
        scene black with sdis
    
    #####################################################
    label shin22_fireworks:
        
        $ event_name = "His smile illuminated by the flower in the sky"
        
        stop music fadeout 1
        pause 1
        play music festa01 fadein 1
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        
        "We passed the time with this and that,"
    
        scene festival_stands with dis
        play sound fireworks_explosion
        show fireworks
        
        "and as we took aim with our rifles,\na loud sound rung out along with some lights\ndifferently colored from the lighting."
        "The fireworks started."
        
        show si 401 at center with dis
        
        si "「Looks like the fireworks have begun. 」"
        fn "「Yeah...{p}\ \ {nw}"
        play sound puu79_b
        extend "....ahh, almost! 」"
        
        show si 404 with dis
        
        "I hit the target,\nbut it was more of a graze than a bull's eye."
        "「Oh, so sorry. 」"
        "I used up all my shots so\nI gave back the gun to the proprietor.{p}Come on, I was so damn close."
        
        show si 401 with dis
        
        si "「Did you really want that stuffed animal? 」"
        fn "「Not so much, but it just annoys me so much. 」"
        si "「But you didn't actually want it though, no? 」"
        fn "「Yeah, I guess so.{p}\ \ But doesn't it make you want to aim high? 」"
        
        show si 410 with dis
        
        si "「Is that so? 」"
        "Shin-kun cocked his head in thought\nas he ate his free caramel.{p}Don't they say 'men should dream big?'"
        "Well even if I do say that, I'd probably get\n'if you can't get results isn't it pointless?'\nas an answer, so I'll just shut up for now."
        
        play sound fireworks_explosion
        show fireworks
        
        fn "「Well that's a good stopping point,\n\ \ so shall we go somewhere else? 」"
        
        show si 401 with dis
        
        si "「Alright. 」"
        
        $ renpy.music.set_volume(0.6, 1.0, channel = "music")
        scene black with wipeleft
        scene forest01 night with dis
        
        "Around here might be good.{p}The two of us took places next to a forest\nthat was a bit away from the festival lights."
        "Since we were away from the grounds,\nthere weren't many people around.{p}It's a pleasant secret place."
        
        play sound fireworks_explosion
        show fireworks
        
        show si 401 night at center behind fireworks with dis
        
        si "「How beautiful. 」"
        fn "「Yeah. 」"
        
        show si 402 night with dis
        
        si "「I've always watched from my room's window,\n\ \ but there's something about seeing it close. {w=.2}\n\ \ I like it. 」"
        fn "「I see then. 」"
        si "「Yeah. 」"
        
        show si 401 night with dis
        
        si "「[fn]. 」"
        fn "「What? 」"
        
        show si 402 night with dis
        
        si "「Thanks for inviting me.{p}\ \ A lot's happened in the time we spent,{w=.2}\n\ \ it was fun. 」"
        "When he spoke to me like that again, it was a bit\nembarrassing.{w} I faltered a bit as I responded\nback to him while he smiled, and said,"
        fn "「Y-you don't need to thank...{p}\ \ I just wanted to come to the festival with you. 」"
        si "「But,{w=.2} it's true I had fun,\n\ \ so I had to tell you that. 」"
        
        play sound fireworks_explosion
        show fireworks
        
        si "「So, thanks. 」"
        fn "「R-really?{p}\ \ Uhh well,{w=.2} you're welcome. 」"
        "All we did was go around together,\neat, and hang out though.{p}I didn't do anything after being thanked again."
        "But...{w=.2} if Shin-kun had fun, isn't that okay?"
        "While I looked at Shin-kun from the side,\nwe raised our eyes up to the\nfireworks blowing in the sky."
        
        if shin_step1 == True and shin_step2 == True:
            jump shin22_hand
        else:
            jump end22
    
    #########################################################
    label shin22_hand:
        
        stop music fadeout 1
        pause 1
        play music free31
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        
        show si 409 night with dis
        
        si "「...{w} {nw}"
        show si 401 night with dis
        extend "[fn] 」"
        fn "「Yeah.？ 」"
        
        show si 409 night with dis
        
        si "「Can I...{w=.2} take your hand? 」"
        fn "「Eh? 」"
        "When I looked at Shin-kun after his sudden request,{w=.2}\nhe cast his eyes down in the darkness,\nstaring at his own feet."
        
        play sound fireworks_explosion
        show fireworks
        
        "That profile when the fireworks shot up,\nit somehow felt really lonely.{p}After being fired it'd soon disappear..."
    
        show si 406 night at jump_up
        
        si "「Ah- 」"
        "I tightly grabbed his left hand.{p}He probably couldn't see in this darkness,\nbut I smiled at Shin-kun as I spoke."
        fn "「How's this? 」"
        
        show si 411 night with dis
        
        si "「O-okay... 」"
        "In the dark it was gentle,\nbut I'm sure I felt the soft hand grabbed back."
        
        show si 413 night with dis
        
        si "「Thank you, [fn]. 」"
        
        play sound fireworks_explosion
        show fireworks
        
        $ shin_key3 = True 
        
        jump end22
    
######################################################
label juuichi22:
    
    $ event_name = "Like a Sudden Flame"
    
    play music free0258
    scene hbroom red with dis
    
    fn "「Will this be okay...? 」"
    "I check myself out wearing a yukata in the full-length\nmirror.{w} It's light blue with a darker blue obi.{w=.2}\nSimple, yet polite."
    "My grandma made this for me just\nfor the summer festival."
    "I refused to wear it at first,\nbut she broke me down in the end."
    "...However, {w=.2}my mind has changed now that I'm wearing\nit.{w} It doesn't cling to my legs as much as I thought\nit would, {w=.2}and it's surprisingly comfortable."
    
    play sound ChimeA
    
    "*Ding dong*"
    "While I'm spinning around like a model,{w=.2}\nI hear the chiming of the doorbell.{w} It seems\nthe one I arranged to with, {w=.2}Juuichi-san, has arrived."
    fn "「Yes yes, {w=.2}I'm coming. 」"
    "I grab my wallet sitting on the desk, {w=.2}exit my room,\nand head towards the entrance. The spending money I\nrecieved from my granpa are my reassuring partner for today."
    
    scene black with wipe_right
    scene hentry red
    show ju 001 red at center
    with wipe_right
    
    ju "「...A yukata? 」"
    "The very first thing out of his mouth is a remark\nabout my clothing.{w} Well, {w=.2}I'm sure it stands\nout compared to my usual clothes."
    fn "「My grandma made me wear it.{p}\ \ ...Is it weird? 」"
    
    show ju 003 red with dis
    
    ju "「Hmm, {w=.2}it's not bad. 」"
    fn "「Heh heh, {w=.2}thanks. 」"
    "He may be flattering me, {w=.2}but it still feels nice to be\ncomplimented by somebody you like.{w} Especially from\nJuuichi-san, who doesn't say things like that very often."
    
    show ju 001 red with dis
    
    ju "「Alright, {w=.2}shall we get going? 」"
    fn "「Sure! 」"
    "Then, we set out to go on our date...{p}er, to the summer festival."
    
    $ event_name = "Harvesting Ritual"

    stop music fadeout 3
    scene black with sdis
    scene rice red
    show ju 001 red at center
    with sdis
    play music free12
    
    ju "「Come to think of it, [ln]. 」"
    "While walking side-by-side,{w=.2}\nJuuichi-san suddenly calls my name."
    fn "「What? 」"
    ju "「Do you know why we have this festival? 」"
    fn "「Huh? 」"
    "I'm caught by suprise by his unexpected question."
    "Uhh, it's just a festival, isn't it...?{p}Is there some kind of reason for having it?"
    "...It's no use, {w=.2}nothing comes to mind at all."
    fn "「I've completely forgot. 」"
    
    show ju 003 red with dis
    
    ju "「Well, {w=.2}things like food stalls had already became\n\ \ mainstays of it by the time you were born. 」"
    "I've heard this story,{w=.2}\nbut after his introduction, Juuichi-san begins."
    
    show ju 001 red with dis
    
    ju "「Originally, {w=.2}it was an occasion to thank the god of\n\ \ the soil for the safey of the crops.{w} A kind of\n\ \ harvest festival, {w=.2}so to speak. 」"
    ju "「It's not well-known to the general public,{w=.2}\n\ \ but it's said that even now the offering ceremony is\n\ \ performed at the shrine. 」"
    ju "「For generations, {w=.2}the Kodori Family has acted as the\n\ \ miko. Apparently Kodori is doing it this year. 」"
    fn "「Wait, {w=.2}you mean Shun-kun? 」"
    ju "「Yes. {p}\ \ He's part of the one of the oldest and most\n\ \ prestigious families in Minasato. 」"
    "Shun-kun's family has traditions like that?{p}It's hard to imagine considering how he acts."
    "But Shun-kun in a miko outfit...?{w} I kind of want to\nsee that.{w} I'm sure it'd look better on him than my\nyukata does on me."
    
    show ju 003 red with dis
    
    ju "「By the way, {w=.2}apparently it's off limits to anybody\n\ \ who's not involved. 」"
    "He shrugs his shoulders.{w} ...That makes sense.{p}Everybody would know about it if it were a big event."
    "A secret ceremony, huh?{p}Who knew Minasato had something like that."
    "And it's really surprising that\nsomebody I'm so familiar with is performing it."
    fn "「Huh,{w=.2}\n\ \ it seems there's a side of Shun-kun I never knew\n\ \ about. 」"
    "He says \"That's right\" to what I blurted out."
    
    show ju 001 red with dis
    
    ju "「I ran into Kodori yesterday, {w=.2}he's excited to be\n\ \ serving as the miko today.{w} {nw}"
    show ju 003 red with dis
    extend " ...I hope he doesn't get\n\ \ overenthusiastic and mess up though. 」"
    "Bite his tongue while reciting the prayer?{p}...That's possible."
    "Stepping on the hem of his hakama and tripping?{p}...That's extremely possible."
    "...Hm.{p}You can do it, Shun-kun! {w=.2}You may not know it,\nbut I'll be cheering you on nearby!"
    
    show ju 001 red with dis
    
    ju "「...Come to think of it, {w=.2}are you sure\n\ \ it's okay that we didn't invite anybody else today? 」"

    show rice red at vshake
    
    "...Ooh.{p}I was ready for it,{w=.2}\nbut has this conversation come at last?"
    fn "「W-{w=.2}well, {w=.2}I went camping with everybody, uhh...{w} this\n\ \ time I wanted to look around the food stalls with a\n\ \ more relaxed atmosphere! 」"
    "I'll never say that I wanted it to be\njust Juuichi-san and I.{w} frantically come up\nwith that while dripping with a cold sweat."
    "I should have thought of an excuse in advance,{w=.2}\nbut I got flustered at this important scene.{p}This would seem like a funny play to an outside viewer."
    
    show ju 003 red with dis
    
    ju "「...I see. 」"
    "Did he really believe that?{p}I sneak a look at his face,{w=.2}\nbut it's that same sullen look he usually has."
    fn "「Juuichi-san...{w} you wanted everybody to come,{w=.2}\n\ \ didn't you? 」"
    
    show ju 001 red with dis
    
    ju "「Yeah...{w} everybody usually gathers at times like\n\ \ these.{w} That's what I assumed was going to happen\n\ \ this time. 」"
    ju "「Oh well, {w=.2}doing this is fine every once in a while\n\ \ too. 」"
    "Thank goodness.{w} I wouldn't have been able to get over\nthe shock of the day when he said he wanted everybody\nto go.{w} I'm sure of it."
    "I sigh with relief quietly so\nJuuichi-san can't hear it."
    ju "「You're awfully fired up today.{p}\ \ ...Don't go overboard just because of the festival. 」"
    "I almost ask him if he's okay,{w=.2}\nbut stop myself."
    "Can he already hear the hustle and bustle of the\nfestival?{w} His rounded ears are twitching.{w} It seems\nlike he's walking faster than he usually does."
    "...He himself probably doesn't realize those things.{p}I have a feeling he'd throw me if I pointed them out,{w=.2}\nso I'll just keep quiet."
    ju "「[ln], {w=.2}are you coming? 」"
    fn "「Oh, {w=.2}yeah I am!{p}\ \ Please don't leave me behind! 」"
    
    $ event_name = "Aimlessly Walking Down the Rows of Stalls"

    stop music fadeout 3
    scene black with sdis
    scene festival_stands with sdis
    play music festa01
    
    "There are people, {w=.2}people, {w=.2}and more people as far as I\ncan see.{w} Seeing the turnout, {w=.2}I can't help but think\n\"Are there this many people living in Minasato?\"."
    "The path leading to the shrine is lined with stalls.{p}The vigorous business phrases flying about\nare just as loud as the children's merrymaking."
    "A sweet and savory aroma wafts through the area.{p}I'm on the verge of a knockout{w=.2}\nfrom all five of my senses being tempted."
    fn "「Wow...{w=.2} There's so many people. 」"
    
    show ju 002 at center with dis
    
    ju "「This is a village with little entertainment.{w} I don't\n\ \ think it's that strange for everyone in it to\n\ \ gather. 」"
    fn "「You're right.{p}\ \ It really does seem like the whole village is here. 」"
    "I take a quick look at Juuichi-san's face.{p}It seems to me... {w=.2}his mouth is very relaxed.{p}It's like he can't hide what a good mood he's in."
    "It might be impolite to say it, but he looks cute...{p}Considering how he normally looks,{w=.2}\nit's hard to imagine him like this."
    "Is that what makes it so attractive?"
    
    show ju 001 with dis
    
    ju "「So, {w=.2}where should we go? 」"
    fn "「It doesn't matter, {w=.2}let's go to all of them!{p}\ \ I've got plenty of money! 」"
    "I pull my wallet out of one of my sleeves.{p}Seeing that it's fuller than usual,{w=.2}\nJuuichi-san slowly nods."
    ju "「How reliable.{p}\ \ Looks like we won't have to worry about running out. 」"
    fn "「Heh heh heh,{w=.2}\n\ \ I'll pay for everything if you don't mind! 」"
    ju "「Don't get too carried away or it'll be empty before\n\ \ you know it. 」"
    fn "「Yeah, I'll be careful.{p}\ \ Oh, {w=.2}let's go take a look at the\n\ \ cotton candy stall on the end! 」"
    
    show ju 003 with dis
    
    ju "「You really are...{w} {nw}"
    show ju 002 with dis
    extend "Fine. 」"
    "After pushing through the crowd, {w=.2}we arrive at the\nstall.{w} Colorful bags stuffed with cotton candy are\narranged under the roof."
    "Noticing us approaching the stall,{w=.2}\nthe person running it briskly calls out to us."
    attendant "「Hey, {w=.2}come on up! 」"
    
    show ju 001 with dis
    
    ju "「Two please.{w} Any color is fine. 」"
    attendant "「Thanks! {w=.2}It's one thousand yen for two. 」"
    "As I reach to pull money out of my wallet,{w=.2}\nJuuchi-san shakes his head."
    ju "「I'll take this one. 」"
    fn "「No, {w=.2}don't do that. 」"
    "I can actually afford it today,{w=.2}\nso I should be allowed to splurge a little."
    
    show ju 003 with dis
    
    ju "「... 」"
    "Juuichi-san grabs my hand, {w=.2}and forces a 500 yen coin\ninto my wallet.{w} Then he takes a 1000 yen bill out of\nhis own wallet and quickly hands it to the man in the stall."
    attendant "「Thanks again! 」"
    
    show ju 001 with dis
    
    "Juuichi-san recieves the two bags of cotton candy,{w=.2} and\noffers one to me.{w} ...Hmm,{w=.2} did turning down his offer\nmake him lose face?"
    "I say thanks and quietly take it.{w} Then I undo the\nrubber band keeping the bag closed,{w=.2} and, after a bit\nof trouble, {w=.2}take all the cotton candy out of it."

    hide ju with dis
    
    "...I tear off a piece and eat it,{w=.2}\nbut my hand gets all sticky.{p}I wish I would've brought some moist towelettes."
    "...No, {w=.2}there's no use crying over spilt milk!{p}I boldly take another huge bite of cotton candy."
    "The fibers melt on my tongue and disappear.{p}Cotton candy really does go well with festivals."
    fn "「Juuichi-san, {w=.2}this tastes great...{w} huh!? 」"
    
    show ju 016 at center with dis
    
    ju "「It does. 」"
    "There's a reason why my sentence ended that way.{w} My\neyes were off him for what should have been just a few\nseconds,{w=.2} but a mask is now on Juuichi-san's face."
    "When did he buy it?"
    "Juuichi-san may be a bear,{w=.2}\nbut that cute,{w=.2}\ndeformed bear face on him is downright surreal."
    "As I'm frozen in place, Juuichi-san extends his hand\ntowards me.{w} Then, he quickly brushes his index finger\non the corner of my mouth."
    ju "「You had some stuck there. 」"
    fn "「Oh, {w=.2}sorry.{w} Thanks. 」"
    
    show ju 017 with dis
    
    ju "「...Hm. 」"
    
    if meet_ten == True:
    
        "...Oh.{p}That reminds me, {w=.2}is it alright for him to be eating\nsweets?{w} He's supposed to be losing weight..."
        fn "「Juuichi-san, {w=.2}are you sure you can eat cotton candy?{p}\ \ After every thing Ten-san said? 」"
        
        show ju 016 with dis
        
        ju "「I don't think it'll be a problem if I go at this\n\ \ pace...{w} But you can never be too careful, {w=.2}right? 」"
        "He holds his bag of cotton candy in his left hand,{w=.2}\nand hands me a plastic bag with his right."
        "...Huh? What did he have besides the cotton candy?{w} I\nexamine the bag's contents with a look of confusion on\nmy face,{w=.2} and find 2 candy apples and 2 apricot candies."
        "...He really is weak for sweets.{p}It looks like saying something to him was the right\nthing to do."
        
        show ju 017 with dis
        
        ju "「... 」"
        "I'm sure he's making a disappointed look under that\nmask. But it's all in vain, I have to\nput my foot down in situations like this!"
        "For some reason I feel like his... no,{w=.2}\nthe judo club's manager."

    
    who "「Oh, {w=.2}good timing. 」"
    "Then, {w=.2}I hear a familiar voice from behind.{w} I turn\naround and and Tatsu-nii standing there not wearing\nhis usual outfit, but rather festival clothes."
    
    hide ju with wipe_right
    show ju 016 at midleft
    show ta 501 at midright
    with wipe_right
    
    ta "「Yo, {w=.2}Juuichi and [fn]. 」"
    fn "「Oh, {w=.2}Tatsu-nii.{w} That happi coat looks good on you. 」"
    "He smiles shyly at my compliment."
    
    show ta 507 with dis
    
    ta "「And what about you!{w=.2}\n\ \ That yukata you're wearing is totally turning me on! 」"
    fn "「T-{w=.2}turning you on...? 」"

    show festival_stands at vshake
    play sound bosu26_b
    
    "He pats my back as hard as he can.{p}...I can't scream in public though.{p}Jeez, {w=.2}he's the same as ever."
    ju "「What did you mean {w=.2}\"good timing\"? 」"
    "Juuichi-san questions Tatsu-nii.{p}He did say that when he saw us, {w=.2}didn't he?"
    
    show ta 508 with dis
    
    ta "「Well, as a matter of fact...{p}\ \ my dad's wasted, {w=.2}so we don't have\n\ \ enough people to build the tower for the dance. 」"
    fn "「What!? 」"

    show ta 502 with dis
    
    "Tatsu-nii laughs like he usually does, {w=.2}but...{p}but this sounds like a terrible situation to me!"
    "A Bon dance with out the tower.{p}I've never seen such a thing."

    show ta 501 with dis
    
    ta "「I wasn't sure what to do, but...{p}\ \ then I happened to come across Juuichi.{p}\ \ That's what I call lucky. 」"

    show ta 510 with dis
    
    ta "「Sorry it's so sudden, {w=.2}Juuichi,\n\ \ but do you mind helping us put it together? 」"
    fn "「Whaaat!? 」"
    "But I finally get to be Juuichi-san!{p}The sudden appearance of this ambush\nmakes me yell."
    
    show ju 017 with dis
    
    ju "「Sure, {w=.2}but today [ln] and I... 」"

    show ta 509 with dis
    
    ta "「Then it's settled.{p}\ \ Now, {w=.2}stop complaining let's get it built! 」"
    ju "「T-{w=.2}Tatsu-san... 」"
    "Tatsu-nii... his mouth is smiling but his eyes aren't.{p}This is serious. {w=.2}It's Tatsu-nii when he's seriously\nreading and writing."
    fn "「Alright then, {w=.2}I'll help too.{p}\ \ Then it'll get done faster, right? 」"
    "That's right, {w=.2}I should have said that right from the\nstart.{w} I don't like that our alone time is shrinking,{w=.2}\nbut our time together shrinking is even worse."
    "With my help it'll be done in a matter of minutes.{p}It's a pretty good suggestion if I do say so myself.\nI wait for Tatsu-nii's reply with a pleased look on my face."

    show ta 506 with dis
    
    ta "「Uh...{w} if this were any other time I'd say sure,{w=.2}\n\ \ but this isn't a small job. 」"
    fn "「Aw, {w=.2}why can't I? 」"
    "He makes a troubled expression\nand scratches at his head.{p}I flare up at him."

    show ta 505 with dis
    
    ta "「Well, {w=.2}each of the parts are extremely heavy.{p}\ \ So it'd be, {w=.2}uh, {w=.2}a huge load for you. 」"
    "The rest he mumbles and speaks in a low voice\nthat I can't hear very well,{w=.2}\nbut even I get what he means."
    "...So wait here by myself?"
    "It'll be loney looking around the stalls without\nJuuichi-san,{w} but the Bon dance is an important part\nof the summer festival, a lot of people will be"
    "disappointed if it's cancelled."
    "I'll just have to put up with it.{p}I sigh in my head."
    "Well, {w=.2}it shouldn't take too long if\nthey're just putting it together..."
    fn "「...Fine.{w} I'll go browse the food stalls. 」"
    ju "「[ln], {w=.2}I'm sorry... 」"
    fn "「No, {w=.2}this is a pain for you too. 」"
    
    show ju 016 with dis
    
    ju "「You can say that again. 」"

    show ta 509 with dis
    
    ta "「Come on, {w=.2}let's go Juuichi! 」"
    ju "「I'll be back later. 」"
    fn "「Juuichi-san, {w=.2}please do your best! 」"

    scene festival_stands with wipe_right
    
    "With a short \"sure\" as his reply,{w=.2}\nTatsu-nii leads him into the crowd and disappears."
    "...Leaving me standing alone.{p}Well, there's no sense in just standing around, right?{p}I pull myself together and head towards the stalls."
    
    if meet_ten == True:
        $ event_name = "Ritual of Protection"
        
        "...Actually, before that,{p}I think I should store these sweets I have in my\nstomach."
        "I restlessly look around for vaccant bench.{p}An elderly couple is using the one over there,{w=.2}\nand a family with little kids are using one over there."
        "Hmm, {w=.2}I guess I don't have a choice.{p}I'll wait a bit for one to become available."
        "I sigh in dejection.{p}Just then, {w=.2}a familiar yet unexpected\nfigure comes into my field of vision."
        fn "「Ten-san! 」"
        
        show tn 001 at center with dis
        
        tn "「Oh, {w=.2}it's you? 」"
        fn "「You go to festivals like this too, {w=.2}huh?{p}\ \ I was sure you'd be training today too. 」"
        tn "「I wanted to,{w=.2} but there's an event that I need to\n\ \ participate in.{w} I'm just here for that. 」"
        fn "「Oh, {w=.2}there's some kind of duty you have to perform? 」"
        tn "「Correct.{w} {nw}"
        show tn 002 with dis
        extend " Someone must take in the evil spirits that\n\ \ approach the one performing the ceremony,{w=.2} and led it\n\ \ to a succesful completion.{w} That is my role. 」"
        "Besides the offering ritual, {w=.2}there's a ritual\nto pray for the safety of the one performing it?{p}A ritual for a ritual? That's surprisingly complex."
        fn "「Wait, {w=.2}evil spirits...? 」"
        
        show tn 001 with dis
        
        tn "「That doesn't mean real monsters are going to appear.{p}\ \ A random villager is selected to play the part of the\n\ \ evil spirit. 」"
        tn "「And I just confront that person impersonating it. 」"
        "So in short it's divided into the confrontation and\nextermination of the monster?{w} That seems like a fun\ngame of playing exorcist.{w} I want to try that too."
        
        show tn 002 with dis
        
        tn "「...Well, {w=.2}that's about the gist of it. 」"
        fn "「Is it alright for you to participate in the festival\n\ \ with your judo gi still on though? 」"
        
        show tn 001 with dis
        
        tn "「Yes.{w} ...It'll get dirty anyways. 」"
        "For some reason, {w=.2}he's more intense than I imagined.{p}But it is his role to protect the practitioner,{w=.2}\nso he might as well do it with pizazz."
        "They sure did have a lot of superstitions\nwhen this festival began."
        fn "「Um, about that ceremony- 」"
        tn "「That's off-limits. 」"
        "He closes me down before I can finish.{p}Hm, it seems Shun-kun is off-limits too,{w=.2}\nbut it was worth a try."
        "It's only human nature to want to have just at least\na peek at something that's hidden from them."
        
        show tn 003 with dis
        
        tn "「...I understand how you feel, {w=.2}but don't even think\n\ \ about following me.{w} If I sense{w=.2} your presence at that\n\ \ time, I'll tear your head from your torso. 」"
        "...Whoa,{w=.2}\nthose look like the eyes of somebody who could kill.{p}I'll just quietly stay over here by the food stalls."
        
        show tn 001 with dis
        
        tn "「Mikazuki will probably come to the festival,{w=.2}\n\ \ but keep a close eye on him.{p}\ \ You must not let him eat sweets. 」"
        "...{p}If Juuichi-san bought all these snacks I'm holding,{w=.2}\nthen I'll have hell to pay."
        "Let's not tell Ten-san about this."
        fn "「I understand,{w=.2}\n\ \ I'll tell him to be careful if I see him. 」"
        
        show tn 005 with dis
        
        tn "「I'm counting on you. 」"
        
        hide tn with dis
        
        "Leaving me with that,{w=.2}\nTen-san disappears into the crowd."
        "If I hadn't moved away from Minasato,{w=.2} I might have\nbeen able to participate in that ceremony.{p}Now I'm feeling pretty bitter about it."
        "But that's all in the past now.{p}I look at my hands.{p}Alright,{w=.2} let's finish the cotton candy for now."


    $ event_name = "Boy Meets Tiger"

    $ renpy.music.set_volume(0.4, 3.0, channel = "music")
    scene black with sdis
    scene festival_stands with sdis
    
    "While taking a bit of my candy apple, I walk around\nthe lined up stalls.{w} Usually I waste my pocket money\nat an alarming pace,{w=.2} but I don't feel like I am now."
    "I wonder if they're done building it yet...{p}That's what I think about as I stand there vacantly."
    "But Juuichi-san left not too long ago.{p}They wouldn't be done already."
    "Oh well, {w=.2}how should I kill time?{p}Err, where were the shops?{p}As I restlessly look around the grounds,"
    who "「Ah, {w=.2}if it isn't [fn]! 」"
    "A voice suddenly calls out ot me from behind.{w} I don't\nneed to turn around,{w=.2} I already know who that voice\nbelongs to.{w} ...To be I honest, {w=.2}I wish I didn't know."

    $ renpy.music.set_volume(0.75, 3.0, channel = "music")
    show to 001 at center with dis
    
    fn "「Oh...{w} Torahiko's here too. 」"
    "Last time things were a little awkward between us.{p}How should I talk to him?{p}As I muster up my wits,"
    
    show to 002 with dis
    
    to "「Hey, {w=.2}it only happens once a year, right!? 」"
    "I see him put his hands on his hips with a hearty\n\"Gahaha\"."
    
    show to 010 with dis
    
    to "「But still, {w=.2}a yukata?{p}\ \ You're looking more seductive than usual. 」"
    fn "「Uhh, {w=.2}what was that? 」"
    
    show to 006 with dis
    
    to "「Aw come on, {w=.2}I'm trying my best to compliment you.{p}\ \ {nw}"
    show to 003 at jump_up
    extend "You don't like it? 」"
    "He looks right at me with a discouraged expression.{p}I don't think there are very many guys\nwho would like to be called \"seductive\"."
    "But besides that...{w} his expression keeps changing,{w=.2}\nhe's almost too much like his usual self."
    "Did that confession never happen and it was just a\ndream?{w} I'd remember something like that."
    "Am I the only one who is conscious of what happened\nthat day...?"
    fn "「I think that's something you'd say to a girl.{p}\ \ Although Tatsu-nii did say something similar to me\n\ \ earlier. 」"
    
    show to 007 with dis
    
    to "「Damn, {w=.2}Tatsu-nii beat me too it? 」"
    fn "「That's not the problem though. 」"
    
    show to 013 with dis
    
    to "「That's something I can't help but say when the,{w=.2}\n\ \ uh...{w} guy I love looks like that. 」"
    "He hangs his head down, {w=.2}but he says that with red\ncheeks.{w} ...I see.{w} I've finally realized it."
    "He's trying to make it so that day never happened,{w=.2}\nand behaving the same way he always has..."
    "If I were in his place,{w=.2}\nwould I do the same thing?"
    fn "「You should say something like \"cool\" or \"handsome\",{w=.2}\n\ \ that'd be better. 」"
    "My reply is forced as well.{p}But that's just speaking for myself,{w=.2}\ndid he think my tone was awkward just now?"
    
    show to 007 with dis
    
    to "「You aren't those types. 」"
    fn "「And yet you're so cheeky! 」"
    "My eyes meet Torahiko.{p}we both stare for a short time...{w=.2}{nw}"
    show to 002 with dis
    extend "\nThen, {w=.2}unable to stand it, {w=.2}we speak at the same time."
    
    scene black with sdis
    scene festival_stands with sdis
    show to 001 at center with dis
    
    to "「So, {w=.2}[fn] did you come here by yourself? 」"
    fn "「I wouldn't be wearing a yukata if I was alone.\n\ \ I'd just look like an idiot. 」"
    to "「Really?{p}\ \ {nw}"
    show to 006 with dis
    extend "But I don't see anybody else with you. 」"
    "Juuichi-san was next to me a short while ago!{p}I never thought he'd be taken away by Tatsu-nii\nthough..."
    fn "「He had some business to take care of,{w=.2}\n\ \ so he's not here now. 」"
    
    show to 010 with dis
    
    to "「Oh I see, {w=.2}did you get dumped right away? 」"
    fn "「No I didn't. {w=.2}Sorry to disappoint you. 」"
    "I haven't gotten to the point where I can talk about\nbeing dumped or anything like that."
    "Even though I was excited about this being a date,{w=.2}\nthat was just my wishful thinking."
    "But it's the same if I screw up the relationship\nwe have now... at least I think it is.{w} Maybe the\ndistance between us now is just right."
    
    show to 006 with dis
    
    to "「Huh, {w=.2}I see...{p}\ \ You were looking so lonely that I was sure you had\n\ \ been dumped or something. 」"
    "...Did I look that way?{p}I didn't notice at all, {w=.2}I need to be careful of that."
    "Then, {w=.2}Torahiko suddenly makes a meek expression,"
    
    show to 007 with dis
    
    to "「...Is that person we're talking about the one you\n\ \ like? 」"
    "and throws that question at me."
    fn "「...Yeah 」"
    "I thought about just going with a \"no comment\",{w=.2}\nbut he'd find out sooner or later so I decide to be\nhonest."
    
    show to 003 with dis
    
    to "「I wonder who that lucky person is. 」"
    fn "「You don't expect me to say, {w=.2}do you? 」"
    
    show to 005 with dis
    
    to "「What? You talked about it this far,{w=.2}\n\ \ saying his name wouldn't be that weird.{p}\ \ You're so stingy. 」"
    fn "「It's okay to be stingy. 」"
    
    show to 003 with dis
    
    to "「It's kind of pathetic that you won't tell me\n\ \ even though you're a man, {w=.2}isn't it? 」"
    fn "「Sorry, {w=.2}I'm a pathetic man. 」"
    
    show to 007 with dis
    
    to "「...Tch. 」"
    "He shows his disappointment.{p}However, suddenly he puts on a big, mischevious grin.{p}...I've got a bad feeling about this."
    
    show to 010 with dis
    
    to "「Well. {w=.2}whatever.{p}\ \ I'll be talking to you like this even when he comes\n\ \ back. 」"
    fn "「...! 」"
    "Dammit, {w=.2}I completely forgot about that.{p}I need to get Torahiko to go away."
    fn "「T-{w=.2}Torahiko... takoyaki!{p}\ \ I know, {w=.2}do you want to get some takoyaki? 」"
    "My voice shakes as I try to win him over.{p}If I know Torahiko, {w=.2}I'm sure food will lure him...!"
    
    show to 003 with dis
    
    to "「No thanks. 」"
    "It didn't work."
    
    show to 006 with dis
    
    to "「What're you getting so impatient about?{p}\ \ The more you try to hide it from me,{w=.2}\n\ \ the more I wanna know. 」"
    fn "「B-{w=.2}but... 」"
    to "「It's no big deal, {w=.2}just say it already.{p}\ \ {nw}"
    show to 010 at jump_up
    extend "...Oh, {w=.2}senpai! 」"
    "Then, {w=.2}he suddenly removes his eyes from me and looks\nbehind me."
    "No way.{p}I wanted him to come back soon,{w=.2}\nbut not right now...!"
    "I move like a robot that needs oiling as I turn around.{p}Sure enough, {w=.2}Juuichi-san is there."

    show ju 016 at midleft
    show to 001 at midright
    with wipe_right
    
    ju "「Sorry, {w=.2}did I keep you waiting?{p}\ \ {nw}"
    show ju 017 with dis
    extend "...Oh, Tora's here too? 」"
    to "「We ran into each other just a little bit ago, {w=.2}{nw}"
    show to 010 with dis
    extend "right? 」"
    "I shake my head in denial.{w} What should I do? {w=.2}I want to\nget away from this situation.{w} But my mind goes blank\nand I can't think of anything."
    
    show to 007 with dis
    
    to "Senpai,{w=.2}\n\ \ what's with that tacky bear mask you have on? 」"
    ju "「...It doesn't look good on me? 」"
    to "「No not at all.{w} Your large body and that cuteness\n\ \ combined is just about enough to break some sort of\n\ \ rule.{w} Kids are crying. 」"
    ju "「... 」"
    
    show ju 003 with dis
    
    "Juuichi-san removes the mask in silence."
    
    show to 001 with dis
    
    to "「By the way, {w=.2}you said you were keeping him waiting\n\ \ just now,{w} does that mean you and fn were\n\ \ planning on meeting up? 」"
    ju "「No, {w=.2}we were looking around the stalls together a\n\ \ short while ago,{w=.2} but Tatsu-san needed me to help\n\ \ with the tower. 」"
    "I would say this is a situation that ended before\nanything started.{w} I think I was paralyzed in the head."
    "Timidly, I look at Torahiko.{p}Although I was sure he was going to make fun of me,{w=.2}\nhis face looks somewhat lonely."
    
    show to 006 with dis
    
    to "「...Oh I see, {w=.2}senpai, {w=.2}huh?{p}\ \ I'm definitely no match for him. 」"
    
    show ju 008 with dis
    
    ju "「Hm? {w=.2}Did you just say something? 」"
    
    show to 001 with dis
    
    to "「No, {w=.2}I just thought it was weird for you to be late.{p}\ \ So that's what happened? 」"
    
    show ju 011 with dis
    
    ju "「His father being such a bad drunk sure does cause\n\ \ problems. 」"
    
    show to 007 with dis
    
    to "That runs in the Midoriya family, huh?{p}\ \ Tatsu-nii gets scary when he's drunk too. 」"
    ju "「...Definitely.{p}\ \ {nw}"
    show ju 001 with dis
    extend "Anyways, {w=.2}are you by yourself today Tora?{p}\ \ You can come with us if you want. 」"
    "!{p}That word finally snaps me back to life."
    "It would be fun if Torahiko came along,{p}but my reason for only inviting Juuichi-san\nwill be lost..."
    
    show to 001 with dis
    
    to "「Nah, {w=.2}sorry.{p}\ \ I need to get back home soon to help my family out. 」"
    fn "「...Torahiko? 」"
    "What about our discussion we had earlier?{p}When I stare at him in amazement,{w=.2}{nw}"
    show to 010 with dis
    extend "\nhe awkwardly winks at me."
    "Torahiko..."
    ju "「I see, {w=.2}we shouldn't be keeping you here then. 」"
    
    show to 001 with dis
    
    to "「Too bad for me.{p}\ \ This could've been a day when finally you buy stuff\n\ \ for me. 」"
    
    show ju 011 with dis
    
    ju "「...Tora, {w=.2}I'm sure I told you before that I'd never\n\ \ treat you again because you'll get carried away and\n\ \ overeat. 」"
    
    show to 005 at jump_up
    
    to "「Aww, {w=.2}come on! 」"
    
    show ju 001 with dis
    
    ju "「Talking like that isn't going to help. 」"
    
    show to 006 with dis
    
    to "「...Tch.{p}\ \ {nw}"
    show to 010 with dis
    extend "Then please treat me if I break my personal record at\n\ \ the next swim meet. 」"
    
    show ju 003 with dis
    
    ju "「...I'll think about it. 」"
    to "「Aw yeah! {w=.2}I won't forget you said that!{p}\ \ {nw}"
    show to 001 with dis
    extend "...Wait, {w=.2}am I talking too much?{p}\ \ I really do need to get back soon. 」"
    
    show ju 001 with dis
    
    ju "「Alright then, {w=.2}be careful. 」"
    "Torahiko walks up next to me,{w=.2}\nand whispers in my ear."
    to "「...Go get'em, {w=.2}champ. 」"
    "In what seems like an instant, {w=.2}my face turns red."
    
    scene festival_stands with wipe_right
    show ju 001 at center with wipe_right
    
    "He pats me on the shoulder once,{w=.2}{nw}"
    play sound step01
    extend "\nand starts walking towards the exit of the grounds."
    "Hmm, {w=.2}I didn't mean to make him worry about me."
    "However, {w=.2}Torahiko eventually found out\nthat Juuichi-san is the person I love...{p}Could you call this some sort of tie?"
    "...It feels like the scope of our conversation was\ndifferent,{w=.2} but I won't think too deeply for now."
    
    show ju 003 with dis
    
    ju "「...He seemed more restless than usual. 」"
    fn "「Y-{w=.2}yeah, he did.{p}\ \ The inn probably has a lot to deal with during the\n\ \ festival, doesn't it? 」"
    
    show ju 001 with dis
    
    ju "「I'm sure this is a busy season for them.{p}\ \ Even so, he still makes time to show up. 」"
    ju "「Well, {w=.2}there's no use standing around.{p}\ \ We could go around the stalls again...{p}\ \ Or do you want to do something else? 」"
    fn "「Hmm... 」"
    "I look around the stalls as I speak.{p}There are a variety of them,{w=.2}\nbut only one catches my eye."
    fn "「How about that one? 」"
    
    $ event_name = "Fish!"

    show ju 008 with dis
    
    ju "「Balloon fishing? 」"
    fn "「Well I'm wearing a yukata,{w=.2}\n\ \ so I might as well do something that goes well with it. 」"
    fn "「I'd like to do goldfish scooping too,{w=.2}\n\ \ but you had to help out with that...{p}\ \ Come on, {w=.2}we've only got so long. 」"
    ju "「...I see 」"
    "Then, {w=.2}I come up with a great idea.{p}Even though there's a lot of people around,{w=.2}\nit won't look unatural... it shouldn't!"
    fn "「So, {w=.2}let's go right now! 」"
    "I shout to cheer myself up,{w=.2}and tightly grab\nJuuichi-san's hand.{w} Then, I start running towards the\nballoon fishing stall."
    
    show ju 015 with dis
    
    ju "「Wh-{w=.2}what the-...? 」"

    hide ju with dis
    
    "Even though I'm putting on a brave face,{w=.2}\nmy heart feels like it's going to explode...!"
    "I thought he'd shake me off,{w=.2}\nbut Juuichi-san follows along and lets me escort him."
    "It was only about 20 meters away,{w=.2}\nbut Juuichi-san and I were definitely holding hands.{p}His large palm is soft, {w=.2}and it covers up mine."
    "Despite it only being for a few seconds,{w=.2} that made me\na little happy.{w} It might be kind of lame,{w=.2}\nbut it's the best I can do for now."
    fn "「Alright, {w=.2}we're here! 」"
    "I don't want to let go, but we can't hold hands\nforever. As me make it to the balloon fishing stall,{w=.2}\nI quickly release my hand."
    
    show ju 012 with dis
    
    ju "「The stall isn't going to run away from us,\n\ \ you don't need to rush. 」"
    fn "「Heh heh, I wanted to do it as soon as possible. 」"
    
    show ju 002 with dis
    
    ju "「...Jeez. 」"
    "Juuichi-san scratches at his cheek.{w} He didn't seem to\nthink there was anything weird about it,{w=.2}\nthank goodness."

    hide ju with dis
    
    "I position myself in front of the water tank with\ncolorful balloons floating in it,{w=.2}\nand hand a coin to a very old fox."
    fn "「One try please! 」"
    attendant "「Here you go. 」"
    "A wire attached to a paper string. {w=.2}This is now my\npartner.{w} I squat down, {w=.2}and start my evaluation."
    "Hm... the red balloon in front looks good.{w} The rubber\nband is positioned towards me,{w=.2} and it's not too big.\nI should be able to lift it before my string breaks."
    "While being careful not to get the string wet,{w=.2}\nI hook the rubber band and slowly lift up."
    "The balloon rises up from the surface of the water... {w=.2}\nor so I thought.{w} The string abruptly breaks.{p}{nw}"
    play sound mizu07
    extend "Sploosh, {w=.2}the balloon falls into the pool."
    fn "「Aw! {w=.2}Just a little bit more and I would've had it! 」"
    ju "「Too bad. 」"
    "Juuichi-san, {w=.2}who has sat down next to me without me\nrealizing it, {w=.2}says.{w} It's really frustrating because\nI was so close."
    
    $ event_name = "More Fishing!!"
    
    fn "「Mister, {w=.2}one more! 」"
    attendant "「Thanks, {w=.2}here you go. 」"
    "Is he being helpful or is this just a coincidence?{p}This time my string is thicker than the one before.\nNow I'll make that red scoundrel mine for sure!"
    "With extreme care, {w=.2}I pass the wire through the rubber\nband.{w} Calmly, I bring it up.{w} This is a time when my\nthread of concentration seems like it's about to break too."
    fn "「Yes! 」"
    "The balloon raises into the air.{p}I remove the rubber band from the wire slowly,{w=.2}\nso that I don't screw up at the last second."
    "Now that I've got the hang of it,{w=.2}\nI carefully do the same thing again,{w=.2}\nand net myself a nice white balloon as well."
    
    show ju 002 at center with dis
    
    ju "「You did a lot better this time. 」"
    "As he says that, {w=.2}it seems like\nhis expression is starting to loosen up."
    fn "「I can do it when I put my mind to it!{p}\ \ ...Here, {w=.2}this is for you. 」"
    "I hand him the white balloon."
    
    show ju 003 with dis
    
    ju "「...Are you sure?{p}\ \ You're the one who caught it. 」"
    fn "「Yep. I did my best so I could give it to you! 」"
    
    show ju 001 with dis
    
    ju "「I see, {w=.2}thank you. 」"
    "He takes the balloon from me,{w=.2} and immediately wraps\nthe rubber band around his thick finger."
    attendant "「Well isn't that nice, {w=.2}dad?{p}A present from your cute son. 」"
    
    stop music
    show ju 014 with qdis
    play sound wind_noise
    
    "...?{p}I think I just heard something I'm not used to\nhearing."
    "I look at the stall owner, {w=.2}who is smiling and laughing\nas he looks at us.{w} When I point at Juuichi-san and I,\nhe continues to laugh as he nods his head."
    "Wha... {w=.2}Wait a minute!{p}You may not be able to tell by looking,{w=.2}\nbut Juuichi-san is only a year older than me!"
    "I take a look beside me and, {w=.2}just as I had expected,\nJuuichi-san's mouth is agape."
    fn "「Um, {w=.2}he's not my dad.{p}\ \ We're not even the same species. 」"
    "Since Juuichi-san is frozen in place,{w=.2}\nI calmly correct him."
    attendant "「Oh, {w=.2}my apologies.{p}My eyes aren't what they used to be. 」"
    "He bows his head as he speaks,{w=.2}\nand quickly apologizes."
    fn "「That's okay, {w=.2}anybody could make that mistake,{w=.2}\n\ \ so we don't mind!{w} Right, {w=.2}Juuichi-san? 」"
    ju "「... 」"
    fn "「Juuichi-san? 」"
    
    show ju 003 with dis
    
    ju "「...Y-{w=.2}yeah. 」"
    
    $ event_name =  "Dream-ColoredFireworksAtTheEndOfSummer"
    
    scene black with sdis
    scene forest01 night with sdis
    play music night_insects
    
    "We leave the balloon fishing stall, {w=.2}and Juuichi-san\nsuggests to me that we take a break on the hill behind\nthe shrine."
    "I wonder if there's any open  parts on it,{w=.2}\nso we can get a nice view of the fireworks?"
    "Only the lights of the festival and the shining stars\nin the night sky can be seen between the trees,{w=.2}\nbut now those are our guideposts."
    "Usually this would be an easy walk,{w=.2}\nbut now it's awfully difficult."
    "I don't excersize much,{w=.2}\nso a little mountain climbing makes me almost\ninstantly short of breath."
    "The geta and yukata that I don't usually wear aren't\nhelping either."
    "I hear the chirping of insects coming from the\nthicket here and there."
    "While thinking about Autumn approaching,{w=.2}\nI'm also reminded that, {w=.2}whether I like it or not,{w=.2}\nthe time I have left in this village is short."
    "Now feeling just a bit sentimental,{w=.2}\nI look over at Juuichi-san's face as he escorts me."
    "On the parts of him not in the light, {w=.2}his brown fur\nmakes for nice camouflage.{w} Except for the moonlight\nshining off his eyes,{w=.2} I can barely tell he's there."
    "His expression is always so hard to read,{p}what is he thinking about?{w=.2}\nI have absolutely no idea."
    "...Could he be lonely too?"

    show ju 001 night at center with dis
    
    ju "「[ln], {w=.2}look where you walking. 」"
    
    play sound bosu34
    
    "He suddenly grabs my arm.{w} I think \"What?\",\nconcentrate on looking where he's pointing,{w=.2}\nand see the root of a large tree sticking out."
    "If I had kept walking, {w=.2}it would have caught my foot\nand made me trip.{w} My yukata could've gotten dirty...{p}or even worse, {w=.2}maybe torn."
    fn "「Ah, {w=.2}sorry. 」"
    ju "「You can't see very well in the dark,{w=.2}\n\ \ so you need to be more careful about where you step. 」"
    fn "「...I will. 」"
    "He scolds me in a strong tone, {w=.2}and makes me feel\ndiscouraged.{w} He's thinking about and talking to me,{w=.2}\nso I shouldn't let something like that get me down."
    "But {w=.2}for a practical problem...{w} it doesn't feel nice\nto have the person you like be angry at you."
    fn "「...Now that I think about it, {w=.2}you're not\n\ \ participating in the bon dance?{p}\ \ You helped build the tower. 」"
    "I shake my head to distract myself from my depressed\nmood,{w=.2} and ask Juuichi-san a question."
    ju "「No, {w=.2}I declined. 」"
    fn "「Really? {w=.2}I'm surprised.{p}\ \ I thought you'd like to be a part of events like\n\ \ that. 」"
    
    show ju 003 night with dis
    
    ju "「... 」"
    fn "「Juuichi-san? 」"
    
    show ju 001 night with dis
    
    ju "「Well... {w=.2}if I left you alone,\n\ \ I would've had to do it by myself.{p}\ \ Do you remember how to do the dance? 」"
    "...{p}Making memories?"
    "If the week passes by like this,{w=.2}\nwill I have to shut up this feeling as a memory?"
    "That suddenly hits me."
    
    show ju 011 night with dis
    
    ju "「Even so,{w=.2}\n\ \ I don't want us to be mistaken as father and son. 」"
    fn "「Yeah... 」"
    "As I worry endlessly in my heart,{w=.2}\nI give a half-hearted reply."
    
    show ju 001 night with dis
    
    ju "「What?{w=.2}\n\ \ Did being seen as a child bother you? 」"
    fn "「No, that's not it.{p}\ \ ...Besides, {w=.2}\n\ \ I think you were the reason for that, {w=.2}not me. 」"
    fn "「You're always wrinkling your brow and making a stern\n\ \ face,{w=.2} so people think you're older than your actual\n\ \ age. 」"
    
    show ju 003 night with dis
    
    ju "「...Really? 」"
    "He sighs and lets his feelings show.{p}...Dammit.{p}I didn't mean that as a joke."
    "I can hardly see his expression in the dark,{w=.2}\nbut he's probably not in a good mood judging from his\ntone just now."
    fn "「U-{w=.2}uh...{w} You've got a nice, {w=.2}strong body and you're so\n\ \ composed, {w=.2}\"breadwinner\" is a word that really fits\n\ \ you! 」"
    ju "「... 」"
    "I tried to follow-up on that, but I was too late.{p}Juuichi-san stays silent, and I continue speaking."
    fn "「When people judge you by just your appearance,{w=.2}\n\ \ you should ignore them!{w} I know that you have\n\ \ more than one expression. 」"
    fn "「The way you're gentle even though your face doesn't\n\ \ show it,{w=.2} or how cute you were when you were looking\n\ \ forward to going to the beach. 」"
    fn "「All those things together are what I love about\n\ \ you! 」"
    "After rapidly talking, {w=.2}I realize what I just said.{p}Did I actually say that last part?{w} While I was\nabsorbed in talking to him,{w=.2} did I... confess?"
    "My face is hot.{p}In the heat of the moment, {w=.2}how much did I say?{p}...I wasn't even thinking about it."
    "I told him.{p}He knows the feelings I've been hiding and not\nplanning on showing."
    "What do I do if he doesn't like me?{p}What do I do if I can never talk to him again?"
    
    show ju 011 night with dis
    
    ju "「...Hm.{w} There's different ways I could retort,{w=.2}{nw}"
    show ju 001 night with dis
    extend " but I\n\ \ can see that you're trying to cheer me up.{w} I should\n\ \ say thank you for that. 」"
    "As I was sinking deeper and deeper into panic,{w=.2}\nJuuichi-san's low tone comforts me.{w} ...Not!"
    "Why is Juuichi-san being so casual about it?{p}He's being his usual self...{p}Didn't I confess?! {w=.2}Didn't I say I love him?!"
    fn "「Wait-, {w=.2}uh, {w=.2}um. 」"
    "I make a poor attempt at saying something clever,{w=.2}\nbut at the same time I'm afraid I'll blow myself up."
    "As a result, {w=.2}I don't make any sense and can only speak\nan enumeration of words."
    
    show ju 008 night with dis
    
    ju "「Hey, {w=.2}what's wrong?{w} You're panicking. 」"
    "He looks confused. I have no idea how to explain.{p}It's obvious if you think about it,{w=.2}\nI confessed for the first time."
    fn "「Um, {w=.2}because, {w=.2}err... 」"
    
    show ju 001 night with dis
    
    ju "「[ln], {w=.2}take a deep breath. 」"
    "I do as he says, {w=.2}and inhale as much as I can.\n{p}Then I hold it.{w} Then exhale.{w} Since I don't think one\ntime was enough, {w=.2}I do it again."
    "However, {w=.2}I still haven't calmed down,{w=.2}\nso I do it several more times."
    "He seems to be waiting for me to regain my composure.{p}He silently watches me take deep breathswith his arms\ncrossed like they usualy are."
    ju "「Are your shoulders relaxed? 」"
    fn "「Yeah, {w=.2}I think... 」"
    "With oxygen back in my brain, {w=.2}I can think clearly\nagain.{w} ...However, {w=.2}I'm still worried about Juuichi-san\nacting like nothing happened."
    "I think he'd react in some way when\nsomebody confesses their love to him..."
    "I was really surprised when Torahiko confessed to me,{p}he must have seen that goofy face I made then."
    "...Wait.{p}I scratch my head,{w=.2}\nand realize one of the possible cases."
    "Could he have maybe not noticed my confession?{p}Or rather...{w} thought of it as like instead of love?"
    "As I look at him quizzically,{w=.2}\nhe tilts his head in confusion once again."
    
    show ju 003 night with dis
    
    ju "「Have you not taken enough deep breaths yet? 」"
    "...I knew it. {w=.2}Seeing the way he's acting, I'm sure of\nit.{w} Is this good or bad luck?{w} He doesn't seem to be\naware of my feelings."
    "Thank goodness.{w} It doesn't seem like this is going to\nbecome a situation where he'd avoid me for the rest of\nsummer vacation."
    "Gah, {w=.2}I'll just leave things as they are.{p}That's what I should do, {w=.2}right?"
    "\"But...\", {w=.2}the devil in my mind whispers.{p}\"This is your chance, {w=.2}isn't it?\"{p}\"A chance to tell Juuichi-san your true feelings\"."
    "I can't use magic.{p}So I'll never get a chance to confess to Juuichi-san\nif I let this moment slip by."
    "...It's possible that I'll never see him again\nfor the rest of my life after this summer ends."
    "The relationship we have now rests on a very,{w=.2}\nvery thin string."
    "I'd go back to the way I was before I got Torahiko's\nletter,{w} busy with day-to-day things, {w=.2}and my memories\nof this summer,{w=.2} as well as Juuichi-san, {w=.2}would fade."
    
    stop music fadeout 5
    
    "I don't want that.{p}I think quietly to myself.{p}What should I do? {w=.2}What should I say?"
    "...I'll be honest, {w=.2}and tell him how I feel."
    
    play music pops_006
    
    fn "「Juuichi-san. 」"
    "I still feel the rush from earlier, {w=.2}probably because\nhe didn't catch it the first time."
    "Next, {w=.2}next I'll tell him the whole thing."
    "I can feel my heart pounding in my chest.{p}As I take a deep breath, {w=.2}I look at him right\nin his eyes that I can clearly see even in the dark."
    fn "「I love you. 」"
    
    show ju 004 night with dis
    
    ju "「You don't have to keep saying it.{p}\ \ It's embarrassing enough already. 」"
    "He misunderstands, {w=.2}and his words make my heart feel\nlike it could shatter."
    "But I've made my decision.{p}Without looking away from him, {w=.2}I say"
    fn "「I am in love with you. 」"
    "I changed it up a bit.{p}His eyes widen at my straightforward confession."
    
    show ju 015 night with dis
    
    ju "「W-{w=.2}wait...{w} are you being serious? 」"
    fn "「I'm not joking! 」"
    
    show ju 009 night with dis
    
    ju "「...Like, {w=.2}romantically? 」"
    fn "「Yes!{w} Juuichi-san, {w=.2}please go out with me!! 」"
    "Despite me being the one who confessed, {w=.2}my tone is\ngetting stronger and stronger.{w} I have to, {w=.2}or else it\nfeels like I'm going to me smashed."
    
    stop music fadeout 5
    
    "With a large sigh, {w=.2}Juuichi-san places his hands on\nboth my shoulders and looks directly into my pupils.{p}The distance between us right now is almost zero."
    "His lips are right in front of me.{w} If I leaned forward\njust a bit more I could touch them,{w=.2} but at the same\ntime they feel endlessly distant."
    
    show ju 001 night with dis
    
    ju "「Listen, {w=.2}[ln].{w} {nw}"
    show ju 003 night with dis
    extend "...Snap out of it. 」"
    
    play music melodious05
    
    "A soft,{w=.2} gentle tone of voice can sometimes be cruel.{p}...My feelings were flat out rejected."
    "Confronted with that fact, {w=.2}tears start to build up in\nmy eyes.{w} Even though I get the feeling Juuichi-san's\nbreath is taken away, {w=.2}I can't stop myself."
    fn "「Juuichi-san, {w=.2}I, {w=.2}I... 」"
    "After I start sobbing, {w=.2}I can't speak right.{w} I can't\nfocus on just one thing and they keeping coming one\nafter another,{w=.2} so I just keeping crying."
    "...I know I'm being pathetic,{w=.2}\nI know I'm being childish."
    "I've realized that the shock of a broken heart\nis a big thing."
    
    show ju 001 night with dis
    
    ju "「...Hey, {w=.2}[ln]. 」"
    "Without looking away from me,{w=.2}\nJuuichi-san begins to speak to me,{w=.2}\nmaking sure I understand each and every word."
    ju "「You're confused about your feelings for me. 」"
    fn "「That's not... 」"
    ju "「Your feelings for your senpai and friend...{w} are\n\ \ respect and familiarity.{w} You're confusing those\n\ \ feelings with love and affection. 」"
    fn "「...That's {w=.2}wrong...{p}\ \ I... {w=.2}you're... you...!{p}\ \ This feeling isn't... 」"
    "My mind is a mess.{p}But this feeling of love in my heart,{w=.2} that's no lie.\nThat alone I was able to say clearly."
    
    show ju 003 night with dis
    
    ju "「... 」"
    "He sighs deeply."
    
    show ju 001 night with dis
    
    ju "「[ln], I'll be honest with you.{p}\ \ ...I too was once in love with a man. 」"
    fn "「What?! 」"
    "This happened to Juuichi-san too.{p}I stare at him in surprise."
    
    show ju 008 night with dis
    
    ju "「It was somebody I got along well with. 」"
    "He begins to tell a story of his past.{p}I carefully listen to each and every word."
    ju "「I noticed I'd feel lonely when he was away from me.{p}\ \ I wished I could always be with him. {w=.2}...and then I\n\ \ had a thought.{w} \"Do I love this man?\". 」"
    fn "「... 」"
    ju "「It's easy for me to talk about it now...{p}\ \ but back then it was all but impossible. 」"
    ju "「I worried and worried,{w=.2}\n\ \ there was only one person I could confide in. 」"
    "I can guess who he's talking about."
    fn "「...Kyouji? 」"
    ju "「...Yes.{w} When I talked to him about my heartbroken\n\ \ thoughts,{w=.2} he simply told me it was like having the\n\ \ flu."
    ju "「He said it was something possible for all men\n\ \ during puberty. 」"
    ju "「...His words give me some relief.{p}\ \ I kept reminding myself that it was just a sickness. 」"
    fn "「...Then what happened? 」"
    
    show ju 001 night with dis
    
    ju "「Nothing. {w=.2}It's always been this way.{p}\ \ Even now I still get along with him because I held\n\ \ back my feelings for him. 」"
    fn "「... 」"
    ju "「...That's enough of my story.{w} Anyways,{w=.2} this is an\n\ \ emotionally unstable time for you. 」"
    ju "「If you look past your emotions,{w=.2}\n\ \ you'll look back on this someday and wonder why you\n\ \ ever said those things. 」"
    ju "「I'll say this much though.{p}\ \ I have definitely accepted your feelings. 」"
    "Juuichi-san strokes my head,{w=.2}\nlike in the way you'd comfort a baby."
    "...Please stop,{w=.2}\nI finally stopped crying and this is making me feel\nlike I'm going to start again."
    fn "「Juuichi-san...{w} can you do something for me? 」"
    "He silently waits for me to continue speaking.{p}That says to me \"I'll try\"."
    fn "「...Just once, {w=.2}please hold me close to you. 」"
    
    show ju 003 night with dis
    
    ju "「...And then you'll be satisfied? 」"
    fn "「...Yes. 」"
    
    show ju 001 night with dis
    
    ju "「...Understood. 」"

    hide ju with wipe_right
    pause .2
    play sound bosu34
    
    "He timidly embraces me.{w=.2}\nHe's warm. I want to melt away in his warmth.\nI know I can't do that though."
    "My whole body shakes.{w} I completely give myself to him.{p}Instead of my body falling to the ground,{w=.2}\nhe holds me tight."
    "I wrap my arms around his back, and squeeze.{w} Without\nresponding,{w=.2} he continues to support me with enough\nstrength so I don't fall."
    "I'm lonely.{p}I'm sad.{p}But I can't do anything about it."
    ju "「...Um, {w=.2}something's hitting my leg. 」"
    "He turns away as he says that.{p}But I can't help it, {w=.2}that's just my intention."
    "He's a man too,{w=.2}\nso he should know that he shouldn't bother saying\nanything."
    fn "「I can't help it, {w=.2}you know?{p}\ \ These things happen when you're with the person you\n\ \ love. 」"
    "He presses his thigh onto me, {w=.2}but that just makes it\nharder instead of softer.{w} Having it pointed out makes\nme all the more aware of it."
    ju "「... 」"
    "Juuichi-san shifts slightly.{p}Even trivial movements like that send pleasure running\nthough me."
    "I slowly move my right hand.{w} His back, {w=.2}his waist, {w=.2}his\nbutt, {w=.2}his thighs...{w} Sensing my movements, {w=.2}Juuichi-san\nspeaks to me in a lower tone."
    ju "「[ln]... {w=.2}you shouldn't go any further.{p}\ \ You won't be able to turn back. 」"
    
    menu:
        "A. Continue":
            jump juuichi22_continue
        "B. Stop":
            jump juuichi22_stop

    ####################################################
    label juuichi22_continue:
            
        $ event_name = "I Choose Not to Go Back"
        
        fn "「I'm sorry, {w=.2}but just a little more... 」"
        "Without waiting for him to respond, I move my hand to\nthe center part.{w} Through his pants,{w=.2} I can feel his\nbody temperature is especially high there."
        "...It's thick.{w} Even though he's not erect, {w=.2}it's bigger\nthan my hand.{w} I thought about it while we were at the\nbeach and camping, but this big?"
        "With the flat of my thumb, {w=.2}I rub it's head.{p}Juuichi-san's body jolts in surprise.{p}At the same time, {w=.2}I firmly grasp it."
        ju "「Ah... {w=.2}stop it. 」"
        
        menu:
            "A. Continue":
                jump juuichi22_keep
            "B. Stop":
                jump juuichi22_stop
    
    #####################################################
    label juuichi22_keep:
            
        $ event_name = "Just the Two of Us"

        stop music fadeout 10
        
        "His way of speaking has gotten softer.{p}If he really didn't like this,{w=.2}\nhe should be able to push me away."
        "...Please stop reacting like that.{p}I'm just misunderstanding him, {w=.2}aren't I?"
        "The truth is... he really does love me, {w=.2}doesn't he?{p}He is in love with me, right?{w} He's just embarrassed,{w=.2}\nso he can't say how he really feels, right?"
        
        play music cicada01
        $ renpy.music.set_volume(0.5, 0.0, channel = "music")
        
        fn "「It's too late, {w=.2}I can't control myself any longer... 」"
        "You hug the person you love.{p}That means Juuichi-san should love me,{w=.2}\nbut he still can't say it yet."
        "I'm reflected in his pupils,{w=.2}\nbecoming wilder than any beastman,{w=.2}\ntrying to attack my prey."
        ju "「[ln]... 」"
        "I thrust my left hand down, {w=.2}quickly slipping it\ninto his pants.{w} Now I can get a better feel for\nhim than earlier."
        "When I rub over his fundoshi,{w=.2}\nthe base of his cock gradually becomes stiffer."
        "It also seems like his arms wrapped around me are\nproportionally weakening."
        fn "「Juuichi-san, {w=.2}I'm making you excited, {w=.2}aren't I? 」"
        ju "「N-{w=.2}no!{w} It's Just a reaction from stimulation! 」"
        "While he's trying to explain, {w=.2}he continues to grow.{p}In almost no time at all, {w=.2}he's completely erect."
        "I unconsciously swallow saliva.{p}The bulge it's making in his pants make it obivously\nclear."
        ju "「Stop... {w=.2}don't look... 」"
        "He weakly shakes his head to show his unwillingness.{p}...That means \"please look\", {w=.2}right?"
        "I finally understand.{p}This is all because he's a shy person."
        
        play sound standup
        
        "To make him a little more compliant,{w=.2}\nI pull down his pants all at once.{w} I hear his\nrestrained voice, {w=.2}but this too is all for him."
        "It has quite a volume when it's soft,{p}but I can't help but think that it's\njust like a juice can when he's erect."
        fn "「Juuichi-san, {w=.2}you're huge... 」"
        ju "「... 」"
        "He turns his face away.{w} It's so big though,{w=.2} what the\nheck is he embarrassed about?{w} On the contrary, {w=.2}it's\ngiving me an inferiority complex."
        "The fundoshi guarding his crotch has a large opening\non the side because of his erection.{w} I slowly invade\nit with my hand."
        "His fur here is clearly different, it feels stiffer.{p}Oh, it's different here? {w=.2}Just a little more to the\nfront..."
        "A gasp escapes from his mouth,{w=.2}\nbut that only further inflames my lust."
        "I feel something thick, {w=.2}warm, {w=.2}and strongly pulsating\nin my left hand.{w} It's like all of him as gathered\nhere."
        "I try gripping it, {w=.2}but my fingers don't reach all the\nway around it.{w} ...He really is thick."
        "As I rub up and down the stiff shaft, {w=.2}Juuichi-san\nmutters something, but his voice had a hint of\npleasure to it."
        "...Does he happen to be the type that gasps a lot at\ntimes like these?{w} That's really cute, {w=.2}when he does\nit."
        "I'm so fortunate to hear him make noises like that.{p}So, {w=.2}I'm the only one in the whole world that should\nlove him."
        "I want him to be more indecent, {w=.2}more confused.{p}Kneeling in front of Juuichi-san, {w=.2}I bring my face up\nto the large, {w=.2}bulging part of him."
        "It smells, {w=.2}but I don't care because it's the scent\nof the person I love.{w} Actually, {w=.2}I start sniffing\neven wilder."
        "...I'm so turned on that I might start going a little\ncrazy."
        "I slowly pull his fundoshi to the side.{p}Does even the strained part stimulate him?{p}I heard him make a small moan."
        fn "「This is your... 」"
        "This time he lets out a distinct gasp.\nI become overjoyed at the thought of him recieving\npleasure from my mouth."
    
        play sound sex1
        
        "It's a little salty.{w} But it doesn't taste as strange\nas I imagined it would.{w} I release it from my mouth,{w=.2}\nand lick it like I would for soft serve ice cream."
        ju "「Oooh... Aah. 」"
        "I stick out my tongue a little,{w=.2}\nand stimulate him from the tip of his glans to the\nbottom of his balls."
        "Then, {w=.2}I put one of them in my mouth and roll it around\nas if it were just candy."
        "Juuichi-san pants like he's gasping for breath.\nWow, {w=.2}he likes it here too...{w} When I start sucking\non it, {w=.2}his voice gets louder."
        "Hmm...{w} It's good that I keep hearing this reaction,{w=.2}\nbut I don't feel like I'm sucking on it that much."
        "I finish off with one strong suck,{w=.2}\nand let it go from my mouth.{w} As Juuichi-san\npants, {w=.2}I look smile at him."
        "I'm not planning on resting yet though.{p}He wants something even better too, {w=.2}right?"
        "With my saliva reflecting off of him in the light of\nthe stars,{w=.2} it makes for an awfully dirty scene."
        "I jerk his gun barrel with my right hand,{w=.2}\nand test the limits of how much I can put in my mouth.{p}I try my hardest, {w=.2}but he doesn't go all the way in."
        "Although I try many times, {w=.2}my head going back and\nforth is making him get pretty worked up.{w} I slowly\nlook up at him.{w} He's quietly enduring the pleasure."
        "Even if he wasn't like that,{w=.2}\nI would offer myself to him any time.{p}I'm prepared to devote myself to him."
        fn "「Juuichi-san, {w=.2}please cum any time you want to.{p}\ \ I'm ready to take it. 」"
        "His round ears twitch."
        "Is that what he wanted to hear?{w=.2}\nOr has can he simply not endure it any longer?{p}He finally speaks those words."
        ju "「[ln]... {w=.2}Haah, {w=.2}I'm getting close...! 」"
        "I silently urge him on.{p}Using more than just my mouth,{w=.2} I jerk him with my\nright hand,{w=.2} pressing him to ejaculate."
        ju "「Kuh...{w} Aah, {w=.2}I-{w=.2}I'm cumming! 」"
        
        play sound heartbeat
        scene white with qdis
        scene forest01 night with dis
        
        "The moment he says that, he explodes in my mouth.{p}I can feel it hitting the back of my throat,{w=.2}\nmaking me think I might choke."
        "But I still don't want to let go.{p}I endure it over and over again,{w=.2}\nbecoming the outlet for Juuichi-san's lust."
        "My mouth is full with his cum.{p}Rather than spit it out...{w} I ready myself,{w=.2}\nand swallow it down."
        "Some of the sticky liquid remians in my throat.{p}...I entertain the out of place expression\nreferred to as \"being connected at the throat\"."
        "After making sure he's done cumming in my mouth and\npulling out,{w=.2}{nw}"
        play sound bosu34
        extend " Juuichi-san falls on his backside with a\nthud."
        "All I can hear from him is rough breathing."
        "I open up the front of my yukata, {w=.2}take out mine\nfrom my underwear.{w} It's been strained for a while now,{w=.2}\nand there's precum dripping from the tip."
        "Seeing Juuichi-san in his blank state,{w=.2}\nI grin widely."
        fn "「Juuichi-san, {w=.2}did that feel good?{p}\ \ ...Now make me feel good too, {w=.2}please. 」"
        "Afterall,{w=.2}\nwe love each other."
        ju "「...{w=.2}What- 」"
        "When he opens his mouth to speak, {w=.2}I ram myself in.{p}It's nothing but warm pleasure.{w} The slippery feeling\nmakes me feel like I could climax just from putting it in."
        "But I'll hold out for just a little longer\nI didn't give him a chance to get used to it,{w=.2}\nso I have to help him out."
        "After groping around in my yukata sleeve, I pull\nsomething out, turn it on, and set it on the ground.{p}{nw}"
        play sound button2_007
        pause 1
        extend "There, {w=.2}this should work."
        "I push his head down, {w=.2}and thrust my hips back and\nforth.{w} He looks up at me with tears in the corners of\nhis eyes."
        "Just that face staring at me makes me feel so good I\nstart shaking.{w} I'm at my limit,{w=.2}\nI got there terribly quick."
        fn "「Aaah, {w=.2}I'm gonna cum! 」"
    
        play sound heartbeat
        scene white with qdis
        scene forest01 night with dis
        
        ju "「Ghk, {w=.2}ack, {w=.2}gah! 」"
        "Even though I shoot forcefully in his mouth,{w=.2}\nhe coughs and gets cum all over his face."
        "...I drank all of his without leaving any behind\nthough.{w} I'm feeling a little hurt by this.{p}Next time I need to make sure he'll do it."
        "While I lick the cum off the bridge of his nose,{w=.2}\nI pick up the cell phone I had set on the ground."
        fn "「Juuichi-san, {w=.2}do you know what this is? 」"
        "I adjust the angle so he can see it,{w=.2}\nand press the button right in front of him."
        "On the phone's screen, {w=.2}the recording of him sucking me\noff and getting covered with my cum is plainly shown."
        "Juuichi-san's face instantly goes pale.{p}I really didn't want it to have to come to this.{p}But this is also thinking of Juuichi-san."
        fn "「It's a cell phone, {w=.2}and they can do this now too. 」"
        ju "「[ln]...{w=.2} You... 」"
        fn "「If I print this out and post it all over the village,{w=.2}\n\ \ can you guess what will happen? 」"
        "I take a step, {w=.2}crushing some twigs.{w} {nw}"
        play sound crash18_a
        extend " The dry sound is\nawfully loud and rocks my eardrums.{w} Maybe that was\nalso the sound of Juuichi-san's heart breaking."
        "Playing the villain is a little painful.{w} But if I do\nthis, {w=.2}I'm sure Juuichi-san will open up to me.{p}He should become obedient."
        "That's right, {w=.2}Juuichi-san is mine... {w=.2}and only mine.{p}Therefore, {w=.2}I can do anything with him now.{p}...I'll try something."
        fn "「You don't want that either, {w=.2}right? 」"
        ju "「What do you want from me...? 」"
        fn "「What do I want?{p}\ \ ...That's been known since the start, {w=.2}hasn't it? 」"
        "I smile at him again."
        fn "「You...{w} I want all of you. 」"
        
        $ event_name = "The Tale of the Locked-Away Garden"
        
        stop music fadeout 5
        scene black with sdis
        pause 3
        play music ambience01
        $ renpy.music.set_volume(0.75 , 0.0, channel = "music")
        
        "--After that,{w=.2}\nJuuichi-san disappeared from the village."
        "In Minasato, {w=.2}where people rarely get angry about\nincidents,{w=.2} a case of a missing person happened.{p}The village was in an uproar."
        "As the last person who saw him, {w=.2}I was questioned too,\nbut the incompetent police never got any clues and\nbacked down in the end."
        "Shortly after,{w=.2}\nthe Kazenari police got involved and searched through\nthe mountains, {w=.2}but their efforts were fruitless."
        "Eventually the police stated that Juuichi-san ran away\nfrom home, {w=.2}and stopped their investigation."
        "\"There's no way Juuichi-senpai would leave without\nsaying anything!\" said Torahiko.{w} It seems he's still\nsearching for him,{w=.2} but... he's wrong."
        "Him disappearing was completely his intention.{p}There might have been a bit of pressure from me,{w=.2}\nbut he wanted this himself."
        "To be together, {w=.2}with me."
        "I sneak out of my room into the brilliant moonlight,{w=.2}\nand stand in front of the storehouse on the corner of\nthe property."
    
        play sound hinge
        
        "As I push open the door, {w=.2}I feel the air gust out\nand brush against my face.{w} While closing the door\nbehind me,{w=.2} I greet the unmoving shadow in the corner."
        fn "「I'm back, my lovely Juuichi-san.{p}\ \ Hm, {w=.2}looks like you're being a good boy.{p}\ \ I'll fill you with pleasure again today, {w=.2}okay? 」"
        fn "「I'll give you plenty.{p}\ \ Let's confirm our love for each other. 」"
        "Our summer...{w} Never ended."
        
        stop music fadeout 5
        scene black with dis
        pause 5
        
        $ renpy.full_restart()
    
    ######################################################
    label juuichi22_stop:
            
        $ event_name = "After the Festival"
        
        "What the heck am I doing?{w} I suddenly snap back to\nreality.{w} Betraying Juuichi-san's trust, {w=.2}that's what\nI'm doing."
        fn "「Juuichi-san, {w=.2}I'm sorry. 」"
        "I slowly pull away from him.{p}Just then I was swept away in a delusion,{w=.2}\nthere's not way I deserve to stand next to him."
        
        show ju 001 night at center with dis
        
        ju "「... 」"
        "He looks at me without saying anything.{p}The pressure of that silence tortures me,{w=.2}\nit makes me feel like running away."
        "...After all that, {w=.2}this happened.{w} I wanted to be good\nfriends with Juuichi-san,{w=.2} but I might have just\ncrushed that possiblity with my own hands."
        "Even though I'm usually careful about thinking before\nI act,{w} I screwed up."
        
        show ju 003 night with dis
        
        ju "「[ln], {w=.2}I-{nw}"
        play sound fireworks_explosion
        show fireworks
        extend " 」" 
        "A body-shaking boom.{p}His words are covered up by the setting off and\nraising of a firework."
        "I'm sure he must have been scolding me.{p}Or was he breaking off relations with me?"
        "Either way, {w=.2}it can't be anything good for me.{p}If that's the case, {w=.2}I better do this myself..."
        fn "「Juuichi-san,{w=.2}\n\ \ I'm really sorry for being so selfish. 」"
        "I bow my head to him. {w=.2}And continue lowering it."
        fn "「So, {w=.2}I'll leave you alone from now on. 」"
        "The tears should have stopped,{w=.2}\nbut they fall and splash on the ground."
        fn "「Please, {w=.2}just forget about me.{p}\ \ ...Thank you, {w=.2}for everything. 」"
        "How did he respond? {w=.2}I wasn't brave enough to find\nout.{w} I turned around with my head down and ran away\nlike a scared rabbit."
        
        play sound stepfield01
        hide ju with dis
        
        "I think Juuichi-san is yelling something to me from\nbehind,{w} but I couldn't look back."
        
        play sound fireworks_explosion
        show fireworks
        
        "I cry, {w=.2}loudly.{p}The fireworks conceal my shameful voice.{p}I continue to cry the whole time as I run."
        "...Good-bye, {w=.2}Juuichi-san."

        jump end22
    
######################################################   
label end22:
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

    jump day23

