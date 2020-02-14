##Day 15 / Camping Trip Part 2

label day15:
    
    $ renpy.music.set_volume(1.0, 0.0, channel = "music")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound2")
    
    $ day = 15
    $ the_date = "August 15"
    $ event_name = "８月15日"
    $ focus_character = ""
    
    window hide
    play music birds_chirping
    
    scene sky01 
    show text "{size=+130}August 15" at truecenter
    with Dissolve(.5)

    pause 3
    scene black with Dissolve(1)
    pause .4
    scene camp_site with Dissolve(1)

    $ affectionlist = [love_tatsuki, love_kounosuke, love_shun, love_kouya, love_shin, love_juuichi, love_soutarou, love_kyouji, love_torahiko]
    $ namelist = ["tatsuki", "kounosuke", "shun", "kouya", "shin", "juuichi", "soutarou", "kyouji", "torahiko"]
    $ selection = affectionlist.index(max(affectionlist))
    $ favorite = namelist[selection]
    
    #"who do I choose?"
    
    #menu:
        #"Tatsuki":
            #$ favorite = "tatsuki"
       # "Kounosuke":
            #$ favorite = "kounosuke"
        #"Shun":
            #$ favorite = "shun"
        #"Kouya":
            #$ favorite = "kouya"
        #"Shin":
            #$ favorite = "shin"
        #"Juuichi":
            #$ favorite = "juuichi"
    
    $ renpy.jump ("camp15_wakeup_" + favorite)

#######################################    
label camp15_wakeup_tatsuki:

    $ event_name = "Morning, Tatsu-nii"

    show ta 002 at center with dis

    ta "「Hey,{w=.2} wake up!{p}It's morning! 」"
    fn "「Mmmm...{w=.2} Good morning, Tatsu-nii.{p}\ \ It's already morning, what time is it? 」"
    
    show ta 001 with dis

    ta "「That doesn't matter,{w=.2} everybody else is already up.{p}\ \ Hurry,{w=.2} get your face washed and brush your teeth. 」"
    "I'm the last to wake up?{p}I overslept. I better get moving."
    
    jump camp15_explore
    
########################################
label camp15_wakeup_shun:

    $ event_name = "Ride me, my Wolf!" 
   
    who "「...[fn]-san! 」"
    fn "「...Mnn... 」"
    who "「[fn]-san, it's time to get up-! 」"
    fn "「Nna? 」"

    stop sound
    play music pops_003 fadein 1
    $ renpy.music.set_volume(0.8, 0.0, channel = "music")
    show su 002 at center with Dissolve(1)    
    
    fn "「Good morning... err, that's right,\n\ \ I'm camping with everybody. 」"

    show su 001 with dis   
    
    su "「Good morning.\n\ \ It's going to be breakfast time very soon- 」"
    "Nn-, Shun-kun's calling me for breakfast.\nIt's a very pleasant awakening for my half-asleep head.\nI face my posture up as I reflect upon that."
    fn "「Shun-kun, you know, I have a small request for you. 」"

    show su 015 with dis
    
    su "「What is it-? 」"
    fn "「It seems I'm not fully awake yet,\n\ \ so I'm going to ask for your cooperation. 」"

    show su 005 with dis
    
    su "「Okay! I'll do my best for you! 」"
    fn "「Thank you. I'm glad to hear that 」"

    show su 004 with dis
    
    su "「Umm, what should I do...? 」"
    fn "「First of all, get on top of me 」"

    show su 003 with dis
    
    su "「Wh,whaaat? I can't do something like that-...\n\ \ I'll crush you. 」"
    fn "「You're light, so it'll be okay. 」"

    show su 004 with dis
    
    su "「I, I see... Well then. 」"
    fn "「Okay, get around my waist... That's good. 」"
    
    show su at center_down with dis
    
    "Ah.\nHe has a comfortable weight."    
    fn "「Put your palms on my stomach. 」"

    show su 010 with dis
    
    su "「Okay... 」"
    fn "「Now, rock your body a little\n\ \ and say 'good morning' like you did earlier. 」"

    show su 006 at shake_side_slow with dis
    pause .2
    
    su "「Nn, nnng... Ooh, I keep slipping off. 」"
    fn "「Then I'll hold on to your waist. 」"
    "I reach my arms out as I say that{p}{nw}"
    show su 004 with dis
    extend "and wrap my hands around his slender as ever lower back.{p}Shun-kun rocks his body a bit and starts to speak."

    show su 001 at bobbing with dis
    
    su "「Uh, umm...{w=.2} Good morning-,\n\ \ [fn]-san, {w=.2}it's time to get up-,{w=.2}\n\ \ Wake up please-...{w=.2} Like that? 」"

    show si 001 at farright with dis
    
    si "「What is going on here? 」"
    fn "「! 」"

    show su 016 at bobbing with dis    
    
    su "「Oh, Shin-san...\n\ \ [fn]-san wanted me to wake him up this way. 」"
    "Shun-kun looks up as he's thrusting his waist on me,\nand Shin-kun glares at me with eyes full of contempt.\nThis kind of play is great."
    "My unsuspecting childhood friend is being decieved,\nrocking on top of the crotch of his suspicious partner.\nSo when Shin said that and pierced me with his gaze,"
    "A chill and an\noverflowing feeling of self-admonition\nruns through my body."

    show si 004 with dis
    
    si "「...Well, whatever.\n\ \ The food is going to be gone, but see if I care. 」"

    hide si with dis
    
    "Shin-kun turns around and leaves.{w} Aah, {w=.2}if it would have been Torahiko, he would have mounted me too,{w} or if it was Juuichi-san he would have mounted me as a form of punishment."
    "If it was Tatsu-nii... a tail bashing!{p}That would have been enough to completely crush me flat."  
    "If it was Kyouji and Soutarou-kun, they would have done the same thing next to us... {w=.3}No."
    "If it was Kounosuke, he would have been taking a flurry of pictures, which I guess I was prepared for happening anyways."
    "So in comparison, I think I was lucky that it was Shin-kun that saw us."
    "...I'll come up with a shoddy excuse later."
    
    show su tailwag 01 at center_down with dis
    
    su "「[fn]-san, did that wake you up? 」"
    "His wagging tail brushes against my feet.\nI'm sorry for toying with him while he was unaware of it."
    "An unintentional transformation in my head had caused me\nto simulate that."
    fn "「Thank you, Shun-kun! Now, let's go get something to eat! 」"
    su "「Okay-! 」"
    
    hide su with dis
    
    jump camp15_explore
  
####################################
label camp15_wakeup_kouya:
    
    $ event_name = "On the edge of sleep"
    
    who "「Hey...{w} Hey, [fn]. 」"
    "In my half-asleep consciousness, I can hear a voice."
    who "「Hey, wake up.\n\ \ It's already morning. 」"
    fn "「Uuh... Mm? 」"
    "At those words, I open my eyes reflexively.\nBut my vision is blurry and I can't see anything."
    "I try my best to look around,\nbut I'm unsuccessful because of the bright sunshine."
    fn "「Mm? Morning...? 」"
    "With my eyes half-closed, I try to sit up.\nIs my body still asleep?\nIt's not usually this difficult to move."
    who "「You're finally getting up.\n\ \ ...No, still asleep? 」"
    fn "「...No, I'm getti-uaaa!? 」"
    "Before I can finish speaking,\nsomething cold covers my face,\nthen begins to wipe roughly."
    "The shock clears away my sleepiness,\nbut I remain still."
    "I'm guessing that this feeling is\ndefinitely the work of a wet towel."

    show ka 001 at center with dis
    
    ka "「So, did that get your eyes open? 」"
    "The towel disappears,\nand it becomes quite clear that the\nperson in my field of vision is Kouya."
    fn "「...Good morning, Kouya. 」"
    "I greet him for the time being."

    show ka 005 with dis
    
    ka "「Oh, good morning.\n\ \ Everybody else is already up,\n\ \ hurry up and get something to eat. 」"
    fn "「Huh? I'm the last one? 」"

    show ka 013 with dis
    
    ka "「That's right, now get moving. 」"
    fn "「R-roger that... 」"
    "This means I overslept, didn't I."
    "I get out of the tent in a hurry."
    
    jump camp15_explore

#######################################
label camp15_wakeup_juuichi:
    
    who "「[ln]. 」"
    fn "「... 」"
    who "「...Hey, {w=.2}[ln]. 」"
    fn "「Mmmm... 」"
    "I'm forced into consciousness,{w=.2}\nand an uncomfortable feeling remains.{p}It's already morning?"
    "But I was up so late yesterday,{w=.2}\nthere's nothing I can do about it if I'm still sleepy."
    "I close my eyes, change the direction of my body,{w=.2}\ncurl up a little, {w=.2}and go back to sleep."
    who "「It's morning. {w=.2}Get up. 」"
    fn "「Mmm, {w=.2}just five more minutes... 」"
    who "「Get up already. 」"
    fn "「Come on... {w=.2}I'm still sleepy... 」"
    who "「... 」"
    "Whew, {w=.2}I hear a sigh.{p}...Seems like he apparently gave up."
    "I don't know who you were, {w=.2}but please forgive me.{p}I have lost the battle against sleepiness."
    "Then, {w=.2}just as I'm about to once again fall into the\nworld of dreams,"
    
    play sound don08
    show camp_site at vshake
    
    who "「WAKE UP-!! 」"
    fn "「Hyaa!? 」"    
    "Surprised by a sudden,{w=.2}\nbooming voice,{w=.2}\nI involuntarily spring up."
    "Juuichi-san stands before my eyes in an imposing\nstance with his arms crossed.{w} ...Although now I would\nhave no objection to calling him the Two Deva Kings."
    "I give him a morning greeting."

    show ju 001 at center with dis
    
    fn "「*Yawn*...{w} Good morning, {w=.2}Juuichi-san. 」"
    ju "「...Yeah.{w} Are you awake now? 」"
    fn "「I already am, {w=.2}completely. 」"
    "With a loud shout like that, {w=.2}of course I am.{p}It made me jump to my feet and snap awake at the same\ntime."
    fn "「Juuichi-san, {w=.2}can you wake me up like that every\n\ \ morning from now on? 」"

    show ju 003 with dis
    
    ju "「...I'm an alarm clock? 」"
    fn "「Hehe. 」"

    show ju 001 with dis
    
    ju "「...Go wash your face first.{w} Then go eat breakfast. 」"
    fn "「Got it- 」"
    "I give a great big stretch.{p}Today is the second day of camping.{p}Let's enjoy it as much as I can!"
    
    jump camp15_explore

######################################
label camp15_wakeup_shin:
    
    $ event_name = "Morning needles"
    
    who "「How much longer are you planning on sleeping? 」"
    "Shake shake shake."
    "Half-awake, I sense somebody shaking my body.\nThe gentle rocking begins to send me back to sleep."
    who "「... 」"
    "The hand shaking me leaves,\nand I return to my half-awake state."
    "I'm still not awake enough to open my eyelids."
    
    play sound swing40_a
    
    fn "「Ah! Yeow-! 」"
    "A sudden pain lances into my cheek,\nand I sit bolt upright."
    fn "「Oww... 」"
    "I wonder what that was...\nIt's like I was just stabbed by something sharp."

    show si 001 at center with dis
    
    si "「Good morning. 」"
    fn "「G-good morning, Shin-kun. 」"    
    si "「Really. How long were you going to stay in bed?\n\ \ Even Kounosuke is awake by now. 」"
    fn "「Fweh? 」"    
    si "「Can you go wash that tardy face of yours? 」"
    fn "「Y-yeah, okay... 」"
    "Shin-kun is strict this morning..."
    
    jump camp15_explore

#########################################
label camp15_wakeup_kounosuke:
    
    $ event_name = "BWAH!"
    
    who "「Heey,{w=.2} wake up- 」"
    "Someone is calling me."
    "I feel somebody approaching as I'm half-asleep,{p}but my brain has instructions to give\npriority to this cozy slumber."
    "..."
    "...?"
    "..."
    "--- ---"
    fn "{size=+15}「BWAH! 」"

    show ko 003 at center with dis
    
    ko "「G'mornin', sleepyhead. 」"
    fn "「Are you trying to kill me!? 」"

    show ko 001 with dis
    
    ko "「Of course not.{w=.2}\n\ \ I was just exaggerating. 」"
    "Exaggerating, huh?{p}He was squeezing my nose shut and\ncompletely covering my mouth!"
    "That's usually called suffocation..."

    show ko 004 with dis
    
    ko "「Anyway,{w=.2} are you going to wash your\n\ \ face and brush your teeth soon?{p}\ \ Everybody's already awake. 」"
    fn "「Everybody? 」"

    show ko 001 with dis
    
    ko "「Yup.{w=.2} You're the last one. 」"
    fn "「... 」"
    "The fact that Kounosuke woke up with\neverybody else is a miracle, isn't it? "
    "But, me sleeping in later than\nKounosuke is simply shocking..."

    show ko 002 with dis
    
    ko "「Come on,{w=.2} hurry,{w=.2} get up and wash your face.{p}\ \ Brush your teeth.{p}\ \ Sleepyhead~. 」"
    fn "「Y-{w=.2}yeah.{w} I got it. 」"
    "Kounosuke pushes at my back,{p}I crawl out of bed and go to wash my face."

    hide ko with dis   
    
    jump camp15_explore

###################################
label camp15_explore:

    $ event_name = "Nature"

    stop music fadeout 1
    scene black with sdis
    scene camp_site with sdis
    play music daily05
    $ renpy.music.set_volume(0.7, 0.0, channel = "music")
    show to 001 at center with dis

    to "「All right,{w=.2} now that we've eaten,{p}\ \ let's do something fun! 」"
    fn "「We were so busy setting things up yesterday... 」"
    
    hide to with wipe_right
    show su 004 at center with wipe_right

    su "「What are we going to do? 」"
    
    show ko 001 at farright with wipe_right

    ko "「I thought that we should do some exploring first. 」"
    
    scene camp_site with wipeleft
    show ky 001 at center with wipeleft

    ky "「If you go farther in from here there's a swamp,\n\ \ and there's also a hot spring near there. 」"
    
    show si 001 at farright with wipeleft

    si "「What should I do... 」"
    
    scene camp_site with wipe_right
    show so 001 at farleft with wipe_right

    so "「We went through all this trouble,\n\ \ so it should be somethin' everybody can do. 」"
    
    show ka 001 at farright with wipe_right

    ka "「If that's the case,\n\ \ the things we could do are limited. 」"

    show ju 001 at center with wipe_right

    ju "「When we got here,{w=.2} everybody had their\n\ \ own idea of what they wanted to do. 」"
    
    scene camp_site with wipeleft
    show ta 006 at center with wipeleft

    ta "「We've got all these different opinions,\n\ \ but this is usually how it is. 」"
    "What do I want to do...{p}I can't think of anything in particular.{p}I feel stupid for not being able to think of anything."
    "I'll ask the others what they'd like to do..."

###########################################
label camp15_choice:
    
    menu:
        "A. Rely on Tatsu-nii.":
            jump camp15_tatsuki
        "B. What's Shun planning to do?":
            jump camp15_shun
        "C. I guess I should go with Kouya.":
            jump camp15_kouya
        "D. What will Kounosuke suggest?":
            jump camp15_kounosuke
        "E. I wonder what Shin-kun is going to do?":
            jump camp15_shin
        "F. Let's hear what Juuichi-san's plan is.":
            jump camp15_juuichi
            
##################################
label camp15_tatsuki:

    $ event_name = "Exploration Party"
    $ love_tatsuki += 1
    $ focus_character = "kounosuke"
    
    "Since he's the oldest,\nlet's see what Tatsu-nii wants to do."
    fn "「Hey,{w=.2} Tatsu-nii. 」"
    fn "「Is there something you wanted to do? 」"

    show ta 001 with dis
    
    ta "「Yeah, of course there is! 」"
    fn "「And what would that be? 」"

    show ta 002 with dis

    ta "「I want to explore. 」"
    fn "「Exploring,{w=.2} huh... 」"
    "What an odd suggestion from the oldest one here..."
    
    hide ta with wipe_right
    show to 001 at center with wipe_right

    to "「I'm going to fish, even brought a pole. 」"
    
    show so 001 at midright with wipe_right

    so "「How about soccer?{p}\ \ We'll have five per team,{p}\ \ I think it'd be fun with this many people here. 」"
    
    show ky 001 at farright behind so with wipeleft

    ky "「Taro, you really do love soccer. 」"
    
    show so 003 with dis

    so "「'course I do! 」"
    
    show si 001 at farleft with wipeleft

    si "「I'll just take it easy around here. 」"
    
    scene camp_site with wipe_right

    "We haven't settled on anything..."
    
    scene black with sdis

    "30 minutes later..."
    
    scene camp_site with Dissolve(1)
    show ta 009 at center with dis

    ta "「All right, let's do this.{p}\ \ I'm starting the Midoriya Exploration Party. 」"
    
    show su 002 at farright with wipeleft

    su "「Woof! I'll come exploring! 」"
    
    show ko 005 at farleft with wipe_right

    ko "「Haah, we never did settle on anything. 」"
    fn "「Anybody else? 」"
    
    scene camp_site with wipeleft
    show ka 001 at center with wipeleft

    ka "「I saw Juuichi-san dragging Torahiko off.{p}\ \ Looks like he did something again. 」"
    
    show ta 001 at farleft with wipeleft

    ta "「Kyouji and Soutarou are enjoying themselves,\n\ \ so we'll just leave them alone. 」"
    fn "「Then what about Shin-kun? 」"
    "I look around and see him reading under the\nshade of a tree."
    
    scene camp_site with wipe_right
    show ta 002 at center with wipe_right

    ta "「Shin, join the Midoriya Exploration Party! 」"
    
    show si 004 at farright with dis

    si "「Tatsuki-san, I'm fine.{p}\ \ I'm just going to read this book. 」"
    
    show ta 008 with dis

    ta "「This isn't the place to be reading.{p}\ \ Let's explore! 」"
    
    show si 001 with dis

    si "「But this place is good, precisely because...{p}\ \ What are you going to explore? 」"
    
    show ta 001 with dis

    ta "「Actually... 」"
    
    show ta 002 with dis

    ta "「There's a river here that leads to a waterfall.{p}\ \ A guardian spirit is said to live in the basin. 」"
    ta "「We're going to find it! 」"
    
    show ta 004 with dis

    ta "「The name for this exploration is\n\ \ 'I saw the Mysterious Giant Salamander at\n\ \ the Waterfall Basin Deep in the Mountains'!! 」"
    
    show ka 005 at farleft with wipe_right

    ka "「How is it mysterious if you\n\ \ give away its true identity? 」"
    
    show si 003 with dis

    si "「See you later. 」"
    
    show ta 008 with dis

    ta "「Don't just say that and leave,\n\ \ there'll be huge crayfish, rhinoceros beetles,\n\ \ and maybe even lots of frogs! 」"
    
    scene camp_site with wipe_right
    show su 001 at center with wipe_right

    "Shun-kun doesn't need to make\nhis eyes sparkle anymore...{p}Everybody's going."

    show si 003 at farleft with dis
    
    si "「Don't be childish... 」"
    
    show su 005 with qdis
    scene camp_site with wipe_right
    show ta 002 at center with wipe_right

    ta "「There'll be some nice stag beetles too.{p}\ \ Stag beetles are tough.{w} There's also\n\ \ dragonflies and swallowtail butterflies there. 」"
    
    show ka 005 at farright with wipe_right

    ka "「Tatsuki-san...{p}\ \ We're exploring, not bug catching. 」"
    
    show si 004 at farleft with wipeleft

    si "「...Okay, if you insist.{p}\ \ I'm not interested in wildlife, however. 」"

    show ta 001 with dis
    
    ta "「Good, I was going to make you if you weren't. 」"
    
    show ta 004 at jump_up

    ta "「All right, we're leaving!{p}\ \ The Midoriya Exploration Party is departing! 」"
    
    scene black with sdis
    scene mountain_path2 with wipeleft

    fn "「We've been walking for quite a while.{p}\ \ I wonder where we are now? 」"
    "We're heading upstream,\nthe river goes deep into the forest."
    "We continue walking through the thicket.{p}Every time I inhale, the lush scent of trees\nfills my lungs."
    "Next to the stream, a glittering brook babbles,\nand the sunlight shining through\nthe trees flickers in the breeze."
    
    show ko 005 at center with dis

    ko "「Are we there yet?{p}\ \ I'm already exhausted. 」"
    
    show ta 002 at midright behind ko with wipeleft

    ta "「Gahahahaha!{w=.2} I don't know how much longer it is.{p}\ \ I did hear that we're gonna have to climb, though. 」"
    fn "「Who did you hear that from? 」"
    
    show ta 001 with dis

    ta "「My dad. 」"
    "Tappei-san, huh...{p}He doesn't seem to have much credibility."
    
    show si 001 at farleft with dis

    si "「I don't think complaining is going to\n\ \ accomplish anything.{w} It's selfish to blame,\n\ \ but let's just keep walking for the time being. 」"
    
    show ta 008 with dis

    ta "「What's the matter?{p}\ \ Who's to blame here? 」"
    
    show si 010 with dis

    si "「... 」"
    
    show ta 004 with dis

    ta "「Hey, watch yourself, this place is a jungle.{p}\ \ Don't let your guard down. 」"
    
    show ko 001 with dis

    ko "「This is just a thicket, isn't it? 」"
    
    show ta 008 with dis

    ta "「You're terrible... 」"
    fn "「Err... What? 」"
    
    show ta 004 with dis

    ta "「Look at this weird object!{p}\ \ This must be a something by the native people! 」"
    
    scene mountain_path2 with wipe_right
    show su 004 at center with wipe_right

    su "「'Do not leave empty cans' is written on it. 」"
    
    show ka 005 at farright with wipeleft

    ka "「...This is definitely something put up by natives. 」"
    
    show ta 008 at midleft behind su with wipe_right

    ta "「You're terrible... 」"
    
    scene mountain_path2 with wipe_right
    show si 010 at center with wipe_right

    si "「... 」"
    "Shin-kun's eyes are ice-cold..."
    
    hide si with wipe_right
    show su 002 at center with wipeleft

    su "「Oh,{w=.2} a butterfly. 」"
    
    show ko 003 at farright behind su with wipe_right
    
    ko "「Ah, it's an Oomurasaki. 」"
    fn "「It is. Those are common around here.{p}\ \ I even happened to see one in Minasato. 」"
    
    show ka 003 at farleft behind su with wipeleft

    ka "「Those things drive away wasps, don't they? 」"
    
    show ta 001 at midright behind ko with wipeleft

    ta "「I've seen 'em chasing small birds. 」"
    fn "「Yeah, they're pretty aggresive\n\ \ about defending their territory. 」"
    
    show ko 005 with dis

    ko "「Enough about that, I'm already worn-out... 」"
    fn "「I'm beat, should be take a quick break?{p}\ \ It looks like it's further than we thought. 」"
    
    show ta 004 with dis

    ta "「It's too soon to be giving up.{p}\ \ The Great Tatsuki Team makes\n\ \ the impossible possible!! 」"
    
    show ka 005 with dis

    ka "「You changed the name...? 」"
    
    scene mountain_path2 with wipe_right
    show si 004 at midright with wipe_right

    si "「Assuming we continue...\n\ \ If the waterfall isn't there,\n\ \ won't we just keep on walking? 」"
    
    show ta 008 at midleft behind si with wipe_right

    ta "「That's...{w=.2} we'll see.{p}\ \ Mmm, we do have a return time. 」"
    
    scene mountain_path2 with wipe_right
    show ko 004 at center with wipeleft

    ko "「Return? 」"
    fn "「Wait,{w=.2} is that it? 」"
    
    show su 001 at farleft with wipe_right

    su "「Oh, I can see the bottom of the waterfall! 」"

    show ta 004 at farright behind ko with wipeleft
    
    ta "「All right, let's go and take a look. 」"
    
    scene mountain_path2 with wipe_right
    show si 010 at center with wipeleft

    si "「That's strange. If there's a waterfall around here,\n\ \ we should have heard it. 」"
    
    scene waterfall1 with sdis

    fn "「This is... a pond? 」"
    "Ahead of us, there's a clearing,\nwith a small pond surrounded by rocks.{p}The water is so clear that you can see the bottom."
    "Hmm, it doesn't seem to be a waterfall basin,\nand there's no waterfall in sight."
    
    show ka 001 at center with dis

    ka "「Looks like a spring.{p}\ \ The river doesn't go on any further,\n\ \ so this must be the source. 」"
    
    hide ka with wipe_right
    show ko 001 at center with wipe_right

    ko "「Ah, I see. You can see the basin here,\n\ \ it's just that the waterfall we were\n\ \ talking about is different. 」"
    
    show ta 001 at farright behind ko with wipe_right

    ta "「First of all, let's look for\n\ \ what we came here for. 」"
    
    show su 002 at farleft with wipe_right

    su "「I agree. 」"
    
    scene waterfall1 with wipe_right
    show ta 004 at center with wipe_right

    ta "「Don't slip.{p}\ \ You won't get hurt, but negligence is forbidden. 」"
    
    show si 001 at farright with wipeleft

    si "「I think you're the most dangerous thing here. 」"
    
    show ta 002 with dis

    ta "「Gahaha.{p}\ \ No way...{nw}"
    show ta 003 with dis
    extend "] Whoa. 」"
    
    show si 005 with dis
    
    "Tatsu-nii takes a bad step and loses his balace.{p}It looks like he could fall at any moment."
    fn "「Wha-? Tatsu-nii, that's a weird place to grab on to. 」"
    
    scene waterfall1 with wipe_right
    show ko 006 at center with wipe_right

    ko "「Watch out! 」"
    
    hide ko with wipe_right
    show ka 005 at center with wipe_right

    ka "「Kounosuke, don't push. 」"
    
    hide ka with wipe_right
    show waterfall1 at vshake
    play sound splash
    
    "{size=+10}Splooosh!"
    
    scene black with sdis
    scene waterfall1 with wipeleft
    show ta 102 at center with dis

    ta "「Well, that felt good... sorry.{p}\ \ Forgive me if that was bad. 」"
    
    show ka 203 at farright with wipeleft

    ka "「You don't need to apologize for that.{p}\ \ It did feel good, it's pretty nice. 」"
    
    show su 201 at farleft with wipeleft

    su "「It feels nice to swim. 」"
    
    scene waterfall1 with wipe_right
    show ko 202 at center with wipe_right

    ko "「The water from the rocks\n\ \ is good enough to drink...! 」"
    
    hide ko with wipe_right
    show si 209 at center with wipe_right

    si "(I thought I was going to die...)"
    
    show si 212 with dis

    si "「Why did I have to get so wet?{p}\ \ And I wasn't planning on swimming in the only pair\n\ \ of underwear I brought. 」"
    
    hide si with wipeleft
    show ta 102 at center with wipeleft

    ta "「Sorry guys, I only have one pair of underwear. 」"
    fn "「Should we swim a little longer before going back?{p}\ \ Um, what did we come here for again? 」"
    
    show ta 108 with dis

    ta "「I heard there was a guardian spirit here. 」"
    
    show ka 201 at farright with wipeleft

    ka "「Even if there was one,\n\ \ it probably ran away when things got noisy. 」"
    
    show si 203 at farleft with wipeleft

    si "「There's no way a protected species would even be\n\ \ here in the first place. 」"
    
    scene waterfall1 with wipe_right
    show su 204 at center with wipeleft

    su "「That's too bad. 」"
    
    show ko 205 at farright with wipeleft

    ko "「There might be some ordinary fish around here. 」"
    fn "「But I am kind of glad that we found something\n\ \ like an unexplored area. You would never see\n\ \ a beautiful place like this in Minasato. 」"
    
    show ka 203 at farleft behind su with wipeleft

    ka "「I guess the result was\n\ \ worth coming out here for. 」"
    "I got tired of walking around soaking wet,\nbut as they say, all's well that ends well.{p}And this is definitely nice."
    
    show ko 201 with dis

    ko "「Huh?{p}\ \ What happened to Tatsu-nii's fundoshi? 」"
    
    scene waterfall1 with wipe_right
    show ta 103 with wipe_right

    ta "「It got washed away... 」"
    "..."
    
    jump camp15_packup
    
################################################
label camp15_shun:

    $ event_name = "Shun and the God of Marriage"
    $ love_shun += 1
    $ focus_character = "shun"

    scene black with dis
    stop music fadeout 1
    pause .5
    scene forest01 with Dissolve (1)
    play music free04
    $ renpy.music.set_volume(0.8, 0.0, channel = "music")
    show ky 001 at farleft
    show ko 001 at farright
    show so 001 at midleft
    show su 001 at midright
    with dis
    
    ky "「...So, this is a monument to the God of Marriage.\n\ \ It seems they say that it dwells within it. 」"

    show su 004 with dis
    
    su "「Wow-, I see- 」"

    show ko 011 with dis
    
    ko "「W,wait a minute, that isn't very convincing. 」"
    ko "「Don't you feel sorry for the second person?\n\ \ In the end, their sweetheart is taken away. 」"
    fn "「It sort of makes sense,\n\ \ although it looks like later you're supposed to\n\ \ have a real fateful encounter and live happily ever after. 」"

    show ko 005 with dis
    
    ko "「Hmm...mmm 」"
    "Standing near the campground, there's a fairly old-looking wooden sign with an arrow on it.{w} 'Mountain Trail' is written on it, and quietly in the corner, are the characters for 'marriage'."
    "Fascinated by this, we made our way down the trackless path indicated by the 'Mountain Path' sign, hoping that it wasn't wrong."
    "Somehow, we finally arrived at a place with what looks like a stone monument.{w} After reading an explaination of it's origins, we take a look around."
    ky "「It's pretty far off the wide trail,\n\ \ but there's a trampled pathway that leads\n\ \ to this medow with a monument in it. 」"
    ky "「This especially shows that many people stop here on\n\ \ their way up, that in itself is a blessing, isn't it? 」" 

    show ko 001 with dis
    
    ko "「I see. It's like following pioneers. 」"
    so "「There's different kinds of offerings around the monument. 」"

    show ky 002 with dis
    
    ky "「Hmm... Praying? That might be what it's for.\n\ \ It seems you offer something related to the\n\ \ person on your mind. 」"
    fn "「I thought it would be a little smaller than this,\n\ \ but it's a pretty big monument,\n\ \ and a lot of people have come here. 」"

    show ky 001 with dis
    
    ky "「This is the place where the god quietly sleeps too,\n\ \ so if we drag it out to pray to it,\n\ \ that might put it in a bad mood. 」"

    show so 005 with dis
    
    so "「F-For real? 」"
    fn "「On the other hand, it could be the god of divorce. 」"

    show so at jump_up
    pause .2
    
    so "「P-please stop! 」"
    ky "「Hahaha, you don't have to think about it that hard. If you \n\ \ pray while holding onto feelings of deep gratitude, you won't \n\ \ befall any sort of misfortune, no matter which god. 」"

    show so 006 with dis
    
    so "「I-is that true? 」"
    ky "「Look, if this monument is in accordance with the legend and\n\ \ has been here for hundreds of years, and we assume it's\n\ \ been left alone that whole time,"
    ky "shouldn't it be a little more worn-down? 」"
    ky "「There are a lot of goods being offered too,\n\ \ and in the case of the food, I think it would have been\n\ \ spoiled, eaten, or cluttered about. 」"
    ky "「It's been properly arranged in order to look this way.\n\ \ Somebody has been keeping this thing maintained.\n\ \ It's probably the campground manager. 」"
    ky "「Because of that, I don't think the god is in a bad mood. 」"

    show so 003 with dis
    
    so "「I see! That's a relief. 」"

    show ko 005 with dis
    
    ko "「It does feel like it's been skillfully put together\n\ \ to seem that way. 」"
    fn "「Hahaha, well then, I'll pray for everybody. 」"
    "Then, as I'm about to take a step forward,"

    show su 010 with dis
    
    su "「[fn]-san...um 」"
    "Shun-kun hangs his head down and speaks to me."

    show su 016 with dis
    
    su "「Is Minasato's shrine god going to get angry? 」"
    fn "「Huh? 」"
    "He seems to think that\nif you make a request to another god,\nMinasato's god will become very jealous."
    "I see.\nThat somewhat brooding behavior he had\nwas because he was worried about this."
    ky "「Shun is the type to worry about those kinds of things 」"

    show so 005 with dis
    
    so "「Eh...I don't think it'll get angry, but... 」"

    show ko 003 with dis
    
    ko "「It should be all right, shouldn't it?\n\ \ We're pretty far away from that shrine 」"
    su "「B-but what about all the way up in the sky?\n\ \ It could be watching us from there 」"
    "Shun-kun looks seriously worried.\nWhat should I do? We stopped here to pray,\nmaybe we should go back... but we've already come this far."
    ky "「Hmm... If Shun thinks Minasato's god\n\ \ is important, then why not ask\n\ \ both gods to answer our prayers? 」"

    show su 001 with dis
    
    su "「Oh! You can do that!? 」"    
    ky "「Between both gods, it should work out all right.\n\ \ If you're still worried, you can pray to the god back home\n\ \ before praying to the god here 」"    
    ky "「You could make the two gods become friends, right? 」"
    "Then, Kyouji shows a slight wink.\nIn that instant, the light in Shun-kun's eyes quickly returns."

    show su 002 at jump_up
    
    su "「Okay!{w=.2}{nw}"
    hide su with dis
    extend "　Umm, umm\n\ \ Minasato's shrine god, today I am saying hello from far\n\ \ away,I've gone camping with everybody... 」"
    "Shun-kun speaks with his back turned to the stone monument and looking up at the sky."
    ky "「Well then, I'm praying for many long years of\n\ \ friendship with Soutarou 」"
    
    show so 006 with dis
    
    so "「Wait Takahara-senpai! I'm prayin' too! 」"
    ky "「For soccer, I'm guessing? 」"

    show so 005 with dis
    
    so "「……{w=.2}{nw}"
    show so 001 with dis
    extend "Y-yeah!{w=.2}　of course! 」"
    "Soutarou-kun looks a little down."

    show ko 008 with dis
    
    ko "「... 」"
    "Next to me, the always noisy Kounosuke\nis unusually silent... No, under his breath\nhe's mumbling something with his hands together."    
    ky "「Well, we should get going soon 」"

    show so 003 with dis
    
    so "「Okay! 」"

    show ko 006 with dis
    
    ko "「...Ah, wait a minute,\n\ \ I'm still not done yet...whisperwhisper 」"
    
    scene forest01 with dis
    show su 002 at center with dis
    
    "Quickly, Shun-kun turns in place\nand faces his body this way,\nthen finishes his prayer to the god on the other side."
    fn "「Well then Shun-kun, did you pray to both of them? 」"

    show su tailwag 01 with dis
    
    su "「Yes! 」"

    jump camp15_packup

#####################################
label camp15_kouya:

    $ event_name = "Kouya's search for the light"
    $ love_kouya += 1
    $ focus_character = "kouya"
    
    fn "「Kouya, what are going to do? 」"
    "For now, I'll ask Kouya,\nsince he's closest to me."

    show ka 001 at farright behind ta with dis
    
    ka "「Well... First I was going to hang around here.\n\ \ I've kind of been looking for something. 」"
    fn "「Looking for something...? 」"
    ka "「Well, it's nothing big,\n\ \ but I don't have anything in particular to do.\n\ \ I just thought I'd kill some time. 」"
    "?"
    "I don't really understand what he's on about.\nHe said he's looking for something,\nbut he doesn't know what he's looking for."
    "But hearing him say something so\nmysterious raises my interest.\nIt piques my curiosity."
    "What could Kouya be looking for\nin the great outdoors!?"
    "Everybody else also seems to be a little interested,\nthey're showing a sense of wordless wonder."

    show si 001 at farleft behind ta with dis
    
    si "「...So, how is this going to end up? 」"
    "In the middle of this, Shin-kun's\ncold voice drops down on us."
    "I return to the question\nthat I had completely forgotten."
    "Then everybody lets out a groan at the same time."

    show ta 001 with dis    
    
    ta "「Ah, it's already too much trouble!\n\ \ All right, now it's free time!\n\ \ Everybody go do whatever you want! 」"
    "Since he's the oldest,\nTatsu-nii has the voice of authority."
    "There are no objections, only words of agreement."
    "Eventually, his words of command\nsmoothly put an end to the conversation."

    show ta 004 with dis
    
    ta "「But!{p}Keep an eye on the time for coming back!{p}{nw}"
    show ta 002 with dis
    extend "That is all! 」"

    scene camp_site with sdis
    stop music fadeout 1
    play music free0213 fadein 1
    $ renpy.music.set_volume(0.8, 0.0, channel = "music")
    
    "At Tatsu-nii's orders, everybody\nscatters and begins to move."
    "Going to the outdoor bath, reading a book,\nor looking around, it seems everybody has already\ndecided what they're going to do."
    "What should I do?\nI'm used to thinking about the scene,\nbut now there's no need for that."
    "What Kouya was talking about\nearlier still hasn't left my head."
    "The more I think about it, the more it bothers me.\nIt just makes me even more curious."
    "In an instant, I'm filled with that feeling,\nand I can't resist anymore."
    "There's only one choice in my mind."
    "From time to time, people come across\na box with unknown contents,\nand now there is one such box in front of me."
    "If that's the case, then I have\nno choice but to open it, right?"
    "So, this is the negotiation phase..."
    fn "「Hey, Kouya. What you were talking about earlier...\n\ \ Can I come along too? 」"
    "I'm going to search for that thing, too.\nI walked up to Kouya to start talking."

    show ka 001 at center with dis
    
    ka "「Oh, it doesn't matter to me. 」"
    "Mission Complete!\nThat was easy."

    show ka 005 with dis
    
    ka "「But I don't know whether or not we'll find it,\n\ \ there's a possiblity we won't.\n\ \ You aren't going to complain? 」"
    fn "「Yeah, that's okay.\n\ \ We'll think about it when we get to it,\n\ \ let's just do this for the memories. 」"
    fn "「Besides, it'll be fun too! 」"
    "I said something nice just now.\nIf I just increased the tension,\nI wouldn't hesitate to congratulate myself."

    show ka 001 with dis
    
    ka "「Yeah, you're right about that. 」"
    "He just quickly brushed away my wise words."
    "...Well, he usually does that."
    fn "「Yeah... Hmmm.\n\ \ So, what are we looking for? 」"

    show ka 003 with dis
    
    ka "「That's a secret.\n\ \ If you come with me,\n\ \ you might find out! 」"
    "Kouya gives a mischievous smile,\nand briskly walks off."

    hide ka with dis
    
    fn "「Huh? Come on, tell me!\n\ \ Hey, wait up-! 」"
    "I half-jog to catch up to him."

    scene black with wipeleft
    scene forest01 with wipeleft
    
    "I'm searching for Kouya's secret.{p}Unaware of the details,\nI weave through the trees along with him."
    "In my chest, I feel an excitement\nI haven't felt since I was a kid."
    "We're on an adventure.\nWhen I think of it that way, it's very fun.\nIt feels like everything is eye-catching and fresh."
    "That's not the only thing I see.\nThe wind caresses me as it passes by,\nand smells of the trees and the grass at my feet."
    "The soft sunlight through the trees is warm."
    "All of these things awaken\na simple pleasure within me."
    fn "「...This reminds me, we used to walk\n\ \ like this when we did different things. 」"
    "Without talking to anybody, I mutter that to myself.\nI reminisce about far away memories."
    "All of them from the old times of Minasato."
    "The things we used to do as children,\nlike playing ball in the schoolyard,\ntalking about silly things in the candy store,"
    "or adventuring around in the hills and fields."
    "That was the way things always were."
    "Of all those things, I think\n'adventure' has a special place in my heart."
    "We never did find anything outrageous.\nAn ordinary walk like this is adventure."
    "But just the act itself was something special."
    "Even if we found nothing, I was happy with that."
    "To see things that have never been seen,\nthat's what I expected."
    "There's definitely a world beyond\nus that we still don't know about, isn't there? \nThat was the wish I think was always in my heart."
    "So I always enjoyed that."
    "Even five years later, that feeling has not changed."
    "Little by little, we've been growing into adults.\nEven though we've changed,\nthere are some things that have not."
    "Thinking about that seems to be a little exciting.\nI accidently laugh."

    show ka 001 at center with dis
    
    ka "「Hm, what is it? 」"
    "Hearing my laugh, Kouya turns to me, puzzled."
    fn "「Oh, just laughing while remembering... I guess?\n\ \ I used to walk around like this in Minasato. 」"
    fn "「I used to do things like this for fun\n\ \ I was thinking about that and laughing 」"

    show ka 003 with dis
    
    ka "「Returning to your childhood innocence? 」"
    fn "「You could say that. I'm glad\n\ \ I haven't forgotten this feeling. 」"
    fn "「Some parts of it are missing,\n\ \ but the time I spent with everybody five years ago\n\ \ is still perfectly within me. 」"
    fn "「It would be great if I could\n\ \ remember everything, wouldn't it? 」"
    "I mock myself,\nand a bitter smile rises to my face."
    "It's fun to reminisce,\nI wonder why I haven't been\nable to remember these things until now?"
    "When I consider that, it's a little painful."

    show ka 005 with dis
    
    ka "「What a lonesome thing to say. 」"

    show ka 001 with dis
    
    "Kouya scoffs at me."
    ka "「You can't help it if you forget about the past.\n\ \ Nobody is always living in the past.\n\ \ You can't know everything that has happened to you. 」"
    ka "「However, [fn]- 」"

    show ka 003 with dis
    
    ka "「You should make memories now.\n\ \ You can't make up for what you lost,\n\ \ but you can have memories to fill in what you had. 」"
    ka "「We should live in the present,\n\ \ shouldn't we? 」"
    fn "「Kouya... 」"
    "His words are a little rough."
    "But on the other side, I can see a certain kindness.\nI makes me feel happy.\nMy heart feels just a little lighter."
    "Kouya isn't straightforward.\nI think that to myself, but don't say it.\nBut I always think about that when I'm around him."
    "I would say that his way of speaking\nwas also this soft back then,\nbut that was a long time ago."
    "That is definitely what I'm the most familiar with."
    "So now I understand Kouya's consolation.\nTherefore, I'm happy."

    show ka 001 with dis
    
    ka "「Well, enjoy life now so that there's\n\ \ never a time when you hurt yourself.\n\ \ Just do that. 」"
    fn "「Yeah, you're right! 」"

    hide ka with dis
    
    "It just as he says."
    "For now, I'll make lots of memories.\nIf I can remember how fun this was,\nthen I'll definitely be fine."
    "I think my heart is a little stronger.\nThen, Kouya and I begin to walk.\nThe grass and trees rustle as we pass by."
    "There isn't much conversation,\nbut my time with Kouya is very comfortable."
    "I can't put it into words,\nbut it's like a strange sense of security."
    "I find myself breaking into a smile.\nThis really is fun.\nIt seems like I could walk like this forever."
    "As if that feeling is made real,\nwe rapidly go deeper into the forest.\nWe still have not stopped walking."
    "I am enjoying this, but wait a minute?"
    fn "「Now that I think of it... 」"
    "A question suddenly comes to mind,\nso I get Kouya's attention."

    show ka 001 at center with dis
    
    ka "「Hm? 」"
    "He looked over his shoulder at me."
    fn "「What are you looking for, anyway? 」"
    "I ask the same question I asked before.\nI still haven't heard an answer."
    ka "「You still want to know? 」"
    fn "「No, it's all right if you want to keep it a secret.\n\ \ But I think it would also be okay if you told me. 」"
    ka "「I see...\n\ \ Suffice to say, it's dark and wet,\n\ \ a damp place, I think. 」"
    ka "「A cave would be best. 」"
    fn "「...Are you going there to\n\ \ get the legendary crystal? 」"
    "I can do that for now if I can return."

    show ka 005 with dis
    
    ka "「This isn't an RPG. 」" 
    fn "「Mushroom hunting? 」"
    ka "「I might do that if they're growing there.\n\ \ Can you eat mushrooms that grow in caves?\n\ \ I don't think you can. 」"
    fn "「Yeah... I thought that, too.\n\ \ They're probably poisonous... 」"
    "It's not a crystal or mushrooms.\nWhat is it then?"

    show ka 001 with dis
    
    ka "「Speaking of valuble, this might be valuable too...\n\ \ View looking around here as something fun to do.\n\ \ That way it will definitely be good. 」"
    fn "「Hmm, if you say so. 」"

    hide ka with dis
    scene black with wipeleft
    scene mountain_path2 with wipeleft
    
    "We push our way further into the forest.{p}As our distance from the tent increases,\nthe rocks at our feet become noticeably more ragged."
    "The tall grass from before is now short like moss,\nit's more like it's sticking to the rocks,\nrather than growing on them."

    show ka 001 at center with dis
    
    ka "「Stop for a second. 」"
    "Kouya suddenly stands still."
    "Because it was so abrupt, the moss at my feet makes\nme slip and fall."
    fn "「Ow... What is it, Kouya? 」"
    "I ask him while using both\nhands to regain my posture."
    ka "「...Can you hear that? 」"
    fn "「Hear what? 」"
    ka "「The sound of the wind. 」"
    fn "「The wind...? 」"
    
    stop music fadeout 1
    play sound wind_noise loop
    
    "He's right, the wind is blowing a little."
    "The breeze shakes the branches,\nand the leaves sound like bells."
    "Hyuu-hyuu, sawa-sawa.\nIt's a very familiar sound."
    fn "「I can certainly hear it, but... 」"
    ka "「That's not it. Keep listening. 」"
    fn "「A-all right... 」"

    hide ka with dis
    
    "I try listening harder."
    "I just hear the wind from before.\nHyuu-hyuu, sawa-sawa."
    "But this is different. Kouya said so."
    "I close my eyes and concentrate harder."
    "Hyuu-hyuu, sawa-sawa.\nI can hear many things being moved by the wind."
    fn "「...? 」"
    "Before long,\nI notice some kind of low sound mixed in."
    
    play sound2 animal02  
    
    "It sounds like the low,\ndull groan of something inhaling."
    fn "「It sounds like 'goooo', then 'buoooo'.{p}\ \ It's like the wind is being\n\ \ sucked in and blown out... 」"

    show ka 003 at center with dis
    
    ka "「You noticed it, good job.\n\ \ Now, let's go towards that sound. 」"
    "Kouya pats me on the head,\nthen sets off again."
    fn "「Oh, wait up, Kouya! 」"

    hide ka with dis
    
    "This time, to prevent slipping,\nI jump from rock to rock while following him."
    
    scene black with wipeleft
    scene cave_entrance with wipeleft
    
    "Then, we finally reach it."
    fn "「...It's a cave. 」"
    "Actually, it seems too small to be called a cave.\nIt's more like a combination\nof big rocks, a little hole."
    "The trees blocking the sunlight hide it.{p}It feels like it's a secret."
    fn "「Is this what you were looking for? 」"
    "I ask him while pointing my\nindex finger at the dark entrance."

    show ka 001 at center with dis
    
    ka "「I'm more interested in what's inside.{p}\ \ I want to do a little nature observation. 」"
    fn "「Nature observation? 」"
    ka "「Well, you'll see when we go in.{p}\ \ I'll go first, you follow me slowly. 」"
    "After saying that,\nKouya suddenly grabs my right hand."
    fn "「Wha-{w=.2}Kouya...! 」"
    ka "「Hm? What? 」"
    fn "「N-nothing... 」"
    "When he unexpectedly grabbed my hand,\nI yelled out in surprise.{p}I couldn't help it."
    "Kouya gives me a slightly quizzical look,\nbut then keeps pulling on my hand."
    "Both of us enter the cave."

    scene black
    show ka 001 night at center 
    with wipe_right
    
    "Soon, damp air wraps around my body.{p}It feels kind of weird."
    "As you can imagine from being in the dark,\nI can only see a little from\nthe light coming in from outside."
    "In the all-too-faint light,\nI have no idea how far this hole goes."
    fn "「Kouya, it's so dark that\n\ \ I can't see a thing. 」"
    ka "「Hold on, I'll get some light 」"

    scene cave_entrance night 
    show ka 001 night at center 
    with sdis
    
    "After I hear a scraping sound a few times,\na dim light illuminates around us."
    "I can't see it because it's in my blind spot,\nbut it seems Kouya is using a lighter."
    fn "「Huh? You smoke? 」"

    show ka 005 night with dis 
    
    ka "「No,{w} just because I have a lighter\n\ \ doesn't mean I smoke.{p}\ \ It's a handy thing to have if you're camping. 」"
    fn "「Oh, I see... 」"
    ka "「Come on, let's go.{p}\ \ If we take too long, Tatsuki-san will yell at us.{p}\ \ Watch your step. 」"

    hide ka with dis
    
    "Saying that, Kouya moves on,{p}still gripping my hand."
    "I suddenly feel my temperature rise,\nand my heart beats faster.{p}My face is probably turning red."
    "Somewhat embarrassed, I bend my head\nand look down a little."

    show ka 001 night at center with dis
    
    ka "「Stop. 」"
    fn "「Alri-{w=.2}oof! 」"

    show ka 005 night with dis 
    
    "Once again, Kouya suddenly tells me to stop."
    "This time, instead of losing my balance,\nI decide to headbutt Kouya's back."
    "I think it's a cliched thing for me to do."
    ka "「What's with the headbutt...? 」"
    fn "「Sorry...\n\ \ But could you say 'stop' a little bit\n\ \ earlier than when you actually do stop? 」"

    show ka 001 night with dis
    
    ka "「...All right. Good news.{p}\ \ It looks like our target is here. 」"
    
    scene black with qdis
    
    "Suddenly, the light around us disappears.{p}Once again, our surroundings are pitch-black."
    "I can't even see Kouya's satisfied\nappearance in front of me."
    fn "「Kouya? 」"
    ka "「Watch. 」"
    "When he says that, I can't say anything more.\nWhile he talks to me,\nI stare into the darkness."

    scene cave_entrance night with Dissolve(.6) #Dark
    scene black with Dissolve(.3)
    
    "Then, an optical illusion?\nIt looks like the walls of the\ncave are starting to gradually light up."
    fn "「Huh...? 」"
    "But the illusion is real,\nthe light keeps getting brighter."

    scene white with Dissolve(1)
    stop sound fadeout 1
    scene cave_entrance night with Dissolve (.5) #Dark    
    play music melodious03 fadein 1
    $ renpy.music.set_volume(0.8, 0.0, channel = "music")
    
    "Soon, I can see it clearly.\nIt changes to the color of young green leaves,\nwith a hint of gold."
    "It's a weak light, like fireflies,\nbut it's definitely there.\nA quiet glittering fills this narrow space."
    "There are spots where the\nlight is stronger than others,\nand makes it look like some kind of pattern."
    "It's beautiful.{p}It looks as if it's been embedded\nwith stars from the night sky."
    "It seems magical, mysterious, and beautiful.{p}A gasp of wonder escapes from my mouth."

    show ka 001 night with dis #Dark
    
    fn "「Wow... 」"
    ka "「Can you see it? 」"
    fn "「Yeah... It's like the walls are shining... 」"
    ka "「It's luminous moss. 」"
    fn "「Huh...? 」"
    "I was so fascinated by the light\nthat I didn't quite understand what Kouya said."
    "I think he said... Luminous moss."
    ka "「This light is true to the moss' name.{p}\ \ It absorbs the small amount of light in here,\n\ \ which is why it appears to be shining. 」"
    ka "「You might find it in other places,\nbut it usually grows in damp places,\nespecially on rocks and in caves like this. 」"
    ka "「It's not very hardy,\n\ \ so a small change in its environment\n\ \ can instantly kill it. 」"
    ka "「It's on the verge of extinction.\n\ \ Because of that, it's a protected species,\n\ \ so you can't take it. 」"
    fn "「Wow...{w=.2} That was very detailed, Kouya. 」"
    ka "「I just know about this.{p}\ \ I learned about it a long time ago... From my dad. 」"
    fn "「Really?{p}\ \ So you and your dad have been here before? 」"
    ka "「No, this is my first time here.{p}\ \ I couldn't sleep last night, so I wandered around,\n\ \ and saw this on a rock near the tent. 」"
    ka "「The area around here is practically untouched,\n\ \ it's like it's all that remains of nature.\n\ \ I think this might be what I'm looking for. 」"
    ka "「That's good, this wasn't a wasted trip. 」"

    show ka 002 night with dis #!#Check if still night sprite
    
    ka "「I even got to show this to you. 」"
    "In the dim green light, I can see Kouya smiling.{p}That smile makes me happy for some reason."
    fn "「Kouya... 」"
    ka "「Are you glad you went? 」"
    fn "「Yes, Thank you. 」"
    "For a while after that, we silently\ngaze at the light in the cave."
    "There's nothing you can do about forgotten memories.{p}I'll be all right if I can remember the fun times.{p}That's what I thought earlier."
    "But, no matter what,\nI will not forget this."
    "That alone is what I wish for."

    jump camp15_packup

##########################################
label camp15_juuichi:

    
    if juuichi_hate == True:
        "...{p}A number of days have passed since that event,{w=.2}\nBut Juuichi-san still isn't speaking to me."
        "...I'd better choose someone else to hang out with."
        
        jump camp15_choice
    
    $ event_name = "Hot Springs, Steamy Romance, what's the difference?"
    $ love_juuichi += 1
    $ focus_character = "juuichi"
    
    fn "「What are you going to do, Juuichi-san? 」"
    "I ask Juuichi-san, who has his arms crossed,\ndeep in thought."

    hide ta with dis
    show ju 003 at center with dis
    
    ju "「Hmm...{p}\ \ Takahara said there are hot springs nearby.{p}\ \ Perhaps they will take care of my fatigue. 」"
    "That's right,{w=.2} he trains hard every day.{p}He doesn't talk about it,{w=.2}\nbut you can see the fatigue in his eyes."
    "All right, I too will help\nease Juuichi-san's fatigue!"
    "...My ulterior motive for doing\nthis is to see him naked?\nUhh... No! Not at all!"
    fn "「Is it all right if I come with you?{p}\ \ I can wash your back, if you like. 」"

    show ju 008 with dis
    
    ju "「I don't mind... 」"
    "Juuichi-san glances over at Tatsu-nii.{p}From here, I can see him making a fuss with Torahiko\nabout something."
    "...Apparently, Tatsu-nii is heading out to explore."

    show ju 001 with dis
    
    ju "「You don't think Tatsu-san\n\ \ is doing something more interesting? 」"
    fn "「No,{w=.2} I'd like to come with you.\n\ \ Hot springs are hard to find in the city... 」"
    "The others are talking of a quest\nto find the fountain of mystery.\n...Tatsu-nii, I hope you come back in one piece."
    "Juuichi-san looks like he's about to say something,\nthen sighs."

    show ju 003 with dis
    
    ju "「...Well, you might be choosing wisely this time. 」"
    fn "「Should we get going,\n\ \ before we get involved with Tatsu-nii? 」"

    show ju 001 with dis
    
    ju "「Yeah. 」"

    hide ju with dis
    
    "Sneaking back to the tent,{w=.2}\nwe grab our towels."
    "There's a dispute over who will lead the expedition.\nWe tiptoe past so Tatsu-nii doesn't notice us."

    show si 001 at center with dis
    
    si "「... 」"
    "Oh.{p}Shin-kun's eyes meet mine."
    "I put my hands together in front of my face and bow.{p}Sorry, please overlook this."

    show si 004 with dis
    
    "Shin-kun sighs and shrugs.{p}It seems he's pretending not to see us."

    hide si with dis    
    
    "Thank you, Shin-kun!{p}I'll have to show my gratitude somehow,\nwhen we get back to the village."
    "Juuichi-san and I depart from the campsite,\nheading towards the hot springs."
    
    stop music fadeout 3
    scene black with sdis
    scene river with sdis
    play music free0213
    play sound water03 loop
    $ renpy.music.set_volume(0.4, 0.0, channel = "sound")
    show ju 001 at center with dis
    
    ju "「We're here. 」"
    "After a 15 minute walk from the tents,\nwe finally arrive at our destination."
    "...Haah, that journey was pretty painful.{p}We went up and down slopes, on a trackless path...{w=.2}\nIt felt a bit like climbing."
    "Is he used to walking in the mountains,\nor is his physical strength just that good?{p}His breathing hasn't changed at all."
    "On the other hand,{w=.2} I don't play sports.\nI was exhausted before we even got here."
    "...Ooh,{w=.2} if I collapse before I soothe Juuichi-san,\nit'll be like putting the horse before the cart."
    "Well, we're already here,{w=.2}\nso let's get in the hot spring!{p}That should blow away my fatigue."
    "I look around.{p}Umm,{w=.2} where is this hot spring?"
    "In front of me, a stream is making a soothing sound.{p}Scattered further upstream are\nrocks about the size of a fist."
    "The water is very clear.{p}It looks good enough to drink."
    "The sunlight reflecting off the surface\nshines like a kaleidoscope,\nand I have to squint my eyes."
    "There's nature as far as the eye can see.{p}...It's really nice here."
    "Wait, this is the hot spring?{p}This is where I'm relaxing with Juuichi-san?"
    ju "「That's not it. 」"
    
    play sound2 shock1
    
    fn "「Huh?! 」"
    "I cry out in surprise at his words."
    fn "「There isn't a hot spring here? 」"
    ju "「There is. 」"
    
    play sound2 step13b
    hide ju with dis
    
    "Saying that, Juuichi-san walks\nbriskly towards the stream."
    "What does he mean?{p}There's a hot spring here, but I can't see it...?"
    "Juuichi-san searches around for something.{p}Before long, he finds it.{w=.2} Looking towards me,\nhe beckons me over."
    "Still uncertain, I walk over to where he's standing."

    show ju 001 at center with dis
    
    ju "「Try feeling the water here. 」"
    "I lean down, and dip my hand into the stream...{w=.2}\n{nw}"
    play sound2 mizu07   
    extend "Huh? It feels strange. I look up at Juuichi-san."
    fn "「This water is warm... 」"

    show ju 002 with dis
    
    ju "「It is. 」"
    "He nods his head in confirmation."
    "When I look closely,\nI can see small bubbles rising to the surface."
    fn "「...Even though there is a hot spring here,\n\ \ how are we going to soak in this? 」"
    "Confused, I ask Juuichi-san my question."

    show ju 001 with dis
    
    ju "「That's what this is for. 」"
    
    play sound2 jap_002
    pause .15
    play sound2 jap_002
    
    "Juuichi-san thrusts a shovel into the ground.\n...I have been wondering why he brought a shovel."
    fn "「...I'm guessing that's for making our own bath? 」"
    ju "「That is correct. 」"
    "Once again, Juuichi-san nods approvingly.{p}...I see, we still have some work to do before\nwe can relax in the hot spring."
    "I'm already exhausted from our walk,{w=.2}\nand I feel dizzy."
    "...But I'm doing this all for Juuichi-san.{p}I'll do my best!{w=.2} Go me!"
    ju "「Now, let's begin.{w=.2} I'll dig the hole.{p}\ \ You shape it so that it's easy to get into. 」"
    fn "「Got it. 」"

    hide ju with dis
    
    "We start contructing our handmade spa.{p}First, we move the stones that are too big."
    "Carrying them makes my face red with effort.{w=.2}\nNext to me, Juuichi-san carries two of similar size."
    "...Even though I'm working hard with both hands,{w=.2}\nhe easily carries it in one.{p}Plus, he's doing two at a time."
    "...Maybe I should train my body a bit more."
    "We get most of the big stones out of the way,{w=.2}\nthen get to work with the shovel."
    "While working with Juuichi-san,{w=.2}\nI can only really offer my support.{p}Hang in there, Juuichi-san, our goal is in sight!"
    "He digs until the hole is about as deep as my leg.{w=.2}\nBefore long, the hot spring gushes\nout from between the rocks."
    ju "「...Hmm. 」"
    "Juuichi-san quickly gets out of the hole."
    fn "「Is something wrong,{w=.2} Juuichi-san? 」"

    show ju 001 at center with dis
    
    ju "「No,{w=.2} it's just hotter than I thought it would be. 」"
    "Oh, really?{p}The water mixed with the stream was warm earlier,{w=.2}\nbut it looks like we're getting to the source."

    hide ju with dis
    
    "I borrow the shovel from him,{w=.2}\nand make a canal linking the river to our bath.{p}Cold water begins trickling in to our hot spring."
    "Juuichi-san nods again, approvingly.{p}That felt like a compliment.{w=.2}\nIt makes me happy."
    "A few minutes later, the hole is full of water.{p}We make a levee to block the small canal.{w=.2}\nWhen it gets too hot, we can just add more cold in."
    "I flatten the bottom of the hole,\nand surround the edge with rocks."
    "I check the temperature with my hand.{p}It might be a little cool,{w=.2}\nbut it's summer, so I think this is good."
    "...Then again, maybe not.{p}I talk to Juuichi-san, who is watching me work\nwith a small smile on his face."
    fn "「It's done! 」"

    show ju 001 at center with dis
    
    ju "「Yeah. 」"
    "At first, I thought I was going to hate this.\nBut somehow, making this\nopen-air bath was really absorbing."
    fn "「All right, let's get in! 」"

    play sound2 standup 
    
    "Full of anticipation, I pull off my shirt and pants.\nStanding there in my underwear,{w=.2}\nI see Juuichi-san isn't taking his clothes off."
    fn "「Juuichi-san,{w=.2} what's wrong? 」"

    show ju 003 with dis
    
    ju "「...This bath might be a too small for two people. 」"
    "As he says that, I take a look at it.{p}...He's right. There might be enough room for me,{w=.2}\nbut it might be a little difficult for both of us."
    "Damn.{p}How could we have made such a basic mistake?"
    ju "「[ln],{w=.2} you can go in first... 」"
    fn "「We made this together!\n\ \ It wouldn't be right if I get in first! 」"
    "I interrupt him with a strong tone."
    "Juuichi-san lets out a sigh.{p}He's like a father with his spoiled child.{p}...That might be true, in a sense."
    ju "「Then what would you suggest?{p}\ \ Should I get in while holding you? 」"
    fn "「Sure, that sounds fine. 」"
    ju "「...You're right.{p}\ \ No matter what the circumstances... 」"
    "What I just said sinks in.{w=.2}\nJuuichi-san looks a little flustered."

    show ju 001 with dis
    
    ju "「...You're okay with that? 」"
    fn "「Of course. 」"

    show ju 008 with dis
    
    ju "「...I see. 」"
    "Juuichi-san takes a deep breath.{p}{nw}"
    play sound2 standup
    extend "Did he make up his mind?\nHe's taking his clothes off."
    "It seems my feelings got through to him.{w=.2}\n...Since both of us went through the trouble,\nI'd feel awkward being the only one getting in."
    "While I was thinking about this,\nJuuichi-san finishes getting undressed.{p}He's now completely nude."

    show ju 101 with dis
    
    "Though there's nothing concealing me,\nI'm not embarrassed."
    "Is it because of this liberating feeling\nI'm getting from being in nature?{p}...I wonder if I'm inclined towards exposure?"
    fn "「Juuichi-san, since the hot water- 」"

    hide ju with dis
    play sound2 bosu34
    
    "Suddenly, I find myself airborne,\nand my words get cut off."
    "I'm being carried in Juuichi-san's arms,\nlike a princess."
    fn "「J-J-Juuichi-san!{w=.2}　Please put me down! 」"
    ju "「I can't hear you. 」"
    "The corner of his mouth curls up,{w=.2}\nshowing a fang."
    ju "「Aren't we getting in together? 」"
    "I'm at a loss for words.{p}...Even though I was the one who sowed these seeds,{w=.2}\nit feels like I've been outwitted by Juuichi-san."
    "While thinking about that,{p}Juuichi-san walks towards our handmade bath.{w=.2}\nConfused, I cling to his neck."
    
    stop music fadeout 3
    
    "The feeling of fur damp with sweat is comfortable.\nI can also smell his sweat,\nbut it is by no means unpleasant."
    "Juuichi-san lowers himself into the bath,{w=.2}\ntwists the upper half of his body,\nand puts me between his legs."
    "He holds me as I sit with my hands around my knees."
    "I gradually feel the warmth of his lower body."
    
    play music free60
    
    fn "「This feels really nice... 」"
    ju "「Yeah.{w=.2} it does... 」"
    "We appreciate the beautiful scenery\nbefore us for a while in silence."
    "...It feels like I'm doing something luxurious."
    ju "「...[ln].{w} Are you tired from all that\n\ \ unexpected hard work? 」"
    "While we're sitting and admiring the view,{w=.2}\nJuuichi-san asks me that."
    "I straighten my back as much\nas I can so that I won't be a burden."
    "Even though I'm trying not to lean on him,\nit seems like he saw through me."
    "Juuichi-san puts his hands on my shoulders,{p}and forces me to sit back down"
    fn "「Waah! 」"
    
    play sound2 water01
    
    "Unable to resist his sudden action,{w=.2}\nI fall into him.{p}He gently embraces me."
    ju "「...{w=.2}Don't be so reserved.\n\ \ Don't we have a relationship? 」"
    "He whispers into my ears.{p}....My face is definitely red now."
    fn "「Juuichi-san... 」"
    "I thought we were close earlier,{w=.2}\nbut now there's no distance between us.{p}Zero.{w} I'm stuck to him."
    "On my back, I can feel his warmth.\nIt's different to the warmth of the hot spring."
    fn "「We probably look like a\n\ \ parent and child doing this. 」"
    "I talk to him in order to hide my embarrassment."
    ju "「...What do you mean? 」"
    fn "「It means just that.{w} Juuichi-san,{w=.2}\n\ \ you look like my father... Somehow. 」"
    ju "「...Are you trying to say that I'm getting old? 」"
    fn "「Not at all. 」"
    "I burst into laughter.\nJuuichi-san worries about something like that?\nThat's kind of cute."
    "When I turn my head to look over my shoulder,{w=.2}\nI'm startled at how close his face is."
    "If I just extend my body a little, we could kiss.\n...Wait, why am I thinking that?!"
    "Embarrassed, I quickly look away.{p}My neck cracks,{w=.2}\nbut I'm too worried about other things."
    ju "「...What are you being so shy about now? 」"
    "I feel him let go of me a little.{p}I'm thankful for his consideration."
    fn "「...Sorry.{p}\ \ I didn't mean to make you worry. 」"
    ju "「I don't mind.{w=.2} That's my role as a senior. 」"
    "He pats me on the head as he says that."
    "Aah, he is an adult after all.{p}I think about this as he pats my head."
    ju "「...It's my duty. 」"
    "He mutters something,{w=.2}\nbut most of it is lost to the sound of the stream."
    fn "「Juuichi-san? 」"
    ju "「Oh, it's nothing.\n\ \ Never mind. 」"
    ju "「Well,we should be getting up soon.\n\ \ Everyone will worry about us if we're late. 」"
    fn "「You're right, let's get up. 」"
    "I'd completely lost track of time.{w=.2}\nI wish we could have spent longer here,\nbut Juuichi-san is right."
    "We get out of the bath,{w=.2}\n{nw}"
    play sound2 standup
    extend "and I start to dry myself off with my towel."
    fn "「Juuichi-san,{w=.2} did that help your fatigue? 」"
    "While pulling my shirt on,{w=.2}\nI ask him that, pretending it was nothing."
    "I mean, I did come here with that goal in mind."
    "If I just made him even more tired...{p}That would suck."

    show ju 401 at center with dis
    
    ju "「...Yeah,{w=.2} it did. 」"
    fn "「Then, I wasn't a bother to you? 」"

    show ju 403 with dis
    
    ju "「...Are you thinking about before? 」"
    "Juuichi-san smiles wryly.{p}Ooh, that was definitely it."

    show ju 412 with dis
    
    ju "「Every once in a while,{w=.2}\n\ \ it's all right to let one's\n\ \ hair down with someone else. 」"

    hide ju with dis
    
    "Saying no more than that, he quickly looks away.\nThank you, Juuichi-san..."
    ju "「Let's go,{w=.2} [ln]. 」"
    fn "「W-{w=.2}wait a minute, Juuichi-san!\n\ \ You still haven't put your shirt on! 」"

    stop music fadeout 1.5
    stop sound fadeout 1.5    
    jump camp15_packup

#########################################
label camp15_shin:

    $ event_name = "Tale of the Lying Kitten"
    $ love_shin += 1
    $ focus_character = "shin"
    
    "I wonder what Shin-kun is going to do?{p}Somehow, I can't see him saying 'exploring'."
    "Isn't he usually doing something like reading?"

    hide ta with wipe_right
    show ko 001 at offleft
    show si 001 at center with wipe_right
    
    fn "「Shin-kun, what are you doing? 」"
    si "「Me?{p}\ \ I haven't decided on anything in particular. 」"

    show ko at move_midleft(0.5)
    show si at move_midright(0.5)
    
    ko "「Oh,{w=.2} if that's the case- 」"

    show si 004 with dis
    
    si "「No thank you. 」"

    show ko 006 at jump_up
    
    ko "「Hey!{p}\ \ {nw}"
    show ko 005 with dis
    extend "I haven't even said anything yet... 」"

    show si 001 with dis
    show to 006 at offright
    
    si "「None of your suggestions has ever\n\ \ led to a pleasant experience. 」"
    fn "「That's true... 」"
    ko "「What's with you two today?{w=.2}\n\ \ It's like I'm some sort of troublemaker. 」"

    show ko at move_farleft(0.5)
    show si at move_center(0.5)
    show to at move_farright(0.5)
    
    to "「Well, it's true, isn't it? 」"

    show ko 011 at jump_up zorder 10 
    
    ko "「No way! 」"

    show si 004 with dis
    
    si "「...{w} By the way,{w=.2} \n\ \ an apple thief appeared in my garden last year. 」"

    show ko 005
    show to 003
    with dis
    
    ko "「Uh... 」"
    to "「Heh,{w=.2} that was you? 」"
    si "「Well, since it's been brought up,{w=.2}\n\ \ the criminal and you had very similar bodyweights.{p}\ \ He broke limbs off the tree he stole from. 」"
    
    play sound puu46
    show ko at shrink(0.8, 1)
    
    si "「Amaki received quite the shock.{p}\ \ Fortuantely, the tree didn't die.{p}\ \ {nw}"
    show si 001 with dis
    extend "Hm? Kounosuke,{w=.2} what are you hiding for? 」"

    play sound puu56
    show ko at shrink(0.5, 1)
    
    ko "「N-{w=.2}nothing... 」"

    show to 007 with dis
    
    to "「That's something a guilty person would do. 」"

    show si 004 with dis
    
    si "「Indeed.{p}\ \ The most stable branch on that tree was such a\n\ \ good place to nap, too... 」"

    show si 005 with qdis
    
    fn "「Huh? 」"
    "Just now, Shin-kun seemed to speak,\nbut no words came from his mouth..."

    show si 010 with dis
    
    si "「...It's nothing. 」"
    
    play sound pyoro57_b
    show ko 002 at shrink(1.0, 0.0)
    
    ko "「Huh?{w=.2}　[fn], did you know about Shin's hobby? 」"

    show si 012 with dis
    
    si "「Kounosuke. 」"

    show ko 005 at shrink(.8, 1)
    
    ko "{size=-10}「Ah-{w=.2} Never mind. 」"

    show to 001
    show si 001
    with dis
    
    to "「Whatever.{w=.2} What are we going to do now?{p}\ \ {nw}"
    show to 010 with dis
    extend "We're men, so we're going to explore, right? 」"

    show si 004 with dis
    
    si "「If you're just going to wander aimlessly,\n\ \ I'll pass. 」"

    show to 006 with dis
    
    to "「In a bad mood, as always.{p}\ \ {nw}"
    show si 001 with dis
    extend "what about you, [fn]? 」"
    fn "「Huh?{p}\ \ I was going to hang out with Shin-kun. 」"

    show si 005 with dis
    
    si "「Eh? 」"

    show to 007 with dis
    
    to "「Really...{p}\ \ {nw}"
    show to 001 with dis
    extend "I guess we'll go look around here, then.{p}\ \ Hey, Kounosuke, let's go. 」"

    show ko 001 at shrink(1, 0.0) 
    
    ko "「O{w=.2}-okay.{p}\ \ {nw}"
    show ko 003 with dis
    extend "See you later, Shin, [fn]. 」"    
    fn "「Later! 」"
    
    play sound step13b
    scene camp_site with wipe_right
    
    "The pair wave and disappear into the woods.{w=.2}\nI turn to Shin-kun."
    fn "「So,{w=.2} uh,{w=.2} what are you going to do? 」"

    show si 010 at center with dis
    
    si "「What are you asking me for?{p}\ \ Is there something you wanted to do? 」"
    fn "「Huh?{w=.2}　Uhh... 」"
    "Even though he asks me that..."
    "Let's see.{w=.2}\nOh, come to think of it,\nOne of the senpais mentioned a hot spring nearby."    
    "...A hot spring?{p}{nw}"
    play sound freeze04
    extend "That's good, right?"
    fn "「How about the hot spring?{p}\ \ Takahara-senpai said there was one around here. 」"

    show si 001 with dis
    
    si "「...Do you know where it is? 」"
    fn "「We could ask. 」"
    si "「Haven't they already headed over there? 」"
    fn "「What!? 」"

    hide si with dis
    
    "Alarmed by his words, I looked around.{w=.2}\nTrue enough, everybody was gone."

    show si 001 with dis
    
    fn "「W-{w=.2}what the hell...{p}\ \ When did that happen? 」"
    si "「While we were talking to Kounosuke earlier. 」"
    
    play sound shock1
    
    "They went without saying anything?\nThey're too cruel!"
    fn "「I wish somebody had said something... 」"

    show si 010 with dis
    
    si "「They did, didn't they?{p}\ \ Or did you not hear them? 」"
    
    play sound shock1
    pause .2
    play sound shock1
    
    "{size=+15}T-that's a lie!"

    show si 004 with dis
    
    si "「You didn't hear them, did you. 」"
    fn "「...No. 」"

    show si 003 with dis
    
    si "「Really. You're a match for Kounosuke. 」"
    "You didn't need to go that far."

    show si 001 with dis
    
    si "「Since you don't know where you're going,{w=.2}\n\ \ why not just aimlessly wander?{p}\ \ I give up. 」"
    fn "「...Okay. 」"
    "As always,{w=.2} Shin-kun's words are merciless."
    "Reluctantly, Shin-kun and I walk back to the tent,{w=.2}\nand sit on some nearby rocks."
    
    play sound paper00
    
    "Shin-kun produces a book,\nand begins to flip through the pages.{w=.2}\nWas this his plan from the beginning?"

    show si 010 with dis
    
    "It looks like a foreign novel."
    "I contemplate asking about it,\nbut even if he tells me,\nI don't think I'll know anything about it."
    "I put the thought out of my mind."
    si "「{cps=10}. . .{cps=40}{w} Pardon me. 」"
    fn "「Huh?{w=.2}　What is it? 」"
    si "「Did you really want to go with everyone else? 」"
    fn "「N-{w=.2}no, thats...{w=.2} Exactly right...{p}\ \ It was my fault, though. 」"
    si "「I see. 」"
    "He's hidden behind his book,\nso I can't see his expression.{w=.2}\nIs he concerned about me getting left behind?"
    fn "「So,{w=.2} what kind of book is that? 」"
    si "「...{w=.2}It's a fairy tale.{p}\ \ It's a story about a lying cat. 」"
    fn "「W-wow. 」"
    "I wasn't expecting such an exact reply."
    "I thought he would cut me off with a\n\"you probably wouldn't understand\"...{w=.2}\nWill it be all right if I dig a little deeper?"
    fn "「U{w=.2}-um, yeah.{p}\ \ Is it okay if I come over there? 」"

    show si 001 with dis
    
    si "「...Why? 」"
    "At my question,{w=.2}\nShin-kun shifts his gaze to me."
    fn "「W-{w=.2}well, no particular reason... 」"
    si "「... 」"
    
    show si 010 at move_midleft(1.5)
    
    "Shin-kun says nothing, and returns to his book.{p}However, he has shifted over a little.{w=.2}\nDid he just make space for me to sit next to him?"
    "Uhh, does that mean he's okay with it?{p}He might have been adjusting his sitting position..."
    "Confused, I say nothing for a short while.{w=.2}\nAah, to hell with it.{p}I boldly move over next to Shin-kun's side."
    si "「... 」"
    "No immediate complaints.{p}That's a start."

    show si 001 with dis
    
    si "「Isn't this a little narrow? 」"
    fn "「Huh?{w=.2}　Oh, sorry.{p}\ \ You're right. 」"

    show si 010 with dis
    
    si "「I didn't say that this is a bad thing. 」"
    fn "「Eh? 」"

    show si 004 with dis
    
    si "「If it's you, I don't mind. Go ahead. 」"
    "Huh...?{p}Could it be he's concerned for me?{p}It would be weird to check that, though..."
    "With the pair of us sharing the rock,{w=.2}\nour bodies are pretty close together,\nwhich I'm completely okay with."
    
    $ renpy.music.set_volume(0.4, 5.0, channel = "music")
    hide si with dis
    play sound paper00
    
    "That said, I still can't think of conversation.{w=.2}\nThe only sounds are the the rustling leaves,\nand Shin-kun turning the pages of his book."
    
    play sound paper00
    
    "It's like time is being stretched."
    "It feels like we're the only\ntwo people left in the world,{w=.2}\nas time passes us by."
    "Suddenly, the silence is broken by a strange sound."

    play sound wind_noise
    
    "Rustle rustle rustle,{w=.2}\nThe wind is flipping through\nthe pages of Shin-kun's book."
    fn "「Shin-kun, your book.{p}...Shin-kun? 」"

    show si 004 with dis
    
    "His body gently leaning against mine,{w=.2}\nhis breathing slow and even.\nHis eyes are closed."
    "He fell asleep...?{p}When did that happen?{p}Wait, Shin-kun dozed off?!"
    si "「... 」"
    "The silence is broken again,\nthis time by a rumbling sound.{p}Could this be... Purring?"
    fn "「...Pft. 」"
    "With that thought,\nI can't help but laugh a little.\nEven Shin-kun has a soft side."
    "Taking care not to wake him,\nI adjust my position on the rock.\nI feel his soft warmth leaning against me."
    "I wonder when everyone else will return?{p}Until then, just for a while,\nI'll enjoy this world of Shin-kun and me."

    $ renpy.music.set_volume(0.75, 1.0, channel = "music")
    
    jump camp15_packup

########################################
label camp15_kounosuke:

    $ event_name = "Exploration Showdown"
    $ focus_character = "kounosuke"
    $ love_kounosuke += 1

    hide ta with wipe_right
    
    fn "「Kounosuke, what are you doing? 」"

    show ko 002 at center with wipe_right
    
    ko "「I'm going to look for a mysterious new creature, {p}\ \ of course. 」"
    "Holding the camera dangling around his neck, Kounosuke{p}gives me a triumphant reply."

    show ju 001 at farright with wipeleft
    
    ju "「I wonder if we shouldn't let him wander off again. 」"

    show ta 008 at farleft with wipeleft
    
    ta "「Hey hey, come and explore with me. 」"
    fn "「Hmm, what should I do? 」"

    show ko 001 with dis
    
    ko "「I think you should go exploring with me, right? 」"

    show ta 002 with dis
    
    ta "「What are you talking about?{p}\ \ I'm the oldest here, so it's my responsibility to be{p}\ \ the captain. 」"

    show ko 005 with dis
    
    ko "「What, I want to be the captain. 」"

    show ta 009 with dis
    
    ta "「Nonono, I'm not handing that over. 」"

    hide ju with wipeleft
    show si 004 at farright with wipeleft
    
    si "「It doesn't matter either way. 」"
    "In the end, they couldn't come to an agreement.\nBoth of them argued over who would be the captain for a long time."

    show si 001 with dis
    
    si "「Why not try this?{p}\ \ Both of you will be leaders, and have a contest to see who{p}\ \ can find something rarer. 」"
    
    show ta 004 at jump_up behind ko
    show ko 002 at jump_up
    pause .2
    
    tako "「That's it! 」" 
    "At Shin-kun's proposal, both of them stick out their fingers at{p}the same time."

    show si 004 with dis
    
    si "「Th-that's right, you'll need a time limit.{p}\ \ Who has a watch here? 」"

    show ko 001
    show ta 001
    with dis
    
    ko "「Oh, {w=.2} I have one 」"
    fn "「I've got one, just in case. 」"

    scene camp_site with wipe_right
    show su 002 at midright
    show ka 001 at midleft
    with wipe_right
    
    su "「I've got one too- 」"
    ka "「Same here. 」"

    scene camp_site with wipe_right
    show si 001 with wipeleft
    
    si "「It seems most of you have one.{w} We will meet back here \n\ \ at 12 sharp.{w} Kounouske's team should especially take care \n\ \ to not be late. 」"

    show ko 005 at farright with wipeleft
    
    ko "「You're already assuming I'm going to be late, aren't you? 」"

    show ta 002 at farleft with wipeleft
    
    ta "「That's how you usually are. 」"
    ko "「Bleh- 」"
    si "「Well then, now have the problem of dividing into teams. 」"
    
    scene black with sdis
    play music daily04 fadein 1.5
    scene forest01
    show to 001 at midleft
    show ko 004 at midright
    with Dissolve(.5)
    
    ko "「We just need to figure out what to search for, right~? 」"

    show to 007 with dis
    
    to "「He said something rare. 」"
    
    scene forest01 with wipeleft
    show ky 001 at midleft
    show so 001 at midright
    with wipe_right
    
    so "「Somethin' rare, somethin' rare...{p}\ \ On TV, new species are usually found in the jungle!{p}\ \ Or somethin' like that. 」"
    ky "「I don't think that would so easily happen in a forest like\n\ \ this. 」"

    show so 005 with dis
    
    so "「I guess so. 」"
    fn "「Well, maybe some kind of rare insect would work?{p}\ \ Like a rhinoceros beetle 」"

    scene forest01 with wipe_right
    show to 006 at midright
    show ko 001 at midleft
    with wipe_right
    
    to "「A rhinoceros beetle~? I don't think there's anything rare{p}\ \ about those. Kick any of the trees around here and you'll{p}\ \ find one right away. 」"
    ko "「Are they rare for city people? 」"
    fn "「Well, if it's not a common rhinocerous beetle, then it{p}\ \ might be a rare kind. 」"

    show to 001 with dis
    
    to "「Ahh, something like a Teracross? 」"

    show ko 004 with dis
    
    ko "「I think you mean 'Heracross'. 」"

    show so 005 at farright with wipeleft
    
    so "「Um, senpais?{p}\ \ Isn't it called 'Hercules'?... 」"
    
    toko "「... 」" 

    show ko 003 with dis
    
    ko "「W-{w=.2}well, those aren't supposed to be in this forest. 」"

    show to 002 with dis
    
    to "「Yeah, definitely. That's impossible. 」"
    fn "「It would be an environmental issue if \n\ \ there were any here. 」"

    show so 001 with dis
    
    so "「I see. 」"

    hide to with wipeleft
    show ky 001 at midright behind ko with wipeleft
    
    ky "「So then, what should we look for? 」"

    show ko 001 with dis
    
    ko "「Hmmm, plants and animals.\n\ \ I haven't seen a detailed encyclopedia, so I'm not sure{p}\ \ but there might be some kind of rare bug or wildflower. 」"
    fn "「Why don't we aim for something bigger?{p}\ \ Like some unexplored area nobody knows about. 」"

    show ko 005 with dis
    
    ko "「I think that would take a lot of time to find.{p}\ \ If we went in for just a short time, then it would{p}\ \ probably be something somebody already discovered. 」"
    ky "「More importantly, if we found such a thing, how would{p}\ \ you prove that you discovered it, [fn]? 」"
    fn "「Oh... you've got a point. 」"

    show ko 001 with dis
    
    ko "「It would be all right if I took a picture.{p}\ \ Anyway, please tell me if you find something unusual.{p}\ \ There could possibly be a new species. 」"

    scene forest01 with wipe_right
    show to 002 at center with wipe_right
    
    to "「Kounosuke-{p}\ \ How about this? 」"

    show ko 001 at farright with wipeleft
    
    ko "「What-?{p}\ \ {nw}"
    show ko 005 with dis
    extend "...Wait, aren't those just mating grasshoppers? 」"

    show to 001 with dis
    
    to "「That's not any good? 」"
    ko "「Be serious about this. 」"
    fn "「Kounosuke, what about that bird? 」"

    show ko 001 with dis
    
    ko "「Which one?{w} ...Oh, that.{p}\ \ I see those around Minasato all the time. It's a kind{p}\ \ of thrus. 」"

    scene forest01 with wipeleft
    show so 001 at center with wipeleft
    
    so "「How 'bout that? 」"

    show ko 001 at farright with wipeleft
    
    ko "「Ah, that bird is also found near the village...?{p}\ \ Huh? But it's pattern is slightly different?{p}\ \ I'll take a picture just in case. 」"
    fn "「Kounosuke, isn't this a rare flower? 」"

    scene forest01
    show ko 004 at center 
    with wipe_right
    
    ko "「Oh, that.{p}\ \ When I first saw it I thought so too, but it{p}\ \ looks like it grows wildly at various places. 」"

    show ky 001 at midright behind ko with wipeleft
    
    ky "「Kounosuke, what about this? 」"    
    ko "「Oh,{w=.2} I've never seen that flower. 」"
    fn "「Kounosuke, this? 」"

    show ko 005 with dis
    
    ko "「That? ...wait, that's just an ordinary drone beetle.{p}\ \ It is kind of big, though. 」"
    fn "「But it's growing some horns... 」"
    
    stop music fadeout 5
    
    ko "「Anyway you look at it, it's a drone beetle, right?{p}\ \ That shining bug...What... 」"

    scene forest01 with wipe_right
    show to 001 at center with wipe_right
    
    to "「Huh, is that a rhinoceros beetle? 」"

    show so 001 at midright with wipeleft
    
    so "「Looks like one, with that kind of shape. 」"
    fn "「But it's really shiny. It's golden. 」"

    scene forest01 with wipe_right
    show ko 006 at center with wipe_right
    
    ko "「No way... A new species!? 」"
    "Oh,{w=.2} it flew off."
    
    play music free0205
    show ko 005 with dis
    
    ko "「Ah! {w=.2} Hey, wait! 」"

    hide ko with wipe_right
    
    fn "「Kounosuke! You shouldn't run \n\ \ without looking where you're going. 」"
    
    play sound bosu31
    show forest01 at vshake
    show to 007 at midright
    show so 005 at midleft
    with dis
    
    "I told you so."

    scene forest01 with wipeleft
    show ko 005 at center with dis
    
    ko "「Ouch... 」"
    
    stop music fadeout 3
    
    fn "「Are you all right? 」"
    ko "「Somehow. 」"

    show ky 001 at farright behind ko with wipeleft
    
    ky "「I wonder what that was just now? 」"

    show ko 003 with dis
    
    ko "「A new species! It was definitely a new species! 」"
    
    play music daily04 fadein 1.5
    
    ky "「It must have been, I've never heard of a shining rhinoceros{p}\ \ beetle before... 」"

    show ko 002 with dis
    
    ko "「I knew it!{p}\ \ There are definitely rare things living in this forest! 」"
    fn "「I'm sure it's rare, but I wonder if rhinoceros beetles{p}\ \ really shine like that? 」"

    show ko 005 with dis
    
    ko "「I'd say so, even though you're the one who discovered it.{p}\ \ {nw}"
    show ko 001 with dis
    extend "We'll know when I develop the film. 」"
    fn "「You got a good shot of it, right? 」"

    show ko 002 with dis
    
    ko "「Perfect.{p}\ \ It might be a little blurry, but I'm sure I got the{p}\ \ subject precisely in this camera. 」"

    show so 005 at farleft behind ko with wipeleft
    
    so "「Are you sure it's okay to do that?{p}\ \ It could be cursed... 」"

    show ko 004 with dis
    
    ko "「It's just a shining beetle, right?{p}\ \ There's no way it would do that. 」"
    so "「I-{w=.2}I see. 」"

    show ko 001 with dis
    
    ko "「Should we take more pictures or withdraw?\n\ \ What time is it right now? 」"
    "When he asks that, we all take a look at our watches.{p}Or rather, I take a look at the clock on my cellphone."
    
    stop music fadeout 7
    
    "The time is 0:00...?"

    show ko 005 with dis
    
    ko "「Huh...? Is my watch not working? 」"
    fn "「No, I think mine's got the same time. 」"    
    so "「Mine too. 」"
    ky "「It looks like it's exactly noon. 」"
    "..."

    play sound bom35
    show forest01 at hshake
    show ko 006 big at center_big with explosion
    
    "{size=+15}「W-{w=.2}WE'RE LATE-! 」"

    scene camp_site with wipeleft    
    play sound stepfield01
    
    fn "「W-{w=.2}we just made it. 」"

    show ko 004 at center with wipe_right
    
    ko "「Sssafe? 」"

    show to 007 at farright behind ko with wipeleft
    
    to "「I think that would be an out. 」"

    show so 005 at farleft behind ko with wipe_right
    
    so "「Waaah, is there gonna be a punishment game? 」"

    scene camp_site with wipe_right
    show ta 006 at center with wipe_right    
    play sound stepfield01
    
    ta "「D-{w=.2}did we make it in time!? 」"

    show ka 001 at farright behind ta with wipeleft
    
    ka "「No, I don't think so. 」"

    show su 003 at midright with wipe_right
    
    su "「Woof, we finally got back- 」"

    scene camp_site with wipe_right
    show ko 005 at center with wipe_right
        
    ko "「Huh? 」"
    fn "「L-{w=.2}looks like they're late too. 」"

    hide ko with wipeleft
    
    show si 001 at midleft
    show ta 006 at midright
    with wipeleft
    
    si "「But Tatsuki-san. It seems the other team was late. 」"

    show ta 009 at jump_up
    pause .2
    
    ta "「Whaaat! Is that true? 」"

    scene black with sdis
    play music free22 fadein 1.5
    scene camp_site
    show ta 002 at midright
    show ko 001 at midleft
    with wipeleft
    
    ta "「Dahaha.\n\ \ Since we're both late, the punishment game will be for{p}\ \ the loser. 」"

    show ko 005 with dis
    
    ko "「I see. 」"

    show ta 009 with dis
    
    ta "「That's right.{p}\ \ It's already been decided it will be for your team. 」"

    show ko 006 with dis
    
    ko "「And why is that!? 」"

    show ta 008 with dis
    
    ta "「Well, there's no doubt about it.{p}\ \ We found a secret hot spring! 」"

    show ko 001 with dis
    
    ko "「A secret hot spring? 」"

    scene camp_site with wipe_right
    show si 001 at farright
    show su 004 at farleft
    show ka 003 at center
    with wipe_right
    
    ka "「Yeah. It's pretty far into the forest.{p}\ \ Nobody's probably ever been there. 」"
    si "「Anyway, we followed Tatsuki-san's intuition.{p}\ \ Thanks to him, we had a very difficult time finding our{p}\ \ way back. 」"   
    su "「I didn't think we were going to make it. 」"

    scene camp_site with wipe_right
    show ta 002 at midright
    show ko 001 at midleft
    with wipe_right
    
    ta "「How about it, Kounosuke? An illusionary secret hotspring{p}\ \ nobody knows about!{p}\ \ Did you find something rarer than that!? 」"

    show ko 005 with dis
    
    ko "「...Um, Tatsu-nii.{p}\ \ Where did you find it? 」"

    show ta 001 with dis
    
    ta "「Way back into the forest. 」"

    show ko 004 with dis
    
    ko "「Do you have any proof? 」"

    show ta 008 with dis
    
    ta "「What do you mean? 」"
    "..."

    show ta 003 at jump_up
    
    "Tatsu-nii makes a strange face.{p}I could have predicted this from the start, but did{p}he really do that?"

    show ta 006 with dis
    
    ta "「N-no.{p}\ \ But we got into the hot water there.{p}\ \ See? Look at this smooth skin. 」"

    show ko 001 with dis
    
    ko "「But it's sticky with sweat... 」"

    show ta 003 at jump_up
    pause .2
    
    ta "「Huh!? 」"

    scene camp_site
    show ju 001 at farleft
    show si 003 at farright
    show ka 001 at center 
    with wipe_right
    
    si "「Well, that's because he got dirty from wandering in the{p}\ \ forest. 」"
    ka "「Oh, with all this sweat and mud, you can't smell the{p}\ \ damn hot springs at all. 」"
    ju "「To make matters worse, I don't know the way there.{p}\ \ We can't take them back. 」"

    scene camp_site with wipeleft
    show ta 006 at midright
    show ko 003 at midleft
    with wipe_right
    
    ko "「It looks like this is the match. 」"

    show ta 009 with dis
    
    ta "「What did you guys find?. 」"

    show ko 002 with dis
    
    ko "「As for us, we found an extremely rare golden{p}\ \ rhinoceros beetle. 」"

    show ta 008 with dis
    
    ta "「A golden rhinoceros beetle?{p}\ \ Hey hey, there's no way something like that exists. 」"

    scene camp_site with wipe_right
    show to 001 at farleft
    show ky 001 at center
    show so 001 at farright    
    with wipe_right
    
    to "「Nope, we're not lying. 」"

    show so 003 with dis
    
    so "「It's true.{p}\ \ We all saw it. 」"
    ky "「Yeah, Kounosuke even took a picture of it. 」"

    scene camp_site with wipe_right
    show ta 006 at midright
    show ko 003 at midleft
    with wipe_right
    
    ta "「S-{w=.2}seriously...? 」"

    show ko 002 with dis
    
    ko "「Seriously.{p}\ \ It's right on this film... 」"

    show ko 006 with dis
    
    "Kounosuke stops moving the camera in his hand."
    fn "「What's wrong? 」"

    show ko 005 with dis
    
    ko "「Th-{w=.2}the film's not in my camera... 」"

    show ta 002 with dis
    show camp_site at hshake
    
    "{size=+15}「WHAT!? 」"

    scene camp_site with wipe_right
    show to 007 at farleft
    show ky 001 at center
    show so 005 at farright
    with wipe_right
    
    to "「Are you serious, Kounosuke!? 」"
    so "「Kuri-senpai, please be steady! 」"
    ky "「Ahhh, I knew this was going to happen. 」"

    scene camp_site with wipe_right
    show ta 002 at midright
    show ko 007 at midleft
    with wipe_right
    
    ta "「So that means this is a draw.{p}\ \ A happy ending. 」"

    show ko 005 with dis
    
    ko "「B-{w=.2}but we really saw it! 」"

    show ta 001 with dis
    
    ta "「If that's the case, then we really saw was a glittering{p}\ \ fountain at the end of a long and gloomy cave. 」"

    show ko 004 with dis
    
    ko "「That sounds like a lie. 」"

    show ta 004 at jump_up
    pause .2
    
    ta "「That's what it was! 」"
    "Uh-oh, they're starting again."
    fn "「Anyway, why don't we go get lunch soon?{p}\ \ I'm starving from walking around in the forest. 」"

    scene camp_site
    show to 002 at center
    show so 003 at farleft
    show su 002 at farright
    with wipe_right
    
    "「'Yes-!' 」"    
    fn "「Hey, you two. We're going to eat- 」"

    scene camp_site with wipe_right
    show ta 004 at midright
    show ko 005 at midleft
    with wipe_right
    
    ta "「You're always--- 」"
    ko "「Well you're always--- 」"
    
    stop music fadeout 7

    show ta 008 at jump_up
    pause .2
        
    ta "「○％＆△×☆□! 」"

    show ko 006 at jump_up
    pause .2
    
    ko "「＃％□＋△＊! 」"

    show ta 009 with dis
    
    ta "「△□×! 」"

    show ko 004 with dis
    
    ko "「○×××! 」"
    "We had no choice but to leave them alone."
    
    jump camp15_packup

######################################
label camp15_packup:
    
    $ focus_character = ""
    $ event_name = "Packing up"

    stop music fadeout 1.5
    scene black with sdis
    scene camp_site with sdis
    play music daily03 fadein 1.5
    show to 002 at center with wipeleft

    to "「Let's start cleaning up...! 」"
    
    show ky 001 at farright behind to with wipe_right

    ky "「We won't be finished before the day is over,\n\ \ so we'll be going home in the middle of the night.{p}\ \ Stay alert. 」"
    
    show so 001 at farleft with wipe_right

    so "「All right. 」"
    
    scene camp_site with wipe_right
    show ta 001 at center with wipe_right

    ta "「The baggage is the same as when we got here,\n\ \ so we'll be able to get it on the truck easily. 」"
    
    show ju 001 at farright behind ta with wipeleft

    ju "「I can carry the heavy things... 」"
    
    show su 001 at midleft with wipeleft

    su "「I can help too! 」"
    ju "「Kodori... go ask over there.{p}\ \ It looks like they don't have enough help. 」"
    
    show su 004 with dis

    su "「Am I not good enough? 」"
    "The luggage is too much for Shun-kun.{p}On the other hand, he might be able to carry it on\nthe way back."
    fn "「Physical labor is impossible for me too. 」"
    
    scene camp_site with wipe_right
    show si 001 at center with wipeleft

    si "「Is it impossible, or do you just not want to do it? 」"
    fn "「Th-{w=.2}that's not it, you're the one who doesn't\n\ \ want to do it. 」"
    si "「That may be, but there is a thing called\n\ \ 'the right person in the right place'. 」"
    si "「Would you really say that physical\n\ \ labor is suitable for me? 」"
    fn "「That's not it... 」"
    
    show si 003 with dis

    si "「Fine then...{p}\ \ If I get another asthma attack,\n\ \ are you going to take responsibility? 」"
    fn "「W-{w=.2}wait, Shin-kun. 」"
    
    hide si with wipeleft
    show ka 002 at midleft
    show ta 001 at midright    
    with wipeleft

    ta "「Shin, you look like you're in a good mood. 」"
    ka "「Is it because he's come out to play? 」"

    scene black with sdis
    scene camp_site red with sdis
    stop music fadeout 2

    "When the air is nice, the sky looks beautiful.{p}Everything has been put away,\nand there's nothing left to do."
    "..."
    "In just a short time we'll be done with camping..."
    
    play music melodious01
    
    "Today is the 15th, so I'm\nnow in the second half of my\nstay at Minasato..."
    "That was fast."
    "Because there's only half left,\nI wish I could stay in the village longer."
    "Well, we're returning..."
    "Huh?"
    
    $ affectionlist = [love_tatsuki, love_kounosuke, love_shun, love_kouya, love_shin, love_juuichi, love_soutarou, love_kyouji, love_torahiko]
    $ namelist = ["tatsuki", "kounosuke", "shun", "kouya", "shin", "juuichi", "soutarou", "kyouji", "torahiko"]
    $ selection = affectionlist.index(max(affectionlist))
    $ favorite = namelist[selection]
    $ focus_character = favorite
    
    $ renpy.jump ("camp15_confess_" + favorite)

#########################################
label camp15_confess_tatsuki:

    $ event_name = "Tatsu-nii"

    show ta 001 red at center with dis
    
    ta "「What are you doing here?{p}\ \ Let's get back to the village. 」"
    fn "「Tatsu-nii... 」"
    
    show ta 008 red with dis

    ta "「What is it? Is something wrong? 」"
    fn "「Well. 」"
    fn "「I was thinking about the second half of my vacation\n\ \ in Minasato and got kind of lonely. 」"
    
    show ta 002 red with dis

    ta "「Idiot. You're only halfway, right? 」"
    fn "「But the first half went by so quickly.{p}\ \ It would be bad if I didn't notice that until the\n\ \ day I go home. 」"
    
    show ta 008 red with dis

    ta "「What are you standing there feeling all alone for.{p}\ \ Try to remember that half that went by so fast. 」"
    ta "「There was your welcoming party, our trip to the beach,\n\ \ and we camped today.{p}\ \ Haven't you also been playing and working at my house? 」"
    fn "「And we're putting together an airplane. 」"
    
    show ta 002 red with dis

    ta "「That's right. 」"
    ta "「And with all that, there's also the second half.{p}\ \ Think of all the fun things ahead. Gahaha! 」"
    fn "「But it's going to be hard to go back home. 」"
    
    show ta 007 red with dis

    ta "「Then come back in Winter.{p}\ \ And if that's not enough, come back in Spring too. 」"
    
    show ta 004 red with dis

    ta "「If you say you can't come,\n\ \ then I'll come running, any time.{w} It's\n\ \ likely I'll get my dad's fist afterwards, though. 」"
    fn "「Wow, that's reliable. 」"
    
    show ta 001 red with dis

    ta "「So don't worry about what's ahead.{p}\ \ Just enjoy Minasato as much as you can now. 」"
    ta "「If you don't, even the things you like become dull. 」"
    fn "「Thanks, Tatsu-nii. I'm feeling better.{p}\ \ You're right, thinking about that would be a loss. 」"
    
    show ta 002 red with dis

    ta "「It would.{p}\ \ Besides, I might eventually go to the city too. 」"
    fn "「What, you're also leaving Minasato? 」"
    
    show ta 001 red with dis

    ta "「Yeah, I'll probably have to leave sooner or later to\n\ \ continue my training. But I've still got plenty of my\n\ \ apprenticeship left, so that's a few years away yet. 」"
    fn "「Then you might be closer to me. 」"

    show ta 008 red with dis
    
    ta "「Well, you never know what lies ahead.{p}\ \ To become a man, it would be bad to not leave home once.{p}\ \ But I will come back to carry on the family business. 」"

    show ta 001 red with dis

    ta "「[fn], what about you?{p}\ \ What are you going to do in the future? 」"
    fn "「Hmmm... I'm not sure.{p}\ \ First of all, I'll go to college.{w} Of course what you're\n\ \ doing is what you always talked about in the past. 」"
    
    show ta 004 red with dis

    ta "「Yes, to become the best craftsman in Japan. 」"
    fn "「It's nice that you have a goal. 」"
    
    show ta 002 red with dis

    ta "「I get lucky with these kind of things,\n\ \ so I ended up figuring it out faster than the others.{p}\ \ I think you'll find something if you look carefully. 」"
    fn "「Yeah. I wonder what I should do. 」"
    
    show ta 001 red with dis

    ta "「If you have nowhere to go, come to my house,\n\ \ and you'll be accepted immediately.{w} If I have to,\n\ \ I'll even use my authority as the next boss. 」"
    fn "「Hahaha, I'll think about it. 」"
    
    show ta 007 red with dis

    ta "「You'll get the job whether or not the\n\ \ business side decides it.{w} That's because\n\ \ they don't have the right to put you on hold. 」"
    fn "「First of all, I'd have to choose where to interview.{p}\ \ I wonder if I'd be profitible for the Midoriya Group... 」"
    
    show ta 008 red with dis

    ta "「Don't say that. What we're talking about, I'll make\n\ \ sure dad definitely hears all about it. 」"
    fn "「Th-{w=.2}that's okay. You don't need to go that far... 」"
    
    show ta 002 red with dis

    ta "「Heh, I understand, I understand. 」"
    
    show ta 001 red with dis

    ta "「Well, I won't ask for your help at my house tomorrow.{p}\ \ Same goes for the airplane, though it was pretty\n\ \ tiring to work on by myself. 」"
    fn "「I'll leave it to you then, it's gotten to\n\ \ the point where you're doing a good job on it. 」"
    
    show ta 008 red with dis

    ta "「That's nice of you to say,\n\ \ even though it's not ready to fly yet.{p}\ \ It really is a pain. 」"
    fn "「Eheheh. 」"

    show ta 001 red with dis
    
    ta "「Well then, we should get back.{p}\ \ If we keep talking here,\n\ \ everybody's going to worry about us. 」"
    
    hide ta with wipeleft

    "Tatsu-nii says that, then turns around to\nwalk back towards everyone.{p}I follow behind him."
    fn "「Yeah. 」"
    "Let's go back to Minasato."
    "The Amaryllis buds have begun to swell, showing that\nthe peak of Summer is declining."
    "My summer vacation has reached that point too,\nbut I shouldn't think about that."
    "I don't know what's going to happen,\nso I'll make sure to enjoy this year's summer,\nsince it only happens once."
    
    show ta 001 red at center with wipeleft

    ta "「[fn]. 」"
    fn "「What? 」"
    
    show ta 002 red with dis

    ta "「When the airplane is completed,\n\ \ we're going to fly together.{p}\ \ Don't forget. 」"
    fn "「Yeah, let's try our best. 」"
    "The second half..."
    "I'll enjoy it as much as I can."
    
    show ta 007 red with dis

    ta "「All right then. 」"
    fn "「Ah, that's dangerous Tatsu-nii.\n\ \ There's a cliff over there!! 」"
    
    show ta 003 with dis

    ta "「What!? Ah... WAAAAAAAAAAH!! [fn]!! 」"
    
    hide ta with wipe_down_slow
    play sound bosu26_b

    fn "「Tatsu-nii!! 」"
    
    $ route_lock = "tatsuki"
    
    jump end15

#########################################
label camp15_confess_shun:

    $ event_name = "I don't want it to end"

    show su 004 red at center with dis
    
    su "「[fn]-san. 」"
    fn "「Shun-kun?{w=.2}　What's wrong? 」"

    show su 010 red with dis
    
    su "「It's already time to go back, isn't it... 」"
    "His shoulders drop.{p}I see, since he got to play with everybody for two full days,\nhe's reluctant to go back."
    fn "「That's right, we have to. 」"
    "He has sad eyes and a dropping tail.{p}Shun-kun smiles at my words but also hangs his head down."
    fn "「Still, you're coming with everybody, right? 」"
    "I pet his head.{p}Usually, he would reply with an energetic response.{p}His brown coat is stained red with the setting sun."
    fn "「Are you sad? 」"
    su "「Yes...{w=.2}but I did get to take a bath with everybody,\n\ \ and I got to sleep and wake up early\n\ \ with you, Tatsuki-san, and Ko-ya-san.  」"
    su "「But everything will go back to the way it was tomorrow. 」"
    fn "「I'm sad too.{p}\ \ But I'll still get to have fun with everybody, right?{p}\ \ There's going to be the festival at Minasato's shrine. 」"
    su "「Y-yeah... 」"
    fn "「So don't look like that.{p}\ \ Did you have fun camping? 」"

    show su 002 red with dis
    
    su "「Yes! {w=.2}I got to play a lot!{p}\ \ I also got to hear a lot of stories,\n\ \ but there's still something I don't understand... 」"
    "I-is he talking about that obscene thing from yesterday?"
    fn "「If you really didn't understand, I'll tell you. 」"
    su "「Thank you very much!{w=.2}{nw}　"
    show su at jump_up
    extend "{w=.2}Woof! 」"
    fn "「Still, I have half of my summer vacation left?{p}\ \ I haven't talked or played enough with you.{p}\ \ There's still plenty of time. 」"
    fn "「So tomorrow will just be getting back to my vacation. 」"

    show su 004 red with dis
    
    su "「...{w=.2} {nw}"
    show su 002 red with dis
    extend "Yeah!{w=.2}　Okay! 」"
    fn "「Are you feeling better now? 」"
    su "「Yes! {w=.2}I still get to do\n\ \ plenty of fun things with you!{p}\ \ And everybody else!{w} So I'm already not sad! 」"

    show su 007 red with dis
    
    su "「[fn]-san, I like you so much-♪ 」"
    
    $ route_lock = "shun"
    
    jump end15

#######################################
label camp15_confess_kouya:

    $ event_name = "Time Limit - Countdown Phase"
    
    "Somebody approaches me from behind.{p}The Sun behind me makes a glare,\nso I'm not sure who it is."
    "That's..."

    show ka 001 red at center with dis
    
    fn "「Kouya... 」"
    "My eyes gradually adjust\nand I can see who it is."
    "He walks up straight up to me and\nasks me a question."
    ka "「What are you doing in a place like this? 」"
    fn "「Mm... {w=.2}I was feeling a little sentimental.{p}\ \ My summer vacation is already halfway over. 」"
    fn "「It feels like it's going faster than usual.{p}\ \ Time really has passed in the blink of an eye. 」"
    "When half of it was over,{w=.2}\n'There's still another half. I've got time,'\nis what I imagined I would be thinking."
    "Since it's hot, I didn't bother going outside much.{p}I just sat around in the house all day."
    "However, time keeps flowing,\nand my vaction keeps moving on."
    "But there is no room for\nthose feelings in this summer."
    "I also can't be wasting time.{p}There are so many things I want to-{w=.2}\nNo, have to do."
    "So I become filled with even more deep emotion."
    ka "「You're right...{p}\ \ I also think this year's\n\ \ summer has gone by quickly. 」"
    fn "「You too? 」"
    ka "「Yeah. 」"

    hide ka with dis
    
    "With just that short response,\nKouya turns toward the setting sun."
    "The light going into his eyes\nmakes them look beautiful.\nI follow suit, and turn my eyes too."
    "Red streaks color the sky."
    "The red in the distance shifts to blue above us,\nand being reflected off the clouds in some places,{w=.2}\nit makes a fantastic scene."
    "It's somewhat nostalgic,\nlike a scenery you've known\nof since before you were born."
    "I don't see this very often in the city.{p}The sky is narrow between the tall skyscrapers."
    "Maybe because I'm not used to this,\nit feels extra nice."
    "But this is informing of the approaching night."
    "When you think of it like that, it's something that\nconveys the fact that the day has begun to end,\nand that makes me feel a little sad."
    "Because of this feeling,\nI speak the words that are on my mind."
    fn "「If my vacation didn't end,\n\ \ I would be able to stay with everybody longer... 」"
    "That way, I could make more memories.{p}Then I could be with everybody longer.{p}That's what I thought."
    "There would no longer be such a thing as\ninsufficient time, I could have as much fun with\neverybody as I want."
    "It would be just like a dream."

    show ka 001 red at center with dis
    
    ka "「Yeah...{p}\ \ That probably would be nice. 」"
    "Kouya also agrees with me.{p}However, there was a somewhat sad tone in his voice."
    "Even I know why.{w=.2} It's simple."
    "We both know it's nothing more than a dream.{p}It's something that could never happen."
    "I know that too.{p}Because of that, Kouya doesn't say any more.\nI don't have anything to add after that."
    "The silence flows naturally between us.\nI feel a slightly cold wind."
    ka "「You know... 」"
    "After a while, Kouya begins to talk."
    fn "「What? 」"
    ka "「Someday... Summer vacation is going to be over. 」"
    fn "「...Yeah. 」"
    ka "「Then we should at least spend the remaining time\n\ \ together even more than we did before. 」"
    ka "「If you do that, then you'll be\n\ \ able to make more memories. 」"
    "Kouya ruffles my hair.\nEven though they were only a few words,\nI understood his encouragement."
    "His concern makes me happy,\nas well as a little embarrassed."
    fn "「Kouya... 」"
    ka "「When your vacation is over,\n\ \ the connection between us\n\ \ and your memories aren't going to disappear. 」"

    show ka 002 red with dis
    
    ka "「So... You'll be all right. 」"
    "Kouya gives a shy laugh as he says that."
    "His smile clears away the depressed feelings I had.{p}I can feel energy seep into the depths of my heart."
    "I spontaneously smile and turn toward Kouya."
    fn "「Yeah. 」"
    "He's right, it's nothing to worry about.{p}Just as he said, even if time passes,\nthis isn't going to disappear."
    "I had completely forgotten such an obvious thing."
    "But the most important part, the basis, has not.{p}In this half of a month,\nI've thought about this countless times."
    "If that's the case,\nI'm sure it will be this way in the future."
    "If that's the case, then that's enough for me."
    ka "「We should get back soon. It's getting dark. 」"
    fn "「Okay! 」"
    "When he says that, Kouya heads back the way he came.{p}I follow behind him."
    "'Then we should at least spend the remaining time\ntogether even more than we did before.'"
    "That's what Kouya said earlier.{p}While walking, I reflect upon it.{p}Then, I whisper in my mind:"
    "Thank you, Kouya."
    
    $ route_lock = "kouya"
    
    jump end15

###########################################
label camp15_confess_juuichi:

    $ event_name = "Words Sinking With the Setting Sun"
    
    "Everybody breaks away from the circle,{w=.2} leaving\nJuuichi-san standing alone.{w} For some reason, {w=.2}he stares\nat the remains of the campfire."
    "The burnt firewood is illuminated by the evening sun.{p}It glows a dull, {w=.2}fake orange that isn't from a flame.{p}The charcoal will probably never burn again, either."
    "It seems to have proclaimed the end of our camping\ntrip. I feel an undescribable loneliness."
    "I wonder what Juuichi-san is looking at that's so\ninteresting."
    fn "「Juuichi-san, {w=.2}what's the matter? 」"

    show ju 001 red at center with dis
    
    ju "「...[ln]. 」"
    "He looks at me, {w=.2}then returns to staring at the\ncampfire."

    show ju 003 red with dis
    
    ju "「I'm just thinking about something. 」"
    fn "「What's bothering you? 」"

    show ju 001 red with dis
    
    ju "「...I wouldn't say it's bothering me.{p}\ \ I just remembered something from the past. 」"
    fn "「Was it when I was still living here? 」"
    "He shakes his head."

    show ju 008 red with dis
    
    ju "「Not that far back.{p}\ \ It was about the time I started high school. 」"
    "I have no idea what it could be if that's the case..."
    "I can't fill that time I was away from everybody.{p}That doesn't mean it's my fault, {w=.2}or Juuichi-san's.{p}We were all just kids, {w=.2}it was beyond our control."
    "But it still stings my heart."
    fn "「I see... 」"

    show ju 001 red with dis
    
    ju "「Sorry,{w=.2}\n\ \ but it doesn't have anything to do with you. 」"
    "His expression is overtly stern.{p}There's no way I could pry any further than that."
    "...I'm sure it's something I can't just ask about out\nof curiosity."

    show ju 003 red with dis
    
    ju "「...I'm sorry 」"
    fn "「No, that's fine.{p}\ \ I was just being too nosy. 」"
    "Things have gotten awkward.{p}With that, Juuichi-san stays silent."
    "Him staring at the former bonfire is unusual.{p}It's like he's there in body but not in spirit."
    "I should say something.{p}But my thoughts keep going in circles.{p}It's caught in my throat and won't come out easily."
    fn "「Um, {w=.2}Juuichi-san... 」"
    ta "「Heey, {w=.2}what're you guys doing!?{p}\ \ Get in the truck already! 」"
    "Just as I nervously speak to him,{w=.2}\nTatsu-nii yells over me.{p}...That was really bad timing."

    show ju 001 red with dis
    
    ju "「...[ln], {w=.2}let's go. 」"
    fn "「Oh, {w=.2}yeah. 」"
    "He begins to walk briskly towards the truck.{p}I too head towards everybody."

    hide ju with dis
    
    "Juuichi-san's orange-dyed back walking fowards{w=.2}\n-the back that always looks so strong-{p}now looks weaker than usual to me."
    
    $ route_lock = "juuichi"
    
    jump end15

################################################
label camp15_confess_shin:

    $ event_name = "I'm not fond of Sunsets"
    
    "I found Shin-kun looking pensively at the sunset."

    show si 001 red at center with dis
    
    fn "「What are you doing? 」"
    "Hearing my voice, Shin-kun looks at me for a moment.\nLooking briefly back at the sky,\nhe speaks to me in his usual tone."
    si "「Nothing. 」"
    fn "「It's beautiful. 」"

    show si 010 red with dis
    
    si "「...Really? 」"
    fn "「Huh? 」"
    si "「I don't like this time of day.{p}\ \ Even though it's still light,\n\ \ it always seems to feel slightly lonely. 」"
    fn "「Hmm.{w=.2} I see what you mean,\n\ \ but I still don't hate it.{p}\ \ It has a quiet elegance. 」"
    fn "「Isn't it nice for two people\n\ \ to share a sunset like this?{p}\ \ It's like a scene from a drama. 」"

    show si 005 red with dis
    
    si "「Hm? 」"

    show si 009 red with dis
    
    si "「It is,{w=.2} is it... 」"
    "...Huh?"
    "I expected his usual venom,\nbut instead he looks down in silence."
    fn "「Shin-kun? 」"

    show si 001 red with dis
    
    si "「What? 」"
    fn "「What's wrong?{p}\ \ You're not looking so good. 」"
    si "「It's nothing...{w} {nw}"
    show si 009 red with dis
    extend " Just... 」"
    fn "「Just what? 」"

    show si 010 red with dis
    
    si "「... 」"
    "Shin-kun mumbles to himself."
    ta "「Hey,{w=.2} It's time to go home...! 」"
    "Just as I open my mouth,\nI hear Tatsu-nii's voice from the campsite."
    fn "「Oh, it's time to head back. 」"

    show si 001 red with dis
    
    si "「Yeah.{w=.2} You're right. 」"
    
    if shin_key1 == True:
        jump camp15_mumble2
    else:
        jump camp15_mumble1

############################################
label camp15_mumble1:

    scene black with sdis
    
    "In the end, I didn't get to hear what Shin-kun said,\nbut we had a very full two days."
    "I hope I can do something\nlike this with everybody again."

    $ route_lock = "shin"
    
    jump end15

############################################
label camp15_mumble2:

    scene white with sdis
    
    "However, I'm lonely and a little uneasy.{p}With this red light enveloping the world,\nI feel left behind, and alone."
    "...I'm not a child anymore."
    
    $ route_lock = "shin"
    
    jump end15

##################################################
label camp15_confess_kounosuke:
    
    $ event_name = "The Spoiler Tanuki"
    
    ko "「Wha~t are you doing, [fn]? 」"
    
    play sound bosu29
    show camp_site red at hshake
    
    fn "「Wah. 」"

    show ko 001 red at center with wipe_right
    
    "While I was feeling sentimental, Kounosuke suddenly{p}grabs me from behind."    
    fn "「I-{w=.2}it's nothing. 」"

    show ko 003 red with dis
    
    ko "「Really~? 」"
    fn "「Really. 」"
    "Kounosuke gets on my shoulders until I finally let them{p}down and talk."    
    fn "「It's just that I was thinking about everybody, and that{p}\ \ I only have half a month left. 」"

    show ko 001 red with dis
        
    ko "「Pshh. 」"
    fn "「Wh-{w=.2}what? 」"

    show ko 003 red with dis
    
    ko "「That's it? 」"
    "He says that with a grin, so I don't get annoyed."
    fn "「I guess I was just feeling a little sentimental. 」"

    show ko 005 red with dis
    
    ko "「Nobody would say there's anything wrong with that. 」"
    "They wouldn't say it out loud.{p}This is a bad attitude to have, right?"

    show ko 001 red with dis
    
    ko "「[fn], acting like that is just going to make{p}\ \ things dull. 」"
    fn "「Huh? 」"

    show ko 003 red with dis
    
    ko "「You went through all that trouble to come and visit\n\ \ everybody.{w} Besides, there's still plenty of your vacation left,\n\ \  isn't there?{w} And yet you're making that face. 」"
    fn "「... 」"
    "That's right.\nIn his own way, Kounosuke has been worrying about me."
    fn "「Thank you. 」"

    show ko 001 red with dis
    
    ko "「? {w=.2} What for? 」"
    fn "「What? 」"
    ko "「What were you thanking me for? 」"
    fn "「... 」"
    "Is he slow...?{p}He really can spoil things."

    show ko 005 red with dis
    
    ko "「Huh? Wait, [fn]!{p}\ \ Are you angry?{p}\ \ Wait, what did I do~? 」"
    
    hide ko with wipe_right
    
    $ route_lock = "kounosuke"
    
    jump end15

#################################################
label end15:

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
    
    jump day16
