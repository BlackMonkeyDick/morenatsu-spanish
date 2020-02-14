## Day 10

screen marketplace10:
    hbox:
        add "arrow down"
        at marketbounce1
    hbox:
        add "icon_shun"
        at marketbounce2
    hbox:
        text "Market"
        xalign .5 yalign .52
screen busstop10:
    hbox:
        add "arrow down"
        at busbounce1
    hbox:
        add "icon_juu"
        at busbounce2
    hbox:
        text "Bus Stop"
        xalign .8 yalign .38
screen forest10:
    hbox:
        add "arrow down"
        at forestbounce1
    hbox:
        add "icon_kouno"
        at forestbounce2
    hbox:
        text "Forest"
        xalign .61 yalign .87
screen tatsukihouse10:
    hbox:
        add "arrow right"
        at tatsukibounce1
    hbox:
        add "icon_tatsu"
        at tatsukibounce2
    hbox: 
        text "Tatsuki's House"
        xalign .85 yalign .88

screen minasatomap10a():
    add "map"
    add "mapdate"
    imagebutton idle "a icon" hover "icon loop"  xpos 372 ypos 249  action Jump("shun10") hovered Show("marketplace10")  unhovered Hide("marketplace10") hover_sound "av/audio/click_008.wav"
    imagebutton idle "a icon" hover "icon loop"  xpos 453 ypos 447  action Jump("kounosuke10") hovered Show("forest10")  unhovered Hide("forest10") hover_sound "av/audio/click_008.wav"
    hbox:
        text "{size=+30}August 10"
        at maptime
        
screen minasatomap10b():
    add "map"
    add "mapdate"
    imagebutton idle "a icon" hover "icon loop"  xpos 372 ypos 249  action Jump("shun10") hovered Show("marketplace10")  unhovered Hide("marketplace10") hover_sound "av/audio/click_008.wav"
    imagebutton idle "a icon" hover "icon loop" xpos 583 ypos 165 action Jump("juuichi10") hovered Show("busstop10")  unhovered Hide("busstop10") hover_sound "av/audio/click_008.wav"
    imagebutton idle "a icon" hover "icon loop"  xpos 453 ypos 447  action Jump("kounosuke10") hovered Show("forest10")  unhovered Hide("forest10") hover_sound "av/audio/click_008.wav"
    hbox:
        text "{size=+30}August 10"
        at maptime
        
screen minasatomap10c():
    add "map"
    add "mapdate"
    imagebutton idle "a icon" hover "icon loop"  xpos 372 ypos 249  action Jump("shun10") hovered Show("marketplace10")  unhovered Hide("marketplace10") hover_sound "av/audio/click_008.wav"
    imagebutton idle "a icon" hover "icon loop"  xpos 453 ypos 447  action Jump("kounosuke10") hovered Show("forest10")  unhovered Hide("forest10") hover_sound "av/audio/click_008.wav"
    imagebutton idle "a icon" hover "icon loop"  xpos 662 ypos 391  action Jump("tatsuki10") hovered Show("tatsukihouse10")  unhovered Hide("tatsukihouse10") hover_sound "av/audio/click_008.wav"
    hbox:
        text "{size=+30}August 10"
        at maptime
        
screen minasatomap10d():
    add "map"
    add "mapdate"
    imagebutton idle "a icon" hover "icon loop"  xpos 372 ypos 249  action Jump("shun10") hovered Show("marketplace10")  unhovered Hide("marketplace10") hover_sound "av/audio/click_008.wav"
    imagebutton idle "a icon" hover "icon loop" xpos 583 ypos 165 action Jump("juuichi10") hovered Show("busstop10")  unhovered Hide("busstop10") hover_sound "av/audio/click_008.wav"
    imagebutton idle "a icon" hover "icon loop"  xpos 453 ypos 447  action Jump("kounosuke10") hovered Show("forest10")  unhovered Hide("forest10") hover_sound "av/audio/click_008.wav"
    imagebutton idle "a icon" hover "icon loop"  xpos 662 ypos 391  action Jump("tatsuki10") hovered Show("tatsukihouse10")  unhovered Hide("tatsukihouse10") hover_sound "av/audio/click_008.wav"
    hbox:
        text "{size=+30}August 10"
        at maptime
        
##########################################
label day10:
    
    $ renpy.music.set_volume(1.0, 0.0, channel = "music")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound2")
    
    $ day = 10
    $ event_name = "８月10日"
    $ the_date = "August 10"
    $ focus_character = ""
    
    window hide
    play music birds_chirping
    
    scene sky01 
    show text "{size=+130}August 10" at truecenter
    with Dissolve(.5)

    pause 3
    scene black with Dissolve(1)
    pause .4
    
    scene hbroom with wipe_corner

    fn "「I wonder what I should do today. 」"
    
    play music "<from 2.5>av/audio/free0422.ogg"
    
    if part_time == True:
        if borrow_jacket == True and love_shun >= 3:
            call screen minasatomap10d
        else:
            call screen minasatomap10c
    elif borrow_jacket == True and love_shun >= 3:
        call screen minasatomap10b
    else:
        call screen minasatomap10a
    
    
##############################################    
label kounosuke10:
    
    $ event_name = "Tanuki in the forest"
    $ love_kounosuke += 1
    $ focus_character = "kounosuke"

    scene map
    hide screen forest10
    play music free53 fadein 1
    scene forest01 with sdis
    
    "In the forest, {p}Dazzling sunlight spills through the trees."
    "It's better than being in a sunny spot, {p}but it's still unbearably hot and humid."
    fn "「Ah, damn...! 」"
    "I was bitten by a mosquito, {p}on the back of my neck. {p}Damn, when did it get me!?"
    "Don't suck my blood! {p}I'm going to start a genocide! Aah!! {p}...Oops. The heat made me break character."
    "When I was little and it was this hot, {p}I'd run around the forest, river, and village. {p}I was an energetic kid."
    "Oh? Huh? {p}Is that Kounosuke over there?"
    
    show ko 001 at center with dis

    "What is he doing? {p}He's holding his prized camera, {p}that always hangs from his neck."
    "It looks like he's trying to take a picture."
    fn "「Heeey, Kounosuke! 」"
    "{cps=100}...... {w=.5}{p}{cps=40}No reply. Did he not hear me? {p}If that's the case..."
    fn "「Yo. What are you doing, Kounosuke? 」"
    
    ko "「UWAAAAA!? 」{nw}"    
    show ko 006 at hop_off
    extend "{w=1.25}{nw}"
    play sound bosu34
    show forest01 at vshake    
    extend ""
    hide ko
    show ko 005 at bottomleft
    
    "Wh, what? {p}I just suddenly put my face... {p}in front of his camera."
    "He's surprised that I'm here...?"
    
    show ko at move_center(2)

    ko "「O-oww... 」"
    fn "「A-are you okay? 」"
    ko "「Darn it! You're terrible, [fn]!! 」"
    fn "「S-sorry. I didn't think you'd be that surprised. 」"
    
    show ko 001 with dis
    ko "「Jeez......{w=1}{nw}"
    show ko 006 with qdis
    extend " ah! 」"

    "Quickly brushing off the grass and dirt, {p}Kounosuke seems to be in a panic, {p}and climbs back up the slope he fell off of."
    "He returns to his original position, {p}and when he sets his camera up, {p}he lets out a voice of disappointment."
    
    show ko 007 with dis
    
    ko "「Aaaww... 」"
    fn "「What were you taking a picture of? 」"
    
    show ko 005 with dis
    
    ko "「Birds. {p}\ \ But they've completely escaped now... 」"
    fn "「S-sorry... 」"
    "He gives me a bitter sidelong glance. {p}At once, I make a fake smile, {p}and turn my head to hide."
    fn "「W-why are you taking pictures of birds? 」"
    
    show ko 001 with dis
    
    ko "「Why, you ask? 」"
    
    show ko 005 with dis
    
    ko "「...You won't tell anybody? 」"
    fn "「Sure, I won't. 」"
    ko "「Absolutely? 」"
    fn "「Yeah. 」"

    show ko 001 with dis
    
    ko "「Well then, I'll just tell you, {p}\ \ but you absolutely won't tell anybody else? 」"
    "After stressing \"absolutely\" many times, {p}he reaches into his favorite bag, {p}and shows me a single copy of a magazine."
    "What, \"Monthly {w=.3}Elegance\"? {p}Flipping through it, {p}there's only photographs and poems."
    "Nothing in there that interests me."
    "Isn't this aimed at adults or old men? {p}It's like an arts and literature magazine."
    "Kounosuke likes to read this... {p}When it comes to magazines, {p}I only read comics myself."
    "I feel a slight sense of inferiority."
    fn "「W-wow, you like reading this? 」"
    "Even though my voice wavers, {p}I make an effort to ask calmly."
    ko "「What? Not particularly. {p}\ \ I just happened to pick it up recently 」"
    "Oh, is that so..."
    
    show ko 005 with dis
    
    ko "「The magazine isn't the problem here.\n\ \ It's this article. 」"
    "Kounosuke points to where he's talking about, {p}the section for recruiting reader contributions."
    
    scene black with dis
    
    $ renpy.music.set_volume(0.6, 0.0, channel = "music")
    
    "{i}~Mass Recruitment for Reader Contributions~{p}This month's theme is \"Nostalgic Scenery\". {p}A photo accompanied by a short article for this."
    "{i}Not only will the winner be used in this magazine, {p}the wonderful, sparkling grand prize, {p}is a monetary award of 100 million yen."
    "And the latest digital camera as a present."
    
    scene forest01 with sdis
    $ renpy.music.set_volume(0.7, 0.0, channel = "music")
    show ko 005 with dis
    
    "Looking closely, there's a small, {p}simplification on the cover of the magazine."
    fn "「Is this it? 」"
    
    show ko 001 with dis
    
    ko "「Yep, that's it. 」"
    fn "「Have you thought about applying? 」"
    
    show ko 002 at jump_up
    
    ko "「Of course! 」"
    
    show ko 004 with dis
    
    ko "「I'm saving money for the city, {p}\ \ but it's not easy to gather. {p}\ \ However, if I get this grand prize... 」"
    
    show ko 002 with dis
    
    ko "「I can use that money for my dream, {p}\ \ of becoming a city dweller."
    ko "And getting that digital camera? {p}I could cut out the cost for film! {p}That's why. 」"
    fn "「Oh, I see... 」"
    "I didn't think it was as simple as that. {p}First of all, in Japanese class, {p}I remember Kounosuke getting bad scores ."
    "It's normal for him to have such a silly idea. {p}Yep."
    "The fact that he doesn't subscribe to this magazine, {p}gives me a feeling of relief, {p}and a slight sense of superiority!"
    
    if kouno_magazine == True:
        jump kounosuke10_lastweek
    else:
        jump kounosuke10_busy

    ########################################
    label kounosuke10_lastweek:

        fn "「That reminds me, {p}\ \ did you happen to buy this magazine last week? 」"

        show ko 001 with dis
    
        ko "「Eh? Yeah, but... {p}\ \ how did you know that? 」"
        fn "「I was also in the bookstore then. 」"
        ko "「What? You were? 」"
        fn "「I was. I tried talking to you, {p}\ \ but you finished too quickly with the cashier, {p}\ \ and you left before I could talk to you. 」"

        show ko 005 with dis
     
        ko "「Eh? Hmm... {p}\ \ Now that you mention it. {p}\ \ There was somebody different. 」"
        "Just as I thought, {p}he didn't see me."
        fn "「Don't you think you should correct that habit? 」"

        show ko 002 with dis
    
        ko "「That's the result of concentration! 」"
        "Should I be shocked or should I admire him? {p}When he seriously says that, {p}I place my hand on my forehead."
        "I also give a slightly exaggerated sigh."
        fn "「Haah. Hmm... 」"

        show ko 001 with dis
    
        ko "「Did you buy something? 」"
        fn "「I uhh... {p}\ \ Th-they didn't have the magazine I came for, {p}\ \ so I just randomly browsed around. 」"
        "Wh-whew. {p}I almost blurted out that bought... {p}porn in broad daylight."

        show ko 005 with dis
    
        ko "「Hmm? 」"

        show ko 002 with dis
    
        ko "「Were you looking for porn, {p}\ \ in the middle of the day? 」{w} {nw}"
        show forest01 at vshake
        play sound hit_p07
        extend "{w=.1}{nw}"
        
        "Guh!{nw}"
        show forest01 at hshake
        extend ""
        
    
        fn "「{cps=100}N-no.\n\ \ I'm not even old enough to do that! 」"
        ko "「You have a point. 」"
        "Hahaha, both of us laugh. {p}Kounosuke is unexpectedly sharp."
    
    #########################################
    label kounosuke10_busy:

        show ko 001 with dis
    
        ko "「Well, that's why I'm doing it, {p}\ \ I'll first have to find scenery, {p}\ \ worthy of the prize."
        ko "I'm too busy, though. {p}Maybe some other time. 」"
        
        hide ko with wipe_right
    
        fn "「Oh, okay. Also... 」"
        "He waves his hand and says goodbye to me. {p}Without waiting for my reply, he leaves. {p}He's so energetic..."
    
        $ kouno_busy = True
        
        jump end10

##############################################        
label shun10:

    $ love_shun += 1
    $ event_name = "Square button"
    $ focus_character = "shun"

    scene map
    hide screen marketplace10    
    stop music fadeout 1
    scene black with wipe_dr
    pause .3
    scene market with dis
    play music tam_n06
    $ renpy.music.set_volume(0.8, 0.1, channel = "music")

    "The shopping district in early afternoon. {p}Completely different from the bustle of the\nevening, it's a modest, yet comfortable scene."
    "The signs on the timeworn street lamps, the closed\nshutters, the sound of music leaking out from\na cafe to the street, and the smell of cooking oil."
    "I am welcomed by the town I had almost forgotten."
    "When I look up, the wooden telephone poles\nare linked with unreliable looking wires."
    "I'm surprised at how I've just come back\nand I'm already familiar with,{p}or rather adapted to, the old scenery."
    "A black unmanned payphone, roofs thatched\nwith grass. At first each thing surprised me,{p}but now nothing does."
    fn "「...ah 」"
    
    stop music fadeout .25
    play music codekdr
    $ renpy.music.set_volume(0.8, 0.1, channel = "music")
    
    "...a world of dots is reflected in an old-style TV.{p}A red and white machine connected to video terminal\nsends in the hero of an action game to the screen."
    "Minasato's game store still uses old generation\nhome-use video games,{w} and supplies the source\nof blips and bloops to the shopping district."
    "Sorry, I was surprised."
    
    menu:
        "A. But it is very nostalgic":
            jump shun10_nostalgia
        "B. I haven't been playing video games recently":
            jump shun10_play

    #########################################
    label shun10_nostalgia:

        "Wow... {p}The glow of the TV screen is strangely real."
        "The world consisting of dots and electronic sounds\nwas more fascinating than anything else when\nI was a kid.{w} I was certainly inside the game."
        "...who taught me that? {p}The one who showed me realize the appeal\nof video games and my first game?"
        who "「[fn]-san. 」"
        "That's right,{w} back then my first glimpse\nof that red and white machine connected\nto the TV wasn't at my house..."
        
        show su 005 at center with wipe_down
    
        su "「[fn]-san! 」"
        fn "「Waah!? 」"
        "There's Shun-kun with cheeks puffed out in anger.{p}D-don't call out to me so suddenly!{w=.3}\nI'm not surprised!"
        
        stop music fadeout .25
        pause .3
        play music pops_003
        
        show su 010 with dis
    
        su "「Ooh, I've been calling out to you for a while {p}\ \ but you weren't noticing me. 」"
        fn "「S-sorry, sorry. 」"
    
        show su 015 with dis
    
        su "「What are you thinking so deeply about? 」"
        fn "「Oh, uum, I was just remembering some old stuff. 」"
        
        show su 001 with dis
        
        su "「? 」"
        fn "「Look at this game console. {p}\ \ Since my life began, it hasn't changed\n\ \ It's nostalgic. 」"
        
        show su 004 with dis
        
        su "「Y-you're right.{p}\ \ Even though new consoles are sold inside... 」"
        su "「Only this old square button\n\ \ has been here for a long time. 」"
        fn "「Because of that, I was thinking\n\ \ about the first video game I played. 」"
        
        show su 002 at jump_up
        
        su "「Wah, that was at my house, wasn't it?{p}\ \ That brings back memories♪ 」"
        fn "「Yeah, back then I could\n\ \ only play games at your house. 」"
        su "「[fn]-san, you came\n\ \ to my house a lot, didn't you? 」"
        fn "「Hehe, I did. Shun-kun,\n\ \ you've always loved video games since then. 」"
        su "「That's right♪{w=.3}\n\ \ And I'm buying a new game today... 」"
        
        jump shun10_newgame

    ########################################        
    label shun10_play:

        "Recently, or maybe I should say, it's been\na great deal of time since I last did. {p}Occasionally I'd play a monster collecting game."
        "I dutifully carried around a huge\nand heavy portable game console."
        "I'd peer into the black and white screen,\nthrow balls, feed them, send them back\nand forth through cyberspace,"
        "...Huh? I mixed something up."
        "The differences before and after they evolved\nterrified me, so I stopped playing."
        "I thought that since they were tiny,\nthey would stay that way."
        
        play sound tm2_slidedoor000
        
        fn "「Ah. 」"
        
        show su 002 at center with dis
        
        su "「Hanyaa, [fn]-san!{w=.3} Yaay. 」"
        "{cps=20}Ah!{w=.3} A SHUN-KUN\nappeared from the game store!"
        
        play sound metalhit001
    
        fn "「I'm gonna catch yooooooouuuuuu!! 」"
        
        show su 003 with qdis
    
        su "「Wanyaaaaaaaaaaaaaaaa!! 」"
        
        stop music fadeout .25
        scene black with Dissolve(1)
        pause .1
        
        scene market
        show su 005 at center 
        with dis
        play music pops_003
    
        su "「P-please don't scare me! 」"
        fn "「Sorry, I don't know what came over me.{p}\ \ Anyways, what are you doing at the game store?{p}\ \ Are you buying something? 」"
        
        show su 001 with dis
        
        su "「There's a game I want to get. 」"

        jump shun10_newgame

    ##############################################    
    label shun10_newgame:

        $ event_name = "Not Being Sold on Launch Day"

        stop music fadeout .25
        play music free0213
        $ renpy.music.set_volume(0.8, 0.1, channel = "music")
        show su 003 with dis
    
        su "「...aaawwwww 」"
        su "「Today is the launch day, but...{p}\ \ I knew it. it's not here. 」"
        fn "「Huh? 」"
        "Why isn't it here on its launch date?{w=.3}\nAnd, \"I knew it\"?"
        
        show su 010 with dis
    
        su "「The shipment...\nit's been delayed a few days for this store. 」"
        "Wow. The countryside is frightening.{p}That reminds me, my magazines\nwere a little late too."
        "Minasato seems to still have yet\nto catch up to the cutting edge."
        su "「I thought there might be a chance\n\ \ it'd be here, but...{w} I'm disappointed,\n\ \ I hope it gets here soon. 」"
        "Shun-kun's shoulders dropped.{p}I wish I could help him,\nbut there's nothing I can do about this..."
        su "「Gaku-san was right... *sigh* 」"
        fn "「Gaku-san? 」"
        "That name is unfamiliar to me."
        
        show su 001 with dis
    
        su "「Yeah, my second cousin's big brother. 」"
        "Huh, I didn't know about him.{p}Shun-kun's onii-san? Hmmm." 
    
        show su 002 with dis
        
        su "「Ah, I know!{w} [fn]-san,\n\ \ would you like to go to Kazenari with me? 」"
        fn "「To the next town over? 」"
        su "「I'm going to Gaku-san's game store.{p}\ \ If it wasn't being sold here,\n\ \ I promised to buy it there. 」"
        su "「I want you to meet Gaku-san,\n\ \ so if you're free, please come! 」"
        fn "「Hmmm... 」"
    
        menu:
            "A. Since you want me to so much.":
                jump shun10_goodgame
            "B. I'll have to decline for today.":
                jump shun10_badgame
    
    ##########################################
    label shun10_badgame:

        $ love_shun -= 1
        
        fn "「Hmm... I'll have to decline for today. 」"
        
        show su 016 with dis
        
        su "「Really? That's too bad. 」"
        fn "「Sorry, ask me some other time. 」"
        
        show su 002 with dis
    
        su "「Okay!{w=.3} I will!! 」"
        
        hide su with dis
        
        "I see Shun-kun off to the bus stop. {p}Now, I wonder if I should make my way home..."
        
        jump end10
    
    ############################################
    label shun10_goodgame:

        $ love_shun += 1
    
        fn "「Alright then, I'll go with you. 」"
        su "「Yaaay♪ 」"
        
        hide su with dis
    
        "He squeezes onto my arm from the side.{p}Him stuck to me like this makes the differences\nin our heights all the more apparent."
        "We look like brothers... no, parent and child."
        
        scene black with dis
        
        "That reminds me, when I was at Shun-kun's house\nthe other day, I saw his dad and mom."
        "I should have seen them plenty of times\n5 years ago, but my childhood memories are fuzzy."
        "I could only remember that their figures\nwere similar to Shun-kun's."
        "And sure enough, when they greeted me at the\nfront door, they were as small as Shun-kun."
        "It seems the differences between the\nadult and child wolves in this village\ndon't have the specifications like Sylvania."
        "When evening came, their three peculiar shadows\nfrom the sunset waved at me as I left Shun's home."
        
        #hide text box
        
        scene bus with dis
        
        "I can't come back until evening if I leave\nthe village this early in the afternoon."
        "Because of the small number of buses,\nit doesn't seem like Shun-kun sees Gaku-san very much."
        "From what I heard, he's a wolf who\nloves video games as much as Shun-kun."
        "Although he may be older since he called him\n\"onii-san\", he probably isn't all that tall,\nbased on previous examples."
        
        show su 001 at center with dis
    
        su "「We're going to be there soon♪ 」"
        "Shaking as much as usual,\nthe bus arrives to its destination."
        
        scene black with Dissolve(1)
        
        scene street_corner
        show su tailwag 01 at center
        with dis 
 
        $ event_name = "Gaku-san's store"
        
        su "「[fn]-saaan, this way♪ 」"
        "Just a short walk from the station,\nI see the store.{w} I chase after Shun-kun,\nwho is gleefully half running."
        
        scene black with dis
        pause .1
        scene bookstore with dis
        show su 002 at midright with dis
        
        play music shop02
        $ renpy.music.set_volume(0.8, 0.1, channel = "music")
    
        su "「Good afternoon♪ 」"
        
        show gk 001 behind su at midleft with dis
        
        who "「Aah, Shun. 」"
        "Huh?"
        
        show su 016 with dis
        
        su "「Gaku-san, you still haven't got the shipment. 」"
        
        show gk 002 with dis
        
        $ encounter_gaku = True
    
        gk "「No, I haven't. 」"
        
        show su 003 with dis
        
        su "「But I was going to play it when I got home today... 」"
        su "「And since I was going to buy it here,\n\ \ it'll be late when I get back and\n\ \ I'd have to do it tomorrow... *sniffle* 」"
        gk "「It's too bad they don't put demo units in homes...{p}\ \ {nw}"
        show gk 001 with dis
        extend "Don't feel down. 」"
        
        show su 010 with dis
        
        su "「Uuu. 」"
        "What?"
        
        show su 002 with dis
        
        su "「Oh, Gaku-san!{w=.5} This is [fn]-san!{p}\ \ He moved away from Minasato 5 years ago,\n\ \ but he came back this summer♪ 」"
        "He's tall."
        su "「[fn]-san!{w=.3} This is Gaku-san!{p}\ \ He's my second cousin's big brother\n\ \ and works at this game store♪ 」"
        
        show gk at bowing
    
        gk "「...thanks for taking care of Shun. 」"
        fn "「Oh, no, I should be saying that. 」"
        "I never thought his line of sight would be coming\nfrom above.{w} He's... err.... like Kyouji? {p}It doesn't seem like he's a blood relative of Shun."
        "Rather than slender, underweight seems more correct.{p}It's different from a body Shun would have when\nhe's older... Um, well..."
        "He looks unhealthy."
        gk "「Did you bring Shun with you? 」"
        fn "「N-no, he invited me. 」"
        su "「He came with me!{p}\ \ Hehee, I wanted you to meet him too,\n\ \ so I invited him. 」"
        gk "「...Is that so? Thanks. 」"
        
        $ event_name = "All Kinds of Test Play Stands"
    
        show su 004 with dis
        
        su "「[fn]-san, may I play for a little bit? 」"
        fn "「Hm? 」"
        "Fidget, fidget. {p}Shun-kun seems like he can't contain himself."
        "I looked over earlier, covering the whole\ninside wall of the store are test play units.{p}I get it."
        fn "「Sure, go have fun. {p}Has it been a while since you've been here? 」"
        
        show su tailwag 01 with dis
    
        su "「Yaay♪ {p}\ \ Thank you~☆ 」"
        "Looking delighted from the bottom of his heart,{p}Shun-kun approaches the screen {p}and picks up a controller."
        "Aah, his tail's contact width has gotten really good."
        "For now I'll gaze at it.{p}..."
        
        show su 001 with dis
    
        stop music fadeout .25
        play music battle01
        $ renpy.music.set_volume(0.8, 0.1, channel = "music")
    
        su "「I should think about the height differences\n\ \ of the mountain area map, shouldn't I? 」"
        gk "「Movement on cliffs is impossible for characters\n\ \ who can't move or fly more than 3 steps. 」"
        
        show su 015 with dis
    
        su "「Do firearms have any effect? 」"
        
        show gk 002 with dis
    
        gk "「Bow and arrow types and bullet types are out,\n\ \ so you can ignore long-range skills. 」"
        
        show su 001 with dis
    
        su "「Field magic... each attribute\n\ \ seems to be different. 」"
        
        show gk 001 with dis
    
        gk "「Physical attributed ones like meteorite are\n\ \ useless, so your attack range is narrowed. 」"
        "That's called a strategy simulation RPG, isn't it?{p}Characters are walking on a grid and\na guy is attacking or defending a castle."
        "Even though they don't dislike me,\nthere's no chance for me\nto get in to their discussion."
        
        menu:
            "A. Listen to them talk.":
                jump shun10_gametalk1
            "B. I'm getting sleepy":
                jump shun10_sleepy
    
    ####################################
    label shun10_gametalk1:
    
        "Seeming to be satisfied with playing for a while,\nShun-kun reaches for the next game."
        
        show su 002 with dis
        stop music fadeout .25
        play music free22
        $ renpy.music.set_volume(0.8, 0.1, channel = "music")
    
        su "「I'm happy for the exclusive\n\ \ controller simultaneous release♪ 」"
        gk "「The operability isn't very good, to be honest.\n\ \ It's filled with buttons. 」"
        "Ah, I might be able to get in on the conversation."
        fn "「Don't you... strike that thing to the music? 」"
        su "「That's right, you do Morse code with the music♪ 」"
        fn "「???{w=.1} Huh?{w=.1}\n\ \ The game already started? {p}\ \ Do you say something like \"beep beep\"? 」"
        
        show su tailwag 01 with dis
    
        su "「・－・・・　－－・－　－・　・・　－－・\n\ \ －－・－・　・・－・　・－－　・・－ 」"
        su "「・－・・・　－－・－　－・　・・　－－・\n\ \ －－・－・　・・－・　・－－　－・－－－ 」"
        su "「・－・・・　－－・－　－・　・・　－－・\n\ \ －－・－・　・・－・　・－－　・－・・・\n\ \ ♪♪♪♪♪ 」"
        fn "「It's so fast!{w=.1}\n\ \ I mean, where do you look on the screen and tap!? 」"
        
        show gk 002 with dis
    
        gk "「Neither the lyrics or\n\ \ the notes appear in stealth mode. 」"
        
        menu:
            "A. Keep listening.":
                jump shun10_gametalk2
            "B. I'm getting sleepy.":
                jump shun10_sleepy
        
    ##########################################
    label shun10_gametalk2:

        show su 001 with dis
        
        "The next screen has realistic scenery\nreflected in it.{w} Oh, this is CG isn't it?\nTechnology these days sure is amazing..."
        fn "「Wow, that scenery looks like the real thing,\n\ \ doesn't it? 」"
        
        show su 010 with dis
        pause .2
        stop music fadeout .25
        play music oo39_cho_ys001
        $ renpy.music.set_volume(0.8, 0.1, channel = "music")
    
        su "「Uu, I'm not good with 3-D maps... 」"
        
        show su 003 with dis
    
        su "「Hauhau,{p}\ \ I still don't know where I'm standing...{p}\ \ Spin spin spin spin... 」"
        gk "「Keep changing the perspective like that\n\ \ and you'll get even more dizzy. 」"
        
        show su 006 with dis
    
        su "「Spin spin♪ 」"
    
        show gk 001 with dis
    
        gk "「Shun isn't any good at polygon shooting either. 」"

    #######################################    
    label shun10_sleepy:

        $ event_name = "Don't Break Him"
    
        scene bookstore with Dissolve(1)
        stop music fadeout .6        
        pause .2        
        show gk 001 at center with dis
        pause .5
        play music ambience01
        $ renpy.music.set_volume(0.8, 0.1, channel = "music")
    
        gk "「[fn]-san. 」"
        fn "「Y-Yes!? 」"
        "Suddenly, he calls my name."
        "He resembles Shun-kun,\nbut has a nice, low voice. {p}Since he used \"san\", I strangely sat up."
        "Softly and silently he approaches me.\nThen, quietly into my ear."
        
        show gk 001 big at center_big with dis
    
        gk "「Making Shun cry is alright,\n\ \ but don't break him. 」"
        "!!"
        "W-wait a minute, how did he know?{p}Did he hear from Shun-kun about how\nI made him cry the other day?"
        "I mean, that wasn't even my fault\nin the first place..."
    
        show gk 005 big with dis
    
        gk "「...don't break him. 」"
        "The sharp glint in his eyes\nis enough to give me the chills.{p}He emphasizes the second half."
        fn "「A-Alright... I'm sorry... 」"
        "I give into his power and apologize. {p}Really, that's a strange thing\nto say for a first meeting..."
        "But he said \"making him cry is alright\"?\nWhat's that supposed to mean?"
        
        scene bookstore with Dissolve(1)
        #Hide text box
        pause .2
        show gk 001 at midleft with dis
        stop music fadeout .25
        play music shop02
        $ renpy.music.set_volume(0.8, 0.1, channel = "music")
    
        gk "「Alright. 」"
        
        show su 001 at midright with dis
    
        su "「Hehe♪{w=.1} Thank you. 」"
        "While I'm thinking about various things, {p}Shun-kun finishes shopping before I notice it\nand Gaku-san goes back to the cash register."
        gk "「Okay, Shun. Be careful. {p}\ \ {nw}"
        show gk 002 with dis
        extend "...with [fn]-san too. 」"
    
        show su 015 with dis
    
        su "「Huh? 」"
        fn "「I-It's nothing! 」"
        
        scene black with dis
        
        scene street_corner
        show su 002 at center
        with dis
    
        su "「That was fun♪ 」"
        fn "「Th-That was fun? 」"
        "Anxious about his new game,\nhe checks it once again."
        "Probably because it's been a while\nsince he last saw Gaku-san,{p}Shun-kun happily skips to the bus stop."
    
        show su 001 with dis
    
        su "「[fn]-san, thank you for going with me♪ 」"
        fn "「Oh, sure... 」"
        "On one hand, I'm not sure how I should\ntake those words from earlier."
        "I think he was just making fun of me,\nbut...{w} he had serious eyes."
        "It seems Gaku-san is cautious of me\nfor some reason,{w} but it looks like he was\nokay with me going home with Shun-kun."
        "Is he a worrier?{w=.2} Overprotective?{p}Was it electro-magnetic waves?"
        "Something like \"break\" is an exaggeration."
        "While looking at Shun-kun's happy profile waiting\nfor the bus, I repeat the words from earlier" 
        "and calculate the time it'll take\nto get back to the village."

        $ meet_gaku = True
   
        jump end10

##############################################    
label juuichi10:

    $ event_name = "Let's Go to Kazenari!"
    $ love_juuichi +=1
    $ focus_character = "juuichi"

    scene map
    hide screen busstop10    
    scene rice_paddy with dis
    play music daily01

    "The green rice sways in the breeze."
    "When I first came here, only straight leaves\nfilled the rice paddies,{w=.2} but now it seems that\nthe ears are sprouting."
    "Gravity's pull forces them into arcs.{p}People usually imagine rice ears as golden-yellow,{w=.2}\nbut I like them more in their green growth stage."
    "I don't think I really payed much\nattention to things like this in the past..."
    "That said, it was the norm for me,\nso I suppose I wouldn't have noticed."
    "Whoops, this isn't the time to slip into nostalgia.{p}The bus is going to be here soon."
    "I'm going to Kazenari today.{p}Not that I'm tired of Minasato or anything...{w=.2}\nI just have a good reason to go."
    "I look down at the item in my hand.{p}Wrapped in a cloth is a washed and\nneatly-folded blue jersey."
    "It's not mine, of course.{p}For one thing, it's way too big."
    "The other day,{w=.2}\nJuuichi-san and I happened to to take shelter from\nthe rain together, and he loaned me his jacket."
    "Today, I'm returning it."
    "Delivering it to his house would probably be best,{p}but returning it without saying thank you\nwould feel ungrateful."
    "...Well, that's one part of it, at least.{w=.2}I can't deny that I'm also curious to\nsee what Kazenari is like."
    "On my way to Minasato, the bus stopped there,\nbut only for a short time.{w=.2}Because of that, I didn't get to see much."
    "I remember my parents taking me to a\nbig department store there.{p}I wonder if it's still there?"
    "The excitement of being in a large building\nthat isn't in Minasato is coming back to me."
    "...Stop that.{w=.2}\nI'm not going to Kazenari to fool around.{p}I'm only going to say thank you to Juuichi-san."
    "But it would be nice to go around the place\nwith Juuichi-san."
    
    play sound car000 fadein 2 loop #Buf = 2?

    "While I think about that,{w=.2}\nI see the bus approaching on the horizon."
    
    stop sound fadeout 2 #Buf = 2?
    
    $ event_name = "Ancient traditions of Kazenari"
    
    scene black with wipe_right
    pause 1
    scene kazenari01 with wipe_right

    "It's a short, bumpy hour on the bus.{p}As we travel, the countryside gives\nway to a more modern look."
    "...This area is still less built-up than\nwhere I'm from, though."
    "I arrive at Kazenari,\nand pull a note out of my pocket."
    
    if juuichi_fireflies02 == True:
        jump juuichi10_memory
    else:
        jump juuichi10_memo
        
    #########################################
    label juuichi10_memory:
    
        "So that I don't make the same mistake that I made\nwhen I went firefly hunting, I, [fn] [ln],{w=.2}\nmade sure to write down directions!"
        "...I get the feeling that passers-by are\naverting their eyes from me,\nbut I'm sure I'm imagining it. Definitely."
        
    ##########################################
    label juuichi10_memo:
    
        "On the note are directions from the bus stop to\nKazenari High."
        "I moved when I was in elementary school,{w=.2}\nso I don't really remember where it is."
        "I called Juuichi-san yesterday,\nto make sure I had the right place,\nand that he'd be there at this time."
        "With a tournament coming up soon,{w=.2}\nit seems he practices judo all day long."
        "...I hope his enthusiasm doesn't lead to injury.{p}Surely Juuichi-san, of all people,\nwouldn't do such a thing."
        "I think about that as I walk around Kazenari,{w=.2}\nnote clenched in my hand."
        "...Oh, wasn't there a burger joint around here?{p}Memories of seeing commercials for it without\nbeing able to eat there fill me with despair."
        "There should be a model store over there...\nIt looks like it's been replaced\nby a convenience store now, though."
        "Hm, are models not enough to\nmake a living from these days?{p}Times sure have gotten tougher."
        "Even if Kazenari has advanced this far,{w=.2}\nit's only a little more effort\nto open a store in Minasato."
        "Somehow, I think a store there would prosper well."
        "While I'm thinking about convenience stores,{w=.2}\nmy destination comes into view."
        "When I look up, I see a worn concrete building.{p}It's three stories tall.\nI wonder if the floors are divided by grade."
        "Outside the gate, there are parking spaces\nfor teachers' and students' bicycles.{p}Even the entrance of this place is huge..."
        "Strictly speaking, I don't have any\nbusiness in Kazenari High.{p}I shift my gaze away from the building."
        "Next to the school stands a\nlone single-story building."
        "Ah, is this the dojo Juuichi-san was talking about?{p}I'm a little jealous, as my school only has a gym."
        "We do judo in gym class during winter.{w=.2}\nUnfortunately, 1st period has to set up the mats,\nand 6th period has to pack them up."
        "When your hands are numb with cold,\nit's a huge pain to do."
        "Whose idea was it to it to\ndo judo in gym class, anyway?"
        "...If I said something like that,\nJuuichi-san would probably never speak to me again."
        "Whoops, I can't be standing around like this.\nI need to return the jacket to Juuichi-san.\nI start walking in the direction of the dojo."
        
        stop music fadeout 3
        #Hide text box
        scene black with wipe_right
        pause 1
        scene dojo with wipe_right
        play music cicada01

        $ event_name = "Nothing Ventured, Nothing Gained"
    
        "From the open doorway,{w=.2}\nI gingerly poke my head inside."
        "It makes me strangely nervous\nto be entering another school.{w=.2}\nMaybe it's because I'm an outsider."
        "Beside the entrance is a space with wooden flooring.{p}Based on the protective gear lined up there,\nI'd say that it's for the kendo club."
        "Beyond that space,\nmats are spread out across the floor.{p}Two people are sitting on them, their eyes closed."
        "One is a wolf that I've rarely seen in Minasato.{p}The other, of course, is Juuichi-san."
        "For some reason,\nit feels like something tense is going on,{w=.2}\nmaking me hesitant to say anything."
        
        $ renpy.music.set_volume(0.4, 3.0, channel = "music")
        
        "It seems like this atmosphere is even overwhelming\nthe noisy cicadas.{w} It feels like a world\nI can't step into with my tainted shoes."
        "Masters of the dojo.{p}That would be the right way to describe those two."
        "Usually, Juuichi-san looks out of place,{w=.2}\nbut he looks right at home in a martial arts dojo."
        "His brow is wrinkled,{w=.2}\nand his mouth is set in a horizontal line."
        "I suppose should be used to him\nlooking like a martial arts expert."
        
        stop music fadeout 3
    
        "That expression that I could never pull off,\ncombined with the atmosphere in the dojo,\nmakes him look so mature and cool to me."
        "Man, a judo gi looks really good\non people with Juuichi-san's build."
    
        show tn 002 at center with dis
    
        wolf "「Mikazuki,{w=.2} there's a visitor. 」"
        "The wolf's ears twitch as he speaks.{p}...Wow,{w=.2} he noticed me from that far away?"
        "He's a scary wolf, as well as a judo expert..."
    
        hide tn with wipe_right
        
        show tn 002 at midright
        show ju 301 at midleft
        with wipe_right
        play music free10
        $ renpy.music.set_volume(0.95, 0.1, channel = "music")
    
        ju "「...[ln]? 」"
        "Juuichi-san opens his eyes.{w=.2}\nTurning towards the entrance,\nhe stands up, and beckons to me."
        "...Hmm, I can come in?{p}I'm not interrupting, am I?{p}But Juuichi-san is inviting me..."
        "Nothing will get done if I hesitate here, right?{p}I take off my shoes and socks,\nand step onto the wooden floor."
        "Has the floor been warmed by the weather?{w=.2}\nThe soles of my feet start to get warm.{p}I'm disappointed that it isn't as cool as it looks."
        "I jam my socks into my pockets,{w=.2}\nand tiptoe towards the two of them.{p}I feel like a cat burglar."
    
        show ju 308 with dis
    
        ju "「...Why are you walking like that? 」"
        fn "「Well,{w=.2} I stick out like a sore thumb here.{p}\ \ I'm feeling a little awkward. 」"
        
        show ju 301 with dis
    
        ju "「I don't think you need to worry about that. 」"
        "No matter what he says,{w=.2}\nit still makes me uneasy to enter somewhere\nlike this without authorization."
        
        ju "「Sorry for making you come all the way out here.{p}\ \ I'm usually stuck here until sunset these days. 」"
        fn "「That's fine,{w=.2} I had other things to do here. 」"
        "Since the situation was explained yesterday,{w=.2}\nwe settle everything with a simple conversation.{p}This is going really smoothly."
        "I undo the package I'm carrying,{w=.2}\nand pull out the carefully-folded blue jersey.{p}As I hand it over, I say thank you to Juuichi-san."
        fn "「Here, thanks for lending this to me.{p}\ \ I didn't catch a cold, thanks to you. 」"
        
        show ju 303 with dis
    
        ju "「No problem. 」"
        "He's as blunt as ever.{p}That said, he did let out a small sigh of relief."
        "Even though I didn't want him to make him worry,\n it always seems to turn out like this."
        "Have I not grown up at all since I moved away?{p}I'd remember an illusion like that."
    
        show ju 301 with dis
    
        ju "「Ten,{w=.2} can we finish up for today? 」"
        "Juuichi-san turns to talk to the wolf.{p}Ten-san...{w} It's not a name I'm familiar with,{w=.2}\nbut I suppose it's a big world."
    
        play sound freeze04
        show tn 003 with dis

        $ encounter_ten = True #!#Check to see if this is where it is actually called
    
        tn "「... 」"
        "The wolf suddenly opens his eyes,\nstaring straight at me."
        "This feels really intimidating...{p}Actually,{w=.2} this is just plain frightening."
        "If looks could kill,{w=.2}\nI'd most certainly be dead right now."
        "Is he the coach of the judo club, or something?{p}With those scars on his face, though,{w=.2}\nI don't see him having a respectable occupation..."
        "Or being an ordinary person."
        "No, wait.{p}Juuichi-san would never talk so casually to a coach.{w=.2}\nDoes that mean they're the same age?"
        "...He's quite a mysterious beastman."
        
        show tn 001 with dis
    
        tn "「...Hmph,{w=.2} fine. 」"
        "His eyes narrow.{p}I immediately regret not coming here a little later."
        "That's right, the tournament is coming up soon."
        "There are so many types of beastmen\nthat are naturally stronger than humans,{w=.2}\nso they can train right up to the last minute."
        fn "「Sorry, I didn't mean to interrupt your training.{p}\ \ Please don't mind me, I'll be going soon. 」"
        ju "「No, don't worry about it.{p}\ \ I was thinking about getting up soon anyway. 」"
        fn "「But...{w} What about Ten-san? 」"
        
        show tn 003 with dis
    
        tn "「You have no right to call me by my first name,{w=.2}\n\ \ but I'll let it go this time,\n\ \ as you're an acquaintance of Mikazuki. 」"
        "He glares at me with a sharp glint in his eyes.{p}I feel like a herbivore standing\nin front of a carnivore."
    
        show tn 001 with dis
    
        tn "「We usually stay in the dojo until dark.{p}\ \ ...But we'll end early today, since a friend asked.\n\ \ Mikazuki asked before we started, anyway. 」"
        "Huh? Really?{p}I glance over at Juuichi-san,\nwho quickly looks away."
        
        show ju 308 with dis
    
        "It seems it's just as he said."
        
        show tn 005 with dis
    
        tn "「...We're done with training for today. 」"
        "Ten-san stands up as he says that.{p}Whoa, he's taller than I expected.{p}He's literally looking down on me."
        "He has a different presence than Juuichi-san.{p}He has the silhouette of an inverted triangle."
        "His muscular body reminds me of a martial artist,{w=.2}\nrather than just someone who practices judo."
        "This overwhelming pressure...{w=.2}\nIt takes my breath away."
        
        hide tn with wipe_right
    
        "Ten-san quietly crosses between Juuichi-san and me,{w=.2}\nand enters a door near the entrance.{p}It's probably the dojo's locker room."
    
        hide ju with wipe_right
        show ju 301 at center with wipe_right
    
        ju "「He's not actually a bad guy...{p}\ \ He's just cautious about meeting new people. 」"
        "As I absentmindedly watch Ten-san leave,{w=.2}\nJuuichi-san covers for him.{p}Did I really look that scared?"
        fn "「Wait,{w=.2} he was making that face because he was shy? 」"
        "Hearing my response,{w=.2}\nJuuichi-san curls his mouth into a wry smile."
        ju "「No, it's not like that.{p}\ \ It's not that he can't open up to others,\n\ \ he just isn't comfortable doing it. 」"
        ju "「It's almost like a habit. 」"
        
        stop music fadeout 3
    
        "No matter how much of a judo master he is,{w=.2}\nI don't think he needs to be so standoffish...{p}I wonder if there's another reason he's like that?"
        
        play music free0470
    
        "Maybe his life is constantly under threat?{p}If he got those scars from living a brutal life,{w=.2}\nit'd be understandable for him to act like that."
        "That must be his boss or dad's way of\nwelcoming him into the business!"
        "Aah, I see.{p}So that's how it is."
        "My terrifying imagination makes my body shiver."
        
        stop music 
        play sound kara00
        show ju 311 with dis
    
        ju "「What are you associating him with? 」"
        "He lets out a sigh."
        
        play music free10
        show ju 301 with dis
    
        ju "「In his family,{w=.2} it's customary to educate their\n\ \ children in martial arts. 」"
        ju "「He told me he got those scars as a child,\n\ \ when he failed to dodge a real sword. 」"
        "That's not that different from what I imagined.{p}I'm so glad I was born into an ordinary family."
        "I thank my parents for giving\nbirth to just another child."
        ju "「Anyway,{w=.2} we're finished with training today.{p}\ \ I'll go get changed too. 」"
        fn "「Okay,{w=.2} I'll wait here. 」"
        
        hide ju with wipe_right
    
        "I watch Juuichi-san disappear into the locker room.{p}In the master-less dojo,\nthe cries of the cicadas are almost overwhelming."
        "...Oh yeah, that reminds me.{p}{nw}"
        play sound standup
        extend "I rummage around in the cloth the jersey was\nwrapped in, and pull out a piece of candy."
        "Wait, this isn't candy, is it?{p}'Electrolyte replacement supplement'\nis printerd on the transparent wrapper."
        "Of course this isn't mine.{p}It was in the pocket of Juuichi-san's jersey."
        "I noticed it and took it out before washing it,{w=.2}\nbut I completely forgot to give it back to him."
        "Isn't this the right time to take it?{p}He was really sweating."
        "This doesn't mean that I'm being opportunistic.{p}{nw}"
        scene black with wipe_right
        extend "I grasp it tightly, rush to the locker room,{w=.2}\n{nw}"
        play sound door_close
        extend "and open the door with a clank."
        
        $ event_name = "Attacked in the Jaws of Death"
        
        stop music fadeout 3
        scene white with qdis
        pause .3
        scene dojo_changing_room with wipe_right
    
        fn "「Juuichi-san, this was in your pocket.{w=.2}\n\ \ I didn't know if you wanted to take it now,{w=.2} or... 」"
        "My words trail off at the scene in front of me."
        "I suppose I should have expected this,\nsince it is a locker room."
        "Juuichi-san and Ten-san,\nboth in the middle of changing,\nturn to look at me."
        
        play music free0428
        show tn 204 at midright
        show ju 114 at midleft
        with dis
    
        "...This is what's known as 'bear-naked'."
        "There's a nice contrast between their bodies.{p}I could tell, even when they were wearing their gi,{w=.2}\nbut it's even more obvious when they're naked."
        "Just like he was at the beach,\nJuuichi-san has a layer of fat on his muscles."
        "For comparison, I'd like to ask what\nTen-san's body fat percentage is,\nwith that lean body of his."
        "And their you-know-whats are dangling in the open.{p}I don't even bother comparing theirs to mine."
        "I try to convince myself that it's because of\ndifferences in our physique."
    
        show tn 203
        show ju 111
        with dis
    
        "Just as I'm measuring which is bigger with my eyes,{w=.2}\nI finally come to my senses.{w} ...For some reason,{w=.2}\ntheir eyes seem really cold."
        ju "「[ln],{w=.2} even if you're only coming into\n\ \ the locker room for a second,\n\ \ you should always knock first. 」"
        tn "「...Opening a door without warning is something\n\ \ you shouldn't have to be careful about.{p}\ \ You should learn to show a little discretion. 」"
        fn "「...I can't think of anything to say. 」"
        "Come to think of it,{w=.2} I should have probably\njust waited outside until Juuichi-san was done."
        
        stop music fadeout 2
    
        "...Yeah,{w=.2} let's pretend my head wasn't just spinning.\nI'll do that."
        
        play music free0211
        show ju 101 with dis
    
        ju "「Why did you barge in here, anyway?{p}\ \ You started saying something. 」"
        fn "「Oh,{w=.2} I wanted to return this to you... 」"
        "I sheepishly hold out my hand.{p}Juuichi-san tilts his head and looks at it."
        fn "「It was in the pocket of your jersey.{p}\ \ I took it out before I washed it,{w=.2}\n\ \ but I forgot it was there. 」"
        fn "「I thought that you might want it now, but...{p}\ \ I guess I could've waited until you were done.{w=.2}\n\ \ Sorry about that. 」"
        ju "「Ah,{w=.2} so that's why. 」"
        "He nods his head in understanding.{p}Then,{w=.2} Ten-san voices his disapproval."
        
        show tn 201 with dis
    
        tn "「Sweets again?{p}\ \ Be more careful about what you eat\n\ \ when you're trying to lose weight. 」"
    
        show ju 103 with dis
    
        ju "「I've told you before that these\n\ \ tablets are salt supplements.{p}\ \ Besides,{w=.2} these don't have very many calories. 」"
        tn "「That's not the problem.{p}\ \ I'm going to be get in trouble if you don't drop\n\ \ down to regulation weight. 」"
        tn "「If you need salts, you should just eat rock salt. 」"
        
        play sound swing40_a
    
        "Ten-san snatches the tablet from my hand.{p}R-rock salt? Is he kidding...?"
        "No, he's being serious.{p}I could easily imagine him doing that."
        "...By the way,{w=.2} how long are they going to\ncontinue this conversation in the nude?{p}Well, I suppose this is my fault, after all."
        "They both look very impressive, so I guess they\ndon't really have a reason to cover themselves."
        "Actually, they don't seem to care.\nIs this how it usually is with athletic groups?"
        "Well,{w=.2} if they don't care,\nthen neither do I.{w=.2} No sir."
        
        show ju 101 with dis
    
        ju "「I'll be fine.\n\ \ I've been steadily losing weight. 」"
        
        show tn 204 with dis
    
        tn "「...Hmph.{p}\ \ That reminds me of the fool who said that in winter,{w=.2}\n\ \ then barely made regulation weight. 」"
        
        show ju 108 with dis
    
        ju "「... 」"
        "Juuichi-san frowns openly.{p}It seems he knows who Ten-san is talking about."
        "...Hold on,{w=.2} I thought there weren't weight\ndivisions in judo?{p}I ask Juuichi-san about this."
        
        show ju 101 with dis
    
        ju "「Some tournaments only run an open category,{w=.2}\n\ \ but this time Kazenari is having weight divisions.{p}\ \ An open weight division is difficult with my body. 」"
        "He shrugs his shoulders."
        ju "「There are the 60, 66, 73, 81,\n\ \ 90, 100, 111, 123, 134, 150,\n\ \ and above 150 kilogram divisions. 」"
        ju "「These are the 11 classes they have now.{p}\ \ It changes a little with species,\n\ \ but strength is generally proportional to weight. 」"
        fn "「Wow,{w=.2} judo is really divided up.{p}\ \ Which class are you trying for? 」"
        ju "「The 111 kilogram class. 」"
        fn "「And what's your weight right now? 」"
        
        show ju 103 with dis
    
        ju "「...114 kilograms. 」"
        "Hearing Juuichi-san's mutter,{w=.2}\nTen's pointed ears twitched."
        
        play sound don08
        show tn 203 at briefzoom
    
        tn "「Mikazuki,{w=.2} you're still hanging around that weight?!{p}\ \ Damn... If I had a sword on me right now,{w=.2}\n\ \ I'd slice off that stomach of yours! 」"
        "Uhh... Just one thing.{p}When Ten-san speaks like that,\nit doesn't sound like he's joking at all."
        "Out of fear of backlash,{w=.2}\nI keep my comments to myself,\nand stay quiet."
        tn "「Listen, there are less than two weeks left.{w=.2}\n\ \ Pay attention to what you're eating.{p}\ \ All sweets are prohibited! 」"
        "I tremble at his low, growling voice,\neven though he's not talking to me."
        
        show ju 108 with dis
    
        ju "「...I understand. 」"
        "Juuichi-san nods, reluctantly.{p}A ban on sweets...{p}Sports with weight restrictions sure are rough."
        tn "「And you,{w=.2} [ln]. 」"
        fn "「Huh?{w=.2} Uh,{w=.2} yes? 」"
        "Thinking that this conversation\nwould never involve me,\nI boneheadedly reply."
        "Looking at me, one of Ten-san's eyebrows twitches.{p}It doesn't look like he's blaming me, though."
        
        show tn 201 with dis
    
        tn "「You'll do the same as Mikazuki,{w=.2}\n\ \ and make sure he doesn't eat sweets.{p}\ \ Understood? 」"
        
        menu:
            "A. Yes.":
                jump juuichi10_understood
            "B. No.":
                jump juuichi10_hesitation
       
    ###########################################         
    label juuichi10_understood:

        fn "「I-{w=.2}I will... 」"
        "With his tone showing no signs of accepting refusal,{w=.2}\nI nod my head like a broken doll."
        
        jump juuichi10_manage
      
    ###########################################
    label juuichi10_hesitation:

        fn "「Eh,{w=.2} but... 」"
        "Not knowing how to reply,{w=.2}\nI hesitate to speak."
        tn "「I'm not talking about fasting.{p}\ \ Just don't snack between meals.{w=.2}\n\ \ That should be easy, right? 」"
        fn "「Putting aside whether or not it's easy,{w=.2}\n\ \ I think I'll be able to manage that... 」"
    
    ###########################################
    label juuichi10_manage:

        tn "「Then I'll leave it to you.{p}\ \ I can't be with Mikazuki all day long, after all. 」"
        "...I guess that's been decided.{p}When I look over at Juuichi-san in confusion,{w=.2}\n{nw}"
        show ju 103 with dis
        extend "he scratches at his cheek, looking embarrassed."
        
        ju "「[ln],{w=.2} sorry about this,\n\ \ but can you say something to me if I reach\n\ \ for sweets without thinking about it? 」"
        ju "「It's something that bears do unconsciously...{p}\ \ And a lot. 」"
        fn "「I don't know how much help I'll be,{w=.2}\n\ \ but I'll try. 」"
        "He bows his head,{w=.2}\nmaking it impossible for me to refuse."
        "But...{w=.2} I should've just returned his jersey,{w=.2}\nbut somehow this turned into a strange situation."
        
        show tn 101 with wipe_up
        play sound standup
    
        tn "「Now then,{w=.2} how long to you plan on standing there? 」"
        "He asks this while skillfully\ntying his fundoshi one-handed.{p}Oh, did he finally notice...?"
        "They acted like it didn't matter\nthe whole time we were talking."
        "Still, are fundoshi the norm in this village?{p}First Tatsu-nii and Juuichi-san,{w=.2} and now Ten-san."
        "No, fundoshi was underwear a long time ago!{p}But then the scourge of boxers and briefs...\nWait, why am I getting so worked up over this?"
        "The dull-colored fundoshi tightly holds his crotch,{w=.2}\ngiving him an impressive bulge.{p}It goes well with his toned body."
        "...Speaking bluntly, I think he has a\nmagnificent body that wouldn't be safe\nfor small children to see."
        
        play sound freeze04
        show tn 103 with dis
    
        tn "「... 」"
        "With a glare that could murder somebody,{w=.2}\nhe looks at me with a gleam in his eyes."
        fn "「E-excuse me... 」"
        "It was only for a short time,\nbut that really did a number on my nerves.{p}{nw}"
        play sound step03
        extend "Overwhelmed, I had to flee from that place."
        
        scene black with wipe_right
        pause 1
        scene dojo with wipe_right
    
        "I'm sitting on the floor outside the locker room,\nwaiting for Juuichi-san to finish changing,{w=.2}\n{nw}"
        play sound door_close
        extend "when the door suddenly opens with a clank."
        "I glance up to see Ten-san, dressed casually."
        "...Not only does he wear old-fashioned underwear,\nhe wears old-fashioned clothes, too."
        "With the scars on his face and all those muscles...\nNo, I'll stop imagining strange things."
        "As he walks towards the entrance,\nhe speaks to me without looking at me."
        tn "「Don't forget, watch him. 」"
        "Hmm, he didn't even give me the time of day.\nAs I watch him leave, his tail swaying side-to-side,\nI hear the creaking of the dojo door again."
        
        show ju 001 at center with dis
    
        ju "「Oh,{w=.2} did Ten already leave? 」"
        fn "「Yeah. 」"
        "Juuichi-san lets out a small sigh.{p}Then, he takes the tablet out of pocket,{w=.2}\nunwraps it, and pops it into his mouth."
        fn "「Juuichi-san,{w=.2} is it okay to eat that? 」"
        "I told Ten-san I'd do it...{w=.2}\nBut I ask indirectly, to be careful."
        ju "「Yeah.{w=.2} Like I said earlier, it's low in calories.{p}\ \ Much less than a spoonful of honey. 」"
        "He chews on the tablet.{p}It's just like him to compare it to honey."
        fn "「You have to lose 3 kilograms.\n\ \ Won't that be difficult? 」"
        ju "「It shouldn't be too hard.{w=.2}\n\ \ You're half...{p}\ \ {nw}"
        show ju 008 with dis
        extend "No, two-thirds my body weight. 」"
        "...I'm pretty sure it's double.{p}The speed at which he loses weight would\nbe different, wouldn't it?"
        fn "「Well,{w=.2} you probably won't need me that much. 」"
        ju "「Probably not.{p}\ \ {nw}"
        show ju 003 with dis
        extend "...Ten always has exaggerated things. 」"
        fn "「Well, you should still be careful.{p}\ \ I'll help however I can. 」"
        ju "「...Sorry for getting you involved.{p}\ \ {nw}"
        show ju 001 with dis
        extend "I was sure you were going to refuse. 」"
        fn "「I was worried that I would be told to something\n\ \ technical,{w=.2} but I was just told to keep an eye\n\ \ on you so that you don't overeat. 」"
        fn "「...Besides,{w=.2} nobody could say no\n\ \ if Ten-san was glaring at them like that. 」"
        "It was like being commanded by a scary teacher to\nstay after school.{w} 'No veto power'\nwould be a good way to put it."
        
        show ju 008 with dis
    
        ju "「Hm... I'm used to seeing him like that,\n\ \ so I didn't think anything of it. 」"
        ju "「I guess it's different for\n\ \ someone meeting him for the first time. 」"
        "He speaks with a growl in the back of his throat."
        "...I almost say that Juuichi-san\ncan be just as scary,{w=.2}\nbut I stop myself just at the right time."
        "So dangerous.{p}The mouth truly is the origin of disaster."
        fn "「So what are we going to do now?{p}\ \ I haven't eaten yet.\n\ \ I was thinking we could get lunch. 」"
        
        show ju 003 with dis
    
        ju "「Really? 」"
        fn "「I passed a burger joint on the way here,\n\ \ but I didn't go in since I\n\ \ was planning on inviting you. 」"
        fn "「...We'll probably get\n\ \ yelled at by Ten-san for that. 」"
        
        show ju 008 with dis
    
        ju "「I should really stop with the junk food.{p}\ \ Hm, there's an onigiri shop a short walk from here,\n\ \ how about that? 」"
        fn "「Wow, there's a store like that? 」"
    
        show ju 001 with dis
    
        ju "「Yeah.{w} It's part of a business that uses rice\n\ \ from Minasato. They started out in Kazenari,\n\ \ and I heard that they plan to expand. 」"
        "Oh yeah, I remember Torahiko saying something\nlike that at the welcoming party.\nSmall chains don't tend to do well, though..."
        fn "「Are they any good?{p}\ \ Something like that doesn't always work well. 」"
    
        show ju 008 with dis
    
        ju "「...It's become a hangout for sports club types,{w=.2}\n\ \ but the management seems okay with it.{p}\ \ I don't know whether that's a good or a bad thing. 」"
        fn "「I wonder if they're making money...{p}\ \ Well, let's try it.{p}\ \ It's got to be healthier than hamburgers, right? 」"
        
        show ju 001 with dis
    
        ju "「Sorry for making you have to worry about that. 」"
        fn "「No, I don't mind.{p}\ \ I'm interested in trying out new things, anyway. 」"
        ju "「...I see.{p}\ \ All right, let's go. 」"
        "And so I spent the rest of the day at the unusual\nrestaraunt with Juuichi-san."    

        $ meet_ten = True
       
        jump end10

##############################################
label tatsuki10:

    $ event_name = "Part-time job at the Midoriya Group"
    $ love_tatsuki += 1
    $ focus_character = "tatsuki"

    scene map
    hide screen tatsukihouse10
    stop music fadeout .8
    scene black wipe_dr
    play music free02
    scene tatsuki_house_front with wipe_corner
    scene old_house2 with Dissolve(1)

    fn "「Excuse me,{w=.2} is it all right if I put this over there? 」"
    
    show te 001 at center with dis

    te "「Yes, that is fine.{p}\ \ Anyway, it seems like you're doing more work,\n\ \ and you're getting better at it. 」"
    fn "「No, no, I'm only putting things in order.{p}\ \ Even at that, I need to do my best.{p}\ \ Now,{w=.2} time to work even harder! 」"
    "I've been working for several days, but\nhaven't improved yet.{p}I've been too busy with odd jobs to even think,"
    "and I've needed to use my muscles.\nEven though I knew all that beforehand...{p}Working's tough."
    
    show cu 001 at midright with wipe_right

    cu "「If the veteran Tetsu-san said it,\n\ \ then there's no mistake. 」"

    show te 003 with dis
    
    te "「No...{w=.2} I'm not quite at that level yet.{p}\ \ Even after all the time I have spent here,\n\ \ I can still get scolded by the boss. 」"
    
    $ encounter_tetsuya = True
    
    "Tetsuya-san's a splendid worker,\nbut he's surprisingly humble."
    "His manners are so proper,\nand he's the opposite type of Tappei-san."
    fn "「If I remember right, you came here to learn.\n\ \ Even after fully qualifying, it's amazing that you\n\ \ can improve further. 」"
    
    show te 001 with dis

    te "「I came here to study because I was inexperienced.{p}\ \ I only know how to do the basics. 」"
    
    show cu 002 with dis

    cu "「Tetsu-san, saying that makes ya so refined. 」"

    show ta 002 at farleft behind te with wipe_right

    ta "「Craftsmen bring their own techniques to improve them. 」"
    ta "「Seeing how other people work and getting\n\ \ experience in a buch of different places is good,\n\ \ better than always working in just the one place. 」"
    "So, Tatsu-nii, when are you going to leave Minasato?"
    te "「[fn]-kun's muscles are looking good.{p}\ \ At this rate, if you wanted to study with the Midoriya\n\ \ Group, you should be able to become a fine craftsman. 」"
    fn "「No way, I couldn't be one. 」"
    
    show ni 001 at farright with wipe_right

    ni "「It doesn't matter to me if you can become a\n\ \ craftsman or not, but if you do try,{p}\ \ I don't think you'll understand anything. 」"
    
    show cu 001 with dis

    cu "「If it's you, Aniki, you should be able t' do it. 」"
    fn "「I'm so glad you can say that. 」"

    show ta 004 with dis

    ta "「[fn] is a man I recognize.\n\ \ It'll be a piece of cake for him to do it. 」"
    
    show ni 002 with dis

    ni "「The same couldn't be said for you, could it.{p}\ \ In any case, this isn't your job station, is it? 」"

    show te 003 with dis

    te "「Young Master,\n\ \ it would be bad if the Chief found you here. 」"
    
    show ta 006 with dis

    ta "「I know,{w=.2} I came here because I had something to do.{p}\ \ {nw}"
    show ta 001 with dis
    extend "Later, [fn]. 」"
    
    hide ta with wipe_right
    show tp 401 at farleft with wipe_right

    tp "「Oh, are you bastards done with work?{p}\ \ If you're free, then get your hands moving. 」"
    tp "「[fn], if you're free,\n\ \ come assist me in my office. 」"
    fn "「Okay, I'll be there soon. 」"
    "This really is different from usual,\nTappei-san's scary when he's in the middle of work..."
    
    stop music fadeout .5
    scene black with Dissolve(1)
    play music cicada01 fadein 1
    $ renpy.music.set_volume(0.4, 0.1, channel = "music")
    scene old_house_inside with Dissolve(.5)

    fn "「Uhh, the total amount this month is...{p}\ \ Huh? Negative??? 」"
    
    show ta 001 at center with wipe_right
    
    ta "「What's wrong, [fn]? 」"
    fn "「Nothing, the calculations aren't matching...{p}\ \ Wait, why are you here, Tatsu-nii? 」"

    show ta 002 with dis

    ta "「Gahaha, I'm busy.{p}\ \ Always having to move around until dark. 」"
    fn "「Even though you're an apprentice? 」"
    
    show ta 001 with dis
    
    ta "「Shut up, don't be so picky.{p}\ \ Here, can't do addition? Let me see. 」"
    fn "「Somehow, we're in the red... 」"
    
    show ta 008 with dis
    
    ta "「Hmm...\n\ \ Maths isn't my strong point,\n\ \ but maybe this isn't wrong. 」"
    fn "「Huh?!　But we're in the negatives! 」"
    ta "「About Pa, if he sees good lumber, he buys it up\n\ \ right there.{w} He never thinks about money... 」"
    fn "「You don't buy only as much lumber as you need?\n\ \ Do you really need that much on hand??? 」"

    show ta 002 with dis

    ta "「The wood we use is a little different. 」"

    show ta 001 with dis

    ta "「For example, there's a thick post for the ceiling,\n\ \ right? It's called a beam, but there aren't any\n\ \ trees big enough left in Japan to be used for"
    ta "things that size. 」"
    fn "「But even so... 」"
    ta "「Anyway, before we use the wood, we have to dry it.\n\ \ There have been times where the planks have been\n\ \ stored dry for 100 years. 」"
    ta "「Meaning, after a guy cuts down the tree,\n\ \ with proper treatment you can preserve it for\n\ \ centuries. Timber can be amazingly durable. 」"
    fn "「100 years!? So there is wood that lasts that long. 」"

    show ta 002 with dis

    ta "「Oh yeah, inside there's wood about 300 years old.\n\ \ It can last that long. 」"
    ta "「It's the same with woodwork.\n\ \ There's still some left standing\n\ \ from one or more centuries ago. 」"
    ta "「Craftsmen today can't just think about the 'now',\n\ \ they've gotta think about things hundreds of years\n\ \ from now. 」"
    "Tatsu-nii sure loves his work...{p}He's being lively, in a way I hadn't seen him before.{p}Taking pride in his work, huh?"
    
    show ta 010 with dis
    
    ta "「Still, since we have a dumbass who buys wood without\n\ \ thinking, we're losing money.{p}\ \ Just look at the costs. 」"
    fn "「Tappei-san sure doesn't seem like that kinda guy. 」"
    
    show tp 401 behind ta at offright
    show ta 008 with dis
    
    ta "「It'd be fine if it were just carpentry, but\n\ \ Pa has to deal with making furniture without nails. 」"
    ta "「Because of that, his obsession makes things\n\ \ difficult. We get pressed into taking side jobs. 」"
    ta "「Whether workers buy wood they're interested in...{p}\ \ Let's just say that if there's work to be done\n\ \ without wood, I couldn't deal with it as well... 」"
    
    show ta at move_midleft(0.5)
    show tp at move_midright(0.5)
    
    tp "「Well, look who's having fun.\n\ \ Is your nice little explanation done yet? 」"
    
    show tp 403 at hit_left
    show ta 006 with qdis
    play sound bosu32
    
    "An extra-large fist was swung at Tatsuki's head."
    tp "「Are you that free, bastard? Get back to work! 」"
    ta "「Oww... 」"
    tp "「'Oww...' my ass.\n\ \ Get back to what you're supposed to do. 」"
    tp "「[fn], if you're done caring about\n\ \ this idiot and finished, wipe the table,\n\ \ then you're done for the day. 」"
    fn "「Yes, Boss. 」"
    "He's mad, that's all I can tell.{p}I should finish up before I piss him off, too."
    
    #hide text box
    scene black with wipeleft
    scene old_house2 with Dissolve (1)
    play music free53 fadein 3

    fn "「Now then... Just a little more, and I'm finished. 」"
    
    show ta 001 at center with dis

    ta "「Yo, you almost done? I'll give you a hand. 」"
    fn "「Is that okay, Tatsu-nii?\n\ \ You'll make him mad again... 」"

    show ta 002 with dis

    ta "「What are you worried about?\n\ \ Don't pay it any mind. 」"
    "Is this really all right...?"
    fn "「Thanks, Tatsu-nii.{p}\ \ Ever since I came back, you've always been helping me,\n\ \ but today will be the opposite. 」"

    show ta 001 with dis

    ta "「Now that you mention it, yeah.{p}\ \ Well, how is it? We talked about it before,\n\ \ but are you adjusting to things? 」"
    fn "「Hmm, I'm still a little tired.{p}\ \ I'm starting to talk like the Midoriya Group, though. 」"
    
    show ta 008 with dis
    
    ta "「That so? It'd be great if you got used to things\n\ \ quickly. 」"
    fn "「Yep.{p}\ \ But it's fun, and it might\n\ \ get even better if I do adjust. 」"

    show ta 002 with dis

    ta "「Of course. Where do you think you'll be working?{p}\ \ Gahahaha! 」"
    "Man, I want to be more helpful to the Midoriya Group.{p}\ \ That'd be fun, too."
    
    scene old_house2
    show tp 403 at midright
    show ta 001 at midleft
    with wipe_right

    tp "「Are you fooling around again? 」"

    show cu 001 at offright_far
    show tp at hit_left
    play sound bosu32
    show ta 006 with qdis

    ta "「Eeyow! 」"
    "Tatsu-nii...{p}Even though you're in the middle of work,\nyou still mess around."
    
    show ta at move_offleft_far(1)
    show tp at move_midleft(1)
    show cu at move_farright(1)

    cu "「Master, I'm finished. 」"
    tp "「Don't call me that, how many times do I have to say\n\ \ it. Just call me boss, damnit! 」"
    
    show cu 009 at hit_right
    play sound hit81
    $ chuu_beat += 1
    
    cu "「Gwoh...! 」"
    
    scene old_house2
    show ni 005 at center
    with wipeleft

    ni "「（It's bad right now... He's pretty annoyed.） 」"
    "This is bad. I'd die if I got hit by that.{p}Let it end quickly and quietly."
    
    #Hide text box
    scene black with Dissolve(1)
    pause .1
    scene old_house2 with wipe_right

    $ event_name = "After Work"

    stop music fadeout .5
    play music higurasi
    $ renpy.music.set_volume(0.7, 0.1, channel = "music")

    fn "「Whew, I'm tired. 」"
    "I'm completely exhausted, and it's finally done.{p}I've been working for 1, 2 hours, and I'm this tired."
    "Tatsu-nii and everyone else\nare tough to be working since morning."
    
    show ta 001 at center with dis

    ta "「Good work.{p}\ \ You're thirsty, right? I brought some iced tea. 」"
    fn "「Awesome, thanks Tatsu-nii.{p}\ \ ...Hwaah,{w=.2} it's great when it's cold.{p}\ \ Having a cup after work really is awesome. 」"
    fn "「Maybe we can get some candy up here, too. 」"
    
    show ta 002 with dis

    ta "「When you get tired after moving around, You just\n\ \ want something sweet.{w} You totally get it, don't\n\ \ you? 」"
    ta "「I love drinking sake, though. 」"
    fn "「I'm worried about getting fat from constantly eating\n\ \ them.{w} It'd be a problem if I became like you. 」"
    
    show ta 010 with dis

    ta "「Hey, I'm not getting fat, dragon bellies are round.{p}\ \ Anyway, if you ate steadily you'd grow taller. 」"
    fn "「Hahaha, that's so unreasonable.{p}\ \ Say, Tatsu-nii, just how tall are you? 」"
    
    show ta 008 with dis

    ta "「210 centimetres or so...{p}\ \ I think I weigh 135. 」"
    fn "「So, what do I do if I grow past two metres and\n\ \ weigh more than 100 kilograms? 」"

    show ta 006 with dis

    ta "「Huh? 」"
    
    stop music fadeout .3
    play sound dream
    scene white with wave #!#There also seems to be some sort of shaking effect... fix this later
    play music oo39_cho_ys001

    fn "「Hey, Tatsu-nii. 」"
    
    play sound bosu35
    #Shake textbox 10
    "{cps=0}{size=+40}BANG! {w=1}{nw}"
    play sound bosu35
    #Shake textbox 20
    extend "BANG! {w=1}{nw}"
    play sound bosu35
    #Shake textbox 50
    extend "BANG!{w=1}"

    fn "「There, I've stretched until I'm as big as Tatsu-nii,{p}\ \ and my weight has increased by 100 kilos. 」"
    fn "「Now we can play-wrestle like they\n\ \ did in the Greco-Roman times.{p}\ \ {nw}"
    play sound puu75
    extend "Now, Let's do it for real! 」"
    
    play sound puu79_a

    ta "「Gyaah!! 」"

    play music higurasi fadein 1
    scene old_house2
    show ta 008 at center
    with wave #!#Same trasition as before with shaking wave
    pause 1

    ta "「Hmm... That was gross.{p}\ \ {nw}"
    show ta 010 with dis
    extend "You're disgusting, [fn]. 」"
    fn "「You're so mean. And all that,\n\ \ after you told me to get bigger. 」"

    show ta 008 with dis

    ta "「Anyway, I think there's another kind\n\ \ of wrestling, without leotards... 」"
    fn "「Tatsu-nii?{w=.2} What are you talking about...? 」"
    
    show ta 010 at jump_up

    ta "「N-nothing.{p}\ \ Never mind that, are you free today after this? 」"
    fn "「Yeah,{w=.2} I've got nothing later.{p}\ \ It's because I'm free that I can do this work. 」"

    show ta 001 with dis

    ta "「Then come out with me for a bit.{p}\ \ I'll take you someplace nice. 」"
    fn "「Hm, okay. Let's do it.{p}\ \ But what is this \"nice place\"? 」"

    show ta 002 with dis

    ta "「Gahahaha, if you're free just shut up and come.{p}\ \ look forward to it!{p}\ \ I'll get my car, get in get in! 」"
    
    scene old_house2
    show ta 002 at midleft
    show cu 001 at midright
    with wipe_right

    cu "「Huh? Where are you guys going?{p}\ \ Please take me, too? 」"
    
    show ta 001 with dis

    ta "「Sorry, Chuu, this isn't for fun today. 」"

    show cu 004 with dis

    cu "「It isn't?{p}\ \ Where're you goin' then? 」"

    show ta 002 with dis

    ta "「Hehehe, I can't say...{p}\ \ It's a nice place, you hear.\n\ \ Gahaha! 」"
    fn "「Sorry, he's not telling me, either. 」"
    ta "「Later. Counting on you\n\ \ to look after the place. 」"
    
    hide ta with wipe_right
    show cu 005 with dis

    cu "「Tch, I've been wanting to hang out with Aniki, too.{p}\ \ Aren't they getting on too well for childhood\n\ \ friends? 」"
    cu "「...!? 」"
    
    show cu 006 with dis

    cu "「No way, could Aniki and Young Master...{p}\ \ That can't, no way.{p}\ \ {nw}"
    show cu 007 with dis
    extend "Right. Absolutely not. 」"
    
    scene black with blind_vert
    
    $ event_name = "Past the Mountain"

    play music free10
    $ renpy.music.set_volume(0.8, 0.0, channel = "music")
    pause .3    
    
    scene mountain_path
    show ta 001 at center
    with blind_vert

    fn "「Hey, are we there yet?{p}\ \ It's been 30 minutes. Is it that far? 」"

    show ta 008 with dis

    ta "「Don't get your pants in\n\ \ a bunch, we're nearly there. 」"
    "I'm not panicking, but because of Tatsu-nii's driving,\nit feels like I'm losing all my strength.{p}Let me off soon..."
    fn "「Hurgh. But what's up in the mountain?{p}\ \ There shouldn't be anything near Minasato\n\ \ Village... 」"
    fn "「Was something done? 」"

    show ta 001 with dis

    ta "「No, it's something that's been there for a while,{p}\ \ but I'm using it now. 」"
    fn "「\"Using it\"? 」"

    show ta 002 with dis

    ta "「Pipe down, already.{p}\ \ Look, here we are. 」"

    scene prairie
    show ta 002 at center 
    with Dissolve(1)

    fn "「\"We're here\", you say...\n\ \ this is that nice place you mentioned? 」"
    ta "「Yep. Isn't it a great view? 」"
    "Ahead in the field, there's nothing in sight,\nexcept for...{w=.2} something that could be a vacant\nparking lot."
    "It looks like some sort of huge highway,\nbut I'm getting worried about the cliffside."
    
    show ta 001 with dis

    ta "「Too surprised to say anything?{w=.2}\n\ \ It's still too early for that.\n\ \ It starts for real, here. 」"
    ta "「You'll be knocked off your feet,\n\ \ once you see what's inside. 」"
    fn "「Inside? Inside of what? 」"
    ta "「Hehe, come along now. 」"
    "Tatsu-nii said that, got out of the light truck,\nand briskly started walking across the field.{p}I chased after him."
    ta "「You're slow, hurry it up. 」"
    fn "「Hold on a sec. 」"
    "At the end of the field, Tatsu-nii entered the forest\nand walked along the animal trail."
    "I followed behind,\nthen saw him entering a large\nhole in the mountainside."
    
    scene cave_entrance
    show ta 001 at center 
    with Dissolve(1)

    "Is this a cave?{p}It wouldn't be strange, since it's in a mountain...{p}I wonder what's inside."
    
    hide ta with dis

    "Oh, while I was thinking about it,\nhe already went in...{p}I suppose I should go in, too."
    
    #hide box with dis #!#HideInterface()
    scene black with Dissolve(1)

    fn "「Tatsu-nii...{w=.2} Where are you...? 」"
    "It's so dark I can't see anything,\nand I can't walk along a wall."
    ta "「Over here, just a minute. 」"
    "I thought we were separated for a bit,\nbut judging by the voice he seems to be close by."
    fn "「Hey, what the hell is in here?{p}\ \ Just tell me, already. 」"
    fn "「W-Wha! 」"
    "Huh? The wall's direction changed.{p}It feels like the edges got wider,\nbut I can't see..."
    ta "「Oh, the switch is over here. 」"

    scene cave_inside
    show ta 002 at center
    with Dissolve(1)

    ta "「Sorry. It's usually just me in here,\n\ \ so I didn't think about it.\nGahaha! 」"
    fn "「Whoa, it's amazing... 」"
    "With the light hanging from the ceiling illuminated,\nI finally got a chance to take in my surroundings."
    "There's a lot of space inside this cave,\nalmost like a room."
    "I wonder how Tatsu-nii got this far,\nbecause somehow it feels like\nhis life has been adrift."
    fn "「It looks like a secret base. 」"
    "Looking around the room, I notice a desk\nand chair.{w} I don't know if Tatsu-nii\nwas the one to bring them in, though."
    "Is that a...{w=.2} blueprint?"
    "There's scraps, random parts and stuff scattered\nboth on the ground and on top of the desk.\nIt's so messy."
    ta "「How about it? A man's hiding place, yeah?\n\ \ There's electricity and a well nearby. 」"
    ta "「You could live in this place for a while,\n\ \ if you needed to. 」"
    "But how come he's stayed quiet about it?{p}If Tatsu-nii had this kind of place,{w=.2}\nsurely he'd have told everyone about it..."
    ta "「And, this became the door. 」"
    fn "「If there's a door, why didn't we come in that way?{p}\ \ Just what... 」"
    "Further in the room was an opening,\nand in front of it was a huge bundle,\ncovered with a sheet."
    
    show ta 001 with dis

    ta "「Oh, this isn't a door meant for people.{p}\ \ It's the passageway for this thing. 」"
    "Tatsu-nii pulled off the sheet,\nand struck the object underneath with a light tap."
    fn "「Is that an airplane!? 」"
    "It's a red aircraft with a propeller,\nlike the kind I've seen in movies.\nThe design has two wings placed one above the other."
    "It's still only partially painted,\nbut the fuselage would look good with a bright red."
    fn "「Cool! Can it fly? 」"
    
    show ta 002 with dis

    ta "「No, it's in the middle of repairs. So not yet. 」"
    "Now that he mentions it, it looks like there\nare a few holes in parts of the framework.{p}It'd crash if it tried to fly."

    show ta 001 with dis

    ta "「But still... 」"
    fn "「Yeah? 」"

    show ta 002 with dis

    ta "「Sometime, during the Summer,\n\ \ I'll complete and fly this thing.{p}\ \ If it works, I'll give you a ride too. 」"

    jump end10

##############################################
label end10:    
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
    jump day11
    
##############################################    
