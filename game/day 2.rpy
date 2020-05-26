##Day 2

screen shinhouse02:
    hbox:
        add "arrow left"
        at shinbounce1
    hbox:
        add "icon_shin"
        at shinbounce2
    hbox:
        text _("Shin's House")
        xalign .16 yalign .70
screen marketplace02:
    hbox:
        add "arrow down"
        at marketbounce1
    hbox:
        add "icon_kouno"
        at marketbounce2
    hbox:
        text _("Marketplace")
        xalign .5 yalign .52
screen ricefield02:
    hbox:
        add "arrow down"
        at ricebounce1
    hbox:
        add "icon_juu"
        at ricebounce2
    hbox:
        text _("Rice Fields")
        xalign .245 yalign .66
        
screen riverbed02:
    hbox:
        add "arrow down"
        at riverbounce1
    hbox:
        add "icon_kouya"
        add "icon_shun"
        spacing 5
        at riverbounce2
    hbox: 
        text _("River")
        xalign .625 yalign .7
screen tatsukihouse02:
    hbox:
        add "arrow right"
        at tatsukibounce1
    hbox:
        add "icon_tatsu"
        at tatsukibounce2
    hbox: 
        text _("Tatsuki's House")
        xalign .85 yalign .88
        
        
screen minasatomap02():
    add "map"
    add "mapdate"
    imagebutton idle "a icon" hover "icon loop" xpos 87 ypos 278  action Jump("shin02") hovered Show("shinhouse02")  unhovered Hide("shinhouse02") hover_sound "av/audio/click_008.wav"
    imagebutton idle "a icon" hover "icon loop"  xpos 372 ypos 249  action Jump("kounosuke02") hovered Show("marketplace02")  unhovered Hide("marketplace02") hover_sound "av/audio/click_008.wav"
    imagebutton idle "a icon" hover "icon loop"  xpos 197 ypos 325  action Jump("juuichi02") hovered Show("ricefield02")  unhovered Hide("ricefield02") hover_sound "av/audio/click_008.wav"
    imagebutton idle "a icon" hover "icon loop"  xpos 458 ypos 351  action Jump("river02") hovered Show("riverbed02")  unhovered Hide("riverbed02") hover_sound "av/audio/click_008.wav"
    imagebutton idle "a icon" hover "icon loop"  xpos 662 ypos 391  action Jump("tatsuki02") hovered Show("tatsukihouse02")  unhovered Hide("tatsukihouse02") hover_sound "av/audio/click_008.wav"
    hbox:
        text _("{size=+30}August 2")
        at maptime

#####################################################        
label day02:
    
    $ renpy.music.set_volume(1.0, 0.0, channel = "music")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound2")

    $ day = 2
    $ the_date = _("August 2")
    $ event_name  = _("８月２日")
    $ focus_character = ""
    
    window hide
    play music birds_chirping
    
    scene sky01 
    show text "{size=+130}August 2" at truecenter
    with Dissolve(.5)

    pause 3
    scene black with Dissolve(1)
    pause .4
    
    scene hbroom with wipe_corner
    pause .2
    fn "「What should I do today? 」"

    play music "<from 2.5>av/audio/free0422.ogg"
    call screen minasatomap02
    
####################################################### 
label shin02:
    
    $ focus_character = "shin"
    $ event_name = _("Old Memories and a Capricious Cat")
    
    scene map
    stop music
    hide screen shinhouse02
    scene path with Dissolve(1)
    play music tam_n06
    
    "Hmm, I've heard the talks,\nbut it's true nothing changed."
    "I just went out for a walk on a whim,\nbut I was really surprised\nto actually feel that."
    "I thought I'd forgotten the village's structure,\nbut as I walk I'm sure this connected\nto someplace, and there's a sidepath here."
    "I sure remember a lot..."
    
    scene shin_house_front with wipeleft
    
    "Over here, somewhat disconnected from\nthe village, out of place among\nthe Japanese-style houses,"
    "there was a Western-style home\nwith a pure white wall."
    
    play sound tm2_chime002
    pause 2
    
    who "「Yes, who might this be? 」"    
    fn "「Hello.{p}\ \ I'm a friend of Shin-kun's, {p}\ \ my name is [fn] [ln]. 」"
    who "「[ln]?{p}\ \ Oh! Please wait a moment... 」"    
    "......"
    
    play sound tm2_chair003
    pause .5
    show si 001 at center with dis
    
    fn "「Good afternoon, Shin-kun. 」"
    si "「Good afternoon.{p}\ \ So, what brings you here all of a sudden? 」"
    fn "「Uhh. 」"
    "Now that I've been asked,\nthe words just won't come out."
    "I was out on a walk\nwhen I noticed I had come here,"
    "then I just felt like seeing his face,\nso it wasn't anything really important."
    "Well this is a fix.{p}It would've been great if I had\nanything to talk about..."
    fn "「Uhh...{w=.3} I just came by unexpectedly\n\ \ and wanted to see you. 」"
    si "「... 」"
    
    show si 004 with dis
    pause .3
    
    "Well, that was expected.{p}Shin's embarrassed and shocked expression\npierced straight through me."
    si "「Yesterday and today,{w=.3} you really are an abrupt person."
    
    fn "「A-haha... 」"
    "Now I was just laughing politely.{p}I wonder, am I actually getting in the way\nof something by coming here so suddenly?"
    
    play sound cicada01 fadein .5
    pause 2
    show si 001 with dis
    
    si "「Well, since you're already here,\n\ \ would you like to come up? 」"
    fn "「Y-yeah.{p}\ \ Thanks for inviting me in. 」"
    "As I relaxed when Shin-kun's face relaxed,\nI entered his home."
    
    stop sound
    stop music fadeout 1
    scene black with sdis
    scene shin_house_den with sdis
    play music piano3_015
    show si 001 at center with dis
    
    si "「Make yourself at home. {p}\ \ I'll bring something back. 」"
    fn "「Oh, okay. Thanks. 」"
    
    hide si 
    show si 001 at offright
    with wipe_right
    
    "Hmm, even so, it's all as I expected."
    "I never thought about it much as a kid,\nbut this year even my impression\nof this house completely changed."
    "There was a nice feeling carpet on the\nsparkling clean floor, a nice cushy sofa,\nand what looks like a high class table."
    "At first glance it looked no different from any\nold home, but when you observe it for yourself,"
    "you can simply tell that\nnothing's a cheap low class article.{p}There wasn't a speck of dust on anything."
    "You couldn't sarcastically call it\nhigh class pricey stuff,\nit was all just simple and elegant."
    "Adding to that, the decorative plants added\nto the corners of the room help direct\nthe cozy atmosphere in here."
    "It isn't an exaggeration to say this\nwould be the best way to relax at home."
    "The air conditioner works really well too.{p}Even the air conditioning in Shin-kun's house\nis different, as expected."
    "As for what, it's something about the air.\nTo be specific...it's amazingly refreshing.\nIt isn't just because the temp's down low."

    show si 001 at offright
    show si at move_center(2)
    
    "As soon as I took one step in here,\nthat nice chilly sensation wrapped me up."
    "Viva air conditioning!{w} Viva the rich!{p}Here on this soft sofa, I could sleep\nthrough the whole summer!"
    
    stop music fadeout 1.5
    
    si "「{cps=5}. . . 」"
    
    show si 010 with dis
    
    si "「Well, you certainly are making\n\ \ yourself comfortable. 」"
    fn "「Uweh? 」"
    
    play music awkward fadein 1
    
    "Sometime while I was basking\nin the upper class atmosphere,\nShin-kun had come back."
    "In short, I was so absorbed in feeling the sofa\nthat I was slovenly laying across it,"
    "not minding that I was in someone else's\nhome when Shin-kun saw me."
    "Furthermore, my shirt got rumpled so much\nmy stomach was showing."
    "I reflexively sat straight up again,\nbut by that point it was already too late."
    "Shin-kun's shocked face was looking at me,\nand I was swallowed up by a deep despair."
    
    show si 003 with dis
    
    si "「I kind of admire that side of you.\n\ \ You could be a match for Kounosuke. 」"
    fn "「IESU-! I apologize, I'm sorry. 」"
    
    show si 001 with dis
    
    si "「Well I wouldn't go that far...{p}\ \ Is it that hot outside? 」"
    fn "「Yeah.{p}\ \ Didn't it break 30 C? 」"
    si "「It always gets hot here every year. 」"
    
    play sound tm2_stone001
    
    show si at bowing
    
    "As he said that,\nhe placed an ice tea in front of me."
    "It's such a little thing,\nbut Shin-kun looks like he fell\nout of a painting doing even that."
    
    show si 002 with dis
    
    si "「There's cookies too, so no need to hold back.\n\ \ Eat. 」"
    fn "「I'll take nine, please. 」"
    
    show si 001 with dis
    
    si "「? 」"
    "When I took a bite,\nI suddenly returned to my senses."
    "In Shin-kun's topicless eyes,\nI reached out for a cookie on the table."
    
    show si 004 with dis
    
    "After relaxing so carelessly\nin someone else's home,"
    "isn't it completely childish to stuff some\nsnacks placed right in front of me into my mouth?"
    "You might need a Mach number\nto estimate my stress value like this..."
    "After taking a bite and realizing my actions,\nI saw Shin-kun sitting on the other side,\nleaning over a glass."
    
    show si 001 with dis
    
    si "「No good? 」"
    fn "「Oh, not that. 」"
    "After carelessly meeting his eyes,\nShin-kun asked me."
    "In a panic, I shoved the rest of the\ncookie into my mouth then drained\nthe rest of my cold tea."
    fn "「...{w=.3}this cookie is awesome. 」"
    "My mouth just moved by itself.{w} Hey!? {p}My mind was struggling to keep my act clean,\nand it decides to do something stupid?"
    "Already I've done:{p}Impudent Childhood Friend{w} →Had Terrible Manners{p}→Been Narrow-minded Until I Saw His Face"
    "→Left for Mars,{p}and obviously headed nowhere in mind."
    "No, it's partly a joke, but isn't this a terrible\nimpression?{w} I played it cool just like always,\nthen timidly, turned my eyes up to him and..."
    
    show si 002 with dis
    
    si "「Really?{p}\ \ {nw}"
    stop music fadeout 1.5
    extend "If it suited your tastes, then that's good. 」"
    
    play music piano3_015
    
    "...{w=.3}huh?{p}I was so sure he'd be shocked and go\n\"You really are such a kid.\""
    
    show si 004 with dis
    
    "Shin-kun's face was calmer than expected,\nand for a moment he was smiling widely."
    "He turned away from my eyes,\nand took another sip of tea."
    fn "「Is it okay if I have another? 」"
    
    show si 001 with dis
    
    si "「Go ahead.{w} Just don't go over nine pieces\n\ \ like you said before. 」"
    "It was unusually awkward to be seriously replied\nto when joking, but what held my interest was\nless that and more the snacks in front of me."
    "An airy sweetness spread into my mouth when my\nteeth cut into them.{w} But one step later, the\ngentle aroma of cinnamon was left inside my mouth."
    "So I wanted that sweetness one more time,\nmore,{w=.3} and more,{w=.3}\nand before I knew it I was reaching out again."
    "Crap. These really are good.{w} Great as it is,\nthe taste isn't heavy so I could eat a lot more.{p}I could lick up the whole plate afterward."
    "I wonder where he got them?{w} There aren't many\nsweet shops here, so was it from Kazenari?{p}No, it's probably something he ordered."
    fn "「Were these possibly ordered and sent here? 」"
    
    show si 004 with dis
    
    si "「Mm, well. 」"
    "Shin-kun bit into the cookie in his hand.{p}So picturesque."
    
    show si 001 with dis
    
    si "「Mom has always been particular\n\ \ about the black tea... 」"
    fn "「No, I meant about the cookies. 」"
    si "「Eh? 」"
    
    show si 002 with dis
    
    si "「What do you think? 」"
    
    menu:
        "A. So it is an import?":
            jump shin02_an_import
        "B. Something actually cheap and nearby?":
            jump shin02_actually_cheap
        "C. Could it be... Handmade?":
            jump shin02_something_handmade
        
        
########################################
label shin02_an_import:
    $ love_shin -= 1
    fn "「I guess, something authentically high class? 」"
    
    show si 001 with dis
    
    si "「Eh? 」"
    
    show si 003 with dis
    
    si "「Well... {w=.5}you're wrong. 」"
    fn "「But it must be from some famous store,\n\ \ isn't it? 」"
    si "「Don't exagerrate so much\n\ \ about a drop cookie... 」"
    
    show si 001 with dis
    
    jump shin02_amaki_recipe
   
########################################    
label shin02_actually_cheap:
    fn "「Um, is it from a new sweets shop in Kazenari? 」"
    si "「No point for you. 」"
    "Shin-kun giggled like a little kid.{w} It's\nthe first time I've seen him laugh like this...{p}Crap, I'm getting kind of excited by this."
    
    jump shin02_amaki_recipe
    
########################################
label shin02_something_handmade:
    $ love_shin += 1
    
    fn "「Could it be... handmade? 」"
    
    show si 001 with dis
    
    si "「Yeah, you could tell? 」"
    fn "「What? Really? 」"
    
    show si 002 with dis
    
    si "「I baked them just this morning. 」"
    
    jump shin02_amaki_recipe
    
#####################################
label shin02_amaki_recipe:
    si "「It's Amaki's recipe. 」"
    fn "「Amaki-san?{w} So wait, {w=.3}a servant's? 」"
    
    show si 001 with dis
    
    si "「Yes.{w} Do you remember? 」"
    fn "「Kind of. 」"
    "I reached for another cookie as\nI mumbled in confirmation."
    fn "「That reminds me, didn't I used\n\ \ to come here a lot for Amaki's treats as a kid? 」"
    
    show si 004 with dis
    
    si "「That's true.{p}\ \ It wasn't just you though,\n\ \ Kounosuke kept asking me stubbornly. 」"
    fn "「I remember that.{p}\ \ 'Will there be treats tomorrow?'{p}\ \ 'When can I come over?'{w=.3} Like that. 」"
    
    show si 003 with dis
    
    si "「Yes, just like that. 」"
    "He'd follow Shin-kun around with ulterior\nmotives, and got a good scolding from his\nparents when they found out."
    "Amaki-san smiled through it all,\nbut they apologized so much."
    "So,{w=.3} for a while we all\nrestrained ourselves when coming over here."
    "At that point, Shin-kun hadn't really fit\nin yet, so he was sort of cut off by himself\neven at school."
    fn "「\'The Mansion Exploration Tour,\' huh...{p}\ \ That brings back memories. 」"
    
    show si 001 with dis
    
    si "「Mansion exploration...? 」"
    fn "「Come on, don't you remember?{w} The first time\n\ \ Torahiko, Kounosuke, and I came here.{p}\ \ Back then,{w=.3} when we were just classmates. 」"
    
    show si 004 with dis
    
    si "「Oh. {w=.3}\n\ \ You really do remember a lot. 」"
    fn "「After all,\n\ \ if you think about it wasn't that the beginning? 」"
    
    show si 001 with dis
    
    si "「I...suppose so? 」"
    fn "「You cried so much then, Shin-kun. 」"
    
    show si 010 with dis
    
    si "「...you certainly do remember a lot. 」"
    "Looking back, that incident really was the\nbeginning of our relationship with Shin-kun."
    
    $ event_name = _("Exploring the Mansion")
    
    stop music fadeout 2
    scene black with Dissolve(1)
    scene school01 with Dissolve(1)
    play music free0213
    
    "In those days, Shin-kun was the newest person\nin our school, and there was no one\nhe could call a friend."
    "There were times someone transferred\nand there was no room, but somehow"
    "there was an approachable mood around him,\nand he fit in well enough."
    "We could figure it out later on,\nbut at the time Shin-kun's\nlooks was the source of it."
    "He was half-foreigner.{w} As a human, even\nnow I can't really tell all that well, but\nbeastmen could easily tell from looking at him."
    "So naturally everyone put Shin-kun a bit aways,\nI picked up on that,\nand somehow felt like getting closer."
    "The one who zeroed in on that isolation\nwas Kounosuke."
    ko "「Hey Shin, do you know where you live? 」"
    "I clearly remember that joyful form\ntalking with him."
    
    scene shin_house_front with Dissolve(1)
    
    "At the time, we were entering into the\nWestern-style house that left\non the outskirts of the village."
    "The building was clearly different from the rest\nin the village, which made it so suitable to our\nchildish adventure-seeking hearts."
    "If it was a vacant house,\nwe would have absolutely\nmade it our secret base."
    "But there were residents there,\nand the adults would strictly tell us\n\"Don't make a mess!\""
    "In order for us to boldly walk in,\nour reason was Shin-kun."
    "We used the fact he was our classmate\nso we could look around that house."
    "That was the hope of us Three Stooges,{p}Torahiko,{w} Kounosuke,{w} and my resolve,"
    "but it was Kounosuke\nwho suggested the \"Mansion Exploration Tour.\""
    
    scene shin_bedroom with Dissolve(1)
    
    "We never really talked that much about it,\nbut the three of us walked in all of a sudden,\nand Shin-kun looked so worried."
    "We were children, so we didn't have any\nreservations about playing on the bed,\nand we messed up every room we ran into"
    
    stop music fadeout 1.5
    
    "And then, that's when it happened.{p}It started when I picked up a little\nornamental black cat from the end of the shelves."
    
    play music free44
    
    fn "「Shin-kun, what is this? 」"
    si "「Ah! Don't touch that! 」"
    to "「Oh? What's that? 」"
    
    play sound open00
    
    "Torahiko was surprised from Shin-kun's\nloud voice, then came over to pick up\nthe black cat from my hand."
    play sound swing30
    si "「Give that back!{w=.3}  "
    play sound swing30
    extend "Give it back! 」{w=.3}"
    
    
    "Shin-kun tried to reclaim it, but with the height\ndifference he couldn't reach even when he jumped.{p}Even so, he desperately tried to get it back."
    "There wasn't any ill intent behind it,\nbut I just sat back and watched those two."
    to "「Ha ha. 」"
    play sound swing30
    si "「Give it back!{w=.3} "
    play sound swing30
    extend "I said give it back!{w=.3} "
    play sound swing30
    extend "GIVE IT! 」"
    
    
    "It was funny seeing the normally stoic\ntransfer student showing some emotion.{p}And then..."
    to "「Kounosuke, catch! 」"
    
    play sound swing40
    
    ko "「Hm? What? 」"
    
    play sound step06
    
    fn "「Ah-! 」"
    
    pause 1
    play sound metalhit000
    play sound metalhit002
    stop music
    
    "The ornament Torahiko threw hit\nKounosuke's head, then bounced out\nthe second story window."
    ko "「Oh man, Torahiko~ 」"
    to "「I-{w=.3}It's your fault for not catching it! 」"
    ko "「How could I ever catch that? 」"
    si "「... 」"
    "We all overdid it, and we quickly\nlooked at Shin-kun.{p}He said nothing as his shoulders quaked"
    fn "「Shin-kun...? 」"
    "At the same time I called out to him,\na large tear fell out of those big eyes."
    
    play music melodious08
    
    "We tried to calm him down however we could,\nbut nothing we said to him had any effect."
    
    scene shin_house_den with Dissolve(1)
    
    "After that, Amaki-san brought us all together\ninto the living room.{w} By then Shin-kun\nstopped crying,{w=.3} but he still said nothing."
    "The unbearable, awkward\nsilence for children continued,{w=.3}\nand as we trembled in fear of the biggest"
    "scolding of our lives,{w=.3}\nthere was some sweets in front of us."
    "We all ate them in bewilderment together with\nShin-kun, and while a bit of it was burned,\nit was really sweet and delicious."
    "We apologized again afterwards, but as\nShin-kun only said {w=.3}\"I don't care anymore,\"{w=.3}\nwe weren't sure he really forgave us."
    "We all felt uncomfortable,\nso after that we all went home.{p}Even so, we were in the wrong."
    
    scene shin_house_front with Dissolve(1)
    
    am "「Come again. 」"
    "That gentle adult voice that called out to us\nas we left was the biggest forgiveness for us,"
    "so that's why{w=.3} we all felt\nas though we did something horrible."
    
    stop music fadeout 1.5
    
    scene school01 red with Dissolve(1)
    play music free0258
    
    "So after that apology, it was strained at first,\nbut we started being able to talk to one another."
    "If we had just talked to him,\nnone of it would have happened."
    "He was the \"mysterious gloomy guy,\" but we\nwere children who didn't change anything."
    "Before we realized,\nthat invisible wall we felt between us\nand Shin-kun{w=.5} disappeared."
    "There are parts we can't really understand,\nbut he wasn't a bad guy.{p}We all understood that."
    "And so, we all became friends."
    
    $ event_name = _("Time passes by quickly")
    
    scene shin_house_den red
    show si 003 red at center
    with Dissolve(1)
    
    fn "「D-do you remember?{w=.3}That one time we went to the river. 」"
    si "「Why do you remember only those things...? 」"
    fn "「Well, because I can't forget them. 」"
    
    show si 010 red with dis
    
    si "「My fear of water is 80\% your's\n\ \ and Torahiko's fault. 」"
    fn "「Huh?{w} Me too!? 」"
    
    show si 004 red with dis
    
    si "「You'd always sit back and watch quietly.{p}\ \ Same thing. 」"
    fn "「Come on... 」"
    
    play sound fantasy_004
    pause 1
    
    "Just when we reached a good stopping point,\nthe clock rung."
    "We looked over as if to fish something out,\nand the hand was much further\nalong than I expected."
    
    show si 001 red with dis
    
    si "「It's that time already? 」"
    fn "「What?{w} Seriously? 」"
    "Before I realized it,\nthere was no more tea or snacks left."
    "We really have been reminiscing\nlonger than I thought."
    si "「Now seems like a good place\n\ \ to stop for the day. 」"
    fn "「Yeah,{w=.3} I have to get back soon. 」"
    
    scene black with Dissolve(1)
    
    scene shin_house_front red
    show si 001 red at center
    with sdis
    
    fn "「Well see you later,{w=.3} Shin-kun. 」"
    si "「Later. 」"
    fn "「Can I come over again? 」"
    si "「Of course... 」"
    
    show si 002 red with dis
    
    si "「...not.{w} How does that feel? 」"
    fn "「Huh!? 」"
    si "「I'm kidding.{p}\ \ {nw}"
    show si 001 red with dis
    extend "I can't do any grand entertainments,\n\ \ but come over whenever you like. 」"
    
    fn "「Ah, okay... 」"
    
    show si 002 red with dis
    
    si "「Well then,{w=.3} take care on your way back. 」" 
    fn "「See you later. 」"
    
    scene black with Dissolve(1)    
    scene path red with Dissolve(1)
    
    "Shin-kun hasn't changed much over these 5 years.{p}I mean that in a good way.{p}He feels a lot more gentler than I remember."
    "As I walked back on the sunset-dyed road,\nI kept thinking about that."
    
    jump end02
     
##############################################
label kounosuke02:
    
    $ event_name = _("At the bookstore")
    $ focus_character = "kounosuke"
    scene map
    hide screen marketplace02
    stop music fadeout 1.5
    scene black with wipe_dr 
    pause .3
    scene market with wipeleft
    play music cicada01
    
    "While walking downtown, {p}passing by the stores and houses on the street, {p}makes me feel very nostalgic."
    "It's no different than it was 5 years ago."
    "No, it's changed a little, {p}mainly the construction of stores on the streets."
    "But the atmosphere of Minasato, {p}is no different than it was in my memory."
    "The only thing that looks different, {p}is the height-level from which I'm viewing things, {p}compared to when I was little."
    "It seems like there are less children... {p}running around on the streets than there used to be. {p}The population must be declining."
    "The amount of people leaving Minasato, {p}to go to the city seems to be increasing every year. {p}I too did that to myself."
    "I don't think this village is going to disappear, {p}but the way the bustling streets of Minasato, {p}from my memory have become so empty..."
    "makes me feel just a little sadness in my heart."
    
    stop music fadeout 2
    scene black with wipeleft
    pause .2
    scene bookstore with wipeleft
    play music shop01
    
    fn "「Whew. 」"
    "As soon as I enter the store, {p}I feel the temperature suddenly drop."
    "The air is cooler and comfortable. {p}Correction. The air conditioning might...  {p}be a little too cold."
    "But compared to the scorching hell outside, {p}this is heaven on Earth."
    "I lightly air out my shirt, {p}it had become sticky with sweat."
    "Hmm. {p}Long live the power of science?"
    "While looking around in the small store, {p}I find what I'm looking for in the corner. {p}Wait, it's old."
    "Even in a rural area like this, {p}the weekly publications are neatly stocked. {p}The problem is... they're all last week's issue."
    "While recieving a bit of culture shock, {p}I think about returning home, {p}but decide not to because of the damned hot weather."
    "For now I'll just kill some time by browsing."
    "The assortment is like the size of the store. {p}Smaller."
    "All the weekly magazines that I usually read, {p}are from last week."
    "There are no new publications."
    "I toss away an old magazine, {p}that looks like it's from the past decade."
    "Reluctantly, I pick up one that has more... {p}questionable content, {p}and I skim through it halfheartedly."
    "...Huh. {p}This is surprisingly interesting."
    "Should I subscribe to it now? {p}No, that would hurt my wallet... {p}Maybe I should buy it when it comes out as a book."
    
    play sound closebook
    pause .5
    
    "I close the magazine and put it back where it was. {p}Looking at the clock in the store, {p}I see that 30 minutes haven't even passed yet."
    "I guess I'll browse a little more."
    "While looking for my next catch, {p}I see a familiar figure in the corner of my eye."
    
    show ko 001 at center with dis
    
    "I turn my face to the side, {p}and see that it's Kounosuke."
    "I wonder when he got here. {p}Or maybe he's been here the whole time?"
    "I mean, Kounosuke's the one who usually... {p}finds me in public like that."
    "With a magazine in one hand, {p}he reads an article, {p}completely glued to the spot."
    "I lightly wave my hand to the side, {p}but he shows no signs of noticing."
    "Oh, this reminds me, {p}when Kounosuke's engrossed like that, {p}he completely shuts out everything around him."
    "It's something he's known for."
    fn "「Kounosu- 」"
    "I try to approach and greet him, {p}but at almost exactly the same time,"
    "he raises face up from his magazine, {p}and passes right by me."
    
    hide ko with wipe_right
    
    fn "「Ke, ah... 」{w} {nw}"  
    play sound register
    extend "{w=2.5}{nw}"
    
    clerk "「Thank you very much. 」"
    "Without stopping, {p}Kounosuke buys his magazine and leaves the store. {p}The clerk's dull voice is left in the store."
    "I couldn't get him to notice me at all... {p}While being thoroughly ignored, {p}my eyes meet with the clerk's."
    "I hurriedly turn back to the magazine corner. {p}Come to think of it, what did Kounosuke buy? {p}It looked like he was really into it."
    "Just out of plain curiousity, {p}I move to the corner where Kounosuke was. {p}After randomly looking around the shelves, I find it."
    
    stop music fadeout 4
    
    "I found it. I've found it. {p}Just next to the magazine corner, {p}left there messily,"
    "is the erotic book shelf."
    "『F-Men Mixture of Different Species Battle 』"
    "No way, there's no way this is... {p}But no matter how many times I re-read the title, {p}it's always the same."
    
    play music shop03
    
    "This is THE beastmen's ultimate gay book... {p}There are numerous pages and, {p}it's almost twice as thick as the one next to it."
    "It's such an extreme representation of a niche genre. {p}This was the last the editing company sent out, {p}before it shut down forever."
    "It's an \"everything I want crammed into one\", {p}erotic book, {p}and it's not so easy to get your hands on it, either."
    "Every once in a while it shows up on a net auction, {p}for a ridiculous price however. {p}So what's it doing in a country bookstore like this?"
    "With trembling fingers, {p}I pull it from the shelf."
    "There's no doubting the intended genre, {p}just from the front cover."
    "And its contents, {p}well you might say its contents are..."
    
    play sound dream
    show bubbles with circle_out
    
    "{size=+15}ARCADIA."
    
    hide bubbles
    stop sound
    
    "Taken aback, I look around the store. {p}There's the store clerk and me, just two people. {p}In other words, I'm the only customer."
    "This kind of situation...! {p}There's no doubt. {p}I need God's guidance!{w} {nw}"    
    play sound register
    extend "{w=2.5}{nw}"
    
    clerk "「Thank you very much. 」"
    
    show market with wipe_right
    
    "This volume is way to big to read it, {p}all while standing in the store."
    "And it's full of... such juicy content. {p}There's no way I would do such a wasteful thing."
    "Thanks to this unexpected bounty, {p}my nights won't be lonely for a while."
    
    scene sky with qdis
    
    "Thank you, Kounosuke!"
    
    $ kouno_magazine = True
    
    stop music fadeout 2
    window hide
    show day_logo2 with Dissolve(.5)
    pause .5
    show day_logo with dis
    pause 1
    
    scene magazine
    show day_logo
    with Dissolve(2)
    pause 3
    scene black with Dissolve(2)
    pause 1

    jump day03
    
#############################################    
label river02:
    
    $ event_name = _("Let's Cool Off at the Riverbed")
    $ focus_character = "kouya"
    
    scene map
    stop music
    hide screen riverbed02  
    scene hbroom with dis
    play music cicada01
    
    fn "「It's so hot...! 」"
    "I don't really get why, but it's seriously hot.{p}When I look outside, the air looks all distorted."
    "It's called a heat haze,\nbut my head's feeling kind of weird,\nso I'm not too sure about that."
    "It's been like this all morning:{p}A deep blue sky. Brilliantly pouring sunlight.{p}The cicadas are calling loudly enough to hurt my ears."
    fn "「So... damn... hot! 」"
    "I don't know for sure, but everywhere else is hot.{p}The temperature feels like it's rising quickly,\nso I don't bother to look at the thermometer."
    fn "「Hnngh... 」"
    "I writhe in absolute misery as I groan."
    "When did Minasato feel like such a tropical zone?{p}It at least felt better before I moved away...!"
    "Maybe it's that \"{cps=10}global warming{cps=40}\" thing,{p}or that \"{cps=10}greenhouse effect{cps=40}\" stuff."
    fn "「Yeah, those fads didn't need to continue... 」"
    "Complaining wasn't going to drop the temperature.{p}But instead, it felt like it was doing the opposite,{p}I shouldn't really cry over it though..."
    "Ahhhhhh!"
    "Gah, this town is trying to kill me!{p}Either I'll get dehydrated or I'll go crazy..."
    "I'm at my breaking point right about now,{p}and if I don't get to somewhere that's cool soon..."
    
    scene black with Dissolve(1)
    stop music
    pause .5
    play music water03
    scene river with wipe_right
    
    fn "「Well, once you put it like that...{p}\ \ there's no place better than right here... 」"
    "Here I am, out at the river bed."
    fn "「Ahh... this is great...! 」"
    "Somehow I feel like...{p}just having water around makes me cooler."
    "What the hell am I doing standing around!?{p}I am definitely cooling off, no doubt about it!"
    "Goodbye to the hot and hello to the cool!{p}Screw you, Mother Nature!"
    "Ahh, that was close...{p}I was almost overcome by that...{p}\'global warming\' conspiracy crap."
    fn "「I bet taking a dip will cool me down... 」"
    "Even then, it'd probably take three hours,{p}before I actually cooled down.{p}I can tough it out until then."
    "The green grass covered the hill as I walked down,{p}and I drew closer to the sound of the running river."
    "The familiar hush of running water...{p}it gave me a feeling of nostalgia."
    who "「Hmm? [fn]-san? 」"
    "All of a sudden, I hear a voice call out my name.{p}Instinctively, I look for the source."
    
    show ka 001 at midleft
    show su 001 at midright
    with dis
    
    show su 002 with dis
    
    su "「Hey, it is you!{w} Hi, [fn]-san! 」"
    
    show ka 003 with dis
    
    ka "「Yo, [fn]. 」"
    fn "「Well, look who it is.{p}\ \ What are you guys here for? 」"
    
    show su 004 with dis
    
    su "「Uuu. We couldn't take the heat,\n\ \ so we came here to cool off a little. 」"
    "If I had looked earlier,\n\ \ I'd have seen them already in the water."
    
    show ka 001 with dis
    
    ka "「Heh, what about you, [fn]? 」"    
    fn "「Eh, it's the same for me.{p}\ \ I came out here to protect myself,\n\ \ from the horrors of global warming. 」"
    
    show ka 003 with dis
    
    ka "「The hell is that? 」"
    "Kouya smiled as he said that."
    su "「But today is even hotter than usual.{p}\ \ Isn't this the hottest it'll be all summer?{p}\ \ {cps=10}The highest temperature was...{nw}"
    play sound swing40
    hide su
    show su 005 big shiver at center_bottom
    with dis
    extend " 」"
    
    fn "{cps=0}「Waaah! Don't say it! 」"
    
    show ka 005 with dis
    
    "Shun-kun's confused mouth was tightly held down."
    fn "「You can't say the temperature, man!{p}\ \ If you do, the devil will jump into your body,{p}\ \ and he'll change your body temperature! 」"
    fn "「It's a forbidden spell!{p}\ \ He'll make it so that you'll never cool down! 」"
    su "「Mgh, mghhh! 」"
    
    show ka 001 with dis
    
    ka "「[fn]. 」"
    fn "「W-what, Kouya? 」"
    
    show ka 005 with dis
    
    ka "「With the way you're holding him,\n\ \ he won't be able to breathe. 」"
    "He says that with a shocked face.{p}I look at my hands."
    "My arms are wrapped around Shun-kun's muzzle,{p}with both my hands clasped around his mouth.{p}That was pretty brutal, even for me."
    "Rather than saying I was holding him down,{p}it'd be more accurate to say\nthat I was pinning him beneath me."
    fn "「Wah! S-sorry, Shun-kun! 」"
    "I let go of the panicking wolf."
    
    show su 003 at midright with dis
    
    su "「Bwah!{w} You're so mean, [fn]-san... 」"
    "The teary look in Shun-kun's eyes shoot through me.{p}The cicadas couldn't compare to this...{w=.3} it hurt."
    fn "「I-I'm sorry! I wasn't paying attention... 」"
    
    show ka 001 with dis
    
    ka "「Seriously, bro? You were overdoing it... 」"
    "Both of their saddened gazes pierce through me.{p}It feels like I've been stabbed."
    "...Why does this have to be so awkward?"
    fn "「N-not really...{w=.3} I mean... Uhh...{p}\ \ Even if hearing about the temperature\n\ \ doesn't actually make things hotter... 」"
    fn "「I think... It'd make things feel like that.{p}\ \ R-right? 」"
    "I make an attempt to fix the situation quickly."
    fn "「I was trying to avoid the topic...{p}\ \ but I guess I got a little too worked up about it.{p}\ \ That's what I'm saying... 」"
    "The explanation doesn't seem to better the situation.{p}Their cold looks seem to strengthen."
    "That seems to be the only thing\ncooling me down right now.{p}Crap, I'm breaking out into a cold sweat."
    fn "「Ugh... Yes... This was all my fault.{p}\ \ I-I'm sorry...! 」"
    
    show ka 005 with dis
    
    ka "「Uhh... what? 」"
    "He stares at me like I'm some kind of alien.{p}Those eyes of his are telling me I've gone overboard."
    "I think so too..."
    
    show ka 001
    show su 002
    with dis
    
    su "「Oh well, let's cool down all together! 」"
    "Shun-kun called out to me in his usual self.{p}This time, I'm tearing up from the kindness."
    "Oh, friendship, it's such a miracle..."
    "I accept the offer, and into the water I go.{p}{nw}"
    play sound mizu07 
    extend "A cool feeling spreads from my legs up to my body.{p}Exactly what I've been looking for all day..."
    "And then, somehow, I feel at peace."
    fn "「Hey, now that I think about it,{p}\ \ you guys didn't hang out a lot before.{p}\ \ How did you guys get to be such good friends? 」"
    "I voice the thought in my head out loud."
    "As far as I can remember,{p}Shun and Kouya weren't this close."
    "But when Kouya can even understand,{p}Shun's muffled words, that's the feeling I get."
    "When I was gone,{p}was there some kind of event\nthat brought them closer together?"
    
    show ka 002 with dis
    
    ka "「Ehh, it's complicated, I can't really explain it.{p}\ \ Shun knows more about it than I do...{p}\ \ B-but it's not like we came here together... 」"
    
    show ka 003 with dis
    
    ka "「U-uhh... right? 」"
    "Kouya nudges Shun for a response."
    
    show su 004 with dis
    
    su "「Th-that's true!{w} I do remember something but...\n\ \ the reason why we're so close{cps=10}...\n\ \ {nw}"
    show su 022 with dis
    extend "{cps=40}I don't really get it... 」"
    
    "Shun-kun blushes a bit as he says that."
    "But...{w=.3} Why is he blushing?"
    
    show ka 001 with dis
    
    ka "「Welp, that's the story for today. 」"
    fn "「Hmm, is that so? 」"
    
    show ka 005 with dis
    
    ka "「Yeah, it is. 」"
    
    play sound bosu34
    hide ka with wipe_down
    
    "After he finished speaking,{p}Kouya crashes into the water, with his backside up."
    "Shun-kun and I exchange glances,{p}and then, with smiles on our faces, follow suit."
    
    play sound bosu34
    scene sky with wipe_down
    
    "The world above spread out in front of my eyes.{p}A piercing blue sky, with soft looking clouds."
    "The murmur of the river, the sound of the wind,{p}and the voices of the insects and birds.{p}They all harmonized into a natural anthem."
    "It was impossible to find this kind of serenity in\nthe crowded city. It was like I was in another world.{p}This was what I missed about the country."
    "The three of us lay there in silence,{p}but it didn't feel strange or awkward."
    "Instead..."
    fn "「Maaan... this is great... 」"
    "I murmur quietly."
    "Being away from nature so long...{p}for me especially, this was refreshing."
    ka "「Can't get this where you live, eh, City-Boy? 」"
    "Kouya spoke as though he could read my mind."
    ka "「But don't you think this is awesome too? 」"
    "With a wry smile, I could sense him silently agreeing."
    fn "「Yeah... it really is... 」"
    "I honestly concur."
    "Next to me, Shun-kun nods his head."
    "I'm having a lot of fun being back here again,{p}but something like this... taking in the nature...{p}it's a different kind of enjoyment."
    "But no matter what kind of experience it is,{p}it's always enjoyable."
    "Maybe everyone else feels the same."
    ka "「Oh yeah, not long ago there was a time...{p}\ \ when Shun got pulled in by the river. 」"
    su "「Oh yeah! I remember that... 」"
    "When Kouya spoke all of a sudden, Shun-kun agreed."
    fn "「Eh? Something like that happened? 」"
    ka "「Hey hey, did you forget? 」"
    "For the millionth time today, Kouya spoke in shock.{p}His face is probably all surprised too."
    fn "「Uhh, when did that happen? 」"
    su "「When I was about five or maybe four. 」"
    "So when Shun-kun was five or four,{p}then it'd be when I was six?"
    fn "「Ehh... Umm... Uhh... 」"
    
    menu:
        "A. Oh, I remember!":
            jump river02_can_remember
        "B. Hmm, I can't remember...":
            jump river02_cannot_remember
        "C. Oh, is it time for a rescue story?":
            jump river02_story_time

    #########################################        
    label river02_can_remember:
        
        $ event_name = _("Oh, I remember!")
        $ love_shun += 1
        $ love_kouya += 1
        
        fn "「Oh, I remember! 」"
        
        play sound bosu34
        
        scene river
        show ka 001 at midleft
        show su 001 at midright
        with wipe_up
        
        "My voice came out of me with great force.{p}and Kouya and Shun both sat up to look at me."
        ka "「And by 'Oh, I remember,' you mean 'Oh, I forgot.' 」"
        "Kouya emulates the tone of my voice mockingly."
        
        show su 004 with dis
        
        su "「Uuu, it's sad that you forgot... 」"
        fn "「Err, I remember it! Don't be so harsh, guys... 」"
        "Didn't those two only just remember it?{p}They forgot about it too!"
        "I thought about it, but I didn't say anything.\nAt least I'm a bit mature about it..."
        
        show ka 005 with dis
        
        ka "「Yeah, yeah, whatever. You still hurt my feelings.{p}\ \ It was a really important moment for me,{p}\ \ but for you, it was probably just Tuesday. 」"
        su "「What a shock... 」"
        "Urrgh, it feels like I'm being bullied..."
        
        show ka 001 with dis
        
        ka "「Well, like [fn] said,{p}\ \ we should give him some slack for just remembering.{p}\ \ Although I'd be pissed if he actually forgot. 」"
        
        show su 001 with dis
        
        su "「That's true. I think so too! 」"
        fn "「{cps=10}. . . 」"
        "I guess it's okay...{w} It seems like\nthe two of them are just teasing me."
        "They're not taking it seriously,{p}that much I can understand."
        "But damn, if they're so happy I remembered,{p}they could just say so.{p}Damn you guys, shrinking violets..."
        
        show ka 005 with dis
        
        ka "「What's up, bro? Thinking about something? 」"
        fn "「Eh!? N-no! That's not true at all! 」"
        
        show ka 009 with dis
        
        ka "「...Whatever floats your boat, man. 」"
        "For some reason, Kouya's annoyingly sharp today.{p}If I think about things too carelessly,{p}I might accidentally let it slip out."
        "Kouya... you're mean."
        
        show su 004 with dis
        
        su "「Even so, that time was really surprising! 」"
        "That time?"
        "...Oh, that time when Shun got pulled into the river.{p}Yeah, that's right. That's what we were talking about."
        "All right, it's time to focus,{p}and to see if I can really recall it!"
        "Now, {cps=10}that was..."
        
        jump river02_memory
        
    #########################################    
    label river02_cannot_remember:
        
        $ event_name = _("Hmm, I can't remember")
        $ love_shun -= 1
        $ love_kouya -= 1
        
        play sound bosu34
        
        scene river
        show ka 001 at midleft
        show su 001 at midright
        with wipe_up
        
        fn "「Sorry, I can't remember... 」"
        
        show su 004 with dis
        
        su "「But, nooo... 」"
        "Shun-kun was disappointed, and I could see."
        "Pangs of heartbreak assail me\n\ \ as I see that expression of his."
        fn "「Eh, ah... 」"
        "I'll try to remember that time again..."
        fn "「Uh, um... 」"
        "I don't think I've ever tried so hard...{p}tor remember something before..."
        "Wait, no. And maybe not even after this.{p}But still, I can't really recall the situation."
        fn "「Ooohhh...! 」"
        "I've come to the conclusion\nthat I really can't remember."
        fn "「...Sorry, I can't remember it after all. 」"
        "I try to speak with an innocent smile in my face."
        
        show ka 005 with dis
        
        ka "「... 」"
        su "「... 」"
        "Oh, I can't get this past them, can I?"
        fn "「Well, hahahaha... cut me some slack, guys... 」"
        
        show ka 001 with dis
        
        ka "「Welp, can't be helped I guess...{p}\ \ Sucks that you can't remember, though.{p}\ \ You haven't been around for a while, anyway. 」"
        
        show su 001 with dis
        
        fn "「Thanks for understanding{p}\ \ Maybe I could remember, if I had a more...{p}\ \ Specific hint to go off... 」"
        "I mean, Shun-kun got pulled away right?{p}I mean, come on. It's not that easy to forget\nsomething like that, is it? He almost drowned. 」"
        
        "But...{w=.3} no...{w=.3} I still forgot about it...{p}I should be able to remember."
        
        show su 004 with dis
        
        su "「That's true, I said it earlier, but...{p}\ \ I was about four or five. Everyone else was... 」"
        "Shun-kun let's out a puzzled 'hmm'\nas he tried to recall it as well."
        "But he was really young when it happened.{p}I'd be surprised if he could remember it clearly.{p}Or at all, for that matter."
        su "「It was... around there! 」"
        
        show ka 003 with dis
        
        ka "「It was on a day that was hot like this.{p}\ \ Then, that's right... During last year's festival.{p}\ \ Torahiko was panicking about a ghost or something... 」"
        fn "「Torahiko? 」"
        "Torahiko. Ghost."
        "Hmm. Maybe, that could be a keyword..."
        "No... It would be of no use.{p}Who knows how many situations could involve\nTorahiko and ghosts.{w} It could just..."
        fn "「...Oh. 」"
        
        show ka 009 with dis
        
        ka "「Did you remember? 」"
        fn "「...Yeah...{w=.3} Sorta. 」"
        "You never know what can stir up a memory,{p}especially in these times. Right?"
        "Yeah... it was..."
        
        jump river02_memory
      
    #########################################    
    label river02_story_time:
        
        $ event_name = _("Calling, Somewhere from Within")
        
        fn "「Oh, is it time for a rescue story?{p}\ \ Like, you know, the one with the river god. 」"
        
        play sound bosu34
        
        scene river
        show ka 001 at midleft
        show su 001 at midright
        with wipe_up
        
        stop music fadeout 5
        
        "Right, I'm sure it's that story.{p}I'm definitely sure about it."
        
        show ka 005 with dis
        
        ka "「...? 」"
        
        show su 015 with dis
        
        su "「...? 」"
        
        play music oo39_cho_ys001
        
        "Hey, I can see a question mark over their heads.{p}Huh, did I really say something that weird?"
        
        show ka 001 with dis
        
        ka "「[fn]... not to sound rude...{p}\ \ but what the hell are you talking about? 」"
        "What the hell did I blurt out!?{p}No, wait, calm down, there's no way that could be it!{p}Chill out, [fn] [ln]!"
        fn "「What? No, I mean, isn't it the story,{p}\ \ where Shun-kun almost got swept away by the river... 」"
        fn "「And then we saw a dragon-like river god\n\ \ save him when he went under the water... 」"
        "And then after that, he got lost\nwith his parents in a strange world."
        "But then, he fell into some trap,{p}and got caught in this huge crisis."
        "Eventually, though, he got out,{p}because everyone came together to help pull him out."
        "Yes, I'm sure that happened!{p}But Kouya and Shun-kun...{p}are making really puzzled faces at me."
        fn "「Huh, did I say something weird again?{p}\ \ Uh... was I wrong...? 」"
        
        show ka 005 with dis
        
        ka "「[fn]... 」"
        
        show su 010 with dis
        
        su "「[fn]-san... 」"
        "They look at me like I'm something pitiful."
        fn "「W-what?{w} What's up with you guys, seriously...{p}\ \ S-stop looking at me like that!{p}\ \ {nw}"
        show river at vshake
        play sound freeze04
        extend "Seriously, cut it out, guys! 」"
        
        play music tam_n06 fadein 2
        show ka 001 with dis
        
        ka "「...That time was a big surprise, Shun. 」"
        
        show su 002 with dis
        
        su "「...It really was.{p}\ \ I was wondering what was going to happen to me,{p}\ \ and I got really scared, and I felt hopeless. 」"
        "What? Are they talking about something\nthat happened when I wasn't even around?"
        "Isn't that funny?{p}And the BGM came back before I realized too."
        
        "What is this? Hey, wait...{p}Awful, awful alienation!{p}Is this what it feels like to be bullied!?"
        "Tch, if that's how it is, then...{p}I'll get back at you with a comeback!{p}And it'll be smooth!"
        "I'll search for that memory with all my body and soul.{p}I'll definitely be able to find it. That one memory!"
        
        show river at shivering
        play music loop04 
        play sound don17 loop
        
        fn "「{size=+15}{cps=5}Oooooooaaaaaagh 」!{nw}"
        show river at still
        extend ""
        "The signals run through my brain.{p}Like a computer,{w} I make a frantic search\nthrough the database of my mind."
        "Now, with all my power... {cps=10}raaagh!"
        fn "「{cps=10}...{nw}"
        stop sound
        play sound freeze07
        extend "! 」"
        
        play music tam_n06 fadein 2
        
        "I see! I see it!{p}It was in the 53rd cycle!"
        fn "「That time really was a huge shock. 」"
        "All right, I've got it now, right!?{p}If I get on this current,{p}I can get back into the conversation."
        "Okay, [fn]. Don't screw this up again."
        "...Still, it really was a shock. That time was..."
        
        jump river02_memory

    #########################################    
    label river02_memory:
        
        $ event_name = _("A Story from Long Ago")
        
        stop music fadeout 1
        scene black with Dissolve(1)
        play music free0213
        
        "On that day, it was as hot as it was today."
        to "「Let's all go play in the river! 」"
        "Just like that, Torahiko made the suggestion."
        "It was sudden,{p}but as it was so hot, everyone agreed.{p}That way we could play and cool down a bit."
        "Everyone went back to their homes,{p}got their swimsuits, and came back."
        "After that, we faced the river,{p}and we all raced to be the first one to jump in."
        
        scene river gray 
        show over red light 
        with wipe_right
        play sound water01
        
        who "「Oh, this feels great! 」"
        "That's what the one who got in first said.{p}All of us behind him, me included, picked up the pace,{p}and hurried into the water."
        "All at once the pleasantly cool feeling,{p}wrapped up around us.{p}It felt amazingly good."
        "After we got into the water,{p}we played and came closer,{p}without ever getting tired of it."
        "We talked while swimming,{p}competed for the weirdest-looking rock,{p}and tried to see who could stay under the longest."
        "Time flew by as we had our fun."
        "But still, sooner or later,\nwe ran out of things to play."
        "Everyone was thinking, 'so what do we do next?'"
        ko "「Wanna go out to the middle of the river? 」"
        "In the end, Kounosuke spoke up nervously."
        "Even then, everyone was a little hesitant."
        "The middle part of the river is the deepest,{p}where you could get quickly swept away by the current."
        "The grown-ups would remind us so often\nabout how dangerous that part was."
        fn "「It's dangerous, so let's not, okay? 」"
        "Several others agreed with me."
        to "「I know, but still. I wanna do it. 」"
        "It's true, even after saying it,{p}I was a still little interested."
        
        play music water02 fadein 3
        
        "The place where the adults said 「don't go. 」"
        "We thought we knew what they meant,\nwhen they said it was dangerous.{p}But our curiousity was growing."
        "A place where we might be swept away quickly.{p}A place where we might not be able\nto reach the bottom with our feet."
        "Even after all that,{p}it definitely seemed more\nfun than where we already were."
        "In the end, our curiosity got the best of us."
        "We all quickly headed towards the center.{p}Our bodies sunk into the water, bit by bit."
        "The current grew faster, and then,{p}even though we were just standing,{p}it took some strength to stay in one spot."
        "But we didn't stop. We pushed forward."
        "Cheers of 「Ooh, the stream's fast! 」 rose up,{p}and we enjoyed our little adventure."
        "Pretty soon, the one at the head of our venture said:"
        "「Ooh, here we can go deeper in one shot! 」"
        "Yells of surprise and excitement rose up."
        "And then it happened."
        
        play sound water01
        stop music 
        
        su "{size=+20}「Whah!? 」"
        
        play music free27
        
        "Shun-kun was caught by the currents."
        "As the youngest in age, height, and weight,{p}Shun-kun stepped out too far."
        
        play sound water01
        
        "Then, the sounds of splashing."
        "All of us cried out."
        "...This is bad, we gotta do something!"
        "I think all of us were thinking the same thing.{p}But inside our heads we all blanked out.{p}In the end, we didn't know what to do."
        "So at any rate, we faced Shun-kun and yelled."
        "Even then, Shun-kun was swept further away.{p}Everyone was holding their breath."
        
        show river gray at vshake
        
        who "「What the hell are you kids doing!? 」"
        "We heard adults shouting from the river bed."
        
        stop music fadeout 4
        scene black with Dissolve(3)
        pause 1
        
        play music water03 fadein 2
        
        scene river red
        show ka 009 red at midleft
        show su 001 red at midright
        with Dissolve(1)
        
        ka "「And then after that, Shun-kun was safely pulled out,{p}\ \ and all of us got our asses handed to us. 」"
        fn "「Yeah, that's right.{p}\ \ That did happen, come to think of it. 」"
        "Yet how could I have forgotten such an event?"
        
        show su 004 red with dis
        
        su "「I really was thinking about,{p}\ \ what was going to happen then... 」"
        
        show ka 005 red with dis
        
        ka "「Shun couldn't swim yet then.{p}\ \ I still think that when I look at him now. 」"
        fn "「Yeah. And a little after that,{p}\ \ no one would suggest going to the river. 」"
        
        show su 002 red with dis
        
        su "「But this time I know how to swim.{p}\ \ So it'll be okay if we go into the center. 」"
        fn "「Nah, even if we did go in,{p}\ \ it wouldn't be able to drag us along now. 」"
        ka "「For sure. 」"
        
        play sound kara00
        
        pause 1.5
        
        "At that time, a crow was cawing overhead.{p}Looking closely, it seems the sun's setting."
        "Before we knew it, it was getting late."
        
        show ka 001 red 
        show su 001 red 
        with dis
        
        ka "「All right guys, let's pack up. 」"
        su "「I should, too. 」"
        fn "「Huh, you two are going back? 」"
        
        show ka 002 red with dis
        
        ka "「Yeah, it's not like I have\n\ \ all the time in the world. 」"
        fn "「In that case, I should go home too.{p}\ \ It can't be helped if I'm by myself,{p}\ \ and the heat's cooled down a bit. 」"
        "The three of us got up from the river together,{p}put on our shoes, and then...{p}I realized I didn't have a towel."
        fn "「Ah...! 」"
        "At this rate, I'll get a lot of things wet.{p}I should have worn sandals."
        
        show ka at jump_up
        
        ka "「Hey, [fn]. 」"
        "Once he got my attention, Kouya threw a towel to me."
        fn "「Thanks Kouya. You really are prepared. 」"
        
        show ka 003 red with dis
        
        ka "「Don't mention it. 」"
        "I wiped off the water with the borrowed towel,{p}then put my shoes back on."
        fn "「Really, thanks a lot Kouya.{p}\ \ It saved me some trouble. 」"
        "I thanked him one more time as I threw the towel back."
        
        show ka 006 red at jump_up
        
        ka "「I said don't mention it! 」"
        
        show su 002 red with dis
        
        su "「Okay, guess it's time to split up for today. 」"
        fn "「Yeah, that's right. 」"
        su "「Okay, [fn]-san, Kouya-san, see you next time! 」"
        
        show su at move_offright(0.5)
        
        "Shun-kun waved as he ran off cheerfully.{p}Kouya and I waved back."
        
        show ka 001 red with dis
        
        ka "「Shun, you'll fall if you aren't careful! 」"
        
        su "「I'll be okay...{w} {nw}"
        play sound puu79_a 
        extend " {cps=20}Woah! 」{nw}"
        play sound bosu31
        extend ""
        
        "As soon as he said that,\nShun-kun tripped dramatically."
        "It was kind of impressive actually."
        
        show ka 005 red with dis
        
        ka "「Oh, what the hell, Shun? 」"
        
        fn "「This time it wasn't swimming,{p}\ \ but keeping our eyes in front of us... 」"
        
        show ka 003 red at move_offright(.75)
        
        "The two of us smiled wryly as we ran up to Shun-kun."
        
        play sound kara00
        pause 1.2
        
        "Up in the sky, the crow let out a cry,{p}almost as if it were reciting a soliloquy."
        
        jump end02

##############################################
label tatsuki02:
    
    $ event_name = _("Playing with Tatsu-nii")
    $ focus_character = "tatsuki"
    
    scene map
    hide screen tatsukihouse02
    stop music
    $ love_tatsuki += 1
    scene black with wipe_dr_slow
    scene tatsuki_house_front with wipe_corner  
    play music free53
    show ta 001 at center with wipe_right
    
    ta "「Oh, work isn't finished yet.{p}\ \ {nw}"
    show ta 002 with dis
    extend "Just wait for a bit,\n\ \ it'll be done soon. 」"
    
    fn "「It's cool. I came too early,\n\ \ so don't worry about it. 」"
    
    show ta 001 with dis
    
    ta "「It's my fault, calling you over,\n\ \ and then making you wait.{p}\ \ Don't just stand there, take a seat. 」"
    "It's great I promised to hang with Tatsu-nii,\nbut I got so excited that, well..."
    "I just lost my sense of time."
    "I don't want to be in the way...{p}Better be careful."
    
    show ta 002 with dis
    
    ta "「After I finish this and clean up, I'll be done. 」"
    fn "「All right. 」"
    "I give up... I've got too many things\nweighing down on my mind.{p}That's it!"
    fn "「All you have to do is clean up? 」"
    
    show ta 001 with dis
    
    ta "「Yep. Almost done. 」"
    fn "「Then I'll help too.{p}\ \ If it's cleaning,\n\ \ I should be able to do it. 」"
    
    show ta 008 with dis
    
    ta "「It's fine, you don't need to do that.{p}\ \ Just wait a little more. 」"
    fn "「I'm tired of waiting,\n\ \ and wouldn't it be faster if both of us did it?\n\ \ Here, let me help. 」"
    
    show ta 001 with dis
    
    ta "「All right, all right, no way around it.{p}\ \ If you're so eager about it,\n\ \ then I'll let you help. 」"
    
    show ta 008 with dis
    
    ta "「Though, to tell you the truth,\n\ \ amateurs shouldn't be let into the workplace. 」"
    fn "「Awesome. So...{p}\ \ How can I help out? 」"
    
    show ta 002 with dis
    
    ta "「For you... sweep up the sawdust.{p}\ \ Broom's over there. 」"
    fn "{size=+15}「Screw that! 」"
    
    show ta 008 with dis
    
    ta "「...If you're just gonna hang with me,\n\ \ you could just go home, you know. 」"
    fn "「What!?{p}\ \ Is that your answer as a craftsman? 」"
    
    show ta 002 with dis
    
    ta "「I didn't say that.{p}\ \ You're just being such a...{p}\ \ stereotypical city person. 」"
    "He really is aiming to succeed his father,\nand to take over the family business."
    "He always said he'd do it,\neven since he was a kid."
    "I never thought he'd actually do it,\nthat is until I saw him again."
    "Even Torahiko...{p}he's seriously studying up on cooking."
    "Everyone's working hard,\nto achieve their future goals."
    "If you were to say if anyone hasn't changed..."
    "It's probably only me."
    
    show ta 001 with dis
    
    ta "「What are you spacing out for?{p}\ \ {nw}"
    show ta 002 with dis
    extend "Not helping?{w} {nw}"
    show ta at jump_up
    extend "Gahahaha! 」"
    
    fn "「Sorry, I was just thinking about...{p}\ \ how I missed the old times. 」"
    fn "「And speaking of which, back then,\n\ \ they wouldn't let me into the workplace. 」"
    fn "「You said that it\n\ \ \"wasn't a place for kids to play around in\"... 」"
    fn "「And I couldn't help,\n\ \ even with you watching me. 」"
    
    show ta 008 with dis
    
    ta "「It's dangerous with the tools lying about.{p}\ \ Even then, the guys were just hanging around. 」"
    
    show ta 001 with dis
    
    ta "「This isn't a good place to hang out, anyway.{p}\ \ They wouldn't let me start as an\n\ \ apprentice until I graduated. 」"
    
    show ta 002 with dis
    
    ta "「It's only recently that I was able\n\ \ to start learning as an apprentice. 」"
    fn "「That's too bad.{p}\ \ In that case, I'd be no use if I tried to help... 」"
    
    show ta 001 with dis
    
    ta "「Nah, since this is the garden,\n\ \ you've been watching me a lot.{p}\ \ My old man's been getting soft on ya. 」"
    fn "「Huh, really?{p}\ \ I can't picture him as anything\n\ \ but mad and scary. 」"
    
    show ta 002 at jump_up
    
    ta "「Well, about that,\n\ \ it's because you and Tora\n\ \ were always messing around. 」"
    ta "「But if I were him,\n\ \ I'd be a lot nicer for sure. 」"
    ta "「If you needed me to fix something,\n\ \ I'd take out my tools,\n\ \ and do it in a heartbeat! 」"
    ta "「Besides, don't remind me of those...\n\ \ shenanigans you and Tora got into. 」"
    fn "「You think I'd mess around like that?! 」"
    
    show ta 007 with dis
    
    ta "「Don't tell me you forgot.{p}\ \ All those pranks you did ended up\n\ \ being passed down as the stuff of legends! 」"
    
    show ta 010 with dis
    
    ta "「My Pa might have taken an interest\n\ \ because your family is so well known. 」"
    ta "「You know, sometimes,\n\ \ he still talks about you guys. 」"
    fn "「What, and you didn't pull your\n\ \ fair share of childhood pranks, too? 」"
    
    show ta 002 with dis
    
    ta "「Well, I'm not gonna lie.{p}\ \ I pulled some pretty awesome pranks, too.{p}\ \ I remember some of the stuff I did was crazy. 」"
    fn "「Oh, really... 」"
    "I've forgotten everything I've done,\nbut if I remembered any of that stuff...{p}Man, I wouldn't be too happy."
    
    stop music fadeout 1
    
    who "「Oh, you two messing around again? 」"
    
    play music free04
    show ta 002 at midleft
    show tp 401 at midright
    with wipe_right
    
    fn "「G-good afternoon...{p}\ \ It's been a while, h-hasn't it? 」"
    tp "「Long time no see, kid.{p}\ \ Heard ya came back from the city.{p}\ \ It's your old home town, relax. 」"
    "That sharp voice,\nthat piercing, determined gaze...{p}No doubt about it, it's Tappei-san."
    
    $ encounter_tappei = True
    
    "His hair's gotten thinner since I last saw him.{p}Does he still have his favorite pipe?"
    "I can smell pipe tobacco.{p}He's still a little scary.\nIt doesn't help that he looks bigger all around."
    "I think he weighs more than Tatsu-nii.{p}They still look alike, though."
    "Once I think about it,\nif Tatsu-nii were to grow older,\nhe'd look like Tappei-san."
    "Hmm... strange."
    
    show tp 403 with dis
    
    tp "「Hey, can't an apprentice\n\ \ be done with the clean up? 」"
    tp "「If a guest has to help,\n\ \ then anybody could be teaching you. 」"
    
    show ta 006 with dis
    
    ta "「T-that's... 」"
    fn "「H-hold on,\n\ \ I forced him into letting me help.{p}\ \ I-I'm sorry. 」"
    
    show ta 005 with dis
    
    ta "「This is is my responsibility.{p}\ \ You don't need to apologize. 」"
    fn "「But... 」"
    "So he really is a scary guy.{p}Clean up is also a big job,\nso I shouldn't have put my hands into it."
    "I got Tatsu-nii into trouble,\nNow Tappei-san's angry..."
    
    show tp 402 with dis
    
    "Wait, he's laughing?"
    
    show tp at jump_up
    
    tp "「Gahahahaha, I'm kidding!{p}\ \ Why so serious with that look on your face? 」"
    fn "「Huh? But, you said that...{p}\ \ I got in the way of work. 」"
    
    show tp 401 with dis
    
    tp "「Work? we're just running errands today.{p}\ \ The guys and I work in the late afternoon. 」"
    tp "「If you wanna do some work that much,\n\ \ why don't you get a job yourself? 」"
    "While Tappei-san can be scary when he's mad,\nhe's usually a playful, old guy."
    "His temper left a strong impression.{p}I recall his tantrums first..."
    "But there were also times\nwhen he would play with us too."
    "Hell, he even got along with Torahiko,\nwhen he was at his worst, that is."
    "With that said, him being mad...{p}it's weird, isn't it?"
    
    show tp 402 with dis
    
    tp "「I didn't ask you to work here today.{p}\ \ It's all right as you've got free time,\n\ \ and you've been cleaning up since last night. 」"
    tp "「So how about you help out,\n\ \ with a little organizing here? 」"
    
    show tp 401 with dis
    
    tp "「Earning a buck never hurts, right?{p}\ \ You can get started with a part-time wage. 」"
    fn "「Huh? What are you saying all of a sudden... 」"
    
    play music free44
    show tp 402 with dis
    
    tp "「Free time sure is great.{p}\ \ If you hate working,\n\ \ you can just show your face around here too. 」"
    tp "「Let's see... The tools need to be put back...{p}\ \ There's some lumber that needs stacking... 」"
    tp "「At that rate you'll make a decent amount. 」"
    "Tappei-san...{p}You aren't the type to go on...{p}Paid days off, are you?"
    
    show ta 004 with dis
    
    ta "「That's enough, Pa!{p}\ \ Using me like that, jeez. 」"
    ta "「[fn], trust me.{p}\ \ Don't hang out with this guy. 」"
    
    show tp 403 with dis
    
    tp "「Shut up!{p}\ \ Don't shoot your mouth off\n\ \ at the work of craftsmen! 」"
    
    show ta 008 with dis
    
    ta "「(That makes no difference...) 」"
    tp "「Listen, I'm saying this for your own sake.{p}\ \ Understand, son? 」"
    tp "「Even after [fn] came back after so long,\n\ \ I thought you were the kind of son\n\ \ who'd finish work before going to play. 」"
    
    show tp 401 with dis
    
    tp "「Your father has a smart plan after all.{p}\ \ You oughta thank me. 」"
    
    show ta 002 with dis
    
    ta "「Oh, sorry Pa. Thanks after all. 」"
    
    show ta 004 at jump_up
    
    ta "「What? Is that what you wanted to hear?{p}\ \ Yeah, like I'd actually say that!{p}\ \ You're totally doing this all for yourself. 」"
    
    stop music fadeout 3
    
    "Hmm, but it's true I'm running low on cash."
    "I could do it while I'm free,\nand if it's during the evening,\nthen it won't affect any plans..."
    
    play music free0211
    
    fn "「Well if it's all right,\n\ \ when my hands are empty,\n\ \ then please let me help. 」"
    
    show ta 006 with dis
    
    ta "「Are you serious?{p}\ \ You don't have to force yourself. 」"
    fn "「Yeah, of course I am.{p}\ \ It'll be tough with the money I have now.{p}\ \ I have to pay for souvenirs, travel fees... 」"
    fn "「And besides,\n\ \ I've been wanting to hang out with you. 」"
    
    show ta 007 with dis
    
    ta "「Idiot. You're coming over to play,\n\ \ not to work. 」"
    
    show tp 402 with dis
    
    tp "「Well then. It's decided.{p}\ \ If that's how it goes,\n\ \ I have to explain the work to you. 」"
    tp "「And after that,\n\ \ we can grab a bite to eat. 」"
    "Looks like I'll have a great time.{p}Hanging with Tatsu-nii and everyone\nis always a lot of fun."
    "Tappei will probably scold us for being late,\nlike he always does when we're out."
    "If it gets to be late,\nand I get to be a little dirty,\nI wonder if I can wash up here."
    "After that, we'll all gather for dinner...{p}Sounds like a plan."
    
    show ta 001 with dis
    
    ta "「Sorry Pa, but [fn] and I are going out,\n\ \ and actually having a good time. 」"
    ta "「Just a little more to do,\n\ \ and then we can leave, all right? 」"
    "We promised to hang out today but,\nat this rate it wouldn't be bad\nto have a dinner with Tappei and company."
    
    menu:
        "A. But I promised to hang with Tatsu-nii.":
            jump tatsuki02_hangout
        "B. Let's talk with everybody over food.":
            jump tatsuki02_eat
         
    ###################################################
    label tatsuki02_hangout:
        
        $ event_name = _("Let's go play")
        $ love_tatsuki += 1
        
        fn "「Hmm, it's tempting...{p}\ \ but for a while now,\n\ \ I've wanted to spend time with Tatsu-nii. 」"
        "I've been looking forward to it,\nso I guess I'll have to turn down Tappei-san."
        "Maybe I can call over Torahiko,\nand the three of us can horse around,\njust like old times..."
        "We're not kids anymore though, so...{p}acting like one is a no-no.{p}Wonder who else I can call..."
        fn "「Ehehe, I haven't started work yet,\n\ \ and I've already made a promise with Tatsu-nii. 」"
        fn "「We'll relax and eat together another time.{p}\ \ The fun's just getting started... 」"
        
        show tp 401 with dis
        
        tp "「Is that so...{p}\ \ Well then boys, see you later. 」"
        tp "「Be sure to come back on time for work.{p}\ \ I'm gonna need some help tonight. 」"
        
        scene tatsuki_house_front
        show ta 001
        with wipe_right
        
        "Huh, for a second he looked lonely...{p}Was that my imagination?"
        
        show ta 008 with dis
        
        ta "「\"Gonna need some help,\" my ass.{p}\ \ Jeez... He was eating earlier,\n\ \ and he even gave that excuse. 」"
        ta "「What the hell is he getting at? 」"
        fn "「Hey, at least Tappei-san seems lively.{p}\ \ My dad isn't that much fun... 」"
        "A bigger, bolder,\nlivelier middle aged dragonman.{p}If I had a father like that..."
        
        show ta 010 with dis
        
        ta "「You're kidding me, right?{p}\ \ There's nothing good about living with him.{p}\ \ That damned old man... 」"
        
        show ta 008 with dis
        
        ta "「When it comes to work,\n\ \ he can be strict like a demon.{p}\ \ I guess that's why he's so successful. 」"
        fn "「Huh, so you do respect your dad. 」"
        
        show ta 007 at jump_up
        
        ta "「Whaa!? No way that's true.{p}\ \ I recognize him as a craftsman,\n\ \ but how could I respect him? 」"
        "What a bad lie.{p}You're getting all red and bashful.{p}It's cute even if you're so big..."
        ta "「What are you smiling about?{p}\ \ Anyway, get ready. 」"

        jump tatsuki02_coworkers

    ############################################
    label tatsuki02_eat:
        
        "Since all the workers live\nand work around the house,\nit could be fun joining them."
        "It's almost like an extended family.{p}Nothing but buff beastmen,\ngathered around the dinner table..."
        fn "「Ah, it's been so long...{p}\ \ I want to have dinner with the gang.{p}\ \ I want to hear some stories about work, too. 」"
        tp "「Right, aren't you quick to pick up on things. 」"
        ta "「But isn't Ma not here today?{p}\ \ Wouldn't that mean we'd have to make dinner? 」"
        tp "「We can still talk about work, at least.{p}\ \ [fn], when you're done, we'll eat at Raimon. 」"
        
        show ta 008 with dis 
        
        ta "「Pa... You don't have money now, do you?{p}\ \ Ma asked me to watch over you,\n\ \ so that you don't go crazy with your cash. 」"
        
        show tp 403 at jump_up
        
        tp "「What!? Geh, I'm gonna empty my wallet then.{p}\ \ This is work-related, so...{p}\ \ It wouldn't concern Ma. 」"
        ta "「So we're going to Raimon? 」"
        
        show tp at jump_up
        
        tp "「Still! 」"
        
        show ta 004 with dis
        
        ta "「'Still' my ass!{p}\ \ Old people should pipe down and be good.{p}\ \ I'm not the only one watching you today. 」"
        
        show tp 401 with dis
        
        tp "「Keh... It's all right if I'm good, right.{p}\ \ Staying at home by myself is all right,\n\ \ for a guy like me. 」"
        
        show ta 008 with dis
        
        ta "「No worries, Pa.\n\ \ It's a large family here, you won't be alone. 」"
        
        show tp 402 with dis
        
        tp "「You're starting to act like your mother.{p}\ \ Fine, I'll stay at home. 」"
        tp "「Hey, [fn], hurry back for work.{p}\ \ If you come, next time I'll take you for a drink.{p}\ \ Keep that a secret, yeah? 」"
        
        scene tatsuki_house_front
        show ta 008 at center
        with wipe_right
        
        ta "「Sigh... How did he become a father? 」"
        fn "「Hey, at least Tappei-san seems lively.{p}\ \ My dad isn't that much fun... 」"
        "A bigger, bolder,\nlivelier middle aged dragonman.{p}If I had a father like that..."
        
        show ta 010 with dis
        
        ta "「You're kidding me, right?{p}\ \ There's nothing good about living with him.{p}\ \ That damned old man... 」"
        
        show ta 008 with dis
        
        ta "「When it comes to work,\n\ \ he can be strict like a demon.{p}\ \ Guess that's why he succeeds so well. 」"
        fn "「Huh, so you do respect your father. 」"
        
        show ta 007 at jump_up
        
        ta "「Whaa!? No way that's true.{p}\ \ I recognize him as a craftsman,\n\ \ but how could I respect him? 」"
        "What a bad lie.{p}You're getting all red and bashful.{p}It's cute even if you're so big..."
        ta "「What are you smiling about?{p}\ \ Anyway, get ready. 」"
        
        jump tatsuki02_coworkers
        
    ##########################################    
    label tatsuki02_coworkers:
        
        $ event_name = _("The One who cares")
        
        hide ta with wipeleft
        stop music fadeout 1
        scene black with Dissolve(1)
        play music cicada01 fadein 2
        scene tatsuki_house_front with Dissolve(1)
        
        "Even so, was Tappei-san that kind of person?{p}He's kind, and has a playful side to him,\nbut I get the feeling he's changed a lot."
        "Like he's positively excellent, or something...{p}I've made him mad a lot,\nso I had an impression of him as a scary guy..."
        "But maybe he was always like this."
        
        show ni 001 at center with wipe_right
        
        horse "「Hm? Who are you?{p}\ \ You don't look like a customer. 」"
        horse "「This place is dangerous,\n\ \ so outsiders shouldn't come in. 」"
        fn "「No, I'm not anyone suspicious. 」"
        "What am I saying.{p}Why did he suddenly talk to me all irritated?"
        
        show ni 005 with dis
        
        horse "「What are you saying?{p}\ \ That's not what I'm asking you. 」"
        
        show ni 001 with dis
        
        horse "「Coming onto the premises,\n\ \ mumbling to yourself, and nothing?{p}\ \ So suspicious... 」"
        "I got myself into a suspicious mess.{p}And even I'm not doing anything wrong.{p}Hey, wait. Who is this guy?"
        "If he's a member of the Midoriya Group,\nhe should be wearing the provided uniform,\nand he looks about the same age as me..."
        "but I don't recognize him.{p}I'm suspicious? The suspicious one is this guy."
        fn "「Excuse, can I ask you one thing?{p}\ \ I'm a little uneasy... If I remember right... 」"
        fn "「I thought everyone here\n\ \ wears the same work clothes,\n\ \ but are you a craftsman here? 」"
        "Heheheh, if my thinking is right,\nthen it should be different."
        
        play sound puu79_a
        
        "The one who sees through the truth,\n{nw}"
        play sound puu79_b
        extend "whose looks are human,\n{nw}"
        play sound puu79_a
        extend "whose taste is in beastmen..."
        
        "His name is...{p}{nw}"
        play sound freeze04
        extend "The Great Detective [fn]!{p}{size=+15}The suspicious one...{nw}"
        play sound metal38
        show tatsuki_house_front at hshake
        extend "Is YOU!"
        
        show ni 005 with dis
        
        horse "「No. 」"
        "Hey watch, as I take him to the office,\nand prepare for Tappei-san to give him...{p}an intense chastisement."
        
        show ni 001 with dis
        
        horse "「I'm still an apprentice.{p}\ \ I received the work clothes,\n\ \ but we're free to wear what we'd like. 」"
        horse "「Originally, I was working elsewhere,\n\ \ so I'm not wearing the clothes here. 」"
        
        show tatsuki_house_front at hshake
        play sound hit81
        "That can't be!?{p}My thinking was wrong..."
        
        show ni 001 big with dis
        horse "「Are you done?{p}\ \ If so, come with me to the office.{p}\ \ We'll listen to your story there. 」"
        horse "「Though I guess only the boss will. 」"
        
        play sound bosu34
        
        fn "「Uh, I...{p}\ \ Hey, hey wait. 」"
        "An apprentice, huh.{p}He looks rich, but he's fairly strong."
        "If Tappei-san came out,\nhe probably won't get mad,\nbut he might laugh about it. Tatsu-nii would..."
        
        show cu 005 at farright behind ni with wipe_right
        
        rat "「What're you doin', Senpai?{p}\ \ Hn?{p}\ \ {nw}"
        show cu 001 with dis
        extend "Could you be... [fn]-san?"
        fn "「Yes, that's right... 」"
        
        scene tatsuki_house_front
        show ni 001 at midleft
        show cu 001 at midright
        with wipe_right
        play music free02
        show cu 002 with dis
        
        cu "「It's the real thing for sure!{p}\ \ I'm an apprentice for the Midoriya Group.\n\ \ Name's Chuukichi. 」"
        
        $ encounter_chuukichi = True
        
        show ni 002 with dis
        
        cu "「Sweet, it's an honor to think that I'd be able\n\ \ to meet the legendary [fn]-san. 」"
        
        show ni 001 with dis
        
        horse "「Oh, that [fn]-kun.{p}\ \ If that was the case,\n\ \ you should've said something earlier. 」"
        
        $ encounter_akira = True
        
        ni "「I'm Akira Nikaidou.{p}\ \ As I've told you earlier,\n\ \ I'm an apprentice here. 」"
        "Legendary? How do you know me?{p}If it was 'legend,'\nthen it would have to be..."
        
        show cu 007 with dis
        
        cu "「Not only within the Midoriya Group,\n\ \ but in the village, too... 」"
        cu "「I've gotten so much respect for you,\n\ \ since I've heard the stories 'bout you. 」"
        
        show cu 011 with dis
        
        cu "「In town, there isn't anyone like that.{p}\ \ Can I call you Aniki? 」"
        "What are you asking..."
        
        show ni 003 with dis
        
        ni "「Did you come over to play?{p}\ \ Then I'll call him over. 」"
        "I should have greeted them,\nby saying that I was an apprentice."
        "I was surprised there were people here,\nwho were my age and working."
        fn "「Oh, I've already talked with Tatsu-nii,\n\ \ and he already left. 」"
        fn "「So it's okay, thanks.{p}\ \ I came over to hang out today,\n\ \ but after this I'll be helping out with work. 」"
        fn "「So I look forward to working with you. 」"
        
        show cu 012 at jump_up
        
        cu "「F'real!? Working together wit' Aniki,\n\ \ is gonna be like a dream come true.{p}\ \ Looking forward to working with you. 」"
        "So I've already become Aniki...{p}between Tatsu-nii and Tappei-san,\nI wonder..."
        "Which of them inspires more weird things?{p}Probably Tappei-san? But Tatsu-nii has...{p}more unknown points."
        fn "「Hey, Chuukichi-kun.{p}\ \ Who did you hear about me from? 」"
        
        show cu 005 with dis
        
        cu "「Just Chuukichi is fine.{p}\ \ I heard a lot 'bout you from Master,\n\ \ and Young Master. 」"
        "Which one..."
        
        show ta 002 at farright behind cu with wipeleft
        
        ta "「Who's Young Master?{p}\ \ It's like you guys just heard,\n\ \ Pa forced him into a part time job here. 」"
        ta "「And we'll be counting on him. 」"
        
        show cu 001 with dis
        
        cu "「'kay. 」"
        
        show ni 001 with dis
        
        ni "「It can't be helped, if the boss decided it.{p}\ \ I look forward to working with you. 」"
        
        show ni 003 with dis
        
        ni "「That said, don't get in the way,\n\ \ and I hope you'll keep me out of it\n\ \ if circumstances cause trouble. 」"
        ni "「Like in the old stories.{p}\ \ I'm sure you've heard about them. 」"
        
        show ta 004 with dis
        
        ta "「Hey, don't say stuff like that. 」"
        
        show ni 002 with dis
        
        ni "「Hmph... still,\n\ \ it's more fun if work is bustling.{p}\ \ Do your best. 」"
        
        hide ni with wipeleft
        
        fn "「Am I hated all of a sudden...? 」"
        
        show ta 001 with dis
        
        ta "「No way, that was more like a welcoming.{p}\ \ He's not a bad guy,\n\ \ but he sucks at expressing emotions. 」"
        fn "「Is that so?{p}\ \ He's a type like Shin-kun then. 」"
        
        show ta 002 with dis
        
        ta "「Shin's not that docile,\n\ \ but that's not all. 」"
        ta "「He doesn't understand relationships,\n\ \ but he's a guy who's easy to understand,\n\ \ and he's not bad at sociability. 」"
        
        show cu 008 with dis
        
        cu "「There're times where he gets into a bad mood,\n\ \ but he's an interestin' enough dude. 」"
        cu "「He's also got times\n\ \ where he gets snappy and selfish, tho'. 」"
        fn "「Huh, in that case I can relax and work. 」"
        
        show ta 001 with dis
        
        ta "「Don't be so careless. 」"
        ta "「Pa would get strict,\n\ \ and Nikaidou can get like that too,\n\ \ so they won't go easy. 」"
        "Uhh, suddenly I'm feeling uneasy..."
        
        show ta 002 with dis
        
        ta "「Hehehe, don't feel that way.{p}\ \ Let's hurry up and go already. 」"
        
        show cu 002 with dis
        
        cu "「Where you goin'?{p}\ \ Take me along too please. 」"
        
        show ta 008 with dis
        
        ta "「Wait, you aren't leaving the stuff,\n\ \ you still have to do, are you? 」"
        
        show cu 006 at jump_up
        
        cu "「Ah, no good! This is bad,\n\ \ who knows what Master might do to me! 」"
        cu "「Also, my big sis told me to do something for her.{p}\ \ In that case, Young Master, Aniki, good work! 」"
        
        play sound step03
        scene tatsuki_house_front
        show ta 008 at center
        with wipe_right
        
        "Chuukichi-kun ran back to the office."
        fn "「Seems like a fun workplace. 」"
        
        show ta 002 with dis
        
        ta "「Everyone's close since we all live together,\n\ \ but even with the fun times,\n\ \ there's a lot more tough times. 」"
        fn "「Sounds like a real big pain,\n\ \ with Tatsu-nii as an apprentice too.{p}\ \ But I think that mood will pass. 」"
        fn "「Everyone's bulking up,\n\ \ but your muscles are fairly brawny already. 」"
        fn "「And I can see your horns growing larger,\n\ \ you're really turning into quite a handsome guy.{p}\ \ Your back and stomach look like they filled out. 」"
        
        show ta 007 with dis
        
        ta "「Like I said, this isn't fat,\n\ \ dragonmen are naturally like this.{p}\ \ Well, not all dragonmen. 」"
        fn "「Of course, I get it. So squishy. 」"
        
        show ta at hit_right
        
        ta "「Stop that, don't rub my stomach.{p}\ \ Ah, hey! Don't run off. Come back here! 」"
        fn "「Hahaha, I've been waiting for you.{p}\ \ Let's hurry up and go.{p}\ \ It's a race to Torahiko's house! 」"
        
        scene sky with Dissolve(1)
        
        "A part time job with the Midoriya Group...\nI'm looking forward to it."
        "It's fun meeting up with everyone,\nbut this doesn't happen every day.{p}I have to do my best."
        ta "「I said wait!\n\ \ If you weren't about to run off I've got a car! 」"
        
        $ part_time = True
        
        jump end02

#######################################    
label juuichi02:
    
    $ event_name = _("Meeting on the Second Day")
    $ focus_character = "juuichi"
    
    scene map
    stop music
    hide screen ricefield02
    $ love_juuichi += 1
    scene rice with dis
    play music cicada01
    
    "The cicadas sing as a chorus.{p}The thunderheads overhead growing steadily larger.{p}The sun streaming down."
    "As I wipe the sweat off my brow,{w=.3}\nI'm reminded that this is\nwhat summer in the country is like."
    "On both sides of the path,\nthe rice fields spread out endlessly."
    "It looks like the rice hasn't finished growing yet:\nThe countless leaves growing towards the heavens\nare almost invisible."
    "It looks like a green carpet has been rolled out.{w=.3}\nIt's a shame I won't be here for harvest this year."
    "...Wait, I shouldn't be thinking things like that.{p}It'll spoil my long-awaited return.{p}I shake my head to clear these thoughts."
    "I only got back to Minasato yesterday.{p}Torahiko's violent welcoming is fresh in my mind."
    
    $ renpy.music.set_volume(0.4, 2.0, channel = "music")
    
    scene black with wipe_down_slow
    
    scene bstop gray    
    show to 002 gray
    show over red light
    with wipe_down_slow
    
    "Even though I've grown in the time I've been gone,{w=.3}\nI need to look up to make eye contact with Torahiko."
    "...I thought I'd grown a fair bit, though.{p}That makes me feel a bit down."
    
    show to 001 gray
    with dis 
    
    "Then, Torahiko told me about the welcoming party.{p}I didn't think they'd actually manage to plan that,\nso that was a surprise."
    "I hadn't been keeping in touch with anybody at all.{w=.3}\nFor all I know, they could have forgotten about me."
    "But they still welcomed me back as an old friend.{p}That made me really happy."
    
    show to 011 gray 
    with dis 
    
    "As I recall yesterday's events one by one,{p}I can't help but smile."
    "...Ahh, I really am back here.{p}The sun is really scorching,\nbut it's somewhat comfortable here."
    "My skin is going to be so dark\nby the time my vacation is over.{p}Oh well. It's kind of healthy to get a tan, right?"
    
    who "「Hey, [ln]. Are you okay? 」"
    
    $ renpy.music.set_volume(0.8, 0.0, channel = "music")
    play sound bom26
    scene rice with qdis
    
    fn "「...?! 」"
    "I jump as a voice calls my name from behind me.{p}It looks like I was lost daydreaming."
    
    stop music fadeout 10
    
    fn "「...Please don't scare me like that. 」"
    "I speak to the owner of the voice as I turn around."
    "There's only one person in this village who\ncalls me by my last name."
    "I heard this low voice yesterday, too.{p}There's no mistaking it."
    
    play music free02
    
    show ju 001 at center with wipeleft
    
    "Just as I guessed, it's Juuichi-san."
    
    $ event_name = _("Suddenly, a Bear!")
    
    show ju 011 with dis
    
    ju "「I think anybody would say something,\n\ \ if they saw their friend standing in the middle of\n\ \ the road with a dazed look on their face. 」"
    fn "「I guess you're right. 」"
    "Since he spoke out of concern,\nI have no reason to complain.{p}...It was my fault for letting my mind wander."
    
    show ju 003 with dis
    
    ju "「...Looks like it was nothing.{p}\ \ I thought for sure you'd gotten heat stroke. 」"
    "Ooh, now I feel guilty.{p}I've been getting lost in thought a lot recently...{w=.3}Or maybe I should say I've been daydreaming."
    "I should really do something about that."
    
    show ju 001 with dis
    
    ju "「So,{w=.3} what are you doing out here, anyway? 」"
    fn "「Oh, right.{w} I'm taking a walk through the village. 」"
    "I straighten my posture as I answer his question.{p}...There's nothing in particular to feel guilt about,{w=.3}but I remember what happened to Torahiko yesterday..."
    fn "「I haven't been here since elementary school,{w=.3}\n\ \ so I've forgotten about a lot of places.{p}\ \ I thought I'd remember them if I went for a walk. 」"
    "Some places come back to me quite easily,\nsuch as the candy store, and the Ooshima Inn."
    "On the other hand, places I didn't visit very often\nhave completely escaped me."
    "I thought I'd remember more...\nIt seems my memory is worse than I thought."
    
    show ju 003 with dis
    
    ju "「...I see.{w} Forgetting things is a shame,\n\ \ but I guess there's not too much you can do about it. 」"
    fn "「Sorry...{p}\ \ But I'll be sure to have fun this summer,\n\ \ {w=.3}and make new memories to take with me! 」"
    
    show ju 002 with dis
    
    ju "「That's true.{w=.3} You should have a rewarding vacation. 」"
    fn "「I will!{p}\ \ By the way,{w=.3} are you on your way home from practice? 」"
    "I remember him talking a bit about judo yesterday,\n{w=.3}so I try to shift the topic of conversation."
    
    show ju 001 with dis
    
    ju "「Yes, I am.{p}\ \ There's a tournament coming up soon,\n\ \ {w=.3}so I've been training hard since this morning. 」"
    "Training hard since this morning...?{w} Knowing him,\nhe's probably got a pretty strict regimen.\nThere's no way that I would be able to stand that."
    fn "「Ah... You must be pretty worn out.{p}\ \ But a tournament? In the middle of summer vacation?{p}\ \ There aren't many sports I know of that do that. 」"
    ju "「Oh,{w=.3} the Kazenari Martial Arts League is hosting it,\n\ \ so it's not a regular event. 」"
    
    show ju 008 with dis
    
    ju "「...I guess it is a bit like a regular event\n\ \ for those of us who live around here, though. 」"
    fn "「Wow, really?{w} I guess I can't enter it then, huh. 」"
    
    show ju 002 with dis
    
    ju "「You weren't planning on it to begin with. 」"
    "Juuichi-san shows his sharp canines as he says that.{p}I've never been particularly good at sports,\n{w=.3}so people who are look really cool to me."
    "In Juuichi-san's case,{w=.3} he's not a show off.\nI really think he can win."
    "Torahiko, on the other hand, gets ahead of himself,\nand falls flat on his face too much...{p}I worry about him, sometimes."
    "Hmm, I wonder if coolness and wisdom come with age..."
    fn "「Umm...{w=.3} If it's all right with you,\n\ \ can I come and cheer for you? 」"
    "I've finally come back to Minasato,\nso I want to see him in action with my own eyes."
    "Seeing him flinging his opponents away...{p}That would be an amazing spectacle."
    
    show ju 001 with dis
    
    ju "「I don't mind.{p}\ \ {nw}"
    show ju 008 with dis
    extend "...Now I'll have to try not\n\ \ to be clumsy during the match. 」"
    
    "Juuichi-san quietly mutters to himself.\nSomething about more training?"
    "For such a strong person to say that they actually\npractice impresses me quite a lot."
    "I remember being taught that you can\nbe great with just one talent.{p}I'm missing that last bit of the equation, though."
    fn "「...You don't mind practicing during your free time?\n\ \ It's summer vacation, after all. 」"
    
    show ju 001 with dis
    
    ju "「If I do the same thing as other people,\n\ \ {w=.3}I'll only get the same result as those people.{p}\ \ In the end, I think that will make a difference. 」"
    fn "「... 」"
    "What's with this heavily persuasive power?{p}He's only a year older than me...\n{w=.3}How is he able to think like that?"
    "Juuichi-san and I might live in the same world,\nbut we have completely different\nways of looking at it."
    fn "「...That's impressive. 」"
    "I tried to say something clever,\n{w=.3}but that's all I could think of.{p}I'm a little disappointed in myself."
    
    show ju 003 with dis
    
    ju "「Not really.{p}\ \ Stronger guys who practice more than I do\n\ \ are a dime a dozen. 」"
    ju "「There are even a few around here. 」"
    "Wow, the world of sports must be tough.{p}But, if you ask me, I think Juuichi-san\nis strong enough for it."
    "...Wait,{w=.3} I've never watched any of his matches.\nIsn't it a bad idea for me to say that?"
    ju "「Besides...{p}\ \ {nw}"
    show ju 009 with dis
    extend "If I'm going to do it,{w=.3} I want to win. 」"
    
    "Juuichi speaks thoughtfully,\nscratching his chin with a thumb."
    
    show ju 001 with dis
    
    ju "「It's a difficult feeling to put into words...{p}\ \ {nw}"
    show ju 002 with dis
    extend "But that feeling of victory is unforgettable.\n\ \ {w=.3}It's probably why I do judo. 」"
    
    "Juuichi-san speaks with his eyes partly closed.\nHe seems to have a different mood to earlier."
    "I'm quite surprised to see him like this.{p}So he can make an expression like that, too..."
    
    show ju 003 with dis
    
    ju "「...Sorry.{p}\ \ I'm not boring you, am I? 」"
    fn "「Ah, no, not at all!{p}\ \ Juuichi-san,{w=.3} you really do like judo. 」"
    
    ju "「...Well,{w=.3} I wouldn't keep doing it if I didn't. 」"
    fn "「You know that's not what I meant... 」"
    "At my objection,{nw}"
    show ju 002 with dis
    extend "{w=.3} Juuichi-san's face relaxes a bit."
    
    show ju 001 with dis
    
    ju "「...Well,{w=.3} I should get going. 」"
    fn "「Oh, sure.{p}\ \ Sorry about keeping you here. 」"
    "About 30 minutes have passed.{p}I'm not used to having long\ntalks in this sweltering heat."
    ju "「Don't worry about it.{p}\ \ I started the conversation, after all. 」"
    
    hide ju with wipe_right
    
    "With that, and a wave of his hand,\n{w=.3}Juuichi-san turns his large back towards me.{p}{nw}"
    play sound step01
    extend "The sound of his footsteps on the gravel get quieter."
    
    "I think about where I should go next.{p}...After all, I did start this walk without\na particular destination in mind."
    "I think I'll head to the candy store\nto get some ice cream while I think about it.\nI feel like cooling off in the shade now, anyway."
    "...Ah, should I invite Juuichi-san, too?"
    "When I turn to look for him, he's already gone.{p}Damn, too slow.{p}Oh well. I'm sure I'll get another chance."
    "Summer vacation has just started, after all!{p}I start walking in the opposite direction\nJuuichi-san went."
    
    jump end02

label end02:

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

    jump day03
        
