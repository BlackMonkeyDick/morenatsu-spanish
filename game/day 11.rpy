## Day 11

screen marketplace11:
    hbox:
        add "arrow down"
        at marketbounce1
    hbox:
        add "icon_juu"
        at marketbounce2
    hbox:
        text _("Market")
        xalign .5 yalign .52
screen shinhouse11:
    hbox:
        add "arrow left"
        at shinbounce1
    hbox:
        add "icon_shin"
        at shinbounce2
    hbox:
        text _("Shin's House")
        xalign .16 yalign .70
screen riverbed11:
    hbox:
        add "arrow down"
        at riverbounce1
    hbox:
        add "icon_tatsu"
        at riverbounce3
    hbox:
        add "icon_shun"
        at riverbounce4
    hbox:
        add "icon_sou"
        at riverbounce5
    hbox:
        add "icon_juu"
        at riverbounce6
    hbox:
        add "icon_kyou"
        at riverbounce2
    hbox:
        add "icon_kouno"
        at riverbounce7
    hbox:
        add "icon_shin"
        at riverbounce8
    hbox:
        add "icon_kouya"
        at riverbounce9
    hbox:
        add "icon_tora"
        at riverbounce10 
    hbox: 
        text _("Dry Riverbed")
        xalign .625 yalign .7
        
screen minasatomap11a():
    add "map"
    add "mapdate"
    imagebutton idle "a icon" hover "icon loop" xpos 87 ypos 278  action Jump("shin11") hovered Show("shinhouse11")  unhovered Hide("shinhouse11") hover_sound "av/audio/click_008.wav"
    imagebutton idle "a icon" hover "icon loop"  xpos 372 ypos 249  action Jump("juuichi11") hovered Show("marketplace11")  unhovered Hide("marketplace11") hover_sound "av/audio/click_008.wav"
    hbox:
        text _("{size=+30}August 11")
        at maptime
        
screen minasatomap11b():
    add "map"
    add "mapdate"
    imagebutton idle "a icon" hover "icon loop" xpos 87 ypos 278  action Jump("shin11") hovered Show("shinhouse11")  unhovered Hide("shinhouse11") hover_sound "av/audio/click_008.wav"
    hbox:
        text _("{size=+30}August 11")
        at maptime
        
screen minasatomap11c():
    add "map"
    add "mapdate"
    imagebutton idle "a icon" hover "icon loop" xpos 87 ypos 278  action Jump("shin11") hovered Show("shinhouse11")  unhovered Hide("shinhouse11") hover_sound "av/audio/click_008.wav"
    imagebutton idle "a icon" hover "icon loop"  xpos 458 ypos 351  action Jump("tatsuki11") hovered Show("riverbed11")  unhovered Hide("riverbed11") hover_sound "av/audio/click_008.wav"
    hbox:
        text _("{size=+30}August 11")
        at maptime
        
        
screen minasatomap11d():
    add "map"
    add "mapdate"
    imagebutton idle "a icon" hover "icon loop" xpos 87 ypos 278  action Jump("shin11") hovered Show("shinhouse11")  unhovered Hide("shinhouse11") hover_sound "av/audio/click_008.wav"
    imagebutton idle "a icon" hover "icon loop"  xpos 372 ypos 249  action Jump("juuichi11") hovered Show("marketplace11")  unhovered Hide("marketplace11") hover_sound "av/audio/click_008.wav"
    imagebutton idle "a icon" hover "icon loop"  xpos 458 ypos 351  action Jump("tatsuki11") hovered Show("riverbed11")  unhovered Hide("riverbed11") hover_sound "av/audio/click_008.wav"
    hbox:
        text _("{size=+30}August 11")
        at maptime
        
###################################################        
label day11:
    
    $ renpy.music.set_volume(1.0, 0.0, channel = "music")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound2")
    
    $ day = 11
    $ event_name = _("８月11日")
    $ the_date = _("August 11")
    $ focus_character = ""
    
    $ affectionlist = [love_tatsuki, love_kounosuke, love_shun, love_kouya, love_shin, love_juuichi, love_soutarou, love_kyouji, love_torahiko]
    $ namelist = ["tatsuki", "kounosuke", "shun", "kouya", "shin", "juuichi", "soutarou", "kyouji", "torahiko"]
    $ selection = affectionlist.index(max(affectionlist))
    $ favorite = namelist[selection]
    
    window hide
    play music birds_chirping
    
    scene sky01 
    show text "{size=+130}August 11" at truecenter
    with Dissolve(.5)

    pause 3
    scene black with Dissolve(1)
    pause .4
    
    scene hbroom with wipe_corner
    
    fn "「I wonder what I should do today. 」"
    
    play music "<from 2.5>av/audio/free0422.ogg"
    
    if juuichi_hate == False:
        if favorite == "tatsuki":
            call screen minasatomap11d
        else:
            call screen minasatomap11a
    elif favorite == "tatsuki":
        call screen minasatomap11c
    else:
        call screen minasatomap11b
        
####################################################    
label shin11:

    $ love_shin += 1
    $ focus_character = "shin"
    $ event_name = _("Rain of Friday")

    scene map
    hide screen shinhouse11
    call rain_set from _call_rain_set
    pause 0.01
    play music rainfall
    $ renpy.music.set_volume(0.5, 0.0, channel = "music")
    scene path 
    show over black
    show raining
    with dis

    "This is not a day to be doing errands.\nStill, I shouldn't make my grandparents\ndo this sort of thing."
    "Uhh, so I'm buying sides for tonight's dinner and..."
    
    show si 001 at center behind raining with dis

    si "「Hello. 」"
    fn "「Oh, Shin-kun. Good afternoon. 」"
    "As I was on my way to the shopping district,\nthere was a figure of a cat wearing boots\nwalking towards me."
    "Wait, it's Shin-kun."
    si "「Good afternoon.{p}\ \ Are you walking on a day like this?{p}\ \ You have so much time. 」"
    "Ugh...{w} so suddenly?{p}That's just like him though."
    fn "「N-no. I'm on errands today. 」"
    "Under this vinyl umbrella,\nI pulled out a piece of paper from my pocket\nand showed it to Shin-kun."
    fn "「Grandpa strained his back.\n\ \ Grandma's looking after him,\n\ \ so I have to do this much. 」"
    
    show si 009 with dis

    si "「Is that so?{p}\ \ Sorry. I said something mean, didn't I? 」"
    fn "「No, don't worry about it.\n\ \ What are you doing Shin-kun? 」"

    show si 001 with dis

    si "「Something I sent for repairs seems to be done.{p}\ \ I'm going to Kounosuke's house to pick it up. 」"
    fn "「Oh, I see. 」"
    "Oh yeah,\nKounosuke's house is the repairman's shop.{p}I don't remember much being done there though."

    show si 002 with dis

    si "「If you like, want to come along for a bit? 」"
    fn "「Huh? But... 」"

    show si 001 with dis

    si "「It's an opportunity. 」"
    si "「Besides, don't you think it's a chance\n\ \ to know the local products and the people\n\ \ who lived here for so long better? 」"
    fn "「In that case, maybe I'll ask them for help. 」"
    
    scene black with dis
    scene market 
    show over black
    show raining
    with dis

    "Of course, since it's raining\nthe shopping district is quiet."
    "As Shin-kun lead me around,\nI bought the things on my list one by one."
    "We carelessly intruded on\nthe same store's third floor,\nand when Shin-kun's pitiful thing was looked at,"
    "I wondered if the sad summer memory\nwould be carved into my heart."
    
    show si 001 at center behind raining with dis

    si "「Is there anything else? 」"
    fn "「Let's see,{w=.2} done,{w=.2} done,{w=.2}\n\ \ so it should all be done after this last one?{p}\ \ Oh, there's also a whetstone on the list. 」"
    si "「A whetstone? 」"
    fn "「I remember the kitchen knives dulling a bit lately. 」"

    show si 004 with dis

    si "「Oh, then you can go to Kounosuke's for that.{p}\ \ {nw}"
    show si 001 with dis
    extend "The time's right, so maybe\n\ \ you can accompany me for my stuff. 」"
    fn "「Of course. 」"
    
    scene black with dis
    pause 1
    scene kouno_house_in
    show over black
    show ko 001 at center
    with dis
    play sound tm2_slidedoor000
    play music free02
    $ renpy.music.set_volume(0.7, 0.0, channel = "music")

    ko "「Yes, welco...{p}\ \ {nw}"
    show ko 003 with dis
    extend "Oh, Shin-kun and [fn].\n\ \ What's up? 」"
    si "「I came to pick up what I asked for on the phone. 」"
    fn "「I came to buy a whetstone. 」"

    show ko 001 with dis

    ko "「A whetstone?{w} They're on that shelf. 」"

    hide ko with wipe_right
    
    "The shelf he pointed out had big, small,\nround, and handle-attached whetstones.\nThe variety's a lot bigger than I figured."
    "Is a whetstone not a whetstone?{p}It doesn't matter which one I buy."
    fn "「Uhh...? 」"
    "It's for knife-sharpening,\nso maybe this rectangular one?"
    "Then again,\nthis smaller one with a handle attached\nto it looks easy to use."
    
    show ko 001 at midright with dis

    ko "「What's wrong? 」"
    fn "「What's the best way to use this for sharpening? 」"

    show ko 005 with dis

    ko "「Whatever's easiest, I guess. 」"

    show si 001 behind ko at midleft with dis

    si "「I wrote it down on a memo,\n\ \ but maybe what I left at home is broken? 」"

    show ko 001 with dis
    
    ko "「Oh, is it?{p}\ \ {nw}"
    show ko 003 with dis
    extend "Then, how about this one? 」"
    "And so, Kounosuke picked up a two-layered\nblack and gray whetstone.{p}Huh. So this is for sharpening."
    fn "「I see, there isn't just one kind of whetstone. 」"

    show ko 004 with dis

    ko "「The size and toughness can change their use,\n\ \ but I guess some are for rough work\n\ \ and some for finishing? 」"
    ko "「Oh, and the round ones are for grinding. 」"

    show ko 001 with dis

    ko "「There are people who obsess over the differences,\n\ \ but most people just use whatever they're used to. 」"

    show ko 003 with dis

    ko "「By the way, the toughness on this one is different\n\ \ on each side, and it's your grandma's favorite. 」"
    ko "「The rough side for sharpening,\n\ \ the soft side for finishing. 」"
    fn "「Uh-huh. 」"
    "I guess I really won't be using\ncountryside knife sharpeners."
    si "「Anyways, wouldn't it be better to bring\n\ \ the knife itself here and get it sharpened?{p}\ \ It's what I always do. 」"
    fn "「Really? 」"

    show ko 004 with dis

    ko "「We can't really ask money for that, so it's free. 」"
    ko "「Besides knives,{w=.2} there's scissors,{w=.2}\n\ \ sickles,{w=.2} hoes,{w=.2} saws,{w=.2} lawn cutters,{w=.2}\n\ \ and other convenient edged things. 」"

    show ko 003 with dis

    ko "「I think Shin's the only one who brings\n\ \ things here for sharpening though. 」"

    si "{cps=10}「...{cps=40}{w}{nw}\n\ \ "
    show si 010 with dis
    extend "really? 」"

    show ko 001 with dis

    ko "「Yeah. 」"

    show si 003 with dis

    si "「Why didn't you tell me that earlier? 」"

    show ko 002 with dis

    ko "「Well it's not like there's any reason to refuse.{p}\ \ Actually why don't we take an official business tour?{p}\ \ You can pay in tea and snacks. 」"
    si "「I must respectfully decline.{p}\ \ That aside, I also came here to ask\n\ \ something about what I requested repairs on? 」"

    show ko 001 with dis

    ko "「Oh, the hand mixer?\n\ \ Just a sec.{p}\ \ {nw}"
    show ko at midright_down with qdis
    show ko at tilting
    extend "Uh...{w=.2}A-103,{w=.2} A-103... 」"
    
    hide ko with dis

    "Kounosuke dived behind the counter\nas he muttered those numbers,"
    "and before long he pulled out a cardboard box\nlabeled A-103 and placed it on the counter."
    
    show ko 001 at midright with dis

    ko "「Here it is.{p}\ \ Would you like to confirm\n\ \ everything for yourself? 」"
    "Shin-kun nodded in silence as he recieved the box,\nthen sifted through the contents to check."
    "The way things were going, I felt like\nthis was an exchange with the mafia."

    show ko 003 with dis

    ko "「There's a one-year warranty.{p}\ \ {nw}"
    show ko 004 with dis
    extend "Still, isn't it about time to get a new one? 」"
    ko "「I look at it, and it feels like\n\ \ it's been used for a long time 」"

    show si 004 with dis

    si "「It actually hasn't been used much.{p}\ \ It's helpful as an auxiliary tool,\n\ \ so there's not much need to get a new one. 」"

    show ko 001 with dis

    ko "「Huh. 」"
    fn "「I didn't know you could fix those here too. 」"
    
    show si 001
    show ko 005
    with dis

    ko "「Sometimes.\n\ \ We normally do farm tool fixing and selling. 」"
    ko "「We can't fix something this small,\n\ \ so we have to take it all the way to town. 」"

    show ko 001 with dis

    ko "「We take an intermediation fee, kinda?{p}\ \ {nw}"
    show ko 004 with dis
    extend "]Well, I can take it apart and put it back,\n\ \ but if it's one of a kind I can't fix it. 」"
    fn "「Can you fix it...? 」"

    show ko 003 with dis

    ko "「If I can figure out the internal structure... 」"

    show ko 004 with dis

    ko "「Oh well,\n\ \ I haven't actually taken apart a lawn mower's\n\ \ engine or a hand mixer before though. 」"
    
    show si 004 with dis
    
    "Uh, okay then...{p}Well that was reassuring."
    "Is Shin-kun used to this?\nHe's looking so calm ignoring all this."
    
    show si 001 with dis

    si "「In that case, I'm going home.{p}\ \ How about you [fn]? 」"
    fn "「I... 」"

    menu:
        "A. Stay and talk with Kounouske":
            jump shin11_stay
        "B. Leave with Shin":
            jump shin11_leave

    ###########################################
    label shin11_stay:

        $ love_shin -= 1
        $ love_kounosuke += 1 #!#This shouldn't be negative, right?
    
        fn "「I'll go after talking with Kounosuke a bit. 」"
    
        show ko 002 with dis
    
        ko "「Oh, really?{p}\ \ Cool, I was bored out of my mind tending the store. 」"
        si "「...aren't you in the middle of your errands? 」"
        fn "「Ah... 」"
    
        show si 004 with dis
    
        si "「Well, it's fine.{p}\ \ {nw}"
        show si 001 with dis
        extend "See you. 」"
        fn "「Later. 」"
        ko "「See ya. 」"
    
        hide si with wipe_right
        play sound tm2_slidedoor000
    
        fn "「Uhh... 」"
        "Staying is fine and all,\nbut I really do have errands.{p}The bag is getting heavy too."
        fn "「Sorry, I guess I will go home after all. 」"
    
        show ko 005 with dis
    
        ko "「Whaaat? 」"
        fn "「I'll come again after putting these away.{p}\ \ There's fresh stuff that might bruise here too. 」"
    
        show ko 001 with dis
    
        ko "「Oh.{p}\ \ {nw}"
        show ko 003 with dis
        extend "Well you are coming again, right? 」"
        fn "「Yeah. 」"
    
        show ko 002 with dis
    
        ko "「Okay then.{p}\ \ I'll be waiting, so come back soon. 」"
        fn "「Right, see you in a bit. 」"
        
        play sound tm2_slidedoor000
        stop music fadeout .8
        scene black with Dissolve(1)
        play music rainfall
        pause 1
    
        "Well, so I promised Kounosuke,\nbut just as I got back the rain picked up hard,\nso in the end I couldn't go back to Kounosuke's house."
        "Instead,"
        
        play sound phone_pickup
        $ renpy.music.set_volume(0.3, 0.2, channel = "music")
        pause .2
        scene hentry night with dis
    
        ko "「It's fine, the weather sucks after all.{p}\ \ I'd be worried if you forced yourself. 」"
        ko "「But anyways,\n\ \ is there any fashionable food over there?{p}\ \ Something that goes well with bagels? 」"
        ko "「...what?{w=.2} Am I wrong?{p}\ \ I'm a real fan of donuts and... 」"
        "And just like this as the rain poured,\nI spent the afternoon on the phone with Kounosuke."
    
        jump end11
    
    #########################################
    label shin11_leave:

        $ love_kounosuke -= 1
        $ love_shin += 1
    
        fn "「I have to get going.{p}\ \ I was doing errands and all. 」"
    
        show ko 001 with dis
    
        ko "「Oh, okay then. 」"
        si "「See you later then. 」"
        fn "「Later, Kounosuke. 」"
    
        show ko 003 with dis
    
        ko "「See you two. 」"
        
        play sound tm2_slidedoor000
        stop music fadeout .8
        scene black with dis
        pause .5
        call rain_set from _call_rain_set_1
        scene path 
        show over black
        show raining
        with dis  
        play music rainfall
        $ renpy.music.set_volume(0.65, 0.0, channel = "music")
    
        "I walked alongside Shin-kun, here in rainy Minasato."
        "If possible I'd like to get used to a closer\ndistance all casually, but with the umbrellas\nin the way we had to stay apart more."
        "However, there weren't many people around,\nso it was enjoyable with the mood just between us."
        "The rain fell peacefully,\nalmost like quiet ambient BGM."
        
        show si 010 at center behind raining with dis
    
        si "「'S'il pleut vendredi,\n\ \ il pleuvra aussi sans doute dimanche.' 」"
        fn "「Wait, what? 」"
    
        show si 001 with dis
    
        si "「Oh, sorry.{p}\ \ There was a line I read in a book the other day. 」"
        si "「It went 'If it rains on Friday,\n\ \ it may rain on Sunday too.' 」"
        fn "「So what's that mean? 」"
    
        show si 004 with dis
    
        si "「Who knows?\n\ \ It sounds like a proverb from another country. 」"
        si "「But at the end,\n\ \ the protagonist muttered it to himself. 」"
        si "「I thought if it did rain two days later,\n\ \ I'd be depressed. 」"
        fn "「Yeah, that's true.{p}\ \ It'd be a rain of mercy for the crops though. 」"
    
        show si 001 with dis
    
        si "「It's not like I hate the sound of rain.{p}\ \ {nw}"
        show si 010 with dis
        extend "Still, I don't like being wet. 」"
        
        $ renpy.music.set_volume(0.8, 0.1, channel = "music")
    
        "As the passing rain grew stronger,\nour own pace hastened,\nand we hurried on home on this rainy day."
    
        scene black with dis
        pause .5
        
        "The rain got even heavier when I got back,\nand even with the umbrellas\nmy lower half was soaking wet."
        "As I wiped off and changed my clothes,\nI suddenly wondered how Shin-kun was\ndoing, so I called up his house."
        
        play sound phone_pickup
        $ renpy.music.set_volume(0.3, 0.2, channel = "music")
        pause .2
        scene hentry night with dis
    
        si "「The weather really is horrible out.\n\ \ Are you okay over there?{w} ...I see, that's good.{p}\ \ Oh, wait a moment. 」"
        si "{size=-10}(I know! I'll go in soon, just wait!)"
        si "「Sorry, I just got back and I haven't changed out.\n\ \ Maybe next time we'll have more time.{p}\ \ ...yes.{w=.2} Good bye. 」"
    
        jump end11
    
####################################################
label juuichi11:

    $ event_name = _("The Library has a ominous scent")
    $ love_juuichi += 1
    $ focus_character = "juuichi"

    scene map
    hide screen marketplace11    
    scene black 
    scene hbroom with Dissolve(.5)
    play music cicada01
    
    fn "「Man, it's so hot... 」"
    "I mutter weakly to myself,\nlooking away from my English book."
    "I haven't been doing a very good job keeping up\nwith my homework,{w=.2}\nbut every once in a while I feel like trying."
    "I look back at my book as\nI wipe the sweat off my brow."
    "Usually the words go into my head pretty easily,\nbut I seem to be having a hard time today."
    "Umm, 'that' is a relative pronoun,{w=.2}\nso you have to read the following English sentence\nas one large part..."
    "Come to think of it, my teacher would say\n'one large part' like it was nothing,\nbut it feels indecent when I try to say it."
    "Large and hard,{w=.2} like a man's crotch...{w=.3}\nNo, no, I can't be thinking things like that."
    "Ahh, I need to stop that.{p}I accidentally started having erotic thoughts.{p}I shake my head, and return to my homework."
    "'As soon as possible'? What did that mean again?{p}{nw}"
    play sound paper00
    extend "{w=.3}{nw}"
    play sound paper00
    extend "I flip through my dictionary,\nand run my finger over the relevant part."
    "Uhh, what?{cps=15} ...As soon as one can?{p}This can also be abbreviated as A.S.A.P?"
    "{cps=15}People in English-speaking countries just\nabbreviate whatever they want, huh?"
    "{cps=15}It sounds like the name of a special forces group.{p}{nw}"
    play sound freeze04
    extend "'We need the A.S.A.P as soon as possible!'"
    "{cps=15}Ha, without even realising this,\nI've gotten off track!{p}What was I doing?"
    
    fn "「It's so hot, I can't concentrate at all... 」"
    "I{cps=15} used up the remainder of\nmy strength in this one phrase."
    "{cps=15}There's no air conditioner in my grandpa's house.{p}That means I have to study in this unrelenting heat.{p}In other words...{cps=40} It's impossible."
    "Now my proof is finished... Wait,{w=.2}\nI'm doing English homework, not math."
    fn "「Aah, cut that out! 」"
    
    play sound book_close
    
    "I slam my reference book shut,\nand lay down in defeat on the floor."
    "Was I mistaken from the beginning\nby thinking that I could study in this heat?"
    "I need to take refuge somewhere cool.{p}Somewhere very, very cool."
    "A pool.{p}I'd go jump in one right now,\nbut I can't really study in one."
    "The graveyard.{p}It'd probably send shivers down my spine...\nBut there aren't any desks there."
    "Study on a grave?{p}If I did such a disrepectful thing,\nI'd be cursed all the way to my grandchildren."
    "No way."
    "The library!{p}It's a cool, quiet, air-conditioned place.{p}Plus, the only thing I can do there is study."
    "...I can't believe I didn't think of that first.{w=.2}\nThis heat must be really wearing me out."
    "I stuff all of my study materials into my bag.{p}...I guess it's time to go now?{p}{nw}"
    play sound standup
    extend "I slowly stand up."

    stop music fadeout 2
    scene black with Dissolve(1)
    pause 1
    play music tam_n06
    scene library with Dissolve(1)

    $ event_name = _("The Pleasantly Cool Place")

    "...So.{p}Here I am, at the library."
    "The room is chilled by the\nwonders of modern society.{w=.2}\nIt welcomes me, as though I've been blessed."
    "Well, it was worth waiting 30 minutes for the bus.{p}Air conditioning, I love you!{p}I cheerfully make my way into the building."
    who "「I'm surprised to meet you in a place like this. 」"
    
    play sound bom26_b
    
    fn "{size=+15}「Gyaaah! 」" #!#Make text box shake
    "A voice says my name from behind me,{w=.2}\nmaking me cry out in surprise.{p}I try to close my mouth, but I'm too slow."
    
    play sound freeze04
    
    "Oops."
    "A-ahaha, everybody around me is staring.{p}That's what happens when you yell in a library..."
    fn "「S-sorry... 」"
    "I quietly apologize to everyone.{p}I turn around to face the person who startled me,{w=.2}\nand find Shin-kun there, looking shocked."
    
    show si 010 at center with dis
    
    "Do I look sad like this?{p}Or is him scaring me part of the cause."
    "...Ooh, his cold eyes cutting into me hurt.{p}What do you think I'd do, Shin-kun?!"
    
    show si 004 with dis

    si "「You're supposed to be quiet in the library.{w=.2}\n\ \ Weren't you taught that in elementary school? 」"
    fn "「Yes... 」"
    
    show si 001 with dis

    si "「Then try demonstrating your knowledge. 」"
    fn "「Yes... 」"
    "...Oh man, I'm getting really chewed out."
    "I'm like an ex-friend mince pie.{p}Or a bloody soup of small mushrooms."
    "More and more horrible dishes come to mind,\npassing in front of my eyes.{p}Help me, Gyoza fairy!"

    show si 003 with dis

    si "「Well, that's how you usually are. 」"
    who "「What's wrong with maintaining the status quo? 」"
    "A hand of salvation, not from a fairy,{w=.2}\nis extended to me."
    "The face of a familiar bear shows up.{p}It's Juuichi-san, here to put an end to\nShin-kun's drawn-out sermon."
    
    hide si with wipe_right
    
    show si 003 at midright
    show ju 001 at midleft
    with wipe_right

    fn "「Oh, Juuichi-san.{w=.2} Good afternoon. 」"
    "He raises his hand in response.{p}I-I've been saved.{p}Shin-kun is really merciless at times like these."
    
    show si 004 with dis

    si "「...Well,{w=.2} whatever. 」"
    "He suddenly turns away.\nWe must have hit a sore spot."
    "Silence."
    "More silence."
    "Even more silence."
    "...This is awkward. Too awkward.{p}{nw}"
    show ju 008 with dis
    extend "I glance over at Juuichi-san, and he looks troubled\nwhile scratching his cheek."
    "His expression tells me that we'd\nbest leave sleeping dogs lie.\nNo reinforcements. We're stranded."
    "I need to get back on Shin-kun's good side.{p}It wouldn't be good for him to\nbe in a bad mood all summer."
    fn "「So, what book are you taking out? 」"
    
    scene library with wipe_right
    show si 001 at center with wipe_right

    si "「{cps=15}...{cps=40}This one. 」"
    "Although it took some time for the words to come,{w=.2}\nShin-kun bluntly hands his nook to me.{p}Mentally, I strike a triumphant pose."
    fn "「...What's this? 」"
    "My feeling of accomplishment is destroyed,{w=.2}\nthe instant I take a look at the book."
    "It's an old-fashioned hardcover. That's fine.{p}The problem is that it's obviously written\nin a language that isn't English."
    
    play sound paper00
    pause .2
    play sound paper00

    "I flip through the pages,\nbut it's impossible for me to decipher."
    "Firstly, I don't get these slash and dot symbols.{p}I think these are European letters..."
    "...Oh, that reminds me.{p}Now that I think about it, I finally realize.{p}Shin-kun's mother is from France, isn't she?"
    fn "「What is this, Shin-kun? 」"
    si "「It's exactly what you think it is. 」"
    fn "「French...? 」"

    show si 002 with dis

    si "「Oui, c'est juste. 」"
    "His expression softens a little."
    "I think those were words of confirmation..."

    show si 001 with dis
    
    si "「This place has foreign language books too.{p}\ \ I read French regularly to keep my skills up. 」"
    si "「I'd like to have a conversation in French\n\ \ after reading it...{w} Amaki doesn't speak it, though.{p}\ \ I suppose that's a bit of a minor problem. 」"
    fn "「Oh, I see... 」"
    "Unlike English, I rarely even experience French...{p}I guess you have to do that to stay at his level."
    "I used to think it was amazing\nhe could speak French,{p}but I guess it was the result of hard work."
    si "「Well, enough about me.{p}\ \ ...Why did you come to the library? 」"
    "He turns the question on me.{p}Wow, I got him into a better mood, didn't I?{p}It's rare that he uses one of my questions."
    
    show si 004 with dis

    si "「You're not much of a reader, are you? 」"
    "He sank my battleship.{p}A harsh blow from Shin-kun..."
    fn "「I'm actually very delicate and pure!{p}\ \ It makes me cry when you say things like that! 」 "

    show si 010 with dis

    si     "「... 」"
    "He glares at me."
    "...Don't look at me with such cold eyes.{p}It was just a little joke, okay?"
    fn "「...Ahem, I'm working on my homework.{p}\ \ There's no air conditioning at home,\n\ \ so I couldn't concentrate. 」"
    
    show si 001 with dis
 
    si "「That's what I thought. 」"
    "If you already knew, then why did you ask..."
    fn "「Juuichi-san, are you taking out a book too? 」"
    "I speak to Juuichi-san, who has been\nstanding there this whole time."
    
    hide si with wipe_right
    show ju 001 at center with wipe_right

    ju "「Yes, that's right.{p}\ \ A new book in the 'Soft and Fair Goes Far'\n\ \ series has is out. 」"
    "Wait, what?{p}Without thinking, I ask him to repeat himself."

    show ju 006 with dis

    ju "「'Soft and Fair Goes Far'. 」"
    fn "「Uhh, you can get porn at the library? 」{w}{nw}"    
    play sound hit_p00
    show ju 011 with dis
    show library at hshake #Needs to for one sec
    #extend "{w=.25}{nw}"

    "Juuichi-san strikes me with full force.{p}My field of vision goes black for a moment."
    "Ow... I was just joking around.{p}It seems he didn't take it that way, though."
    "Torahiko gets this every day,{w=.2}\nand he just takes it like it's nothing..."
    "It even seems like he enjoys\ntheir little back-and-forths.\nI wonder if this is what they call 'harmony'?"
    "As I look over to Juuichi to talk about that,{w=.2}\n{nw}"
    show ju 001 with dis
    extend "he glares at me, and looks like he wants to say\nsomething.{w} I quickly change the subject."
    fn "「A-ahem!{p}\ \ By the way, Shin-kun, do you play any sports? 」"
    
    hide ju with wipe_right
    
    show si 005 at midright
    show ju 001 at midleft
    with wipe_right

    si "「...Me? 」"
    fn "「Yeah.{p}\ \ I think sports would be something you'd like. 」"
    "Shin-kun looks confused."
    "...Of course he would be.\nSorry for using you,\nI'll treat you to something nice some time."
    
    show si 004 with dis
    
    si "「...I'm not particularly into sports, though. 」"
    "I'm being awfully forward right now,{w=.2}\nbut I'm in the clear now... Right?"
    
    show si 001 with dis
    stop music fadeout 7

    si "「Well, that aside, I'd like to try one.{p}\ \ What would you recommend? 」"
    fn "「R-recommend...? 」"
    
    play sound wind_noise
    
    "Crap, I didn't think of that.{p}I didn't think things would go this way.{p}I'm sweating, despite the cool air."
    
    show ju 008 with dis

    ju "「...No matter what you choose, you'll need strength.{p}\ \ Remember that, if you plan on\n\ \ playing with [ln]. 」"
    "A fatal blow from Juuichi-san..."
    "I rummage around my bag,{w=.2}\nand pull out three cards.{p}I fan them out, and hold them up in front of me."
    "'Safe Answer'{p}'Appropriate Answer'{p}'Evade'"
    "Those are my three options."
    "Which one?{p}Which one do I choose?!"
    
    menu:
        "A. Recommend Tennis.":
            jump juuichi11_tennis
        "B. Recommend Swimming.":
            jump juuichi11_swimming
        "C. Dodge the question.":
            jump juuichi11_dodge

    #########################################
    label juuichi11_tennis:

        $ event_name = _("Aim For the Prince of Tennis")
        $ love_juuichi += 1
        $ love_shin += 1
        
        "I steel myself, and select one.{p}The 'safe answer' card."
        
        play music free21
        
        fn "「Tennis would be a good match for you, wouldn't it? 」"
        si "「Tennis? 」"
        fn "「That's right.{w} It's not like soccer,\n\ \ where you're running around all the time,\n\ \ so I think it'd suit you. 」"
        "...I can't believe what I'm saying.{p}It's like getting a burst of strength\nat the scene of a disaster."
        "It remains to be seen whether or not\nI have the strength for this situation."
        
        show ju 003 with dis
    
        ju "「I think tennis is a pretty intense sport, though- 」"
        "I quickly close Juuichi-san's mouth,\nbefore he says too much."
        "It seems he's still trying to speak,\nbut his voice is too muffled to be heard.{p}Okay, he's stopped."
    
        show si 004 with dis
    
        si "「... 」"
        "Shin-kun has his hand on his chin,\nand seems to be in deeo thought.{p}Hm, I'll need to give him another push."
        fn "「I think you'd look good in tennis wear, too. 」"
        "A pure white polo shirt, and large shorts.{p}Those would go great with his black fur."
    
        show si 001 with dis
        
        "「Sorry, but tennis is out of the question. 」"
        "Furthermore, you could get a peek\nof his underwear up his shorts!{p}The demand for this must be through the roof!"
        
        $ renpy.music.set_volume(0.0, 2.0, channel = "music")
    
        "...Wait, did he just say it's out of the question?"
        fn "「O-out of the question...? 」"
        si "「I say that because I avoid\n\ \ long periods of exercise. 」"
        
        play sound shock1
        
        "..."
        si "「I moved to Minasato for medical treatment.{p}\ \ I think I'm all right for the most part, though. 」"
        si "「If I want to do something that requires strength,\n\ \ I need to think about it first. 」"
        "It was such a good idea, though...{p}I hung my head in defeat."
        
        $ renpy.music.set_volume(0.85, 2.0, channel = "music")
    
        show ju 001 with dis
    
        ju "「How about you go talk to Takahara about it?{p}\ \ He should be finishing up with his club about now. 」"
        si "「All right then, I'll give it a try.{p}\ \ ...Now, if you'll excuse me. 」"
        ju "「Later. 」"
        
        show ju at move_center(0.5)
        show si at move_offleft(0.5)
    
        "The automatic door slides open,\nand Shin-kun steps outside."
        "Since the light out there blinds me,\nI can't see him leave."
        
        hide shin
    
        ju "「Hey, [ln]. 」"
        "While I'm feeling discouraged,\nJuuichi-san speaks to me."
        fn "「...What? 」"
    
        show ju 003 with dis
    
        ju "「Do you want to go somewhere to relax? 」"
        "His kindness pierces me.{p}Without thinking, I hug Juuichi-san."
        fn "「Juuichi-san...! 」"
        
        show ju 014 at jump_up
    
        ju "「Don't hug me in here.{p}\ \ {nw}"
        show ju 003 with dis
        extend "You've got a runny nose. 」"
        "...Is that all he's worried about?"
        "Juuichi-san peels me off him,{w=.2}\nand briskly exits the same way Shin-kun did."
        
        show ju at move_offright(0.25)
    
        fn "「Aah,{w=.2} please wait! 」"
        "I quickly chase after him."
        
        stop music fadeout 2
        scene black with Dissolve(1)
        
        "...It wasn't until I got home and said goodbye to\nJuuichi-san that I realized I had completely\nforgotten to do my homework."
    
        jump end11
        
    #############################################
    label juuichi11_swimming:

        $ event_name = _("120% Wrath")
        $ love_shin -= 1
        $ love_juuichi -= 1
        
        "I steel myself, and select one.{p}The 'appropriate answer' card."
        fn "「You like swimming, don't you? 」"
        
        play music ambience01
        show si 006 with dis
    
        si "「Swim...{w} ming? 」"
    
        show si 003 with dis
        
        "Huh? His expression looks more grim.{p}However, the die has been cast.\nI can't re-roll."
        "I fearfully continue to speak."
        fn "「Yeah, swimming.{p}\ \ It doesn't put too much strain on your body,{w=.2}\n\ \ so that'd be best for you, wouldn't it? 」"
        
        show ju 011 with dis
    
        ju "「[ln]... 」"
        "Juuichi-san gives me a stern look.{p}...It seems that I made the wrong choice."
        
        show si 012 with dis
    
        si "「Whatever.\n...I'm going home. 」"
        fn "「Sh-Shin-kun...? 」"
        
        play sound step03
        show ju at move_center(0.25)
        show si at move_offright(0.25)
        
        "While I'm confused about this sudden declaration,{w=.2}\nShin-kun quickly exits the library.{p}He doesn't look back."
        "Did I just offend him...?"
        fn "「J-Juuichi-san...? 」"
        "I look towards him, begging for his help."
        
        show ju 006 with dis
    
        ju "「How stupid can you get? 」"
        "I've made Juuichi-san angry, too.{p}But why did Shin-kun get so worked up?\nI still don't understand..."
        "Reading my expression,{w=.2}\nJuuichi-san sighs deeply."
    
        show ju 001 with dis
        
        ju "「Kuroi can't swim.{p}\ \ ...How could you forget something like that? 」"
        fn "「Oh. 」"
        "Now that I think about it, Shin-kun never did Swim.{p}When we had swimming lessons in elementary school,\nhe always watched from the side."
        
        show ju 003 with dis
    
        ju "「Judging by your expression,\n\ \ you just remembered... 」"
        fn "「...I completely forgot. 」"
        
        show ju 011 with dis
    
        ju "「...{p}\ \ Make sure you apologize,\n\ \ the next time you see him. 」"
        
        show ju at offright with regmove
        
        "Juuichi-san leaves as he says that.{p}I'm the only one left in the library."
        "I should've thought about that more seriously.{p}Ah well, no use crying over spilt milk...\nIt's too late now."
        
        stop music fadeout 2
        scene black with Dissolve(1)
        
        "I didn't study, either.{p}In the end, I spent the rest of\nthe day feeling pretty bad."
    
        jump end11
    
    ###########################################
    label juuichi11_dodge:

        $ event_name = _("The Impertinent, Salty Taste of Youth")
        $ love_juuichi -= 1
        
        "I steel myself, and select one.{p}The 'evade' card."
    
        play music free0258
    
        fn "「B-but you're moving your\n\ \ hand every day, aren't you? 」"
        "I make a circle with my thumb and index finger,\nand flick my wrist.{p}This is what's called a gesture."
    
        show si 005 with dis
    
        si "「What? 」"
        "My crazy talk makes him roll his eyes.{p}I'm pushing the envelope here.{w=.2}\nI have to do it, though."
        fn "「You know,{w=.2} your hand. 」"
        
        show si 001 with dis
    
        si "「...Well,{w=.2} I certainly do move it. 」"
        fn "「I know, right?{p}\ \ And your hand is tired after you're done. 」"
        si "「Yes... It really is tiring,\n\ \ if you do it several times a day. 」"
    
        show ju 004 with dis
    
        fn "「That's why it's an unexpected form of exercise! 」"
        
        show si 010 with dis
    
        si "「...{p}\ \ {nw}"
        show si 001 with dis
        extend "Let's leave it at that. 」"
        "Was that too ridiculous to refute,\neven for Shin-kun?{w=.2}\nThat was a really curt reply."
        "Well, it seems I was somehow able to evade."
        
        play music free44
    
        ju "「Hey, [ln]... 」"
        "Seems I'm not quite out of this yet.{p}After staying quiet for so long,\nJuuichi-san joins the conversation."
        "Hm?{p}Why is his face so red?{p}What's wrong? Is he hot, too?"
        ju "「It really isn't so bad to do, is it? 」"
        fn "「Huh? 」"
        ju "「It's not something usually discussed in public. 」"
        "I don't get what he's going on about.{p}What the heck is he talking about?"
        "I wasn't planning on talking about anything odd..."
        fn "「Juuichi-san,{w=.2} what are you talking about? 」"
        "His face turns even more red.{p}He whispers something,\nbut I'm barely able to hear it."
    
        ju "「{size=-10}{cps=5}Mas...{cps=40}{size=+10}\n\ \ We shouldn't talk about it in a place like this. 」"
        
        play sound puu46
        show ju at shrink(0.8, 1) #!#Check to see if this shrinks him down to 80%
        
        fn "「Mas?{p}\ \ What's 'mas'? 」"
        "I missed most of his whisper.{p}He looks like he's going to cry.{p}Wow, that's a rare expression for him."
        "Since I have no idea what this 'mas' is,\nI continue to question him."
        
        ju "「You know... {size=-10}{cps=10}Mas..."
        
        play sound puu46
        show ju at shrink(0.5, 1) #!#Check to zoom to 50%
    
        fn "「I can't hear you. 」"
        "It's like every single one of my words\nis a death sentence to him."
        "But, since I ask him once more,\nhe has no other choice."
        
        #[eval exp="kag.bgm.currentBuffer.flags[0]=1;"] #!#Figure out what this flag does........
    
        show ju at shivering
        
        ju "「{cps=5}Mas... 」"
    
        play sound puu46
        show ju at shrink(0.3, .5)
        pause .5
        show ju at shivering
    
        fn "「Mass? 」"
        "Is he talking about weight?{p}But that has nothing to do with my\nconversation with Shin-kun."
        "Then, suddenly..."
        
        play sound hit78
        show ju at still
    
        "Crack.{p}I'm sure I heard the sound of something snap."
        
        play sound don08
        #!#shake screen
        show ju 007 at shrink(1.3, .5)
    
        ju "{size=+15}「Masturbate! 」"
        ju "{size=+15} 「It's something healthy\n\ \ young men do every day!! 」"
        
        stop music
        
        #[eval exp="kag.bgm.currentBuffer.flags.reset();"]
    
        fn "「... 」"
        si "「... 」"
        bystanders "「... 」"
        
        play sound wind_noise
        
        "Everybody in the library freezes."
        "Juuichi-san clamps his mouth shut,\nbut it's too late.{p}All eyes are on him."
        fn "「{cps=15}...{cps=40}Uhh, Shin-kun and I were\n\ \ talking about writing. 」"
        "Shin-kun nods."
        
        hide ju
        show ju 015 at midleft
        with dis
    
        ju "「...Huh? 」"
        "Juuichi-san stands frozen in place, his mouth agape."
        fn "「Your fingers and arm get tired from holding a\n\ \ pencil for a long time, right?{p}\ \ Your head, too. 」"
        
        show si 004 with dis
    
        si "「Some days, I study for hours at a time. 」"
        ju "「B-{w=.2}but,{w=.2} that motion you were making... 」"
        fn "「What?{p}That was supposed to be writing... 」"
        "I make the gesture again."
        "...Oh.{p}I finally understand what caused\nJuuichi-san's misunderstanding."
        "I waved my arm parallel towards Shin-kun.{p}From where Juuichi-san is standing,{w=.2}\nIt looked like it was moving vertically."
        "...It really does look just like that."
        fn "「...Sorry,{w=.2} Juuichi-san. 」"
        "I don't mean to say it was my fault,{w=.2}\nbut I feel like I should apologize to him."
        
        show si 010 with dis
        
        "Shin-kun doesn't say anything from a mix of shock,\nsympathy, and disappointment,\nand looks at Juuichi-san."
        "If he were looking at me with that expression,\nI don't think I'd be able to live with myself..."
        "If that were the case,{p}I think I'd rather him call me an unwashed mongrel."
        "After such a scornful expression from Shin-kun,\nJuuichi-san is at a complete loss for words.{p}...I suppose that's to be expected."
        si "「...My condolences. 」"
        
        play sound hit81
        show ju at jump_up
        
        "With those words,\nShin-kun delivers his final blow to Juuichi-san."
        "Staggering like a zombie,\nhe heads towards the library entrance."
        "A young woman walking in his direction\nquickly avoids him.\nHe runs off, shouting something."
        
        show ju at move_offleft(0.25)
        show si 001 with dis
        
        "An icy silence falls on the library."
        
        hide ju
        
        fn "「Th-the next time I see him,\n\ \ I'll have to bring him a box of sweets. 」"
        si "「I think I should too{cps=15}...{cps=40} Right? 」"
        fn "「Yeah{cps=15}...{cps=40}Let's get out of here. 」"
        "We decide to leave as quickly as possible, too.{p}Man, jumping to conclusions really screwed\nJuuichi-san over..."
        
        scene black with wipeleft
        
        "It wasn't until I got home and said goodbye to\nShin-kun that I realized I had completely\nforgotten to do my homework."
    
        jump end11

####################################################
label tatsuki11:

    $ love_tatsuki += 1
    $ focus_character = "tatsuki"
    $ event_name = _("Fireworks Gathering")

    scene map
    hide screen riverbed11
    stop music fadeout .8
    scene black with wipe_dr
    play music river_flow fadein 3
    scene river red with Dissolve(1)
    
    "I heard we're having a fireworks\nmeeting today.{p}Are we getting together around here?"
    "It's been so long since we set off\nfireworks together.{w} There aren't many places\nto do it in the city."
    
    show ta 001 red at center with dis

    ta "「You're late,{w=.2} [fn]. 」"
    
    show su 002 red at midright with dis

    su "「You came late, [fn]-saaaaan. 」"
    "I go over to the dry riverbed,\nwhere everyone already is.{p}Seems like I'm the last to arrive."
    fn "「And all that, even after running\nall the way here. 」"

    scene river red with wipeleft
    show to 002 red at center with wipeleft

    to "「Have you been getting soft from\n\ \ living in the city?{p}\ \ That must be why you haven't gotten any taller. 」"
    fn "「It's not that I'm short, it's\n\ \ that you're too tall, Torahiko. 」"
    
    show ko 003 red at farright with wipe_right

    ko "「Ahaha!{w=.2} You have grown a lot. 」"
    
    show si 001 red at farleft with wipe_right

    si "「Anyway, it's still light out,\n\ \ but what should we do? 」"
    
    scene river red with wipeleft
    show ta 002 red at center with wiperight

    ta "「We should start off with shopping.{p}\ \ I'm collecting money for that. 」"
    
    scene black with dis

    "......"

    scene river red
    show to 001 red at midleft
    show so 001 red at midright
    with dis

    so "「Here's my part. 」"
    to "「Everyone's pitched in now,\n\ \ right? 」"
    
    scene river red with wipeleft
    show ka 002 red at midright with wipe_right

    ka "「We're going shopping, so what\n\ \ should we get? 」"
    
    show ta 002 red at midleft behind ka with wipeleft

    ta "「We need a bucket for the\n\ \ preparation, and after that we\n\ \ need to get fireworks and food."
    ta "And then we need sake. 」"
    
    scene river red with wipeleft
    show to 002 red at center with wipeleft

    to "「Hurry up and get those, then.{p}\ \ By the time you get back, the\n\ \ time should be perfect. 」"
    
    scene river red
    show to 002 red at midright
    show ju 001 red at midleft
    with wipeleft

    ju "「Hey, Tora, they aren't buying\n\ \ anything like a clock. 」"
    
    show to ray 01 red with dis

    to "「I get it.{w} It'll be all right if\n\ \ I get honey, yeah? 」"
    
    show ju 006 red with dis
    hide to with wipe_down
    show river red at hshake
    play sound bosu35
    
    "After Torahiko said that, Juuichi-san\nput him down with one perfectly-timed\nshoulder throw."
    "So fast...{w=.2} that's what you call smooth.{p}Torahiko couldn't even resist."
    
    hide ju with wipeleft

    fn "「Whoa.{w=.2} That looked like it hurt. 」"
    
    show ky 001 red with wipe_right

    ky "「He'll be fine, this happens all the time.{p}\ \ And sometimes, this doubles as practice,\n\ \ so Torahiko falls properly. 」"
    "Is that practice for a Manzai comedy\nroutine?"
    
    show ka 005 red at farright with wipe_right

    ka "「C'mon,{w=.2} it's not like they're going out,\n\ \ or whatever."
    ka "Aren't we supposed to finish the shopping\nquickly? 」"
    ky "「Yeah. Let's split up so one group gets{p}\ \ food and the other gets fireworks. 」"
    
    show su 002 red at midright with wipe_right

    su "「Woof!{p}\ \ Shopping with everyone! 」"
    
    scene river red with wipeleft
    show ta 002 red at center with wipeleft

    ta "「What'll you do,{w=.2} [fn]?\n\ \ Let's go together. 」"
    
    "Hmm.{w=.2} What should I do?"
    
    menu:
        "A. Summer is all about fireworks.":
            jump tatsuki11_fireworks
        "B. Go for practicality":
            jump tatsuki11_food

    ######################################
    label tatsuki11_fireworks:

        $ event_name = _("At the General Store")

        play music free53
    
        "I definitely should get fireworks.{p}I have to buy my own,{w=.2} right?"
        fn "「I'll go buy fireworks. 」"
    
        scene river red
        show ta 002 red at midright
        show to ray 01 red ay center
        with wipeleft
    
        ta "「All men should. 」"
    
        show to 002 red with dis
    
        to "「All right, it's decided.{p}\ \ Let's go then. 」"
        
        scene black with Dissolve(1)
        
        scene market red
        show to 001 red at midright
        with Dissolve(.5)
    
        to "「Next is the small stuff.{p}\ \ Getting that should be fine. 」"
        
        show ta 001 red at midleft behind to with wipeleft
    
        ta "「That's true, we can get most of it\n\ \ from the general store.{p}\ \ How about we go to the candy store next? 」"
        fn "「It's great that the general store had\n\ \ a set.{w} It's a pain going into town to shop,\n\ \ and it's gotten expensive. 」"
        
        scene market red with wipeleft
        show ka 005 red at midright with wipeleft
    
        ka "「If you'd said something earlier,\n\ \ we could have gotten something bigger. 」"
        
        show ko 003 red at midleft behind ka with wipeleft
    
        ko "「Kouya lives close to town, right? 」"
        ka "「We needed a plan or something...{p}\ \ When Tatsuki-san and Torahiko asked\n\ \ about what to do today, that was a bit too fast. 」"
        
        scene market red with wipeleft
        show su 002 red at center with wipeleft
    
        su "「But everyone is all together like this\n\ \ and shopping is so fun! 」"
        
        show ta 001 red at midright behind su with wipeleft
    
        ta "「Oh yeah, we could've asked Kouya.{p}\ \ Whatever, this is enough for the day.\n\ \ Off to the candy store. 」"
        
        scene candystoreout red with Dissolve(1)
        show su 001 red at midright with wipeleft
    
        su "「There's so much! Which should we get? 」"
    
        show ta 001 red at midleft behind su with wipeleft
        
        ta "「First we get the popular rockets.{p}\ \ Buy a bunch of those, then spend the rest\n\ \ equally on the other kinds. 」"
        "Hmm. I wonder if we can get some sweets, too."
        "We scattered around the candy shop.{p}After we were done shopping,\nwe gathered to check what we bought."
        
        scene candystoreout red with wipeleft
        show to 003 red at center with wipeleft
    
        to "「What are you talking about?{p}\ \ We picked the spark wheels. 」"
        
        show ka 001 red at farright with wipeleft
    
        ka "「No, it was the dragonfly. 」"
    
        show ko 003 red at farleft with wipeleft
    
        ko "「Oh, snake fireworks.{p}\ \ And some smoke bombs too. 」"
        
        show ko 001 red with dis
     
        ko "「It's so nostalgic...{p}\ \ Since we can't see them at night, we\n\ \ don't need any, right? 」"
        ka "「Nowadays, kids don't want spark wheels.{p}\ \ Even if it's called a fireflower, it\n\ \ doesn't look like one. 」"
    
        show to 002 red with dis
    
        to "「Heh. Dragonflies are so minor!{p}\ \ No one uses those. 」"
        "Why do I feel like I've seen this scene before..."
        "Torahiko and Kouya always fight over\nanything, but it's not like they\ncan't get along."
        "It'd be better if they didn't fight as often,\nthough."
        
        scene candystoreout red with wipeleft
        show ta 001 red at center with wipeleft
    
        ta "「Did we get a bunch of sparklers and rockets?{p}\ \ So we didn't need firecrackers after all. 」"
    
        show su 002 red at midright with wipeleft
    
        su "「Tatsuki-saaaan.{p}\ \ I want this one too. 」"
    
        scene candystoreout red with wipeleft
        
        show to 001 red at midleft
        show ka 001 red at midright 
        with wipeleft
    
        ka "「Dragonflies have a meaning, right?{p}\ \ They're different from the plain fireworks,\n\ \ and they don't make stupid noises. 」"
    
        show to 006 red with dis
    
        to "「Anyone can use spark wheels.{p}\ \ We know at least that much from the old\n\ \ days. 」"
        to "「There's a big difference between what you\n\ \ hear, and what you see. 」"
        fn "「Now, now, it's not like we can only do one\n\ \ of them today.{p}\ \ Calm down, you two. 」"
        
        show to 003 red with dis
    
        to "「Spark wheels fit the best for the fireworks\n\ \ gathering! 」"
        
        show ka 007 red with dis
    
        ka "「Dragonflies are the ones worth being the\n\ \ main event! 」"
    
        show to at jump_up
    
        to "「Spark wheels!!! 」"
    
        show ka at jump_up
    
        ka "「Dragonflies!!! 」"
    
        scene candystoreout red with wipeleft
        
        show ta 006 red at center 
        show ko 001 red at farleft
        show su 002 red at midright
        with wipeleft
    
        ta "「Hey, how long are you two gonna carry on\n\ \ like that?{p}\ \ We're done shopping, so we're going now. 」"
        su "「We got sooo much! 」"
        
        show ko 002 red with dis
    
        ko "「We got both kinds, so just relax. 」"
    
        scene candystoreout red
        show to 005 red at midleft
        show ka 007 red at midright
        with wipe_right
    
        to "「Huh? 」"
        ka "「Huh? 」"
        
        jump tatsuki11_showtime
    
    #############################################
    label tatsuki11_food:

        hide ta with Dissolve(1)
    
        "If I went to buy fireworks, that still\nwouldn't change anything on the inside."
        "In that case, it'd be better to go buy\nsomething to eat."
        fn "「I'm gonna go buy some food, since I'm\nhungry. 」"
        "It looks like everyone's decided which\ngroup they're going with."
        
        show ju 001 red at center with wipeleft
    
        ju "「Everyone's decided what they're\nbuying, right? 」"

        show ky 001 red at farright with wipeleft
     
        ky "「Shall we go, then? 」"
    
        show so 003 red at midright with wipeleft
    
        so "「Roger. 」"
        
        play music free02
        scene black with Dissolve(1)
        scene market red with Dissolve(.5)
    
        fn "「What should I get?{p}\ \ It's best not to buy too much, right? 」"
        
        show ky 001 red at center with wipeleft
    
        ky "「That's true, it's not like we're\n\ \ doing a barbeque."
        ky "Anyway, it should be enough for\n\ \ us to get drinks and some candy. 」"
    
        show so 001 red at midright with wipeleft
        
        so "「It'd be awesome if we got some\n\ \ watermelon. 」"
        
        show si 001 red at farright behind so with wipeleft
    
        si "「I'm fine with anything. 」"
        fn "「Well, the food we get isn't\n\ \ that important, so isn't it okay\n\ \ if we just buy whatever we like? 」"
        
        show ju 001 red at farleft behind ky with dis
    
        ju "「All right if we buy a little\nof what we like? 」"
        fn "「Yeah, I think it's okay. 」"
        
        show ju 003 red with dis
    
        ju "「...... 」"
        "I wonder what's up...{p}Is there anything I want?"
        
        scene market red with wipeleft
        show ta 001 red at center with wipeleft
    
        ta "「If it's a small amount,\n\ \ then it's okay to get what you want. 」"
        "Now then, what should I get?{p}I'll probably buy a large juice,\nand some candy, depending on the price."
        "Then again, if I buy only the\nthings that I like, I'd feel a little awkward..."
        "What's everyone else getting?"
        
        hide ta with wipe_right
        
        show ky 001 red at center
        show so 001 red at midright
        with Dissolve(1)
        show so 006 red with dis
    
        "Kyouji-senpai is together with\nSoutarou-kun?"
        "Looks like everyone's picking\nsomething they like to eat after all.{p}Somehow that looks like a lot of fun."
        
        scene market red with wipe_right
        show ju 004 red at center with wipe_right
    
        "Hmm, Juuichi-san's on the opposite side."
        "He seems to have a bottle of something\nin his hand..."
        "Honey?{p}I wish he'd admit to it..."
        
        hide ju with wipe_right
        show si 001 red at center with wipe_right
    
        "Oh,{w=.2} Shin-kun's over there."
        "He said he was fine with anything, but\nthe way he's thinking hard about it is\nso like him."
        "Seems like he's looking at some sweets,\nbut Shin-kun and sweets together\nis...{w=.2} surprising."
        
        hide si with wipe_right
        
        who "「Hey, boy.{p}\ \ What are you being sneaky for? 」"
        "What am I doing?"
        "I'm secretly watching what everyone's\ngetting, and staring..."
        "No matter how much you look at it, I'm a\nstalker.{p}Thank you very much."
        
        show ta 002 red at center with wipe_right
    
        ta "「Gahahahaha!{w=.2} Why are you so surprised?{p}\ \ Did you do something wrong? 」"
        fn "「Hey, Tatsu-nii, don't freak me out like that. 」"
        
        show ta 008 red with dis
    
        ta "「You were just loitering around just now. 」"
        "He saw a sore spot..."
        "You don't have to mock me with that huge grin.{p}This is a little embarrassing,\nso let's change the subject."
        fn "「So what'd you get, Tatsu-nii? 」"
        
        show ta 001 red with dis
    
        ta "「Me?{p}\ \ I've been thinking about it, and beer on the\n\ \ riverside is good, but cold sake's good too... 」"
        ta "「What should I do? 」"
        "He really likes his sake.{p}But this is bad..."
        
        menu:
            "A. Stop him.":
                jump tatsuki11_stop
            "B. Don't stop him":
                jump tatsuki11_proceed
    
    ############################################
    label tatsuki11_stop:

        $ event_name = _("Abstinence")
        
        fn "「The main event today is fireworks, so it'd\n\ \ be better if you don't get sake. 」"
        
        show ta 006 red with dis
    
        ta "「You think so? 」"
        
        show ta 008 red with dis
    
        ta "「We're doing fireworks, so I thought we could\n\ \ also get some moon-viewing sake... 」"
        fn "「Fireworks are way more fun.{p}\ \ I don't want to deal with you clinging to me\n\ \ smelling like sake,{w=.2} Tatsu-nii. 」"
        
        show ta 010 red with dis
    
        ta "「Sorry about my bad drinking. 」"
        fn "「If you aren't going to drink, it'd be all right...{p}\ \ Holding onto me, that is. 」"
    
        show ta 002 red with dis
    
        ta "「There's no helping it, I won't drink today.{p}\ \ Then I get to hold you as much as I want! 」"
        "Tatsu-nii said that, caught me in his big arms,\nand easily picked me up."
        fn "「Wait, Tatsu-nii.{p}\ \ Let me go, it's embarrassing if you do it here. 」"
        
        show ta 007 big red at center_big with dis
    
        ta "「What are you talking about?{p}\ \ I'll let you go, if you ask nicely. 」"
        
        jump tatsuki11_showtime

    #################################################    
    label tatsuki11_proceed:

        $ event_name = _("Drinking but not drunk")

        fn "「Is cold beer that good today? 」"
    
        show ta 002 red with dis
        
        ta "「Yeah, maybe I should get beer today.{p}\ \ You should get a drink too, [fn]. 」"
        fn "「Okay, I guess I'll see what it's like. 」"
        
        scene black with Dissolve(1)
        scene river night with Dissolve(1)
        
        play sound rocket_scream
        pause 5
        show ta 002 night at center with wipe_right
    
        ta "{size=+15}「BBbaaaawwwwllllsssss. 」"
        
        show to 006 night at farright with wipeleft
    
        to "「Tatsu-nii, that was just a standard rocket... 」"
    
        scene river night
        show ka 005 night at midright
        with wipeleft
    
        ka "「Who's the guy who let Tatsuki-san have sake? 」"
    
        show si 001 night at midleft behind ka with wipeleft
    
        si "「[fn]... 」"
        fn "「Wait, balls!?{p}\ \ Tatsu-nii, you couldn't have found any balls!{p}\ \ There-{w=.2}there's-{w=.2}oh hey, sparklers! 」"
        fn "「Fwahahaha, you gotta do these ones.{p}\ \ If you tie them up all together and then\n\ \ light them, I wonder what happens? 」"
        "I can't help it if I'm having fun.\nAnyway, time to light them up."
        fn "「Kyahahaha, it finished while I was thinking\n\ \ about it...! 」"
        ka "「...Who made [fn] drink? 」"
        
        show ju 003 night behind si with dis
    
        ju "「Tatsu-san... 」"
        ta "「Huh?{p}\ \ I don't have any balls 'round my crotch!!{p}\ \ But [fn] does,{w=.2} you know...! 」"
        fn "「I said no, Tatsu-nii.{p}\ \ You can't touch there.{p}\ \ That's my shrine to Inari. 」"
        fn "「Okay then, I wonder where Tatsu-nii is.{p}\ \ If I look for him will he appear. 」"
        ta "「He-hey, don't touch my sensitive spots.{p}\ \ If you wanna touch something so much, I'll get\n\ \ something else for you. 」"
        
        scene river night with wipeleft
        
        show ky 001 night at midright
        show su 004 night at midleft
        with wipe_right
    
        su "「[fn]-san... 」"
        ky "「Tatsuki-san's the same, but [fn]'s\n\ \ drunken behavior is pretty bad... 」"
        
        scene river night with Dissolve(1)
        show ta 302 big night at center_big with Dissolve(.5)
    
        ta "「[fn]...{p}\ \ You're so small and cute. 」"
        "Tatsu-nii stared at me hotly."
        fn "「That's 'cause you're so big and burly,\n\ \ Tatsu-nii.{p}\ \ And so plump and cool..."
        "Having you hold me is nice,{w=.2} too. 」"
        "I stared back at Tatsu-nii in response."
        ta "「[fn]... 」"
        fn "「Tatsu-nii... 」"
        "Today, Tatsu-nii looks like a really\nhandsome older brother.{p}For him to be this good looking..."
        "How did I not notice until now?"
        
        scene river night
        show ko 005 night at midright
        with wipeleft
    
        ko "「What are you two doing...? 」"
        
        show to 007 night at center behind ko with wipe_right
    
        to "「Let's just leave 'em alone,\n\ \ and do the fireworks ourselves. 」"
        
        show ky 001 night at farleft with wipeleft
    
        ky "「Yeah... 」"
        
        scene river night with Dissolve(1)
        pause .5
    
        "Oh yeah, I thought about it the\nother way around."
        "If I'm against having Tatsu-nii holding\nme while smelling like sake, it'll be\nall right if I drink too."
        "That's what I thought."
        ta "「[fn]...! 」"
        fn "「Tatsu-nii...! 」"
        
        jump end11
    
    ##########################################
    label tatsuki11_showtime:

        $ event_name = _("Let's set off Fireworks!")

        scene river night with sdis
        play music river_flow
    
        "So I ended up not buying anything after all."
        "But that's fine, there wasn't anything\nI really wanted, and everyone else\ngot the necessary things..."
        "Or so I told myself."
        "Anyway, let's have some fun with the fireworks!"
        fn "「We gotta start with the handheld stuff. 」"
    
        show to ray 01 night with dis
    
        to "「What's up, [fn]?{p}Being all good and quiet.{p}We gotta be louder! 」"
        "Having said that, Torahiko grabbed some\nfireworks with both hands, then started\nbrandishing them with his arms and tail."
    
        show ka 001 night at farright with wipeleft
    
        ka "「That's if you're alone...{p}And if you're doing fireworks, lighting\nhowever many at once, and waving them all around. 」"
        
        show si 001 night at farleft with wipeleft
    
        si "「If one guy does it, then everyone else\nwill, and that'd be an eyesore. 」"
        
        scene river night with wipe_right
        
        show ky 001 night at midright
        show so 005 night at midleft
        with wipeleft
    
        ky "「It's almost time. 」"
        so "「Ayup. 」"
        
        scene river night
        show ju 006 night at midright
        show to 008 night at center
        with wipe_right
        play sound bosu31
        #[quake time="500"]
    
        ju "「Hmph! 」"
        
        show to 008 big night at center_big with explosion
    
        to "「Gyaaaah!!! 」"
        
        scene river night with dis
        show si 001 night at center with wipe_right
    
        si "「I'll do this one. 」"
        "Same old routine...{p}Shin-kun's completely ignoring it all.{p}Oh man, that chilly side of him is so fantastic."
        
        hide si with wipeleft
        show ta 002 night at center with wipeleft
    
        ta "「You guys, the bucket's filled with water now,\n\ \ so put out any fires by putting them in there.{p}\ \ The trash afterwards goes into a bag. 」"
        "Tatsu-nii has a diligent side to him...{p}He's usually so rough."
        
        hide ta with wipe_right
        show ju 001 night at midright with wipe_right
    
        ju "「It sure did drop a lot. 」"
    
        show su 002 night at center with wipeleft
    
        su "「That was surprising! 」"
        
        show ta 002 night at center behind ju with wipeleft #!#Something missing around here...
    
        ta "「All right, it's about time we do 'that'.{p}\ \ It's the most fun if we do this one. 」"
        "If Tatsu-nii is looking forward to something{p}it'd have to be...{p}A dragon fountain? He is a dragon, after all."
        
        show ta 008 night with dis
    
        ta "「This one right here. 」"
        "Yep, a fountain."
    
        scene river night
        show to 006 night at center
        with wipe_right
        
        to "(A fountain.)"
        
        scene river night
        show ky 001 night at center
        with wipe_right
    
        ky "(A fountain.)"
        
        scene river night
        show ju 003 night at center
        with wipe_right
    
        ju "(Fountain.)"
    
        scene river night
        show ka 001 night at center
        with wipe_right
        
        ka "(Fountain.)"
    
        scene river night
        show si 004 night at center
        with wipe_right
        
        si " (...A fountain.)"
    
        scene river night
        show ko 004 night at center
        with wipe_right
        
        ko "(A fountain.)"
    
        scene river night
        show su 005 night at center
        with wipe_right
        
        su "(A fountain.)"
        
        scene river night
        show so 003 night at center
        with wipe_right
    
        so "(Fount'n.)"
        
        hide so
        show ta 002 big night at center_big with wipe_right
    
        ta"「The sparklers! 」"
        
        play sound bosu35
        "{size=+15}*CRASH*!!"
        
        show ta 001 big night with dis
    
        ta "「If we start with this one first,\n\ \ it makes me look forward to things. 」"
        
        hide ta
        show to 003 night at center
        with wipe_right
    
        to "「... 」"
    
        hide to
        show ky 001 night at center
        with wipe_right
        
        ky "「... 」"
    
        hide ky
        show ju 001 night at center
        with wipe_right
        
        ju "「... 」"
    
        hide ju
        show ka 001 night at center
        with wipe_right
        
        ka"「... 」"
    
        hide ka
        show si 010 night at center
        with wipe_right
        pause .2
    
        si "「... 」"
    
        hide si
        show ko 004 night at center
        with wipe_right
        
        ko "「... 」"
    
        hide ko 
        show su 004 night at center
        with wipe_right
        
        su "(...desu)"
    
        hide su
        show so 005 night at center
        with wipe_right
        
        so "(...ssu)"
        
        hide so with wipe_right
     
        "..."
        fn "「...This will be last.{p}\ \ Do you guys like it? 」"
        
        show ta 001 night at center with dis
    
        ta "「We can only do one.{p}\ \ Well, this one will be done in a minute,\n\ \ and we can light the rest then. 」"
        "Hmm. There are so many ways to have\nfun with fireworks."
        "Anyway, I guess I'll pick something\nfrom what's left.{p}Which one should I get?"
        
        menu:
            "A. The rocket.":
                jump tatsuki11_rocket
            "B. Whatever's at the bottom.":
                jump tatsuki11_bottom
            "C. The fountain.":
                jump tatsuki11_fountain
       
    ###################################### 
    label tatsuki11_rocket:

        $ event_name = _("Rocket Firework")    
        $ love_juuichi -= 1
        $ love_torahiko -= 1
        
        scene river night with wipe_right
        
        "It just wouldn't be right without\nusing some bottle rockets."
        
        show to 002 night at center with wipeleft
    
        to "「Hey, what's up? 」"
        fn "「I was thinking about using the bottle rockets. 」"
        
        show to 001 night with dis
     
        to "「The rockets, huh?{p}\ \ When we were kids, we fought over these. 」"
        "I've got a bad feeling about this.{p}That can't be good..."
        
        show to 002 night with dis
    
        to "「Wanna do it? 」"
        fn "「No way.{w} We've done it before as a prank in the\n\ \ old days, but we aren't kids anymore,\n\ \ and everyone's here... 」"
    
        show to 003 night with dis
    
        to "「Then let's invite everyone else...{p}\ \ Except we can't do that.{p}\ \ It doesn't look like there's enough. 」"
        fn "「I know, right? Let's just launch it normally. 」"
        
        show to 006 night with dis
    
        to "「I was thinking of fighting,\n\ \ and not hurting much. 」"
        fn "「I've been hit by Tatsu-nii however many\n\ \ times, so there's no way anyone else could\n\ \ hurt me. 」"
    
        show to 002 night with dis
        
        to "「It's Tatsu-nii, so nothing would happen,\n\ \ but everyone else would get hurt.{p}\ \ How about one punch, then? 」"
        
        play sound rocket_scream
    
        fn "「Whoa, it'd be dangerous if you set it off on its side.{p}\ \ What'll you do if there're people around? 」"
    
        show to 001 night with dis
    
        to "「There's nothing there, and no one either. 」"
        fn "「Huh?{w=.2} I thought I saw something moving. 」"
        
        show to 002 night with dis
    
        to "「It's just your imagination.{p}\ \ I wonder how many I should tie together and\n\ \ fire rapidly? 」"
        "No, there definitely was something there..."
        "Aha! There is something, just as I thought."
        "A bear?{p}...No, wait,{w=.2} it's Juuichi-san!!"
        fn "「Hey, Tora. 」"
        
        show to 003 night with dis
    
        to "「One sec, I'm setting up an attack here. 」"
        "It's coming this way, and it looks sort of\nlike an aura."
        fn "「This is bad. Juuichi-san is overcome with\n\ \ that fighting spirit...{p}\ \ Anger is written all over his face! 」"
        "A-{w=.2}an oni?{p}That is an oni."
        
        show to 006 night with dis
    
        to "「I've got a good spot right now.{p}\ \ What, did someone say something? 」"
        fn "「Torahiko,{w=.2} run awaaay! 」"
        
        hide to
        show ju 006 big night at center_big
        with explosion
        
        ju "{size=+15}「Nyooooooooooryaaaaaaaa! 」"
        
        play sound rocket_scream
    
        to "「Nyaan! 」"
        
        hide ju with sdis
        
        "Torahiko flew like a rocket launch,\ndisappearing into the night sky.{p}Ahh, that's so sad, Torahiko."
        
        scene starry_sky with Dissolve(1)
    
        "Torahiko never returned to Earth.{p}He'll eternally wander as an existence\nbetween man and tiger."
        "And since he can't die even if he wanted to,\neventually he'll just stop thinking."
        
        jump end11

    #############################################    
    label tatsuki11_bottom:

        $ event_name = _("What's left over?")
        $ love_shun += 1
        scene river night with wipe_right
        
        "Let's see, smoke balls or fire snakes?{p}In this darkness, they might be fun."
        
        show su 001 night at midright with wipeleft
    
        su "「[fn]-san, what are you doing? 」"
        fn "「Oh, Shun-kun. I was thinking of using up\n\ \ what's left, but I was wondering which\n\ \ would be brighter... 」"
        "Sigh, Shun-kun's eyes are glittering.{p}His face is bursting with curiosity."
        "So cuuute.{p}If his eyes get any bigger and rounder, I..."
        fn "「Well, anyway, let's take a look. 」"
        
        show su tailwag 01 night with dis
    
        su "「Woof. Are you doing it now? I'm so excited! 」"
        "T-that's too cute Shun-kun.{p}I just want to eat you up.{p}No, I can't. I can't. Calm down."
        "I guess I'll start off with the smoke bomb."
        "If I light it, a lot of smoke will spout out.{p}What'll happen to the darkness?"
        
        show ko 001 night at midleft behind su with wipe_right
    
        ko "「[fn] and Shun-kun, what are you guys\n\ \ doing over there?{p}\ \ Let me in on it. 」"
        fn "「I'm about to do this. 」"
        
        show ko 005 night with dis
    
        ko "「You're going to use smoke balls and\n\ \ fire snakes in this darkness? 」"
        fn "「It'll be fine. Because it'll be cute,\n\ \ and I wanna eat it.{p}\ \ Time to go. 」"
        "......"
        ko "「It's smoky, and I can tell the fumes\n\ \ are coming out somehow, but I'm feeling\n\ \ a little weird. 」"
        
        show su 004 night with dis
    
        su "「I don't understand. 」"
        fn "「Then let's see how the fire snake is. 」"
        "A fireworks that looks like a snake that\nstretches out in an irregular way..."
        "If it's this..."
        "If it's this then..."
        "You wouldn't be able to see it well now but..."
        "It should be ENTERTAINING!!!"
        
        show su 005 night with dis
    
        su "「I can't really see or understand it. 」"
        fn "「You should be able to see it moving at\n\ \ least, somehow. 」"
        
        show ko 004 night with dis
    
        ko "「It's supposed to be plain and simple,\n\ \ but the plain part is the only thing\n\ \ highlighted... 」"
        "Who the hell bought this thing?{p}This is clearly a stupid selection."
        
        show su 004 night with dis
    
        su "「To be honest I bought that one, but it\n\ \ looks like it's no good.{w} I'm sorry... 」"
        "This is terrible!{w=.2} Shun-kun's adorable eyes\nlook like they'll be completely clouded\nover with tears."
        "That can't be. That cannot be!{p}What do I do!?"
        fn "「Hahaha, that's not true.{p}\ \ {nw}"
        hide ko with Dissolve(1)
        extend "This one isn't bad.{p}\ \ Right,{w=.2} Kounosuke? 」"
        fn "「...Huh? 」"
        "That tanuki. He's all the way over there,\nlighting some sparklers!"
        "You bastard..."
        su "「Is something wrong? 」"
        fn "「No,{w=.2} nothing. 」"
        fn "「These ones are more fun during the day,\n\ \ so remember that.{w} Next time,\n\ \ when there's more light, we'll do it together. 」"
        
        show su 002 night with dis
    
        su "「Really? 」"
        fn "「Yeah, really. I promise. 」"
        su "「It's a promise! 」"
        "Somehow I managed to spin that around."
        "I'll definitely find this at the\ncandy store, and buy it while those eyes\nshine..."
        "I won't disappoint Shun-kun like that."
        
        jump end11
    
    #########################################
    label tatsuki11_fountain:

        $ event_name = _("Dragon")
        $ love_tatsuki -= 1
    
        fn "「Hey, Tatsu-nii. 」"
    
        show ta 002 night at center with dis
        
        ta "「Hm, what's up? 」"
        fn "「Can you light this for me? 」"
    
        show ta 007 night with dis
        
        ta "「Sure, but how come you seem so happy? 」"
        fn "「I-{w=.2}it's nothing. 」"
        "Kukuku, the dragon lighting a fountain...{p}It's a masterpiece."
    
        ta "「Hey, did you know?{p}\ \ All the fountain fireworks are all handmade. 」"
        fn "「Is that so? 」"
    
        show ta 002 night with dis
        
        ta "「The guy who made this one... He designed it\n\ \ thinking about the kids during the Showa Era. 」"
        fn "「Wow, That's an interesting bit of trivia. 」"
        
        show ta 001 night with dis
        
        ta "「If you knew that and saw it,\n\ \ you'd see it differently to before.{p}\ \ Here. 」"
        
        play sound dragon_scream
        pause .2
        
        fn "「It's beautiful.{w} If I see it after hearing\n\ \ you say that, it definitely looks better than\n\ \ how I used to see it. 」"
    
        show ta 002 night with dis
    
        ta "「That's right, isn't it pretty?{p}\ \ {nw}"
        show ta 008 night with dis
        extend "By the way...{w=.2} you didn't pick the\n\ \ fountain because I'm a dragonman, did you? 」"
        
        "{size=+40}{cps=0}\ \ \ \ \ \ \ \ ＼(^o^)／ "
        #!#Need to create effect to make everything shine in fireowork colors, including sound effect
        
        fn "「N-{w=.2}no,{w=.2} that's not it.{p}\ \ I just wanted to see it together with\n\ \ you, because it looked nice. 」"
        ta "「Liar.{p}\ \ It's so obvious. 」"
        
        "{size=+40}{cps=0}\ \ \ \ \ \ \ \ ／^o^＼"
        #!#Fireworks effect with sound
    
        show ta 010 night with dis
        
        ta "「When we were kids and talks turned to fireworks,\n\ \ they'd always say 'dragon fountain'.{p}\ \ Did you know? 」"
        
        show ta 004 night with dis
    
        ta "「Just like how they say all Russians\n\ \ drink vodka, or how all Indians eat curry. 」"
        
        show ta 008 night with dis
    
        ta "「And how all Chinese people know kung fu,\n\ \ and can do stunts like Jackie Chan.{p}\ \ It's that kind of talking. 」"
        fn "「I-I'm sorry...{p}\ \ My bad. 」"
        
        show ta 008 night with dis
        
        ta "「I'll let you go this time,\n\ \ if you keep it in mind.{p}\ \ Don't forget it next time. 」"
        "So many people could say that during\nfirework times...{w} Is everyone thinking the\nsame thing?{w} This talk won't happen ever again."
        
        jump end11
    
####################################################       
label end11:
    
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
    jump day12
    
####################################################
