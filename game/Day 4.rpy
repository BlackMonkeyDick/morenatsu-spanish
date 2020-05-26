##Day 4

screen kounohouse04: 
    hbox:
        add "arrow down"
        at kounobounce1
    hbox:
        add "icon_kouno"
        at kounobounce2
    hbox:
        text _("Kounosuke's House")
        xalign .76 yalign .43
screen juuichiriver04:
    hbox:
        add "arrow down"
        at riverbounce1
    hbox:
        add "icon_juu"
        at riverbounce2
    hbox: 
        text _("River")
        xalign .625 yalign .7
screen shinmarket04:
    hbox:
        add "arrow down"
        at marketbounce11
    hbox:
        add "icon_shin"
        at marketbounce21
    hbox:
        text _("Marketplace")
        xalign .515 yalign .54
        
screen shuncandy04:
    hbox:
        add "arrow down"
        at marketbounce12
    hbox:
        add "icon_shun"
        at marketbounce22
    hbox:
        text _("Candy Store")
        xalign .47 yalign .53
screen tatsukihouse04:
    hbox:
        add "arrow right"
        at tatsukibounce1
    hbox:
        add "icon_tatsu"
        at tatsukibounce2
    hbox: 
        text _("Tatsuki's House")
        xalign .85 yalign .88
        
screen date04:
    hbox:
        add "images/image/map_date.png"
        
screen minasatomap04_t():
    add "map"
    add "mapdate"
    imagebutton idle "a icon" hover "icon loop" xpos 662 ypos 391 action Jump("tatsuki04") hovered Show("tatsukihouse04")  unhovered Hide("tatsukihouse04") hover_sound "av/audio/click_008.wav"
    hbox:
        text _("{size=+30}August 4")
        at maptime
        
screen minasatomap04_r():
    add "map"
    add "mapdate"
    imagebutton idle "a icon" hover "icon loop" xpos 549 ypos 195 action Jump("kounosuke04") hovered Show("kounohouse04")  unhovered Hide("kounohouse04") hover_sound "av/audio/click_008.wav" 
    imagebutton idle "a icon" hover "icon loop" xpos 458 ypos 351 action Jump("juuichi04") hovered Show("juuichiriver04")  unhovered Hide("juuichiriver04") hover_sound "av/audio/click_008.wav"
    imagebutton idle "a icon" hover "icon loop" xpos 382 ypos 259 action Jump("shin04") hovered Show("shinmarket04")  unhovered Hide("shinmarket04") hover_sound "av/audio/click_008.wav"
    imagebutton idle "a icon" hover "icon loop" xpos 352 ypos 249 action Jump("shun04") hovered Show("shuncandy04")  unhovered Hide("shuncandy04") hover_sound "av/audio/click_008.wav"
    hbox:
        text _("{size=+30}August 4")
        at maptime
  
###########################################        
label day04:
    
    $ renpy.music.set_volume(1.0, 0.0, channel = "music")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound2")
    
    $ day = 4
    $ the_date = _("August 4")
    $ event_name = _("８月4日")
    $ focus_character = ""
    
    window hide
    play music birds_chirping
    
    scene sky01 
    show text "{size=+130}August 4" at truecenter
    with Dissolve(.5)

    pause 3
    scene black with Dissolve(1)
    pause .4
    
    scene hbroom with wipe_corner
    
    ####Remember #!#Consider making at the end of Tatsuki day02 for part time job
    #if love_tatsuki >= 1: #This seems rather odd, going to replace this with checking to see if you spent time with him on Day 2
    if part_time == True:
        jump day04_phonecall
    else:
        jump day04_regularday

############################################
label day04_phonecall:
    
    "Ah, free time...{p}When you have nothing to do, it really drags on."
    "But going out right now...{p}It would be too much of a hassle."
    "Ah! I could invite somebody over!{p}They might be bored of lying around, too."
        
    play music [ "<silence .3>",   phone_ring]
    pause 1
    scene hentry with Dissolve(.5)
    
    fn "「I'll get it!{p}{nw}"
    stop music fadeout .5
    play sound phone_pickup
    pause .3
    extend "Yes, this is [ln]. 」"
    
    ta "「Is this [fn]? 」"
    ta "「Are you enjoying Minasato so far?{p}\ \ You should come over! 」"
    "It's Tatsu-nii."
    "He sounds awfully tense,\nbut with this I can say goodbye to my boredom."
    "I'll have to go."
    fn "「Sure, I'll leave right now. 」"
    
    play music "<from 2.5>av/audio/free0422.ogg"
    call screen minasatomap04_t
   
#########################################    
label day04_regularday:
    
    stop music
    
    fn "「I wonder what I should do today? 」"
    
    play music "<from 2.5>av/audio/free0422.ogg"
    call screen minasatomap04_r
    
##########################################    
label tatsuki04:
    
    $ focus_character = "tatsuki"
    $ love_tatsuki += 1
    $ event_name = _("Drunk Dragons")
    
    scene map
    stop music fadeout 1.5
    hide screen tatsukihouse04
    play music cicada01
    scene black with wipe_dr_slow
    scene tatsuki_house_front with wipe_corner

    "Ah, it's hot...{p}I shouldn't have come out so carelessly.{p}Better hurry and get inside."
    fn "「Excuse me...! 」"
    "I tried shouting from the entryway. Since a lot of\ncraftsmen live and work inside Tatsu-nii's house\nlike a big family, the house is big and splendid."
    "Because it's so old, there isn't a bell to ring.\nI have to call in a loud voice, otherwise no one\nwould hear, and that'd be a problem."
    "While I was remembering all that,\nI could hear footsteps coming from inside."
    
    show ta 301 at center with wipeleft
    
    ta "「Oh,{w=.3} you came. 」"
    
    show ta 302 with dis
    
    ta "「Hurry up and come in,\n\ \ you gotta start sweeping up... Or something.{p}\ \ Gahahahahahahaha!!! 」"
    "Urgh,{w=.3} it smells like sake."
    fn "「Tatsu-nii, you reek of sake. 」"
    fn "「It's not even noon, and you're already drinking.\n\ \ Your face is so red. 」"
    "Tatsu-nii's face was colored red,\nand his face was slackened into a happy smile.{p}That, and he smelled like sake."
    
    show ta 301 with dis
    
    ta "「I was made to drink in weather like this.{p}\ \ Hey, come in already, or it'll all be finished. 」"
    "What are you saying..."
    
    play music free0421 fadein 1.5
    scene old_house_inside with wipe_right

    "Inside the living room, Tappei-san\nwas sitting in front of the low dining table,\nhumming a song in a good mood."
    
    show tp 406 at midright with dis

    tp "「Ooh, if it isn't [fn]! You come over here\n\ \ and have a drink, too.{p}\ \ You're old enough, right? 」"
    fn "「Tappei-san, you'll have to excuse me.{p}\ \ I'm not old enough to drink yet. 」"
    
    $ encounter_tappei = True
    
    show tp 407 with dis
    
    tp "「The hell are you on about, I was even younger\n\ \ than you when I had my first.{w} Are you saying you\n\ \ don't want my sake? Disrespecting your elders... 」"
    
    show ta 308 at midleft behind tp with wipe_right

    ta "「Pa's talks get pointlessly long,\n\ \ so I'll cut him off there. 」"
    "Phew, I'm saved."
    
    show ta 302 with dis
    
    ta "「Anyway, let's make a toast. 」"
    fn "「No, that's not... 」"
    
    show tp 406 with dis
    
    tp "「First off, beer. 」"
    
    show tp 401 at jump_up
    
    tp "「Or cold sake, shochu, brandy, wine, tequila, rum,\n\ \ vodka, gin, plum wine, shaoxing wine, or whiskey.\n\ \ Pick whichever you like. 」"
    "So many!!!{w=.3}　And so long!!!"
    
    show ta 301 with dis
    
    ta "「It's gotta be beer. I'll bring the vintage. 」"
    
    hide ta with wipe_right
    
    fn "「No, {w=.3}uh... 」"
    
    tp "「[fn], in the time I haven't seen you, you\n\ \ became a real good-looking man.{p}\ \ C'mon, sit down next to me. 」"
    
    show tp 402 with dis
    stop music fadeout 2

    tp "「I'll teach ya about so many things... 」"
    
    play music free44
    
    fn "「Ta-Tappei-san, what are you going to teach me?{p}\ \ Would you please wait???{p}\ \ And not pull me into strange situations!? 」"
    
    play sound unari00
    show ta 004 at midleft behind tp with wipe_right 

    ta "「Pa, what are you doing, you bastard?!{p}\ \ [fn]'s mine,{w=.3}{nw}"
    show ta at jump_up
    extend "hands off!!! 」"
    
    fn "「Uh, hey...{p}\ \ I feel like you two are going to rip me in half. 」"
    "Yet, I'm kinda happy they're scrambling over me..."
    
    play sound dream
    
    "I'm a terrible person."
    
    show tp 404 with dis
    
    tp "「Get lost, shorty.{p}\ \ This is grown-up time. 」"
    
    show ta at jump_up
    
    ta "「Shut it, baldy.{p}\ \ This is the age of youth. 」"
    "Aaah, what should I do...?"
    
    menu:
        "A. Party together.":
            jump tatsuki04_party
        "B. Scold them both.":
            jump tatsuki04_scold
        "C. Call for help.":
            jump tatsuki04_help

############################################            
label tatsuki04_party:
    
    $ event_name = _("Just a little bit...")
    
    show tp at jump_up

    tp "「Bastard... Defying your father!!! 」"
    
    show ta at jump_up
    
    ta "「If you're my father I'll eat my tail!!! 」"
    "This isn't getting better.{p}But how do I stop this...{p}Screw it. I've got to use my last resort!"
    fn "「Please don't angry, you two.\n\ \ Let's make a toast. 」"
    
    show tp 402 with dis
    
    tp "「Oho, so you do understand me.{p}\ \ Unlike a certain someone. 」"
    
    show ta 002 with dis
    
    ta "「So it's like that.{p}\ \ Let's do this! 」"
    
    scene black with wipeleft
    
    "Two hours later..."
    
    scene old_house_inside with wipeleft
    
    fn "「It hurts...{p}\ \ Hurk!{p}\ \ I can't...{w=.3} Drink anymore... 」"
    
    show ta 308 at midright with wipe_right
    
    ta "「What's that...? 」"
    ta "「We just started, and you're already finished. 」"
    
    show tp 407 at midleft with wipe_right 

    tp "「Oh well... Let's keep drinking at Raimon.{p}\ \ My treat, so come along. 」"
    fn "「Hurk! We're still drinking...? 」"
    
    scene black with wipeleft

    "Two hours later..."
    
    scene raimon1 with wipeleft
    
    fn "「Spin... Spin... The world is spinning... 」"
    
    show tp 407 at midleft with wipeleft
    
    tp "「So stubborn! 」"
    tp "「I said [fn] will be staying in my room!!! 」"
    
    show ta 004 at midright behind tp with wipeleft

    ta "「Why does it have to be yours? 」"
    
    show tp at jump_up
    
    tp "「Shaddup!{w} Stop bitching about what I do!! 」"
    
    show ta at jump_up
    
    ta "「You'd do absolutely anything, wouldn't you,\n\ \ old man.{w} [fn]'s mine,\n\ \ there's no way I'll hand him over! 」"
    
    show tp at jump_up
    
    tp "「What was that? I'll give you a stern talking to,\n\ \ for going against your father.{w} Come outside,\n\ \ I'll beat that temper of yours back into line. 」"
    ta "「Heh, bring it on. 」"
    ta "「I won't hold back, prepare yourself!! 」"
    
    scene raimon1 with wipe_right
    scene black with wipeleft
    stop music fadeout .8

    fn "「U-{w=.3}uuumm... 」"
    om "「Kid,{w=.3} kid,{w=.3}wake up.{p}\ \ It's closing time. 」"
    
    show raimon1 with circle_out_slow

    fn "「Hm?{w} Huh, where am I...?{p}\ \ Urgh,{w=.3} I feel sick... 」"
    om "「Kid, are you all right? 」"
    fn "「That's right, I was drinking at Raimon.{p}\ \ Huh...? Where'd those two go? 」"
    om "「Right, here's the bill. 」"
    
    play music free0531

    fn "「What!? 」"
    "I saw the amount,\nand my inebriation was blown away."
    "This bill is strange...\nIsn't that about the amount\nthat someone makes in a month?"
    
    stop music fadeout .8

    om "「Don't make that face{w=.3} it's a joke.{p}\ \ This should make Mr. Midoriya uneasy. 」"
    "This isn't a joke, I just lost years off my life.{p}It's pointless to drink sake...\nI'll meditate on this."

    jump end05

####################################
label tatsuki04_scold:
    
    $ event_name = _("With Guts!")
    $ love_tatsuki -= 1
    
    stop music 
    play sound bom26
    
    fn "「Please stop this, you two! 」"
    fn "「What are you two even saying,{p}\ \ and drinking at this hour...{p}\ \ I'm not anybody's thing! 」"
    "Hmhmhm, I forcibly told them off.{p}I can do things when I need to..."
    
    play sound bom35
    
    show ta at jump_up
    show tp at jump_up
    
    "Both" "「Shut up, you!!! 」"
    
    play music free44
    
    tp "「You'll never get anywhere,\n\ \ if you're always like that!!! 」"
    ta "「Good god you're slutty.{p}\ \ You're a man, get ahold of yourself!!! 」"
    fn "「No, the one who'd be slutty would be... 」"
    
    play sound bom35
    
    show ta  at jump_up
    show tp  at jump_up
    
    "Both" "「What was that?! You got a problem?! 」"
    fn "「No, not at all.{w} I'm so sorry. 」"
    tp "「Are you self-aware about being angry?{p}\ \ I'll say this for your sake. 」"
    
    show ta 308 with dis
    
    ta "「Seriously, that was shameful.{p}\ \ What happened to the old you? 」"
    "Why are these drunkards making me mad?{p}These two get nasty when they drink...{p}I won't drink, and won't get close when they do."
    
    play sound bom35
    
    show ta 004 at jump_up
    show tp 404 at jump_up
    
    "Both" "「You even listening? 」"
    fn "「Yes, I'm listening. 」"

    jump end04

#############################################
label tatsuki04_help:
    
    $ event_name = _("Help")
    $ love_tatsuki += 1

    stop music fadeout .8
    
    show tp 409 with dis
    
    tp "「O-kay, I got it. 」"
    
    show tp 407 with dis

    tp "「Why don't we let [fn] pick? 」"
    
    show ta at jump_up
    
    ta "「I was waiting for that.{p}\ \ [fn], who do you think is better, me or Pa?{p}\ \ Pick the one you like. 」"
    "???"
    
    play sound gun09_r
    play music free0205
    
    "Whaaat!!!{p}What the hell!!?"
    "What do I do!?"
    "If I pick one, then I lose the other!!!{p}But!!{w} 　There's a really good situation here, too."
    "This is a once-in-a-lifetime chance.{p}I can't let this go right under my nose."
    "Ok, I've decided.{w} And that..."
    
    stop music
    play sound tm2_slidedoor000
    
    who "「You guys, what are you doing with no one around?\n\ \ Doesn't that look fun. 」"
    fn "「Oh, uh, it's been a long time.\n\ \ Sorry to be a bother. 」"
    
    play music free53
    show ta 006 with dis
    
    ta "「Ma!? 」"
    "At some point, Yukino-san had appeared in the\ndoorway.{p}I wonder how much she saw?"
    
    $ encounter_yukino = True

    yukino "「Oh my, welcome.{p}\ \ After coming back all of a sudden,\n\ \ I'm sorry for these two bothering you like this. 」"
    
    show tp 401 with dis
    
    tp "「Didn't you have a village assembly to go to? 」"
    
    yukino "「I did. 」"
    yukino "「Today it seemed like Ueda-san had urgent business,\n\ \ from what I heard. 」"
    yukino "「More importantly, it looks like you've drunk a\n\ \ lot.{w} What kind of snacks do you want? 」"
    
    show tp 407 with dis
    
    tp "「Won't need any, we're going out now.{p}\ \ Bring me my clothes!! 」"
    yukino "「You're going out?{p}\ \ Even though you're in the\n\ \ middle of drinking? 」"
    tp "「Just hurry and get them.{p}\ \ They'll be in my room! 」"
    yukino "「Yes, yes, I understand.{p}\ \ I'll clean up here. 」"
    
    hide tp with wipe_right
    
    "Tappei-san is running away from his wife...{p}Can't see that in such a scary guy."
    yukino "「Geez... that man can't be helped.{p}\ \ As soon as the living room gets messy, he runs. 」"
    yukino "「I'm sorry, [fn]-kun,\n\ \ you're always welcome here.{p}\ \ Come on, don't stand there idly. See them off. 」"
    
    show ta 005 with dis

    ta "「My bad.{w} I got a bit hot under the collar there...{p}\ \ I'll treat you to a meal. 」"
    fn "「Aaawesome.{w} But no alcohol. 」"
    
    show ta 007 with dis
    
    ta "「Just food, I got it.{p}\ \ All right, let's go. 」"
    
    jump end04

########################################    
label shin04:
    
    $ event_name = _("Shin-kun's Shopping")
    $ ficus_character = "shin"
    $ love_shin += 1
    
    scene map
    hide screen shinmarket04
    scene black with dis
    
    scene market with Dissolve(.5)
    play music free53
    
    fn "「Let's see, eggs are... 」"
    "I was wandering confused while looking at a list.{p}I thought I'd be done with shopping in a flash,\nbut for some reason I was completely lost."
    "As I tried to find what I wanted,\nsoon after I lost track of where I was,{p}so now I'm trying to figure that part out."
    "I have been doing it so many times now."
    "The convenience mart and the supermarket are both\nin the same building, it shouldn't be this hard.{p}This is why the countryside..."
    "Well crap.\nI could probably get directions if I call up a friend,\nbut then cell phones don't work out here..."
    "It's awkward to get someone\nto come along just to shop too."
    "Besides, if I tell someone I got lost on a grocery run,\nI'll probably never live it down."
    "Uhh, wait eggs should have been somewhere back there.\nAfter that is konbu, soy sauce, onions, wheat flour..."
    
    play sound bosu29

    fn "「Ah-! 」"
    who "「Ah- 」"
    
    show si 009 at center with dis

    si "「Excuse me. 」"
    fn "「No, it's my fault...{w} what? 」"
    
    show si 005 with dis

    si "「[fn]? 」"
    fn "「Shin? 」"
    
    show si 001 with dis

    si "「Are you out shopping? 」"
    fn "「Well, yeah.{w} Grandma asked me. 」"
    
    scene black with dis
    
    "{cps=5}..."
    
    scene path
    show si 001 at center 
    with dis
    
    fn "「I'm really lucky you were around Shin-kun.{p}\ \ I couldn't get a bead on where anything was. 」"
    si "「You're welcome. 」"
    fn "「It really is inconvenient not being able\n\ \ to use my cell phone. 」"
    si "「Really?{w} I think I get on fine without it. 」"
    fn "「It's already become\n\ \ the most important everyday thing.\n\ \ Not being able to use it is a real pain. 」"
    
    show si 010 with dis

    si "「Hmm... 」"
    fn "「Are you out buying something? 」"
    
    show si 001 with dis
    
    si "「Does that surprise you? 」"
    fn "「Yeah.{p}\ \ Always figured you'd have\n\ \ high class stuff delivered home. 」"
    
    show si 002 with dis
    
    si "「We've got so much fresh produce nearby,\n\ \ why order in from far away? 」"
    "Has little Shin-kun taken root here?{p}As he said, Minasato is a farming village,\nso who actually would order food deliveries?"
    fn "「B-but still,\n\ \ won't you have to do it for everyone at home? 」"
    
    show si 001 with dis
    
    si "「Everything was all left to someone else back then.\n\ \ Still, I'm not a child so I want to be able to\n\ \ do some of the everyday tasks by myself. 」"

    show si 002

    si "「Besides, shopping can be pretty fun.{p}\ \ I'm looking for myself, picking something out,{w=.3}\n\ \ checking to see if what I want is within budget... 」"
    fn "「O-oh... 」"
    "That's so..."

    menu:
        "A. Like a commoner":
            jump shin04_commoner
        "B. Familial":
            jump shin04_familial

##########################################
label shin04_commoner:

    $ love_shin -= 1

    fn "「Shin-kun, you're more like a commoner than I thought. 」"

    show si 001 with dis

    si "「What do you mean by that? 」"
    fn "「I thought you'd be more detached\n\ \ from ordinary life or something. 」"
    
    show si 010 with dis

    si "「... 」"
    
    jump shin04_after

############################################
label shin04_familial:
    
    fn "「Shin-kun, you're surprisingly familial-minded. 」"
    
    show si 001 with dis

    si "「Surprisingly? 」"
    fn "「Yeah.{w} I thought you'd leave\n\ \ all the house matters to the servants. 」"
    
    show si 010 with dis

    si "「...there's only one servant in the house, you know?\n\ \ Besides, even I do housework. 」"
    
    $ shin_step1 = True
    
    jump shin04_after

############################################
label shin04_after:
    
    $ event_name = _("Imposed Image")
    
    show si 004 with dis
    
    si "「I don't know what image you have in your head,\n\ \ but I don't live a life that cut off from reality. 」"
    fn "「Ah, yeah. 」"
    "Did I make him mad?"
    
    show si 010 with dis

    si "「I hate it.{p}\ \ I hate having people put this image on me like that. 」"
    fn "「Sorry... 」"
    
    show si 009 with dis

    si "「It's fine... 」"
    "Now it kind of feels like the mood's been soured.{p}Afterwards, we exchanged words trying to keep\nthings there, but nothing really perked up."
    "The conversation was choppy as\nwe approached the parting of ways.{p}Looks like this is where Shin-kun is leaving."
    
    show si 001 with dis

    si "「See you later, [fn]. 」"
    fn "「Oh, right. Later. 」"
    
    hide si with wipe_right

    "We waved each other off,\nthen went our own separate ways.{p}Hopefully next time we meet he's in a better mood."
    
    jump end04

#############################################
label shun04:
    
    $ event_name = _("Lemonade and Marbles")
    $ focus_character = "shun"
    $ love_shun += 1
    
    scene map
    hide screen shuncandy04
    stop music fadeout 1
    scene black with wipe_dr_slow
    scene rice with dis
    play music daily01
    
    "I rustle the hem of my shirt open,\nsending a breeze directly to my bare skin."
    "The steamy air that flows in isn't very effective,\nbut it's better than nothing."
    "It's still morning, and yet the sun's starting\ndash isn't half-done."
    "Surely by afternoon some of the village's\nresidents will have melted."
    "I'm flowing with sweat.{p}In an impending water shortage,\nmy body sends out an SOS."
    "<SAVE OUR SWEATS.>"
    "I'll stop at the candy store\nand buy something to drink."
    
    scene black with dis
    scene candystoreout dis
    
    "Uugh, I'm dizzy just from walking a little bit.{p}I wonder if there's body training to endure heat..."
    "Gasping for air, I barely manage to make it\nto my destination and its proceeding visitors."
    "It's slightly cooler under the edge of the eaves,\nsince it makes shade."
    "Two people are lined up, sitting on a bench,\nand holding something in their mouths.{p}I recognize them by the shape of their ears."
    
    show so 001 at midleft
    show su 001 at midright
    with dis
    
    fn "「Heeey! 」"
    
    show su 002 with dis

    su "「Ah, [fn]-san! Good morning! 」"
    
    show so 003 with dis

    so "「Good mornin'! 」"
    fn "「Aah, morning, to both of you. 」"
    
    hide so
    hide su
    with dis
        
    "I want to greet them,{w} but I'm already\nout of strength to run up to them."
    "I stagger into the store,\nget a bottle of ramune,{p}and finally sit next to Shun-kun."
    
    show su 004 at midright
    show so 005 at midleft
    with dis
    
    su "「A-are you alright? 」"
    so "「You were staggerin' around. 」"
    fn "「Ahaha, I'm fine I'm fine.{p}\ \ It's a little too hot today... 」"
    
    show su 001
    show so 001
    with dis
    
    "It's different for them.{p}Unlike me, both of them have spent\nmany summers in Minasato."
    "This heat and humidity{p}doesn't seem to be much to them."
    "Rattle.{p}Rattlerattle.{p}Rattlerattlerattle."
    fn "「Guh, it's hard to drink. 」"
    "I was deceived by it's refreshing\nappearance and made a mistake."
    "The ramune I selected to quench my dried up body\nwas not fit for quickly supplying moisture."
    "Even though I rotate and tilt the bottle many times,\nthe marble is still an obstruction."
    
    show su 004 with dis
    
    su "「Um, [fn]-san, there's- 」"
    fn "「Wait a minute, Shun-kun.\n\ \ I need some carbonic acid. 」"
    
    show su 001 with dis
    
    su "「At the neck of the bottle there's a spot where{p}\ \ you trap it and drink. 」"
    fn "「What? 」"
    "Shun-kun garnishes his words with reservation.{p}Once again I stare at the thing in my hand."
    "Sexily decorated around the neck of the see-through\nbody, there are a few finger-sized hollow spots."
    "In other words, if it does this from the inside,\nthis must be the \"bulge\"!"
    fn "「Ooh! 」"
    "Gently tilting it, I hold back the marble\nof the root of all evil."
    "A clear, fresh stream fills the inside of my mouth.{p}My throat dances to the stimulus\nthat pierces through."
    fn "「Guh! Thanks, Shun-kun!{p}\ \ So this is how you drink ramune. 」"
    
    show so at jump_up
    
    so "「You didn't know? 」"
    "There's no implication of criticizing me for\nignorance in his eyes, pure surprise dwells in them."
    "Yeah, it's probably common sense\nfor everybody in this village."
    
    show su at jump_up
    
    su "「[fn]-san used to drink\n\ \ like that back then, too. 」"
    
    show su 002 with dis

    su "「You forgot, didn't you? 」"
    fn "「Oh, well... 」"
    "Really?{w=.3} When I was a kid,\nI probably visited this candy store frequently."
    "To get marbles at a reasonable price,\nI would often buy ramune.{w} I should have learned\nhow to drink it at some point."
    "Perhaps living in the city, in conjunction\nwith my body that won't lose to the sun,\nhas robbed my memory of the original experience."
    
    $ event_name = _("Halfsies")

    show su 001 with dis

    "Setting that aside, Shun-kun and Soutarou-kun\nare heartily gulping down their popsicles.\nThey have the same colors."
    fn "「Both of you are eating the same popsicle? 」"
    
    show so 003 
    show su tailwag 01
    with dis
    
    so "「Yep. 」"
    su "「We split it in half. 」"
    "He shows me the empty package.{p}Stuck on a stick, are long and narrow lumps of ice,\nthe two of them joined together."
    "It can be broken vertically and eaten,\na popsicle double bar.{p}It's green and seems to taste like soda."
    fn "「Even so, it's only half.\n\ \ What if you both want to eat a whole one? 」"
    "They don't have much pocket money do they?{p}I worry about that."
    "Actually, the way Shun-kun and Soutarou-kun\nare sitting next to each other\nand eating their popsicles,"
    "it really doesn't seem\nlike they'd be around the same age as me."
    "It gives me the feeling of even smaller\nlittle kids waiting for a meeting."
    "Even if the contents of their wallets\nwere 100 yen and 200 yen,\nthey don't feel out of place."
    
    show su 005 behind so with dis

    su "「It's too big for me to eat. 」"
    "Shun-kun feverishly tells me how one\nice cream is too much to eat."
    "Is it because of the smallness of his body?{p}Or maybe he's naturally weak against cold things."
    
    show su 001 with dis

    su "「So when we take it out to eat,\n\ \ I choose the small one. 」"
    fn "「What about you, Soutarou-kun? 」"
    "I try to compare their heights.\nThey're not very different."
    "However, I don't think his muscled body,\ncultivated from daily training,\nwould be daunted by something like a popsicle."
    "Maybe he went halfsies with Shun-kun\nbecause they're dating?"
    
    show so 001 with dis

    so "「I'm kinda restrictin' myself from too much\n\ \ sweet stuff right now. 」"
    "When I think about it, he gave me solid reply.{p}But for a growing exercise-enthusiast kid,\nisn't that remark too uncharacteristic?"
    fn "「Isn't soccer a sport where you run around a lot?{p}\ \ I'd think that eating a lot would be helpful. 」"
    
    show so 006 with dis

    so "「I'm goin' easy on the sweets so I'll only\n\ \ be hungry for breakfast, lunch, and dinner.{p}\ \ Having too much sugar is bad. 」"
    fn "「I see. 」"
    "I'm satisfied with each of their reasons."
    "They want to eat a popsicle, but a whole one\nis a lot, so they friendlily come\nto an agreement to split it in half."
    "It's heartwarming."
    "I remove the marble from the top of my ramune\nand check the details of the 2 popsicles\nby intermittently looking to the side."
    "B-but the wolf and lion kids next to me\nhave rod-shaped things in their mouths,\nand they're occasionally swallowing!?"
    "The theme for my research project has been\nstrongly decided!"
    "August 4th."
    
    show su 007 with dis
    
    "Shun-kun chomps little-by-little at the tip,{p}and enjoys rolling the bitten off pieces\naround in his mouth."
    "He's the type who chews and swallows."
    
    show so 003 with dis

    "For Soutarou-kun,{p}he starts on the upper half of the shaft\nand licks upwards while tasting it."
    "He's the type who gradually wears it down."
    "They softly bite down, and it changes shape\nin the tip of their muzzles."
    "Occasionally they lick up the drops oozing down.{p}Then they put their lips gently around the tips\nand rotate it so that it runs along their tongues."
    "Furthermore, both of them are taking their sweet\ntime doing it.{w} This spectacle that will inevitably\nturn dirty spreads out before my eyes."
    "Ooh, it's no use.{p}Dammit, the heat seems to have wrecked\nmy central nervous system."
    "I withdraw from the immoral direction my thoughts\nwere going."
    "However,{p}my hot bar has begun to raise its head."
    "I think I should enjoy this situation a little longer!"

    menu:
        "Get a bite of Shun-kun's":
            jump shun04_biteshun
        "Get a bite of Soutarou-kun's":
            jump shun04_bitesou

#########################################
label shun04_biteshun:
    
    $ event_name = _("A Bite from Shun-kun")
    $ love_shun += 1
    
    show so 001 with dis
    
    play music pops_003 fadein .2
    
    fn "「Shun-kun.{p}\ \ Too much cold stuff isn't good for my stomach,\n\ \ I can only eat 1 bite of a popsicle. 」"
    
    show su tailwag 01 with dis

    su "「Well then, go ahead and have some of mine♪ 」"
    "He offers it to me without hesitation.{p}Not too long, not too thick. The best size."
    "Half of it has already been chewed,\nand the surface has melted."
    fn "「Thank you!\n\ \ Alright, let's eat! 」"
    "The heat from Shun-kun's mouth was transmitted\nto the popsicle, but it has already been\nneutralized by the cold."
    "This is the rod Shun-kun has been licking\nand rolling his tongue on..."

    "[fn], bite at it from the side☆{w}{nw}"
    play sound pyoro46
    "Kapu. Porori."  

    "I bite at the lump of ice I could no longer resist,\nbut I'm too late and it loses its strength."
    "My wish that it escapes into my mouth\nalso doesn't come true,{p}and it falls off the stick and onto the ground."
    
    show so 005 with dis
    
    so "「Ah. 」"
    fn "「Ah. 」"

    show su 002 with dis
    
    su "「... 」"
    
    show su 004 with dis

    su "「Fueh. 」"
    
    show su 003 with dis
    
    su "「It fell off. 」"
    
    hide so
    hide su
    with Dissolve(1)
    
    "After that, I buy another\nof the same kind of popsicle,"
    "Remove a portion of the same length that fell,{p}and, needless to say, give it to Shun-kun."
    
    jump end04

############################################
label shun04_bitesou:
    
    $ event_name = _("A Bite from Soutarou-Kun")
    $ love_soutarou += 1
        
    play music free0551 fadein .3
    show su 001 with dis
    
    "While I'm thinking,\nShun-kun already finishes his popsicle."
    fn "「Soutarou-kun. 」"
    fn "「I've also been thinking about my body weight\n\ \ from eating too many sweets,\n\ \ so I can only have one bite of a popsicle. 」"
    "I say with wistful eyes and stare\nat both Soutarou-kun and his popsicle."
    
    show so 005 with dis

    so "「Um... 」"
    so "「Sorry, but no. 」"
    "!{w} I've been rejected!{p}But he has an apologetic look on his face!{w=.3}\nPush him further!"
    fn "「Just a little will be fine, won't it?{p}\ \ I want to taste it. 」"
    so "「No. 」"
    fn "「You don't like me? 」"
    so "「Th-that's not it, but. 」"
    "A brief silence."
    so "「...that's like an indirect {size=15}×kiss×,{size=25} isn't it? 」" 
    "He quietly mutters.{p}I make up for the part I couldn't hear\nwith the surrounding context."
    "My midsummer day brain is not to be made light of!"
    
    show su 015 with dis
    
    su "「? 」"
    "On the other hand, Shun-kun tilts his head\nin deep interest."
    su "「I couldn't hear you very well. 」"
    
    show so 006 with dis
    
    so "「Uhh, that's because... 」"
    "Then Shun-kun stares at him with pure eyes.\nFeeling bewildered,{w} Soutarou-kun's cheeks redden."
    "Shun-kun must still be at an age where he doesn't\nworry about those kinds of things."
    "My heart is healed by the shy behavior\nof a new friend,{w} and the naiveté\nof my unchanged childhood friend."
    
    show su 002 with dis
    
    su "「Ah, Soutarou-kun! 」"
    "Suddenly,\nShun-kun's expression does a complete change."
    
    show so 001 with dis

    so "「Huh? 」"
    
    show su tailwag 01 with dis
    
    su "「You're a winner! It's the winner mark! 」"
    "We look at where he's talking about.{p}The popscile Soutarou-kun is licking\nhas become thin."
    "The word \"winner\" is showing through\non the stick."
    
    show so 003 with dis
    
    so "「It is a winner! I already have one,\n\ \ so I'll give it to [fn]-sempai! 」"
    fn "「Oh... okay. Thanks, Soutarou-kun. 」"
    "Looks like he gave me the slip.{p}I'm heartbroken."
    su "「Good for you! 」"
    
    jump end04

###############################################
label juuichi04:
    
    $ focus_character = "juuichi"
    $ event_name = _("Firefly's Light, Lamplight, and the Day of a Promise.")
    $ love_juuichi += 1    
    
    scene map
    stop music fadeout 1
    play music free10
    
    hide screen juuichiriver04
    scene hbroom with dis
    
    "Smoke rises silently from the pig figurine's nose.{p}I watch it from the corner of my eye,{w=.3}\nas I flop down to go to sleep."
    "Nothing happens in the country after dinner.{p}It's completely different to the city."
    "When I'm there, I have to keep the windows shut\nbecause of the air conditioner."
    "When I found out my grandpa's house doesn't\neven have a working fan,{p}I was wrapped in a feeling of despair."
    "...When you get used to having it,{w=.3}\nthat's what happens."
    "I tried to come up with an explanation that the low\ntech surroundings somehow lessen the heat,\nwhile fanning myself."
    "The feeling of a full stomach is making me sleepy.{p}My eyelids gradually get heavier."
    
    scene black with dis
    
    "It might be rude to fall asleep after eating,{w=.3}\nBut surely a nap would be okay...?"
    
    scene hbroom with Dissolve(.1)
    $ renpy.music.set_volume(0.75, 0.0, channel = "sound2")
    play sound2 others_09 

    "Any chance of a nap is thrown out the window\nwhen loud voices start coming from the television."
    "...Come on, I'd finally managed to ignore the heat.{p}As I blearily rub my eyes,\nI glance over at the source of the noise."
    "It looks like a feature on living in the country.{p}What's on screen is fascinating.{w=.3}\nGreen lights are floating freely by a river."
    "The studio audience voices their awe at the scene.{w=.3}\nThat must have been what woke me."
    "Fireflies, huh...{p}I haven't seen one since I moved away from Minasato.{p}Even then, I barely remember seeing them."
    "Maybe I should go firefily catching while I'm here.{p}My brain quickly resumes activity as I think."
    "Let's see, where did I last see any?{p}I think I went with my grandpa,{w=.3}\nbut I can't remember clearly."
    "...Hmm,{w=.3} It's no use.{p}My memory is like an out-of-focus photograph."
    "Well,{w=.3} perhaps I should ask Grandpa where it was?\nI'll need some bug spray, too.{p}Getting covered in insect bites would be awful."
    "All right,{w=.3} I'm doing something, at least!{p}I start preparing,\nmy chest pounding with excitement."
    
    stop music fadeout 2
    scene black with Dissolve(1)
    scene river night with Dissolve(1) 
    play sound river_flow loop
    
    $ event_name = _("Lost Child Alert!")

    fn "「...This is bad. 」"
    "I scratch my cheek as I look around.{p}Getting directions from Grandpa was a good start,{w=.3}\nbut I've completely forgotten Minasato's layout."
    "As a result, I'm now lost."
    "...I think I know roughly where I am,{w=.3}\nbut it looks like I won't make it to my destination,\nno matter how hard I try."
    fn "「Aaah,{w=.3} where was it? 」"
    "My voice is swallowed up by the darkness."
    "The lights of faraway houses flicker in the distance,{w=.3}\nthe only other light coming from the moon and stars."
    "Although it looks brighter than the city,{w=.3}\nthere's still not enough light for me to\nsee where I'm putting my feet."
    "What the hell happened to the rustic scenery\nthat I see during the daytime?{p}I regret rushing this far out."
    "This calls for a trip back home,{w=.3}\nto get a map from my grandpa..."
    "That said, I feel like I shouldn't\ngo out at a time like this anyway."
    "I guess I could come back tomorrow, but...{p}I've worked up a sweat coming this far,{w=.3}\nand it'd be irritating to return without seeing them."
    "I should be in the general area,{w=.3}\nso I'll look around a little longer.{p}I check out my surroundings."
    "I can definitely see green lights dancing around.{p}...But, I came all this way to catch fireflies,{w=.3}\nso I want to find a place with many more around."

    $ event_name = _("Feels like I'm cursed")
    
    $ renpy.music.set_volume(0.7, 5.0, channel = "sound")

    "...Hm?"
    "While I was imagining places I'd rather be,{w=.3}\na light clearly different from the fireflies appears.{p}It appears and disappears in a steady rhythm."
    "While it does blink,\nit's not weak like the fireflies.{p}It's not green, either."
    "Even from this distance,\nI can distinctly tell that it's white."
    "It's moving slowly, but...{w=.3}\nIt looks like it's gradually moving towards me."
    "Summer.{w=.3} Near water.{w=.3} A place with light.{w=.3}\nNo other people around.{p}It didn't take me long to guess what it might be."

    "No way... Is this thing...{w=.3}{nw} "
    play sound2 giwaku1
    extend "A disembodied soul?{p}A cold sweat runs down my back at my guess."
    
    "Normally, I wouldn't believe in such things,{w=.3}\nBut in this situation...{p}My mind has gone against my will."
    "I suppress the urge to take off at full tilt,{w=.3}\nand decide to sit down.{p}In times like this, I need to stay calm."
    "No pushing,{w=.3} no running,{w=.3} no talking.{p}Surely the things I learned from earthquake drills\nin school will be useful."
    "...{w} Geh!{p}{nw}"
    play sound2 step13b 
    extend "As soon as I think such a leisurely thing,{w=.3}\nit came right up to me!"
    "Oh God oh God oh God oh God!{p}That was a near miss!{p}Wh-wh-what do I do!?"
    
    scene black with qdis

    "I crouch down and tightly close my eyes.{p}It seems to be true that you freeze when\nyou're truly scared."
    "Aah,{w=.3} please don't find me..."
    "...{p}...{p}..."
    "The sound of the rustling grass suddenly stops.{p}There's definitely something close by...!{p}I swallow my saliva with a loud gulp."
    "...{p}...{p}..."
    "...Nothing happened?{p}Timidly,{w=.3} I open one eye."
    
    scene river night with split_open
    pause .5

    "When I look up,{w=.3}\nI see the freshly-severed head of a bear."
    
    play music free0531
    play sound2 hit_p09
    show river night at vshake

    fn "「Gyaaah!! 」"
    "I sink back down to the ground.{p}As I lie there, trembling,{w=.3}\nthe head suddenly speaks."
    who "「...Hey,{w=.3} [ln] 」"
    fn "「N-n-n-no! 」"
    who "「[ln],{w=.3} it's me. 」"
    "Odd that it knows my name.{w=.3}\nI gingerly decide to check it again."
    "I've seen that disembodied head before.{w=.3}\nIn fact, it's a face I know very well..."
    fn "「Wh-{w=.3}what the...{w=.3} You aren't Juuichi-san, are you?{p}\ \ Please don't scare me... 」"
    
    play music daily03
    show ju 003 night at center with dis

    ju "「...That's not what I was doing.{p}\ \ I just came from over there. 」"
    fn "「Huh? 」"
    
    show ju 001 night with dis

    ju "「I could see you by the river,{w=.3} and came to warn you.{p}\ \ It's dangerous to be near the water without a light. 」"
    
    show ju 003 night with dis

    ju "「I was worried something was wrong with you,{w=.3}\n\ \ since you curled into a ball as I approached.{p}\ \ ...Screaming when I spoke your name didn't help. 」"
    fn "「... 」"
    "So it was all a complete misunderstanding?{p}The light I thought was a soul is just a flashlight?{w=.3}\nThe presence I felt so close to me was Juuichi-san?"

    play sound2 yooo
    
    "{cps=10}The soul that I saw{w=.3}\nUpon closer inspection{w=.3}\nWas just a flashlight"
    "[fn], this...{w=.3}\nThis isn't the time for haiku from the heart."
    fn "「I'm so sorry! 」"
    "I threw myself prostrate on the ground,\nand apologized to Juuichi-san."

    $ event_name = _("Bear's Shadow in a Cup")
    
    scene black with Dissolve(1)
    pause .5
    
    scene river night
    show ju 011 night at center
    with Dissolve(1)

    ju "「So,{w=.3} you thought I was a ghost? 」"
    fn "「Yeah... 」"
    "As I finish explaining why I was screaming,{w=.3}\nJuuichi-san sighs deeply."
    
    show ju 003 night with dis
    
    ju "「...I've been told my bluntness is scary,{w=.3}\n\ \ but this is the first time I've been\n\ \ mistaken for another creature entirely. 」"
    "I-I might have been mistaken,\nbut I was really scared!"
    
    show ju 001 night with dis
    
    ju "「You shouldn't be in a place\n\ \ like this without a light. 」"
    "My protesting is cut short in an instant.{p}...Yes,{w=.3} I completely agree."
    "That reminds me,{w=.3} didn't Grandpa tell me\nto take a flashlight with me?{p}I ended up leaving it behind, though."
    "Don't tell me that's what caused all this...{p}Is this what 'the future is a closed book' means?"
    
    $ event04 = renpy.random.choice(["no", "no", "no", "yes"])

    if event04 == "no":
        jump juuichi04_rideback
    
    hide ju with wipe_right
    
    $ event_name = _("A mysterious story")
    
    show ju 001 night at midright
    show na 001 night at midleft
    with wipe_right

    boy "「Juuichi is bothered by all this.{w=.3}\n\ \ Don't you think that you\n\ \ shouldn't say things like that, [fn]? 」"
    fn "「Ooh,{w=.3} I'm so ashamed of myself... 」"
    
    show ju 014 night with dis

    ju "「Wait a minute. 」"
    
    show ju 001 night with dis

    "Juuichi-san looks towards us with sharp eyes."
    
    show ju 003 night with dis

    ju "「I may have a somewhat scary face,{w=.3}\n\ \ but I don't remember saying that it bothers me. 」"
    boy "「Hm? It doesn't?{w} Just the other day,\n\ \ you crossed paths with an elementary school student.{p}\ \ You looked awfully sad as he ran away crying. 」"
    boy "「But,{w=.3} if you say I'm wrong,\n\ \ then I must be wrong, right? 」"
    
    show ju 012 night with dis

    ju "「...How did you see that? 」"
    
    show na 002 night with dis

    boy "「Hehehe,{w=.3} it's a secret. 」"
    "As he smiles,{w=.3}\nJuuichi-san has no choice but to stay silent.{p}Instead, {w=.3}{nw}"
    show ju 001 night with dis
    extend "he sighs heavily."
    
    show na 001 night with dis

    boy "「Seems like that kid had gotten lost.{p}\ \ It was bad enough that he was alone and scared,{w=.3}\n\ \ but then a scary old man started talking to him. 」"
    boy "「So,{w=.3} you've been putting up with it so far.\n\ \ But you're getting tired of it, right? 」"
    
    show ju 003 night with dis

    ju "「Old man... 」"
    "That was a mean thing to say to Juuichi-san.{p}But, from the eyes of a child,{w=.3}\nMaybe a high school student would look old?"
    ju "「[ln],{w=.3} are you going to back me up here? 」"
    
    show na 002 night with dis

    boy "「Ahaha.{p}\ \ {nw}"
    show na 001 night with dis
    extend "I have a habit of moving weirdly in the air,{w=.3}\n\ \ I can't seem to get rid of it. 」"
    "Oh,{w=.3} I don't have anything to respond with..."
    fn "「You say that, but- 」"
    
    stop music fadeout 3

    "Suddenly, I notice something.{p}Na?{w=.3}　Na... What was it?{w} Why was I even having a\nconversation with this kid in the first place?"

    show na 002 night with dis

    boy "「Looks like it's time to go. 」"
    "He smiles, softly.{p}I can't seem to look away from him.\nIt's like I'm being held in a vice."
    fn "「Na,{w=.3} na... 」"
    boy "「Welcome back,{w=.3} [fn].{p}\ \ I enjoyed talking to you. 」"
    
    scene white with qdis
    pause .3
    scene black with Dissolve(2)
    pause .5
    scene river night with Dissolve(1) 
    play music daily03
    show ju 001 night with dis

    ju "「What's wrong?{w=.3}\n\ \ You look confused. 」"
    fn "「Huh?{w=.3} Juuichi-san...? 」"
    
    show ju 011 night with dis
    
    ju "「It looked like you were talking to somebody. 」"
    fn "「No,{w=.3} I wasn't... 」"
    "A faint lump remains in my chest.{p}Why am I feeling so fuzzy?{p}I feel like I've forgotten something important..."
    
    show ju 001 night with dis

    ju "「...Huh?{w=.3}　You're a weird one.{p}\ \ Well, whatever. 」"
    
##########################################
label juuichi04_rideback:

    $ event_name = _("I Would Like a Ride Back, Please!")

    ju "「...If you sit on the grass like that for too long,\n\ \ your pants are going to be soaked with dew. 」"
    "Saying that,{w=.3} he offers me his hand.{p}I grab it, and he pulls me upright."
    fn "「...Huh? 」"
    "There's no strength in my legs.{p}Although Juuichi-san got me standing,{w=.3}\nI immediately collapse."
    
    show ju 003 night with dis

    ju "「...What,{w=.3} did your back give out? 」"
    fn "「Seems like it... 」"
    
    show ju 011 night with dis

    ju "「...You're hopless. 」"
    
    scene river night with wipe_right 

    "He turns his back to me, and crouches down."
    ju "「I'll give you a ride home.{w=.3}\n\ \ Hurry up and get on. 」"
    fn "「What?! 」"
    "I blurt out my response a bit too loudly\nat his sudden proposal."
    fn "「You don't need to do that!{p}\ \ Give me a minute and I'll be able to stand. 」"
    ju "「There's no way I'm going to\n\ \ leave you here in the dark. 」"
    fn "「Yeah, but... 」"
    ju "「Then don't just sit there and whine. 」"
    fn "「...Sorry,{w=.3} I'll do it. 」"
    "I eventually give in.{p}With a word of thanks,{w=.3}{nw}"
    play sound2 bosu34
    extend "\nI entrust my body to Juuichi-san's back."
    
    "I can feel him tensing up.{p}Without any time to think,\nI'm hoisted off the ground."
    "I hastily wrap my arms around his neck,\nso that I don't fall off."
    "His short brown fur isn't\nas bristly as I thought it would be.{p}With each step he takes, it tickles my arms a bit."
    "I can see the world from 2 metres up.{p}This must be the way Juuichi-san sees the world.{p}The scenery seems to feel fresh, for some reason."

    $ event_name = _("Summer Piggyback!")

    stop sound fadeout 3
    
    scene black with Dissolve(1)
    scene field2 night with Dissolve(1) 

    fn "「Juuichi-san,{w=.3} aren't I heavy? 」"
    "I ask him quietly, as he carries me in silence."
    ju "「The guys I usually throw around are a lot heavier.{p}\ \ ...Tora, for instance. 」"
    fn "「Hahaha... 」"
    "I let out a dry laugh.{p}Since being back, I've witnessed Torahiko\ngetting thrown more than a few times..."
    "It also feels like Torahiko knows he's going to get\nthrown, and provokes Juuichi-san into doing it."
    ju "「...I don't know why,{w=.3}\n\ \ but lately he's been particularly bad.{p}\ \ I guess he used to be more endearing. 」"
    fn "「Have you guys really changed that much?{p}\ \ As soon as you started messing around,{w=.3}\n\ \ it was like the old days again. 」"
    ju "「He used to be more timid about it,{w=.3}\n\ \ but lately he doesn't hesitate at all. 」"
    ju "「...I'm certain that Tatsu-san is\n\ \ being a bad influence on him. 」"
    "Juuichi-san sighs deeply.{p}To clear away the heavy mood,{w=.3}\nI hurriedly change the subject."
    fn "「Th-that doesn't mean that Torahiko means offense!{p}\ \ ...By the way,{w=.3} what were you doing out here\n\ \ at this hour? 」"
    "I finally ask the question that's been on my mind.{p}I didn't think anybody in the village would be\naround the riverbed at a time like this..."
    ju "「...Taking a walk. 」"
    fn "「A walk? 」"
    ju "「Yeah.{w} It's kind of a daily routine for me. 」"
    fn "「Wow,{w=.3} really? 」"
    "It feels like I just learned something.{p}I had an image in my head of him being stoic,\nand practicing judo in his spare time."
    ju "「What were you doing out there, anyway?{p}\ \ What lead to you mistaking me for something else? 」"
    fn "「Didn't I tell you?{p}\ \ I was planning on catching fireflies. 」"
    ju "「Catching fireflies?{p}\ \ That's quite tasteful of you. 」"
    "He talked with a slightly gentler tone of voice."
    ju "「...If you're looking for fireflies, though,\n\ \ I think you should go farther upstream. 」"
    fn "「Huh,{w=.3} that's weird.{p}\ \ Grandpa said they'd be around here. 」"
    "I explain the place Grandpa told me about.{p}Then, Juuichi-san sighs softly."
    ju "「...I knew it. You can't remember the area, can you?{p}\ \ Even though your grandfather\n\ \ told you where to find them? 」"
    fn "「...No comment. 」"
    "Just when I feel like I'm starting to remember,{w=.3}\nI'm reminded by the fact that I don't."
    ju "「If you go there now, you'll be up too late.{p}\ \ Your body's not up to it, either.{w=.3}\n\ \ You should stop for today. 」"
    "The whole cause of this was that I didn't prepare,\nand rushed out as quickly as I could.{p}Well, that and being strangely stubborn."
    "I quietly reflected on Juuichi-san told me."
    "Besides,{w=.3} I feel a little embarrassed for\nsaying where I want to go,\ndespite not having a pair of working legs."
    "It's the same as getting on Juuichi-san's back,{w=.3}\nand telling him where to go."
    "I'm sure if I did that,{w=.3}\nhe'd bring the hammer down on me."
    "...I remember what happened to Torahiko,{w=.3}\nand involuntarily shudder."
    ju "「Hm?{w=.3} Are you cold? 」"
    fn "「Oh,{w=.3} no,{w=.3} I'm fine.{p}\ \ Your body is warm. 」"
    ju "「... 」"
    "Juuichi-san falls silent.{p}Huh?{w=.3} I didn't say anything particularly weird...{p}Did I?"
    "Thanks to their fur,{w=.3}\nbeastmen trap heat better than humans."
    "In fact,{w=.3} Juuichi-san's body temperature is gradually\nbeing transferred to me through his back."
    "Still,{w=.3} it doesn't feel strange or uncomfortable.{p}Actually,{w=.3} it makes me feel a\nvaguely familiar sense of relief."
    "Under our combined weight,\nthe gravel makes a loud crunching sound."
    "There aren't many paved roads in Minasato,{w=.3}\nso crunching gravel is not an unusual sound."
    
    $ renpy.music.set_volume(0.5, 5.0, channel = "music")

    "The sound is rhythmic.\nI'm being rocked up and down.\nWarmth is coming off Juuichi-san's body."
    "...{p}...{p}...Zzz..."
    
    $ renpy.music.set_volume(0.85, 0.0, channel = "music")

    "Whoa,{w=.3} I dozed off there for a second.{p}I quickly pull back my face that had been buried in\nthe back of Juuichi-san's neck."
    "Now that I think about it,\nI was falling asleep before I left the house."
    "Walking around in an unfamiliar place\nat night probably didn't help,\nso it's not surprising that I dozed off like that."
    "That said,{w=.3}\nit'd be rude to Juuichi-san if I fell asleep."
    "Oh, did he notice me starting to doze off?{w=.3}\nHe turns his head and talks to me."
    ju "「You seem sleepy. 」"
    fn "「I-{w=.3}I'm not going to sleep! Not yet... 」"
    ju "「...That's basically admitting you're sleepy.{p}\ \ I'll wake you up when we reach your house.{w=.3}\n\ \ Rest until then. 」"
    fn "「But,{w=.3} that's... 」"
    ju "「Don't worry.{p}\ \ I'm doing this because I want to. 」"
    fn "「Ah,{w=.3} I need to tell you how to get to my house... 」"
    ju "「I've lived here for a long time.{p}\ \ ...There's no reason for me to have forgotten. 」"
    fn "「...Sorry.{w=.3}\n\ \ I guess I'll sleep for a bit. 」"
    "During this short exchange,{w=.3}\ndrowsiness attacks me without mercy."
    "I rest my head against the back of his neck,{w=.3}\nand close my eyes."
    
    scene black with split_close_slow
    pause .5

    "Juuichi-san's back is so soft and warm...{p}Wrapped up in warmth and happiness,{w=.3}\nI drift off to sleep."
    
    stop music fadeout 1.5
    scene black with dis
    pause 2    
    scene rice night with dis
    play music free60

    ju "「...[ln]. 」"
    fn "「...Nnah? 」"
    ju "「Are you still tired from the trip back to Minasato?{p}\ \ You were pretty fast asleep. 」"
    "His words snap me out of my half-asleep state."
    "Looking around in confusion,{w=.3}\nI recognize the familiar surroundings.{p}Grandpa's house is right in front of us."
    fn "「...How long was I out? 」"
    ju "「About 30 minutes, give or take. 」"
    "...Wow.{w} I'd meant to sleep for\n5 minutes to clear my head.{p}I didn't mean to sleep that long."
    "My thick-headedness is formidable.{p}So is Juuichi-san's soft fur, however..."
    fn "「Oh, I'll be fine from here. You can put me down!{p}\ \ You've been carrying me for so long... 」"
    ju "「This really isn't a big deal for me.{p}\ \ Are you sure about me putting you down already? 」"
    fn "「I can feel my legs again, mostly.{p}\ \ I'll probably be fine! 」"
    "Juuichi-san crouches down,\nwithout wobbling in the slightest.{p}He's as stable as ever."
    "Lowering my feet to the ground,{w=.3}\nI gingerly get off him."
    "Hm... There don't seem to be any problems.{p}I lightly stretch, and twist around to test my back."
    
    show ju 001 night at center with dis

    ju "「Hm,{w=.3} seems that there's nothing to worry about. 」"
    "Seeing that I can move my body properly,{w=.3}\nJuuichi-san gives a nod of approval."
    fn "「Juuichi-san,{w=.3} thank you so much for everything. 」"
    
    show ju 008 night with dis
    
    ju "「Ah,{w=.3} no problem. 」"
    "As usual,{w=.3} his response is only a few words.{p}I feel like I could never compete with him.{p}...Well,{w=.3} not in judo, at least."
    "Even so,{w=.3} next time I go out to catch fireflies,{w=.3}\nI'll make sure to ask Grandpa for a map.{p}I never thought I'd forget something like that."

    show ju 001 night with dis
    
    ju "「...So,{w=.3} can I go with you tomorrow? 」"
    fn "「Huh? 」"
    "I tried to stop myself,{w=.3}\nBut I blurted my surprise out loud anyway.{p}...I'm doing nothing but embarrassing myself today."

    show ju 003 night with dis

    ju "「I'm worried about letting you\n\ \ walk around alone at night. 」"
    "...That's right,{w=.3} I've been a huge pain today.{p}Going along with Juuichi-san seems like a good idea."
    "At the very least,{w=.3}\nit'd be much more enjoyable than going alone."
    fn "「...Would you, if it's not too much trouble? 」"
    
    show ju 002 night with dis

    ju "「Sure. 」"
    "Unfortunately, today didn't go so well.{w=.3}\nBut, in the end, things worked out all right?"
    "It might be a little sudden,{w=.3} but I'll prepare\nright away for our trip tomorrow.\nIt's the least I can do."
    "...It's not like I have anything\nelse to do with my free time."
    
    show ju 001 night with dis
    
    ju "「Make sure you dress appropriately tomorrow. 」"
    fn "「I will. 」"
    "Umm...{w=.3} A flashlight, compass, something to drink.{p}I'll be able to last for a day if anything happens!{p}...Well, that won't happen if Juuichi-san's with me."
    "Ah, what about nets and containers?{p}Keeping fireflies as pets seems difficult..."
    "I'll have a look around the shed tomorrow,{w=.3}\nand see if I can find anything useful."
    ju "「Well then,{w=.3} see you tomorrow. 」"
    
    play sound step13b
    hide ju with dis

    "With a wave of his hand,{w=.3}\nhe turns and starts walking\nin the direction of his house."

    "Catching fireflies with Juuichi-san...{w=.3}\nI'm looking forward to it."

    $ juuichi_fireflies01 = True

    jump end04

######################################
label kounosuke04:
    
    $ love_kounosuke += 1
    $ focus_character = "kounosuke"
    $ event_name = _("Reunion with Yukiharu")
    
    scene map      
    hide screen kounohouse04
    scene kouno_house_out with dis
    
    play music cicada01 fadein 5
    $ renpy.music.set_volume(0.6, 0.0, channel = "music")
    
    fn "「It's still the same... 」"
    "The memories I'm following are fuzzy, {p}but the scenery I remember hasn't changed. {p}I mutter this to myself."
    "The building seems to be a little worn. {p}This store also hasn't changed."
    
    play sound tm2_slidedoor000
    scene kouno_house_in with Dissolve(.2)
    
    fn "「Oh, hello. 」"
    who "「Yes? 」"
    "The store smells a little dusty and old."
    
    $ renpy.music.set_volume(0.0, 3.0, channel = "music")
    
    "When I call into the store, no one is there. {p}Then, a tanuki pops out. {p}He looks like a mini-Kounosuke."
    
    play music free51
    $ renpy.music.set_volume(0.8, 0.0, channel = "music")
    $ encounter_yukiharu = True    
    show yk 001 at center with dis
    
    yk "「Sorry, dad's out right now.{p}\ \ Is there something you need? 」"
    fn "「Ah. I came to see Kounosuke.{p}\ \ Is he here right now? 」"
    yk "「Big brother? {p}\ \ He went somewhere... 」"
    
    hide yk with wipe_right
    
    yk "「Mom! Do you know where Kounosuke went? 」"
    
    $ encounter_harue = True
    
    harue "「Well now, I was wondering that myself. 」"
    yk  "「Looks like one of his friends is here. 」"
    harue "「Maybe he didn't leave? 」"
    yk "「So you don't know where he is? 」"
    harue "「Hmm, I'm still not so sure... 」"
    "...... {p}When Yukiharu-kun goes back into the store.{p}I can hear his exchange with an older woman."
    
    show yk 003 at center with dis
    
    yk "「Sorry. Hmm, where did he go... {p}\ \ I think he's probably somewhere in town. 」"
    fn "「Oh well. That's okay I guess. {p}\ \ I didn't come here for anything business related.{p}\ \ Just wanted to see if he was around. 」"
    yk "「Really? 」"
    fn "「By the way, you're Yukiharu-kun, aren't you? {p}\ \ You've gotten bigger! 」"
    
    show yk 001 with dis
    
    yk "「Huh? 」"
    yk "「Umm, who are you? 」"
    "Guh, he doesn't remember me..."
    fn "「Hey, it's me. {p}\ \ I transferred to another school 5 years ago. {p}\ \ [fn]-onii-chan. Remember? 」"
    
    show yk 003 with dis
    
    yk "「...... 」"
    "For a while, Yukiharu stares at me, puzzled."
    
    show yk 002 with dis
    
    yk "「Uh, ah... were you the one who...{p}\ \ always got into trouble with my brother? 」"
    "Oh..."
    "It seems like he remembers one thing, {p}but then I would get dragged along with Kounosuke. {p}I didn't have anything to do with it."
    "Well, there's no use in testifying."
    fn "「Y-yeah... that [fn]-onii-chan. 」"
    yk "「I kind of remember.{p}\ \ Why are you back in Minasato? 」"
    fn "「I'm just here for Summer vacation. 」"
    
    show yk 001 with dis
    
    yk "「Oh, that's it, then. {p}\ \ Well then, I need to get back there. 」"
    
    play sound tm2_slidedoor000
    
    ko "「I'm back! 」"
    "While talking to Yukiharu-kun, {p}Kounosuke seems to have come back."
    "When I turn around, {p}it's just one innocent tanuki face."
    
    show yk 002 with dis
    show ko 001 at offleft
    
    yk "「Ah, you're back. 」"
    fn "「Welcome home. 」"
    
    show yk at move_midright(0.5)
    show ko at move_midleft(0.5)
    
    ko "「Oh, what's wrong [fn]? {p}\ \ Is there something you need? 」"
    fn "「No, I just came to drop in and visit. 」"
    
    show ko 003 with dis
    
    ko "「Ah, is that so. 」"
    
    show yk 003 with dis
    
    yk "「Hey, onii-chan! {p}\ \ I'm not the only one who has to watch the store! 」"
    
    show ko 006 with dis
    
    ko "「What! {p}\ \ I wouldn't make you do something like that. 」"
    yk "「But you just went out somewhere! 」"
    
    show ko 002 with dis
    
    ko "「But dad didn't catch me leaving, did he? 」"    
    yk "「I wanted to go out and play too! {p}\ \ But I promised I wouldn't! 」"
    fn "「C-come on now. Calm down you two... 」"
    "A fight between brothers suddenly breaks out, {p}so I rush in and try to calm things down."
    
    show ko 001 with dis
    
    ko "「Eh? But what needs calming down? 」"
    
    show yk 001 with dis
    
    yk "「What's wrong? 」"
    "They look at me as if nothing happened, {p}I'm at a loss for words. {p}Is this what it's normally like for siblings?"
    harue "「Yuki-chan, Kou-chan! {p}\ \ The noodles have boiled. {p}\ \ Come and eat! 」"
    
    show ko 003 
    show yk 002
    with dis
    
    brothers "「Coming! 」"
    
    show yk at move_offright(0.5)
    show ko at move_center(0.5)
    
    ko "「[fn], you should eat with us! 」"
    fn "「Ah, okay. Is that alright? 」"
    
    show ko 002 with dis
    
    ko "「Of course, of course. 」"
    fn "「Then without further ado, {p}\ \ I'll take your offer! 」"
    
    hide ko with wipe_right
    
    harue "「Oh, that's right! {p}\ \ Kounosuke, you're watching the store this afternoon. 」"
    
    show ko 006 at center with wipe_right
    
    ko "「Whaaa!? 」"
    harue "「Yuki-chan wants to play with his friends. {p}\ \ I told him he could, and besides, {p}\ \ I'm a mother, I like to keep things even. 」"
    
    show ko 005 with dis
    
    ko "「That's... 」"
    harue "「Now, now. You're the older brother. 」"
    
    show ko 007 with dis
    
    ko "「Ooh... 」"
    "Kounosuke complains and glances to the side, {p}while slurping his noodles. {p}Suddenly, his eyes meet mine."
    
    play sound freeze04
    show ko 001 big at center_big with explosion    
    pause .2
    
    "At that moment, a light dwells in his eyes. {p}A restless light, I can't miss it."    
    
    stop music fadeout 3
    
    show ko 002 big with explosion
    
    ko "「[fn]...{p}\ \ Can I... discuss something with you...? 」"
    "......"
    
    scene black with sdis
    
    "And for some reason, {p}I helped Kounosuke out all afternoon.{p}I was a salesperson."
    "I'm not sure why I did this, {p}but it went on and on until sundown..."
    
    scene kouno_house_out red with sdis 
    play sound kara00
    pause 1
    play sound kara00
    pause 1

    #[eval exp="f.kounosuke_m2_flag=true"] #!# Guessing this is just a flag that shows you met Yukiharu

##############################################    
label end04:
    
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
    
    jump day05

    
    
    
    
    
    

