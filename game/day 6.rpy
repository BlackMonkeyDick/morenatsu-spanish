###Day 6

screen torahouse06:
    hbox:
        add "arrow down"
        at torabounce1
    hbox:
        add "icon_tora"
        at torabounce2
    hbox:
        text "Torahiko's House"
        xalign .5 yalign .58
        
screen kounocandy06:
    hbox:
        add "arrow down"
        at marketbounce1
    hbox:
        add "icon_kouno"
        at marketbounce2
    hbox:
        text "Candy Store"
        xalign .5 yalign .53

screen minasatomap06():
    add "map"
    add "mapdate"
    imagebutton idle "a icon" hover "icon loop" xpos 363 ypos 283 action Jump("torahiko06") hovered Show("torahouse06")  unhovered Hide("torahouse06") hover_sound "av/audio/click_008.wav"
    imagebutton idle "a icon" hover "icon loop" xpos 372 ypos 249  action Jump("kounosuke06") hovered Show("kounocandy06")  unhovered Hide("kounocandy06") hover_sound "av/audio/click_008.wav"
    hbox:
        text "{size=+30}August 6"
        at maptime

#######################################        
label day06:
    
    $ renpy.music.set_volume(1.0, 0.0, channel = "music")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound2")
    
    $ day = 6
    $ the_date = "August 6"
    $ event_name = "８月6日"
    $ focus_character = ""
    
    window hide
    play music birds_chirping
    
    scene sky01 
    show text "{size=+130}August 6" at truecenter
    with Dissolve(.5)

    pause 3
    scene black with Dissolve(1)
    pause .4
    
    scene hbroom with wipe_corner

    fn "「Hmm, what to do today... 」"

    if juuichi_fireflies01 == True and juuichi_fireflies02 != True:
        
        "I stretch out my back as I say that.{w} Even though thatlazy feeling is coming back, {w=.3}I want to make the most\nof my homecoming and go somewhere."
        "Somewhere I can't experience in the city,{w=.3}\nso I can feel satisfied when I leave."
        "...Hm?{w} I just suddenly thought of something.{w} That's\nright, {w=.3}there was something I could only do here in\nMinasato."

        play music [ "<silence .3>",   phone_ring]
        
        "Oh, the phone.{p}I suspend my thoughts,{w=.3}\nlazily stand up, {w=.3}and pick it up."
        
        scene hentry with dis
        stop music fadeout .5
        play sound phone_pickup
        pause .5
        
        fn "「Hello, {w=.3}[ln] speaking. 」"
        ju "「...[fn]? 」"
        "It's Juuichi-san on the other end.{p}His voice sounds lower than usual. {p}What's wrong?"
        fn "「Yeah, {w=.3}it's me, but...{p}\ \ Did something happen to you? 」"
        ju "「... 」"
        fn "「Um, {w=.3}Juuichi-san? 」"
        ju "「...[ln], {w=.3}there's something you've forgotten. 」"
        fn "「I forgot something?{p}\ \ Hmmm, {w=.3}let me think... 」"
        "I rack my brains trying to remember what he said I\nforgot.{w} But it wouldn't take so much effort if it was\nsomething simple."
        fn "「Maybe I did, {w=.3}but I can't think of anything... 」"
        ju "「...I see, {w=.3}so you don't remember?{p}\ \ I guess promises don't mean much to you, [ln]. 」"
        "Even though it's over the phone,{w=.3}\nI can still hear him let out a deep sigh.{p}...A promise, {w=.3}with him?"
        "...{p}...{p}...Oh."
        fn "「Aaaaaaaaaaaaaaaaaaaaaah!! 」"
        ju "「If you want to go catch fireflies again,{w=.3}\n\ \ don't bother inviting me. 」"
        "I promised to go catch fireflies with him...!{p}How could I forget something so important?{p}I'm such an idiot!"
        "My cell phone doesn't work here either,\nso I can't stay in contact."
        "And I can't see the river bed very well at night.{p}I kept him waiting there the whole time..."
        "He must have been looking all over,{w=.3}thinking something happened to me.{p}He never would have found me though."
        "When he tried coming to my house just in case,{w=.3}\nhe saw me laughing at a variety show on tv."
        "He felt tired and disappointed when he heard me,{w=.3}\nwondering how I could so such a thing."
        "I don't want to think about it,\nbut I have to.\nThis was all my fault."
        fn "「Juuichi-san, {w=.3}I'm so sorry... 」"
        ju "「...{p}\ \ It's already done. 」"
        fn "「... 」"
        ju "「...I know you're in a festive mood because you've\n\ \ finally returned,{w=.3} but that doesn't mean you can do\n\ \ whatever you want. 」"
        ju "「Promises are built upon mutual trust.{p}\ \ I've known you for a long time.{p}\ \ You've never broken a promise before. 」"
        ju "「People change easily over time...{p}\ \ That's too bad. 」"
        fn "「Juuichi-san... 」"
        ju "「...That's all I wanted to say. 」"
        "Without saying good-bye, {w=.3}he hangs up the phone."
        
        play sound call05
        
        "Click.{p}It feels like that was the sound of the path\nconnecting Juuichi-san and I closing."
        
        $ love_juuichi -= 10
        $ juuichi_hate = True
        
        scene black with Dissolve(2)
        pause 1
    
    play music "<from 2.5>av/audio/free0422.ogg"
    call screen minasatomap06
    
###############################################    
label torahiko06:
    
    $ event_name = "First time use"
    $ focus_character = "torahiko"
    $ love_tatsuki += 1
    $ love_torahiko += 1
    
    scene map
    stop music fadeout .8
    hide screen torahouse06
    scene black with wipe_dr_slow
    pause .5
    scene market with wipeleft
    
    play music cicada01

    "Torahiko called me over all of a sudden.{p}I wonder why?\nAnyway, I'd better get inside."
    
    scene tora_house_in with wipe_right
    show to 002 at center with dis

    to "「Ah, [fn], you're here.{p}\ \ Tatsu-nii's coming too, so wait a bit. 」"
    fn "「So, Tatsu-nii's coming too,\n\ \ but what are we doing today? 」"
    
    show to 010 with dis
    
    to "「Don't be in such a rush, I'll tell you later.{p}\ \ Hey, it looks like Tatsu-nii's right on time. 」"
    
    show ta 001 at midleft
    show to 001 at midright
    with wipeleft
    
    show ta 002 with dis
    
    ta "「Hey, sorry to keep you waiting.{p}\ \ {nw}"
    show ta 001 with dis
    ta "Oh, [fn]'s here, too?\nSo what are we doing? 」"
    
    show to 002 with dis
    
    to "「Now that you're both here I'll tell you.{p}\ \ You guys want to eat something tasty? 」"
    
    play music piano_014
    
    fn "「What are you saying all of a sudden? 」"
    
    show ta 002 with dis
    
    ta "「Isn't it that? 」"
    ta "「The thing you always make for us? 」"
    fn "「'Always'? 」"
    
    show ta 001 with dis
    
    ta "「Hm?　When Tora's trying out new meals,\n\ \ he gets us to taste-test for him. 」"
    
    show to 007 with dis
    
    to "「That's true...{p}\ \ Since I can't tell what tastes good or not,\n\ \ I need to consult someone. Usually, it's Tatsu-nii. 」"
    
    show ta 002 at jump_up

    ta "「Gahaha! Whether they're good or not is no problem.{p}\ \ Because they're always good. 」"
    "This isn't much of a consultation..."
    
    show to 009 with dis
    
    to "「*Cough* 」"
    
    show to 001 with dis
    
    to "「Eh, today we have all gathered\n\ \ to help buy the ingredients for the new\n\ \ cooking challenge that I'm doing today. 」"
    
    show ta 008 with dis
    
    ta "「You don't really need to put on an air, do you? 」"
    "Really..."
    
    show to 002 with dis
    
    to "「Heheh. If you watched the Pururun Stay show\n\ \ on TV yesterday, it was about someone doing\n\ \ a homestay out of the country. 」"
    to "「The destination was an Italian pasta maker's\n\ \ house. If you saw it, it looked so good...!{p}\ \ I had no choice, I thought 'I can make that, too.' 」"
    
    show ta at stagger
    
    ta "「Huaaah... 」{w=2}{nw}"
    show ta at still
    extend ""
    "Tatsu-nii, don't yawn like that.\nJust listen for a bit longer."
    
    show to 009 with dis
    
    to "「And so, because I'm making classical spaghetti,\n\ \ Tatsu-nii will go and buy the ingredients,{p}\ \ and [fn] will help. 」"
    to "「I've got setup to do, so you can leave me here. 」"
    
    show ta 001 with dis
    
    ta "「What are you saying? If we're going shopping,\n\ \ it's pointless unless you're there.{p}\ \ I'll bring the truck around, so get ready. 」"
    
    hide ta
    show to 001 at center
    with wipe_right
    
    show to 006 with dis

    to "「[fn], I'm counting on you for this.{p}\ \ I've got a list of the stuff we need. 」"
    fn "「Torahiko, it should be fine if you come, too. 」"
    
    show to 007 with dis
    
    to "「[fn], you don't know, so it's fine,\n\ \ but Tatsu-nii's driving is freaking terrifying.{p}\ \ {nw}"
    show to 011 with dis
    extend "Just leave it at that.{w} C'mon,{w=.3} please. 」"
    
    ###Apparently there was going to be a choice of whether you accept Torahiko's request or refuse, but unavailable in last version of original
    
    $ event_name = "Going on an errand"
    
    fn "「Since this is something you want to do,\n\ \ of course you need to come too, right? 」"
    
    play music pops_004
    show to 008 with dis
    
    to "「Seriously.{w} I'm begging ya. 」"
    fn "「Don't you think it's a bit pointless to call us\n\ \ over, then ask us to do some shopping for you? 」"
    
    show to 007 with dis
    
    to "「It's true I made a decision when I called you\n\ \ guys over.{w} Seems I really did get scared...{p}\ \ All right, no more thinking scary thoughts. 」"
    fn "「Is it really that bad? 」"
    
    show to 005 at briefzoom 
    
    to "「Really! 」"
    
    show ta 002 behind to at farright with wipe_right
    
    ta "「Yo, everything's ready. 」"
    
    show to 008 with dis
    
    to "「Damnit, this is because [fn]'s too slow! 」"
    
    show ta 008 with dis
    
    ta "「Tora,{w=.3} give it up.{w} In any case,\n\ \ you already said you're afraid of my driving,\n\ \ haven't you?{w} Let's just go. 」"
    
    show to 007 with dis
    
    to "「Ugh, damnit.\n\ \ My stomach's tying itself into knots. 」"
    "Uhh... knowing Tora's belief in letting nature\ntake its course...\nFor him to be this against it..."
    "I'm starting to get a bad feeling about this, too."
    "..."
    
    stop music fadeout 1
    
    scene black with wipe_down_slow
    pause .5
    
    scene rice 
    show ta 001 at midright
    show to 007 at midleft
    with wipe_down
    
    play music cicada01
    show ta 002 with dis

    ta "「Okay, get in, get in. 」"
    fn "「And how are we all supposed to do that? 」"
    "For three people to get into a light truck,\nit seems hopeless."
    "It looks barely possible, if were just Torahiko,\nwith his good physique, and Tatsu-nii."
    "Which means..."
    "Tatsu-nii by himself is over two metres tall,\nso how he gets in is a mystery.\nWhere's he going to ride?"
    
    show ta 001 with dis
    
    ta "「Tora,{w=.3} you can sit in the back. 」"
    
    show to 005 at briefzoom 
    
    to "「No way,{w=.3} absolutely not!{p}\ \ It's ok if I don't fit, I'm going home. 」"
    
    show ta 002 with dis
    
    ta "「Dahaha! Kidding,{w=.3} I'm kidding.{p}\ \ We'll squeeze in. 」"
    
    show to 005 with dis
    
    to "「...... 」"
    to "「In that case, I'll get in first.{p}\ \ [fn], sit in between me and Tatsu-nii,\n\ \ because we might crash, you know. 」"
    
    hide to
    hide ta 
    with wipe_right
    
    "Tatsu-nii was already sitting in the driver's seat,\nand it already looks cramped."
    "Torahiko took the seat next to him,\nbut I'm feeling boxed in just from looking.{p}Am I really getting in like this?"
    fn "「Well, in I go... 」"
    "No point in thinking.\nI forced myself into the car."
    
    scene black with wipe_down
    
    "On that note..."
    "This reminds me of a show I saw once."
    "It was about some wagon that was full of refugees\ngetting chased by a patrol car."
    "I think there were about forty people in there,\nall jammed together like baby spiders.{p}I don't think it could compare to this, though..."
    ta "「Yeah, get in, come on. 」"
    
    play sound bosu34
    pause .3
    
    to "「Oww, [fn], you're stepping on me. 」"
    fn "「Sorry, I'll be out of the way soon. 」"
    
    play sound puu75
    pause .3
    
    ta "「Aah,{w=.3} [fn], that's... 」"
    fn "「Huh?{w=.3} Oh,{w=.3} sorry. 」"
    "I touched somewhere inappropriate, didn't I."
    "But, in this place with nowhere to put my hands,\nthere's not much I can do except struggle about.\nWe're all just trying to get seats."

    play sound bosu29
    pause .3
    
    to "「[fn], your leg is in my face... 」"
    fn "「Sorr...{nw}"
    play sound puu75
    pause .5
    play sound puu75
    pause .5
    extend " 」"
    
    ta "「Oooh, it's about to come out...!{p}\ \ If you keep touching it like that!!! 」"
    fn "「Huh!?{w} I'm sorry! 」"
    
    play sound puu75
    pause .3
    
    to "「[fn]... your ass is in my face.{p}\ \ Is that how it is?{w} 　It is, isn't it.{p}\ \ Not that there's anything wrong with that. 」"
    "I see, so I have to force myself to stand up.\nHow about this, then!!!"
    
    play sound bosu31
    pause .3
    
    to "「Don't throw yourself onto his lap!!! 」"
    ta "「Awesome! Do it again, harder!!! 」"
    fn "「Tatsu-nii? 」"
    
    stop music fadeout 1
    
    "Eventually,{w=.3} we all managed to fit in the truck."
    
    play music free22
    
    scene supermarket with wipe_right
    
    show ta 001 at midright
    show to 001 at midleft
    with dis
    
    show ta 002 with dis
    
    ta "「Okay, we're here. 」"
    "We said we'd be shopping in town,\nBut the store we need is in Kazenari's outskirts..."
    fn "「Tatsu-nii, you're pretty good at driving. 」"
    fn "「I mean, you drive way too fast,\n\ \ and there were times where we screamed,\n\ \ but nothing else really happened. 」"
    ta "「I'm taking the Group's car, so I had to drive\n\ \ super safe. It'd be way more amazing if we took\n\ \ my light truck! 」"
    
    show to 009 with dis
    
    to "「Listen, don't ever get on Tatsu-nii's light truck.{p}\ \ If you want to survive, that is... 」"
    
    show ta 008 with dis
    
    ta "「What, you got a problem?{p}\ \ I'm not letting you ride anymore. 」"
    
    show to 011 with dis
    
    to "「No, I kid, I kid.{p}\ \ You came through again, Tatsu-nii.{p}\ \ Ya saved me. 」"
    
    show ta 001 with dis
    
    ta "「Give me a break, you're in a good mood.{p}\ \ We're here to shop, so let's get that done with. 」"
    clerk "「Welcome! 」"
    "Wait what, this is the import shop, World 21?"
    "It's bigger than I thought, and it's got more than\nfood stocked. Darts, cigarettes in colors and\nshapes I'd never seen before, antiques, toys,"
    "furniture, and more. All sorts of foreign goods\nwere lined up on the shelves.\nAn atmosphere of curiosity hung in the air."
    
    show ta 002 with dis
    
    ta "「Hey, look at this, they've got foreign minicars.{p}\ \ Foreign toys and Japanese ones are different,\n\ \ but they're kinda stylish. 」"
    ta "「In Japan, there aren't any Mustang minicars. 」"
    
    show to 002
    show to ray 01 at midleft
    with dis
    
    to "「Oh, they've got portable stoves and pots, too.{p}\ \ There's also cutely shaped and efficient stuff,\n\ \ but they look hard to use. 」"
    "There really is a staggering variety of things\non display."
    fn "「It's my first time in an import goods shop,\n\ \ it's interesting to see how much stuff there is.\n\ \ It'd be hard to get bored from looking. 」"
    
    show to 001 with dis
    
    to "「That's true. It'd be good if there was one in\n\ \ Minasato. 」"
    fn "「When did this one open? I wasn't around for it. 」"
    to "「It was finished recently, this is my first time,\n\ \ too.{w} I got interested when I heard they had\n\ \ specialty ingredients here,"
    to "but it's even better than I thought.{p}I'm glad I came. 」"
    
    show to 002 with dis
    
    to "「Well then, we'll buy the stuff we came for,\n\ \ go home, then I'll cook! 」"
    "Oho, he's really getting into it.{p}He get's really serious when it's time to cook.{p}I'm looking forward to when it's done."
    
    show ta 001 with dis
    
    ta "「They've got pastries over here,\n\ \ and over there it looks like they've lined up\n\ \ the sundried and canned goods. 」"
    fn "「Whoa, what's this...\n\ \ They've got whole frozen birds. Pigeon? 」"
    
    show to 010 with dis
    
    to "「Oh yeah, they call that squab.\n\ \ It's mostly used in French cooking. 」"
    fn "「Huh, is that so.\n\ \ Torahiko, you sure know a lot about cuisine. 」"
    
    show to 011 with dis
    
    to "「Uhh, yeah, kind of. 」"
    "Despite Torahiko sounding triumphant as he said it,\nhe got embarrassed and red in the face afterwards."
    fn "「I see, French cuisine.{w} I don't see Tatsu-nii\n\ \ as all that French, but it feels like he could\n\ \ tear through this whole thing, right? 」"
    to "「Yeah, I get you.{w} His body's big, and his fangs\n\ \ are, too. He totally feels like a meat eater.{p}\ \ {nw}"
    show to 002 at jump_up
    extend "Ya beast! 」"
    
    show ta 008 with dis
    
    ta "「Just who is? I'm totally into alcohol.{p}\ \ I like Japanese style stews and fish.\n\ \ Pa talks about food a lot, so that's my influence. 」"
    
    show to 005 with dis
    
    to "「That's funny... for a guy who likes his drink,\n\ \ you should eat just about anything,\n\ \ whether it's spicy or sweet. 」"
    fn "「Hahaha, but Torahiko,\n\ \ earlier, didn't you say he ate meat? 」"
    
    show to 001 with dis
    
    to "「No, you're the one who brought that up.{p}\ \ You can't judge things by their cover. 」"
    
    show ta 004 at briefzoom 

    ta "「You guys.\n\ \ How about I start at your heads,\n\ \ and tear my way through? 」"
    fn "「I'm small, and there wouldn't be much to eat...\n\ \ But if it's Tatsu-nii, then it's okay. 」"
    
    show to 009 with dis
    
    to "「There's probably no place you could eat, but in\n\ \ older times people had dashi, and ate everything\n\ \ dedicated to spiritual improvement. 」"

    show to 001 with dis
    
    to "「So I'll prepare you.{w} First, I'll cut you into\n\ \ three slabs, but you need to take off your\n\ \ clothes first. Hurry now. 」"
    "I'll take my clothes off here, so please eat me."
    "To be nibbled on by two people with sharp fangs\nwhile naked...{p}You,{w=.3} you beasts!!"
    
    show to 007 with dis
    
    to "「What are you spacing out for?{p}\ \ Don't stand there, come over here. 」"
    "Telling me to come over after you tempted me."
    "I'll go, I'll go.{w} I'm going right now."
    
    scene black with sdis
    pause .5
    scene supermarket with Dissolve(.5)
    show ta 003 at center with wipe_right
    
    ta "「Whoa,{w=.3} isn't this cartoon cheese?{p}\ \ The cheese that Jerry risked his life for,\n\ \ every day in Tom and Jerry? 」"
    ta "「This is the first time I've seen it. 」"
    fn "「This was also on a cooking show I saw once.{p}\ \ They fried it on top of hamburger patties.{p}\ \ It looked so good... 」"
    
    show to 001 at midright with dis
    
    to "「It's Emmental cheese. 」"
    to "「There are guys who like the smell of it,\n\ \ but the taste doesn't seem that good. 」"
    fn "「But, you want to get it so you can fry it in\n\ \ butter on hamburgers, right? 」"
    
    show to 007 with dis
    
    to "「You don't use butter for that,\n\ \ and I'm not buying cheese,\n\ \ since I'm not using it. 」"
    
    show ta 008 with dis
    
    ta "「Cheapass. 」"
    fn "「Stupid Kurara!{w} 　Buy the cheese!! 」"
    
    show to 001 with dis
    
    to "「Tatsu-nii, don't say that.{p}\ \ Besides, you're a working adult,\n\ \ so buy it yourself. 」"
    ta "「For stuff like this,\n\ \ isn't it better if others buy it for you?{p}\ \ {nw}"
    show ta 010 with dis
    extend "Please? 」"
    
    fn "「Please? 」"
    
    show to 007 with dis
    
    to "「I'm already making a meal for you guys.{p}\ \ That was a mistake, wasn't it... 」"
    
    show ta 001 with dis
    
    ta "「You can eat the cheese with some wine.{p}\ \ It's not bad having it with your food. 」"
    
    show to 002 with dis
    
    to "「I see...\n\ \ If you want cheese so bad, we'll get this.{p}\ \ {nw}"
    show to at hit_left
    play sound bosu29    
    extend "C'mon, [fn]. 」"
    
    "Torahiko crouched down,\nand handed me a lump of cheese.{p}I didn't quite drop it, but it was really heavy."
    fn "「Whoa, it's heavy.{w} What is it?{p}\ \ I can't carry this unless I use both hands.{p}\ \ I don't want it at all. 」"
    fn "「How're you going to use this?{w} 　You're buying it.{p}\ \ Man, it's so heavy... 」"
    
    show ta 002 with dis
    
    ta "「Heavy, is it? I'll carry it, then. 」"
    
    hide ta
    hide to
    with wipe_right
    
    "Tatsu-nii said that,\nand then I was being lifted like a princess."
    fn "「You're so tall, Tatsu-nii, this is how you see\n\ \ the world.{w} But... I'm holding the cheese,\n\ \ and it's seriously heavy. 」"
    fn "「I want to stay up here, but can you put me down? 」"
    ta "「My bad, I'll put you down for now.{p}\ \ It'd be bad if you got altitude sickness.{p}\ \ Gahahaha! 」"
    to "「What's with you two. I'm getting in on this. 」"
    
    play sound bosu29
    
    "After Tatsu-nii put me down,\nTorahiko jumped onto him."
    "It seems his habit of pouncing\non people is still strong, huh."
    
    show ta 004 at center 
    show to 002 at farright
    with wipe_right

    ta "「No you don't!! 」"
    
    show to at move_midleft(0.25)

    "Tatsu-nii stopped Torahiko with perfect timing.\nIn one fluid movement,{p}he swept Torahiko off his feet."
    
    show to 003 with dis

    to "「Gah.{w} You bastard, stop doing that. 」"
    
    show ta 002 with dis
    
    ta "「That was naive. Who do you think you try that on\n\ \ all the time?{w} Tora, I can read your movements.{p}\ \ {nw}"
    show ta 004 with dis
    extend "You're in the palm of my hand, just like Son Goku! 」"
    
    "The dragon and the tiger."
    "Each with their own powers and techniques.\nIt looks exactly like the beginning of a war.{p}The dairy corner was full of an unusual tension."
    "Like a princess getting argued over by two suitors,\nI could do nothing but watch."
    "Is there anyone capable\nof stopping this sudden fight...?"
    clerk "「Um... excuse me. 」"
    clerk "「All your jumping and noisemaking is\n\ \ disturbing the other customers here.\n\ \ Could you kindly settle down, please? 」"
    
    show ta 005 with dis
    
    ta "「Sorry. 」"
    
    show to 007 with dis
    
    to "「Sorry. 」"
    "There is!!"
    
    stop music fadeout 1.5
    scene black with sdis
    pause 1
    scene tora_house_in with wipe_right
    show ta 002 at center with wipe_right
    
    ta "「We're baaack! 」"
    
    show to 003 at farright with wipe_right
    
    to "「All right, we got what we went for, time to cook!{p}\ \ I'll make it especially good, so wait here. 」"
    fn "「I'm looking forward to it.{p}\ \ With all the shopping and moving around,\n\ \ my stomach is rumbling. 」"
    
    show ta 001 with dis
    
    ta "「I've got high hopes, Tora. No pressure. 」"
    
    show to ray 01 with dis
    
    to "「Don't pressure me like that.\n\ \ You're supposed to be waiting patiently for it. 」"
    
    scene black with Dissolve(1)
    
    "30 minutes later..."
    
    scene tora_house_in
    show ta 001 at farright
    show to 002 at center 
    with dis
    
    to "「Thanks for waiting, it's ready! 」"
    fn "「This looks amazing.{p}\ \ Did you make it all yourself, Torahiko? 」"
    
    show to 010 with dis
    
    to "「Yep. 」"
    to "「While there was some stuff I didn't have,\n\ \ I finished it off with some of my creativity.{p}\ \ I call it zucchini and tomato vegetable pasta! 」"
    "When it comes to cooking, Torahiko gets so lively.{p}Being cheerful like a kid is how he always is,\nbut it's great that he makes other people happy."
    
    show to 002 with dis
    
    to "「Now, hurry up and eat, before it gets cold. 」"
    fn "「Yeah, it looks good. Time to eat...! 」"
    
    show ta 004 with dis
    
    ta "「This is great. 」"
    
    "*!?\n{nw}"
    scene white
    play sound hit_p07
    scene tora_house_in
    show ta 004 at farright
    show to 002 at center
    with dis
    extend "This is..."
    
    $ event_name = "This is..."
    
    menu:
        "A. Delicious!":
            jump torahiko06_delicious
        "B. Not that good.":
            jump torahiko06_notgood
        "C. Disgusting!":
            jump torahiko06_disgusting

########################################            
label torahiko06_delicious:
    
    $ event_name = "Amazing"
    $ love_tatsuki += 1
    $ love_torahiko += 1

    play sound bom35
    
    fn "「Awesome!! 」"
    
    play music pops_001
    show to 007 with dis
    
    to "「You and Tatsu-nii both think so? 」"
    fn "「Well, that's because it's delicious.{p}\ \ That means you've got real skill, Torahiko. 」"
    
    show to 011 with dis
    
    to "「I see. In that case, there's more.{p}\ \ If it were just Tatsu-nii,\n\ \ he'd eat the mess-ups and still say they're good. 」"
    
    show ta 001 with dis
    
    ta "「If I say it's good, I mean it, Torahiko. 」"
    
    show to 007 with dis
    
    to "「Hang on, you must be speaking funny.{p}\ \ [fn] said something like it, earlier. 」"
    
    show ta 002 with dis
    
    ta "「Men don't sweat the small stuff.{p}\ \ One word for tasty is enough, right?{p}\ \ Seconds! 」"
    
    show to 002 with dis
    
    to "「I get it.{w} Since [fn] still has some,\n\ \ you can keep stuffing yourself nonstop. 」"
    fn "「How about I ask for seconds, then? 」"
    ta "「Hurry up and get your own restaurant.\n\ \ Then I can eat your cooking every day. 」"
    
    show to 007 with dis
    
    to "「Why does it have to be like that?{p}\ \ If I get my own store, I'm going to be using the\n\ \ Midoriya Group's truck all the time. 」"
    to "「You better be ready for that. 」"
    fn "「Hahaha! In that case, I'll also come every day\n\ \ and have you cook for me. 」"
    
    show to 003 with dis
    
    to "「You two are hyenas! 」"
    
    show ta 008 with dis
    
    ta "「No, I'm a dragon. 」"
    fn "「And I'm human, last I checked. 」"
    
    show to 007 with dis
    
    to "「Oh, whatever...{w} Just eat as much as you like. 」"
    
    show ta 004 with dis
    
    ta "「I would, even if you didn't say anything. 」"
    "It really would be great,\neating Torahiko's cooking every day..."
    
    jump end06

########################################    
label torahiko06_notgood:
    
    $ event_name = "Pasta should be..."
    $ love_tatsuki -= 1
    $ love_torahiko -= 1

    ta "「This is great. 」"
    "Tatsu-nii's eating it like it's great,\nbut I don't think it is at all..."
    
    play music free0456 fadein 1.5
    
    fn "「This is badly done. I can't eat it. 」"
    
    show to 003 with dis
    
    to "「...What?{p}\ \ What's badly done?{p}\ \ Just tell me! 」"
    fn "「The sauce has good flavour,\n\ \ but it's too watery. 」"
    fn "「You made it right now, so you couldn't help it,\n\ \ but it needs to boil down over a long time. 」"
    fn "「The flavor is also a bit unsatisfying.{p}\ \ I think you need to add anchovies, mozzarella,\n\ \ basil, and stuff like that. 」"
    
    play sound hit_s06_r
    show to at hit_right
    
    to "「Guh! 」"
    fn "「The choice of noodles was perfect, but... 」"
    fn "「The pack says 6 minutes on it,\n\ \ but you shouldn't always cook it that long. 」"
    fn "「Match what you make with the season,\n\ \ the temperature, the humidity... you need to vary\n\ \ the boiling time, stove heat, and amount of salt. 」"
    fn "「Then you could serve it, I think. 」"
    fn "「You'll need to serve it beautifully.\n\ \ Pile the pasta in the middle of the plate,\n\ \ then put the sauce on top... 」"
    
    show ta 008 with dis
    
    ta "「Now that you mention it, he always makes the\n\ \ things he wants,\n\ \ but I can't think of anyone else who eats it... 」"
    
    play sound hit_s06_r
    show to 007 at hit_right
    
    to "「Kuh! 」"
    fn "「But, that's not all.{p}\ \ What is it, there's a faint scent... 」"
    fn "「It's important to pay attention\n\ \ to this small thing... 」"
    fn "「In most pastas,\n\ \ the scent gives a soft, fresh taste. 」"
    to "「... 」"
    fn "「This sweet and sour scent... is it fruit?{p}\ \ It's not orange, not strawberry...{p}\ \ Not grape, not peach, not nashi... 」"
    fn "「That's it! 」"
    fn "「I heard in Italy, if they burn something,\n\ \ they add apples to adjust the flavour. 」"
    fn "「Because when you cook apples, in Italy,\n\ \ the taste is said to resemble tomatoes. 」"
    fn "「When you made the sauce,\n\ \ you added a squeeze of apple juice.{p}\ \ You did, right? 」"
    
    stop music
    
    show to 006 with dis
    
    to "「...No,{w} it was ketchup. 」"
    
    jump end06

##############################################
label torahiko06_disgusting:
    
    $ event_name = "What should I do...?"
    $ love_tatsuki += 1
    $ love_torahiko -= 1
    
    play music oo39_cho_ys001
    
    "What do I do...?"
    "I don't really like spaghetti.{p}Or tomatoes, for that matter..."
    "But, I can't just say I hate it."
    "Maybe I can bluff my way through this."
    fn "「Whoa, it's good. 」"
    
    show ta 002 with dis
    
    ta "「Tasty tasty. 」"
    
    show to 001 with dis
    
    to "「I see... if you don't want seconds, just tell me. 」"
    
    hide to with wipe_right
    
    "Damn...{p}That was a little cold.{p}Well, I'll leave the seconds to Tatsu-nii."
    
    show ta 001 at center with dis
    
    ta "「Phew, I ate so much.{w} Such good food and wine.{p}\ \ It was a good plan to do wine and cheese,\n\ \ after all.{w} {nw}"
    show ta 002 with dis
    extend "Okay, next is dessert. 」"
    
    play sound puu75
    
    fn "「Wai-{w=.3}what are you doing, stop it.{p}\ \ I told you not to touch me there, Tatsu-nii. 」"
    
    play music free44
    show ta 007 with dis
    
    ta "「C'mon, it's fine...! 」"
    ta "「Today, when I almost came out,\n\ \ weren't you touching me? 」"
    
    show ta 302 big at farright_big with circle_out2 
    
    ta "「That gorgonzola I ate earlier,\n\ \ it stank real bad,\n\ \ but what would you smell there? 」"
    "Tatsu-nii pinned me to his body, touched me here,\nthere, and all over, licked the back of my neck,{p}and generally sexually harrassed me."
    "Drinking habits are really bad.{p}It feels a little exciting,\nbut it's still really bad."
    fn "「It's bad, Tatsu-nii.{w} I won't eat it. 」"
    
    show to 003 at farleft behind ta with dis
    
    to "「It was bad, huh...{p}\ \ My bad for making something inedible. 」"
    fn "「That's wrong. It's not that, Tora, Tatsu-nii... 」"
    
    show to 006 with dis
    
    to "「Sorry, Tatsu-nii was a bust, too...{p}\ \ Don't force yourself to eat it.{p}\ \ Send the plate back, I'll clean up. 」"
    fn "「Wait, that's not it, Tatsu-nii's- 」"
    
    show ta 308 big with dis 
    
    ta "「You wait, too. You wanna touch, don't you?{p}\ \ Come over here. You can tie me up if you want. 」"
    fn "「Ahh! 」"
    "I give up."
    "I've been misunderstood,\nbut I wonder if I could persuade him..."
    
    jump end06
    
######################################
label kounosuke06:
    
    $ focus_character = "kounosuke"
    $ event_name = "Right, let's take Paranormal Pictures"
    stop music
    scene map
    hide screen kounocandy06
    scene candystoreout with dis
    show ko 005 at offright
    
    play music cicada01
    
    "「Thank you very much! 」"
    "With ice cream in one hand, {p}I leave the candy store."
    "Again I meet the horrible humidity and sun. {p}The weather today is a little too good..."
    fn "「It's so hot... 」"
    "I just bought this ice cream soda, {p}and it's already melting and dripping. {p}That was quick."
    "Hiding in the shade of the storefront, {p}I eat my ice cream, {p}and flap my shirt with my left hand."
    who "「Hey, [fn]! 」"
    "From across the road, {p}somebody waves their hand, {p}and comes this way."
    "That's..."
    fn "「Kounosuke? 」"
    
    play sound step03
    show ko at move_center(0.5) 
    
    ko "「Whew, I finally found you! 」"
    "In this awful heat, {p}you'll sweat just from standing. {p}You can imagine what'd be like if you ran."
    "Kounosuke's shirt sticks to his body. {p}It's soaked through with sweat. {p}He puts his hands on his knees and pants."
    fn "「What's wrong? You're out of breath. 」"
    ko "「Huh? It's not a big deal... 」"

    show ko 001 with dis
    
    ko "「Ah, that ice cream looks good! 」"
    fn "「You can't have it. 」"

    show ko 005 with dis
    
    ko "「Tightwad. 」"
    fn "「Go get some yourself. {p}\ \ Anyways, what do you want? 」"
    "I steer the dicussion back on track. {p}Kounosuke remembers what he came to me for, {p}and claps his hands together."

    show ko 001 with dis
    
    ko "「Ah, that's right. {p}\ \ This evening, around 7 or 8, {p}\ \ could you meet me in front of the school? 」"
    fn "「Why? 」"

    show ko 002 with dis
    
    ko "「I'm planning a test of courage! 」"
    fn "「A test of courage...? 」"

    show ko 001 with dis
    
    ko "「Yep. You know it's been so hot lately, {p}\ \ I figured this would be a good time to do it. 」"
    "A test of courage, huh..."
    ko "「It would be great with just 1 or 2 people. {p}\ \ Pleeeaaase!? 」"
    "As he says that, {p}Kounosuke puts both hands together, {p}and bows his head."
    "Indifferent to Kounosuke's preface, I..."
    menu:
        "A. Well, if you insist...":
            jump day06_accepttest
        "B. Sounds suspicious. I'll pass.":
            jump day06_declinetest

########################################
label day06_accepttest:
    #*承諾 #save file name probably
    
    $ love_kounosuke += 1
    $ kounosuke_test = True

    fn "「There's nothing to worry about? 」"
    "I had no reason to refuse the offer, {p}so I agreed to go."

    show ko 002 with dis
    
    ko "「Thank you [fn]!! 」"
    "With that, he tightly grasps my left hand, {p}and with all of his strength, {p}he shakes it up and down."
    fn "「Hey, I dropped my ice cream! 」"

    show ko 006 with dis
    
    ko "「Aah, sorry! 」"
    fn "「Jeez... 」"
    "He says that just as restless as ever, {p}but really he's over reacting."

    show ko 002 with dis
    
    ko "「But with this, {p}\ \ I've gathered a number of people. {p}\ \ I'm really thankful, [fn]! 」"

    hide ko with wipe_right
    
    ko "「Alright then. {p}\ \ Tonight, don't forget! 」"
    fn "「Yeah. 」"
    "Right as he's finished talking, {p}he runs off in the opposite direction he came. {p}What a busy guy..."
    "Really, Kounosuke was carefree back then, {p}but he was acting so restlessly, {p}usually..."
    "(Usually...?)"
    "As I was thinking to myself, {p}an alarm goes off in my head. {p}An alarm that's been dormant for 5 years."
    "For Kounosuke to talk like that suddenly, {p}means he has some good-for-nothing plan..."
    "Well, I know he doesn't mean any harm, {p}but..."
    "But his tendencies to get in trouble, {p}and his weird curiousities, {p}make him a nuisance sometimes..."
    "I mean, he really is a good guy, {p}so he has no bad intent."
    "(I wouldn't say it's strange, would I...?)"
    "Now I'm starting to get excited and anxious, {p}and I feel the midsummer air around my body."
    "I hope this isn't anything weird, {p}but I wonder..."
    
    jump day06_testofcourage

#####################################    
label day06_declinetest:  #This isn't used in the original, but may be brought in for an edited version 

    $ love_kounosuke -= 1

    fn "「Sorry, I don't think today will work... 」"

    show ko 006 with dis

    ko "「Eh!? 」"
    fn "「Look, I'm really sorry! {p}\ \ How about another time? 」"

    show ko 005 with dis

    ko "「Are you absolutely sure you don't want to? 」"
    fn "「I'm sure. 」"

    show ko 007 with dis

    ko "「I see... yeah. {p}\ \ Some other time, then. 」"

    hide ko with dis

    "Kounosuke's dropping shoulders make me feel... {p}guilty."
    "Actually, I have no plans tonight... {p}but wait a minute!"
    "Usually when Kounosuke's like that, {p}he's probably trying to get me involved. {p}Involved with something that's no good!"
    "Kounsouke usually doesn't mean any harm, {p}but it's hard to tell this time."
    "I just walk back into the candy store. {p}I feel a little sorry. {p}But that's about it."
    "(I guess it's a little late... {p}to not be cold to him, he's a nice guy.)"
    
    jump end06

###########################################
label day06_testofcourage:
    
    stop music fadeout 1
    scene black with sdis
    scene school01 red with dis
    play music higurasi

    "A little past 7:00 PM."
    "Being wrapped in the light of dusk, {p}the atmosphere feels kind of lonely."
    "As told by Kounosuke, {p}I'm in front of the school. {p}There's Torahiko and Shun."
    
    show to 001 red at midright
    show su 001 red at midleft
    with wipe_right

    to "「Oh, [fn]! 」"

    show su 002 red with dis
    
    su "「Ah, [fn]-san. Good evening! 」"
    "Kounosuke mentioned two other people coming, {p}this must be who he meant."
    fn "「Huh? Just two people? 」"

    show su 004 red with dis
    
    su "「Yep. 」"
    fn "「And Kounosuke? 」"

    show to 007 red with dis
    
    to "「Not here yet. 」"
    fn "「...... 」"
    #there's a comment here, 虎彦、いらつき. Translating shows it to be an irritated Torahiko sprite, but I guess it was never created. It should be added later if one is created
    to "「Jeez, he's the one who told us to come, {p}\ \ and of course he has to be here late... 」"
    "He hasn't made any progress at all..."
    "He's in high school already. {p}I thought he'd be a little better by now, {p}but..."
    fn "「His habit of being late... {p}\ \ he still hasn't gotten rid of it... 」"

    show to 001 red with dis
    
    to "「He's never going to get rid of it. 」"
    "Well, it's what I expected... {p}But it is Kounosuke. Hmm."
    "Should I say I'm impressed, {p}or should I just give up? {p}This mood makes me put my hand to my head."

    show su 002 red with dis
    
    su "「B-but I'm getting kind of nervous. {p}\ \ We're meeting at a time like this... 」"
    "To cover up for Kounosuke, {p}Shun-kun hastily changes the topic. {p}Wait, Shun-kun?"
    fn "「Huh? {p}\ \ Don't you have a curfew? {p}\ \ Is this going to be alright? 」"

    show su 001 red with dis
    
    su "「Oh, yeah! {p}\ \ My mom gave me permission. {p}\ \ No big deal. 」"
    fn "「Hmm... 」"
    "I'd say he's breaking his curfew, {p}so he can go out and play at this time. {p}I guess this tickled his childish curiousity..."
    "They're waiting in a similar way, {p}except Torahiko's getting frustrated, {p}while Shun-kun seems to be somewhat cheerful."

    show to 006 red with dis
    
    to "「Nevertheless, Kounosuke is such a slow guy. 」"
    
    stop music
    scene black with Dissolve(1)
    play music free0468

    "30 minutes later..."
    
    scene school01 night 
    show ko 001 night at offright
    show to 007 night at center
    show su 001 night at farleft
    with dis
    
    show ko at move_farright(1)
    
    ko "「You kept me waiting! 」"
    "By now, it had become darker. {p}Finally, the expedition leader shows up..."

    show to 003 night with dis
    
    fntora "{size=+50}『You're late. 』" 
    
    show ko 004 night with dis
    
    ko "「But I spent so much time preparing! 」"

    show to 007 night with dis
    
    to "「Even though you're the one who told us, {p}\ \ \"not to be late.\" 」"

    show ko 005 night with dis
    
    ko "「What!? I'm not late. {p}\ \ I told you to be here at 7 or 8, {p}\ \ didn't I? 」"
    
    show ko 001 night
    show su 004 night
    with dis
    
    everybody "「...... 」"
    "Kounosuke says that incorrigibly, {p}and puts it aside."

    show to 003 night with dis
    
    to "「I'm going home... 」"

    show ko 006 night at jump_up
    
    ko "「Wha!? I'm sorry I made you wait, {p}\ \ Torahiko! 」"
    to "「If that's what you really think, {p}\ \ then you can start by making an honest apology. 」"

    show ko 005 night with dis
    
    ko "「Y-yes, I'll reflect on this... 」"
    "Ah, I've missed this. {p}The comedy of Kounosuke and Torahiko."

    show to 001 night with dis
    
    to "「Alright then, what have you been planning? {p}\ \ You even called Shun out for this! 」"
    fn "「Isn't this a test of courage? 」"

    show to 005 night at jump_up
    
    to "「Coura...!? 」"

    show ko 002 night with dis
    
    ko "「Well, it's Summer, it's night, {p}\ \ and we're at the school, right? 」"
    "Then, Kounosuke's takes out a flashlight. {p}With a click of the switch, {p}he turns it on."
    
    scene school01 night
    show ko 002 night at midleft
    with dis

    ko "「Therefore... {p}\ \ this is now the, {p}\ \ \"Seven Wonders of Minasato School\" challenge."
    ko "I would like to hold a competition. {p}A test of courage competition! 」"
    "Getting himself psyched up, {p}Kounosuke begins to explain the rules."
    "We're to be divided into 2 teams of 2 pairs, {p}for every one of the Seven Wonders you find, {p}you get 3 points."
    "As proof of that, {p}you must take a picture at each location. {p}It's something like that."
    "For the sake of developing photos, {p}this seems like a good chance, {p}to take a lot of photos..."
    ko "「To not use all of the film, {p}\ \ would be a shame, wouldn't it? 」"

    show to 003 night at midright with wipe_right
    
    to "「W-wait a minute, {p}\ \ did I not hear that correctly!? 」"

    show ko 001 night with dis
    
    ko "「Huh? Ah, sorry. {p}\ \ Did I forget to say something? 」"

    show to 007 night with dis
    
    to "「On the pictures, {p}\ \ what if something... err... {p}\ \ strange shows up on one!? 」"

    show ko 002 night with dis
    
    ko "「I'm not expecting that. 」"
    ko "「Still, I'd like to take one myself... {p}\ \ a ghost photograph... 」"
    "......"
    "Kounosuke sounds so indifferent... {p}Everybody else is lost for words, {p}not just Torahiko."
    "Oh... I see."
    fn "「In other words... {p}\ \ this test of courage is just so... {p}\ \ you can take ghost photos...? 」"

    show ko at jump_up
    
    ko "「Yes. 」"
    "Just like always, {p}he can't come up with anything good."

    show to 003 night with dis
    
    to "「I-I... I don't want anything... {p}\ \ to do with this crap!! 」"
    fn "「Oh, why not? 」"

    show to 005 night with dis
    
    to "「[fn]? You too...? 」"
    fn "「Ghost photography aside, {p}\ \ I'll just consider this... {p}\ \ a normal test of courage."
    fn "Besides, this is nostalgic. 」"
    "In this old fashioned building, {p}is where we used to go to school."

    show ko at jump_up
    
    ko "「As expected of [fn]. {p}\ \ Being open-minded! 」"
    "Just like always, {p}Kounosuke's the only excited one..."
    "He goes on and on, {p}about what he was talking about earlier."
    "He still hasn't convinced Torahiko, {p}but as Kounosuke goes on, {p}Torahiko realizes that it's useless to resist."
    "He stays silent."
    
    hide ko
    hide to
    show su 004 night at center
    with wipe_right

    "And Shun-kun... {p}He's been silent for a while, {p}but it seems like..."
    "He's taking Kounosuke pretty seriously."
    
    hide su
    show ko 001 night 
    with wipe_right

    ko "「Well then, {p}\ \ let's decide how to split up... 」"
    "Now, what should I do?"
    menu:
        "A. Go with Kounosuke.":
            jump day06_pick_kounosuke
        "B. Go with Torahiko.":
            jump day06_pick_torahiko
        "C. Go with Shun.":
            jump day06_pick_shun

###########################################            
label day06_pick_kounosuke:

    $ love_kounosuke += 1
    $ ghost_encounter = 1
    
    fn "「Alright then... {p}\ \ I'll go with Kounosuke. 」"
    "Kounosuke is still out of control, {p}I'll go with him to keep an eye on him."
    
    scene black with dis
    
    "The places we're going to are the library, {p}the gym, and the art room."

    $ ghost_encounter = 1
    jump day06_testbegin

#############################################
label day06_pick_torahiko:

    $ love_torahiko += 1
    $ ghost_encounter = 2
    
    hide ko
    show to 007 night
    with wipe_right

    fn "「Alright then... {p}\ \ I'll go with Torahiko. 」"
    "Torahiko seems to be the most reliable, {p}so I choose him."
    
    scene black with dis

    "We're told to go to the gym, {p}the stairs, and the music room."

    $ ghost_encounter = 2
    jump day06_testbegin

###############################################
label day06_pick_shun:

    $ love_shun += 1
    $ ghost_encounter = 3
    
    hide ko
    show su 001 night at center 
    with wipe_right

    fn "「Alright then... {p}\ \ I'll go with Shun-kun. 」"
    "Of all of us here, {p}he's the youngest, {p}so I need to take care of him."
    "Who knows what would happen, {p}if I left him with Kounosuke or Torahiko."
    
    scene black with dis
    
    "The places we're supposed to go are the stairs, {p}the library, and the science room."

    $ ghost_encounter = 3
    jump day06_testbegin

##############################################
label day06_testbegin:
    
    $ event_name = "Secret of the Seven Wonders"
    play music higurasi fadein 2
    
    scene school01 night
    show su 004 night at midleft
    with wipe_right

    su "「Excuse me, may I say something? 」"

    show ko 001 night at midright behind su with wipe_right
    
    ko "「Sure Shun-kun. {p}\ \ What is it? 」"

    show su 001 night with dis
    
    su "「It's Minasato School's \"Seven\" Wonders. {p}\ \ Isn't that one too many? 」"
    fn "「Oh, that's right. 」"
    "I answer instead of Kounosuke."
    fn "「They say that, {p}\ \ when you know what the seventh wonder is, {p}\ \ something strange will happen. 」"
    fn "「Nobody knows what the seventh wonder is, {p}\ \ even I have absolutely no idea. 」"
    "I lower my tone, {p}to make it sound a little eerie."
    "A lukewarm, nighttime Summer breeze, {p}caresses my cheek."
    "The mood should have been perfect, {p}but it didn't seem to do much for Shun-kun."
    "He has a blank look on his face, {p}while I become more awkward."
    fn "「Th-the point is... {p}\ \ now you should be excited, {p}\ \ to see the seventh wonder! 」"

    show su 004 night with dis
    
    su "「Huh? 」"
    fn "「In other words, {p}\ \ the seventh wonder is a ghost story."
    fn "「A \"secret you're not supposed to know\", {p}\ \ kind of thing. {p}\ \ The rumor itself is a ghost story. 」"

    show su 002 night with dis
    
    su "「Oh, I see! 」"
    "In understanding, {p}Shun-kun's ears stand on end."
    "His tail sways gently behind him. {p}Oh, he's so cute..."

    show ko 005 night with dis
    ko "「[fn], that's not right... 」"
    fn "「Huh? 」"
    ko "「Of the Seven Wonders of Minasato School, {p}\ \ I have found the seventh. {p}\ \ I have really seen it! 」"

    show su 004 night with dis
    
    su "「Is that so? 」"
    fn "「This is the first time I've heard that. 」"

    show ko 001 night with dis
    
    ko "「Yeah. From what I've investigated, {p}\ \ there shouldn't be any doubt. {p}\ \ Those documents weren't easy to find... 」"

    show ko 002 night with dis
    
    "Nyahaha. {p}Kounosuke gives a deceiving laugh."
    "Hmm. {p}I've never heard this gossip before, {p}that Kounosuke is revealing."

    show ko 011 night with dis
    
    ko "「D-don't take my intelligence work... {p}\ \ so lightly! 」"
    fn "「N-no, I'm not... 」"
    "Kounosuke is being strangely on edge."

    show ko 001 night with dis
    
    ko "「Really? 」"
    fn "「Really. Anyways... {p}\ \ we've decided our teams. {p}\ \ Let's hurry up and go. 」"
    
    hide su
    hide ko
    with dis

    "So we went, {p}and made our way into the building."
    
    scene black with Dissolve(1)
    pause .3

    if ghost_encounter == 1:
        jump day06_kounotest
        
    if ghost_encounter == 2:
        jump day06_toratest
        
    if ghost_encounter == 3:
        jump day06_shuntest

############################################        
label day06_kounotest:

    $ event_name = "Gossip-loving Tanuki"
    stop music fadeout 2
    scene school hallway 1 night with dis
    pause 1
    scene school hallway 2 night with dis
    
    "The library."
    "There's a rumor that there's, {p}\"The Enthusiastic Bookworm\" here."
    "Apparently, {p}there was a student who loved books."
    "But right before graduation, {p}they died in a freak accident..."
    "However, that kid still loves books, {p}and has been haunting the library, {p}even beyond the grave."
    "Recently, an unknown student has been seen, {p}reading in this library."
    "However, when you take your eyes off of him, {p}even just for a moment, {p}he disappears completely."
    "Either that, {p}or you can see a faint outline of a person."
    "As far as I know, {p}the only sighting of one of the wonders, {p}has only been in this library."
    
    play sound door04
    pause .5
    show ko 001 night at center with dis

    ko "「Huh? 」"
    fn "「Looks like it's locked... 」"
    
    play sound door06
    pause 1
    show ko 005 night with dis
    
    ko "「Crap. Oh well... 」"
    
    show white with qdis
    play sound se_033
    pause .1
    hide white with qdis 
    
    "Kounosuke looks disappointed, {p}but if it's locked, {p}there's nothing he can do."
    "I feel discouraged right from the start, {p}but I take a picture for now. {p}We decide to go to our next location."

    scene school hallway 1 night with dis
    
    fn "「Is everywhere... {p}\ \ going to be locked up like this? 」"

    show ko 006 night at center with dis
    
    ko "「[fn], stop it, {p}\ \ don't say such negative things! 」"
    fn "「But isn't that normal for a school? 」"

    show ko 005 night with dis
    
    ko "「I thought that, you know... {p}\ \ the security would be a little more lax. 」"
    
    show ko 011 night with dis
    
    ko "「If push comes to shove, {p}\ \ I'll look for the key in the staff room. 」"
    fn "「That wouldn't be a good idea... 」"
    
    show ko 004 night with dis
    
    ko "「Eh? I know that's bad! {p}\ \ It was simply a joke. Really... 」"
    "That was definitely not a joke..."
    "Really, in the end, {p}I was right about keeping watch over him."
    
    scene black with Dissolve(1)
    pause .2
    scene school gym night with dis

    "The gym."
    "It's rumored that, {p}\"The Headless Basketball Player\" is here."
    "One night, {p}there were noises coming from the gym."
    "The teacher on night duty looked in, {p}and saw one of the students, {p}practicing basketball."
    "Thinking it was a strange time for that, {p}the teacher carefully went into the gym."
    "But upon a closer look, {p}the kid had no head."
    "And where the kid's head should've been, {p}there was a ball instead."
    "The teacher found the boy's head. {p}With a broad grin, {p}it looked at the teacher and laughed."
    "Then, it disappeared along with the body."

    show white with qdis
    play sound se_033
    pause .1
    hide white with qdis
    
    show ko 001 night at center with wipe_right
    
    ko "「By the way [fn], {p}\ \ do you know if that rumor is true? 」"
    fn "「You mean... {p}\ \ about the headless basketball player? 」"
    ko "「Not that, {p}\ \ the part at the end of the story. 」"
    fn "「The teacher found a ghost, {p}\ \ then it laughed and disappeared. 」"

    show ko 004 night with dis
    
    ko "「That's not right. 」"
    fn "「Huh? 」"

    show ko 001 night with dis
    
    ko "「That's actually an old rumor. 」"
    ko "「When the teacher found the ghost, {p}\ \ it walked up to the teacher, {p}\ \ and said \"I'm sorry.\""
    ko "Then, it thanked him, {p}and disappeared. 」"
    ko "「There's no laughing part of the story, {p}\ \ and besides, back then, {p}\ \ volleyball was the popular sport."
    ko "The story has changed a lot. 」"
    fn "「Ehh... 」"
    ko "「Perhaps the polite ghost wasn't scary enough? {p}\ \ So somebody changed it, {p}\ \ to make it more interesting."
    ko "They probably also changed the sport, {p}so it would seem more current. 」"
    "That's very detailed, Kounosuke."

    show ko 002 night with dis
    
    ko "「This perfectly matches my data! 」"
    "I'm impressed. {p}Kounosuke gives the V sign."
    ko "「Didn't I tell you? {p}\ \ Don't underestimate my intelligence network! 」"
    "Ah, I'm still concerned..."
    
    scene black with Dissolve(.5)
    pause .2
    scene school artroom night with dis

    "The art room."
    "To be honest, {p}I don't understand these rumors."
    "At night you can see a disembodied soul, {p}a shadow drawing, {p}a picture of Mona Lisa that moves,"
    "a sculpture of Mona Lisa that talks, {p}or even a ghost that makes sculptures..."
    "The list goes on and on. {p}If I recall correctly, they call this place, {p}\"The Arts and Crafts Room of Mystery.\""
    fn "「So, anyways... 」"
    "Why is it that... {p}there are so many rumors about this place?"
    "The Mona Lisa is hanging on the wall, {p}and there are sculped faces, {p}and hands at the back of the room."
    "It feels creepy enough by itself, {p}and shining a light through the darkness, {p}makes it extra eerie."
    
    show white with qdis
    play sound se_033
    pause .1
    hide white with qdis

    "...but this eerie atmosphere... {p}it doesn't seem to affect Kounosuke at all..."

    show ko 001 night at center with wipe_right
    
    ko "「Well then [fn], {p}\ \ we should be getting back soon. 」"
    fn "「Y-you know, Kounosuke, {p}\ \ aren't you being pretty slow? 」"

    show ko 005 night with dis
    
    ko "「What's with you all of a sudden? {p}\ \ That's rude... 」"
    fn "「No, it's just... 」"
    "No, I don't believe. {p}But even though I don't believe, {p}this place still..."
    "...just doesn't have a good feeling."

    show ko 001 night with dis
    
    ko "「This is the place, right? {p}\ \ Where all the ghost stories are about? 」"
    fn "「Y-yeah. It is, {p}\ \ but what do you have to say about it? 」"
    "Why is he so... calm?"
    "While Kounosuke searches for something, {p}I roll my eyes in complaint."
    "Then, he points his light at a single picture."
    
    scene old drawing with dis
    play music free58
    
    ko "「That's the picture. 」"
    fn "「What? 」"
    ko "「One of the wonders... {p}\ \ of the arts and crafts room. 」"
    "The picture was drawn with crayons. {p}It was probably drawn unskillfully, {p}by some elementary school kid."
    "There's the school building, {p}and a lot of kids are playing."
    "Someone is wearing a red and white hat, {p}this is a picture of sports day."
    "This picture isn't all that realistic, {p}and I don't feel anything weird about it."
    "Instead, I'm definitely more afraid... {p}of that Mona Lisa on the wall."
    "I wonder... {p}What does this have to do the the rumors?"
    ko "「Apparently, a ghost drew this picture. 」"
    fn "「A ghost drew it...? 」"
    ko "「The rumor here is called \"The Lonely Artist\". {p}\ \ A long time ago at this school, {p}\ \ there was a student with a very frail body. 」"
    "He wanted to play with the other students, {p}but he couldn't. {p}He had lunch instead of gym class."
    "So, from this room, {p}he watched the schoolyard instead, {p}and drew pictures."
    "While the others were in the schoolyard playing, {p}he would secretly mix himself in with them."
    "However, that student's disease got worse, {p}and he died."
    "After that, {p}the student settled down into his drawing."
    "He said that now, {p}he could play with everybody in it."
    "This is where the story gets weird..."
    "When you look into that picture, {p}it sucks you in. {p}No, it turns you into a sculpture!"
    "The Mona Lisa and the boys are friends, {p}and every night they talk to each other."
    "No no, the Mona Lisa talks to the sculptures. {p}The Mona Lisa turns students into sculptures."
    "Don't know what happened with the original story. {p}But they go on and on like that."
    "That's why it really is, {p}\"The Arts and Crafts Room of Mystery.\""
    
    scene school artroom night
    show ko 005 night at center
    with wipe_right

    ko "「Besides, ghosts were originally people, {p}\ \ right [fn]?"
    ko "So when you think about it, {p}there's nothing to be afraid of."
    ko "Curiously enough, {p}you know what I'm more afraid of? {p}Having an annoying partner! 」"
    fn "「I-I see... 」"
    "I think his reasoning is mixed up, {p}but Kounosuke appears to be composed about it."
    
    stop music
    show ko 002 night with dis

    ko "「Incidentally, {p}\ \ the student who painted this picture, {p}\ \ is actually still perfectly alive. 」"
    fn "「Huh? 」"
    ko "「Have you not noticed it yet, [fn]? 」"
    "To see why Kounosuke is laughing, {p}I take another close look at the picture."
    
    play music oo39_cho_ys001
    scene old drawing with dis

    "Come to think of it, {p}before I transferred, {p}I think I saw this picture."
    "It says: {p}[fn] [ln], 5th Year"
    "This is my drawing!"

    scene school artroom night
    show ko 002 night at center 
    with dis
    
    ko "「Did I fool you? 」"
    fn "「I completely fell for it... 」"

    show ko 001 night with dis
    
    ko "「Sorry, sorry. {p}\ \ But what I said earlier is true."
    ko "Unfortunately though, {p}the ghost's drawing has never been found. 」"
    fn "「Is that right... 」"
    "Afterwards, {p}he had so much fun fooling me, {p}that for the whole time,"
    "a smile stuck to his face."
    "...I'll get even some day."
    
    play music musi2
    scene black with Dissolve(1)
    pause .2
    scene school entryway night with dis

    "We went back to the entranceway, {p}and it appears that we are early, {p}as the other two still had not gotten back."
    "We just have to wait, {p}but Kounosuke can't sit still. {p}He keeps clicking his shutter at things."
    
    show ko 001 night at center with dis

    ko "「They're both slow. 」"
    fn "「Kounosuke's the one saying that...? 」"
    "However, they sure are taking their time. {p}Maybe I should go look for them? {p}But I might miss them."
    
    play sound double_step
    scene school hallway 1 night
    show to 008 night at offleft
    show su 003 night at offleft
    with dis
    pause 1

    "Ah, are they coming?"
    torashun "「G-g-g-g... 」"
    
    show to at move_midright(0.25)
    show su at move_midleft(0.2)
    
    torashun "{size=+30}「GET OUT!! 」"
    
    stop sound fadeout .5

    fn "「Geh, T-Torahi... you're back... 」"
    
    hide to
    show to 008 big night at right 
    with dis
    
    to "「We gotta get out of here! {p}We saw it! 」"

    show su at shivering

    su "「[fn]-san, please help! 」"
    fn "「P-please, y-you're gonna kill me! 」"
    
    scene school entryway night
    show su 003 night at farleft    
    show to 008 night at center
    show ko 006 night at farright
    with dis
    show su at shivering

    ko "「Torahiko, what are you doing!? {p}\ \ [fn]'s going to die! 」"
    
    show to at jump_up

    to "「It's not that! {p}\ \ Look, right over there 」"
    fn "「Guh... 」"
    "Right over there, {p}in front of me, {p}I can see the River Styx..."
    "Once I recover from a lack of oxygen, {p}I understand what's going on, but... {p}Aah, my vision is blurry..."
    "I feel like I'm seriously going to fall down. {p}While trying to keep my consciousness, {p}I look up and see that those two have arrived."
    
    stop music
    scene school hallway 1 night
    show na 201 night
    play sound giwaku1
    pause 3
    
    "That's... what?"
    
    #$ saw_nana = True #Not really sure what the point of this is when you can use the $ ghost_encounter flag
    
    show white with qdis
    play sound se_033
    pause .1    
    hide white
    hide na 
    with qdis
    
    ko "「Eh? 」"
    to "「Ah... 」"
    su "「Huh? 」"
    "I hear their three dumbfounded voices."
    "Choking, I try to bring air into my lungs, {p}I look in the same direction, and..."
    
    scene school entryway night
    show bo 003 big night at center_big #Make big
    with wipe_right

    fn "「Eh, Botan, teacher? 」"
    
    show bo at jump_up_big
    pause .1
    show bo at center_big

    bo "{size=+15}「WHAT ARE YOU DOING HERE, {p}\ \ AT A TIME LIKE THIS!!?? 」"

    scene white with qdis
    play sound puu79_a
    pause.1
    scene black with qdis    
    pause .1
    play sound puu79_b
    scene white with qdis
    pause .1
    scene black with qdis
    pause .1
    play sound puu79_a
    scene white with qdis
    pause .1
    scene black with qdis
    pause.1
    play sound puu79_b
    scene white with qdis
    pause .1
    scene black with qdis
    play music free51
    
    pause 4
    
    scene school01 night
    show su 003 night at farleft
    show to 003 night at farright
    show ko 005 night at center
    with wipe_right

    to "「I told you! {p}\ \ This was a bad idea from the beginning! 」"

    show su at shivering
    
    su "「Ooh, my head hurts... 」"

    show to 007 night with dis
    
    to "「Kounosuke, this is all your fault. 」"
    
    show ko at jump_up

    ko "「S-sorry... 」"
    fn "「But Torahiko, that was really tight. {p}\ \ I thought I nearly saw the River Styx... 」"
    "I had seen the Styx, {p}but just for an instant, {p}I saw something strange."
    to "「Eh? Oh, r-really? 」"

    show ko 004 night with dis
    
    ko "「All brawn and no brains! 」"
    
    show to 003 night at jump_up

    to "「What!? {p}\ \ But it was you in the first place- 」"
    fn "「Come on now... 」"
    "I try to calm those two down, {p}and call out to Shun-kun, {p}who was completely in the outfield."
    "Since the test of courage, {p}we were noisy all the way home."
    
    scene black with dis
    
    scene path night
    show su 004 night at farleft
    show to 003 night at farright
    show ko 002 night at center
    with dis

    "On the way back,\nTorahiko was still complaining, {p}but even after all that,"
    "I don't know if Kounosuke even understood."
    "While those two are arguing, {p}I try to calm Shun-kun."
    "Which reminded me, before I transferred, {p}the mood was always like this. {p}I've missed this."
    
    jump day06_testend
    #[jump target="*４帰り道"]

######################################    
label day06_toratest:

    $ event_name = "The Cowardly Tiger"
    play music musi2
    scene school gym night with dis

    "The gym."
    "There's a rumor of a \"headless basketball player\" here."
    "One night, there were noises coming from the gym. {p}The teacher on night duty looked in, {p}and saw one of the students practicing basketball."
    "Thinking it was a strange time to be doing that, {p}the teacher carefully went into the gym."
    "But upon a closer look, {p}the kid had no head."
    "And where his head should've been, {p}there was a ball."
    "The teacher found the boy's head. {p}With a broad grin, {p}it looked at the teacher and laughed."
    "Then, it disappeared along with the body."

    show to 006 night at center with wipe_right
    
    to "「Th-there's nothing here. 」"

    show to at shivering
    
    fn "「Torahiko, you're grabbing my arm too tight. 」"

    show to 005 night at still with dis

    to "「Ah, s-sorry... 」"

    show to 001 night with dis
    
    "Hmm..."
    "He lets go for a moment, {p}but a few steps later he grabs back on again."
    "It's not that I don't like this, {p}I just wish his grip was a little weaker."
    
    show white with qdis
    play sound se_033
    pause .1
    hide white with qdis
    
    fn "「You know Torahiko, {p}\ \ I was just thinking something earlier. 」"

    show to 007 night with dis
    
    to "「Wh-what? 」"
    fn "「Torahiko, are you scared? 」"

    show to 003 night at jump_up
    
    to "「I-I'm not scared! 」"

    show to 007 night with dis
    
    to "「I'm not afraid, not at all. {p}\ \ But I don't like this. 」"
    fn "「Doesn't that just mean you're scared...? 」"

    show to 003 night with dis
    
    to "「I'm not scared, that's not it! 」"
    fn "「Uh huh, sure... 」"
    "Well, I'll just leave it at that for now."
    "Perhaps I've been in a bad mood since we came in. {p}I wasn't amazed with Kounosuke's plan."
    "I didn't want to do a test of courage, {p}so why are we doing this?"
    
    stop music fadeout .5
    scene black with dis
    pause .2
    scene school stairway night with dis

    "The stairs on the north side of the school building."
    "The wonder here is called, {p}\"The Spiral Staircase of Evil\"."
    "The stairs are connected to a mysterious space, {p}and if you're just walking absentmindedly, {p}you'll never make it to the next floor."
    "At the landing of the stairs, {p}there are mirrors that can lead to the underworld. {p}And if you leap into them, you can go there."
    "There are a bunch of other stories like that."

    show to 001 night at center with wipe_right
    
    to "「...... 」"
    
    show to 005 night at briefzoom 
    show to 001 night with dis

    fn "「...... 」"
    to "「...... 」"

    show to 005 night at jump_up
    pause .1
    
    show to 006 night with dis

    fn "「...... 」"
    "For some time now, {p}Torahiko has been holding onto my arm."
    "I'm afraid to be afraid... {p}But the one next to me is so scared, {p}that it calms me down for some reason."
    "My arm is simply in pain. {p}Torahiko is hopless like this. {p}I wasn't expecting him to be like that."

    show white with qdis
    play sound se_033
    pause .1
    hide white with qdis
    
    "I face towards the mirror and click my shutter, {p}finishing my quota for this area."
    "Then, I immediately think about our next location. {p}But... there seems to be something... {p}something in the mirror."
    "I stand still and call out to Torahiko."
    
    play music oo39_cho_ys001
    
    fn "「T-Torahiko...? 」"
    to "「Wh-what? 」"
    fn "「Th-the mirror... 」"
    to "「The mirror? 」"
    fn "「On your shoulder! 」"
    "We both look into the mirror, {p}a hand reaches out from behind Torahiko..."
    
    show to 005 night at jump_up

    to "{size=+15}{nw}"
    play sound bosu32
    extend "「UWAAAAAA!! 」"
    
    show to at move_offleft(0.2) 
    
    "The moment he sees that, {p}Torahiko runs to dash up the stairs."
    "I chase after him in hot haste, {p}and catch him as he's climbing the staircase."
    
    scene school hallway 1 night with wipe_right

    "We safely make it to the next floor. {p}There aren't any more stairs that lead up."

    show to 005  night at center with wipe_right
    
    to "「Th-th-that thing appeared. {p}\ \ It did, didn't it? {p}\ \ Did you see it? J-just now? 」"
    "He is completely shocked. {p}I purposely grin and laugh at Torahiko."
    fn "「Yep. That hand that appeared behind you, {p}\ \ was my hand! 」"
    "Then, I give him the V sign."
    
    play sound freeze04
    
    fn "{size=+15}「The Paranormal Phenomena. 」" 
    
    show to 003 big night at center_big with dis 
    
    to "「[fn]!! 」"
    
    play sound attack00
    pause .8

    fn "「Uncle, uncle! {p}\ \ You're squeezing me too much! 」"
    to "「Shut up! 」"
    "I-I didn't think it would work this well."
    "While receiving a jokingly strong headlock, {p}I desperately apologize to him."
    
    stop music fadeout .5
    scene black with dis
    pause .5
    scene school hallway 1 night with dis

    fn "「But still, {p}\ \ you're such a scaredy cat, Torahiko. 」"

    show to 003 night at center with dis
    
    to "「There's nothing I'm afraid of! {p}\ \ It's just that... {p}\ \ I-I don't like this kind of stuff! 」"
    fn "「Hahaha! 」"
    "I wish he would just admit it already."
    "For him to be so panicked, {p}and yet still desperately deny it, {p}is so adorable, and makes me laugh."

    show to at jump_up
    
    to "「It's true! {p}\ \ Really, I'm not s-scared at all! 」"
    
    play sound metronome loop
    $ renpy.music.set_volume(0.5, 0.0, channel = "sound")
    play music ambience01 fadein 3
    scene school hallway 3 night

    "At the other end of the darkness, {p}I hear a sound."
    "Not only does Torahiko freeze, {p}but I do too."
    "In the completely silent school building, {p}there is certainly a ticking sound."

    $ renpy.music.set_volume(0.8, 4.0, channel = "sound")

    "It's the sound of a metronome, {p}swaying back and forth..."
    "It's ahead of us. {p}The music room. {p}The wonder there is \"The Shapeless Musician\"."
    "When the room should be empty, {p}you can hear the sound of a piano."
    "The metronome, which hasn't been touched, {p}is said to start ticking its own rhythm."

    show to 008 night at center with wipe_right
    
    to "「A-are we going in there? 」"
    fn "「Wh-what should we do? 」"

    show to 008 big night at center_big with dis
    
    to "「It's too dangerous! 」"
    fn "「B-but then we won't get any pictures. 」"
    "It's not just about Kounosuke, {p}It's about Shun-kun too."
    "As his senpai, if I were to say, {p}\"I couldn't take any pictures, {p}because I was too scared\","
    "that would be really lame."
    
    hide to with dis
    $ renpy.music.set_volume(1.0, 0.5, channel = "sound")

    "Slowly approaching the music room, {p}the sound becomes clearer."
    "There's no mistaking it, {p}that's the sound of a metronome."
    "It's the middle of the night, {p}nobody could have mistakenly turned it on."
    "Also, it's Summer vacation, {p}so there's no reason for anybody to go in there."
    "I grab onto my camera with my sweaty palms. {p}Torahiko is hiding behind me, {p}and won't let go of my shirt."
    "Huddled next to each other, {p}we stand before the music room's door, {p}which was ajar for some reason."
    "Gulp..."
    "I make up my mind, {p}and boldly peer into the opening, {p}for just a moment."
    
    stop music
    $ renpy.music.set_volume(0.5, 0.0, channel = "sound")
    play sound2 bosu32
    
    show white with qdis
    play sound2 se_033
    pause .1
    hide white with qdis
    show school hallway 3 night at hshake 

    fntora  "{size=+40}「UWAAA!! 」"


    show ko 001 night at center with dis
    
    ko "「Great success! 」"
    "A sudden flash of light comes from the music room. {p}Then, a familiar voice and, {p}illuminated by a flashlight, a familiar face."

    show ko 002 night with dis
    
    ko "「How was it? Were you surprised? 」"
    "Why is Kounosuke here? {p}Great success? {p}Why is he laughing..."
    "Err... {p}In other words, the metronome earlier..."
    "So it's like that?"
    fntora "「Ko... 」"
    "Once I understand the source, {p}my fear from earlier disappears."
    "Something different fills my head instead, {p}and boils over."
    fntora "{size=+ 40}「KOUNOSUKE!! 」"
    
    show ko 006 night at jump_up

    ko "「Th-that hurts, let me go! 」"
    fntora "{size=+10}「SHUT UP!! 」"
    "Torahiko puts him in a headlock, {p}and I use my rubbing combination technique."
    
    show ko 005 night with dis
    
    ko "「I-I'm dying! 」"
    "After a bit, we finally free him, {p}he holds his head and groans."
    
    scene school hallway 1 night
    show ko 005 night at midright
    show to 003 night at midleft
    with wipe_right

    ko "「Oohh... 」"
    fn "「That was a bad, good-for-nothing trick! 」"
    to "「It's just as [fn] says! 」"
    ko "「Oh, if I was a ghost, {p}\ \ I'd definitely haunt you... 」"
    "While cursing us out, {p}Kounosuke staggers over to the metronome, {p}and stops it."

    stop sound 
    
    "With the metronome turned off, {p}the school is silent again."
    fn "「Huh? Kounosuke, where's Shun-kun? 」"

    show ko 001 night with dis
    
    ko "「Eh? Oh, he's below us. 」"

    show to 005 night with dis
    
    to "「Wait, why did you leave him behind!? 」"
    ko "「If the two of us needed to escape, {p}\ \ I would lie in wait untill morning. {p}\ \ So I asked him to wait in the hallway. 」"
    fn "「Irresponsible as ever... 」"
    ko "「But I made sure to give him a flashlight! 」"

    show to 003 night with dis
    
    to "「Still, why did you leave him behind? 」"

    show ko 005 night with dis
    
    ko "「That's... 」"
    fn "「Enough of that, {p}\ \ let's just hurry and find Shun-kun. 」"

    show ko 002 night with dis
    
    ko "「Th-th-that's right! {p}\ \ That's a good idea, [fn]! 」"
    
    show ko at move_offleft(0.5)
    show to 008 night with dis

    to "「Ah, don't try to get out of this! 」"
    ko "「Hurry, hurry. Let's go to Shun-kun. 」"

    show to 007 night with dis
    
    to "「Jeez, that guy... 」"
    fn "「Come on, come on... 」"
    
    show to at move_offleft(0.5)

    "I forget the anger I was feeling up to now, {p}and it's replaced with fear once again."
    "Without grabbing onto my shirt this time, {p}Torahiko stomps after Kounosuke."
    "Nearly leaving it behind, {p}I close the door to the music room. {p}I get beside Torahiko in a hurry."
    
    scene black with dis
    scene school stairway night with dis

    "We join Kounosuke at the bottom of the stairs, {p}who was waiting for us, {p}then the three of us proceed to the first floor."
    "Being lined up like this, {p}is kind of nostalgic."
    "In the past, {p}it was mainly on Kounosuke's whim, {p}but us three would go out and do something foolish."
    
    show ko 001 night at midleft
    show to 001 night at midright
    with wipe_right

    ko "「But that was fun. 」"
    to "「We're not having any fun. {p}\ \ Right, [fn]? 」"
    fn "「Well, it was quite the thrill, wasn't it? 」"

    show ko 002 night with dis
    
    ko "「You've got an open mind, just as I expected! {p}\ \ That's completely different, {p}\ \ from a certain someone... 」"
    to "「Did you say something? 」"
    "Without changing his expression, {p}Torahiko squeezes his open hands together."

    show ko 005 night with dis
    
    ko "「N-nothing, nothing... 」"
    "Always one word too many, Kounosuke."

    show ko 001 night with dis
    
    ko "「But, it's alright to have a crazy night, {p}\ \ every once in a while. 」"
    to "「The school isn't a good place for that, {p}\ \ don't you think? 」"

    show ko 002 night with dis
    
    ko "「Then should we have our next test... {p}\ \ at a shrine? 」"

    show to 003 night with dis
    
    to "{size=+15}「And this is why... 」"
    fn "「Oh, will you two just shut up already! 」"
    "Somehow, we manage to get to the first floor."
    
    play music musi2
    scene black with dis
    pause .3
    scene school entryway night with dis

    "Even though I really hope to see it, {p}Shun-kun's figure is not there. {p}Just the glow of my flashlight."

    show to 001 night at center with wipe_right
    
    to "「Anybody there? 」"
    fn "「Kounosuke, where's Shun-kun? 」"
    "I call back to where Kounosuke is, {p}but there's no answer."
    fn "「Kounosuke? 」"
    "I look back and there's nobody there."
    fn "「Eh...? 」"
    
    show to 005 night at jump_up
    
    scene white with Dissolve(.8)
    pause 1
    
    scene school entryway night
    show ko 002 night at center
    show su 001 night at farright
    with dis

    ko "「Boo! Surprised? 」"

    show su 002 night with dis
    
    su "「Oh, Kounosuke-san, you're so bad. 」"
    "Then, those two come out from the shadows. {p}They turned off their flashlights, {p}and were hiding."

    show to 007 night at farleft with wipe_right
    
    to "「Once again, you disgust me... 」"

    show ko 001 night with dis
    
    ko "「Woah, that didn't go over so well. 」"
    fn "「No wonder. That was the second time! 」"

    show to 003 night with dis
    
    to "「I'll fix this! {p}\ \ I'll make you into the seventh wonder! 」"
    
    show ko 006 night at move_midright(0.25)

    ko "「Waah! Shun-kun, help! 」"

    show su 004 night with dis
    
    su "「Eh? Ahwawawa! 」"
    "Torahiko tries to grab Kounosuke, {p}but Kounosuke uses Shun-kun as a shield, {p}and hides behind him."
    "Shun-kun is stuck, {p}and doesn't know what to do."
    fn "「Hey you two, stop bothering Shun-kun. {p}\ \ Besides, at a time like this, {p}\ \ why don't you just save it for tomorrow? 」"

    show to 001 night with dis
    
    to "「Aah, alright...{nw}"
    show su 002 night with dis
    extend " 」"  
    su "「I've been saved! 」"
    to "「We should finish up soon. 」"
    
    hide ko
    show ko 001 night at midright
    with dis

    ko "「Roger that. 」"
    
    scene black with dis
    
    scene path night
    show to 003 night at farleft
    show ko 002 night at center
    show su 004 night at farright
    with wipe_right

    "On the way back, {p}Kounosuke teased Torahiko, {p}and even got Shun-kun involved."
    "I tried to calm them."
    "This reminded me, before I transfered, {p}it was always like this. {p}I've missed it."
    
    jump day06_testend

#############################################
label day06_shuntest:

    $ event_name = "Small Wolf"
    stop music fadeout 2
    scene school stairway night with dis
    
    "The stairs on the north side of the school building."
    "The wonder here is called, {p}\"The Spiral Staircase of Evil\"."
    "The stairs are connected to a mysterious space, {p}and if you're just walking them absentmindedly, {p}you will never make it to the next floor."
    "At the landing of the stairs, {p}there are mirrors that lead to the Underworld. {p}If you leap into them, you can go there."
    "There are a bunch of other stories like that."

    show su 004 night at center with dis
    
    su "「I-is this the place? 」"
    "He's scared, and clings to me tightly. {p}Yeah, I have to be his senior, {p}so I try to appear confident."

    show white with qdis
    play sound se_033
    pause .1
    hide white with qdis
    
    "To be honest, I am a little scared, {p}but I keep a calm facade. {p}I set up my camera to take a picture."
    fn "「Is this okay? 」"
    su "「I think it's good. 」"
    fn "「Then let's go to the next place. 」"

    show su 002 night with dis
    
    su "「Okay! 」"
    "Whether it's because I'm trying to appear excited, {p}or I'm trying to appear scared, {p}I hold out my hand and he firmly grasps it."
    "The two of us head up the stairs."
    "This isn't the kind of place... {p}you would go on a date at... {p}Wait, why am I even thinking about that!?"
    fn "「By the way, Shun, {p}\ \ there's something I've been wondering about. 」"

    show su 001 night with dis
    
    su "「What is it? 」"
    fn "「Did you not know what the Seven Wonders were? 」"
    su "「Yeah. {p}\ \ I'd never heard any rumors about this school. 」"
    fn "「Hmm... 」"
    "So it's just between us, {p}I thought this was like a major story..."
    su "「Is it a famous story? 」"
    fn "「Well, it is for us. 」"
    "In our case, {p}Kounosuke is our only source."
    "That kind of gossip was our information. {p}They were just things he would hear about."
    "Actually, I guess it... {p}wasn't really that famous of a story?"

    show su 004 night with dis
    
    su "「Err... 」"
    fn "「Hm, what? 」"

    show su 001 night with dis
    
    su "「The Seven Wonders... {p}\ \ what kind of story is it? 」"
    fn "「Oh. Umm... 」"
    "We proceed to the next floor. {p}I tell Shun-kun about the Seven Wonders, {p}and the rumors surrounding them."
    "The stairs on the north side of the school are, {p}\"The Spiral Staircase of Evil\"."
    "In the science room is \"The Moving Mannequin\"."
    "The gym has \"The Headless Basketball Player\"."
    "In the music room is, {p}\"The Shapeless Musician\"."
    "And in the library is, {p}\"The Enthusiastic Bookworm\"."
    "Then there's \"The Arts and Crafts Room of Mystery\"."
    fn "「We're at \"The Spiral Staircase of Evil\". {p}\ \ Kounosuke said something about the last one, {p}\ \ but I don't know anything about it... 」"
    su "「I see. 」"
    "As we reach the top of the stairs, {p}I finish talking."
    fn "「...Hm? 」"
    su "「Is something wrong. 」"
    fn "「No, but we were going up the stairs... {p}\ \ as we were talking, right? 」"

    show su 004 night with dis
    
    su "「Huh? Yeah. 」"
    fn "「And we didn't stop in the middle? 」"

    show su 001 night with dis
    
    su "「No, we didn't. 」"
    "The Seven Wonders, well six to be exact, {p}isn't a story that can be summed up shortly."
    "And yet... {p}we climbed the stairs, {p}right up until the end of it..."
    "Are those stairs really that long?"

    show su 004 night with dis
    
    su "「[fn]-san...? 」"
    fn "「Ah, oh. It's nothing. {p}\ \ Just my imagination, yeah. 」"
    "Just my imagination, just my imagination."
    "I felt like I was in a daze while talking, {p}but only my feet slowed down while walking. {p}Yeah, that's it."
    "While hurrying away from that spot, {p}I repeatedly tell myself, {p}that it's all in my head."
    
    scene black with dis
    scene school hallway 1 night with dis
    pause .5
    scene school hallway 2 night with dis

    "The library."
    "There's a rumor that there's, {p}\"The Enthusiastic Bookworm\" here."
    "Apparently, there was a student who loved books, {p}but the kid died in a freak accident, {p}right before graduation."
    "However, that kid still loves books to this day, {p}and has been living in the library to read, {p}even beyond the grave."
    "Currently, an unknown student has been reading books, {p}and when you take your eyes of him for just a bit, {p}he completely disappears from sight."
    "That, or you see a faint glowing figure of a person."
    "As far as I know, {p}the only eyewitness account of these wonders, {p}has only been in this library."

    play sound door04
    pause .5
    
    fn "「Huh? 」"
    
    play sound door06
    pause 1
    show su 001 night with qdis

    su "「Looks like you need a key... 」"
    "I soon see another door, {p}but it's also locked."
    fn "「Hmm... what to do... 」"

    show su 004 night at center with dis
    
    su "「Eh? Well, what could we do? 」"
    fn "「Hmm, well, it seems... {p}\ \ there's nothing that can be done. 」"

    show white with qdis
    play sound se_033
    pause .1
    hide white with qdis
    
    "I point my shutter through the glass on the door. {p}I have a feeling Kounosuke will complain about it, {p}but I can't do anything else."
    "What happened earlier was a little creepy... {p}No, it's just my imagination."
    
    scene black with dis
    scene school hallway 1 night with dis
    pause .5
    scene school hallway 2 night with dis

    "The science room."
    "The rumor here is \"The Moving Mannequin\"."
    "It is said that, {p}it's common for the mannequin in there, {p}to move in the middle of the night."
    "Ooh, I don't like this one..."
    "That mannequin is old, {p}and if it moves even just a little bit, {p}it makes a creepy squeaking noise..."
    "I touched it once out of curiosity, {p}it moved, and it really freaked me out."
    "Well, it had simply become weakened, {p}but its arm just dropped off."
    "When that happened, well... {p}talk about childhood trauma."
    "Long story short, the science room, {p}it's somewhere I don't want to be in at night. {p}Well, that is, behind the bathrooms."
    "Although, I don't think the bathrooms are a wonder, {p}so, I guess this is still number one."
    fn "「That mannequin... 」"
    
    show su 001 night at center with qdis

    su "「What's wrong? 」"
    "Remembering my childhood trauma, {p}I hesitate to take my hand away from the door, {p}and I start talking to Shun-kun."
    fn "「I think it would be best to... {p}\ \ just skip over this place! 」"
    su "「Really? 」"
    "\"Really\", he says... {p}Aren't you afraid too, Shun-kun?"
    "Well, I'm not too scared, {p}It's just that... well... {p}I don't like this creepy feeling..."
    "I-I'm a disappointment. {p}I can't show my miserable face, {p}in front of Shun-kun."
    su "「Ah, is that so? {p}\ \ I don't understand, [fn]-san. 」"

    show su 002 night with dis
    
    su "「The science room's mannequin... {p}\ \ isn't it gone? 」"
    fn "「Huh? 」"
    su "「That thing was so old, {p}\ \ they must have thrown it away! 」"
    "I-is that true!?"
    "What...? {p}If that's the case, {p}then there's no need to skip here."
    "No, instead this was the right place to go to."
    "I mean, there's nothing too weird here, {p}and when you take away the mannequin, {p}all that remains is a slightly smelly class room."
    "Now knowing this, {p}there's really nothing to be afraid of."
    
    hide su with dis
    play sound tm2_slidedoor000
    pause 1
    scene mannequin with explosion
    pause 1.5

    "I-IIIIIIIIII-"
    
    scene school hallway 2 night with dis
    show su 003 night at center
    pause .01
    show su at briefzoom

    fnsu "{size=+15}「IT'S HERE!! 」"
    "Spontaneously, we cling to each other and scream."
    
    scene black 
    show su 003 night at center
    with dis
    
    pause .5
    
    scene school hallway 1 night
    show su 003 night at center
    with dis

    fn "「Why, why? {p}\ \ Didn't they already get rid of it!? 」"
    su "「I-I don't know! 」"
    "Completely caught off guard, I panic. {p}I grab Shun-kun by the shoulders, {p}and violently shake him."

    show su 006 night with dis
    
    su "「Hauu. [fn]-san, {p}\ \ my eyes are spinning... 」"
    "At his words, I snap back to reality. {p}The next thing I know, he's in my arms, {p}his eyes are rolling, and he's gone limp."
    fn "「Whoa! Shun-kun, {p}\ \ get a hold of yourself!! 」"
    su "「Kyuuu... 」"
    "I'm a disappointment. {p}I'm older than him, {p}but I didn't show him any mercy."
    
    hide su with dis

    "I raised my head and look forward. {p}Illuminated by my flashlight, {p}that creepy mannequin stands there, expressionless."
    
    play music ambience01
    scene mannequin with dis

    fn "「Th-there's nothing to be afraid of. {p}\ \ Nothing at all! 」"
    "I try saying it out loud, but it's still creepy. {p}Even so, I slowly step into the science room, {p}closer to the mysterious mannequin."
    fn "「...Huh? 」"
    "Then, I noticed something."
    fn "「That mannequin... is new? 」"
    "My flashlight reflects off its fake skin. {p}I know nothing about this mannequin."
    "The one from before was more dull, {p}it had stains here and there, {p}and would immediately fall apart if you touched it."
    "It was just too scary."
    "But this..."
    
    stop music fadeout .5

    fn "「Oh, I see... 」"
    
    scene black with dis
    pause .3
    scene school hallway 2 night with dis

    "When you think about it calmly, it's simple. {p}The old one was thrown away and, {p}the school bought a new mannequin."
    "It's simply nothing more than that."
    fn "「What... 」"
    "I understand now, {p}and I lose the strength in my shoulders. {p}That really did surprise me."

    show su 003 night at center with dis
    
    su "「[fn]-san, are you okay? 」"
    "Shun-kun peeks his head into the classroom, {p}and cautiously calls out to me."
    fn "「Oh, I'm alright, I'm alright. {p}\ \ This looks like a new mannequin. 」"
    "Unaware of it, {p}my reply is dilligently cheerful."
    fn "「If you think about it normally, {p}\ \ there's nothing surprising about it! 」"
    "Hahaha, I look over and laugh, {p}Shun-kun also seems to be relieved somehow."

    show su 001 night with dis
    
    su "「Th-that's right! 」"

    show su 004 night with dis
    
    su "「Ah, but... it's still creepy. 」"
    fn "「You've got a point. 」"
    "I had carelessly forgotten my fear. {p}Even though it's new, it's still a mannequin."
    
    scene mannequin with wipe_right
    show white with qdis
    play sound se_033
    pause .1
    hide white
    
    scene school hallway 2 night
    show su 004 night at center
    with qdis
    
    "I face towards it and take a picture, {p}then we quickly leave the science room."
    
    scene black with dis
    scene school hallway 1 night with dis
    show su 001 night at center with dis
    
    fn "「Mission complete. 」"
    "Now we just need to meet Kounosuke, {p}at the back entrance."
    su "「Haah, my heart was pounding! 」"
    fn "「That reminds me, {p}\ \ there was something I was wondering. {p}\ \ Why did you come here? 」"

    show su 004 night with dis
    
    su "「Eh? 」"
    "Ah, I wonder if he heard something... {p}he didn't want to hear."
    fn "「Well you see, {p}\ \ you have a curfew at your house. {p}\ \ I know Torahiko could come..."
    fn "but you're younger than us, {p}so it seems a little strange. 」"
    "Shun gives a small, \"yeah\" and nods."

    show su 002 night with dis
    
    su "「Kounosuke-san asked me at lunch. {p}\ \ \"I need your help\", he said. 」"
    "Oh... {p}I see, I see. {p}Kounosuke begged Shun-kun to come."
    fn "「By the way, {p}\ \ did he just ask you normally? 」"

    show su 004 night with dis
    
    su "「Huh? 」"
    fn "「Did he, you know, {p}\ \ beg? Was he bowing and stuff? 」"

    show su 001 night with dis
    
    su "「Oh, yeah, he did. 」"
    "I knew it."
    fn "「Kounosuke is really... 」"
    su "「B-but aren't there some... {p}\ \ good things about Kounosuke-san? 」"
    fn "「Like what? 」"
    su "「Err... 」"
    fn "「...... 」"

    show su 004 night with dis
    
    su "「...... 」"
    "You're stuck in a fatal rut there, Shun-kun..."
    
    play music musi2    
    scene black with dis
    
    scene school entryway night 
    show ko 001 night at midleft
    show to 001 night at midright
    with dis

    ko "「Ah, you finally got here! 」"
    to "「You're late, [fn]. 」"
    "We get to the front door, {p}but it seems we were too slow. {p}Those two were already waiting."
    ko "「I know, right? {p}\ \ If you didn't get here soon, {p}\ \ Torahiko was going to... 」"

    show to 003 night with dis
    
    to "「Kounosuke! 」"

    show ko 005 night with dis
    
    ko "「Oh, nothing, nothing. 」"
    "Eh? What?"

    show to 001 night with dis
    
    to "「Anyways, lets finish up and hurry home. {p}\ \ It's gotten pretty late... 」"

    show ko 001 night with dis
    
    ko "「You just want to get out of here. 」"

    show to 003 night with dis
    
    to "「Koouunoosuukee... 」"
    
    show ko at move_farleft(0.4)

    ko "「You're too soft. {p}\ \ [fn] Barrier, go! 」"
    "Wait, hey!"
    fn "「Wha-uwaa!! 」"
    "Kounosuke pulls me over, {p}and now that I'm in his grip, {p}he uses me as a shield."

    show su 004 night at farright with dis
    
    su "「P-please stop! 」"

    show ko 002 night with dis
    
    ko "「It's alright, it's alright. {p}\ \ We're just playing around. 」"

    show to 002 night at move_center(0.4)
    
    to "「An opening! 」"
    
    show school entryway night at hshake
    show ko at hshake
    show to at hshake
    show su at hshake
    show ko 006 night with dis
    
    "Uwawawa!"
    "Kounosuke's negligence creates a gap, {p}and Torahiko tears me off."

    show to 001 night with dis
    
    to "「Are you okay, [fn]? 」"
    fn "「Ah, yeah... 」"
    "He pulled me off a little roughly, {p}but it was just a slight shock, nothing more."
    to "「Bwahahaha. {p}\ \ There's no way out now...! 」"

    show ko 001 night with dis
    
    ko "「Heh. I wonder about that. 」"

    show to 003 night with dis
    
    to "「What!? 」"
    ko "「There's still another barrier! {p}\ \ I've got a Shun-kun Barrier! 」"
    
    hide ko
    hide to
    show su 003 night at center
    with qdis

    su "「Huh? Eeh!?\n\ \ Uwawawa!! 」"
    
    show to 003 night behind su at farright with dis
    show ko 004 night behind su at farleft with dis

    "Now that Shun-kun is a shield, {p}a stand-off between Kounosuke and Torahiko begins."
    fn "「Wait, let's just go back already! {p}\ \ Both of you! 」"
    "If I left them alone, {p}this would probably never end."
    "So I step in and end it. {p}Then we finally make our way back."
    
    scene black with dis
    play music free51
    pause .3
    
    scene path night
    show ko 002 night at center
    show su 004 night at farright
    show to 003 night at farleft
    with wipe_right

    "On our way home, {p}Kounosuke teases Torahiko, {p}and I sometimes get caught in the middle."
    "Shun-kun would watch anxiously and get caught up too."
    "Which reminded me, before I transferred, {p}the mood was always like this. {p}I've missed this."
    
    jump day06_testend

########################################
label day06_testend:

    $ event_name = "Heading home"

    show ko 001 night with dis
        
    ko "「Well then, this is it. 」"

    show to 001 night with dis
    
    to "「Oh, yeah. 」"
    ko "「Alright, see you tomorrow. {p}\ \ Ah, I can't wait to develop the film! 」"

    show to 006 night with dis
    
    to "「Go and die! Jeez. {p}\ \ Well, [fn] and Shun. {p}\ \ See you tomorrow! 」"

    show su 002 night with dis
    
    su "「I had a good time today. {p}\ \ See you tomorrow! 」"
    
    scene path night with dis

    fn "「Yeah. See you guys tomorrow. 」"
    "Now then. {p}I need to get back home."
    "That was a crazy, {p}but fun night, I guess?"
    "Ghost photography... {p}Well, I'm not expecting much."
    
label end06:
    
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
    
    jump day07


