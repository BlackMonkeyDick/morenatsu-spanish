###Day 23
label day23:
    
    $ renpy.music.set_volume(1.0, 0.0, channel = "music")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound2")
    
    $ day = 23
    $ the_date = _("August 23")
    $ event_name = _("８月23日")
    
    if favorite == "tatsuki" or favorite == "kouya":
        window hide
        play music birds_chirping
            
        scene sky01 
        show text _("{size=+130}August 23") at truecenter
        with Dissolve(.5)
        
        pause 3
        scene black with Dissolve(1)
        pause .4
        
    else:
        jump day24
        
    $ renpy.jump (favorite + "23")
    
    
###################################################
label tatsuki23:
    
    $ event_name = _("After the Festival")

    scene tatsuki_bedroom with sdis
    
    "Inside the room, a faint light shone,\ninforming us that it was morning."
    "The insects have also just woken up,{w=.2}\nand I could hear the cicadas off in the distance.{p}They seemed unusually quiet today."
    "Tatsu-nii was still asleep next to me, naked."
    fn "「He's drooling in his sleep...{p}\ \ He's surprisingly cute when he's like this. 」"

    show ta 108 at center with dis
    
    ta "「Ng...{w=.2}Hwa-{w=.2}aa. 」"
    fn "「Morning, Tatsu-nii. 」"
    ta "「Morning, [fn]. 」"
    "After what happened last night,\nwe came back holding each\nother the whole way."
    "I went in and out of Tatsu-nii so many times..."

    show ta 401 with dis
    
    ta "「Aah... Oh, yeah.{w=.2} Today looks like a good day too... 」"
    fn "「Yeah. 」"
    
    show ta 408 with dis
    
    ta "「R-{w=.2}r-{w=.2}right. Y-{w=.2}you're not hurt, are you?{p}\ \ I wasn't too rough? 」"
    fn "「I'm fine,{w=.2} you were gentle to me.{p}\ \ But shouldn't that be the other way around?{w=.2}\n\ \ I topped you, after all.{w}Are you okay? 」"
    
    show ta 410 with dis
    
    ta "「I-i-i-i-idiot,{w=.2} I'm completely fine.\n\ \ There's a bit of you left in me though. 」"
    fn "「...Huh. 」"
    
    show ta 403 at jump_up
    
    ta "「Ah,{w=.2} no, not like that.{nw}"
    show ta 410 with dis
    extend " Uhh...{p}\ \ {nw}"
    show ta 401 with dis
    extend "In any case, I'm all good today.{p}\ \ Now then,{w=.2} let's do our best at work too! 」"
    fn "「Where are you going?{w=.2} There's no work today.{w}You\n\ \ said that the day after the festival is a holiday\n\ \ every year.{w}Anyway, put some clothes on. 」"
    
    show ta 403 with dis
    
    ta "「Ah,{w=.2} crap!{w}You're right! 」"
    
    hide ta with dis
    stop music fadeout .1
    play music shop01
    $ renpy.music.set_volume(0.7, 0.0, channel = "music")
    scene tatsuki_bedroom
    show ta 001 at center
    with sdis

    ta "「Let's go for a test flight today.{w}{nw}"
    show ta 009 at jump_up
    extend "{w=.2} Raah!{p}\ \ Get pumped! 」"

    hide ta with wipe_right
    
    fn "「Tatsu-nii,{w=.2} that's your closet. 」"
    "I'm embarrassed too, but just where did\nall that awkwardness come from?"
    "Is today going to be all right...?"

    $ event_name = _("Take Off!")
    
    scene prairie with wipe_down_slow 
    
    "The sun is high in the sky,\nand the sky today is perfectly clear."
    fn "「Whew,{w=.2} after doing all the preparations,\nit's already the middle of the day. 」"

    show ta 002 atc center with dis
    
    ta "「It's a good time for flying, isn't it?{p}\ \ It's all bright out, and conditions are good. 」"
    
    show ta 009 at jump_up
    pause .2
    
    ta "「Okay, let's start this already. 」"
    
    scene cave_inside with wipe_right
    
    "As Tatsu-nii said that, he put his hand on the door we\nnormally didn't use. It opened slowly,\ngiving a little peek into the familiar cave within."
    
    show ta 002 at center with dis
    
    ta "「I've been waiting for this day... 」"
    fn "「We're finally done. 」"
    
    scene biplane with dis
    
    "When I first saw the biplane, it didn't\nseem like it could fly, but now everything's repaired."
    "Some parts have even been improved."
    "The worn-out fuselage was painted a bright red,\nwhich now shone proudly in the sunlight."
    "It should be able to fly now, like this."

    scene cave_inside with wipeleft
    show ta 002 at center with dis
    
    ta "「All right,{w=.2} I'm off. 」"
    
    play music plane_start
    hide ta with dis
    
    "Tatsu-nii boarded the plane, then turned the ignition."
    "The engine started, and the propeller began spinning."
    fn "「Be careful. Don't take any risks. 」"
    ta "「I'll be back soon. Then we'll fly together. 」"

    scene white with qdis
    
    "The propeller spun faster,{w=.2}\nand Tatsu-nii aligned the plane on the runway."

    scene runway1 with dis
    
    fn "「Take care. 」"
    
    stop music fadeout 5
    
    "As it moved along the runway, its speed increased,\nand grew smaller into the distance."
    fn "「Tatsu-nii... 」"
    
    play sound plane_engine loop fadein 1
    $ renpy.music.set_volume(0.7, 0.0, channel = "sound")
    scene cockpit with wipe_right
    
    ta "「Damnit, the velocity's no problem.{w=.2}\n\ \ Is it just too heavy?{w}Son of a bitch, I won't\n\ \ make it at this rate.{w}Can't anything be done? 」"
    "The plane kept accelerating down the runway,\ngetting closer to the end."
    "There's nothing past the end of the runway.\nAt this rate, he'll run off the edge."
    
    stop sound  fadeout .5
    scene runway1 with wipe_right
    
    fn "「Fly...{w=.2} Tatsu-nii. 」"
    
    play music melodious05
    $ renpy.music.set_volume(0.9, 0.0, channel = "music")
    play sound plane_engine loop fadein .5 
    scene cockpit with wipe_right
    
    ta "「Fuuuuuck!{w=.2} Fly, damniiiiit! 」"
    
    scene cockpit with dis
    scene white with circle_out_slow

    "..."
    "..."
    "..."

    scene cockpit with sdis
    
    ta "「Am I floating? 」"
    "It's only a little, but the plane is floating in\nmidair, hovering just above the surface of the tarmac."
    "There's a little bit of wobble,\nbut for now it looks like he'll make it."
    ta "「Okay,{w=.2} if I go on like this... 」"
    "The runway disappeared, but the plane didn't fall."
    
    stop sound fadeout .5
    scene runway1 with wipe_right
    
    fn "「All right, you did it! Tatsu-nii, you're flying! 」"
    
    play sound plane_engine loop fadein 2
    $ renpy.music.set_volume(0.7, 0.0, channel = "sound")
    $ renpy.music.set_volume(0.8, 0.0, channel = "music")
    scene cockpit with wipe_right
    
    ta "「Aw man, give me a break. Scaring me like that... 」"
    ta "「Hehehe,{w=.2} better head back and get him on board. 」"
    
    stop sound fadeout .5
    scene runway1 with wipe_right
    
    "I'm glad. I'm really glad.\nI'm so glad my belly could burst."
    "I wonder when he'll be back?\nI hope it's soon."
    "What should I say if he gets back?\nStart off with his impressions, maybe."
    
    stop music fadeout 1
    play sound plane_engine loop fadein 2
    $ renpy.music.set_volume(0.8, 0.0, channel = "sound")
    scene cockpit with wipe_right
    
    ta "「Huh, why isn't it going up?\n\ \ Have I always been at this altitude? 」"
    ta "「The meter says I'm already at top speed,\n\ \ and I can't go any faster. Where's the problem? 」"
    ta "「I give up, I'm not going any higher.\n\ \ I'll just stay at this same altitude.\n\ \ Wait, am I falling? Crap... 」"
    
    stop sound fadeout .5
    scene prairie with dis
    
    fn "「Is that Tatsu-nii's plane?\n\ \ It's flying extremely low, though. 」"
    
    play sound plane_engine loop fadein 2
    $ renpy.music.set_volume(0.7, 0.0, channel = "sound")
    scene cockpit with wipe_right
    
    ta "「Hey, I'm begging ya, the speed can't drop, too...\n\ \ Don't tell me the engine's still faulty. 」"

    stop music fadeout .5
    scene prairie with sdis
    
    fn "「Is it still dropping somehow...?\n\ \ there's nowhere to land over there. 」"
    "That's definitely weird.\nTatsu-nii, Tatsu-nii, come back safely..."
    
    play sound plane_engine loop fadein 2
    $ renpy.music.set_volume(0.7, 0.0, channel = "sound")
    scene cockpit with wipe_right
    
    ta "「Dammit, I'm gonna fall! 」"
    ta "「[fn]... I'm sorry. 」"
    
    stop sound fadeout 5
    scene cockpit with dis
    scene white with sdis
    pause 2
    play sound bom35
    
    fn "{size=+15}「TATSU-NIIII!! 」"
    
    scene white with dis
    scene black with sdis
    play music sad03 fadein 5
    scene old_house_inside
    show tp 001 at midright
    show cu 006 at farright
    show ni 001 at farleft
    with sdis
    
    cu "「*sniff*{nw}"
    show cu at hit_right
    extend "{w=.2} *hic*.{w=.2} Young Master... 」"

    show tp 003 with dis
    
    tp "「Men don't cry openly. 」"
    
    show cu 008 with dis
    
    cu "「But... 」"

    show ni 002 with dis
    
    ni "「Tatsuki-kun,{w=.2} you're such an idiot... 」"

    scene old_house_inside with wipe_right
    show ta 005 at center with dis
    
    ta "「Sorry, making you all worry like that. 」"

    show cu 006 at midright with wipe_right
    
    cu "「*Sniff*,{w=.2} when I heard you crashed,{w=.2}\n\ \ I thought you'd died. 」"
    
    show ta 010 with dis
    
    ta "「Yeah, my bad. I'm all right now. 」"
    ta "「Still, it's great I fell above the forest.{p}\ \ It's thanks to the trees in good health\n\ \ I landed on that I only have grazes on me. 」"
    fn "「Are you really all right? 」"
    
    show ta 006 with dis
    
    ta "「I said I'm okay. You worry too much. 」"
    
    show cu 008 with dis
    
    cu "「B-{w=.2}but... 」"

    show ni 004 at farleft with wipeleft
    
    ni "「What do you mean by 'okay?'{p}\ \ Don't you understand just\n\ \ how much of a mess you've made? 」"
    ni "「If anything had happened to you,\n\ \ you'd inconvenience everyone around you.{p}\ \ Just how much did you think we all worried? 」"
    fn "「Wait. It's true that he worried us,\n\ \ but now, of all times... 」"
    
    show ta 010 with dis
    
    ta "「Calm down. How long are you going to have such a\n\ \ gloomy face?{w}I'm back, and that's all that matters,\n\ \ right?{w}I'm sorry for bothering you. 」"
    
    show ni 001 with dis
    
    ni "「Hmph... 」"

    scene old_house_inside with wipe_right
    show tp 003 at center with dis
    
    tp "「Well, no helping how much we've talked over here.\n\ \ Stop huddling together. Break it up,{w=.2} break it up. 」"
    tp "「Oh, and [fn]?{p}\ \ You can go back home starting tomorrow.\n\ \ Tetsu will be back by then. 」"
    fn "「Eh?{w=.2} But- 」"
    "Tappei-san caught me by the scruff of my neck,\nand from there he whispered to me."
    
    hide tp
    show tp 003 big at center_big_tp
    with dis 
    
    tp "「He probably wants to be alone for now.\n\ \ Can't you do that for him just for today? 」"
    
    show tp 002 big with dis
    
    tp "「He's always been stubborn.\n\ \ All that bravado is probably a facade. 」"
    fn "「Really? I see...{w=.2} I understand. 」"
    
    show tp 001 big with dis
    
    tp "「My bad. 」"
    "I guess even the blunt Tappei-san\nmust worry as a father."

    hide tp
    show tp 001 at center
    with dis
    
    tp "「Hey hey, how long are you bastards gonna sit\n\ \ in the living room?{w}I'm not gonna relax,\n\ \ even if this is our holiday. 」"
    tp "「Get back to your rooms already. 」"
    cu "「Well... Excuse me. 」"
    
    show ni 002 at farleft behind tp with dis
    
    ni "「I'll be going out. 」"
    fn "「Bye. 」"
    
    hide tp
    show ta 010 at center behind ni
    with wipe_right
    
    "I guess I'll get my stuff together and head home..."    
    fn "「Tatsu-nii... 」"
    
    show ta 006 with dis
    
    ta "「My bad,{w=.2} making you worry like that. 」"
    fn "「What happened to the plane? 」"
    
    show ta 005 with dis
    
    ta "「It's caught up in the trees.\n\ \ It's in a hard-to-reach-place, so it doesn't seem\n\ \ like we can get it out anytime soon. 」"
    fn "「Is that so. 」"
    
    show ta 008 with dis
    
    ta "「Sorry,{w=.2} looks like I can't keep my promise. 」"
    fn "「Don't worry about that. 」"
    
    show ta 002 with dis
    
    ta "「Hehehe, I'm really tired.{p}\ \ Tommorow looks good too, so can you let me sleep?{p}\ \ Later.{w=.2} I'll see you tomorrow. 」"
    
    hide ta with sdis
    
    "Tatsu-nii addressed me as cheerfully as usual,\nthen went back to his room."
    "He said he's okay, but that can't be true."
    "His face is all smiles,\nbut really, he should want to cry..."
    "In a time like this,{w=.2} what's the best thing I can do?"

    jump end23


###################################################
label kouya23:
    
    $ event_name = _("4th Day's Aspiration Survey Book")
    
    play music free0258
    scene bedroom with dis
    show ka 005 at center with dis
    
    ka "「...Are you seriously saying that? 」"
    fn "「I'm seriously saying it. 」"
    ka "「Well I do appreciate you saying that but...{p}\ \ Your break is about to end soon.{w=.2} Are you sure\n\ \ you want to continue hanging around with me? 」"
    "Kouya was making a worried face.{p}And the one causing him to look so worried was me."
    "Today's the day I'm supposed to leave his house,{w=.2}\nand go back to my grandparents', just as planned."
    "Since that was promised from the start,{w=.2}\nI wasn't planning on saying anything\nat this point in time."
    "I do want to stay here for a while longer,{w=.2}\nbut that's a different discussion."
    "So why is Kouya so worried?"
    "Because I made a new \"request\"."
    fn "「If you're okay with it,\n\ \ and the rest of the band, too...\n\ \ But only if. 」"
    "Kouya took in my words while\ngroaning and scratching his head."
    
    show ka 001 with dis
    
    ka "「Well,{w=.2} I'm sure that if there\n\ \ was another hand around things would change...{p}\ \ But still, why are you saying this all of a sudden? 」"
    ka "「This 『I want to help with band practice』 thing. 」"
    "Yes,{w=.2} that was my new request."
    "These three days.{w} It was just three days,\nbut so much has happened."
    "I haven't said all of it before,{w=.2}\nbut I've seen so much."
    "After thinking about it, that was my conclusion."
    fn "「...Since last night,{w=.2} I've thought a lot.{p}\ \ About what's happened over the past\n\ \ three days, and of other things. 」"
    fn "「In these three days,{w=.2} I learned a lot about you\n\ \ that I didn't know about until now. 」"
    fn "「About how you fought\nwith your dad and left your home,{w=.2}\n\ \ and how you've never been back until recently. 」"
    fn "「And now, how you've bet everything\n\ \ on the next contest.{w} I saw all of that.{p}\ \ Always by your side. 」"
    fn "「At the end of the three days,{w=.2}\n\ \ you'll go back to band practice,\n\ \ and I'll go back to my vacation. 」"
    fn "「Everything I've done will fade into memory. 」"
    fn "「But I wondered if I was really okay with that.{p}\ \ I've made it my business up to this point,\n\ \ but isn't there more I could do? 」"
    fn "「...No, that's not it.{p}\ \ I thought 'I want to do something.' 」"
    fn "「This isn't a sense of responsibility.\n\ \ I just wanted to be your strength. 」"
    
    show ka 002 with dis
    
    ka "「So it's like that, huh? 」"
    "Kouya asked me in a kind voice.{p}His confused expression from before had disappeared,\nand now he's smiling gently."
    fn "「Yeah.{p}\ \ I've thought about it, and I've decided.{p}\ \ I want to see this to the end. 」"
    "I was aware of how selfish I was sounding.{p}The best I can do is random chores.{p}If I do things badly, I'll only get in the way."
    "Even so, I still want to be with him.{p}For me to not speak up about my feelings\nand to leave things as they are now..."
    "That's out of the question."
    
    show ka 001 with dis
    
    ka "「...Really,{w=.2} you sure it's okay?{p}\ \ It's your first vacation back and all. 」"
    fn "「I've said it haven't I?{w=.2} I've thought about it,\n\ \ and I've decided.{w}No matter how many times you ask,\n\ \ my answer won't change. 」"
    "This time Kouya sighed a little.{p}Then, he laughed."
    
    show ka 014 with dis
    
    ka "「My god... You sure are curious.{p}\ \ {nw}"
    show ka 002 with dis
    extend "All right, I'll ask.{w} Just wait a sec. 」"
    "After that, Kouya picked up the phone.{p}He punched in a number from memory,\nthen held the receiver up to his ear."
    
    play sound call02
    pause 3
    play sound call02
    
    "The person he'll be talking to\non the other end of the line\nis probably one of the people in the band."
    
    show ka 001 with dis
    
    ka "「Hello,{w=.2} it's me.{p}\ \ There's something I want to discuss... 」"
    "Kouya spoke into the receiver.{p}It seems he knows this person."
    "Occasionally glancing at me,{w=.2}\nKouya repeated his explanations and questions."
    "I paid close attention to the conversation\nas I strained my ears."
    ka "「...Yeah,{w} that's right...{p}\ \ Understood,{w=.2} we'll head over right now.{p}\ \ See you later, then. 」"
    
    play sound call05
    
    "And then the reciever was put back.{p}Kouya turned to me."
    ka "「You got that, right? 」"
    "I nodded in silence in answer to his question.{p}Having confirmed that, Kouya continued."
    ka "「The guy I was talking to just now was our leader.{p}\ \ I think he's fine with it,{w=.2}\n\ \ but we're going to go meet him. 」"
    fn "「Okay... 」"
    "This time I spoke up and nodded harder.{p}Even I could tell I was feeling nervous."
    "Reading through my expression,\nKouya's face relaxed."
    
    show ka 002 with dis
    
    ka "「Don't worry, he just wants to talk about it,{w=.2}\n\ \ so you can relax.{p}\ \ You don't need to look so stiff. 」"
    fn "「R-{w=.2}really? 」"
    ka "「Yeah, that's the kind of guy he is.{p}\ \ He's said stuff like 'is that sort of thing okay?' 」"
    ka "「Since that's how it is, we'll be going to Kazenari.{p}\ \ Get ready. 」"
    
    stop music fadeout 3
    scene black with wipe_right
    pause 1.5    

    $ event_name = _("Going up")
   
    play music shop03
    scene kazenari01 with wipe_right
    
    "We got onto Kouya's bike, and drove into Kazenari."
    "Parking the motorcycle in front of the music store\nwhere Kouya worked,{w=.2} we walked to the cafe\nwhere we'd promised to meet."
    "Being a larger town than Minasato,\nit naturally has more people.{p}It feels a little strange."
    "Maybe it's because I'm a\ncountry guy in a bigger city.{p}With more people around,{w=.2} it somehow feels fresher."
    "But for me to feel that way,{w=.2}\nit's kind of funny.{p}I came from the city myself, after all."
    "Normally I wouldn't really mind it,{w=.2}\nbut I think I do now because I'm oddly tense."
    "Kouya said it wasn't necessary,\nbut it's hard for me to get over it."
    fn "「Hey,{w=.2} Kouya.{p}What kind of person is your leader? 」"
    "I figured I could ease my\nanxiety a bit by asking a question."
    
    if meet_band != True:
        jump kouya23_leader_unknown


########################################################
label kouya23_leader_known:
      
    $ event_name = _("That Guy and the Impromptu Interview")
    
    show ka 001 at center with dis
    
    ka "「Haven't you met him once before?{p}\ \ It's Keisuke, Kei-su-ke.{w}That horse. 」"
    fn "「Ah, so Keisuke-san is the leader? 」"

    scene black with dis
    show ke 006 at center with dis
    
    "In my mind a heartily-laughing horseman appeared,{w=.2}\npulled a victory pose, then disappeared again."

    scene black with dis
    scene kazenari01 with dis
    show ka 001 at center with dis
    
    "Somehow, that's the image I have in my head."
    ka "「Well, that's because he's 20,\n\ \ and the oldest among us.{p}\ \ Work-wise...{nw}"
    show ka 013 with dis
    extend " He pulls his weight. 」"
    fn "「Huh... I see then. 」"
    "Hang on... What was that?{p}It bugs me.{w}It bugs me, but if I worry\nabout it I feel like I'll forget it."
    "...Oh well, I'll just ignore it."
    fn "「I see.{w=.2} If it's Keisuke-san,\n\ \ I can relax a little bit. 」"
    
    show ka 002 with dis
    
    ka "「Right?{w} He's a pretty lax guy,{w=.2}\n\ \ so it's all right to loosen up.{p}\ \ No need to get worked up like that. 」"
    ka "「He'll just want to talk for a bit.{p}\ \ You don't need to worry about anything. 」"
    fn "「Yeah,{w=.2} you're right.{p}\ \ All right, I feel a bit better now. 」"
    
    show ka 003 with dis
    
    ka "「That's the most important thing.{p}\ \ Now, loosen up those shoulders and let's go. 」"
    "Kouya clapped me on the back,\nthen quickened his pace.{p}I matched his speed to make sure we weren't late."

    hide ka with dis
    
    "A short while later, we arrived.{p}It was just inside an alleyway off the main street.{p}Established there was a well looked-after cafe."
    "The retro-style door contained a glass panel,{w=.2}\nso it was possible to peek inside through that."
    "It was early in the morning, probably not even 9.{p}That might be why there aren't many people inside.{p}I could count how many were in there on one hand."
    "Well, if a lot of people were\ninside a cafe at this hour,{w=.2}\nthat'd be something odd in itself."
    ka "「Oh,{w=.2} he's already here. 」"
    "Kouya, who like me was also\nlooking in through the glass,\nquietly murmured to me."
    fn "「Keisuke-san? 」"
    ka "「Yeah.{p}\ \ He's sitting further in and eating. 」"
    
    scene black with dis
    scene cafe with dis
    show ka 001 at center with dis
    play sound iron_pipe
    
    "We opened the door, and went inside.{p}The dingling of the bell announced our appearance."
    "After the customary 'Welcome,'{w=.2}\na voice called out to us, going 'Hey!'"
    "Kouya walked straight over\nto the source of the voice."
    ka "「Sorry.{w} Did we keep you waiting, Keisuke? 」"
    "A familial exchange of words.{p}In front of us was a light brown-haired horseman.{p}He was sitting at a four-person table."
    "I've met him once before.{p}There was no mistaking it, it's Keisuke Hirama."

    hide ka with wipe_right
    
    show ke 001 at center with wipe_right
    
    ke "「Nah, just got here.{p}\ \ I was hungry, so I got something to eat.{p}\ \ Ah, long time no see, [fn]. You doing okay? 」"
    fn "「Yeah,{w=.2} I'm fine. Thanks. 」"
    
    show ke 002 with dis
    
    ke "「That's what's most important.{p}\ \ {nw}"
    show ke 001 with dis
    extend "Anyway,{w=.2} have a seat. 」"
    "At Keisuke-san's insistence,{w=.2} I sat next to Kouya.{p}Keisuke-san was sitting directly opposite me."

    hide ke with dis
    show ka 001 at midleft
    show ke 001 at midright
    with dis
    
    ke "「This is a surprise.{p}\ \ All of a sudden, Kouya calls me up and tells me\n\ \ that you want to help out with the band. 」"
    ka "「Yeah, it was kinda out of the blue.{p}\ \ I was also wondering what you\n\ \ were talking about, at first. 」"
    fn "「Yeah, sorry for bringing it up so suddenly. 」"
    
    show ke 006 with dis
    
    ke "「No, no,{w=.2} it doesn't really matter.{p}\ \ Actually, since it was you, [fn],\n\ \ I'd totally welcome that. 」"
    "I hung my head in apology,{w=.2}\nand then Keisuke-san said that as a follow-up."
    
    show ke 001 with dis
    
    ke "「Right now, we can't do anything yet,{w=.2}\n\ \ but I'm thinking of having you\n\ \ show up the day after tomorrow. 」"
    fn "「Okay...{w}Wait,{w=.2} really? 」"
    "I was suprised at how easily he gave the OK.{p}I thought there'd be more to it."
    ke "「I don't have a reason to say no.{p}\ \ Besides, this was what you wanted to do, wasn't it? 」"
    fn "「Well, yeah... 」"
    ke "「Then there's no problem at all!{p}\ \ The other two guys know you already,{w=.2}\n\ \ so you'd be great as an assistant. 」"
    ke "「Besides, we're on the home stretch,\n\ \ the fine-tuning period. 」"
    ke "「If you could listen to our performance,{w=.2}\n\ \ then give us your honest thoughts on it,\n\ \ we'd really appreciate that. 」"
    ke "「It's not like I'm busking anymore.{p}\ \ It sounds completely different when you're playing. 」"
    
    show ke 008 with dis
    
    ke "「Besides,{w=.2} my beloved Kouya's asking\n\ \ for a favor, so how can I say no? 」"
    
    show ka 014 with dis
    
    ka "「What did you just call me? 」"
    
    show ke 001 with dis
    
    ke "「I have to let the other members know.\n\ \ Because of that, work starts two days from now. 」"
    ke "「Yuuki isn't here tomorrow,\n\ \ and I can't get a hold of him. 」"
    
    show ke 006 with dis
    
    ke "「With that out of the way,{w=.2}\n\ \ let's work well together, [fn]! 」"

    jump kouya23_accepted

###################################################
label kouya23_leader_unknown:
    
    $ event_name = _("Whoever That Guy Is and the Impromptu Interview")
    
    show ka 005 at center with dis
    
    ka "「Hmmmmm...{w} He's a horseman called Keisuke Hirama.{w=.2}\n\ \ 'Bright Moodmaking Drumming Older Brother'\n\ \ kind of guy, or something. 」"
    fn "「...Or something? 」"
    "「What's that about? 」{w=.2}\nI silently asked with a furrowed brow."
    
    show ka 001 with dis
    
    ka "「It's self-styled.{w=.2} That's what he calls himself.{p}\ \ Well, it isn't necessarily wrong...{p}\ \ Anyway, that's the kind of guy he is. 」"
    fn "「Huh... 」"
    "I didn't really get what he was saying,\nand I let slip a half-baked reply.{p}Noticing that,{w=.2} Kouya tried to elaborate further."
    ka "「What?{w=.2} I said you don't need to worry so much.{p}\ \ He'll probably just ask a few questions.{w=.2}\n\ \ Nothing to be so tense about. 」"
    ka "「Besides, it's not like you'll need to say much,{w=.2}\n\ \ he'll just want to talk for a bit.{p}\ \ Nothing to be so nervous about. 」"
    fn "「Y-yeah.{w}I'll do my best. 」"
    
    show ka 003 with dis
    
    ka "「Oh, you. 」"
    "Whatever I just did made Kouya laugh a little."
    fn "「What? What are you laughing about?{p}\ \ Did I do something weird? 」"
    ka "「No, it's nothing. 」"
    "Kouya kept up his smile as he said that.{p}I wasn't really satisfied by that."
    fn "「Seriously, what is it? 」"
    ka "「It's nothing, really.{p}\ \ ...Anyway, good luck. 」"
    "Kouya clapped me on the back,{w=.2}\nthen quickened his pace.{p}I matched his speed to make sure we weren't late."
    "All of a sudden,{w=.2} I couldn't keep up with his smile.\nWhile I thought up a complaint,\nI let go of his hand."

    hide ka with dis
    
    "A short while later, we arrived.{p}It was just inside an alleyway off the main street.{p}Established there was a well looked-after cafe."
    "The retro-style door contained a glass panel,{w=.2}\nso it was possible to peek inside through that."
    "It was early in the morning. Probably not even 9 yet.{p}That might be why there aren't many people inside.{p}I could count how many were in there with one hand."
    "Well, if a lot of people were inside a cafe\nat this hour,{w=.2} that'd be something odd in itself."
    ka "「Oh,{w=.2} he's already here. 」"
    "Kouya, who like me was also looking in\nthrough the glass, quietly murmured to me."
    fn "「You mean Hirama-san? 」"
    ka "「Yeah.{p}\ \ He's sitting further in and eating. 」"

    scene black with dis
    scene cafe with dis
    show ka 001 at center with dis
    play sound iron_pipe
    
    "We opened the door, and went inside.{p}The dingling of the bell announced our appearance."
    "After the customary 「Welcome, 」{w=.2}\na voice called out to us, going 「Hey! 」"
    "Kouya walked straight over\nto the source of the voice."
    ka "「Sorry.{w}Did we keep you waiting, Keisuke? 」"
    "A familial exchange of words.{p}In front of us was a light brown-haired horseman.{p}He was sitting at a four-person table."
    "I guess he's the 'leader' in question."

    hide ka with wipe_right
    show ke 001 at center with wipe_right
    
    $ encounter_keisuke = True
    
    ke "「Nah, just got here.{p}\ \ I was hungry, so I got something to eat.{p}\ \ So,{w=.2} is that him behind you? 」"
    ka "「Yeah,{w=.2} just like I said on the phone. 」"
    ke "「Huh, I see then.{p}\ \ All right you two,{w=.2} sit down over here. 」"
    ka "「'Kay. 」"
    "At his insistence, I sat down next to Kouya.{p}Hirama-san was sitting directly opposite me."

    hide ke with dis
    show ka 001 at midleft
    show ke 001 at midright
    with dis
    
    ke "「Now, first off is introductions, yeah?{p}\ \ Kouya's probably already told you,{w=.2} but I'm Keisuke Hirama.{p}\ \ {nw}"
    show ke 002 with dis 
    extend "Nice to meet ya. 」"
    "At Hirama-san's words,\nI became a little flustered and hung my head."
    
    show ke 001 with dis
    
    ke "「Kouya and I, then two other guys, came together\n\ \ to form a band,{w=.2} and for now, I've become the leader.{p}\ \ It's only in name, though. 」"
    ka "「You got that right. 」"
    
    show ke 002 with dis
    
    ke "「Hey! You can't go finishing for others like that.{p}\ \ You're hurting your big brother's feelings! 」"
    "Hirama-san said that to Kouya with a carefree smile.{p}Then he turned to me with the same expression."
    ke "「Now,{w=.2} you are...{nw}"
    #[emb exp="f.mname.charAt(0)"]  #!#Find out if it's possible to extract the first letter from name
    extend " ... 」"
    fn "「Ah, I'm [fn] [ln]. 」"
    "Since I spoke so abruptly, my voice quavered.{p}In an instant my face felt hot."
    
    show ka 005 with dis
    
    "Hirama-san saw that and laughed in a way\nthat his teeth gleamed."
    "I didn't look at Kouya,\nbut he was probably smiling, too."

    show ka 001 at midleft #!# Position
    show ke 001 at midright
    with dis
    
    ke "「Come on, no need to be so nervous.{p}\ \ It's just that I want to get to know\n\ \ possible assistants first. 」"
    ke "「Even then, I'm not that good at being tough.{w=.2}\n\ \ Don't really care for formal language.{p}\ \ Just call me by first name.{w=.2} I'll be doing it too. 」"
    ke "「Actually, I think everyone in the band\n\ \ calls each other by first name. 」"
    fn "「Ah,{w=.2} I understand. 」"
    
    show ke 003 with dis
    
    ke "「Formal- 」"
    fn "「-Sorry, got it. 」"
    
    show ke 002 with dis
    
    ke "「Yeah, yeah. Like that. 」"
    
    show ke 001 with dis
    
    ke "「So first of all,{w=.2} I think I'll have you show\nup for band practice the day after tomorrow. 」"
    fn "「Okay...{p}\ \ Wait,{w=.2} really? 」"
    "I was suprised at how easily he gave the OK.{p}I thought there'd be more to it."
    ke "「I don't really have a reason to say no.{p}\ \ I was planning on saying yes from the start. 」"
    ke "「Besides, we're on the home stretch,\n\ \ the fine-tuning period. 」"
    ke "「If you could listen to our performance,{w=.2}\n\ \ then give us your honest thoughts on it,\n\ \ we'd really appreciate that. 」"
    ke "「It's not like I'm busking anymore.{p}\ \ It sounds completely different when you're playing. 」"
    
    show ke 008 with dis
    
    ke "「Besides,{w=.2} my beloved Kouya's asking\n\ \ for a favor, so how can I say no? 」"
    
    show ka 014 with dis
    
    ka "「What did you just call me? 」"
    ke "「I have to let the other members know. Because of\n\ \ that, work starts two days from now. 」"
    ke "「With that out of the way,{w=.2}\n\ \ let's work well together, [fn]! 」"


############################################
label kouya23_accepted:
    
    $ event_name = _("Speech of Warning")
    
    "He extended his hand from across the table.{p}I was a bit overwhelmed by Keisuke-san\nas I took his hand."
    fn "「Y-{w}yeah, looking forward to it. 」"
    
    show ka 005 with dis
    
    ka "「{cps=5}. . . . . . 」"
    "Kouya was staring at us from the side\nat Keisuke-san's forced movements."
    "He didn't say anything, but I understood.{p}「Say something. 」{p}That's what he wanted to say through his eyes."
    
    show ke 001 with dis
    
    ke "「So anyway,{w=.2} what made you decide\n\ \ you wanted to help us?{p}\ \ I mean, I'm happy about it, but I'm so curious. 」"
    
    show ka 001 with dis
    
    ka "「Hey, you ass!\n\ \ Did you ignore everything I said earlier? 」"
    "This time he did speak up."
    "However, Keisuke-san met that with a wide smile."
    
    show ke 003 with dis
    
    ke "「Whaaat, Kouya?{w} I'm still interviewing [fn].{p}\ \ Are you feeling lonely because I haven't paid\n\ \ attention to you for a few minutes? 」"
    
    show ka 014 with dis
    
    ka "「...No,{w=.2} it's fine. 」"
    "Scowling, Kouya muttered under his breath."
    "I haven't seen him make a face like that before.{w=.2}\nI didn't know he made faces like that."
    
    show ke 001 with dis
    
    ke "「Come on, no need to pout like that.{p}\ \ I'll get right into your business later,\n\ \ until you're sick of it. 」"
    
    show ka 001 with dis
    
    ka "「Seriously sorry, I'll deal with it. 」"
    ka "「While we're at it, would you do me a favor\n\ \ and go to a hospital?{p}\ \ One with nice padded walls. 」"
    ke "「So,{w=.2} what's your reason? 」"
    fn "「Ehh? 」"
    "I was watching back and forth between them,{w=.2}\nwhen the focus abruptly shifted back to me.{p}It was quite startling."
    "Man, that's been happening a lot."
    ke "「Like I said,{w=.2} what makes you want\n\ \ to help out with our band?{p}\ \ What for? 」"
    fn "「Umm... 」"

    scene cafe with dis
    
    "I felt a little worried about being asked again."
    "This morning, I told Kouya my deepest feelings.{p}I want to be his strength.{p}I want to see everything through to the end."
    "After thinking that, I asked to help."
    "But now that I think about it again,{w=.2}\nI'm a bit reluctant to tell anyone besides Kouya.{p}I mean, it's embarrassing."
    "Keisuke-san stared at me while waiting for my answer.{p}I guess the subject won't change\nuntil I say something."
    "Kouya stole a sidelong glance at me,\nas if wanting to help."
    "I guess Kouya was thinking about the same thing,{w=.2}\nsince he was looking a little worried."
    "...If that's the case, time for me to get ready!"

    show ka 001 at midleft
    show ke 001 at midright
    with dis
    
    fn "「I... 」"
    ke "「I...? 」"
    fn "「I wanted to be Kouya's strength...{p}\ \ Or something like that. 」"

    show ka 013
    show ke 004
    with dis
    
    ke "「{cps=5}... 」"
    "Keisuke-san stared at me blankly."
    "Ahh,{w=.2} now I've done it.{p}I felt like running away and hiding."
    "I must have looked really funny,{w=.2}\nbecause Keisuke-san..."
    
    show ke 002 with dis
    
    ke "「*Snort*...{w=.2} Hahahaha! 」"
    "...Started laughing from the bottom of his lungs."
    "Because he was laughing so much,{w=.2}\nI felt that much more embarrassed.{p}At this point, I'm sure my face is bright red."
    
    show ka 001 with dis
    
    ka "「Hey, Keisuke,{w=.2} stop laughing so much. 」"
    ke "「Whew, sorry.{w=.2} But it was funny\n\ \ to see him say something so bold\n\ \ and get all embarrassed by it. 」"
    
    show ke 001 with dis
    
    ke "「But that's a good reason.{p}\ \ Really? I see, then.{w}Yep yep. 」"
    "Keisuke-san kept nodding his head\nas he agreed with himself."
    
    show ke 006 with dis
    
    ke "「Oh, the springtime of youth. 」"
    
    show ka 005 with dis
    
    ka "「The only place it's spring around\n\ \ here is in your damn head.{p}\ \ And enough of you and your teasing. 」"
    
    show ke 003 with dis
    
    ke "「Oh no, now I've made Kouya feel awkward.{p}\ \ {nw}"
    show ke 001 with dis
    extend "Well, if you're saying that, then how about we\n\ \ break things off here? 」"
    
    play sound bosu10_c
    
    "Keisuke-san picked up his receipt,\nand got up from his seat.{p}A few moments later, Kouya and I also left the cafe."

    play sound iron_pipe
    scene black with wipe_right
    scene kazenari01 with wipe_right
    show ka 001 at midleft
    show ke 001 at midright
    with wipe_right
    
    ke "「Okay, I'll be going back for now.{p}\ \ Kouya, there's a meeting at 6 today.{p}\ \ Don't you forget that. 」"
    ka "「You saying not to forget\n\ \ about the time just irritates me.{p}\ \ You said that Yuuki won't be here tomorrow, yeah? 」"
    ke "「Yeah.{w}But Jun's okay for today,{w=.2}\n\ \ so I figure we should let him know. 」"
    ka "「Well, I guess that's true. 」"
    
    show ke 002 with dis
    
    ke "「Well then, my regards.{p}\ \ Later, [fn],{w=.2} see you two days from now. 」"
    fn "「Yeah, I look forward to working with you too. 」"

    scene kazenari01 with wipe_right
    show ka 001 at center with wipe_right
    
    "Keisuke-san waved, and left down the street.{p}A while after we saw him off,{w=.2} Kouya spoke up."
    ka "「...Shall we head back, too? 」"
    fn "「...Yeah. 」"

    hide ka with dis
    
    "We turned around, and walked side by side."
    "There was a bit of awkwardness between us.{p}Somehow I think I know why.{p}It's probably Keisuke-san's fault."

    scene black with wipe_right
    scene music_shop with wipe_right
    
    "Because of that,{w=.2} we walked along in silence."
    "We picked up the bike\nfrom the front of the music store,\nand drove back to Minasato Village."

    scene black with wipe_right
    scene kouya_apartment with wipe_right
    
    "Nothing really changed on the way back,{w=.2}\nand the only thing close to a conversation\nwas when we went got off the bike."
    fn "「All right, I should get back\n\ \ to my grandparents' house. 」"
    ka "「Yeah. 」"
    "And now I was standing in the entryway,\nmy luggage in hand.{p}Kouya was there to see me off."
    
    show ka 001 with dis
    
    fn "「Thanks for the past three days.{p}\ \ And thanks for taking care of me. 」"
    ka "「No, that's something I should be saying.{p}\ \ I really do have to thank you. 」"
    fn "「No no, you don't need to do that. 」"
    "While I smiled a bit at his words,{w=.2}\nI waved my hand a little to deny it."
    "And then they faded out."
    
    stop music fadeout 7.5
    
    fn "「...All right, thanks again for everything.{p}\ \ I'll be going now. 」"
    ka "「Yeah, careful on your way home. 」"
    "It's not like we weren't going to meet again,{w=.2}\nyet this felt like some grand formal exchange.{p}I almost laughed."
    fn "「Right, thanks.{p}\ \ Well, see you in two days. 」"
    ka "「Yeah. 」"
    "I turned my back to Kouya,\nand reached for the doorknob."
    "It was then."
    ka "「...Hey. 」"
    fn "「Hm? 」"
    "The call stopped me and made me turn my head."
    "Kouya was making an expression\nthat suggested he had something difficult to say."
    
    show ka 013 with dis
    
    ka "「Um, well... 」"
    "Looking embarrassed, Kouya stopped talking there.{p}But a moment later,{w=.2} he continued right on."
    
    show ka 001 with dis
    play music free31
    
    ka "「Since it's only a couple days from now,\n\ \ wanna keep staying over? 」"
    fn "「Eh? 」"
    ka "「Well, in a couple of days you'll\n\ \ be commuting to Kazenari, won't you? 」"
    ka "「It's more convenient if you go with me,{w=.2}\n\ \ and if you're going with me,\n\ \ it'd be easier to stay here. 」"
    ka "「It's fine if you want to stay over starting today,{w=.2}\n\ \ but like Keisuke said,\n\ \ today's practice might drag on for a while. 」"
    ka "「So, in the next few days.{p}\ \ If you're okay with it...\n\ \ Will you stay over? 」"
    fn "「Kouya... 」"
    "It wasn't an invitation I was hoping for.{p}I didn't really expect something like this."
    
    show ka 005 with dis
    
    ka "「So,{w=.2} will you? 」"
    "Kouya seemed just a little uneasy as he asked.{p}It's kind of charming."
    "He didn't have to be so embarrassed about it."
    "I was so happy about it, that the\n'getting to practice' thing didn't mean much to me."
    fn "「Seriously? 」"
    ka "「Why would I lie? 」"
    fn "「But wouldn't that bother you? 」"
    ka "「If I thought that,\n\ \ I wouldn't be offering in the first- 」"
    "That's where it seemed that Kouya noticed."
    
    show ka 003 with dis
    
    ka "「...This is just like three days ago. 」"
    "The two of us got a good chuckle out of that."
    "Three days ago, the same thing happened.{p}So in that case,{w=.2} the next thing to say is-"
    
    show ka 001 with dis
    
    ka "「Do I have to say it again? 」"
    "He asked me again after noticing my look.{p}I nodded slightly."
    
    show ka 006 with dis
    
    "He groaned, closing his eyes and scratching his head.{p}After straightening out his thoughts,\nhe looked right into my eyes."
    
    show ka 001 with dis
    
    ka "「I want you to stay at my place.{p}\ \ But only if you're okay with that.{p}\ \ Or, do you... Not want to, this time? 」"
    fn "「No, that's not it.{p}\ \ Then I guess I'll take you up on your offer.{p}\ \ ...Please take care of me, Kouya. 」"

    jump end23
    
#########################################################
label end23:
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
    
    jump day24

