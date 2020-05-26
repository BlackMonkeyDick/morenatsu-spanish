## Day 7

screen busstop07:
    hbox:
        add "arrow down"
        at busbounce1
    hbox:
        add "icon_juu"
        at busbounce3
    hbox:
        add "icon_sou"
        at busbounce4
    hbox:
        add "icon_kyou"
        at busbounce5
    hbox:
        add "icon_shun"
        at busbounce6
    hbox:
        add "icon_shin"
        at busbounce2
    hbox:
        add "icon_kouno"
        at busbounce7
    hbox:
        add "icon_kouya"
        at busbounce8
    hbox:
        add "icon_tatsu"
        at busbounce9
    hbox:
        add "icon_tora"
        at busbounce10 
    hbox:
        text _("Bus Stop")
        xalign .8 yalign .38

screen minasatomap07():
    add "map"
    add "mapdate"
    imagebutton idle "a icon" hover "icon loop" xpos 583 ypos 165 action Jump("beach07_meetup") hovered Show("busstop07")  unhovered Hide("busstop07") hover_sound "av/audio/click_008.wav"
    hbox:
        text _("{size=+30}August 7")
        at maptime

##########################################
label day07:    
    
    $ renpy.music.set_volume(1.0, 0.0, channel = "music")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound2")

    $ focus_character = ""
    $ event_name = _("８月7日")
    
    scene hbroom with wipeleft
    
    fn "「Whew... Another day is over.{p}\ \ I can't believe how busy I've been since I got here. 」"
    
    play music [ "<silence .3>",   phone_ring]
    pause 1

    gm "「[fn]-chan, can you get the phone?{p}\ \ I'm busy in the kitchen right now. 」"
    gp "「And I'm too busy watching baseball. 」"
    fn "「Haah, I guess I have to do it...{p}\ \ Okay, I'll get it. 」"
    
    scene hentry night with dis 

    "I used to have to answer the\nphone like this all the time."
    
    stop music
    play sound phone_pickup
    
    fn "「Hello? 」"
    
    ################# Will replace code below with affection checker later
    
    $ affectionlist = [love_tatsuki, love_kounosuke, love_shun, love_kouya, love_shin, love_juuichi, love_soutarou, love_kyouji, love_torahiko]
    $ namelist = ["tatsuki", "kounosuke", "shun", "kouya", "shin", "juuichi", "soutarou", "kyouji", "torahiko"]
    $ selection = affectionlist.index(max(affectionlist))
    $ favorite = namelist[selection]
    
    if favorite == "torahiko":
        jump beach07_invite_tatsuki
    elif favorite == "kyouji":
        jump beach07_invite_soutarou
    else:
        $ renpy.jump ("beach07_invite_" + favorite)    
    

#############################################
label beach07_invite_tatsuki:
    
    $ event_name = _("Phone call from Big Bro Tatsuki")
    
    ta "「Yo, [fn]. You know who this is?{p}\ \ It's Tatsu-nii! 」"
    fn "「Yeah, I could tell it was you. 」"
    ta "「You know about the beach party, right?{p}\ \ The one we talked about at your welcoming party? 」"
    ta "「Well, sorry it's so sudden,\n\ \ but we're going tomorrow...{p}\ \ Is that all right with you? 」"
    fn "「Eh!?{w=.3} Tomorrow!?{p}That's all right, but...{p}It is very sudden... 」"
    ta "「Well, with everybody's club activities,\n\ \ I was thinking about it. 」"
    ta "「I figured tomorrow would be just the right time.{p}\ \ I don't know if we'll get another day like this. 」"
    fn "「Yeah, I understand.{p}\ \ It's tough getting us all together. 」"
    ta "「Okay then, here's the plan:{p}\ \ We're meeting at the bus stop tomorrow at 7.{p}\ \ Don't oversleep, or you'll get left behind! 」"
    fn "「Be careful not to do that yourself! 」"
    ta "「Gahahaha! There's no way I'd do that!{p}\ \ See you tomorrow. 」"
    fn "「Yeah, tomorrow. Seeya! 」"
    "Boop. Boop. Boop."
    "All right, I'll get ready right away!"
    
    jump beach07_packing

#########################################  
label beach07_invite_kounosuke:
    
    $ event_name = _("Phone call from Kounosuke")

    ko "「Hello. Is this [fn]-kun? 」"
    fn "「Kounosuke? 」"
    ko "「Ah, yeah. [fn]? 」"
    fn "「Yep, what's up? 」"
    ko "「Do you remember what we talked about earlier?{p}\ \ You know, at the welcoming party? 」"
    fn "「Err... 」"
    ko "「Come on? Don't you remember?{p}\ \ We were all talking about the beach party? 」"
    fn "「Uh... We did talk about that... 」"
    ko "「Yeah, the date's been decided.{p}\ \ It's tomorrow. 」"
    fn "「Ah, tomorrow!? 」"
    ko "「Yeah. Everybody has their club activities,{p}\ \ so it wasn't easy to find a good time. 」"
    ko "「So if we don't do it tomorrow,{p}\ \ who knows when the next time could be. 」"
    fn "「I see... 」"
    ko "「So that's why,{p}\ \ that's what I was told.{p}\ \ See you later! 」"
    fn "「W-wait a minute, Kounosuke! 」"
    ko "「What? 」"
    fn "「When and where are we meeting tomorrow? 」"
    ko "「Oh! I forgot...{p}\ \ Hmm... we're meeting at...{p}\ \ ...at the bus stop at 6:30, I think. 」"
    fn "「In the morning? 」"
    ko "「Yes. 」"
    fn "「Understood.{p}\ \ Tomorrow at 6:30,{p}\ \ meet at the bus stop. 」"
    ko "「Yep. See you tomorrow then.{p}\ \ Bye! 」"
    fn "「Yeah, bye. 」"
    
    play sound call05
    pause .2
    play music [ "<silence .3>",   call00]

    "Boop boop boop."
    
    stop music

    "Tomorrow morning?{p}Hmm, when should I wake up?{p}I better get up as early as possible to get ready."

    jump beach07_packing
    
#########################################
label beach07_invite_shun:
    
    $ event_name = _("Phone call from Shun")
    
    who "「Good evening, is this the [ln] residence? 」"
    fn "「Yes, it is...{p}\ \ Is that you, Shun-kun? 」"
    su "「Yes! This is Shun!{p}\ \ [fn]-san, good evening. 」"
    fn "「Good evening to you too, what's up?{p}\ \ Is there something you need? 」"
    su "「Yes there is!{p}\ \ The other day at the welcoming party,{p}\ \ we were talking about going to the beach. 」"
    fn "「Oh yeah, we did!{p}\ \ Have we decided on a plan? 」"
    su "「Umm, err...{p}\ \ Tomorrow, but if that's... 」"
    "He murmurs an apology in a low voice.{p}Then he tells me they're planning,{p}on going in less than half a day."
    "I'm surprised."
    fn "「Huh!?{p}\ \ Tomorrow!? Tomorrow as in the 7th!?{p}\ \ The tomorrow that will come if I go to sleep? 」"
    su "「Yeah...{p}\ \ it's hard to get everybody's schedules to match up,{p}\ \ so we talked about different times and decided that..."
    su "Tomorrow is best... 」"
    su "「[fn]-san, will you please go...? 」"
    "I'm not so fickle,{p}that I would turn down your earnest request,{p}Shun-kun."
    "Fufufu, don't worry.{p}This is my chance to be a big brother!"
    fn "「Of course! That's fine! 」"
    "I give my reply,{p}and I hear the sound of relief and joy.{p}on the other end of the line."
    su "「Woof! That's good... I'm happy,{p}\ \ everybody's going! 」"
    "Judging by his excited tone,{p}I'm sure his tail is wagging at full throttle."
    "Fufufu, I love making him worry at first,{p}and then making him happy!"
    fn "「Yeah, I'm going because it's been so long. 」"
    su "「The time and place we're meeting is... umm...{p}\ \ 7 in the morning at the bus stop. 」"
    fn "「Mm-hm. 」"
    su "「You should bring your bathing suit,\n\ \ and stuff to play with. 」"
    fn "「I see. It feels like\n\ \ you've been putting a lot of effort\n\ \ into planning everything out! 」"
    su "「S-sorry... 」"
    fn "「There's no need to apologize!{p}\ \ This is a little exciting!{p}\ \ It's like we're kids again, isn't it? 」"
    su "「Th-that's right. 」"
    fn "「All right then,\n\ \ we're meeting at the bus stop tomorrow at 7. 」"
    su "「Yes! 」"
    "He methodically reapeat the time,\nmeeting spot, and what I need to bring."
    "Excited and in high spirits,\nShun-kun hangs up the phone.{p}Well, I better start packing."
    
    jump beach07_packing

########################################
label beach07_invite_kouya:
    
    $ event_name = _("Phone call from Kouya")
    
    ka "「Yo, [fn]. It's me. 」"
    fn "「Huh, Kouya? What are you calling for? 」"
    ka "「Well, back at your welcoming party,\n\ \ everybody was talking about going to the beach...{p}\ \ You remember? 」"
    "I try to remember what we talked about.{p}Yeah, we did discuss that."
    fn "「Oh yeah, I remember. 」"
    ka "「About that, sorry if it's on such short notice...{p}\ \ But would tomorrow be okay? 」"
    "An apologetic voice comes from the phone."
    fn "「Tomorrow?{p}\ \ Well, that should be all right,\n\ \ but why tomorrow? 」"
    ka "「Ah, if you think about everybody's plans,\n\ \ then this is when it's most convenient. 」"
    ka "「If we miss tomorrow, I don't know\n\ \ when the next time could be,{p}\ \ so we have to do it then. 」"
    fn "「Oh, I see.{p}\ \ Yeah, sounds good. 」"
    ka "「I'm really sorry for being so sudden. 」"
    fn "「No, you don't need to apologize.{p}\ \ Have you decided on a meeting time? 」"
    ka "「Uh, tomorrow morning at seven.\n\ \ we're meeting at the bus stop. 」"
    ka "「There's nothing specific that you need,{p}\ \ so bring whatever you want. 」"
    fn "「Yeah, got it.{p}\ \ I'll see you tomorrow. 」"
    ka "「Yeah, see ya. 」"
    "*Click*{p}I hang up the phone."
    "So, it's tomorrow.{p}Even though it was so sudden,\nI'm somehow already excited."
    "Okay, I have to start preparing right away."
    
    jump beach07_packing

###########################################
label beach07_invite_juuichi:
    
    $ event_name = _("Phone call from Juuichi")
    
    ju "「Hello, this is Mikazuki speaking.{p}\ \ Is [fn]-kun home? 」"
    "I hear Juuichi-san's voice from the phone.{p}His tone seems somewhat higher than usual."
    fn "「Oh, Juuichi-san, this is [fn].{p}\ \ Good evening. 」"
    "Juuichi-san always uses honorifics\nwhen speaking to me."
    "His respectful way of talking\nis kind of embarrassing."
    "While I'm thinking about that,{p}Juuichi-san greets me."
    ju "「...[ln].{p}\ \ I'm sorry for calling at a time like this. 」"
    fn "「No no, that's all right.{p}\ \ What do you need? 」"
    ju "「Ahem... 」"
    "Juuichi-san lightly clears his throat."
    ju "「A few days ago, at your welcoming party,\n\ \ do you remember talking about going to the beach? 」"
    fn "「I remember. 」"
    ju "「Well, we were planning on going, but... 」"
    fn "「Is that right? Sounds fun.{p}\ \ ...When are you going? 」"
    ju "「...Um. Tomorrow. 」"
    fn "「All right, tomorrow it is.{p}\ \ ...{p}Tomorrow!? 」"
    "I accidently yelled that out loud.{p}Going to the beach would be fun,\nbut isn't that kind of soon?"
    ju "「...Sorry. Tomorrow is the only time\n\ \ everybody will be able to go. 」"
    "Juuichi-san's tone is apologetic.{p}That's right, they have their club activites,\nsupplementary lessons, and other stuff."
    "Tomorrow...{p}I don't have anything important to do,\nso I readily agree."
    ju "「I see. 」"
    "It could be my imagination,\nbut Juuichi-san's voice sounds more lively."
    ju "「We're meeting at the bus stop at 7 tomorrow. 」"
    ju "「You only need to bring the essentials.{p}Your swimsuit, towel, and sandals...{p}Things like that. 」"
    ju "「...Do you have any questions? 」"
    fn "「No, I'm fine. 」"
    ju "「I understand...{p}See you tomorrow, then. 」"
    fn "「Yeah, good night. 」"
    
    play sound call05
    
    "I hang up the phone.{p}Immediately, I return to my room to prepare."
    "Everybody at the beach...{p}I can hardly wait."
    "Thinking about tomorrow,\nI involuntarily start smiling."
    "...Ah.{p}Grandpa and I meet eyes\nas he's on his way to the bathroom."
    "He stares at me as though\nhe had just seen something weird."
    fn "「I-it's nothing! 」"
    "Oh, that was embarrassing...{p}I run to my room."
    
    jump beach07_packing

########################################
label beach07_invite_shin:
    
    $ event_name = _("Phone call from Shin")
    
    si "「Hello, this is Kuroi. 」"
    fn "「Oh, Shin-kun? 」"
    si "「[fn]? 」"
    fn "「Yeah. This is unusual.{p}\ \ A call from Shin-kun. 」"
    si "「Really? 」"
    fn "「Just a little.{p}\ \ So, what do you need? 」"
    si "「I'm sure you remember talking about going\n\ \ to the beach some time ago.{p}\ \ At the welcoming party...? 」"
    fn "「Oh yeah. Now that you mention it, I do. 」"
    si "「I'm calling to tell you the plan.{p}\ \ Tomorrow morning at 7,{p}\ \ we're meeting at the bus stop. 」"
    fn "「Huh? Tomorrow morning at 7? 」"
    si "「I was just told that a few moments ago.{p}\ \ I think it's too sudden... But it must\n\ \ be the only convenient time for everybody else. 」"
    fn "「Oh, tomorrow, huh. That is kind of sudden. 」"
    si "「What are you going to do?{p}\ \ If that's unreasonable,\n\ \ I'll go ahead and tell everybody. 」"
    fn "「I-I'm going, I'm going. I'll go!{p}\ \ Shin-kun, stop making me sound so cold. 」"
    si "「That's not it... 」"
    "It sounds like he's mumbling something,\nbut I can't hear it very well."
    fn "「Shin-kun? Sorry, I can't hear you. 」"
    si "「Never mind.{p}\ \ Anyway, there's not much you need to do to prepare.{p}\ \ Tomorrow morning at 7, meet at the bus stop. Okay? 」"
    fn "「Yeah. Understood. 」"
    si "「See you then. 」"
    "*Click*{p}Boop boop boop."
    "Tomorrow, huh?{p}Well then, I need to start getting ready now."
    
    jump beach07_packing

#######################################
label beach07_invite_soutarou:
    
    $ event_name = _("Phone call from Soutarou")
    
    who "「Good evenin'! Is this [ln]-san? 」"
    "Ah, that way of talking, it's..."
    fn "「Could this possibly be Soutarou-kun? 」"
    so "「Oh, yep! Ehehe, [ln]-san,{p}\ \ you knew who it was just from my voice. Amazin'! 」"
    fn "「No no, that's... 」"
    "It's not that I'm amazing,{p}there's just a certain characteristic about him..."
    fn "「So, what do you need today?{p}\ \ You need to report something? 」"
    so "「Ah, yeah! Umm...{p}\ \ at your welcoming party the other day..."
    so "Everybody was talkin',{p}\ \ about goin' to the beach... 」"
    fn "「Oh, I remember that too. 」"
    so "「Yeah... seems they we're in...{p}\ \ a hurry and decided to go tomorrow. 」"
    fn "「What?! T-tomorrow!? 」"
    so "「Yep. Thinkin' about the others' schedules,{p}\ \ they won't match up if we don't do it tomorrow. 」"
    fn "「I see, when you put it like that... 」"
    so "「So... is tomorrow okay with you...? 」"
    fn "「Oh, of course tomorrow is okay. 」"
    so "「Really!? That's great! 」"
    "Soutarou-kun's voice gets loud,{p}when he hears that I'm going."
    so "「Ah... sorry about that.\ \ I get a little nervous about...{p}\ \ goin' on field trips like this... 」"
    fn "「Ahaha, you're right.{p}\ \ It is like a field trip. 」"
    fn "「So where are we meeting? 」"
    so "「Umm, the bus stop at 7 AM! 」"
    fn "「Got it. Thanks for telling me.{p}\ \ Soutarou-kun, make sure to get plenty of sleep, okay? 」"
    so "「Th...thank you very much!{p}\ \ Now, if you'll excuse me! G'night 」"
    fn "「Yeah. Good night. 」"
    "Finished talking, I hang up the phone."
    fn "「Before going on a field trip... 」"
    "When I hear field trip, I suddenly remember,{p}when I used to live in this village."
    "I haven't gone on a trip like this,{p}with everybody since elementary school."
    fn "「...Okay! Let's finish preparing for tomorrow. 」"
    "I quickly get back to my room."
    
    jump beach07_packing

#######################################
label beach07_packing:
    
    $ event_name = _("Did I forget anything?")
    
    scene hbroom with sdis
    play music free0211
    play sound packing loop
    
    "Let's see...{p}We're probably going swimming,\nso I'll bring my swim trunks, and my sandals."
    "Oh, I don't have goggles...{p}But they sell those at the 100 yen shop.\nI'll just buy them there."
    "I wonder if I should get a swim ring,\nor something like that..."
    
    stop sound
    
    fn "「Grandma, I'm going to the beach tomorrow.{p}\ \ Do we have like a beach ball or something? 」"
    gm "「I wonder where it is...{p}\ \ If I remember correctly,\n\ \ your father had one. 」"
    gm "「At least, I think he had one... 」"
    "If Dad did use one,\nit'll be from 10 or 20 years ago..."
    fn "「Oh, you don't need to get it,\n\ \ I was just curious.\n\ \ I'm sure everybody else will have them. 」"
    gm "「Are you sure?{p}\ \ Guess I don't have to get it out. 」"
    "Even if they don't have plenty,\nit'll be fine as long as somebody brings one..."
    fn "「Thank you, though. 」"
    "Even if there's something I don't have,\nthey'll probably have it at the beach store."
    "So there, that's enough packing.{p}I need to get to bed early for tomorrow."
    
    stop music fadeout 1
    scene black with Dissolve(1)
    
    $ day = 7
    $ the_date = "August 7"
    window hide
    
    scene sky01 
    show text "{size=+130}August 7" at truecenter
    with Dissolve(.5)

    pause 3
    scene black with Dissolve(1)
    pause .4
    
    play music [ "<silence .3>",   birds_chirping]
    scene hbroom with Dissolve(.5)

    "Huh... It's morning already?{p}What time is it?{p}5:53 AM..."
    "I set my alarm for 6,\nbut I got up earlier than that."
    "Why is it whenever I go on a trip,\nI always wake up early?{p}Strange..."
    fn "「Good morning. 」"
    gm "「Good morning. I got up early myself. 」"
    gp "「You're up early.{p}\ \ You're usually sleeping like a log at this hour. 」"
    "Old people sure do get up early...{p}I wonder if that means that I'm an old man..."
    gm "「Go wash your face.{p}\ \ I'll make you something to eat. 」"
    fn "「Okay... 」"
    "Everybody else is probably still asleep."
    fn "「Thanks for breakfast. 」"
    "Well, it's a little early,\nbut I'll go to the bus stop.{p}I can't wait anymore!"
    fn "「All right, I'm leaving now. 」"
    gm "「Oh, heading out so soon? 」"
    gp "「All right, be careful. 」"
    fn "「See you later. 」"
    
    play music free0203
    call screen minasatomap07
    
###########################################
label beach07_meetup:
    
    $ event_name = _("Everyone Assemble")
    scene map
    hide screen busstop07
    scene bstop with wipe_right

    "Early in the morning, I hurry to the bus stop.\nIt doesn't look like everybody's here yet..."
    fn "「That person over there...\n\ \ Is that...? 」"

    show ju 001 at center with wipe_right
    
    ju "「...[ln].{p}\ \ You're here very early.{p}\ \ Isn't there plenty of time? 」"
    fn "「Good morning.{p}\ \ I guess I woke up kind of early. 」"
    fn "「Besides, now you don't have to wait\n\ \ for me to get here. 」"
    fn "「You're early, too. 」"
    ju "「I get up early most days,\n\ \ since I have training. 」"
    fn "「Heh, so you're an early riser. 」"
    "Amazing."
    "If that's the case,\nKyouji and Torahiko probably have to get up\nearly for their clubs, too."
    "...Although waking up early doesn't suit Torahiko."
    fn "「By the way, Juuichi-san,\n\ \ it looks like you brought a lot of stuff. 」"
    "I noticed it when I first saw him."
    "Juuichi-san has a backpack that's almost\nthe same size as his body.\nIt's stuffed full, and clinging to his back."
    "Do you think he'd say anything\nif I messed with it?"
    
    show ju 008 with dis
    
    ju "「...Oh, this.{p}\ \ I think it's something I should bring,\n\ \ if we're going to the beach. 」"
    fn "「Isn't that a lot? 」"

    show ju 003 with dis
    
    ju "「Isn't this how much you'd usually bring? 」"
    "If he says so, then it must be."
    fn "「But I don't have any goggles... 」"

    show ju 001 with dis
    
    ju "「If I have to...{p}\ \ I'll let you borrow a spare. 」"
    
    play sound packing

    "From a parasol to a straw mat, he has everything.{p}He even has enough goggles for everybody...{p}Is there a reason why?"
    "But will I be able to use Juuichi-san's spare?{p}I hope they're normal ones,\nbut they'll slip off if they're made for beastmen."
    
    hide ju with wipe_right
    show ka 001 at center with wipe_right

    ka "「Looks like you guys got here early. 」"
    fn "「Oh, Kouya.{p}\ \ Good morning.{p}\ \ You're early, too. 」"

    show ka 002 with dis
    
    ka "「I wouldn't have been on time,\n\ \ if I didn't get here early. 」"
    who "「Good morning.{p}\ \ It's unusual for you to be early.{p}\ \ I hope it doesn't rain. 」"
    
    show si 001 at midright with wipe_right

    fn "「Good morning, Shin-kun.{p}\ \ I like to get up early for trips.{p}\ \ That's why. 」"

    show si 004 with dis
    
    si "「You still have some growing up to do. 」"
    fn "「That's... 」"

    show si 002 with dis
    
    si "「I'm just joking.{p}\ \ It's natural that you'd get here early. 」"

    show si 001 with dis
    
    si "「...Of course, it's not surprising,{p}\ \ that some people are going to be a pain,\n\ \ and get here late. 」"
    "Shin-kun sure is talkative today.{p}He must be in a good mood."
    
    hide ka
    hide si
    with wipe_right
    
    show ju 001 at midright with wipe_right

    ju "「Looks like more people are showing up. 」"

    show ta 009 at midleft with wipe_right
    
    ta "「Whoa whoa whoa whoa, there're more here than\n\ \ I thought there would be! 」"
    fn "「Morning, Tatsu-nii.{p}\ \ You're looking good today. 」"

    show ta 002 with dis
    
    ta "「Good morning, [fn]! 」"
    ta "「Look at what's happened!{p}\ \ A carpenter's work begins before the sun rises.{p}\ \ So it was easy for me to get up today. 」"
    
    hide ta
    hide ju
    with wipe_right
    
    show ky 001 at farright
    show so 001 at center
    show su 001 at midleft
    with wipe_right

    ky "「Good morning.{p}\ \ I could hear Tatsuki-san's voice\n\ \ from all the way over there. 」"
    ky "「So I already knew that you guys\n\ \ were gathering before I arrived. 」"

    show so 003 with dis
    
    so "「Everybody is so early! 」"

    show su tailwag 01 with dis
    
    su "「Good morning everybody! 」"
    fn "「Good morning. 」"
    "Shun-kun politely bows his head,\nand I straighten up to greet him."
    
    show ta 002 at farleft behind so with wipe_right

    ta "「Oh, good morning.{p}\ \ Hang on, there's another person\n\ \ hiding behind Kyouji, isn't there? 」"
    su "「Yeah, he came over and got me. 」"
    ky "「It's the same direction from Tarou's house,{p}\ \ so he came along with us today. 」"

    show ta 001 with dis
    
    ta "「I see, good for Shun. 」"

    show su 002 with dis
    
    su "「Yep. 」"
    
    hide ta
    hide su
    hide so
    hide ky
    show ka 005 at center
    with wipe_right

    ka "「...Speaking of getting somebody,\n\ \ are they going to get here soon?{p}\ \ It's almost time to go. 」"

    show ky 001 at farright with wipe_right
    
    ky "「Ooshima should be fine,\n\ \ but I don't know about Kounosuke... 」"

    show ju 001 at farleft with wipe_right
    
    ju "「If I remember correctly,\n\ \ Tora was going to go get him,\n\ \ to make sure he isn't late. 」"
    "Come to think of it,\nKounosuke's house is the closest\nto Ooshima Inn..."
    "Hm?"
    to "「Hey, hurry up!{p}\ \ Can't you run any faster? 」"
    ko "「I'm running!{p}\ \ There's no need to rush! 」"
    "Ah, speak of the devil."
    
    hide ju
    hide ka
    hide ky
    show to 006 at center
    show ko 005 at farleft
    with wipe_right

    to "「Hah...{p}\ \ Hah, I finally made it... 」"
    ko "「Wheeze... Wheeze...{p}\ \ See... We didn't need to hurry... 」"

    show ky 001 at farright behind to with wipe_right
    
    ky "「What on earth happened to the pair of you? 」"

    show to 001 with dis
    
    to "「It's nothing. I just went to get him,\n\ \ and he was still eating,\n\ \ then long, long after that... 」"

    show ko 001 with dis
    
    ko "「Hahaha, sorry. There just happened to be\n\ \ something good on TV. 」"
    ko "「Also, I wanted to check over\n\ \ what I'm bringing before I left. 」"

    show to 006 with dis
    
    to "「...Didn't I tell you\n\ \ when I was going to come get you? 」"

    show ko 002 with dis
    
    ko "「Yep, I remembered exactly\n\ \ when you were coming. 」"
    
    hide to
    hide ko 
    hide ky
    show si 001 at farright
    with wipe_right

    si "「I think you should have gotten here\n\ \ earlier than the planned meeting time. 」"

    show ko 003 at midleft with wipe_right
    
    ko "「Oh really?{p}\ \ But I didn't hurry,{p}\ \ and everything's okay, right? 」"
    
    hide ko
    hide si
    show to 006 at center
    with wipe_right

    to "「Well... 」"

    show ka 005 behind to at farright with wipeleft
    
    ka "「...No matter what we say,\n\ \ he's not going to get any better. 」"

    show ta 002 behind to at farleft with wipeleft
    
    ta "「This is good, isn't it?{p}\ \ At least we got everybody here\n\ \ before the bus showed up. 」"
    ta "「You guys haven't forgotten anything?{p}\ \ The bus is here, so let's go! 」"
    
    hide ta
    hide to
    hide ka
    show so 003 at midleft
    show su 001 at midright
    with wipe_right

    fn "「Yeah! 」"
    so "「All right! 」"
    su "「Okay! 」"
    
    scene black with sdis
    pause .5
    scene bus with wipe_down_slow
    
    $ event_name = _("Let's go to the sea")

    fn "「Come to think of it,\n\ \ was there a beach around here? 」"
    ju "「There is...{p}\ \ If you go the other direction, away from Kazenari.{p}\ \ There's no other reason to go out this way. 」"
    ko "「I discovered it by chance the other day,\n\ \ so I checked it out. 」"
    su "「That's a great discovery, isn't it?{p}\ \ It's wonderful! 」"
    ky "「I'm pretty sure there's a river around here.\n\ \ It must be the source of the big river\n\ \ that flows through Minasato. 」"
    si "「Oh, I've heard of that. 」"
    ky "「In fact, the one that runs through the inner\n\ \ part of the village seems to come from the\n\ \ largest mountain in the area. 」"
    fn "「Is that so?{p}\ \ You seem to know a lot about this. 」"
    ky "「No, this is just some second-hand knowledge. 」"
    so "「But if it's in the mountains,\n\ \ what does it have to do with the sea? 」"
    ky "「Tarou, you'll understand some day. 」"
    
    play music traffic01 fadein .5
    scene bus night with Dissolve(1)

    su "「Hawawawa, it got dark all of a sudden. 」"
    ju "「Looks like we entered a tunnel. 」"
    "...{p}...{p}..."
    fn "「This tunnel sure is long. 」"
    ka "「I don't really like tunnels...{p}\ \ They make a weird sound. 」"
    fn "「I know, the air pressure feels strange. 」"
    
    stop music fadeout .5

    to "「Oh, seems like it'll be over soon.{p}\ \ Look. 」"
    
    scene white with dis
    pause 1
    play music free0203
    scene ocean with wipe_corner 
    pause .5

    fn "「Whoa, it's so blue! 」"
    "Amazing, who knew there was a place like this?{p}And we're on top of a mountain,{p}so the view is even better."
    su "「It's the ocean. 」"
    ko "「It is!{w} It's beautiful. 」"
    ka "「It's just the sea. 」"
    si "「Don't act like children... 」"
    ky "「It looks like the ocean continues on from here. 」"
    ju "「It's quite the view. 」"
    so "「It's beautiful!{p}\ \ It just appeared,\n\ \ right as we crossed over the mountain. 」"
    to "「Wow, there's a boat!{p}\ \ Hm? Is that a yacht on the other side?{p}\ \ But that thing looks so small. 」"
    ky "「I think that's windsurfing...{p}\ \ It looks fun. Would you like to try that, Tarou? 」"
    so "「Eh, what, with 2 people!? 」"
    ky "「No, did I say anything about 2 people? 」"
    so "「Eh... Aah! 」"
    "Soutarou-kun is so cute.{p}Is he like that when they're at the club?"
    ka "「It's something you usually think about\n\ \ doing when you're at the beach. 」"
    si "「I'm not interested... 」"
    su "「Oh!?{p}\ \ Look, somebody is flying! 」"
    to "「Seriously!{p}\ \ He's just coming down by parachute,\n\ \ isn't he? 」"
    ka "「What?{w} Where!? 」"
    "I'm still anxious..."
    "If that's the case,\nthen it's good that I've been meekly watching\nsince the beginning."
    ko "「It looks like parasailing,{p}\ \ the boat pulls you and you get to take\n\ \ a walk through the sky. 」"
    ko "「I'd like to try something like that today. 」"
    to "「It looks like a blast!{p}\ \ Are you going to try it, Tarou? 」"
    so "「Ah... Sure... 」"
    to "「What, you're not going to react\n\ \ any different than when Kyouji-senpai asked? 」"
    so "「Huh?{p}\ \ No, I wouldn't do somethin' like that. 」"
    ju "「Tora and I can fly together. 」"
    to "「Why!? 」"
    su "「Ahaha, that's good, Torahiko-san.{p}\ \ You've got a close friend. 」"
    fn "「Hahaha, it's just like back\n\ \ at the welcoming party. 」"
    "Are these two going to go fly?"
    si "「I just hope they'll be able to do it right. 」"
    ka "「When we get to the beach,\n\ \ Torahiko and Juuichi-san should fly... 」"
    
    scene bus with qdis 
    show bus at hshake

    ta "{size=+15}「GUOOOOO! 」" 
    "What the...?"
    ta "「GUOOOOO, ZZZZZZ, *snore*... 」"
    ju "「Looks like he's sleeping. 」"
    "Really, he even has the nose bubble..."
    so "「He said he didn't have any problem\n\ \ getting up today. 」"
    ka "「But what a snore... 」"
    su "「But nobody heard him until now? 」"
    si "「I thought I heard him,\n\ \ before we entered the tunnel. 」"
    "We must have been focused on\nwhat we were talking about."
    ta "「*Mumblemumble*, Sachiko-san, is the food done yet?{p}\ \ That's my favorite dish, isn't it... 」"
    ko "「Ahahaha, I wonder what he's dreaming about? 」"
    driver "「Next, the beach, next up is the beach!{p}\ \ Please press the stop button if you are departing. 」"
    ky "「Should we wake him up soon? 」"
    fn "「Hey, we're here, Tatsu-nii... 」"
    ta "「*Mumble*?　Yeah...{p}\ \ [fn]-san, is the food going to get here soon?{p}\ \ I've only eaten lunch... 」"
    fn "「Get a grip, Tatsu-nii!{p}\ \ We're at the ocean! 」"
    ta "「We're eating the ocean today...?{p}\ \ The ocean? Here? 」"
    to "「Hyahahahahaha, did you bring something to eat,{p}\ \ Tatsu-nii? 」"
    ta "「Why's everybody laughing...? 」"
    fn "「Who is Sachiko? 」"
    ta "「That has nothing to do with you.{p}\ \ Sachiko-san is... 」"
    si "「Excuse me, please give me the change. 」"
    driver "「Yep, here you go.{p}\ \ Thank you very much. 」"
    "Shin-kun...{p}He's just ignoring us and gets off."
    ka "「Tatsuki-san,{p}\ \ it sounds like something was...{p}\ \ happening with Sachiko in your dream. 」"
    to "「Sachiko-san, is the food done yet? 」"
    ta "「Shut up!{p}\ \ I'm fine, and don't disrespect Sachiko-san! 」"
    to "「Oh, he's getting angry.{p}\ \ Run away. 」"
    su "「Yay, it's a race.{p}\ \ Tatsuki-san's face is turning red. 」"
    ko "「I don't think he's red because he's angry,{p}\ \ I'm guessing he's embarrassed. 」"
    ky "「Off the bus, everybody.{p}\ \ I'll pay the fare. 」"
    ta "「Wait up! 」"
    
    scene black with sdis
    pause 2
    
    scene beach01
    show su 001 at center
    with wipe_corner    
    show su 002 at jump_up

    su "「Woof, it's the sea! 」"
    fn "「It's huge!{p}\ \ I can look right through the water,{w=.3}\n\ \ and see little fish swimming around! 」"

    show to 001 at farright with wipe_right
    
    to "「It's less crowded than I thought it'd be. 」"

    show ky 001 behind su at farleft with wipe_right
    
    ky "「That's because it's inconvenient to drive\n\ \ all the way out here. 」"
    ky "「But it's popular among divers,{w=.3}\n\ \ because it's a little-known place. 」"

    show so 001 at midleft with wipe_right
    
    so "「There're a lot of stores here, too! 」"

    scene beach01
    show ju 001 at center
    with wipe_right

    ju "「It's also close to a harbor.{p}\ \ It would be nice if we could go there later. 」"

    show to 002 at midright with wipe_right
    
    to "「Senpai, I guess you didn't forget your honey. 」"

    show ju 006 with dis
    
    ju "「...Do you want me to use my technique? 」"

    show beach01 at hshake
    play sound bosu32
    show to 008 at move_midleft(.5)

    to "「Puh, puh, I got sand in my mouth. 」"
    "I guess he doesn't mind being thrown,\nas long as he's on the beach..."
    
    scene beach01 with wipeleft
    show ta 002 at farleft with wipe_right

    ta "「All right, we should go change. 」"
    "Of course we're swimming first.{p}What's everybody doing?"
    
#############################################
label beach07_choice:
    menu:
        "A. Is Tatsu-nii going to swim?":
            jump beach07_tatsuki
        "B. I'll ask Kouya.":
            jump beach07_kouya
        "C. I want to play with Shun-kun at the beach.":
            jump beach07_shun
        "D. What's Shin-kun doing?":
            jump beach07_shin
        "E. Let's swim with Kyouji.":
            jump beach07_kyoutarou
        "F. Should I mess around with Kounosuke?":
            jump beach07_kounosuke
        "G. Try to take it easy with Juuichi-san.":
            jump beach07_juuichi
        "H. I'll swim with Torahiko.":
            jump beach07_torahiko
        
#############################################    
label beach07_tatsuki:

    $ focus_character = "tatsuki"
    $ event_name = _("The Beach")
    $ love_tatsuki += 1

    scene black with sdis
    pause .5
    scene beach02 with dis
    
    fn "「Hey, are you going to swim, Tatsu-nii? 」"

    show ta 004 at midleft with wipe_right
    
    ta "「You moron. I'll tell you now,\n\ \ I'm ridiculously awesome at swimming.{p}\ \ {nw}"
    show ta 002 with dis
    extend "I won't lose to Tora. 」"

    show to 001 at midright with wipe_right
    
    to "「No way I can ignore that.\n\ \ Who did you just say you were better than? 」"

    show to 003 with dis
    
    to "「You think you can win against me? 」"

    show ta 001 with dis
    
    ta "「It's a challenge, then.{p}\ \ {nw}"
    show ta 004 with dis 
    extend "First one to get to the buoy. 」"
    to "「Interesting. Let's do this. 」"
    ta "「One round in the challenge.{p}\ \ The loser buys shaved ice for the winner? 」"

    show to 001 with dis
    
    to "「Good, let's do that.{p}\ \ {nw}"
    show to 010 with dis 
    extend "No hard feelings among the three of us. 」"
    "Three of us?"
    fn "「...Wait, I'm in this too? 」"
    
    play sound bosu35
    
    show to 005 at jump_up
    show ta 003 at jump_up
    pause .2

    fn "「Hey, don't make that surprised face. 」"

    show to 006 with dis
    
    to "「What are you saying?{p}\ \ {nw}"
    show to 010 with dis
    extend "Of course you are! 」"

    "Why...?"

    show to 003 with dis
    
    to "「What? Are you running away? 」"

    show ta 008 with dis
    
    ta "「Man, give me a break.{p}\ \ Someone from the city's acting like a jellyfish. 」"  

    show to at briefzoom 
    to "「Weakling! 」"
    
    show ta 004 at briefzoom 
    ta "「[fn], you meanie! 」"
    fn "「Okay, okay.{p}\ \ I'll join you, okay? 」"

    show to 002 with dis
    
    to "「Oh, yeah, it's wrong\n\ \ if you're not in a good mood. 」"

    show ta 002 with dis
    
    ta "「It's decided.{p}\ \ {nw}"
    show ta 001 with dis 
    extend "Now hurry up and change, you bastards. 」"
    fn "「What about you, Tatsu-nii? 」"

    show ta 202 with dis
    
    ta "「I brought the perfect fundoshi to change into. 」"
    "You can't use that as a bathing suit..."
    
    scene black with sdis
    pause 1.5
    scene beach04 with Dissolve(.5)
    pause .5
    play sound water01
    pause 1
    play sound water01
    pause 2.5
    play sound water01

    ta "「[fn] loses! 」"
    to "「Bring the shaved ice here. 」"
    "I get how it turned this way,{p}but I feel like I'm getting screwed..."
    fn "「You're much better at swimming, Tatsu-nii. 」"
    ta "「Hehehe, that's because I don't have fur.{p}\ \ Also, having a tail like mine really helps. 」"
    ta "「When I swim, I swing my tail back and forth. 」"
    fn "「Tatsu-nii, you're like a crocodile\n\ \ when you swim. 」"

    play sound bosu35
    
    ta "「WHO ARE YOU CALLING A CROCODILE?! 」"
    ta "「I'm already mad, go get me a melon ice and milk. 」"
    to "「I want strawberry ice, and a cola. 」"
    fn "「Sorry, I can't do that...{p}\ \ My wallet... 」"
    ta "「What should we do then? 」"
    to "「Let's battle for some different stakes.{p}\ \ First one back to the beach? 」"
    to "「And if [fn] wins,\n\ \ we call off the debt. 」"
    ta "「If we're diving,\n\ \ there's no way I'll lose. 」"

    play sound water_splash
    pause 1
    
    to "「So it's a diving contest now.{p}\ \ Sorry, but I'm winning this one too. 」"
    fn "「If it's about endurance,\n\ \ I have some faith in myself.{p}\ \ Torahiko, are you getting ahead of yourself? 」"
    to "「Hmph, no way! 」"

    play sound water_splash
    
    ta "「Fwaaaaaahhh!{p}\ \ All right, let's do it! 」"
    to "「Then, we start in 3!{p}\ \ 2...{p}\ \ 1... 」"
    
    stop music fadeout 1.5

    "Huh?{p}There's something floating in the water..."
    "This long white piece of cloth is...{p}{nw}"
    play music free0205
    extend "A fundoshi!"     
    "This is bad."

    play sound water_splash
    
    to "「Go! 」"
    fn "「Tatsu-nii, wait! 」"

    show ta 104 with dis
    
    ta "「This is a contest, I can't wait!{p}\ \ Don't think I'm that easy to trick!{p}\ \ It's not gonna work.{nw}"
    show ta 102 with dis
    extend "  Later. 」"
    
    stop music fadeout 1
    hide ta with sdis

    fn "「Tatsu-nii, your fundoshi! 」"
    pause .5
    play sound jap_002
    pause .125
    play sound2 jap_002
    pause .5

    "{cps=0}Key Item: 6 foot Fundoshi GET!" 
    
    jump beach07_ridehome
    
#########################################    
label beach07_kouya:
    
    $ event_name = _("Something Floating in the Water")
    $ focus_character = "kouya"
    $ love_kouya += 1
    
    scene black with Dissolve(1)
    pause .5
    scene beach01 with Dissolve(.5)

    fn "「Starting off with swimming too, Kouya? 」"
    "For some reason I felt like asking."

    show ka 001 at center with wipe_right
    
    ka "「Yeah, that's right.{p}\ \ We already came here,{p}\ \ it'd be a waste to not go in. 」"
    fn "「Well that's true. 」"

    show ka 003 with dis
    
    ka "「Right?{p}\ \ Now let's hurry up and change."
    ka "If we take it too easy,{p}\we won't have done anything,{p}and it'll be over. 」"

    hide ka with wipe_right
    
    "Kouya laughed as he walked out.{p}I followed after."
    "The two of us got in line\nfor the changing rooms."

    scene beach02 with wipeleft
    
    "The changing rooms weren't that impressive.{p}They looked like they could be blown away."
    "I got in and took my swimsuit out of my luggage.{p}I thought \'time to get changed\',{p}but then my hand stopped."
    "As for why I stopped,{p}there wasn't much reason."

    show ka 001 at center with wipe_right
    
    ka "「What's wrong, [fn]? 」"
    fn "「Oh uh, nothing? 」"
    ka "「Really?{p}\ \ Well okay. 」"

    hide ka with wipe_right
    
    "That was why I stopped.{p}It was nothing but him changing clothes."
    "Like I thought,{p}a person changing quickly\nisn't much of a sight."
    "Is it a loss to look and have to leave it?{p}That's what I think, but then I also think...{p}That it isn't right."
    "My mind is conflicted...{p}Hm, but is it okay to look...{p}Just a little...?"
    fn "「Yeah, it's all right... 」"
    "I muttered so no one could hear, and decided."
    "Mom, Dad, I am a bad child!{p}I've become filthy!{p}But I have no regrets!"
    "As I continued changing,{p}I looked at Kouya from the side,{p}as though I didn't notice."

    show ka 301 at center with wipe_right
    
    "Wait, he's already done!?"
    "Eh, what is this?{p}What trick did he pull?"
    "When did Kouya get so good\nat time management?{p}I-is he a new Stand User!?"

    show ka 305 with dis
    
    ka "「Hmm? You still haven't changed, [fn]?{p}\ \ You'll get left behind. 」"
    fn "「Whuh!?{p}He-hey wait! 」"

    hide ka with wipe_right
    
    "Kouya left me behind,{p}promptly picked up his clothes,{p}and put them behind the changing rooms."
    "Almost exactly done in the blink of an eye."
    fn "「...From here on,{p}\ \ I won't waver and just stare. 」"
    "Being left alone,{p}I decided that with all my heart."
    
    scene black with sdis
    pause 1
    scene beach01 with Dissolve(.5)

    "I lagged behind Kouya a little,{p}and came outside too.{p}But I don't see him anywhere."
    fn "「Huh, was I really left behind? 」"
    "I got anxious, and looked around the area."
    "There's people playing beach volleyball,{p}people playing in the shallow water..."
    "And unlike the others,{p}there are people swimming\nin the opposite side."
    "It seems everyone's enjoying\nthemselves as they please here."
    "Importantly, Kouya is..."
    fn "「...Ah, I see him. 」"
    "Kouya was floating face up on top of the sea."
    "He was cradled by the waves,{p}as if he was naturally part of the ocean.{p}Somehow, he seemed to be in a good mood."
    "As I watched,{p}inside me a mischievous idea was born."
    "As revenge for being ditched,{p}I'll surprise him a bit."
    "From the point I was left behind,{p}I moved and entered the sea."
    "Then, so I wouldn't be noticed,{p}I got down low and approached Kouya.{p}Slowly, slowly."
    "The distance to Kouya gradually shortened,{p}and if I claw at the water's surface,{p}the splash should reach him."
    "However, Kouya's looking at the sky,{p}just as usual."
    "He won't notice me here.{p}This is so convenient."
    "Silently, but with all my strength,{p}I sucked my breath in."
    "And just as silently,{p}my body went under into the water."
    "Since it's not that deep yet,{p}my feet touched the ground."
    "I kicked the cold sand,{p}and swam across the floor over Kouya."
    "When I look up, I see his tufty tail,{p}being cradled in the waves."
    "Just like I thought it would.{p}Without meaning to, my cheeks slackened."
    "Now then, it's about time I pull my prank."
    "The old people have said it.{p}If a string is hanging from the ceiling,{p}just pull on it and see what happens."
    "In this case...{nw}"
    show beach01 at hshake
    play sound hit81

    fn "{size=+20}「HIYAAAHH! 」"
    "One shout,{p}turned into nothing but a bubbling murmur."
    
    play sound puu75
    pause .2

    "I reached out for the base of Kouya's tail.{w} {nw}"
    show ka 312 big at center_big
    extend "{w=.01}{nw}"
    show ka at briefzoom 
    
    ka "{size=+15}「Whuh!? 」" 
    "Kouya jumped in surprise."
    "His feet floundered,{p}as if he was searching for solid ground."
    "To get him so freaked out\nsomehow feels refreshing.{p}Yeah, I got him good."
    "Soon after Kouya's feet hit the sand,{p}he stood up."
    "After checking to make sure,{p}I surfaced."

    hide ka
    show ka 305 at center 
    with wipeleft 
    
    ka "「Who'd have thought it...{p}\ \ [fn]. 」"
    "Kouya said that faintly,{p}while he was catching his breath."
    fn "「Correct, it was me. 」"
    ka "「Still with the stupid stuff... 」"
    fn "「But that's because you really ditched me.{p}\ \ I got a revelation from God, saying that\n\ \ paying you back one time would be all right. 」"

    show ka 307 with dis
    
    ka "「Wrong, it was from an evil god.{p}\ \ Don't listen to the voices.{p}\ \ Don't do what they say. 」"
    fn "「I'll only put in effort next time.{p}\ \ Anyway, that was a good reaction back there. 」"
    fn "「Now I know your tail is weak. 」"

    show ka 306 with dis
    
    ka "「Nope.{p}\ \ It's because you suddenly grabbed it. 」"
    "Well, I guess that's true too.{p}The tail seems to be connected to their spine,\nso they would be sensitive to it."
    "However, after finishing this prank,\nsomehow it feels unfinished.{p}So for a little longer, I bothered Kouya."
    "I've already had to chase after Kouya,{p}so I was ready to run."
    "While I was thinking about that,\nI threw one last line at Kouya."
    fn "「Hmph.{p}\ \ Well, you made a great face.{p}\ \ Maybe I'll tell Torahiko how to do it too. 」"

    show ka 306 big at center_big with dis    

    ka "「...Wait just a minute, [fn]. 」"
    "Yes..."
    fn "「Eh?{p}\ \ Oh hey, perfect timing. 」"
    fn "「Torahiko's right over there.{p}\ \ Hey! Torahiko! 」"

    hide ka with wipe_right
    
    "I began running with all my power."
    
    play sound gun09_r

    "\nBoom."
    ka "{size=+15}「You wait right there, [fn]! 」"
    fn "「No way!{p}\ \ I'm not going to wait at all! 」"
    "And then, this oceanside game of tag began,\njust as planned."
    "I'm always getting teased by Kouya.\nDoing this once in while is fine, right?"
    
    jump beach07_ridehome
    
#####################################
label beach07_shun:
    
    $ event_name = _("The Blue Sea! The Shining Sun! And Shun-kun!")
    $ focus_character = "shun"
    $ love_shun += 1
    
    scene black with sdis
    scene beach01 with wipeleft

    "Anyway the beach is here,{p}but if they notice everyone will go on ahead."
    "If I get left behind in that case,{p}I'll chase after them."
    "Which reminds me, Shun-kun's clothes,{p}are blue and white,{p}the color of the sky and sea!"
    "I wonder what his swimsuit's like!{p}Those thoughts started up,{p}and the search for him on the beach began."
    "..."
    "Ah, there he is."
    "On top of a leisure seat on the beach,{p}sitting while holding his knee,{p}enjoying the salty air."
    "That soft whipping sound I hear,{p}it's coming from his tail,{p}hitting the ground."
    su "「Ocean, ocean!{p}\ \ Swimming, floating, diving,{p}\ \ scubasailing! 」"
    "..."
    su "「Ocean, ocean!{p}\ \ Swimming, floating, diving,{p}\ \ scubasailing! 」"
    "...What's scubasailing?"
    
    show su tailwag 01 at center with wipeleft

    su "「[fn]-san!{p}\ \ I'm done readying up!{p}\ \ Let's go swimming! 」"
    "Shun-kun grabbed my surprised self,{p}and shouted out in a clear voice.{p}...What did he get ready?"
    
    scene black with sdis
    pause .5
    scene beach02 with wipeleft
    pause 1

    "He pulled my arm to a changing room,{p}and we entered a little shack."
    
    show su tailwag 01 at center with wipeleft

    su "「Ocean, ocean... 」"
    "Shun-kun's song is in its 6th repeat,{p}but it's okay."
    "Today's main show is the live changing,{p}of a childhood friend (of 5 years.)"
    "As the rest of the group have already left,{p}and jumped into the water,{p}let us carefully observe."

    show su 002 with dis
    
    su "「Scubasailing! 」"
    "The beginning starts with a wrap towel.{nw}"
    show su 001 with dis
    extend ""
    
    su "「[fn]-san,{p}\ \ you aren't going to change? 」"
    fn "「Y-yeah. 」"
    "...So, shall I start taking my clothes off too?{p}I have to make sure not to miss my best shot."

    show su 002 with dis
    
    su "「Nyan nyan nyan nyan nyan! 」"
    "Seems to be an interlude."
    "Shun-kun took off his outer clothes,{p}patted and folded them,{p}then placed them on the tatami mat."
    "What a delicate body.{p}You could almost feel,{p}the slenderness of his shoulder."
    "Yeah, stick your arm into the towel,{p}and while you're at that,{p}take your underwear off."
    "As I thought,{p}he's wearing white briefs.{p}Mhmm."

    show su 101 with dis
    hide su with wipe_down 
    
    "And then when his legs go through the swimsuit,{p}his wrap towel slips a little.{p}...You can see his crotch from here!"
    su "「U-urg... Hrm... 」"
    "Shun-kun has become a little confused,{p}and embarrassed as he pulls up his towel.{p}Now he's pulling it up each leg at a time."
    "Since his swim trunks are not firmly in place,{p}let's take off the towel."
    su "「*Mumble*. 」"
    "Now that the towel has been lifted,{p}up over the head and taken off..."
    fn "「Shun-kun, that looks so good on you. 」"
    su "「Really?{p}\ \ But this is what I always wear. 」"
    "After politely putting away the towel,{p}he's now putting on a yellow swim cap."
    "Bring that old swimsuit out here,{p}to your Onii-san,{p}so I can reuse it for the sake of Earth."

    show su 301 at center with wipe_up 
    
    "Shun-kun appeared wearing the stock school swimsuit."
    "Yes, I've already set my expectations,{p}but this is also splendid."

    show su 304 with dis
    
    su "「The white ones were too tight,\n\ \ so I didn't want to wear them. 」"
    su "「That's not weird, is it...? 」"
    
    stop music 
    play sound tsuzumi

    "{size=+30}!"
    
    play music free0203

    "That's what I call a swimmer guy!"
    "Once again, I stare at that bulge."
    "He's still not aware of it,\npushing itself along the outline\nof the slippery cloth."
    "Ergh, this is dangerous after all.{p}In a typical summer at a beach like this..."
    "It can really influence one\ninto releasing that juvenile body.{p}There's no mistake."
    "My eyes are too rooted to the spot,{p}it wouldn't be good if he became aware\nof my... Uhh... Observational skills."
    "What do I do?"
    menu:
        "A. Buckle-Up.":
            jump beach07_buckleup
        "B. Let it hang loose.":
            jump beach07_hangloose

#########################################
label beach07_buckleup:

    "I'll do it for the sake of dignity."
    fn "「Maybe, it's better to put on the white ones,{p}\ \ since they won't let anything important get broken. 」"
    su "「B-but... 」"
    fn "「Tatsu-nii's wearing those too. 」"
    "On the opposite side is Tatsu-nii,{p}who looks like he hasn't changed yet."
    "He's taking off his clothes,{p}getting out and putting on a white fundoshi,{p}and he diligently checks the knot."
    "It doesn't look any different,{p}from the underwear he took off though.{p}...Maybe it's water resistant?"

    show su 316 with dis
    
    su "「Uguu. 」"
    fn "「C'mon, I think the white ones,{p}\ \ are important after all. 」"

    show su 305 with dis
    
    su "「I-I understand.{p}\ \ If [fn]-san says so... 」"
    "Shun-kun's obedient.{p}He's rummaging for the wrap towel from before.{p}Now, time to watch live changing again!"
    
    show ta 204 with circle_out 

    ta "「Hey let's go [fn]!{p}\ \ Summer is calling to me! 」"
    fn "「Wait, I'm not done changing yet. 」"
    "Srtch srtch srtch.{p}The sounds of my body dragging along."
    "Up until my clothes got dumped into the water,{p}Tatsu-nii wouldn't let go of the back of my neck."
    
    jump beach07_ridehome

##########################################
label beach07_hangloose:
    
    $ love_shun -= 1

    "Okay.{p}I have to tell everyone how great this is."
    fn "「Yep!{p}\ \ If it's not uncomfortable, it's okay! 」"

    show su 302 with dis
    
    su "「Ahaha, I'll go on ahead then.{p}\ \ [fn]-san, please hurry on over too! 」"
    
    scene beach01 with wipe_right

    "Shun-kun said that and rushed out energetically."
    "After taking off the clothes he usually wears,{p}the sight of light brown,{p}with blue and yellow accents is dazzling."
    "His wagging tail and figure,{p}matched in with the sky and sea.{p}It made for some awesome scenery."

    show ju 501 at center with wipe_right
    
    ju "「Hey, Kodori. 」"

    show su 304 at midright with wipe_right
    
    su "「Yes, Juuichi-san? 」"
    "Is the sightseeing-pamphlet worthy scene,{p}Juuichi-san, in his casual swimsuit,{p}called and stopped Shun-kun."
    "He's whispering something into his ears."

    scene beach02 with sdis #!#Check

    "Shun-kun looked a little surprised,{p}and he returned to the changing room,{p}as his shoulders dropped."

    show su 310 at center with wipeleft
    
    su "「Fine... I'll put on a supporter... 」"
    "He pulled out his wrap towel,{p}and put it on his lower back again.{p}Then, Juuichi-san sluggishly showed up."

    show ju 501 behind su at midright with wipeleft
    
    ju "「[ln], didn't you notice?{p}\ \ Kodori, you didn't put on a supporter did you? 」"
    fn "「Oh!{p}\ \ I see it, now!{p}\ \ I completely, entirely didn't notice! 」"

    show ju 506 with dis
    
    ju "「[ln]! 」" 
    fn "「I'm so sorry. 」"
    "He saw through my fickle motives,{p}and I hung my head in defeat,{p}from his silent heavy pressure."

    jump beach07_ridehome

#############################################     
label beach07_shin:

    $ event_name = _("Sunscreen is a Man's Love")
    $ focus_character = "shin"
    $ love_shin += 1
    
    scene black with sdis
    pause .2
    scene beach01 with Dissolve(.5)

    "Anyway, everyone's changed into swimsuits,{p}and came back to the beach."
    "If there's a chance,{p}I'd take advantage of the changing,{p}to sneak a peek at everyone."
    "How would that go anyway?"
    "While I was lost thinking about that,{p}everyone had already finished changing,{p}leaving me for last."
    "Dammit! When we go back,{p}I'll definitely look.{p}I'll look for sure!"
    "Umm, that aside everyone is...{p}Oh, underneath that parasol is Shin-kun."
    
    scene beach03 with wipeleft
    
    show si 301 at center with Dissolve(1)
    
    si "「Hey. 」"
    fn "「Huh? You're not going to swim Shin-kun? 」"

    show si 304 with dis
    
    si "「I'm going to pass.{p}\ \ I don't really like getting wet. 」"
    fn "「But we came all the way to the beach. 」"

    show si 310 with dis
    
    si "「Well, if it's a shallow place,{p}\ \ then okay... 」"
    fn "「Eh? 」"

    show si 301 with dis
    
    si "「Nothing. 」"

    show si 310 with dis
    
    "After saying that,{p}Shin-kun opened the lid of a bottle."
    "He started rubbing a milky,{p}white cream all over himself."
    "Some kind of sunscreen?"
    fn "「What's that? 」"
    si "「UV Cream.{w} Amaki insists that\n\ \ ultraviolet rays are bad for fur. 」"

    show si 301 with dis
    
    "This Amaki-san, is he someone...{p}who manages Shin-kun's household?"

    show si 304 with dis
    
    si "「I don't really like this cream, though.{p}\ \ I can't see my back,{p}\ \ and I could miss a spot. 」"
    fn "「Uh-huh. 」"
    "It's true, trying to rub your own back,{p}with your hands looks hard no matter what."
    "...Sigh{p}I often see this kind of situation in manga..."
    fn "「If it's all right, how about...{p}\ \ I put it on your back for you? 」"

    show si 305 with qdis
    
    si "「Eh? 」"
    "Suddenly, Shin-kun's movements stopped.{p}While I heard everyone's distant cheerful cries,{p}I waited for Shin-kun's answer."
    "Is he suspecting me like I thought?"

    show si 311 with dis
    
    si "「Then...{p}\ \ {nw}"
    show si 302 with dis
    extend "Is it all right if I ask you to? 」"
    "I-it happened!"
    "Underneath the parasol,{p}Shin-kun was laying face down,{p}on top of the beach mat."
    "I picked up the bottle on the side,{p}then squirted the cream onto my hand."
    "Spuuurt.{p}I put that hand gently on Shin-kun.{p}Whoa, it's so soft to the touch."
    "The thin and supple fur coiled around my fingers,{p}and smoothly moved through the gaps between them."
    "Somehow, it's starting to feel weird."

    show si 310 with dis
    
    si "「[fn]. 」"
    fn "「Wh-what?{nw} 」"
    show si 301 with dis
    
    si "「Don't rub on the top so hard,{p}\ \ can you rub it more closely to the roots?{p}\ \ You have to do it closer to the skin. 」"
    fn "「Um, like this? 」"
    "Man, I got impatient.{p}I thought he realized what I was thinking,{p}so my heart hasn't calmed down yet."
    fn "「Um, like this? 」" 

    show si 304 with dis
    
    si "「Put your fingers into it more.{p}\ \ Like you would when you use shampoo. 」"
    fn "「N-now? 」"

    show si 301 with dis
    
    si "「Yes, like that. 」"
    "Wa-wa. Right now, I'm totally feeling,{p}Shin-kun's body heat."
    "Is it okay for Shin-kun,{p}to be this defenseless?"

    show si 302 with dis
    
    si "「[fn], that tickles. 」"
    "N-no, I was asked by Shin-kun,{p}so that's why I'm doing it.{p}No way am I feeling guilty."
    
    play sound pyoro45_a
    show si at briefzoom

    si "「Fufufu, haha!{p}\ \ [fn], n-not there! 」"
    "Ayep. Nothing to feel guilty about."
    
    play sound pyoro46
    pause .3
    play sound2 pyoro46
    show si at shivering

    si "「Ahahaa, I-I'll do my tail myself!{p}\ \ Ah, ugh! Aha, ahahahaa! 」"
    ka "「What are you guys doing? 」"
    
    show si 305 at jump_up
    
    show ka 301 at offright
    show su 301 at offright
    
    fnsi "「Oh. 」{w} {nw}"    
    show si at move_midleft(0.75)
    show su at move_midright(0.75)
    show ka at move_farright(0.75)
    extend "{w=.75}{nw}"

    ka "「When did you two get so close? 」"

    show su 302 with dis
    
    su "「You two look like you're having so much fun. 」"

    show si 311 with dis
    
    si "「Y-you're mistaken!{p}\ \ This is just me having [fn]\n\ \ put sunscreen on me. 」"
    
    show su behind ka
    show ka 303 at move_midright(0.25)

    ka "「Shun, you can't look! 」"
    
    show su 303 at jump_up

    su "「Woof!?　But why? 」"
    ka "「Because.{p}\ \ This is too...{p}\ \ stimulating for children. 」"

    show su 305 with dis
    
    su "「Please don't treat me like a child. 」"

    show ka 302 at farright with dis
    
    ka "「Well... Whatever."
    ka "You two look like you're having fun,\nso we're not going to intrude.{p}Let's go play volleybal over there. 」"

    show su 301 with dis
    
    su "「Uu, I understand. 」{w} {nw}"    
    show ka at move_offright(0.25)
    show su at move_offright(0.25)
    extend "{w=.25}{nw}"
    
    show si 303 at move_center(1.5)

    si "「... 」"
    fn "「... 」"
    si "「... 」"
    fn "「...Uh. 」"

    show si 310 with dis
    
    si "「Thanks, [fn]. 」"
    fn "「N-no, that's... Sorry. 」"
    si "「... 」"
    "And then for a short while afterwards,{p}Shin-kun wouldn't say a word to me."

    jump beach07_ridehome

########################################    
label beach07_kyoutarou:

    $ event_name = _("See-through")
    $ focus_character = "kyoutarou" 
    $ love_soutarou += 1
    $ love_kyouji += 1
    
    scene black with sdis
    pause .2
    scene beach01 with Dissolve(.5)

    fn "「Of course you're swimming too, right Kyouji? 」"

    show ky 001 at center with wipeleft
    
    ky "「Ah. Everybody's been waiting a long time,{p}\ \ to come here."
    ky "It would be a loss if we return,{p}without having fun. Right, Tarou? 」"

    show so 003 at midright with dis
    
    so "「Yep! I'm really gonna enjoy this day!{p}\ \ This is my first time goin' to the beach,{p}\ \ with Takahara-senpai! 」"
    ky "「Haha, it is. But you aren't going,{p}\ \ to get too hyper, are you? 」" 

    show so 006 with dis
    
    so "「I won't!{p}\ \ Ehehe... 」"
    "Soutarou-kun gets a little embarrassed,{p}and scratches his nose."
    "By the way things are going,{p}we should be getting in the sea soon..."
    ky "「Okay, let's change our clothes first.{p}\ \ Where is the changing room...? 」"
    fn "「Oh, is that hut over there?{p}\ \ Everybody's walking over there. 」"
    ky "「Looks like it...{p}\ \ should we head on over? 」"

    show so 001 with dis
    
    so "「Oh, I'm goin' too! 」"

    scene beach02
    show ky 001 at center
    show so 001 at midright
    with wipe_right
    
    "We get to the changing room hut.{p}Good timing, it's already our turn."
    fn "「All right, I'll get changed.{p}\ \ You two wait out here. 」"
    ky "「Oh, I know. 」"
    "Suddenly, Kyouji thinks of something and\nclaps his hands together."
    ky "「Why don't all three of us go in together? 」"
    
    show so 005 at jump_up

    so "「...! 」"
    fn "「Whaaaat!? 」"
    "When Kyouji says that,{p}he has a serious look on his face."
    "He said that without any warning.{p}I shout from a strange place,{p}in the back of my throat."
    fn "「Ch-change together? 」"
    ky "「Yeah. Three people going separately,{p}\ \ isn't very efficient, right?"
    ky "This way we won't keep the next person,{p}waiting until we're done. 」"
    fn "「I-I guess so, but...{p}\ \ H-hey? Soutarou-kun. 」"
    "I glance over at him."
    "The small changing hut looks,{p}like it would be a bit crowded,{p}with 3 people inside."
    "But above all, I'll be in an enviroment,{p}where those two will be naked,{p}only a few centimeters away."
    "I have no idea how much,{p}of that I'll be able to resist."
    "Surely Soutarou-kun,{p}must be embarrassed about this..."

    show so 001 with dis
    
    so "「I don't see anything wrong with that... 」"
    fn "「Wh-Whaaat!? 」"
    "When Soutarou kun says that,{p}he has a serious look on his face."
    ky "「What's wrong, [fn]?{p}\ \ Your voice sounds strange. 」"
    fn "「N-no no! I-It's nothing!{p}\ \ You just suggested that so suddenly,{p}\ \ that it took me off guard, that's all. 」"
    ky "「Is that so?{p}\ \ Anyway, let's get in.{p}\ \ We're holding those behind us up. 」"
    to "「Hey [fn], hurry up and get in there,{p}\ \ Are you gonna skip your turn? 」"
    fn "「A-all right... 」"
    "Feeling the pressure from Torahiko,{p}we finally enter the changing room."
    
    hide ky
    hide so
    with wipe_right

    "As soon as we get in,{p}Kyouji immediately begins to undress."

    play sound changing
    
    "I hesitate once, but I can't stand it,{p}I sometimes glance over them."
    "Huh? I'm not feeling guilty?"
    "Because we're changing,{p}with our backs facing each other,{p}they won't notice."
    "...I'll probably be safe."
    "Kyouji has a tight body,{p}while Soutarou-kun's is slender and delicate."
    "They've trained their bodies from soccer,{p}so there's no excess fat at all."
    "I look down at my stomach and compare.{p}...I haven't been getting much excersise lately."
    "Some fat is clearly showing.{p}I try pinching it with both of my hands."
    "..Just as I expected, it's gotten pretty bad."
    
    show ky 301 at center
    show so 301 at midleft
    with wipe_right

    so "「Okay, I'm ready! 」"
    ky "「...Hm, [fn] you haven't...{p}\ \ changed yet? 」"
    fn "「Huh? 」"
    "I turn my head. They're standing there,{p}already in their bathing suits.{p}Aaaah, I've failed my mission..."
    so "「Oh, did you forget somethin'? 」"
    "Soutarou-kun asks.{p}Th-this pain in my chest is too much..."
    fn "「No, that's not it...{p}\ \ Th-that's right!"
    fn "My pants zipper is stuck!{p}I can't get it to go down... 」"
    ky "「I see...{p}\ \ Well, we'll go out first. 」"
    ky "「Let's go, Tarou. 」"

    show so 303 with dis
    
    so "「Okay! 」"

    hide so
    hide ky
    with wipeleft
    
    "They put their clothes in their bags and leave."
    "Now it's just me left in the hut."
    fn "「...Anyway, shall I get changed? 」"
    "Feeling awkward, I pick up my bathing suit." 
    
    scene black with wipeleft
    scene beach01 with wipeleft

    "Finished changing, I return to the beach,{p}and I see everybody's in the water,{p}having a good time."
    "Now where did those two go..."
    "Ah, there they are. {p}I wave at them from the beach."
    "I run straight down the sandy beach,{p}to where they are."
    
    show ky 301 at center
    show so 301 at midleft
    with wipe_right

    fn "「Wait up! 」"
    ky "「Good. [fn] has arrived,{p}\ \ so we can start warming up first. 」"
    fn "「Eh... but aren't we just swimming?{p}\ \ There's no need to warm up for that... 」"
    ky "「Now now, [fn],{p}\ \ isn't being prepared for anything important? 」"
    ky "「Your opponent is the sea.{p}\ \ It's different from the pool,{p}\ \ and the river."
    ky "So if you don't prepare, {p}there's a chance you could even drown. 」"
    fn "「That's overdoing it... 」"
    
    show ju 501 at farright behind ky with wipeleft

    ju "「...No, there's a reason,{p}\ \ for Takahara's instructions. 」"
    fn "「Whoa, Ju-Juuichi-san... 」"
    "At my negligent reply,{p}Juuichi-san suddenly appears from behind."
    "I turn around and see him,{p}looking at me square in the eyes."
    ju "「There's no such thing as being 100\% prepared.{p}\ \ However, thanks to the act of preparation,{p}\ \ you can recognize your own inexperience. 」"
    ju "「...Understand? 」"
    fn "「Y-yeah...{p}\ \ I'll be more diligent... 」"
    "I give him an agreeable response,{p}then get out of his focus.{p}Whew, that was scary..."
    ju "「So, I'll join in too.{p}\ \ Is that fine, Takahara? 」"
    ky "「Oh, of course it is. 」"

    scene beach01 with wipe_right
    
    "Then, we, along with Juuichi-san,{p}begin our warm up excercises on the beach."
    "In front of us, Kyouji leads the work-out."
    "Since he's the captain of his club,{p}he's almost like a coach,{p}in the middle of pratice."
    "The only difference,{p}is that we're in our bathing suits."
    "Well, we were naked together...{p}but, for now I'll let this be my motivation."
    "..."

    show ka 302 at center with wipe_right
    
    ka "「What's wrong, [fn]?{p}\ \ It's just a warm-up, but it looks like,{p}\ \ you're pulling your back all weird. 」"
    "Looking at my posture,{p}Kouya makes fun of me from behind."
    fn "「Th-this is nothing!{p}\ \ Besides, you're just standing there,{p}\ \ watching, you should join us. 」"

    show ka 305 with dis
    
    ka "「Oh, I'm fine.{p}\ \ Even if I get a cramp or anything,{p}\ \ I'm sure I'll be able to manage somehow. 」"
    fn "「R-really... 」"
    "His arm...{p}I don't think there would be any problem."

    show ka 303 with dis
    
    ka "「Well then, I should get back,{p}\ \ to swimming soon.{p}\ \ Good luck with the exercise. 」"

    hide ka with wipe_right
    
    "As he says that,{p}Kouya starts running down the beach."
    "As he departs, I give him a look of envy,{p}shake away my delusions, {p}and stretch the tendons in my foot."
    
    show ky 301 at center 
    show so 301 at midleft
    with wipe_right
    
    show so 303 with dis
    pause .2

    so "「Senpai, let's hurry up and get in! 」"
    ky "「Oh, come on now, Tarou.{p}\ \ Don't rush too much. 」"
    "We finish warming up,{p}and head straight for the water."
    "Soutarou-kun grabs on to Kyouji's arm,{p}and forcefully pulls him."
    "First things first,{p}I get to the water's edge,{p}and try to soak my feet."
    "The clear waves caress my bare feet.{p}Ah, this... feels good..."
    
    play sound water01
    pause .5
    
    ky "「Hey, Tarou! 」"
    "Kyouji swipes at the water's surface,{p}sending a spray of water,{p}in Soutarou-kun's direction."

    show so 306 with dis
    
    so "「Waah, s-senpai, please stop! 」"
    "Soutarou-kun doesn't like how he's acting,{p}but he's enjoying it a little."
    "The sight of those two playing,{p}creates a romantic scene."
    "D-damn... I'm jealous...{p}If those two can show off like that,{p}then I...!"

    play sound water01
    
    fn "「Take this! 」"
    
    show so at hit_right
    
    so "「Woah, you too, [ln]-san!? 」"
    ky "「All right, Tarou!{p}\ \ Now, focus your attack on [fn]! 」"

    show so 303 at jump_up
    
    so "「Okay! 」"

    show ky at jump_up
    
    ky "「There! 」"
    fn "「Eh, you two are being unfair... Woah! 」"
    "Water is splashed at me,{p}from two different directions at once."
    "I-I'm being attacked by two athletes,{p}I'm clearly at a disadvantage here!"
    "Frolicking around the water like this,{p}it reminds me of how,{p}we used to play in the river."

    jump beach07_ridehome
    
########################################
label beach07_kounosuke:
    
    $ focus_character = "kounosuke"
    $ love_kounosuke += 1
    $ event_name = "Swimming Rings and the sea, that's Summer!"
    
    scene black with sdis
    pause .2
    scene beach02 with wipeleft

    "This changing room is pretty shabby,{p}but it's better than nothing.{p}I finish changing in this hut."
    "Hmm, the endless blue sky. The dazzling sun.{p}The deep blue ocean that stretches out.{p}And the scorching hot sand."
    "Ooh, I feel like I could just cry out."

    show ko 303 at center with wipeleft
    
    ko "「Yahoo! 」"
    "..."
    "Well, I guess Kounosuke is different."

    show su 302 at midright with wipeleft
    
    su "「Yahoo! 」"
    "Don't get caught up with him, Shun-kun..."
    "Thinking about crying out, too, for a moment,{p}but then realize it's a stupid idea.{p}I'm getting embarrassed."

    show ko 302 with dis
    
    ko "「Are you going to yell too, [fn]? 」"

    show su 301 with dis
    
    su "「It feels good to shout! 」"
    fn "「No, stop... 」"
    
    show ko 301 
    show su 304
    with dis

    kosu "「But it's so refreshing! 」" 
    "Don't sing in harmony."
    fn "「Shun-kun aside, Kounosuke,{p}\ \ you're too old to be using a swimming ring. 」"

    show ko 304 with dis
    
    ko "「Huh? You don't understand.{p}\ \ Floating around the waves is comfortable.{p}\ \ Right, Shun-kun? 」"

    show su 301 with dis
    
    su "「It is.{p}\ \ Besides, I know how to swim properly. 」"
    
    show ko 303
    show su 302
    with dis

    kosu "「That's right! 」" 
    "...Since when have you guys been buddies?{p}Well, in essence, isn't it like using a boat,{p}made for one person?"

    show ko 301 with dis
    
    ko "「Why don't you get one too?{p}\ \ It gives you a resistance to the waves,{p}\ \ and it's more fun than just swimming."
    ko "I borrowed mine from the beach hut over there. 」"
    fn "「Hmm. Well, I guess I'll get one too. 」"
    
    show ko 303
    show su 301
    with dis

    ko "「See you! 」"
    su "「Later! 」"

    scene beach01 with wipe_right
    
    fn "「Oh. This is pretty nice. 」"
    "Kounosuke was right,{p}using a swim ring to float,{p}on the waves without sinking is fun."
    "It gets in the way when I try to swim,{p}but that resistance to swimming,{p}makes it unusually interesting."
    
    show ko 303 at center
    show ko 303 at bobbing
    with wipeleft    
    
    ko "「See? It is fun, isn't it? 」"    
    
    show su 302 at farright with wiperight
    show su at bobbing
    
    su "「Splash splash! 」"
    "Kounosuke approaches me,{p}wearing a swimming ring as well."
    "Shun-kun is floating a short distance away.{p}We play and splash about in the water."
    fn "「Yeah. It's pretty amusing. 」"
    
    show ko 301 with dis

    ko "「Why don't we teach him about how fun this is? 」"
    fn "「Huh? 」"
    
    scene beach03
    show si 301 at center
    with wipeleft

    si "「... 」"
    
    scene beach01
    show ko 301 at center
    show ko at bobbing
    with wipeleft

    fn "「But Shin-kun's a really bad swimmer isn't he? 」"

    show ko 302 with dis
    
    ko "「It's all right, it's all right.{p}\ \ He won't sink with a swim ring. 」"
    fn "「Eh. I think it's better if we don't. 」"
    ko "「He'll be fine. 」"

    hide ko with wipe_right
    
    "When Kounosuke has that face,{p}it usually means he's up to no good."
    "With a touch of uneasiness,{p}I follow him to the beach."
    
    scene beach03
    show si 301 at center
    with wipeleft

    si "「... 」"
    
    show ko 303 behind si at midright with wipeleft
    pause .2
    show si 310 with dis

    si "「...I have some money on me,{p}\ \ but I'm not sure how much... 」"

    show ko 301 with dis
    
    ko "「Shin-kuuun. 」"

    show si 301 with dis
    
    si "「What? 」"
    "Shin-kun languidly raises his eyes,{p}from the paperback he was reading."

    show ko 302 with dis
    
    ko "「Let's swim together! 」"

    show si 310 with dis
    
    si "「... 」"

    show si 304 with dis
    
    si "「I'll pass. I don't like getting wet. 」"

    show ko 305 with dis
    
    ko "「Don't say that.{p}\ \ You can have a swim ring,{p}\ \ so you won't go underwater. 」"

    show si 310 with dis
    
    si "「A swim ring... 」"
    ko "「There's nothing embarrassing about it.{p}\ \ We're not at the swimming pool,{p}\ \ but you still can have one."

    show si 303 with dis
    
    ko "Look, Shun-kun's having fun over there. 」"
    si "「Even if you say that,{p}\ \ I still don't like getting wet... 」"

    show ko 301 at move_center(0.5)
    
    ko "「Come on, we've been waiting,{p}\ \ a long time to go to the beach. 」"
    
    show si 305 at jump_up

    si "「Wait a minute Kounosuke!{p}\ \ My book is getting wet. 」"

    show ko 303 with dis
    
    ko "「Then hurry up and put it down.{p}\ \ Let's get in the water and swim! 」"
    si "「What!? Don't pull on me! 」"
    
    scene beach04 with wipeleft
    
    show ko 301 at midright with wipeleft
    show ko at bobbing

    ko "「See, isn't rocking in the waves fun? 」"
    
    show si 305 at center
    show si at bobbing
    with wipeleft

    si "「Y-yeah... 」"
    ko "「Let's go away from the beach,{p}\ \ where it's deeper. 」"
    si "「Sto-wait! 」"
    
    play sound water01
    show si at shivering

    "Kounosuke swims behind Shin-kun,{p}and pushes on his swim ring."
    "Naturally, this causes him,{p}to go towards the open sea."
    si "「Kounosuke! D-don't grab my foot! 」"
    ko "「Look, splash, splash! 」"
    si "「N-no! Sto-stop it! 」"
    "Shin-kun's shouting gets gradually weaker."

    hide ko with wipeleft
    
    si "「K-Kounosuke.{p}\ \ T-take me back already.{p}\ \ Kouno... 」"
    "Then, Shin-kun looks like,{p}he sees what's coming."
    "Kounosuke pushes harder,{p}than he means to on his swim ring,{p}and disappears before I know it."
    "Even thought it looks like the open sea,{p}the depth is only a little less than one meter."
    "This is usually a place,{p}where your feet can touch the bottom."
    "It seems his swim ring,{p}gets away from him for a little bit."
    "I think he's all right but Shin-kun...{p}doesn't move an inch.{p}Worried, I approach him."
    fn "「Shin-kun? 」"
    si "「[fn]... h-help me. 」"
    "He grabs tightly on to his swim ring, shaking.{p}The usually cool Shin-kun has teary eyes,{p}and asks me for help in a trembling voice."
    fn "「Y-you'll be okay.{p}\ \ It's not that deep. 」"
    si "「I-impossible... 」"
    "Shin-kun shakes his head and talks,{p}in a barely audible voice.{p}Th-this is scary."
    "Still, he's not where it's deep enough,{p}to go over his head."
    
    play sound water_splash
    hide si with wipe_down

    si "「Wah. 」"
    "His swim ring is losing balance,{p}and it looks like,{p}he's standing on the water."
    si "「H-hur-hurry. 」"
    "As though he's clinging to a flying donut,{p}he gets back to his original position,{p}and I pull him back to the beach."
    
    scene black with Dissolve(1)
    
    scene beach01
    show ko 305 at midright
    show si 310 at midleft
    with Dissolve(.7)

    ko "「Err-sorry, sorry.{p}\ \ My hand slipped a little. 」"
    si "「... 」"

    show ko 301 with dis
    
    ko "「Shin? 」"
    
    show si 312 big at farleft_big with dis 
    pause .1
    play sound bom35
    hide si with wipe_right

    si "{size=+30}「IDIOT! 」"
    
    show si 307 at midleft with dis
    pause .1
    hide si with wipe_right

    "Shin-kun runs off, crying."

    show ko 305 with dis
    
    ko "「... 」"
    fn "「...Kounosuke, will you give him\n\ \ a better apology later? 」"

    show ko 307 with dis
    
    ko "「Y-yeah...{p}\ \ ...I was just joking around a little. 」"
    "A little, huh?{p}That's still not a good reason."

    jump beach07_ridehome 
   
######################################    
label beach07_juuichi:

    if juuichi_hate == True:
        "...{p}It's no good, Juuichi-san is avoiding me.\nI'd better hang out with someone else today."
        jump beach_choice07
    else:

        $ event_name = _("Reckless, Let's Go! Paradise")
        $ focus_character = "juuichi"
        $ love_juuichi += 1
        
        scene black with sdis
        pause .2
        scene beach01 with Dissolve(.5)
        
        "The blue sea! White clouds!{p}And the shining sun!"
        "The weather today is just right for the beach.{p}For no reason, I nod my head."
        "The water's surface brilliantly glitters,{p}from the reflected rays of the sun."
        "In the open water I see the yacht,{p}that we saw from the bus."
        "On the sandy beach,{p}families leisurely collect shellfish."
        fn "「Now, let's have fun today! 」"
        "Oh! As if to say that,{p}I cheerfully thrust my right hand to the sky."

        show ju 001 at center with wipe_right
        
        ju "「...Before that, help me find\n\ \ a place to put the luggage. 」"
        "Suddenly, Juuichi-san's face appears at my side."
        "As he says that,{p}he looks around the area restlessly,{p}it seem there's no other choice besides me."
        "...That's weird.{p}I thought everybody was there just now."
        fn "「Oh, where's everybody else? 」"

        show ju 008 with dis
        
        ju "「...They left their bags behind,{p}\ \ and went to change. 」"
        fn "「What!? 」"
        "So that means Juuichi-san is settling with me?"
        "I painfully understand\nthat feeling of wanting to go play,{p}but everybody just impatiently left."
        "Usually we're like a big family."
        "With just two of us working,{p}I'll collapse from exhaustion\nbefore I can have fun."

        show ju 001 with dis
        
        ju "「...Well, let's do it. 」"
        fn "「Are you serious? 」"
        ju "「There's no use in relying,{p}\ \ on those who are not there. 」"
        "Ooh, do I not have any choice...?{p}I don't want to pointlessly waste my summer,{p}I should just quickly go and change my clothes."

        show ju 006 with dis
        
        ju "「...Are you running away? 」"
        "Juuichi-san puts his hand on my shoulder,{p}and looks into my eyes."
        "...Ooh, okay, I understand.{p}I sigh and look at all the bags,{p}that have been left there."
        
        scene black with Dissolve(.5)
        pause 1
        scene beach03 with Dissolve(1)

        "We do various things like spread out the beach mat,{p}and we put together three umbrellas."
        "I blow into the swim rings,{p}and rubber boat, until I'm about to die."
        "After a full 15 minutes,{p}we finally complete our base...{p}Err... place to put our luggage."
        "...I'm dripping with sweat,{p}before I even get to swim.{p}It's a good thing I brought an extra shirt."
        "Juuichi-san is also extremely sweaty,{p}his chest is soaked with sweat."
        "While wiping my forehead with the arm of my t-shirt,{p}Kouya, who had just changed into his bathing suit,{p}leisurely calls out to us."

        show ka 302 at center with wipe_right
        
        ka "「Oh, it's already done? 」"
        fn "「... 」"
        "I give Kouya a scornful gaze.{p}{nw}"
        show ka 305 with dis
        extend "His eyes immediately stare off in another direction.{p}He had this planned out from the beginning, didn't he?" 
        "Just according to plan."

        show su 302 at midright with wipe_right
        
        su "「Wow, the floats are already filled up! 」"
        "I take a stance to give Kouya,{p}his well-deserved punishment,{p}but Shun-kun runs up from behind."
        "Crestfallen, I collapse from exhaustion."
        "Shun-kun sets his butt,{p}right into the center of the swim ring,{p}and shouts with delight."
        "...That destructive power is tremendous."
        "I look away and supress my nosebleed,{p}by pinching my nose,{p}and looking up at the sky."

        show si 304 at farleft with wipe_right
        
        si "「Good work, both of you. {p}\ \ We saw you over here, hurry up and get changed.{p}\ \ There's an old changing room over there."
        "Shin-kun, who is also in his bathing suit,{p}urges us to get changed."
        "Althought I frown,{p}he's probably saying that,{p}because of our heavy sweating."
        
        scene beach03 with wipe_right
        show ju 201 at center with wipe_right

        ju "「We should.{p}\ \ ...Let's go. 」"
        "Saying that, Juuichi-san briskly walks away,{p}with a full set of clothes."
        fn "「Oh, wait up Juuichi-san! 」"
        "I chase after him from behind in a hurry.{p}Then, talk to Juuichi-san along side him."
        
        scene beach02 with wipeleft
        show ju 201 at center with wipe_right

        fn "「Do you have any idea,{p}\ \ where the changing room is? 」"

        show ju 203 with dis
        
        ju "「...It's probably that. 」"
        "He points his finger straight ahead.{p}That causes me to look ahead."
        "It's just like Shin-kun said,{p}there stands a changing room in name only,{p}as it's more like a dilapidated hut."
        fn "「It sure is run-down. 」"
        ju "「It's better than nothing. 」"
        "While talking, Juuichi-san and I,{p}enter the changing room."

        hide ju with wipe_right
        
        "I look around inside.{p}There are shelves to temporarily put your stuff on."
        "And also a screen that's so torn up\nit might as well not be there."
        "...This place hasn't betrayed my expectations."
        "Juuichi-san puts his belongings\non the appropiate shelf."
        "I take out my bathing suit,{p}and excitedly take of my clothes."
        "I intermittently steal sideways glances.{p}...Nay, I observe."
        "...Look at how much my childhood friend has grown.{p}This is just because I know him!{p}There isn't any ulterior motive!"
        "Wait, who am I making excuses for?"
        "Juuichi-san doesn't seem to be aware of my eyes.{p}He takes off his tank top, becoming half-naked."
        
        play sound changing
        show ju 103 big at center_big with wipeleft 

        "Gulp. {p}I swallow my saliva without thinking."
        "There are firm muscles,{p}around his shoulders and arms."
        "I'm a little concerned about his fat stomach,{p}but when it moves I can see some muscle."
        "Even though he's not completely muscular,{p}his body can best be described,{p}as a judo practitioner's physique."
        "In my mind, I admire it.{p}Besides, I personally think that,{p}muscle with a little fat is sexy..."
        "No, it's nothing, yeah."
        "To see my childhood friend completely grown up,{p}and naked I anguishedly try to..."
        ju "「[ln], is something wrong? 」"
        "Juuichi-san calls out to me."
        fn "「N-no, nothing! 」"
        "He tilts his head.{p}I thought he was about to say something,{p}but he puts his hand on his jersey."
        "While taking off my t-shirt,{p}I look to the side again."
        "Then, Juuichi-san takes his pants off,{p}and gives me a shock."
        fn "「Ju-Ju-Ju-Juuichi-san,{p}\ \ i-i-is that? 」"
        
        hide ju
        show ju 401 at center
        with dis

        ju "「What? 」"
        "My eyes drop down below Juuichi-san's abdomen.{p}Then I let out a gasp."

        show ju 404 with dis
        
        ju "「Is this unusual?{p}\ \ It's a fundoshi. 」"
        "It is.{p}Juuichi-san has a fundoshi."
        "I can't take my eyes,{p}off of that awfully thick bulge."
        "It seems to be squeezed...{p}pretty tight in there,{p}doesn't it?"
        fn "「...I didn't expect there\n\ \ to be any fundoshi around here. 」"

        show ju 401 with dis
        
        ju "「Well, probably not.{p}\ \ I started wearing one\n\ \ when I entered high school. 」"
        "That's right, when I try to think back\nto when we were kids,{p}I don't recall him ever wearing one."
        ju "「It's surprisingly nice,{p}\ \ and it's comfortable around my tail. 」"
        
        hide ju with wipeleft

        "Juuichi-san turns his back to me.{p}The string creeps around his body,{p}and draws a T on his plump butt."
        "...There's no level for this hotness!"
        "That's right, I should count my prime numbers!{p}2, 4, 6, 8... Wait, those are even numbers,{p}aren't they!?"
        "While somehow pacifying\nmy lower body's reaction,{p}I observe Juuichi-san's buttocks."
        "The string is tightened,{p}around the base of his tail."
        "It seems with other underwear,{p}there's a hole to put it through,{p}and getting the right fit isn't very easy."
        "...Oh, I see."
        "While I'm admiring him,{p}Juuichi-san occasionally moves around,{p}his short tail."
        "Freedom of movement is probably its appeal."
        "...Pfft."
        "This is already too awesome,{p}and now he's not hesitating,{p}to do something like that."

        show ju 404 at center with wipe_right
        
        ju "「H-hurry up and get changed. 」"
        "Juuichi-san reaches his hand around him,{p}and fumbles around with something.{p}It looks like he's untying his fundoshi."
        "This means that..."
        "It happens before I can comprehend,{p}what's going on."
        "Gently, the fundoshi that was covering...{p}his private parts falls on the floor."

        show ju 101 with dis
        
        "N-no matter how you put it,{p}Juuichi-san's too defenseless...!"
        "Without thinking, I stare right at that part."
        "...Although there are many differences,{p}between humans and beastmen,{p}and differences in our stature."
        "It exceeds my length and thickness,{p}isn't that a little unfair?"

        show ju 106 with dis
        
        ju "「...Where are you looking? 」"
        fn"「Uh. 」"
        
        play sound puu79_b

        "Thud. {p}His fist falls on my head. {p}I rub my forehead while revealing my thoughts."
        fn "「Juuichi-san, it's very impressive. 」"

        show ju 112 with dis
        
        ju "「...Is that so? 」"

        hide ju with wipeleft
        
        "In what way did he take what I said?{p}Juuichi-san quickly turns away,{p}and puts on his bathing suit."

        show ju 501 at center with dis
        
        ju "「...Have you still not changed yet? 」"
        fn "「Oh, sorry. 」"
        "I quickly take off what I was wearing,{p}and put on my battle suit."
        "Of course Juuichi-san,{p}is going to guard his eyes.{p}After a show like that, go ahead."
        "Man is a creature,{p}that is always particular about size.{p}...I tell that to myself in vain."
        fn "「L-let's go! 」"
        "I regroup and shout loudly."
        ju "「... 」"
        "...?{p}No reply. {p}Juuichi-san is still staring at me."
        "I look around my body,{p}to see if there's something strange,{p}but I can't find anything."
        "I speak to Juuichi-san."
        fn "「Juuichi-san, is there something wrong? 」"

        show ju 503 with dis
        
        ju "「...Oh, sorry. 」"
        fn "「You're dissapointed,{p}you couldn't see mine... 」" 

        show ju 501 with dis
        
        ju "「That's not it. 」"
        fn "「Then hurry up and... 」"
        "That was a joke.{p}...Let me at least say the end of it, please."
        ju "「S-stop fooling around and go. 」"
        fn "「All right... 」"
        "With the stuff we brought at out sides,{p}we head out to the beach."
        
        scene beach01 with wipe_down 

        fn "「...So, What are you going to do?{p}\ \ A little bit of swimming? 」"
        "Making a shifting sound,{p}while walking on the sand,{p}I throw out a topic of discussion"

        show ju 501 at center with wipe_right
        
        ju "「...Hm, how about watermelon splitting? 」"
        fn "「Oh, that's definitely something,{p}\ \ you do at the beach. 」"
        "...Wait, did we bring any watermelon?{p}I ask him that question."
        ju "「I didn't overlook that. 」"
        "He returns with a downright surprising answer."
        "As expected of Juuichi-san.{p}He wasn't just showing off\nwhen he patted his backpack."
        ju "「I put it in the cooler,{p}\ \ we can eat it when it gets cold. 」"
        "...It's already good enough."
        "While talking, we come back to our spot,{p}and immediately start preparing."

        show ju 503 with dis
        
        ju "「Kuroi, a moment please? 」"
        "Noticing Shin-kun using his backpack,{p}as the back of a chair and reading,{p}Juuichi-san speaks to him."

        show si 301 at farright with wipe_right
        
        si "「... 」"
        "With a fleeting glance,{p}Shin-kun creates a space between him\nand the backpack."
        "To make sure he doesn't get in the way,{p}of Juuichi-san's work,{p}he puts down the book he was reading."

        hide si with wipe_right
        
        ju "「Excuse me. 」"
        "Juuichi-san bends his large body over,{p}and sticks his hand into the backpack,{p}he begins rummaging around."
        "One small sheet.{p}This is what we'll put the watermelon on."
        "One cooler.{p}This is what the watermelon,{p}was being stored in."
        "One wooden sword.{p}...He even brought one of those?{p}Juuichi-san is frightening."
        ju "「...Is this it? 」"
        "A few minutes later.{p}Finished setting up the watermelon splitting,{p}Juuichi-san takes a short rest."
        
        scene beach02
        show to 310 at center
        with wipeleft
        
        to "「All right, let's get started! 」"
        "Torahiko suddenly calls out from the side.{p}Where the heck did he come from?{p}Where was he up until now?"

        show to 301 with dis
        
        to "「It's fine guys,\n\ \ don't worry about it! 」"
        "He opens his big mouth and laughs."

        show su 302 at farright with wipe_right
        
        su "「I want to split the watermelon too! 」"

        show ka 302 at midright behind to with wipe_right
        
        ka "「Oh, that looks like fun doesn't it? 」"
        "One by one, more people show up.{p}...This must be the immense power of food."
        
        scene beach02 with wipe_right

        "So, Juuichi-san and I, Torahiko,{p}and Kouya, and then Shun-kun,{p}are going to split the watermelon."
        "I asked Shin-kun,{p}but he mildly turned me down.{p}Just to look good or something."
        "I think it would actually be more fun,{p}if he joined...{p}Oh well. It would be bad to force him."
        "We play rock-paper-scissors,{p}to determine the order we go."
        "It's Shun-kun, Kouya, me,{p}Torahiko, and then Juuichi-san."

        show ka 302 at center with wipe_right
        
        ka "「Here's the blindfold. 」"
        "Kouya hands over a towel to Shun-kun.{p}Shun-kun says thank you,{p}then tightly ties the towel to mask his eyes."

        show ju 501 at farright with wipe_right
        
        ju "「Take this. 」"
        "Juuichi-san lets Shun-kun,{p}take a hold of the wooden sword."
        "His body staggers when he carries it.{p}The way he sways side to side worries me."
        "...Hmm, will he be okay?{p}I hope he doesn't trip half-way through."
        
        scene beach01
        show to 301 at midright
        show su 301 at center 
        with wipe_right

        to "「Come on, let's spin! 」"
        "As soon as he says that,{p}Torahiko forcefully rotates Shun-kun around."
        
        show su 306 at spinning                
        play sound swing30 loop

        su "「Wawawawawa! 」"
        fn "「...Torahiko, don't overdo it. 」"
        
        show to 310 with dis
        
        to "「I know! 」"
        "Unexpectedly, the speed at which he spins,{p}Shun-kun doesn't drop.{p}...I really wonder if he understood."
        
        stop sound fadeout .3
        hide su
        show su 306 
        with dis

        su "「The worle world's spinning... 」"
        "After being spun about 20 times,{p}Shun-kun is finally let go."
        "His gait is as unsteady,{p}as a drunken old man's."
        "He repeatedly staggers,{p}from one side to another."
        "Reminds me of Tatsu-nii."

        show to 306 with dis
        
        to "「...Did I spin him too much? 」"
        "You're slow to notice that, Torahiko."

        show ju 501 at farright behind to with wipe_right
        
        ju "「Kodori, go straight forward. 」{w} {nw}"
        
        show su 306_stagger at move_farright(3)

        "Relying on Juuichi-san's words,{p}Shun-kun totters towards the watermelon."

        show ka 302 at farleft behind su with wipe_right
        
        ka "「Right, a little more to the right. 」"
        fn "「Too far!{p}\ \ Get a little back to the right! 」"

        show to 301 with dis
        
        to "「There, keep going straight ahead! 」"
        
        show su at move_center(3)

        "With everybody's guidance,{p}Shun-kun gets right up to the watermelon."
        ka "「Shun, right there! 」"

        show su 306 with dis
        
        "At the sound of his voice,{p}Shun-kun swings the sword down."
        "He's going right on target.{p}Is this going to end with the first person?"
        "Swoosh."
        "Shun-kun loses his balance,{p}and completely misses the watermelon.{p}The sword flies off somewhere."

        show to 306 with dis
        
        to "「Oh jeez... 」"
        "Torahiko can't look,{p}and places his palm on his forehead."

        show su 303 with dis
        
        su "「I messed up at the end... 」"
        "Shun-kun removes the blindfold,{p}and sadly looks towards the watermelon."
        "The rotund, green form of it,{p}is no longer a tasty snack, but rather,{p}it is only a reminder of his failure."
        
        show ju 503 with dis

        ju "「You almost had it. 」"
        ka "「Well, maybe you won't get so dizzy,{p}\ \ a second time. 」"

        show su 302 with dis
        
        "Shun-kun's face brightens,{p}when he hears Kouya's words."
        to "「Oh, what's with this...{p}\ \ premature celebration? 」"

        show ka 305 with dis
        
        ka "「Oh... 」"
        "Kouya scratches his head,{p}with embarrassment."
        "...Huh, when he says that,{p}I wonder what's going to happen next."
        "I have no idea."
        
        scene beach01 with wipe_right
        show ju 501 at center with wipe_right

        ju "「Next is Kouya's turn. 」"
        "Shun-kun excitedly hands over the blindfold,{p}and sword to Kouya.{p}He begins to prepare."

        show su 302 at midleft with wipe_right
        
        su "「Kouya-san, please do your best! 」"

        show ka 301 at farright with wipe_right
        ka "「Yeah. 」"
        
        scene beach01
        show to 301 at midright
        show ka 301 at center 
        with wipe_right
        
        to "「Right, looks like you're all ready! 」"
        
        show ka 305 at spinning with dis
        play sound swing30 loop

        "Just as he did with Shun-kun,{p}Torahiko vigorously spins Kouya."
        "...{p}...{p}..."
        "...Does he needs to spin him that many times?"
        
        show to at jump_up

        to "「Spin spin spin! 」"
        ka "「Don't you think that's enough spinning!? 」"
        to "「No, not yet! 」"
        "Torahiko completely ignores him.{p}Kouya squeezes out those faint words."
        to "「...Whew. Is that enough? 」"
        
        stop sound fadeout .5
        hide ka 
        show ka 305 at center 
        with dis
        #!#Stop the spinning animation

        ka "「B-Bastard...{p}\ \ I-I'll remember this... 」"
        "Torahiko finally gives his hands a rest,{p}and Kouya timidly states his words."
        fn "「Kouya, are you all right? 」"
        ka "「I'm feeling a little sick... 」"
        "After being spun that much,{p}and for that long,{p}anybody would feel that way."
        "If it were me,{p}I'd sit down somewhere."
        "Kouya's body sways back and forth a lot,{p}and each time it looks like,{p}he's going to lose his balance."
        "He steps his foot down,{p}to try to not fall over."
        "Through sheer willpower,{p}Kouya deals with splitting the watermelon."
        "Still, it ended with the swing,{p}missing the direction of the watermelon."
        to "「I knew it was going to end like this... 」"
        "Torahiko shrugs his shoulders.{p}Kouya gives Torahiko a glare,{p}then hands the blindfold and sword."

        show ka 307 with dis
        
        ka "「Please destroy my rival... 」"
        fn "「Y-your rival... 」"
        
        scene beach01
        show to 301 at center
        with wipe_right

        to "「N-next is [fn]'s turn! 」"
        "At Torahiko's words,{p}I hide my eyes with the towel."
        
        scene black with sdis #!#Change to circling outwards
        play sound changing
        pause 3

        to "「Okay, ready to spin? 」"
        "Torahiko places his hands,{p}on my shoulders."

        play sound swing30 loop
        
        "...{p}..."
        "Ah, this is faster than I imagined.{p}I think while spinning."
        "...{p}..."
        "As expected, my head feels dizzy.{p}I ask Torahiko to stop."

        stop sound
        
        to "「Already?{p}\ \ That's unexpectedly sloppy. 」"
        fn "「No, I don't think,{p}\ \ that's the problem... 」"
        "With my body moving unsteadily,{p}I think I muttered that,{p}in Torahiko's direction."
        
        play sound step01
        pause 1.5

        su "「[fn]-san, it's right ahead. 」"
        ka "「No, right, it's to the right. 」"
        to "「It's to the left!{p}\ \ [fn] go left! 」"
        ju "「Go in the direction your feet lead you. 」"
        "Juuichi-san, I think that goes against,{p}the spirit of watermelon splitting."
        "Still, I wonder with all these...{p}scattered directions."
        "I have no idea which one to follow."
        "For now, I'll just go in the direction,{p}I think the watermelon is."
        ka "「Hey, that's the wrong way. 」"
        to "「Keep going that way, [fn]! 」"
        su "「Wah, [fn]-san it's not over there! 」"
        "...{p}I follow the majority rule,{p}and correct my angle."
        to "「...Tch. 」"
        fn "「...Torahiko, I just now heard,{p}\ \ you clicked your tongue. 」"
        to "「No, that was just your imagination. 」"
        "Torahiko tries to whistle,{p}to cover up his cheating."
        "Isn't that the same,{p}as confessing the truth?"
        "Okay, from now on,{p}I'll ignore Torahiko's navigation."
        "... {p}...{p}..."
        fn "「Ultra Dragon Fang Sword!{p}\ \ Slice it in two! 」"
        
        play sound swing40
        
        scene white with slashing
        scene black with slashing
        
        #!#There is a special scene transition here that makes it look like it's being sliced, need to check files

        "With a pointless yell,{p}I swing my sword down."
        
        play sound bosu32
        
        "Thump.{p}Unfortunately, that isn't the response,{p}of the watermelon splitting."
        
        scene beach02 with sdis

        "I remove the blindfold,{p}to check the position of the watermelon."
        "It seems I'm too far,{p}from smashing it."
        "I scatter the sand in regret of this result,{p}and drop my shoulders in dissapointment."

        show to 301 at center with wipe_right
        
        to "「Don't worry about it [fn]!{p}\ \ Because I'm gonna slice the watermelon open! 」"
        "I hand over the blindfold and sword,{p}to a very enthusiastic Torahiko."
        
        hide to with wipe_right
        
        show ju 501 at midleft
        show to 301 at center 
        show su 301 at midright
        with wipe_right
        
        pause .1
        
        show su 305 with dis

        su "「Are you going to spin? 」"

        show ju 502 with dis
        
        ju "「...Have you prepared yourself? 」"
        "Both of them look like they're enjoying this.{p}Did I just sense something disturbing from them?"
        to "「...Please be gentle. 」"
        "Torahiko has a very timid tone.{p}...Where did all that power he had,{p}up till now go?"
        
        play sound swing30 loop
        show to 308 at spinning with dis 

        "When Torahiko puts on the blindfold,{p}Shun-kun borrows the support of Juuichi-san,{p}to carry out the spinning."
        "From an outside perspective,{p}it looks as if Shun-kun and Juuichi-san{p}are a parent and a child having fun."
        "But if I were to say that,{p}Juuichi-san would throw me."
        "Watching the two of them spin Torahiko,{p}Kouya approaches me from the side,{p}and quietly whispers."

        scene beach01
        show ka 307 at center
        with wipeleft
        
        ka "「Hey, [fn], want to tell him,{p}\ \ the opposite directions for revenge? 」"
        fn "「...Isn't that against the rules? 」"

        show ka 302 with dis
        
        ka "「Didn't Torahiko break the rules? 」"
        "...He did.{p}He spun Kouya like crazy,{p}and then he mislead me..."
        fn "「...All right. Let's do it. 」"

        show ka 303 with dis
        
        ka "「Now you're talking. 」"
        "Kouya gives me a wink."

        stop sound
        
        "Good timing too,{p}Torahiko has just begun to walk."
        "Although he seems confident in his strength,{p}when it comes to his feet,{p}he's meandering from side to side."
        
        scene beach02
        show su 305 at farleft
        show to 306 at midright
        with wipe_right

        su "「Keep going that way... 」"
        fn "「Torahiko, go the other way,{p}\ \ the other way! 」"

        show ka 301 at farright with wipe_right
        
        ka "「Don't you have any sense of direction?{p}\ \ It's the exact opposite way. 」"

        show su 304 with dis
        
        "At our unexpected yelling,{p}Shun-kun blinks at us in surprise."
        "He doesn't seem to have any idea,{p}of what we're doing."
        "Sorry Shun-kun, this is our form of justice...!"
        "Torahiko quickly turns around,{p}and goes in the opposite direction,{p}of the watermelon."
        "Kouya and I look at each other and grin."
        "When Juuichi-san looks at us,{p}he sighs deeply.{p}It looks like he doesn't blame us."
        "... {p}... {p}..."
        fn "「Torahiko, now! 」"
        to "「Let's go go go! 」"
        "Torahiko swings down the sword,{p}with all the strength he can muster."
        "Not in front of the watermelon, of course.{p}It's... driftwood."
        
        play sound hit51
        show to 305 at jump_up

        "Clunk!"
        to "{size=+15}「...YEEEEEEOW! 」" 
        "Torahiko drops the sword,{p}and shakes his hands around,{p}while jumping up and down."

        show ka 303 with dis
        
        "Kouya and I give each other a bro-fist.{p}The sound it makes me feel great."
        "I'm making a note here,{p}huge success."
        
        scene beach02
        show to 306 at midleft
        with wipe_right

        to "「[fn], Kouya, you jerks...! 」"
        "He glares at us while blowing his hands.{p}There are tears in his eyes."

        show ju 501 at midright behind to with wipe_right
        
        ju "「Are you satisfied? 」"
        ka "「Yeah. 」"
        fn "「You bet! 」"
        ju "「Tora, you're not going to forget,{p}\ \ why they did that? 」"
        to "「...I understand! 」"
        "Torahiko humphs and turns away.{p}He's in a completely bad mood now.{p}...D-did we go a little too far?"
        fn "「Last up is Juuichi-san. 」"
        ju "「Okay. 」"
        "Juuichi-san gets the watermelon splitting set,{p}from Torahiko and puts the blindfold on."
        
        scene beach02
        show to 306 at midright
        show ju 501 at center
        with wipe_right

        "With a discouraged look on his face,{p}Torahiko starts spinning Juuichi-san's body."
        fn "「Torahiko, don't overdo it,{p}\ \ if you don't want to receive,{p}\ \ one of Juuichi-san's techniques... 」"
        
        show to 305 with qdis
        show to 306 with dis

        to "「...Oh. 」"
        
        play sound swing30 loop
        show ju at spinning

        "There was a slight delay,{p}before he replied."
        "Is he trying to provoke Juuichi-san's temper?{p}And it doesn't look like he's thought,{p}of a counter-attack."
        "Even though he received that firm punishment,{p}at the welcoming party..."
        "Torahiko, how long,{p}have you had that daredevil personality?"
        
        stop sound fadeout .5
        hide ju
        show ju 501 at center
        with dis

        to "「Senpai, that should be enough. 」"
        "Reluctantly holding his tail,{p}Torahiko finishes up by giving a push,{p}to Juuichi-san's back."
        
        show su 301 at farright behind ju with wipe_right

        su "「Juuichi-san, go straight! 」"
        show to 301 with dis
        show ju 501_stagger

        to "「A little to the right, right! 」"

        show ka 301 at farleft behind ju with wipe_right
        
        ka "「A little to the left? 」"
        fn "「Juuichi-san, straight! 」"
        "I shout so that my voice{p}won't lose out to everybody else's."

        show su 303 with dis
        
        su "「Wah, please go back a little! 」"

        show to at jump_up
        
        to "「Keep going straight! 」"

        show ka 302 at jump_up
        
        ka "「Straight, straight. 」"
        fn "「A little more to the right. 」"

        show to 305 at briefzoom
        
        to "「Woah, too far!{p}\ \ More to the left! 」"
        
        show su 301 at jump_up
        
        su "「It's left, please go more to the left. 」"
        fn "「Juuichi-san, make an adjustment to the left! 」"
        
        show ka 301 at jump_up
        
        show ju at move_midleft(2)

        ka "「It's a little more to the left. 」"

        show to 301 at jump_up
        
        to "「Keep going that way! 」"
        su "「Juuichi-san, straight ahead! 」"
        
        show to 301 at jump_up

        to "「More to the right, right! 」"
        fn "「Just a tiny bit more to the right! 」"
        
        show ju at move_center(2)

        "...Hm?"
        "For some reason,{p}it feels as if he's only,{p}following my directions."
        fn "「Juuichi-san, left! 」"
        "I try shouting the appropiate direction.{p}Juuichi-san changes his course to the left,{p}just as I said. I yell out in a hurry."
        fn "「Just a little more to the right! 」"
        
        show ju at move_midright(2)

        "Juuichi-san changes his body's direction.{p}...Ooh, this is a serious responsibility.{p}I'm terrified."
        "...{p}...{p}..."
        fn "「Juuichi-san, now! 」"
        "I give my final instruction.{p}Juuichi-san readies his sword.{p}Then..."

        show ju 506 at jump_up

        ju "「...HA! 」"
        "With a sharp exhale,{p}he swings the sword,{p}directly onto the watermelon."
        
        play sound hit78

        "Crack!{p}The watermelon that was once a single sphere,{p}had become 2 perfect domes."

        show su 302 with dis
        
        su "「Wow, Juuichi-san is amazing! 」"

        show ka 303 with dis
        
        ka "「...Well done. 」"
        
        #!#Torahiko sprite change?
        
        to "「Jeez, in the end, senpai just had to...{p}\ \ have that deliciouness, didn't he? 」"
        fn "「As expected of a martial artist.{p}\ \ The watermelon is in two beatiful equal parts. 」"
        "We run over to Juuichi-san's side,{p}and tell him how impressed we are."
        "He takes off the blindfold,{p}to check out the state of the watermelon,{p}and seems to be a little surprised."

        show ju 501 with dis
        
        ju "「That's a pretty clean cut.{p}\ \ ...I wonder if it was because...{p}\ \ of those precise instructions? 」"
        "...Huh?{p}Is he talking to me?"
        "I look over at Juuichi-san,{p}and our eyes perfectly meet.{p}He immediately turns away, though."
        ju "「Hey, Kuroi.{p}\ \ Go get the knife out of my bag. 」"
        "He speaks to Shin-kun."
        
        scene beach02 with wipeleft

        "Hmm, maybe he wasn't referring to me...{p}But he did quickly look away."
        "I wonder why Juuichi-san,{p}would say something like that?"
        "...It's no good.{p}The more I think about it,{p}the more confused I get."
        "I decide to just throw up the white flag."
        "When he hears Juuichi-san,{p}calling out to him,{p}Shin-kun puts a bookmark in the book."
        "Then, he opens Juuichi-san's backpack,{p}and pulls out a knife."
        "When I see that Shin-kun,{p}is heading this way,{p}I talk to Juuichi-san."
        
        scene beach01
        show ju 501 at center
        with wipeleft

        fn "「...Juuichi-san, you're always prepared. 」"

        show ju 502 with dis
        
        ju "「Forewarned is forearmed. 」"
        "Juuichi-san has a vague expression,{p}of satisfaction on his face."

        show si 301 at midright with wipeleft
        
        si "「Here. 」"
        "Shin-kun tries to give Juuichi-san the knife,{p}but he stops him."

        show ju 501 with dis
        
        ju "「This would be more suitable for Ooshima. 」"
        si "「...Certainly. 」"

        hide si with wipeleft
        
        "Shin-kun gives the knife,{p}to Torahiko as he's told."
        "That sulleness Juuichi-san had up until now,{p}doesn't concern him at all."
        "Torahiko gives a high-spirited shout."

        show to 301 behind ju at midright with wipeleft
        
        to "「Please leave it to me! 」"

        show ka 305 behind ju at farright with wipeleft
        
        ka "「You're such a simple guy... 」"
        "Kouya stands alone and mutters that."
        
        scene beach01 with Dissolve(1)

        "Torahiko evenly carves the watermelon,{p}and we eat happily together.{p}Even incluiding Shin-kun."
        "I was nervous for a moment,{p}but things settled peacefully in the end."
        "After that we made sand castles,{p}and went swimming."
        "We enjoying bathing in the sea,{p}until the sun began to set."

        jump beach07_ridehome
        
###########################################
label beach07_torahiko:
    
    $ event_name = _("With Torahiko")
    $ focus_character = "torahiko"
    $ love_torahiko += 1

    scene black with sdis
    pause .2
    scene beach03 with Dissolve(.5)
    
    "I wonder what Torahiko's doing..."
    "Knowing him, he most likely,{p}went straight to the water for a swim."
    "But actually, he approaches me.{p}I can't believe he wasn't racing,{p}to be first in the water."

    show to 301 at center with wipe_right
    
    to "「What's up, [fn]?{p}\ \ Are you just gonna sit there and space out?"
    to "Or are you scoping out hot swimsuit girls? 」"
    fn "「Wha-th-that's not it! 」"
    to "「I know, you're not that shameless.{p}\ \ Hurry up and change,{p}\ \ so we can have some fun. 」"
    fn "「You're already done changing?{p}\ \ You're awfully hasty, Torahiko... 」"
    to "「Well yeah, everybody else,{p}\ \ is already done and out playing. 」"
    to "「Look, Juuichi-san's trying,{p}\ \ to be first at something,{p}\ \ isn't it fun running around on the beach!? 」"
    fn "「Huh? 」"
    "Really... everybody's already out,{p}having fun in their bathing suits."
    "Did I just get left behind?"

    show to 306 with dis
    
    to "「Haah, what a pity...{p}\ \ Back then you were always the first,{p}\ \ to finish changing to jump in the water. 」"
    fn "「I-I was...? 」"
    to "「I've been waiting long enough!{p}\ \ Hurry up and get changed, get changed! 」"
    fn "「W-wait a sec,{p}\ \ I'm going to the changing room now. 」"
    to "「Nobody's gonna see you,{p}\ \ just change here. 」"
    fn "「There's no way,{p}\ \ I'm taking anything off right here. 」"
    to "「Are you embarrassed to be seen?{p}\ \ I'll hide you, so it'll be okay. 」"
    fn "「That's not the problem. 」"

    show to 310 with dis
    
    to "「Hmm. 」"
    fn "「What's with that smile you have there? 」"
    to "「Do you not want anybody to see you...{p}\ \ because you have a small dick? 」"
    fn "「I-idiot!{p}\ \ That's not it! 」"

    show to 305 at jump_up
    
    to "「Hmmm!? Maybe it's the opposite,{p}\ \ and you don't want anybody to see,{p}\ \ because it's too big, then!? 」"
    fn "「No! 」"
    to "「That's a relief. 」"
    fn "「In regard to what? 」"
    to "「Isn't that a thing of male pride? 」"
    "Sigh, I don't have much pride to show..."

    show to at jump_up
    
    to "「Well, don't worry about it!{p}\ \ How big it is isn't particularly important. 」"
    to "「...But if you haven't changed at all,{p}\ \ since elementary school,{p}\ \ then that would be a huge problem!"
    to "Dahaha...{p}{nw}"
    play sound bosu31
    show to at jump_up
    extend "Daaaaaaa! 」"
    
    "For his rude behavior,{p}I punish him in the form,{p}of a light body blow to the stomach."
    fn "「I said that's not it. 」"

    show to 308 with dis
    
    to "「Okay... sorry...{p}\ \ I-I won't joke around anymore... 」"
    fn "「I'll go change then. 」"
    to "「Yeah... see you later... 」"
    "He really has no delicacy.{p}It's extremely uncivilized,{p}to be naked outside."
    to "「Dohoho...{p}\ \ He was just like Juuichi-san... 」"
    
    #!#hide window
    scene black with sdis
    pause .1
    scene beach03 with Dissolve(1)

    "After changing clothes,{p}I return to where we were."
    "Torahiko's waving a huge surfboard in his hands."

    show to 301 with wipe_right
    
    to "「Hey, kept me waiting long enough. 」"
    fn "「Sorry, sorry.{p}\ \ Anyway, is that a surfboard?{p}\ \ You're going surfing? 」"
    to "「Yep! They just put rental boards,{p}\ \ in that store. 」"
    fn "「Oh, that's surprising.{p}\ \ I thought for sure,{p}\ \ that you'd be going swimming. 」"

    show to 310 with dis
    
    to "「Swimming is fun too,{p}\ \ but I've been waiting so long,{p}\ \ to go to the beach."
    to "That's not the only way,{p}\ \ to have a good time here.{p}\ \ Look, I rented one for you too! 」"
    fn "「Eh, but I've never...{p}\ \ gone surfing before. 」"

    show to 301 with dis
    
    to "「That's okay, I'll start teaching you.{p}\ \ It feels awesome when you ride a wave. 」"
    fn "「I-I see... I'll give it a try. 」"
    "I wonder if I'll be safe...{p}I've seen it on TV,{p}but it looks pretty hard."
    to "「You'll be fine!{p}\ \ Just let nature take its course. 」"
    "As if seeing straight through my feelings,{p}Torahiko pats both of my shoulders,{p}and laughs loudly."
    "While I would like to try,{p}I don't think I'll be any good at it."
    "But when I hear Torahiko's reassurances,{p}worrying about it seems absurd."
    "There's no use in not giving it a try.{p}All right, I'll do it!"

    scene beach01 with wipeleft
    
    "After some light warm-up exercise,{p}we walk down the the water's edge.{p}The wet sand feels pleasantly cool on my feet."

    show to 301 at center with wipe_right
    
    to "「Oh, I'm getting a good feeling about those waves.{p}\ \ These are perfect surfing conditions. 」"
    fn "「Hey, show me how to do it first.{p}\ \ I want to see how it's done. 」"
    to "「Okay, leave it to me! 」"

    hide to with wipe_right
    
    "He says as he plunges into the sea,{p}splashing about as he swims."
    "He swims fairly far away,{p}then stops, and faces me."
    "Is that the signal he's starting?{p}He displays a great wave on his hand."
    "He puts his stomach on the board then gently paddles,{p}while watching the waves intently."
    "A decent-sized wave,{p}begins a steady approach.{p}Nimbly, Torahiko stands up on his board."
    fn "(It looks a little awkward,{p}but it must feel pretty good,{p}to ride a wave.)"
    "While drawing an S-shaped curve as he moves,{p}a sharp spray of water flies up into the air.{p}This is really cool."
    "On his way back to the beach,{p}Torahiko lowers his foot into the water,{p}and returns with a splash."

    show to 301 at center with wipeleft
    
    to "「It's been a while,{p}\ \ but that was pretty good! 」"
    fn "「That was amazing.{p}\ \ I honestly didn't think,{p}\ \ you were that good at it. 」"
    to "「Heh, heh, I'm not that great!{p}\ \ Well then, [fn],{p}\ \ why don't you try it right now? 」"
    fn "「R-right now? 」"
    to "「Yeah, that way you too shall know,{p}\ \ the joy of surfing. 」"
    fn "「...Wait a minute,{p}\ \ let me take a deep breath. 」"
    "Now it's my turn.{p}Despite that awesome preformance,{p}I'm still nervous."
    "It's been a long time since,{p}I've been to the beach itself...{p}And Torahiko swam pretty far out there..."
    "As I'm thinking,{p}the sand which was so pleasant up until now,{p}becomes cold."
    "It seems as if the sea\nis trying to drag me in.\nMy legs freeze up all on their own."

    show to 310 with dis
    
    to "「Just stick with me.{p}\ \ You'll feel better once I show you,{p}\ \ how simple it is. 」"
    fn "「O-okay... 」"
    "I-I shouldn't be afraid.{p}I won't get anywhere,{p}if I don't step forward."
    "Anyway, with great concentration,{p}I begin to swim using the board."

    show to 305 with dis
    
    to "「Oh hey hey hey!{p}\ \ Are you using that as a kick board? 」"

    show to 301 with dis
    
    to "「First, make sure to not open your legs,{p}\ \ when swimming on the board."
    to "Then just look straight ahead and relax. 」"
    "I-I'm fine...{p}I'm absolutely fine..."
    "I fell off the board several times,{p}but I was somehow able,{p}to get to the open water."
    "Still, because I have someone next to me,{p}someone like Torahiko, I feel quite calm."
    fn "「S-so how do I do this? 」"
    "I should only rely on Torahiko's lecture.{p}I'll try to do what I'm told."
    to "「First you wait for a wave,{p}\ \ while paddling around,{p}\ \ on the sides of the board."
    to "When you see a wave,{p}\ \ that you've got a good feeling about,{p}\ \ stand up quick!"
    to "Then, give a gutsy yell or something. 」"
    "What does he mean by 'or something'...?{p}Even if I get into an aggressive state,{p}I'll still be worried." #fixed a typo, "agressive" -> "aggressive"
    fn "「I don't understand your explanation.{p}\ \ A beginner like me can't just...{p}\ \ catch a wave right away, can he!? 」"

    show to 310 with dis
    
    to "「Just watch me.{p}\ \ If I can do it, you can too! 」"
    fn "「W-wait, hey Torahiko! 」"

    hide to with wipe_right
    
    "As he says that,{p}\ \ Torahiko gallantly rides a wave."

    scene beach04 with dis
    
    "Leaving me alone in the vast sea."
    "Is it just my imagination,{p}or does it feel like I'm...{p}gradually being swept away?"
    "Crap, this is way people drown to death."
    "Feeling my fear building up,{p}I ask Torahiko for help,{p}by wildly waving my hand around."
    "On the shore,{p}Torahiko doesn't gets what I mean,{p}and waves back obliviously."
    to "「Yo! [fn]!{p}\ \ You hurry up and get back here too! 」"
    "Damn, this is bad isn't it?{p}I guess it doesn't matter,{p}I'll try it!"
    "I'll just do what I saw Torahiko do..."
    "Without any feeling,{p}I get on the board and wait for a wave."
    "I hope I can get up quick enough,{p}when I meet the wave."
    "I mean, Torahiko got up,{p}on his feet so suddenly.{p}And then after that, he yelled out..."
    "In the meantime,{p}my body suddenly rises gently."
    fn "(Oh, a wave I have a good feeling about...?)"
    "It's already gotten here!{p}I desperately try to recall,{p}the visual image of Torahiko standing."
    "I draw my feet in towards my body,{p}in order to get myself standing."
    "The board gradually increases height,{p}as it's being washed away by the wave."
    "I stand up on the board,{p}and let the momentum take me."
    fn "(Huh, I'm... standing?)"
    "For a moment I think I am, at least.{p}"
    "The wave rapidly gets higher.{p}to the point where it springs up,{p}to a white cap."
    "It sends my body into the air."
    
    scene beach01 with Dissolve(2)
    pause 1
    
    play sound waves2
    pause .3
    
    "I'm violently jostled by the wave,{p}with no idea of what's going on."
    "The next thing I know,{p}I find myself lying face-up on the beach."

    show to 310 at center with wipe_right
    
    to "「Awesome, [fn]!{p}\ \ That was quite the wave to go against,{p}\ \ for your first time surfing. 」"
    fn "「Torahiko... 」"

    show to 301 with dis
    
    to "「W-what? 」"
    fn "「Surfing is impossible for me. 」"

    show to 305 with dis
    
    to "「Eh, what's with you all of a sudden?! 」"
    fn "「I just don't have the talent... 」"
    to "「Really?{p}\ \ Didn't you think it was totally cool? 」"
    fn "「... 」"
    "I wasn't blessed with a coach...{p}I think about saying that sarcastically.{p}...Nah."
    "When Torahiko looks at my face,{p}he looks pretty dissapointed,{p}so I decided to keep that in mind."
    "I see an untarnished boyishness,{p}in his eyes that clears away,{p}any anger or resentment."
    "I think Torahiko was planning on teaching me.{p}He's a guy who goes with what he feels,{p}literally, instead of logic..."
    "But I can't do that."

    scene beach04 with dis
    
    "While staring out at the ocean,{p}I suddenly see somebody riding a board,{p}heading this way."
    "A silver gray body shines,{p}as he rides a wave,{p}creating a pure white splash of water."
    fn "(It's Kouya...)"
    "He doesn't make any unecessary movements,{p}as he rides the wave."
    "As Kouya approaches the shore,{p}he draws a big U-shaped curve with his board,{p}making a huge spray of water splash at Torahiko."
    
    play sound water01
    pause .5

    to "「Bwah! 」"
    "The spray forcefully hits Torahiko in the face,{p}causing him to spit out salty water."
    
    scene beach01 
    show ka 303 at midleft
    show to 305 at midright
    with wipeleft

    ka "「Yo. 」"
    fn "「Amazing!{p}\ \ You're also a great surfer, aren't you? 」"

    show ka 301 with dis
    
    ka "「What do you mean by 'also'?{p}\ \ Sorry, we're not even close to the same level. 」"
    "As he says that, Kouya makes sure,{p}to cast a glare right at Torahiko."
    to "「What are you... 」"
    "Sparks always fly when those two meet."
    to "「Hey Kouya.{p}\ \ You just splashed water at me on purpose,{p}\ \ didn't you? 」"

    show ka 302 with dis
    
    ka "「That's right. 」"

    show to at jump_up
    
    to "「That's right!?{p}\ \ Apologize, right now! 」"

    show ka 301 with dis
    
    ka "「Hmph, I'm just speaking on behalf,{p}\ \ of [fn]'s thoughts. 」"
    "What, me?"
    "I wish I could have splashed him or something,{p}but I didn't think about that..."
    to "「Why are you dragging [fn] into this!? 」"
    ka "「Didn't you take off and leave [fn] alone? 」"

    show to 306 with dis
    
    to "「I-I planned that to be an example... 」"
    ka "「[fn]'s still a beginner,{p}\ \ who doesn't know his left from right,{p}\ \ isn't he?"
    ka "You should always stay with him,{p}\ \ keeping him away from danger. 」"
    ka "「What if something happened to him,{p}\ \ while you were away?{p}\ \ What would you have done? 」"
    "Wow... that's a pretty solid argument."
    
    show to at hit_left

    to "「Ugh... 」"
    to "「B-but he stood up on that wave,{p}\ \ so there wasn't any problem in the end! 」"

    show ka 302 with dis
    
    ka "「Regarless of the outcome,{p}\ \ that would have been a serious incident,{p}\ \ had [fn] been injured..."
    ka "How about you give him an apology? 」"
    to "「Guh... 」"
    "With that said, Torahiko falls silent."
    "Usually when those two fight,{p}each of their claims develop,{p}like parallel lines."
    "Then when things get too hot,{p}somebody arbitrates so it's okay."
    "However, I feel that Torahiko is at a...{p}disadvantage this time."
    "Being left alone in the water,{p}certainly did make me nervous."
    "And being carried away by that wave,{p}really could have drowned me..."
    "But I don't mind.{p}I don't think I even want him to apologize."
    "I simply have no idea what I should do,{p}about this uneasy atmosphere."
    "There's nothing that he needs to apologize about.{p}Kouya wouldn't allow me to say that, thought."
    "Now I'm not the 3rd party of this argument,{p}and I'm not standing in the line,{p}of opposition. It's a delicate position."
    "This is troubling... What should I do?"

    show ka 301 with dis
    
    ka "「Why are you so quiet? 」"
    to "「...Shut up. 」"
    "Because of that argument,{p}Torahiko can't come up with a retort."
    "Nevertheless, he obviously can't stomach,{p}the idea of doing what Kouya,{p}ordered him to do."
    "He makes a stern facial expression,{p}from the strain of his stubborness."

    show ka 302 with dis
    
    ka "「Psh, you don't even know,{p}\ \ what [fn]'s thinking."
    ka "How dare you shamelessly,\n\ \ be his coach like that. 」"
    "Laughing through his nose,{p}and leaning his head forward,{p}he provokes Torahiko."
    "The atmosphere is starting to get tense,{p}I feel more and more unpleasant..."
    "It wouldn't be strange if this...{p}touchy situation broke out into a scuffle..."
    fn "「Forget it, why are you two fighting?{p}It's true I was a little scared,{p}but I don't care anymore. 」"
    "Both of them look taken aback,{p}when they realize what I said."
    "Together, they both glare at me.{p}It seems like they've already forgotten."
    fn "「Kouya, you said too much.{p}\ \ Since we went through all this,{p}\ \ to have a good time"
    fn "Let's try to get along a bit better... 」"

    show ka 301 with dis
    
    ka "「[fn]... 」"
    to "「... 」"
    fn "「Well then, I'm going for a swim. 」"
    
    scene beach01 with wipe_right

    "I say no more and raise my hand,{p}with my back turned to both of them."
    "I then carry my board,{p}and get into the water."
    "Somehow, in the flow of adolescent-like drama,{p}it's better to swim out to the open sea.{p}Just don't remind me of not being able to surf."
    "I wonder why I tried to look good like that...{p}Oh well, it's already too late to turn back."
    ka "「[fn], it's stupid for a beginner,{p}\ \ to go riding alone. 」"
    fn "「Oh, Ko-Kouya... 」"
    to "「Yo, have you been caught by the...{p}\ \ charm of surfing or something? 」"
    fn "「And Torahiko too... 」"
    "They talk as if nothing had happened,{p}and greet me like they usually would,{p}giving a small embarrassed laugh."
    to "「This time I'll give you a proper take-off,{p}\ \ and be a reliable teacher! 」"
    ka "「First, you should practice,{p}\ \ with the white caps near the shore."
    ka "Don't force yourself too much,{p}\ \ and steadily step up. 」"
    fn "「All right, hehehe.{p}\ \ I wonder if I can do this right. 」"
    to "「You'll be fine!{p}\ \ Just work your way up! 」"
    ka "「That's my line. 」"
    to "「Shut up! 」"
    fn "「Hey hey, are you fighting again?{p}\ \ ...Jeez. 」"
    "From then on I get lectured,{p}by both Torahiko and Kouya."
    "Though my progress isn't rapid,{p}I am now able to stand on the board."
    "A little while after,{p}I get to the point,{p}when I can ride a wave."
    "Both of them,{p}along with myself,{p}were quite pleased."
    "Unconsciously, they decide,{p}to cross their arms,{p}and strike a triumphant pose,"
    "Then quickly, they turn their faces,{p}away in embarrassment,{p}and try to laugh it off."
    "It seems those two still have something...{p}similar to a good relationship."
    
    #hide window
    scene black with Dissolve(1)
    scene beach01 with Dissolve(.5)

    "When we return to the shore at noon,{p}my body is pleasantly exhausted."

    show ka 303 at midright with wipe_right
    
    ka "「We sure did play a lot. 」"

    show to 306 at midleft with wipe_right
    
    to "「Heh heh, I actually wanted to get out,{p}\ \ into the higher waves,{p}\ \ but today was pretty fun! 」"
    fn "「Both of you can be so energetic.{p}\ \ I couldn't move another step. 」"
    to "「You're so slobby...{p}\ \ A man's body is his capital. 」"
    "Torahiko bangs on my shoulders,{p}laughing loudly."

    show ka 302 with dis
    
    ka "「You really were riding out there,{p}\ \ seeing you look so excited was amusing. 」"

    show to 310 with dis
    
    to "「Humph, it's rare for you to compliment me,{p}\ \ isn't it? Even if you did make me,{p}\ \ do something like swallow sea water? 」"

    show ka 301 with dis
    
    ka "「D-don't get the wrong idea... 」"
    ka "「The way you just force yourself,{p}\ \ through anything is just funny, is all! 」"

    show to 306 with dis
    
    to "「Y-you're joking right?{p}\ \ Why am I embarrassed...{p}\ \ Jeez what a creepy feeling. 」"
    to "「I-if that's the case... Then your...{p}\ \ surfing technique is pretty impressive. 」"

    show ka 305 with dis
    
    ka "「R-really...? 」"
    to "「Y-yeah... 」"
    "This is a strange sight."
    "Just a little bit ago they were fighting,{p}and now they're complimenting each other."
    fn "「Kouya and Torahiko,{p}\ \ I can't tell if your relationship,{p}\ \ is good or bad. 」"
    
    show ka 301 at jump_up
    show to 305 at jump_up

    to "「K-Kouya and I getting along? 」"
    ka "「Don't say something so...{p}\ \ disgusting! 」"
    fn "「There's no need for you two,{p}\ \ to be so serious..."
    fn "It's just the way you looked there,{p}\ \ was much better than...{p}\ \ when you're fighting. 」"

    show to 306 with dis
    
    to "「Ooh... 」"

    show ka 305 with dis
    
    ka "「Hmm... 」"
    "Oops, just when they were starting to forget,{p}I accidentally said something to remind them."
    "I go silent again,{p}and an air of akwardness flows in."
    to "「Y-you know what...? 」"
    "Breaking the atmosphere,{p}Torahiko timidly speaks up."
    to "「About earlier... I'm sorry. 」"
    fn "「It's all right, I don't mind.{p}\ \ It's kind of my own fault, anyway... 」"
    to "「Heh heh, that's okay."
    to "But, you felt a little better,{p}\ \ when you continued surfing, right? 」"

    show to 301 with dis
    
    to "「Also... 」"
    "Torahiko glances over at Kouya and mutters."
    to "「What Kouya said certainly wasn't wrong...{p}\ \ I was also a little too stubborn."
    to "But spraying water at me...{p}\ \ was unacceptable! 」"
    to "「Eh,  what I'm... In other words,{p}\ \ I'm at fault here too."
    to "So when you factor it all in,{p}\ \ it makes it about 50-50! 」"
    
    show to 306 at jump_up

    to "「So...!{p}\ \ I guess you could say...{p}\ \ {nw}"
    show to 305 with dis
    extend "...my bad. 」" 
    "Compared to my time,{p}that apology took...{p}some time to come out."

    show ka 303 with dis
    
    ka "「I also went farther than needed.{p}\ \ I'll honestly apologize for the water.{p}\ \ ...Sorry. 」"
    "To be honest, I also got hit,{p}by that water pretty good too,{p}but..."
    "If I were to say that now,{p}I'd surely be recognized,{p}as the guy who can't read people's moods."
    fn "「So then, I'd say we resolved this.{p}\ \ So is this talk is over...? 」"
    to "「That's right!{p}\ \ If we hang around this any longer,{p}\ \ we'll never move on!"
    to "Let's cheer up! 」"

    show ka 305 with dis
    
    ka "「You change just as fast as ever... 」"

    show to 310 with dis
    
    to "「A cool guy doesn't stick in the past! 」"
    ka "「Jeez...{p}\ \ {nw}"
    show ka 301 with dis
    extend "Well, if [fn]'s pleased with the result,{p}\ \ then it was worth it for us to teach him. 」"
    fn "「But I'm still a beginner compared to you two. 」"
    to "「You're so modest.{p}\ \ I think you we're able to understand a lot,{p}\ \ considering it's for your first time. 」"
    fn "「Really? 」"
    to "「Definitely! In fact...{p}\ \ The Torahiko Association of Surfing,{p}\ \ officially recognizes you as..."
    to "...About 5th grade level! 」"
    fn "「...I'll gratefully accept that. 」"
    "After all, I did pretty well...{p}For my first time, at least."
    "However it seems doubtful I'll get,{p}to where I'm really good..."
    to "「When you get better, {p}\ \ we should go tandem together! 」"
    fn "「T- tandem, huh...{p}\ \ That'd hurt, you'd be grinding up,{p}\ \ against my face! 」"

    show ka 302 with dis
    
    ka "「Stop talking nonsense, Torahiko.{p}\ \ There's nobody here who's eager,{p}\ \ to take a ride with you. 」"

    show to 306 with dis
    
    to "「Really? 」"
    fn "「Hey hey, stop.{p}\ \ You guys can fight,{p}\ \ when we get back to the village. 」"

    show to 310 with dis
    
    to "「All right.{p}\ \ When we get back to the village.{p}\ \ Remember that, Kouya. 」"

    show ka 301 with dis
    
    ka "「Then let's do it. 」"
    "Oh great, they reverted back,{p}to the way they usually are."
    "Their relationship seems to have improved,{p}for the the time being..."
    "But that's just the way things are."

    show to 301 with dis
    
    to "「I'm getting kind of hungry.{p}\ \ Let's go get some food. 」"
    fn "「Sure. 」"
    "Did we decide to go tandem together? {p}I don't really know what tandem means,{p}but I hope I can have fun with Torahiko again."
    to "「What are you talking about?{p}\ \ Are you coming? 」"
    fn "「Huh? 」"

    show ka 303 with dis
    
    ka "「[fn], surfing is really fun.{p}\ \ Now that you've gotten a little better,{p}\ \ do you think you get it? 」"
    to "「Oh! Up next is Great Teacher Torahiko's,{p}\ \ swimming club training."
    to "So prepare for some really hard lessons! 」"
    "Apparently, that's what he has,{p}in mind for me.{p}For now I'm going to eat, though."
    "I'll get to play with him again."
    fn "「All right, next I'm aiming,{p}\ \ to go from grade 5 to 2! 」"

    show to 305 briefzoom 
    to "「What! Isn't grade 2...{p}\ \ a little too sudden? 」"

    show to 306 with dis
    
    to "「Don't you think that's awfully hasty?{p}\ \ I'd even say that for grade 3. 」"

    show ka 305 with dis
    
    ka "「Torahiko, What is your standard for...{p}\ \ dividing grades, anyway...? 」"

    jump beach07_ridehome

    
###########################################
label beach07_ridehome:
    
    $ focus_character = ""
    $ event_name = _("Bus Ride Home")
    stop music fadeout 2.5
    scene black with sdis
    scene bus red with Dissolve(.5)
    play music traffic01

    fn "「Whew, I'm tired... 」"
    si "「Zzz, zzz... 」"
    to "「*Snore*, *snore*... 」"
    "Seems like everyone's asleep.{p}It's been so long since\nwe all went out together."
    "And so long since, I've played so cheerfully."
    ky "「Zzz, Sou... Want to try it? 」"
    so "「...Senpai...{p}\ \ for sure... *snore*... 」"
    "Hmhm, even in their dreams,\nthey're still playing."
    ta "「Sa-Sachiko-san... 」"
    "Hm?"
    ta "「Sachiko-san...{p}\ \ is the dashi for Father's meal done? 」"
    ta "「There's also dust collecting on the window sill. 」"
    ta "「The meal preparations are far from done,{p}\ \ and I wonder if the cleaning is done well enough. 」"
    ta "「Guoooooh, *whistle*...{p}\ \ Like you said, people are truly...{p}\ \ *whistle*... 」"
    "Seriously, who is Sachiko-san?{p}And what's more, did you change roles?"
    ky "「Hey Sou, how's this...?{p}\ \ You like it, don't you? Zzz... 」"
    so "「Aah, I can't...{p}\ \ I can't take that anymore...{p}\ \ *snore*... 」"
    "Just what kind of dream are they having over there?"
    ka "「Zzz... Hey, isn't it all right?{p}\ \ Just for a little bit,\n\ \ nothing bad by doing it. 」"
    ko "「Zzz...{p}\ \ No [fn]... I...{p}\ \ Zzz... 」"
    "And what are those two doing?"
    fn "「It's almost too good to be true,{p}\ \ especially on a day like this.{p}\ \ I wanted to go see everyone again. 」"
    "Outside the window,{p}everything's being dyed red by the setting sun."
    "The sea, the mountains, the sky,{p}everything's the color of orange juice."
    "Somehow I feel like I'm the\nonly one who's been locked up,\non a different world."
    "...Something like that."
    fn "「*Yawn*... I'm sleepy... 」"
    "Since everyone else is sleeping,\nI'm starting to feel it it too.{p}But, I want to stay awake a bit more."
    "We still haven't played enough.{p}I want to be with everyone."
    fn "「Y-You think I'll sleep...{p}\ \ Sleep ...Zzz... 」"
    to "「*Snore* *snore*. 」"
    si "「Fufuu, there really is no helping you, is there...{p}\ \ Zzz, zzz... 」"
    
    hide window
    scene black with sdis
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
    
    jump day08
    #jump day07

    
