##This will be the Script for the Welcome Back Party

screen nightshow():
    add  FileCurrentScreenshot() xpos 100 ypos 100 at menublur
    

#################################################
label begin:  
    
    $ var0 = 0
    $ var1 = 0
    $ var2 = 0
    
    $ renpy.music.set_volume(1.0, 0.0, channel = "music")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound2")
    
    $ day = 1
    $ the_date = _("August 1")
    $ event_name = _("The Letter")
    
    scene black
    
    scene hhome with Dissolve(1)
    play music cicada01 fadeout 1
    $ renpy.music.set_volume(0.6, 0.0, channel = "music")    
    
    ##$ event_name = "Test"
    #$ change = renpy.list_slots(regexp=None)
    #$ change = renpy.newest_slot(regexp=None)    
    #"The newest save is [change]"   
    
    fn "「Haaaaah... 」"
    "It's called summer vacation, \nbut there's nothing to do...{p}Especially when you don't have any hobbies."
    fn "「Guess I'm not doing anything this summer either... 」"
    mom "「What are you talking about?{p}\ \ The weather outside is nice today, \n\ \ and you're lying around doing nothing. 」"
    mom "「Anyway, did you do your homework? 」"
    fn "「Of course I did it.{p}\ \ Sheesh, it's vacation, \n\ \ and all I'm doing is being lazy. 」"
    mom "「Oh, that's right.{p}\ \ A letter from one of your friends came today.{p}\ \ It sounds familiar. 」"
    fn "「A letter? In this age?{p}\ \ I didn't know I had a friend like that. 」"
    
    play sound paper1
    scene letter with circle_out_slow

    "This was the letter from my old friend."
    "The handwriting was bad, \nand the sentences were short."
    "\"Hey, how are you doing?{p}I'm the same as usual.{p}Everybody really wants to see you.\""
    "\"Come and visit every once in a while.{p}I'll be waiting.\""
    fn "「The handwriting's sort of crappy...{p}\ \ and they probably should've written more...{p}\ \ but it seems sincere. 」"
    "This letter is from my hometown, \nMinasato Village."
    "Various things started to surface in my mind.{p}That endless blue sky, \nand under it the vast countryside."
    "The sounds of the insects, \nand the murmuring of the streams."
    "The trees rustling in the gentle breeze, \nand the faces of my childhood friends, \nas we played until sunset."
    "I never forgot about all of those memories..."
    fn "「I'm going home! 」"
    
    scene hhome with qdis
    #pause 1
    
    ##########################
    $ event_name = _("On the Bus")
    ##########################
    
    #scene black with wipe_up
    pause 1.5
    play music car 
    $ renpy.music.set_volume(0.6, 0.0, channel = "music")
    scene bus with wipe_up_slow

    "That was yesterday."
    "I immediately contacted my old friend. {p}His phone number hadn't changed, \nand he sounded a little embarrassed."
    "I left home that very same day."
    fn "「It's an hour-long bus ride to town... {p}\ \ just a little bit more. 」"
    "The window on the bus was cold to the touch. {p}The same mountain scenery continued on, \nbut I had a feeling we were getting close."
    fn "「Ugh, it's so cold. {p}\ \ Why doesn't this bus have AC? 」"
    "However, my body temperature is the opposite.{p}It's been so long since I've been there, \nthe inside of my chest is hot and beating fast."
    "I wonder how everybody is doing."
    "I haven't talked to any of them since I moved. \nHeard they were all going to the same high school."
    "Never really thought of going to see them."
    "I should have visited them earlier. {p}I'm excited to see everyone.  {p}Wonder what's going on in town right now."

    play sound chime1
    pause 1

    driver "「Next stop, Minasato. {p}\ \ Please press the stop button if you are departing. 」"
    fn "「Yeah, I'm getting off. 」"
    "In just a minute, no, a few seconds I'll be there. {p}I feel somewhat pleasant, calm, and happy. {p}I'm a little embarrassed feeling like this."
    "Hurry, hurry, I can't wait any longer."

    $ renpy.music.set_volume(1.0, 2.0, channel = "music")
    scene white with qdis
    scene sky01 with Dissolve(2)
    pause 1
    scene sky02 with Dissolve(2.5)
    pause 1
    stop music fadeout 3
    
    ################################
    $ event_name = _("At the Bus Stop")
    ################################
    
    pause 3    
    play music cicada01 fadein 5
    $ renpy.music.set_volume(0.4, 0.0, channel = "music")
    scene bstop with Dissolve(2)

    fn "「Just as I thought, \n\ \ it feels so much better than the city. 」"
    "The fresh air here is delicious.{p}I've completely become a city person."
    fn "「Now then, the house should be around here.{p}\ \ {nw}"
    play sound rustle1
    extend "...Hm? 」"

    "What? The bushes over there are rustling..."

    show to 002 big at center_big with explosion
    
    play sound bosu35

    who "{size=+15}「GUWAAAAAOOOOOooooo! 」"

    play sound bosu31

    fn "{size=+15}「Uhyaaaaa!? 」"

    show to 001 big with dis

    who "「Pff.... Bwahahahaha!{p}\ \ What're you falling over for,\n\ \ your luggage is flying everywhere. 」"
    who "「Here, I'll pick it up. 」"
    fn "「To... Torahiko?{p}\ \ Are you Torahiko? 」"

    $ encounter_torahiko = True
    
    hide to
    show to 007 at center
    with dis
    play music free0258 
    $ renpy.music.set_volume(0.6, 0.0, channel = "music")

    to "「What?{p}\ \ Have you completely forgotten about me? 」"
    fn "「But back then you were so small,\n\ \ I was taller than you... 」"

    show to 001 with dis

    to "「Ah, I started growing after junior high.{p}\ \ I've grown a lot up to now. 」"
    "He has completely outgrown me.{p}I'm a little bothered by this."

    show to 002
    show tora_ray
    with dis

    to "「I heard you were coming today,\n\ \ so I waited here."
    to "You were taking so long.{p}I decided to surprise you. 」"
    fn "「You waited all that time just for me? 」"

    hide tora_ray
    show to 010
    with dis

    to "「I wouldn't put it like that.{p}\ \ The only way to get here is by bus."
    to "Morning, noon, and night,\nthey're the only 3 times it comes here.{p}I'm glad your bus came on time today. 」"
    "He's the same as ever.{p}Always energetic."

    show to 001 with dis

    to "「Anyway... 」"
    fn "「Anyway? 」"
    
    play sound bosu29
    show to 002 big with circle_out    

    to "「It's been so long,\n\ \ get over here, ya bastard!! 」"
    fn "「Wa-wait, Torahiko!\n\ \ You're heavy, it hurts... 」"
    "Torahiko gives me a firm hug,\nwith his furry striped arms.{p}Back then, he'd have to jump up to hug me."
    "In those days he was so small and cute,\nnow there's this large,\nstrong Torahiko hugging me..."
    "I...{p}This really hurts!{p}I'm gonna die..."

    hide to big2
    show to 001 at center
    with dis

    fn "「Bwuaa, hah hah...{p}\ \ Torahiko, go easy on me.{p}\ \ Things are a little different since I left. 」"

    show to 002 with dis

    to "「Sorry, I'm just glad to see you.{p}\ \ Besides that...{p}\ \ Everybody's talking about you coming back. 」"
    to "「We're having the welcoming party at Raimon,\n\ \ {nw}"
    show to at jump_up
    extend "we had to have one. 」"

    to "「You need to get over there\n\ \ and start talking to everybody.{p}\ \ This is for all the trouble we went through! 」"
    "While saying that, he put me in a headlock,\nand started rubbing his fist into my head."
    fn "「Owowow, wait, stop...{p}\ \ You sent me that letter, didn't you? 」"

    show to 001 with dis

    to "「You came back faster than I thought...{p}\ \ but I'm glad.{p}\ \ Well then, coming to the welcoming party? 」"
    fn "「There's really a welcoming party!?{p}\ \ Sounds great, but... 」"
    fn "「I need to say hello to my grandparents,\n\ \ and put my stuff away. 」"

    show to 002
    show tora_ray
    with dis

    to "「All right, understood.{p}\ \ I'll be there.{p}\ \ I'm not the kind of person who'll be late. 」"
    fn "「Right, Raimon. I should probably be okay.{p}\ \ Oh, I almost forgot.{p}\ \ Give me your cell phone number and e-mail. 」"

    hide tora_ray
    show to 007 at center
    with dis

    to "「Ah, I don't have a cell phone. 」"
    fn "「Then do you know somebody who has one? 」"

    show to 001 with dis

    to "「...Nobody has one.{p}\ \ I think the village is out of range. 」"
    fn "「What!? 」"
    "I take out my cell phone and check.{p}The antenna has disappeared,\nand it's indicating I'm outside range."

    show to 002 with dis

    to "「We're so far out here that most of\n\ \ the villagers don't even have them.{p}\ \ Even if we wanted to use them, we couldn't. 」"
    "I know this is a pretty rural area,\nbut you can't even use a cell phone...?"

    show to 001 with dis

    to "「Just give it up.{p}\ \ Using it isn't a big deal anyway. 」"
    "I guess there's nothing I can do.{p}Not like I need to use my phone now."
    "So I'll go say hi,\nput away my luggage,\nthen go to Raimon."
    "A welcoming party, huh?{p}Wonder if everybody is going.{p}I'm really excited!"

    ###################################
    $ event_name = _("To Grandparents' Home")
    ###################################
    
    scene rice with wipeleft
    pause 1

    "Nothing has changed at all.{p}Farther up the dirt road, it becomes pavement...{p}Town looks just like it did back then."
    fn "「Is there anything that's changed since I left?{p}\ \ Have you done anything, or has anything happened? 」"

    show to 002 at center with wipeleft

    to "「Really... nothing much has happened.{p}\ \ You coming back is about the only thing. 」"
    fn "「Eh, nothing?{p}\ \ Not even something small? 」"

    show to 001 with dis

    to "「A few small things here and there.{p}\ \ They were all Kounosuke's fault.{p}\ \ They caused quite the uproar. 」"
    to "「There was a thing called\n\ \  \"the village revitalization project.\" 」"
    to "「The number of weird souvenirs increased,\n\ \ but there isn't anything considered big news. 」"
    "5 years have passed and nothing has changed...{p}More importantly, what did Kounosuke do?{p}Back then he was always causing trouble, but..."
    "About the number of souvenirs increasing.{p}I'm interested in that."

    show to 002 at jump_up

    to "「Oh, he'll be wanting to hear from you.{p}\ \ We'll talk plenty at the welcoming party.{p}\ \ Well, I gotta get going. Don't be late! 」"
    fn "「Yep, got it.{p}\ \ See you at the welcoming party. 」"

    hide to with wipeleft

    "Just like back then,\nwhen we were done playing,\nwe would say good-bye here."
    "Nothing has changed.{p}Just Torahiko's figure has grown."
    fn "「Well, I need to get going too. 」"

    #############################
    $ event_name = _("Homecoming")
    #############################
    
    scene black with sdis
    stop music fadeout 5
    pause 3
    play music cicada01 fadein 3
    $ renpy.music.set_volume(0.5, 0.0, channel = "music")
    scene hentry with wipe_dr
    pause .5    
    play sound door_slide

    fn "「Hello! 」"
    gm "「Hi. Come on in, [fn]-chan.{p}\ \ Please come in.{p}\ \ Dear! [fn]-chan has arrived! 」"
    fn "「Grandma, it's been so long.{p}\ \ Thanks for letting me stay. 」"
    gp "「[fn]?{p}\ \ I heard you were coming today,\n\ \ I didn't think it would be this soon. 」"
    gp "「You decided to visit so suddenly,\n\ \ wish you could've called earlier. 」"
    fn "「Long time no see, grandpa.{p}\ \ Sorry, it was on somewhat of a whim. 」"
    gp "「No no, there's no need to apologize.{p}\ \ No difference between here and your house!{p}\ \ So please, make yourself at home. 」"
    gm "「Here, I'll show you to your room.{p}\ \ It used to be your father's room. 」"
    fn "「Yep, it was right over there. 」"

    scene hbroom with wipeleft

    gm "「Here we are.{p}\ \ It's old and not very luxurious,\n\ \ but there is a TV and a fan. 」"
    gm "「The futon is in the closet\n\ \ you can spread it out yourself. 」"
    gm "「If you need to use the phone,\n\ \ it's by the front door. 」"
    fn "「Thank you very much. 」"
    fn "「I need to get going soon.{p}\ \ I just heard that my friends are\n\ \ throwing a welcoming party. 」"
    fn "「There's no need to make dinner for me.{p}\ \ I'll be leaving in just a bit. 」"
    gm "「I was going to make something nice for you...{p}\ \ But there's nothing that can be done about that. 」"

    scene black with Dissolve(1)
    scene hbroom with wipedown
    pause 1

    "Now then,\njust need to sort out my luggage a little,\nthen it's off to Raimon."
    "My cell phone is...{w=0.5} out of range.{p}Now it's useless. Nothing I can do.{p}I'll just put it away in my bag for now."
    "I set down my bag,\nand put my clothes in the dresser."
    "Whew, it's hot in here.{p}It's a small room,\nso the electric fan should help."

    play sound switch

    "{w=1}Huh? What? It's not working...{p}Probably because no one's used it in a while.{p}It looks old so there probably isn't a spare."
    "I'd ask my grandparents to trade,\nbut that would be rude..."
    "Heh, guess I'll have to deal with it.{p}Anyway, better get going to Raimon."

    #Insert Transition
    scene hentry with wipeleft

    fn "「I'm leaving, I'll be back soon! 」"
    gps "「Have a good time! 」"
    
    #####################################
    $ event_name = _("The Welcome Party Begins")
    #####################################

    scene black with Dissolve(2)
    scene market with wipe_corner
    play music free53
    $ renpy.music.set_volume(0.9, 0.0, channel = "music")

    fn "「Supposed to be somewhere around the mall...{p}\ \ Ah, red paper lanterns.{p}\ \ That's gotta be Raimon. 」"
    "Raimon is the only restaurant in town.{p}Originally it was just a bar."
    "Except for the desk part,\nthere's a lid sitting on the counter.{p}When you remove it there's an iron plate."
    "You can make okonomiyaki and yakiniku.{p}The menu isn't anything too special.{p}It has the stuff you'd expect from a cheap place."

    scene raimon1 with wipeleft

    om "「Come on in! 」"
    fn "「Hello. Umm... 」"
    "Wonder if everybody else is here already..."
    om "「I'm guessing you're...{p}\ \ the guest of honor. 」"
    fn "「Yeah? 」"
    om "「The one that's visiting your friends.{p}\ \ Today you're renting out the place.{p}\ \ 2 of 'em are already back there. 」"

    scene raimon2
    show si 001 at midright
    show ka 001 at midleft
    with wipeleft

    fn "「Oh, if it isn't Shin-kun and Kouya.{p}\ \ It's been a while, hasn't it? 」"

    show ka 003 with dis
    show ta 001 at offleft
    
    $ encounter_kouya = True

    ka "「Yo, long time no see! 」"
    "Kouya has become more adult-like.{p}He's getting more and more handsome too."
    
    $ encounter_shin = True 
    
    si "「...It's been a while.{p}\ \ Why haven't we gotten in touch sooner? 」"
    si "「You could have done it in your spare time,\n\ \ but I guess this is easier for you... 」"
    "S-Shin-kun's sharp tongue hasn't changed.{p}But that's Shin-kun for you,"
    "plainly stating what's on his mind,\nand not holding anything back."
    "Still, just \"it's been a while\"\nwould've been nicer..."
    om "「There something else you were going to say?{p}\ \ About how you were excited to see him? 」"
    om "「Already been here for 2 hours, haven't you?{p}\ \ You must have really been good friends. 」"
    fn "「... 」"
    si "「... 」"

    show ka 006 with dis
    show to 001 at offleft behind ka

    ka "「... 」"
    
    show ka 001 with dis
    show ka at move_center(0.5)
    show si 001 at move_farright(0.5)
    show to at move_farleft(0.5)
    
    to "「Hey everybody!{p}\ \ Oh, why are you guys so quiet?{p}\ \ [fn]'s back, be excited! 」"
    "I was looking forward to a proper greeting,\nbut knowing them,\nit's better that they're quiet..."
    fn "「You're unusually early, Torahiko. 」"

    show to 002 with dis

    to "「Of course, today is a special day. 」"
    fn "「But is renting out this place all right?{p}\ \ I don't have much on me... 」"

    show to 001 with dis

    to "「Don't worry about it,\n\ \ we collected enough for today."
    to "Making you pay would be rude.\nBesides, you shouldn't worry about money.{p}Right pops? 」"
    om "「Yep. When you heard he was coming back,\n\ \ you told everybody to pitch in, right? 」"
    om "「It wasn't a big deal for somebody like you.{p}\ \ This was the request from the carpenter's son.{p}\ \ There's no way I could refuse. 」"
    to "「Wait, no way!{p}\ \ But I talked to Tatsu-nii about this. 」"
    fn "「Is that so?{p}\ \ Sorry, I feel a little bad about this."
    fn "I came back so suddenly,\nand you go and do all this for me. 」"
    to "「Don't apologize, I'm glad to do this. 」"

    show ka 002 with dis

    ka "「That's right.{p}\ \ Nothing to apologize to Torahiko about. 」"

    show to 003 at jump_up

    to "「Whaddaya mean by that? 」"

    show ka 001 with dis

    ka "「I mean exactly what I said. 」"
    "What should I do,\nthe mood's starting to a get...{p}kind of negative..."

    scene raimon1
    show su 001 at center
    with wipeleft
    
    $ encounter_shun = True

    su "「Hello! Woof! It's [fn]-san!{p}\ \ It's been so long! 」"
    "This is Shun-kun, bursting in with a smile.{p}Talk about nice timing."
    fn "「Long time no see, Shun-kun.{p}\ \ So, have you been a good boy? 」"
    "While saying that,\nI ruffle his messy hair."

    show su tailwag 01 with dis

    su "「That's embarrassing!{p}\ \ Please, stop! 」"
    "Even though he's saying that,\nhe can't stop laughing and wagging his tail.{p}He's so adorable."

    show su 001 with dis

    su "「[fn]-san! [fn]-san!{p}\ \ Do you still play video games? 」"
    fn "「Yeah, every once in a while. 」"

    show su 002 with dis

    su "「Then...{p}\ \ would it be okay if we could play?{p}\ \ Just like back then? 」"
    fn "「Sure, sounds good! 」"
    "With those sparkling, innocent eyes,\nthere's no way I could refuse."
    "We had a good rivalry going on.{p}I was pretty tough."

    show su 002 at  jump_up
    show su tailwag 01

    su "「Yay, I'm so happy!{p}\ \ I play with the others, but...{p}\ \ they don't play video games as much as I do. 」"
    fn "「Doing nothing but playing video games,\n\ \ it isn't good.{p}\ \ You should get outside, too. 」"
    su "「Tatsuki-san and Kouya-san take me out!{p}\ \ I get to do stuff with them,\n\ \ so it's okay. 」"
    fn "「Oh, really? 」"
    "Tatsuki I can see doing that, but Kouya?{p}I know him and Shun-kun get along, but...{p}didn't think that they'd do something like that."

    scene raimon2
    show to ray 01 at center
    show ka 001 at farright
    with wipeleft

    to "「Shun looks up to Kouya-san,\n\ \ isn't that right Shun? 」"

    show ka 007 with dis

    ka "「Shut up... 」"

    show su 001 at farleft with wipeleft

    su "「Yeah, he's so cool!{p}\ \ I wanna be like him. 」"

    show ka 006 with dis

    ka "「Do you...{p}\ \ even know what you're saying...? 」"

    show su 002 with dis

    su "「'Course I do! 」"
    "Must be something between them I don't know.{p}Shun-kun does have a good point, though.{p}Maybe I'm putting too much thought into it."

    show to 010 with dis

    to "「Kouya is such a nice big brother!{p}\ \ Koouuyaa-oniiii-chaan! 」"
    "Torahiko's overdoing it..."

    scene raimon2
    show to ray 01 at center
    with wipeleft

    to "「Kouya-nii-{nw}"
    show to 008 at hit_right
    play sound hit_p00
    extend "guh! 」"

    "With a merciless sharp thrust,\na large arm drills right into Torahiko,\nknocking him flat on to the ground."

    scene raimon2
    show to 008 at midright
    show ju 001 at midleft
    with wipeleft
    
    $ encounter_juuichi = True

    ju "「You are being impolite, Tora. 」"
    "That rugged mood, that large, round body,\nit's none other than Juuichi-san.{p}Since when did he get here?"
    "Besides that,\nwhat was with the attack on Torahiko?{p}I wonder if he'll be all right..."

    scene raimon1
    show ju 001 at farright
    show ky 001 at center
    show so 001 at farleft
    with wipe_right
    
    $ encounter_kyouji = True

    ky "「Oh, [fn]! How have you been doing?{p}\ \ I was wondering if you were coming today. 」"
    fn "「Long time no see,\n\ \ Juuichi-san and Kyouji-senpai.{p}\ \ I'm doing fine. 」"
    ju "「Looks like you are doing well.{p}\ \ I had a club meeting today,\n\ \ but I was able to make it on time. 」"
    "Juuichi's still doing judo, huh?{p}He looks even bigger than before."
    ky "「I was afraid us three would be late.{p}\ \ Oh, that's right,\n\ \ there's somebody I need to introduce you to. 」"
    ky "「Meet my junior in the soccer club,\n\ \ and fellow classmate, Soutarou. 」"
    
    $ encounter_soutarou = True

    show so 006 with dis

    so "「I'm a first year student at the high school,\n\ \ Soutarou Touno. How d'ya do? 」"
    so "「I heard all about you from Takahara-senpai,\n\ \ pleased to meetcha! 」"
    fn "「I'm [fn] [ln].{p}\ \ Nice to meet you, Soutarou-kun. 」"
    "Kyouji-senpai is still playing soccer,\nhe even has a junior now."
    "He was popular with the girls,\nand was always very helpful.{p}I'm certain he had many admirers."
    "And Soutarou-kun,\nit's always nice to see a new face.{p}He looks very athletic."
    ky "「I was talking to Tarou about today.{p}\ \ He said he wanted to come along.{p}\ \ Told him about you and everybody else. 」"

    show so 003 with dis

    so "「I've heard a lot about you. 」"
    "Wonder exactly what he's been told..."

    scene raimon1
    show ta 001 at center
    show to 002 at offright
    with wipe_right
    
    $ encounter_tatsuki = True

    show ta 002 with dis

    ta "「Yooo! Oh, [fn]!{p}\ \ I've missed you so much!{p}\ \ Look at you! Your height hasn't changed."
    ta "Are you sure you're eating right?{p}Gahahahaha!! 」"
    "This huge guy is Tatsu-nii."
    fn "「You're looking good, Tatsu-nii.{p}\ \ Even thought it might not look like it,\n\ \ I have grown. 」"

    show ta 002 at move_midleft(0.5)
    show to 002 at move_midright(0.5)

    to "「Tatsu-nii, you're slow.{p}\ \ I was gettin' tired of waiting. 」"

    show ta 001 with dis

    ta "「My bad.{p}\ \ I tried to get here as soon as possible,\n\ \ but I just couldn't get away from work. 」"
    fn "「Oh, you have a job? 」"

    show ta 002 with dis

    ta "「Yep, after graduating high school,\n\ \ I've become an apprentice at home. 」"
    ta "「I could've done it after junior high,\n\ \ but I wanted to finish high school. 」"
    "So Tatsuki is already working.{p}He's always wanted to be a craftsman,\neven as a kid."
    fn "「Wow, you're an apprentice carpenter now.{p}\ \ By the way, have you not gotten any taller? 」"
    "By his 6th year of school,\nhe was already as tall as an adult."
    "I thought he would be bigger than this...{p}still, I can't see his face unless I look up."

    show ta 001 with dis

    ta "「Really? I've passed 2 meters,\n\ \ but you're so small.{p}\ \ {nw}"
    show ta 004 with dis
    extend "Eat lots and lots, don't be too picky! 」"

    show ta 001 with dis

    ta "「Fill up on meat today.{p}\ \ I actually prefer veggies and fish.{p}\ \ {nw}"
    show ta 002 at jump_up
    extend "Gahahaha! 」"

    "That's surprisingly healthy..."
    fn "「But I really have grown.{p}\ \ I've got some muscle from doing physical labor.{p}\ \ Though my stomach has... 」"

    show ta 009 at jump_up
    
    ta "「It's different for me.{p}\ \ When dragons become adults,\n\ \ our bellies start to show."
    
    show ta 007 with dis
    
    ta "I'm not that fat, I swear! 」"

    show to 001 with dis
    to "「Tatsu-nii's such a glutton.{p}\ \ Besides, you can get fat any age.{p}\ \ {nw}"
    show to 002 with dis
    extend "[fn], feel his belly! Poke poke! 」"

    "Poke poke. Huh."

    show ta 009 at jump_up

    ta "「Stop pokin' me.{p}\ \ {nw}"
    show ta 001 with dis
    extend "Anyway, is everyone here?{p}\ \ He isn't here yet, is he? 」"

    show to 006 with dis

    to "「Nope, of course he's going to be late today. 」"

    show raimon2
    show su 001 at center
    show si 001 at farright
    show ky 001 at farleft
    show so 003 at midleft
    with wipeleft

    ky "「I wasn't expecting him to come early. 」"
    si "「He was told when we were meeting,\n\ \ but it's already been 30 minutes. 」"

    show su 004 with dis

    su "「I was looking forward to seeing him... 」"

    show so 005 with dis

    so "「I heard he just likes talkin' about the city. 」"
    "This doesn't sound good..."

    scene raimon2
    show ka 001 at midright
    show ju 001 at midleft
    with wipe_right

    ka "「Half an hour late isn't too bad for him.{p}\ \ The other day, he showed up...{p}\ \ right as we were all saying good-bye. 」"
    ju "「He shouldn't have forgotten about this.{p}\ \ Probably... 」"

    scene raimon1
    show ko 001 at offleft_far
    with wipe_right
    show ko 001 at move_center(0.5)
    
    $ encounter_kounosuke = True

    ko "「Helloo!{p}\ \ Everyone got here early, didn't they?{p}\ \ {nw}"
    show ko 003 with dis
    extend "Oh, [fn], is that you?"
    show ko 002 with dis
    ko "「Long time no see! 」"

    show to 006 behind ko at farright with wipe_right
    
    to "「We've already been here a while, Kounosuke... 」"

    show ko 003 with dis
    
    ko "「But I got here just on time!{p}\ \ Everybody's here now, so...{p}\ \ I'd say that's a good time to show up. 」"

    scene raimon2
    show ju 003 at midright
    show ka 005 at farleft
    show si 001 at farright
    show so 005 at center
    show su 004 at midleft
    with wipe_right

    "Huh, you don't say..."

    scene raimon1
    show ta 001 at midleft
    show ko 001 at midright
    with wipe_right

    ta "「Well...{p}\ \ All that matters is that you tried. 」"

    show ko 004 with dis
    ko "「Uh huh.{p}\ \ {nw}"
    show ko 003 at jump_up
    extend "But more importantly, [fn]!! 」"
    
    ko "「What's it like living in the city?{p}\ \ I'm so jealous, you city-dweller! 」"
    ko "「Could I come and visit sometime? 」"

    show ko 001 with dis

    ko "「Course, you'd have to give me a tour.{p}\ \ Anything new going on there?{p}\ \ Anything weird happen? 」"

    show ko 004 with dis

    ko "「I wanna hear all about it! 」"
    fn "「Err, wait a minute. 」"

    show ta 006 with dis

    ta "「Calm down, Kounosuke.{p}\ \ I know you're excited,\n\ \ but you're being kinda obnoxious. 」"

    show ta 001 with dis

    ta "「[fn] just got here.{p}\ \ Give him some time to relax today. 」"

    show ko 001 with dis

    ko "「Oh, all right. Sorry.{p}\ \ {nw}"
    show ko 002 with dis
    extend "But you have to tell me about it sometime! 」"
    
    fn "「Yeah, I will. 」"
    "Kounosuke's still living at his own pace.{p}Looks like it's getting worse, too..."
    "I don't hate talking to him...{p}But if he wants to hear about the city,\nhe'll have to buy me a souvenir!"

    scene raimon2
    show ky 001 at center
    show so 001 at midright
    with wipe_right

    ky "「Now that everybody is here,\n\ \ we should get started soon. 」"

    show so 003 with dis

    so "「Finally! 」"
    ky "「Tarou, don't tell me you just came for the food... 」"

    show so 006 with dis

    so "「Ehh, that's not what I meant! 」"

    show to 002 at farleft with wipe_right

    to "「You two are like a married couple,\n\ \ from a sitcom. Let's just sit now. 」"
    ky "「We do seem like a husband and wife,\n\ \ don't we Tarou? 」"

    show so 004 at jump_up

    so "「Husband and wife?! 」"

    show ju 003 at farright with wipe_right

    ju "「Touno, don't take him too seriously... 」"

    scene raimon1
    show ta 001 at center
    with wipeleft

    ta "「Come on, let's get started.{p}\ \ Let's get some service here, pops!{p}\ \ I want non-stop meat and drinks! 」"
    om "「You're the Midoriya's son,\n\ \ of course you want drinks.{p}\ \ That's almost all you guys ever ask for. 」"

    show ta 002 with dis

    ta "「I know, I know.{p}\ \ Now give it to me,\n\ \ straight from the barrel! 」"

    show si 001 behind ta at farright with wipe_right

    si "「It doesn't concern me, but...{p}\ \ I don't think minors are allowed to drink... 」"

    show ka 002 behind ta at farleft with wipe_right

    ka "「It'd be better if we didn't drink.{p}\ \ Even if we did, Tatsuki would down most of it. 」"
    fn "「Will Tatsu-nii be allowed to drink? 」"

    scene raimon2
    show su 002 at midright
    with wipe_right

    su "「Tatsu-nii sure drinks a lot of sake! 」"

    show ky 001 behind su with wipe_right

    ky "「Oh, it's no problem.{p}\ \ Dragons have a higher alcohol tolerance,\n\ \ so the law's a little different for them."
    ky "It'll be all right if Tatsuki-san drinks. 」"

    show ko 004 at farleft with wipe_right

    ko "「But it already looks...{p}\ \ as if he's been drinking for a while. 」"

    scene raimon1
    show ta 001 at midright
    show to 001 at midleft
    with wipe_right
    show ta 004 with dis

    ta "「Wh-what, can't a man drink in peace?{p}\ \ C'mon, sit down already! 」"

    show to 002 with dis

    to "「Hey, [fn]!{p}\ \ Sit over here! 」"

    scene raimon2
    show ka 005 at midright
    with wipe_right

    ka "「It's not like he has to sit with you. 」"
    fn "「Wait, I have to go to the bathroom... 」"

    show ko 002 at midleft with wipe_right

    ko "「Ahaha! Nice save, [fn]! 」"

    show to 007 behind ko at farleft with wipe_right

    to "「What's that? 」"

    scene raimon2
    show ju 001 at midright
    show su 001 at midleft
    with wipe_right

    ju "「Fine then, I'll just sit next to Tora. 」"

    show su 002 with dis

    su "「Ahaha!\n\ \ At least someone's next to Torahiko-san! 」"
    to "「Uhh, no thank you! 」"
    fn "「Excuse me, I'll be back in a bit... 」"

    scene raimon1
    show si 002 at center
    with wipe_right

    si "「Fufu.{p}\ \ Weren't you ever taught to go\n\ \ before you went out somewhere? 」"
    fn "「Move it, Shin-kun. 」"
    "Wow, I'm getting kinda stressed.{p}I've only been here a few hours,\nbut it feels like I've been here all day."
    "And when I get back,\nthe party's going to begin.{p}It's hectic, but I miss this atmosphere."
    "Wasn't every day back then like this?{p}My memories are so vague,\nthey might not be too accurate, I guess."
    "Oh boy.{p}This is going to be a busy Summer..."
    "......"
    
    ################################
    $ event_name = _("Who to sit beside?")
    ################################

    scene black with Dissolve(2)
    scene raimon2 with circle_out
    play music free53 fadein 1.5

    fn "「I feel better.{p}\ \ Now I'm ready... oh. 」"
    "Everyone's already taken seats.{p}I wonder who has an empty spot."
    
    menu:
        "A. Next to Tatsu-nii?":
            jump sit_with_tatsuki
        "B. How about with Kouya?":
            jump sit_with_kouya
        "C. Ah, spot next to Shin-kun.":
            jump sit_with_shin
        "D. Space next to Kounosuke.":
            jump sit_with_kounosuke
        "E. Between Kyouji and Soutarou...":
            jump sit_with_kyoutarou
        "F. Too cramped next to Juuichi?":
            jump sit_with_juuichi
        "G. Probably room next to Shun-kun.":
            jump sit_with_shun
        "H. I feel Torahiko looking at me.":
            jump sit_with_torahiko

    ##########################################
    label sit_with_tatsuki:
        $ event_name = "Together With Tatsu-nii"
        $ love_tatsuki += 1
        
        scene raimon1 with wipeleft
        show ta 002 at center with wipeleft

        ta "「Hey hey, get over here.{p}\ \ I got a seat for ya! 」"

        show ta 002 at farleft
        show to 001 at farright
        with wipe_right

        to "「Don't take seats like that,\n\ \ [fn] can sit wherever he wants. 」"

        show ta 007 with dis

        ta "「It just happened to be open by chance.{p}\ \ [fn], hurry up and sit,\n\ \ across from Torahiko! 」"
        fn "「All right.\n\ \ I guess that looks like a good seat. 」"
        "He sure is being pushy..."
        "I was already going to sit next to him,\nbut I'll just follow his directions."
        "He's clearly happy.{p}It's written all over his face."

        scene raimon2
        show ky 001 at center
        with wipe_right

        ky "「There, now everybody has a seat. 」"
        "At the table there are dishes full of meat.{p}When I was in the bathroom,\nthey must've been brought out."

        show to 002 at farleft with wipe_right

        to "「Do you have something to drink? 」"

        scene raimon1
        show ta 001 at center
        with wipe_right

        ta "「Hey, you should try the oolong tea. 」"
        fn "「Okay, thanks. 」"

        scene raimon2
        show to 002 at center
        with wipe_right

        to "「Well then...{p}\ \ Let's start the party! 」"
        to "「Cheeeers!! 」"

        scene raimon2
        show ky 001 at midleft
        show ko 002 at farright
        show ka 001 at farleft
        show so 001 at center
        show su 002 at midright
        with wipe_right

        "{size=+15}「Cheeeers!! 」"

        scene raimon2
        show to 001 at center
        with wipe_right

        to "「All right, I'm gonna eat and eat some more! 」"

        show ky 001 at farright behind to with wipe_right

        ky "「If there's anything else you want,\n\ \ don't be afraid to ask for it. 」"

        scene raimon1
        show ta 002 at center
        with wipe_right

        ta "「Bring me seconds! 」"
        fn "「Didn't you just get a drink? 」"
        ta "「That wasn't enough.{p}\ \ Do you want some? 」"
        fn "「No, I'm fine with what I've got. 」"

        show ta at jump_up

        ta "「Gahaha! There's no need to hold back!{p}\ \ ...*urp* gimme more, Pops! 」"
        "As he shouts that,\nTatsu-nii thrusts his empty, extra-large,\nmade-for-beastmen mug into the air."
        "He is such a heavy drinker."

        scene raimon2
        show to 001 at farright
        show si 001 at farleft
        show ju 001 at center
        show su 002 at midleft
        with wipeleft

        ju "「Hmm, what should I start with... 」"
        si "「... 」"

        show to ray 01 at jump_up

        to "「It's arranged in such a flimsy way,\n\ \ I'm not sure what to do... 」"
        to "「I'll just go with a plate of ribs for now. 」"

        show su 003 at jump_up

        su "「Amazing...{p}\ \ I can't see the plate under all this meat! 」"

        hide ju
        show ju 006 at center
        show ju at briefzoom

        ju "「TORAAAAA!!! 」"

        scene raimon1 with wipeleft
        pause .2

        "Sounds like something's happening over there..."

        show ta 001 at center with dis

        ta "「So [fn], what's the city like? 」"
        fn "「Umm, there's a lot of buildings and people...{p}\ \ but it's not too different from here. 」"

        show ta 002 with dis

        ta "「Gahaha, what are you talking about?\n\ \ I think it'd be a really weird place. 」"
        ta "「Hey pops!{p}\ \ A pitcher of shochu on the rocks over here! 」"
        om "「Coming up! 」"
        fn "「Well, it can be a strange place,\n\ \ but no matter where I live it's the same.{p}\ \ Besides, you can be pretty weird, too. 」"
        ta "「Really? 」"
        "Even though he's sitting,\nTatsu-nii is still huge."
        "Just by being next to him,\nI could be completely hidden."
        "He's become even more muscular.{p}His chest is big and his arms are like logs."
        "His body looks sturdy like a tree trunk,\nand looks quite strong too."
        fn "「Yeah, you look like an adult.{p}\ \ I didn't think you could get any taller.{p}\ \ Now it looks like you've grown over 2 meters! 」"

        show ta 001 with dis

        ta "「Yeah, it happened in high school.{p}\ \ I'm over 100kg now, too!{p}\ \ Pops, next up is the sake. Gimme the bottle! 」"
        fn "「You're huge.{p}\ \ Not only has your body gotten stronger,\n\ \ your horns have grown out nicely, too. 」"

        show ta 007 with dis

        ta "「Oh, I'm just getting stronger from my job.{p}\ \ {nw}"
        show ta at jump_up
        extend "I know!{p}\ \ You should come over to my house sometime! 」"

        show ta 001 with dis

        ta "「I work during the day,\n\ \ but we're usually done around 5.{p}\ \ whenever you wanna come is fine. 」"
        ta "「If you want,\n\ \ I can give you a tour while I'm working. 」"
        fn "「Ehh, that would be nice,\n\ \ but I don't want to be a nuisance.{p}\ \ Your dad can be... scary. 」"

        show ta 002 at jump_up

        ta "「Gahahaha! Why?{p}\ \ There's nothing to worry about.{p}\ \ During my break would be a good time. 」"
        ta "「But like I said,\n\ \ any time you want will be fine! 」"
        fn "「All right then, I'll drop in sometime.{p}\ \ So, your job has you working out, huh? 」"

        show ta 001 with dis

        ta "「Oh, you wanna touch them? 」"
        "Tatsuki flexes his huge biceps,\nand shows them off for me."
        om "「Hold on a sec!!{p}\ \ Here's your sake.{p}\ \ It's \"Beast Man Mountain\" brand. 」"
        fn "「Ehh, is this all right?{p}\ \ Wow, it's as hard as a rock. 」"

        show ta 002 with dis

        ta "「But look at you!{p}\ \ You're all skin and bones, aren't you? 」"
        "When he said that, Tatsu-nii grabbed me,\nand felt me to make sure."
        fn "「H-Hey, what's with you?{p}\ \ You're not usually like this! 」"

        show ta 001 with dis

        ta "「Nah, you just need some training.{p}\ \ {nw}"
        show ta 002
        extend "See, my pecs are amazing.{p}\ \ Go on, touch 'em. 」"
        fn "「Amazing, they swell out so much,\n\ \ and they're smoother than I thought. 」"
        "With his chest exposed,\nI touch him with my hand,\nmy heart pounding."
        "Tatsu-nii's skin... I mean, scales,\nare so smooth.{p}Touching them feels nice."
        ta "「Mom buys this soap for scale treatment,\n\ \ but dad and I use it too. 」"

        show ta 001 with dis

        ta "「There's also this nighttime gel and oil.{p}\ \ But it looks sticky when it's on.{p}\ \ {nw}"
        show ta 002 with dis
        extend "...Pops! One more! 」"
        
        "I guess dragons can be\nreally particular about their scale-care."

        show ta 001 with dis

        ta "「What's your skin like, [fn]?{p}\ \ {nw}"
        show ta 002 with dis
        extend "Oh, it's smooth isn't it? 」"

        play music free0421 fadeout 3

        "Without any hesitation,\nTatsu-nii slips his hands under my shirt.{p}He begins to feel up my body."
        fn "「T-Tatsu-nii! This is embarrassing...! 」"

        show ta 302 with dis

        ta "「My belly feels good, too... 」"
        "He grabs my hand,\nbrings it down to his belly,\nand starts making me feel it."
        "Tatsu-nii's belly does feel pretty good..."
        fn "「Woah, your stomach's gotten bigger... 」"

        show ta at jump_up

        ta "「It's not that big.{p}\ \ Now, keep going lower..."
        "While grinning and laughing,\nTatsu-nii grabs my hands,\nthrusting them into his pants"
        fn "「T-Tatsu-nii!! Not down there!{p}\ \ I hit something kind of warm!{p}\ \ Wh-what are you doing?!"

        show ta 301 with dis

        ta "「Well, now...{p}\ \ it's getting bigger.{p}\ \ Try touching it... 」"
        "His gigantic hands draw closer,\nand closer to his pants."
        "If I let him do this,\nI'll end up groping his crotch!"
        "Tatsu-nii is way too strong,\nit's only a matter of time...{p}before my guard breaks!"

        fn "「Stooooop!!{p}\ \ Don't make me touch it!{p}\ \ That's... 」"

        scene raimon2
        show ko 005 at center
        with wipe_right
        
        ko "「Oh, Tatsu-nii's at it again... 」"

        show ka 005 at farright with wipe_right

        ka "「Jeez. He's even doing it here,\n\ \ out in the open. 」"

        show to 002 at farleft behind ko with wipe_right

        to "「Oh yeah, [fn] doesn't know.{p}\ \ This is what happens when he gets drunk.{p}\ \ He'll sexually harass you without thinking. 」"

        scene raimon2
        show ju 001 at center
        with wipe_right

        ju "「...And this is exactly what's happening. 」"

        show ky 001 at farright behind ju with wipe_right

        ky "「It's just like that one time,\n\ \ isn't it Tarou? 」"

        show so 006 at midright with wipe_right

        so "「Oh yeah, that...{p}\ \ It was awful! 」"
        so "「Midoriya-senpai made me strip down,\n\ \ in front of everyone, too!{p}\ \ It was so embarrassing... 」"

        scene raimon1 with wipe_right

        "They could have said something earlier...{p}I mean, everybody knows about this."
        "Why didn't they tell me first?{p}No wonder nobody sat near us..."

        show ta 302 big at center_big with wipe_right

        ta "「Hey, if you want it,\n\ \ don't hold back...{p}\ \ you can tie me up if you'd like... 」"

        play music free44
        show ka 001 at farright behind ta with wipe_right

        #Accelerate music

        ka "「Old man, get the rope. 」"
        om "「Here, use this! 」"

        show to 001 at farleft behind ta with wipe_right

        to "「Tatsu-nii, put both hands behind you. 」"

        show ta 303 big 
        show ta at jump_up_big
        pause .1
        show ta 303 big at center_big
        #show ta at center_big
        #pause .184
        #show ta 303 big at center

        ta "「Whaaaaat...? 」"

        show to 002 with dis

        to "「I'll get you tied up real nice... 」"
        ta "「Oof, I see. 」"
        to "「Let's tie up that loud mouth of yours. 」"
        
        hide ta
        show ta 003 at center
        with dis

        ta "「Mmph! Mmm! 」"

        show to 009 at move_midleft(0.5) with qdis

        to "「We don't want him to run off.{p}\ \ I'll tie his legs together. 」"
        to "「We don't want his tail thrashing, either.{p}\ \ I'll get it! 」"
        "From the way Torahiko tied him up,\nall Tatsu-nii can do is wiggle around."
        "That rope won't be coming off right now."

        show to 001
        show ta 103
        with dis

        to "「There, that's good. 」"
        "Wait, what? Why is he naked?"

        hide ka
        show ju 001 at farright behind ta 
        with wipeleft

        ju "「I'll take it from here. 」"
        "Juuichi-san winds the rope around Tatsu-nii.{p}He puts him inside a bag,\nand carries him outside over his shoulder."

        scene raimon2
        show ko 001 at center
        with wipe_right

        fn "「Err... will he be okay? 」"

        show ko 004 with dis

        ko "「Don't worry, happens all the time. 」"

        show ka 002 at farleft behind ko with wipeleft

        ka "「Give him 10 minutes and the alcohol will pass.{p}\ \ The party must go on. 」"

        show to 002 behind ko at midleft with wipeleft

        to "「He's a bit of an alcoholic.{p}\ \ Also, when he's driving,\n\ \ be careful when you're riding with him. 」"
        "I'll keep that in mind..."
        "Wait. Isn't Tatsu-nii the oldest of us?"

        show ky 001 at farright with wipe_right

        ky "「Come on, we're in the middle of a meal.{p}\ \ You should eat something, too. 」"

        show ka 003 with dis

        ka "「Old man, no more alcohol without asking, okay? 」"
        om "「I hear ya! 」"
        "This happens all the time?\nEveryone was so nonchalant about it..."

        scene raimon2
        show to ray 01 at center
        with wipeleft

        to "「Hey, [fn]. You gonna eat that?{p}\ \ Or can I have it? 」"
        fn "「Hold on, I'm eating, I'm eating. 」"
        "Mmm, it's good.\nI'll just eat more meat."

        scene black with wipedown
        #stop music fadeout 4
        #pause 5

        jump party_end
        
    #########################################
    label sit_with_kouya:
        $ event_name = _("Next to Kouya")
        $ love_kouya += 1
        
        show ka 002 at center with wipe_right
        
        "When I look around,\nI see an open spot next to Kouya."
        "I wanted to talk to him,\nso I'll sit there."
        fn "「Is it all right if I sit here? 」"

        show ka 003 with dis
        
        ka "「Oh, go ahead. 」"
        fn "「Thanks. Excuse me... 」"
        "I lower my waist to sit down,\nwhile I'm doing that however,\nI can hear Torahiko's voice."

        scene raimon2
        show ka 003 at midleft
        show to 003 at farright
        with wipe_right

        to "「[fn], what are you doing?{p}\ \ Next to Kouya? 」"
        fn "「Huh? Do you have a problem? 」"
        
        show to 007 with dis

        to "「No... nothing in particular... 」"

        show ka 009 with dis

        ka "「What, are you jealous? 」"
        "Kouya mocks him with a faint sneer.{p}Torahiko struggles to find his words,\nand his face turns a little red."

        show to 013 at jump_up

        to "「Oh...{p}\ \ i-it's not like that! 」"

        show ju 001 at midright behind ka with dis

        ju "「What are you so upset about, Tora?{p}\ \ Next to me is fine. 」"
        "As he says that,\nhe puts his hands on Torahiko's shoulders."
        "...Oh, that's why Torahiko said that.{p}He invited me to sit with him first.{p}Did I do something wrong?"

        show to 006 with dis

        to "「Nah... it's never fun sitting with you,\n\ \ Juuichi-sanowowowowowow!! 」"
        to "「It just slipped outKAAAAAA!!{p}\ \ {nw}"
        show to 011 with dis
        extend "Wait, I give up! Sorry! 」"

        show ka 005 with dis

        "Torahiko's pained cries echo,\nlooks like Juuichi-san is tightening his grip."
        "His seat is a short distance away,\nbut I can see those fingers digging into him.{p}I can almost hear it..."
        "Juuichi-san did say he was still doing judo,\nthat must be where his grip is from.{p}All I can hear is Torahiko screaming..."
        "Ouch... watching is making me sore..."

        show ju 006 with dis

        ju "「Don't know why you need to sit next to [fn],\n\ \ but don't say such heartless things.{p}\ \ {nw}"
        show ju 001 with dis
        extend "Now do you have a problem with me? 」"

        show to at jump_up

        to "「No, n-not at all!\n\ \ I-in fact, I should be really thankful, r-right?! 」"
        ju "「Good. 」"

        scene raimon2 with wipeleft

        "Finally, Juuichi-san releases Torahiko."

        show to 006 at center with wipe_right

        to "「I-I thought my collarbone was gonna... 」"
        "Torahiko mumbles as he rubs his shoulders.{p}His face has gone from red to pale."
        "What should I say...{p}sorry Torahiko."

        scene raimon1
        show ta 001 at center
        with wipeleft

        ta "「Hey, playin' around is fine, but control it!{p}\ \ Let's start, [fn]'s returned!{p}\ \ {nw}"
        show ta 002 at jump_up
        extend "Pops! I wanna order something! 」"
        om "「Yeah, whaddya want?! 」"

        hide ta with wipeleft

        "At the sound of Tatsu-nii's voice,\nthings got moving along."
        "The old man comes out,\nand begins to take our orders.{p}I just ask for some oolong tea."
        "I think it'd take a while for things to come,\nbut because we rented out the place,\nour drinks were brought to us immediately."
        "The food, that is to say, the yakiniku,\nhas already been prepared.{p}It was brought out with the drinks."
        "And with that,\nthe preparations are complete.\nTorahiko stands to check things out."
        "Because his shoulders are still sore,\nhe gives a small grimace.{p}He seems to have recovered a bit."
        "It wasn't too serious,\nbut I'm still relieved."
        "He coughs once to clear his throat.\nThe noisy restaurant quiets down."
        "At last, it's beginning."

        show to 001 at center with wipeleft

        to "「All right then,\n\ \ did everyone get a drink? 」"
        "{size=+15}YEAH!"

        show to 002 with dis

        to "「Good, good.{p}\ \ Let's get this party started! 」"

        show to ray 01 with dis

        to "「After five years,\n\ \ let's pick up right where we left off.{p}\ \ Let's have fun, everybody! 」"

        scene raimon2
        show ta 002 at center
        with wipe_right

        ta "「Tora, stop talking already! 」"

        hide ta with wipe_right

        "{size=+15}「Hahahahaha! 」"
        "Tatsu-nii causes everybody to laugh.{p}Even Torahiko gives an embarrassed giggle."
        "I have to say, I missed this atmosphere."

        scene raimon1
        show to 001 at center
        with wipeleft

        to "「Shut up!{p}\ \ I don't have anything else to say.{p}\ \ Just get started already! 」"

        show to 003 with dis

        to "「Ahem, but first,\n\ \ I think it'd be nice to hear a greeting. 」"
        to "「A greeting from our honored guest,\n\ \ [fn]! 」"

        show to 002 with dis

        to "「So then, [fn].{p}\ \ I ask you to make the toast!{p}\ \ I'm leaving it to you! 」"
        fn "「Whaaaa?! 」"
        "I didn't see this coming.{p}Did I hear him correctly?!"
        "Still, everyone looks at me.{p}They turn in anticipation,\nexpecting me to say something."
        "Are...{p}Are they ganging up on me?"
        fn "「U-umm... well... 」"
        "I stand up in an attempt,\nto over come the pressure."
        "However, I suddenly struggle with my words.{p}We're all friends, but I'm still nervous."
        "Wh-what do I do?!{p}My face is turning white..."

        show ka 003 at farright behind to with wipeleft

        ka "「[fn], you can do it. 」"
        "I look to my side.{p}I can see Kouya calling out to me,\nsmiling gently."
        "Because of that,\nmy tension eases a little."

        scene raimon2 with wipeleft

        fn "Err... i-it's been a long time,\nb-but I have this to say,\nI'm glad to be back like t-this! 」"

        show to 002 at midleft with wipe_right

        to "「The hell, [fn]!{p}\ \ We're your friends! 」"

        show ta 002 at midright behind to with wipe_right

        ta "「Yeah, you're bein' too shy! 」"
        "Voices from everywhere rise up."
        "This is kind of embarrassing,\nbut more than that, I'm happy."

        show raimon1 with Dissolve(1)

        fn "「Thanks. I'm not very good at,\n\ \ err, saying these kinds of things,\n\ \ but thanks for everything guys! 」"
        fn "「Well then, to our reunion!{p}\ \ Cheers! 」"
        "{size=+15}CHEERS!"

        play sound glass

        "And with that,\nthe peaceful hustle and bustle returns."
        "There aren't any other customers,\nbut we're enough to keep it busy"
        fn "「Whew... 」"
        "The sounds of joyous laughter,\nthe sound of the roasting meat,\nhearing them makes my nervousness dissipate."
        "Getting tired from the crowd,\nI sit back down."

        scene raimon2
        show ka 003 at center
        with wipeleft

        ka "「Nice job.{p}\ \ That was quite the greeting. 」"
        "He still has the same smile from earlier.{p}I say thanks to Kouya."
        fn "「Oh, thanks. It was surprising.{p}\ \ I wasn't expecting Torahiko to...{p}\ \ put me on the spot like that. 」"
        fn "「It was weird, I got really nervous! 」"

        show ka 001 with dis

        ka "「You looked like you were frozen solid.{p}\ \ Well, you gotta expect the unexpected sometimes. 」"
        fn "「Eh, sorry about that.{p}\ \ My face was beginning to turn white.{p}\ \ Ah, but because of you, 」"
        fn "「I was able to get back on track.{p}\ \ Thanks, it would've been awful if I didn't. 」"

        show ka 003 with dis

        ka "「Well, thanks for the gratitude. 」"
        ka "「Anyway, it's been a while, [fn].{p}\ \ You seem to be doing well. 」"
        "While saying that,\nKouya gives me a light pat on the shoulder"
        fn "「You too.{p}\ \ Actually, everyone seems to be doing well. 」"

        show ka 005 with dis

        ka "「Heh, I think that's my line.{p}\ \ You never contacted us,\n\ \ weren't you ever concerned? 」"
        fn "「Oh yeah, sorry about that... 」"

        show ka 003 with dis

        ka "「Well, now you'll be able to see,\n\ \ just how good everyone is doing.{p}\ \ So [fn], you seem to have grown. 」"
        fn "「You think so?{p}\ \ Not too long after I moved,\n\ \ I started to get taller. 」"
        fn "「You have too, haven't you? 」"
        fn "「You're taller than me,\n\ \ and you seem even more mature...{p}\ \ you were always so cool. 」"

        show ka 002 with dis

        ka "「Thanks.{p}\ \ A little bit of flattery is never bad. 」"
        "He says that while giving me a smile. 」"
        fn "「Well, I didn't mean it like that... 」"
        "When he says thanks to me,\nI feel a bit embarrassed.{p}My face is turning red."
        "On the other hand, he's so nonchalant.{p}The more I think about it,\nthe more I feel stuck."
        "Aah, this is really embarrassing..."
        fn "「A-anyway, what have you been up to?{p}\ \ Like club activities, or something? 」"
        "I change the subject quickly,\nto conceal my humiliation."
        "Because I left after junior high,\nI've had no idea what everyone's up to.{p}So, I was a little interested."

        show ka 001 with dis

        ka "「Nope, I don't do clubs.{p}\ \ I'm in a band. 」"
        fn "「Oh, really?{p}\ \ What do you do? Vocals? 」"

        show ka 002 with dis

        ka "「No, I only do that occasionally.{p}\ \ I mainly play the guitar. 」"
        fn "「Wow, that's amazing!{p}\ \ I'm no good with music.{p}\ \ I have to confess, I'm jealous. 」"
        fn "「Even if I could play one instrument,\n\ \ I'd be satisfied. 」"
        ka "「Yeah, it is pretty nice.{p}\ \ {nw}"
        show ka 003 with dis
        extend "I know, you want lessons sometimes? 」"
       
        fn "「Eh, would that be all right? 」"
        ka "「Sure.{p}\ \ If you're interested, let's talk. 」"
        "With those words,\nKouya gives a smile."
        "It's as if he's confirming my determination,\nand saying \"what will you do?\""
        "Without any thought,\nI already know the answer."
        "I don't have any reason to refuse.{p}And more importantly, it sounds fun.{p}That's enough for me."
        fn "「Well, if I get the opportunity,\n\ \ I'll take you up on your offer. 」"
        fn "「If it's not too much trouble,\n\ \ I'd also like to hear you play sometime. 」"

        show ka 002 with dis

        ka "「Ah, I don't mind at all.{p}\ \ Actually, I'm going to be playing live,\n\ \ so you could come then if you want. 」"
        fn "「You're playing live?{p}\ \ That sounds like a big deal. 」"

        show ka 003 with dis

        ka "「I'm aiming for it to be my debut,\n\ \ so it is a pretty big deal. 」"
        ka "「I can get you a ticket if you want. 」"
        fn "「Yeah, I'd love to go!{p}\ \ I'm looking forward to it. 」"

        show ka 002 with dis

        ka "「I'll be expecting you then.{p}\ \ Well, enough about that.{p}\ \ Look, the meat is starting to burn around here. 」"
        "As he says that,\nhe serves me a plate of food."
        fn "「Oh, sorry Kouya, thanks! 」"

        show ka 003 with dis

        ka "「Eat all you want.{p}\ \ Today is your welcoming party after all,\n\ \ or are you going to hold back? 」"
        "Kouya's grin made me feel a little warm.{p}It was a nostalgic feeling that I had forgotten."
        fn "「Yeah!{p}\ \ Let's eat right away.{p}\ \ Thanks for the food. 」"
        "I pick up my chopsticks and begin."
        "It's been a long time since I've eaten here.\nThe taste was also a nostalgic feeling."

        jump party_end
        
    #################################################
    label sit_with_kyoutarou:
        $ event_name = _("Across from Kyouji-senpai and Soutarou-kun")
        $ love_soutarou += 1
        $ love_kyouji += 1

        show ky 001 at center with wipeleft

        ky "「Oh, [fn].{p}\ \ Are you looking for an empty seat? 」"
        "Kyouji stands up.{p}There's an empty seat across from him."
        fn "「Ah, thank you.{p}\ \ Err, Kyouji... Senpai. 」"
        ky "「Haha, you don't have to call me senpai.{p}\ \ It'd be better if we dropped the honorifics. 」"
        ky "「This is your long-awaited welcoming party.{p}\ \ It's not suitable for us to be so formal, right? 」"
        fn "「A-are you sure?{p}\ \ Well in that case...{p}\ \ Is here all right... Kyouji? 」"
        ky "「Ah, by all means, of course. 」"
        "His openhearted response makes me feel awkward,\nbut I cheerfully sit down anyway."

        scene raimon1
        show to 002 at midleft
        with wipe_right

        to "「Hey, [fn]!{p}\ \ Are you gonna order something? 」"
        fn "「What, order? 」"

        show su 002 at midright with wipe_right

        su "「Get your favorite drink,\n\ \ [fn]-san. 」"
        "Whoops, looks like I kept everyone waiting.{p}I take a peek at the menu and order some tea."

        scene raimon2 with wipeleft

        "Shortly after that,\ndishes of meat are carried out."

        show so 003 at midright with wipeleft

        so "「Whoa, that looks really good... 」"

        show ky 001 at midleft with wipeleft

        ky "「Tarou, doesn't it still need to be cooked? 」"

        show so 006 with dis

        so "「I-I know... 」"
        fn "「Ahaha! 」"
        "Those two have a good tempo when they talk,\nI can't help but laugh a little."
        "In these kinds of situations,\nthis must be how they usually act."

        scene raimon1 with wipe_right

        "Before long, everyone gets their drinks.{p}Torahiko raises his glass and begins to speak."

        show to 002 at center with wipe_right

        to "「All right, now we're ready,{p}\ \ ready to reunite with [fn]!{p}\ \ Cheers! 」"

        scene raimon2 with circle_out
        play sound glass

        "{size=+15}CHEERS!"
        "The sound of clinking glasses echo in unison."
        "After the toast is over,\nthe food is set out in front of us."
        "The delicious aroma of cooking meat,\nit spreads throughout the restaurant."

        show ky 001 at midleft
        show so 005 at midright
        with wipe_right

        so "「I'm already really hungry... 」"
        ky "「Haha, I am too.{p}\ \ It's because of all that exercise. 」"
        fn "「Oh, that's right.{p}\ \ You just got back from your club. 」"
        ky "「Yeah, we had a pretty close practice game.{p}\ \ We're still working on our formations. 」"
        fn "「Wow...{p}\ \ You're still serious about soccer. 」"
        ky "「Yep, I never tire of kicking that little ball.{p}\ \ I'm still playing soccer,\n\ \ just like when I was younger. 」"
        fn "「Yeah. Back in elementary school,\n\ \ especially after class. 」"
        ky "「After you moved, everybody changed a little.{p}\ \ For example, Ooshima is swimming,\n\ \ and Kouya's into music. 」"
        ky "「But then there's me.{p}\ \ I haven't changed one bit. 」"
        fn "「Th-that's not true!{p}\ \ You're way different. 」"
        "I take a good look at Kyouji."
        "First of all, there's his body.{p}Soccer has made his arms and legs stronger.{p}His shoulders have also gotten wider."
        "We haven't seen each other in five years.{p}It isn't strange that he's different..."
        "On the other hand,\nhis facial expressions and eyes haven't changed."
        "I can't tell if they're open,\nbut when I look into them,\nI'm filled with a calm feeling."
        "They are gentle eyes."
        fn "「...Of course you've changed.{p}\ \ I have a feeling that you're more mature now. 」"
        ky "「...Really? 」"
        fn "「Yeah, you're almost...{p}\ \ like a father... 」"

        show ky at jump_up

        ky "「Heheh, just be honest and say I'm old. 」"
        fn "「Haha, you got me! 」"

        hide ky
        hide so
        with dis

        ky "「...But to be honest,\n\ \ I'm really glad to hear that.{p}\ \ Thanks. 」"
        "Kyouji rubs his nose in embarrassment.{p}\"Dad\" and I cook our meat,\nand put it on our plates."
        "I start eating without hesitation.{p}...The taste of meat spreads onto my tongue."
        fn "「Mmm...{p}\ \ this is great! 」"
        ky "「Haha, it's the best!{p}\ \ Tarou, is everything all right for you? 」"

        show so 003 at midleft with wipeleft

        so "「Yeah!{p}\ \ After all, eating with company,\n\ \ always makes it better. 」"

        show ky 001 at midright with wipeleft

        ky "「That's right.{p}\ \ You're still growing,\n\ \ are you eating enough? 」"

        show so 006 with dis

        so "「Ehehehe,\n\ \ you spoil me too much. 」"
        "Soutarou-kun looks shy as he says that,\nand stretches out his chopsticks again."

        scene raimon2
        show ky 001 at center
        with wipeleft

        ky "「[fn], if you want to,\n\ \ would you like to see us practice? 」"
        fn "「Huh? Both of you practice? 」"
        ky "「We're a relatively open club,\n\ \ so anybody can come and watch.{p}\ \ Surely our teammates would have no problem. 」"
        fn "「I see...{p}\ \ If that's the case,\n\ \ maybe I'll stop by if you guys don't mind. 」"
        fn "「Oh, where do you guys practice? 」"
        ky "「The neighboring town's high school grounds.{p}\ \ I go there just about every day.{p}\ \ Why don't we do it tomorrow? 」"
        fn "「Eh? T-tomorrow? 」"
        ky "「No no, I was just speaking figuratively.{p}\ \ But if you change your mind,\n\ \ would that be too much for you? 」"
        ky "「You must be tired from your long trip,\n\ \ you should just relax. 」"
        fn "「Y-yeah, I guess you're right. 」"
        "I give an uncertain response to Kyouji,\nbut because I'm his friend,\nI'll definitely do it."
        "...I'll head to bed early tonight."
        ky "「Oh, is that so, [fn]? 」"
        "Kyouji turns over the meat.{p}As if he remembered something,\nhe opens his mouth to speak."
        ky "「This is your first time meeting Soutarou, right?{p}\ \ You don't know him very well,\n\ \ so this would be a good chance to catch up. 」"
        ky "「That is, a chance to strengthen your friendship. 」"
        fn "「Oh, you're right. 」"
        "The whole time I've been sitting here,\nI've been acting like Soutarou-kun wasn't here."
        "Besides, when he introduced himself he said,\n\"I've heard lots of interesting things about you.\""
        "The \"interesting\" part has been on my mind..."

        scene raimon2
        show ky 001 at midright
        show so 005 at midleft
        with wipe_right

        so "「Eh, but that's...\n\ \ You're kind of forcing me here... 」"
        ky "「Hm, but when we talked about [fn],\n\ \ you said many times you wanted to meet him,\n\ \ didn't you? 」"

        show so at jump_up

        so "「Huh?! Y-yeah, but... 」"
        ky "「Hey, don't be so shy. 」"

        show so 006 with dis

        "When Kyouji pushes him,\nSoutarou-kun looks away in embarrassment.{p}I guess he's the shy type..."
        "If that's the case,\nmaybe I should say something to break the ice..."

        scene raimon1
        show ta 302 at center
        with wipeleft

        ta "「O-oh,\n\ \ is this a marriage interview? 」"
        fn "「A what? 」"
        "As I was worrying about what to say,\nTatsu-nii's drunken voice shouts from behind."
        "At \"marriage interview,\"\neverybody's chopsticks abruptly stop moving.{p}All eyes in the restaurant gather on me."
        "...Wh-what's with this atmosphere..."
        fn "「T-Tatsu-nii,\n\ \ have you been drinking too much? 」"

        show ta 301 with dis

        ta "「H-hm?{p}\ \ I'm not drunk at a-all... 」"
        "I don't think so,\nhe's having trouble with his words."

        show ta 310 with dis

        ta "「So, [fn] and S-Soutarou...{p}\ \ Isn't today the first time y-you've met?{p}\ \ It's also the f-first time you're dining together! 」"
        ta "「All the more reason for a-a marriage interview! 」"
        "I-I think it's called group dating...{p}Oh... group dating is probably...{p}something not known too well here."

        show ta 001 with dis

        ta "「Ah, and is Kyouji the matchmaker? 」"

        show ky 001 at farleft behind ta with wipe_right

        ky "「Well... you could say I am. 」"

        show so 005 at midleft with wipe_right

        so "「S-Senpai!{p}\ \ What're you talking about?! 」"
        "This is starting to get out of hand,\nKyouji's going along with Tatsu-nii..."

        show ta 002 with dis

        ta "「They're both so innocent...{p}\ \ A-as the senior here,\n\ \ should I teach them a-about... 」"
        ta "「...intimate relationships? 」"
        fn "「W-wait, Tatsu-nii,\n\ \ why don't you do someone else's,\n\ \ \"marriage interview\"... 」"

        show ta at jump_up

        ta "「Don't be shy, don't b-be shy.{p}\ \ Everybody's n-nervous the first time... 」"
        "Tatsu-nii grabs my shoulders,\nand whispers it into my ears.{p}H-his breath reeks of alcohol..."
        ky "「Tatsuki-san, they haven't even been on a date,\n\ \ so let's not overdo it.{p}\ \ For now, leave the matchmaking to me. 」"
        ta "「I see, I-I see...{p}\ \ {nw}"
        show ta 009 with dis
        extend "I'll leave them to you,\n\ \ don't let me down! 」"
        
        ky "「Eh, please look forward to it! 」"

        hide ta with wipeleft

        "At Kyouji's honest reply,\nTatsu-nii finally moves away from us."
        "...I guess Kyouji knows how to deal with his...{p}drunkenness."
        "I let out a deep sigh of relief."

        scene black with Dissolve(1)
        scene raimon2
        show ky 001 at midleft
        show so 001 at midright
        with circle_out

        so "「Aah, my heart was pounding... 」"
        fn "「Kyouji...{p}\ \ Why did you have to play along like that? 」"
        ky "「Heheh, I just wanted you two to...{p}\ \ get a little flustered. 」"
        ky "「Besides, you seem like a perfect match,{p}\ \ don't you think? 」"
        fn "「What!?{p}\ \ A-a perfect match...? 」"
        "When he's so explicit about it,\nit's difficult to respond!"
        ky "「At last, my time has come, Tarou.{p}\ \ We must be separated! 」"
        ky "「It's complex, but I'm happy as your senpai. 」"

        show so 005 with dis

        so "「T-that's...{p}\ \ That's not something for you to decide!{p}\ \ You're awful, senpai... 」"
        "Soutarou-kun's face looks sad,\nand he droops his ears.{p}Is he taking Kyouji's little show seriously?"
        ky "「Haha, I'm just kidding, just kidding!{p}\ \ Sorry, Tarou. 」"

        show so 003 with dis

        so "「R-really...? 」"
        ky "「Ah, is matchmaking really this simple? 」"
        "As he says that,\nKyouji gently strokes Soutarou-kun's mane."

        show so 006 with dis

        so "「...S-senpai... 」"
        "He seems to like it when he does that.{p}While his mane is being stroked,\nSoutarou-kun's expression relaxes a little."
        "I can see why Kyouji...{p}plays around with him like that."
        ky "「We'll have an official interview another time. 」"
        fn "「K-Kyouji...{p}\ \ that's... 」"
        ky "「Haha, I know.{p}\ \ I'll let you two go steady first,\n\ \ then a marriage interview. 」"
        ky "「Are you friends now? 」"
        fn "「Yeah, of course.{p}\ \ Nice to meet you, Soutarou-kun! 」"

        show so 003 at jump_up

        so "「Oh yeah! Same here,\n\ \ nice to meetcha! 」"
        "As I talk to Soutarou-kun,\nmy mind recovers."
        "I hate to say it but,\nthanks to Tatsu-nii,\nthe distance between Soutarou and I has shortened."

        jump party_end
        
    #######################################
    label sit_with_juuichi:
        $ event_name = _("Juuichi-san is still continuing with judo, huh?")
        $ love_juuichi += 1
        
        "I return from the bathroom,\nthere's a pile of meat and vegetables on the table.{p}The first thing I hear is Torahiko's whining."

        show to 009 at center with wipeleft

        to "「[fn], sit down! 」"

        show si 001 at farright behind to with wipeleft

        si "「...You know,\n\ \ the guest of honor being late to his own party\n\ \ is a grave situation. 」"
        fn "「Ahaha, sorry, sorry. 」"
        "I look around restlessly.{p}Hmm, where should I sit...{p}As I'm struggling think, Torahiko yells again."

        scene raimon2 with wipe_right
        show to 001 at center with wipeleft

        to "「Hey [fn], sit over here! 」"
        "He's patting an extremely narrow space,\nnext to Juuichi-san.{p}Wa-wait a minute, nobody could fit there!"

        show ka 001 at farleft behind to with wipe_right

        ka "「That'll be too much trouble for [fn].{p}\ \ Stop asking him to do stupid things. 」"
        "It would be a lot of trouble for me,\nI'm glad Kouya's helping me out here."
        "If it wasn't for him,\nI wouldn't have noticed right away."

        show to 009 at jump_up

        to "「Heh, did \"big Kouya-sensei\",\n\ \ save a spot for that special someone? 」"
        to "「Is that why you don't want him to sit there? 」"

        show ka 007 at jump_up
        play sound bosu32

        "SLAM!{p}Kouya stands up without saying a word.{p}D-did he always have such a low boiling point?"

        show ka at shivering

        "His body responds to what's on his mind,\nthat shaking fist carries his message pretty well.{p}Kouya gives Torahiko a fierce glare."
        "With a clack of his chair,{p}Torahiko stands up too.{p}Sparks silently fly between them."
        "Back then,\nthey would get in fights all the time.{p}It looks like that hasn't changed."
        "I just sigh in resignation."
        "THUMP."

        show to 005 at jump_up
        play sound puu75
        
        show ka 007 at farleft

        to "{size=+15}「GYAAAAA!! 」"
        "Suddenly, Torahiko cries out in a strange voice.{p}I look closely, and I can see Juuichi-san."
        "He's tightly grasping the base of Torahiko's tail.{p}Torahiko's stripes look funny when his fur stands up"

        show ju 001 at farright with wipeleft

        ju "「You are being very bad right now. 」"
        "In a considerably low voice,\nJuuichi-san scolds Torahiko."

        show to 006 with dis

        to "「B-but... 」"
        "After several strange meows,\nTorahiko collapses to the floor."

        play sound puu75
        pause .17
        play sound puu75
        pause .1
        show to 008 at jump_up
        pause .1
        hide to with wipe_down
        play sound bosu31

        "Since I don't have a tail,\nI'm not sure how that would feel."
        "But judging by the looks on everyone's faces..."

        scene raimon1
        show ta 006 at center
        show su 004 at midleft
        show ko 005 at midright
        with wipeleft

        "It wouldn't be too hard to make a guess."

        scene raimon2
        show ju 001 at center
        with wipeleft

        "Torahiko's carefree presence was shut down,\nwith only one hand, too."
        "As expected of Juuichi-san.{p}His title of martial artist isn't just for show..."
        ju "「...Kouya, sit. 」"

        show ka 005 at farleft behind ju with wipeleft

        ka "「O-okay. 」"
        "Kouya obediently sits down as soon as he is told.{p}After seeing such an amazing show of force,\nI wouldn't have expected him to do anything else."
        "Meanwhile, Torahiko is still twitching on the floor.{p}...Looks like he's taken some substantial damage."
        ju "「[ln], how long do you plan on standing there? 」"
        fn "「S-sorry! 」"
        "He suddenly calls out my name.{p}I was so on edge that I tensed right up."
        "I think for just a bit,\nthen sit down next to him.{p}Juuichi-san stares right at my face."
        ju "「...Is here all right? 」"
        fn "「Yeah, it's okay. 」"
        ju "「Good. 」"

        show ju 003 with dis

        "Juuichi-san quickly looks away."

        scene raimon1
        show ta 008 at center
        with wipeleft

        ta "「Ah, ahem. 」"
        "In an attempt to improve the mood,\nTatsuki clears his throat loudly."

        show ta 001 with dis

        ta "「Anyway, we should have a toast. 」"

        show ko 005 at farright with wiperight

        ko "「Y-you're right. 」"

        show ko 002 with dis

        "Having smoothed over the situation,\nKounosuke raises his glass into the air.{p}Everybody else folllows."
        "Oh, with one exception.{p}Torahiko remains down on the floor."

        scene raimon1
        show su 001 at center
        with wipeleft

        su "「Uh, umm...{p}\ \ Torahiko-san is still... 」"
        "Shun-kun timidly points at Torahiko."

        show si 001 at farright with wipe_right

        si "「You'll have to wait until sunset before he recovers. 」"

        show ta 002 at farleft behind su with wiperight

        ta "「Leave him alone for now.{p}\ \ He'll be up and running again soon enough. 」"

        show su 004 with dis

        su "「Hmmm...{p}\ \ will he really be all right? 」"
        "Even after hearing their reassurances,\nShun-kun turns his head in doubt."

        scene raimon2
        show ko 005 at midleft
        with wipeleft

        ko "「...So what should we toast to? 」"
        "Kounosuke eagerly waits for an answer.{p}I just want this to be over ASAP."
        "Well, in Kounosuke's case,\nI just want him to hurry up so he'll move.{p}I'm not prepared for his barrage of questions."

        show ka 001 at midright with wipeleft

        ka "「That should be obvious. 」"

        show ko 006 with dis

        ko "「Huh? 」"

        show ka 005 with dis

        "Kounosuke's mouth hangs open.{p}Kouya shakes his head in disappointment."

        show ky 001 at farright with wipeleft

        ky "「We're toasting to [fn]'s return,\n\ \ of course. 」"

        show ko 001 with dis

        ko "「Oh, that's right... 」"
        "Everyone lowers their glasses.{p}Kounosuke hasn't changed a bit."

        scene raimon1
        show ta 008 at center
        with wipeleft

        ta "「So, are we gonna drink soon?{p}\ \ Is everybody ready? 」"

        show ta 001 with dis

        "As Tatsu-nii said that,\nI straightened myself up."
        ta "「There are a lot of things I could talk about,\n\ \ but let's push that aside for now.{p}\ \ All right, you guys ready? 」"
        ta "「To [fn]'s return! 」"

        show ta 002 at jump_up
        ta "{size=+30}「CHEERS!! 」"

        scene raimon2

        everybody "{size=+30}「CHEERS!! 」"

        play sound glass
        pause .3

        "After the toast,\nI gulp down the contents of my glass."

        show ko 001 at center
        show ky 001 at farleft
        show si 002 at farright
        with wipeleft

        "Once everybody's glasses are empty,\nthey start cheering loudly."
        "...Well, I'm just drinking juice.{p}That's all I'll ask the old man for, for now."

        scene raimon2 with wipe_right
        show ju 001 with wipe_right

        "I casually look over and see Juuichi-san.{p}He's silently arranging the food on his plate.{p}His glass is already empty."
        "Juuichi-san finished his drink quicker than me...{p}He's terrible."
        fn "「Juuichi-san,\n\ \ are you gonna get more to drink? 」"

        show ju 003 with dis

        ju "「Hmm, yeah... 」"
        "He grabs some meat with his chopsticks,\nthen stops to ponder something."

        show ju 001 with dis

        ju "「Some tea would be nice... 」"
        "Just as I'm about to say something,\nTatsu-nii wobbles over,\nwith a mug full of a golden-colored liquid."

        show ta 002 at farright behind ju with wipe_right

        ta "「Hey, hey wait a sec.{p}\ \ [fn]'s back, right?{p}\ \ You should be celebrating with beer! 」"

        show ju 003 with dis

        ju "「Tatsu-san, alcohol isn't recommended for minors... 」"
        ta "「Heh, you can't be a minor,\n\ \ with a huge body like that! 」"
        "Tatsu-nii pats Juuichi-san's shoulders.{p}He's already completely drunk..."
        "The law is different for dragons.{p}They can start drinking when they turn 16."
        "...At least that's what Tatsu-nii told me,\nso there's not much credibility."
        ju "「It's all right for you, but I can't. 」"

        show ta 008 with dis

        ta "「Heh, still hardheaded as ever... 」"
        "For a moment he looks disappointed, but then,\nan expression of lust appears on his face."

        show ta 002 with dis

        ta "「...Could the source of that hardheadedness...{p}\ \ be from here...? 」"
        "As soon as he said that,\nTatsu-nii moves his hand to Juuichi-san's crotch.{p}{nw}"
        play sound puu75
        extend "A little \"sproing\" sound plays in my head."

        "Tatsu-nii, I think you've crossed the line..."
        "Tatsu-nii is grinning and laughing,\nbut Juuichi-san is just staring at him quietly."

        show ta 010 with dis

        ta "「...Hm? What are you doing? 」"
        "Suddenly, movement."

        show ju 006 with dis

        ju "「...Hmph!! 」"

        show ta 003 at jump_up
        pause .1
        hide ta with wipe_down
        show raimon2 at vshake
        play sound bosu31
        pause .2

        "One moment, Tatsu-nii's talking.{p}The next, he's on the ground."
        "He makes a loud \"GUH!\" sound.{p}He lets out a small moan."
        "Juuichi-san breathes heavily,\ngiving an imposing stance."
        "I know it's called self-defense,\nbut I think he may've gone a little too far..."
        fn "「J-Juuichi-san!{p}\ \ Cool down! 」"
        "He pulls the cuffs of his blue jersey down."

        show ju 001 with dis

        ju "「...Sorry, I was distracted. 」"
        "With a thump, Juuichi-san sits back down.{p}It's not a very comfortable seat,\nso he moves around a bit, then sits again."
        fn "「I wonder if Tatsu-nii will be okay...{p}\ \ Now I'm 100\% sure he's not okay,\n\ \ judging from those terrible sounds he's making. 」"
        "I catch a glimpse of Tatsu-nii.{p}He's still twitching on the floor."

        show ju 003 with dis

        ju "「Usually I hold back a little, but...{p}\ \ Tatsu-san has a sturdy body, he'll be fine. 」"
        "If this is something that's common,\nthen I'll have to watch what I say,\nfor my own sake."
        "Spending my Summer in a hospital,\nis something I don't want."
        "Come to think of it,\ndid Juuichi-san just do a one-armed shoulder throw?"
        "If I remember correctly,\nhe practiced judo when he was younger."
        "Is he still doing it?"
        "I ask Juuichi-san what's on my mind."
        ju "「...I am still doing judo. 」"
        fn "「Have you been in any matches? 」"
        ju "「Yeah. 」"
        fn "「And...? 」"
        ju "「I have a winning streak...{p}\ \ and nothing but.{p}\ \ It's okay, I guess. 」"
        fn "「Whoa, that's amazing! 」"
        ju "「...It's nothing deserving of praise. 」"
        fn "「...Come on.{p}\ \ I bet that you were secretly hoping that,\n\ \ I'd give you some kind of compliment. 」"
        "When I said that,{nw}"
        show ju 002 with dis
        extend "Juuichi-san's mouth curved into a small smile.{nw}"
        show ju 001 with dis
        extend ""

        "That reminds me,\nI haven't seen him smile at all today."
        "Until now he's been but a \"grumpy bear,\"{p}literally."

        show ju 003 with dis

        "As I look at him and think about that,\nJuuichi-san scratches his face with his finger,\nand asks me a question."
        ju "「Hm, is there something wrong with my face? 」"
        fn "「...No, that's not why I'm looking at you. 」"
        ju "「That kind of answer just worries me... 」"
        "Even though Juuichi-san is my friend,\nI can't just ask him, \"Are you in a bad mood?\"{p}Hmm, I'll have to break the ice."
        "I guess I'll employ more...{p}subtle tactics instead."
        fn "「...Juuichi-san,\n\ \ is there something wrong with...{p}\ \ your body...? 」"

        show ju 001 with dis

        ju "「...No, there's nothing wrong...{p}\ \ Do you think there is...? 」"
        "Uh-oh, might be digging my own grave here."
        fn "「Err, well, you see,\n\ \ I was thinking that...{p}\ \ your facial expressions don't seem too happy. 」"

        show ju 003 with dis

        ju "「...Hm, really? 」"
        "Juuichi-san's head tilts in contemplation."
        "Kyouji-senpai,\nwho was in front of us talking to Soutarou-kun,\nsuddenly joins in on our conversation."

        show ky 001 at farleft with wipe_right

        ky "「Oh, Mikazuki is always like that.{p}\ \ Don't worry about him, [fn]. 」"

        show ju 001 with dis

        ju "「...Hey, what do you mean by that? 」"
        ky "「It's nothing.{p}\ \ You should just work on improving your...{p}\ \ social graces, is all. 」"
        ky "「With that sour look,\n\ \ anybody would think you're not in a good mood. 」"
        "..I didn't say a word,\nhow did he know what I was thinking?"
        "And he was just talking to Soutarou-kun,\nbut he heard our conversation too."
        "Kyouji-senpai's evil, I mean, err...{p}observant eyes are frightening."
        ky "「Didn't you make a child cry the other day? 」"

        show ju 003 with dis

        ju "「...You saw that? 」"
        ky "「I just happened to be passing by. 」"
        "Not only does Juuichi-san have a stern face,\nbut he's pretty tall as well."
        "Tatsu-nii has him beat,\nbut he's has to still be around 2 meters."
        "...I'm only average,\nbut I'm not envious about what Kyouji-senpai said."
        "Even if I had a body like that,\nI wouldn't want to scare small children."
        "His voice is also lower than I remember it."

        show ju 001 with dis

        ju "「[ln]...{p}\ \ does it really look like I'm in...{p}\ \ a bad mood? 」"
        fn "「...Well, yeah. 」"
        "Well, there's no use hiding it.{p}I nod to Juuichi-san's words."
        ju "「...I see. You worry about me too much.{p}\ \ It's a bad habit, I'll try to fix it... 」"
        ky "「Incidentally,\n\ \ he's actually in a good mood today. 」"
        "...What, with that kind of face!?{p}The words in my head almost slip out,\nbut I frantically swallow them."
        ky "「Actually, he's like you, [fn].{p}\ \ When Mikazuki's emotions change,\n\ \ I can notice it immediately. 」"
        ky "「In other words,\n\ \ His behavior is easy to understand. 」"
        fn "「I-I see... 」"
        "I steal a glance at his face,\nit's still as stern as it was before.{p}Is he really in a good mood...?"
        ju "「If you ask me,\n\ \ Takahara is the one who's,\n\ \ \"hard to understand.\" 」"
        "Juuichi-san mutters,\nwhile getting a small plate of meat."
        ky "「Hahaha! 」"
        "Kyouji-senpai laughs a little.{p}Juuichi-san gives a bitter smile."
        "It seems like the two are good friends.{p}Pretty sure they're the same age, too.{p}They probably do things together on a daily basis."
        ju "「Here's your portion, [fn]. 」"
        "A small plate of food is placed in front of me.{p}Ah, this must be mine."
        "Juuichi-san expresses his gratitude,\nthen puts some meat into his mouth."
        "Oh, this is delicious.{p}The meat itself is pretty good,"
        "but being surrounded by old friends,\nonly makes it better."
        "While thinking, I leisurely eat."
        "Hey!{p}I'm still unfinished,\nbut there's more meat!"

        show su 002 at midright with wipe_right

        su "「[fn]-san, please have some! 」"
        "Shun-kun politely holds out another serving for me.{p}Of course he's providing this service with a smile.{p}I can't refuse, so I say thanks and take it."

        show so 001 at farright behind su with wipe_right

        so "「Senpai, you have some, too! 」"
        "Every time Shun-kun serves something,\nSoutarou-kun does the same.{p}...Is this like an infinite loop"
        "Well, for now I'll just concentrate on eating.{p}All I'll think about is the piles of meat,\nlining up in front of me."

        jump party_end

    ############################################
    label sit_with_shun:
        $ event_name = _("Dinner with Shun")
        $ love_shun += 1

        show su 001 at center with wipeleft

        "With orange juice in front of him,\nShun-kun is perched on his chair.{p}Suddenly, I feel as if I'm back in those days."
        fn "「Is it okay if I sit next to you? 」"

        show su 002 with dis

        su "「[fn]-san! Of course it is. 」"
        "This wolf with big round eyes,\nhe's my childhood friend Shun Kodori.{p}He greets me with a brilliant smile."

        show su tailwag 01 with qdis

        su "「...Hehe. 」"
        "His chopsticks and meat are flying about,\nit almost looks like a battleground around him.{p}...Hmm, should I start eating?"
        fn "「Shun-kun? Here,\n\ \ did you lose some of your meat? 」"

        hide su504
        hide su505
        hide tailwag
        show su 001
        with dis

        su "「Ah, thanks! Hehe. 」"

        show su 002 with dis

        su "「You came back, I'm so happy!{p}\ \ Everybody's glad... I am too. 」"
        fn "「R-really? I feel kind of awkward...{p}\ \ Here, you eat too. 」"
        su "「Okay! 」"

        show su 001 with dis

        "He nods his head,\nthen picks up his chopsticks and bowl."
        "While asking a hectic barrage of questions,\nShun-kun watches my every move."
        "Nom.{p}Munch-munch.{p}Gulp."

        show su 002 with dis

        su "「Really? 」"

        show su 001 with dis

        "Nom.{p}Munch-munch.{p}Gulp."

        show su 005 with dis

        su "「I don't have that. 」"

        show su 001 with dis

        "He swallows a big mouthful,\nthen continues talking."
        "A big mouthful again,\nthen the same as before.{p}Somtimes I can't keep up with the conversation."
        "He doesn't have very good manners,\nmaybe I should teach him some."
        "There's a difference between how he eats,\nand how everyone else does."
        "I'd like to to tell him how to carry his food,\nor how to evenly break his chopsticks."

        show su 004 with dis

        su "「Ah, [fn]-san,\n\ \ a grain of rice. 」"
        fn "「Hm? 」"
        "Shun-kun gently sets his dish down,\nstretches his hand out to my cheek,\nand picks up the rice with his finger."

        show su 001 with dis

        "He wraps it in a nearby napkin."
        "I felt a little humiliated.{p}\"Oh, it's not a big deal.\" he says.{p}Well, if he says so."
        "Should I have just licked it off?"

        show su 002 with dis

        su "「[fn]-san, you've gotten so much bigger! 」"
        fn "「You think so?{p}\ \ Shun-kun, you've... 」"

        show su 005 with dis

        "I take a good look at him.{p}From head to toe,\nno matter how hard I try to convince myself,"
        "Shun-kun just hasn't changed that much."
        fn "「Shun-kun, I guess you're growing...? 」"
        "I try to make my words vague."

        show su 002 with dis

        su "「That makes me happy,\n\ \ not a lot of people say that to me. 」"
        "It's been 5 years,\nI wonder if anybody's said something about...{p}his height as well."

        scene raimon1 with sdis

        "The party goes on.{p}The sound of this familiar hustle and bustle,\nit tickles my ears."
        "I had no choice but to loosen my cheeks.{p}Time stopped, then started.{p}That's what it feels like."
        "Has Shun-kun really not gotten any taller...?"

        jump party_end
        
    ######################################
    label sit_with_shin:
        $ event_name = _("Next to Shin-kun")
        $ love_shin += 1

        fn "「Is it all right if I sit next to you? 」"

        show si 001 at center with wipe_right

        si "「...Go ahead. 」"
        "His reply is half-hearted,\nbut it's not to the point of being unsocial."
        "This is my childhood friend speaking like this,\nbut I'd feel uncomfortable if it was anyone else."

        show ka 002 at midright behind si with wipe_right

        ka "「Shin, are you like, anxious or something? 」"
        si "「Not particularly... 」"

        show ka 001 with dis

        ka "「Yeah, you're saying that, but...{p}\ \ you got here even earlier than I did.{p}\ \ Isn't there something you wanted to say to him? 」"
        fn "「Huh? Is that true? 」"
        ka "「Yeah. 」"
        si "「I just didn't want to be late.{p}\ \ So I got here ahead of time. 」"

        show ka 003 with dis

        ka "「Is that really it? 」"

        show ko 002 at farleft with wipe_right

        ko "「Hah, doubt it. 」"

        scene raimon2 with wipe_right

        si "「... 」"
        "Kounosuke cuts in from the side.{p}Shin-kun tries to keep his cool.{p}His cheeks are red, is he embarrassed?"
        "Come to think of it,\nShin-kun was never a very social person.{p}I see what's going on here."
        fn "「Shin-kun, have you been thinking about me? 」"
        "I tease him a little,\nand put my hand on his shoulder.{p}A little fooling around will brighten the mood."

        show si 001 at center with wipe_right

        si "「...It would be stupid...{p}\ \ for me to think about things like that. 」"
        "Guh!{p}As expected, my teasing has no effect."
        "He roughly brushes my hand off his shoulder,\nand glances at me with a look of contempt.{p}I quickly look away from him."
        fn "「S-Shin-kun.{p}\ \ It was just a hand on the shoulder,\n\ \ I'm just messing with you. 」"
        si "「I know. 」"

        scene raimon2
        show ka 001 at midright
        show ko 001 at farright
        with wipeleft

        ko "「Uh-oh. 」"

        scene raimon2 with wipeleft

        "Apparently, I've completely offended him.{p}Before I know it,\nKouya and Kounosuke withdraw from the conversation."
        "Tension arises between Shin-kun and me.{p}However, everyone else is asking me many questions.{p}Food and drink arrive at the same time."
        "We didn't have to wait long,\nprobably because we've rented the place out."
        "The meat is served to each table,\nand the drinks are served as well.{p}Then, Tatsu-nii stands up."

        scene raimon1
        show ta 002 at center
        with wipeleft

        ta "「So then, this time we're celebrating our reunion!{p}\ \ Cheers! 」"
        "{size=+30}「CHEERS! 」"
        
        play sound glass 

        scene raimon2 with wipe_down

        "With a beer in each hand,\nTatsu-nii raises them for a toast."
        "Shin-kun is a little more conservative.{p}He raises his melon soda."

        show ta 002 at center with wipe_right

        ta "「Glug, glug, bwah! 」"
        "Right after the toast,\nTatsu-nii chugs down both his drinks."

        show ta 004 with dis

        ta "「[fn], hurry up and eat!{p}\ \ There's no need to hold back! 」"
        fn "「Yeah, I will. 」"

        hide ta with wipeleft

        "While holding his alcohol with vigor,\nTatsu-nii throws some meat onto his plate."
        "The sizzle of cooking meat,\nand the smell of it as well,\ncarries itself throughout the restaurant."
        "Tatsu-nii grabs lumps of meat,\nwhile Shin-kun neatly takes pieces,\none by one."
        "Enchanted by the smell and sound,\nmy stomach is already begging for some.{p}I decide to go for it."

        show si 001 at center with wipe_right

        si "「Wait, it hasn't cooked yet. 」"
        fn "「Huh? 」"
        si "「I turned it over a little bit ago.{p}\ \ This way it will cook slowly. 」"
        fn "「Th-thanks. 」"
        "He points to the meat as he explains.{p}It certainly is going to be cooked well,\nbut half my life will be gone before that."
        si "「Half a lifetime isn't good for digestion. 」"
        "Shin-kun adds,\nas if he heard what I was saying in my head."
        si "「Or would you rather have it medium rare? 」"
        fn "「No, I'd say well done would be better. 」"
        si "「All right then... 」"
        "After I say that,\nShin-kun returns to working on the meat."
        fn "「Are you going to eat? 」"
        si "「I will. 」"
        "Although he says that,\nShin-kun has just been poking around with his food.{p}I haven't been able to get a plate for myself."
        fn "「But it's been so long. 」"
        si "「Hm? Oh. 」"
        "Without much reaction,\nShin-kun shifts from arranging his food to eating it.{p}Maybe he's still mad at me?"
        si "「Is something wrong?{p}\ \ It looks like you stopped moving your chopsticks. 」"
        fn "「N-no, it's nothing... 」"
        "I-I don't understand.{p}I really have no idea what he's thinking.{p}Is he not angry...?"

        show ta 002 at midright behind si with wipe_right

        ta "「Heeey, you!{p}\ \ Are you eating right? 」"
        si "「Eh, err. Well... 」"

        show ta 007 with dis

        ta "「Hmm, w-what's the matter Shin?{p}\ \ You've been w-waiting so long for...{p}\ \ [fn] to be at y-your side, 」"
        ta "「but you still look down. 」"

        si "「It's nothing, this is how I usually am. 」"

        show ta 001 with dis

        ta "「I know you can be picky.{p}\ \ Go on. M-make sure you're eating right,\n\ \ and as much as y-ya can, too! 」"
        si "「Ah!? 」"

        show ta 009 at jump_up

        ta "「[fn], you should eat more v-veggies, too!{p}\ \ If you only e-eat meat you'll get fat. 」"
        "While saying that,\nTatsu-nii fills up my plate with veggies."

        hide ta with wipe_right

        ta "「Hey, little kids!{p}\ \ Are you eating right? 」"
        su "「Yes, I am. 」"
        ta "「You're not eating anything at all are you?{p}\ \ You're not g-going to grow at this rate! 」"
        su "「Whawhawhawha!?{p}\ \ I-I can't eat that much! 」"
        so "「M-Midoriya-senpai!{p}\ \ There's no way I could eat all that! 」"
        "H-he's completely drunk...{p}And keeps finding little games to get involved in."
        "With a bitter smile on my face,\nI return to eating for the second time."
        "I can use my chopsticks again,\nnow that he stopped using them to get food."
        "I can't get to the meat like this.{p}Still, I don't want to return it..."
        si "「[fn], wait. 」"
        "I think about asking someone for help,\nbut Shin-kun speaks out."
        fn "「What's the matter? 」"
        si "「...You can have my meat. 」"
        fn "「Huh? Th-thanks, but why? 」"
        "Shin-kun holds out his plate.{p}There's a sharp contrast between\nthe amount of meat on our plates."
        si "「I don't like beef.{p}\ \ It's too greasy... 」"
        "With him and his high class ways,\nI was expecting something like,"
        "\"This cheap meat isn't suitable for me.\"{p}But his answer was surprisingly... Normal."
        "Come to think of it,\nShin-kun was eating meat a little bit ago."
        "It was chicken, though.{p}Does he have the same nutritious, healthy,\neating habits as Tatsu-nii?"
        fn "「Would you like to switch with mine? 」"
        si "「It doesn't matter. 」"
        "Yes!{p}Now that Tatsu-nii is bothering Torahiko,\nwe secretly swap plates."
        "It's yakiniku, so of course there should be meat.{p}But was forcing all of that on him... Rude?"
        "I check my thoughts with Shin-kun,\nbut he's already shoveling them into his mouth,\none after another."
        "I think he's almost smiling."

        show si at jump_up

        si "「Ah, onion... 」"
        "He stops his chopsticks.{p}The way he whispers to himself is... Funny."

        jump party_end
        
    ###########################################
    label sit_with_kounosuke:
        $ event_name = _("Next to Kounosuke")
        $ love_kounosuke += 1

        show to 001 at farleft
        show ju 001 at farright
        show ko 001 at center
        with wipeleft

        fn "「Kounosuke, is here all right? 」"

        show ko 003 at move_midright(1.5)

        ko "「Go ahead, go ahead. 」"
        "Even though he says that,\nhe's stuffed in there."

        show ju 003 with dis

        ju "「Kounosuke, there's not enough room. 」"

        show ko 001 with dis

        ko "「Ah, sorry. 」"

        show to 006 with dis

        to "「Why are you going over there? 」"
        fn "「Well, it looked like there was space... 」"
        to "「If it wasn't so packed there would be. 」"

        show ko 005 with dis

        ko "「You're being bossy, Torahiko.{p}\ \ He can sit wherever he wants,\n\ \ it's not a big deal. 」"
        to "「Well yeah, but... 」"
        "Now that I think about it,\nTorahiko did say he wanted to sit next to me,\nwhen he greeted me."
        "I guess he was really excited to see me..."
        "If that's the case, sorry Torahiko."

        scene raimon2 with wipe_right
        show ko 001 at center with wipe_right

        ko "「By the way, [fn]... 」"
        "Here it comes, I'm prepared for this.{p}That's why I sat here.{p}The assault of questions begins."
        "I wanted to talk with everyone else,\nbut I was mostly answering his questions."

        show ta 001 at farleft behind ko with wipe_right

        ta "「H-hey, guys, d-did you get something to drink? 」"

        show ko 002 with dis

        ko "「I have a Coke.{p}\ \ Anyway, let's continue... 」"

        show ta 002 with dis

        ta "「Hey, hey, let h-him rest a bit.{p}\ \ You've been interrogating him for a while,\n\ \ haven't you? 」"

        show ko 001 with dis

        ko "「It's not like that!{p}\ \ Right [fn]? 」"
        fn "「Err, I'd like to order something...{p}\ \ I think... 」"

        show ko 006
        show ta 008
        with dis
        ta "「I don't have all day. 」"

        show ko 005 with dis

        ko "「Hmm, sorry.{p}\ \ I didn't mean to do that. 」"
        fn "「No, no, it's all right. 」"
        "He doesn't mean any harm,\nbut he is a little obstinate.{p}Kounosuke really hasn't changed."

        scene raimon1 with wipe_right

        "I ask for the oolong tea.{p}I was going to order some meat but,\nsince we've rented the place out,"
        "everything's already ordered and set."
        "Awesome, it's like a dream come true.{p}It's like ordering everything at a yakiniku stand.{p}It's every high schooler's dream, I'm happy."
        "Right when I order my drink,\nthe already prepared food is brought out.{p}Finally, each drink is raised for the toast."
        "{size=+30}「CHEERS! 」"

        play sound glass

        "At that signal,\nthe aroma and sound of cooking meat spreads."
        "I set out the meat the way I like it,\nthen wait for it to turn a good color."

        scene raimon2
        show ko 001 at center
        with wipeleft

        ko "「[fn], could you pass the sauce? 」"
        fn "「Oh, sure. 」"

        show ko 002 with dis

        ko "「Thanks. 」"
        fn "「Huh? 」"
        "I pass the sauce and return my eyes to my plate.{p}My salted tongue has disappeared!"

        show ko 001 with dis

        ko "「What's wrong? 」"
        fn "「My salted tongue is gone... 」"

        show ko 005 with dis

        ko "「Was it the one right over there? 」"
        fn "「...Yeah. 」"

        show ko 003 with dis

        ko "「Ah, sorry! I ate it... 」"
        fn "「What!? 」"
        "He's saying that while eating some beef ribs."
        fn "「Aaaugh....{p}\ \ And I was the one who made it, too! 」"
        "I just turned it over not too long ago,\nso it still needed more time to cook."

        show ko 004 with dis

        ko "「Don't worry about something so small,\n\ \ we've still got plenty. 」"
        ko "「Besides, when it comes to yakiniku,\n\ \ it's first-come-first-served.{p}\ \ Survival of the fittest. 」"
        fn "「Hmph. 」"
        "The world of yakiniku has harsh laws."

        show ko 006 at jump_up

        ko "「Hey, that's my wiener! 」"
        fn "「You're too soft, Kounosuke.{p}\ \ Yakiniku is survival of the fittest,\n\ \ after all. 」"

        show ko 005 with dis

        ko "「Hmph. 」"
        fn "「Ah! My salted tongue!{p}\ \ That's two times now! 」"

        show ko 002 with dis

        ko "「Survival of the fittest! 」"

        show ko 006 at jump_up

        ko "「Ah! You took my wiener again! 」"
        fn "「Oh crap, I was aiming for that... 」"

        show ko 001 with dis

        ko "「That's my sagari meat! 」"
        fn "「My salted tongue!{p}\ \ That's the third time! 」"

        show ko 004 with dis

        ko "「Wiener get! 」"
        fn "「I got a salted tongue! 」"

        scene raimon2 with wipe_right
        show si 001 at center with wipeleft

        si "「Can't you guys eat a little more quietly? 」"

        show su 004 at midright with wipeleft

        su "「You guys have bad manners... 」"
        "Kounosuke and I continued...{p}Our fierce yakiniku war waged on and on."

        jump party_end
        
    #######################################
    label sit_with_torahiko:
        $ event_name = _("Torahiko's Welcome")
        $ love_torahiko += 1

        "I decide to sit with Torahiko."

        show to 002 at center with wipe_right

        to "「Oh, [fn]!{p}\ \ Over here! Over here! 」"
        "Torahiko bangs on an empty seat,\nand cheerfully beckons me over."
        fn "「Well then, excuse me. 」"

        show to 001 with dis

        to "「Heh heh, of course you'd sit next to me! 」"
        "Torahiko rubs up on me, looks like he's happy.{p}He always loved physical contact,\nI can see that hasn't changed."
        fn "「Stupid, there just happened to be a spot. 」"

        show to ray 01 with dis

        to "「Dahaha, you're just being shy!{p}\ \ I'll be the yakiniku magistrate,\n\ \ since you're the honored guest today! 」"

        show ju 001 at farright with wipe_right

        ju "「Don't burn it, or take it all for yourself. 」"

        show to 007 with dis

        to "「You don't trust me, Senpai? 」"
        ju "「Yes, your gold-medal gluttony is a blight.{p}\ \ Not only on Minasato Village,\n\ \ but to the whole nation. 」"

        hide to
        show to 002 at midright
        with dis

        to "「Don't worry, you'll get your share.{p}\ \ {nw}"
        show to 001 with dis
        extend "But I'll get you lots of veggies,\n\ \ because you've been looking plump lately. 」"

        show ju 007 with dis
        ju "「Dahahaha{nw}"
        show ju at jump_up
        play sound hit_p00
        show to 005
        show raimon2 at hshake
        show to at hshake
        extend "DAAA! 」"

        "I hear a loud blunt sound down by our feet.{p}Under the table,\nthere seems to have been a violent impact."

        show ju 001 with dis

        ju "「This isn't fat, it's muscle.{p}\ \ An equal amount of meat and vegetables,\n\ \ will be fine, Tora. 」"

        show to 008 with dis

        to "「Fuwah... fuwah...{p}\ \ Th-that was my shin, my shin... 」"
        "As he curls his body in agony,\ntears start to form in Torahiko's eyes."
        "Well, it looks like...{p}Juuichi and Torahiko are as comical as ever."

        scene raimon1 with wipe_right

        om "「Yo, what are you waiting for?{p}\ \ There's plenty here!{p}\ \ So don't be afraid to eat as much as you want! 」"
        "The old man yells vigorously,\nas he comes out of the kitchen.{p}He brings out a platter, full of meat and veggies."
        "Suddenly, cheers can be heard,\nthroughout the restaurant."

        scene raimon2 with wipeleft
        show to 003 at center with wipe_right

        to "「Oh yeah!{p}\ \ Today I'm gonna eat and eat! 」"
        "Just a bit ago he had a tortured look on his face,\nbut now it seems that\nthe mountain of meat has stolen his heart."
        "That was a hasty recovery."

        show to 002 with dis

        to "「Well then, I'll start cooking.{p}\ \ I think I'll roast it, then eat it up fast! 」"

        show to 001 with dis

        to "「Ah, Shun.{p}\ \ Could you set the heat on maximum? 」"

        show su 002 at farright behind to with wipe_right

        su "「Okay! 」"
        "Here and there,\nI hear the sound of cooking meat and vegetables."
        "The delicious smell of cooking meat,\nstirs up my appetite."
        "Everybody is sitting,\nand happily talking to each other.{p}I like this kind of atmosphere."

        scene raimon2 with wipe_right
        show to 001 at center with wipe_right

        to "「I'm always impatient,\n\ \ when it comes to cooking meat. 」"

        show ju 001 behind to at farleft with wipeleft

        ju "「At times like this,\n\ \ I make some sauce. 」"
        "As he says that,\nJuuichi-san mixes sweet and spicy sauces,\nto make his own."
        "When he is satisfied with the combination,\nJuuichi-san takes a bottle out of his pocket.{p}It's full of a yellow liquid, and he adds it."
        "What is that?{p}I think it's lemon juice or vinegar but...{p}It's coming out all syrupy..."

        show ju 002 with dis

        ju "「There, that's good... 」"
        "After completing his special sauce,\nJuuichi-san tastes a light sample of it.{p}He nods with a satisfied look on his face."

        show ju 001 with dis

        "Stuck on the bottle is a small bee sticker."
        "It's yellow, comes out syrupy,\nhas a bee sticker, and he's a bear...{p}Seriously!?"
        "Upon realizing what the yellow liquid is,\nI almost spit out my tea."
        "I-it's honey sauce... for yakiniku?{p}Juuichi-san... no matter how good it is,\nI should have expected that."

        show to 007 with dis

        to "「Juuichi-senpai still has a sweet tooth...{p}\ \ It can get out of hand. 」"
        fn "「Juuichi-san showing his true character...{p}\ \ It can be amazing, sometimes. 」"
        ju "「Did you say something? 」"
        "Juuichi-san gives us a sharp glare.{p}Torahiko and I cringe in fear."

        show to 011 at jump_up

        to "「N-nothing! L-look! The meat's burning!{p}\ \ The salted tongue will...{p}\ \ go well with your special sauce! 」"

        show ju 002 with dis

        ju "「...You don't need to tell me that. 」"
        "Looks like he's back in a good mood..."
        "Torahiko passes out the food for everybody."

        scene raimon2 with wipe_right
        show to 002 at center with dis

        to "「[fn], hurry up and eat! 」"
        "With the essentials passed out,\nwe start grilling all of the meat and veggies."

        show su 004 behind to at farright with wipeleft

        su "「Torahiko-san, there's so much I have to cook,\n\ \ I won't have time to eat. 」"

        show to 011 with dis

        to "「Ah, sorry, sorry.{p}\ \ I have a habit of getting preoccupied.{p}\ \ All right let's eat, thank you for the meal! 」"

        show su 001 with dis

        "Torahiko's love of cooking and skill,\ncomes from him being his family's only son."
        fn "「That reminds me,\n\ \ are you still helping out at the inn? 」"

        show to 001 with dis

        to "「Hm? Oh yeah. 」"

        show to 002 with dis

        to "「After starting junior high,\n\ \ I had to work more and more.{p}\ \ It got pretty serious! 」"
        fn "「Really, I can see things haven't changed. 」"
        "Torahiko's family owns the Ooshima Inn."
        "In elementary school,\nhis parents were always busy.{p}Because of this, he had to do some of the work."
        "He had to go shopping, do the laundry, clean, etc.{p}I remember even as a child,\nhis family put some of the burden on him."

        show to 006 with dis

        to "「Man... I have to work without getting paid...{p}\ \ They're so stingy.{p}\ \ {nw}"
        show to 002 with dis
        extend "Ah, old man! Let's get some more rice 」!"
        
        "Ooshima Inn is the town's only inn.{p}It's not the best place,\nbut the villagers stop by for its hot springs."
        "If I remember correctly,\nhis father's cooking was the reason for its success.{p}Many people would travel from afar to have it."
        "It went from being an inn for those in the know,\nto a reputable, well-established place."
        "Torahiko would treat me to dinner at his house.{p}His father would make a meat and potato stew.{p}The flavor would stick with me even when I got home."
        "I would always ask my mom to make it."
        fn "「I want to eat your dad's cooking again... 」"

        show to 001 with dis

        to "「If you want, I could make something.{p}\ \ I could show you a little of my cooking,\n\ \ to see how confident I am. 」"

        show su 002 with dis

        su "「Torahiko-san's dad has been teaching him. 」"

        show to 002 with dis

        to "「Yeah, my dad's passing down his recipes!{p}\ \ Food is my forte now. 」"
        "I'm a little skeptical about Torahiko's cooking.{p}I wonder what the hell it'd taste like..."
        "While I was thinking about that,\nthe meat on the grill has cooked,\nto just the right condition."

        show to 001 with dis

        to "「Here, take some more of the meat!{p}\ \ If you don't,\n\ \ it's gonna disappear quickly. 」"
        "Shun-kun stares at a piece of cooked meat."

        show su 001 with dis

        su "「I'll get that one. 」"

        show to 002 at jump_up

        to "「...(Munch, munch.) 」"
        su "「... 」"
        "It doesn't look like he got it...{p}He pulls himself together,\nand reaches out for another piece."

        show su 005 with dis

        su "「All right then, this one. 」"

        show to at jump_up

        to "「...(Om, nom.) 」"

        show su 004 with dis

        su "「...Aww. 」"
        "With lowered ears and sad, pleading eyes,\nhe stares at Torahiko."

        show to ray 01 with dis

        to "「Heh heh, what's wrong, Shun? 」"

        show su 003 with dis

        su "「Ooh, you're being mean,\n\ \ and taking the meat before I can get it. 」"

        show to 003 with dis

        to "「You're too naive!{p}\ \ Grub grill's a game of speed and dexterity. 」"
        to "「The strong get the meat,\n\ \ the weak are left with vegetables. 」"

        show to ray 01 with dis

        to "「That's the way the game of grub grill works!{p}\ \ {nw}"
        show to  at jump_up
        extend "Dahaha! 」"

        show su 004 with dis

        su "「So it's the...{p}\ \ grub grab grub grill game? 」"

        show to 002 with dis

        to "「Yeah, the grub grub grill...{p}\ \ The grab grub grade...{p}\ \ {nw}"
        show to 006 with dis
        extend "The... grub grab girl game... 」"

        "Those two still haven't taken a bite..."

        show su 005 at jump_up

        su "「Torahiko-san, I won't lose! 」"
        "With his new-found resolve,\nShun is a completely different person."
        "His chopsticks move with great speed,\nback and forth from the iron plate."

        show su at jump_up

        su "「Hiyaa! 」"

        show to 003 at jump_up

        to "「Oh! Don't think I'll let you win! 」"
        to "「Om, nom, om, nom, om, nom. 」"

        show su 003 with qdis

        su "「...Oooooh. 」"

        show to ray 01 with dis

        to "「Come on, concentrate...{p}\ \ {nw}"
        show to ray 01 at jump_up
        extend "Dahaha...{p}\ \ {nw}"
        hide tora_ray
        play sound bosu31
        show to 008 at jump_up
        extend "DAAAAA!! 」"

        "At that time I hear a strong impact under the table.{p}Torahiko holds his shin in pain."

        show ju 001 at farright with wipeleft

        ju "「...Tora.{p}\ \ Stealing is not something to be admired. 」"
        to "「A-all right, I won't steal... 」"
        "Jeez, 10 minutes haven't even passed.{p}I didn't think I'd see that happen again..."

        scene raimon2
        show ky 001 at center
        with wipeleft

        ky "「Don't worry about it too much, [fn]. 」"

        show ka 002 at farleft with wipe_right

        ka "「Ah, we see this happen all the time. 」"

        show so 005 at midleft with wipeleft

        so "「Usually Ooshima-senpai will mess with Shun-kun,{p}\ \ then Juuichi-san will punish him.{p}\ \ It's a regular pattern. 」"
        ky "「Haha. Oh, Mikazuki.{p}\ \ It looks painful,\n\ \ but he's going easy on him. 」"
        fn "「I-I see... 」"
        "Compared to Torahiko,\nI wouldn't stand a chance."
        "I'd probably fall down in surprise,\nand wouldn't be able to move..."

        scene raimon2
        show ju 001 at farleft
        show su 001 at farright
        show to 008 at center
        with wipe_right

        to "「A... a kick can't go...{p}\ \ in the same place consecutively! 」"

        show su 004 with dis

        su "「T-Torahiko-san...{p}\ \ are you okay...? 」"

        show to 006 with dis

        to "「Sh-Shun... 」"
        ju "「Shun, go get some vegetables for Tora.{p}\ \ The vitamins and minerals you get from them,\n\ \ are important for nutrition. 」"

        show su 002 with dis

        su "「Roger that! 」"

        show to 007 with dis

        to "「Dohoho... 」"
        "Torahiko's getting what he deserves."

        scene raimon1 with wipe_down

        "We're getting right into the middle of the party,\nand my stomach is nice and full."
        "But we're still at the age where we eat a lot,\nso everybody is still at it."
        "Even Shin-kun, with his small appetite,\nis having a good time.{p}He's happily moving his chopsticks along."

        scene raimon2 with wipeleft

        om "「Oh, you're waiting on more meat!{p}\ \ Your appetite is the same as ever, Tora! 」"

        show to 002 at center with wipeleft

        to "「Yep, I'm eatin' nonstop! 」"

        hide to with wipe_right
        show ky 001 at center with wipeleft

        ky "「Ooshima sure is fast.{p}\ \ There's plenty of time,\n\ \ so don't rush yourselves. 」"

        show ju 003 at farright with wipeleft

        ju "「Don't eat too much.{p}\ \ Your meet is coming up soon. 」"

        show to 002 at farleft with dis

        to "「Heh heh, since it's [fn]'s welcoming party,\n\ \ it's all right not to hold back,\n\ \ so there's no need to say that, senpai. 」"

        show ju 001 with dis

        ju "「Don't use [fn] as an excuse, damn it...{p}\ \ Also, there's not going to be enough meat for him. 」"
        fn "「Don't worry, I'm eating at my own pace. 」"

        show to 001 with dis

        to "「Hey, hey, [fn]'s all right with it! 」"

        show ju 006 with dis

        ju "「You... just settled that because...{p}\ \ you're just being coy! 」"
        "This isn't turning out good."
        "Before that happens a third time,\nI think of something to change to topic."
        "Come to think of it,\nJuuichi-san did mention that a meet was coming up..."

        scene raimon2 with wipe_right

        fn "「A little bit ago,\n\ \ Juuichi-san said something about a swim meet.{p}\ \ Are you entering, Torahiko? 」"

        show to 001 at center with dis

        to "「Ah, I haven't told you yet.{p}\ \ I'm in the swimming club. 」"
        "Back in elementary school,\nTorahiko was a very fast swimmer."
        fn "「Back then you were always the fastest.{p}\ \ And now you're in the swimming club. 」"

        show su 002 at farright behind to with wipeleft

        su "「You're amazing, Torahiko-san!{p}\ \ All the best swimmers are gonna be there,\n\ \ from all around the country, it's gonna be big! 」"
        "Shun-kun takes the words right out of my mouth."
        fn "「That is really amazing, isn't it? 」"

        show ko 003 at farleft behind to with wipeleft

        ko "「In your first year you,\n\ \ won the prize at the rookie match, didn't you? 」"
        ko "「You're something of a celebrity,\n\ \ in the world of high school swimming. 」"

        show to ray 01 with dis

        to "「Heh heh, when that sort of talent is born,\n\ \ that's the kind of result you would expect,\n\ \ or something like that, at least. 」"
        "Torahiko triumphantly puffs his chest out with pride."

        show ta 001 at midleft behind ko with wipe_right

        ta "「Toraa, you're usually so carefree,\n\ \ but when you decide to snap into it,\n\ \ you look really... Awesome... 」"
        "Somehow, Tatsu-nii appeared from the side.{p}His eyes keep looking all around Torahiko,\nand stayed like that as he continued talking."

        show to 005 at jump_up

        to "「Whoa, when did you get here!? 」"

        show ta 002 with dis

        ta "「Torahiko, get fired up!{p}\ \ Banshaaaaaaaai...! 」"

        show to 011 with dis

        to "「Th-thanks...? 」"

        show ta 004 at jump_up

        ta "「Toraa... I was just thinking of something earlier!{p}\ \ You're a man among men! 」"

        show to at hit_left

        to "「Hey hey, there's no need for that much...{p}\ \ Err... Flattery. 」"
        "Torahiko is being humble,\nwhile giving a troubled, wry smile."
        "Without any care,\nTatsu-nii continues to stare at Torahiko,\nhis expression as blank as ever."
        "He's looking really strange..."

        show ta 007 with dis

        ta "「You're so cute... 」"

        show to 007 with dis

        to "「Eh? 」"

        ta "「When you hide your embarrassment like that,\n\ \ it's really cute, Toraa...\n\ \ Mm, {nw}"
        play sound puu75
        show ta at hit_right
        extend "kiss, {w=.15}{nw}"
        play sound puu75
        show ta at hit_right
        extend "kiss, {w=.15}{nw}"
        play sound puu75
        show ta at hit_right
        extend "kiss! 」{w=.1}"

        "While grabbing onto Torahiko from the side,\nhe starts rubbing his face around."

        show to 008 at jump_up

        to "「Geh, you're a little drunk, aren't you?{p}\ \ Whoa, stop gettin' all over me.{p}\ \ And I'm not that cute. 」"

        show to 005 with dis

        to "「Ah, idiot. That's... 」"
        "Tatsu-nii's violently shaking Torahiko,\nit doesn't look like he'll be...{p}releasing his firm embrace any time soon."

        show ju 007 at farright with wipe_right

        ju "「Tatsu-san, what are you doing? 」"
        "As Juuichi-san hastily pulls them apart,\nhis face is red for some reason."

        scene raimon2
        show ta 002 at midleft
        show to 005 at farright
        show ju 007 at center
        with wipe_right

        ta "「Juuichiii, are you lonely because,\n\ \ nobody's touching your belly? 」"

        show ju at jump_up

        ju "「Wh-what are you doing!? 」"

        hide ta with wipe_down
        play sound bosu35
        
        show raimon2 at vshake
        show ju at vshake
        show to at vshake

        ta "「Fugeh! 」"
        "Juuichi performs a one-armed shoulder throw.{p}Tatsu-nii isn't going to be moving for a while."

        show ju 003 with dis

        ju "「Oops, those were just my reflexes... 」"

        show ko 004 at midleft with wipe_right

        ko "「Mmhm, he's been completely flattened... 」"

        "......"

        scene raimon2 with wipeleft

        "After a few minutes Tatsu-nii woke back up,\nbut had not yet sobered up,\nas his eyes still looked the same."

        show su 004 at center with wipeleft

        su "「I-I'll just take Tatsuki-san...{p}\ \ outside to rest for a bit. 」"

        hide su with wipe_right

        "Shun-kun pushes at the side of Tatsuki-san's waist,\nand takes him outside of the restaurant."

        show to 007 at center with wipeleft

        to "「Damn, Tatsu-nii was really gettin' me confused,\n\ \ his hands were all over my chest. 」"

        show si 001 at midright with wipeleft

        si "「He seemed to have been considerably drunk. 」"

        show ju 003 at farright behind to with wipeleft

        ju "「Anyway, I'm confiscating all the alcohol.{p}\ \ If he drinks anymore,\n\ \ it's only gonna get worse. 」"

        show ky 001 at farleft behind to with wipe_right

        ky "「Emergency level 1, or something like that.{p}\ \ To sober up, he had better drink some tea. 」"

        show so 001 at midleft with wipe_right

        so "「We have to keep early prevention in mind! 」"

        scene raimon2 with wipe_right
        show to 006 at center with dis

        to "「Jeez, if those two were alone,\n\ \ I don't think the outcome would be pretty. 」"
        "With that finally over,\neverbody gives a sigh of relief."
        "Still, he really changes when he's that drunk...{p}Is that really emergency level 1?"
        "But, as they say,\nall's well that ends well."

        show ko 001 at farright with wipeleft

        ko "「Hey, I have a question,\n\ \ is it all right to leave Shun-kun,\n\ \ out there alone with Tatsu-nii? 」"

        show to 005 with dis

        to "「Ah. 」"

        show ky 001 at farleft behind to with wipe_right

        ky "「This is bad... 」"
        "Everybody looks towards the entrance in unison."
        "The next moment,\nShun-kun's cry resounds throughout the restaurant."

        su "「Hiyaaaaaa!!{p}\ \ Stop it, Tatsuki-san!!{p}\ \ I pee from there!! 」"

        scene raimon2
        show to 006 at center
        with wipe_right

        to "「H-hey!{p}\ \ We have to stop Tatsu-nii!! 」"
        "It seems a big scene is about to happen..."

        scene black with wipeleft
        pause .2
        scene raimon2 with dis

        "About 10 minutes pass...{p}Saved by a desperate tackle,\nShun-kun escapes the danger."
        "Then, Tatsu-nii received Juuichi-san's...{p}iron judgement for the molestation of a minor."
        "Tatsu-nii was stunned for a while,\nthen a few minutes later,\nhe got up as if nothing happened."
        "Now he's back sitting with everybody,\nand in a good mood."

        show to 006 with wipe_right

        to "「Jeez, Tatsu-nii can be annoying...{p}\ \ He comes in out of the blue,\n\ \ and fills himsef up with yakiniku. 」"
        fn "「I wonder what would've happened...{p}\ \ if you didn't land that finishing blow. 」"

        show to 001 with dis

        to "「Oh no. 」"

        show to 007 with dis

        to "「Our conversation of the meet,\n\ \ was interrupted about half-way. 」"
        to "「As for what would've happened,\n\ \ it would have been interesting. 」"
        fn "「Ahaha, it was a chance to save the day.{p}\ \ Is everyday like this for you guys? 」"

        show to 001 with dis

        to "「No way, you came back today,\n\ \ don't you expect there to be some tension? 」"
        "After Juuichi-san's physical abuse,\nand Tatsu-nii's drunken fiasco,\neverybody returns to normal."
        "I've been living in the city for so long,\nthis gave me a new feeling of nostalgia."
        "I'd say it's the calm,\ncarefree way of life,\nbut Minasato is definitely different from the city."
        fn "「Anyway...{p}\ \ You're going to be in a national swim meet... 」"
        fn "「Torahiko, you're helping at the inn,\n\ \ and you still have to study, too!{p}\ \ Not only that, but you still have to work out. 」"
        fn "「That's a lot to deal with, isn't it? 」"

        show to 002 with dis

        to "「No, ahahaha!{p}\ \ I don't think it's that much! 」"

        show ju 001 at farright behind to with wipeleft

        ju "「Have you been studying? 」"

        show to 011 with dis

        to "「Guh... don't bring that up, senpai. 」"
        ju "「The 2nd year's Summer vacation,\n\ \ involves a lot of homework.{p}\ \ Don't cry about it and run away when it's over. 」"

        show to 003 at jump_up

        to "「I-it's okay!{p}\ \ I've got everything perfectly planned out! 」"
        fn "「Didn't you say that every year...{p}\ \ in elementary school? 」"

        show to 007 with dis

        to "「Guh... 」"
        ju "「Grow out of copying other's homework,\n\ \ it's irresponsible to say the least. 」"

        show to 002 with dis

        to "「Ha, hahaha! Summer vacation has just begun.{p}\ \ If you only think about the future,\n\ \ you won't get started with anything! Hahahaha... 」"
        "Torahiko gives a dry smile and laugh."
        fn "「Mm-hm, he's taken a defiant attitude... 」"

        show ju 003 with dis

        ju "「Looks like this year isn't going to be good. 」"
        to "「Hahahahahaha! Hahaha...{p}\ \ {nw}"
        show to 007 with dis
        extend "Haaa... 」"

        "Torahiko is completely down,\nand lets out a big sigh."
        "His keen ears are down,\nand his whiskers are drooping."
        "I fill up my plate with meat and vegetables,\nand place it in front of Torahiko."
        fn "「You've slowed down eating.{p}\ \ Here, eat some meat. 」"
        to "「[fn]... 」"
        fn "「It's okay that you're only thinking,\n\ \ about the swim meet right now.{p}\ \ You need the nutrition. 」"

        show to 002 with dis

        to "「O-oh yeah!{p}\ \ All right then, I'm gonna eat and eat and eat!{p}\ \ So that I'll definitely win! 」"

        show to ray 01 with dis

        "Torahiko fills up his bowl with rice,\nand starts shoveling in meat,\nand vegetables with amazing vigor."
        fn "「I think his bad mood is gone,\n\ \ he's completely fine now... 」"

        show ju 002 with dis

        ju "「It's because he's a simple guy.{p}\ \ He's the type of person who can...{p}\ \ change their mood very quickly. 」"
        fn "「I see. 」"

        show ju 001 with dis

        "At first I was surprised at how...{p}different he looked since elementary school."
        "But talking to him like this makes me feel,\nas if I've gone back to the way things...{p}used to be in Minasato Village."
        "His endless cheer and simple character,\nTorahiko hasn't changed at all."

        show to at jump_up

        to "「I'll be fine with just swimming and cooking!!{p}\ \ Just get rid of the homework!! 」"
        fn "「You're still...{p}\ \ dragging your feet about that... 」"

        show ju 003 with dis

        ju "「Half his food is already gone... 」"
        "Still just a little childish as ever...{p}Well, I'll just have to see what happens."

        jump party_end
        
    #######################################
    label party_end:
        $ event_name = _("The Party in Full Swing")

        stop music fadeout 3
        scene black with Dissolve(2)        
        pause 2
        scene raimon2 with circle_out
        play music free02 fadein 3

        fn "「Whew, my stomach's full.{p}\ \ I can't eat another bite... 」"

        show to 001 at center with wipe_right

        to "「I ate and ate...{p}\ \ It was just meat but there sure was a lot,\n\ \ and then there was also dessert. 」"

        show ky 001 at farright behind to with wipeleft

        ky "「Well, this looks like a good time\n\ \ to wrap things up. 」"

        show so 001 at midright with wipeleft

        so "「Uh-huh! 」"

        show su 002 at midleft with wipeleft

        su "「I had a lot of fun today. 」"
        fn "「Yeah, it was nice to see you guys,\n\ \ after such a long time. 」"

        show to 007 with dis

        to "「Today isn't the only day you're having fun!{p}\ \ You're here all Summer vacation,\n\ \ let's meet every single day! 」"

        show ju 001 behind to at farleft with wipeleft

        ju "「...Meet every single day? 」"

        show to 002 with qdis

        to "「It's a figure of speech.{p}\ \ A. Figure. Of. Speech. 」"

        scene raimon1
        show ta 001 at center
        with wipeleft

        ta "「Well, we played every day back then.{p}\ \ We liked to play baseball or go fishing,\n\ \ or do things like have a game of tag. 」"

        show to 002 at farright with wipeleft

        to "「That's right! Why don't we have...{p}\ \ a game of tag sometime?{p}\ \ Even better, we could do it all day long! 」"
        to "「We could call it \"24-Hour Tag Endurance\"! 」"
        fn "「A 24-hour game of tag? All day? 」"

        show to 001 with dis

        to "「Yep, I think it's worth a try.{p}\ \ It won't be over until everybody's caught! 」"

        scene raimon2
        show ka 005 at midright
        show si 001 at midleft
        with wipeleft

        ka "「I think we're a little too old...{p}\ \ to be playing tag. 」"
        si "「It's ridiculous... 」"

        show ta 001 behind ka with wipeleft

        ta "「Don't say that, it could be fun. 」"
        ta "「You aren't allowed to use any vehicles,\n\ \ and you can hide anywhere in Minasato.{p}\ \ Do those sound like good rules? 」"

        show ka 001 with dis

        ka "「If that's the case...{p}\ \ the area around my house should be the boundary. 」"

        show si 002 with dis

        si "「Then it would be good to hide in my house.{p}\ \ However, that would make things too simple and easy. 」"
        "Those two were just complaining,\nand now they're eager to join in..."

        scene raimon2 with wipe_right
        show ky 001 at center with wipeleft

        ky "「But wouldn't it be troublesome to do that,\n\ \ all day in the middle of Summer? 」"

        show ju 001 at farright behind ky with wipeleft

        ju "「That's not very realistic. 」"

        show so 003 at midleft with wipeleft

        so "「It's Summer, so shouldn't we do...{p}\ \ something Summer-ish? 」"

        show su 002 behind so at farleft with wipeleft

        su "「Before [fn]-san moved,\n\ \ we would go bug-catching or fishing! 」"
        "Shun-kun holding a bug-catching net,\nand wearing a straw hat..."
        "That would be suitable for him.{p}But, that's not really something\na high school student would do..."
        ky "「No, that's a little... 」"

        scene raimon2 with wipe_right
        show ko 001 at center with wipeleft

        ko "「Hmm, something Summer-ish.{p}\ \ How about we all go to the beach? 」"
        fn "「That sounds great! 」"

        show to 002 behind ko at midright with wipe_right

        to "「Kounosuke suggested something normal for once,\n\ \ that's rare! 」"

        show ko 005 with dis

        ko "「What? I'm always normal...{p}\ \ {nw}"
        show ko 004 with dis
        extend "A 24-hour game of tag sounds pretty stupid. 」"

        show to 003 with dis

        to "「What!? 」"

        show ju 001 at farleft with dis

        ju "「...I don't think that sounded so bad. 」"

        show ta 001 behind to at midleft with wipe_right

        ta "「Hm, Juuichi? Did you say something? 」"

        show ju 003 with qdis

        ju "「No, it's nothing... 」"

        show ta 002 with dis

        ta "「So then, the next thing to do is go to the beach. 」"
        ta "「I have work, and you guys are busy,\n\ \ so it would be convenient\n\ \ to go on everybody's next day off. 」"
        ta "「We'll work out the details eventually. 」"

        show to 001 with dis

        to "「All right, we'll try that. 」"

        show ko 002 with dis

        ko "「I agree! 」"

        scene raimon1 with wipe_right
        show so 001 at center with wipeleft

        so "「The beach, huh?{p}\ \ I've got a bathing suit! 」"

        show su 002 behind so at midright with wipe_right

        su "「Woof! I'm excited! 」"

        stop music fadeout 3
        show ky 001 behind so at midleft with wipe_right

        ky "「So it's decided.{p}\ \ Then we have just one\n\ \ last thing to do before we end today. 」"
        fn "「What do you mean? 」"

        show to 002 big at center_big with wipe_right

        to "「One... two... 」"

        scene raimon2

        "{size=+15}「WELCOME HOME, [fn]! 」"

        play music free31
        $ renpy.music.set_volume(1.0, 0.0, channel = "music")
        pause 1.5

        "Aah, I've really come back to Minasato Village...{p}To my friends who are so warm."
        fn "「I'm back, everyone!{p}\ \ Thanks for today! 」"
        "I was born and raised in this village,\nand I met everyone here, too.{p}It feels really great."

        show to 002 at center with wipeleft

        to "「Heh heh, don't cry! 」"
        fn "「Yeah, I'm not crying. 」"

        show ta 002 behind to at farleft with wipe_right

        ta "「Things have gotten sappy here,\n\ \ but the next time we meet at the beach,\n\ \ we'll be excited. Don't forget! 」"

        show si 002 behind to at farright with wipeleft

        si "「But you're the best at forgetting things. 」"

        show ta 006 with dis

        ta "「Shin, don't say such things. 」"
        fn "「Ahahaha! 」"

        scene raimon2 with Dissolve(2)

        "For the next month,\nI'll be in Minasato Village with everybody."
        "Not only are we going to the beach,\nI'm sure there are plenty of other things in store."
        "Inside my chest,\nmy heart is like an album."
        "When I open it,\nmy memories shine like brilliant jewels."
        "There I can make a new page.{p}This year's Summer only happens once.{p}So, I'll enjoy it as much as I can."
        
        stop music fadeout 2
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

        jump day02




    return
