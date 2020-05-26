## Day 8

screen tatsukishrine08:
    hbox:
        add "arrow up"
        at shrinebounce1
    hbox:
        add "icon_tatsu"
        at shrinebounce2
    hbox:
        text _("Minasato Shrine")
        xalign .16 yalign .12
        
screen kouyaforest08:
    hbox:
        add "arrow down"
        at forestbounce1
    hbox:
        add "icon_kouya"
        at forestbounce2
    hbox:
        text _("Forest")
        xalign .61 yalign .87
        
screen kounocandy08:
    hbox:
        add "arrow down"
        at marketbounce1
    hbox:
        add "icon_kouno"
        at marketbounce2
    hbox:
        text _("Candy Store")
        xalign .5 yalign .53

screen minasatomap08a():
    add "map"
    add "mapdate"
    imagebutton idle "a icon" hover "icon loop" xpos 164 ypos 104 action Jump("tatsuki08") hovered Show("tatsukishrine08")  unhovered Hide("tatsukishrine08") hover_sound "av/audio/click_008.wav"
    imagebutton idle "a icon" hover "icon loop" xpos 453 ypos 447  action Jump("kouya08") hovered Show("kouyaforest08")  unhovered Hide("kouyaforest08") hover_sound "av/audio/click_008.wav"
    hbox:
        text _("{size=+30}August 8")
        at maptime
        
screen minasatomap08b():
    add "map"
    add "mapdate"
    imagebutton idle "a icon" hover "icon loop" xpos 372 ypos 249 action Jump("kounosuke08") hovered Show("kounocandy08")  unhovered Hide("kounocandy08") hover_sound "av/audio/click_008.wav"
    hbox:
        text _("{size=+30}August 8")
        at maptime


########################################
label day08:
    
    $ renpy.music.set_volume(1.0, 0.0, channel = "music")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound2")
    
    $ day = 8
    $ the_date = _("August 8")
    $ event_name = _("８月8日")
    $ focus_character = ""
    
    window hide
    play music birds_chirping
    
    scene sky01 
    show text _("{size=+130}August 8") at truecenter
    with Dissolve(.5)

    pause 3
    scene black with Dissolve(1)
    pause .4
    
    if  kounosuke_test == True:
        play music "<from 2.5>av/audio/free0422.ogg"
        call screen minasatomap08b
        
    scene hbroom with wipe_corner
    
    fn "「Hmm, what to do today... 」"
    
    play music "<from 2.5>av/audio/free0422.ogg"
    call screen minasatomap08a
    
##############################################
label tatsuki08:

    $ event_name = _("Just another Day for Tatsuki and Torahiko")
    $ love_tatsuki += 1
    $ focus_character = "tatsuki"
    
    scene map
    hide screen tatsukishrine08    
    stop music fadeout .7
    scene black with dis
    pause .5
    scene shrine with Dissolve(1)
    play music free0258

    fn "「Whew, it's so hot...{w=.3} Hm?{w} Someone's here. 」"
    
    show ta 002 at center with dis

    ta "「Stop, damn it! Leggo, n-no, not there...!{p}\ \ Dahaha! Stop, I'm ticklish! 」{w} {nw}"    
    show ta at move_midright(0.5)
    extend "{w=.5}{nw}"
    show to 002 at midleft with dis

    to "「It's fine, isn't it? No big deal. 」"
    
    show ta 007 with dis
    
    ta "「That's not the problem.{p}\ \ Sheesh, you're always pouncing at me. 」"
    ta "「It's fine if you want to jump out at me,\n\ \ but stop trying to catch my tail.{p}\ \ It's my weak point, especially at the base... 」"
    to "「C'mon, I was just happy to meet you.{w} Besides...\n\ \ Your tail excites me for some reason, Tatsu-nii.{p}\ \ So you say you're weak right...{w} Here? 」"

    show ta 010 at hit_left

    ta "「Wai-! 」"
    "Approaching the grounds,\nI saw Tatsu-nii and Torahiko horsing around."
    "Tatsu-nii was flailing his arms around as he ran,{p}trying to shake off Torahiko as he clung to his tail."
    "Sheesh...{p}Still, the two of them are really close."
    fn "「Hey, what are you guys doing on a day like this? 」"

    menu:
        "A. Let me in on it, too!":
            jump tatsuki08_join
        "B. Such a beautiful couple...":
            jump tatsuki08_couple
        "c. Torahiko, ease up a bit.":
            jump tatsuki08_stop

##########################################
label tatsuki08_join:
    $ love_tatsuki -= 1
    $ love_torahiko -= 1

    fn "「Let me in on it, too! 」"

    show ta 008 with dis
    
    ta "「[fn], help! Do something about him! 」"

    show to 010 with dis
    
    to "「Hey, [fn]!{w=.3}　Come and help me out! 」"
    fn "「This looks fun,\n\ \ I'm coming over right now.{p}\ \ Whoa...{w=.3} Oh crap,{w=.3} I'm falling over-! 」"
    
    hide to
    hide ta
    with wipe_down
    
    #!#Insert screen shake
    play sound bosu31

    fn "「Oww, seriously.\n\ \ Who put a trap like this here?{p}\ \ Huh? What's this? 」"
    "When I fell,\nmy hand caught something,\nbut... Oh my..."
    
    stop music fadeout .2
    play music free0421

    "WHAAAT!?{w=.3}　What is this!?{p}...I-it can't be, it's-{w=.3}　Underwear!{p}It's not just any kind, either!{w=.3}　It's a fundoshi!"
    "Whoa-!{w=.3}　I'm losing my balance again...!{p}Dammit, I'm falling down,\nand pulling Tatsu-nii's fundoshi with me...!?"
    "{size=+15}AAAAAAAAAAUGH!!!"
    "Tatsu-nii's going to end up starring in\nan \"uncensored flashing\" event!"
    
    show ta 107 at midright
    show to 003 at midleft
    with wipe_up
    pause .3

    fn "「Huh?{w=.3}　It's all smooth with nothing there... 」"
    "I figured it'd be dangling freely, but it's all flat.{p}There should at least be something there,\nbut there's not a single thing..."
    "Hmm...{w=.3} There is a slit there...{w} Not that I'm looking."
    to "「[fn], what're you doing?{w=.3}\n\ \ If Tatsu-nii loses his underwear,\n\ \ it's going to be a huge problem. 」"
    
    show to 002 at center
    show to ray 01 at midleft
    with dis

    to "「Didn't you know?{w=.3}　Tatsu-nii's just like a lizard,\ \ the important stuff is stored inside.{p}\ \ Right, Tatsu-nii? 」"
    narr "Time for an explanation!"
    narr "For the dragonmen in this world,\ntheir reproductive organs are kept inside their body,\njust like reptiles!"
    narr "So, just like other dragonmen,\nTatsuki's dick is kept inside,\nwhich lets them avoid harm to their sensitive parts."
    fn "「Oh, I see. Sorry, Tatsu-nii,\n\ \ that was careless of me. 」"
    
    stop music fadeout 1

    ta "「... 」"
    fn "「Seriously, my bad. Hahaha...{w} Tatsu-nii? 」"
    
    play music free44

    ta "「[fn], you idiot!! I'm not a lizard! 」"
    
    show ta 105 with dis

    "Tatsu-nii shouted that, then ran off, embarrassed.{w} {nw}"    
    show ta at move_offright(0.25)
    extend "{w=.25}{nw}"

    show to 007 with dis

    to "「Tatsu-nii, your pants are still off. 」"
    ta "「Geh-! 」"
    "Just as expected...{p}While we watched,\nTatsu-nii's legs got caught, and he tripped."
    fn "「Tatsu-nii, watch out!{w=.3}　You'll fall down the steps! 」"
    "*Roll roll roll* {w=.3}{nw}"
    play sound CarStopA
    extend "*Screech*{w=.5}{nw}"
    show shrine at hshake
    play sound bosu35
    extend "{w=.3} *Crunch☆*{w=.1} Gyah!"
    
    fn "「Too late...{w=.3} I wonder if he's okay?{p}\ \ I swear I just heard a car braking,\n\ \ then a kind of collision sound... 」"
    to "「I'm sure he's okay...{w=.3} Tatsu-nii's pretty tough...{p}\ \ Well, it's not your fault, so don't worry about it.{p}\ \ Let's hurry down and check on him. 」"
    "You say that, Torahiko, but your face is all stiff.{p}He's not hurt, is he?{w=.3}　I wonder if he's all right..."
    "It was an accident,\nbut it looks like I did something bad..."

    jump end08

####################################
label tatsuki08_couple:

    $ love_tatsuki -= 1
    $ love_torahiko += 1
    stop music fadeout .4
    play music pops_001

    fn "「Such a beautiful couple... 」"

    show to 010 with dis
    
    to "「Yo, [fn]. Sorry, but Tatsu-nii's mine. 」"
    fn "「What was that? Well, I'm not gonna lose! 」"
    "I dashed out and jumped on top of Torahiko,\nthen grabbed both Tatsu-nii's and Torahiko's tails."

    show ta 003 with dis
    
    ta "「Hey, [fn]!?{w=.3}　Hold on a sec...{p}\ \ What's going on, are you guys grasshoppers? 」"
    fn "「I won't let go!{w=.3}　Tatsu-nii's mine. 」"

    show to 003 with dis
    
    to "「Well, I'm not handing him over.\n\ \ Tatsu-nii's always been mine. 」"

    show ta 006 with dis
    
    ta "「I don't get you guys...\n\ \ Just stop that, and let go already. 」"

    show to 001 with dis
    
    to "「[fn], you'd better stop.\n\ \ Tatsu-nii's saying you're too heavy. 」"
    fn "「Well, there's no helping it.\n\ \ I'll let go if you do. 」"

    show to 003 with dis
    
    to "「Fine, we lot go on three?{w=.3}　One, two, three... 」"

    show to ray 01 at midleft with dis
    
    fntora "「Hey, you were meant to let go.{w} Dahahaha! 」"

    show ta 004 with dis
    
    ta "「You guys, stop messing around already! 」{w} {nw}"
    show ta at spinning
    extend "{w=.85}{nw}"
    show ta at still
    extend "{w=.01}{nw}"
    show ta at shivering
    play sound swing40
    extend "{w=.2}{nw}"
    play sound2 swing40
    extend "{w=.2}{nw}"
    show ta at still
    show to 008 at move_offleft(0.25)
    extend "{w=.3}{nw}"
    show shrine at hshake

    "Tatsu-nii spun his body,\nthen used his momentum to swing us off his tail."
    fn "「Oww... You didn't need to hurl us off like that. 」{w} {nw}"    
    show to 002 at move_midleft(0.4)
    extend "{w=.4}{nw}"

    to "「Yeah, it was just simple brushing against each other.{p}\ \ Skinship, you know. 」"

    show ta at briefzoom
    
    ta "「Like I care.\n\ \ If you guys want to hold onto something so damn much,\n\ \ just hold each other. 」"
    "Hold onto Torahiko, huh...?{p}That doesn't sound too bad.{w} {nw}"    
    show ta at move_offright(0.25)
    extend "{w=.3}{nw}"

    fn "「Oh! Tatsu-nii, wait! 」"
    "Hmm, I guess I overdid it.\nI'll apologise the next time I meet him."

    jump end08

#####################################
label tatsuki08_stop:

    $ love_tatsuki += 1
    $ love_torahiko -= 1
    
    stop music fadeout .4
    play music piano2_015

    fn "「Torahiko, ease up a bit. Tatsu-nii seems so sad. 」"

    show to 001 with dis
    
    to "「Whaaat? This is just a little skinship. 」"

    show ta 008 with dis

    ta "「{cps=10}[fn],{w=.5}{cps=40} you're a life saver.{p}\ \ Torahiko's bullying me. 」" 
    fn "「Okay, okay, I'm coming to help. 」"

    show to 003 with dis
    
    to "「What is this? You're treating me like a villain? 」"
    fn "「Okay, Torahiko.{w=.3}\n\ \ You'd better let go of Tatsu-nii quickly,\n\ \ or this is going to be ugly. 」"

    show to 006 big at center_big with sdis
    
    to "「How so? 」"
    fn "「Tatsu-nii will get dizzy,\n\ \ and you're out of luck if he turns his back to me.{p}\ \ Like now! 」"
    
    stop music fadeout .5
    play music free0428

    "I lunged at Torahiko's defenceless back,\nand started touching him indecently from behind.{p}As I poked his sensitive spots, he cried out in joy..."

    show to 010 big at bobbing
    
    to "「Aaahahaha!{w=.3} Stop, that tickles! 」"
    fn "「Cootchie cootchie cootchie! 」"
    
    "Torahiko writhed and shook in pleasure,\nand tears streamed down his ecstatic expression."

    show to 011 big at tilting_big with dis 

    to "「Stop...!{w} Someone help! Hyahahaha! 」"
    "Torahiko begged for me to stop.\nI kept going, all over his body.{w}{nw}"
    show to 011 big at tilting_big_stop with dis
    extend "{w=.01}{nw}"
    show to 012 big at shivering with dis
    
    to "「Wahaha! Oh man, I can't take any mooore! 」"
    "I'm also getting close to my limit\n(my hands, at least)...{p}Rather than stop, I redoubled my efforts."

    show to 008 big at briefzoom
    
    to "「Uwoooohoho-! 」"
    "Torahiko let out a roar as he fell off,\nand then he was done.{p}He dropped to the ground like a toy out of batteries."
    
    hide to with wipe_down_slow
    play sound bosu31

    to "「Haah... Haah... 」"
    fn "「Well, that was fun. 」"

    show to 003 at midleft with wipe_up_slow
    
    to "「Dammit! You better remember this! 」"

    show ta 010 with dis
    
    ta "「Are you a villain, or something? 」{w} {nw}"
    show to at move_offleft(0.25)
    stop music fadeout .4
    extend "{w=.4}{nw}"    
    play music daily02
    show ta 002 with dis

    ta "「Whew, you saved me there, [fn].{w=.3}\n\ \ My tail really is my weakest point.{p}\ \ I'll have to treat you at Raimon as thanks. 」"
    fn "「I just heard something amazing...{p}\ \ If you tell me something like that,\n\ \ does that mean it's okay for me to go for it? 」"
    
    show ta 003 big at center_big with Dissolve(1)
    stop music fadeout .5
    play music free0428 fadein .5

    ta "「Uwah, stop that! What are you doing!? 」"
    fn "「Cooootchie cootchie cootchie! 」"
    
    show ta 002 big at jump_up_big
    pause .15
    show ta at jump_up_big

    ta "「Gahahaha! Someone, help!!! 」"

    jump end08
    
############################################
label kouya08:

    $ love_kouya += 1
    $ focus_character = "kouya"
    $ event_name = _("Secret Concert Meeting")

    scene map
    hide screen kouyaforest08
    stop music fadeout .7    
    scene black with Dissolve(.5)
    pause .5
    scene path with wipe_dr_slow
    play music cicada01 fadein .7

    "Very recently, I've noticed\nthat walking is quite enjoyable."
    "This kind of setting is impossible to recreate.{p}The refreshing summer breeze blows past me,{p}as the leaves in the trees rustle."
    "With peaceful surroundings and clean air,{p}when people talk about clearing their minds,{p}this is probably what they mean."
    fn "「Well, I'm free to screw around every day,{p}\ \ and if I come to that conclusion while walking,{p}\ \ it'd be nice to get that feeling... 」"
    "As I was playing the straight man to myself,{p}I kept walking along in the sunlight."
    "Hmm... How about I take a walk through the forest?"
    "Magnificently large trees,\nsilently blooming flowers.{p}Yep, it's nature, all right."
    "No one's allowed to go in there,{p}because of the abundance of insects.{p}You'd swear that they spawn out of the air."
    "But... I feel like going in, anyway."
    "...Besides, I have nothing better to do."
    "Well, I guess Minasato's tranquility is one\nof its best aspects.{w} But it doesn't\nchange the fact that I'm bored to death."
    "So I'm going in. Yeah, I'm going in all right.{p}So what if entry is prohibited!?{p}Screw the establishment!"
    "If I don't take this chance now,{p}I'd regret wasting another day,{p}and I'd rather be eaten by mosquitos than face that!"
    fn "「...Nah, maybe I said too much on that matter... 」"
    "Again with the one-man comedy act...{p}I've got too much time on my hands,{p}and it's starting to become habit."
    "It's a little scary, even to myself."
    
    scene forest01 with sdis

    "As I continue on, houses faded away from view,{p}and even the faintest of civilization vanished.{p}When I finally stopped, I was on some forest trail."
    "Rays of sunlight penetrate through the forest canopy.{p}It really is nice, to come to a place like this..."
    "But, looking at the stunning forest scenery,{p}it's almost a little... eerie.{p}It's quiet, but, it feels a little too quiet."
    "It might be because something\nkeeps moving into my line of sight."
    "But... it feels like there's...{p}something in the shadows.{p}It makes my heart race."
    "There aren't bears or anything in here, are there?"
    "I mean, it'd be fine if it were Juuichi-san,{p}but an actual bear? Nope."
    "Nah, the forest isn't too deep.{p}There's no way there are any here, right?"
    fn "「... 」"
    "Since I've come this far,{p}there's no way I can consider making a U-turn."
    "...O-okay then."
    "As a bit of anxiety fluttered in my chest,{p}I steeled my nerves as I took a step..."
    
    stop music
    play sound guitar fadein .1

    fn "「Eh!? 」{w=2}"
    "...I stumbled backwards,{p}accidentally falling over."
    "No, I wasn't scared,{p}I just heard something."
    "What is it,{w=.3} this...{w=.3} that sound...{p}It's like something I've heard from an instrument.{p}Some kind of chord,{w=.3} I guess."
    "It was unexpected,{p}but I definitely hear something like a chord."
    "A chill ran down my spine."
    "Just what is it?"
    fn "「...A piano? 」"
    "That's ridiculous, there can't be a piano out here.{p}I'm probably mistaken about what kind of sound it is."
    "In my field of vision, I can see a lot of weirdness."
    "It can't be, what's coming out isn't a bear,{p}but some kind of demon...{p}No, not that, but some creature...!?"
    
    play sound guitar fadein .1
    
    fn "「Huh? 」"
    "Once again, my ears picked up the faint sound.{p}It clearly wasn't a natural noise,{p}but a chord played by a person."
    "There's no mistake, I didn't just hear something.{p}There's someone playing nearby."
    "Eh, but who could it be?{p}It's not like one of the seven wonders\nof the school made its way all the way over here..."
    "...But if I really think about it, aren't there...{p}plenty of instruments besides pianos?"
    "Like, for example..."
    fn "「Is it... a guitar? 」"
    "The question was answered in an instant.{p}What comes to mind would be,\namong people, one person."
    "This time, I stepped forward,{p}towards the direction of the sound."
    "Little by little, the sound got louder.{p}And then, I saw the person making it."
    
    show ka 001 at center with Dissolve(1)

    ka "「...Hm?{p}\ \ Oh, [fn]? 」{nw}" 
    play music daily02
    extend ""
    
    "Sure enough, it was Kouya.{p}He was casually leaning down,{p}and sitting on a rock as he looked at me."
    "In his hands, he was firmly holding a prized guitar."
    fn "「Oh... So it is you, Kouya.{p}\ \ That's great, really. 」"
    "So it wasn't some unknown being."

    show ka 005 with dis
    
    ka "「What'd you say? 」"
    fn "「No, nothing. Just talking to myself. 」"

    show ka 001 with dis
    
    ka "「Hmm. Well, whatever.{p}\ \ ...So, what brings you out here? 」"
    fn "「What, you mean... taking a walk? 」"

    show ka 005 with dis
    
    ka "「A walk, huh... it's fine with me,{p}\ \ but with all of Minasato's forests and mountains,{p}\ \ there's a lot of places you shouldn't go. 」"
    ka "「You know that, right? 」"
    fn "「Y-yeah... 」"

    show ka 001 with dis
    
    ka "「It's okay since there's nothing here,{p}\ \ but it's unsafe to be messing around.{p}\ \ What if you were hurt? 」"
    fn "「T-that's true. Sorry... 」"
    "I don't really get it,\nbut it seems I've made him mad."
    "He's saying that to me,{p}but Kouya's also come in all this way too.\nThat's a bit unfair."
    "Wait. If I think about it, rather than being angry,{p}could it be..."
    fn "「Th-thanks for worrying about me. 」"

    show ka 006 with dis
    
    ka "「...You dumbass, that's not what I said. 」"
    fn "「Hehehe...{p}\ \ So anyway, what are you doing here, Kouya?{p}\ \ You've brought your guitar, I see. 」"

    show ka 001 with dis
    
    ka "「Hmm? What am I doing out here?{p}\ \ There's a pretty obvious reason. 」"
    ka "「I have a guitar because, gasp,{p}\ \ I'm practicing! See?{p}\ \ P-R-A-C-T-I-C-I-N-G. 」"
    ka "「And besides, sometimes I want to go\n\ \ to a place that's quiet and uncrowded,{p}\ \ so I like to come out here. 」"
    ka "「It puts me in a good mood. 」"
    "As he said that,{p}he tapped the body of the guitar a few times."
    fn "「Ohh, I see.{p}\ \ ...I'm not bothering you, am I? 」"

    show ka 002 with dis
    
    ka "「No, you aren't. I was thinking that\n\ \ it was a good time to take a break, anyway.{p}\ \ ...If you're free, do you want to listen? 」"
    fn "「Eh, is that okay? 」"

    show ka 003 with dis
    
    ka "「Sure, it's been so long.{p}\ \ Just sit wherever. 」"
    
    hide ka with wipe_right
    stop music fadeout 2.5

    "At his suggestion,{p}I sat down on the ground where I stood,{p}resting my back against a handy little rock."
    "Once Kouya was satisfied,{p}he slowly began to play his strings."
    
    play music acoustic2

    "In this peaceful forest,{p}Kouya's playing filled the air."
    "I've heard this before,{p}it's a verse of a popular song."
    "With a guitar-only performance,{p}it has a fresh feel to it."
    "As he played, the song slowly came to an end.{p}And a little while, after holding the final note,{p}the tune faded out."
    
    play music daily02 fadein 2
    show ka 002 at center with Dissolve(.5)

    fn "「...Wow, you really are awesome at guitar, Kouya. 」"

    show ka 006 with dis
    
    ka "「Well, thanks. 」"
    "As soon as I told him what I thought,{p}Kouya laughed a little in response, blunt as ever.{p}I can see that attitude looking good and being cool."
    fn "「No, you really are.{p}\ \ I can't play an instrument at all,{p}\ \ so I'm a little jealous that you can play so well. 」"

    show ka 003 with dis
    
    ka "「Well, that's because I practice.{p}\ \ ...If that's all it is,{p}\ \ how about I teach you a little guitar? 」"
    fn "「Huh, really? 」"

    show ka 002 with dis
    
    ka "「I was thinking of taking a break at first,{p}\ \ but that seems more fun than spacing out by myself. 」"

    show ka 003 with dis
    
    ka "「And I did promise to teach you earlier. 」"
    fn "「Oh, come to think of it, that's true. 」"
    ka "「Yep. So I thought it'd be a good opportunity... 」"

    show ka 002 with dis
    
    ka "「So how about it, [fn]? 」"
    "Kouya's proposal to me was sounding pretty good.{p}I have the time, and I feel like trying it out."
    "But a part of my mind wanted to hold back,{p}thinking 'will I really be okay?'"
    "Well, what should I do?"
    menu:
        "A. Teach me.":
            jump kouya08_teachme
        "B. I'll pass.":
            jump kouya08_pass

#############################################
label kouya08_teachme:

    $ event_name = _("Secret and Private Lesson")
    $ love_kouya += 1

    fn "「All right, I guess I'll take you up on that. 」"

    show ka 003 with dis
    
    ka "「Sure, go at it as much as you like. 」"

    show ka 002 with dis
    
    ka "「Well, first, take the guitar. 」"
    "Kouya said that as he got up,\npresenting to me the guitar he had been playing."
    "I extended my hand to receive it,{p}then tried to handle it as he had."
    "It felt like my cheeks had slackened a little.{p}For a minute, I got the feeling that I could do it."

    show ka 003 with dis
    
    ka "「Hey hey, you look kind of good like that. 」"
    fn "「Hehe, really? 」"
    ka "「Yeah, well enough. Now for starters,{p}take your right thumb and try stroking the strings.{p}It's fine to not hold them down. 」"
    
    hide ka with wipe_right

    "Kouya gestured by waving his wrist to the side,{p}as if to say 'like this.'"
    "I imitated this, slowly putting my thumb\non the widest string and stroking it."
    
    stop music fadeout .2
    play sound guitar_tune
    pause 4

    "The sound from the string spread out, then faded away."
    
    show ka 002 at center with wipeleft
    play music daily02 fadein 2

    ka "「Yeah, just like that.{p}\ \ And now you've finished the first lesson. 」"
    fn "「So, this is a good start, eh? 」"
    ka "「Uh-huh.{w=.3} Playing the string like that\n\ \ is called stroking, but it can't be done well,\n\ \ and the sounds come off weird. 」"

    show ka 001 with dis
    
    ka "「Just playing the strings is really easy.{p}\ \ I think that you shouldn't make\n\ \ a big deal out of it. 」"

    show ka 003 with dis
    
    ka "「On the other hand,{p}\ \ I also think it's wrong to shrug it off. 」"
    fn "「Hmm, that's pretty deep. 」"
    ka "「Yeah, it might be.{p}\ \ I still don't get it myself, even now. 」"

    show ka 002 with dis
    
    ka "「But whatever,{w=.3} let's move on.{p}\ \ How about you try playing a simple chord next? 」"
    fn "「Chord? 」"
    ka "「In other words, hold the strings down,\n\ \ then play a group of notes. 」"
    ka "「Guitars have been used to make chords\n\ \ in music for who knows how long. 」"

    show ka 003 with dis
    
    ka "「Of course you can just play with only one note,{p}\ \ but as you can guess, that's not very useful. 」"
    ka "「So that's why we're starting\n\ \ with learning to play a chord. 」"
    fn "「I see. 」"

    show ka 009 with dis
    
    ka "「That's the idea, and I was thinking\n\ \ of having you play something,{p}\ \ but now...{w} Let me see your left hand. 」"
    fn "「Oh, okay. 」"

    show ka 001 big at center_big with dis 
    
    "Kouya took my hand, then guided my fingers\nto where I was meant to hold the string."
    "As he moved them around the neck of the guitar,{p}I only partially felt the hard strings."
    "Mostly, I noticed the warmth of his hand,{p}and my heart beat a little faster."
    "Ahh... This warmth makes me so happy..."

    show ka 002 big with dis
    
    ka "「And, this should be good to start with.\n\ \ Now, [fn]...{p}\ \ {nw}"
    show ka 005 with dis
    extend "Wait.{w=.3} What's wrong, not feeling well? 」" 
    fn "「Whu... Oh! Sorry, I'm fine.{p}\ \ I was spacing out a little. 」"

    show ka 001 big with dis
    
    ka "「Your face is kind of red though.{p}\ \ You didn't catch a cold did you? 」"
    fn "「That can't b-{w=.3} I'm fine, really. 」"

    show ka 005 big with dis
    
    ka "「...Huh. If you say so, then all right. 」"
    fn "「Yeah,{w=.3} I'm totally okay.{p}\ \ Anyway, how do I play this? 」"
    "I changed the subject back to the guitar.\nWhatever's on Kouya's mind is a mystery,{p}but he seems not to be giving it too much thought."
    "Man, that was close.{p}I don't really get what happened,{p}but it was close."
    
    hide ka
    show ka 001 at center
    with dis 

    ka "「For now, push down firmly with these fingers\n\ \ then play like you did before. 」"
    "I did as he asked, then tried it out."
    "This time, the sound was different than before.{p}When I played with no strings,\nthe sound was very open and free..."
    "But this time, the note cut off awkwardly."
    "Even I could tell that I'd done something wrong."
    fn "「...I did something wrong,{w} huh? 」"

    show ka 005 with dis
    
    ka "「Yep. You did well in holding down the strings,{p}\ \ but holding the neighboring strings by accident\n\ \ could mess everything up. 」"

    show ka 002 with dis
    
    ka "「Everyone sucks in the beginning, though.{p}\ \ I didn't get good all of a sudden, either. 」"

    show ka 003 with dis
    
    ka "「Getting to being able to play that well\n\ \ is just a matter of practice. 」"
    fn "「Hmm, I guess instruments are really hard.{p}\ \ If I keep playing my fingers will hurt more{p}\ \ I can still see the marks on them. 」"

    show ka 002 with dis
    
    ka "「If you keep it up, it gets better.{p}\ \ It's always like that when you start. 」"
    fn "「Perseverance becomes strength, I guess... 」"
    ka "「Basically. 」"
    fn "「So, can I keep trying for a little longer?{p}\ \ Stopping just like that feels a little irritating. 」"

    show ka 003 with dis
    
    ka "「Sure, I don't mind. 」"
    fn "「Thanks, Kouya. Let's see...{p}\ \ So I'm not supposed to touch the other strings? 」"

    show ka 001 with dis
    
    ka "「Right, if you keep pressing\n\ \ your fingertips vertically... 」"
    
    stop music fadeout .5
    scene black with Dissolve(1)
    pause 1
    play music cicada01 fadein 3
    scene forest01 with Dissolve(1)

    "The sound rang out, loud and clear,{p}\ \ then slowly faded into the surrounding area."
    "Kouya praised me, and applauded."

    show ka 002 at center with wipe_right
    
    ka "「Oho, you got better! 」"
    fn "「All because of your help.{p}\ \ Really, thanks. 」"

    show ka 006 with dis
    
    ka "「Nah, it's not that.{p}\ \ You kept trying until the end. 」"

    show ka 002 with dis
    
    ka "「Like, if you do it, then you will. 」"
    fn "「Hahaha. Then I'll keep that in mind.{p}\ \ Anyway, all this holding down makes my fingers hurt.{p}\ \ My left hand is dead. 」"
    "While I said that, I pulled up the guitar,\nfrom my lap and handed it back to Kouya."
    "If I stay any longer I'd probably get in the way,\nso this might be a good point to go back."

    show ka 003 with dis
    
    ka "「Hm, good work there.{p}\ \ Did you have fun? 」"
    fn "「Yeah, it was great.{p}\ \ Thank you. 」"

    show ka 002 with dis
    
    ka "「No need to thank me.{p}\ \ If you had fun, that's all that matters. 」"
    fn "「Are you going back to practice after this? 」"

    show ka 003 with dis
    
    ka "「I was thinking of doing some more before going back.{p}\ \ What about you? Wanna listen for a little longer? 」"
    fn "「Nah, I've already gotten in the way,{p}\ \ so I'm about to head back. 」"

    show ka 002 with dis
    
    ka "「I see.{p}\ \ We have a live concert coming up,\n\ \ so you could come to that, if you want. 」"
    ka "「And not just the guitar,\n\ \ I want you to hear the whole band perform. 」"
    fn "「Oh,{w=.3} really?{p}\ \ That sounds like fun.{w} When is it? 」"

    show ka 003 with dis
    
    ka "「Somewhere around the second half of the month.{p}\ \ I have a spare ticket, so if it's really okay,\n\ \ please come. 」"
    fn "「Right, I'll be there for sure.{p}\ \ I'm looking forward to it, okay? 」"

    show ka 002 with dis
    
    ka "「Yeah, just watch me.{p}\ \ I'll give you the best performance ever. 」"
    fn "「I'll hold you to that.{p}\ \ Well, later then, Kouya.{p}\ \ Good luck with your practice! 」"

    show ka 003 with dis
    
    ka "「Right, take care as you go home. 」"

    hide ka with wipe_right
    
    "I waved, then went off on my own."
    "A live concert, huh?{p}I've never been to anything like that,{p}so it sounds really fun."
    "Since it's somewhere past mid-month,{p}I should keep things open."
    
    scene path with Dissolve(.5)

    "As I decided that, I walked back along the path,{p}moving with a lighter gait this time."
    "I didn't think that I'd like it all that much,{p}but walking through the forests is quite nice."
    
    jump end08

########################################
label kouya08_pass:

    $ event_name = _("Cherish your Alone Time")
    
    fn "「Hmm, I came all this way but I think I'll pass.{p}\ \ If I'm here, you can't take a break can you? 」"

    show ka 001 with dis
    
    ka "「No, it's not like that...{p}\ \ But I guess I should thank you\n\ \ for your consideration. 」"
    fn "「Sorry, Kouya. 」"

    show ka 005 with dis
    
    ka "「Nah, nothing you need to apologize for.{p}\ \ But if you ever do have time, get in touch with me,{p}\ \ and I'll teach you. 」"
    fn "「Okay. Next time, for sure. 」"

    show ka 002 with dis
    
    ka "「Take care on your way back. 」"
    fn "「Thanks. Good luck with your practice, Kouya. 」"

    hide ka with wipe_right
    
    "I waved, then walked off."
    "It kinda feels like I've done something wrong.\nBut it's okay. Like he said,\nI'll just contact him next time I'm free."
    
    jump end08
    
########################################
label kounosuke08:
    
    $ focus_character = "kounosuke"
    $ event_name = _("Spirit Photography results")

    scene map 
    hide screen kounocandy08
    stop music
    scene candystoreout with dis
    play music cicada01

    fn "「The photographs are ready? 」"

    show ko 001 at center with wipe_right
    
    ko "「Yep. I'm revealing them now. 」"
    "Including Kounouske, who wasn't late for once, {p}members from that day, {p}have already gathered at the candy store."

    show su 002 at farleft with wipe_right
    
    su "「I'm kind of excited! 」"

    show to 007 at farright with wipe_right
    
    to "「I don't really care, but... 」"

    show ko 004 with dis
    
    ko "「Torahiko, are you scared? 」"

    show to 009 at jump_up
    
    to "「It's not like that! 」"
    fn "「Calm down... 」"
    "As usual, I have to step in between those two, {p}and our inspection meeting finally starts."
    "Kounosuke takes photographs out of his bag, {p}and scatters them on the table. {p}Then, we each take a photo."
    
    show su 001
    show ko 001
    show to 001
    with dis

    "{cps=10}......"
    
    if ghost_encounter == 1:
        jump day08_pictures_kouno
    elif ghost_encounter == 2:
        jump day08_pictures_tora
    elif ghost_encounter == 3:
        jump day08_pictures_shun

        
############################################
label day08_pictures_kouno:

    $ event_name = _("Someone I know, but don't know")
    $ love_kounosuke += 1

    show ko 002 with dis

    ko "「Look, look at this photo of Torahiko. 」"

    show to 006 with dis
    
    to "「W-what is it? 」"

    show ko 001 with dis
    
    ko "「Look at his tail 」"
    fn "「His tail? 」"

    show su 004 with dis
    
    su "「Nothing's there, {p}\ \ I don't think there's anything strange. 」"

    show ko 004 with dis
    
    ko "「I'm talking about the fur on his tail. {p}\ \ It's totally standing on end! 」"

    show to 005 at jump_up
    
    to "「Geh... 」"
    fn "「Oh, it really is! 」"

    show ko 001 with dis
    
    ko "「We hadn't even gotten inside yet. 」"

    show to at jump_up
    
    to "「T-that's not it! {p}\ \ I-I was just cold! 」"

    show ko 004 with dis
    
    ko "「Yeah right. 」"

    show to 003 at jump_up
    
    to "「Really! 」"

    show ko 001 with dis
    
    ko "「Hmm? 」"
    "This inspection meeting is more like... {p}an excuse to just hang out."
    
    scene candystoreout with wipe_right

    "When we look over the photographs, {p}we can't find anything strange."
    
    show ko 005 at center
    show su 001 at farleft
    show to 001 at farright
    with wipe_right

    su "「It doesn't look like... {p}\ \ there's anything in particular. 」"
    fn "「Well, I'd be more worried if, {p}\ \ it were that simple. 」"

    show to 007 with dis
    
    to "「Definitely. 」"
    ko "「Darn... 」"
    "In all honesty, {p}taking those photos scared me a little, {p}but this is reality, isn't it?"

    show ko 001 with dis
    
    ko "「...Hm? 」"
    "All of a sudden, {p}Kounosuke starts rummaging through the photos."
    "Instead of inspecting them one by one, {p}like we had been doing up until now, {p}he just quickly looks and moves to the next."
    fn "「Kounosuke, what is it? 」"

    show ko 005 with dis
    
    ko "「Wait a minute... 」"
    "Did he find something? {p}He gathers up all the pictures."
    "After finishing looking at them, {p}he turns his head to the side, {p}and counts them."

    show to 003 with dis
    
    to "「S-stop that! 」"

    show su 004 with dis
    
    su "「Is something wrong...? 」"
    ko "「Hmm... 」"
    "Kounosuke \"hmms\" as he answers, {p}picks out several photos from the table, {p}and moves the rest to the side."

    show ko 001 with dis
    
    ko "「Are these all the photos... {p}\ \ that were taken at the entrance? 」"
    fn "「Which ones? 」"
    "I check the pictures that were set aside. {p}Kounosuke's right, {p}there aren't any photos of the entrace."
    fn "「Looks to be that way... 」"
    su "「Is there something there? 」"

    stop music
    show ko 005 with dis

    ko "「There isn't anything there. 」"
    fn "「Huh? 」"
    "Not knowing what he's talking about, {p}we naturally take a look at the pictures."
    "Before we split up, there were several photos. {p}They were taken by Torahiko, {p}Kounosuke, Shun-kun, and I."
    "We used up all the film. {p}There were no photos of ghosts or anything."
    fn "「Err, Kounosuke? {p}\ \ Can you explain so that... {p}\ \ you know, we can understand? 」"

    show ko 001 with dis
    
    ko "「So, at that time, {p}\ \ those two were running from the ghost."
    ko "I thought that was the perfect time to take, {p}two or three pictures. 」"
    su "「Oh... 」"
    fn "「That reminds me... 」"
    "Now that he mentioned that, {p}I think I heard the shutter and saw, {p}the flash of light from the camera."
    "Everybody probably remembers that. {p}Shun-kun and Torahiko are quiet, {p}and I feel my body temperature drop."

    show ko 005 with dis
    
    ko "「Yet why aren't there... {p}any pictures of Botan-sensei? 」"
    "None. Not even one. {p}When he showed up, {p}there were pictures taken of him."
    "There are 2 or 3 photos, {p}that match up with the angle of what I remember."
    "But only by the shoe cuboard, {p}in the darkness of the school at night is there, {p}there's nobody."
    
    play sound fuurin 
    scene sky with dis

    "No one says anything."
    "In the silence, {p}the faint sound of bells, {p}can be heard in the distance."
    
    play sound bosu32
    scene candystoreout
    show ko 001 at center
    show su 003 at farleft
    show to 005 at farright

    su "「Hii! 」"
    fn "「Waa! 」"

    show ko 005 with dis
    
    ko "「S-sorry. 」"

    show to 007 with dis
    
    to "「D-don't scare me like that! 」"
    "A notepad falls out of Kounosuke's pocket, {p}making an abrupt sound."

    show ko 001 with dis
    
    ko "「Eh... 」"
    "Kounosuke picks the notepad up, {p}and suggestively stops moving again."

    show to 006 with dis
    
    to "「Wh-what's wrong? Kounosuke? 」"
    ko "「...This. 」"
    "Perhaps while he was picking it up, {p}when it happened to open to a page when it fell, {p}Kounosuke places the notepad on the table."

    show ko 006 with dis
    
    ko "「Th-that's wrong? {p}On that day, {p}I should have completely looked through this. 」"
    "On the title of that page, {w=.3}\n{nw}"
    play sound giwaku1
    extend "~The Seventh Wonder: The Mystery Person~\nis written."
    
    scene school01 gray with Dissolve(1) 
    pause 2
    play music ambience01

    "At Minasato Elementry, {p}it seems a ghost will appear, {p}and disguise itself as somebody familiar."
    "Because it appears that way, {p}if you happen to meet it, {p}you won't know it's a ghost."
    "But if you try to check who it is later, {p}then you will find that it was absolutely... {p}impossible for that person to be there."
    
    scene candystoreout
    show ko 005 at center
    show su 001 at farleft
    show to 001 at farright
    with wipe_right
    
    fn "「Th-this can't be right! 」"

    show su 003 with dis
    
    su "「We saw Botan-sensei then... 」"

    show to 005 at jump_up
    
    to "「That was a ghost...? 」"
    fn "「Th-that means we had... {p}\ \ a paranormal experience the other day? 」"
    "That unimaginable fact, {p}sits on the table now."

    play sound fuurin
    
    "Everbody is at a loss for words, {p}and we're all getting the chills."
    "Only the sound of cicadas, {p}and whind chimes can be heard. {p}It's like they're laughing at us."
    "Even Kounosuke was at a loss of words, {p}There was only a slight quiver in his shoulders."
    
    stop music fadeout .5

    ko "「Wh... 」"

    play music free44
    show ko 011 with dis

    ko "「When we were there, {p}I wish I could have gotten... {p}a good picture of it! 」"
    
    play sound bosu35
    show candystoreout at vshake
    show to 007 with dis

    allthree "{size=+30}「AAAAAH!! 」" 
    fn "「Don't act like that, Kounosuke! 」"

    show ko 005 at jump_up
    
    ko "「But, but, I had been waiting so... {p}\ \ long to have a real encounter with it, {p}\ \ and now there's no evidence...! 」"

    show to 003 with dis
    
    to "「Th-there's no problem with that! 」"

    show su 005 with dis
    
    su "「That's right! {p}\ \ If we had taken a photo of it, {p}\ \ it could have cursed us! 」"
    "I agree! {p}...Wait, Shun-kun? {p}Isn't that slightly off-topic...?"

    show ko 011 with dis
    
    ko "「But aren't you guys... {p}\ \ bothered that it was able to punch you!? 」"
    fn "「No, well...\n\ \ But that fist really did hurt. 」"

    show ko at jump_up
    
    ko "「It did, right!? 」"
    
    show su 001
    show to 001
    with dis

    everybody "「...... 」"
    "When Kounosuke completely gets away from the point, {p}you can feel the temperature change."
    fn "「B, but... {p}\ \ now that you mention it, {p}\ \ it wasn't scary at all."
    fn "Well, it was scary, but in a different way 」"

    show su 004 with dis
    
    su "「Wh-when you put it like that, {p}\ \ you're right. 」"
    fn "「It was just a little painful. 」"

    show su 002 with dis
    
    su "「Ahaha, it was! 」"

    show to 007 with dis
    
    to "「But did we meet the real thing...? 」"

    show ko 005 with dis
    
    ko "「Why are you laughing? 」"
    "Still, much to Kounosuke's chagrin, {p}it was thanks to him that we were somehow... {p}able to get rid of our fear."
    "Our laughter livened up the candy store."
    
    scene sky with dis

    "The meeting then turned to chit-chat. {p}Whether we had met a ghost or not, {p}it had just become nothing but a conversation topic."
    
    play music cicada01 fadein 5

    "And so our slightly strange (and creepy)\nSummer experience ended."
    
    ###Keep these until I know what they do...
    #[if exp="f.kimodame1read !== true"]
    #[eval exp="f.kimodame1read = true"]
    #[eval exp="f.numreadevent++"]

    #[jump target="*孝之助サブイベ終わり"]
    
    jump end08


##############################################
label day08_pictures_tora:
    
    $ event_name = _("Wasn't it Kounosuke.....")
    $ love_torahiko += 1
    
    show ko 005 with dis

    ko "「These pictures of the school at night... {p}\ \ they're as creepy as I thought they'd be! 」"

    show to 007 with dis
    
    to "「You don't need to say that. 」"

    show su 002 with dis
    
    su "「[fn]-san, should I buy some juice? 」"
    fn "「Oh, sorry. {p}\ \ Orange juice, please. 」"
    
    play sound step03
    show su at move_offleft(0.25)
    show ko 001 with dis

    ko "「Ah, Shun-kuuun, {p}\ \ please get me a cola. 」"

    show to at jump_up
    
    to "「You're... 」"
    su "「Torahiko-san, do you want something? 」"

    show to 001 with dis
    
    to "「I'll take a cider then. 」"
    su "「Okay. Got it. 」"

    show ko 005 with dis
    
    ko "「Aren't you going to take my order? 」"

    show to 003 with dis
    
    to "「Shut up! 」"
    "This meeting is more like an excuse to hang out."
    
    scene candystoreout with wipe_right

    "When we look over the photographs,\nwe can't find anything strange."
    
    show ko 005 at center
    show su 001 at farleft
    show to 001 at farright
    with wipe_right

    su "「It doesn't look like there's... {p}\ \ anything in particular. 」"
    fn "「Well, I'd be more worried, {p}\ \ if it were that simple. 」"

    show to 006 with dis
    
    to "「Definitely. 」"

    show ko at jump_up
    
    ko "「Darn... 」"
    "Honestly, when I was taking those pictures, {p}I was a little worried. {p}But this is reality, isn't it?"

    show ko 001 with dis
    
    ko "「Huh? But what about the music room? 」"

    show to 005 at briefzoom
    
    fntora "「Ah... 」"
    "That reminded me... {p}I was so distracted by Kounosuke popping out, {p}that I forgot to take some pictures."

    show ko 002 with dis
    
    ko "「Is it possible that you were... {p}\ \ too scared to take any pictures? 」"
    
    show to at move_midright(.25)
    show to 003 with dis

    to "「That was your fault! 」"

    show ko 006 with dis
    
    ko "「O-oww, oww! 」"

    show su 003 with dis
    
    su "「Kounosuke-san, {p}\ \ you shouldn't play tricks like that. 」"

    show to 001 with dis
    
    to "「That's right. 」"
    ko "「Oww, sorry, sorry! {p}\ \ It was me who started the metronome! {p}\ \ I'm sorry! So let go of my ears! 」"

    show to 002 with dis
    
    to "「[fn], should I? 」"
    fn "「Hm, well I guess I'll forgive him. 」"

    show ko at jump_up
    
    ko "「Yeowch, you pulled too hard, Torahiko! 」"

    show to at jump_up
    
    to "「That's divine punishment. 」"

    show ko 005 with dis
    
    ko "「Ooh, if I was a ghost, {p}\ \ I'd definitely haunt you. 」"
    fn "「You reap what you sow. {p}\ \ Didn't you say that at that time? 」"
    ko "「......? 」"

    show to 001 with dis
    
    to "「By the way, {p}\ \ where are all your pictures from then? 」"
    fn "「I can't find them. {p}\ \ Kounosuke, are they over there? 」"
    ko "「Which time are you talking about? 」"
    fn "「That time in the music room, {p}\ \ when you were taking pictures of us. 」"

    show ko 006 with dis
    
    ko "「Pictures from the music room, {p}\ \ wait... who? 」"

    show to 007 with dis
    
    to "「Huh? Who else would it be besides you? 」"

    show ko 005 with dis
    
    ko "「What are you talking about? 」"
    fn "「It was when you deserted Shun-kun, {p}\ \ you're playing dumb again. 」"

    show ko 006 at jump_up
    
    ko "「Owowowowow, [fn]! {p}\ \ L-let go of my ears! 」"
    
    play sound puu75
    show to 002 at hit_left

    to "「Then what about over here? 」"

    show ko at jump_up
    
    ko "「Uhyahya! Stop, not the side of my stomach! {p}\ \ That hurts! It tickles! I'm gonna die! 」"

    show su 004 with dis
    
    su "「Um... 」"
    
    show ko 005 with dis
    show to 001 with dis

    to "「Hm? What, Shun? 」"

    show su 001 with dis
    
    su "「What do you mean he deserted me? 」"
    fn "「During the test of courage, {p}\ \ Kounosuke left you behind on the first floor, {p}\ \ and ambushed us in the music room. 」"

    show su 004 with dis
    
    su "「But Kounosuke-san was with me... {p}\ \ the whole time... 」"
    
    stop music fadeout 1.5
    
    fn "「What...? 」"

    show to 005 at jump_up
    
    to "「Huh...? 」"
    "Shun-kun doesn't know what we're talking about, {p}and we involuntarily stiffen up."
    "Kounosuke takes that chance, {p}to get away from Torahiko and I."
    
    scene candystoreout
    show ko 005 at farleft
    show su 001 at center
    show to 005 at farright
    with dis

    su "「He did go on ahead to the music room, {p}\ \ to mess with the metronome, {p}\ \ but he came right back out."
    su "Then we waited the whole time,\nby the entryway with the lights out. 」"

    show ko 004 with dis
    
    ko "「That's right. {p}\ \ My plan was to suddenly pop out, {p}\ \ after you two rushed back down from the music room."
    fn "「W-wait a minute! 」"
    "This is ridiculous. {p}That had to have been Kounosuke!"
    fn "「At that time, {p}\ \ didn't we meet you... {p}\ \ when you came out of the music room!?"
    
    play music ambience01
    
    fn "Right, Torahiko? 」"

    show to 008 with dis
    
    to "「Y-yeah! 」"

    show ko 005 with dis
    
    ko "「I was on the first floor the whole time! 」"

    show su 004 with dis
    
    su "「He was with me, {p}\ \ there's no doubt about that. 」"
    "What is this? {p}What does this mean?"
    "Kounosuke and Shun-kun... {p}were on the first floor..."
    "Then the Kounosuke we encountered... {p}at that time was...?"
    fn "「Impossible... 」"
    "That couldn't have been Kounosuke..."
    fn "「Then that wasn't Kounosuke...? 」"
    "In the humid midsummer air, {p}I could feel a cold sweat along my back."
    "Torahiko says nothing, {p}well, nothing I can say, {p}and stiffens up the same way I do."

    show ko 001 with dis
    
    ko "「Maybe you saw two people? 」"
    fn "「No, I don't think so. 」"

    show to at shivering
    
    to "「Ah-aaaah! 」"
    "Torahiko's awkward reply, {p}makes it sound as if his soul is coming out."

    play sound fuurin
    
    "In that humid midsummer air, {p}we're left speechless."
    "Only the sound of cicadas, {p}and whind chimes can be heard. {p}It's like they're laughing at us."

    show ko 005 with dis
    
    ko "「Why... 」"

    stop music fadeout .5
    show ko 011 with dis
    
    ko "「Why didn't you take a picture, {p}\ \ of such a juicy experience! 」"
    
    play music oo39_cho_ys001
    
    "...what?"
    fn "「D-don't be ridiculous. 」"
    "But no matter how you look at it, {p}that was Kounosuke."
    "If we had known that was a ghost, {p}there wouldn't be any room for doubt now."
    ko "「That was awfully sly of you two, {p}to have a paranormal experience without me! 」"
    
    show to 007 at still with dis 

    to "「Sly... 」"

    show ko 012 at jump_up
    
    ko "「Sly, really sly! {p}\ \ I've never seen a ghost before!"
    ko "It's possible that, {p}\ \ I'll never see one my whole life!! 」"

    show su 003 with dis
    
    su "「I-I think it's better... {p}\ \ to have never seen one. 」"

    show ko 006 with dis
    
    ko "「That was the best time to take a picture! {p}\ \ I should have gone to the music room, {p}\ \ if I knew that was going to happen! 」"
    fn "「The best time to take a picture... 」"
    "While he vents his meaningless anger, {p}everybody else doesn't know what to do, {p}and doesn't say a word."
    "Ko-Kounosuke. {p}As usual, you have missed the point."

    show ko 011 with dis
    
    ko "「Let's have another test of courage! {p}\ \ One more time! 」"

    show to 003 at jump_up
    
    to "{size=+15}「NOPE. 」"
    fn "「Same for me! 」"
    "Kounosuke turns around, {p}and tilts his head toward Shun-kun."

    show su at shivering
    
    su "「Huh? I-I have a curfew... 」"
    
    show su at still
    show ko 012 at jump_up
    
    ko "「Oh... Everybody's betraying me! {p}\ \ Fine then! {p}\ \ I'll just go by myself! 」"
    "As soon as Kounosuke says that, {p}he rushes out of the candy store."
    
    show ko at move_offleft(0.25)
    show su 004 with dis
    
    su "「He's gone... 」"

    show to 006 with dis
    
    to "「H-he'll get cursed... 」"
    fn "「Probably... 」"

    show su at jump_up
    
    su "「Wh-what should we do? 」"

    show to 007 with dis
    
    to "「Aah, screw it, {p}\ \ he's not gonna listen to us... 」"
    "We had been completely abandoned. {p}For a while we were stunned, {p}and not sure what to do."
    "So after that, {p}we talked for a bit and then left."
    
    scene sky with Dissolve(.4)
    
    "That night, a ghost never appeared."
    "When Kounosuke was caught, {p}entering the school without permission, {p}it was said that he was wrung out by the teacher."

    play music cicada01 fadein .75
    
    "And so our slightly strange, {p}Summer experience ended."
    
    jump end08


########################################
label day08_pictures_shun:
    
    $ event_name = _("The Seventh Wonder")
    $ love_shun += 1

    show ko 005 with dis
    
    ko "「By the way, it's hot. 」"

    show su 004 with dis
    
    su "「It's because there's no air conditioning. 」"

    show to 003 with dis
    
    to "「It's not just hot, it's too hot. 」"

    show ko 001 with dis
    
    ko "「Yeah, why don't we eat some ice cream? 」"
    fn "「Oh, that'd be good... 」"
    
    show su 001
    show to 001
    with dis

    ko "「Yes. So, what kind do you want? 」"
    fn "「I'll take a cup of vanilla. 」"
    na "「I like chocolate. 」" 
    to "「I guess I'll take the same. 」"

    show ko 003 with dis
    
    ko "「What about you, Shun-kun? 」"

    show su 004 with dis
    
    su "「Huh? I, I'm fine. {p}\ \ I'll buy some for myself. 」"

    show ko 002 with dis
    
    ko "「Don't be so modest. {p}\ \ Be honest when I'm treating you like this! 」"
    su "「But... 」"

    show ko 004 with dis
    
    ko "「Besides, Torahiko is paying. 」"

    show to 005 with dis
    
    to "「Me!? 」"

    show ko 003 with dis
    
    ko "「[fn] too. Treat us properly. 」"
    
    "This meeting is more like an excuse to hang out."
    
    scene candystoreout with dis

    "When we look over the photographs, {p}we can't find anything strange."

    show su 004 at farleft with dis
    
    su "「It doesn't look like there's... {p}\ \ anything in particular. 」"
    fn "「Well, I'd be more worried, {p}\ \ if it were that simple. 」"
    
    show to 003 at farright with dis

    to "「Definitely. 」"

    show ko 007 at center behind to with dis
    
    ko "「Darn... 」"
    "Honestly, when I was taking those pictures, {p}I was a little bit worried. {p}But this is reality, isn't it?"
    
    stop music fadeout 3
    
    scene candystoreout with wipe_right
    show na 001 at center with wipe_right

    na "「Oh, there was one after all! 」" 
    "During the pause in the middle of our work, {p}Nana-kun suddenly shouts."

    show to 005 behind na at farright with wipe_right
    
    to "「Wh-what is it, Little-[fn]? 」"
    
    play sound bosu29
    show ko 005 at farleft with wipe_right

    ko "「Did you find something!? 」"

    show na 002 with dis
    
    na "「No no. This, this. 」"
    
    play sound paper00
    scene ghostpic clear with wipe_dr_slow
    pause .3

    "He presents a photo of Nana-kun, {p}hugging around Torahiko's waist."
    
    scene candystoreout
    show to 005 at farright
    show na 001 at center
    show ko 005 at farleft
    with Dissolve(1)

    na "「Darn. I dodged all the cameras, {p}\ \ but one still caught me off guard! 」"
    
    play music cicada01 fadein 1.5
    show ko 004 with dis
    
    ko "「What? 」"

    show to 001 with dis
    
    to "「Oh, that. You surprised me! 」"
    fn "「That reminds me, {p}\ \ didn't you used to hate cameras? 」"

    show na 002 with dis
    
    na "「Yeah. See, it's not good for me, {p}\ \ to be captured on film. 」"
    fn "「Really? {p}\ \ But I don't think there's... {p}\ \ anything particular about that."
    fn "I'm more surprised by that... err... {p}horrible look on Torahiko's face. 」"

    show to 003 at jump_up
    
    to "「That was bad. 」"
    fn "「Oh, sorry... 」"
    "Torahiko forces a smile, {p}when he sees the photo of those two."
    "Nevertheless, there's nothing... {p}really strange about Nana-kun."
    "He looks just like Shun-kun, {p}in face and figure."
    "But he's much smaller, {p}like he's really in elementary school. {p}He should be the same age as Shun-kun, yet..."
    
    #Hide text box
    scene black
    show to 003 at farright
    show na 002 fade at center
    show ko 004 at farleft
    with dis
    
    stop music
    play sound ringing loop 
    $ renpy.music.set_volume(0.5, 0.25, channel = "sound")
    pause 1
    
    scene candystoreout
    show to 003 at farright
    show na 002 at center
    show ko 004 at farleft
    with dis

    "!?"
    
    hide ko
    hide to
    with sdis
    
    "What's this strange feeling just now? {p}Something's wrong. {p}Nana-kun... Wait, who's Nana-kun?"

    show na 001 with dis
    
    na "「[fn]? 」"
    fn "「You... who are you...? 」"
    
    scene candystoreout gray
    show na 001 gray at center
    stop sound
    pause 1

    "At that moment, {p}all sound disappears from the world."
    "As if time had stopped, {p}I can't hear a thing."
    "Nobody is moving. {p}Even I can't move."

    show na 002 gray with dis

    na "「Oh, did you find out the truth? 」"
    "In the middle of this, {p}I can only hear the the voice, {p}of the child named Nanafuse."
    na "「If it was night, {p}\ \ it would be a little easier... {p}\ \ to apply the suggestion. 」"
    
    show  gray with dis

    na "「It seems everybody else can't hear anymore. 」"
    fn "(What is this? Y-you are...?)"
    na "「Do you remember? [fn]?\n\ \ [fn], you gave that name to me. 」"
    fn "(What...?)"
    na "「I am the Seventh Wonder. {p}\ \ \"The Person Everybody Knows, {p}\ \ the Person Nobody Knows\"."
    na "Back then, I used to play with you guys. 」"
    "The Seventh Wonder? {p}The Seventh Wonder..."
    "Nanafuse, Nanafuse [fn], {p}seven, nana... {p}Nana-kun."
    fn "(...Oh)"
    
    scene white with dis
    pause .3
    scene school01 red
    play music melodious06 fadein .5
    $ renpy.music.set_volume(0.6, 0.0, channel = "music")

    "It was an evening as hot as today. {p}In the corner of the schoolyard, {p}Shun-kun found a lone child."
    "I asked the child for his name, {p}and he just said \"Nana\"."
    "I thought that was a strange last name. {p}Then the child whispered... {p}the same first name as mine."
    "I said: {p}\"You're called [fn]? {p}Wow, that's the same as me.\""
    
    scene white with dis
    pause .3
    
    scene candystoreout gray
    show na 102 gray
    with dis   

    na "「At that time, {p}\ \ when I found Shun, I received my form."
    "And when you gave me a name, {p}I gained consciousness. {p}I have valued those two things. 」"
    "Oh yeah. That's right. {p}Now I understand the true nature, {p}of that kid we used to play with."
    "Nana-kun is the Seventh Wonder. {p}The ghost of a child who inhabits the school, {p}given birth by everybody's image."
    "And already one of our close friends."
    "But we played a lot when I was a kid, {p}why did I forget? {p}I even forgot that I had forgotten."

    show  gray with dis
    
    na "「That just happens. {p}\ \ Everybody forgets me when they leave me. {p}\ \ That's why I \"don't exist.\" 」"
    
    show na at fading(0.4, 2.0)
    
    "!?"
    "Little by little, Nana-kun's form gets pale, {p}I finally realize what's going on."

    show na 102 gray with dis 
    
    fn "(N-Nana-kun!?)"
    na "「Soon, we'll be out of time... 」"
    fn "But I just realized who you are..." 
    na "「Ahaha, you're different. {p}\ \ Now that the suggestion has been unraveled, {p}\ \ I can't be seen."
    na "Someday, I'll find somebody to mimic, {p}and appear in front of everybody. 」"
    
    show  gray with dis 

    na "「And at that time, I'll surprise you again.{p}\ \ Just like in the science room. 」"
    
    show na 102 gray with dis 

    na "「Oh, also, I'll give you that picture, {p}\ \ that made Torahiko faint. 」"

    show  gray with dis 
    
    "The picture from that time, {p}is in Nana-kun's hand."

    $ renpy.music.set_volume(1.0, 0.0, channel = "music")
    play sound paper00
    show ghostpic blur1
    pause 1.5
    show  ghostpic blur2 with dis
    pause .5

    "The outline of Nana-kun's form, {p}on the picture becomes dim."
    "And only a white mist, {p}wrapped around Torahiko can be seen."
    
    hide ghostpic blur2
    show na 102 gray
    with dis
    show na at fading (0.0, 2)

    na "「See? I look bad in photos, right? 」"
    
    hide na 
    
    "As he leaves his last joke, {p}Nana-kun melts into the air."
    
    stop music fadeout 1
    scene white with sdis

    fn "「Nana-kun! 」"
    
    play sound bosu35
    
    $ encounter_nanafuse = True
    
    #Shake the chat box vertically

    to "{size=+30}「WHAAA! 」{w=.3}"
    
    play music cicada01
    $ renpy.music.set_volume(0.4, 0.0, channel = "music")
    scene candystoreout
    show ko 006 at center
    show su 004 at farright
    show to 005 at farleft
    with dis

    su "「[fn]-san, wh-what's wrong, {p}\ \ all of a sudden? 」"
    fn "「Huh...? 」"
    ko "「Is Torahiko okay? 」"

    show to 001 with dis
    
    to "「Oh, yeah. 」"
    fn "「What? Huh? Umm... 」"
    "What was that? {p}I felt like I was talking to... {p}somebody just now, but... huh?"
    "It seems like I lost my... {p}memory for a second somehow..."
    fn "「What were we doing just now? 」"
    su "「[fn]-san? 」"

    show ko 001 with dis
    
    ko "「[fn]? 」"

    show to 005 with dis
    
    to "「H-hey, are you alright? 」"
    "All three of them look at me with concern. {p}Err... Oh, that's right. {p}I think we were appraising ghost photos."
    fn "「Sorry, sorry. {p}\ \ I just spaced out there for a minute. 」"

    show ko 004 with dis
    
    ko "「Is that really it? {p}\ \ You were shouting, {p}\ \ something like \"Nana-kun.\" 」"
    "Nana-kun? {p}Nana-kun, Nana-kun..."
    "What is that? {p}It feels like those are important words, {p}but I just can't remember. 」"
    fn "「I was saying that? 」"

    show ko 001 with dis
    
    ko "「...Well, I hope you're alright. 」"

    show su 002 with dis
    
    su "「Are you alright? [fn]-san? 」"
    fn "「I'm fine, don't worry. 」"
    "In the end, we couldn't gather anything, {p}so after that we just ate some sweets, {p}talked, and left as usual."
    
    scene sky with dis

    "On the way back, {p}the word \"Nanafuse\" came out of Shun-kun's mouth. {p}For some reason I couldn't get it out of my head."
    "Even though I have no idea what it means, {p}it's mysterious."
    
    stop music fadeout 1.2
    
    "And so our slightly strange, {p}Summer experience ended."
    
    $ persistent.ghost_pictures = True

    #*孝之助サブイベ終わり
    
#################################################    
label end08:
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

    jump day09

    
        
