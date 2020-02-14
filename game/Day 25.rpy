###Day 25
label day25:
    
    $ renpy.music.set_volume(1.0, 0.0, channel = "music")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound2")
    
    $ day = 25
    $ the_date = "August 25"
    $ event_name = "８月25日"
    
    if favorite == "tatsuki" or favorite == "kouya":
        window hide
        play music birds_chirping
            
        scene sky01 
        show text "{size=+130}August 25" at truecenter
        with Dissolve(.5)
        
        pause 3
        scene black with Dissolve(1)
        pause .4
        
    else:
        jump day26
        
    $ renpy.jump (favorite + "25")
    
#################################################
label tatsuki25:

    $ event_name = "The Result of Sorrow"

    scene old_house2 with sdis
    play music cicada01    
    
    "The Obon Festival passed by,\nand the height of summer passed with it."
    "Far away in the sky, the sun\ncontinued to emit its strong radiance."
    "Today, I was at the the\nMidoriya Group's workshop again."

    $ renpy.music.set_volume(0.5, 0.0, channel = "music")
    show tp 403 at center with dis

    tp "「Are you listening to me!?\nI said to do it straight and firm! 」"

    show tp at move_midright(0.5) with regmove
    show ta 006 at midleft with dis
    
    ta "「*Sigh*... Yeah, you don't need to\n\ \ shout so loud for me to hear you. 」"
    "For a few days... Things went\nback to the way they were before,\nas if nothing had happened."
    "Tatsu-nii wasn't his usual cheerful self, though."
    
    play sound crash20_b
    show old_house2 at vshake
    show tp at jump_up
    pause .2
    
    tp "「You're doing it wrong!\n\ \ How many times has it been today?\n\ \ Stop messing around!! 」"

    show ta 005 with dis
    
    ta "「...I'm sorry. 」"
    tp "「Did you think an apology would make it all better?{p}\ \ Enough. I don't need anyone who can't do their work. 」"
    
    hide ta with dis
    hide tp with dis
    show ni 002 at center with wipe_right
    
    ni "「Oh, please, do something like that earlier.\n\ \ I don't want anyone over here getting in the way. 」"
    
    show te 003 at farright with dis
    
    te "「The young boss isn't energetic,\n\ \ and now no one is in any better mood. 」"

    show cu 008 at farleft with dis
    
    cu "「Figures, still seems like he's in a lot o' shock. 」"
    "Normally, there're a lot of errors,\nbut he's never made this many before."
    "Every time, he'd just laugh off any mistakes,\nso I can't believe how he's\nhanging his head about it constantly."
    "Not being able to see Tatsu-nii's\nsmile is really depressing..."
    ni "「If this keeps up I won't be able to take it anymore.{p}\ \ {nw}"
    show ni 001 with dis
    extend "[fn]-kun, can't you do something about this? 」"
    fn "「Eh?{w} Why me? 」"
    
    show ni 002 with dis
    
    ni "「You get along best with him,\n\ \ and this affects you too,\n\ \ so of course you should be able to do it. 」"
    fn "「But, what should I do...? 」"
    "I'm helpless in this case.{p}The one I love is in trouble,\nbut there's nothing I can do."
    
    show ni 001 with dis
    
    ni "「So think about it.\n\ \ That's all I'm saying. 」"
    ni "「If you give up from the beginning,\n\ \ the things you should do will become impossible.\n\ \ That's what the boss taught me. 」"
    "I see... It's not that I'm not doing anything,\nit's that I haven't done anything."
    "If the one doing the cheering up is timid,\nthen that's no good at all."
    fn "「Thanks Akira-kun. I'll do that,\n\ \ and try to think about something I can do. 」"
    
    show ni 003 with dis
    
    ni "「Heh. If this goes on much longer I'll get bothered.\n\ \ I'm counting on you. 」"
    
    stop music fadeout 3
    play sound crash20_b
    scene workplace1
    show workplace1 at vshake
    "{size=+15}*Gashunk*{nw}"
    play sound2 metalic 
    extend "*crash*"   
    "Tatsu-nii must've screwed something up again.{p}That collapsing sound seemed metallic,\nand the crash echoed throughout the workshop."

    show te 003 with dis
    
    te "「Oh, how horrible... 」"
    te "「The Chief's winter plum tree... 」"
    "The lumber that Tatsu-nii had broken snapped and flew\ninto the air, then rolled on the ground."
    "The blade from the plane broke off,\nand a section of it cracked."
    
    hide te with wipe_right
    show ta 005 at center with dis
    
    ta "「Ah,{w=.2} I... 」"
    "A heavy air hung in the workshop."
    tp "「... 」"
    fn "「Um, Tappei-san. 」"
    tp "「Shut it. 」"
    fn "「Please don't be mad. Tatsu-nii also... 」"

    play sound don08
    show workplace1 at vshake
    
    tp "{size=+10}「Shut up. This is between him and me!\n\ \ Don't stick your face into this!! 」"
    "*Sniff* I can't say anything.{p}I think this is the first time he's been mad with me. 」"

    play music sad03 fadein 5
    show tp 408 at midright behind ta with dis
    
    tp "「...Go take a break. 」"

    show ta 006 with dis
    
    ta "「Huh? 」"
    tp "「I said you don't need to come to work anymore.\n\ \ If you can't do well enough, please don't. 」"

    show ta 004 with dis
    
    ta "「No, I can work. I don't need a break.\n\ \ Give me something to do...\n\ \ I feel weird if I'm not doing anything. 」"
    tp "「Don't chirp like some baby bird.\n\ \ My word is law, don't try to work your way around it.\n\ \ Now, just go. We'll figure something out about it. 」"
    
    show ta 005 with dis
    
    ta "「No way...I, I- 」"

    hide ta with dis
    show cu 008 at midleft with dis

    cu "「Young Master. 」"
    
    show tp 403 at jump_up
    
    tp "「Why did you stop moving your hands?\n\ \ The only one who can stay still is this guy.\n\ \ Two are out, so you have to pick up the pace. 」"

    hide cu with dis
    show te 003 at midleft with dis
    
    te "「In that case, go with the young boss. 」"

    show tp 401 with dis
    
    tp "「[fn], good work for everything until now.{p}\ \ You don't have a buddy around anymore,\n\ \ so you probably don't want to hang around. 」"
    tp "「We should end your part-time work here too. 」"
    fn "「No, I want to help out more.{p}\ \ I've gotten closer to everyone in the Group,\n\ \ and I don't want to end things like this. 」"

    hide te with dis
    show cu 008 at midleft with dis
    
    cu "「Yeah, tha's just too sudden. 」"

    show tp 403 with dis
    
    tp "「Zip it. It doesn't change a thing,\n\ \ no matter who talks.{w} Thanks for you work,\n\ \ it's been fun. Later. 」"
    tp "「You can come get your unpaid wages in a bit. 」"
    tp "「The rest of you, get back to work. 」"

    hide tp
    hide cu
    with dis
    show ta 002 at center with dis
    
    ta "「Now, where do we go?{p}\ \ I finally get some time off, so I ought to use it.{p}\ \ Maybe we'll go to Tora's place. 」"
    fn "「Hey, Tatsu-nii. 」"

    show ta 001 with dis
    
    ta "「What is it? 」"
    fn "「I'm wondering how the plane is,\n\ \ so let's take a look at it after this.{p}\ \ Maybe something happened. 」"

    show ta 008 with dis
    
    ta "「Nah... It's useless.{p}\ \ I already took a look, myself. 」"
    ta "「Getting it down from the tree's a huge project.{p}\ \ Even then, we can't get it quick and easy.{p}\ \ Then, if it fell, the whole thing'd probably break. 」"
    ta "「Short version is that we'll need to\n\ \ really improve it before it can actually fly.{p}\ \ There's no time or money left for that. 」"

    show ta 006 with dis
    
    ta "「...Even then, I can't.{p}\ \ I don't have the skill or the know-how,\n\ \ I'm just useless. 」"
    fn "「Don't say that.{p}\ \ You promised.{p}\ \ You said you'd fly with me into the sky. 」"

    show ta 005 with dis
    
    ta "「I promised, and I can't deliver on it... 」"
    "I can't say anything when he's like this.{p}I can't say anything to break this silence,\nand I can't even move."
    "The humid air coiled around me,\nand the heat and heaviness clouded my thoughts."

    stop music fadeout 1.5
    play sound door_slide

    sg  "「Hohoho! Excuse me. 」{w} {nw}"    
    show ta at move_midleft(0.5) 
    extend "{w=.3}{nw}"
    show sg 002 at midright with dis
    show ta 006 with dis
    
    ta "「Uncle... 」"
    sg "「Excuse my abruptness, but can I ask you to\n\ \ mend my low dining table?{w} Lately it has been wobbly,\n\ \ and it's hard to eat off. 」"

    show ta 008 with dis
    
    ta "「Uncle, please ask Pa to fix that. 」"

    show sg 001 with dis

    sg "「If I ask the Master, he'd refuse out of business.{p}\ \ You have some free time, so I came over to ask for\n\ \ your help... How about it? Will you do it? 」"

    show ta 005 with dis
    
    ta "「Sorry, I'm not in the mood.{p}\ \ Plus, I don't have the ability. 」"
    sg "「It's simply constructed, so it's not that difficult.{p}\ \ Nothing so complex as the works out of\n\ \ the woodshops of Edo Sashimonoya. 」"
    sg "「Just a normal low dining table.{p}\ \ If it's you, then you should be able to do it. 」"
    fn "「Let's do it, it's not like we have other stuff to do.{p}\ \ Sounds fun... Right? 」"

    show ta 008 with dis
    
    ta "「Hmm. Well, in that case, I'll take a look at it. 」"

    show sg 002 with dis

    sg "「Thank you, you're a big help. 」"

    show ta 006 with dis
    
    ta "「Don't get your hopes up. 」"

    show sg 001 with dis

    sg "「I think I'll leave it in your care.{p}\ \ When you have fixed it, please bring it back to me.{p}\ \ You can take your time with it. 」"

    hide sg with dis
    show ta at move_center(0.5)
    
    ta "「Now, how do we start this thing? 」"

    show ta 001 with dis
    
    "Tatsu-nii carefully began inspecting the table\nShigure-san had brought along."
    "He turned it over a few times,\n{nw}"
    show ta 005 with dis
    extend "checked it out with his hands,\n{nw}"
    show ta 008 with dis
    extend "and examined its every corner."

    show ta 001 with dis
    
    ta "「Did the leg get worn down?\n\ \ Maybe it'll be fine with just replacing this part... 」"
    ta "「The construction's excellent,\n\ \ but I wonder if I can take it to pieces. 」"
    "Tatsu-nii began closely inspecting\nthe table as if I wasn't there.{p}His concentration is amazing. Is it a family thing?"
    "In any case, I'm glad he's gotten his motivation back."
    
    jump end25
    
    
#####################################################    
label kouya25:
    
    $ event_name = "First Day at a New Job"
    
    scene hentry with dis
    
    fn "「All right, I'm going out. 」"
    "It was morning.{p}As I was tapping the tip of my shoes\nonto the floor, I called out."
    "In my hand was a lodging set:\nIn other words, my entire luggage in a bag.{p}Same form as it was a while ago."
    "Starting from now, I'll be heading to Kouya's place.{p}Starting from today, I'll be starting\nas an 'assistant'."
    "I asked for this myself,{w=.2} but I'm feeling\na bit nervous after all.{p}Ever since I woke up,\nthe inside of my mouth felt dry."
    gm "「Okay.{w=.2} Be careful on your way over.{p}\ \ Don't be too much of a bother to your host now. 」"
    "Grandma stuck her head out of the living room,{w=.2}\nwhere she tossed out that line\nI've heard countless times."
    "I think I can remember this\nhappening the last time I went out.{p}If I think about it like that, it's kind of funny."
    fn "「Yeah, I know.{p}\ \ And sorry,{w=.2} for having to go back so soon\n\ \ and making so much noise. 」"
    gm "「Oh, it's okay.{w} You look like you've\n\ \ been having fun lately, so that's enough.{p}\ \ Go and make a lot of nice memories. 」"
    fn "「Okay, thanks.{p}\ \ I'm heading out. 」"
    gm "「Okay,{w=.2} take care. 」"
    "Grandma's smiling face saw me out\nas I left the house."
    
    play sound tm2_slidedoor000
    stop music fadeout 1
    scene black with wipe_right
    scene rice_paddy with wipe_right
    
    "Now I'm going to get a bit busier.{p}It's possible that I won't be coming back here{w=.2}\nuntil the day before I return to the city."
    "I got a little lonely, thinking about it like that,\nand I felt kind of apologetic.{w} It was like the\nsound of hollow wind blowing in my heart."
    "But still,\nI was also looking forward to things.{p}Everything starts after this."
    "And my mind was full of curiosity.{p}Because of that, the apologetic feeling\nwas relatively faint."
    "There's also what Grandma said.{w} 「Go and make\na lot of nice memories. 」{w} In that case,\nI won't need to worry about things too much."
    "Unconsciously my feet stopped moving,{w=.2}\nand I looked back around.{p}Grandpa's house looked somewhat far away."
    "As I steadily looked at it,\nI screwed up my courage and muttered to myself."
    "There's three more days before the contest,\nincluding today, meaning I have only\n72 hours to help out."
    fn "「All right, I'm off. 」"
    "Time's extremely limited,\nbut I'll do it,{w=.2} perfectly."

    scene black with wipe_right
    scene kouya_apartment with wipe_right
    play music daily05
    
    $ event_name = "Together With Kouya"
    
    "When I arrived, Kouya was already outside\nhis run down-looking apartment."

    play sound phone_pickup
    pause .5
    play sound load_gun
    
    "He was crouching in front of his motorbike,{w=.2}\nand fiddling with it for some reason."
    
    show ka 001 at center with dis
    
    fn "「Good morning,{w=.2} Kouya. 」"
    ka "「Oh,{w=.2} morning. 」"
    "Kouya greeted me with a smile,\nand a small raise of his hand."
    "He had work gloves on,{w=.2} so I figure Kouya\nmust be trying to fix the motorcycle.\nI wonder what happened?"
    fn "「What's wrong?{w=.2} Did the bike get busted? 」"
    ka "「Nah.{w=.2} I'm just doing a little tune-up.{p}\ \ You'll be riding along in a bit after all.{p}\ \ I thought it'd be a good thing to do. 」"
    fn "「Ohh.{w=.2} Well, thank you for your consideration.{p}\ \ But I didn't know you could fix bikes.{p}\ \ Kinda surprising. 」"
    ka "「When you ride one you can do more or less do that,\n\ \ right?{w} I'm almost done,{w=.2}\n\ \ so go put your stuff inside. 」"
    fn "「Okay.{w=.2} Where's the key? 」"
    ka "「It's open.{w=.2} The spare key is on top of the table,\n\ \ so lock up when you come out. 」"
    fn "「Don't you have any luggage, Kouya?{p}\ \ Like instruments or stuff? 」"
    "I noted that Kouya seemed to be empty-handed.{p}I'm sure he had a guitar with him the other day,{w=.2}\nbut is it okay for him to go without it?"
    ka "「Not especially,{w=.2} it's pretty much\n\ \ all over there already.{w} Since there's so many,\n\ \ I put one over there yesterday. 」"
    fn "「I see.{p}\ \ All right, I'll put my stuff away for now. 」"
    ka "「Sure. 」"

    hide ka with dis
    
    "I picked up my bag, then went to Kouya's room."
    
    scene black with wipe_right
    scene bedroom with wipe_right
    
    "It hasn't even been three days since I've been here,\nbut I feel like I'm already getting used to it,{w=.2}\nlike it's also my room now."
    fn "「Maybe because I cleaned it up last time...? 」"
    "That's probably one factor.{p}...I'll just{w=.2} quietly leave that memory aside for now."
    "I swept aside my idle thoughts, I went in and\n{nw}"
    play sound bosu34
    extend "put my stuff down in the corner."
    "After that, I picked up the spare key from the table,\nand turned on my heel to leave."
    "I put my shoes on then turned the doorknob.{p}Right before I crossed that boundary,"
    fn "「So once again,{w=.2} I'm in your care. 」"
    "I bowed my head a little in this empty room.\nThere was no reason. I just felt like it."
    
    scene black with wipe_right
    scene kouya_apartment with wipe_right
    
    "I took the key with me as I went back to Kouya,\nwho, having finished his maintenance,{w=.2}\nwas stowing his tools and gloves under the seat."
    
    show ka 001 at center with dis
    
    fn "「Results,{w=.2} all good? 」"
    "I tried asking.{p}{nw}"
    play sound door_close
    extend "After shutting the seat with a snap,\nKouya replied back."
    
    show ka 003 with dis
    
    ka "「Yeah, that's everything.{p}\ \ It should run smoothly today, too. 」"
    fn "「I see,{w=.2} that takes a load off my mind. 」"
    
    show ka 001 with dis
    
    ka "「Well,{w=.2} the bike's fine, but if I\n\ \ have an accident that'd be the end of me. 」"
    fn "「Don't say things like that.{p}\ \ I mean, nothing like that would happen would it? 」"
    
    show ka 009 with dis
    
    ka "「I wouldn't know.{p}\ \ There are a lot of mysterious things\n\ \ that can happen in life. 」"
    "As he cracked that joke,{w=.2}\nKouya handed over a helmet to me."
    
    show ka 001 with dis
    
    ka "「So, in that case,{w=.2}\n\ \ we should have good contingency plans. 」"
    fn "「Is it okay to leave it at that? 」"
    
    show ka 013 with dis
    
    ka "「Shut up,{w=.2} it's not like I'll be falling\n\ \ right from the start so this is fine. 」"

    hide ka with dis
    
    "Kouya put on his own helmet.{p}I moved to imitate that and put on my own helmet\nthe way I was shown before."
    ka "「Is it on right? 」"
    fn "「Yeah,{w=.2} I think it's fine. 」"
    ka "「All right then. 」"
    "After a quick final check, Kouya got on the bike."
    ka "「You can get on now. 」"
    fn "「'Kay,{w=.2} excuse me... 」"
    "I took the cue and gingerly sat down\nin the back seat.{w} I've done it so many times,{w=.2}\nbut my heart keeps pounding every time it happens."
    ka "「It's dangerous,{w=.2} so hold on tight, okay? 」"
    fn "「O-{w=.2}okay. 」"
    "I put my arms around his waist as he said so,\nthen grabbed on.{w} This also happened a lot,{w=.2}\nand it makes my heart pound even faster."
    "I was a little worried that Kouya\nmight actually notice my increased heartbeats."
    ka "「All right, let's go then. 」"

    play sound load_gun
    pause 1.5
    play sound motor_engine
    
    "I put my worries aside for the moment,{w=.2}\nas Kouya finished up his preparations\nand started up the engine."
    "Then the bike we were riding on\nraced through the peaceful countryside."

    stop sound fadeout 3
    stop music fadeout 3
    scene black with wipe_right

    $ event_name = "At the Studio"
    
    play music shop02
    scene music_shop with wipe_right
    
    "Whenever Kouya and the band need a place\nto practice,{w=.2} they use a studio\nestablished in a certain instruments store."
    "This store was where Kouya had a part-time job,{w=.2}\nand also the place where he parked his bike\nwhen we came to meet Keisuke-san."
    "The interior and exterior both give a calming\nimpression,{w=.2} and rather than seeming like a\nstore it feels more like a kind of museum."
    "The manager greeted us with the habitual 「welcome 」\nand an incline of his head,{w=.2}\nthen Kouya brought me further inside."
    
    scene black with wipe_right
    scene studio with wipe_right
    show ke 001 at center with dis
    
    ke "「Ohh, you're finally here, [fn]. 」"
    "Just past the door leading to the studio, there\nwere three people.{w} Then when Keisuke-san noticed\nme first,{w=.2} he immediately called out to me."
    fn "「Hehe,{w=.2} I guess I'll be a burden here on out. 」"
    
    show ke 006 with dis
    
    ke "「Yeah, I'm counting on it.{p}\ \ Seriously counting on it. 」"
    fn "「Wha!? 」"
    "Keisuke-san suddenly caught me in a headlock,{w=.2}\nwhere he proceeded to give me a noogie."
    fn "「Wai-{w=.2} Keisuke-san, stop!{w} M-my heaaad... 」"
    
    show ke 003 with dis
    
    ke "「What's that!?{w} Don't stop!? 」"
    fn "「What!?{w} What are you talking about!? 」"
    who "「Yes, yes, it's okay if you horse around,{w=.2}\n\ \ but you'd better do your work properly. 」"
    "While the two of us were making a racket, a cold,\nadmonishing voice suddenly rung out in the room.{p}{nw}"
    show ke 001 with dis
    extend "Keisuke-san then let go of me."
    
    if meet_band != True:
        jump kouya25_band_meet

    #######################################################
    label kouya25_band_reunion:
        
        $ event_name = "Reunion of the Three Guys"  
        
        "Surprised, Keisuke-san looked up.{p}The voice we'd heard had come from a canary birdman.{p}Next to him stood a quiet tortoiseshell cat."
        
        show yu 001 at farleft
        show jn 001 at farright
        with dis
        
        yu "「It's been a while, [fn]-kun.{p}\ \ {nw}"
        show yu 002 with dis
        extend "I hope you're doing well? 」"
        fn "「Yeah I'm fine, thanks.{p}\ \ It's great to see everyone else doing all right too.{p}\ \ Nice seeing you again too, Jun-kun. 」"
        jn "「...yeah. 」"
        "Jun-kun gave a little nod of his head.{p}He's as conservative of his word usage as ever."
        
        show yu 003 with dis
        
        yu "「And you, Keisuke.{p}\ \ [fn]-kun's just started coming over to help,{w=.2}\n\ \ so couldn't you welcome him better? 」"
        
        show ke 004 with dis
        
        ke "「Ohh,{w=.2} that's just like you, Yuuki.{p}\ \ You really are a high level straight man,\n\ \ all the time. 」"
        yu "「I'm not your straight man.{p}\ \ Stop pulling these antics, and start\n\ \ working properly when it's time! 」"
        "Yuuki-san pointed his index finger\nat Keisuke-san as he scolded him.{p}This little dynamic hasn't changed at all either."
        
        show yu 001 with dis
        
        ke "「Yeah, yeah...{p}\ \ It feels like a really late time to do it,{w=.2}\n\ \ but how about we introduce ourselves again? 」"
        
        show ke 001 with dis
        
        ke "「Now, since this is the second time,\n\ \ I'll be a bit more serious.{p}\ \ First off is the tortoiseshell cat, Jun Nekonishi. 」"
        ke "「He's the youngest of us,\n\ \ a first-year highschooler.{p}\ \ He's in charge of bass. 」"
        ke "「And, as you know, he's really quiet.{p}\ \ Still, he's a seriously good guy.{p}\ \ And now you say something,{w=.2} Jun. 」"
        
        show jn 006 with dis
        
        jn "「...Looking forward to working with you. 」"
        ke "「Next off, the one next to Jun is Yuuki Torii.{p}\ \ He's a kind of canary. 」"
        ke "「His eyes are cute, so he might look young,\n\ \ but he's really 18 so he's older than you. 」"
        ke "「He's in charge of the vocals.{p}\ \ He can also play the keyboard,\n\ \ but rarely ever does. 」"
        ke "「And that's about it.{p}\ \ Your turn to say something, Yuuki. 」"
        
        show yu 003 with dis
        
        yu "「You're an interesting one, that's for sure...{p}\ \ {nw}"
        show yu 002 with dis
        extend "Well, I look forward to working with you,\n\ \ [fn]-kun. 」"
        ke "「And now,{w=.2} next is Kouya... I don't think\n\ \ you need an intro, so we'll skip him.{p}\ \ Honestly, you probably know better than me. 」"
    
        scene studio with dis
        show ka 001 at midleft
        show ke 001 at midright
        with dis
        
        ka "「Maybe so.{w} Anyway,{w=.2}\n\ \ I'll be counting on you. 」"
        ke "「Right,{w=.2} and now a word from me, Keisuke Hirama.{p}\ \ I'm the leader and in charge of the drums.{p}\ \ {nw}"
        show ke 002 with dis
        extend "...Yeah,{w=.2} I'm the leader, got it? 」 "
        yu "「You don't need to say that twice.{p}\ \ No one doubts that. 」"
        
        show ke 001 with dis
        
        ke "「Really? Okay then.{p}\ \ Anyway, it's cooler to be mysterious\n\ \ so I'll leave the intro at that. 」"
        
        jump kouya25_musikus
    
    ##################################################
    label kouya25_band_meet:
            
        $ event_name = "First Time with the Three Guys"
        
        "I fixed up my hair, and raised my head.{p}Over where I heard the other voice come from,{w=.2}\nI saw a birdman."
        "He was completely green from head to toe,\nand about as tall as I am."
        "He had a certain brightness in his eyes,{w=.2}\nwhich gave him a youthful impression."
        
        show yu 001 at farleft
        show jn 001 at farright
        with dis
        
        who "「It's the first time Jun and I have met him,\n\ \ you know?{w} We have to do the introductions,{w=.2}\n\ \ or there's nothing that can be done about things. 」"
        "For a second time,{w=.2} he spoke in a strict voice."
        
        show ke 002 with dis
        
        ke "「I guess that's true.{p}\ \ Right, way too careless of me.{p}\ \ {nw}"
        show ke 001 with dis
        extend "All right,{w=.2} time to start with the intros. 」"
        
        $ encounter_jun = True
        
        ke "「First off is the tortoiseshell cat, Jun Nekonishi. 」"
        ke "「He's the youngest of us, a first-year highschooler.{p}\ \ He's in charge of bass. I think you've noticed,\n\ \ but he's really quiet. 」"
        ke "「On the other hand,{w=.2} he's good at expressing\n\ \ things with his face so if you watch him\n\ \ you'll know what he wants to say. 」"
        ke "「In any case, he's an awesome guy,\n\ \ you should get along well with him.{p}\ \ Now,{w=.2} say something, Jun. 」"
        
        show jn 006 with dis
        
        jn "「...Looking forward to working with you. 」"
        
        $ encounter_yuuki = True
        
        ke "「Next off, the one next to Jun is Yuuki Torii.{p}\ \ He's a kind of canary. 」"
        ke "「His eyes are cute, so he might look young,\n\ \ but he's really 18 so he's older than you. 」"
        ke "「In this band he does the vocals\n\ \ and acts the straight man. 」"
        
        show yu 003 with dis
        
        yu "「Wait, what's this about being a straight man? 」"
        
        show ke 002 with dis
        
        ke "「By the way, the wise guy's probably me. 」"
        yu "「I'm asking you a question, here. 」"
        
        show ke 001 with dis
        
        ke "「He can also play the piano or keyboard,{w=.2}\n\ \ but rarely ever does.{w} And that's about it.{p}\ \ Your turn to say something, Yuuki. 」"
        yu "「Ignoring things is your specialty, isn't it...?{p}\ \ {nw}"
        show yu 002 with dis
        extend "Oh well,{w=.2} I look forward to working with you,\n\ \ [fn]-kun. 」"
        ke "「And now,{w=.2} next is Kouya...\n\ \ I don't think you need an intro, so we'll skip him.{p}\ \ Honestly, you probably know better than me. 」"
    
        scene studio with dis
        show ka 001 at midleft
        show ke 001 at midright
        with dis
        
        ka "「Maybe so.{w} Anyway,{w=.2}\n\ \ I'll be counting on you. 」"
        ke "「Right,{w=.2} and now a word from me, Keisuke Hirama.{p}\ \ I'm the leader and in charge of the drums.{p}\ \ {nw}"
        show ke 002 with dis
        extend "...Yeah,{w=.2} I'm the leader, got it? 」 "
        yu "「You don't need to say that twice.{p}\ \ No one doubts that. 」"
        
        show ke 001 with dis
        
        ke "「Really? Cool.{w} Also, I'm 20.{p}\ \ That makes me the only legal adult here.{p}\ \ So if you have any problems, come talk to me. 」"
    
    ###################################################
    label kouya25_musikus:
            
        $ event_name = "Welcome to Musikus"
        
        ke "「And now,{w=.2} we'll need\n\ \ to introduce you to the band, [fn]...{p}\ \ Kouya, I leave that to you. 」"
        
        show ka 005 with dis
        
        ka "「Me?{w=.2} ...well, all right.{p}\ \ {nw}"
        show ka 001 with dis
        extend "Let's see...{w=.2} He's my childhood friend,\n\ \ [fn] [ln]. 」"
        ka "「He's visiting Minasato on vacation,\n\ \ but he specifically requested to help out here. 」"
        ka "「There's been some changes here and there,{w=.2}\n\ \ but he's a good guy at heart\n\ \ so I'm sure he'll work well with us. 」"
        ka "「All right, [fn].{p}\ \ Your turn to say something. 」"
        "Kouya urged me on with a light hand on my shoulder.{p}After giving a slight nod,{w=.2} I looked steadily\nat everyone."
        
        show yu 001 at farleft
        show jn 001 at farright
        with dis
        
        fn "「Umm, {w=.2}I'm sorry for offering so suddenly to\n\ \ become an assistant here.{w} However, I want to\n\ \ help everyone, so I plan on doing my best. 」"
        fn "「I think it will only be for a short time,{w=.2}\n\ \ but I look forward to working with you all. 」"
        "After I finished my short speech,\neveryone replied back with a 「same here. 」{p}I started feeling a warmth in my chest."
        ke "「Now, everyone's said their part.{p}\ \ Oh yeah,{w=.2} since you're now our temporary manager\n\ \ and official member of our band... 」"
        ke "「There's one last thing.{w=.2} [fn]- 」"
        "Keisuke-san paused.{w} I felt a bit of tension\nin the surrounding air,{w=.2} which made me\nreflexively straighten out my back."
        "Everyone else also seemed to sense it,{w=.2}\nas their faces became a touch more serious\nthan they were earlier."
        "Keisuke-san took a quick glance\nto the sides to check on the others."
        "After a cough to clear out his throat,{w=.2}\nhe turned to face me once more.{p}And then his mouth opened up again."
        
        show ke 006 with dis
        
        ke "「Welcome...{w=.2} to Musikus! 」"
        
        $ event_name = "The Uncharted World"
        
        scene black with sdis
        stop music fadeout 3
        
        "Musikus.{w} The German word\nfor instrumentalists and musicians."
        "That was the name of Kouya's band."
        "With four members: a horse,{w=.2}\na dog,{w=.2} a cat,{w=.2} and a bird."
        "They each resemble the four animals represented\nin that famous Grimm's fairy tale\n\"The Bremen Town Musicians\"."
        "Those are the performers they had their eyes on."
        "...or rather, with their combined wishes\nto be a group of musicians like them,\nthat led to their naming of the band like this."
        
        play music shop02 fadein 3
        scene studio with sdis
        show ka 001 at midleft
        show ke 001 at midright
        show yu 001 at farleft
        show jn 001 at farright
        with dis
        
        ka "「Still,{w=.2} in the fairy tale they never\n\ \ actually make it to Bremen, and they didn't become\n\ \ an actual band, either. 」"
        ka "「So because of that when the time came\n\ \ to pick a name,{w=.2} we didn't go with\n\ \ \"The Bremen Town Musicians\". 」"
        "In the original story, the four animals came\nacross a hut in the forest being robbed by thieves,\nand after chasing them away they lived in it."
        "And that's where it ended.\nAt least, that was the explanation that I got\nwhen I asked."
        fn "「Huh...{w=.2} I see, then. 」"
        ke "「Well,{w=.2} that's about as much as we know.\n\ \ Let's start practice.{w} [fn],\n\ \ your work for today will be to listen. 」"
        fn "「To... Listen? 」"
        ke "「Yeah.{w} From what Kouya's said, you\n\ \ never did much music, right? 」"
        fn "「Yeah,{w=.2} the recorder is the last thing I've done... 」"
        "I felt kind of awkward after saying that.{p}It's nothing to get all ashamed about,{w=.2}\nbut compared to these guys I'm nothing."
        ke "「So, in that case,{w=.2} you're in a completely different\n\ \ world from us, which means that you can give\n\ \ an honest opinion and stuff...{w} do you get it? 」"
        fn "「Well,{w=.2} sort of. 」"
        "In other words, I can give the opinion of an\nordinary person who'd come over to a music shop to\nbuy a CD,{w=.2} or something like that."
        "And evidently, that's my position."
        ke "「We can tell when we mess something up,{w=.2}\n\ \ so you don't have to point that out. 」"
        ke "「Right now what we want is the opinion\n\ \ of someone who hasn't heard us before. 」"
        
        show ke 002 with dis
        
        ke "「That's where you come in.{p}\ \ You listen to our performance,{w=.2}\n\ \ and then honestly tell us what you think. 」"
        ka "「Pretty much which parts were good,\n\ \ which parts weren't that exciting,{w=.2}\n\ \ that sort of thing. 」"
        fn "「O-{w=.2}okay.{w} I'll try my best. 」"
        "Since I wasn't very confident,\nI only slightly nodded my head.{p}It probably showed up on my face too."
        "It must have, as when Yuuki-san looked at me\nhe said:"
        
        show yu 002 with dis
        
        yu "「You don't need to stiffen up so much.{p}\ \ Just relax and listen to us play. 」"
        
        show jn 006 with dis
        
        jn "「... 」"
        "Jun-kun also suddenly nodded his head\nin agreement with Yuuki-san's comment."
        "Hey, wait,\ncheering up the guy who came to help is kinda..."
        fn "「Okay, thanks.{p}\ \ I'll try my best to start with. 」"
        "I laughed a bit in response to help\ndispel the negative thoughts within me."
        ke "「Yeah, we're counting on you.{p}\ \ All right everyone,{w=.2} get ready. 」"
    
        scene studio with wipe_right
        stop music fadeout 5
        
        "With one word from Keisuke-san\neveryone picked up their instruments."
        "Kouya and Jun-kun tuned their strings,{w=.2} and\nKeisuke-san made minute adjustments to his drums."
        "The air in the room grew thick with tension,{w=.2}\nand only the sounds of their\ninstruments could be heard."
        "It felt so electric in here.{w} It's almost\nlike that friendliness from earlier was a sham,{w=.2}\nand now everyone was the picture of seriousness."
        "I even felt my own emotions change,\nsharpening up my expression.{p}I could tell that much..."
        "Before long, all the preparations were finished,{w=.2}\nand everyone exchanged looks with a nod."
        "That was the cue."
        "Keisuke-san set up the rhythm, which Kouya and\nJun-kun picked up.{w} Each and every sound\nlined up,{w=.2} packing together to make one song."
        
        play music free0451
        
        "The tune had a bit of an upbeat tempo.{p}Just listening to it made my heart dance,{w=.2}\nkeeping time with the melody."
        "A short moment after the introduction,{w=.2}\nYuuki-san's clear voice\nadded itself into the mix."
        "That voice,{w=.2} combining together with the instruments,\ncame together and formed a deeper,\nmore complete sound."
        "I thought,{w=.2} 'this is absolutely amazing.'{p}I couldn't do anything but admire it."
        "I was paying so much attention that I forgot\nI was supposed to do something else too."
        
        stop music fadeout 3
        
        "The moment the song was over,\nthe room became silent again.{p}{nw}"
        play sound applause
        extend "At this point I stood up and applauded."
    
        show ka 001 at midleft
        show ke 001 at midright
        show yu 001 at farleft
        show jn 001 at farright
        with dis
        play music pops_008
        
        fn "「You were all amazing!{w} Really! 」"
        "I couldn't put it into any better words,{w=.2}\nso I just gave my honest feelings.{p}That was the greatest praise I could give them."
        
        show ke 002 with dis
        
        ke "「Whee,{w=.2} thanks a lot.{p}\ \ Well, that wasn't bad, was it? 」"
        fn "「Yeah!{w} I was so touched by it! 」"
        
        show ke 006 with dis
        
        ke "「I'm glad you thought so. 」"
        yu "「But because of this break,{w=.2}\n\ \ we only managed a part of what we could do. 」"
        yu "「Sorry,{w=.2} this last-minute playthrough was because\n\ \ I had to go grave-visiting. 」"
        
        show jn 006 with dis
        
        jn "「Me too... 」"
        "Jun-kun followed up on Yuuki-san\nwith an apologetic looking expression."
        "That reminds me,{w=.2}\never since I've stayed over at Kouya's\nhe's never once went to band practice."
        "He'd strum his guitar at night,{w=.2}\nbut that was it."
        "I see,{w=.2} since those two were gone\nthat meant he was on break.{w} Maybe that's\nwhy he let me lodge at his place for a bit."
        ke "「Don't worry about it,{w=.2} you have to care\n\ \ about things like that.{w} {nw}"
        show ke 001 with dis
        extend " But Kouya,\n\ \ you still seem off from yesterday. 」"
        fn "「Eh? 」"
        "When Keisuke-san mentioned that,{w=.2}\na strangled voice came out of my mouth."
        ka "「Yeah...{w} I've had something\n\ \ on my mind lately. 」"
        "As Kouya's hand kept opening and closing,\nhe muttered almost to himself."
        "This might be my imagination,{w=.2} but I think I could\nsee a shadow pass over his face."
        fn "「Kouya...{w} Are you okay? 」"
        "I spoke up without thinking about it."
        "I must have said what everyone was thinking,{w=.2}\neven if I didn't know the intricacies of music."
        "But when it comes to Kouya,\nI should have a leg up on that."
        "Because of that,{w=.2} I can't stay quiet."
        
        show ka 002 with dis
        
        ka "「Yeah, thanks.{p}\ \ But you don't need to worry about me.{p}\ \ I'll be back to normal soon. 」"
        "He returned with a vague smile.{p}As for me, I couldn't say anything beyond that."
        
        show ka 001 with dis
        
        ka "「Sorry guys.{w} I think I'll get back to normal\n\ \ if I keep at it, so let's move on to the next one. 」"
        ke "「All right.{w} For now then,{w=.2}\n\ \ we'll do the same song from the top again. 」"
        
        stop music fadeout 3
        scene black with sdis
        pause 2
        
        $ event_name = "Timing"
        
        "Practice ran on well into the night,\nbut eventually it was time to stop."
        "During all that time,\nI'd occasionally get drinks\nand listen to them play."
        "To be honest,{w=.2}\nI don't think I was all that helpful."
        "But when I whispered\n'Man,{w=.2} I don't think was able to do much today...'"
        
        scene studio with sdis     #!#[env colorall=true grayscale=true rgamma=1.3 ggamma=1.1]
        show jn 001 with dis       #!#Color near sepia
        
        jn "「It's okay.{w} You were a big help. 」"
        jn "「This time,{w=.2}\n\ \ everyone had more fun than usual. 」"
        "Jun-kun said something like that to me."
        "Since it didn't seem like he\nwas trying to reassure me,{w=.2}\nI was a little happy.{w} And a little relieved."
        "Still,{w=.2} there was something else on my mind."
        
        scene black with sdis
        scene bedroom night with sdis
        show ka 001 night at center with dis
        play music free58
        
        fn "「Hey,{w=.2} Kouya. 」"
        ka "「Hm?{w=.2} What? 」"
        "I called out to Kouya,\nwho was lying in bed reading a magazine.{p}He raised his head up as he replied back."
        fn "「Wanna go out for a walk? 」"
        ka "「A walk...?{p}\ \ Fine with me, but where to? 」"
        fn "「Just...{w=.2} out. 」"
        "I avoided that question.{p}It'd be fine to say so,{w=.2} but I needed a reason.{p}There's something I wanted to talk to him about."
        ka "「...All right.{p}\ \ Let's go. 」"
    
        play sound standup
        
        "Kouya stood up and put his magazine down,\nthen we went out."
    
        scene black with wipe_right
        scene rice night with wipe_right
        play sound night_insects loop
        
        "I moved in a quick march just a few steps\nin front of Kouya.{w} Unexpectedly, he said\nnothing and just followed."
        "However,{w=.2} that meant\nwe didn't talk about anything."
        "Underneath this noiseless night sky,{w=.2}\nonly the cries of the insects and the sounds\nof our footsteps shook the air."
        "In this place,{w=.2}\nthere was nothing else but that."
        "But as we walked along there was one new sound\nthat reached our ears."
    
        scene black with sdis
        
        ka "「This is...{w=.2}\n\ \ the place you came to. 」"
        "A few moments before I stopped,{w=.2}\nKouya spoke up.{p}I silently confirmed it."
        
        scene black with wipe_right
        scene river night with wipe_right
        play sound river_flow loop
        
        "Over there was the riverbed.{p}The time I found Kouya,{w=.2} it was here."
        
        play sound2 step13b
        
        "I walked over the night dew-ridden grass,{w=.2}\nall the way to the water's edge.{p}Kouya followed along behind me."
        fn "「Y'know,{w=.2} whenever I think about you,\nyou're usually here. 」"
        
        show ka 001 night at center with dis
        
        ka "「That's true...{p}\ \ And that time I told you why I left home,{w=.2}\n\ \ it was over here. 」"
        "Yeah,{w=.2} I can say it all started\nhere when I think about Kouya.{p}That's why I wanted to talk over here."
        "I wondered if what I felt\nearlier today was all in my mind.{p}That's what I came here to check."
        "I turned around,{w=.2}\nand faced him from the front.{p}Then I started the ball rolling."
        fn "「Kouya.{p}\ \ Are you still worried about something?{p}\ \ Earlier today,{w=.2} you seemed... Different. 」"
        ka "「{cps=5}. . . 」"
        "He didn't respond.{p}He just quietly and slowly breathed in and out."
        "It faded out along with the insects' noises.{p}Only the sound of water hit my ears."
        "And once again along with the return of\nthat nightly chorus, Kouya's mouth opened up."
        ka "「...It's not so much worrying,{w=.2}\n\ \ more... impatience. 」"
        fn "「I thought so.{w=.2} Is it about the promise? 」"
        ka "「Yeah...{w} {nw}"
        show ka 014 night with dis
        extend " Being in a hurry won't help,\n\ \ and I know it's going down the wrong way,{w=.2}\n\ \ but I can't help but feel that way. 」"
        "Kouya slightly shifted his eyes skyward as he\nsounded shameful.{w} I'm almost sure those eyes\nreflected the entire starry night sky."
        "I wonder what he sees up there?"
        "In that upraised expression,{w=.2}\nI could see a bit of loneliness in it."
        
        show ka 001 night with dis
        
        ka "「So really,{w=.2} it's not like I'm really worried.{p}\ \ This is all just something that I have to do alone.{p}\ \ I'll show you I can get past this. 」"
        
        show ka 002 night with dis
        
        ka "「...Thanks, [fn].{w} You...{w=.2}\n\ \ were worried about me, weren't you.{p}\ \ You saying that makes for nice encouragement. 」"
        fn "「Kouya... 」"
        "This time I said nothing. In the end,\nall I really can do is worry. That sense of\nhelplessness tormented me in my chest."
        "Regretfully,{w=.2} I nodded in silence."
        
        show ka 001 night with dis
        
        ka "「What are you looking so meek for?{p}\ \ That's what I should look like, right? 」"
        fn "「But,{w=.2} I couldn't really help after all. 」"
        ka "「I said that's not true.{p}\ \ Jun said it too.{w} When you came over, everyone\n\ \ had more fun than usual.{w} Isn't that enough? 」"
        
        show ka 006 night with dis
        
        ka "「Besides...{w} For me,{w=.2} I was also happy\n\ \ you could listen to our performance.{p}\ \ Still, I'm sorry it wasn't done all that well. 」"
        
        show ka 001 night with dis
        
        ka "「That's not all.{p}\ \ Thanks to you being here for me,{w=.2}\n\ \ I could do this and be true to my feelings. 」"
        "Now, I had some words to say.{w} And yet,{w=.2}\n\ \ the words stuck inside my chest didn't come out."
        
        show ka 002 night with dis
        
        ka "「Anyway,{w=.2} why am I the one comforting you?{p}\ \ Weren't you planning on doing that for me? 」"
        fn "「W-{w=.2}well, that's 'cause,{w=.2} you- 」"
        "The words that came after that wouldn't connect.{p}After thinking this conversation was a little\nodd,{w=.2} I couldn't really keep it up."
        "As our eyes met, we laughed aloud."
        
        show ka 003 night with dis
        
        ka "「Sigh.{w=.2} Man, you really are something. 」"
        "Kouya ruffled my hair."
        
        show ka 001 night with dis
        
        ka "「...Pretty soon,{w=.2} we should be heading back. 」"
        fn "「Yeah. 」"
        "Sometime later,\nwe started walking again."
        "This time, Kouya lead the way.{p}From behind,{w=.2} it looked like\nhe was a bit closer to me."
    
        jump end25
    
########################################################
label end25:
    stop sound fadeout 3
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
    
    jump day26
    
    
