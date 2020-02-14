###Day 21
label day21:
    
    $ day = 21
    $ the_date = "August 21"
    $ event_name = "８月21日"
    
    if favorite == "kouya":
        window hide
        play music birds_chirping
        
        scene sky01 
        show text "{size=+130}August 21" at truecenter
        with Dissolve(.5)
    
        pause 3
        scene black with Dissolve(1)
        pause .4
    else:
        jump day22
        
    $ renpy.jump (favorite + "21")
    
    
####################################################
label kouya21:
    
    $ renpy.music.set_volume(1.0, 0.0, channel = "music")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound2")
    
    $ event_name = "Waking Up Somewhere Else"

    stop music fadeout 1.5
    play music se_037 fadein 1
    play sound birds_chirping
    scene bedroom with sdis
    
    "Tick, tick, tick..."
    "In my light sleeping, I heard a tiny noise.{p}Maybe it was the second hand of a clock,\nand the intermittence made me open my eyes."
    fn "「Mm... 」"
    "Opening my eyes,{w=.2}\nI was greeted by an unfamiliar room."
    "My heart skipped a beat,\nbut immediately afterwards my memory came back.{p}My violently pumping heart quickly calmed down."
    fn "「Oh yeah, I'm staying over at Kouya's place... 」"
    "The light leaking through the gap\nin the curtains illuminated the room.{p}Based on the light, it must be really early."
    "When I looked to where the sound was coming from,\nthe small hand was pointing down."
    "6:32...{p}Compared to my usual, I woke up really early."
    "I was wondering what I should do since I was awake,{w=.2}\nbut if I get up, I'd most likely wake Kouya up too."
    "Since I'm not that stealthy,\nI just stayed in the futon."
    "...yeah, that's a hard thing to do..."
    "Still,{w=.2} since I'm not doing anything else,\nit's not that fun."
    "Basically, I'm trying to kill time."
    "It's comfortable just lying in bed,\nbut I'm not feeling sleepy at all."
    fn "「And I woke up so late yesterday, too... 」"
    "Well, instead of waking up,{w=.2}\nit's more like I never went to sleep."
    "I was in the futon just after midnight,\nand then after that I thought deeply."
    fn "「Kouya... 」"
    "Kouya, who ran away from home."
    "As I thought about it,\nit wasn't a question of what had happened.{p}But the topic kept spinning around in my head."
    fn "「Is it...{w=.2} Okay for me to stay here...? 」 "
    "All of a sudden I became uneasy."
    "When you run away from home,\nyour parents can't exactly provide assistance.{p}How does he make a living from his part-time work?"
    "Even I could tell it was tough{w=.2}\nwithout needing to think about it."
    fn "「It'd be great if I wasn't in the way... 」"
    "I'm starting to hate\nhow often I'm thinking that lately."
    "But if I go and say 「I'm going back, 」\nKouya isn't going to say\n「Oh, okay then, 」 and let me go."
    "On the contrary, it'd most likely hurt him."
    "「I want you to stay at my place.{p}But only if you're okay with that.{p}Or, do you...{w=.2} Not like that idea? 」"
    "He went unusually far with that line.{p}Also, {w=.2}「If I thought that,\nI wouldn't be offering in the first place. 」"
    "That's more something Kouya would say."
    "...Yeah,{w=.2} I'm sure of it."
    "My gaze moved to Kouya, who was beside my bed."
    "I guess he'd turned over in his sleep,\nsince his fearless face was pointed this way."
    "I could easily see him rolling\nover on the spread out futon on the floor."
    "Kouya wanted me to take the bed,{w=.2}\nbut as a freeloader I thought it was\ntoo presumptious for me to take the bed."
    "Kouya looked comfortably asleep.{p}The sound of his easy breathing reached me easily."
    "...I guess I'll stay another two days after all."
    "I also want to be here if I could be anywhere.{p}So I'll be here."
    "When I look at Kouya's face,\nsomehow I feel a bit more determined."
    "Just now, everything I was worrying over\nmade me feel like an idiot."
    "I really am an idiot.{p}Worrying about weird things again.{p}Kouya would say something like that."
    "Thinking about it like that, I laughed a little."
    "Then, Kouya woke up and opened his eyes."

    show ka 005 at center with sdis
    
    ka "「Why are you laughing at someone's sleeping face...? 」"
    "Kouya spoke in a sleepy voice.{p}I faltered a bit."
    fn "「I-{w=.2}I'm not... 」"
    ka "「Then what are you laughing about? 」"
    fn "「Um...{w} It's because you were talking in your sleep,\n\ \ going 『Stop, not there... Don't touch that.』 」"
    ka "「Liar.{w=.2} You just made that up right now. 」"
    "Kouya spoke over his shoulder as he sat up.\nThen he stretched once."
    ka "「Mph... Hwaaah.. 」"
    fn "「You seem sleepy, Kouya. 」"
    
    show ka 001 with dis
    
    ka "「Obviously. It's first thing in the morning. 」"
    fn "「But you still woke up surprisingly early.{p}\ \ It's not even 7 yet. Did I wake you up? 」"
    "I got up from my futon, then opened up the curtains.{p}The light that was originally peeking in\nnow flooded the room."
    "There's going to be good weather today."
    ka "「Well, no...{p}\ \ Oh yeah. I forgot to tell you something important. 」"
    fn "「Eh, what? 」"
    
    show ka 013 with dis
    
    ka "「You'll have to stay here by yourself for a while,{w=.2}\ns\ \ ince I have to go to work. It's from 9 to 3. 」"
    fn "「Ueh-{w=.2}seriously? 」"
    
    show ka 014 with dis
    
    ka "「I'm really sorry...{p}\ \ I'm getting a break tomorrow.{p}\ \ But because of that, I can't hang out today. 」"
    fn "「Hmm. Well, I guess that's that.{p}\ \ You do live alone after all. 」"
    
    show ka 013 with dis
    
    ka "「Thanks for understanding.{p}\ \ You can do as you like while I'm gone.{p}\ \ I'll give you a spare key. 」"
    ka "「If you wanna go out that's fine. 」"
    fn "「Oho!{w} So are you saying it's also okay\nfor me to go through all your stuff\nand look for your dirty magazines? 」"
    
    show ka 002 with dis
    
    ka "「You could do that,\n\ \ but I dunno if you'll find anything. 」"
    "With his usual poker face,\nhe passed by me."
    "Tch, it would have been funny if he'd\ngotten all flustered and said 「stop! 」..."
    fn "「H-hmph!{w} Then I really will do it! 」"
    
    show ka 003 with dis
    
    ka "「But before that, let's have breakfast.\n\ \ I can't take it easy just yet. 」"
    "Kouya got out of bed and went into the kitchen."
    "Hey, did he just ignore what I said?"
    "Well,{w=.2} that's fine..."
    fn "「...so, what's for breakfast? 」"
    "With the change in topic,\nI asked Kouya as he started preparations.{p}...I think I have an idea what it is, though."
    
    show ka 001 with dis
    
    ka "「Hm?{w} I'm kinda reluctant about it\n\ \ since you're visiting,{w=.2} but same as last night? 」"
    fn "「Of course... 」"
    "Saying that, Kouya began heating the pot of curry."
    
    scene black with sdis
    
    $ event_name = "House-sitting Freeloader"

    play music free0213
    scene bedroom
    show ka 002 at center
    with wipe_right
    
    ka "「All right, I'm off. 」"
    fn "「Okay. Do your best at work. 」"
    
    show ka 003 with dis
    
    ka "「Right. 」"

    hide ka with wipe_right
    
    "I saw Kouya off from the doorway,\njust like a newlywed would."
    "Kouya slightly raised his hand in response to me,/n{nw}"
    play sound door_close
    extend "then afterwards the only thing that was left\nwas the sound of the door closing."
    "And then I was alone."
    fn "「Okay,{w=.2} what should I do... 」"
    "I got the key for the house at breakfast.{p}I could go out if I wanted to."
    fn "「But there isn't any place\n\ \ I particularly want to go to... 」"
    "Hmm,{w=.2}\nI'll need to think about this."
    "Frankly,{w=.2} there's nothing to do."
    
    stop music fadeout 1
    scene black with wipe_right
    play music free0428
    
    fn "「Hmm...{p}\ \ So I should go looking for Kouya's porn mags? 」"
    fn "「No, no,{w=.2} that would be bad. 」"
    fn "「Hmm.{w=.2} I'll do some cleaning then.\n\ \ And if something were to turn up,{w=.2}\n\ \ wouldn't that be an accident? 」"
    fn "「I mean, yeah, but...{p}\ \ Isn't that kind of sneaky?{p}\ \ Besides, can I just waltz into his room? 」"
    fn "「It's fine,{w=.2} he probably changed the hiding place.{p}\ \ Since he was cleaning in a panic yesterday. 」"
    fn "「I could at least put things in order,{w=.2}\n\ \ out of virtue. 」"
    fn "「But, well... 」"
    fn "「I'll stop complaining.{p}\ \ Right, I'll get to it. Out of virtue. 」"
    
    stop music fadeout 1.5
    scene bedroom with wipe_right
    play music free0213
    
    "Ah,{w=.2} I slipped into a mental self-conference\nbefore I realized it.{w=.2} Please, don't mind me."
    fn "「Anyhow, {w=.2}\n\ \ I'll start off with cleaning up. 」"
    "Hm.{w} Since I've found myself in a position\nto help Kouya,{w=.2} I came across a good idea\nwhile thinking about other things."
    "I'm not feeling guilty at all.{w=.2} Yep."
    fn "「All right, let's do this. 」"
    "I should be done by noon, so I'll set out right now.{p}Okay,{w=.2} I wonder if anything will turn up..."

    scene black with sdis
    
    "......"
    "..."
    
    scene bedroom with blind_vert
    
    fn "「N-{w} nothing's here... 」"
    "That can't be.{p}Not that I was looking."
    "However,{w=.2} nothing really popped out."
    "Up until now,\nI've spent nearly three hours cleaning...{p}The clock has already struck noon."
    "Thanks to that,\nI can see the area there shining.{p}It's positively sparkling."
    fn "「Shit...{p}\ \ Nothing...{p}\ \ Nothing there...{w=.2} impossible! 」"
    "I waved a clenched fist as I insisted so."
    fn "「I mean, this is Kouya's room isn't it!?{p}\ \ Why didn't anything turn up?{p}\ \ That's completely weird! 」"
    "The mediocrity is kinda irritating."
    fn "「Damn you, Kouya.{p}\ \ Just what kind of- 」"
    "At that moment,{w=.2}\nthis morning's conversation crossed my mind."

    scene black with dis
    show ka 002 at center with dis
    
    ka "『You could do that,\n\ \ but I dunno if you'll find anything.』"
    
    hide ka
    scene bedroom
    with dis
    
    fn "「N-{w=.2}no way... 」"
    "I don't know if I found anything."
    "I was confident\nthat there definitely was a hiding space,{w=.2}\nand I've been telling myself so..."
    "But could it be..."
    fn "「There was 'nothing' to begin with!? 」"
    "In that case, what have I been doing\nthe past few hours?"
    fn "「...I'll go eat. 」"
    "I unintentionally sighed, {w=.2}\nthen went towards the kitchen."
    "But then."
    
    stop music fadeout 1.5
    play sound ChimeA
    
    pause 1
    
    "That familiar sound echoed through the room."
    fn "「Hueh? 」"
    "The suddenness of it made me start."
    fn "「W-{w=.2}what do I do... 」"
    "A visitor coming\nwas out of line with my expectations."
    "Is it okay for me to answer?{p}No, but is it bad?"
    
    play sound ChimeA
    
    "*Ding-dong*"
    "The chime echoed again while I was thinking."
    fn "「If it's quick,{w=.2} that would be troubling... 」"
    "Oh yeah,{w=.2} I'm house-sitting at the moment.{p}For now it'd be okay to go look."
    
    play sound ChimeA
    
    "*Ding-dong*"
    fn "「I'm coming! 」"
    "I came to my conclusion\nand went to the door."
    
    play sound KeyA
    
    "I slowly opened the door."
    fn "「Yes,{w=.2} who is i- 」"
    "When I saw who it was,\nI forgot whatever it was that I was about to say."
    "Staring blankly,\nthere's no way I could mistake who it was."
    "That appearance hasn't changed at all\nfrom the image in my memories."
    "When I was still in Minasato,{w=.2}\nshe took care of me a lot."
    who "「...[fn]...-kun? 」"
    fn "「...Mrs... 」"    
    "It was Kouya's mother,{w=.2} Kazumi-san."
    
    play music free60
    
    $ encounter_kazumi = True
    
    kz "「Oh, it really is you,{p}\ \ it's been so long.{p}\ \ You've gotten so big! 」" 
    kz "「Meeting someone from so long ago,{w=.2}\n\ \ I'm just so surprised.\n\ \ How long will you be here? 」"
    fn "「For all of August.{p}\ \ Right now,{w=.2} I'm on summer vacation. 」"
    kz "「I see.{p}\ \ Since it's been so long since you've been here,{w=.2}\n\ \ you must have missed so many things. 」"
    fn "「Yes. Definitely. 」"
    kz "「Mhmm,{w=.2} I see. 」"
    "Kazumi-san smiled and nodded at my words."
    "But that only lasted a moment,{w=.2}\nbefore her expression changed to something complex."
    kz "「...By the way,{w=.2} has Kouya...{w} gone out? 」"
    fn "「Eh? Ah, yes.{w=.2} He's not here.{p}\ \ He's at his job now. 」"
    fn "「I'm house-sitting since I'm not paying him\n\ \ anything while I'm here. 」"
    fn "「He'll be here...{w} in a few hours or so. 」"
    kz "「I see...{p}\ \ Then, when he comes back,{w=.2}\n\ \ will you give this to him? 」"
    "After saying that,{w=.2}\nKazumi-san held out a brown envelope."
    "'-To Kouya' was written neatly on it."
    fn "「Ah-{p}\ \ Yes, I understand. 」"
    kz "「I'm sorry, [fn]-kun.{p}\ \ Well then, I'll be counting on you. 」"
    "Kazumi-san entrusted the letter to me,\nthen left."    
    fn "「... 」"
    "Completely flabbergasted,{p}I stood stock still in front of the entryway."
    "...The envelope was still in my hand."
    
    stop music fadeout 1
    scene black with sdis    
   
    ##########################################################    
    label kouya21_letter:
        
        $ event_name = "Dining Table and a Letter"
        
        play music daily03
        scene bedroom red
        show ka 002 red at center
        with sdis  
        
        ka "「'Kay, meat and veggie fried rice ready. 」"
        fn "「Mmm, no matter how many times I try it,\n\ \ you are really good at this.\n\ \ Just what you'd expect from someone who lives alone. 」"
        
        show ka 001 red at center with dis
        
        ka "「It's nothing to be praised about.{p}\ \ Besides, you've only seen me cook twice. 」"
        fn "「The number of times doesn't matter, for sure. 」"
        ka "「Really.{p}\ \ Anyway, take this over there for me. 」"
        fn "「Yes sir. 」"
        
        hide ka with dis
        
        "I diligently brought over our portions\nto the table, just like Kouya asked."
        "Out of the corner of my eye,\nI noticed the clock had only just passed 6."
        "It's a bit early,{w=.2}\nbut we couldn't think of anything to do,\nso we decided to have dinner."
        
        show ka 001 red at center with dis
        
        ka "「Now then, let's eat before it gets cold. 」"
        fn "「Mmm,{w=.2} time to eat. 」"
        
        show ka 002 red with dis
        
        ka "「Yeah,{w=.2} let's eat.{p}\ \ ...Still,{w=.2} to spend all day cleaning like that,\n\ \ you must've really been bored. 」"
        "Kouya's eyes seemed to be saying,{w=.2}\n「Wouldn't it have been okay to just go somewhere? 」"
        fn "「Well,{w=.2} there wasn't any place\n\ \ that I especially wanted to go.{p}\ \ So I thought cleaning up would be better. 」"
        
        show ka 003 red with dis
        
        ka "「You went around searching for porno, didn't you? 」"
        "All of a sudden Kouya was prodding at me,\nand my heart lept to my throat."
        fn "「...hey, this fried rice\n\ \ is awesomely delicious. 」"
        
        show ka 001 red with dis
        
        ka "「So, did you find my prized collection?{p}\ \ Inside the magazines? 」"
        fn "「Lies.{w=.2} I couldn't find it anywhere. 」"
        
        show ka 005 red with dis
        
        ka "「Then you did go looking. 」"
        fn "「Guah,{w=.2} that was a horrible trick. 」"
        
        show ka 014 red with dis
        
        ka "「Then don't fall for something like this... 」"
        "Kouya was looking at me,\ncompletely aghast."
        "I'm begging you,\nstop looking at me with those eyes..."
        
        show ka 005 red with dis
        
        ka "「My god... 」"
        fn "「Uuu, I'm sorry... 」"
        
        show ka 002 red with dis
        
        ka "「Whatever, just eat. 」"
        fn "「Yeah, okay. 」"
        "Happy for the change in subject,\nI quickly finished up the rest of my food."
        fn "「Whew,{w=.2} thanks for the food.\n\ \ Today's meal was also very delicious. 」"
        
        show ka 001 red with dis
        
        ka "「I said it earlier,\n\ \ it's nothing to be praised about. 」"
        fn "「No, it's not that...{p}\ \ Ah,{w=.2} I can handle dealing with the dishes.{p}\ \ I mean, let me handle them. 」"
        
        show ka 014 red with dis
        
        ka "「You're being strangely helpful.{p}\ \ You don't need to go so far out of your way. 」"
        fn "「I know. {w=.2}\n\ \ But this is a problem with my feelings. 」"
        
        show ka 002 red with dis
        
        ka "「Uh-huh...{w=.2} If you say so.{p}\ \ I'll leave it to you again. 」"
        fn "「I'll take care of it. 」"
        "After boasting, I stood up\nso I could take the dishes to the kitchen."
        
        play sound paper00
        
        "It was then that something fell out of my pocket."
        fn "「――ah. 」"
        "It was an envelope."
        "The thing that Kazumi-san had me hold on to."
        "After Kazumi-san gave it to me,{w=.2}\nI'd put it in my pocket and left it there."
        "It's not that I forgot about it.{p}And I wasn't hiding it."
        "It's just... It was hard to give it to him.{p}There wasn't a reason for it.{p}I didn't even understand it myself."
        "I simply never gave it to him."
        
        show ka 001 red with dis
        
        ka "「Hm? What's that? 」"
        fn "「...Eh?\n\ \ Ah, sorry for taking so long to give it to you.{p}\ \ During the day, I was asked to deliver it. Here. 」"
        "I handed the envelope over."
        "Kouya looked at it curiously as he turned it around."
        ka "「Who's it from?{p}\ \ There's no sender written on it. 」"
        fn "「...Mrs Kazumi.{p}\ \ She hasn't changed a bit since back then. 」"
        
        stop music fadeout 1
        play music cicada01 fadein 5
        $ renpy.music.set_volume(0.6, 0.0, channel = "music")
        
        ka "「... 」"
        "Kouya's face turned into\nsomething a bit... inscrutable."
        "It was a mechanical,{w=.2} cold expression."
        "「I thought so, 」{w=.2} his face seemed to say."
        "Kouya, who should have left home.{p}And Kazumi-san, who came to visit."
        "One way or another,\nKouya didn't seem too happy."
        "It's possible that\nit's because it wasn't given to him earlier."
        fn "「Kouya... 」"
        "He didn't answer,\nand opened the envelope in silence."
        "With a sudden movement,\nhe opened the seal and checked inside."
        "What fell out was a page of stationary."
        "It was folded in three,\nwhich Kouya opened and began reading quietly."
        "It looks like it was written on\nall the way down to the bottom,\nbut I couldn't read anything from where I stood."
        ka "「... 」"
        "Kouya kept going on{w=.2} in complete silence."
        "Standing there felt somewhat awkward,\nso I took the dishes into the kitchen."
    
        hide ka with dis
        
        "The mood felt heavy,\nheavier than any leftovers on the plates."
        "The oppressiveness kept weighing in for a while.\nI want to say something to Kouya."
        "However,{w=.2} I couldn't think of anything\nthat seemed like it would do anything."
        "It feels like my heart had put a clamp on my mouth."
        "I carried on like that, feeling a bit pitiful.{p}I got a little depressed."
        fn "「Sigh... 」"
        "A tiny sigh came out as I turned the faucet."
        "It was then."
        
        play sound PaperD
        
        "I could hear that sound coming from the table."
        "I looked over my shoulder."
        "My eyes met with Kouya's as he stood up,\nfixing the edge of his shirt."
        
        show ka 001 red at center with dis
        
        ka "「I have to go shopping.\n\ \ The fridge is looking a bit empty. 」"
        fn "「Oh...{w} Okay, got it.{p}\ \ I'll take care of things here. 」"
        "...No."
        "That's not what I wanted to say."
        "I always chose the words that wouldn't burden him,\nthat wouldn't become a bother to him."
        "But it was useless.{p}Right now I can't do that."
        "But as I thought, the words wouldn't come out."
        
        show ka 002 red with dis
        
        ka "「Right. 」"
        
        hide ka with dis
        
        "Without another word,\nhe turned and left."
        
        play sound door04 
        play sound DoorCloseB #!#
        
        "The door closed with a thud.\nI was left alone with the sound of running water."
        "When I remembered about the faucet,\nI turned that off and finally it was silent."
        fn "「What do I do...? 」"
        "Again, another sigh."
        "At this rate, maybe it'd be better to let him go."
        
        menu:
            "A. Chase after him.":
                jump kouya21_chase
            "B. Don't chase after him.":
                jump kouya21_stay
    
                
    #############################################
    label kouya21_stay:
    
        $ event_name = "Cowardly Housewatch"
        
        "Is it okay to let Kouya go?"
        "No,{w=.2} there's no way it should be."
        "But, what can I do even if I go after him?"
        "...I can't do anything as I am now.{p}If there was something I could do,\nI don't how to do it."
        "So, I'm saying nothing can be done."
        "In that case, it'd be best to stay here."
        "So if I can't do anything, it's better to not\nrun off with only a half-baked idea."
        "I say I want to be his strength,{w=.2}\nbut I couldn't do anything in the end..."
    
        scene black with sdis
        
        "...Some time later, Kouya came back\nlike nothing had happened."
        "Neither Kouya nor I\nbrought up the topic about the letter.{p}After the mutual silence, it was tabooed and sealed."
    
        jump kouya21_badend
    
    #############################################    
    label kouya21_chase:
    
        $ evemt_name = "Timid Support"
        
        "Is it okay to let Kouya go?"
        "No,{w=.2} there's no way it should be."
        "But what can I say?{p}What can I say to him?"
        "...I don't know."
        fn "「I just don't know... 」"
        "Still, I can't let things go on like this."
        fn "「For now,{w=.2} I have to go after him. 」"
        "Right now I can't leave Kouya by himself.{p}As for why, I thought about it."
        "I want to be Kouya's strength.{p}I've always thought that."
        "A minute later,\nI was walking out the door."
        "While en route, I went and picked up\nthe letter he rolled up into the garbage,{p}and the wallet he left on his bed."
        
        stop music fadeout 2
        scene black with wipe_right

        $ event_name = "His Whereabouts"

        play music piano4_001

        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        
        "There's no such person who would go shopping\nand forget their wallet."
        "I saw Kouya's wallet\nwhen I was leaving the room."
        "Someone going shopping wouldn't leave that behind."
        "To do something like that\nis completely unlike Kouya."
        "I noticed it just as I was about to leave,{w=.2}\nsomething that shouldn't be overlooked."
        "So why was it left behind?"
        fn "「He wasn't planning on shopping to begin with... 」"
        "...so where did Kouya go, then?"
        "I ran around the village looking for him."
    
        scene market red with wipe_right
        
        fn "「Not here... 」"
    
        scene park night with wipe_right
        
        fn "「Not here either... 」"
        "Even after searching in the village,{p}I couldn't find him."
        "There's pretty much nowhere left I haven't looked.{p}Steadily the sunlight was dimming."
        fn "「Kouya,{w=.2} where did... 」"
        "I stopped to catch my breath,\nand calmed down a little."
        fn "「No good,{w=.2}\n\ \ I didn't find anything running around at random... 」"
        "I'll have to think about it.{p}If I were Kouya, where would I go?"
        "A popular place is out of the question.{p}Kouya would want to be alone.{p}That he left in silence should be proof of that."
        "So there's no way that can be it."
        "If I think about it like that,\nhe probably didn't go to anyone's house."
        "So aside from all that,\nwhat kind of place would he go to?"
        
        menu:
            "A. The riverside.":
                jump kouya21_river
            "B. The lake.":
                jump kouya21_lake
            "C. The forest.":
                jump kouya21_forest
    
    
    ####################################################
    label kouya21_river:
        
        $ event_name = "His Place"

        scene white with sdis
        
        "As I thought it over, I skimmed over all my memories."
        "In that white, white space,{p}I could see the form of one huskyboy, sitting down\nwith his legs spread out in front of him."
        "He was looking off into the distance,{w=.2}\nnot noticing me behind him."
        "I slowly approached his back,\nthen clapped him on the shoulder."
        "He turned around."
    
        scene park night with sdis
        
        fn "「The riverside...? 」"
        "After coming back from a soundless,{w=.2}\nodorless,{w=.2} senseless vision,{w=.2}\nfor some reason it felt instinctual."
        "I don't have any supporting evidence."
        "But before I think about it further,{w=.2}\nI put my faith into that idea."
    
        scene path night with wipe_right
        
        "It was darker than the city,{w=.2}\nbut I ran through the evening."
        "As I approached the stream,{w=.2}\nI had a thought that seemed\nto be telling me something."
        "『I'm over here.』"
        "I began running as though I'd actually been called."
        "At the same time, I remembered more, bit by bit.{p}「When stuff happens, I usually come out here. 」{p}That's what that boy said."
        "He said that when he looks at the flowing water,\nit's somehow calming."
        "On hot summer days when he wanted to get nice and cool,\nthat was always his favorite place from back then."
    
        scene rice night with wipe_right
        
        "I weaved my way through the paddy fields,\nand before long the river bank\nspread open in front of my eyes."
    
        scene river night with wipe_right
        
        fn "「... 」"
        "In the light of the night sky,\nreflected off the river..."
        "I saw him sitting down,\nlegs spread in front of him."
    
        jump kouya21_reason
    
    ##############################################
    label kouya21_lake:
        
        $ event_name = "His Direction"
        
        fn "「Maybe at the lake...? 」"
        "Without any reason, I thought that."
        fn "「Anyway, I'm going. 」"
        "I took a deep breath,\nthen turned in the direction of the lake."
        "Then,{w=.2} just when I was about to run:"
        who "「Hey, if it isn't you, [fn]. 」"
        "I heard a familiar voice from behind me."
        "A deep voice, filled with energy..."
        
        show ta 001 night at center with dis
        
        fn "「Tatsu-nii... 」"
        ta "「What're you doing over here? 」"
        fn "「Oh, I'm just looking for Kouya.{p}\ \ Have you seen him? 」"
        
        show ta 008 night with dis
        
        ta "「Huh?{w} If you're looking for Kouya,\n\ \ I saw him by the river.{p}\ \ What's wrong, did something happen? 」"
        fn "「...No, it's nothing.{p}\ \ Thanks, Tatsu-nii.{p}\ \ You've helped me a lot. 」"
        
        show ta 001 night with dis
        
        ta "「Really?{p}\ \ ...Well, be careful.{w=.2}\n\ \ It's already pretty late. 」"
        fn "「Okay.{p}\ \ Really, thank you. 」"
        "I thanked him, then ran off."
    
        show ta at jump_up
        
        ta "「[fn]! 」"
        "Tatsu-nii called after me, and I stopped."
        
        show ta 008 night with dis
        
        ta "「Uh, let's see...{p}\ \ {nw}"
        show ta 010 night with dis
        extend "It looks like a lot's happened,\n\ \ but good luck. 」"
        ta "「He's all wound up.{p}\ \ But if it's you,\n\ \ things should be fine... 」"
    
        show ta 005 night with dis
        
        ta "「...I didn't know what to say to him, myself.{p}\ \ Anyway, get in there! 」"
        fn "「...Yeah! 」"
    
        hide ta with dis
        
        "Thanks, Tatsu-nii."
        "I said that inside my mind and looked on ahead."
        "Third time's the charm.{p}I'm running for real this time."
        "Then, a few minutes later,\nI finally found him."
    
        jump kouya21_reason
    
    #################################################
    label kouya21_forest:
        
        $ event_name = "His Form"
        
        fn "「Maybe the forest...? 」"
        "For no particular reason, I thought that."
        "But it is a very quiet place, so it's possible."
        fn "「Well, the only thing I can do is check. 」"
        "I took a deep breath,\nthen turned in the direction of the forest."
        "Then,{w=.2} just when I was about to run-"
        who "「Oh, it's you, [fn]. 」"
        "A familiar voice came from behind me."
        "A deep voice, one that gave\na sense of a large presence..."
        
        show ju 001 night at center with dis
        
        fn "「Juuichi-san... 」"
        ju "「What are you doing over here? 」"
        fn "「Oh, I'm just looking for Kouya.{p}\ \ Have you seen him? 」"
        ju "「If you're looking for Kouya,\n\ \ I just saw him by the river.{p}\ \ What's wrong? Did something happen? 」"
        fn "「...no,{w=.2} it's nothing.{p}\ \ Thanks, Juuichi-san.{p}\ \ You helped me a lot there. 」"
        
        show ju 003 night with dis
        
        ju "「That so?{p}\ \ ...Well, anyway, be careful.{p}\ \ It's pretty dark out. 」"
        fn "「Okay.{p}\ \ Really, thanks. 」"
        
        show ju 001 night with dis
        
        ju "「...Oh yeah,{w=.2} take this with you. 」"
        "After saying that,\nJuuichi-san reached into his pocket{w=.2}\nand pulled out a small yellow vinyl package."
        "Two of them, actually."
        "...These are honey sweets."
        ju "「Sweet things are good for when you're tired.\n\ \ Take it...{w} Give one of them to Kouya.{p}\ \ He looked pretty tired, too. 」"
    
        show ju 002 night with dis
        
        ju "「He'll probably have something to say to you.{p}\ \ Come on,{w=.2} get going. 」"
        fn "「Juuichi-san...{p}\ \ Thank you,{w=.2} I'm going now. 」"
        "I thanked him, then ran off."
        "Then, a few minutes later,\nI finally found him."
    
        jump kouya21_reason
    
    ################################################
    label kouya21_reason:
        
        $ event_name = "His Reason"

        scene river night with wipe_right
        show ka 001 night at center with sdis
        
        "Kouya was alone there."
        "He wasn't doing anything aside from sitting there."
        "It's as if time had stopped."
        "But the sound of insects\nand the murmuring of the river\ntold me it wasn't the case."
        "I slowly approached."
        "Standing here behind him,{w=.2} Kouya's back\nsomehow looked smaller than usual."
        fn "「Kouya... 」"
        "From behind him, I spoke."
        "At the sound of his name,\nKouya looked over his shoulder."    
        ka "「[fn]...{p}\ \ What is it, how's the apartment? 」"
        "Kouya replied back,{w=.2}\nlooking the same as he ever did."
        "As I answered,\nI sat down beside him."
        fn "「I just used the duplicate key,{w=.2} since I had it.{p}\ \ Someone went out shopping and forgot their wallet. 」"
        ka "「... 」"
        "Kouya said nothing.{p}Most likely,{w=.2} he knows what I was thinking\nin coming over here."
        "And so, that thought is likely correct."
        "If that's the case,{w=.2}\nthere are things I need to say to him."
        "Even if it's meddlesome, it's all okay.{p}I've got things I want to say\nand things I've thought about."
        "And also, I've decided."
        "I decided this morning, when I was at Kouya's.{p}I decided I would tell him my feelings."
        "Therefore, with determination in my chest,\nI opened my mouth."
        fn "「Hey,{w=.2} Kouya. 」"
        ka "「What? 」"
        fn "「This is just simple nosiness.{p}\ \ You might hate it,{w=.2} but would you still listen? 」"
        ka "「... 」"
        "Kouya shut his mouth again, so I kept on."
        fn "「I don't know what happened to you before.{p}\ \ But I do know that right now you're worrying,{w=.2}\n\ \ and that you're suffering. 」"
        fn "「Kouya, don't worry about things by yourself...{p}\ \ You aren't alone.{p}\ \ You've got everyone,{w=.2} right at your side. 」"
        fn "「Kounosuke and Shin-kun,{w} Shun-kun and Kyouji,{p}\ \ Tatsu-nii and Juuichi-san,{p}\ \ Soutarou-kun and Torahiko. 」"
        fn "「And also,{w=.2} right now,{w=.2} I'm here. 」"
        fn "「I'm not that reliable,\n\ \ but I'm sure I can at least\n\ \ be a bit of strength for you. 」"
        fn "「So, rely on me more.{p}\ \ Don't hold back.{p}\ \ ...We're friends, aren't we? 」"
        "I wasn't lying,{w=.2} those were my true feelings."
        "I want him to rely on me more.{p}It's all right for him to count on me more."
        "It's a little thing, but I thought\nI want to be Kouya's strength,{w=.2}\nlike I was reaching out to him."
        ka "「... 」"
        "Kouya stayed quiet, just taking in my words."
        "He seemed to be thinking about something."
        "And now I said nothing myself,{w=.2}\nand silence ran between the two of us."
        "Only the sound of water kept going."
        "Before long, it was Kouya who broke the silence."
        ka "「...I'm an idiot.{p}\ \ I was trying not to worry you,\n\ \ and I ended up doing the exact opposite. 」"
        ka "「I really am a big idiot... 」"
        fn "「Kouya... 」"
        ka "「Sorry, [fn]...{p}\ \ Looks like{w=.2} I made you worry too much. 」"
        
        show ka 002 night with dis
        
        ka "「It's just as you said. 」"
        ka "「If you came all the way here,{w=.2}\n\ \ it would've been better if\n\ \ I talked to you from the start. 」"
        "After saying that, Kouya laughed sadly."
        ka "「I left home about the time I entered high school.{p}\ \ ...I had a fight with my father. 」"
        "And then, little by little, he started talking.{p}Things I didn't know about,{w=.2}\nthat happened in Minasato when I wasn't around."
        
        show ka 001 night with dis
        
        ka "「...I started playing the guitar\n\ \ during the last few years of grade school. 」"
        ka "「Since no one talks about it,{w=.2}\n\ \ I doubt you knew about that. 」"
        ka "「...I've always loved music since back then.{p}\ \ I was interested in it.{p}\ \ I thought I'd try it sometime. 」"
        ka "「Around then, it was still just a hobby,\n\ \ so I thought it would be fine to just enjoy it. 」"
        ka "「But then I started thinking,\n\ \ if I had the chance,\n\ \ I would want to be a musician. 」"
        ka "「That was around the summer\n\ \ of the first year of middle school. 」"
        ka "「My motive wasn't anything special.{p}\ \ It was around then that I became acquainted\n\ \ with a street musician. 」"
        ka "「You see them now and again in Kazenari,\n\ \ but after seeing him so many times,\n\ \ I started stopping to listen to his song. 」"
        ka "「Nobody else stopped,\n\ \ and I wonder why I was so captivated by that song. 」"
        ka "「And then, one day, something happened.{p}\ \ I was going there to listen to the song like always,\n\ \ when he called out to me... 」"
    
        scene white with sdis
        
        who "「Hey, you there. 」"
        ka "「...me? 」"
        who "「Yeah, you.{p}\ \ I've been seeing your face a lot lately. 」"
        who "「I can remember you since you're\n\ \ the only one to stop and listen. 」"
        who "「I guess you like my song, then. 」"
        ka "「No... To be honest, I don't really understand.{p}\ \ Every time, my feet would just stop for some reason.{p}\ \ To listen to your song, maybe. 」"
        ka "「It's a strange way of putting it,\n\ \ but it feels like it was calling me over. 」"
        who "「...Hmhm, I see.{p}\ \ Like you were called, eh? 」"
        ka "「... 」"
        who "「Oh, sorry for laughing. It's just that{p}\ \ that's the first time anyone's said that.{p}\ \ You're an interesting kid. 」"
        ka "「Is that a compliment? 」"
        who "「Of course.{w} So how about it?\n\ \ If you're okay with it, why don't you come over\n\ \ and talk to me again when you have time? 」"
        who "「I still don't know many people in this town.{p}\ \ ...What do you think? 」"
    
        scene river night
        show ka 001 night at center
        with sdis
        
        ka "「I didn't have any special reason to say no,\n\ \ so I accepted his invitation. 」"
        
        show ka 002 night with dis
        
        ka "「And so, just as before,\n\ \ I'd sometimes go over to listen\n\ \ and just talk for a little bit. 」"
        "Kouya laughed shyly."
        "I stayed quiet and waited for Kouya to keep going.{p}『I'll listen to it all,』 I thought."
        
        show ka 001 night with dis
        
        ka "「But we talked about a lot of things\n\ \ without getting tired of it. 」"
        ka "「And then, sometime afterwards,\n\ \ I started thinking about one thing. 」"
        ka "「『It'd be great if I could get a lot of people\n\ \ to listen to my song, just like this guy.』{p}\ \ That's what I thought. 」"
        ka "「It's because of that\n\ \ that I started aiming to be a musician. 」"
        ka "「There's a chance that I've had that\n\ \ thought since I started playing on the guitar.{p}\ \ But I'm sure the kickstart was because of him. 」"
        ka "「I think it's a kind of yearning.{p}\ \ Living like that is probably fun, I figured. 」"
        ka "「If I could live with the one I love,{w=.2}\n\ \ it'd always be fun. 」"
        ka "「That's when I started taking the guitar seriously.{p}\ \ I practiced hard, and occasionally\n\ \ I played alongside next to that person. 」"
        ka "「It quickly became a lot of fun,\n\ \ and I met a lot of friends and acquaintances. 」"
        ka "「So, in the third year of middle school,{p}\ \ I told my parents that when it was time\n\ \ to decide a career. 」"
        ka "「That I wanted to walk the way of a musician.\n\ \ But my dad... 」"
    
        scene white with wipe_right
        
        mi "「No, I'll never allow that.{p}\ \ I said nothing when you wanted to play the guitar,\n\ \ but becoming a musician is ridiculous! 」" 
        ka "「Wait!{p}\ \ I've been thinking about it a lot and- 」"
        mi "「You understand nothing! 」"
        ka "「...! 」"
        mi "「Listen, you're free to have your own dreams.{p}\ \ But you can't live on dreams alone! 」"
        mi "「Boys like you aiming to be a musician\n\ \ are a dime a dozen.{p}\ \ Take a closer look at reality. 」"
        mi "「If you're going to keep saying that,\n\ \ you won't be able to stay while\n\ \ keeping up with the guitar! 」"
        ka "「...the hell...? 」"
        ka "「Are you saying for my sake\n\ \ to not listen to other people!? 」"
        ka "「Stop screwing with me!{p}\ \ I have my own ideas! 」"
    
        scene river night
        show ka 001 night at center
        with wipe_right
        
        fn "「...And then? 」"
        
        show ka 002 night with dis
        
        ka "「Then we had an even bigger argument.\n\ \ ...Looking back on it, it was a stupid fight.\n\ \ It would have been better if I spoke more clearly. 」"
        
        show ka 001 night with dis
        
        ka "「But I don't regret anything.{p}\ \ I don't hate the way I am now, after all. 」"
        ka "「If I never left home,\n\ \ I'm sure I'd never have turned out this way. 」"
        "As Kouya said that, I could see\na bit of loneliness in his face."
        "I was also feeling a bit lonely myself."
        fn "「Kouya... 」"
        ka "「...You know that letter?{w=.2}\n\ \ It said to come visit tomorrow. 」"
        ka "「'I want to talk to you,\n\ \ it'll be a secret from your father,' and all that. 」"
        fn "「...What'll you do? 」"
        ka "「Right now,{w=.2} I still haven't decided. 」"
        "Kouya said only that much, and hung his head."
        ka "「Whatever I do,\n\ \ it's probably going to be awkward. 」"
        ka "「That's why I'm still thinking it over... 」"
        "Kouya raised his head,\nand looked up at the night sky."
        ka "「Just...{w=.2} What's the best thing to do? 」"
        ka "「...Hey, what would you do, [fn]? 」"
        fn "「Hmm...{p}\ \ If it were me... 」"
        "If it were me, what would I do?"
        "If I were Kouya..."
        
        menu:
            "A. Go see her.": 
                jump kouya21_go
            "B. Don't go see her.":
                jump kouya21_avoid
            "C. I don't know myself.":
                jump kouya21_unsure
    
    ##################################################
    label kouya21_go:
            
        $ event_name = "Positive Answer"
        
        fn "「If it were me, I'd go. 」"
        "After thinking about it, that would be my answer."
        fn "「Just as you said,{w=.2}\n\ \ it might turn out to not be that good a talk. 」"
        fn "「But on the other hand,\n\ \ it's possible the opposite is true. 」"
        fn "「No one really knows what will happen. 」"
        "It's true, after all.{p}The future still isn't decided yet."
        "As for the choices that weren't picked,\nyou can't go back and choose them."
        "But as we live,\nI think it's something that can't be helped."
        fn "「So, if I were the one doing it,\n\ \ I wouldn't want to have regrets.{p}\ \ I'd go, if it were me. 」"
        ka "「[fn]...{p}\ \ {nw}"
        show ka 002 night with dis
        ka "Yeah, you're right. 」"
        "As Kouya murmured, I felt\nI could see a light shining in his eyes."
        "Unless I'm delusional,\nI'm sure it was his determination."
        ka "「Thanks, [fn].{p}\ \ Because of you, I remembered something important. 」"
        fn "「Hm? 」"
        
        show ka 003 night with dis
        
        ka "「One of my favorite mottos.{p}\ \ Where there's a will, there's a way. 」"    
        "And so, Kouya laughed."
        "It felt like I haven't\nseen that smile in forever.{p}And it's only been a few hours too."
        "It's a feeling I've missed."
        ka "「I'll go meet her, just like you said.{p}\ \ Whatever happens, I won't know until I try.{p}\ \ If I don't try, nothing'll happen. 」"
        "Kouya stood up."
        
        jump kouya21_gohome
    
    #####################################################
    label kouya21_avoid:
        
        $ event_name = "Negative Answer"
        
        fn "「If it were me, I don't think I'd go. 」"
        "After worrying about it, that would be my answer."
        "If Kouya went over there,{w=.2}\nI don't think he'd have a nice talk."
        "I think that for parents,\nthey can't help but be anxious\nif their children decide to be musicians."
        "But, I like the Kouya\nthat plays the guitar."
        "If Kouya himself wants to keep on going with it,\nthen I want him to continue on."
        "Therefore, if it were me, I wouldn't go meet her.{p}I wouldn't want to."
        "And so I told Kouya all that."
        ka "「That so... 」"
        "Kouya didn't have anything to say\nafter I told him my thoughts."
        "We went back to the apartment just like that."
        
        jump kouya21_badend
    
    #####################################################
    label kouya21_unsure:
        
        $ event_name = "Your Answer"
        
        fn "「...That's not something you should be asking me. 」"
        "I tossed out all the responses,\nthen said that to Kouya."
        fn "「What would I do?{p}\ \ That's not the answer you want. 」"
        fn "「You already have your own answer.{p}\ \ You're just anxious about it,\n\ \ so I don't think you really want mine. 」"
        ka "「... 」"
        "At my pointing out, Kouya shut his mouth."
        "After seeing that, I'm sure of it."
        fn "「I get that you feel unsure.{p}\ \ But in the end, it's wrong if you don't decide yourself.\n\ \ Whatever I'd do with has nothing to do with it. 」"
        fn "「Maybe people live as they believe.{p}\ \ But if anything happens,\n\ \ I'm sure they'd take responsibility for it. 」"
        fn "「That's why you have to decide.{p}\ \ It's your life.{p}\ \ Nobody else can change places with you. 」"
        "And that was everything I wanted to tell him."
        "I don't know if that came out all that well.{p}It might've become a flat-out refusal."
        "But that was everything."
        "People can always ask for a hand from others.{p}However, there will always be times\nwhen they'll have to choose for themselves."
        "In the times where you can't run away,\nor times where it's hard to decide,\nyou'll always have to make a choice."
        "Right now, Kouya is probably thinking about that."
        fn "「Hey, Kouya, what do you want to do?{p}\ \ What do you think is the best thing to do? 」"
        "The most I can do is open the door."
        "Besides that, there's probably nothing else."
        ka "「I-{w=.2}I think... 」"
        ka "「In that case,{w=.2} I think...{w=.2} I'll go see her. 」"
        ka "「Up until now, I've always had\n\ \ as much space as I like.{p}\ \ I've never been asked back. 」"
        ka "「Why I was called, I don't know.{p}\ \ But, if I keep going without understanding,\n\ \ I'll just be going on half-baked. 」"
        ka "「Just like I am now.{p}\ \ I'm sure that I started regretting\n\ \ things somewhere on the way. 」"
        ka "「I'll go meet her.{p}\ \ That'd definitely be best. 」"
        "As he declared that,\nI'm sure I could see his determination coming back."
        "For a second, it felt like the\nregular old Kouya had returned."
        "I clapped him on the back happily."
        fn "「Yeah, that's good.{p}\ \ I thought you'd do that. 」"
        ka "「[fn]... 」"
        fn "「Sorry about things.{p}\ \ I said earlier that I wanted to be\n\ \ a source of great strength for you. 」"
        fn "「But with all the things I didn't do,\n\ \ I guess it all means nothing. 」"
        ka "「That's not true. 」"
        "As I laughed in self-derision,\nKouya said that while looking seriously at me."
        ka "「I'm sure that if you'd never said\n\ \ any of that to me,{w=.2}\n\ \ I'd go on being vague and lying to myself. 」"
        ka "「So it's thanks to you\n\ \ that I could decide. 」"
        
        show ka 002 night with dis
        
        ka "「You became my strength. 」"
        "After smiling tenderly,\nKouya gently ruffled my hair."
        "It kind of tickled."
        fn "「Kouya... 」"
        ka "「Sorry about worrying you.{p}\ \ And...{w=.2} Thanks. 」"
        
        show ka 003 with dis
        
        ka "「I'll try my best.{p}\ \ Where there's a will, there's a way. 」"
        "With one more smile, Kouya stood up."
    
        jump kouya21_gohome
    
    
    ##############################################
    label kouya21_badend:
            
        $ event_name = "One Ending"
        
        stop music fadeout 1.5
        scene black with sdis
        play music free60
        
        "After that, time passed on with nothing happening."
        "Before I realized, the promised three days ended,{p}and not long after that, August was over."
        "And now, I've returned to the city."
        "It was a fun summer vacation.{p}I've made irreplacable memories."
        "At least...{w=.2} I think."
        "But deep in my heart,\nit felt like a hole opened up."
        "It felt like something disappeared.{p}But what that is, I don't know.{p}If I did, I wouldn't be troubled."
        "The thing I do know is{p}that I'm sure it was something important."
        "Whatever I lost, I'm sure\nI left it behind in Minasato Village."
        "It's possible that I'll never get it back.{p}Whatever that \"thing\" I lost was,\nit was lost to eternity."
        "Because of that, I sometimes think about something.{p}The times when I look up into the sky,\nin the middle of all the noise."
        "The times I look up into the sky,\nconfined by the surrounding buildings."
        "...Right now,{w=.2} I wonder what he's doing?"
        "Yes,{w=.2} that's what I think of from time to time."
        
        scene black with sdis
        
        #Insert promt to either go to menu or jump back to beginning of day
        jump kouya21_letter
        
        #[hidecharacters with sdis msgoff][wt][wait time="1000"]
        #[gameover_confirm gobackto="*bad-kou"]
    
    
    ############################################
    label kouya21_gohome:
        
        $ event_name = "His Hand"
        
        "That figure somehow looked bigger than usual."
        
        show ka 002 night with dis
        
        ka "「All right, shall we head back?{p}\ \ Even in the summer, if we stay out at night\n\ \ like this we might catch a cold. 」"
        fn "「Yeah, that's true. 」"
        "After answering back, I also began to stand up.{p}Seeing this, Kouya extended a hand from above."
        ka "「Here, [fn]. 」"
        fn "「Thanks, Kouya. 」"
        "I took his hand, and pulled myself up next to him."
        "If someone saw from the end of the street,\nit'd look like a handshake."
    
        show ka 006 night with dis
        
        ka "「H-hey, [fn]. 」"
        "Kouya began to talk while we stayed that way."
        fn "「Hm? 」"
        ka "「Th-thanks,{w=.2} a lot. 」"
        
        hide ka with dis
        
        "After saying that,\nKouya turned his embarrassed face away\nand walked along, still holding my hand."
        fn "「Wa- 」"
        "-it a second."
        "I thought of saying it, but I stopped."
        "When I saw Kouya's tail wagging like that,\nI somehow lost the will to speak."
        "And occasionally, this sort of thing...{w=.2}\nisn't too bad."
        ka "「[fn]. 」"
        fn "「What? 」"
        ka "「Thanks, for coming out to meet me. 」"
        fn "「...yeah. 」"
    
        jump end21

####################################################

label end21:
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

    jump day22
