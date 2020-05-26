###Day 29
label day29:
    
    $ renpy.music.set_volume(1.0, 0.0, channel = "music")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound2")
    
    $ day = 29
    $ the_date = _("August 29")
    $ event_name = _("８月29日")
    
    if favorite == "tatsuki" or favorite =="kounosuke" or favorite == "kouya" or favorite == "juuichi":
        window hide
        play music birds_chirping
            
        scene sky01 
        show text _("{size=+130}August 29") at truecenter
        with Dissolve(.5)
        
        pause 3
        scene black with Dissolve(1)
        pause .4
        
    else:
        jump day30
        
    $ renpy.jump (favorite + "29")
    
##########################################################
label kounosuke29:

    $ event_name = _("What was promised")

    play music cicada01 fadein 3
    $ renpy.music.set_volume(0.4, 0.0, channel = "music")
    scene hbroom with wipe_corner
    
    "In the later stage of my Summer vacation,{p}I'm busy with unfinished homework."
    "It's already absolutely impossible alone."
    "When I remember the bargaining point,{p}from the other day,{p}I decide to call Kounosuke over to help."

    if kouno_badend == True:
        jump kounosuke29_homework
    else:
        jump kounosuke29_sex

    ##########################################################
    label kounosuke29_homework:
        
        $ event_name = _("The Words I Could Not Say")        
        
        stop music fadeout 7
        
        "Still, even with two people,{p}taking one or two days, it won't get done."
        "Ah, why didn't I go at a steadier pace?{p}If I would have a done a little bit each day,{p}I wouldn't need to rush."
        
        play music free51
        $ renpy.music.set_volume(0.75, 0.0, channel = "music")
    
        show ko 001 at center with wipe_right
        
        ko "「[fn], are you still mad? 」"
        fn "「About what? 」"
        
        show ko 005 with dis
        
        ko "「The thing with the competition. 」"
        fn "「Oh, that? It doesn't matter. 」"
        
        show ko 007 with dis
        
        ko "「I see. 」"
        fn "「But, you are keeping your end of the deal. 」"
    
        show ko 005 with dis
        
        ko "「I-I know. But despite that,{p}\ \ don't you think there's a bit too much?{p}\ \ You haven't worked on it at all... 」"
        fn "「That's because I spent a whole day,{p}\ \ being dragged around in the village,{p}\ \ with a certain somebody... 」"
        
        show ko 007 with dis
        
        ko "「Ooh. So you are still mad. 」"
        fn "「No I'm not! 」"
        "However, because that's a factor in this,{p}he is naturally going to compensate."
        "That's right."
        "I haven't been working on this,{p}because I've been spending,{p}all of every day in idle amusement."
        "I was spending time with everybody...{p}it's not my fault that I couldn't do it!{p}I had no choice, it's not my fault..."
        "...I tell that to myself in vain.{p}Now I'm focusing all my attention,{p}to getting this homework done."
        "Come on, Kounosuke!{p}Don't you slow down either!"
    
        scene hbroom red with sdis
        show ko 007 red at center with wipeleft    
        play music melodious06
        
        fn "「It's finished...! 」"
        ko "「I-I'm tired... 」"
        "When everything was said and done,{p}we spent about three whole days on this."
        "Still, it's best to do homework,{p}at a steady pace."
        "If I hadn't slacked off and been lazy,{p}I wouldn't have dealt with this at all!"
        fn "「You're tired too, huh. 」"
    
        show ko 005 red with dis
        
        ko "「Definitely. I've been kept in confinement,{p}\ \ for three long days... 」"
        fn "「But you did promise... 」"
        
        show ko 001 red with dis
        
        ko "「Well yeah, but still... 」"
    
        show ko 006 red with dis
        
        ko "「Ah shit. I gotta go soon... 」"
        fn "「It's still light out, isn't it?{p}\ \ You should relax a little... 」"
    
        show ko 001 red with dis
        
        ko "「I'd really like to do that,{p}\ \ but I have to help out at home.{p}\ \ {nw}"
        show ko 005 red with dis
        extend "Yukiharu will complain if I skip again... 」"
        fn "「Oh... 」"
        "If that's the case,{p}then it would be bad for me to restrain him."
    
        hide ko with wipe_right
        scene black with dis
        scene hentry red with dis
        show ko 001 red with wipeleft
        
        ko "「See you, [fn]! 」"
        fn "「Yeah. Later. 」"
        
        show ko 007 red with dis
    
        pause 1
        
        ko "「...Umm, [fn]... 」"
        fn "「What? 」"
        ko "「Err...{p}\ \ {nw}"
        show ko 001 red with dis
        extend "On second thought, it's nothing. Sorry. 」"
        fn "「You're weirding me out.{p}\ \ I wish you would say things more clearly. 」"
    
        show ko 002 red with dis
        
        ko "「But it is nothing.{p}\ \ I mean, I forgot what I was going to say. 」"
        fn "「Hey! 」"
        ko "「Nyahaha. That's it.{p}\ \ Well then, see you later! 」"
        
        play sound tm2_slidedoor000
        hide ko with wipe_right
        
        "In the end, it seems Kounosuke had nothing to say.{p}Well, I'll just forget about it,{p}it probably wasn't anything important anyways."
        "Whew. With all this homework out of the way,{p}the only thing I want to do tomorrow,{p}is to have as much fun as possible."
        "I'm leaving the day after tomorrow.{p}I'll play as much as I can,{p}so I won't have any regrets."
    
        jump end29

    ##########################################################
    label kounosuke29_sex:
        
        if persistent.replay == True:
            $ first = persistent.name_first
            $ last = persistent.name_last
            $ day = 29
            $ event_name = "A Lover's Proof"
            scene hbroom with dis
        
        $ event_name = _("A Lover's Proof")
    
        show ko 005 at center with dis
        
        ko "「I mean, you really think this...{p}\ \ is impossible too, don't you? 」"
        fn "「Kounosuke, please move your hand. 」"
        "For the past few days,{p}he has been helping me through this."
        "Now it feels like I'm just...{p}hearing complaints all the time."
        "Because..."
        
        show ko 004 with dis
        
        ko "「Don't you think it's funny,{p}\ \ that the magazine was from a year ago,{p}\ \ to begin with? 」"
        "...of the picture he sent for the competition.{p}It seems he finished his submission,{p}but it was immediately sent back."
        "Because of that, he asked the editing company.{p}The magazine had already ceased publication."
        "If you look carefully,{p}you'll see that the magazine,{p}had been printed last year."
        "That country bookstore is horrible...{p}By the way, he complained to the bookstore,{p}and could have gotten half the price back, but..."
    
        show ko 002 with dis
        
        ko "「Haah, that old thing disappeared.{p}\ \ {nw}"
        show ko 005 with dis
        extend "If that's how that store manages its goods,{p}\ \ I shouldn't spend my money there! 」"
        "...it seems nothing can be done,{p}to make him satisfied,{p}so he'll be like this for a while."
        "He's already helping me with my homework,{p}and making me hear his complaints."
        "Yet somehow we're on the home stretch,{p}I'll finally be done with all of this."
        
        stop music fadeout 4
        hide ko with dis
        scene hbroom red with Dissolve(3)
        play music free10
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        
        fn "「I-it's done... 」"
    
        show ko 007 red at center with dis
        
        ko "「I'm tired. 」"
        fn "「You're exhausted too, huh. 」"
        "I have to say, Kounosuke can be quite helpful.{p}His mental calculating is as quick as I expected,{p}and we chatted while going smoothly through math."
        "On the other hand,{p}it was nothing but complaining,{p}with the exception of that chat."
        "Although I have a feeling that,{p}it was only a hindrance to me..."
        "Well, we finished without any problems,{p}so that's okay."
        "I've been sitting the same way for a while,{p}so my back is sore."
        "My spine pops when I stretch.{p}Next to me,{p}Kounosuke lightly stretches the same way."
    
        show ko 001 red with dis
        
        ko "「Come to think of it,{p}\ \ today's been awfully quiet. 」"
        fn "「Oh, my grandparents said,{p}\ \ they were going to visit a grave."
        fn "They also said they were going,{p}to go to the grocery store on the way back.{p}I don't think they'll be back before evening. 」"
        ko "「Hmm... 」"
        "I see Kounosuke intermittently,{p}looking at me from the side."
        fn "「What? 」"
    
        show ko 006 red at briefzoom
        
        ko "「Nothing. 」"
    
        show ko 005 red with dis
        
        ko "「Err, there's... 」"
        "He's been looking back,{p}and forth at me for some time,{p}fidgeting and sounding weird."
        fn "「You're weirding me out... 」"
    
        show ko 006 red at jump_up
        
        ko "「Eh. {nw}"
        show ko 007 red with dis
        extend "S-sorry! 」"
    
        show ko 005 red with dis
        stop music fadeout 5
        
        ko "「Err... um, well that's not it,{p}\ \ the mood has nothing to do with it. 」"
        fn "「So what is it? 」"
    
        show ko 001 red with dis
        
        ko "「I love you, [fn]. 」"
        fn "「Huh? 」"
        ko "「I love you! 」"
        "He softly grasps my hand sitting on the desk,{p}and stares at me with serious eyes.{p}For a few seconds, there's nothing but silence."
        
        play music melodious06
        
        fn "「Pft. Ahahaha! 」"
    
        show ko 005 red with dis
        
        ko "「Wh-what?{p}\ \ I'm being serious! 」"
        fn "「S-sorry. For some reason,{p}\ \ that serious look on your face,{p}\ \ made me do that. 」"
        ko "「Tch... 」"
        fn "「Sorry, sorry.{p}\ \ I love you too, Kounosuke. 」"
        
        show ko 007 red with dis
        
        ko "「...That's not it. 」"
        fn "「What? 」"
    
        show ko 001 red with dis
        
        ko "「I love you. I'm not joking, really!{p}\ \ More than as a friend...{p}\ \ {nw}"
        show ko 008 red with dis
        extend "It's deeper than that. 」"
        "Kounosuke looks straight at me."
        "He had gotten his point across,{p}with that serious expression,{p}but is this...?"
        fn "「Uhh, is this a confession...? 」"
    
        show ko 001 red with dis
        
        ko "「Well, yeah. 」"
        "Huh? It couldn't be,{p}even if he did just suddenly confess...\nH-how should I answer?"
    
        show ko 005 red with dis
        
        ko "「Huh, I knew it,{p}\ \ you're not happy that it's being said,{p}\ \ by a male beastman, are you? 」"
        fn "「N-no no! That's not it at all.{p}\ \ I'm, um... very happy about that... 」"
    
        show ko 001 red with dis
        
        ko "「Really!? 」"
        fn "「Y-yeah.{p}\ \ I l-love you too? 」"
    
        hide ko with wipe_right
        play sound ClothD
        
        "Mfph?"
        "My mouth is suddenly closed up,{p}and I can't understand,{p}what's going on for a moment."
        "He puts his hands around my shoulders,{p}then firmly pins me down,{p}and puts his face right in front of mine."
        "Kounosuke's cheek whiskers,{p}tickle when they hit my face."
        "I can feel the heat,{p}from his fur on my lips..."
        fn "「Mm!? 」"
        "A warm feeling going into my mouth,{p}suddenly brings me back to reality."
        "Ko-Kounosuke!?"
        fn "「Mm, mm! 」"
        "I attempt to struggle,{p}but he has me pinned down,{p}and I can't get away from him."
        "He's surprisingly strong.{p}Still, Kounosuke gets off me after a short time."
    
        show ko 008 red at center with sdis
        
        ko "「I'm sorry. Was I hurting you? 」"
        fn "「I wouldn't say you were hurting me... 」"
        "That kiss was so sudden, and deep too.{p}It was surprising or disorienting,{p}but I kind of liked it."
        "I'm confused."
        fn "「D-don't you think it was too sudden? 」"
        
        show ko 001 red with dis
        
        ko "「But there isn't any more time left. 」"
    
        show ko 007 red with dis
        
        ko "「I should have said something earlier,{p}\ \ but there was never a good time... 」"
    
        show ko 001 red with dis
        
        ko "「I'm sorry it came to this.{p}\ \ It might've been too sudden like you said,{p}\ \ but I really mean it! 」"
        "Kounosuke continues to stare at me."
        ko "「[fn]. I want to be your lover. 」"
        "That serious face I first laughed at,{p}now looks like a beast watching its prey."
        "Although he gently put his hand on mine,{p}my right hand doesn't move at all."
        "Our body heat is transmitted,{p}through each other's clothes."
        "The thumping I hear,{p}might be our hearts beating."
        fn "「S-sure. Alright... 」"
        "In my half-slown state, I nod my head."
    
        stop music fadeout 3
        scene black with sdis
        scene hbroom red with sdis
        show ko 201 red at center with dis
        play music cicada01 fadein 5
        $ renpy.music.set_volume(0.3, 0.0, channel = "music")
        
        fn "「Nobody can see us from outside? 」"
        ko "「It's safe, right? 」"
        "The futon I usually sleep on is layed out,{p}Kounosuke and I sit on it in our underwear.{p}I got through that okay, but I'm still nervous."
        fn "「S-so now our underwear... 」"
    
        show ko 202 red with dis
        
        ko "「Yep. 」"
        "Here it goes."
        "Ah."
    
        show ko 105 red with dis
        
        ko "「[fn], you cheated. 」"
        fn "「S-sorry. 」"
        "My hands were sweaty,{p}from being so nervous and slipped,{p}so he got naked ahead of me."
        "He gives me an unsatisfied look."
        fn "「I-I'm taking it off now. 」"
        "Under his watchful gaze,{p}I pull my underwear down."
        "After they're down,{p}I quickly look away in embarrassment."
    
        show ko 102 red with dis
        
        ko "「Oh, yours is already half up. 」"
        fn "「D-don't look! 」"
    
        show ko 101 red with dis
        
        ko "「You don't need to hide it.{p}\ \ It's going to get even better after this. 」"
        "Oh, he's right.{p}When he saw me, I hid myself out of reflex.{p}I expose myself to Kounosuke once again."
        "Ooh... I know what we're going to be doing,"
        "And we're not taking a bath,{p}so being closely seen by another person,{p}is still embarrassing."
    
        show ko 102 red with dis
        
        ko "「[fn]. 」"
        fn "「Nn... 」"
    
        play sound changing
        
        "I entrust myself to the arm,{p}that's gently around my shoulder,{p}and we embrace each other."
        "I thought it would be a little more rough,{p}but being buried in his fur,{p}is surprisingly soft and fluffy."
        "We both get a feel of each other's bodies."
        "Kounosuke's fur tickles my skin.{p}The heat from his palms is transferred to mine.{p}His stomach feels squishy."
        "That kiss from before was too sudden,{p}now we can feel each other slowly."
    
        show ko 108 red with dis
        
        ko "「Nh, hah...{p}\ \ This is like a dream.{p}\ \ I'm doing this with you... 」"
        fn "「Maybe this is a dream? 」"
    
        show ko 105 red with dis
        
        ko "「Eh. Don't say something bad like that. 」"
    
        show ko 106 red at jump_up
        
        ko "「Yeowowowowow! 」"
        fn "「Ah, so it isn't a dream. 」"
    
        show ko 105 red with dis
        
        ko "「You're terrible, [fn]. 」"
        fn "「Then what if I do this... 」"
    
        show ko 103 red with dis
        
        ko "「Ahahaha! S-stop it.{p}\ \ The side of my stomach is my weakness, hee... 」"
        "For a while we touched each other like that.{p}We were just acting playful,{p}but our hands work lower and dirtier."
        "We compared each other's sizes,{p}then I took it in one hand,{p}and tried stroking it in different places."
        "While playing around with it in silence,{p}our eyes suddenly meet."
        "We both start to feel strange,{p}and spurt out afterwards,{p}then kiss deeply again."
    
        show ko 101 red with dis
        
        ko "「Hey, do you want to actually do it now? 」"
        fn "「Yeah... let's try it. 」"
        "Kounosuke cuts right to the chase,{p}his crotch already prepared."
    
        show ko 102 red with dis
        
        ko "「Alright, get on your hands and knees. 」"
        fn "「Huh? W-wait a minute! 」"
        
        show ko 101 red with dis
        
        ko "「What's wrong? 」"
        fn "「I'm the bottom? 」"
        ko "「Yeah. 」"
        fn "「Between the two of us,{p}\ \ I'd say I would be a better top. 」"
        "Another reason is that,{p}I'm saving my body before marriage,{p}just in case..."
        "I am interested in doing that,{p}but a little scared."
        
        show ko 105 red with dis
        
        ko "「Eh, but I don't know what it's like,{p}\ \ to be a bottom. I heard it hurts. 」"
        fn "「Then that would be,{p}\ \ all the more reason for me not to! 」"
    
        show ko 102 red with dis
        
        ko "「It's alright, it's alright.{p}\ \ In human and beastman pairings,{p}\ \ most porn has the human bottoming. 」"
        fn "「Huh? Oh. Now that you mention it,{p}\ \ I guess you're right. 」"
        
        show ko 103 red with dis
        
        ko "「That's right, that's right.{p}\ \ So hurry up and... 」"
        fn "「Wait, get your hands off me! 」"
        "We're both very naked, and between our legs,{p}our penises are both standing straight up.{p}So what are we arguing for?"
        "Both of us remain adamant.{p}and refuse to debate any further.{p}Then, Kounosuke slowly breaks the silence."
    
        show ko 101 red with dis
        
        ko "「I know. Let's try rock paper scissors! 」"
        fn "「Rock paper scissors? 」"
    
        show ko 103 red with dis
        
        ko "「Yes! The winner gets to be the top,{p}\ \ the loser is the the bottom!{p}\ \ That'll be it, no complaining! 」"
        "Rock paper scissors huh...{p}Kounosuke's still saying whatever he's saying."
        "But as we are now, we won't get past this point,{p}so I decide to go along with it."
        "Rock,{w} paper,{w} scissors!\nI throw out scissors.{p}Kounosuke... paper."
    
        show ko 106 red at briefzoom
        
        ko "「Whaaat! 」"
        fn "「Yes! 」"
    
        show ko 105 red with dis
        
        ko "「Alright, best two out of three! 」"
        fn "「Rejected. Not knowing when to give up is bad. 」"
    
        show ko 107 red with dis
        
        ko "「Oohh...! 」"
        "Kounosuke starts to say something."
        "I won the game fair and square,{p}so I won't allow him,{p}to talk his way out of this."
        "Kounosuke whines,{p}then reluctantly gets on all fours."
    
        show ko 101 red with dis
        
        ko "「Oh, I almost forgot. 」"
        fn "「Eh? 」"
    
        play sound standup
        
        "Kounosuke reaches into his pants,{p}that he had taken off earlier,{p}pulls something out, then hands it to me."
        ko "「Use this. 」"
        fn "「What is it? 」"
    
        show ko 103 red with dis
        
        ko "「Lotion. If you don't use it,{p}\ \ you'll tear me up. 」"
        fn "「Oh. And why do you have this...? 」"
    
        show ko 111 red with dis
        
        ko "「Well, it goes without saying, right? 」"
        fn "「...But surely you haven't been keeping this,{p}\ \ for the past three days just in case that...{p}\ \ you decide to bang me. 」"
    
        show ko 101 red with dis
        
        ko "「Oho, but I have. 」"
        fn "「...... 」"
        "How do you comment on that...{p}Perhaps this was his secret motive for...{p}helping me with my homework...?"
        "Still, I'm amazed and have to admire,{p}Kounosuke for that dedication.{p}That's how I feel."
        ko "「Hey, hurry up and put the lotion on already.{p}\ \ {nw}"
        show ko 102 red with dis
        extend "Or do you want me to put it on for you? 」"
        fn "「No, I can do it myself! 」"
        "During our conversation my dick,{p}had calmed down quite a bit."
        "Kounosuke puts some of the slippery,{p}shiny looking lotion in his hand."
        "Then, in order for things to go smoothly,{p}I also take it, squeeze some of it out,{p}and spread it thickly on myself."
        "...Is this like a massage?"
        "Both of us finish preparing,\nand Kounosuke gets on all fours again."
        "Somewhat hidden under his fur,{p}and under the base of his tail,{p}I open up a faintly red-colored hole."
        "Gulp.{p}I swallow my saliva in my mouth,{p}but not because I'm thirsty."
        "My heart is beating in...{p}anticipation and excitement.{p}My once drooping self is standing solidly again."
        "Gently, I insert my dick into Kounosuke's ass.{p}I try to push straight into it,{p}but it doesn't go in easily."
        "I impatiently thrust my hips a few times,{p}but it slips off every time{p}and the lotion just smears around the hole."
        "Ah, but just his fur brushing on my glans,{p}feels good on its own."
    
        show ko 101 red with dis
        
        ko "「[fn], relax. 」"
        fn "「Y-yeah. 」"
        "Kounosuke rests down on his shoulders.{p}With his arms free,{p}he opens himself up to support me."
        ko "「In order to not do it all at once,{p}\ \ make sure to slowly push it in. 」"
        fn "「Okay... 」"
        "Firmly supporting my dick,{p}I align myself at his opening."
        "I make sure to slowly push my hips,{p}forward like he said,{p}and slip myself into Kounosuke."
    
        show ko 106 red with dis
        
        ko "「Fuwah? 」"
        "With the help of the lotion,{p}getting the rest in is surprisingly...{p}simple after inserting the tip."
    
        show ko 101 red with dis
        
        ko "「Are you in? 」"
        fn "「Y-yeah... 」"
    
        show ko 108 red with dis
        
        ko "「H-how does it feel? 」"
        fn "「Huh? Umm... 」"
        "I try to express how it feels for the first time,{p}but I can't find the right words.{p}Because of that, I force myself to say,"
        fn "「...It's warm. 」"
        "It's clamped tight around the entrance,{p}but the inside is soft and warm."
        "At first it's only that,{p}but then I'm gradually...\nenveloped by a pleasant feeling."
        ko "「Does it feel good? 」"
        fn "「Yeah. 」"
    
        show ko 102 red with dis
        
        ko "「Great... 」"
    
        hide ko with wipeleft
        scene ev_kounosuke_1 with dis
        stop music fadeout 10
        pause 3
        
        ko "「M-move slowly. 」"
        fn "「Okay. 」"
        
        play sound sex2 loop  
        
        "I slowly move back and forth like he said,{p}and then his ass tightens up nicely.{p}I work him with my cock."
        "The walls of his insides,{p}are completely wrapped around my shaft.{p}It's warm, and I want to rub myself against it."
        fn "「Hah... This feels really good... 」"
        "While being unware of myself,{p}I thrust my hips in desire for pleasure."
        ko "「Hyah, ah, ooh...{p}\ \ [fn], wait, time out... 」"
        fn "「Huh? What? 」"
        ko "「D-don't do that!{p}\ \ S-stop it, that's d-dangerous.{p}\ \ Wait, a little slower 」"
        "He says stop, but his voice,{p}sounds unusually excited.{p}Now I try thrusting my hips harder."
        ko "「Hyaaa, st-stop, it tickles! 」"
        "His body goes against what he says, arches back,{p}and tightens up on me.{p}What's this feeling? This is..."
        "Every time I thrust my hips,{p}his breathing gets harder..."
        "And surges forward in pleasure,{p}at the same time."
        "Above all, I'm ravishing my partner,{p}telling him my true feelings,{p}by giving him this pleasure."
        "It's making me hot."
        ko "「N-no, [fn], [fn], ahng! 」"
        "Clinging on the futon with both hands,{p}and laying on the side of his face,{p}Kounosuke shakes his head back and forth."
        "I stick out my waist to thrust myself into his body,{p}then pull out right at the last minute."
        "I simply repeat this action,{p}many, many times over."
        "Every time Kounosuke raises his voice,{p}I fuck him harder and harder."
        "But the lotion does help a lot,{p}there's nothing impeding my movement."
        "On the other hand,{p}it simply becomes loose when my movement weakens."
        "It's as if I'm coaxing it out of him."
        ko "「Aah, ah, aah! 」"
        "He can't think of anything more to say,{p}just cries out in pleasure,{p}and thrusts his hips too."
        "It's only in porn where the beast,{p}is the only one writhing in pleasure."
        fn "「This is amazing...{p}\ \ Kouno... suke...! 」"
        ko "「Ha, ah, [fn]... aah! 」"
        "I thrust my hips,{p}churning into his hole of flesh,{p}and indulge myself in this pleasure."
        "My body gets hotter every time,{p}my hips seeking an even greater pleasure."
        ko "「[fn]......Hah, you're so good. Ah..."
        ko "It feels so good through my whole body,{p}ah it feels weird, I'm getting close...{p}Aaaaaaaah! 」"
        "That was sudden."
        "At that moment I thrust,{p}even deeper into him in excitement."
        "Kounosuke's body trembles,{p}and his hot flesh constricts around me."
        "I've become sensitive from the heat, friction,{p}and tight squeezing.{p}The inside of my head is hazy and goes blank."
        fn "「Ah, dah, Kounosuke...!{p}\ \ You're so tight, it-it's coming out! 」"
        
        stop sound fadeout 7.5
        play sound2 heartbeat
        scene white with qdis
        scene ev_kounosuke_1 with qdis
        pause .75
        play sound2 heartbeat
        scene white with qdis
        scene ev_kounosuke_1 with qdis
    
        ko "「Aah. I-I'm cumming, [fn], ah, aah! 」"
        "「AAAAAH! 」"
        
        scene white with sdis
        scene black with sdis
        
        "「...... 」"
        
        scene hbroom red with sdis
        show ko 107 red at center with wipe_right
        play music free31
        $ renpy.music.set_volume(0.75, 0.0, channel = "music")
        
        ko "「That felt good, I'm so tired. 」"
        fn "「Yeah... 」"
        "We lay facing each other on the futon,{p}completely exhausted and spent."
        fn "「I feel like I've been wrung out... 」"
        "Both of us in that moment,{p}there's nothing you can compare,{p}to that powerful squeezing."
        "I'm not able to move any more."
        "Meanwhile, Kounosuke's body convulses.{p}In order to squeeze out every last drop of cum,{p}I tighten myself over and over again."
        "The feeling of pleasure has passed,{p}and all the strength in my body has been drained.{p}Yet thanks to that, strength doesn't enter my body."
    
        show ko 102 red with dis
        
        ko "「Nyahaha, so, was it good? 」"
        fn "「It was too good... 」"
    
        show ko 101 red with dis
        
        ko "「I felt really good too.{p}\ \ Even though I was scared, I couldn't stop it..."
        ko "And in the end, you came inside me.{p}Just as I thought, a real one is different. 」"
        fn "「...A real one? 」"
        ko "「...... 」"
    
        show ko 105 red with dis
        
        ko "「Uh... 」"
        "Kounosuke-kun, what could that possibly mean?{p}Is that thing you're talking about a sex toy?"
    
        show ko 108 red with dis
        
        ko "「C-can you act like you...{p}\ \ didn't hear that just now? 」"
        fn "「No way. I mean, do you really have it?{p}\ \ A fake one? 」"
        "Furthermore, he's talking as if,{p}he has experience using it?"
    
        show ko 111 red with dis
        
        ko "「T-that's enough about that. 」"
        fn "「So you've been preparing,{p}\ \ for this on your own? 」"
    
        show ko 105 red with dis
        
        ko "「No, but I have been interested in it for a while.{p}\ \ I'd say I was preparing because,{p}\ \ I wanted my first time to feel good. 」"
        fn "「You're a sullen pervert. 」"
    
        show ko 111 red with dis
        
        ko "「Sh-shut up! {nw}"
        show ko 108 red with dis
        extend "All men are perverts.{p}\ \ You are too, you just came inside me earlier! 」"
        fn "「Er, well... 」"
    
        show ko 111 red with dis
        
        ko "「So we're done talking about this! 」"
        fn "「O-okay, okay! 」"
        "While trying to calm his vigorous snapping,{p}I think that if he was going to be like this,{p}then I should have bottomed to begin with."
        "There was no need for rock paper scissors."
    
        show ko 102 red with dis
        
        ko "「Well then, [fn]! 」"
        fn "「Huh? What? 」"
        "Kounosuke suddenly covers me from above."
        ko "「Since you did it first, now it's my turn! 」"
        fn "「It's your... wait. 」"
        "He has the lotion in his hand again,{p}and has now started to smear it on my private area."
        fn "「W-wait a minute! Give me a break! 」"
        
        show ko 105 red with dis
        
        ko "「But that's not fair! 」"
        "I try to resist as hard as I can,{p}with my still-tired body,{p}but I can't do a thing."
        "He steadily hastens his \"preparations\".{p}I decide to prepare myself for the worst."
    
        stop music
        play sound door_slide
        pause 4
        
        gm "「We're back! 」"
        "I hear a voice from the front door,{p}and feel my body temperature immediately drop."
        
        play music free44
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        show ko 106 red with dis
        
        fn "「OH SHIT. 」"
        ko "「Aww fuck, w-w-w-what do we do!? 」"
        fn "「Just get your clothes back on! 」"
        
        if persistent.replay == True:
            scene black with dis
            $ renpy.end_replay()
            
        $ persistent.event_kounosuke1 = True
        
        scene black with dis
        scene hbroom red with dis
        show ko 001 red at center with wipe_right
        
        gm "「Sorry for being late.{p}\ \ I'll get dinner started right away.{p}\ \ Oh my, it's Kounosuke-kun. 」"
        
        show ko 002 red with dis
        
        ko "「H-hello. 」"
        gm "「You're welcome here any day.{p}\ \ Is your homework going well? 」"
        fn "「Y-yeah. I just finished it. 」"
        gm "「Oh, good for you. Ah, Kounosuke-kun,\n\ \ would you like to stay for dinner?"
        gm "I'd like to thank you,\nwith a meal for helping out! 」"
        
        show ko 001 red with dis
        
        ko "「Oh, okay. In that case, I'll take it. 」"
        gm "「Well then, I'll call your house.{p}\ \ I am a grandmother,{p}\ \ so I'll put all my effort into it."
        gm "Please look forward to it! 」"
        "Then, right as my grandma,{p}is about to leave the room..."
        gm "「Hm? Isn't it too early,{p}\ \ to be laying out your futon? 」"
    
        show ko 003 red at shivering with dis
        
        fn "「Huh? Ah, th-this is... 」"
        gm "「Well, you should put it away.{p}\ \ Don't you think you're being discourteous?{p}\ \ Sorry about the dirty room, Kounosuke-kun. 」"
        
        show ko 001 red with dis
        
        ko "「N-no... 」"
        gm "「Put it away neatly. 」"
        fn "「Y-yes. I understand! 」"
        "Somehow, I got my grandma,{p}out of the room and I close the door.{p}Finally, we let out a sigh."
        
        play music cicada01 fadein 4
        $ renpy.music.set_volume(0.4, 0.0, channel = "music")
        show ko 005 red at still with dis
        
        ko "「Th-that was close... 」"
        fn "「Huh, really, Kounosuke. Really. 」"
        "Both of us are dripping cold sweat.{p}But we're relieved that we were able,{p}to somehow keep our secret."
        fn "「W-we're done for screwing around today.{p}\ \ Literally. 」"
        ko "「You're right... 」"
    
        show ko 011 red with dis
        
        ko "「But I'm definetely topping next time! 」"
        fn "「Shhh. what if they hear you!? 」"
        
        show ko 005 red with dis
        
        ko "「Oh, sorry. 」"
    
        show ko 001 red with dis
        
        ko "「But you have to promise.{p}\ \ It's a promise between lovers,{p}\ \ so I'll get seriously angry if you break it! 」"
        fn "「O-okay... 」"
        "After that, we finished cleaning up,{p}until dinner time."
        "We managed to avoid any more problems,{p}for the rest of the day."
        "And most importantly...{p}I was forced to keep that strange promise."
    
        jump end29

##########################################################
label tatsuki29:
    
    $ event_name = _("Feeling the Wind")

    play music wind_noise fadein 5
    scene prairie with sdis
    
    fn "「The day has finally come. 」"
    "Today we've all gathered at the airfield.{p}Today is the day we'll fly the plane."
    "It's the second time the plane's been completed."
    "Mostly, all it needed was adjustments,{w=.2}\nso the project went smoothly and quickly."
    
    show ni 001 at center with dis
    
    ni "「The preparations are done.{p}\ \ There're no problems this end,\n\ \ and the weather is good.{w} It can go at any time. 」"

    hide ni with dis
    show ta 001 at center with dis
    
    ta "「Well then, I'm going. 」"
    fn "「Wait,{w=.2} let me come, too. 」"
    
    show ta 006 with dis
    
    ta "「Don't you get it?{p}\ \ We don't know what's going to happen.{p}\ \ It might crash again... 」"
    fn "「Mmm, that's fine.{p}\ \ As long as we're together.{p}\ \ If you're going, I'm coming with you. 」"
    
    show ta 008 with dis
    
    ta "「It's pretty dangerous...{w=.2}\n\ \ Are you sure? 」"
    fn "「You promised, remember?{w=.2}\n\ \ That I'd come with you when you flew.{p}\ \ I believe in you, Tatsu-nii. 」"
    
    show ta 001 with dis
    
    ta "「...All right.{w} Get in behind me. 」"

    hide ta with dis
    
    "We both boarded the plane, then turned the key."
    play sound plane_start loop
    
    "The engine sprang to life,\nas though it was tired of waiting."
    
    show cu 002 at center with dis
    
    cu "「Have a safe trip!{w} Be careful, now. 」"
    
    scene runway1 with sdis
    
    ta "「Here we go,{w=.2} partner. 」"
    fn "「Let's go.{w=.2} To the skies! 」"    
    "The plane turned to face the runway.{p}While it's happening the same as before,\nthis time I'm riding alongside."
    "I won't be separated again."
    
    $ renpy.music.set_volume(0.5, 0.0, channel = "sound")
    scene runway1 with dis
    scene prairie
    show ni 001 at midright
    show cu 008 at midleft
    with wipe_right
    
    cu "「They'll be all right...{w=.2}\n\ \ My heart's poundin' like crazy. 」"
    
    show ni 003 with dis
    
    ni "「Let's hope for the best.{p}\ \ We can't do anything else for them. 」"
    
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound")
    scene runway1 with wipeleft
    
    "Eep, my nerves are getting to me.{p}This is just like the start of a roller coaster.{p}There's so much suspense."
    ta "「It's all right to get off if you're afraid.{p}\ \ You can still make it off here. 」"
    fn "「I'm not getting off.{p}\ \ I'm going to fly too. 」"
    "Still, I'm scared... Huh?"
    
    menu:
        "A. What's that?":
            jump tatsuki29_friends
        "B. What's this?":
            jump tatsuki29_destruction

    ######################################################
    label tatsuki29_friends:

        $ event_name = _("Our Friends")
        
        who "「Heeey, over here! Here! 」"
        "As we were approaching the runway,\nwe heard a voice calling out from somewhere."
        fn "「To-{w=.2}Torahiko? 」"
        
        scene runway1 with dis
        stop sound fadeout 1
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        scene prairie
        show ju 001 at farright
        show ka 001 at farleft
        show to 001 at center 
        with wipe_right
        pause 1
        show to 003 with dis
        play music melodious07
        
        to "「Hey, what's with the big secret?{w=.2}\n\ \ You two were being all sneaky.{p}\ \ We'd have helped, if you'd said something. 」"
        ta "「My bad,{w=.2} I didn't want to bother you guys. 」"
        
        show ju 002 with dis
        
        ju "「...If Tora helped you,\n\ \ this would probably get delayed. 」"
        
        show ka 003 with dis
        
        ka "「You can say that again. 」"
        
        show to 005 with dis
        
        to "「What...{w=.2} that's not true. 」"
        
        scene prairie
        show si 001 at farleft
        show su 001 at center 
        show ko 001 at farright
        with wipe_right
        show ko 002 with dis
        
        ko "「Yoohoo!{w} [fn], Tatsu-nii, you all right? 」"
        
        show su 002 with dis
        
        su "「Wooow!{w=.2}　This is the first time I've seen a biplane!{p}\ \ Cool!! 」"
        
        show si 004 with dis
        
        si "「Flying doesn't particularly appeal to me,{p}\ \ but be careful. 」"
        
        scene prairie
        show so 001 at midleft
        show ky 001 at midright
        with wipe_right
        
        ky "「Come back safely.{w} We'll be waiting for you. 」"
        so "「Please come back in one piece! 」"
        
        scene runway2 with sdis
        
        "It's not just me.{w} Everyone's here.{p}Everyone's...{w=.2} watching over us."
        "Never have things looked so promising.{p}Today, we'll fly.{w=.2} Definitely."
        ta "「It's almost time!{w} 　Are you ready? 」"
        fn "「Of course. 」"
        "We started accelerating,\non the long road that led to the sky."
    
        scene sky with explosion
        
        "Everyone already looks far away,\nand they're had to distinguish."
        ta "「The wind sure is strong today... 」"
        "The sky was clear,\nbut a mighty wind swept over our faces.\nThe engine roared, and our speed ramped up."
        
        scene cockpit with sdis
        
        fn "「Hey,{w=.2} we're already halfway along the runway,\nbut we haven't flown yet... 」"
        ta "「Don't worry.{w=.2} Everything's going to plan. 」"
        ta "「This is an airfield, so it's made for flying.\n\ \ The runway is a bit shorter than usual, though. 」"
        ta "「So, we need to pick up speed on the second half. 」"
        "It feels like we've already reached top speed..."
        "The plane's going to run off the cliff again.{p}We're so close to the edge."
    
        scene white with circle_out
        
        fn "「Please, fly! 」"
        "The meter pointed at max speed."
        "The wind felt like a wall.{p}The edge of the cliff was getting closer..."
        
        scene white with dis
        scene prairie
        show ka 001 at farleft
        show to 003 at center 
        show su 005 at farright
        with wipe_right
        
        to "「Flyyy! 」"
        su "「[fn]-san, Tatsuki-san, please fly! 」"
        ka "「You gotta fly! 」"
        
        scene prairie
        show cu 001 at center 
        with wipe_right
        show cu 002 with dis
        
        cu "「Somehow... Please fly! 」"
            
        play sound plane_engine loop
        $ renpy.music.set_volume(0.8, 0.0, channel = "sound")
        scene cockpit with wipe_right
        
        "The fuselage rattled and shook.{p}There is only a little bit of runway left,{p}and with the speed we're going,{w=.2} we can't stop."
        "Now, I can only see the sky."
        ta " {size=+15}「Uwooooooooh!{w=.2}　Fly, damniiittt!! 」"
        
        $ renpy.music.set_volume(0.0, 1.0, channel = "sound")
        scene prairie
        show ni 001 at center 
        with sdis
        
        "..."
        
        show ni 002 with dis
        
        ni "「It flew. 」"
        
        show ni 003 with dis
        
        ni "「You've got some fine wings, now. 」"
        
        $ renpy.music.set_volume(1.0, 0.0, channel = "music")
        $ renpy.music.set_volume(1.0, 0.0, channel = "sound")
        scene white with sdis
        pause 3
        
        "{cps=10}Oh,{w=.2} the sky is so blue,{w=.3} so radiant..."
        
        stop sound fadeout 1
        stop music fadeout 1
        scene white with dis
        scene white with sdis
        scene plane_near with wipe_right
        pause 2
        scene plane_far with dis
        pause 2
        play music wind_noise fadein 5
        $ renpy.music.set_volume(0.7, 0.0, channel = "music")
        scene prairie
        show ju 002 at farleft
        show ka 001 at center
        show ko 002 at farright
        with wipe_right
        
        ko "「Look! Look! It's flying!{w} 　The plane is flying! 」"
        ju "「...Looks like they succeeded. 」"
        
        show ka 003 with dis
        
        ka "「Phew. My heart almost stopped for a second there. 」"
        
        scene prairie
        show ky 001 at midright
        show so 003 at midleft
        with wipe_right
        
        ky "「I'm still a little worried.{w=.2}\n\ \ It looks like they'll be fine, though. 」"
        so "「Whoa, they're goin' up so high! 」"
        
        scene prairie
        show to 001 at center 
        show si 001 at farleft
        show su 002 at farright
        with wipe_right
        
        su "「So high!! 」"
        
        show si 002 with dis
        
        si "「The sky... it's more beautiful than ever. 」"
        
        show to 007 with dis
        
        to "「They're off...{p}\ \ Tch, I can't do anything, if it's Tatsu-nii. 」"
        
        scene prairie with dis
        
        "The plane rose even higher, vanishing into the sky."
        
        show ni 003 at midright
        show cu 001 at midleft
        with wipe_right
        show cu 006 with dis
        
        cu "「Yeah!{w=.2}　It worked!{p}\ \ Young Master and Aniki flew! 」"
        ni "「...I've fallen for you,\n\ \ so I knew you could do it.{p}\ \ Isn't that right?{w} Tatsuki-kun... 」"
        
        scene white with sdis
        
        jump tatsuki29_flying
    
    ############################################################    
    label tatsuki29_destruction:

        $ event_name = _("Becoming a Legend")
        
        "What do we have here..."
        "There's a red button here,\nwith a skull-and-crossbones drawn on it.{p}It's not a self-destruct button, right?"
        fn "「No way... 」"
        ta "「Hm? You say something? 」"
        fn "「No, nothing. 」"
        "Maybe I should ask him.{p}But is this really a self-destruct button?{p}I get the feeling he'll make fun of me if I ask..."
        "Yah, push it!"
        
        play sound press_button
        
        "Beep."
        
        play sound alert loop
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
    
        scene alert1
        pause .25
        scene alert2
        pause .35
        scene alert1
        pause .25
        scene alert2
        pause .35
        scene alert1
        pause .25
        scene alert2
        pause .35
        scene alert1
        pause .25
        scene alert2
        pause .35
        scene alert1
        pause .25
        
        "「Warning,{w=.2} warning,{w=.2} explosion in ten seconds.{p}Please evacuate at once.{w} Repeat.{w=.2} Warning,{w=.2} warning,{w=.2} explosion in ten seconds. Please evacuate at once. 」{nw}"
        play music free0531
        extend ""
        ta "「Dumbass,{w=.2} that was the self-destruct switch. 」"
        "「10,{w=.5} 9,{w=.5} 8,{w=.5} 7 」"
        fn "「Whaaa! It really was a self-destruct switch!? 」"
        "「6,{w=.5} 5,{w=.5} 4,{w=.5} 3 」"
        ta "「It's only supposed to be used when cornered,\n\ \ isn't that obvious!? 」"
        fn "「Sorry. 」"
        "「2,{w=.5} 1,{w=.5} 0 」{nw}"
        stop sound
        extend ""
    
        scene alert1 with dis
        stop music
        play sound don08
        scene white with sdis
        pause 3
        
        "The plane exploded violently.{p}The blaze burned through the sky,\nwhich then spread across the world."
        "In an instant, Minasato was turned to ash, {w=.2}burning it off the map."
        "This was the beginning of the Cosmic War,\nthe conflict that changed history..."
        "Fin."
        
        play sound rainstorm
        pause 1.5
        scene old_house2 with wipe_right
        play music free60
        $ renpy.music.set_volume(0.6, 0.0, channel = "music")
        
        "Uncle Shigure's Balcony Diary"
    
        show sg 002 at farright
        show cu 001 at farleft
        with wipeleft
        
        sg "「I say. If you press a self-destruct button,\n\ \ of course it's going to blow up. 」"
    
        show cu 006 at hit_right
        
        cu "「Def'nitely blow up. 」"
        
        show sg 001 with dis
        
        sg "「Listen,{w=.2} just think before you make a choice. 」"
        
        show cu 004 with dis
        
        cu "「Yeah! 」"
        
        show sg 002 with dis
        
        sg "「There's not much before this story ends,{w=.2}\n\ \ but don't lose focus.{w} Bad ends lurk everywhere,{w=.2}\n\ \ and don't forget that.{w} Now, until we meet again. 」"
        
        show cu 005 with dis
        
        cu "「Y'know, I've been thinkin' about this for a while,\n\ \ but this bit's meant for hints, right? 」"
        cu "「Every time, we talk about random stuff,\n\ \ but that can't be much o' a hint... 」"
        
        show sg 001 with dis
        
        sg "「There were only two choices,\n\ \ so there's not much of a problem, is there? 」"
        
        show cu 008 with dis
        
        cu "「F'real...? 」"
        sg "「Well then, keep at it for just a bit longer.{p}\ \ Stick with things for a little more. 」"
        
        show cu 002 with dis
        
        cu "「See ya! 」"
        
        scene old_house2 with sdis
        pause 2     
        
        $ persistent.backtrack_name = "tatsuki29"
        play music awkward
        call screen backtrack
    
    ###################################################    
    label tatsuki29_flying:

        $ event_name = _("Skylab")
        
        stop music fadeout 1.5
        play sound plane_engine loop
        $ renpy.music.set_volume(0.8, 0.0, channel = "sound")
        scene sky with sdis
        play music melodious06 fadein 2
        
        ta "「We're flying... 」"
        "Right now, we're in the middle of the blue sky."
        "Sucked up into vast heights\nthat stretch for an eternity."
        "Above, the skies continue on,\nbroken up by a few puffy clouds."
    
        scene cockpit with dis
        
        fn "「It's a weird feeling, flying in the sky like this. 」"
        ta "「We are really high up.{p}\ \ If we fell from here, we'd be completely screwed. 」"
        fn "「Hey!{w} 　Don't joke about that.{p}\ \ If I think about that, I'll get goosebumps. 」"
        ta "「Goosebumps?{w} 　I've got scales, so I don't get it.{p}\ \ Are you gonna turn into a bird and fly off?{p}\ \ Gahaha! 」"
        ta "「Anyway,{w=.2} take a look. That's Minasato. 」"
        fn "「That's Minasato, huh?{p}\ \ It's too small for me to make out...\n\ \ Does that mean that's Kazenari over there? 」"
        ta "「Yeah, and past that mountain is the ocean.{p}\ \ Not long ago, we were all there together... 」"
        fn "「I didn't know there was a\n\ \ wind like this near the village. 」"
        fn "「When we were kids... I always wondered what was\n\ \ just beyond the mountains,{w=.2}\n\ \ but now we're free to go even further. 」"
        ta "「Let's take a look, then, since we can go anywhere.{p}\ \ I'll take you wherever you want to go. 」"
        fn "「Then... I want to see the ocean past the mountain.{p}\ \ I wonder what's past that? 」"
        ta "「Got it. The ocean, yeah? 」"
        fn "「Yeah, I want to see it. 」"
        ta "「Here we go, then.{w} Don't get cold feet! 」"
        fn "「Tatsu-nii's driving, and a plane at that... 」"
        ta "「Don't worry about it.{p}\ \ It's not like there're\n\ \ traffic lights or laws up here. 」"
        ta "「[fn],{w=.2} close your eyes for a bit. 」"
        fn "「Eeh? 」"
        ta "「Just do it, already. 」"
        fn "「Mm, okay. 」"
        "I closed my eyes, just as asked."
        ta "「Next, stick out your chin. 」"
        fn "「Like this? 」"
        ta "「Yeah, that's good.{w} Now don't move. 」"
    
        scene sky with dis
        $ renpy.music.set_volume(0.2, 2.0, channel = "sound")
        
        "{w=1}One second,{w=1} two seconds,{w=1} time flew by, just like the clouds."
        "Suddenly, it's as though the wind stopped blowing,{w=.2}\nand something warm pressed against my lips."
        fn "「Mng... 」"
        "We kissed.{p}In the middle of the streaming wind,{w=.2}\namidst skies died blue."
        "A long, passionate kiss..."
        ta "「...Finally, we made it. 」"
        ta "「I promised I'd take you up into the sky, didn't I? 」"
        "The skies continued out forever."
        "Without a doubt, Summer will fade into the sky,\nand the next season will follow on."
        "But for now, Summer is in the middle of it all."
        "There's nowhere in the world I'd rather be..."
        
        scene sky with dis
        scene black with wipeleft

        $ event_name = _("Embers")

        stop music fadeout 2
        stop sound
        pause 2
        scene old_house_inside with wipeleft
        play music daily02
        $ renpy.music.set_volume(0.7, 0.0, channel = "music")
        
        "At the end of the day, after we landed,\nTorahiko and everyone else\nheld a congratulatory party."
        "This also doubled as my farewell party,{w=.2}\nso the party continued well on into the night."
        
        show ta 001 at center with dis
        
        ta "「Guys, sorry for all the trouble. 」"
        
        hide ta with dis
        show to 001 at farleft
        show ko 001 at midleft
        with wipeleft
        
        to "「Nah, it's for your launch occasion. 」"
        
        show to 007 with dis
        
        to "「Besides, we already knew you were going to fly. 」"
        
        show ko 002 with dis
        
        ko "「Yeah, yeah,{w=.2} we're here for [fn]'s sake. 」"
        
        show ta 004 at farright with wipeleft
        
        ta "「Why you, you'd better not forget this.{p}\ \ Otherwise I'll bomb your roof with timber. 」"
        
        show to 005
        show ko 006
        show si 002 at offright_far
        with dis
        show ta at move_midright(0.5)
        show si at move_farright(0.5)
        
        si "「Uh-huh...{w=.2} In the event that actually occurs,\n\ \ I wonder if it'd be all right to have\n\ \ Tatsuki-san fix our houses. 」"
        
        show ta 002 with dis
        
        ta "「Of course, but you'd have to pay for it. 」"
    
        show to 003 with dis
        
        to "「Ogre. 」"
    
        show ko 005 with dis
        
        ko "「Demon. 」"
        
        show ta 008 with dis
        
        ta "「Hehe,{w=.2} I can also do some rennovation\n\ \ while I'm fixing stuff.{p}\ \ It's really gonna cost ya, though... 」"
        
        scene old_house_inside
        show ky 001 at farright
        show ka 001 at farleft
        show so 001 at midright
        with wipe_right
        
        ky "「Tatsuki-san...{w=.2} you sound like a corrupt dealer. 」"
    
        show so 005 with dis
        
        so "「'S terrible... 」"
        
        show ka 005 with dis
        
        ka "「If there's a complaint about the cost,{w=.2}\n\ \ we'd probably get taken\ninto Tappei-san's office... 」"
        
        scene old_house_inside
        show ta 002 at center
        show ko 001 at farleft
        with wipe_right
        
        ta "「Oh yeah, and the other guys will...{w=.6}\n\ \ {nw}"
        show ta 004 at briefzoom
        extend "{w=.2}wait, I won't do anything like that. 」"
        
        show ko 005 with dis
        
        ko "「So the Midoriya Group works like that, eh... 」"
        fn "「There's probably some buildings around that{w=.2}\n\ \ have corners cut on earthquake-proofing and whatnot. 」"
        
        show ta 010 with dis
        show ni 001 at offright_far        
        
        ta "「Hey, you helped work on those houses too, you know. 」"
        
        show ni at move_farright(0.5)
        
        ni "「As for the employees, we get paid little,\n\ \ and get worked like horses. 」"
        
        show ta 004 with dis
        show to 001 at offleft_far
        
        ta "「Nikaidou!! 」"
        ta "「You work on houses, too, don't you? 」"
        
        show ta at move_midright(0.5)
        show ko at move_center(0.5)
        show to at move_farleft(0.5)
        with regmove
        
        to "「The heir over there probably sucks. 」"
        fn "「Yeah, he's like a greenhorn who\n\ \ keeps messing everything up. 」"
        
        show ni 002 with dis
        
        ni "「He doesn't even come close to my skills. 」"
        ta "「You bastards... 」"
        
        scene old_house_inside
        show cu 004 at center
        show si 001 at midleft
        show ka 001 at farright
        with wipe_right
        
        cu "「Daaah!{w} 　Get ahold of yourself.{p}\ \ Craftsmen won't put up with insults\n\ \ about their skills!! 」"
        
        show si 003 with dis
        
        si "「...This talk doesn't concern you. 」"
        
        show ni 001 at farleft behind so with wipe_right
        
        ni "「No concern whatsoever. 」"
        ni "「However, that's also his work...{p}\ \ Now, would you mind? 」"
    
        show cu at jump_up
        pause .2
        
        cu "「I can't take it anymore!{w=.2} I challenge you!! 」"
        
        show ka 005 with dis
        show ju 002 at offright_far behind cu
        
        ka "「Isn't that something Tatsu-nii should be saying? 」"
        
        show cu at move_midright(1)
        show ni at move_midleft(1)
        show ka at move_offright_far(1)
        show si at move_offright_far(1)
        show ju at move_farright(1)
        
        ju "「Hmm.{w=.2} I'll take you on. 」"
        
        show ni 003 with dis
        
        ni "「Your challenge has been accepted.{p}\ \ First one to get a point wins. 」"
    
        show cu 006 at briefzoom
        pause .2
        
        cu "「H-huh?{w} I was just kiddin',{w=.2} kiddin'! 」"
        
        show ju 006 with dis
        
        ju "「I'll go easy on you, if you face me head on. 」"
        ky "「Right,{w=.2} do your best. 」"
        
        show ko 004 with dis
        
        ko "「It's a big room with tatami mats,\nso there shouldn't be any problems. 」"
        cu "「Wa-{w=.2}wait... 」"
        
        show ni at move_offleft_far(0.5)
        show cu at move_midleft(0.5)
        show ju at move_midright(0.5)
        
        ta "「Begin the match! 」"
        ju "「Here I come! 」"
        
        show ju at move_farright(10)
        scene black with sdis
        
        #!#Get all of this in order.... should be shaking text box instead of background
        cu "「Hiiiiiii- 」{w}{w=.25}{nw}"
        play sound bosu35
        show black at hshake
        extend "{w=.55}{nw}"
        show black at vshake
        play sound hit_p07
        extend "{w=.35}{nw}"
        show black at hshake
        play sound2 bosu35
        extend "{w=.55}{nw}"
        show black at vshake
        play sound puu75
        extend "{w=.35}{nw}"
        show black at hshake
        play sound2 crash18_a
        extend "{w=.55}{nw}"
        show black at hshake
        play sound bosu35
        extend "{w=.35}{nw}"
        
        $ chuu_beat += 1
        
        "..."
        "......"
        
        scene black with dis
        scene old_house_inside
        show ky 001 at farright
        show ka 001 at midleft
        show so 001 at midright
        with wipe_right
        
        ka "「Well, I gotta go now.{p}\ \ I've got work tomorrow. 」"
        ky "「I guess we should go home,\n\ \ since we have club practice in the morning. 」"
        so "「Guess so. 」"
        
        scene old_house_inside
        show ni 001 at midleft
        show cu 001 at midright
        with wipeleft
        
        ni "「This is a good place to finish up,{w=.2}\n\ \ so how about we call it a night? 」"
        
        show cu 004 with dis
        
        cu "「What, it's over already?{w=.2}\n\ \ Let's have a li'l more fun. 」"
        
        show ni 003 with dis
        
        ni "「Shh...{w=.2} we have to disperse the extras,\n\ \ then give those two some time alone. 」"
        
        show cu 011 with dis
        
        cu "「B-{w=.2}but... 」"
        ni "「Come on, we're going. 」{w} {nw}"        
        show ni at move_offleft_far(0.5)
        show cu at move_offleft_far(0.5)
        extend "{w=.5}{nw}"
        show su 002 at farleft
        show ju 001 at farright
        show ko 001 at midleft
        show si 003 at midright
        with wipeleft
        
        ju "「Later, [ln]. 」"
        ko "「Bye bye, [fn]! 」"
        su "「Goodbye, [fn]-san! 」"
        si "「Take care, [fn]. 」"
        
        scene old_house_inside
        show ta 009 at midright
        show to 001 at farleft
        with wipe_right
        
        ta "「Aren't any of you gonna say anything to me? 」"
        "...It's not the day I go back just yet,{w=.2}\nbut parting with everyone\nlike this feels kind of lonely."
        
        show ta at move_offright(0.5)
        show to at move_center(0.5)
        with regmove
        
        to "「Hey, [fn]. 」"
        fn "「What is it? 」"
        
        show to 010 with dis
        
        to "「Be happy with Tatsu-nii. 」"
        to "「Always get along with him,{w=.2} from now on... 」"
        fn "「Why so formal all of a sudden?{w=.2}\n\ \ I already do get along with him.{p}\ \ Isn't it the same for you? 」"
    
        show to 006 with dis
        
        to "「That's not what I mean... 」"
        to "「Well,{w=.2} about you, I... 」"
        fn "「You... what? 」"
    
        show to 001 at hit_right
        pause .2
        
        to "「Heh,{w=.2} well... it's nothing.{p}\ \ {nw}"
        show to 002 with dis
        extend "It's great that the other guy is Tatsu-nii. 」"
        fn "「Eh-{w=.2}uh-{w=.2}what? 」"
        
        show to 001 with dis
        
        to "「I said it's nothing.{p}\ \ Later, [fn]. 」"
    
        show to at move_offleft(0.5)
        
        "What was that all about?"
    
        show ta 001 with wipeleft
        
        ta "「Hey, what are you standing around for? 」"
        "Well, whatever."
        ta "「Come sit over here.{w} Feels nice. 」"
        "Tatsu-nii called me over to the porch."
        fn "「Mmm, it does feel nice. 」"
        "The evening breeze, the tone of the wind chimes,\nand the smell of the mosquito coil,\nall of it put me in a good mood."
        
        show ta 002 with dis
        
        ta "「Man, today was a huge success. 」"
        "Tatsu-nii talked while he waved his fan."
        fn "「I know,{w=.2} It's great that we made it back safely. 」"
        
        show ta 008 with dis
        
        ta "「What was that?{w=.2}\n\ \ You saying you're afraid of my piloting skills? 」"
        fn "「N-no.{w} That's not what I meant,\nso stop poking me. 」"
        
        show ta 002 with dis
        
        ta "「Heheh.{w=.2} If you told me to stop, I'd stop. 」"
        fn "「Don't touch me there-! 」"
        ta "「What's wrong?{p}\ \ I'm feeling good today,\n\ \ so I'll go through to the end. 」"
        fn "「Tatsu-nii!! 」"
        
        show ta 001 with dis
        
        ta "「And now, I've kept our promise.\n\ \ I've made a dream come true.{p}\ \ Now, I have to become Japan's best craftsman. 」"
        fn "「Yeah. If it's you, you can do it.{p}\ \ Now, let me go. 」"
        
        show ta 008 with dis
        
        ta "「[fn], what are you gonna do?{p}\ \ Is there anything you want to do,\n\ \ or anything you want to be? 」"
        "Tatsu-nii suddenly looked serious as he asked me."
        fn "「I don't know.{w=.2}\n\ \ I haven't really thought ahead about anything yet. 」"
        ta "「...I want to try building a house once in my life. 」"
        fn "「A house? 」"
        ta "「My family is a bunch of temple craftsmen,\n\ \ so we never make anything for people to live in. 」"
        ta "「We're temple carpenters,\n\ \ but it's not like that's all we can build.{w=.2}\n\ \ My family doesn't think about making profits. 」"
        ta "「If we built homes for people when we should be\n\ \ building homes for gods, we'd be punished if we\n\ \ took money for it. So we never did. 」"
        fn "「Tappei-san said the same thing. 」"
        
        show ta 002 with dis
        
        ta "「Still, I want to try building one.{p}\ \ One for you and me to live in. 」"
        
        show ta 007 with dis
        
        ta "「If I do build one...{p}\ \ [fn], will you live together with me? 」"
        "This must be his way of proposing to me."
        "I..."
        fn "「Tatsu-nii... I- 」"
    
        show ta 303 with qdis
        
        ta "「Dah!{w=.2}　Hold on.{p}\ \ I'm not ready to hear it, yet. 」"
        fn "「Tatsu-nii? 」"
        
        show ta 308 with dis
        
        ta "「Well, it's not just me who needs to get ready.{p}\ \ Don't you need to, too?\n\ \ You aren't ready yet, not at all, right?{w} 　Right? 」"
        fn "「Uhh... 」"
        
        show ta 001 with dis
        
        ta "「You don't have to answer right away.{p}\ \ You can think about it. 」"
        "I'm scared.{w} I've just been proposed to..."
        "Haah, it's a man thing,{w=.2} it's not a man thing..."
        
        show ta 002 with dis
        
        ta "「Well then, let's pick up from where we left off.{p}\ \ Push yourself in with all you've got today. 」"
        ta "「I'm not letting you sleep\n\ \ until after at least five shots. 」"
        fn "「Uhh, wait a minute.{p}\ \ I'm not ready- 」"
        
        show ta 009 with dis
        
        ta "「You can't run now.{p}\ \ Make a mess of me tonight!! 」"
        fn "「Tatsu-nii, what you're saying\n\ \ and what you're doing aren't matching up!! 」"
    
        hide ta with wipe_right
        
        "And so I was carried off to Tatsu-nii's futon."
        
        jump end29


##########################################################
label kouya29:
    
    $ event_name = _("What Lies Ahead of Him")
    
    play music piano4_001
    scene kouya_house_out night
    show ka 001 night at center
    with dis
    
    fn "「All right, I'll wait here. 」"
    ka "「Right. 」"
    "I stopped in front of the house, and spoke to Kouya.{p}He gave a nod, but somewhere in there,\nI could see a bit of apprehension."
    "It should have only been a week since Kouya came\nhere, but for me it's been five years.{p}When I thought that,{w=.2} it felt kind of nostalgic."
    "It was that house in front of me.{p}Kouya's parents' home."
    "The place where Kouya made a promise to Kazumi-san.{p}And now, it's the place to reach a conclusion."
    "Yesterday's band contest.{p}We came over today to tell them the results."
    ka "「...Now,{w=.2} just wait for me. 」"

    hide ka with wipe_right
    
    "He looked pointedly at the light\npeeking out through the window,\nthen he slowly walked inside."
    "I gave him a tiny nod, and saw him off."
    "After making sure that Kouya had gone in,\nI leaned on a nearby telephone pole to wait."
    "Last time I was house-sitting,{w=.2}\nbut this time I'd come along at Kouya's request."
    "I'd thought about whether we should go together,{w=.2}\nbut when Kouya had blushed and said 「I want us 
    to go together, 」 there wasn't any other choice."
    "But this is as far as I can go.{p}The other side of the door\nis a place I can't enter at the moment."
    "And now,{w=.2} since I'm alone,\nthe night breeze feels a bit chilly."
    fn "「Sigh... 」"
    "I gave a small sigh, and looked upwards.{p}The whole starry sky spread out in front of me."
    "As it continued on forever,\nit seemed to reflect a bit of myself."
    
    stop music fadeout 5
    
    "It seemed to fill itself up with one's own feelings,{w=.2}
    or at least, so I think."

    scene black with rotation
    
    $ event_name = _("The Last Gate")
    
    "As the door made its usual sound,{w=.2}\nit opened onto a familiar corridor\nthat looked untouched by time."
    "Since the lights weren't turned on,{w=.2}\nthe light coming from the living room\nwas the only illumination."
    "I stepped into that gloomy space,\nand the weight in my chest got heavier."
    "That was my anxiety and tension.{p}That, and the wall that had\nbeen built up over half a year."
    "There was nothing else."
    ka "「... 」"
    "The combined weight of these feelings gave me pause."
    "I have to do this.{p}I've already come this far.{p}I can't go back."
    "...There's nothing else but to keep going."
    "My mind kept telling me that\nas I took a deep breath."
    "That decided it.{p}What I said at the start,{w=.2}\nwhat I would be saying now, all of it."
    "I took a step forward to shed some of the emotions\ncoiling around my heart,{w=.2} then stretched my hand\nout to push open the second, and last, door."
    
    play sound door04
    scene white with dis
    scene kouya_house_in with wipe_corner
    play sound clock_tick loop
    
    "The room I had been dreading greeted me.{p}Only the sound of the clock could be heard, {w=.2}\n{nw}"
    play sound2 hinge
    extend "and the door hinges creaked as they showed me in."
    "At the noise, Mom and... 
    that person... looked towards me."
    "To answer those looks, I didn't hesitate,{w=.2}\nand I didn't falter, I just spoke the words\nthat I had decided on earlier."
    ka "「I'm back. 」"
    
    scene black with wipe_right
    
    $ event_name = _("Last Stop of the Ticket Stub")

    scene kouya_house_in with wipe_right
    play sound2 dishes
    
    "A little bird chirped,\nand there were cups placed on the table."
    "Mom had set down drinks for three,\nand she sat facing me."

    show mi 002 with sdis
    
    $ encounter_mitsuhisa = True
    
    "Next to her was the father I continued to avoid,{w=.2}\nsitting there with his eyes closed."
    "The way he was rejecting me hurt,{w=.2}\nand I wanted to turn my eyes away."
    "But that's not what I came here to do.{p}I've made up my mind, and come all the way here,\nso looking away from him wouldn't be helpful."
    "Even though he won't look this way,\nI won't make any rash actions.{p}I focused my attention forward."
    kz "「So, what happened?{p}\ \ You came all the way over at this hour. 」"
    "Mom must have noticed my intentions,\nas she opened up the conversation for me."
    "She should already know why I'm here,{w=.2}\nyet she plays dumb."
    "I gave some thanks inside my heart,\nand took a deep breath.{p}Then I spoke."

    stop sound
    play music piano3_014
    
    ka "「I came over today to apologize.{p}\ \ For everything up until now,\n\ \ and for everything after this. 」"
    ka "「...Yesterday, there was a big contest.{p}\ \ If we did well in it, there was a chance\n\ \ we could make our debut there. 」"
    ka "「My friends and I participated in it.{p}\ \ It was always my dream.{w} I always wanted to\n\ \ express something through music to someone. 」"
    ka "「I've always thought that, even before I left.{p}\ \ Even now, my feelings on that haven't changed. 」"
    ka "「...Back then, you told me.{p}\ \ You said that this world was full of people like me.{p}\ \ You said to 'take a closer look at reality'. 」"
    ka "「It's true, I thought about that.\n\ \ But I knew, right from the beginning. 」"
    ka "「What I wanted to do was reckless,{w=.2}\n\ \ and I didn't have to do it. 」"
    ka "「I'm sure there could always be\n\ \ someone else who could've taken my place. 」"
    ka "「But I wanted to give it a shot.{p}\ \ It didn't matter if anyone could do it,\n\ \ I wanted to try it out myself. 」"
    ka "「And so, if I ever realized I was no good\n\ \ that might've been okay.{w} If I'd tried and failed,{w=.2}\n\ \ I probably would have given up. 」"
    ka "「But I couldn't give up before trying.{p}\ \ So I left home. 」"
    ka "「In half a year, I've made it this far.{p}\ \ I've tried to keep going, however I could.{p}\ \ To struggle onward to the place I was aiming for. 」"
    ka "「I had no idea if it was going\n\ \ to be a long journey or not.{w} But, during that time,\n\ \ I discovered many things inside myself. 」"
    ka "「That's why I came over today to apologize. 」"
    ka "「Mom, Dad.{w} For everything up to now,{p}\ \ all the troubles and worries I've caused you,{p}\ \ I'm sorry. 」"
    ka "「It's been such a long time coming,{w=.2} but I thought,\n\ \ if only if I could've spoken more clearly then.{p}\ \ I'm truly, honestly sorry for everything. 」"
    "I hung my head a little."
    "With those words,{w=.2}\nthe weight in my chest lifted a little."
    "For half a year, I'd pretended not to notice\nthese feelings in my heart\nthat came from somewhere."
    "I thought that the huge gap between us\nhad gotten a bit smaller,{w=.2} just a little bit."
    ka "「...But- 」"
    
    stop music fadeout 5
    
    "However, I can't be satisfied with that.{p}I still had so many things I needed to say,\nthings I had to get through."
    "I didn't just come here to look back at the past.{p}...I also came for the sake of continuing on."
    ka "「But I guess...{p}\ \ I won't be coming back, after all. 」"
    
    play music melodious07
    
    ka "「I think it'll be the same as the first time I left.{p}\ \ What I want to do could be done by anyone else,\n\ \ and it was very reckless. 」"
    ka "「Even then, it's not as if\n\ \ it's something I have to do. 」"
    ka "「...From the bottom of my heart, I honestly thought\n\ \ that we could make the Grand Prix. 」"
    ka "「Because of that,{w=.2}\n\ \ I want to try and go as far as I can. 」"
    ka "「This might just be selfishness,{w=.2}\n\ \ but in the end, I want to go as far as possible,\n\ \ until I understand myself. 」"
    ka "「Because of everything that's happened, I don't think\n\ \ you'd be happy with such a simple explanation.{p}\ \ I'm not confident I can really explain it, either. 」"
    ka "「But if it's possible,\n\ \ for all the things I've done...{p}\ \ Please forgive me. 」"
    "As I quietly informed them,{w=.2} Mom's face\nlooked a bit lonely."
    "And then:"
    kz "「I see... 」"
    "She looked a bit pale,{w=.2}\nbut she answered me clearly."
    "My chest hurt,{w=.2} just a little bit."
    "I'm sure that Mom always wanted me to come back.{p}But, on the other hand,\nshe always did cheer me on."
    "That must be why she made me promise.\nIf I did well, then she could stop worrying...\nMaybe."
    "But even if she felt that way,{w=.2}\nI think she really did want me to come home."
    kz "「Then you've already decided? 」"
    ka "「Yeah.{p}\ \ It's not like I'll stop living alone, move back here\n\ \ and then pick up from where I left off... 」"
    ka "「It's just... for a little while longer,{w=.2}\n\ \ I want to try walking by myself. 」"
    mi "「You want to try walking by yourself,{w=.2} you say. 」"
    
    show mi 001 with dis
    
    "When he suddenly spoke up,\nI turned to face him in surprise."
    "Up until now, my dad had sat\nthere with his eyes closed,{w=.2}\nbut now he was looking straight at me."
    mi "「Do you understand what you just said?{w=.2}\n\ \ The meaning of those words? 」"
    "Rather than questioning, his strong tone implied\nthat he was looking for confirmation."
    "It's the same stern demeanor.{p}As I remembered my respect for him,\nI forgot the words I was about to say."
    mi "「I've always said that life is a series of choices,\n\ \ that there are many different ways to the same end. 」"
    mi "「Originally, one starts on their own.{p}\ \ That never changes, no matter the circumstances. 」"
    mi "「But often, people form connections with others.{p}\ \ When someone makes a decision, another choice\n\ \ and outcome becomes closed off. 」"
    mi "「Those would be families, parents, children,{w=.2}\n\ \ and true friends.{p}\ \ Close relationships all the more so. 」"
    mi "「People meet and influence each other,\n\ \ then they continue on. 」"
    mi "「When you say you walk by yourself,\n\ \ you're saying you'll shoulder all the\n\ \ responsibilities of your choices by yourself. 」"
    mi "「Just as you have, ever since you've left. 」"
    mi "「But that by itself is not enough.{p}\ \ When you walk alone, you also have 
    to walk the path you picked. 」"
    mi "「Instead of running from your emotions,\n\ \ shoulder your responsibilities.{p}\ \ But don't just be stubborn, have some flexibility. 」"
    mi "「It sounds obvious, but it's not that simple. 」"
    mi "「It doesn't help that the path\n\ \ you chose is a thorny one. In the future,\n\ \ it's likely to be even steeper and painful. 」"
    mi "「Keeping a definite goal will become difficult,\n\ \ and if you lose focus even for a moment,\n\ \ you'll lose track of where you're going. 」"
    mi "「If you ever lose your conviction,\n\ \ you'll never make your dream come true.{p}\ \ It's that deep. 」"
    mi "「...Still,{w} you're prepared to go through with this? 」"
    "He asked me that question again.{p}As he threw another pointed look at me,\nit felt like the temperature in the air dropped."
    "However, that wasn't fear and anxiety pressing in,{w=.2}\nbut more the feeling of my determination.{p}After all, I'd already decided my answer."
    "This time, I didn't hesitate, and I spoke up."
    ka "「Yeah.{w} Even if something is waiting, I'm going. 」"
    
    show mi 002 with dis
    
    mi "「I see. In that case, 
    wait for a minute. 」"

    hide mi with dis
    
    "My dad said that as he got up,\nthen left the living room."
    "He came back a moment later with\na case that looks familiar."
    "It was a guitar case."
    
    show mi 001 at center with dis
    
    mi "「I don't really know if this is something good.{p}\ \ The manager of an instrument store chose it for me.{p}\ \ ...Take it, as a farewell gift. 」"
    "Whatever expression I had on my face,\nI couldn't tell.{p}It was probably complete surprise."
    "At the same time, my heart was beating in my ears."
    "I opened up the case on the table carefully as if\nit would break at any rough treatment."
    
    play sound load_gun
    
    "And inside it...{w=.2} was an antique guitar,\nalong with a piece of paper.\nI've seen this at the shop. "
    "The guitar could be called a vintage piece.{w=.2}\nThis sort of thing is normally expensive."
    "I've always joked that if I made my debut\nI'd go and buy this sometime."
    "Sitting alone on top was that tiny piece of paper,\nand I feel like I've seen it somewhere before,{w=.2}\nbut I can't remember where."
    mi "「Do you understand, Kouya?{p}\ \ What I said before wasn't a lie. 」"
    mi "「If your mind is made up, I won't repeat myself.{p}\ \ Don't hesitate, walk on the path you believe in.{p}\ \ Grab your dream with your own hands. It's your life. 」"
    ka "「...Yes. 」"
    mi "「That's all I have to say. 」"

    play sound standup
    
    "My dad stood up again, then turned his back to me.{p}「Get going, already, 」 he seemed to say."
    "But before he left the room,{w=.2}\nhe looked over his shoulder at me."
    
    show mi 004 with dis
    
    mi "「...No, there's one more thing.{p}\ \ I don't really understand music... 」"
    
    show mi 003 with dis
    
    mi "「But yesterday's performance was quite good. 」"
    mi "「Come visit us, once in a while. 」"

    hide mi with sdis
    
    "When he said that,{w=.2} I remembered."
    "The little scrap of paper in the guitar case.{p}It's a ticket stub from the contest yesterday."
    "When I realized what it was, my eyes grew hot."
    "I stood bolt upright, and called out to him."
    ka "「Thank you, Dad...! 」"
    "The dam in my chest unblocked,{w=.2}\nmy eyes filled with tears."
    "At the edge of my blurred vision, Mom smiled."
    
    stop music fadeout 3
    scene black with sdis

##################################################
label kouya29_sex:

    if persistent.replay == True:
        $ first = persistent.name_first
        $ last = persistent.name_last
        $ day = 29
   
    $ event_name = _("His Tune")

    scene kouya_house_out night with dis
    play sound night_insects loop
    
    "I had no idea how long I've\nbeen looking at the night sky."
    "When I did notice, a fair amount of time had passed,{w=.2}\nand Kouya was standing in front of me."
    
    show ka 001 night at center with dis
    
    fn "「...Is it over? 」"
    ka "「Yeah.{w} I've finished it properly. 」"
    "When I saw his clear expression, I felt relieved."
    "I pushed myself off the telephone pole,{w=.2}\nand the two of us walked slowly along the road.{p}Our shadows stretched out along the country path."
    "While we walked back to the apartment,{w=.2}\nKouya told me about what had happened."
    "Told me about how he planned to keep going\nwith the band and not return home.{p}About how his dad forgave him."
    "And now, about the guitar he was holding."
    "He seemed a bit embarrassed as his tail wagged,\nand he relaxed a little as he spoke.{p}I'm glad, really."

    scene black with sdis
    stop sound
    scene bedroom night with dis
    show ka 001 night at center with dis
    
    ka "「Hey,{w=.2} [fn]. 」"
    fn "「Hm? 」"
    "Right after we got back inside, Kouya called me\nwhile I was looking out the window.{p}The lights weren't even on yet."
    
    show ka 006 night with dis
    
    ka "「For now,{w=.2} will you...{w=.2} give me a moment? 」"
    fn "「Okay, but...{p}\ \ what's going on that you\n\ \ have to sound so formal for? 」"
    ka "「Nothing,{w=.2} it's just that I wanted you\n\ \ to be the first to hear me play on this... 」"
    "When he said that, he held up the guitar case\nhe was given.{w} That seems to be it."
    fn "「Uh,{w=.2} well I certainly don't mind, but...{p}\ \ You're sure,{w=.2} about me being first? 」"
    fn "「Wouldn't it be better to play it tomorrow,\n\ \ in front of Keisuke-san and the other-- 」"
    "Kouya quietly shook his head as I spoke."
    ka "「It's true that I want to tell everyone tomorrow...{p}\ \ {nw}"
    show ka 001 night with dis
    extend "But I want you to be the first to hear it. 」"
    "Kouya's eyes shone in the\nmoonlight as they looked at me."
    "I've always thought this,\nbut this particular expression is so mean."
    "I can never refuse him when he looks at me like that."
    "Well, although I tried to resist,{w=.2}\nI was honestly happy, and didn't plan on saying no."
    fn "「In that case,{w=.2}\n\ \ I guess I'll take you up on that. 」"
    
    show ka 002 night with dis
    
    "Kouya smiled at that response, then sat down
    in the chair as he opened up the case.{p}{nw}"
    play sound load_gun
    extend "I sat down next to him and waited."

    hide ka with dis
    
    "I thought about turning on the lights, but as there\nwas plenty of light from the window,{w=.2} I stopped.{p}I wanted to try listening in this kind of atmosphere."
    "Kouya took out the guitar and gave the strings
    a flick to test them."
    "Six notes echoed in the room in a rough chord."
    ka "「... 」"
    "Without saying anything, Kouya\nimmediately started tuning it."
    "Each time he strummed the strings,\nthe sounds started to harmonize,{w=.2}\nand when it was complete, it felt nice."
    
    play sound guitar_tune
    
    "Soon, after tuning the sixth string,\nand Kouya winked at me."
    "I picked up on that, and replied with a nod.{p}Then, Kouya slowly started playing a song."
    
    play music free0344
    
    "I knew which song it was from the first few notes."
    "Yesterday's contest.{p}It was the second song they'd played,\nthe one Kouya had written,{w=.2} that song."
    "There was no bass,{w=.2} drums, or vocals.{w=.2}\nIt's a piece played only with the guitar."
    "It felt even more heartrending\nthan when all four of them played it."
    "Even so, the notes wrapping\naround me felt warm and gentle."
    "The calming effect was like being\ngently rocked by the ocean waves."
    "It's almost as if the guitar itself\nwas carrying me along on its sound."
    "However,{w=.2} I'm sure it wasn't just that."
    "I'm sure it came together with Kouya's feelings,\nand made the notes even deeper."
    "I stayed silent, and the reverberating notes shook me.{p}As that happened, time passed in a blink of an eye."
    
    stop music fadeout 3
    
    "Kouya plucked out the last note,{w=.2}\nand ended with it trailing out peacefully.\nThen, my clapping took its place. {nw}"
    play sound applause
    extend ""
    "It would have been nice to tell him my impressions,\nbut I couldn't find the words for it.{p}So, clapping was all I could do."
    
    show ka 002 night at center with dis
    play sound night_insects loop fadein 3
    $ renpy.music.set_volume(0.5, 0.0, channel = "sound")
    
    ka "「Sorry for being so selfish. 」"
    fn "「No, it's not like that.{p}\ \ I like hearing you play. 」"
    ka "「Haha,{w=.2} hearing the one I love say that\n\ \ really makes me happy. 」"
    "It feels kind of uncomfortable to hear Kouya say that.{p}Even though he's told me to my face before,\nI guess I'm still not used to it."
    "I unintentionally looked down at the floor."
    "When he saw that, Kouya gave a small laugh."
    "When I heard that laugh, I looked up in indignation,{w=.2}\nbut Kouya's whole face filled my field of vision,\nthen passed right next to mine."

    show ka 001 night big at center_big with dis
    
    "At the same time,\nmy body was wrapped up in a fluffy warmth."
    ka "「Having things like this,\n\ \ being able to play this guitar,{w=.2}\n\ \ and the fact that I can keep going after my dream... 」"
    ka "「It's all pretty much thanks to you, [fn]. 」"
    fn "「T-{w=.2}that's not true.{p}\ \ It's because you-{w} because everyone worked hard.{p}\ \ I didn't do anything but support you. 」"
    "Since he was whispering so close to my ear,{w=.2}\nI ended up fumbling a bit."
    "My heart pounded wildly as a pair\nof hands firmly clasped around my back."
    ka "「But if you didn't support me,\n\ \ I never would have gotten to this point.{p}\ \ I'll say it again: I truly am thankful. 」"
    
    show ka 002 big night with dis
    
    ka "「Thanks, [fn]. 」"
    "At the edge of my vision,\nI saw Kouya appear like a mirror's reflection."
    "The hand he put on my shoulder felt kind of hot."
    "It might be because I'm feeling excited,\nor maybe because I'm nervous,\nbut I suddenly forgot how to blink."
    "Our faces slowly parted,{w=.2}\nbut our eyes didn't break away."
    "In that instant, Kouya looked straight at me.{p}In the next..."

    hide ka with wipe_right
    
    "Our lips pressed together."
    
    $ event_name = _("The Form of Gratitude")
    
    "Our lips separated, almost immediately."
    "My mouth opened up to protest at that,{w=.2}\nand as though he'd waited for it,\nKouya took my lips again."
    "This time they didn't just touch,{w=.2}\nas his tongue pressed in and\nmade this a more indulgent kiss."
    "That long tongue slowly moved\naround the inside of my mouth."
    fn "「Ph...{w=.2}Ng...{w=.2} 」"
    "Because of that warmth, a ticklish sort of numbness\nspread through my body again, to my inner cheeks,\nmy tongue, and everywhere else."
    "It's like I was beginning to float away,\nlike I was drifting off."
    "Gradually, I stopped thinking.\nI stopped wanting to think.{p}I just wanted to stay like this."
    "The hand Kouya had put on my\nshoulder moved down to my back again,\nthen strongly pulled me into a tight embrace."
    "As if to keep pace with his movements,\nhe pressed his tongue in more forcefully."
    fn "「Mn,{w=.2} ku...u,{w=.2} mm... 」"
    ka "「Ff-{w=.2}...n... 」"
    "On top of me, Kouya really got into the kiss,{w=.2}\nas his tongue started wrestling with mine."
    "All sense of time disappeared.{p}A moment stretched out to forever.{p}Still, that wasn't eternity."
    "Soon, our long kiss ended,{w=.2}\nand the slightly cool night air filled my mouth."
    "For a second, my fuzzy-feeling head cleared."

    show ka 002 night with dis
    
    fn "「I noticed that before...{w=.2}\n\ \ You really like kisses, huh? 」"
    ka "「Maybe...{w} I'm not really aware about it,\n\ \ but you could probably say that. 」"
    
    show ka 003 night with dis
    
    ka "「But with you, it's even more pleasant and intense. 」"
    "After saying that,{w=.2}\nKouya kissed me once more,\nand pushed me into the bed."
    "As I laid back, my shirt got pulled up a little,\nand Kouya put his hand on my exposed skin."
    "It felt like an airy blanket.{p}Each time his fingers touched me,\nmy body twitched a bit, as though shocked."
    
    show ka 001 night with dis
    
    ka "「Does that feel good? 」"
    "Being asked again felt really embarrassing.{p}As my face turned a deep red,\nI gave a small nod."
    
    show ka 002 night with dis
    
    "Seeing me like that, Kouya laughed,{w=.2}\nthen completely took off my shirt."
    "Now that there wasn't anything covering\nmy shoulders, it felt pleasantly cool."
    
    hide ka with dis
    
    "After he tossed my shirt down somewhere,\nKouya kissed me again another three times."
    "This time it was the same as the first one,\njust a quick brush of the lips."
    "I felt his warmth around my mouth, but it immediately\nvanished,{w=.2} and then, just as quickly, I felt\nsomething else start to draw a line down my body."
    fn "「Hi-{w=.2} Uun... 」"
    "It was Kouya's tongue,{w=.2}\ngoing steadily lower,{w=.2} lower,{w=.2} and lower.{p}It hit my sensitive spots countless times on the way."
    "He traced along my collarbone,{w=.2}\nprodded against my nipples,{w=.2}\nthen went around in circles,{w=.2} rotating around my navel."
    "The feeling was more intense\nthan when he used his fingers,\nand it spread throughout my body."
    fn "「Haaah,{w=.2} Kou...{w=.2}ya...! 」"
    "As he kept on, I unintentionally called out."
    "As if in response, the heat\ntraveling across my body\nslowly faded away."
    "It lessened, little by little,\nand as I rode out the feelings of that warmth,\nI stared blankly at the ceiling."
    "However, my respite only lasted a moment."
    fn "「Ngaah-! 」"
    "A sudden shock ran through me,\nmaking me raise my head and cry out.{p}Kouya's form was pressing itself into my groin."
    "It seems that the movements hadn't stopped,\nthey'd just continued downwards."
    fn "「Ahh,{w=.2} kuh...mn! 」"
    "Kouya nibbled a little, causing me to gasp again."
    "All the gentle touching was making my penis ache,{w=.2}\nand the pleasure made it twitch happily."
    "However, the indirectness of the touching 
    felt like such a tease."
    "Kouya probably noticed my mood,\nas he pushed himself up,{nw}"
    play sound tyakuO
    extend "{p}then put his hand on my pants."
    "When I noticed that, I slightly raised my hips."

    play sound standup
    
    "Then there was nothing covering up my body anymore.{p}Kouya followed suit, removing all of his own clothes,{w=.2}\ntossing them at me again, then got onto all fours."

    show ka 101 night at center with dis
    
    "Before long, I saw his golden eyes.{p}They looked so bewitching in the moonlight\npeeking through the window,{w=.2} I blushed a little."
    "As I kept looking at them, spellbound,\nKouya suddenly asked me something."
    ka "「Hey, [fn]. 」"
    fn "「Hm? 」"
    ka "「For tonight,{w=.2}\n\ \ is it all right if we...{p}\ \ go all the way? 」"
    "Since he asked me so hesitantly,\nI didn't immediately grasp the meaning of his words.{p}I tried sorting through it in my head."
    "All the way...{w=.2} which means...{w=.2}\nin other words...{w=.2} that's-"
    fn "「When you say all the way,{w=.2}\n\ \ you mean \"that\", right? 」"
    "Sex, pretty much?"
    ka "「Yeah,{w=.2} that's right. 」"
    fn "「Uh... ummm 」"
    "「After so long, we're finally up to this, 」{w=.2}\nI thought somewhere in my head."
    "However,{w=.2} now that we're here,\nI'm feeling really insecure."
    "But at the same time,\nI also wanted to connect with Kouya even more."
    "After hesitating a bit, I said:"
    fn "「Okay,{w=.2} it's fine.{p}\ \ If it's with you...{w=.2} I want to try it. 」"
    "As I looked straight at Kouya,{p}I spoke after making up my mind.{p}He might not be the most embarrassed one, now."
    "After I said so, Kouya hugged me."
    "Then he whispered thanks into my ear,{w=.2}\nand suddenly, our positions were flipped.{p}I found myself looking at the ceiling."
    ka "「Then...{w=.2} I'll keep going. Turn yourself around.{p}\ \ And relax, or...{w=.2}{nw}"
    show ka 106 night with dis
    extend " or it won't work. 」"
    fn "「R-{w=.2}right. 」"
    
    hide ka with dis
    
    "I changed my position as he said that,{w=.2}\nand my manhood was right in front of Kouya's face."
    "Having done that, Kouya focused on it.{p}He seemed to be just as hard as I was,\nand he set a rhythm going with his penis."
    "Just like our first time, we were in the 69 position.{p}But this time, I'm the one who was on top.{p}Kouya probably likes this position."
    "We each grabbed the other's cock, and began licking."
    
    play sound2 sex1 loop
    $ renpy.music.set_volume(0.6, 0.0, channel = "sound2")
    
    "I unintentionally drew back my hips as the strong,\ndirect pleasure shot straight through my body.{p}My voice came out spontaneously."
    fn "「Hah,{w=.2} ff... 」"
    ka "「Mn,{w=.2} gk,{w=.2} uu... 」"
    "Kouya seemed to feel the same,{w=.2}\nas I heard his voice mumbling from around my stomach."
    "Last time it was one-sided on my end,{w=.2}\nso this time I could think about making it equal,\nand it made me a bit happy."
    "I wanted to give Kouya more.{w=.2}\nMore of these feelings, more pleasure...\nI intensified my actions."
    "As I remembered those times,{w=.2}
    Kouya followed up on my lead as he too began
    to suck and lick more frantically."
    ka "「Ngh!{w=.2} Uwah- 」"
    "Below me, Kouya only shifted\nslightly at the development."
    "As if to get even, he began sucking harder."
    fn "「Hyah-! 」"
    "Kouya opened his mouth wide,\nand swallowed my entire length,\nusing his tongue to lick my scrotum."
    "He began massaging my sack mercilessly,{w=.2}\nmaking me raise my voice at the sudden pleasure."
    "A tingling sensation spread through my body,{w=.2}\nstarting from the tip of his tongue."
    fn "「Hagh,{w=.2} mn,{w=.2} ff-! 」"

    stop sound2 fadeout 7.5
    
    "To distract myself from the sensations, 
    I stuffed Kouya's cock into my mouth again."
    "Over at Kouya's end, he let go of my length,{w=.2}\nand used his tongue to ravage my sack."
    "My balls were juggled around so many times by it,{w=.2}\nKouya only pausing occasionally to suckle me."
    "However, after a few times he suddenly stopped,{w=.2}\nthen began to move lower."
    "Finally, the wet heat came into contact
    with my rear end."
    "As he pressed on, a shudder ran through me.{p}Until now, I'd felt nothing in that spot,\nbut suddenly that changed."
    "As Kouya lapped back there,{w=.2} his tongue glided\nover my hole so many times."
    fn "「Ha,{w=.2} aff,{w=.2} mn,{w=.2} haaah- 」"
    "Little by little, I got used to the feeling,\nand I started breathing hard through my mouth."
    "At this point, I forgot about licking Kouya's rod\nand just held his hot member in my lips."
    "Every time his tongue moved over my back gate,\nmy mind went blank bit by bit."
    ka "「Do you only feel the licking,{w=.2} [fn]? 」"
    "I gave a slight nod to the question."
    "Kouya probably couldn't see from his position,{w=.2}\nbut he seemed to pick it up from my motions."
    ka "「I see.{p}\ \ Then, we'll have to loosen you gradually,{w=.2}\n\ \ so relax and don't force yourself. 」"
    "After saying that, Kouya once again\npressed his tongue against my backside."
    "But this time it wasn't a lick,{w=.2}\nmore like he was pushing into me."
    "The tip of his tongue managed to wedge itself in,\nbut then moved around to try to pry me looser."
    fn "「Ahh,{w=.2} ah... 」"
    "He followed along my inner walls,\nthen steadily moved deeper."
    "Every time he got a bit further,\na small moan escaped my throat."
    "Before long, the tongue reached its limit.{w=.2}\nThen, something covered in short hair pressed in,\ngetting inserted in slowly."
    "I'm pretty sure it was Kouya's finger."
    fn "「Haah,{w=.2} guh...uh- 」"
    "When the finger scratched my insides\nas it twisted and turned,\nmy voice rose in discomfort."
    ka "「You okay?{w} It's almost over.{p}\ \ Just be patient a little bit longer. 」"
    "Kouya made to distract me a little bit,{w=.2}\nand he began lightly rubbing my penis\nafter it started softening a bit."
    "At the provocation, my relaxed body became tense.{p}Kouya didn't overlook that fact, as he now\nput in two fingers."
    fn "「Fuh,{w=.2} gck... 」"
    "Having more pushed inside me felt a bit tight,\nbut my body was starting to get accustomed to it,\nand I relaxed."
    "Soon it became three fingers,\nwhich went all the way in back there."
    "For a short while, those three fingers moved freely\ninside me,{w=.2} and my anal ring became completely\nloosened."
    ka "「If it's this loose, then you're probably ready... 」"
    "I wriggled a bit as he pulled out his fingers."
    "It was then that I noticed I had been\nholding his cock in my mouth."
    "Covered in my spit,{w=.2}\nit gleamed somewhat obscenely in the dim light."
    "Kouya set me down on his lap,\nand all the preparations were ready."
    ka "「Okay,{w=.2} it should be able to fit. 」"
    fn "「Ahh,{w=.2} umm...{w=.2} 」"
    ka "「Don't worry,{w=.2} I'll take it slow. 」"
    "As he said that, his penis began pressing into me.{p}Even though it was just the tip, it felt so hot."
    "To be honest, I wanted a bit more time\nto get mentally prepared, but I couldn't say so."
    ka "「Here we go. 」"
    fn "「Y-{w=.2}yeah... 」"
    "As unease about my first time flooded my chest,\nI managed to get out that short reply."
    "After he checked with me, Kouya began slowly\nsliding deeper into my body."
    fn "「Uu...agh- 」"
    "This was the first time I've taken anyone's manhood.{p}Its girth was way beyond the scale of a finger,{w=.2}\nand I cried out in slight pain."
    ka "「[fn],{w=.2} try to relax... 」"
    fn "「...Guh- 」"
    "Little by little he pushed in further."
    fn "「-ngh,{w=.2} ngaaah- 」"
    "I still couldn't quite keep up, and gasps\nleaked out of my mouth."
    "It hurt."
    "It wasn't only that though,\nas I also felt another sensation."
    "Ever since his fingers were in there, I've felt it."
    "I didn't understand what it was, but it felt like\nit was filling me up from inside."
    "While I was thinking about that feeling,\nKouya hilted his length inside me."
    ka "「...[fn], it's all in.{w} You okay? 」"
    "He held me close like he was leaning on my back,\nand then he whispered into my ear.{p}Somehow, I managed a nod."
    ka "「Sorry.{w=.2} Even though this is your first,\n\ \ I've been kind of rough.{p}\ \ It looks like you're enjoying it, though. 」"
    "Kouya's hand was touching near my navel,\nthen quickly slid down to my crotch."
    "And just as quickly he felt the head of my dick,\nwhile another strange sensation shot through me."
    "Earlier it had softened a bit,{w=.2}\nbut it had since stiffened back up,\nand was dripping precum."
    "Finally, the feeling I'd noticed earlier,{w=.2}\nwhich my brain hadn't quite deciphered,\ncame about again."
    ka "「Seriously,{w=.2} I'm almost over the edge,{w=.2}\n\ \ and I don't think I can last,{w=.2} but don't move. 」"
    fn "「Kou-{w} yah-! 」"
    "Kouya picked me up, then sat on the bed."
    "With the sudden change in seating,{w=.2}\nKouya's dick moved further into me,\nand I cried out."
    
    scene ev_kouya_2a with sdis
    play sound2 humping loop 
    
    "Kouya began thrusting his\nhips slowly as the bed creaked."
    "Bit by bit that rhythmic movement crept in,{w=.2}\nand I could do nothing but gasp."
    fn "「Hah,{w=.2} ahh,{w=.2} ngah,{w=.2} ah- 」"
    ka "「Kuh... 」"
    "This burning feeling seemed like it would scald me,\nand it kept churning inside my body."
    "It felt so hot that\nI thought I'd melt from within."
    "Every time Kouya's pointed head poked within me,\nan indescribable wave pleasure shot through me."
    ka "「Hah,{w=.2} hah,{w=.2} kuh,{w=.2}\n\ \ this,{w=.2} feels great,{w=.2} [fn]- 」"
    fn "「Haaah,{w=.2} kuah,{w=.2} Kouya- 」"
    "Our gasps filled the room,\nalong with the squeaks from the bed."
    "I could hear Kouya's panting near my shoulders.{p}The long breaths felt kind of dirty,\nand they stirred up my excitement even more."
    "Kouya's movements steadily\ngrew faster and more intense."
    "Every time he pressed into me,\nmy body felt like it was floating in the air,\nalmost like a thrown ball."
    "The intervals between them got shorter and shorter,{w=.2}\nand all the feelings I was experiencing\nstarted to blend together."
    "All I could do was grit my teeth\nat the overwhelming pleasure."
    "However, I was reaching my limit."
    "From the core of my body,\nmy desires were gushing out in a mess,{w=.2}\ncrawling around on the surface of my skin."
    fn "「Kou-{w=.2} ya,{w=.2} I-{w=.2}I'm...! 」"
    ka "「Hang in there,{w=.2} just a little longer.{p}\ \ I'm,{w=.2} almost-! 」"
    "He somehow kept going as his reply got fainter,\nand his hips moved even more rapidly."
    "The intensity was that of a real beast."
    "In response,{w=.2} the tingling in\nmy lower half reached a peak."
    "And then:"
    fn "「Ugh,{w=.2} haah,{w=.2} nnggaaaahhh-! 」"
    
    play sound3 heartbeat
    scene white with qdis
    scene ev_kouya_2b with qdis
    
    "I reached my peak and cried out."
    "My cock pulsed, spraying my seed all over the place."
    ka "「Kuh,{w=.2} I'm cumming too...{p}Ugh, gaaahhh-! 」"

    stop sound2
    play sound2 heartbeat
    scene white with qdis
    scene ev_kouya_2b with qdis
    
    "Kouya thrusted as deeply into me as he could,{w=.2}\nand as if drawn along with my release,\nreleased his load into me."
    fn "「Guh, uu-... 」"
    "As I felt his warmth spread through me,\nI leaned back and collapsed against Kouya's chest."

    scene black with sdis
    
    "A warm hand gently stroked\nmy head as if thanking me."
    "I closed my eyes, and basked\nin the warmth of the afterglow."
    
    if persistent.replay == True:
        scene black with dis
        pause .5
        $ renpy.end_replay()
        
    $ persistent.event_kouya2 = True    
    
    stop music fadeout 3
    stop sound fadeout 3
    
    jump end29
    
##########################################################
label juuichi29:
    
    $ event_name = _("Dreaming of the Two from that Day")
    
    scene forest01 night with sdis
    play music piano3_014
    
    "Pretty fireworks fill the night sky.{p}{nw}"
    play sound fireworks_explosion
    show fireworks
    extend "They open and die one after another, {w=.2}a fleeting life."
    "Even though they're beautiful, {w=.2}it's a somewhat sad\nscene.{w} I watch them as I lay on the ground on my\nback."
    "On the back of my neck, {w=.2}I feel a faint warmth.{p}Until a short while ago, {w=.2}I never knew how an arm\npillow could make me so happy."
    "I bend my left arm and bring it close to my ear.{p}My fingers become covered with fur."
    "I slowly look to my side.{p}Juuichi-san is watching over me."
    
    play sound fireworks_explosion
    show fireworks
    
    fn "「Juuichi-san, {w=.2}you're not watching the fireworks? 」"

    show ju 002 big night at center_big with dis
    
    ju "「The fireworks aren't what I want to look at right\n\ \ now. 」"
    "Upon hearing his sweet words,{w=.2}\nI look away in embarrassment."
    "Since when did he start saying things\nlike that?{w} ...But it feels like\nI could be swept away by it too."
    
    show ju 001 big night with dis
    
    "Juuichi-san puts his right hand on my chin.{p}Then, {w=.2}before I can even think about it, {w=.2}he\nturns my head so that it's facing him once again."
    
    show ju 009 big night with dis
    
    ju "「...You don't like this? 」"
    "...He's being a bit more forward today.{w} It might be\nnice to have days like this every once in a while\nthough."
    fn "「I... {w=.2}like it. 」"
    
    show ju 002 big night with dis
    
    ju "「I see. 」"
    "My words make him smile happily.{p}Then, {w=.2}he slowly slowly brings my face closer.{p}I quietly close my eyes."

    scene black with sdis
    stop music fadeout 10
    
    "...{p}...{p}...?"
    "No matter how much time passes,{w=.2}\nI never feel his lips."
    
    scene white with wipe_corner
    scene hbroom with sdis
    
    "I hazily open my eyes in confusion.{p}Instead of Juuichi-san, {w=.2}I see the fluorescent\nlight shade hanging from the celing."
    "...A dream?{p}I thightly grasp my right hand that should have been\nentwined with Juuichi-san's fingers."
    fn "「...{w=.2}I still have feelings for him. 」"
    "I weakly mutter to myself."
    
    $ event_name = _("At the Bottom of Discouragement and Despair")
    
    scene black with sdis
    scene hbroom with sdis
    pause 1.5
    play music sad01
    
    "A few days have passed since then.{p}I haven't seen Juuichi-san after my awkward goodbye.{p}...I can't see him."
    "Is it the same for him?{w} He hasn't come over to visit\nme either.{w} As much as I am relieved, {w=.2}it's also heart-\nwrenching.{w} This is such a complicated feeling..."
    "I've shut myself in the house and just been waiting\nfor time to pass.{w} Each day I end up doing nothing.{p}I don't think I care about anything now."
    "I shouldn't have confessed if things were going to\nend up like this.{w} I had gotten carried away,{w=.2}\nI shoudln't have done those things."
    "How many times have I thought those things since that\nday?{w} Too many to count, {w=.2}I think them all the time."
    "It doesn't matter though, {w=.2}it doesn't change what I\ndid.{w} I know I've got no choice but to accept that\nfact.{w} But..."
    fn "「Haah... 」"
    "A sigh escapes from my mouth."
    "If I'm not careful, {w=.2}memories of my time with Juuichi-\nsan start coming to me.{w} The welcoming party, {w=.2}the\nbeach, {w=.2}camping.{w} And then... {w=.2}the day of the festival."
    "I shake my head. If I keep going like this,{w=.2}\nI'll probably fall into a bog of despair again."
    "...I don't want to be in Minasato anymore.{w} If I stay\nhere I'll only remember all the fun times I had."
    "That's just painful for me now.{p}Painful and unbearable."
    "It's still a few days before I said I'd leave,{w=.2}\nbut my grandpa will understand if I say\nI still have homework left to do at home."
    "When I got the letter from Torahiko, {w=.2}I was so\nexcited about coming back here.{w} I never thought\nI'd be leaving in such a gloomy mood."
    "Should I... {w=.2}tell everybody?{p}If they see me off, {w=.2}there's a chance\nJuuichi-san will be there."
    "I have a feeling of guilt I can't be silent about any\nlonger.{w} But... {w=.2}I'm more scared of seeing Juuichi-san."
    "Being rejected by him, {w=.2}that's what I'm scared of."
    
    $ event_name = _("An Unexpected Visitor")
    
    play sound ChimeA
    
    "Ding dong."
    "The dry sound of the doorbell rings through the\nhouse.{w} ...Oh yeah,{w=.2} my grandparents are out at\nsome old folks gathering."
    
    play sound standup
    
    "I sluggishly stand up,{w=.2}\nand trudge to the front door."

    scene hentry with wipe_right
    
    fn "「Yeah, {w=.2}who is it? 」"
    "Even though I think I should act a little more\ncheerful just in case it's someobdy wanting to see my\ngrandparents, {w=.2}my tone still sounds dark and heavy."
    
    play sound tm2_slidedoor000
    
    "I open the front door.{p}{nw}"
    show ky 001 at center with dis
    "Slim eyes with spotted markings, {w=.2}and drooping ears.{p}The person at the door is Kyouji."
    
    show ky 002 with dis
    
    ky "「Oh my, {w=.2}he looks terrible too. 」"
    fn "「...Huh? 」"
    
    show ky 001 with dis
    
    ky "「Nothing. {w=.2}Don't worry about it.{p}\ \ Anyways, {w=.2}do you have a moment? 」"
    fn "「Well, {w=.2}I guess so. 」"
    ky "「Really?{w} Thank goodness.{p}\ \ There's something I'd like to talk to you about. 」"
    "I appreciate him coming over here just for me, {w=.2}but\nthere's no way I can talk to him when I'm feeling so\ndepressed.{w} I'll make up a reason to get him to leave."
    ky "「...May I? 」"
    "He pins me down with a sharp look.{p}I keep back the words I was going to say."
    "Although I rub my eyes and get another look at the\nperson standing in front of me, {w=.2}Kyouji is just all\nsmiles as usual."
    "...Hmm, {w=.2}was I imagining things?{p}The sense of intimidation I'm getting from him makes\nme take a half step back."
    
    show ky 002 with dis    
    
    ky "「What I want to talk to you about has nothing to do\n\ \ with me.{p}\ \ {nw}"
    stop music fadeout 2.5
    play music melodious08 fadein 2.5
    extend "...It's about Mikazuki. 」"
    "Huh? {w=.2}Why Juuichi-san?{w} My eyes go wide in surprise.{p}His name coming out of Kyouji's mouth at a time like\nthis?"
    "Maybe Juuichi-san told Kyouji...{p}No... He's too tight-lipped,{w=.2}\nI'm sure he wouldn't.{w} That's what I want to believe."
    "...But I've betrayed that trust too.{p}I tightly clench my dry lips."
    fn "「Ju-{w=.2}Juuichi-san? 」"
    "My voice is hoarse, {w=.2}despite me trying not to make it\nsound that way."
    
    show ky 001 with dis
    
    ky "「Yes.{p}\ \ For about a week now,{w=.2}\n\ \ Mikazuki has been acting a bit strange. 」"
    "A week.{p}Those words make me flinch back."
    fn "「... 」"
    
    show ky 002 with dis
    
    ky "「I tried to find out if something happened,\n\ \ but he won't say a word. 」"
    ky "「I'm wondering what's going on with him,{w=.2}\n\ \ so I decided to drop by and visit you for a bit. 」"
    fn "「...Why me? 」"
    
    show ky 001 with dis
    
    ky "「Why? Elementary, {w=.2}my dear Watson. 」"
    "He gives a forced wag of his finger."
    ky "「Mikazuki started acting strange after the festival.{p}\ \ You were with him at that time, {w=.2}according to the\n\ \ testimony I already got from Torahiko. 」"
    ky "「In other words, {w=.2}something happened between you and\n\ \ him on the day of the festival.{p}\ \ ...It's only natural to think so, {w=.2}right? 」"
    "Hearing his reasoning, {w=.2}I'm at a loss for words.{p}...But it seems that Kyouji hasn't been able to\nfigure out what happened."
    "I breathe a sigh of relief at that fact.{w} Then, {w=.2}Kyouji\nslowly narrows his eyes.{w} It's like he's seeing all\nthe way through me, {w=.2}making me shudder."
    ky "「It's rare for a guy who doesn't like showing\n\ \ weakness to others to act like that.{w} That means\n\ \ something happened to him to make him be that way. 」"
    ky "「...I'll go right out and ask.{p}\ \ [fn], {w=.2}did you tell Mikazuki you love him? 」"
    "How did you know?{w} I almost blurted that out but\nstopped myself at the last second.{p}Kyouji smiles wryly."
    ky "「...You're not very good at keeping secrets.{p}\ \ It's written all over your face. 」"
    "Sigh.{p}I knew it,{w=.2}\nit's nigh-impossible to lie to Kyouji."
    fn "「...How did you know? 」"
    
    show ky 002 with dis
    
    ky "「Hmm... How should I put it?{w} The look in your eyes\n\ \ when you see Mikazuki, {w=.2}it's the exact same look in\n\ \ Sou's eyes when he sees me, {w=.2}I guess? 」"
    "My eyes...?{p}Even if he says that,{w=.2}\nI have no idea what he means."
    "And why did he bring up Soutarou-kun?{p}He said we have the same look in our eyes though..."
    "When I question him about it,{w=.2}\nhe scratches at his nose in a bit of embarrassment."
    
    show ky 001 with dis
    
    ky "「I was waiting for a chance to say this in front of\n\ \ everybody, {w=.2}but now would be a good time.{p}\ \ Honestly, {w=.2}Sou and I... are dating. 」"
    fn "「Oh I see.{w} So now I'm supposed to say:\n\ \ Wow, the two of you are...{w} Wait, {w=.2}what!? 」"
    ky "「I see you just now figured out I'm not joking. 」"
    fn "「S-{w=.2}s-{w=.2}so that means you're, {w=.2}uh, {w=.2}boyfriends...? 」"
    
    show ky 002 with dis
    
    ky "「Yes, {w=.2}Sou confessed his love for me at the festival.{p}\ \ I love him too,{w=.2}\n\ \ so we decided to officially be boyfriends. 」"
    
    show ky 001 with dis
    
    ky "「Well, that happened so recently.{p}\ \ It's still embarrassing for me to say. 」"
    "While my love was unrequited,{w=.2}\ntheir love has bloomed.{w} The confessions happened on\nthe same day, {w=.2}but our results were different."
    "Kyouji shyly smiles, making me a bit...{w=.2}\njust a bit jealous.{p}I can't honestly be happy for them."
    
    show ky 002 with dis
    
    ky "「...Sorry.{w} That wasn't very considerate of me. 」"
    "He doesn't have anything to apologize for.{p}Things went well for them, {w=.2}and they didn't between\nJuuichi-san and I.{w} That's all. But..."
    "The difference between those two things is endlessly\ndistant."
    "In an effort to change the subject,{w=.2}\nKyouji loudly clears his throat."
    
    show ky 001 with dis
    
    ky "「It's going to be problematic between you two now\n\ \ too, {w=.2}I can't force you to tell me what happened. 」"
    ky "「...But talking to somebody helps sort out your\n\ \ feelings.{w} Even if it's just complaining, {w=.2}you should\n\ \ say something. 」"
    ky "「[fn]... {w=.2}are you going to keep this to yourself\n\ \ forever?{w} Don't do that.{w} When times are tough, {w=.2}you\n\ \ shouldn't force yourself to put up with it. 」"
    fn "「...I can't.{w} Even if you say you'll listen,{w=.2}\n\ \ telling me to like that won't make me want to talk,{w=.2}\n\ \ will it? 」"
    ky "「Ha ha.\n\ \ Seeing you like this has made me more eloquent. 」"
    "Kyouji smiling tempts me into smiling as well.{p}Jeez... {w=.2}I wonder why there's so many strong people\naround me."
    "I prepare myself,{w=.2}\nthen start telling him the events of the other day."
    
    $ event_name = _("Facing Each Other")
    
    stop music fadeout 5
    scene black with sdis
    scene hbroom
    show ky 002 at center
    with sdis
    play music free58
    
    ky "「I see, {w=.2}so that's what happened...{p}\ \ Your ability to act in unexpected situations\n\ \ hasn't changed at all. 」"
    "After telling Kyouji the whole story about the\nfestival, {w=.2}he sits down next to me with a strained\nsmile."
    fn "「...I think I made a fool of myself. 」"
    
    show ky 001 with dis
    
    ky "「Wouldn't I need to keep repeating myself if that\n\ \ was the case? You seem plenty remorseful. 」"
    "He pats me on the shoulder.{p}Then he suddenly puts his hand on top of my head,{w=.2}\nand begins to stroke it like he's comforting a child."
    "Feeling Kyouji's hand reminds me once again of\nJuuichi-san's."
    "I hazily think that even though he's doing the same\nthing, {w=.2}there's a difference between the two."
    "Juuichi-san moved his hand more awkwardly.{p}And his palms are a little bigger."
    ky "「I can fawn on you every once in a while, {w=.2}right?{p}\ \ ...Ah, {w=.2}but Sou will get mad at me if I get any\n\ \ closer with you. 」"
    fn "「...I understand.{w} I don't want Soutarou-kun to be\n\ \ mad at you either. 」"
    "I think we both feel fulfilled now.{p}It'd be thoughtless of me to want more.{p}That's why this should be a one-time thing."
    "Now that I think about it,{w=.2}\nthat depressed feeling I had earlier has disappeared."
    "...Once again I realize that there's no use in\nbrooding over my problems alone."
    "All he did was see me like this\nand listen to me talk,{w=.2}\nbut I feel way better now."
    fn "「Thank you, {w=.2}Kyouji. 」"
    "I can't help but thank him."
    ky "「I'll help anytime you need me. 」"
    fn "「Sure thing.{p}\ \ ...Come to think of it, {w=.2}earlier I said Juuichi-san\ni\ \ s worried, {w=.2}but that's my fault, {w=.2}isn't it? 」"
    
    show ky 002 with dis
    
    ky "「Hmmm.{w} I'm sure you were the one that probably\n\ \ triggered it. 」"
    fn "「Huh?{w} What do you mean? 」"
    "He says something strange,{w=.2}\nmaking me tilt my head in confusion."
    
    show ky 001 with dis
    
    ky "「Did Mikazuki tell you that falling in love with the\n\ \ same sex is like an illness? 」"
    fn "「...Yeah.{p}\ \ But he said that was advice he got from you. 」"
    "Kyouji scratches at one of his drooping\nears as if something is troubling him."
    
    show ky 002 with dis
    
    ky "「Practically speaking, {w=.2}there seems to be decent\n\ \ percentage of people our age temporarily falling in\n\ \ love with the same sex. 」"
    ky "「Was it his sexuality?{w} Or did it have to do with his\n\ \ environment and sexual characteristics?{w} I think I\n\ \ needed time to say for sure. 」"
    ky "「At that time I should have told him that he needed\n\ \ to face himself. 」"
    ky "「...Maybe \"illness\" was too strong of a word?{p}\ \ Him sorting out his feelings seemed to be only\n\ \ temporary. 」"
    "Kyouji mutters \"This was my fault\"\napologetically in a low tone."
    ky "「He should have resolved his feelings by your sudden\n\ \ prodding, {w=.2}so I'm at a loss as to what to do. 」"
    fn "「That's what is troubling you? 」"
    
    show ky 001 with dis
    
    ky "「That's correct. 」"
    "As Kyouji stops talking for a moment,{w=.2}\nI still have my eyes fixed on him."
    ky "「[fn], {w=.2}do you still... like Mikazuki? 」"
    fn "「...Of course I do.{w} I can't simply let go of my\n\ \ feelings for him just because I was rejected. 」"
    
    show ky 002 with dis
    
    ky "「I see... 」"
    "He contemplates something while rubbing his muzzle.\nWhat kind of plan could he have at this point?"
    ky "「[fn].{w} Did you know there's a tournament in\n\ \ Kazenari today? 」"
    fn "「Yeah{w} ...Up until the festival,{w=.2}\n\ \ I was going to go and cheer for Juuichi-san. 」"
    
    show ky 001 with dis
    
    ky "「It's not too late.{w} You should go. 」"
    fn "「...I don't know.{p}\ \ I'd just be a bother if I went, {w=.2}wouldn't I...? 」"
    "I just don't want to get in his way.{p}If I become any more of a burden,{w=.2}\nit'll be more than just a match for him."
    
    show ky 002 with dis
    
    ky "「...Are you just saying that so you can continue to\n\ \ avoid him? 」"
    fn "「... 」"
    "I can't answer back.{p}Kyouji has pointed out exactly\nwhat I was trying to do."
    "I covered up my feelings of not wanting to see him\nby pretending to be condsiderate."
    
    show ky 001 with dis
    
    ky "「I understand you think it's difficult. 」"
    ky "「But if you go home with the way things are now,{w=.2}\n\ \ you'll be burning the bridge between the both of\n\ \ you. 」"
    ky "「What you need to do now is take a step forward\n\ \ before you hesitate again. 」"
    ky "「Remember the courage you had when you confessed.{p}\ \ You can do it... right? 」"
    "I repeat in my head what Kyouji told me."
    "I see what he means, {w=.2}but I'm still not sure.{p}Would I really be able to do that?"
    "...No, {w=.2}I need to stop that.{w} Kyouji said it too.{p}I can do it."
    fn "「...{p}\ \ I'm going to see Juuichi-san.{w} I still...\n\ \ don't like being away from him like this. 」"
    "My words satisfy Kyouji,{w=.2}\nand he nods with a smile."
    
    if meet_ten == True:
        jump juuichi29_kodori
    else:
        jump juuichi29_wolf

    ###########################################################        
    label juuichi29_kodori:
            
        $ event_name = _("The Search for the Crescent")
        
        stop music fadeout 5
        scene black with vsdis
        scene arena_entrance with vsdis
        play music daily03
        
        "It's about a twenty minute walk after getting off the\nbus.{w} In front of the large building, {w=.2}I see people\ndressed in Judo gi here and there."
        "The atmosphere is tense."
        "This is the Kazenari martial arts hall,{w=.2}\nand Juuichi-san is somewhere inside."
        "Even if he is inside, {w=.2}it's so large.{p}I'm not even sure I'm allowed to just walk right in."
        "It'd be best if I could find him directly, {w=.2}but I'm\nnot familiar with this place and there's nobody\nfamiliar around."
        "This looks to be a difficult task."
        "Just as I'm thinking that, {w=.2}I gasp with surprise.{p}No, {w=.2}it's not Juuichi-san... {w=.2}but it is somebody who's\nlimitlessly close to him."
        
        show tn 002 at center with dis
        
        fn "「Ten-san! 」"
        "I yell the name of the wolf who is sitting in the\nshadow of a bronze statue, {w=.2}meditating."
        
        show tn 001 with dis
        
        "His pointed ears twitch,{w=.2}\nand I enter his field of vision as he opens his eyes."
        tn "「Mikazuki just barely made it below regulation\n\ \ weight.{w} I don't know if you had anything to do with\n\ \ it, {w=.2}but I suppose I should thank you... 」"
        fn "「Ten-san, {w=.2}where is Juuichi-san?! 」"
        "I interrupt him,{w=.2}\nand ask about Juuichi-san's location."
        "Ten-san gives me a look of suspension and frowns.{p}I don't have time to worry about that right now\nthough."
        "That's because there is something I must do."
        tn "「...Well, {w=.2}I can't tell you.{p}\ \ But if you came here to support him,{w=.2}\n\ \ you're going to be disappointed with the results. 」"
        fn "「Huh? {w=.2}What's that supposed to mean? 」"
        tn "「I mean exactly what I said.{w} Perhaps because of his\n\ \ strict diet, {w=.2}or maybe because something else is\n\ \ bothering him, {w=.2}he can't get his spirits back. 」"
        "He lets out a small sight.{p}I can clearly see a look of disappointment on his\nface."
        fn "「...That might be my fault. 」"
        "I ready myself.{w} Timidly, {w=.2}I tell Ten-san about the\nother day.{w} I still leave out the part about my\nconfession falling flat though."
        
        show tn 002 with dis
        
        tn "「...{p}\ \ I never though Mikazuki would be the kind of man\n\ \ to let such petty bickering get to him. 」"
        
        show tn 001 with dis
        
        "He stares at me fixedly.{p}So much so that it's like he's trying\nto find something I've hidden in my words."
        "If I look away, {w=.2}this wolf won't talk\nto me about Juuichi-san.{w} I won't do it,{w=.2}\nI can't afford to lose any clues about him."
        "There are no words between us,{w=.2}\njust the occasional enthusiastic voice from the\ncrowd."
        tn "「...I can't let the person who made him this way be\n\ \ near him, {w=.2}that would be outregous.{w} It might even\n\ \ make him feel worse. 」"
        tn "「Do you still want to see Mikazuki?{p}\ \ What is it that's driving you? 」"
        fn "「Juuichi-san is important to me.\n\ \ I want to talk to him, I want him to smile.\n\ \ That's why I won't leave. 」"
        
        show tn 003 with dis
        
        tn "「What you're saying makes no sense. 」"
        fn "「...You're right. 」"
        "It's really frustrating to not be able\nto explain how you feel on the inside."
        "I might have been better off telling him the full\nstory, {w=.2}then even Ten-san would understand."
        "I stop trying to convince him with words,{w=.2}\nand stare into Ten-san's yellow eyes with just the\nutmost feeling of wanting to see Juuichi-san."
        "Juuichi-san.{p}I want to see Juuichi-san."
        
        show tn 001 with dis
        
        tn "「...Hmph, {w=.2}I can trust those eyes much\n\ \ more than your words. 」"
        "As he says that, the sense of intimidation concealing\nhim suddenly relaxes."
        tn "「Even now a match with Mikazuki would end with a\n\ \ victory for me. 」"
        
        show tn 002 with dis
        
        tn "「...It was his fault for not being in peak condition\n\ \ for the tournament to begin with. 」"
        tn "「In other words, what happened to him to make him be\n\ \ like this now is none of my concern. 」"
        "Ten-san gets out of his meditation position,{w=.2}\nand stands up straight.{w} Then, {w=.2}he turns his back to\nme."
        
        show tn 005 with dis
        
        tn "「...What are standing there for?{p}\ \ Quickly, {w=.2}come with me. 」"
        fn "「...Y-{w=.2}yes sir! 」"
        "I don't know how I suddenly got though to Ten-san.\nBut I still mutter words of gratitude to him in my\nhead."
    
        hide tn with wipe_right
        
        "I chase after him at a quick pace so as not to lose\nsight of his long, {w=.2}swaying tail."
        "We go down a corridor, {w=.2}up some stairs, {w=.2}and then down\nanother corridor."
        "Then Ten-san stops for a moment in front of a set of\ndouble doors, {w=.2}and turns towards me."
        
        show tn 001 at center with dis
        
        tn "「Beyond this door is the waiting area for Kazenari\n\ \ High.{w} I'll look around downstairs.{p}\ \ Wait in here so you don't get lost. 」"
        fn "「I'm sorry for being such a bother to you.{p}\ \ Thank you for doing this. 」"
        "Ten-san barely knows me, {w=.2}he doesn't have to do this.{p}And yet he's going this far for me.{p}I bow my head towards him."
        
        show tn 006 with dis
        
        tn "「...Hmph.{p}\ \ If you're going to thank me,{w=.2}\n\ \ give Mikazuki a little encouragement too. 」"
        fn "「H-hmm, {w=.2}I can't guarantee that much though...{p}\ \ That wasn't originally the reason I came here\nanyways. 」"
        
        show tn 003 with dis
        
        tn "「But you came here to support him.{p}\ \ Or something else?{w} Did you come here to bother him? 」"
        fn "「No, {w=.2}that's absurd!{p}\ \ I'm supporting him, {w=.2}that's why I came here! 」"
        "He stares me down like a snake would a frog.{p}Or would a wolf and a rabbit be be a better fit for\nthis situation?"
        
        show tn 001 with dis
        
        tn "「...If you say so, {w=.2}good. 」"
        "Like a sword being drawn, {w=.2}Ten-san's thrist for blood\nrises, {w=.2}but is satisfied and returns it to its sheath."
        "He really can just wield that as he pleases.{p}I take a small breath to calm my pounding heart."
        "Did he not notice?\n-He probably did but I don't dare press any further-{p}He goes downstairs once again."
        
        hide tn  with wipe_right
        
        "Then, {w=.2}he suddenly stops as he's going down.{p}Without looking towards me,{w=.2}\nTen-san speaks to himself."
        tn "「...Please take care of Mikazuki. 」"
        fn "「Ten-san... 」"
        "This time Ten-san's back fades away into the first\nfloor.{w} He must be worried about Juuichi-san too\nfor him to say something like that."
        "Even though he sees me as nothing more than a bad\ninfuence.{w} Ten-san is taking it upon himself to let me\nin."
        "In an awkward way.{p}Can I really live up to his expectations?"
        "...No, {w=.2}I shouldn't think about that right now."
        "I take a deep breath so as not to get impatient\nduring a serious matter.{w} So as not to repeat my\nmistake."
        "I push open the door in front of me.{p}In an instant, {w=.2}I can hear all sorts of sounds."
        
        scene arena with explosion
        play sound cheering2
        
        "Thundering roars, {w=.2}someone being slammed into the mat,{w=.2}\nexcited cheers, {w=.2}and the calls of referees.{p}From here and there, {w=.2}they all come to me at once."
    
        stop sound fadeout 10
        
        "I feel somewhat detached,{w=.2}\nlike something is bubbling up from the bottom of my\nbody."
        "I've never been on a sports team,{w=.2}\nso I can really feel the participants' enthusiasm."
        "Is the second floor for the audience?{p}Being familiar with only small school gyms,{w=.2}\nI look around in amazement."
        "A square within a square.{p}That's how I would describe the structure."
        "There are mats laid on the first floor,{w=.2}\nThe matches are carried out in 4 different squares,{w=.2}\nperfectly forming the \"田\" kanji."
        "Each school has seating on the east, {w=.2}west, {w=.2}south,{w=.2}\nand north sides.{w} On each side and in front of me,{w=.2}\nthere are flags for each school hanging down."
        "I walk to the front of the audience seating,{w=.2}\nand lean over the railing as I look down below."
        "\"Katsumi\" is written in large, powerful letters,{w=.2}\nwith Kazenari High Judo Team beneath it."
        "I look at the seats behind me.{p}Although everybody is wearing Judo gi,{w=.2}\nunfortunately there's no sign of Juuichi-san."
        "Oh well, {w=.2}I guess I'll have to wait for Ten-san to get\nback.{w} As I sit on one of the chairs,{w=.2}\nI hear a familiar high-pitched voice call out to me."
        
        $ event_name = _("As Told by the Swining Tail")
        
        show su 002 at center with dis
        
        su "「Oh, {w=.2}[fn]-san! 」"
        fn "「...Shun-kun?{w} What are you doing here? 」"
        "Looking completely out of place in a Judo hall,\nShun-kun turns towards me with an endlessly bright\nsmile."
        su "「I'm cheering for Juuichi-san.{p}\ \ nw}"
        show su 004 with dis
        extend "That's what you're here for too, {w=.2}right? 」"
        fn "「...Y-{w=.2}yeah, {w=.2}I guess. 」"
        "Although my inarticulate reply confuses him,{w=.2}\nhe returns to his smiling expression."
        
        show su 001 with dis
        
        su "「Thank goodness. {w=.2}I was getting a little lonely.{p}\ \ {nw}"
        show su tailwag 01 with dis
        extend "But I feel better now that you're here! 」"
        "Well, {w=.2}there certainly are a lot of big people around\nhere, {w=.2}maybe he was feeling lost with his particularly\npetite stature."
        "I catch sight of his tail sweeping back and forth."
        
        show su 004 with dis
        
        su "「I was with Juuichi-san earlier,{w=.2}\n\ \ but he had to go downstairs for a match... 」"
        "Apparently we just missed each other."
        
        hide su with wipe_right
        show tn 001 at midright
        show su 004 at midleft
        with wipe_right
        
        tn "「It seems Mikazuki is in a match now. 」"
        "Whether it be good or bad timing, {w=.2}Ten-san returns\nto inform me.{w} Hmm, {w=.2}I wanted to speak to Juuichi-san\nas early as possible though."
        "Then, {w=.2}Ten-san suddlenly bends down on one knee and\nbows his head.{w} Seeing him do something so unexpected\nmakes my eyes go wide with shock."
        
        show tn 002 with dis    
        
        tn "「Shun-sama, {w=.2}I have told you many times that you must\n\ \ not come to places like this. 」"
        "He says with his head still lowered.{p}Unlike me, {w=.2}Shun-kun isn't surprised.{p}The two of them know each other?"
        
        show su 005 with dis
        
        su "「I told you,{w=.2}\n\ \ please don't use \"sama\" when we're out. 」"
        "Shun-kun puffs his cheeks out.{p}With a posture straight out of a period drama,{w=.2}\nTen-san gives a short reply."
        tn "「I cannot consent to that. 」"
        "...{p}...{p}..."
        
        stop music
        play music free44
        show arena at vshake
        play sound bom35
        
        $ event_name = _("Shun, SAMA!")
        
        fn "「SHUN-SAMAAAAAA?! 」"
        "What the heck happened that made\nsomebody with that scary of a face\nstart using that honorific with Shun-kun?"
        fn "「Sh-Sh-Sh-Shun-kun, {w=.2}you know Ten-san?!{p}\ \ Why does he call you \"Shun-sama\"?! 」"
        
        play sound freeze07
        show tn 003 with dis
        
        tn "「...Shun-sama, {w=.2}may I kill this rude person? 」"
        fn "「Whaa?! 」"
        
        show su 016 with dis
        
        su "「Wawawa, no way! 」"
        tn "「Then how about an injury that will take half a year\n\ \ to heal... 」"
    
        show su 005 with dis
        
        su "「Don't injure [fn]-san,{w=.2}\n\ \ don't even hurt him! 」"
        
        show tn 002 with dis
        
        tn "「...As you wish.{p}\ \ {nw}"
        show tn 003 with dis
        extend "Hmph, you should be thankful for Shun-sama's\n\ \ compassion. 」"
        "Shun-kun saved me from an execution that I didn't\nknow was happening.{p}...The reason itself isn't even clear to me."
        "I look away from the scary person next to me...{w=.2}\ner rather, {w=.2}Ten-san, {w=.2}and timidly ask Shun-sama a\nquestion."
        fn "「Shun-sama,\n\ \ how do you and Ten-san know each other? 」"
        
        show su at jump_up
        pause .175
        show su at jump_up
        
        su "「Please don't call me \"sama\". 」"
        "...But the person next to me is\nglaring at me with a look that says,{w=.2}\n\"call him sama\"."
        
        show su 001 with dis
        
        su "「Umm, {w=.2}Ten-san and I are relatives. 」"
    
        show arena at vshake
        play sound bom35
        
        fn "「WHAAAAAAAAAAAAT?! 」"
        "I accidentally shout upon hearing something I never\nimagined I would."
        
        $ event_name = _("Japan's Summer, The Kodori Family's Summer")
        
        $ encounter_ten = True#!#
        
        "According to Shun-sama's explanation, {w=.2}his family is\nthe head family and Ten-san's family is a branch\nfamily or something like that."
        "I know he has a big family, {w=.2}but I never though it'd\nbe this big..."
        "Shun-sa-... er, {w=.2}Shun-kun is so small and cute,{w=.2}\nhow could he be blood related to the huge and rugged\nTen-san?"
        "I can't believe they share some of the same DNA."
        "The shape of their tails, {w=.2}the color of their fur...{p}I don't think I'd have any objections to calling them\ncompletely different species."
        
        show tn 001 with dis
        
        tn "「My family has been active in incorporating outside\n\ \ blood. 」"
        tn "「I may look very different from the head family...{w=.2}\n\ \ but Kodori blood definitely flows through my veins. 」"
        "Noticing my staring, Ten-san answers."
        
        stop music fadeout 5
        
        "I see, {w=.2}so for Ten-san it's a given name?"
        "I thought it sounded strange for it to be his last\nname, {w=.2}but I thought it was when Juuichi-san called\nhim that..."
    
        show su at jump_up
        
        su "「Oh, {w=.2}[fn]-san, {w=.2}Ten-san.\n\ \ There's Juuichi-san! 」"
        
        $ event_name = _("Is there Hope?")
        
        play music free0456 fadein 4
        
        "I look towards the corner of the hall.{p}Dressed in a pure white Judo gi,{w=.2}\nJuuichi-san walks up to the a mat."
        "His opponent is a dog.\nPrompted by the referee, {w=.2}they bow to each other."
        "Compared to Juuichi-san, {w=.2}the other guy seems small\nand compact to me.{w} He looks shorter and lighter."
        "I shouldn't be judging by appearances,{w=.2}\nbut it doesn't seem to me that he has any chance of\nlosing."
        fn "「Do you think Juuichi-san can win when he's like\n\ \ that? 」"
        "Ten-san replies, {w=.2}continuing to stare at the scene\nbelow us instead of looking at me."
        
        show tn 002 with dis
        
        tn "「...He needs to get the strength he had before\n\ \ back. 」"
        "Shun-kun raises his voice in agreement."
        
        show su 004 with dis
        
        su "「You're right.{p}\ \ Juuichi-san doesn't look like he's feeling well\n\ \ today. 」"
        "...Ugh.{p}Things seem to be more serious than I guessed."
        "At the referee's signal, {w=.2}Juuichi-san and the dog\nboth raise their arms.{w} The dog makes the first move.{p}He springs toward Juuichi-san's chest."
        
        show tn 001 with dis
        
        tn "「He got him by the cuffs so easily. 」"
        "Making use of his light footwork, {w=.2}the dog moves in\nfor a standing throw.{w} Did he not see a chance for a\ncounterattack?"
        "It's clear even for me that he's just playing\ndefensively."
        "Seeing the progress of the match,{w=.2}\nTen-san lets out a huge sigh."
        
        show tn 002 with dis
        
        tn "「...In Judo, you must overcome yourself before you\n\ \ can be victorious. 」"
        "The referee yells \"Stop!\", {w=.2}and both of them return to\ntheir places.{w} They straighten out their gi and face\neach other again."
        "Then, {w=.2}the referee declares a \"Foul!\" towards Juuichi-\nsan."
        
        show su 016 with dis
        
        su "「Uh oh, {w=.2}he got fouled... 」"
        fn "「A foul?{w} That means he loses a point, {w=.2}right? 」"
        
        show su 004 with dis
        
        su "「Yes.{w} You shouldn't get them because they become a\n\ \ disadvantage when it's time for the judges... 」"
        
        show tn 001 with dis
        
        tn "「He has been in many dangerous situations before.{p}\ \ ...Perhaps Mikazuki won't fall here. 」"
        fn "「What?! 」"
        "He waves his hand at me, {w=.2}telling me to be quiet."
        tn "「I told you earlier, if he can get his strength\n\ \ back, {w=.2}there's no way he'll lose.{p}\ \ ...You realize that too, {w=.2}right? 」"
        fn "「...Umm, {w=.2}so he's not going to attack at all? 」"
        tn "「Correct.{w} {nw}"
        show tn 003 with dis
        extend "That is like becoming Judo itself. 」"
        
        show su 016 with dis
        
        su "「You can't lose here!{p}\ \ You can do it, {w=.2}Juuichi-san! 」"
        "Shun-kun shouts as much as his tiny body can.{w} I don't\nhear any other sound.{w} It looks like Juuichi-san is\nfinally ready to handle his oppontent."
        "Then, {w=.2}the dog spins in place, {w=.2}hooking his right foot.{p}Without time to think, {w=.2}Juuichi-san's large body\ndances in the air."
        
        play sound bosu35
        
        "Boom, {w=.2}the heavy impact echoes throughout the hall."
        
        show tn 001 with dis
        
        tn "「...He was saved by his opponent's inexperience. 」"
        "A win didn't come out of this one.{p}The referee swings his right arm out parallel to the\nmat, {w=.2}and declares \"Half-point!\"."
        "Although the dog hurries into a hold,{w=.2}\nJuuichi-san stiffens his solid body,{w=.2}\nmaking it impossible for the dog to turn him over."
        "Therefore, {w=.2}the referee issues a restraint signal."
        tn "「Now Mikazuki has all but cut off any way of\n\ \ retreating.{w} Hm... {w=.2}has he resigned himself to losing,{w=.2}\n\ \ or is he just trying to scare the hell out of me? 」"
        "I stare at Juuichi-san downstairs.{w} He shouldn't be\nshaken by anything.{w} On that face that should usually\nbe a moody frown, {w=.2}is clearly a look of impatience."
        "It's no use.{w} As it is now,{w=.2}\nJuuichi-san is going to lose."
        "--Nothing is going to change if I just stand here.{p}Why am I here right now?"
        "Many things are spinning around in my head,{w=.2}\nbut drive out all the unnecessary thoughts."
        "I take a deep breath.{p}Then, {w=.2}I yell with all the strength I can muster."
        
        $ renpy.music.set_volume(0.3, 1.0, channel = "music")
        
        fn "{size=+25}「JUUICHI-SAN!! 」"
        fn "{size=+25}「YOU CAN DO IT!! 」"
        
        $ event_name = _("And Then, There was Hope")

        $ renpy.music.set_volume(0.75, 10.0, channel = "music")
        
        "His face turns towards me.{p}As if he had seen something unbelievable,{w=.2}\nhis eyes open wide in surprise."
        "I'm sorry it took me so long to get here...{w=.2}\nKyouji scolded me a lot too.{p}But even so, {w=.2}I'm finally here."
        "That's why... {w=.2}my way of talking is a little strange.{p}Juuichi-san, {w=.2}please win this match!"
        "The match restarts with the referee's call."
        "Juuichi-san suddenly changes from the way he was\nearlier, {w=.2}and displays a burning fighting spirit by\ngrabbing his opponent."
        
        show tn 004 with dis
        
        tn "「...Hmph, {w=.2}he had me worrying. 」"
    
        show su 002 at jump_up
        
        su "「Wow, {w=.2}he's acting totally different now! 」"
        "Shun-kun hops up and down in excitement."
        
        show tn 002 with dis
        
        tn "「Now his chances of losing are slim. 」"
        "In contrast to Shun-kun, {w=.2}Ten-san calmly comments."
        "When the match resumes and they grapple each other,{w=.2}\nJuuichi-san quickly takes the offensive."
        "He takes a step forward with his left foot,{w=.2}\nand grabs his opponent's arm cuffs,{w=.2}\nmaking him lose his balance."
        "Then, {w=.2}without giving the dog a chance to think,{w=.2}\nJuuichi-san sweeps his right leg."
        
        play sound hit_p09
        
        "SLAM! The sound of the dog striking the mat reaches\nmy ears.{w} {nw}"
        play sound cheering2
        extend "At the same time, {w=.2}the referee raises his\nright arm up, {w=.2}declaring Juuichi-san's victory."
        
        play music free04 fadein 2.5
    
        show su at jump_up
        
        su "「Juuichi-san won! 」"
        fn "「Yes! 」"
        
        stop sound fadeout 10
        
        "Shun-kun and I both jump around in excitement.{p}Until now, {w=.2}I've never seen such a magnificent good-\nbye reversal grand slam."
        
        show tn 005 with dis
        
        tn "「That was a decent sweeping leg throw just now.{p}\ \ Considering how he's been up until now,{w=.2}\n\ \ I'm pleased he didn't let go. 」"
        "...Was that his way of sayinig he's really\nhappy Juuichi-san won?{w} His tail is wagging the\nsame way Shun-kun's is next to me."
        "He's not a very honest person.{p}I can't help but laugh at the\ngap between his words and his actions."
        "I've gotten to see a common point betweent these two.{p}They look completely different, {w=.2}but Ten-san\nis a still a member of the Kodori family."
        "The opponent's shoulders droop.{p}\nJuuichi-san offers his hand to help him up.{p}Something like this just screams \"Sportsmanship!\"."
        "They bow to each other, {w=.2}step off the red mats\ndividing the match spaces, {w=.2}then bow again."
        
        show tn 001 with dis
        
        tn "「I wonder if this means Mikazuki will put up a good\n\ \ fight.{w} {nw}"
        show tn 003 with dis
        extend " ...This should be interesting. 」"
        fn "「Huh? {w=.2}What are you talking about? 」"
        
        show tn 001 with dis
        
        tn "「I'm saying I am Mikazuki's next opponent. 」"
        fn "「Whaaat?! 」"
        "Even though they go to the same school,\nthey have to fight..."
        tn "「Now what?{p}\ \ This is an individual competition, {w=.2}it has nothing to\n\ \ do with were you come from. 」"
        fn "「Y-{w=.2}yeah, {w=.2}but... 」"
        "Trying to hold on to me,{w=.2}\nan extremely sad look appears on Shun-kun's face."
        
        show su 004 with dis
        
        su "「It's only determined by a lottery...{p}\ \ but I wanted to see the finals. 」"
        
        show tn 002 with dis
        
        tn "「...This may be the best stage for this though.{p}\ \ If he was defeated by someone else and not able to\n\ \ face me, {w=.2}I'd instantly give up the match. 」"
        "I want both of them to win, {w=.2}but that's not possible.{p}It's either going to be him or Juuichi-san."
        
        show tn 001 with dis
        
        tn "「You should go with your original goal,{w=.2}\n\ \ to support Mikazuki. 」"
        tn "「If you're thinking about how long Mikazuki and I\n\ \ have known each other, {w=.2}don't trouble yourself over\n\ \ it. 」"
        "Did Ten-san read my expression?{p}He said that so simply."
        "That's what I should do, {w=.2}but...{p}I still feel kind of sad about it."
        tn "「Besides, {w=.2}I have Shun-sama.{p}\ \ Compared to you, {w=.2}he's ten times as...{p}\ \ No, {w=.2}there is no comparison. 」"
        
        show su 005 with dis
        
        su "「Ten-san,{w=.2}\n\ \ please don't tease [fn]-san too much. 」"
        "He protected me once again.{p}It feels like Shun-kun is my only ally here."
        
        show tn 002 with dis
        
        tn "「As you wish.{p}\ \ {nw}"
        show tn 005 with dis
        extend "My body has gotten cold,{w=.2}\n\ \ I'm going downstairs to warm up for a short while. 」"
        
        show su 002 with dis
        
        su "「Okay, {w=.2}see you later. 」"
        fn "「Oh, {w=.2}I'll go with you... 」"
        "As I try to apologize and bow my head,{w=.2}\nTen-san halts me with his hand."
        
        show tn 002 with dis
        
        tn "「As I said earlier, {w=.2}there's no need for apologies.{p}\ \ I did everything by my own volition, {w=.2}don't worry\n\ \ about it. 」"
        fn "「O-okay.{p}\ \ ...Um, please do your best! 」"
        
        show tn 004 with qdis
        
        "The wolf stares at me in wonder.{w} Before long, {w=.2}his\nmouth starts to quiver.{w} Then, {w=.2}he starts to laugh."
        "I don't think this is the right time for him to be\ndoing that..."
        "Did I say something weird?{p}Although I look over at Shun-kun,{w=.2}{nw}"
        show su 004 with dis
        extend "\nhe looks just as confused as me."
        
        show tn 001 with dis
        
        tn "「...If I do my best, {w=.2}does that mean you're okay with\n\ \ Mikazuki losing? 」"
        fn "「Ah!! 」"
        "Indeed.{p}I promptly open my mouth to speak,{w=.2}\nbut he has a point."
        tn "「You really are a funny guy.{p}\ \ ...From the beginning I wasn't worried about losing,{w=.2}\n\ \ but now I must win no matter what. 」"
        fn "「That's the problem! 」"
        
        show tn 003 with dis
        
        tn "「I don't care.{p}\ \ Now that I have your support, {w=.2}losing isn't an option.{p}\ \ To protect my pride as a Kodori, {w=.2}and as a wolf. 」"
        "He bares his canines, {w=.2}displaying a wild smile.{p}Ah, {w=.2}it looks like he's completely fired up."
        "I'm sorry Juuichi-san.{p}I've stirred up your rival."
        
        show tn 005 with dis
        
        tn "「Mikazuki should be coming up here soon.{p}\ \ Watching amateur matches between strangers is boring,{w=.2}\n\ \ but you're just going to have to wait. 」"
        
        play sound step01
        hide tn with wipe_right
        
        "Ten-san departs, leaving me with a strangely\nvillainous line.\nThen, he suddenly turns towards us."
        tn "「I apologize for bothering you Shun-sama,{w=.2}\n\ \ but may I ask you to assist me in some stretching\n\ \ exercises? 」"
        "He suggests towards Shun-kun.{p}Probably so he can do things like push his back in."
        "For him to cross his arms and straighten his back...{w=.2}\nis impossible with his build."
        su "「Huh?{w} Oh, {w=.2}sure, {w=.2}that's okay... 」"
        "Shun-kun quickly looks towards me.{p}He can't bring himself to leave me all by myself."
        "Until I saw us,\nI said that things were a little uncomfortable."
        "Seeing him looking worried, {w=.2}I nod once towards him.{p}Ten-san gently puts his hand on Shun-kun's shoulder,{w=.2}\nand he trudgingly walks towards the stairs."
    
        hide su with qdis
        
        "Ten-san casts his yellow eyes towards me again.{p}He says nothing, {w=.2}nods once,{w=.2}\nthen follows suit with Shun-kun and disappears."
        "...Oh, I see.{p}He's doing this for me.{p}This way it'll just be Juuichi-san and I."
        "I guess that's what he was signaling at earlier."
        "Ten-san has gone out of his way to make this chance\nfor me.{w} That's definitely not something you can just\ndo spur of the moment."
        "I take a few deep breaths,{w=.2}\nand patiently wait for Juuichi-san to return."
        "Warm air from the floor below comes in contact with\nmy skin.{w} For no reason in particular, {w=.2}I look over in\nthat direction."
        "At the four different parts, {w=.2}four matches are\nunfolding.{w} Some of them are settled quickly, {w=.2}while\nothers aren't as easily until a decision is made."
        "I thought Judo would be a little more flashy,{w=.2}\nbut now that I'm watching it,{w=.2}\nit's actually quite the opposite."
        "I thought you won by throwing your opponent,{w=.2}\nbut that surprisingly doesn't happen that much."
        "You either hold them down for thirty seconds or get\ntwo half points."
        "The classes at school were relatively one-sided,{w=.2}\nbut that must be unique to amateurs or something."
        "When two people who train every day clash,{w=.2}\nit's completely different."
        
        $ event_name = _("Reunion for the First Time in a Week")
        
        stop music fadeout 1.5
        
        ju "「...[ln]. 」"
        "Hearing my name suddenly called from behind makes my\nbody freeze.{w} I push out all the air in my lungs so he\nwon't notice, {w=.2}and slowly turn around."
        
        show ju 318 at center with wipe_right
        
        fn "「Juuichi-san. 」"
        "...Was I able to say that as naturally as I usually\ndo?{w} I try to smile, {w=.2}but it feels a little awkward."
        
        play music free60
        show ju 310 with dis
        
        ju "「You came. 」"
        fn "「...Yep.{p}\ \ I promised before that I'd come to support you,{w=.2}\n\ \ didn't I? 」"
        ju "「...Indeed, {w=.2}you did say something like that.{p}\ \ By the way, {w=.2}you're not with Kodo-... {w=.2}Shun and Ten? 」"
        "He asks after looking around me."
        fn "「They left just a minute ago.{p}\ \ Ten-san took Shun-kun with him to help with his\n\ \ stretching. 」"
        ju "「...So that's why they're not here. 」"
        fn "「...Yeah. 」"
        "Then there's nothing but an uncomfortable silence\nbetween us."
        "...Don't go quiet now.{p}I almost forgot why I came here today.{p}I take a step forward."
        fn "「...Juuichi-san. 」"
        
        show ju 303 with dis
        
        ju "「... 」"
        fn "「I'm sorry for what happened before.{p}\ \ I ran away before we were done. 」"
        fn "「...Until today I was too scared to see you and kept\n\ \ avoiding you. 」"
        
        show ju 301 with dis
        
        ju "「...[ln]. 」"
        fn "「But it feels like I could never talk to you again\n\ \ if I went back home with the way things are now.{p}\ \ So, {w=.2}I... 」"
        fn "「I'm not going to say I want you to love me.{p}\ \ I'm not going to say I don't like you either.{p}\ \ I just wanted to apologize. 」"
        fn "「I pushed my feelings on to you,{w=.2}\n\ \ not thinking one bit about how you felt.{p}\ \ I really am... sorry for what happened. 」"
        "My head hangs down as I talk.{w} As I wait for his\nresponse, {w=.2}I hear cheers coming from down below.{p}A sigh escapes from his mouth."
        
        show ju 303 with dis
        
        ju "「...Bring your head back up.{p}\ \ If anybody has to apologize, {w=.2}it's me. 」"
        fn "「You didn't do anything wrong...! 」"
        "I lift my head up by reflex when I hear what he says."
        
        show ju 301 with dis
        
        ju "「No.{w} I was only looking at you through my common\n\ \ sense.{w} I thought it would be good for you if I\n\ \ stubbornly refused. 」"
        ju "「It was my mistake to begin with. 」"
        
        show ju 308 with dis
        
        ju "「Some part of me thought you shouldn't be having\n\ \ those feelings.{w} So I naturally protected my self by\n\ \ refusing what you said. 」"
        
        show ju 311 with dis
        
        ju "「It's funny when you think about it.{w} I had the\n\ \ experience of falling in love with someone of the\n\ \ same gender once... 」"
        ju "「Even though I knew how you felt more than anyone\n\ \ else, {w=.2}I rejected you from the start. 」"
        
        show ju 303 with dis
        
        ju "「...I apologize for that.{w} Forgive me, {w=.2}[ln]. 」"
        "As he bows his head,{w=.2}\nI try to figure out how I should reply."
        "If I forgive him it'll seem like I'm being \"holier\nthan thou\", {w=.2}but on the other hand it doesn't feel\nright to say I understand."
        "The reason we're having this conversation in the\nfirst place is because of my confession."
        "I should be apologizing, {w=.2}not Juuichi-san...{p}Wait, {w=.2}now I'm just back to the beginning."
        
        $ event_name = _("Proof of Reconciliation")
        
        "Think, think.{w} ...Eventually I give up trying to find\nthe right words and stick my right hand out towards\nJuuichi-san."
        fn "「Juuichi-san.{w} How about we shake hands to reconcile?{p}\ \ Even if it is hard to say whether or not we'll have\n\ \ a clean slate just by doing this. 」"
        
        show ju 301 with dis
        
        ju "「Something like that might not be enough.{p}\ \ {nw}"
        show ju 302 with dis
        extend "...But, {w=.2}it's not a terrible idea either. 」"
        "He reaches out and grabs my right hand.{p}Then he tightly squeezes it,{w=.2}\nstrengthing his grip as his response."
        "Feeling somewhat happy and comfortable, {w=.2}I turn\ntowards him and smile.{w} Juuichi-san does the same, {w=.2}and\ngives me an awkward smile."
        "I can't say for sure whether or not every thing is\npatched up between us, {w=.2}but with this, {w=.2}things have\ncertainly changed dramatically from when I was doing nothing."
        "Thank goodness I came here.{w} Thank goodness I found\nthe courage to do this.{w} I think so sincerely."
        clubmem "「Oh, {w=.2}you're still here senpai?{p}\ \ It's almost time for the match, {w=.2}please hurry! 」"
        "The sound of a voice interrupts us.{p}The owner of the voice, {w=.2}a rabbit wearing a Judo gi\nnear the entrance, {w=.2}jogs up to us."
        "...Well,{w=.2}\nto be more accurate I should say Juuichi-san."
        
        show ju 308 with dis
        
        ju "「...Hm, {w=.2}it's already time? 」"
        "He slowly releases my hand hand turns his back\ntowards me.{w} Then he begins to chase after the\nrabbit... {w=.2}and suddenly stops."
        
        show ju 301 with dis
        
        ju "「...There's still something I have yet to tell you.{p}\ \ After this match, {w=.2}okay? 」"
        fn "「...?{p}\ \ Sure, {w=.2}got it. 」"
        "With a light nod at my reply,{w=.2}{nw}"
        play sound step03
        hide ju with wipe_right
        extend "\nJuuichi-san runs from the audience seating for real\nthis time."
        "What on earth is he going to tell me?{p}It must be something very important\nfor him to say something like that."
        "Hmm, {w=.2}it's bothering me...{p}but for now, {w=.2}let's concentrate on cheering for him."
        
        jump juuichi29_ten_fight
    
    ################################################
    label juuichi29_wolf:
        
        $ event_name = _("That Ferocious Man")
        
        stop music fadeout 5
        scene black with vsdis
        scene arena_entrance with vsdis
        play music daily03
        
        "It's about a twenty minute walk after getting off the\nbus.{w} In front of the large building, {w=.2}I see people\ndressed in Judo gi here and there."
        "The atmosphere is tense."
        "This is the Kazenari martial arts hall, {w=.2}and Juuichi-\nsan is somewhere inside.{w} Even if he is inside, {w=.2}it's\nso large."
        "I'm not even sure I'm allowed to just walk right in."
        "It'd be best if I could find him directly\nbut that might be a difficult task.{p}...Alright, {w=.2}it's time for a slight change of plan."
        "I look around restlessly."
        "I only want to ask a specific question, {w=.2}so anybody\nwould be fine, {w=.2}but I would like it if it was somebody\nwho goes to the same school as him."
        "Then I'd be able to get to Juuichi-san\nwithout taking too much of their time."
        "With that in mind, {w=.2}I greet a wolf meditating in the\nshadow of a bronze statue with his eyes closed."
        
        show tn 002 at center_down with dis
        
        fn "「Um, excuse me. 」"
        
        show tn 003 with dis
        
        "His eyes snap open.{w} He glares at me."
        "...The aura drifting in the air is no longer normal.{p}Even if he's psyching himself up before a match,{w=.2}\nthere's a limit."
        "He's like a soldier preparing for battle.{p}Are all the players like this?{p}I've never been to a tournament, {w=.2}so I wouldn't know."
        "Although I force myself to smile politely,{w=.2}\nhe continues to stare at me, {w=.2}not moving his\nfrightfully scarred face even a single millimeter."
        "H-{w=.2}he's so scary!{w} Maybe I made a slight mistake in\ntalking to him.{w} Why is his face covered with scars in\nthe first place?"
        "Does Judo have weapons that can cut your face like\nthat?"
        "It'd feel more appropriate to call him a warrior\nrather than a martial artist."
        "He's proof you can't strike up a conversation with\nanybody.{w} I swallow, {w=.2}then ask him a question\nwhile trembling in fear."
        fn "「U-um...{w} do you know where the waiting place for\n\ \ Kazenari High is? 」"
        wolf "「... 」"
        "Hmm, did he not hear me?{p}But he's been looking...{w} or maybe I should\nsay watching me for a while now."
        wolf "「... 」"
        "...Maybe I shouldn't get too involved with this\nkind of person.{w} I decide to apologize,{w=.2}\nthen flee from this situation."
        "The idea of apologizing first is probably the nature\nof a coward."
        fn "「U-{w=.2}um, {w=.2}I'm in a hurry...{w} sorry,{w=.2}\n\ \ thank you for your cooperation. 」"
        "I have no idea what he cooperated in,{w=.2}\nbut please overlook that figure of speech,{w=.2}\nI beg of you."
        "In order to not get involved with him further,{w=.2}\nI awkwardly turn my back to him.{w} He suddenly makes a\ngrowl so low, {w=.2}it's like it's creeping on the ground."
        wolf "「...Wait, {w=.2}boy. 」"
        "Wow, he actually spoke...{p}Feeling desperate,{w=.2}\nI look back towards him."
        "With a sharp glint in his narrowed eyes,{w=.2}\nhe questions me."
        
        show tn 001 with dis
        
        wolf "「You want to know where someone who goes to Kazenari\n\ \ Hight is? 」"
        fn "「Y-{w=.2}yes... 」"
        wolf "「What a muddled reply.{p}\ \ {nw}"
        show tn 003 with dis
        extend "Do you want to know or not? {w=.2}Give me a clear answer! 」"
        "He roars.{p}Even though he was by no means loud,{w=.2}\nhis intensity forces me to straighten up and answer."
        fn "「Y-Yes! {w=.2}I want to know! 」"
        wolf "「...{p}\ \ {nw}"
        show tn 001 with dis
        extend "If that's the case, {w=.2}you may tell me who it is. 」"
        fn "「Really!? 」"
        
        show tn 003 with dis
        
        wolf "「...However, {w=.2}there's one thing you will answer\n\ \ before that.{w} For what reason do you approach my\n\ \ alma mater? 」"
        "Just like when I first greeted him,{w=.2}\nthe air feels like it could shatter at any moment.{p}I cringe whenever he glares at me."
        "...Hm? {w=.2}Did he just say this is his alma mater?{p}In other words, {w=.2}this scary person is involved with\nKazenari High?"
        "And that Judo gi he's wearing most likely means he's\na contestant."
        "He doesn't really look like a high schooler though.{p}Oh... {w=.2}but Juuichi-san doesn't look like a teenager at\nfirst glance either."
        "I wonder if most people in Judo look so mature."
        "Anyways, {w=.2}I've lucked out.{p}...In more ways than one."
        fn "「Does somebody named Juuichi Mikazuki belong to\nthere? 」"
        
        show tn 002 with dis
        
        wolf "「... 」"
        "The wolf tilts his two pointed triangles in silence.{p}I don't want to provoke his anger,{w=.2}\nso I continue to speak to him."
        fn "「Err, {w=.2}Juuichi-san is an old friend of mine...{p}I came here today to support him. 」"
        
        show tn 001 with dis
        
        wolf "「...Hmph, {w=.2}you are an acquaintance of Mikazuki's? 」"
        
        play sound standup
        hide tn
        show tn 001 at center 
        with wipe_up
        
        "The wolf stands up as he speaks.{p}I didn't realize it when he was sitting,{w=.2}\nbut this guy is really tall."
        "Could he be bigger than Juuichi-san?"
        "His legs are long and slender, {w=.2}yet their muscles are\nsolidly built.{w} His huge chest that juts out when he\nstands shows no signs of sagging."
        "His old-fashioned tone and atmosphere about him that\npushes away strangers kind of makes resemble Juuichi-\nsan, {w=.2}but their physiques are completely opposite of each other."
        "He's like Juuichi-san if he cut out the junk food and\nwas more sharp.{p}...Juuichi-san would probably take offense to that."
        
        show tn 005 with dis
        
        "He glances at me for a moment,{w=.2}\nthen silently enters the building.{p}...Does that mean I'm supposed to go with him?"
        
        hide tnwith wipe_right
        
        "I chase after him at a quick pace so as not to lose\nsight of the wolf.{w} We go down a corridor,{w=.2}\nup some stairs, {w=.2}and then down another corridor."
        "He suddenly stops in front of a set of double doors,{w=.2}\nthen turns around to face me."
        "...?"
        "I push open the door in front of me.{p}In an instant, {w=.2}I can hear all sorts of sounds."
        
        play sound cheering2
        scene arena with explosion
        
        "Thundering roars, {w=.2}someone being slammed into the mat,{w=.2}\nexcited cheers, {w=.2}and the calls of referees.{p}From here and there, {w=.2}they all come to me at once."
    
        stop sound fadeout 10
        
        "I feel somewhat detached,{w=.2}\nlike something is bubbling up from the bottom of my\nbody."
        "I've never been on a sports team,{w=.2}\nso I can really feel the participants' enthusiasm."
        "Is the second floor for the audience?{p}Being familiar with only small school gyms,{w=.2}\nI look around in amazement."
        "A square within a square.{p}That's how I would describe the structure."
        "There are mats laid on the first floor,{w=.2}\nThe matches are carried out in 4 different squares,{w=.2}\nperfectly forming the \"田\" kanji."
        "Each school has seating on the east, {w=.2}west, {w=.2}south,{w=.2}\nand north sides.{w} On each side and in front of me,{w=.2}\nthere are flags for each school hanging down."
        "I walk to the front of the audience seating,{w=.2}\nand lean over the railing as I look down below."
        "\"Katsumi\" is written in large, powerful letters,{w=.2}\nwith Kazenari High Judo Team beneath it."
        "So, {w=.2}Juuichi-san should be in this section here,{w=.2}\nbut..."
        "I look for him in the seats behind me with eyes wide\nopen.{w} Although everybody is wearing a Judo gi,\nI don't see Juuichi-san among them."
        
        show tn 001 with dis
        
        wolf "「Bad timing.{w} It seems Mikazuki went to a match. 」"
        "The wolf approaches some people near the entrance\nwho must have gotten here earlier.{p}It seems he's asking other members for me."
        "...This person looks fiendish,{w=.2}\nbut maybe he's not such a bad person afterall."
        fn "「Sorry for making you go out of your way like that,\n\ \ I'm really thankful. 」"
        
        show tn 005 with dis
        
        wolf "「...Hmph.{w} There's no reason for me to not make it\n\ \ so even somebody who came here to cheer for the\n\ \ staff is free of obstacles. 」"
        wolf "「That would be against my moral code. 」"
        "He stands next to me, {w=.2}and looks down on the venue in\nsilence.{w} In contrast to his blunt words,{w=.2}\nI catch sight of his tail wagging excitedly."
        "...Correction.{p}I have no doubt he's definitely a good person."
        wolf "「...I've become serious for you. 」"
        fn "「Huh? 」"
        
        show tn 004 with dis
        
        wolf "「...That was a slip of the tongue.{p}\ \ {nw}"
        show tn 001 with dis
        extend "Not a word about that to anyone, {w=.2}alright? 」"
        fn "「...Y-yeah. 」"
        "I didn't hear much of what he said earlier,{w=.2}\nbut I don't know what'll happen if I ask him.{p}I should just let sleeping dogs lie."
        "I decide to keep quiet."
        wolf "「Anyways, Mikazuki's match is starting.{p}\ \ You should do what you came here to do rather than\n\ \ talk with me. 」"
        
        play music free0456 fadein 4
        
        "He jerks his chin to the side to show me."
        "Just as I look over at a section of the hall,\nJuuichi-san is dressed in his Judo gi,\nexchanging bows with his opponent."
        "Compared to Juuichi-san, the other guy seems small\nand compact to me.{w} He looks shorter and lighter."
        "Is he getting cold feet from looking at Juuichi-\nsan...?"
        "I shouldn't be judging by appearances,{w=.2}\nbut it doesn't seem to me that he has\nany chance of losing."
        fn "「It looks like Juuichi-san will win if that's his\nopponent. 」"
        "The wolf replies, {w=.2}continuing to stare\nat the scene below us instead of looking at me."
        wolf "「He has good eyes for an amateur...{p}\ \ I have to praise him for that. 」"
        fn "「Huh? Even if you say that,{w=.2}\n\ \ he obviously looks weak, right? 」"
        "Juuichi-san grapples with the dog.{w} In contrast to his\npassive attitude earlier, {w=.2}the dog boldy takes the\noffensive."
        "...For some reason,{w=.2}\nJuuichi-san is acting as if the wind has been taken\nout of his sails."
        "He had me completely fooled.{p}...But I can't like him for something like that.{p}I mean that's not fair, {w=.2}right?"
        "Making use of his light footwork, {w=.2}the dog moves in\nfor a standing throw.{w} Did he not see a chance for a\ncounterattack?"
        "It's clear even for me that he's just playing\ndefensively."
        "Seeing the progress of the match,{w=.2}\nthe wolf lets out a huge sigh."
        
        show tn 002 with dis
        
        wolf "「...In Judo, {w=.2}you must overcome yourself before you\n\ \ can be victorious. 」"
        "The referee yells \"Stop!\", {w=.2}and both of them return\nto their places.{w} They straighten out their gi and\nface each other again."
        "Then, {w=.2}the referee declares a \"Foul!\" towards Juuichi-\nsan."
        fn "「A foul?{w} That means he loses a point, {w=.2}right? 」"
        
        show tn 001 with dis
        
        wolf "「Correct.{w} Think of it as a disadvantage when it's\n\ \ time for the judges.{w} His opponent certainly is a\n\ \ small fry from the lower ranks... 」"
        wolf "「Hmph, {w=.2}this could be the end for Mikazuki. 」"
        fn "「What?! 」"
        "He waves his hand at me, {w=.2}telling me to be quiet."
        wolf "「If he can get his strength back,{w=.2}\n\ \ there's no way he'll lose.{p}\ \ ...You realize that too, {w=.2}right? 」"
        fn "「...Umm, {w=.2}so he's not going to attack at all? 」"
        wolf "「Correct.{w} {nw}"
        show tn 003 with dis
        extend "That is like becoming Judo itself. 」"
        "The dog spins his body and hooks his right leg."
        "Although Juuichi-san isn't lifted up and resists,{w=.2}\nin the end he can't withstand it,{w=.2}\nand his large bodydances in the air."
        
        play sound bosu35
        
        "Boom, {w=.2}the heavy impact echoes throughout the hall."
        
        show tn 001 with dis
        
        wolf "「...He was saved by his opponent's inexperience. 」"
        "Just as the wolf says, {w=.2}there is no winning judgement.{p}The referee swings his right arm out parallel to the\nmat, {w=.2}and declares \"Half-point!\"."
        "Although the dog hurries into a hold,{w=.2}\nJuuichi-san doesn't miss his chance and raises his\nbody.{w} The referee issues a restraint signal."
        wolf "「Now Mikazuki has all but cut off any way of\n\ \ retreating.{w} Hm... {w=.2}has he resigned himself to losing,{w=.2}\n\ \ or is he just trying to scare the hell out of me? 」"
        "I stare at Juuichi-san downstairs.{p}He shouldn't be shaken by anything."
        "On that face that should usually be a moody frown,{w=.2}\nis clearly a look of impatientce."
        "It's no use. As it is now, {w=.2}Juuichi-san is going to\nlose.{w} The thought of that scares me.{w} Why am I here\nright now?"
        "That's right-- {w=.2}I can shout and cheer for him."
        
        $ renpy.music.set_volume(0.3, 1.0, channel = "music")
        
        fn "{size=+25}「JUUICHI-SAN!! 」"
        fn "{size=+25}「YOU CAN DO IT!! 」"
        
        $ renpy.music.set_volume(0.75, 10.0, channel = "music")
        
        "His face turns towards me.{p}As if he had seen something unbelievable,{w=.2}\nhis eyes open wide in surprise."
        "I'm sorry it took me so long to get here...{w=.2}\nKyouji scolded me a lot too.{p}But even so, {w=.2}I'm finally here."
        "That's why... {w=.2}my way of talking is a little strange.{p}Juuichi-san, {w=.2}please win this match...!"
        
        show tn 004 with dis
        
        wolf "「...Hm? {w=.2}His expression changed.{p}\ \ Cheering for him seems to have motivated him. 」"
        "Just as the wolf says, {w=.2}Juuichi-san suddenly changes\nand bares his teeth to show that he has gotten fired\nup."
        "I can't hear it very well from here, {w=.2}but he also lets\nout a low growl.{w} His opponent curls his tail and puts\nit between his legs."
        "It looks like Juuichi-san is going to completely\ndevour the dog."
        
        show tn 001 with dis
        
        wolf "「Now the real match begins. 」"
        "The referee starts the match, {w=.2}and Juuichi-san goes\nright for the collar with a roar.{w} His opponent tries\nto shake him off, {w=.2}but the grip on him is too strong."
        "He takes a step forward with his left foot,{w=.2}\nand grabs his opponent's arm cuffs,{w=.2}\nmaking him lose his balance."
        "Then, {w=.2}without giving the dog a chance to think,{w=.2}\nJuuichi-san sweeps his right leg."
        
        play sound hit_p09
        
        "SLAM! The sound of the dog striking the mat reaches\nmy ears.{w} {nw}"
        play sound cheering2
        extend "At the same time, {w=.2}the referee raises his\nright arm up, {w=.2}declaring Juuichi-san's victory."
        
        play music free04 fadein 2.5
        
        fn "「Yes! 」"
    
        stop sound fadeout 10
        
        "I jump around in excitement.{p}Until now, {w=.2}I've never seen such a magnificent good-\nbye reversal grand slam."
        
        show tn 002 with dis
        
        wolf "「That was a decent sweeping leg throw just now.{p}\ \ Considering how he's been up until now,{w=.2}\n\ \ I'm pleased he didn't let go. 」"
        "...Was that his way of saying he's really happy\nJuuichi-san won?{w} His tail is wagging again.{p}This guy isn't a very honest person."
        "The opponent's shoulders droop.{p}Juuichi-san offers his hand to help him up.{p}Something like this just screams \"Sportsmanship!\""
        "They bow to each other,{w=.2}\nstep off the red mats dividing the match spaces,{w=.2}\nthen bow again."
        "Juuichi-san turns his face upwards,{w=.2}\nlooking me right in the eyes."
        "Then he suddenly looks away, {w=.2}and continues heading\nfor the exit.{w} Although it's too late, {w=.2}I start feeling\na little too embarassed."
        
        show tn 001 with dis
        
        wolf "「What, {w=.2}did you catch a cold?{p}\ \ Your face is bright red. 」"
        fn "「No, {w=.2}that's not it... 」"
        
        show tn 004 with dis
        
        wolf "「You're blushing even though you're not sick...{p}\ \ You're a strange person. 」"
        "...I guess the words shy or embarassed don't exist in\nhis vocabulary.{w} I feel slightly envious of that."
        
        show tn 001 with dis
        
        wolf "「Well, whatever.{p}\ \ I wonder if this means Mikazuki will put up a good\n\ \ fight.{w} {nw}"
        show tn 003 with dis
        extend "...This should be interesting. 」"
        fn "「Huh? What are you talking about? 」"
        
        show tn 001 with dis
        
        wolf "「I'm saying I am Mikazuki's next opponent. 」"
        fn "「Whaaat?! 」"
        "I accidentally yell.{p}Even though they go to the same school,{w=.2}\nthey have to fight..."
        wolf "「Now what?{p}\ \ This is an individual competition,{w=.2}\n\ \ it has nothing to do with were you come from. 」"
        fn "「Y-yeah, but... 」"
        "I want both of them to win, {w=.2}but that's not possible.{p}It's either going to be him or Juuichi-san."
        wolf "「You should go with your original goal,{w=.2}\n\ \ to support Mikazuki. 」"
        wolf "「If you're thinking about how long Mikazuki and I\n\ \ have known each other, {w=.2}don't trouble yourself over\n\ \ it. 」"
        "I'm not sure if he knows what I'm thinking,{w=.2}\nbut he tells that to me."
        "He's right though...{p}He must have picked that up in the short amount of\ntime we've been talking."
        
        show tn 005 with dis
        
        wolf "「Now then, {w=.2}I must get going soon.{p}\ \ I want to clear my mind before the match. 」"
        fn "「Oh, {w=.2}thanks for showing me the way, {w=.2}and I'm... 」"
        "When I try to bow my head and say I'm sorry again,{w=.2}\nthe wolf stops me with his hand."
        
        show tn 002 with dis
        
        wolf "「As I said earlier, there's no need for apologies.{p}\ \ I did everything by my own volition,{w=.2} don't worry\n\ \ about it. 」"
        fn "「O-okay.{p}\ \ ...Um, {w=.2}please do your best! 」"
        
        show tn 004 with qdis
        
        "The wolf stares at me in wonder.{w} Before long, {w=.2}his\nmouth starts to quiver.{w} Then, {w=.2}he starts to laugh."
        "I don't think this is the right time for him to be\ndoing that..."
        "Did I say something weird?"
        
        show tn 001 with dis
        
        wolf "「...If I do my best, {w=.2}does that mean you're okay with\n\ \ Mikazuki losing? 」"
        fn "「Ah!! 」"
        "Indeed.{p}I promptly open my mouth to speak,{w=.2}\nbut he has a point."
        wolf "「You really are a funny guy.{p}\ \ ...From the beginning I wasn't worried about losing,{w=.2}\n\ \ but now I must win no matter what. 」"
        fn "「That's the problem! 」"
        
        show tn 003 with dis
        
        wolf "「I don't care.{p}\ \ Now that I have your support, {w=.2}losing isn't an option.{p}\ \ To protect my family name, {w=.2}and my pride as a wolf. 」"
        "He bares his canines, {w=.2}displaying a wild smile.{p}Ah, {w=.2}it looks like he's completely fired up."
        "I'm sorry Juuichi-san.{p}I've stirred up your rival."
        
        show tn 005 with dis
        
        wolf "「Mikazuki should be coming up here soon.{p}\ \ Watching amateur matches between strangers is boring,{w=.2}\n\ \ but you're just going to have to wait. 」"
        
        play sound step01
        hide tn with wipe_right
        
        "The wolf departs, {w=.2}leaving me with a strangely\nvillainous line.{w} ...As I watch him leave,{w=.2}\nI suddenly realize I never got his name."
        "After the wolf leaves I return to watching the\nmatches down below.{w} Just like he said, {w=.2}they aren't\ninteresting, {w=.2}but I have nothing else to do right now."
        "At the four different parts, {w=.2}four matches are\nunfolding.{w} Some of them are settled quickly, {w=.2}while\nothers aren't as easily until a decision is made."
        "I thought Judo would be a little more flashy,{w=.2}\nbut now that I'm watching it,{w=.2}\nit's actually quite the opposite."
        "I thought you won by throwing your opponent,{w=.2}\nbut that surprisingly doesn't happen that much."
        "You either hold them down for thirty seconds or get\ntwo half points."
        "The classes at school were relatively one-sided,{w=.2}\nbut that must be unique to amateurs or something."
        "When two people who train every day clash,{w=.2}\nit's completely different."
        
        $ event_name = _("Reunion for the First Time in a Week")

        stop music fadeout 1.5
        
        ju "「...[ln]. 」"
        "Hearing my name suddenly called from behind makes my\nbody freeze.{w} I push out all the air in my lungs so he\nwon't notice, {w=.2}and slowly turn around."
        
        show ju 318 at center with wipe_right
        
        fn "「Juuichi-san. 」"
        "...Was I able to say that as naturally as I usually\ndo?{w} I try to smile, {w=.2}but it feels a little awkward."
        
        play music free60
        show ju 310 with dis
        
        ju "「You came. 」"
        fn "「...Yep.{p}I promised before that I'd come to support you,{w=.2}\ndidn't I? 」"
        ju "「...Indeed, {w=.2}you did say something like that.{p}By the way, {w=.2}about that guy...{p}You were with the captain, {w=.2}weren't you? 」"
        fn "「What guy? 」"
        ju "「The wolf that was standing next to you. 」"
        fn "「Oh, {w=.2}that guy.{w} He left just a minute ago.{p}He had a really strong aura about him,{w=.2}\nbut that makes sense if he's the captain. 」"
        
        show ju 303 with dis
        
        ju "「...Do you two know each other? 」"
        "He frowns as he asks.{p}I shake my head."
        fn "「No... I simply asked him for directions,{w=.2}\n\ \ after that we somehow ended up watching the match\n\ \ together.{w} Today is the first time I've met him. 」"
        
        show ju 308 with dis
        
        ju "「...I see.{p}\ \ You were talking in such a friendly way that I was\n\ \ sure you were old friends. 」"
        fn "「We looked like we were getting along that well?{p}\ \ I thought that guy was overwhelming me. 」"
        ju "「...Oh.{w} It's rare for the captian to talk to anybody\n\ \ before a match to begin with. 」"
        ju "「Well... {w=.2}would it be more correct to say that nobody\n\ \ talks to those who are tense and look like they have\n\ \ a thirst for blood? 」"
        fn "「He was definitely scary at first.{p}\ \ He turned out to not be such a bad person after we\n\ \ talked. 」"
        
        show ju 302 with dis
        
        ju "「...You show an unusual ability to take the\n\ \ initiative on rare occasions. 」"
        ju "「It was courageous of you to talk to the captain\n\ \ before a match, {w=.2}or during the fireworks the other\n\ \ day... 」"
        
        show ju 308 with dis
        
        "After saying that much, {w=.2}he becomes tight-lipped.{p}Then there's nothing but an uncomfortable silence\nbetween us."
        "...Don't go quiet now.{p}I almost forgot why I came here today.{p}I take a step forward."
        fn "「...Juuichi-san. 」"
        
        show ju 303 with dis
        
        ju "「... 」"
        fn "「I'm sorry for what happened before.{p}\ \ I ran away before we were done. 」"
        fn "「...Until today I was too scared to see you and kept\n\ \ avoiding you. 」"
        
        show ju 301 with dis
        
        ju "「...[ln]. 」"
        fn "「But it feels like I could never talk to you again\n\ \ if I went back home with the way things are now.{p}\ \ So, {w=.2}I... 」"
        fn "「I'm not going to say I want you to love me.{p}\ \ I'm not going to say I don't like you either.{p}\ \ I just wanted to apologize. 」"
        fn "「I pushed my feelings on to you,{w=.2}\n\ \ not thinking one bit about how you felt.{p}\ \ I really am... {w=.2}sorry for what happened. 」"
        "My head hangs down as I talk.{w} As I wait for his\n\ \ response, {w=.2}I hear cheers coming from down below.{p}\ \ A sigh escapes from his mouth."
        
        show ju 303 with dis
        
        ju "「...Bring your head back up.{p}\ \ If anybody has to apologize, {w=.2}it's me. 」"
        fn "「You didn't do anything wrong...! 」"
        "I lift my head up by reflex when I hear what he says."
        
        show ju 301 with dis
        
        ju "「No.{w} I was only looking at you through my common\n\ \ sense.{w} I thought it would be good for you if I\n\ \ stubbornly refused. 」"
        ju "「It was my mistake to begin with. 」"
        
        show ju 308 with dis
        
        ju "「Some part of me thought you shouldn't be having\n\ \ those feelings.{w} So I naturally protected my self by\n\ \ refusing what you said. 」"
        
        show ju 311 with dis
        
        ju "「It's funny when you think about it.{w} I had the\n\ \ experience of falling in love with someone of the\n\ \ same gender once... 」"
        ju "「Even though I knew how you felt more than anyone\n\ \ else, {w=.2}I rejected you from the start. 」"
        
        show ju 303 with dis
        
        ju "「...I apologize for that.{w} Forgive me, {w=.2}[ln]. 」"
        "As he bows his head,{w=.2}\nI try to figure out how I should reply."
        "If I forgive him it'll seem like I'm being \"holier\nthan thou\", {w=.2}but on the other hand it doesn't feel\nright to say I understand."
        "The reason we're having this conversation in the\nfirst place is because of my confession."
        "I should be apologizing, {w=.2}not Juuichi-san...{p}Wait, {w=.2}now I'm just back to the beginning."
        
        $ event_name = _("Proof of Reconciliation")
        
        "Think, think.{w} ...Eventually I give up trying to find\nthe right words and stick my right hand out towards\nJuuichi-san."
        fn "「Juuichi-san.{w} How about we shake hands to reconcile?{p}\ \ Even if it is hard to say whether or not we'll have\n\ \ a clean slate just by doing this. 」"
        
        show ju 301 with dis
        
        ju "「Something like that might not be enough.{p}\ \ {nw}"
        show ju 302 with dis
        extend "...But, {w=.2}it's not a terrible idea either. 」"
        "He reaches out and grabs my right hand.{p}Then he tightly squeezes it,{w=.2}\nstrengthing his grip as his response."
        "Feeling somewhat happy and comfortable, {w=.2}I turn\ntowards him and smile.{w} Juuichi-san does the same, {w=.2}and\ngives me an awkward smile."
        "I can't say for sure whether or not every thing is\npatched up between us, {w=.2}but with this, {w=.2}things have\ncertainly changed dramatically from when I was doing nothing."
        "Thank goodness I came here.{w} Thank goodness I found\nthe courage to do this.{w} I think so sincerely."
        clubmem "「Oh, {w=.2}you're still here senpai?{p}\ \ It's almost time for the match, {w=.2}please hurry! 」"
        "The sound of a voice interrupts us.{p}The owner of the voice, {w=.2}a rabbit wearing a Judo gi\nnear the entrance, {w=.2}jogs up to us."
        "...Well,{w=.2}\nto be more accurate I should say Juuichi-san."
        
        show ju 308 with dis
        
        ju "「...Hm, {w=.2}it's already time? 」"
        "He slowly releases my hand hand turns his back\ntowards me.{w} Then he begins to chase after the\nrabbit... {w=.2}and suddenly stops."
        
        show ju 301 with dis
        
        ju "「...There's still something I have yet to tell you.{p}\ \ After this match, {w=.2}okay? 」"
        fn "「...?{p}\ \ Sure, {w=.2}got it. 」"
        "With a light nod at my reply,{w=.2}{nw}"
        play sound step03
        hide ju with wipe_right
        extend "Juuichi-san runs from the audience seating for real\nthis time."
        "What on earth is he going to tell me?{p}It must be something very important\nfor him to say something like that."
        "Hmm, {w=.2}it's bothering me...{p}but for now, {w=.2}let's concentrate on cheering for him."
    
    #################################################################
    label juuichi29_ten_fight:
            
        $ event_name = _("War Cry Chat")

        play music free02 fadein 3
        
        "As I tightly grasp the hand railing,{w=.2}\nI once again overlook the hall."
        "The match between Juuichi-san and his captain...{w=.2}\nis going on this side.{w} The other spots are busy with\nmatches, {w=.2}so this has to be it."
        "Then, {w=.2}people wearing Judo gi slowly gather around me.{p}They all have \"Kazenari High\" sewn on the left side\nof them."
        "...For some reason, {w=.2}the number of club members\nis higher than I expected."
        "Some of them don't hesitate to stare at me as an\noutsider.{w} Others don't mind at all and think I'm\nsomebody's brother or something."
        "There's a great variety of responses to me."
        clubmem "「...Even so, {w=.2}it's a waste. 」"
        clubmem "「Yeah.{w} The captain and assistant captain have plenty\n\ \ of medals, {w=.2}do they have to fight here? 」"
        "I listen to the conversation beside me.{p}If that wolf is the captain,{w=.2}\nthat means the assistant capatain... {w=.2}is Juuichi-san?"
        "I've never heard him mention that before.{p}It would've been nice to know that earlier."
        "...There's no possible way for me to know,{w=.2}\nbut still, {w=.2}I think wanting to is human nature,{w=.2}\nright?"
        clubmem "「It could at least be the semi-finals.{p}\ \ Then it'd be possible to get bronze if you lost. 」"
        clubmem "「The real finals should be held during the quarter\n\ \ finals.{w} The results of the lottery are a pain to\n\ \ deal with. 」"
        clubmem "「The senpais don't have any luck either. 」"
        clubmem "「Even though this is their last high school\n\ \ tournament, {w=.2}it's going to be far from a one-two\n\ \ punch finish since neither one is going to give up the medal easily. 」"
        "...Once again, {w=.2}I hear inexcusable words.{p}Their last tournament?{w} So this is a retirement match?"
        "This is an important event...{w} Hmm, {w=.2}this is Juuichi-\nsan we're talking about here, {w=.2}so I guess he didn't\nwant to make a big deal out of it?"
        "I wanted to look forward to it more naturally since\nit's the last."
        "...Well, {w=.2}It's a forgone conclusion that I would've\nmade a big fuss about it had I known."
        "I probably would have done something like try to\nbring all our friends along."
        "Even though I'm talking to myself here...{w=.2}\nthat'd be more than likely."
        clubmem "「Oh, {w=.2}looks like they're getting started. 」"
        
        $ event_name = _("Their Final Showdown")

        play music free27 fadein 2.5
        
        "Just as he says that, {w=.2}the two of them appear in the\nhall.{w} They both bow to each other on the red mat,{w=.2}\nthen again at the line in the middle."
        "Both of them raise their arms at the same time.{p}Then, {w=.2}the referee shouts \"Begin!\".{p}People all around me start cheering for them."
        "The captain goes right for Juuichi-san's arm cuffs,{w=.2}\nso he responds by stretching out his arms."
        "It seems both of them are trying not to be pulled\nright at the start."
        "After the grappling at the start, {w=.2}there's a series of\nshort, {w=.2}quick movements.{w} Do they not want to show any\nopenings?"
        "Or are they trying to get each other to make a move?"
        "Despite the brief skirmishes, {w=.2}they don't make very\nmany noticeable movents.{w} I can't tell at all who has\nthe upper hand at the moment."
        "Then at the next moment, {w=.2}Juuichi-san turns to attack.{p}He turns his back to the captain while grabbing his\nright arm, {w=.2}trying to throw his opponent by his waist."
        clubmem "「A one-armed shoulder throw!? 」"
        "The judo club members next to me start cheering so\nmuch that it's like they're about to start foaming at\nthe mouth."
        "...I appreciate their explanations,{w=.2}\nbut it'd be nice if they were a little quieter."
        "Juuichi-san's one-armed shoulder throw tosses the\ncaptain--{w} However, {w=.2}what I expected to see happen\ndoesn't come true."
        "The captain sidesteps right as he's about to be\nthrown, {w=.2}preventing Juuichi-san from getting complete\ncontrol of his body."
        "Juuichi-san tries to toss his halfway thrown body\nwith the remaining momentum."
        "The captain's back finally coming in contact with the\nmat doesn't happen though."
        "The captain makes a split-second decision as he\nfalls."
        "Although Juuichi-san tries to pin him down,{w=.2}\nhe becomes like a young turtle and is impossible to\nmove."
        "The referee immediately pauses the match.{p}Without realizing it, {w=.2}I let out a long exhale.{p}Uugh, {w=.2}I don't like this tense feeling."
        "They adjust their gi, {w=.2}then the signal to start is\nissued just as they get to their starting places."
        "Almost instantly they start grappling,{w=.2}\nthis time with the captain attacking."
        "He tries disrupting Juuichi-san's balance by pulling\non his gi.{w} However, {w=.2}the difference in their body\nweights makes it clear that's not going to happen."
        "Even so, {w=.2}the captain tries a second, {w=.2}and then a third\ntime.{w} Does he realize that's not going to work?{p}Juuichi-san takes a step forward to attack."
        "The captain's eyes light up.{p}He looks like a hunter that's about to kill his prey."
        "He sweeps his long leg just barely above the mat,{w=.2}\ncatching the leg Juuichi-san had taken a step forward\nwith."
        
        play sound bosu35
        
        "With great ease, {w=.2}Juuichi-san's large body tips over."
        clubmem "「A leg sweep! {w=.2}That's a finisher! 」"
        "...Technique names aside, {w=.2}I'm sure there's no way he\ncan win now with the way things are going."
        "Gulp.{p}Fortunately, {w=.2}the referee calls a \"Half-point!\".{p}I instantly feel relieved."
        clubmem "「What? {w=.2}That leg sweep completely got him...! 」"
        "The captain seems to understand,{w=.2}\nand goes to pin Juuichi-san down without stopping."
        "He secures his legs, {w=.2}and fortifies his hold on\nJuuichi-san's keft shoulder.{w} From above, {w=.2}the position\nlooks just like an upsidedown V."
        "I learned about this in gym class."
        clubmem "「A compactor! {w=.2}The assistant captain's huge body has\n\ \ become a disadvantage! 」"
        "...That's slightly different from what I learned,{w=.2}\nbut that's okay."
        "Even so, {w=.2}the second half of what he said makes me\nworry.{w} Juuichi-san's body is definitely in a tight\nhold, {w=.2}he can barely move an inch."
        "At this rate, {w=.2}is it only a matter of time...?{p}Unable to do anything, {w=.2}time cruely marches on.{p}5 seconds, {w=.2}10 seconds, {w=.2}15 seconds..."
        "He bounces his body to try to get him off,{w=.2}\nthen tries rotating and shaking both his legs\ntogether.{w} But he still can't get free."
        "Then, {w=.2}the timer runs out.{p}The digital sound of the beep and the captain's howl\noverlap."
        
        stop music fadeout 10
        
        "...Juuichi-san lost.{p}The reality of that hits me like a train."
        clubmem "「...The assistant captain beat him at last year's\n\ \ tournament, {w=.2}so I thought he was always winning\n\ \ against the captain. 」"
        clubmem "「He must have been silently laying down the road\n\ \ work from his hate of that day to lead to this. 」"
        "I listen to them talk next to me.{p}...I see, {w=.2}the captain wanted to\nbeat Juuichi-san in this tournament."
        "Now I understand why he looked so disappointed when\nit seemed like Juuichi-san was going to lose in that\nearlier match."
        "The two of them return to their places and exchange\nbows.{w} Juuichi-san lifts his head up and suddenly\nlooks in my direction."
        "He awkwardly scratches at the side of his face."
        clubmem "「So that's how this year's champion is decided,\n\ \ huh? 」"
        clubmem "「Yeah, {w=.2}the captain is the champ unless there's\n\ \ an upset. 」"
        "I wonder to myself what conversation they would be\nhaving now if Juuichi-san was the champion."
        "I wanted to see Juuichi-san holding a medal,{w=.2}\nbut there's nothing I can do about it."
        "Being his sole supporter,{w=.2}\nthat's all I can do for him."
        "I think about that while waiting several minutes for\nthem to return.{w} The two who waged a fierce battle\nside-by-side enter the audience seating."
        
        if meet_ten == True:
            jump juuichi29_rival_ten
        else:
            jump juuichi29_rival_captain
    
    ##################################################
    label juuichi29_rival_ten:
        
        $ event_name = _("Rivals Then, Friends Now")
    
        show tn 001 at midright
        show ju 318 at midleft
        with wipe_right
        play music free31
        
        fn "「Juuichi-san, {w=.2}Ten-san, {w=.2}good game. 」"
        both "『Thanks. 』"
        "Their voices harmonize beautifully.{p}When I see them cooridinate so well like this,{w=.2}\nit's hard to think that they just fought each other."
        "Juuichi-san and Ten-san both have refreshed looks on\ntheir faces. I think to myself, \"Is this what they\ncall friendly rivals?\"."
        ju "「Today's battle was settled fairly quickly. 」"
        tn "「I got encouragement from a spectator who came to\n\ \ support you.{w} That's why I was in somewhat high\n\ \ spirits. 」"
        
        show ju 310 with dis
        
        ju "「Encouragement? 」"
        "Juuichi-san glances over towards me.{p}\"What do you mean?\" he wordlessly asks me."
        fn "「Th-that was an accident,{w=.2}\n\ \ I didn't mean to. 」"
        "I become flustered and try to explain."
        
        show tn 003 with dis
        
        tn "「...Oh?{p}\ \ Does \"Please do your best\" have some other meaning? 」"
        "He shoots me a sharp look.{p}In other words, {w=.2}I've got a bear at the front door,{w=.2}\nand a wolf at the back...?"
        
        show ju 313 with dis
        
        ju "「...I know what you mean, {w=.2}more or less.{p}\ \ I'll pardon you for that. 」"
        
        show tn 001 with dis
        
        "With a poof, {w=.2}Ten-san's atmosphere is cleared by\nJuuichi-san's words.{w} ...Although I had suspected it\nfor bit beforehand, {w=.2}I've been completely toyed with."
        "...I'm afraid to ask if that's true though."
        tn "「...By the way, {w=.2}Shun-sama isn't with you?{p}\ \ He should have come here by himself. 」"
        fn "「Shun-kun? {w=.2}I haven't seen him in a while.{p}\ \ I just thought he was cheering for you downstairs. 」"
        
        show tn 003 with dis
        
        tn "「This is why I begged him to not come to places like\n\ \ this...! 」"
        
        show ju 319 with dis
        
        ju "「...This place is unexpectedly complex. 」"
        
        show tn 005 with dis
        
        tn "「I'll go look for him...{p}\ \ Are you okay now? 」"
    
        show ju 318 with dis
        
        ju "「Yes, {w=.2}sorry about that. 」"
    
        hide tn with dis
        
        "Ten-san turns his back to us,{w=.2}\nand runs downstairs."
    
        show ju 301 at center with wipe_right
        
        fn "「Uh oh, Ten-san is in trouble now... 」"
        ju "「Yeah, seems like it... 」"
        "Shun-kun should be safe.{p}Well, {w=.2}as long as he doesn't end up somewhere\nstrange in this martial arts hall..."
        
        show ju 311 with dis
        
        ju "「...Anyways,{w=.2}\n\ \ I looked pretty pathetic out there today. 」"
        fn "「That's not true!{w} During your matches you were so\n\ \ lively and looked good.{w} I've fallen in love with you\n\ \ all over again. 」"
        
        show ju 304 with dis
        
        ju "「...I see. 」"
        "He looks down as he speaks,{w=.2}\nand seems somewhat restless compared to earlier."
        "Silently, {w=.2}he rummages around in his bag and wipes\nsweat off with the towel he pulls out."
        "While watching him,{w=.2}\nI'm reminded of something he said before the match."
        "What does he want to tell me?"
        
        show ju 314 at briefzoom
        
        ju "「... 」"
        
        show ju 308 with dis
        
        "He stops wiping with the towel and starts to me a\nquestion."
        "As he looks left and right restlessly, {w=.2}it seems like\nhe's worried about people around us listening."
        
        show ju 303 with dis
        
        ju "「...Sorry, {w=.2}I can't talk about it here.\n\ \ Can we go somewhere else? 」"
        fn "「Sure, {w=.2}no problem I guess... 」"
        "What does he want to talk about that other people\ncan't hear?{w} It seems rare for Juuichi-san to want to\ntalk about something in private."
        "I follow Juuichi-san,{w=.2}\nand go to the outside of the martial arts hall."
    
        jump juuichi29_confession
    
    #############################################################
    label juuichi29_rival_captain:
            
        $ event_name = _("Rivals Then, Friends Now")
        
        show tn 001 at midright
        show ju 318 at midleft
        with wipe_right
        play music free31
        
        fn "「Juuichi-san, {w=.2}Captain, {w=.2}good game. 」"
        captain "「You have no reason to call me captain. 」"
        
        show ju 308 with dis
        
        ju "「Oh be quiet. 」"
        
        show tn 002 with dis
        
        captain "「...Hmph, {w=.2}whatever. 」"
        "When I see them talk like this,{w=.2}\nit's hard to think that they just fought each other."
        "Juuichi-san and the captain both have refreshed looks\non their faces.{w} I think to myself, {w=.2}\"Is this what they\ncall friendly rivals?\""
        
        show ju 301 with dis
        
        ju "「Anyways, {w=.2}today's battle was settled fairly\n\ \ quickly. 」"
        
        show tn 001 with dis
        
        captain "「I got encouragement from a spectator who came to\n\ \ support you.{w} That's why I was in somewhat high\n\ \ spirits. 」"
        
        show ju 303 with dis
        
        ju "「Encouragement? 」"
        "Juuichi-san glances over towards me.{p}\"What do you mean?\" he wordlessly asks me."
        fn "「Th-that was an accident,{w=.2}\n\ \ I didn't mean to. 」"
        "I become flustered and try to explain."
        
        show tn 003 with dis
        
        captain "「...Oh?{p}\ \ Does \"Please do your best\" have some other meaning? 」"
        "He shoots me a sharp look.{p}In other words, {w=.2}I've got a bear at the front door,{w=.2}\nand a wolf at the back...?"
        
        show ju 308 with dis
        
        ju "「...I know what you mean, {w=.2}more or less.{p}\ \ I'll pardon you for that. 」"
        
        show tn 001 with dis
        
        "With a poof, {w=.2}Ten-san's atmosphere is cleared by\nJuuichi-san's words.{w} ...He can just start and stop\nhis thirst for blood as he pleases."
        captain "「...The next match is coming up.{p}\ \ I'll be going soon. 」"
        
        show ju 301 with dis
        
        ju "「Alright. {w=.2}Sorry for keeping you. 」"
        captain "「Loaning out my time is costly. 」"
        ju "「I'll keep that in mind.{p}\ \ ...So, {w=.2}you're not going to go easy on me? 」"
        captain "「Don't be ridiculous. {w=.2}I never intended to. 」"
        
        show tn 005 with dis
        
        "He turns his back to us as he speaks."
        fn "「Um!{w} \"Please do your best!\". 」"
        
        hide tn with wipe_right
        
        "The captain walks out without looking back.{p}If his pointed ears hadn't twitched,{w=.2}\nI would have thought for sure he didn't hear me."
        "I didn't just force it this time,{w=.2}\nso I think I was able to properly express myself\nproperly."
    
        show ju 301 at center with wipe_right
        
        ju "「...Is this really the first time you two have met?\n\ \ Your ability to get along well with anybody is quite\n\ \ impressive sometimes. 」"
        fn "「What? {w=.2}That's not true.{p}\ \ I was just talking to him, {w=.2}that's all. 」"
        
        show ju 302 with dis
        
        "Instead of replying, {w=.2}Juuichi-san shows a small smile.{p}Huh? {w=.2}Did I say something weird?"
        
        show ju 311 with dis
        
        ju "「...Anyways,{w=.2}\n\ \ I looked pretty pathetic out there today. 」"
        fn "「That's not true!{w} During your matches you were so\n\ \ lively and looked good.{w} I've fallen in love with you\n\ \ all over again. 」"
        
        show ju 304 with dis
        
        ju "「...I see. 」"
        "He looks down as he speaks,{w=.2}\nand seems somewhat restless compared to earlier."
        "Silently, {w=.2}he rummages around in his bag and wipes\nsweat off with the towel he pulls out."
        "While watching him,{w=.2}\nI'm reminded of something he said before the match."
        "What does he want to tell me?"
        
        show ju 314 at briefzoom
        
        ju "「... 」"
        
        show ju 308 with dis
        
        "He stops wiping with the towel and starts to me a\nquestion."
        "As he looks left and right restlessly,{w=.2}\nit seems like he's worried about people around us\nlistening."
        
        show ju 303 with dis
        
        ju "「...Sorry, {w=.2}I can't talk about it here.{p}\ \ Can we go somewhere else? 」"
        fn "「Sure, {w=.2}no problem I guess... 」"
        "What does he want to talk about that other people\ncan't hear? {p}It seems rare for Juuichi-san to want to\ntalk about something in private."
        "I follow Juuichi-san,{w=.2}\nand go to the outside of the martial arts hall."
    
    #######################################################
    label juuichi29_confession:
            
        $ event_name = _("Words Reflected in the Sunset")
        
        scene black with wipe_right
        pause 1
        scene arena_entrance red with wipe_right
        
        "A lot of time has passed during the tournament,{w=.2}\nthe building is dyed a beautiful shade of orange."
        "Juuichi-san walks in silence.{p}I don't say anything either."
        "We go around the martial arts hall, {w=.2}and go up a\nnarrow staircase that's out of sight from the public."
        
        scene arena_outside red
        show ju 301 red at center
        with wipe_right
        
        "Then, {w=.2}Juuichi-san stops walking and turns around to\nface me."
        "I think the evening sun shining on his face makes him\nlook even more dashing than usual for some reason."
        "What is he going to talk to me about?{p}Gulp, {w=.2}I swallow saliva."
        
        show ju 308 red with dis
        
        ju "「I've known what your thoughts are so far.{p}\ \ For a while now, {w=.2}I've thinking about my own\n\ \ feelings. 」"
        ju "「...Well, {w=.2}originally I was just going to think about\n\ \ it, {w=.2}I honestly thought nothing would come of it. 」"
        
        show ju 303 red with dis
        
        ju "「What should I do, {w=.2}should I try to find you?{p}\ \ Without being able to make up my mind,{w=.2}\n\ \ time just dragged on. 」"
        ju "「...Honestly, {w=.2}I didn't think you would come here\n\ \ today.{w} Because of that, {w=.2}I didn't think you would\n\ \ cheer for me. 」"
        ju "「That's why, {w=.2}when I heard your voice...{w=.2}\n\ \ I was really surprised. 」"
        ju "「And really...{w} {nw}"
        show ju 302 red with dis
        extend "happy. 」"
        fn "「Juuichi-san... 」"
        
        show ju 301 red with dis
        
        ju "「I don't think this is a case where logic or common\n\ \ sense can be applied.{w} From the start, {w=.2}it was a\n\ \ matter of my heart. 」"
        ju "「I wanted to be honest with my feelings, {w=.2}without\n\ \ being swayed by outside things.{w} When you came here\n\ \ for me, {w=.2}what was that warmth I felt in my chest? 」"
        
        show ju 308 red with dis
        
        ju "「I felt strength flow into my body from your\n\ \ cheering.{w} When you smile at me, {w=.2}my chest tightens so\n\ \ much it hurts for some reason. 」"
        ju "「As I thought about you,{w=.2}\n\ \ I knew you still think about me. 」"
        
        show ju 301 red with dis
        
        ju "「...So, {w=.2}I've finally made up my mind.{p}\ \ From the bottom of my heart, {w=.2}my true fleeings. 」"
        ju "「I don't think I have an obligation to say it at\n\ \ this point. Even so, I... No, I didn't come up here\n\ \ for worthless boasting. 」"
        ju "「[ln], {w=.2}I-- 」"
        
        stop music fadeout 3
        
        "He cuts himself off.{p}Then he looks right into my eyes,{w=.2}\nand takes a deep breath."
        ju "「--I love you too. 」"
        
        play music pops_006
        
        "...Thank goodness for the sunset right now.{p}Otherwise I'm sure Juuichi-san would be able\nto see my cheeks turn bright red."
        ju "「If it's alright with you,{w=.2}\n\ \ will you spend the rest of your time here with me? 」"
        fn "「...Yes, {w=.2}I'd be glad to. 」"
        "I bury my face in his chest.{p}Then gently brush my hand across the crecent marking\non it."
        "His fur feels moist with sweat.{p}The strange smell of it doesn't bother me."
        "If I'm the person Juuichi-san loves, {w=.2}I can accept it.{p}That's the only thing I care about."
        "I wrap both my arms around his shoulders,{w=.2}\nand raise my head while standing on tiptoes."
        "Seeing what I want to do,{w=.2}\nJuuichi-san bends over and brings his face closer to\nmine."
    
        hide ju with dis
        
        "Then I kiss him for the first time.{w} Sweet, {w=.2}that's how\nhe tastes.{w} When our lips part, {w=.2}I try to hide my\nshyness."
        fn "「...Didn't somebody once tell me\n\ \ your first kiss tastes like lemon?{p}\ \ I think that person was wrong. 」"
        fn "「I only tasted sweetness. 」"
        
        show ju 303 red at center with dis
        
        ju "「Oh, {w=.2}that...{p}\ \ I licked some honey candy before the match. 」"
        fn "「What? 」"
        
        show ju 301 red with dis
        
        ju "「Have you ever seen sports club members\n\ \ eat lemon soaked in honey before a game? 」"
        ju "「That was originally because honey\n\ \ has the effect of relieving fatigue. 」"
        fn "「Wow, {w=.2}honey does that, {w=.2}huh?{p}\ \ ...But that's a \"to hell with the mood\" kind of\n\ \ answer. 」"
        
        show ju 303 red with dis
        
        ju "「You might be right.{p}\ \ Well what else could I have said? 」"
        fn "「This is like after school behind the school\n\ \ building...{w} That seems about right, {w=.2}doesn't it?{p}\ \ There's nobody else around. 」"
        
        show ju 308 red with dis
        
        ju "「...Is it really? 」"
        "Seeing him look confused, {w=.2}I nod a few times.{p}In the shadow of a building at dusk with nobody\naround, {w=.2}I think it's the ideal situation."
        fn "「Juuichi-san, {w=.2}can we... do it again? 」"
        "Without answering,{w=.2}\nhe once again brings his face to my mouth.{p}I do the same and close my eyes."
        
        scene black with split_close
        
        "This time it's much, {w=.2}much longer than the first."
        "My tongue gingerly enters Juuichi-san's mouth.{p}For a moment his body freezes up, {w=.2}but he immediately\nrelaxes and even assertively uses his tongue too."
        "Rather than romantic...{w=.2}\nit's more crude and shows our inexperience.{p}We both recognize each other's work."
        "Even so, {w=.2}I'm just happy to be able to kiss him like\nthis."
        "I feel something warm and hard pressing against my\nstomach.{w} I'm also in a position that makes it easy\nfor me to see if he's aroused."
        
        scene arena_outside red
        show ju 301 red at center 
        with split_open
        
        fn "「Juuichi-san...{w} Um, {w=.2}something's hitting me. 」"
        
        show ju 304 red with dis
        
        ju "「I'm a guy, {w=.2}I'm going to get excited from doing this\n\ \ with the person I love. 」"
        "He's talking as if the situation earlier was nothing.{p}...Did the feeling of kissing me get him that worked\nup?"
        "It's kind of like we've reversed our positions from\nearlier.{w} I secretly laugh sarcastically."
        "\"The person I love\", huh?{p}Those words make me feel just a touch embarrassed."
        "We've united each other's feelings like this,{w=.2}\nbut it still doesn't seem real...{p}This isn't a dream or something like that."
        ju "「So... {w=.2}yeah.{p}\ \ I won't force you if you don't want to,{w=.2}\n\ \ but would you like to... {w=.2}here, {w=.2}right now? 」"
        fn "「Here? 」"
        
        show ju 309 red with dis
        
        ju "「...You don't want to? 」"
        "Even though there's pretty much nobody around,{w=.2}\nI'd still feel guilty doing it in a public place."
        "But I'm feeling a just a bit cornered here,{w=.2}\nbeing swept off my feet by Juuichi-san's\nblushing face as he stares at me."
        "I'm the only one who has seen this unexpected side of\nhim.{w} Mine has been affected by him too.{p}I'm achingly erect."
        "I'll probably feel better about once we're doing it.{p}...Now I'm trying to justify it."
        fn "「...Okay. 」"
        
    ################################################
    label juuichi29_sex:

        if persistent.replay == True:            
            $ first = persistent.name_first
            $ last = persistent.name_last
            $ day = 29
            $ event_name = _("Deep Twilight, Strong Feelings")
            
            scene arena_outside red with dis
            
        $ event_name = _("Deep Twilight, Strong Feelings")

        hide ju with dis
        stop music fadeout 10
        $ renpy.music.set_volume(0.25, 10.0, channel = "music")
        
        "He kisses me almost as soon as I answer.{p}\"You don't need to hurry, {w=.2}I'm not running away\"{p}I try to say as my mouth is closed."
        "...There's no need to rush.{p}We still have time.{p}I want to keep feeling him too."
        "As he continues to kiss me,{w=.2}\nhe slowly inserts his hands under the hem of my\nshirt."
        "I try to return the favor and do the same,{w=.2}\nbut I'm blocked by the belt tied tightly around his\nJudo gi.{w} ...This isn't fair, {w=.2}is it?"
        "His thick fingers slide across my chest.{p}Until now, {w=.2}I've never experienced such a\nsweet numbness going through my body."
    
        show ju 303 red at center with dis
        
        ju "「...Sorry, {w=.2}did my claws scratch you? 」"
        fn "「No, {w=.2}that's not it.{p}\ \ ...It just, {w=.2}uh, {w=.2}feels kind of good. 」"
        
        show ju 309 red with dis
        
        ju "「I see. 」"
        
        play sound standup
        
        "Juuichi-san seems impatient as he lifts my shirt up.{p}{nw}"
        hide ju with dis
        extend "I feel his warmth on my chest.{w} I know he's licking my\nnipples, {w=.2}it took me a short time to realize it."
        "Whenever his tongue teases my chest, {w=.2}an indescribable\npleasure strikes me.{w} I never knew until now\nhow sensitive my nipples were..."
        "I can't yell, {w=.2}just gasp.{p}So nobody nearby will hear-, {w=.2}so I won't make any\nnoise-...{w} I can't finish my thoughts."
        "Juuichi-san's tongue creeps around the front of me.{p}Is he not satisfied with just my chest?{p}He licks my stomach and under my armpits."
        "The sight of him doing this reminds me of a bear\nsticking his head in a beehive and licking all around\nhim, {w=.2}looking for honey."
        "...I wonder if that's like a habit or something for\nbears."
        "While he stimulates my nipples with his tongue,{w=.2}\nhe slowly wraps his hand around my lower part."
        "The feeling I'm getting from above and below\nmakes me gasp and shout, {w=.2}even though I try not to.\nJuuichi-san, {w=.2}not that! {p}It's too much..."
        "Suddenly, {w=.2}he slips his hand that was groping me\nthrough my pants into my underwear.{w} He's in direct\ncontact with me."
        "I come close to reaching just that fact."
        "In fact, {w=.2}his warm hand feels so good I could almost\ncry.{w} Each time his thumb rubs my glans, {w=.2}my head goes\nnumb."
        "Juuichi-san lifts his mouth off my chest,{w=.2}\nand kisses me once again.{p}My metal belt makes a jingling noise."
        "He grabs my pants and underwear, {w=.2}and pulls them\ndown to my knees.{w} The central part of me is exposed\nto the open air."
        "Even though there's nobody around,{w=.2}\nI'm still very embarrassed."
        fn "「Juuichi-san, {w=.2}it's not fair if I'm the only one... 」"
        
        show ju 303 red with dis
        
        ju "「...I understand. {w=.2}How about this? 」"
        "He unties his pants.{p}Normally gravity would pull them down,{w=.2}\nbut it looks like his crotch is holding them up."
        
        show ju 304 red with dis
        
        "Then he scratches his chin as he kicks them off.{p}I can feel his arousal and warmth,{w=.2}\nas if he wasn't wearing underwear."
        "...I expected him to be big, {w=.2}but this is incredible.{p}When I see his erect lower half,{w=.2}\nI have to stop myself from drooling."
        "At any rate, {w=.2}his presence is overwhelming.{p}I peel his underwear to the side,{w=.2}\nand see the huge thickness."
        "This thing which throbs with his heartbeat,{w=.2}\nit's seems like something any man wish they had."
        
        show ju 312 red with dis
        
        ju "「...Don't stare at it so much, {w=.2}it's embarrassing. 」"
        fn "「It's so impressive though. 」"
        "I'm only looking at it right now with the\nway we're standing, {w=.2}but I feel like I\ncould start sucking it without hesitation."
        fn "「Um, {w=.2}can I touch it? 」"
        "Juuichi-san nods."
        "I reach out my right hand, {w=.2}and squeeze the shaft\nas hard as I can.{w} {nw}"
        show ju 304 red with dis
        extend "Seeing his face scrunch up a bit\nI quickly let go."
        fn "「Sorry, {w=.2}did that hurt? 」"
        ju "「...No, {w=.2}quite the opposite.{p}\ \ Touching it myself and having somebody else touch it\n\ \ feel different.{w} ...I like it. 」"
        "Breathe a sigh of relief.{w} Then I touch his gun barrel\nagain, {w=.2}this time slowly moving my hand up and down to\nget a feel for it."
        
        play sound sex2 loop
        show ju 312 red with dis
        
        "Juuichi-san seems to be quietly enjoying the\npleasuring of the lower half of his body."
        "He's looking up towards the sky with his eyes closed,{w=.2}\nand occasionally lets out a sharp gasp."
        "He feels my hand.{w} His stern face relaxes,{w=.2}\nand his breathing quickens.{p}That makes me extremely happy."
        "Juuichi-san touches the lower half of my body as\nwell, {w=.2}and starts to stroking it up and down\nforcefully."
        "Even though I'm close to cumming,{w=.2}\nI haven't got to build it up."
        fn "「Ju-{w=.2}Juuichi-san...{w} If you do so much at once,{w=.2}\nI'll cum already... 」"
        
        show ju 309 red with dis
        
        ju "「...I see. 」"
    
        hide ju with dis
        
        "He kisses me.{w} I'm orally ravished, and the lower part\nof me is teased.{w} The waves of pleasure hitting me are\nalmost like an illusion."
        "From my mouth, {w=.2}as well as down there,{w=.2}\nI hear dirty, {w=.2}sloppy sounds."
        "I can't take it anymore.{w} I try to tell Juuichi-san,{w=.2}\nbut with his head firmly fixed into a deep kiss with\nme, {w=.2}that doesn't work out so well."
        fn "「Mmm, mmm! {w=.2}Mmm, mmm! 」"
        "Juuichi-san, {w=.2}it's too late.{w} That's what I wanted to\ntell him, {w=.2}but my words just end up being muffled\nnonsense."
        "I'm going to get his gi dirty.{w} I can't stop it now.{p}Even though I think that, {w=.2}Juucihi-san shows no signs\nof letting me go."
        "He kisses me while intensely stroking me.{p}It's too late.{p}The urge to cum takes over me."
        fn "「Mmm! 」"
     
        stop sound fadeout 5
        play sound2 heartbeat
        scene white with qdis
        scene arena_outside red with qdis
        
        "The fruit of my white lust falls onto his gi.{p}Two times, {w=.2}three times that pleasure makes me shoot.{p}My legs quiver, {w=.2}I can barely stand."
        "Noticing I'm about to collapse to my knees,{w=.2}\nJuuichi-san supports me with his arm."
        
        show ju 304 red at center with dis
        
        ju "「...Are you okay? 」"
        fn "「Y-{w=.2}yeah, {w=.2}I think so.{p}\ \ It just felt so good it made my legs go weak... 」"
        ju "「Take a short rest. 」"
        fn "「...Sorry. 」"
    
        hide ju with dis
        
        "Juuichi-san and I sit down with our backs leaning\nagainst a wall.{w} I have a feeling my heavy breathing\nis audible, {w=.2}making me feel a little embarrassed."
        "He silently puts his arm around my shoulders and\npulls me closer.{w} I quietly lean against him."
        "While listening to the sound of his powerfully\nbeating heart, {w=.2}I take another deep breath.{w} I wonder\nwhy hearing this sound makes me feel so relaxed."
        "It feels like my body is one with his.{p}I stretch my body just a bit, {w=.2}and kiss him."
        fn "「Juuichi-san, {w=.2}you're still hard. 」"
        
        show ju 309 red at center with dis
        
        ju "「...It's from seeing you like that.{p}\ \ I can't settle down. 」"
        "Precum drips from his tip and falls to the ground,{w=.2}\nbut I don't say anything obscene.{w} I reach out,{w=.2}\nwrap my hand around it, {w=.2}and stimulate his glans."
        "His face scrunches.{p}But he said earlier that he wasn't making\nthat expression out of pain."
        "When I turn my wrist, {w=.2}his body shivers with pleasure."
        "A sharp exhale passes from his lips.{p}He endures the pleasure in motionless silence.{p}There's no mistaking that his face is turning red."
        "I want him to feel even better.{p}Quietly, {w=.2}I bring my face closer to his\nthrobbing member."
        "There's a slight odor, {w=.2}but I can put up with it.{p}I open my mouth wide, {w=.2}and take Juuichi-san's glans\ninto my mouth as he tears up with ecstasy."
        
        show ju 312 red with dis
        
        ju "「Guh... 」"
        "He makes a noise.{p}Each time I caress him with my tongue,{w=.2}\nhis brow wrinkles up."
        "Right as I release him, he pushes me to the ground\nwith all his might.{w} When I look up while lying on my\nback, {w=.2}Juuichi-san's form looms over me."    
        "He looks really turned on.{p}Even though it's hard to tell with the backlighting,{w=.2}\nI feel his rough breathing hit my face many times."
        ju "「Sorry, {w=.2}[ln]... {w=.2}I can't hold back any longer.{p}\ \ ...May I put it in? 」"
        fn "「Juuichi-san... 」"
        "To tell you the truth, {w=.2}I'm scared.{p}I don't think there's any way something like that\nwill fit in me."
        "But when I see him look at me so lustfully,{w=.2}\nI hesitate to refuse.{w} This was probably going to\nhappen sooner or later."
        "...So for Juuichi-san, {w=.2}I lift up my rear.{p}I look obidient.{w} Then, {w=.2}I prepare myself."
        fn "「Be gentle, {w=.2}please. 」"
        
        show ju 309 red with dis
        
        ju "「I will.{p}\ \ ...I'd never do anything to hurt you. 」"
        "That makes me feel slightly at ease.{p}He said so, {w=.2}so I'm sure it's true.{p}I just need to trust him."
    
        hide ju with dis
        
        "Juuichi-san lifts my legs up towards his head.{p}I feel the inner parts of them exposed to the air."
        "Suddenly, {w=.2}a warm, {w=.2}rough feeling hits me.{p}At the same time as that creepily good feeling,{w=.2}\nI'm given an indescribably complex stimulation."
        "Like loosening a tightly closed door,{w=.2}\nJuuichi-san licks me with the tip of his tongue."
        "It tickles at first,{w=.2}\nbut I gradually start making sounds of pleasure."
        fn "「Ah, {w=.2}kuh... 」"
        "I've heard stories about it, {w=.2}but...{p}I never knew I was so sensitive there too,{w=.2}\nnor that it felt so good."
        ju "「I'm putting a finger in. 」"
        fn "「O-{w=.2}okay... 」"
        "He backs his face off,{w=.2}\nand presses his middle finger against me."
        "My breathing becomes unwittingly shallow from my\nnervousness of experiencing something I never have\nbefore."
        "Then he pushes harder.{p}It's slightly less painful than I imagined."
        "If anything,{w=.2}\nthis foreign sensation is uncomfortable."
        "...But perhaps that can't be helped because it's\nbeing used for the exact opposite of what it's\nusually used for."
        "As I exhale all the air in my chest, {w=.2}I try to relax\nas much as I can.{w} If I'm not careful, {w=.2}I'll push\nJuuichi-san's finger out."
        "If I lose heart now, {w=.2}he probably won't be able to\nput his in.{w} I quietly endure the sensation while a\ncold sweat runs down my brow."
        "Juuichi-san waits patiently until I'm used to his\nfinger."
        "I try to shift my concentration to other things, {w=.2}when\nhe was groping me, {w=.2}kissing me, {w=.2}or teasing my nipples."
        "Will it be like this for a few minutes?{p}I think I've gotten fairly used to it."
        "I send a signal to Juuichi-san with my eyes.{p}He replies with a nod, {w=.2}and pulls his finger out all\nat once."
        "The rubbing against my intestinal walls gives me a\nstimulus I can't describe."
        "He takes the base of his cock in his right hand,{w=.2}\nand puts the tip against the entrance."
        "...Then finally, {w=.2}Juuichi-san is inside me.{p}I rejoice that I'm able to take him in, {w=.2}while feeling\nanxious about whether or not my body can hold up."
        "No, {w=.2}I decided to trust him, {w=.2}didn't I?{p}To feel anxious would be betraying him.{p}I just focus on Juuichi-san."
        "Weight heavily presses on that part of me.{p}I hear a slippery sound."
        fn "「Oh, {w=.2}Guh... 」"
        "It's hot.{w} \"My insides aren't going to get burned,{w=.2}\nare they?\" I think.{w} I feel that kind of pain in the\nlower half of my body."
        "Even though just just the tip is in,{w=.2}\njust like that, {w=.2}my breathing has become rough."
        "He stops for a moment once he enters,{w=.2}\nand reaches to the part of me that has drooped from\nthe pain."
    
        play sound sex2
        
        "Pain has replaced the sweet, {w=.2}pleasant feeling from\nearlier.{w} \"How did that happen?\" I think as my head\ngoes numb."
        "Juuichi-san proceeds farther in.{w} Pain runs through\nme.{w} He stimulates my penis.{w} It produces pleasure."
        "I relax.{p}Juuichi-san proceeds farther in...{p}The process repeats."
        "How long is that going to continue?{p}The pain from my insides being forcefully expanded\ncompletely numbs my sense of time."
        ju "「I'm all the way in. 」"
        "He puts my right hand where we're joined.{p}Instead of his cock, {w=.2}my hand rubs\nagainst his stiff pubic fur."
        "His huge penis is completely inside me.{p}I entertain the out of place thought of how\nthe body's ability to adapt is really amazing."
        ju "「Sorry, {w=.2}I'm pushing you too far. 」"
        fn "「No, {w=.2}I wanted to do this too,{w=.2}\n\ \ so please don't worry. 」"
        "I try to talk like I normally do,{w=.2}\nbut my breathing cuts me off in strange places.{p}I don't want to worry Juuichi-san too much..."
        ju "「...Are you okay? 」"
        "Right after I say that, I make him concerned for me.{p}I try to force myself to smile,{w=.2}\nbut the dull pain in my abdomen makes me grimace."
        "Seeing that, Juuichi-san tries to pull out.{p}I grab his hand,{w=.2}\nand shake my head left and right."
        fn "「I'm fine.{p}\ \ Please, {w=.2}give me a kiss... 」"
        "He seems to be troubled about what to do,{w=.2}\nbut eventually he seems to comply with what I said."
        "So that there isn't too much weight on where we're\njoined, {w=.2}I quietly bring my face to his."
        "I wrap my arms around his neck and squeeze tightly,{w=.2}\nnot ever wanting to be separated from him again."
        "We kiss.{p}Although that doesn't erase the pain,{w=.2}\nit gives me a sense of fufillment."
        "As far as I'm concered,{w=.2}\nthat's more important than anything else right now."
        ju "「Can I thrust too? 」"
        "I nod once silently.{p}He puts his hands on my shoulders,{w=.2}\nand begins to slowly push."
    
        play sound sex1 loop
        
        "The rubbing sensation inside me\nsets off fireworks in my brain several times."
        "The pain still hasn't subsided,{w=.2}\nbut it seems like it won't be around much longer."
        ju "「You're so tight around me. 」"
        fn "「...Ngh! 」"
        "Juuichi-san wraps his arms around my back and\nbuttocks, {w=.2}firmly embracing my body.{w} What the? I've\nbeen released from the clutches of gravity."
        
        $ event_name = _("When Mind and Body are United")
        
        scene ev_juuichi_1a with sdis
        
        "Juuichi-san pushes in farther.{p}The only thing I can do is moan."
        "Each time he thrusts upwards, {w=.2}the shock that\npenetrates my body is like a hammer striking my head."
        ju "「Sorry, {w=.2}it just feels so good inside you,{w=.2}\n\ \ I don't think I can control myself that much...! 」"
        "I steadily nod while clinging to him.{p}He's moving his back remarkably fast.{p}I endure the relentless pain and hold my breath."
        ju "「Hah, {w=.2}haah...! 」"
        "The sound of gasping and panting escapes from his\nmouth.{w} Slightly sweaty, {w=.2}Juuichi-san looks into my\neyes with a frantic expression."
        ju "「[fn]...! 」"
        fn "「Juuichi-... {w=.2}san. 」"
        ju "「I'm getting close... 」"
        "I focus on where we're joined.{p}He has a slightly dizzy look on his face,{w=.2}\nbut he grimaces in pleasure."
        ju "「Ah, {w=.2}I-{w=.2}I'm cumming, {w=.2}[fn]! 」"
        "I cover up his mouth with my own.{p}He corresponds by forcefully pulling me closer."
        "As he thrusts up and down,{w=.2}\nI almost feel like I could lose conciousness."
    
        stop sound
        play sound2 heartbeat
        scene white with qdis
        scene ev_juuichi_1b with qdis
        
        "Then, {w=.2}he pops.{w} I can feel him shoot cum inside me\nseveral times.{w} It happens over and over again,{w=.2}\nmaking me unsure of when it'll stop."
        ju "「Hah, {w=.2}hah... 」"
        "I hear his disheveled breathing.{p}All I can do now is wait for him to calm down."
        "The energy emitted from him gradually declines.{p}The interval of his thrusts become much longer as\nwell."
        "He pulls his waist back, {w=.2}pulling himself out of me.{p}The white fluid that Juuichi-san released drips out\nof my gaping hole below."
        "...It's not my fault at all,{w=.2}\nbut it's still extremely embarrassing."
        
        scene black with sdis
        scene arena_outside red with sdis
        
        play sound bosu34
        
        "Juuichi-san lowers me to the ground, {w=.2}and sits\ndown with a thud.{w} He may be an active sportsman,{w=.2}\nbut holding me for so long still wears him out."
        "A dull pain circulates around my hole.{p}I did decide to take it, {w=.2}but still...{p}I hope I don't get hemorrhoids at my age."
        fn "「...Juuichi-san, I think that was a little too\n\ \ acrobatic for my first time. 」"
        "I pout. How many times during that did I feel like I\nwas going to pass out? It still felt amazing, but now\nit hurts."
        
        show ju 303 red at center with dis
        
        ju "「I wasn't used to it either, {w=.2}so I didn't know how to\n\ \ adjust very well.{w} I got too excited, {w=.2}and because of\n\ \ that, was too rough.{w} ...I apologize for that. 」"
        "A rough position?{w} I think I've read too much porn.{p}...But Juuichi-san probably isn't as apologetic\nas he seems about treating me like a sex object."
        fn "「I'm fine, {w=.2}that's no reason for me to get mad at\n\ \ you.{w} ...Oh, {w=.2}this isn't meant to be compensation,{w=.2}\n\ \ but there's something I want you to do. 」"
        
        show ju 308 red with dis
        
        ju "「...Hm, {w=.2}what? 」"
        fn "「You called me by my first name earler, {w=.2}didn't you?{p}\ \ I wasn't aware of it at the time,{w=.2}\n\ \ but that made me really happy. 」"
        fn "「So, {w=.2}from now on I want you do that. 」"
        ju "「Got it. 」"
        "I move my body closer to him, {w=.2}and ask for a kiss.{p}Juuichi-san gently raises my chin up,{w=.2}\nand kisses me several times."
    
        hide ju with dis
        
        "...This is happiness.{w} My heart is comfortably warm,{w=.2}\nand I feel content.{w} I can only have this happiness\nfor another two days, {w=.2}but that doesn't matter."
        "I'm not sad.{p}Now there is someone beside me.{p}Now there is someone who can support me."
        fn "「Juuichi-san... {w=.2}I love you. 」"
        ju "「I love you too, {w=.2}[fn]. 」"
        "As if to confirm those words,{w=.2}\nwe continue to exchange kisses in the evening light."
        
        if persistent.replay == True:
            scene black with dis
            pause .5
            $ renpy.end_replay()
            
        $ persistent.event_juuichi1 = True    
    
        jump end29
    
##########################################################
label end29:
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

    jump day30

