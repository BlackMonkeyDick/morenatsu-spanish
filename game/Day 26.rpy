###Day 26
label day26:
    
    $ renpy.music.set_volume(1.0, 0.0, channel = "music")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound2")
    
    $ day = 26
    $ the_date = _("August 26")
    $ event_name = _("８月26日")
    
    if favorite == "kounosuke" or favorite ==  "shun" or favorite == "kouya" or favorite == "shin":
        window hide
        play music birds_chirping
            
        scene sky01 
        show text _("{size=+130}August 26") at truecenter
        with Dissolve(.5)
        
        pause 3
        scene black with Dissolve(1)
        pause .4
        
    else:
        jump day27
        
    $ renpy.jump (favorite + "26")
    
    
######################################################
label kounosuke26:
    
    $ event_name = _("Encouragement")

    scene hbroom with sdis
    play music cicada01
    $ renpy.music.set_volume(0.7, 0.0, channel = "music")
    
    "It's already been two days,{p}since I visited Kounosuke's house."
    "Usually he would have already called me,{p}to come over to meet up,{p}or have some other form of contact..."
    "But he hasn't contacted me at all since then."
    "For now I've turned my feelings,{p}in a different direction,{p}and tried opening up my homework."
    "But the inside of my head is hazy,{p}and I don't make any progress."
    "It's no use. Maybe I should watch TV...{p}I abandon my pencil,{p}and turn towards the living room TV."

    scene black with wipe_right
    
    "......"
    "For some reason,{p}I don't even feel like watching TV."
    "I half-heartedly flip through the channels,{p}but every one of them is boring.{p}I quickly turn it off."

    scene hentry with wipe_right
    
    gm "「Oh my, [fn]-chan. Are you going out? 」"
    fn "「Yeah. I'm going for a little walk. 」"

    scene path with sdis
    $ renpy.music.set_volume(0.9, 0.0, channel = "music")
    
    "Even though I've gone outside,{p}my mood still hasn't cleared up."
    "I know the source of my depression,{p}but going to Kounosuke's house,{p}would definitely be awkward."
    "The Summer sun blazes down,{p}as if it's laughing at me."
    who "「Umm, excuse me... 」"

    show yk 002 at center with wipeleft
    
    yk "「Hello. 」"
    fn "「Oh... 」"
    "I'm taken aback for a moment,{p}when I turn around,{p}and see the tanuki in front of me."
    "But it's not Kounosuke,{p}it's his little brother Yukiharu-kun.{p}He greets me with his usual polite bow."
    fn "「Hello. 」"

    show yk 001 with dis
    
    yk "「What are you doing? 」"
    fn "「Nothing...{p}\ \ Just taking a walk. 」"
    
    show yk 003 with dis
    
    yk "「I see. 」"
    fn "「What about you? 」"
    
    show yk 001 with dis
    
    yk "「I'm going to the park for a meeting. 」"
    fn "「Hmm... 」"
    "Ah, this road goes straight to the park,{p}doesn't it."
    "I wasn't aware of that,{p}since I was just wandering around."
    "Oh, that's right.{p}I should indirectly ask about Kounosuke."
    fn "「By the way, how is Kounosuke feeling? 」"
    yk "「Huh?{nw}"
    show yk 003 with dis
    extend "　Umm... 」"
    yk "「To be honest,{p}\ \ he doesn't seem to have much energy."
    yk "He's usually like that in front of me,{p}but it looks like he's overdoing it. 」"
    fn "「Is that so... 」"

    show yk 001 with dis
    
    yk "「But he's already over his cold.{p}\ \ Were you guys fighting? 」"
    fn "「No, that's not it. 」"
    "His intuition is sharp.{p}I wonder if it's in his genes."

    show yk 003 with dis
    
    yk "「Since there are times when Kounosuke,{p}\ \ really has his heart set on something."
    yk "There are also times where,{p}he'll be depressed for a while. 」"

    show yk 001 with dis
    
    yk "「But I'm not going to say anything to him.{p}\ \ If it's alright,{p}\ \ would you like to hear what I think? 」"
    fn "「Huh? Well... 」"
    yk "「I think it's a stupid thing anyways,{p}\ \ but if somebody doesn't listen to him,{p}\ \ it seems like he'll be like that for a while."
    yk "But he'll get back to normal,{p}if he's left alone long enough. 」"
    "Y-Yukiharu-kun is surprisingly merciless."

    show yk 003 with dis
    
    yk "「However, if he doesn't get back to normal soon,{p}\ \ it's going to get really quiet at home... 」"
    fn "「...I see. 」"

    show yk 001 with dis
    
    yk "「Ah, that's not good.{p}\ \ I need to get going soon,{p}\ \ everybody might be waiting on me. 」"
    fn "「Oh, yeah. See you later. 」"
    yk "「See ya. 」"

    hide yk with wipeleft
    
    "Yukiharu-kun bows and runs off.{p}His way of talking seemed kind of forced,{p}but just a little."
    "After all, he is worried about Kounosuke."
    "Kounosuke...{p}I wonder what he's doing right now.{p}I shouldn't wait forever, should I."
    "If I don't go see him myself,{p}he could be like this for a long time."
    "...I have to go."
    "I ready myself,{p}then turn my feet,{p}towards the Kuri hardware store."

    if ghost_encounter == 3:
        jump kounosuke26_spiritual_guidence
    else:
        jump kounosuke26_kouno_house

    ##########################################################
    label kounosuke26_spiritual_guidence:
    
        show yk 001 at center with wipeleft
    
        yk "「...{w=.5}...{w=.7} 」"
        
        hide yk with dis
        show na 101 with dis
        
        na "「Haah, I wonder if I made it in time. 」"
    
        show na 102 with dis
        
        na "「Jeez, dad sure can be a handful. 」"
    
        show na 101 with dis
        
        na "「Hang in there, my first friend. 」"
    
        hide na with dis
    
    ########################################################
    label kounosuke26_kouno_house:
        
        scene black with sdis
        stop music fadeout 1
        scene kouno_house_out with sdis
        
        "In front of me is Kounosuke's house.{p}I came out here in over 30℃ weather,{p}so I take deep breaths to calm down my heart."
        "I've come all the way out here,{p}I'm not excited about doing this!"
        "I hesitantly raise my hand to the door,{p}psyche myself up by shouting in my mind,{p}and then open the door at once."
        
        play sound tm2_slidedoor000
        show ko 001 at center with wipeleft
        
        ko "「Welco-oh. 」"
    
        show ko 007 with dis
        
        ko "「[fn]... 」"
        fn "「H-hello. 」"
        ko "「Hello. 」"
        "Ooh...{p}Looks like this is going to be difficult.{p}The mood is heavy. Too heavy."
        "This isn't at all like the usual reaction,{p}I was expecting from him."
        "The air is unusually quiet,{p}and I'm at a loss for words,{p}only for a few seconds."
        
        if kouno_badend == True:
            jump kounosuke26_excuse
        else:
            jump kounosuke26_encourage
    
    
    ######################################################
    label kounosuke26_excuse:
        
        $ event_name = _("Reason For Giving Up")
        
        fn "「U-umm. That thing from before,{p}\ \ are you still worrying about it? 」"
        
        show ko 001 with dis
        
        ko "「Huh? 」"
        fn "「I think I was being...{p}\ \ a little too hard on you then.{p}\ \ So I'm sorry! 」"
    
        show ko 005 with dis
        
        ko "「Wh-what are you apologizing for? 」"
        fn "「You're asking what... "
        fn "You haven't contacted me at all since then,{p}\ \ I heard that you've been...{p}\ \ feeling depressed for a while. 」"
    
        show ko 007 with dis
        
        ko "「Well, that's because I thought you were mad...{p}\ \ And... 」"
        fn "「And? 」"
    
        show ko 005 with dis
        
        ko "「There's something that's really hard to say. 」"
        fn "「...? 」"

        hide ko with dis
        
        "Kounosuke mumbles to himself,{p}and retreats into the back of the store,{p}then comes back with that magazine."
        
        show ko 005 with dis
        
        ko "「I tried reading it again.{p}\ \ Look at this. 」"
        "Then, Kounosuke points to some numbers,{p}on the front cover... huh?"
        ko "「See, this is from last year.{p}\ \ Needless to say,{p}\ \ the deadline passed a long time ago. 」"
        fn "「...... 」"
        "I hope this is a joke,{p}but the numbers printed there,{p}are without a doubt last year's date."
        "This astounding truth leaves me shocked,{p}and at a complete loss for words."
    
        show ko 001 with dis
        
        ko "「And I would have called,{p}\ \ and asked about it."
        ko "But it seems this magazine went...{p}\ \ out of publication about half a year ago. 」"
        fn "「...Seriously? 」"
    
        show ko 005 with dis
        
        ko "「I was putting you through so much trouble,{p}\ \ it was so hard to tell you after all that time.{p}\ \ So, I had to lie to you... 」"
        ko "「I'm sorry.{p}\ \ I should have explained everything,{p}\ \ a long time ago. 」"
        fn "「...No, that's alright... 」"
        
        show ko 007 with dis
        
        ko "「I'm really sorry... 」"
        
        stop music fadeout 1
        hide ko with wipeleft
        scene black with sdis
        
        "After that, Kounosuke went back,\nto his usual self."
        "The news was quite the shock,{p}but it turned into a half-funny story."
        
        show ko 007 at center with wipeleft
        
        "...But when I returned,{p}and looked over my shoulder,{p}I saw Kounosuke look sad for a moment."
        "And I don't think...{p}it was just my imagination."
    
        jump end26
        
    ##########################################################
    label kounosuke26_encourage:

        $ event_name = _("Hunting a Tricky Tanuki")
        
        "Th-this is pretty serious.\nHow should I talk to him..."
        
        show ko 001 with dis
        
        ko "「About before, I'm sorry.{p}\ \ Even though you went through,{p}\ \ all that trouble, I drove you away. 」"
        fn "「D-don't worry about it! 」"
        
        show ko 007 with dis
        
        "The silence was only broken for a bit,{p}now it's returned.{p}Eeh, this is awkward!"
        fn "「Aah jeez!{p}\ \ What's with this mood all of a sudden! 」"
        ko "「...... 」"
        fn "「Kounosuke! Don't you feel a little unusual!?{p}\ \ Why do you have to look so gloomy? 」"
        
        show ko 005 with dis
        
        ko "「...Are you saying an idiot,{p}\ \ isn't supposed to worry? 」"
        fn "「Yes, that's right.{p}\ \ That's how you are,{p}\ \ that's how you've always been... 」"
        fn "「You and your stupid ideas,{p}\ \ royally screwing everything up,{p}\ \ and getting us involved too."
        fn "Saying it's not annoying would be a lie,{p}but being an idiot like that,{p}is what makes you Kounosuke... 」"
        
        show ko 007 with dis
        
        ko "「...... 」"
        fn "「Just follow your instincts,{p}\ \ what happens next isn't as important."
        fn "Don't assume you can grab a tanuki,{p}don't get ahead of yourself. 」"
        fn "「You should be thinking about,{p}\ \ taking that grand prize all for yourself!{p}\ \ But you're getting depressed like this... 」"
        ko "「...... 」"
        fn "「The way you are now is completely wrong.{p}\ \ so, hurry up and get back the usual Kounosuke! 」"
        ko "「...... 」"
        fn "「...... 」"
        "I let what I said sink in,{p}but I might have just been,{p}rubbing salt in his wound."
        "Kounosuke says nothing,{p}and the store is once again silent."
    
        show ko 001 with dis
        
        ko "「...Pfft. 」"
    
        play music daily05
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        show ko 002 with dis
        
        ko "「Ahahaha! That's hilarious! 」"
        fn "「Kounosuke? 」"
        ko "「S-sorry, [fn]. 」"
    
        show ko 001 with dis
        
        ko "「But you said,{p}\ \ don't assume you can grab a tanuki,{p}\ \ that means I'm being hunted, doesn't it? 」"
    
        show ko 002 with dis
        
        ko "「Aha, ahahahaha! 」"
        "I don't know how,{p}but I apparently have gotten through to him."
        fn "「Kounosuke...? 」"
        ko "「S-sorry [fn].\n\ \ H-hold on a second. 」"
    
        hide ko with qdis
        scene black with sdis
        scene kouno_house_out
        show ko 001 at center
        with sdis
        
        fn "「Even so, I'm glad it seems,{p}\ \ like you've recovered. 」"
        ko "「Yeah, Sorry about that.{p}\ \ It looks like I was making you worry. 」"
    
        show ko 002 with dis
        
        ko "「But you're right.{p}\ \ That wasn't like me at all. 」"
        fn "「Mmhmm. 」"
        "That's good.{p}This is the usual Kounosuke."
        fn "「Yukiharu-kun was worrying about you too.{p}\ \ I ran into him at the park a while ago. 」"
    
        show ko 001 with dis
        
        ko "「What? Yukiharu went with his friends,{p}\ \ to play at the river just before noon. 」"
        fn "「Huh? But he said he was meeting...{p}\ \ his friends back at the park... 」"
        "So, in other words...{p}That was an excuse to say something to me?"
        fn "「You should be disqualified as a big brother,{p}\ \ because you made him worry like that. 」"
    
        show ko 005 with dis
        
        ko "「Don't say that.\n\ \ I wonder how Yukiharu noticed... 」"
        "Well, anybody would notice, wouldn't they?"
        "To put it bluntly,{p}he was putting out a depressed aura."
        fn "「Ah, that being said,{p}\ \ are you entering the competition after all? 」"
    
        show ko 001 with dis
        
        ko "「Oh, that. Uhh...{w=.5}...{w=.5} 」"
    
        show ko 005 with dis
        
        ko "「I'll still try to do it.{p}\ \ Even if it is a bother to you. 」"
        fn "「That's good! 」"
    
        show ko 001 with dis
        
        ko "「Yeah. 」"
    
        scene black with sdis
        
        "After that, Kounosuke picked out some candidates,{p}from the pictures he had taken."
        "I'm worried about the poem,{p}he'll attach to the one that he uses."
        "I thought I was going to...\nhave to help him with that too, but..."
    
        show ko 002 at center with wipeleft
        
        ko "「It's alright, it's alright.{p}\ \ You've helped me so much,{p}\ \ from here on, I'm going to finish it myself! 」"
        "...then there was that."
        ko "「I've annoyed you in so many ways,{p}\ \ so I'm definitely going...{p}\ \ to win the grand prize for you! 」"
    
        jump end26   
    
######################################################
label shun26:
    
    $ event_name = _("Some Kind of Idea")
    
    scene hentry night with dis
    play sound night_insects loop fadein 1
    play sound2 phone_ring
    pause 2
    play sound phone_pickup
    pause 1
    
    who "「Good evening,{p}\ \ is this the [ln] residence? 」"
    fn "「Yes, that's right. 」"
    "That voice sounds familiar."
    gk "「Sorry for bothering you.{p}\ \ My name is Gaku Kodori.{p}\ \ Is [fn]-san home? 」"
    fn "「Gaku-san?{w=.2} It's me, [fn]. 」"
    gk "「May I speak to you for a little bit? 」"
    fn "「S-sure... 」"
    "This is the first time Gaku-san has ever\ncalled me.{w} In a way, this is the 4th time\nI've heard his voice, right?"
    "Let's see, there was..."
    "The time I went with Shun-kun to the game store\nin Kazenari,{w} the time when he give me\nthose supplies through the door,"
    "and when I went to return\n\"The Kodori Family ・ Sex Guidebook\"."

    stop sound fadeout 1
    
    scene bookstore with dis #!#Change to transition うねうね
    play music shop02 fadein 2.5
    $ renpy.music.set_volume(0.8, 0.0, channel = "music")
    pause 2.5
    show gk 001 at center with dis
    
    gk "「Welcome. 」"
    "I chose a time when it would\nbe the least crowded as possible.{p}Nobody is in the store. Good."
    "I'll take care of business quickly so\nI won't get in the way of his job."
    fn "「Uh, um!{w=.2} Gaku-san! 」"

    show gk at bowing
    pause .2
    
    gk "「[fn]-san. Please come in.{p}\ \ Thank you for looking after Shun\n\ \ when he fainted. 」"
    "For that 1 time at the Bon Festival\nI bow my head politely to him."
    fn "「W-well, I was free anyways. 」"
    
    show gk 002 with dis
    
    gk "「... 」"
    fn "「... 」"
    "Is that the end of the conversation?"
    fn "「Oh, right!{w=.2} Gaku-san! 」"
    
    show gk 001 with dis
    
    gk "「? 」"
    fn "「H-here... 」"
    "I hold out the aforementioned book.\nWith the cover facing down. I'm embarrassed\nand don't look at Gaku-san's eyes..."
    gk "「Aah. You came here to faithfully return that?{p}\ \ Everything in that bag was for Shun, but since\n\ \ you were the one that got it, I don't mind. 」"
    
    show gk 003 with dis
    
    gk "「...are you giving that to me? 」"
    "Why does his voice seem lonely?{w} Rather than that,\nI want to ask who should have this book.{w=.2}\nAnd why did he give it to me?"
    fn "「Um... the meaning of this note. 」"
    "Timidly, I point at the note sticking out of the book."
    
    show gk 002 with dis
    
    gk "「\"Do this up to here -Gaku,\"{w=.2} was it? 」"
    fn "「Y-yeah... 」"
    
    show gk 001 with dis
    
    gk "「If it's not too much trouble,{p}\ \ I want you to do it up to that point.{p}\ \ Further sanctions are added. 」"
    gk "「...that's what it means. 」"
    fn "「I don't understand those 5 words. 」"
    
    show gk 002 with dis
    
    gk "「...I see. 」"
    "Why did his voice get lonely?{w} Rather than that,\nI want to ask him about the hidden meaning\nof those 5 words."
    "And why did he entrust me with that role?\nIs he joking around or is he serious?"
    "Either way, my intentions in this conversation\nare completely ignored, and he rushes right\ninto the volume without incident."
    
    show gk 001 with dis
    
    gk "「How far did you get? 」"
    "Ah... err...{w} It was written\nin the first chapter of the book, the development\nand mechanisms of sexual characteristics."
    "And after that, how to masturbate.{p}In other words, I taught him what to do\nwhen you're hard and excited!"
    "....I let him go as far as cumming in my mouth.\nI think I may have been too generous\nwith my affection."
    fn "「Oh... well... 」"
    
    show gk 005 with dis
    
    gk "「To here? 」"
    "He points out the note."
    fn "「Y-yeah, right to there... 」"
    "And I did it quite well."
    
    show gk 001 with dis
    
    gk "「I see, that's a relief.{p}\ \ A moderate friend of Shun's happened to\n\ \ come back after 5 years and helped him out. 」"
    gk "「Thank you. 」"
    fn "「Yeah... 」"
    gk "「Thank you. 」"
    fn "「Yeah... 」"
    "I'm a moderate friend.\nIt must be so.\nI decide to think that."
    
    stop music fadeout 2.5
    pause 2.5
    scene hentry night with dis #!#Change to transition うねうね
    play music sad01
    $ renpy.music.set_volume(0.8, 0.0, channel = "music")
    
    "What kind of business will it be this time?{p}Well, if Gaku-san wants to talk to me,\nit can only have something to do with Shun-kun."
    gk "「Did Shun come over? 」"
    fn "「Huh?{w=.2} Shun-kun?{p}\ \ He's not at my place...\n\ \ Did something happen? 」"
    gk "「No, not particularly. Besides the fact\n\ \ that he left home without telling his parents, 」"
    gk "「And about 2 or 3 hours have passed,\n\ \ but nothing in particular. 」"
    fn "「That's not \"nothing in particular\"! 」"
    "It's impossible that he went out to play\nwithout saying anything to his dad and mom."
    "Although he is the kind of kid who would forget\nto leave a note saying when he'd return."
    fn "「Well, do you know where he is right now!?\n\ \ Some kind of idea or something... 」"
    gk "「[fn]-san. 」"
    "Huh."
    gk "「I thought that only you would know\n\ \ why he left without saying anything. 」"
    "Whaaaat!?{p}O-of course, Gaku-san knows{p}what I did with Shun-kun that night..."
    fn "「Gaku-san, um...{p}\ \ Do you know how far Shun-kun and I went...? 」"
    "I'm scared of his reply, but I timidly ask him.{p}As a matter of fact, he hasn't heard\nthe full story from Shun-kun, has he!?"
    gk "「Shun often talks about you.{p}\ \ 5 years ago, and longer before that. 」"
    "That probably means I've been found out, right?"
    gk "「He's not there? 」"
    fn "「Um, I'll go look for him! 」"
    gk "「Is that so? Thank you. 」"
    fn "「A-alright then, I'll stay in touch! 」"
    "I-It's no use."
    "I'm scared he knows the truth and it doesn't\nseem like I can talk to him any longer.{p}I'll leave it off for the time being."
    gk "「Ah, one more thing.{p}\ \ I may have a rough idea of where he's at. 」"
    gk "「I think I might want to\n\ \ tell you Shun's favorite place. 」"
    fn "「His favorite place? 」"
    "I pull out the map next to the phonebook\nto understand where Gaku-san is talking about.{p}The woods behind Minasato."
    "Even though he said that's his favorite place,\nI have never heard Shun-kun ever mention that."
    gk "「I don't think he is lost. 」"
    fn "「I-I see... 」"
    gk "「Alright, talk to you later. 」"

    play sound phone_end
    pause 1
    
    "Gaku-san's emotionless and monotone voice\nmakes me feel like I'm being cornered.{p}My stomach hurts..."
    "At any rate, let's go look for Shun-kun.{p}Before that, I'll try to pick out a few\nplaces he may have been."
    "When I think of Kazenari, he hasn't\ngone to Gaku-san's game store, at least not yet."
    "Because of the long waiting time,\nthere's the possibility that he's\nat the bus stop or is already on the bus."
    "If he's in Minasato,\nhe's probably somewhere video game related,\nlike the game store or the bookstore."
    "The school or somebody's house is also a possibility."
    "Hmm... but even if he's at one of those places,\nthere's no reason for him to leave\nwithout saying anything."
    "I think about what Shun-kun can't tell his parents\nand what he would hesitate to tell somebody."
    "The only thing that comes to mind\nis his secret relationship with me."
    "But we didn't promise to meet anywhere..."
    "Besides, even if we were having a secret date,\ngoing out to play with his childhood friend\nwould have been a good enough explanation."
    "Still, I'm stuck on the fact that\nhe went out without telling anybody,{p}That makes me worry..."
    
    stop music fadeout 1
    pause 1
    scene black with wipe_dr

    $ event_name = _("In the Depths of the Woods")

    play sound musi2 loop
    pause .2
    scene forest01 night with wipe_dr
    
    "I checked the shopping district\nand everybody's houses, walking to places\nof interest within an easy reach,"
    "but I couldn't find any leading information."
    "I wonder if he's here, then...{p}I go into the depths of the woods\nI was informed about."

    show su 013 night at center with sdis
    
    fn "「Shun-kun! 」"
    su "「...Ah. 」"
    su "「[fn]-san, good evening. 」"
    fn "「Shun-kun!{w=.2} Are you alright!? 」"
    
    show su 015 night with dis
    
    su "「Huh? 」"
    fn "「Did you go out to play without telling anybody?{p}\ \ I got a call from Gaku-san. 」"
    
    show su 010 night with dis
    
    su "「I-I'm sorry... 」"
    "Nevertheless, this is a relief.{p}He didn't get lost or kidnapped,\nit seems he just went here by himself."
    "However, his eyes are a little red.{p}I realize immediately that there are\ntraces of wiped tears."
    fn "「Don't worry about it.{p}\ \ More importantly, what are you doing here? 」"
    su "「...I,{nw}"
    show su 002 night with dis
    extend " I was taking a walk from home.{p}\ \ I wasn't paying attention, and ended up here. 」"
    "His tail wags once, then hangs down again."
    "That probably isn't the reason\nwhy his face is a mess,{p}that's apparent without him saying anything."
    fn "「You were crying... weren't you? 」"
    
    show su 001 night with dis
    
    su "「!{w=.2} ...um, I'm lost.\n\ \ I got a little lonely. 」"
    fn "「Shun-kun.{p}\ \ I was worried. 」"
    
    show su 004 night with dis
    
    "I admonish him, but as gently as I can.{p}My voice tightens."
    "What is straining him?{p}What is he enduring?{p}Why won't he say anything?"
    "When he fainted at the Bon Festival and\nwhen he didn't want to go to it."
    "Shun-kun is taking all these things\non himself and worrying about them alone."
    "I finally notice his suffering\nafter he begins to cry."
    "In which case, I'm too late.{p}If only I had been able to understand\nit out sooner."
    "Even though I had decided\nI wouldn't make him cry anymore."
    fn "「Shun-kun. 」"
    fn "「What happened? 」"
    
    show su 010 night with dis
    stop sound fadeout 1    
    play music free58
    $ renpy.music.set_volume(0.8, 0.0, channel = "music")    
    
    su "「N-no. 」"
    fn "「Huh? 」"
    "Shun-kun draws back and guards himself against me.{p}His voice shakes with fear."
    su "「You came here to visit for summer vacation,{p}\ \ so I don't want to say that it hasn't been fun.{p}\ \ I want you to smile. 」"
    fn "「... 」"
    su "「This is a special summer vacation,{p}\ \ and again I'm... thinking about what I want.{nw}"
    hide su with qdis
    extend " 」"
    "I embrace him,{p}not wanting to hear that again."
    fn "「No, don't say that.{p}\ \ Why are you suffering alone!?{p}\ \ Aren't we friends?{w=.2} Childhood friends? 」"
    fn "「We are, there's no reason for us\n\ \ not to be able to talk about anything. 」"
    fn "「A summer vacation without you smiling\n\ \ would be boring for me, right? 」"
    
    show su 016 big night at center_big with dis
    
    su "「B-but... 」"
    fn "「Or is it that you can't help but talk to me?{p}\ \ With both those times at the Bon Festival, haven't\n\ \ you talked to me plenty of times up to now? 」"
    "Shun-kun covers his ears\nin surprise at my loud voice.{p}Sorry, but this is getting out of hand."

    show su 004 big night with dis
    
    su "「[fn]-san, you're so kind...{p}\ \ I'm glad you let me talk to you so much. 」"
    fn "「And that's good, right?{p}\ \ That was the best way\n\ \ I could help you out. 」"
    fn "「You've been hiding your sadness in the depths\n\ \ of your heart and forcing yourself\n\ \ to smile the whole time. 」"
    fn "「If you are happy, then I am happy. 」"
    
    show su 016 big night with dis
    
    su "「Fu...fueh... 」"
    fn "「That's because I love you. 」"
    su "「Uu...{nw}"
    show su 003 big night with dis
    extend " Uwaaan!!\nI... l-love you too... 」"

    hide su with sdis
    
    "Shun-kun sobs into my chest.{p}I want to protect him.{p}I don't want to make him cry."
    "When he wants to shed tears,\nI will always lend a shoulder to cry on.{p}I think that's the kind of partner I want to be."
    
    stop music fadeout 1
    pause 1
    scene black with sdis 
   
    $ event_name = _("Iwao and Gaku's Feud")

    scene forest01 night
    show su 012 night at center
    with sdis    
    play music sad02
    $ renpy.music.set_volume(0.8, 0.0, channel = "music")
    
    "I look after him for the umpteenth time.{p}After he calms down we both sit down side-by-side\nand I listen to him talk, like last time."
    su "「Hic... Iwao-sama and Gaku-san\n\ \ ...They're fighting. 」"
    "Gaku-san...\nHe only told me what he knew, didn't he?"
    "It's like I'm the main cause for Shun's disappearance.{p}Thanks a lot."
    
    show su 004 night with dis
    
    su "「Gaku-san went in my place for the ceremony\n\ \ at the festival the other day.{p}\ \ All of my relatives were okay with it.  」"
    su "「They said that Gaku-san had been properly\n\ \ recognized as part of the Kodori family. 」"
    
    show su 016 night with dis
    
    su "「He said, \"That was like an accident,\n\ \ from now on he will never cross the\n\ \ threshold of the Kodori house\". 」"
    su "「He was saying terrible things... 」"
    "Then Gaku-san got pissed off, withdrew from here,\nand returned to Kazenari."
    "Now it seems their relations are much more strained."
    
    show su 010 night with dis
    
    su "「I... love Iwao-sama and Gaku-san.{p}\ \ But sometimes it's hard to do the ceremony\n\ \ with my whole family... 」"
    su "「I still love them. But even so.{p}\ \ Before I knew it, everybody got angry.{p}\ \ They said I'm being selfish this summer vacation. 」"
    "Shun-kun's selfishness.{p}That was his desire to be with me,{w=.2}\nit was an innocent wish."
    "Because of that, the family that\nis important to him is in discord."
    "So... he ran away from home,\nand eventually Minasato.{p}Nobody wants to see their family fighting."
    
    show su 004 night with dis
    
    su "「When I was thinking about all of that,\n\ \ I ended up here without realizing it. 」"
    "Shun-kun didn't want to be in Minasato\nwith his quarreling grandfather,{p}and it's difficult to get to Gaku-san's place."
    "So he went to the farthest place from the village,\nthe depths of the woods."
    fn "「I see.{w} Gaku-san and your grandfather\n\ \ are both very important to you, aren't they? 」"
    fn "「And that's why you couldn't watch them fight?{p}\ \ You're so gentle, that's what I like about you. 」"
    
    show su 001 night with dis
    
    su "「[fn]-san... 」"
    fn "「What do you want to do?{p}\ \ You don't like Minasato the way it is now, do you? 」"
    
    show su 004 night with dis
    
    su "「Yeah... I want Gaku-san\n\ \ and Iwao-sama to make up with each other.{p}\ \ I want everybody to get along like they used to. 」"
    fn "「You need to tell them how you feel. 」"
    
    show su 016 night with dis
    
    su "「B-but... they won't listen to me. 」"
    fn "「Have you tried talking to them? 」"
    
    show su 003 night with dis
    
    su "「N-no, I can't tell Iwao-sama what I think...{p}\ \ Even during the Bon Festival he was angry... 」"
    fn "「Does he scare you? 」"
    
    show su 010 night with dis
    
    su "「Y-yeah... He's usually nice.{p}\ \ But he's very strict about the ceremony. 」"
    fn "「But you need to talk to him.{p}\ \ He'll understand how you feel, right?{p}\ \ How you want him to reconcile with Gaku-san. 」"
    
    show su 004 night with dis
    
    su "「Okay... 」"
    "「Your grandfather wanted you to be\nin the Bon and Summer Festivals. 」"
    fn "「It's parental love to want you to grow\n\ \ into a fine adult, isn't it? 」"
    fn "「Sorry, but honestly even somebody\n\ \ who is a little hard-headed thinks that. 」"
    
    show su 003 night with dis
    
    su "「W-woof... 」"
    fn "「Sometimes you have to say harsh things\n\ \ if you think it's something important."
    fn "「Even I was forcefully\n\ \ questioning you earlier, right?{p}\ \ ...sorry about that. 」"
    
    show su 004 night with dis
    
    su "「That's okay, please don't apologize... 」"
    fn "「Believe that if you talk to your grandfather\n\ \ about Gaku-san, he may suddenly\n\ \ and unexpectedly forgive him. 」"
    
    show su 001 night with dis
    
    su "「Okay...{p}\ \ I'll try to talk to him.{p}\ \ I want everybody to get along. 」"
    fn "「Yep!{w=.2} It'll be good when things\n\ \ go back to the way they were, right? 」"
    
    show su 002 night with dis
    
    su "「Yes! 」"
    "Shun-kun laughs and smiles.{p}Things still haven't been resolved,\nbut everything will be fine at this rate."
    
    scene black with sdis
    stop music fadeout 1
    pause 1    

    $ event_name = _("Promise from 5 Years Ago")

    scene forest01 night
    show su 001 night at center
    with sdis    
    play music pops_003 fadein 1
    $ renpy.music.set_volume(0.8, 0.0, channel = "music")
    
    fn "「Even so, this summer has been really\n\ \ hectic for you, hasn't it? 」"

    show su tailwag 01 night with dis
    
    su "「Yeah... It's the first it's been like this\n\ \ in a long time.{w} So much has happened.{p}\ \ I'm getting a little tired of it. 」"
    fn "「I see.{p}\ \ Me coming back is part of that, isn't it? 」"
    
    stop music    
    show su 004 night with dis
    
    su "「...Huh? 」"
    fn "「Maybe I shouldn't have come back,\n\ \ A-ahaha... 」"
    
    show su 013 night with dis
    
    "While I'm talking and giving a strained laugh,{p}Shun-kun's face turns white in an instant."
    "I-It was a joke,\nI wanted to lighten the mood!{p}Aaaaah, it looks like I've failed!"
    
    play music sad03
    $ renpy.music.set_volume(0.8, 0.0, channel = "music")    
    show su 013 night at shivering
    pause .2
    
    su "「Th-that's... 」"
    su "「Please don't say something like that. 」"
    su "「Th,this summer... I've... 」"
    su "「had a lot of fun. 」"
    "Dammit.{w} His shoulders are shaking like he could\nexplode at any second, but he still talks\nin a quiet timid voice."
    "It's painful just to look at him.{p}E-Even though I worked so hard to get his smile back,\nI made him cry again..."
    fn "「Sh-Shun-kun, um... 」"
    su "「For a long time I thought you wouldn't\n\ \ come back again... and then you did, so I... 」"
    "Hm?{p}「{cps=10}wouldn't come back again 」?"
    fn "「You thought I wasn't going to come back\n\ \ to Minasato...? 」"
    
    show su 013 night at still with dis
    
    su "「...\"We'll see each other again soon.\"{p}\ \ That's what you told me.{p}\ \ Back when you said goodbye. 」"
    "Over the course of 5 years,\nmy memories of Minasato have faded."
    "When I said farewell to Shun-kun,\nI told him that...{w=.2}it seems.{p}A childish promise."

    show su 008 night with dis
    
    su "「...Hehe, I kept believing in that.{p}\ \ \"Soon, he'll be here soon,\" I kept saying... 」"
    
    show su 012 night with dis
    
    su "「But you didn't. 」"
    su "「So somewhere in my mind I started\n\ \ thinking that you weren't coming back. 」"
    "That was probably easier for Shun-kun, rather\nthan waiting and believing in his friend\nwhose time of return was unknown."
    su "「When I talked about everybody wanting to see you, 」"
    su "「That feeling along with\n\ \ what I wanted to do was too much,\n\ \ and I would get an anxious feeling in my chest. 」"
    su "「...this year, you came back.{p}\ \ The same you as 5 years ago returned. 」"
    su "「So please don't say that\n\ \ you shouldn't have come back. 」"
    su "「I... I had been thinking about if you didn't come.{p}\ \ I was constantly thinking that you weren't coming back. 」"
    su "「You weren't in Minasato for so long.{p}\ \ I was sure you had forgotten about 5 years ago,\n\ \ and it became a Minasato without [fn]-san. 」"
    su "「I... hated that. 」"
    "Only a few tears are flowing out.{p}Is that because he's been crying for so long?"
    "But his voice is getting smaller.{p}Sometimes his body trembles as if he's in pain."
    fn "「It's not like that. 」"
    fn "「It's not like that at all. 」"
    "When I reach out my hand to a completely dejected\nShun-kun, he flinches and ducks his head.\nThat hurts my heart..."
    "I run my fingers through his smooth hair\nand carefully pat his head."
    
    show su 012 big night at center_big with dis
    
    fn "「Sorry. I said something weird, didn't I?{p}\ \ I came back to Minasato.{p}\ \ To see you, right? 」"
    fn "「You don't have to forgive me right now, okay? 」"
    su "「No, that's fine.{p}\ \ You did come back.{p}\ \ You were able to remember. 」"
    "When I gently rub his body, Shun-kun smiles\nwith a bit of relief.{w} The barley tea I brought\nhelps his throat feel better."
    
    stop music fadeout 1
    pause 1
    scene forest01 night with dis 
   
    $ event_name = _("The Same Place")
    
    play music free58
    $ renpy.music.set_volume(0.8, 0.0, channel = "music")

    show su 004 night at center with dis
    
    su "「[fn]-san,\n\ \ the first thing I said was that I got lost, right? 」"
    fn "「...you did? 」"
    "I did think that, but it seems like he's lying.{p}Did he just trick me?"
    
    show su 001 night with dis
    
    su "「That's not true.{p}\ \ I've been here a few times before. 」"
    fn "「Hm? 」"
    su "「When you left, {w=.2}I came here. 」"
    fn "「5 years ago? 」"
    
    show su 002 night with dis
    
    su "「Yes.{p}\ \ Back then I cried so much. 」"
    fn "「Really... 」"
    "A place where you can cry without\nbeing seen by anybody.{w} For Shun-kun,\nthat was in the depths of these woods?"
    
    show su 010 night with dis
    
    su "「On the last day of summer vacation...\n\ \ I'll probably come here. 」"
    fn "「! 」"
    "Th-that's right...\nSo many days have already passed,\nI have to leave Minasato. "
    "Is this how Shun-kun is going to brave\nour impending moment of separation?"
    "「We'll see each other again soon 」{w} ...\n\ \ I stop myself from saying that.{w} That stupid,\n\ \ cliche promise from 5 years ago hurt him."
    
    show su 002 night with dis
    
    su "「I was able to be with you like this, even\n\ \ though I thought I would never see you again. 」"
    su "「This was a very special\n\ \ and valuable summer vacation. 」"
    fn "「Th-that's... 」"
    "He's talking as if he has already had enough fun,\nand has a small resigned smile.{p}I-I'm not sure if I should say something."
    "Should I make a new promise?{p}What would I do if I couldn't keep it?{p}Stay in Minasato longer?"
    "That's unrealistic, isn't it?{p}Take Shun-kun home with me?{p}Isn't that even more unrealistic?"
    "Is there any way I can make him truly smile\nso that he isn't suffering any longer?"
    fn "「Sh-Shun-kun... 」"
    
    show su 022 night with dis
    
    su "「[fn]-san, can I get a little closer...? 」"
    fn "「Oh, yeah, of course! 」"
    
    show su 002 night with dis
    
    "Even though he has the same smiling face as usual,\nhis eyes and cheeks that I don't know\nhow many times have got wet are heartrending."
    "His fur has changed into a lonely color."

    hide su with dis
    
    "Shun-kun stands up and turns to my front,\nI gently receive him.{p}W-whoa, my balance..."

    show su 016 big night at center_big with dis
    
    su "「Hwaaa!?{w=.2} [fn]-san!? 」"

    hide su with dis
    play sound si_gasa03
    
    "I roll back so that I forcefully fall down.\nWith my arms, I turn over his back that had fallen\non me. His body close to me is strangely hot."
    su "「[fn]-sa... 」"
    fn "「I love you, Shun-kun. 」"
    fn "「More than as an old playmate or friend.\n\ \ I think you're very important to me.{p}\ \ I love you more than anything else in the world. 」"
    "I wonder, are these embarrassing words coming out\nbecause I'll be leaving him soon?"
    fn "「So when I heard that you left,\n\ \ I was really worried. 」"
    "I loosen my arms and look up at him.{p}We gaze at each other at close range."
    
    show su 022 big night at center_big with dis
    
    su "「I-I'm sorry... 」"
    
    show su 011 big night with dis
    
    "With reddened cheeks, he hangs his head down again."
    fn "「I'm glad I found you.{p}\ \ ...I love you, Shun-kun. 」"
    "He stares into my eyes as I smile at him."
    
    show su 019 big night with dis
    
    su "「I...{p}\ \ love you too. 」"
    
    show su 022 big night with dis
    
    su "「For 5 years I always, always have. 」"
    
    show su 017 big night with dis
    
    su "「Fueh... 」"
    "This short exchange could possibly\nbe called a confession."
    "With my posture facing upwards,\nI rub Shun-kun's back,\nwhose stomach has sitting on top of me."
    "I alternate between looking\nat the still-bright summer sky,\nand my beloved partner."

    scene black with sdis    
    stop music fadeout 1
    pause 1

#######################################################
label shun26_sex:    
    
    if persistent.replay == True:
        $ first = persistent.name_first
        $ last = persistent.name_last
        $ day = 26
        $ event_name = _("Muffled continued")
        
        scene black with dis
    
    $ event_name = _("Muffled continued")

    scene forest01 night
    show su 017 big night at center_big
    with sdis    
    play music free0468
    $ renpy.music.set_volume(0.8, 0.0, channel = "music")    
    
    "Still, this position might honestly be dangerous."
    "I'm facing upward and he's facing down,\nand we're embracing each other from the front.\nHis head is on my chest."
    "And with this posture in which we're close together,\nthere's no need to think about height difference.{p}Our stomachs rub against each other."
    "Even without that, we're in a special relationship\nin which we understand our love for each other."
    "For a while now I have been breathing\nin the wolf's scent. I'm relieved\nthat I found Shun-kun after he disappeared."
    "In this way I can be happy near him.{p}I can now say that I'm in a very relaxed state."
    "I think more and more about his flicking ears,\nhis muzzle and tail that I want to grab,\nthe boundary line separating the 2 colors of his fur,"
    "The long breaths of his formerly crying voice,\nand his weight sitting on me."
    
    stop music fadeout 1
    
    "Th-the point is, I receiving the stimulus\nthat excites healthy young men.{p}The legs wrapped around me are so tempting to touch!"
    "Ah, wait at least another 30 minutes...{p}my voice of reason fruitlessly tells me."
    "My desire begins to raise its head.{p}I notice it straining stiffly against my jeans."
    
    show su 019 big night with dis
    
    su "「...Ah, [fn]-san... 」"
    "Shun-kun, who has gradually calmed down,\nmutters embarrassingly while casting his gaze at my crotch area.\nHe definitely notices it."
    fn "「S-sorry... 」"
    
    show su 022 big night with dis
    
    su "「U-um,{p}if it's{size=-10} with you... 」"
    "His voice gets smaller and smaller,{p}but my sharp hearing doesn't miss it."
    
    show su 017 big night with dis
    
    su "「{size=-10}That thing... from the other day...{p}\ \ I want to do it. 」"
    fn "「Th-the other day...?{p}\ \ You mean when I stayed at your house? 」"
    "With clouded eyes, he embarrassingly gestures\nwith all his might.{w} His red-colored ears\ndroop slightly, and his tail weakly sways."
    "That swaying... is that proof he wants to do it?{p}That groundless suspicion passes through my mind."
    "Heheheh,{p}he's reached the point where he can ask\nfor it himself, hasn't he?"
    "Although I'm thinking that in the back of my head,\nmy main thought center is bustling with activity."
    "This is the place.{p}May I let him have his first experience here?"
    "First of all, he's missing right now.{p}He needs to get home as soon as possible."
    "Besides, if Shun-kun has the desire to unite\nour bodies, it's simply because I gave him\nthe chance the other day to {cps=10}awaken that."
    "In other words, if I hadn't made a move on him,\nwe wouldn't have ended up like this."
    "The responsibility is all in my hands.{p}Did I leave an impression on him?"
    "No, no, eventually it would have been\nin the hands of somebody of the Kodori family."
    
    show su 019 big night with dis
    
    su "「Yes...{p}\ \ Gaku-san taught me what\n\ \ to do with somebody you love. 」"
    "So by Gaku-san's hand...WHAAAAAAT!?"
    fn "「Wh-what? 」"
    
    show su 018 big night with dis
    
    su "「W-woof, you're being loud...{p}\ \ You scared me. 」"
    fn "「S-sorry... so you talked to Gaku-san\n\ \ about what you want to do with me...? 」"
    
    show su 011 big night with sdis
    
    "Gaaaaah.{p}The tips of his ears redden\nand his tail hangs down."
    "It-it can't be, right?{w} Even I understand that if\na conversation turns in an unpleasant direction,{p}I take into consideration shy Shun-kun's feelings,"
    "and try to refrain from talking about things\nthat agitate his excessive bashfulness!"
    "B-{w=.2}but now that he mentions Gaku-san,\nwhat kind of exchange did they have?!{p}Do I have to check to make sure?!"
    "If Gaku-san heard that I had\nShun-kun's thing in my mouth...\nI'm too afraid to think about it."
    "Even so, I know exactly what Shun-kun means by\n「I want to do that thing 」. I want to do just\nas he wishes because I love him to the fullest."
    "For that reason, I don't need to speak\nthe required information."
    "{size=-10}There's no way I'd ever want\nShun-kun to say a rude thing like\n{cps=10}「Please touch my penis... 」"
    "{size=-10}No way at all."
    
    show su 017 big night with dis
    
    su "「Ha-hau...e-err,\n\ \ this is embarrassing... 」"
    fn "「Y-yeah, it is, isn't it...{p}\ \ But I also want to know\n\ \ what you and Gaku-san talked about. 」"
    
    show su 019 big night with dis
    
    su "「Uu... I asked Gaku-san{p}\ \ ...if I can do that by myself. 」"
    "{size=+15}D I R E C T !{size=-15}{p}How can he talk to a relative like\nthat without hesitation?"
    "But wait a minute, Shun-kun talked\nto me first about his stiffening penis,\nthere was no chance for Gaku-san up to now..."
    
    show su 011 big night with dis
    
    su "「\"You can now,\" he said.{p}\ \ Then he gladly did it for me. 」"
    fn "「A-and what you learned from me...? 」"
    
    show su 020 big night with dis
    
    su "「Even though we did that...\n\ \ I never told Gaku-san about when you stayed over!{p}\ \ {nw}"
    show su 018 big night with dis
    extend "It's embarrassing, and our secret... 」"
    fn "「Y-yeah, it is. 」"
    
    show su 022 big night with dis
    
    su "「Then... he taught me the sort of things...\n\ \ you do together with your lover. 」"
    "!"
    
    show su 019 big night with dis
    
    su "「I love you...{p}\ \ and you said you love me too, so...{p}\ \ we are lovers, aren't we? 」"
    fn "「Th-that's right. 」"
    "Apparently he seems to understand\nthe special nuance of \"love\"."
    
    show su 017 big night with dis
    
    su "「S-so... if you're getting hard...{p}\ \ you want do that together... 」"
    "Aaaaaah.{p}I let him say too much. I'm really regretting it.{p}As expected, this is too obscene."
    "...but from what I'm hearing from Shun-kun,\nit seems {w=.2}「two people standing next\nto each other and doing it alone 」"
    
    pause .2
    
    "is what he recognizes as a sexual act\nbetween two lovers."
    "Well, he's not wrong, but..."
    "The lower part of my body is thinking\nof seeking a deeper stimulus.{p}I've been throbbing in my clothes for a while now."
    fn "「U-um, Shun-kun...{p}\ \ Will you do that dirty thing that lovers do with me? 」"
    
    show su 019 big night with dis
    
    su "「Y-yes... 」"
    fn "「You know what I taught you the other day,\n\ \ ...and a few other things after that.{p}\ \ So this is next in the order of things. 」"
    
    pause 1  
  
    $ event_name = _("In Order")

    play sound musi2 loop 
    
    fn "「Umm... first, I think we kiss. 」"
    
    show su 020 big night with dis
    
    su "「A kiss, huh... 」"
    "A feeling of embarrassment more intense than\nwhen I  made him open his legs the other day\nruns through my body."
    "We both fall silent for a short moment."
    
    show su 022 big night with dis
    
    su "「Umm, who should do it...? 」"
    fn "「Oh, yeah, err, how about me? 」"
    
    show su 019 big night with dis
    
    su "「O-okay... 」"
    "He nods his head and looks around nervously\nat the small space between us."
    "Then he readies himself,\n{nw}"
    show su 017 big night with dis
    extend "and closes his eyes.{p}His flushed cheeks are lovely... but."
    fn "「Shun-kun?{p}\ \ You don't need close your eyes so tightly.{p}\ \ Also... you don't need to stop breathing. 」"
    
    show su 018 big night with dis
    
    su "「Hafu. 」"
    
    show su 019 big night with dis
    
    "He opens his big, round eyes\nand inhales deeply with his mouth."
    su "「R-really? Hafu. 」"
    fn "「Yeah,{w} I feel embarrassed seeing them closed\n\ \ so tightly. And you should breath normally. 」"
    
    show su 022 big night with dis
    
    su "「O-okay... 」"
    "Once again, Shun-kun gets in his standby stance.{p}Has he gotten more tense than he was earlier?"
    "There's no need for him\nto stiffen his shoulders so much."
    fn "「Alright, I'm kissing. 」"
    "With my sincere proclamation,\nShun-kun nods sincerely in return."
    "After brushing one finger on Shun-kun's cheek\nin place of a signal, I put my mouth against his,{w=.2}\ngently,{w=.2} to prevent scaring him. "
    
    show su 017 big night with dis
    
    su "「Mm... 」"
    "My lips receive a ticklish feeling\ndifferent from fur."
    "It's a little cold compared to his cheek\nI felt with my finger."
    "After lightly stroking the surface with my tongue,{p}we separate our mouths."
    
    show su 018 big night with dis
    
    su "「...H-hawah... 」"
    "His expression has a look of sorrow,\nand a mix of unrest and excitement."
    "Ooh, that has fierce destructive power.{p}I want to switch places and be on top."
    
    show su 019 big night with dis
    
    su "「M-my heart was really pounding... 」"
    fn "「Mine too. It's the first time\n\ \ I've felt like that. 」"
    
    show su 022 big night with dis
    
    su "「So that was a kiss... 」"
    fn "「Yep. Although they can get even more... intense. 」"
    
    show su 018 big night with dis
    
    su "「What!?{w=.2} Anymore than that and I'll break... 」"
    "Whether he has no tolerance or is sensitive,\nShun-kun tightly clenched fist presses\ndown on his chest."
    "I could also say that my heart\nhas been beating loudly for a while."
    "When I pat his frightened head and calm him down,{p}I suddenly notice the discomfort below my waist."
    "Well, that's been on the verge\nof exploding for a while now."
    "It's tight on the other side.{p}In other words, Shun-kun is the same.{p}I see a mass growing beneath his clothes."
    fn "「Hm? Are you getting big too? 」"
    
    show su 022 big night with dis
    
    su "「Woof... that kiss was really... 」"
    fn "「Does it ache? 」"
    
    show su 017 big night with dis
    
    su "「Yes... Nnn. 」"
    fn "「Well then... let's undress. 」"
    
    $ event_name = _("The Woods and the Naked Body")
    
    show su 022 big night with dis
    
    "The forest air and our body temperatures\nwill be alright even though we are going\nto take off our clothes."
    "I stand up together with Shun-kun,\nand take off my shirt cheerfully."
    "While turning bright red,{p}{nw}"
    show su 119 big night with dis 
    extend "he imitates me and hangs his hoodie on his arm."
    "I have already seen his\nnaked upper body many times before.{p}The color border on his side is very attractive."
    fn "「That reminds me. 」"
    
    show su 101 big night with dis
    
    su "「What? 」"
    fn "「The other day you were completely nude,\n\ \ but I was still wearing clothes, wasn't I?{p}\ \ Was that unfair? 」"
    "I joke around while talking to him."
    
    show su 105 big night with dis
    
    su "「I was the one being taught then...{p}\ \ so how was that unfair? 」"
    "Even though I'm just messing with him,\nit's nice of him to give an innocent reply."
    fn "「I see. This time it's different, isn't it...{p}\ \ I won't be one-sidedly teaching you,\n\ \ we'll feeling good together. 」"
    
    show su 117 big night with dis
    
    su "「Unyuu... Hafu, okay. 」"
    "He's being shy.{w} It's so cute."
    fn "「Alright, I'll start. 」"
    "I still feel embarrassed doing this outside,\nbut because of my seething lust,\nI won't stop myself."
    "I expose myself to the one I love...\nwhich also arouses me."
    "I remove my shoes, and pull my feet\nout from my pants and underwear.{p}My whole body feels the open air."
    
    show su 122 big night with dis
    
    su "「Fwah... 」"
    "As most would expect, my easily brandished organ\nstands tall with its surface area increasing,{p}throbbing and trembling."
    "It seems to breathe and fully taste the summer night air."
    "I try to make a poetic expression,\nbut Shun-kun is considerably frightened.{p}Aaaah~."
    fn "「Uh, yeah. 」"
    
    show su 119 big night with dis
    
    su "「[fn]-san, it's big... 」"
    "He's probably comparing it to his own,{p}but that size ratio is to be expected\nwith our differences in build."
    "In other words, when he pointed out that it's \"big\",\nit doesn't mean I'm above average,\nso it's not really a compliment."
    "But it's still nice in a sad way."
    fn "「Hey, you too. 」"
    "While he's fascinated by my club,\nand bent on making distinctions,\nI urge him to hurry up and show his weapon as well."
    
    show su 111 big night with dis
    
    su "「Okay... 」"
    "With light beige cheeks stained with pink,{p}he slowly takes off the clothes covering{p}the lower-half of his body."
    "His shoes,{nw}"
    hide su
    show su 222 night at center 
    with wipe_down_slow
    extend " then his pants.{p}He's in his familiar briefs."
    "And then..."

    show su 122 night with wipe_down_slow
    
    "A brand-new Shun-kun stands before me.{p}He has a slender body and thin limbs.{p}It's the same as the last time I saw him on his bed."
    "And stretching itself up with all its might\nis Shun-kun's male organ.{w} It stands between\nhis legs, twitching and trembling."
    "The tip is wrapped in skin,and appears to be just\na touch wider than the last time I saw it."
    fn "「You're so cute.{p}\ \ Now then... 」"
    
    show su 117 night with dis
    
    su "「W-woah, wait... 」"
    fn "「...what? 」"
    
    show su 111 night with dis
    
    su "「I-I can't... not outside... 」"
    "Hiding the area between his legs with his hands,{p}Shun-kun complains in a faint voice.{p}...even if he says that now."
    su "「We're on the ground...{p}\ \ We'll get dirty if we sit down. 」"
    fn "「The grass is soft, so it won't hurt your skin.{p}\ \ And it's not damp, so you won't get wet either.{p}\ \ If you're that worried about it... 」"
    "I spread out the shirt and pants I was wearing\nearlier on the ground."
    
    show su 105 night with dis
    
    su "「! 」"
    fn "「Will this work... in place of carpet?{p}\ \ Hahaha, it's kind of small,\n\ \ just enough for us to sit on, right? 」"
    "I encourage Shun-kun, who seems sorry.{p}He sits his butt on my shirt."
    "I get on the ground on both knees,\nand stand opposite to him."      
    su "「[fn]-san, are you sure about this? 」"
    fn "「I'm alright with it, so it's fine. 」"
    
    show su 101 night with dis
    
    su "「Okay. 」"
    fn "「...do you still not like being outside? 」"
    
    show su 118 night with dis
    
    su "「Woof, Wh-what if somebody shows up... 」"
    fn "「Have you ever seen anybody when you came here? 」"
    
    show su 116 night with dis
    
    "He shakes his head."
    fn "「So it's okay.{p}\ \ There aren't even any paths around here.{p}\ \ and we're surrounded by trees too. 」"
    "This is the perfect spot!"
    
    show su 120 night with dis
    
    su "「Uu... 」"
    fn "「Besides, I want you now.{p}\ \ I'm sorry, okay? But I can't wait any longer,\n\ \ seeing your cute penis. 」"
    
    show su 111 night with dis
    
    su "「Y-you're embarrassing me... [fn]-san. 」"
    fn "「So, are you ready? 」"
    
    show su 117 night with dis
    
    su "「...Uu... Yes...{w} B-but next time,\n\ \ we're doing it in your house, okay...? 」"
    fn "「Thinking about where we're doing it next,{p}\ \ that's awfully dirty of you, isn't it? 」"
    
    show su 120 night with dis
    
    su "「!{w=.2} Ooh!{p}\ \ [fn]-san! 」"
    
    scene black with rotation

    $ event_name = _("Unsealing")

    scene forest01 night with rotation    
    show su 120 big night at center_big with sdis
    
    fn "「Nnn... 」"
    "Even though I told him he didn't have to,\nShun-kun has me in his mouth this time\nto reciprocate for the other day."
    "I give in to his awkward movements,\nand relish the sensation."
    "On the other end, Shun-kun makes sure\nnot to hit me with his fangs, and licks\nthe warm stiffness in his mouth."
    "When he rolls it on his fleshy tongue,\nthe pleasure blows away my awareness."
    "With my legs opened, his face is buried in my crotch.\nOccasionally he looks up to examine me.\nThe slurping noises he makes are too obscene."
    fn "「Shun-kun... that feels so good... 」"
    
    show su 117 big night with dis
    
    su "「Mmm. 」"
    "When it's in his mouth, he doesn't need to answer.{p}Instead, he communicates by sucking harder."
    "The hot breaths from his muzzle\nduring breaks dampens my groin."
    "His ears twitch when I provoke them between\nmy fingers, and his head shakes lightly\nwhen I tickle them."
    "Although I see that he's not shaking me off,{p}he probably feels it."
    "My naked childhood friend...{p}I'm teaching this wolf about sexual pleasure\nunknown to him at the beginning of the summer."
    "In a way, I'm making him serve me.\nAfter he consented, a feeling of guilt\ntorments me despite our loving relationship."
    "With the upper half of his body lowered,\nhis tail and butt are raised high,\nand under that he is unable to hide his excitement."
    "Ooh, this is too good. While a good portion\nof my thoughts are taken away by pleasure,\nI'm still feeling regret and try to pull him away."
    "At this rate I'm going to make him drink my...\nit's still too soon."
    fn "「Th-that's enough... Shun-kun. 」"
    
    show su 119 big night with dis
    
    su "「Fuwah...{p}\ \ Whew, [fn]-san... 」"
    "A thread of saliva is made between my penis\nand Shun-kun's muzzle from my hasty action."
    
    hide su
    show su 103 night at center
    with dis
    
    su "「Uu... it's salty. 」"
    "Did it not bother him that much\nwhen he was licking it?"
    "His face distorts in discomfort\nwhen he separates from what was in his mouth."
    fn "「S-sorry. 」"
    "I put my lips to his muzzle.{p}He closes his eyes as peacefully\nas the last time we kissed."
    "Heheheh, how about this?{p}I slowly insert my tongue."
    
    show su 104 night with dis
    
    su "「!{w=.2}　{nw}"
    show su 116 night with dis 
    extend "Mm... 」"
    "Instantly he opens his eyes in surprise,\nbut surrenders himself\nto pleasure a few seconds later."
    "I also thoroughly enjoy the softness inside\nwith my tongue, and, under the influence\nof my forwardness, kiss deeper."
    fn "「Pwahh. 」"
    
    show su 120 night with dis
    
    su "「Mmg. 」"
    "The thread connecting us reflects\nin the moon and shines."
    
    show su 119 night with dis
    
    fn "「...you're saltier than I am. 」"
    su "「R-really?... Unyu. 」"
    fn "「I wonder if I like kissing like that more?{p}\ \ It feels like we were connecting. 」"
    
    show su 117 night with dis
    
    su "「It's embarrassing...{p}\ \ Your tongue filled up my mouth... 」"
    fn "「You didn't like it? 」"
    
    show su 122 night with dis
    
    su "「I didn't hate it, but... 」"
    
    show su 119 night with dis
    
    su "「...your white stuff...\n\ \ even though it didn't come out,\n\ \ you stopped half-way. 」"
    
    show su 122 night with dis
    
    su "「Did that not feel good...? 」"
    "Aaah.{p}Please don't say lewd things with such big,\nround eyes. His upward glance is too much."
    fn "「Uum, that's not it.{p}\ \ I thought of a... different way to do it. 」"
    
    show su 104 night with dis
    
    su "「Different?{p}\ \ ...with, my hand? 」"
    "Nonono.{p}Although it is very hard to cast aside\nthose tiny fingers.{w} Yep.{w} Well."
    "Is it because it's summer?{p}Or is it because we're outside?"
    "The forest's unique atmosphere in which I lay\neverything bare tempts me into exceedingly\nbolder acts."
    "Even though I stopped him from swallowing earlier,\nmy brain from which such conclusions come from\nis a flower garden.{w} Yessss."
    fn "「I want us to both feel good together. 」"
    
    show su 122 night with dis
    
    su "「A-alright. 」"
    fn "「Can you turn your back towards me a little? 」"
    
    show su 119 night with dis
    
    su "「Okay. 」"

    hide su with dis
    
    "Remaining on all fours, he turns around halfway.{p}His shaft droops a little and his balls shake.{p}I stand before his butt and tail."
    fn "「If it hurts or feels weird,\ntell me, okay?{w} I'll stop... 」"
    "I say that common line.{p}Actually, it depends on the morals of the person\nin question on whether or not I'll stop."
    "I guess I'll try my hardest to."
    su "「Wh-what are you doing? 」"
    fn "「Hmm... wait a minute. 」"
    "I control him while he speaks in a surprised voice.\nI pull lotion out of my small messenger-type bag."
    "My excuse for the time being is that it\nwasn't originally mine. For example,\nit was with those supplies Gaku-san gave me."
    "At first I thought it was one of those ready-made\nmeal seasoning pouches, set it on the dining table,\nbut removed it hurriedly when I realized what it was."
    "I noticed it earlier even though I had just thrust\nit into my bag."
    "Let me stress that this doesn't mean I normally\ncarry it around, dreaming of whether or not\nI'll have this chance."
    "For it to be useful now is just\nthe luckiest of coincidences.{p}Thank you, Gaku-san."
    "Dribble.{p}I break the seal and drip some on my fingertip."
    "It's colder than I expected,\nso I roll it around to heat it up."
    fn "「Now then, I'm touching it... 」"
    
    show su 119 night at center with dis
    
    su "「Okay...{nw}"
    show su 117 night with dis
    extend " {cps=10}{size=+15} FunyAAaaaah!? 」"
    "I wrap my fingers coated with the slimy half-liquid\naround Shun-kun's sensitive shaft.{w} Right as I do\nthat, he yelps and his body trembles in surprise."
    su "「Nnn!{w=.2} Yah!{w=.2} [fn]-{w=.2} ah,{w=.2} san. 」"
    "A lewd, sloppy noise is made as I stroke it."
    "I scoop up the lubricant that runs down to his\nsack without leaving any behind and massage\nit on to the tip, neck, base, and 2 balls."
    
    show su 122 night with dis
    
    su "「Haah! No,{w=.2} that's too much... 」"
    "I stop caressing Shun-kun and gently speak\nto him as he's roughly breathing."
    fn "「Was I going to hard...?{p}\ \ But it felt nice, didn't it? 」"
    "Shun-kun's slippery shaft has risen to the point\nwhere it looks as if it could touch his stomach.{p}The dripping fur at the base is erotic."
    
    show su 120 night with dis
    
    su "「I don't like it, please go slower... 」"
    "Even though he's complaining, his waist shakes back\nand forth wistfully and his tail is off to the side\nso that it's not covering his secret part."
    "By seeing this it's clear that his body\nis urging me to continue."
    fn "「Heheh, alright.{p}\ \ Slower, slower... 」"
    "Muttering that like an incantation,\nI resume the movement of my fingers."
    "I cut down on the speed as he asked,\nand keep smearing lotion on his shaft."
    su "「Fu, fuuu, nnn... 」"
    
    show su 111 night with dis
    
    fn "「Which feels better, this or my mouth? 」"
    
    show su 117 night with dis
    
    su "「I-I don't kn-... Hau, Nnng! 」"
    "His young male organ already seems\nto be at its limit from the attack\nof the stimulating fluid."
    "It trembles, waiting impatiently for the climax,\nand his balls are lifted up as well."
    "At that point, I release my fingers."
    "With his shaft on the brink of losing control\nand releasing, he learns of the intolerable sense\nof discomfort of the heat building up."
    "A liquid different from the lotion\nflows from his glans."
    "It overflows from the tip that hasn't been peeled\ndown yet and runs down thickly onto my shirt."
    
    show su 122 night with dis
    
    su "「Fu, Fuu, why... 」"
    "Shun-kun complains about being brought to his limit."
    fn "「Didn't we decide to feel good together?{p}\ \ I still... haven't got to yet. 」"
    
    show su 117 night with dis
    
    su "「B-but, I... 」"
    fn "「It's okay. You'll get to cum soon. 」"
    "While calming him down as he talks in a sad voice,\nI start to prepare for what's next.{p}I'm also getting close to my limit."
    
    $ event_name = _("Union")
    
    show su 122 night with dis
    
    su "「Wh-whaa... that's... 」"
    "Once again I squeeze out the lotion on to my hand\nwhile looking at Shun-kun, and continue."
    fn "「Won't you be more comfortable\n\ \ doing it when it's slippery like this? 」"
    
    show su 119 night with dis
    
    su "「Y-yeah... 」"
    fn "「I feel it too... 」"
    "As I say that, I gently apply my finger\nto the hole leading to the secret\ninner part at the base of his tail."
    
    show su 117 night with dis
    
    su "{size=+15}]Fyuun!{size=40}{w=.2}　Th-that's my butt... 」"
    fn "「That's right. This is an erotic spot too,\n\ \ didn't you know that? 」"
    
    show su 122 night with dis
    
    su "「Not there... 」"
    fn "「Nn... but I want us to feel good together. 」"
    "Halfway through my sentence,\nmy index finger slides in."
    
    show su 117 night at briefzoom
    pause .2
    
    su "「Yah... [fn]-{w=.2}san... Guh. 」"
    "Although the entrance has firmly narrowed,\nthanks to the lotion it doesn't take much\neffort to get it in up to the 1st joint."
    fn "「Woah... it's tight. 」"
    su "「Kyan... Fuu... 」"
    "Without moving, I check on Shun-kun."
    fn "「Shun-kun, does it hurt? 」"
    
    show su 122 night with dis
    
    su "「It's tense... unng, [fn]-san. 」"
    fn "「Relax, it'll be easier that way. 」"
    "He is completely frightened and has gone soft.\nI gently put my hand on his penis."
    
    show su 119 night with dis
    
    su "「Fu, fuwah... yah, Nn. 」"
    "I continue giving him a light intermittent\nstimulus so his body won't tense up."
    "Has he gradually begun to give himself in to pleasure,\nor has he gotten used to the feeling\nof this foreign substance?"
    "The clamping in his behind\nhas gotten looser as well."
    "I pick the right time to push my finger in little by little."
    
    show su 122 night with dis
    
    su "「Nn... [fn]-san, haau. 」"
    fn "「Does it hurt...? 」"
    
    show su 120 night with dis
    
    su "「It feels weird... Nn. 」"
    "There's plenty of lotion.{p}My finger creeps in at a slow speed."
    
    show su 117 night with dis
    
    su "「I-I'm doing this...\n\ \ just for you... Nnn. 」"
    "Even so, he's blushing to the fullest,\nand opens his body only to me."
    "All of him becomes narrower to allow{p}me to penetrate him."
    fn "「Shun-kun... You're so cute.{p}\ \ I'm doing this just for you too... 」"
    "My index finger completely enters."
    
    show su 119 night with dis
    
    su "「F-fwaah... 」"
    fn "「How does it feel? 」"
    
    show su 118 night with dis
    
    su "「Nn...{w=.2} Nng...{w=.2} It's weird... 」"
    "When I move my finger about and play around,\nShun-kun lets out an exceptionally sweet voice.{p}Yep, he seems to feel it."
    "Without change, I do it as slow as possible.{p}I insert a second, then a third finger."
    "My dominant hand continues\nto caress his shaft and balls,\nbut I do it in moderation so he won't cum."
    "Shun-kun is enveloped in the previous\nsexual feeling from behind."
    
    show su 111 night with dis
    
    su "「Nng, fuu- more... nnn. 」"
    "Then, unable stand it any longer, he begins to heavily pant.{p}Up to their base, my three fingers settle into his hole."
    fn "「Shun-kun... Are you okay? 」"
    
    show su 117 night with dis
    
    su "「Nn... yeah... 」"
    "I think I've got him loosened up, as I can move my fingers around.{p}First, I pull them out."
    
    show su 120 night with dis
    
    su "「Wahn! 」"
    "It's larger than it was at first, and fluid drips down.{p}The entrance twitches with desire."
    
    show su 122 night with dis
    
    su "「Haah...Haah... [fn]-san, are you done...? 」"
    "His teary eyes appealing to me are oppressive.{p}He's in a state as if he's begging for forgiveness."
    "My feelings of guilt are inversely proportional to my\nwarped lust."
    fn "「Shun-kun...Um, here...{p}\ \ I want to put mine in... 」"
    
    show su 119 night with dis
    
    su "「Huh...? 」"
    "He doesn't get what I'm saying,{p}even when I show him with a gesture."
    "Did he take my feelings into consideration?{p}Or can he not assume it as anything\nother than the situation?"
    "While he did seem to understand \"here\" and \"mine\",{p}he answered in a small voice, looking down."
    
    show su 122 night with dis
    
    su "「...I-I'm scared...{p}\ \ {nw}"
    show su 107 night with dis
    extend "But, I'll do it for you.{p}\ \ Because I love you... 」"
    "Kyuun."
    
    show su 111 night with dis
    
    su "「P-please be gentle, okay...? 」"
    
    show su 117 night with dis
    
    "Without another word, he squeezes his eyes shut\nand assumes a recieving posture,\nlike when we first kissed."
    "On all fours, his back shakes."
    fn "「Y-yeah... 」"
    "In the place that he has not used\nfor something like this up to this point,"
    "he allowed me to penetrate it with 3 fingers,\nand now I'll try to put in my risen self."
    "There's no reason to be scared.{p}Because there's no reason to become scared."
    "Still, because he loves me, we have come\nto an understanding through that feeling.{p}He reveals the part of him he's embarrassed about."
    "...We are lovers, so we want to feel good together.{p}Perhaps that's a little simplistic."
    "I should have exercised a little more tact.{p}When I say that, we should have quickly{p}returned for the day."
    "..."
    "It's no use.{w} Saliva and another\nbodily fluid are dripping from him.{p}I can't stand it any longer."
    fn "「Alright then, I'm going in... 」"
    su "「Okay... 」"
    "I touch it so that the tip becomes narrower.{p}Then I just push it as is."
    "Although there is some resistance,{p}it goes in thanks to when I loosened it up."
    "The head goes in with one go."
    
    show su 122 night at briefzoom
    pause .2
    
    su "「...Nn!! 」"
    fn "「Woah... 」"
    "It's hot. I'm being squeezed tightly.{p}I can feel his insides more\ndistinctly than with my fingers."
    
    show su 117 night with dis
    
    su "「[fn]-saaan... 」"
    "A voice that seems painful leaks out.{p}I reach out to his drooping shaft\nand slowly caress it at the same time."
    
    show su 111 night with dis
    
    su "「Fuu, Hau, nn... 」"
    "The short and quick rhythm matches Shun-kun's sighs.{p}I push my waist forward little by little.{p}Over time I'm able to get in all the way to the base."
    
    stop sound fadeout 1    
    scene ev_shun_2a with sdis
    
    su "「Ah... Kuh... 」"
    fn "「Look, I'm all the way in... see? 」"
    "His tail tickles my navel.{p}My oversensitive ball sack touches his ass,\nand I can even feel the tips of his fur."
    su "「Y... yes... 」"
    fn "「I'll go slow. 」"
    "While playing with the sensitive front,\nI urge him to relax."
    "After I don't move for a while and\nhe has gotten used to me,\nI pull my hips halfway and start to come out."
    su "「Hafu, Kuu!{w=.2} Ahn... Aaaah... 」"
    "Shun-kun's body becomes stiff,\nthen gradually relaxes and gets ready\nto accept me..."
    "Woah, the tightness weakened and a great amount\nof heat is coming from it."
    "I mean... I want to thrust my hips.\nI can't stand this rigidness since I went in.\nN-no more...!"
    fn "「T-tell me if it hurts, okay... 」"
    su "「Fuwah, okay... wah, fwaaaaaah! 」"
    "I give a deep thrust, and slip into him."
    "The feel of warm, soft flesh covers the entire hole.{p}In an instant I lose my sense of awareness.{p}I involuntarily start panting."
    fn "「Uwahh... 」"
    su "「Fuu, fwah, fuu, fu... 」"
    "Shun-kun's breathing quickens to the rhythm.{p}Aah, I'm inside him now..."
    fn "「I'm thrusting, okay? 」"
    su "「Fuu, fu... Hwaaah! 」"
    "I pull up without waiting\nfor an answer and push in again."
    fn "「Ah, Aaaaah! 」"
    su "「[fn]-sa-, Nn... HyaAAAaann!! 」"
    "The slopping sound of the lotion\nand our fluid echoes."
    "At fixed intervals,\nhis tail and my stomach touch.{p}Our ball sacks strike against each other."
    fn "「Kuh, uuh, aah...! 」"
    su "「[fn]-sa-, [fn]-saaan... Kuuh, haah. 」"
    "His shaft convulses in my hand.{p}The internal stimulation tightens,\nwraps around me, then tightens again."
    "This feels so good...!{p}I'm connected to Shun-kun...!"
    "He calls out pieces of my name.{p}Fluid oozes out of his tip\nand is massaged onto my skin."
    "He holds me in his ass and pants."
    su "「Nnn, [fn]-san... Ahn, aah. 」"
    "S-so cute... It's so dirty, yet adorable.{p}I think he has probably become disoriented\nbecause of me, and this excites me even more."
    "I stop moving my waist to fully enjoy the inside.{p}His shaft is {cps=10}getting to its limit.{p}I am too..."
    fn "「Aah!{w=.2} Shun-kun!{w=.2} I, I'm cumming!! 」"
    su "「Fwaahn!{w=.2} [fn]-saaan!{w=.2} Me too... Nnah! 」"

    scene white with dis
    scene ev_shun_2b with dis
    
    "I thrust into the inner most part\nand spit out my built-up lust."
    "I tremble profusely and mercilessly\npump an unprecedented amount."
    "A white feeling of pleasure shoots through the head.{p}Shun-kun also cries out in a sweet voice and\nejaculates in my hand."
    "His insides that contract to his discharge\nstimulates me further."
    "I entrust my stiffness to the squeezing\nand repeated spasms."
    "...finished releasing,\nI pull my flaccid self out with satisfaction."
    "Then, I embrace Shun-kun and collapse to the ground."
    
    scene black with sdis 
    
    if persistent.replay == True:
        $ renpy.end_replay()
        
    $ persistent.event_shun2 = True    

    $ event_name = _("On the Way Back")

    scene path night with sdis
    play sound night_insects loop
    
    "The days of summer are long."
    "Even though my hunger is a sign that it's time for\ndinner, it's still relatively bright around here."
    
    show su 010 night with sdis
    
    su "「... 」"
    fn "「... 」"
    "Shun-kun and I drag our exhausted and spent bodies\nalong, and make our way out of Minasato's forest."
    "Ugh, my back hurts."
    "Shun-kun recovers faster than me. I'd like to think\nit's because of the difference in our diets and daily\nlife, not the problems of being a top or bottom."
    fn "「We should be getting\n\ \ to your grandfather's house soon, right? 」"
    su "「Yeah... 」"
    fn "「They're probably worried,\n\ \ so we should make an appearance. 」"
    su "「Okay... 」"
    "Walking without looking up,\nShun-kun says nothing but a reply."
    "Having left his house without telling anybody,\nhis grandfather is probably going to be angry."
    "It's good that he made up his mind to talk about\nreconciliating, but before that he's more scared\nabout being scolded about today's incident."
    "I don't know what to say either,\nand just keep walking next to him."
    "S-still, coming back from the forest first and\ntalking to the Kodori family after calming them down,"
    "Would the person who caressed the lower part\nof Shun-kun's body be wanted?"
    "Rather, before or after aren't the problem.{p}Aah, maybe I shouldn't have gotten involved\nin this situation."
    "No, those actions were to calm Shun-kun's heart!\nWe're mutually in love!{w=.2}\nAnd we also did some things!"
    "...no.{p}No matter how I look at it,\nit might have been rash of me."
    "I'm caught up in a sea of thoughts again.{p}When we turn this corner, we'll be in front\nof his grandfather's house."
    fn "「Ah... 」!"
    
    stop sound fadeout 1    
    play music ambience01
    $ renpy.music.set_volume(0.8, 0.0, channel = "music")
    
    "!?{w=.2}\nWha-, ah!?"
    "Somebody is pressing down on my mouth from behind!{p}Ah, ah, my arms are being bound from behind\nand I can't move..."
    "Shun-kun is too occupied to notice\nthat I stopped walking.{p}Aah, he's gone..."

    hide su with dis
    
    who "「[fn]-san, be quiet and let Shun go. 」"
    fn "「!? 」"
    "Gaku-san!?{p}Wh-what is he doing here!?{p}And why is he targeting me!?"
    
    stop music fadeout 1
    scene old_house1 night with wipe_right    
    play music piano3_014
    $ renpy.music.set_volume(0.8, 0.0, channel = "music")
    
    who "「Shun! 」"
    su "「Iwao-sama... 」"
    "On the other side of the corner,\nI hear an unknown voice.{p}...It's Shun-kun's grandfather."
    gk "「Keep quiet. 」"
    "Gaku-san undoes his restrain when he repeats himself.{p}I stand at the edge in a way to not stand out,\nand peek around the corner."
    "My waist is sore, so I crouch down in place.{p}I observe the situation for now."
    "They're at the front door, and it seems\nboth of them are having a conversation."
    "...There aren't any angry voices or screaming,\nso I'm relieved for the time being."
    "Ah, they're tightly hugging each other."

    show gk 002 night at farright with dis
    
    gk "「To leave Minasato without telling anyone,\n\ \ were you worrying about the ceremony that much? 」"
    
    show gk 001 night with dis
    
    gk "「I-I'm different, because I'm not reliable... 」"
    
    show gk 002 night with dis
    
    gk "「There was no ill-will towards you in my intentions.{p}\ \ But there were times when I said too much.{p}\ \ That was inexcusable of me. 」"
    
    show gk 001 night with dis
    
    gk "「Iwao-sama... Hmm.{p}\ \ I can only say that I'm selfish too.{p}\ \ Sorry for making you worry. 」"
    
    show gk 002 night with dis
    
    gk "「I'm glad you came back safely.{p}\ \ I'm sorry. I would like to start\n\ \ talking with you again. 」"
    
    show gk 001 night with dis
    
    gk "「...I'm assuming that's what they're saying. 」"
    "Is he impersonating Shun-kun and his\ngrandfather now?"
    
    show gk 003 night with dis
    
    gk "「This is too much trouble. 」"
    gk "「He was a foolish grandchild after all.{p}\ \ As soon as you disappeared, he became meek-looking. 」"
    
    show gk 005 night with dis
    
    gk "「He hasn't been coming and going to Minasato\n\ \ as he pleases until now.{p}\ \ That in itself is a shock. 」"
    "...Is he really talking about somebody\nother than Gaku-san?"
    
    show gk 001 night with dis
    
    gk "「He scoured the village for you in a great fuss.{p}\ \ I shouldn't have been so strict if you were\n\ \ that important to him. 」"
    
    show gk 004 night with dis
    
    gk "「Well, it's okay now.{p}\ \ You were safe. 」"
    fn "「Um, Gaku-san, you were looking for Shun-kun too? 」"
    
    show gk 001 night with dis
    
    gk "「No, I knew Shun would be at that place.{p}\ \ So I went to check. 」"
    gk "「Then,{nw}"
    show gk 002 night with dis
    extend " it was just as I had suspected. 」"
    fn "「!!? 」"
    "Did he see us?"
    
    show gk 001 night with dis
    
    gk "「Because of that, I left the forest\n\ \ and returned to Minasato.{p}\ \ One step ahead. 」"
    fn "「I-I see... 」"
    "D-did he see what we were doing...?"
    gk "「I told his parents that he just went out\n\ \ to play with his friends and he'll be home soon. 」"
    gk "「The old family seemed to have got in contact\n\ \ from there, and Iwao-san has been waiting\n\ \ at the entrance the whole time. 」"
    gk "「It looks like he's fallen for you.{p}\ \ At the festival he wanted to be together\n\ \ with his partner. 」"
    
    show gk 002 night with dis
    
    gk "「And then he went and eloped with that guy. 」"
    fn "「Th-that's a weird thing to say! 」"
    
    show gk 001 night with dis
    
    gk "「I'll reflect on this so that I can turn\n\ \ over a new leaf. Was it hard for you? I'm sorry."
    gk "「I'll start showing a more forgiving\n\ \ attitude towards Shun. 」"
    
    show gk 003 night with dis
    
    gk "「Well, my true intention is that I only\n\ \ want Shun to stay connected to Minasato. 」"
    fn "「Gaku-san... 」"
    gk "「This is too much trouble. 」"
    su "「[fn]-saaan!{w=.2} Where are you? 」"
    
    show gk 001 night with dis
    
    gk "「Look, Shun is calling for you.{p}\ \ Aren't you going to feed him?{p}\ \ {nw}"
    show gk 002 night with dis
    extend "...or a bath first? 」"
    fn "「Uh, um, if it comes to that\n\ \ I'll politely refuse and go home... 」"
    "I still can't face his grandfather..."
    
    show gk 001 night with dis
    
    gk "「Bye then, take care of Shun. 」"

    hide gk with dis
    
    "Needing to say no more, Gaku-san has left.{p}In the end he came back without meeting\nShun-kun and his grandfather."
    
    stop music fadeout 1
    pause 1
    scene path night with wipe_right    
    show su 002 night at center with dis    
    play music pops_003
    $ renpy.music.set_volume(0.8, 0.0, channel = "music")
    
    su "「[fn]-san! 」"
    "His whole face is smiling.{p}Having completely come out from being upset,\nhe's smiling with all he can."
    "When I first came back to Minasato,\nthis was expression I saw on his face..."
    
    show su 001 night with dis
    
    su "「Um, Iwao-sama said he hasn't eaten dinner yet. 」"
    "Ah, no, that's not it.{p}That face...{w=.2} it was 5 years ago."
    "When I went to play with him\nhe would smile like that."
    
    show su tailwag 01 night with dis
    
    su "「I want to introduce you to Iwao-sama too. 」"
    "What made Shun-kun forget that extraordinary\nsmile over those 5 years...?{p}Was it my fault...?"
    su "「[fn]-san! 」"
    
    stop music fadeout 2.5

    jump end26

######################################################
label kouya26:
    
    $ event_name = _("Chain Connection")

    play music daily03
    scene studio with dis
    show ke 001 at midright
    show ka 001 at midleft
    show yu 001 at farleft
    show jn 001 at farright
    with dis
    
    "A beautiful melody filled up the area.{p}Keisuke-san's drums,{w=.2} Jun-kun's bass,{w=.2}\nYuuki-san's singing voice. Also,{w=.2} Kouya's guitar."
    "All of that overlapped each other\nand settled into one song.{p}I listened to it, and the mood was great."
    "That's what I felt.{p}All the way,{w=.2} down to the very end."
    "...Kouya's face seemed very low-key today."
    "Today also had a string of repeat performances.{p}Everyone said that it was more 'synthetic'\nthan yesterday's."
    "This time, even I noticed that\nit wasn't really that well-played.{p}The pitch was evidently starting to waver."
    "Yesterday, when Kouya opened up about his impatience,\nit didn't disappear,{w=.2} and instead seemed to\nbecome something that was really bothering him."
    "I could tell how painful it was.{p}And, more than anything,{w=.2}\nI was the most irritated by it."
    "As I quietly kept watching,\nKouya doggedly continued on with the song."
    "I was worried.{w} Yesterday, Kouya said that he'd\nshow me he could get over it.{w} It's not that I\ndidn't have faith in him,{w=.2} but I was concerned."
    "Words of support repeated themselves in my mind,\nfeeling almost like a prayer.{p}That was the only thing I could do."
    
    stop music fadeout 4
    
    "Before long, the end of the song approached.{p}This hope-invoking melody for a lonely future{w=.2}\nleft a drawn out note then faded out."
    "A silence was born.{p}But, it was torn down immediately."
    
    play music shop02
    show ke 004 with dis
    
    ke "「Ah...{p}\ \ Kouyaaa,{w=.2} are you okay...? 」"
    "「You seem worried. You seem out of it, 」 the tone said.{p}「You can always say something,{w=.2}\nwe're here for you, right? 」"
    
    show ka 013 with dis
    
    ka "「Sorry,{w=.2} really. 」"
    "Kouya laughed apologetically as he responded.{p}But, I was able to tell.{w} That laugh was forced."
    "I figured that to begin with,{w=.2}\nI'd go up to Kouya and hand out the drink bottles."

    scene studio with wipe_right
    show ka 001 at center with wipe_right
    
    fn "「Okay,{w=.2} here you go Kouya. 」"
    ka "「Oh,{w=.2} thank you. 」"
    "With that short comment, he took the\nbottle from my hand."
    "For just a second, he looked kind of tired.{p}Since he hasn't been playing up to scratch,{w=.2}\nI think he's getting irritated and getting worse."
    "For now,{w=.2} it might be best to take a break."

    hide ka with wipe_right
    show ke 001 at center 
    show yu 001 at farleft
    show jn 001 at farright
    with wipe_right
    
    fn "「Guys,{w=.2} how about a break?{p}\ \ Now's a pretty good time for one,\n\ \ since you've been going non-stop for a while. 」"
    
    show yu 003 with dis
    
    yu "「Hmm, that's true.{p}\ \ {nw}"
    show yu 001 with dis
    extend "I'm starting to get tired myself,{w=.2}\n\ \ but what do you think, oh Glorious Leader? 」"
    ke "「Huuh.{w=.2} Okay, let's have a break then.{p}\ \ You fine with that, Jun? 」"
    
    show jn 006 with dis
    
    jn "「... 」"
    "Jun-kun gave a sudden nod,\nand it looked like everyone agreed.{p}Everyone sat down on the floor to relax."
    "After I handed out drinks to the other three,{w=.2}\nI returned to my chair over by the wall."
    "Even if it was just a little,\nit'd be great if this improved Kouya's mood..."

    scene studio with dis
    show ke 001 at midright
    show ka 001 at midleft
    show yu 001 at farleft
    show jn 001 at farright
    with dis
    
    ke "「Seriously though,{w=.2} what's up with you Kouya?{p}\ \ {nw}"
    show ke 004 with dis
    extend "You don't seem like yourself. 」"
    
    show yu 003 with dis
    
    yu "「Yeah,{w=.2} something's different.{p}\ \ It feels like you're trying to rush something,{w=.2}\n\ \ but am I imagining things? 」"
    fn "「... 」"
    "For some reason, this conversation's\nmaking me uncomfortable.{w} Keisuke-san and Yuuki-san\nare both saying strangely familiar things."
    "It's like they don't know about Kouya's promise."
    ke "「Yeah,{w=.2} it's like your\n\ \ head's already gone off ahead. 」"
    "...Could that be it?{w=.2}\nThat Kouya hasn't told them about it yet...?"
    "My heart started beating uncomfortably in my chest."
    yu "「I mean, it's true that Keisuke-san and I can't be\n\ \ around here in the next four months, so I can get\n\ \ being impatient because of that... 」"
    yu "「But how about relaxing a bit?\n\ \ Just a bit,{w} {nw}"
    show yu 002 with dis
    extend " Kouya? 」"
    
    show jn 006 with dis
    
    jn "「... 」"
    
    show ke 006 with dis
    
    ke "「Yeah!{w=.2} Just like Jun and Yuuki said.{p}\ \ It's not like the next contest will be the last one. 」"
    
    show ke 008 with dis
    
    ke "「Well,{w=.2} not many go on with\n\ \ this kind of thing in public,{w=.2}\n\ \ but just take a load off for a while- 」"

    play sound standup
    
    "Kouya stood up, interrupting Keisuke-san.{p}Then:"
    ka "「I need to get some fresh air.{p}\ \ ...I'm seriously,{w=.2} seriously sorry. 」"
    
    play sound step03
    show ka at move_offleft_far(1)
    
    "He said that, and quickly left the studio.{p}{nw}"
    play sound door_close
    extend "The door creaked open."
    "All that was left behind was an awkward silence."
    
    scene studio with dis
    show ke 004 at center
    show yu 003 at farleft 
    show jn 003 at farright
    with dis
    
    ke "「...Did I...{w=.2}say something... Wrong? 」"
    "Keisuke-san mumbled in astonishment,{w=.2}\nand the place started moving again."
    "This isn't the time for me to be taken aback, too.{p}I have to run after him-!"
    fn "「Sorry guys, I have to run out for a sec!{p}\ \ I'll be right back! 」"

    show yu at jump_up
    
    yu "「Ah!{w=.2} Wait, [fn]-ku- 」"
    
    play sound step03
    
    "I quickly jabbered without turning my head as I ran.{p}I heard Yuuki-san's voice from behind me,{w=.2}\nbut I didn't have the time to turn to look at him."
    
    play sound door_close
    
    "The door creaked open."

    scene black with wipe_right
    scene studio with wipe_right
    show ke 004 at center
    show yu 003 at farleft
    show jn 001 at farright
    with dis
    
    yu "「-n!{w} Oh, he's gone. 」"
    ke "「Oh man...{p}\ \ Maybe I should go, too...? 」"
    
    show yu 001 with dis
    
    yu "「No,{w=.2} stop.{p}\ \ [fn]-kun probably knew something,{w=.2}\n\ \ which could be related to why Kouya's so wound up. 」"
    
    show jn 006 with dis
    
    jn "「...The next one...{w=.2} might be the last one.{p}\ \ The last contest for Kouya. 」"
    
    show ke 001 with dis
    
    ke "「Jun,{w=.2} did you hear something about this? 」"
    jn "「No.{p}\ \ But somehow, that's the feeling I had.{p}\ \ And what happened just confirmed it. 」"
    
    show jn 001 with dis
    
    jn "「When [fn]-san came over all of a sudden,{w=.2}\n\ \ I thought it was a bit strange. 」"
    jn "「And then when I saw the two of them,{p}\ \ I had that feeling.{w=.2} They weren't calm. 」"
    
    show ke 004 with dis
    
    ke "「Oh...{w} and then I said that there'd be\n\ \ a next time. 」"
    jn "「...Maybe,{w=.2} I think they were worrying about it.{p}\ \ Something must have happened,{w=.2} in Minasato. 」"
    jn "「But we don't need to worry.{p}\ \ 『We are forever with.』{p}\ \ That's what Kouya said.{w} It says this isn't over. 」"
    jn "「So many things and people can be put after 'with.'{p}\ \ And one day,{w=.2} it'll be one word. 」"
    jn "「Kouya helped us all.{p}\ \ That's why he made this word. 」"
    jn "「He felt his friends were the most important thing,{w=.2}\n\ \ more than anything else. 」"
    
    show jn 006 with dis
    
    jn "「But up until now, Kouya couldn't help anybody.{p}\ \ Since he won't say he'll help himself,{w=.2}\n\ \ we didn't notice. 」"
    
    show jn 007 with dis
    
    jn "「However, there's now a person who can help Kouya.{p}\ \ If that person stays near Kouya,{w=.2} it'll be okay.{p}\ \ {nw}"
    show jn 001 with dis
    extend "...Still,{w=.2} I kind of regret it. 」"
    yu "「...Jun,{w=.2} you're unusually talkative today. 」"
    
    show jn 004 with dis
    
    jn "「...Not really. 」"
    
    show ke 003 with dis
    
    ke "「You're so shy, man.{w} {nw}"
    show ke 001 with dis
    extend " But I see...{p}\ \ If it's like that,{w=.2} I guess we need to think up\n\ \ a reprimand instead of an apology, huh. 」"
    
    show ke 006 with dis
    
    ke "「\"We are forever with,\"{w=.2} after all. 」"
    
    stop music fadeout 3
    scene black with sdis 
   
    $ event_name = _("A Complicated Heart")

    scene music_shop night with sdis
    
    "The store interior was completely dark.{p}Since closing time passed a long time ago,{w=.2}\nthe manager was also gone."
    "But right now, none of that mattered to me.{p}Chasing after Kouya was the only thing on my mind.{p}That thought kept circling around inside me."
    
    play sound step03
    
    "I ran past all the instruments around me,{w=.2}\nthen stood in front of the entryway."
    "「Hurry! 」 my feelings urged me on.{p}It should have been a simple thing to turn the key,{w=.2}\nbut it refused to open."
    fn "「...! 」"
    "I bit down on my lower lip,\nand the pain made me calm down.{p}{nw}"
    play sound KeyA
    extend "The lock turned."
    "When I was able to push the door open,{w=.2}\nI suddenly noticed someone's presence to my left.{p}Because of that, I thought to start looking around."
    
    play music sad03 fadein 3
    
    "I slowly turned my head, and there I saw him.\nIt was Kouya, who should have been outside.\n;Why didn't you notice when the door was locked...?"
    "The only lighting in the shop was from the window.{p}From there, the moonlight shone in on the walls."

    show ka 001 night at center with dis
    
    fn "「...{w=.2}Weren't you going out to get some fresh air? 」"
    ka "「...that was a lie. 」"
    "He replied without looking at me in the eye."
    fn "「Everyone's worried. 」"
    ka "「I'm sorry about that. 」"
    fn "「Keisuke-san's kind of overwhelmed. 」"
    ka "「He has his honesty.{p}\ \ {nw}"
    show ka 014 night with dis
    extend "Even though it's my fault. 」"
    fn "「You didn't tell them about the promise, did you. 」"
    "If that's the case,{w=.2} he didn't tell them\nthis could be his last contest."
    
    show ka 001 night with dis
    
    ka "「I wasn't planning on telling them until the end.{p}\ \ Even if I don't do well for now and go home,\n\ \ I don't plan on quitting the guitar. 」"
    ka "「When we started,{w=.2} the four of us,\n\ \ we all decided we'd go through with it.{p}\ \ If any one of us left, it'd be the end of Musikus. 」"
    ka "「That was the promise. 」"
    ka "「That's why I planned on continuing no matter what.{p}\ \ I want to be a member of this band.{p}\ \ I didn't want to make them worry too much. 」"
    ka "「I didn't want to make anyone worry,{w=.2}\n\ \ worry about what would happen if this band split up. 」"
    fn "「Is that why you thought it'd be\n\ \ okay to take all this on yourself? 」"
    ka "「...yeah. 」"
    "Kouya confirmed it in a voice\nthat sounded like it'd go out any second."
    "I feel like I've seen this Kouya before."
    fn "「Right now,{w=.2} what are you thinking about? 」"
    
    show ka 014 night with dis
    
    ka "「...When Keisuke said there'd be a next time,{w=.2}\n\ \ I didn't know what'd happen to me. 」"
    ka "「I don't intend on stopping,{w=.2}\n\ \ but if I couldn't go on...{w} When I thought that,\n\ \ I didn't know what I should do. 」"
    ka "「Keisuke,{w=.2} Yuuki,{w=.2} and even Jun,{w=.2} they all still\n\ \ encouraged me, even after that. 」"
    ka "「I couldn't carry all of this by myself.{p}\ \ Even though you taught me, that night at the river,{w=.2}\n\ \ I made the same mistake again. 」"
    "Kouya spoke in a whisper.{p}His voice was shaking.{p}He really is sorry about it."
    
    show ka 008 night with dis
    
    ka "「And,{w=.2} I should have been\n\ \ able to rely on you more... 」"
    "Kouya cast his eyes down.{p}A single tear ran along his cheek.{p}In this faint moonlight,{w=.2} it reflected a glint."
    fn "「Kouya... 」"
    "Most likely,{w=.2} I think Kouya's started to forget\nthe times he's relied on other people."
    "Kouya, who left home after graduating middle school.{p}Because of a fight,{w=.2} he ran out\nand started living alone."
    "When Kouya was trying to figure out\nhow to live alone, he was desperate."
    "People aren't meant to be independent at 16,\nafter all."
    "During that time, a lot of people must've helped him.{p}People are meant to support each other, I think.{p}Then, somehow, he started trying to fend for himself."
    "After that,{w=.2}\nKouya must have stopped relying on people.\n...He's probably forgotten how to do that, now."
    "That's where I'm guessing it came from,{w=.2}\nthis absolute kindness of his."
    "More than anyone, he hated to see people hurt,{w=.2}\nso if it's for his friends, he'd help\nat the risk of his life."
    "But since he's forgotten how to depend on others,{w=.2}\nI don't know how to best help him.{p}In the end, he's become this awkward."
    "I think his real self is strong.{p}That's why he stood alone.{p}Sadly,{w=.2} that strength became tied to fragility."
    "To me,{w=.2} that's what it felt like."
    "Still,{w=.2} that can be changed bit by bit."
    fn "「It's not the same thing. 」"
    ka "「[fn]...? 」"
    fn "「You didn't make the same mistake.{p}\ \ This time, you didn't notice it yourself. 」"
    fn "「It's different from that time.{p}\ \ Kouya,{w=.2} you already know the best thing\n\ \ to do, don't you? 」"
    "I walked one step closer to him.{p}If I put my hand out,\nI'd be within arm's length of him."
    
    show ka 008 big night with dis
    
    "Since he was leaning his back on the wall,{w=.2}\nhis face was right in front of me."
    ka "「[fn]... 」"
    "In the midst of his crying, Kouya said my name.{p}And at last,{w=.2} he was looking at me."
    "I gently held him close to me,\nhis tears running onto my chest."
    fn "「If you're done thinking about your regrets,\n\ \ how about we go back to everyone?{p}\ \ After all,{w=.2} they're all waiting for you. 」"

    show ka 015 big night with dis
    
    ka "「{cps=5}. . . 」"
    "He said nothing, and cried quietly onto my chest."
    "I said nothing more, and gently stroked his head."
    
    stop music fadeout 3
    scene black with sdis 
   
    $ event_name = _("One answer")
   
    play music melodious03
    scene studio with sdis
    show ke 001 at center
    show yu 001 at farleft
    show jn 001 at farright
    with dis
    
    ke "「Oh,{w=.2} welcome back. 」"
    "When we got back to the studio,{w=.2}\nKeisuke-san's smile greeted us just like always."
    "But he didn't say anything after that.{p}He must be waiting for one of us to speak up."
    "Kouya has a reasonably longer relationship\nwith everyone else."
    "Rather than leaving things unsaid,{w=.2} there are\nprobably parts in there better heard for themselves."
    "I'm pretty sure that earlier,{w=.2}\neveryone figured out what Kouya was thinking.{p}And then, they came to the correct conclusion."
    "That's why they aren't talking.{p}They were waiting for it,{w=.2}\nfor Kouya to speak up first."

    scene studio with wipe_right
    show ka 001 at center with sdis
    
    fn "「Kouya- 」"
    "I urged him on with a look as\nI stood just behind him."
    ka "「Yeah,{w=.2} I get it... 」"
    "After responding, he took a step forward,{p}and opened his mouth."
    ka "「Guys,{w=.2} I'm really sorry about worrying you.{p}\ \ I'm all right now... 」"
    ka "「But before we get back to practice,{w=.2}\n\ \ there's somethine I want to tell you all.{p}\ \ Okay? 」"

    hide ka with wipe_right
    
    show ke 001 at center
    show yu 001 at farleft
    show jn 001 at farright
    with wipe_right
    
    yu "「All right.{w} What is it, Kouya? 」"
    "Yuuki-san kindly spoke in a voice\nthat said he'd be there for him.{p}The others waited for Kouya in the same way."

    scene studio with wipe_right
    show ka 001 at center with wipe_right
    
    ka "「I...{w=.2}think it might be possible that\n\ \ the next contest will turn out to be my last. 」"
    ka "「I think you all know that I ran away from home.{p}\ \ ...The other day,{w=.2} I promised I'd go back\n\ \ if the next result brings nothing. 」"
    ka "「I thought I wanted to take responsibility. 」"
    ka "「If I go back home,\n\ \ I don't plan on stopping with the guitar. 」"
    ka "「But just maybe,{w=.2}\n\ \ things might not work out that way. 」"
    ka "「Lately,{w=.2} I think I haven't been doing well\n\ \ because I've been thinking about that.{p}\ \ I took it upon myself,{w=.2} and went under. 」"
    
    show ka 014 with dis
    
    ka "「I tried moving quickly to not worry you guys,{w=.2}\n\ \ and I ended up causing trouble instead... 」"
    ka "「...Seriously, I'm sorry.{p}\ \ If I depended on you guys more...\n\ \ it would've been better. 」"
    ka "「I'm truly, honestly sorry about that. 」"
    "Kouya hung his head a little."
    "However,{w=.2} everyone was fine with just that."

    hide ka with dis
    show ke 001 at midright
    show ka 001 at midleft
    with dis
    
    ke "「I see...{w} {nw}"
    show ke 002 at center with dis
    extend " Yep, you said it.{p}\ \ If you kept going on like before,{w=.2} you'd probably\n\ \ never say anything until the very end. 」"
    
    show ke 001 with dis
    
    ke "「But you better not do that again next time.{p}\ \ 『We are forever with.』 」"
    ke "「All of us here,{w=.2} we've got dog tags\n\ \ with that carved into them. 」"
    ke "「That was the phrase you picked out for us.{p}\ \ It was a bit too long,{w=.2} but the last word\n\ \ was supposed to be 『us』, wasn't it? 」"
    ke "「That's why it's just like you said,\n\ \ you can count on us more.{p}\ \ Actually,{nw}"
    show ke 006 with dis
    extend " rely on us. We're always together, right? 」"
    "Keisuke-san smiled and laughed without any worries."
    "He's always had this careless attitude about him,{w=.2}\nbut he really is a peerless leader.{p}That's what I thought."
    "After all, he just settled all of this\nwith nothing but a smile.{p}It's just like magic."
    ka "「Sorry,{w=.2} Keisuke- 」"
    
    show ke 005 with dis
    
    ke "「Ahh!{w} It's fine! Apologizing so much wears me out.{p}\ \ {nw}"
    show ke 001 with dis
    extend "Now, since you've come back and we know the story,{w=.2}\n\ \ let's make a new circle with our feelings. 」"
    
    show yu 003 at farleft behind ka
    show jn 001 at farright
    with dis
    
    yu "「A circle... something crazy again? 」"
    ke "「It'll be fine.{w=.2}\n\ \ We did it a lot when we were\n\ \ setting up the band, didn't we? 」"
    ke "「It'll be exactly what we need if we\n\ \ want things to be the way they were.{p}\ \ Enough complaining, come on.{w} You too, Jun, Kouya. 」"

    show yu at jump_up
    
    yu "「Aah!{w} That hurts, Keisuke!{p}\ \ Okay, okay, just let go of my neck!{p}\ \ Are you trying to strangle me!? 」"
    "Keisuke-san caught Yuuki-san under his arms.{p}After seeing that,{w=.2}\nboth Kouya and Jun-kun move next to Keisuke-san."
    ke "「Come on come on,{w=.2}\n\ \ don't just stand there, [fn],\n\ \ come over here! 」"
    fn "「Eh, me too? 」"
    
    show ke 006 with dis
    
    ke "「What are you saying, o great manager?{p}You're our important 5th member,{w=.2} so of course. 」"
    fn "「...well, I am, I guess! 」"
    "I was honestly happy.{p}Keisuke-san's words made me unexpectedly annoyed,{p}{nw}"
    play sound step03
    extend "but I put up with it as I ran over."

    scene studio with wipe_right
    
    "After settling between Kouya and Jun-kun,\nI leant into the circle.{p}All of us came face to face with each other."
    ke "「All right, when we're at the next contest,{w=.2}\n\ \ it's gonna be the biggest landslide win ever.{p}\ \ I'm not joking when I say our futures hang on it. 」"
    ke "「Losing is impossible.\n\ \ So much so that you'll die if it somehow happens!{p}\ \ 'We are forever with'!{w} We'll win for sure! 」"
    "「YEAH! 」"
    "Five voices became one.{p}I'm sure that with our bonds,{w=.2}\nwe can't lose to any other group."
    
    stop music fadeout 3
    scene black with sdis

################################################    
label kouya26_sex:
    
    $ event_name = _("Continuing Speech")

    if persistent.replay == True:
        $ first = persistent.name_first
        $ last = persistent.name_last
        $ day = 26
        $ event_name = _("Continuing Speech")
        
        scene black with dis
        
        pause .5
        
    else:
        pause 2
    
    play sound plane_engine loop
    
    "Kouya's bike cut straight through the night."
    "Today's practice ended on that note.{p}「Everyone, steel up your feelings tonight, 」{w=.2}\nour leader ordered."
    "There were no objections.{w=.2}\nIt seemed that everyone there could use a break."
    "All of us believed that Kouya was essential."
    "Everyone spent all day practicing hard.{p}At this point, there were no talks about the basics:\nTomorrow's practice is the last day we get."
    "The only thing left to do now is to\nmake the performance as ideal as possible.{p}It's a basic task, but it's also extremely difficult."
    "The most critical thing here\nis definitely everyone's hearts."
    "If we're prepared, it should be business as usual.{p}However, the situation is different this time.{p}That's probably why we need a new resolve."
    "A conviction to overcome the pressure of losing.{w=.2}\nThat sort of determination."
    "I'll probably have to steel myself, too.{p}Everyone is recognizing me as 'the 5th',{w=.2}\nthe one who shouldn't be ashamed of the title."
    "My arms were clasped tightly around Kouya's waist.{p}That helped to calm me down a little."
    "「...It's okay, we can do this, 」\nMy mind mumbled,{w=.2} as if to convince me."
    "The bike sped up a little.{p}In what felt like a blink of an eye, we were back in\nMinasato, and the roar of the engine ceased."
    
    stop sound fadeout 1.5
    scene black with dis
    pause 1.5
    scene bedroom night
    show ka 001 night at center
    with dis
    play sound night_insects loop
    play music o97
    
    ka "「I really caused a lot of trouble today.{p}\ \ Sorry you had to see me in such a pitiful mood... 」"
    "As soon as we got inside, Kouya spoke up.{p}I laughed at that,{w=.2}\nwaving my hand in dismissal."
    fn "「Nah, you weren't, really.{p}\ \ People have times like that on occasion. 」"
    fn "「I didn't see it as \"pitiful\", either.{p}\ \ It actually made me happy,{w=.2}\n\ \ to feel like you trusted me. 」"
    
    show ka 006 night with dis
    
    ka "「It's embarrassing, stop saying that... 」"
    "He bluntly spoke his mind,{p}then, in a sudden moment of shyness,\nhe looked at the floor.{w} His face was red."
    "I thought it was kind of cute,{w=.2}\nso I considered teasing him just a bit longer.{p}In the end, I decided against it."
    "...No,{w=.2} it's more I couldn't say anything."
    "Silence moved in to fill the space between us."
    "There were plenty of things that could be said.{p}Something to tease Kouya with,\nor maybe some other topic."
    "But...{w=.2} this timing,\ncombined with the mood Kouya was in...\nIt made me hesitate to say anything."
    "It felt like my chest was rumbling,\nand it feels uncomfortable in here."
    "I can't move at all.{p}It's something I've felt recently."
    ka "「H-{w=.2}hey, [fn]. 」"
    "His face still red, Kouya suddenly spoke up.{p}He looked straight at me."
    "I could feel something in that gaze.{p}Suddenly, the scene in front of me\noverlapped with the images in my head."
    "What I saw was that day at the Summer Festival.{p}The memory of when we sat at the stone steps,\nwaiting for the fireworks."
    "When I became aware of the memory,\nmy heart began beating faster."
    ka "「Do you remember the day of the festival? 」"
    fn "「Y-yeah. 」"
    ka "「At that time, I was seriously about to tell you.{p}\ \ But after that, things kept getting in the way. 」"
    ka "「...I'm sure that if I don't say it now,\n\ \ I'll never be able to. 」"
    ka "「That's why I'll say it now. 」"
    ka "「[fn]...{w} I-{w=.2}I... 」"
    "Kouya continued on."
    "Maybe he realized it.{p}These were the same words he used before."
    "I still didn't know what\nwas going to come after them."
    "My heartbeats reverberated through my body,\nthumping loudly in my ears."
    "As Kouya's pierced through me, I couldn't look away.{p}My chest constricted painfully."
    "In the moment he paused, I felt kind of sick.{p}It felt like I was trapped in an illusion\nthat would never end."
    "However, that wasn't true,{w=.2}\nas Kouya soon found the words he'd lost that day."
    "And this time, they wouldn't be interrupted."
    
    show ka 001 night with dis
    
    ka "「I am in love with you. 」"
    "My heart stopped ringing in my ears.{p}Inside my head, everything was going pure white.{p}I don't understand what he's saying."
    ka "「I was a little interested when you came back.{w=.2}\n\ \ Then, after we started living together,\n\ \ my feelings grew deeper. 」"
    ka "「Saying it to anyone else doesn't feel that special,{w=.2}\n\ \ but when I say it to you, I feel so happy.{p}\ \ I don't really get it myself. 」"
    ka "「At the start, I wondered if it was all in my head.{p}\ \ But it's not like that at all.{p}\ \ Today really brought it home to me. 」"
    ka "「I-{w=.2}I love you. 」"
    "That's the second time he's said it.\nThis time, I was able to catch a bit of it."
    "Umm...{w=.2}So...{w=.2}this would be...{w=.2}that?\nConfessing is fine...{w} right?"
    fn "「...Really? 」"
    ka "「Really. 」"
    fn "「You aren't lying? 」"
    ka "「I'm not lying. 」"
    fn "「{cps=5}. . . 」"
    "Words wouldn't come out.{p}Something. I should be saying something."
    fn "「Uh, umm,{w=.2} ahh...{p}\ \ ...Are you okay with me? 」"
    "When I finally got something out,\nKouya nodded vigorously."
    "It made me so happy, I felt like crying.{p}But I can cry later.{p}Right now, I have to actually answer him."
    fn "「Umm,{w=.2} I feel the same way about you.{p}\ \ So, how do I put this...{w=.2}\n\ \ I can't say it all that well, but-! 」"

    hide ka with wipe_right
    play sound2 bosu34
    
    "My train of thought was lost when\nmy field of vision suddenly darkened."
    "Kouya was hugging me tightly."
    fn "「U-umm...{w} Kouya...? 」"
    "I was so surprised by the action,\nI lost my tongue again."
    
    show ka 001 night at center with dis
    
    ka "「Sorry.{w} But when you said you felt the same,{w=.2}\n\ \ I felt so happy.{p}\ \ ...Do you want me to stop? 」"
    fn "「No.{w} Staying like this is fine.{p}\ \ Besides... I feel the same. 」"
    "With things like this, there's nothing left to say.{p}I moved my arms around Kouya's back,\nand hugged him tightly in return."
    
    stop music fadeout 7.5
    
    "Being so close to him,{w=.2} he felt so very warm."
    
    $ event_name = _("Two Lovers")
    
    "I didn't really understand where things were going,{w=.2}\nbut it felt so comfortable."
    "As I was wrapped up in this warmth,{w=.2}\na sense of inexpressible happiness filled me."
    "My head gradually emptied out,{w=.2}\nalmost as if it were floating out into space.{p}It's a mysterious feeling."
    ka "「[fn]... 」"
    "Hearing Kouya say my name, I raised my head.{p}Kouya's beautiful golden eyes were right there."
    "The image of my expression was reflected in them.{p}And with each passing moment, it got larger."
    "Kouya was slowly bringing his face closer to mine.{p}I could feel his faint breathing so near to me.{p}Soon, there won't be any distance between us."
    "And suddenly,{w=.2} that distance became zero."
    fn "「Mn... 」"
    "Our lips touched as though drawn to each other.{p}Even after parting, a sweet numbness remained.{p}I spoke, almost reflexively."
    fn "「Kou...{w=.2}ya... 」"
    "From just that,{w=.2}\nKouya picked up on what I wanted to do."
    ka "「[fn],{w=.2} you sure? 」"
    fn "「Yeah...{p}\ \ If it's with you,{w=.2}\n\ \ I want to try it... I think. 」"
    
    show ka 002 night with dis
    
    "After telling him this, Kouya smiled slightly.{p}A thump pounded through my chest in response.{p}Just that one tiny gesture felt so adorable."
    "Kouya slowly closed his eyes,\nat the same time drawing his lips closer again.{p}{nw}"
    scene black with sdis
    extend ""
    "I closed my own eyes,\nand waited for the time to come."
    "We kissed again.{p}This time,{w=.2} it was different from\nthe fleeting touch we'd had before."
    "Kouya breathed in and pulled me close.{p}Then,{w=.2} he pushed his long tongue into my mouth."
    "I was a bit surprised by the suddenness of it.{p}But, not a second later,{w=.2} my body relaxed again."
    "After making sure that I wasn't resisting,\nKouya began to move.{p}"
    "He traced along a row of my teeth with his tongue,\nthen entangled his with my own."
    "As he continued without pause,\nI started to get used to it."
    "During all that sweet stimulation,\nI let out only a short gasp."
    fn "「Phew...{w=.2} Uu, nn... 」"
    ka "「Mn...{w=.2} Ffu... 」"
    "As we moved deeper into our kiss,\nthe two of us started breathing heavily."
    "A breath blew out of the tip of Kouya's nose,\nwhich excited me even more."
    "Before long, we slowly separated.{p}A small trailing thread of saliva connected\nto our mouths,{w=.2} which disappeared a second later."

    scene bedroom night with sdis
    
    fn "「Huff,{w=.2} huff,{w=.2} huff... 」"
    "I'm not used to long and deep kisses.{p}To make up for the lack of breath,{w=.2}\nI sucked in oxygen with all my strength."
    
    show ka 001 night at center with dis
    
    ka "「You okay, [fn]? 」"
    fn "「Yeah, I'm fine.{p}\ \ It's just... that was amazing... 」"
    "The sensations were overwhelming,\nso it was difficult to articulate anything.{p}My brain switched to a simpler vocabulary."
    
    show ka 002 night with dis
    
    ka "「Heh, it was good wasn't it?{p}\ \ You seem pretty excited. 」"
    "Kouya tapped my crotch lightly as he said that.{p}A sharp feeling shot through within me,\nstimulating me much more than the kiss had."
    "My face turned hot with embarrassment in a flash."
    fn "「W-{w=.2}well, that was my first time... 」"
    ka "「We've only just started, you know?{p}\ \ I'll do something even better for you. 」"

    hide ka with dis
    
    "While he was speaking, he turned out the lights.{p}Now,{w=.2} only the night sky filtering\ndown through the window illuminated us."
    "My eyes were unintentioanlly drawn away\nbecause of the dream-like scenery.{p}But almost immediately, the illusion disappeared."
    fn "「Wha-!? 」"
    "Kouya carried me to the bed,{w=.2}\nthen gently pushed me down onto it."
    
    show ka 001 night at center with dis
    
    fn "「Wai-{w=.2} Kouya...? 」"
    ka "「It's okay.{w} Just trust me. 」"
    "Kouya whispered tenderly into my ear.{p}Then,{w=.2} he carefully began removing my clothes."

    play sound2 changing
    
    "My pants and shirt were taken off simultaneously,{w=.2}\nthe air in the room wrapped up against my skin.{p}It felt kind of itchy."
    
    show ka 011 night with dis
    pause .2
    
    ka "「Man, you're so hard.{p}\ \ And all we've done so far was kiss. 」"
    "Before long I was compleletly naked on top of the bed.{p}Kouya was mumbling down by my feet,{w=.2}\nall the while staring at my crotch."
    fn "「Could you not say that? It's embarrassing.{p}\ \ And hey,{w=.2} why am I the only one naked? 」"
    "I looked at him in protest.{p}Me being the only one stark naked here{w=.2}\nfeels really unfair."
    
    show ka 002 night with dis
    
    ka "「Don't worry, I'm getting to that.{w} Give me a sec. 」"
    "He smiled widely as he put his hands on his clothes."

    play sound2 standup
    
    "He started with his dog tags,{w=.2}\nthen his tank top,{w=.2} then his jeans."
    "From beneath his stripped-off garments,{w=.2}\nhis toned body became exposed to the air."

    show ka 101 night with dis
    
    fn "「...Kouya, you can't go calling the kettle black! 」"
    "The only thing left on Kouya were his bikini briefs.{p}Even in this darkness,{w=.2}\nI could see the large tent in his crotch."
    "I could see light reflecting\nfrom the tip of that bulge."
    
    show ka 102 night with dis
    
    ka "「Hey, it's not like I can help it.{p}\ \ After I saw how turned on you were... 」"
    fn "「Will you stop saying such embarrassing things...? 」"
    "I scowled at him as I tried to cover it up."
    "But still,{w=.2} It's not like I mind that much."
    
    show ka 105 night with dis
    
    ka "「Don't blame me for making you glare like that.{p}\ \ {nw}"
    show ka 102 night with dis
    extend "Here, I'll make up for it. 」"

    show ka 101 night with dis
    
    "No sooner had he said than he took off his briefs,{w=.2}\nwhich he then tossed onto me."
    "...However, he laid facing the\nopposite direction to me."
    "Kouya's head was perfectly level\nwith something not too far from my stomach."
    "Thinking it was strange, I started to speak.{p}But all of a sudden, something else took priority."

    scene black with dis
    scene ev_kouya_1a with sdis
    
    fn "「Uwah...! 」"
    "Kouya's tongue slowly stroked up my penis.{p}The sensation made me cry out."
    ka "「How was that, [fn]? 」"
    fn "「Mm... I-{w=.2}it felt great. 」"
    "Mustering my strength,{w=.2}\nI finally got out those words."
    "After receiving a satisfactory answer,{w=.2}\nKouya's tongue started working all over my erection."
    "I couldn't even say anything,\nsince it was my first time getting blown."
    fn "「Guh,{w=.2} nn...{w=.2} Haah, aah! 」"
    ka "「Mn...{w=.2} Ff... 」"
    "Kouya's rhythm escalated,{w=.2}\nmaking me gasp harder."
    "After some more licking,{w=.2}\nmy whole length suddenly became\nburied inside his muzzle."
    
    play sound2 sex1 loop
    $ renpy.music.set_volume(0.6, 0.0, channel = "sound2")
    
    "An indecent 'schlop-schlop'\nsound filled the air."
    fn "「Ngaaah! 」"
    "His constant suckling on me pressed continued,{w=.2}\nmaking my cry out loudly before I could stop myself."
    "This feeling was nothing like what\nI've done by myself,{w=.2} and it spread throughout me."
    "A shiver ran down through my spine.{p}It was as if a jolt of electricity shot through me."
    fn "「Wai-{w=.2} Kouya... Ng! 」"
    fn "「Gh,{w=.2} I-{w=.2} ... 」"
    "My voice grew faint, signaling my impending climax.{p}However, it didn't actually arrive.{p}{nw}"
    stop sound2
    extend "Kouya let go of my twitching member."
    fn "「Wh-{w=.2}why...? 」"
    "It almost felt painful as I asked."
    ka "「If you're the only one having fun,{w=.2}\n\ \ wouldn't that be unfair? 」"
    "After saying that, Kouya shook\nhis hips in front of my face."
    "Sticking out from his crotch was Kouya's dick,{w=.2}\nleaning forward at maximum hardness."
    "It's so much bigger than mine."
    ka "「Suck on mine, too.{p}\ \ I'll keep going if you do. 」"
    "He shook his hips one more time to make sure.{p}The way he did it made my heart thump loudly."
    "Timidly, I put my hand out,\nguiding his cock into my mouth."
    "...It's so warm."
    "Together with an assertive flavor,{w=.2}\nan amazing heat spread through my mouth."
    "My head felt oddly numb.{p}As I started feeling so strange,{w=.2}\nmy tongue lapped over the hot shaft."
    ka "「Mm...{w=.2} That's right.{w} Keep it up. 」"
    fn "「Ff,{w=.2} Uu... 」"
    
    play sound2 sex1 loop
    
    "Kouya once again put my dick\nin his mouth as he let out a sigh."
    "If I could open my mouth,\nI'd probably be gasping,{w=.2}\nbut Kouya's cock in my mouth put a stop to that."
    "Instead, I started sucking even harder."
    "If I do it that way, it feels pleasant for me too.{p}A loop of hot pleasure."
    "The peaceful room filled with wet slurping sounds,{w=.2}\nalong with the muffled gasps from the two of us."
    "The sounds reaching my ears\nonly turned me on even more."
    "However, I was getting close\nto the point of no return."
    "My penis was being cranked to its limit,{w=.2}\nas far as it can go before I blow my load.{p}I'd be coming any second now."
    fn "「Ngh,{w=.2} hkh,{w=.2} kuh... 」"
    "A searing heat welled up inside me.{p}I tried to hold it back by\nconcentrating my focus on my stomach."
    "Still, that didn't result in anything.{p}My body was gearing up to release."
    "...Crap, at this rate..."
    fn "「Haaah...{w=.2}Kou...ya!{w} I-{w=.2}I'm gonna come! 」"
    "My voice strained as I tried to warn him."
    "And yet, Kouya didn't slow down."
    "On the contrary,{w=.2}\nKouya wrapped his fingers around\nthe base of my penis and began stroking, hard."

    stop sound2 fadeout 3
    
    fn "「Wai-!{w} Kouya! 」"
    ka "「... 」"
    fn "「Gurkh...{w=.2} Ha-aaaah!! 」"
    "I crossed the threshold.{p}{nw}"
    play sound2 heartbeat
    scene white with qdis
    scene ev_kouya_1b with dis
    extend "As my voice went up,{w=.2}\nI released my seed inside Kouya's mouth."
    "I saw stars as waves of pleasure washed over me."
    ka "「Phh-{w=.2}ng.... 」"
    "His short gasps reached my ears.{p}Seems like he drank down all my cum,\nsucking out every last drop from me."

    scene black with sdis
    scene bedroom night with sdis
    show ka 102 night at center with dis
    
    ka "「...You had a lot saved up, didn't you?{p}\ \ So, was that great, or what? 」"
    fn "「Whew... It was awesome,{w=.2}\n\ \ but you overdid it a little... 」"
    "In my afterglow, I could only speak faintly.{p}That took out so much of my energy,{w=.2}\nbut it left me with a sweet sense of fatigue."
    ka "「Heheh, well, sorry about that.{p}\ \ But it's too early to rest. 」"
    ka "「After all,{w=.2} I haven't gotten off yet. 」"
    fn "「Ah- 」"
    "He pointed down to his crotch.{p}His large cock was still twitching in front of me."
    "It hung there, covered in my spit,{w=.2}\nreflecting the light from outside."
    "Leaving it like this would be impossible,\nno matter how you look at it."
    "I couldn't look away.{p}My eyes were drawn towards it.{p}I was feeling hot all over."
    
    show ka 106 night with dis
    
    ka "「Will you...{w=.2} Finish it for me? 」"
    "His request made my heart pound.{p}I gave a small nod."
    "Between his spread legs,{w=.2}\nI set myself down on all fours\nas I brought my face closer to his stiff member."
    "Once again,{w=.2} I guided it into my mouth.{p}And just like before, I ran my tongue all over it."

    play sound2 sex1 loop
    hide ka with dis
    
    ka "「Mn, that's good, [fn]. 」"
    "Kouya tenderly caressed my head.{p}The compliment made me happy,{w=.2}\nand I sucked harder."
    ka "「Ng,{w=.2} kuh...{w=.2} Haaah! 」"
    "I rubbed my dick more forcefully.\nThis time, the sensations were even more intense."
    fn "「...Ngh... 」"
    "Instead of breathing hard,{w=.2}\nI sucked on Kouya with all of my might."
    ka "「Hng!{w} [fn],{w=.2} I'll blow any second now! 」"
    "I ignored his cries,{w=.2} sucking even harder\nas my tongue wrapped around his length.{p}Since Kouya did this for me, I wanted to do the same."
    "At the same time, I moved my left hand even faster.{p}I was getting close to peaking again.{p}It felt like something was welling up in my stomach."
    ka "「Nn,{w=.2} kuh,{w=.2} uuugh... 」"
    fn "「Fffp,{w=.2} nn,{w=.2} ng-! 」"
    "I hit my peak, and I climaxed for a second time.{p}{nw}"
    play sound3 heartbeat
    scene white with qdis
    scene bedroom night with dis
    extend "This time, my seed just spurted onto my hand."
    ka "「Kuh,{w=.2} a-{w=.2}aaahhh! 」"
    fn "「-! 」"
    "It was almost simultaneous.{p}{nw}"
    stop sound2
    play sound2 heartbeat
    scene white with qdis
    scene bedroom night with dis
    extend "Kouya shot his heavy load into my mouth."
    "I'd brushed against his cockhead with my teeth,\nbut that seemed to be the finisher."
    "A unique taste filled my mouth.{p}It was a mysterious flavor."
    "After swallowing up the stickyness,{w=.2}\nI let go of Kouya's member."
    
    $ event_name = _("Limit Break")
    
    ka "「[fn]. 」"
    "I pushed myself up when he called my name.{p}My head felt empty,{w=.2} and I was irritated at\nat how slowly I seemed to be moving."
    "Soon after rolling over,\nKouya brought his face close,{w=.2}\nand without pause he kissed me."
    "Then he held me in his arms as he pushed me down,{w=.2}\nand the two of us laid down in the bed."
    "I was so comfortable there,\nwrapped up in Kouya's warmth,\nthat drowsiness quickly spread over me."
    "I slowly dozed off in the darkness.{p}I felt like I heard Kouya's voice,{w=.2}\nbut I couldn't tell what he was saying."

    scene black with sdis
    
    "He seemed to notice,{w=.2}\nand he replaced his words with\na soft press of his lips to my brow."
    "After feeling only that,{w=.2}\nI drifted into sleep as softness wrapped around me."
    "What I felt then, more than anything else...{w=.2}\nWas a moment of great happiness."
    
    if persistent.replay == True:
        scene black with dis
        pause .5
        $ renpy.end_replay()
        
    $ persistent.event_kouya1 = True    
    
    jump end26
    
######################################################
label shin26:
    
    $ event_name = _("Amaki wants to talk")
    
    play music melodious08
    $ renpy.music.set_volume(0.8, 0.0, channel = "music")
    
    scene hbroom with sdis
    
    "Since that day, I've never went out more than\nnecessary. I'm not a shut-in,{w=.2} but I was afraid\nof running into Shin-kun or Amaki-san."
    "I can't explain all that well why I'm exactly\nafraid of,{w=.2}but I wasn't sure how should I act\nif I met them,{w} so I didn't want to see them."
    "So I was afraid to see them."
    fn "「Alright, done now. 」"
    "Maybe it was because I was trying to hide my\nanxiety, but I've been unconsciously\ntalking to myself more."
    "I sighed a little when I noticed myself\ndoing it again."
    "I uncharacteristically faced the desk silently\nwhile I was killing time,\nand today the day was mostly over."
    "It's still too early for dinner isn't it?{p}As I felt the slightly cool outside breeze,\nI wiped the sweat off me while considering it."
    gm "「[fn]-chan, phone! 」"
    fn "「Oh, okay! 」"
    "A phone call? From who?"

    scene hentry red with wipeleft
    
    "When I got to the phone,\nGrandma was waiting there holding the receiver."
    fn "「Who is it? 」"
    gm "「Kuroi-san, they said. 」"
    "Kuroi. {w=.2}That name made me stop with a start.{p}It's from Shin-kun..."
    gm "「Well, take it. 」"
    fn "「Y-yes... 」"
    "I picked up the phone awkwardly,\nand tried to keep my voice from shaking\nwhile answering it."
    fn "「Hello... 」"
    am "「Yes, this is Kuroi,{w=.2} [ln]-kun? 」"
    fn "「Amaki-san? 」"
    "When I heard the familiar voice on the line,\nI reflexively smoothed down my chest."
    "Grandma probably had to get dinner ready.{p}I could hear her going back to the kitchen."
    fn "「Um, is Shin-kun... 」"
    am "「Shin-kun?{w} He's doing fine.{p}\ \ That aside,{w=.2} I want to talk with you for a bit.\n\ \ May I have a bit of your time? 」"
    "He's fine.{w=.2} That's a relief to hear, yet it\nalso filled me with a strange sense of sadness.{p}If there wasn't anything, it should've been best."
    fn "「With me? 」"
    am "「Yes.{p}\ \ As soon as possible,{w=.2}\n\ \ maybe even now if you can. 」"
    fn "「Now? 」"
    "What's all this all of a sudden?{p}But with him as busy as he is, he must have really\ntried to scrape some time together for this."
    am "「That won't work? 」"
    fn "「Uh, no. It's fine. 」"
    am "「That so?{p}\ \ In that case, can we meet at the park? 」"
    fn "「The park. Understood. 」"
    am "「I'll be waiting. 」"

    play sound call05
    "Click. {w=.2}{nw}"
    play sound call00 loop
    extend "Boop. Boop."

    stop sound
    
    "What could Amaki-san want?{p}It was stuck in my head, but I couldn't think\non it too hard then, so I obediently went out."
    "Maybe it was the way he always speaks,{p}or maybe it was because of what was\non my mind the past few days."
    fn "「Grandma, I'm going out for a little bit. 」"
    gm "「Right now?{p}\ \ But it's almost dinner time. 」"
    fn "「Sorry,{w=.2} I'll be back as soon as possible.\n\ \ If I end up late, go ahead and eat without me.{p}\ \ I'll be going now! 」"
    "I left while saying that to my grandma,\nwho was leaning out of the kitchen,\nand ran over to the park."

    hide window    
    stop music fadeout 1
    pause 1
    play sound higurasi loop fadein 1
    $ renpy.music.set_volume(0.8, 0.0, channel = "sound")
    scene park red with dis
    show am 001 red at center with dis
    
    am "「Ah, [ln]-kun. Over here. 」"
    "When I reached the park,\nAmaki-san was waiting, waving his hand.{p}I waved back as I entered into the interior."
    "It was almost evening,so there were no children around,\nand the red-dyed scenery shone sadly and quietly."
    
    show am 007 red with dis
    
    am "「Sorry for calling you out so suddenly. 」"
    fn "「It's okay.{p}\ \ So, what did you want to talk about? 」"
    
    show am 001 red with dis
    
    am "「About Shin-kun for a bit. 」"

    play sound heartbeat
    
    "Thump."    
    "It should've been obvious that name\nwould roll out of his mouth,{w=.2}\nbut the way it sounded it felt like"
    "it was out of my expectations,\nand my heart pounded loudly once."
    
    show am 003 red with dis
    
    am "「It would fine if I was just overthinking things,\n\ \ but it seems he's been in a strange mood.{p}\ \ Would you happen to know anything about that? 」"

    if shin_badend == True:
        jump shin26_condemn
    else:
        jump shin26_explain

    ##############################################
    label shin26_condemn:
            
        $ event_name = _("A Guardian's Duty")
        
        fn "「N-no... 」"
        am "「It was about the time you came over though. 」"
        fn "「R-really?{p}\ \ Not much really happened that day though... 」"
        
        show am 001 red with dis
        
        am "「...I see. 」"
        "I instantly lied through my teeth.{p}I didn't have any confidence they felt true\neven though I said it myself."
        "Still, I couldn't say anything else."
        
        show am 004 red with dis
        
        am "「Hmm, maybe my hopes were misplaced.{p}\ \ I thought you out of anyone else might know. 」"
        fn "「Sorry I couldn't help. 」"
        
        show am 007 red with dis
        
        am "「No, I should apologize.\n\ \ I wasted your time and all. 」"
        "At Amaki-san's usual smiling expression,\nI could feel myself breaking out\ninto a cold sweat."
        
        show am 003 red with dis
        
        am "「If that's the case...\n\ \ was the Master's case actually the cause? 」"
        fn "「Eh? 」"
        "I didn't miss what Amaki-san had\nabsently muttered to himself."
        
        show am 001 red with dis
        
        am "「Oh whoops, I was talking to myself.{p}\ \ It's not related to you. 」"
        fn "「... 」"
        "As those words pushed me away\nin the same tone as ever, I felt a cold,\nsharp stab, and I couldn't reply."
        
        show am 005 red with dis
        
        am "「No wait, it's rude of me\n\ \ to speak that way to Shin-kun's friend. 」"
        "After Amaki-san apologized,\nhe continued on from before."
        "It seems like the other day, a letter\ncame in from Shin-kun's father.{p}And the subject written in it was..."
        fn "「Studying overseas!? 」"
        
        show am 001 red with dis
        
        am "「Yes.{p}\ \ It's a prestigious school that has\n\ \ turned out many a great patissier. 」"
        
        show am 005 red with dis
        
        am "「If it's from the Master,\n\ \ it might be a gift for the son\n\ \ he can't normally see. 」"
        am "「At the same time,\n\ \ that would mean moving out of this village. 」"
        fn "「That can't be...{p}\ \ so I can't see Shin-kun anymore? 」"
        
        show am 001 red with dis
        
        am "「We've only just been invited,\n\ \ but nothing's been filed. 」"
        am "「If Shin-kun clearly declines it, then all\n\ \ talks of it could be thrown out though. 」"
        
        show am 003 red with dis
        
        am "「However, he's hesitant.{w} I'm fairly sure\n\ \ he wants to live in this village.{w} However,\n\ \ that would mean refusing his father's goodwill. 」"
        am "「Whether he'll throw away his life and friends\n\ \ from here, whether he'll refuse the Master's,\n\ \ his father's kindness, 」"
        am "「whether he could pick between them,\n\ \ he probably can't decide. 」"
        fn "「But that's...! 」"
        "So that's why he was acting so strange then...{p}\ \ I couldn't contain myself,\n\ \ and I ran off towards Shin-kun's mansion."
        
        show am 006 red with dis
        play sound bosu32
        
        am "「Hey, where are you going? 」"
        fn "「I've decided!{w} I have to see Shin-kun\n\ \ and clearly talk things out. 」"
        
        show am 005 red with dis
        
        am "「Talk? About what...? 」"
        fn "「'About what'...{w=.2}\n\ \ about what we just talked about!{w} Please let me go!{p}\ \ Aren't you letting me go!? 」"
        
        show am 001 red with dis
        
        am "「...this is his problem.{p}\ \ As a caretaker I can't say anything.{p}\ \ The one to decide things...{w=.2} is him. 」"
        fn "「You can't possibly think that!! 」"
        
        show am 002 red with dis
        
        am "「Is that something you can say? 」"
    
        play sound standup
        
        fn "「! 」"
        "As Amaki-san showed his usual smile,\nhe tightly gripped my arm,\ntight enough that it was getting numb."
        am "「Shouldn't you first ask yourself if it's alright\n\ \ for you to show up in front of Shin-kun? 」"
        fn "「... 」"
        "With the pain in my arm and the frozen smile,\nit felt as though a cold hand was grabbing my\nheart, making me go cold."
        "Calmly,{w} calmly as always,{w=.2}\nhe caught me while his eyes pierced through me."
        
        show am 005 red with dis
        
        am "「I am a caretaker.{p}\ \ Therefore, I have no intention in denying his choice,\n\ \ and I will support whatever he chooses to do. 」"
        am "「Even if that choice breaks his heart.{p}\ \ But...{w} if there's anything that would hurt him,\n\ \ I have an obligation to remove it. 」"
        
        show am 001 red with dis
        
        am "「...how about you? 」"
        "He looks as calm and collected as ever,{p}but he isn't.{p}Shin-kun's family was glaring at me with a smile."
        am "「This is a problem that no longer concerns you.{p}\ \ Therefore, you should go home right away. 」"
        
        show am 005 red with dis
        
        am "「...it may be strange to say this after everything,{w=.2}\n\ \ but all interference beyond this point is useless. 」"
        fn "「... 」"
        
        show am 002 red with dis
        
        am "「Got it? 」"
        "Whatever strength he had left,\nhe used to grip me even harder."
        fn "「U-understood. 」"
        am "「Thank you.\n\ \ Well then,{w=.2} goodbye,{w} [ln]-kun 」"
        fn "「Good...{w=.2} bye... 」"
        "He suddenly let go of my arm,\nand headed off into the twilight."
        "Until I could no longer see him,{w=.2}\nI stood shock still next to the seesaw."
    
        hide am with sdis
        scene park red with sdis#!#
        scene black with sdis
        
        "Maybe he had seen everything from the beginning.\nMaybe he was even testing me."
        "However, I had no way of knowing for sure,\nno matter how much I guessed,\nthe truth had passed to nothing."
        "In my mind I had hurt my childhood friend,\nran away, and in the end,{w=.2}\nI lost any chance of fixing things."
        "Probably...{w=.2} forever."
        
        stop sound fadeout 1
        scene black with sdis
    
    #########################################################
        
        $ event_name = _("Shin: Bad ending")
        
        play sound bus_idling loop fadein 1
        $ renpy.music.set_volume(0.8, 0.0, channel = "sound")
        scene bus with sdis
        
        "A few days after that, I was in the bus.{p}The green scenery I had gotten used to this summer\nwas steadily replaced with concrete streets."
        "Since that day, I've never seen Shin-kun.{p}Even on the day I left he never appeared."
        "From what I've heard,\nhe ended up deciding on going overseas.{p}I don't know if he'll ever come back to Japan."
        "...I'll probably never have a chance\nto see him again.{w} I just wanted one chance,{w=.2}\none chance to apologize to him."
        "What I had done to Shin-kun had become a bit\nof a rumor amongst everyone.{w} I found out\nwhen I talked with them at the bus stop."
        "It's a small town, so even if it's hidden\nthe truth will naturally leak out as gossip."
        "Everyone said I wasn't like that,\nbut the self-styled info network said\n'there isn't anything to support you.'"
        "However everyone seemed uneasy, and I couldn't\nlie to them anymore than that.{w} However,\ndidn't have the courage to confess either."
        "I got onto the bus diverting the conversation,\nas if I was running away from everyone.{p}No.{w} 'As if' nothing - I was running away."
        "From the village,{p}from everyone,{p}from Shin-kun..."
        fn "「Huh... 」"
        "On my face, my reflection in the window,\nhow did I notice it at first...?"
        "What was bubbling up when the bus jostled,{w=.2}\nthe moment I blinked,{w=.2}\na drop ran down my cheeks."
        "I pressed down on the corner of my eyes as I sat\nalone, trying to hold it down however I could,\nbut the effort turned out to be for nothing."
        "A formless feeling fell out of a wide hole\nin my heart,{w=.2} I hid my voice,{w=.2} and cried."
        "Goodbye, Minasato.{p}Goodbye, everyone.{p}Goodbye, Shin-kun..."
    
        stop sound fadeout 1
        pause 1
        
        "Oh, I see.{w} Between the indelible past\nand this helpless sense of loss,{w=.2}\nI understood only one simple truth clearly."
        "My summer vacation...{w=.2} is over."
        
        scene black with sdis
        pause 5
        #!#jump splashscreen
        #!#MainMenu()
    
    #########################################################
    label shin26_explain:
            
        $ event_name = _("A Friend's Company")
        
        fn "「No, not really... 」"
        
        show am 001 red with dis
        
        am "「About when his mood started,\n\ \ I don't need that much detail,\n\ \ but have you noticed anything? 」"
        "About when...?{p}That time we went to the festival,\nI thought he was the same as ever."
        fn "「As of the festival,\n\ \ I don't think there was anything.{p}\ \ But after that, he started acting different. 」"
        am "「... 」"
        "That's right. Nothing happened up to the festival.{p}But after that he suddenly told me to not come,\nand he suddenly kissed me..."
        "Thinking about what's out of the ordinary was hard,\nbut Shin-kun that day was completely different,\nand I couldn't understand his intentions at all."
        fn "「As to what, I can't say,{w=.2}\n\ \ but when I think about it,{w=.2} after the festival\n\ \ I felt like his mood suddenly shifted. 」"
        "I can't actually say 'he kissed me,'\nbut I answered as much as I could."
        am "「Hmm... 」"
        
        show am 003 red with dis
        
        am "「Is that it?{p}\ \ It must've definitely been caused\n\ \ by the Master's letter. 」"
        fn "「The Master? 」"
        "As he muttered something important,\nI reflexively asked back."
        
        show am 001 red with dis
        
        am "「Mister Keiichirou.{p}\ \ Shin-kun's father. 」"
        fn "「Shin-kun's... 」"
        
        show am 003 red with dis
        
        am "「That letter came the day\n\ \ after you and Shin-kun went to the festival,\n\ \ and the times match up exactly. 」"
        fn "「What was written in it? 」"
        "Asking what was in the letter was boorish,\nbut I didn't want to not ask."
        "Why did Shin-kun do that?{p}I wanted a hint of some kind,\nno matter how small it might be."
        
        show am 001 red with dis
    
        stop sound fadeout 1
        pause 1
        play music piano4_001
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        
        "The letter was a summation of recent events,{p}a worry about being unable to meet a son, and,{w=.2}\nit was attached to an invitation letter."
        fn "「A letter of invitation\n\ \ from an overseas technical school!? 」"    
        am "「Yes.{p}\ \ It's a prestigious school that has\n\ \ turned out many a great patissier. 」"
        
        show am 003 red with dis
        
        am "「If it's from the Master, it might be a gift\n\ \ for the son he can't normally see, 」"
        am "「but for Shin-kun,\n\ \ he may be nearing a painful choice. 」"
        fn "「What do you... 」"
        
        show am 001 red with dis
        
        am "「To give up his life here,{w=.2}\n\ \ to turn down his father's favor,{w} one of the two. 」"
        "As Amaki-san spoke, he put up a finger for each\nchoice and looked like he was making a peace sign.{p}That's..."
        fn "「Has Shin-kun already decided? 」"
        
        show am 007 red with dis
        
        am "「I can't say anything about that.{p}\ \ If he doesn't want to,{w=.2} and if we inform the Master,{w=.2}\n\ \ it's possible to wipe this off the papers. 」"
        
        show am 004 red with dis
        
        am "「But it might be impossible.{p}\ \ That boy might have discarded the choice{w=.2}\n\ \ to say no while he struggled with it. 」"
        fn "「Why!? 」"
        "Shin-kun said making confections was a hobby.{p}He said so many times\nhe didn't plan to do it for work."
        "And yet, why would he suddenly change his mind?{p}Did he really hate the village that much?"
        "I didn't get it,\nand I unconsciously raised my voice."
        
        show am 005 red with dis
        
        am "「It's a favor from the Master's relative. 」"
        "Amaki-san quietly replied to me\nwhen I shouted, {w=.2}then told me about it.{p}All about Shin-kun."
        
        show am 004 red with dis
        
        am "「Poor child. Looking at him just pains the heart. 」"
        am "「Ever since he was young he always tried his best,\n\ \ all alone, even after he had forgotten\n\ \ why he was trying so hard. 」"
        am "「If that were true, he'd speak selfishly more,\n\ \ depend more, be resistant more, and so much else.{p}\ \ But that boy knows that would be bothersome. 」"
        am "「Because he loved him,{w} truly loved him,{w=.2}\n\ \ he troubled them without even doing anything.{p}\ \ He's such a smart, awkward boy. 」"
        "He sat down on a low seesaw, and\nhe kept talking in a tone that I couldn't\ntell was to me or to himself."
        
        show am 001 red with dis
        
        am "「Do you still remember the reason Shin-kun\n\ \ came to this village? 」"
        fn "「...I'm pretty sure it was for asthma treatment. 」"
        
        show am 007 red with dis
        
        am "「Not treatment, recovery. 」"
        
        show am 004 red with dis
        
        am "「I think from that time, that boy might have\n\ \ already known he was causing his parents trouble.{p}\ \ But that's what children do anyway. 」"
        am "「He could have been more like a child,{w=.2}\n\ \ but he insisted he could do it all by himself.{p}\ \ That sort of perception is strange for a child. 」"
        am "「Even the scarce time his parents had to visit,{w=.2}\n\ \ it'd be more accurate to say he was 'welcoming'\n\ \ them rather than 'depending' on them. 」"
        am "「He tried his best to make them happy,\n\ \ smile for them,{w} and he absolutely never cried\n\ \ until he was alone. 」"
        am "「What resulted is the 'Shin-kun'\n\ \ you all know very well. 」"
        fn "「... 」"
        "An image of Shin-kun, who was always reticent,\nalways looking uninterested,\nand always looking unpleasable crossed my mind."
        
        show am 007 red with dis
        
        am "「Eventually,{w=.2} he'd say that I'd even remember\n\ \ how he'd personally act selfish. 」"
        am "「Somehow, it seems like\n\ \ he's still unable to rely on others. 」"
        
        show am 004 red with dis
        
        "After saying that much,\nAmaki-san gave a little breath.{p}...{w} this guy really is Shin-kun's family."
        "He understood Shin-kun more than anyone else,\nand supported him just as much.{p}But then, {w=.2}why...、"
        fn "「Amaki-san... 」"
        
        show am 001 red with dis
        
        am "「Hm? 」"
        fn "「Amaki-san, is there something you can't do?{p}\ \ You know him the best,\n\ \ and you're the closest to him. 」"
        
        show am 005 red with dis
        
        am "「... 」"
        
        show am 002 red with dis
        
        am "「It's because I'm his caretaker. 」"
        "He spoke with the same bright and cheery face as\nalways.{w} That was the first time I could\ntell it was a finely crafted mask."
        
        show am 007 red with dis
        
        am "「If I told him his true feelings,\n\ \ he would surely follow them. 」"
        am "「If I said {w=.2}'don't you really want to stay here?'\n\ \ he would probably stop feeling conflicted.{p}\ \ But, I have no intention of doing so. 」"
        
        show am 004 red with dis
        
        am "「Whatever he chooses, I will support 100\%.{p}\ \ Shin-kun will be the one to decide in the end.{p}\ \ There's no meaning otherwise. 」"
        fn "「Isn't that cruel? 」"
        
        show am 007 red with dis
        
        am "「I think so.{w} But any advice I'd give\n\ \ would indirectly become an order.{p}\ \ {nw}"
        show am 004 red with dis
        extend "Nothing would change in that situation. 」"
        
        show am 005 red with dis
        
        am "「'Because Amaki said so' is unacceptable.{p}\ \ There's no meaning if he doesn't choose by himself.{p}\ \ {nw}"
        show am 004 red with dis
        extend "That's as far as a guardian's role goes. 」"
        am "「...{p}\ \ {nw}"
        show am 001 red with dis
        extend "That's why I came for your assistance. 」"
        fn "「Eh? 」"
        am "「Would you speak with him one more time?{p}\ \ What he needs now isn't a caretaker like me,\n\ \ but someone like you...{w=.2} a friend. 」"
        "Amaki-san's eyes were looking straight at me,\nfull of sincerity."
        am "「I won't force you to do so.\n\ \ Just seeing and listening to him is enough.{p}\ \ So, can I count on you? 」"
        fn "「Even if I go,\n\ \ I don't know if he'll talk to me... 」"
        
        show am 002 red with dis
        
        am "「It's{w=.2} because it's you that I'm asking. 」"
        fn "「... 」"
        "Amaki-san stressed 'because it's you,'\nand I couldn't answer back."
        "I want to see Shin-kun.{p}I want to see him and\ntalk to him clearly one more time."
        "But won't he just yell and shut me out?"
        
        show am 004 red with dis
        
        am "「I won't take your answer now.{p}\ \ But if you do want to, visit whenever you'd like.{p}\ \ Before you have to leave. 」"
        fn "「...I understand. 」"
        
        stop music fadeout 1
        pause 1
        play music free31
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        
        "When I answered back, Amaki-san grinned\nas he stood up and wiped off his pants."
        
        show am 007 red with dis
        
        am "「Sorry for taking so much of your time.{p}\ \ {nw}"
        show am 002 red with dis
        extend "I have to finish my shopping for dinner,\n\ \ so I have to leave now. 」"
        fn "「Right now?	 」"
        am "「Sometimes the fridge runs empty. 」"
        "Amaki-san winked at {w=.2}'sometimes,'\nand I nodded in understanding."
        
        show am 001 red with dis
        
        am "「Shin-kun will worry if I take too long.{p}\ \ See you. 」"
        fn "「See you then. 」"
    
        hide am with dis
        
        "As I waved back at the smiling Amaki-san,\nmy determination was finalized.{p}If I go, will something actually happen?"
        "I didn't have that much time left to worry.{p}If I don't go see him, I might not get\na second chance to do so."
        
        show am 001 red at center with dis
        
        am "「Oh yes, that's right. 」"
        "Amaki-san seemed to remember something\nas he came back to where I still stood."
        fn "「What is it? 」"
        
        show am 002 red with dis
        
        am "「Have you already at least kissed yet? 」"
        
        show park red at hshake
        
        fn "{size=+25}「PFFFT 」"
        "W-w-w-what!?{p}And wait, why is he even asking that?"
        "Did he hear about it from Shin-kun?\n{w=.2}No wait, he wouldn't say that."
        "It hit harder than expected,\nand I stood stock still unable to answer\nas I flapped my mouth like a fish."
        "I see.{w} So is this what they mean to\n'strike someone dumb?'{w} Or so I uselessly, {w=.2}\ncalmly analyzed myself."
        
        show am 001 red with dis
        
        am "「Kidding. {w=.2}Bye. 」"
        fn "「B-bye. 」"
        "As he waved away while acting silly,\nwas he really the same person who\nlooked so serious when talking about Shin-kun?"
        "I stupidly saw him off as\nI got a little uneasy."
    
        hide am with dis
        
        fn "「...{w} pft. 」"
        "When I couldn't see Amaki-san anymore,\nsomehow I felt like laughing."
        "It really felt like something had\nfallen off my chest."
        "I had been thinking gloomily until now, but now\nit was spilling out from the pit of my stomach."
        fn "「E-{w} eheh,{w} ahahaha 」"
        "I didn't really get what was so weird.{p}Just that it was too weird, and I laughed."
        "If a stranger saw me\nthey'd definitely think I've gone nuts."
        fn "「Hahah, {w=.2}hahahaha! 」"
        "This oppresive feeling that had always been\non my mind left,{w=.2} and in reaction to that\nI was laughing uncontrollably."
        "Next to the seesaw in the dusk-colored park,\nI kept laughing for a while."
        "I've decided that when tomorrow comes,\nI'm going to Shin-kun's house."
        
        jump end26

#######################################################      
label end26:
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

    jump day27


