###Day 20
screen ricefield20:
    hbox:
        add "arrow down"
        at ricebounce1
    hbox:
        add "icon_kouya"
        at ricebounce2
    hbox:
        text "Rice Fields"
        xalign .245 yalign .66
        
screen house20:
    hbox:
        add "arrow down"
        at housebounce1
    hbox:
        add "icon_shun"
        at housebounce2
    hbox:
        text "[fn]'s House"
        xalign .58 yalign .42
        
screen minasatomap20():
    add "map"
    add "mapdate"
    if favorite == "kouya":
        imagebutton idle "a icon" hover "icon loop"  xpos 197 ypos 325  action Jump("kouya20") hovered Show("ricefield20")  unhovered Hide("ricefield20") hover_sound "av/audio/click_008.wav"   
    elif favorite == "shun":
        imagebutton idle "a icon" hover "icon loop"  xpos 418 ypos 185  action Jump("shun20") hovered Show("house20")  unhovered Hide("house20") hover_sound "av/audio/click_008.wav" 
    hbox:
        text "{size=+30}August 20"
        at maptime

######################################################
label day20:
    
    $ renpy.music.set_volume(1.0, 0.0, channel = "music")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound2")
    
    $ day = 20
    $ the_date = "August 20"
    $ event_name = "８月20日"    
    
    if favorite == "tatsuki" or favorite == "shun" or favorite == "kouya" or favorite == "shin":
        window hide
        play music birds_chirping
        
        scene sky01 
        show text "{size=+130}August 20" at truecenter
        with Dissolve(.5)
    
        pause 3
        scene black with Dissolve(1)
        pause .4
    else:
        jump day21
        
    if favorite == "kouya" or favorite == "shun":
        jump map20
    else:        
        $ renpy.jump (favorite + "20")
    
#######################################################
label map20:
    scene hbroom with wipe_corner
    pause .2
    fn "「What should I do today? 」"

    play music "<from 2.5>av/audio/free0422.ogg"
    call screen minasatomap20    
    
#######################################################
label tatsuki20:
    
    scene white with sdis
    "Uuurgh...{p}I'm so stiff."

    scene tatsuki_bedroom with wipe_corner
    
    "The window let in a little bit of morning light.\nIt was dim, but getting lighter."
    "On the wall, the familiar work uniform was hanging,\nand on top of the desk was a wood plane."
    "Looking closer shows a bunch of wood chips nearby,\nwith scraps scattered all over the place.{p}The owner must spend a lot of time around there."
    fn "「This is... 」"
    "I opened my eyes to find Tatsu-nii's arm holding me."
    "Oh, right. I was wondering where I was.\nI forgot that I'm staying overnight\nat the Midoriya Group's place for work."
    "The clock was pointing to around 4:50."
    "I don't normally wake up this early,\nbut this is different.\nIt's like an alarm clock in my head."
    "At the Midoriya group, breakfast starts at 5 a.m.{p}When we're done, we get straight to work.{w} Around now,\nYukino-san is probably making a meal for us."
    ta "「ZZZ 」"
    "Behind me, Tatsu-nii held me tightly,\nand continued sleeping."
    "Even though we're sharing a futon,\nwe should be sleeping separately."
    "However, when it's time to wake up,\nTatsu-nii's clinging to me like this is nothing new."
    fn "「Hup... There! 」"

    play sound changing
    
    "I rolled over onto my other side.{p}Tatsu-nii's face was close to mine."
    "I peeked at a crocodile-like fang,\npoking out from his closed mouth.\nHis breathing was soft as he continued sleeping."
    "Since there's such a size difference between us,\nhe looks far away when we're standing."
    "That's why watching his sleeping face so close to\nmine is something I look forward to."
    
    play sound timer
    pause 1
    play sound timer
    pause 1
    play sound timer
    pause 1
    show ta 108 big at center_big with dis
    
    ta "「Nnn...{w} Oh,{w=.2} morning, [fn]... 」"
    fn "「Morning, Tatsu-nii. 」"
    
    show ta 102 big at center_big with dis
    
    ta "「What is iiit. What're you looking at me fooor?{p}\ \ Stop staring! 」"
    "He laughed as he messed my hair."

    show ta 101 big with dis
    
    ta "「Well, it looks like today's gonna be a great day.{p}\ \ Let's get ready to work.{p}\ \ But first, let's go down and eat Ma's breakfast. 」"

    hide ta
    show ta 102 at center 
    with dis
    pause .8
    hide ta with wipeleft
    
    "Tatsu-nii got up from the futon,\nwearing nothing on his lower half.{p}He's going downstairs in that state..."
    fn "「Eh, Tatsu-nii, you went to bed naked!? 」"
    "Come to think of it,\nI remember feeling his smooth body pressing\nagainst me during the night..."

    scene tatsukihouse_inside with qdis
    play music free44
    
    ta "{size=+25}「Morniiing! 」"

    show tp 403 at center with dis
    play sound bosu35
    show tatsukihouse_inside at hshake
    
    tp "「Morning, my ass.{p}\ \ Go put some damn clothes on, dumbass!!!{p}\ \ Don't go flashing everyone!!! 」"

    show cu 006 at farright with dis
    
    cu "「Young Master!?{w} 　I can see yer inner tool!! 」"
    
    play sound bosu35
    show tatsukihouse_inside at hshake
    
    tp "「Don't go showing off something\n\ \ so dirty in the morning!!\n\ \ {size=+15}LITTLE SHIIIT!!! 」"

    $ event_name = "Half Holiday"

    stop music fadeout 1.5
    scene black with sdis
    play music cicada01 fadein 1.5
    $ renpy.music.set_volume(0.5, 0.0, channel = "music")
    scene workplace1 with rotation
    show tp 401 at center with dis
    
    tp "「Ok, that's enough for today. 」"

    show ni 001 at farright with wipeleft
    
    ni "「We're already done? 」"
    
    show tp 402 with dis
    
    tp "「Yeah, I'm going to go visit Tetsu.{p}\ \ You guys clean up. 」"
    "Oh, I see. Tappei-san's closing early today,{p}so he can make a get-well visit to Tetsuya-san."

    show ta 001 at farleft behind tp with wipeleft
    
    ta "「What's that, Pa?{p}\ \ You planning on going by yourself? 」"
    
    show tp 401 with dis
    
    tp "「This isn't for fun.{p}\ \ You guys just stay here and watch the place. 」"
    
    show ta 009 with dis
    
    ta "「Why you... this is really an excuse to go drinking,\n\ \ isn't it? I'm not letting you go to Raimon! 」"
    
    show tp 403 with dis
    
    tp "「Huh?{w} 　I said I'm visiting Tetsu.{p}\ \ You've got some nerve to be giving me lip like that. 」"

    hide ni with wipeleft
    show cu 001 at farright with dis
    
    cu "「(Giving lip...) 」"

    show ta at jump_up
    pause .2
    
    ta "「Damn you, old geezer!!{w} 　I'm not giving you lip!{p}\ \ I have to ask what you're up to,\n\ \ since Ma told me to be in charge of the money. 」"
    ta "「If you wanna do anything,\n\ \ you'd better go tell Ma first. 」"
    tp "「Ah, not again...{p}\ \ Stop screwing with me.{p}\ \ You her personal agent or something? 」"
    
    show cu 013 big at midright_big with dis 
    
    cu "「(...giving head.) 」"
    
    show ta 010 with dis
    
    ta "「'Hang on to the purse whenever I'm out.{p}\ \ Things will be under control, then.'{p}\ \ Her exact words. 」"

    show tp at jump_up
    pause .2
    
    tp "「Are you her, now?{p}\ \ You sound just like her. 」"
    
    show ta 009 with dis
    
    ta "「Anyway, I'm the one with the money.{p}\ \ Go wherever you want, for all I care. 」"
    
    show cu 002 big at close_right with dis
    
    cu "「(Isn't that awesome!?{p}\ \ Haha,{w=.2} giving head with yer lips... that's-) 」"
    tp "「Stop that smiling!! 」"
    
    show tp at hit_right
    play sound hit_p00
    pause .1
    scene workplace1
    show ta 009 at farleft
    show tp 403 at center
    show cu 009 big at midright_big
    with qdis
    show workplace1 at vshake
    
    cu "{size=+15}「Lip service! 」{w=.5}{nw}"
    hide cu with wipe_down
    $ chuu_beat += 1
    play sound bosu31
    show workplace1 at vshake
    extend ""
    
    show tp 401 with dis
    
    tp "「I already said I'm off to visit Tetsu.{p}\ \ Have a little faith in me,\n\ \ aren't you hearing what I'm saying? 」"
    
    show ta 008 with dis
    
    ta "「I do when we're working, but not anywhere else. 」"

    show tp at jump_up
    
    tp "「Wha-!{w} 　You disobeying your father? 」"
    "The two of them are getting mad...{p}Tappei-san looks like he'd be happy to hit something."

    show ni 001 at farright with wipe_right
    
    ni "「Boss, please calm down. 」"
    tp "「Huh?{w} 　Shut your mouth!! 」"
    ni "「If you're going to visit Tetsu-san,\n\ \ then how about you take us with you?{p}\ \ He's someone we all care about. 」"
    
    show ta 001 with dis
    
    ta "「If you take us with you, then everything's okay. 」"
    tp "「Where I go is my business.{p}\ \ Where do you all get off, jumping in on that!? 」"
    
    show ta 008 with dis
    
    ta "「Ma told me to watch over things.{p}\ \ Unless there's a reason you don't want us to come? 」"
    
    show tp 401 with dis
    
    tp "「Guh, that's... 」"
    "Usually, he's a lot more imposing than this.{p}I guess there's a softer side to him."
    fn "「I also want to go visit Tetsuya-san.{p}\ \ Won't you please let us come, too? 」"
    ni "「Please, Boss? 」"
    "Tappei-san thought about it for a while,{p}then opened his mouth in resignation."
    tp "「...Fine. It's okay if I take you, all right? 」"
    fn "「Yes, thank you very much! 」"
    
    show ni 003 with dis
    
    ni "「Thank you very much. 」"

    hide ni with wipe_right
    show cu 002 with wipe_right
    
    cu "「Yay, a visit! 」"
    
    show tp 403 with dis
    
    tp "「Keh,{w=.2} hurry and clean up, then get ready to go.{p}\ \ And don't forget to lock the doors. 」"

    hide tp with wipeleft
    show cu 008 with dis
    
    cu "「I wonder if Tetsu-san's okay... 」"
    fn "「A get-well visit, huh? How's Tetsuya-san doing?{p}\ \ He has a wife and son around, after all. 」"

    show ni 003 with dis
    
    ni "「What? We'll see when we go.{p}\ \ Besides, we're going so he gets better soon. 」"
    
    show cu 002 with dis
    
    cu "「It'd be great if we could make Tetsu-san happy. 」"
    
    show ta 002 with dis
    
    ta "「All right, now that's settled,\n\ \ let's hurry up and clean up here. 」"
    
    $ event_name = "What is this, the Kaminarimon?" #Kaminarimon = Thunder Gate
    #Looked this up.  It's a gate in Tokyo that's popular amongst tourists.  There is a large lantern in the gate with a wood carving of a dragon on the underside of the lantern.
    #This is just my interpretation, but perhaps you receive a blessing from the dragon when you pass under it.
    #Would make sense since in this scene the main character is given a large sum of money by Tatsuki, a dragon.

    scene black with wipeleft
    play music shop01
    $ renpy.music.set_volume(0.7, 0.0, channel = "music")
    scene raimon1 with sdis
    
    "And so we ended up going to Raimon."

    show tp 401 at center with dis
    
    tp "「Hey, it's me. Get me that thing. 」"
    om "「Oh, the regular?{p}\ \ Are you hoarding them or something...?{p}\ \ Did you only come by to buy it? 」"
    
    show tp 402 with dis
    
    tp "「Gahahahaha!{p}\ \ Nah, I came to get it for someone else today. 」"
    om "「That's unusual for you. 」"
    
    show tp 401 with dis
    
    tp "「Do you have it?{w} 　Today is special,\n\ \ so you have something good, don't you? 」"
    om "「That?{w} Dragon's Blessing?{p}\ \ I'm sorry, we're all out right now. 」"
    om "「I didn't think you'd come buy any,\n\ \ so I didn't order any more. 」"
    tp "「What, don't you have anything else? 」"
    om "「I'm sorry, I can't do anything about it today.{p}\ \ I'll order some now, so come back tomorrow,\n\ \ or the day after. 」"
    tp "「Damnit, there goes that plan. 」"

    show ta 001 at farright behind tp with wipeleft
    
    ta "「Yep, there it goes.{p}\ \ {nw}"
    show ta 009 at jump_up
    extend "Wait, we really did come to Raimon! 」"
    
    show tp 403 with dis
    
    tp "「Problem?{p}\ \ We came here to buy something for the visit. 」"
    ta "「So why are we getting sake for this?{p}\ \ There must be something else we could get. 」"
    
    show tp 402 with dis
    
    tp "「Anyone would be happy to get sake.{p}\ \ There's no way he won't be happy with this. 」"
    
    show ta 008 with dis
    
    ta "「I'm not giving you any money to pay for that. 」"
    
    show tp 403 with dis
    
    tp "「That's MY money you're talking about!{p}\ \ Don't give me that attitude,\n\ \ just because Ma asked you to!! 」"
    
    show ta 010 with dis
    
    ta "「Well, let's do this, then.{p}\ \ We'll put [fn] in charge of the money...{p}\ \ [fn], you decide what we're going to get. 」"
    fn "「Eh, me? 」"
    tp "「Huh?{w} 　I just said that's my money there!! 」"
    
    show ta 001 with dis
    
    ta "「There must be something good somewhere.{p}\ \ I'll leave it to you, [fn].\n\ \ That way Pa won't waste it on something dumb. 」"
    
    show tp 402 with dis
    
    tp "「Hey... [fn].{w} You understand, don't you?{p}\ \ Whose money that is...{w} C'mon, it's not that hard,\n\ \ you're not doing anything wrong. 」"
    "Hmm, there's stuff besides sake, but...\nI'm getting a bad feeling about this.{p}Tappei-san's being scary... what should I do?"
    
    scene black with wipeleft

    $ event_name = "Medication"

    scene tetsuya_house_out with sdis
    show te 001 at center with dis

    te "「Please, come in. 」"
    fn "「Sorry for disturbing you. 」"
    "We finished the shopping,\nthen proceeded to Tetsuya-san's apartment,\nwhere we were taken to his welcoming room."

    scene tetsuya_house_in with wipe_right
    show te 003 at center with dis
    
    te "「My apologies, my wife and son both wanted to greet\n\ \ you all, but they have gone out. 」"

    show tp 401 at farright behind te with wipeleft
    
    tp "「Don't worry about it. 」"
    te "「Sorry for putting you through so much trouble. 」"
    "As expected, Tappei-san could\nbe kind in times like this."

    scene tetsuya_house_in with wipe_right
    show cu 005 at farleft with wipeleft
    
    cu "「Is this picture of your wife? She's pretty.{p}\ \ An' your son looks jus' like you. 」"

    show te 001 at center with dis
    
    te "「My wife does so much for me.{p}\ \ I really am grateful to have her,\n\ \ the lengths she goes to for a novice like myself. 」"

    show ta 008 at farright behind te with wipe_right
    
    ta "「Tetsu-san, you're too cool. 」"
    "He's the exact opposite of Tappei-san,\nbut this is part of manliness too, huh..."
    fn "「How's your injury? 」"
    te "「It is healing, thanks to the time I have had off.{p}\ \ However, while it is great to spend time with my family,\n\ \ I have only been able to think about work. 」"

    hide ta with wipe_right
    show tp 401 at farright behind te with wipe_right
    
    tp "「Guys that can work efficiently are really valuable.{p}\ \ It's easy to forget that. 」"
    te "「Yes, I will return as soon as I am able.{p}\ \ Thank you, Chief.{p}\ \ I have caused so much trouble for you all. 」"
    "Tetsuya-san is so humble and polite.{p}I want to be a respectable adult like that, too."
    
    show tp 402 with dis
    
    tp "「Heh, don't give me that.{p}\ \ Don't you get what I'm saying? 」"
    
    scene tetsuya_house_in with wipeleft
    show ni 001 at center with wipeleft
    
    ni "「You've never made any mistakes, Tetsu-san.{p}\ \ Please, just rest and recover.\n\ \ We'll manage without you, somehow. 」"

    show ta 001 at farright behind ni with wipe_right
    
    ta "「Yeah, take a break.{p}\ \ You don't need to worry about work, with me here. 」"
    
    show ni 002 with dis
    
    ni "「I can't help but feel uneasy in the workplace,\n\ \ with a guy who likes exposing his crotch so often. 」"
    
    show ta 003 with dis
    
    ta "「Wha-{w=.2} you didn't need to bring that up! 」"

    show cu 002 at farleft with wipe_right
    
    cu "「Shishishishi, ya sure were energetic this morning. 」"
    fn "「Say, I thought I felt something poking me earlier,\n\ \ but was it really...? 」"
    
    show cu 011 at hit_left
    
    cu "「You were poked by something...?{p}\ \ Did something happen!? 」"
    
    show ta 008 with dis
    
    ta "「I don't know. I was asleep. 」"
    "I guess Tatsu-nii's embarrassed by that, too."
    
    show ta 001 with dis
    
    ta "「That's right, we got you a get-well-soon present.{p}\ \ C'mon, get it out. You did buy it, right? 」"
    fn "「Yeah, I did. 」"
    
    show cu 001 with dis
    
    cu "「What'cha get? 」"
    fn "「Well... 」"
    
    menu:
        "A. I bought sake.":
            jump tatsuki20_alcohol
        "B. I bought 'sake'.":
            jump tatsuki20_fish
        "C. I bought sweets.":
            jump tatsuki20_sweets

    #######################################################
    label tatsuki20_alcohol:
        
        $ event_name = "Here's something to drink"
        
        fn "「Here, I got some sake. 」"
        
        show cu 006 at hit_left
        pause .2
        
        cu "「Eh?! Y-you bought sake? 」"
        "That's because Tappei-san was scary..."
    
        scene tetsuya_house_in with wipe_right
        show tp 402 at center with wipe_right
        
        tp "「Hey, [fn], you made a good choice.\n\ \ This is pretty good sake.{p}\ \ C'mon, let's drink! 」"
        
        jump tatsuki20_drunk
        
    #######################################################
    label tatsuki20_fish:

        $ event_name = "Salted Salmon"
        
        fn "「Here, I got some 'Sake'. 」"
        "Right. If sake is no good,\n'Sake' brand salmon should be fine."
        
        play music oo39_cho_ys001
        show cu 004
        show ta 008
        with dis
    
        "「... 」"
        
        scene tetsuya_house_in with wipe_right
        show te 001 at midright with wipe_right
        
        te "「'Sake'? Oh, you mean the brand.{p}\ \ Mmm, this is good salmon. 」"
        
        show tp 402 at midleft behind te with wipeleft
        
        tp "「Oh, bringing a drinking snack was a good choice.{p}\ \ Now, where's the sake? 」"
        te "「If you want, we have a little here.\n\ \ If you will excuse me a moment. 」"

        jump tatsuki20_drunk
        
    #######################################################
    label tatsuki20_sweets:
    
        $ event_name = "A Gift of Summer"
        
        "In times like this,\nthe best thing to get is a box of sweets."
        fn "「This is the season for mizuyoukan, after all. 」"
    
        scene tetsuya_house_in with wipe_right
        show tp 402 at center with dis
        
        tp "「What, it's not sake?{p}\ \ And here I thought we'd have a little party. 」"
        "A 'little party' with you...\nThat'd definitely end in a riot."
        
        hide tp with wipe_right
        show ta 008 at midright
        show te 001 at midleft
        with wipe_right
        
        ta "「He was looking for an excuse to drink after all... 」"
        te "「Thank you very much.{w} My wife and son love sweets,\n\ \ they will be delighted to receive these. 」"
        fn "「Don't you also have a sweet tooth, Tetsuya-san?{p}\ \ I got these thinking that you did. 」"
        
        stop music fadeout 1
        show te 004 with dis
        
        te "「Ah,{w=.2} no, I... 」"
        
        play music free02
        show ta 002 with dis
        
        ta "「Oh yeah, when you take a break at work,\n\ \ you get some tea and candy to munch on, huh? 」"
    
        show cu 002 at farleft with wipeleft
        
        cu "「'Round about now,\n\ \ you'd eat three or four pieces o' ohagi,\n\ \ stickin' your tongue out the whole time. 」"
        fn "「Yeah, and then you'd make this super happy face. 」"
        te "「I understand, please don't tease me so much. 」"
        ta "「So that means? 」"
    
        show te 001 with dis
        
        te "「Yes, I am extremely fond of sweets.{p}\ \ In particular anko, kinako, kuromitsu and mochi. 」"
        
        show cu 005 with dis
        
        cu "「So if we put anko inside some mochi,\n\ \ then covered it in kinako and kuromitsu,\n\ \ what would happen? 」"
        
        show te 004 with dis
        
        te "「I-if such a thing were to happen,\n\ \ I would not be able to contain myself. 」"
        te "「However, I would like the anko to be on the plate\n\ \ alongside the mochi, instead of inside it. 」"
        
        show ni 003 at farright with wipeleft
        
        ni "「I like sweets, too. 」"
        ni "「While I'm reading a book at a cafe,\n\ \ I get a cake, or a parfait, and a sweet drink.\n\ \ A perfect way to spend a day off. 」"
        
        show ta 010 with dis
        
        ta "「'I get a cake, or a parfait, and a sweet drink.\n\ \ A perfect way to spend a day off.' 」"
        
        show ta 009 at jump_up
        pause .2
        
        ta "「Man, that makes sweets sound gross.{p}\ \ I like sweet things too,\n\ \ but what's with that air you're putting on? 」"
        
        show ni 002 with dis
        
        ni "「Quiet, flasher. 」"
        
        show ta 005 with dis
        
        ta "「... 」"
        
        show te 004 with dis
        
        te "「Western confections are good, too.{w} A fluffy sponge,\n\ \ good melt-in-your-mouth cream and fresh fruit,\n\ \ that is the superb choux a la creme. 」"
        te "「Tarts and pies are good, too... 」"
        
        show cu 002 with dis
        
        cu "「Amazin'!\n\ \ I've never seen Tetsu-san talk this much. 」"
        "I thought he had a sweet tooth on some level,\nbut wow. This is intense."
        
        show te 003 with dis
        
        te "「Excuse me...{p}\ \ I have said too much. It would appear that\n\ \ I cannot restrain myself on the matter of sweets. 」"
        
        show ta 002 with dis
        
        ta "「Even though you're a fox,\n\ \ you must've gotten that tanuki potbelly\n\ \ because of all the anko. 」"
        "Oh, I see,\nhat stomach is probably is filled with sweets."
        
        show te 004 with dis
        
        te "「That was why I didn't want you all to know\n\ \ that I have a sweet tooth. 」"
        fn "「So you were happy,\n\ \ when we brought you the mizuyoukan. 」"
        
        show te 001 with dis
        
        te "「Er, well...{w} Yes, thank you very much. 」"
        
        show cu 001 with dis
        
        cu "「That looks good. 」"
        te "「It looks like there is a lot packed in,\n\ \ so won't you all have some, too? 」"
        
        show cu 007 with dis
        
        cu "「Eh?{w} 　Oh no, that'd be bad.\n\ \ I wasn't thinkin' about that when I was talkin',\n\ \ please don't mind me. 」"
        
        show te 001 with dis
        
        te "「No, this may be too much for three people,\n\ \ and I have not shown you much hospitality. 」"
        
        show ta 001 with dis
        
        ta "「You say that,\n\ \ but you want to hurry and eat them,\n\ \ don't you, Tetsu-san? 」"
        
        show te 003 with dis
        
        te "「Eeh... You saw through me, there. 」"
        
        show ta 007 with dis
        
        ta "「Tetsu-san, you're drooling. 」"
        
        show te 004 with dis
        
        te "「Th-that can't be. 」"
        
        show ta 002 with dis
        
        ta "「I'm kidding. I want some, too, so let's all eat. 」"
        
        scene tetsuya_house_in with wipe_right
        show tp 403 at center with wipeleft
        
        tp "「You're 100 years too early to be making fun of Tetsu.{p}\ \ Besides, how're you gonna eat our gift by yourself? 」"
    
        show te 003 at farright with wipeleft
        
        te "「That's true. I am sorry, Chief. 」"
        
        show tp 406 with dis
        
        tp "「Well, you have to be honest when receiving gifts.{p}\ \ Hand me some bean paste. 」"
        
        show te 004 with dis
        
        te "「Of course, here. 」"
        
        scene tetsuya_house_in with wipe_right
        show cu 012 at center with wipe_right
        
        cu "「This is great, powdered green tea sucks.{p}\ \ Ahh, summer vacation, mizuyoukan...{p}\ \ This is great. 」"
        fn "「Yep, it sure is-{w=.2}wait, Chuukichi-kun? 」"
    
        show tp 403 behind cu with explosion
        
        tp "「Why the hell you eating before me...\n\ \ I'll kill ya!!! 」"
        
        play sound hit_p00
        show cu 009 with qdis
        show tetsuya_house_in at hshake
        $ chuu_beat += 1
        pause 1.5
        
        jump tatsuki20_hotsprings
    
    #####################################################
    label tatsuki20_drunk:
        
        $ event_name = "Drunken Dragon"
        
        stop music fadeout 1.5
        scene black with sdis
        scene tetsuya_house_out with circle_out
        play music free0421 fadein 2
        show tp 305 at center with dis
        
        tp "「Aw, c'mon, it's okay. Lemme do ya. 」"
        
        show te 005 at farright with wipeleft
        
        te "「Please, stop-!! 」"
        "So Tetsuya-san's apartment was modest, after all?{p}This get-well visit turned into a drinking party.\nNaturally, Tappei-san was causing trouble..."
        
        show tp at move_midright(1)
        
        tp "「Hey, it's all right... You hear what I'm saying?{p}\ \ I won't do anything bad...{p}\ \ It's okay, yeah? 」"
    
        show te 003 at jump_up
        pause .2
        
        te "「You can't-!! 」"
        tp "「What's so wrong about this? 」"
        "As Tappei-san said that, he leaned on Tetsuya-san,\ngroping his crotch."
        te "「Chief, no! I have a wife! 」"
        tp "「You're so loud...\n\ \ Does that mean it'd be okay if you were single? 」"
        "Whoa, this has gone somewhere terrible.{p}I feel like I've seen something I shouldn't have...{w} {nw}"        
        show tp at move_center(1)
        extend "{w=.8}{nw}"
        show cu 004 at midright with dis
        
        cu "「Y-you can't do that sorta thing.{p}\ \ That's bad, Master! 」"
    
        show tp 303 with dis
        
        tp "「SHADDUP!!!{p}\ \ You saying you want to take his place!?{p}\ \ Huh!? 」"
        
        show cu 007 with dis
        
        cu "「He- I couldn't...{p}\ \ I-I'd break... 」"
        "Oh man, what should I do...{p}Something needs to be done."
        
        scene tetsuya_house_in with wipeleft
        show ta 308 at center with circle_out
    
        ta "「[fn]... You are just so cute... 」"
        "Tatsu-nii's drunk, too!?"
        
        show ta 302 with dis
        
        ta "「Hey, I wonder if he's gonna take his clothes off. 」"
        "He's always taking off clothes...\nHe spends a lot of time half-naked, anyway."
        
        show ta 410 with dis
        
        ta "「It'd be great if you got bolder, [fn]... 」"
        "You're the bold one..."
        
        show ni 005 at farright with wipeleft
        
        ni "「Go fix the problem you're responsible for. 」"
        
        show ta 408 big at center_big with explosion
        
        ta "「Mmm, c'mere... 」"
        fn "「Stop it, Tatsu-nii...! 」"
    
    ###################################################
    label tatsuki20_hotsprings:
        
        $ event_name = "Midoriya Group at the Hot Springs"
        
        stop music fadeout 1.5
        scene black with wipeleft
        play music higurasi 
        $ renpy.music.set_volume(0.5, 0.0, channel = "music")
        scene path red with sdis
        show cu 002 red at center with dis
        
        cu "「It's great Tetsu-san's okay. 」"
        fn "「Yeah, I hope he recovers quickly. 」"
        "Something or other just happened...\nAnyway, I'm glad to see Tetsuya-san's doing well."
    
        show tp 401 red at farright behind cu with wipeleft
        
        tp "「Hey, enough with the chatter.{p}\ \ We're going back. 」"
        fn "「Okay! 」"
    
        show cu at jump_up
        
        cu "「'Kay! 」"
    
        show ta 002 red at farleft with wipeleft
        
        ta "「Torahiko's place is close, wanna go use his bath?{p}\ \ I've got the wallet, if we need money. 」"
        "As he said that,\nTatsu-nii waved Tappei-san's wallet around."    
        cu "「Sweet!! 」"
        
        show tp 402 red with dis
        
        tp "「'Sweet!!'{p}\ \ {nw}"
        show tp 403 red with dis
        extend "My ass, little punk!!! 」"
        
        show tp at hit_left
        play sound hit_p00
        show cu 009 red 
        show path red at hshake
        $ chuu_beat += 1
        
        cu "{size=+15}「Gyaaah-!! 」"
        
        scene path red with wipe_right
        show ni 002 red at center with wipe_right
        
        ni "「Did none of you hear what the boss just said?{p}\ \ He said we're going straight home. 」"
    
        show ta 008 red at farleft with wipeleft
        
        ta "「Then you go back.{p}\ \ You just want the bath all to yourself, don't you? 」"
        
        show ni 003 red with dis
        
        ni "「No. If everyone goes, I'll come along.{p}\ \ We're still together as a group at the moment,\n\ \ so wouldn't it be a problem if I went back alone? 」"
        "He totally wants to go."
        
        show ta 009 red with dis
        
        ta "「Go home, wishy-washy bean sprout horse. 」"
        
        show ni 004 red with dis
        
        ni "「Don't tell me that, Half-Naked Carpenter.{p}\ \ {nw}"
        show ni 002 red with dis
        extend "Oh wait, you're still an apprentice...{p}\ \ Take care bathing, Mr. Indecent Flasher Apprentice. 」"
        
        show ta 003 red with dis
        
        ta "「Stop calling me that!!{p}\ \ All right, it'll be okay.\n\ \ Because I'll be taking it all off. 」"
        "Nikaidou-kun seems so stubborn...\nwas he bullied as a kid?{p}Well, as long as Tatsu-nii doesn't mind."
    
        show tp 403 red at farright behind ni with wipe_right
        
        tp "「So you say...\n\ \ No one is going to that bath after this!{p}\ \ Don't put words in my mouth whenever you want!! 」"
        
        show ta 008 red with dis
        
        ta "「So you're going back, right? 」"
        
        show tp 401 red with dis
        
        tp "「I'm going to the bath. 」"
        "..."
        
        scene ooshima_inn_out red with sdis
        play music daily01
        $ renpy.music.set_volume(0.7, 0.0, channel = "music")
        show tp 402 red at center with dis
        
        tp "「All right, I'm paying for this today. 」"
    
        show ta 004 red at farright with wipe_right
        
        ta "「Bastard, weren't you complaining the whole time? 」"
        
        show tp 403 red with dis
        
        tp "「Huh? Don't you start that with me!! 」"
        fn "「A-{w=.2}anyway, let's go in. 」"
        
        show tp 401 red with dis
        
        tp "「Yeah, let's go. 」"
        "Whew, Tatsu-nii is usually pretty gentle,\nbut around Tappei-san he gets pretty agitated.{p}I wonder what happened?"
        
        scene ooshima_inn_out red with wipe_right
        scene ooshima_inn_in with wipeleft
        show to 001 at center with dis
        
        to "「Welcome! 」"
        "Torahiko was standing at the inn counter.{p}The atmosphere there doesn't really suit him...\nIn fact, it's making me a little uncomfortable."
    
        show ta 002 at farright behind to with wipeleft
        
        ta "「Yo, Torahiko! 」"
    
        show to 002 with dis
        
        to "「Yo,{w=.2} Tatsu-nii! 」"
        "Torahiko and Tatsu-nii exchanged a high-five.{p}Man, these two got so close while I was gone.\nI'd probably be the same if I'd stayed here..."
    
        show to at jump_up
        pause .2
        
        to "「Yo,{w=.2} [fn]! 」"
        "Then again,\nit was always going to be like this."
        "I'm having a great time right now,\nand I'm going to enjoy it to the fullest,\nso I won't become some boring thing."
        fn "「Yo,{w=.2} Torahiko. 」"
        "As I greeted Torahiko, these thoughts blew away,\nAnd we had our own forceful high-five."
        
        show to 001 with dis
        
        to "「What, the Midoriya Group, here in full force?{p}\ \ Today can't be like normal. 」"
        
        show ta 001 with dis
        
        ta "「Dumbass, I'm not that greedy. 」"
        
        show to 010 with dis
        
        to "「Heheh, all right. 」"
        "If I remember right,\nTatsu-nii often gets in for free.{p}Nice..."
    
        show cu 001 at farleft behind to with wipeleft
        
        cu "「G'day! 」"
        
        show to 002 with dis
        
        to "「Yo, Chuukichi!{w} 　Energetic as usual? 」"
        
        show cu 002 with dis
        
        cu "「Yo, I'm good!{p}\ \ I can't win against you there, though, Aniki. 」"
        "Chuukichi must have a lot of anikis..."
        fn "「You guys know each other? 」"
        
        show to 001 with dis
        
        to "「Hmm, we've hung out a few times,\n\ \ and I remember him from when I've been to Tatsu-nii's.{p}\ \ It's a small village, anyway. 」"
        "True, if the whole Midoriya Group came out,\nhe'd remember them.{p}Plus, the two of them would probably get along well."
        
        show cu 001 with dis
        
        cu "「Aniki, let us relax today. 」"
        
        show to 002 with dis
        
        to "「Sure, go right ahead. 」"
        "Does that mean he gets along with everyone else?{p}He's pretty fit, and he'd probably meet up\nwith people who have that in common."
        
        scene ooshima_inn_in
        show ni 001 at midleft
        show to 001 at midright
        with wipe_right
        
        to "「G'day! 」"
        ni "「...Hello. 」"
        "Wow... that seemed cold."
        to "「Good weather today, eh? 」"
        "He's not discouraged.{w} Hang in there, Torahiko!"
        ni "「That's true. 」"
        "Nikaidou-kun's returned to his usual blank look.{p}Is this really a conversation?"
        
        show to 002 with dis
        
        to "「On a day like today,\n\ \ it feels good to just soak in the bath. 」"
        
        show ni 005 with dis
        
        ni "「The weather is irrelevant,\n\ \ since you should be bathing every day regardless. 」"
        
        show to 006 with dis
        
        to "「Eh? Aah...{w} \ \ Well, that's true... 」"
        "Hang in there, Torahiko.{p}You're not being ignored,\nso he shouldn't hate you..."
        
        show tp 403 at farright behind to with wipe_right
        
        tp "「Why are we standing here and talking?\n\ \ We're going in.{p}\ \ {nw}"
        show tp 401 with dis
        extend "Hey, Tora, we're gonna impose on you a little. 」"
        
        show to 002 with dis
        
        to "「Yes, thank you for coming.\n\ \ Please take your time. 」"
        
        scene black with sdis
        scene bathhouse_out with sdis
        pause 1.5
        scene bathhouse_enter with wipe_right
        pause 1
        play music hotsprings_ambience fadein 2.5
        $ renpy.music.set_volume(0.6, 0.0, channel = "music")
        scene bathhouse_in1
        show tp 101 at midright
        show ta 101 at farleft
        show cu 101 at farright
        show ni 101 at midleft
        with wipeleft
        
        "Here we are, the Midoriya Group at a hot spring.{p}Now that I think about it,\nthis is the first time I've been here with everyone."
        
        show cu 107 with dis
        
        cu "「Whew, hot springs are awesome. 」"
        
        play music daily04 fadein 2
        $ renpy.music.set_volume(0.6, 0.0, channel = "music")
        show ta 102 with dis
        
        ta "「Ah, there's so much space here.\n\ \ At home it's plain hot water, too. 」"
        "Staying over to do this part-time work is good fun,\nbut it's left me completely exhausted."
        "I really need to get rid of this fatigue."
        
        show ni 103 with dis
        
        ni "「Such a pleasant feeling...{p}\ \ They say this does wonders for your health,{p}\ \ as health and beauty are related. 」"
        fn "「It's good for the body, too. 」"
        ni "「It's supposed to make hair silky.{p}\ \ Hot springs truly are amazing. 」"
        fn "「Oh, cool.\n\ \ So beastmen feel the effects here, too. 」"
        
        show cu 112 with dis
        
        cu "「My tail's so smooth. 」"
        "I see, so the spring helps anyone.{p}Maybe it can help me."
        
        show tp 106 with dis
        
        tp "「It's all right if you guys wanna talk,\n\ \ but today's a holiday, so rest yourselves up.{p}\ \ Tetsu's still not back, so we gotta give our all. 」"
        fn "「Okay. 」"
        
        show tp 101 with dis
        
        tp "「Right, that's enough tough talk.{p}\ \ I'm in a good mood today, so let's go to Raimon.{p}\ \ No one's complaining if I take you all? 」"
        
        show cu 102 with dis
        
        cu "「F'real!?{w} 　I love the pork balls there!{p}\ \ Thank you so much, Master! 」"
        
        show tp 103 with dis
        
        tp "「I said call me Chief!! 」"
        
        play sound splash
        show cu 109 at fall
        hide cu with dis 
        $ chuu_beat += 1
    
        cu "「*Glub glub* 」"
    
        show ta at jump_up
        pause .2
            
        ta "「Gahaha! Well, it is cheap.{p}\ \ If we're going to Raimon,\n\ \ we're gonna drink, yeah? 」"
        
        show ni 102 with dis
        
        ni "「Weren't you against drinking? 」"
        
        show ta 108 with dis
        
        ta "「I-{w=.2}I just got told to keep an eye on things.{p}\ \ If I'm there, it should be fine. 」"
        
        show tp 101 with dis
        
        tp "「You're not drinking. 」"
        
        show ni 103 with dis
        
        ni "「Of course. It is the boss' money, after all. 」"
        
        show ta 103 at jump_up
        pause .2
        
        ta "「No way-! 」"
        "Tatsu-nii pulled a disappointed face,\nand sunk into the water."
    
        show tp at jump_up
        pause .2
        
        tp "「Right, if you guys have rested up,{p}\ \ then let's go decide what to do! 」"
        
        show cu 102 at farright with wipe_up
        
        cu "「'Kay!! 」"
        fn "「Wait, even if you've been told not to go to Raimon,\n\ \ is it all right for you to bring everyone along? 」"
        
        show ta 109 with dis
        
        ta "「That's right!{p}\ \ Ma's not gonna like this!! 」"
        
        show tp 103 with dis
        
        tp "「Huh?{w} 　The lady just doesn't want me to drink!!{p}\ \ I am the law of the Midoriya Group!! 」"
        
        show cu 112 with dis
        
        cu "「Whoa,{w=.2} so cool!\n\ \ That was so manly, Master! 」"
    
        show tp at jump_up
        pause .2
        
        tp "「How many times do I have to say it,\n\ \ before you get it?\n\ \ It's Chief! I'll break your front teeth!!! 」"
        
        play sound splash
        show cu 109 at fall
        hide cu with dis 
        $ chuu_beat += 1
        
        cu "「*Glug glug* 」"   
        fn "「Is he all right...? 」"
    
        scene black with sdis
        
        "The following day,\nwhen Tappei-san was strangely nice to Yukino-san,\nwas a secret to everyone outside the Midoriya Group."
        
        jump end20

    
#######################################################
label shun20:
    
    $ event_name = "The Blue Moon and the Wolf"

    scene map
    hide screen house20
    scene black with wipe_dr_slow
    stop music fadeout 1.5
    play sound night_insects loop fadein 1
    scene hbroom night with dis
    
    "The moon is beautiful."
    "It's as scary as it is beautiful. Sensitive to\nevery single particle of air, the terminal nerves\nthroughout my whole body are tingling this night."
    "At times like this,\nthere's no telling what I'll do."
    "Even without that,\nI somehow feel that there have been many\nsexual stimuli in my daily routine recently."
    "I'll handle it properly before I surrender\nmyself to my growing excitement and end up being\nindebted to somewhere like a police station."
    "Then I'll go to bed."
    who "「Hello, are you there [fn]-san? 」"
    "Aaaaaah!\nA visitoooooor!"
    "Because I don't have the skillfulness to pretend\nthat I'm out, I decide to stand up slowly.{w} Yeah,{w=.2}\nI should be able to deal with a visitor, right?"

    scene hentry night
    show su 007 night at center
    with wipeleft_slow
    
    su "「[fn]-san. 」"
    "Why is he slightly red?{p}Why is his voice somewhat coaxing?{p}And above all else, why is he visiting this late?"
    "This is awfully pleasant,{w} er, I mean rare."
    
    show su at bobbing
    pause .2
    
    su "「Hehee. 」"
    "His tail is swinging more voluptuously than usual."
    "Is he tempting me?{p}Is there nothing that can stop\nmy slightly high tension tonight?"
    
    show su 019 night at still with dis
    
    su "「[fn]-san, do you want to go out and play? 」"
    
    menu:
        "A. Agree without thinking of the consequences.":
            $ shun_play = True
        "B. It'd be a disaster if I mistakenly got involved with him.":
            $ shun_play = False
    
    "The inside of my head should be moderately\nnumbed every once in a while."
    "Aren't there nights where\na calm decision is impossible?{p}This is one of those nights."
    "So..."
    
    if shun_play == True:
        jump shun20_play_accept
    else:
        jump shun20_play_refuse

    ##########################################################
    label shun20_play_refuse:
        
        "My cute childhood friend wolf's (although this\nlate night visit is an unusual thing for him)\nstrange invitation, "
        "while regretting it from the bottom of my heart,\nI decline."
        fn "「Let's go out some other time,\n\ \ it's already too late tonight. 」"
        fn "「Won't your dad and mom worry\n\ \ if you don't get back home?{p}\ \ {nw}"
        show su 011 night with dis
        extend "So I'll- 」"
        "I swallowed down the words 「-take you back 」\nthat had come up my throat because\nI'm worried that if I were charmed "
        "by the moonlight on the way back,{p}I'll start doing something I'd feel guilty about."
        "While I'm hesitating whether or not to say it,\nhis tail that was lightly swimming in the air\nsuddenly stops and his ears droop down."
        "Then, his two big, round eyes begin to moisten."
        
        show su 018 night with dis
        
        su "「[fn]-san... 」"
        "I just did something terrible.{p}I have made the small wolf in front of me cry."
        "Immediately I try to search\nfor something to say, but..."
        
        su "「Waaaahn!{w=.2}{nw}"
        hide su with dis
        extend "　I wanted to{size=-10} go out with... 」"
        
        "I didn't hear the last part very well because\nI think he covered\nhis face with his arm,"    
        "turned away, and started to run at full speed\ndown the dark nighttime road."
        
        if meet_gaku == True:
            jump shun20_angry_gaku
        else:
            jump end20
        
    ############################################
    label shun20_angry_gaku:
        
        $ event_name = "Light Brown Fur Coat"
        
        "Even though I'm flustered and perplexed,\nI slip my feet into my sandals at the entrance\nto chase after him. Then at that moment."
    
        stop sound fadeout 1
        play music ambience01
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        
        "On the other side of the door I was keeping open,\nI run into a light brown fur coat."
        "I wasn't able to clearly see who it was\nbecause my awareness had scattered too much\nin that instant,"
        "But from that slender waist,\nI could tell it was Gaku-san.{nw}"
        scene path night
        extend ""
        "I look around outside the door.{p}About 100 meters ahead, in the middle\nof the road lit by moonlight."
        
        show gk 003 night at midleft
        show su 021 night at center
        with dis
        
        "Shun-kun is caught by Gaku-san."
        "No, he's being protected by him."
        "...err.{p}What I'm supposed to do seems to be gone.{p}I obediently go back to my room and go to bed."
    
        jump end20
        
    ##############################################
    label shun20_play_accept:

        $ event_name = "Nighttime invitation"
            
        scene black with sdis
        scene mountain_path night with blind_skinny
        show su 019 big night at center_big with sdis
        pause 1.5
        
        "His light brown coat shines\nin the dazzling moonlight."
        "His collarbone peeking through the nape\nof his neck is caught in my field of vision\nwith more precision than usual."
        
        hide su with dis
        show mountain_path night at hshake
        show su 007 night at offright_far
        pause .2
        
        "Aah, I shouldn't be doing this.{p}I shake my head from side to side,\ntrying to maintain normal thoughts."
        "Everything is connecting to my sexual desire.{p}Why did I have to give in and say 「Yeah! 」 earlier?"
        "Usually I think he's \"cute\" or \"adorable\",{p}but tonight it has all been converted\nto nothing but 「××× 」."
        "...For 「××× 」, please put in\nyour favorite erogenous word."
        "My only salvation is,"
        
        show su at move_offleft_far(1)
        
        su "「Yaay, yaay, yaay. 」"    
        "Are Shun-kun's feet not touching the ground?{p}In a sense of the meaning of the sentence\nand in a physical sense."
        "I'm afraid he's going to wander onto the nighttime\nstreet happily skipping around like that."
        "While I'm thinking about that, he gallops back to me.{w}{nw}"        
        show su at move_center(0.5)
        extend "{w=.5}{nw}"
        show su at bobbing
        pause .2
        
        su "「[fn]-san! Hey hey, are you coming? 」"
        "He pulls on my arm."
        "Since Shun-kun is so restless,\nit would be terrible if I left him alone!"
        "I must watch over him!{p}My circuit to say that occasionally reacts.{p}Somehow I am able to keep calm."
        "Aah, Shun-kun. The most dangerous thing\nis your onii-san in front of you."
        "If I can avoid this just being the two of us,\nI might be able to get through this alright."
        "Or rather,{w} something is likely to happen\nwhen it's just the two of us!"
        "While I'm endlessly worrying, Shun-kun looks back\nand earnestly advances towards the moonlight."
        
        show su 019 night with dis
        
        su "「Oh Mooooon-samaaaa, climbing pure white♪ 」"
        "Tonight's song is particularly spirited."
        
        show su 021 night with dis
        
        su "「Daifuku♪ 」"
        "It has already lost coherence."
        
        show su at move_offright_far(0.5)
        
        su "「Assault♪ 」"
        "Where!?"
        fn "「W-wait, Shun-kuuun. 」"
        
        show su 007 night at move_center(0.5)
        
        su "「Hurry, hurry. 」"
        fn "「No, wait a minute,\n\ \ we're sprinting at full speed now? 」"
        
        show su 021 night with dis
        
        su "「The daifuku will get cold. 」"
        "It seems he's already completely\nintoxicated by the moon."
        "I am too.{p}When I walk, the frustrations\nbelow my abdomen interfere with reason."
        "Ooh, I should have at least dealt with that\nbefore leaving."
        "We should visit somebody's house\nto avoid this just being the two of us."
        
        menu:
            "A. Let's go to Tatsu-nii's place.":
                jump shun20_visit_tatsuki
            "B. Let's go to Kounosuke's place.":
                jump shun20_visit_kounosuke
    
                
    ####################################################
    label shun20_visit_tatsuki:

        $ event_name = "The Midoriya Family's Bowl"
        
        show su 023 night with dis
        
        su "「We're going to play at Tatsuki-san's place?  」"
        fn "「Yeah, I think he's still awake. 」"
        
        show su 007 night with dis
        
        su "「Let's race then! 」"
        fn "「Huh? 」"
        
        show su 019 night at bobbing with dis
        pause .2
        
        su "「The first one to hug Tatsuki-san wins! 」"
        fn "「Huh?{w=.2}　{w=.2}What?　{w=.2}Shun-kun? 」"
        
        show su 007 night at still with dis
        
        su "「Gooo! 」"
        
        show su at move_offleft_far(0.5)
        
        "Then Shun-kun of the night once\nagain takes off a maximum speed."
        "It's dirty when I add \"of the night.\"{p}No!{w=.2} I have to chase him!"
        
        scene black with blind_vert
        scene tatsuki_house_front night with blind_vert
        
        "Haah, haah, haah..."
        "Alright, I'm done seeing Shun-kun's\nback at Tatsu-nii's house.{p}I can finally slow down."
        "I unsteadily stagger through the gate.{p}Just as I expected, I'm welcomed by a party\ngoing on at full swing."
        
        stop sound fadeout 1    
        play music piano2_015
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        show ta 302 night at midleft with dis
        
        ta "「Yooo!! 」"
        "The scene in front of me from where the greeting\ncame from is prettier than a picture."
        "There's the moon glittering\nin the midsummer night sky, and two dragons."
        "The Midoriya father and son have pulled seats out\ninto the garden and are in the middle\nof watching the moon."
        "And there's no mistaking that Tatsu-nii\nis completely drunk."
        tp "「... 」"
        "Thankfully, Tappei-san is asleep.{p}I pitifully don't have the self-confidence\nto defend the small wolf from those two."
        ta "「No way, that body blow from\nearlier was [fn]'s training!? 」"
        fn "「Body blow? 」"
        
        show su 007 night at midright with wipe_up_slow
        show ta 303 night with dis
        
        ta "「Shun charged in at mach speed right\n\ \ into my dad's chest!{w} He just fell over\n\ \ and hit his head. 」"
    
        show ta 310 night with dis
        
        ta "「It's been a long time since I've seen\n\ \ such an amazing flying technique. 」"
        
        show su at bobbing
        pause .2
        
        su "「Hehee. 」"
        "Don't compliment him!"
        fn "「I-Is Tappei-san going to be okay!? 」"
    
        show ta 004 night with dis
        
        ta "「\"You haven't trained enough to knock me out\n\ \ with something of that level!\" 」"
    
        show ta 308 night with dis
        
        ta "「Is what he'd say.{p}\ \ Don't worry, he'll get up sooner or later. 」"
        "Oh, really...."
        "By the way, there are empty bottles strewn here\nand there, but there's a fresh supply outside?"
        "There's no way both of them opened all of these,\nis there?"
    
        show ta 302 night with dis
        
        ta "「Alright!{w=.2} You drink too, Shun! 」"
        
        show su 019 night at still with dis
        
        su "「Okay!{w=.2} Thank you very much! 」"
        "Wait-wait-wait-wait.{p}This is usual for Tatsu-nii,\nbut what's a good counterattack for Shun-kun?"
        fn "「W-wait a minute Tatsu-nii, don't! 」"
        ta "「What?{p}\ \ Can't you see that moon?{p}\ \ Looook, even I'm reflected in it. 」"
        
        show su 007 night with dis
        
        su "「Wow, it's beautiful. 」"
        "He pours a clear liquid into an empty bowl.{p}A white outline floats on the surface\nand sways to and fro."
        ta "「Now!{w=.2} Drink up! 」"
        
        show su 021 night with dis
        
        su "「Let's drink the moon. 」"
        fn "「N-no, Shun-kun!! 」"
        
        show su 023 night with dis
        
        su "「Hanya? 」"
        "I act quickly."
        fn "「That juice is really bitter,\n\ \ I don't think you should drink it. 」"
        
        show su 020 night at jump_right
        pause .2
        
        su "「Hawah!?{p}\ \ But didn't Tatsuki-san say it's sweet syrup!? 」"
        "Shun-kun puts down his sake bowl\nand pounces on Tatsu-nii."    
        ta "「Yaah, sorry sorry!{p}\ \ I do have another sweet spot though! 」"
        
        show su 007 night at midright with dis
        
        su "「Woof. 」"
        
        show ta 310 night 
        show su 019 night 
        with dis
        
        "Shun-kun's eyes shine with anticipation."
        "On the other hand, Tatsu-nii's eyes\nare emitting a mysterious light and\nhis left hand is across his belt."
        "I drag Shun-kun along{p}and decide to leave that place.{w} {nw}"        
        show su at move_offright_far(1)
        extend "{w=.6}{nw}"
        show ta 402 night with dis
        
        ta "「You just need to tightly suck this up.{p}\ \ The tube is thin, so you have to get it\n\ \ pretty far into your mouth... 」"
        ta "「Huh?{w=.2} Shun?{w=.2} [fn]? 」"
        
        jump shun20_exhausted
    
    #############################################
    label shun20_visit_kounosuke:
        
        $ event_name = "Chasing Kounosuke's Moon"

        scene black with blind_vert
        scene kouno_house_out night
        show su 019 night at midright
        with blind_vert
        
        "We manage to get to the Kuri house.{p}Since he's probably still awake,\nI'll try to talk to him."
        "While I'm thinking that,{p}{nw}"
        play sound2 tm2_slidedoor000
        extend "Kounosuke opens the door and bumps into me."
    
        stop sound fadeout 1    
        play music drumn_018
        $ renpy.music.set_volume(0.5, 0.0, channel = "music")
        show ko 001 night at midleft behind su with dis
        
        su "「Kounosuke-saaan♪ 」"
    
        show ko 006 night with dis
        
        ko "「Oh, Shun, you're in high spirits,\n\ \ aren't you? 」"
        
        show su 020 night with dis
        
        su "「You shouldn't be going out at a time like this! 」"
        
        show ko 004 night with dis
        
        ko "「I should say the same to you.{p}\ \ It's more dangerous for you, right?{p}\ \ Isn't it past your curfew? 」"
        
        show su 019 night with dis
        
        su "「Tonight...{w=.2} [fn]-san is with me,{p}\ \ so it's okay. 」"
        "So the day when Kounosuke is the one\nwarning Shun-kun has come... "
        "Ah- did he notice me smiling bitterly?"
        
        show ko 005 night with dis
        
        ko "「[fn]. You were thinking \"So the day when\n\ \ Kounosuke is the one warning Shun-kun has come.\"\n\ \ just now, weren't you? 」"
        fn "「N-no I wasn't. 」"
    
        show ko 007 night with dis
        
        ko "「You're making a curious looking face.{p}\ \ I am irresponsible after all. 」"
        "Oh great, he's sulking."
        
        show su 007 night with dis
        
        su "「What are you going out to do? 」"
        
        show ko 002 night with dis
        
        ko "「This. 」"
        "He says with a smile and holds up\nthe camera hanging around his neck."
        fn "「Photography? 」"
        
        show ko 003 night with dis
        
        ko "「Yep. I thought I'd take some\n\ \ pictures because it's so beautiful. 」"
        
        show su 007 night at move_offright_far(0.5)
        
        "I follow Kounosuke's line\nof sight up to the summer night sky."
        "This evening's strange daifuku seems to not just\nbe calling to wolves, but tanukis as well."
        
        show ko 001 night with dis
        
        ko "「By the way, 」"
        "Turning his head around, Kounosuke turns towards me.{p}Then, he glances towards Shun-kun.{w} {nw}"        
        show su 021 night at move_midright(1)
        extend "{w=1}{nw}"
        show su at move_offright_far(1)
        
        "Earlier, the wolf had drawn a ring\nand stepped on it, and is singing\n\"The Moon's Song\"(title pending) and dancing."
        
        show ko 005 night with dis
        
        ko "「Did something happen to him? 」"
        "Don't look at me with\nsuch a suspicious expression."
        "I have nothing to do with\nShun-kun's condition this time.{p}Instead, I would like to know."
        ko "「Did you drug him or something? 」"
        fn "「I didn't do it! 」"
        "Once again, we watch the wolf pup dance around.{w} {nw}"        
        show su at move_midright(1)
        extend "{w=1}{nw}" 
        show su at jump_up
        pause .2
        show su at move_offright_far(1)
        
        "It's as if his tail is cutting the sky.{p}The undaunted moon and his fiery shining eyes."
        "Occasionally he jumps and kicks up dirt\nwith both his feet."
        "This is somewhat childish... even for Shun-kun,\nbut this is the first time I've seen him\nso cheerful without thinking of the consequences."
        "I doubt even Kounosuke\neasily reaches the upper area of this."
        "That being said,"
        fn "「That looks fun, so this is okay isn't it? 」"
        fn "「I'll yell, even if it's there's no reason to,\n\ \ this is my long-awaited summer vacation\n\ \ and tonight only comes today! 」"
        fn "「Let's enjoy it to the fullest! 」"
        
        show su 007 night at move_midright(0.5)
        
        su "「That's right! 」"
        "I say with Shun-kun, who has returned."
        "Kounosuke compares us with an even more\nsuspicious facial expression."
        ko "「There's no need to guess,\n\ \ but are you in fairly high spirits as well? 」"
        fn "「Th-that's not it!{p}\ \ Right now I'm on a mission\n\ \ to lukewarmly watch over Shun-kun! 」"
    
        show su at jump_up
        pause .2
        
        su "「It's a mission!{w=.2}{p}\ \ {nw}"
        show su at jump_up
        extend "{w=.2}He's watching over me! 」"
        "He declares."
        "Sorry Kounosuke,\nI might be kind of hopeless as well.{p}I apologize to him in the back of my head."
        
        show ko 004 night with dis
        
        ko "「Well, I guess this is alright."
        ko "「It seems Shun-kun{w=.2} is{w=.2} really trusting of you,\n\ \ so you better live up to his expectations! 」"
        "He stressed \"is\", {w=.2}\nbut I decide not to pay it any mind."
        fn "「Of course. 」"
        
        show ko 001 night with dis
        
        ko "「Alright then, I'm going.{p}\ \ Be a reliable guardian and make\n\ \ sure his stomach doesn't get cold. 」"
        
        show su 007 night at sway
        pause .2
        
        su "「I'll behave! 」"
        fn "「I'll make him behave! 」"
        
        show ko 004 night with dis
        
        ko "「I don't understand you at all. 」"
    
    #############################################
    label shun20_exhausted:
            
        $ event_name = "The Right Way to Spend a Summer Night"

        scene black with sdis    
        stop music fadeout 1
        play sound night_insects loop fadein 1 
        scene field1 night with sdis
        
        "As usual, my air-headed brain mistakes\nShun-kun for someone else."
        "While I'm not watching him,\nI arrive at a field of sunflowers."
    
        show su 019 night with dis
        
        su "「There are a lot of sunflowers,\n\ \ aren't there? 」"
        fn "「They feel a little out of place in the dark. 」"
        "Is this used when they ship out the crops?{p}We sit on a high wooden crate and change\nfrom moon viewing to flower viewing."
        "Why, Shun-kun,\nare you in such high spirits this evening?"
        "Why did you go out at such\na late hour in the first place?"
        "Curiosity surges into swirling doubt.{p}Shall I question him for a moment?"
        fn "「Hey, Shun-kun? 」"
    
        hide su with wipe_down_slow
        
        su "「Suuu... 」"
        "Eh."
        "My childhood friend, after having walked\naround the village for a while,"
        "Has wholeheartedly dozed off and is making\ncute breathing noises in his sleep."
        fn "「Shun-kun? 」"
        su "「Piiii... woof. 」"
        fn "「Are you sleepy? 」"
        
        show su 017 night with wipe_up_slow
        
        su "「I'm not sleepy,\n\ \ I want to play with you some more... Suuu. 」"
        "He nods off and his body is beyond his control.{p}If this keeps up he might collapse."
        fn "「Should we go home soon? 」"
        su "「We're still playing... kuu. 」"
        
        hide su with wipe_down_slow
        pause .2
        
        "He leans on the upper half of my body.{p}Shun-kun's sweet scent softly carries over to me."
        su "「Nnn. 」"
        "He pushes his muzzle into my chest\nand attempts to stabilize his posture.{p}Or rather, he's trying to hug me."
        "His arms wrap around me and tightly cling to me."
        "Whoa, he's really warm.{p}His body heat transfers to me by contact."
        su "「Suuu, piiiii. 」"
        "He has really fallen asleep.{p}Err, this posture is quite painful for both of us."
        "I want to get comfortable somehow."
        "Waking Shun-kun up and going home\nmakes sense to deal with this,\nbut this feels too good."
        "I've been waiting so long for this chance\nto be close to him, I think I'll take advantage\nof this to get some extra benefits!"
        
        show field1 night at hshake
        pause .2
        
        "...aaaah."
        "I shake my head.{p}It's no use, this has been decided\nsince I left home, hasn't it?"
        "Shun-kun has been seduced by the moon,\nI have to take care not to awaken\nstrange feelings."
        "We should leave because I'm supposed\nto be watching over him."
        "No."
        "Let's consider the opposite."
        "Shun-kun invited me out,\ndid he intend to relieve the numbness\nof our bodies fueled by the moonlight together?"
        "That's right.{p}Shun-kun and I have both been\nintoxicated by the moon, haven't we?"
        su "「Nnn... [fn]-san. 」"
        "If that's the case..."
        fn "「Shun-kun... 」"
        "I should meet the expectation\nof the right way to spend a summer night,\nshouldn't I?"
        
        hide su with qdis #!#Check transition

        menu:
            "A. Let him sleep with his head on my lap.":
                jump shun20_lap
            "B. Pester him for a kiss.":
                jump shun20_kiss
    
    ######################################################
    label shun20_lap:
        
        $ event_name = "Lap pillow"

        stop sound fadeout 1    
        play music free0428
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        
        "The act of the head of one person depending\non the thighs of another, known as a lap pillow."
        "Shouldn't it have originally been\ncalled a thigh pillow?"
        "Anyways, now my half-asleep childhood friend\nis right next to me.{w} This is a great chance\nto make a longtime dream come true!"
        fn "「If you're sleepy,\n\ \ would you like to use my lap as a pillow? 」"
        su "「Nnn, I want a pillow. 」"
        fn "「You do? Then carefully shift your body down. 」"
        "I turn my back and let him go from my arms,\nthen his body slowly falls."
        su "「Nng... 」"
        "Shun-kun dutifully slips his finger{p}into the heel of his shoes and takes them off,{p}then lays them diagonally on the top of the wooden box."
        "My back doesn't feel good and my balance\nisn't that great,{p}but oh well."
        "Ah."
        "I just now noticed something serious.{p}You know, it's a lap pillow,\nalso called a thigh pillow."
        "It's between my thighs.{p}It's getting hard."
        "B-but Shun-kun is so soft and fluffy\nand his body is so warm and smells so good\nand the moon is so sexyyyyyy!"
        su "「That's your scent, isn't it? 」"
        "Shun-kun nuzzles his cheeks against my thighs.{p}The stimulation of the cloth over it is tantalizing."
        "Aah, if he shifts just a few centimeters\nhe'll be at a bad spot."
        su "「Nnnn. 」"
        "A few moments later,{p}he distorts his face and opens his eyes."
        
        show su 020 night at center with wipe_up_slow
        pause .2
        
        su "「My butt hurts. 」"
    
        hide su with wipe_down_slow
        pause .2
        
        "Finding his large tail unmanageable,{p}he turns to the side."
        "Wooden boards feel different from a bed.{p}He has passed sleepiness,"
        su "「Uuu. 」"
        "And is in a bad mood."
        
        stop music fadeout 1
        pause 1
        play music free10
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        
        fn "「Here Shun-kun, I'll carry you. 」"
        su "「Okay! 」"
        "He's bold this evening,\nnot reserved or hesitant."
        "This time he turns his arm to my neck\nand sits sideways on my lap."
    
        show su 019 big night at center_big with dis
        
        su "「I'm not heavy, am I? 」"
        "His open muzzle hits my neck\nand lets out a feverish sigh."
        "Shun-kun is somewhat short,\nbut it's still kind of difficult\nto put someone on your knee."
        "Be that as it may, I would regret\nmissing this opportunity to be close to him."
        fn "「I'm okay, you're light. 」"
        "I laugh with a smile.{p}{nw}"
        show su 007 big night with dis
        extend "A smile is lured from Shun-kun's mouth as well."
        "With our bodies pressed\nagainst each other like this,\nboth of our temperatures seem to rise even more."
        "And that one part of my body is stretching and\nstiffening because it's congested with blood."
        "What should I do?"
        su "「Looks like we got back. 」"
        fn "「Huh? 」"
        
        show su 019 big night with dis
        
        su "「[fn]-san, I want to- 」"
        "He woke up?{p}Shun-kun looks up at my face\nand has begun to talk bit by bit."
        su "「-do a reverse warp with you. 」"
        "Suddenly,{p}he says a word I'm not familiar with."
        fn "「Warp? 」"
        su "「It's when your score and remaining lives are zero\n\ \ and you return to the middle of a level instead\n\ \ of the beginning, but you can still keep playing. 」"
        fn "「Keep playing a video game? 」"
        su "「Yes.{w} {nw}"
        show su 022 big night with dis
        extend " You have to be good at it, though. 」"
        fn "「Video games are your strong point, aren't they? 」"
        "I try to grin at the only part\nof the conversation I understand,\nbut he returns an apologetic smile."
        "A rare expression I don't see\nfrom him very much."
        
        show su 007 big night with dis
        
        su "「There aren't many more people\n\ \ who are good at them. 」"
        
        show su 011 big night with dis
        
        su "「So when you left,\n\ \ I thought of how you could come back. 」"
        "He says that and smiles again."
        
        show su 007 big night with dis
        
        su "「Jumping into a pipe would also be a fun way\n\ \ for us to go back and forth. 」"
        su "「Then I could have played games with you,\n\ \ and I could see you again and again. 」"
        su "「You didn't come back though.{p}\ \ It was only natural. 」"
        su "「But you're here now. 」"
        su "「I'm really glad for that. 」"
        fn "「I'm glad too.{p}\ \ I've come back to Minasato to meet everybody. 」"
        fn "「I can't help but be glad I get\n\ \ to be with you like this. 」"
        su "「Hehee... 」"
        "I smile and brush his head,\nhis tail sways with satisfaction."
        "When I do that for a while,\nShun-kun inhales,\nthen peacefully falls into slumber."
    
        hide su with wipe_down_slow
        
        "...but now my joystick is waiting expectantly\nfor it to be grasped and its trigger pulled."
        "What should I do?"
        
        jump end20
      
    ##################################################    
    label shun20_kiss:   
    
        $ event_name = "Saying Goodnight"

        stop sound fadeout 1
        pause 1
        play music melodious04
        $ renpy.music.set_volume(0.6, 0.0, channel = "music")    
        show su 007 night at center with dis
        
        fn "「Shun-kun. 」"
        su "「Yes? 」"
        "I point to my cheek."
        fn "「Can I get you to push against here? 」"
        
        show su 023 night with dis
        
        su "「?{w=.2}\nHow? 」"
        fn "「Your mouth, or rather, your lips. 」"
        "As expected, this is a little awkward.{p}I wonder if that was shameless."
        "On the other hand, Shun-kun consents and I put both\nof our hands together in front of my chest."
        
        show su 007 night with dis
        
        su "「Oh!{w=.2} This is how you say goodnight,{p}isn't it?! 」"
        "Nnah!?"
        
        show su at bobbing
        pause .2
        
        su "「I remember this,{p}\ \ I used to always do it in my futon. 」"
        fn "「Uh, this is probably different\n\ \ than what you're thinking of. 」"
        "While I mutter that,{nw}"
        hide su with qdis
        extend " his body starts to hang on to me.{p}He brings his lips close to my shoulder."
    
        show su 007 big night at center_big with dis
        
        "Funyuu.{p}I feel his soft muzzle on my neck and chin,\nthen it runs up to my left cheek."
        "A sweet smell carried\nby the night wind tickles my nose."
        
        show su 019 big night with dis
        
        "He does it again, on the right side this time.{p}His fur feels soft and his inner heat\nrubs against me."
        "However, I'm dumbfounded\nthe next moment by Shun-kun's face."
        
        show su 007 big night with dis
        
        su "「Goodnight, [fn]-san♪ 」"
    
        hide su
        show su 019 night at center
        with dis
        
        "After that he reseats himself sideways,\nand leans his shoulder against me with\na pleasant weight and body temperature."
        "Before I know it,{w=.2}\nhis left hand is wrapped around my right,"
    
        hide su with wipeleft
        pause .2
        
        "and he makes the healthy breathing\nof a sleeping person."
        "That probably took less than 3 seconds,\nbut it felt much longer to me."
        "Was it because of the moonlight or\nthe effect of his body heat?"
        "It was slightly different\nfrom the kiss I had wanted."
        "My head is somewhat reeling from this\nmore sensational gesture.{p}I'm surprised he had such an obscene bedtime ritual."
        "Shun-kun, who had been continuously talking,\nhas become silent."
        "While I look at his sleeping face,\nand sometimes the sunflowers,\nI don't give into my excitement and cool down."
        
        jump end20
    
#######################################################
label kouya20:
    
    $ event_name = "Lodgings and Staying Over"
    hide screen ricefield20
    scene map
    pause .01

    stop music fadeout 1.5
    scene black with wipe_dr_slow
    scene rice_paddy with wipe_corner
    play music tam_n06
    $ renpy.music.set_volume(0.8, 0.0, channel = "music")
    
    fn "「Hmm,{w=.2} what should I do? 」"
    "It's a clear morning, looking just like always.{p}I was grumbling as I walked down the peaceful country road."
    "If I turned my head to the side,\nthe stalks of rice awaiting harvest\ntime swayed in the wind."
    "Today{w=.2} really is peaceful."
    "Yet in a scene that beautiful,\nI was in an equally downer mood."
    fn "「Haaah... 」"
    "I couldn't think up of any good ideas,\nso I let out a sigh."
    "If I had to say I had anything to worry about here,\nit would be where I'm currently staying."
    "I'm staying with my grandparents right now,\nbut it's already been three weeks."
    "Up until now, they've been living\nand relaxing like a couple, then someone\nlike me just suddenly dropped in for three weeks."
    "They're still my family, but I'm starting\nto think I'm causing them trouble."
    "And if they heard that directly:"
    
    scene hbroom with wipeleft
    
    gm "「That's not true,{w=.2} [fn]-chan. 」"
    gp "「That's right,{w=.2}\n\ \ you don't need to worry about us. 」"

    scene rice_paddy with wipeleft
    
    "Or so I can easily imagine them saying,{p}but I still wonder if it's true."
    "In other words, I was thinking\nabout my circumstances,{w=.2}\nthen started worrying about them."
    fn "「But, this isn't really all that clear... 」"
    "For about two, maybe three days is cool,\nbut maybe I can't really solve this problem.{p}If I could, it'd be something to celebrate."
    fn "「Well it's not like some kind of saviour\nis gonna pop out of the sky... 」"
    who "「Some kind of saviour? 」"
    fn "「Hwah!? {nw}"
    play sound swing30_c
    scene black with wipe_right_fast
    extend ""
    
    "All of a sudden,{w=.2}\nthere was a whisper right next to my ear."
    "Damn it, who's going around pulling dangerous\npranks like this!?{w} My spine's crawling\nbecause of that breath on my ear!"

    scene rice_paddy
    show ka 002 at center
    with wipe_right_slow
    
    fn "「Oh,{w=.2} it's you, Kouya. 」"
    "Looking back and sitting in front of me,\nthere was Kouya's smiling face."
    "Geez,{w=.2} Kouya's so terrible for hiding\nhis presence and sneaking up on me like that.{p}He could have talked to me normally."
    
    show ka 005 with dis
    
    ka "「What's up with that? {w=.2}\n\ \ It can't be that much of a surprise, [fn].{p}\ \ What?{w=.2} Not happy to see me? 」"
    "Kouya pretended to be intimidated by me as a joke.{p}That way of delivery embarrassed me a little,\nso I scratched my cheek."
    fn "「Oh, no,{w} that's not what I meant... 」"
    
    show ka 003 with dis
    
    ka "「I got that much.{w=.2}\n\ \ I just wanted to try saying that.{p}\ \ So, what's up?{w} You don't look too happy. 」"
    fn "「Hm?{p}Ahh,{w=.2} well the thing is... 」"
    
    show ka 001 with dis
    
    "This, that, A, B,{w=.2} and other stuff\nI went over as I explained to Kouya."
    fn "「...And that's how it is.{w=.2}\nSo I was thinking about what I should do about it. 」"
    
    show ka 005 with dis
    
    ka "「Uh-huh.{w} You're worrying about weird stuff again.{p}\ \ You're really dutiful,{w=.2} or something like that... 」"
    "Kouya dismissed all my worries with a 'weird.'"
    "Uu,{w=.2} that was such a shock...{p}I know he's always like that, but Kouya's so blunt..."
    fn "「You could say that...{p}\ \ I tried thinking that way for a bit,\n\ \ but I couldn't sort out anything in my head. 」"
    
    show ka 003 with dis
    
    ka "「But that's one of your good points.{p}\ \ You think about other people,\n\ \ and you make them happy. 」"
    "Kouya said it so quickly."
    "I'm not sure what came over me, but being praised\nto my face was kind of embarrassing.\nEven I could tell my face turned red."
    fn "「R-{w=.2}really? 」"
    
    show ka 002 with dis
    
    ka "「I think so.{p}\ \ ...all right, how about this? 」"
    fn "「Eh, what? 」"
    
    show ka 001 with dis
    
    ka "「Two or three days is okay, right? 」"
    fn "「Yeah. 」"
    ka "「In that case, [fn]... 」"
    fn "「Yeah? 」"    
    ka "「In that case,{w=.2}\n\ \ stay at my place for a while. 」"
    fn "「Uh... huh? 」"
    "...what just happened?"
    ka "「I said,{w} you can stay at my place. 」"
    fn "「... 」"
    
    stop music
    play music cicada01 fadein 1
    
    "Kouya's sudden proposal left me speechless.{p}FUNCTION CEASED,{w=.2} I REPEAT FUNCTION CEASED.{p}ERROR, ERROR. RESTART, RESTART."
    "...okay,{w} what just happened?"
    
    stop music fadeout 1
    play music tam_n06
    
    fn "「Umm, sorry.{p}\ \ Could you say that one more time? 」"
    
    show ka 005 with dis
    
    ka "「W-what?{p}\ \ Like I said,{w=.2} you can stay at my place,{p}\ \ if you're okay with that. 」"
    fn "「...seriously? 」"
    
    show ka 001 with dis
    
    ka "「Why would I lie? 」"
    fn "「But, wouldn't that bother you? 」"
    ka "「If I thought that,\n\ \ I wouldn't be offering in the first place.{p}\ \ And anyway, what are you being so humble for? 」"
    fn "「But- 」"
    
    show ka 014 with dis
    
    ka "「...fine.{p}\ \ I'll rephrase it. 」"
    "Kouya got his face under control."
    "After working his mouth in light\nmovements as if to find the right words,"
    "He looked straight into my eyes\nlike he was deciding his thoughts."
    
    show ka 006 with dis
    
    ka "「I want you to stay at my place.{p}\ \ But only if you're okay with that.{p}\ \ Or, do you...{w=.2} not like that idea? 」"
    "In his face, I could see\nmy own feverishness reflect towards him."
    "In those always-straight-standing ears,\nI could also see them turning slightly red."
    "I guess{w=.2} it really is embarrassing."
    "That makes sense,\nhe's saying something he usually doesn't.{p}I think it's especially unusual for Kouya."
    "He doesn't seem to be the type to talk about this."
    "But because of that, those feelings\nreally were something to be happy about.{p}Definitely. I could feel my face getting more red."
    ka "「So, what'll you do, [fn]?{p}\ \ You wanna come? Or don't you? 」"
    "Kouya pressed me for an answer."
    "But even without the pressure,\nI've already decided my answer:"
    
    menu:
        "A. I'll come over.": 
            jump kouya20_accept
        "B. I'll take you up on that.": 
            jump kouya20_accept
        "C. I-I'll stay at your place, haha!": 
            jump kouya20_accept


    ########################################################
    label kouya20_accept:
            
        $ event_name = "To Three Wonderful Days"
        
        "What was three choices was really one.{p}I'm so easy to understand."
        "Besides, it'd be bad if I didn't go, right?"
        fn "「Then I guess I'll take you up on your offer.{p}\ \ ...please take care of me then, Kouya? 」"
        
        show ka 003 with dis
        
        ka "「Yep. 」"
        "With Kouya's smile,\neverything was stamped with 'approved.'"
        "And that was how my next three days kicked off."
        
        stop music fadeout 1
        scene black with sdis 
   
        $ event_name = "Staying with Kouya Day 1"

        scene rice gray 
        show over red light
        with wipe_corner 
        show ka 002 gray behind over at center with dis
        play music free0213 fadein 1
        
        ka "「When do you want to do it?{p}\ \ Starting from today, or something? 」"
        fn "「Hmm...{p}\ \ The sooner the better,{w=.2}\n\ \ so I guess I'm in your care starting today. 」"
        
        show ka 005 gray with dis
        
        ka "「...the better,{w=.2} huh? 」"
        fn "「Thanks for acting the straight man. 」"
    
        scene hbroom with wipe_right
        
        "Through this and that, for the next three days,\nI'm getting closer to staying at Kouya's place."
        "Right now I'm in the middle of packing for that."
        fn "「By now, most of my stuff\n\ \ is already packed up,{w=.2} I think. 」"
        "When I came over here I had travel bags,\nchanges of clothes, and a bunch of other things,"
        "But honestly, just bringing one\ntravel bag seems like enough."
        "Even then, I didn't bring that much\nwith me in the beginning,{w=.2}\nso it's not like it's a pain to carry around."
        fn "「Now then,{w=.2} time to get going. 」"
        "After checking over all my stuff,\nI grabbed my bag and left the room."
    
        scene hentry with sdis
        
        fn "「Right, I have to say something\n\ \ to my grandparents before leaving. 」"
        "For staying over at Kouya's place,\nthere are steps I have to follow.{p}So just saying 『I'm heading out!』 should be enough."
        "After thinking that, I stuck my head into\nthe living room from the entry hall."
        "The two of them were together,\nsipping tea as they watched the TV."
        fn "「Grandpa,{w=.2} Grandma.{p}\ \ I'm heading off now. 」"
        gp "「Ah, have fun.{p}Be careful. 」"
        gm "「Oh, that's right, [fn]-chan.{p}\ \ Take some vegetables with you. 」"
        gm "「You're getting a favor,{w=.2}\n\ \ but you're going empty-handed, aren't you? 」"
        fn "「Hmm, that's true.{p}\ \ Then I'll bring them. Because it's been a while. 」"
        gm "「Yes,{w=.2} please do. 」"
        "As she said that, Grandma went over to the kitchen."
        "All the vegetables brought into this house\nwere grown by the neighboring farmers,\nso there were a lot."
        "They're all organically grown, and they're\nvery tasty because the soil is so good."
        "Well, this is a present that's\nmore likely to make Grandma happier than Kouya."
        gp "「That reminds me, did Kouya-kun\n\ \ say anything to you?{w=.2} At all?{p}\ \ Something's strange with his home. 」"
        fn "「I don't remember much,\n\ \ but it should be near the shopping district. 」"
        gp "「Is the route okay? 」"
        fn "「...yeah, he's taking me there. 」"
        "So I said,\nbut now a straythought had entered my mind.\nIt's about the meeting place."
        "It's not near the shopping or\nresidential areas, but at the bus stop."
        "Why would Kouya specifically\ndesignate that as the meeting place?"
        gm "「Okay, [fn]-chan, take these with you. 」"
        fn "「T-thanks,{w=.2} Grandma. 」"
        "While I was thinking about this and that,\nGrandma came back from the kitchen carrying a sack."
        "I took that sack, pushing aside the thought."
        fn "「Okay, I'm heading out now. 」"
        gm "「Be careful now.{p}\ \ Don't be a bother. 」"
        fn "「Yeah, I know. 」"
    
        scene rice with wipeleft
        
        "I said as I carried the sack over my shoulder\nas I headed towards the bus stop."
        "Under the oppressive sunlight,\nI'm in a bit of a cheerful mood."
        stop music fadeout 1.5
        scene bstop with sdis
        show ka 001 at center with dis
        play music o97 fadein 1
        
        ka "「Hey, you're here. 」"
        "Over at the bus stop, Kouya was already there.{p}I hurried on over."
        fn "「Sorry, did I keep you waiting? 」"
        
        show ka 002 with dis
        
        ka "「No, I just got here myself.{p}\ \ All right, ready to go? 」"
        fn "「Ah, yeah... 」"
        
        scene mountain_path with wipeleft
        
        "I followed Kouya as he walked off.\nBut the way he was headed was the opposite\nof the residential area..."
        "Just where were we headed?"
        fn "「Hey, Kouya- 」"
        "Where are we going?"
        "Before I could say another word,\nKouya answered my question."
        
        scene kouya_apartment with wipeleft    
        show ka 001 at center with dis
        
        ka "「We're here. 」"
        "Stopping, Kouya looked at somewhere\nin front of us and pointed."
        fn "「Eh? 」"
        "Over there was an old-fashioned apartment building."
        "It looked like a run-down place from a picture,\ndirty in several places, with a brownish outer wall.{p}Perhaps, because it's made of wood."
        "It doesn't seem like a place anyone would live in,\nand it looked like it could be abandoned."
        "If it were nighttime, it'd be a place\nwhere ghosts and stuff might pop out."
        ka "「Over there,{w} that's my apartment. 」"
        fn "「...what？ 」"
        ka "「I left home as a middle schooler,{w=.2}\n\ \ so I live there by myself. 」"
        fn "「Huh... I didn't know that... 」"
        "It was all so overwhelming\nthat I couldn't say more than that."
        "I seriously wanted to ask\n「Why are you living alone? 」{w=.2}\nAnd stuff like that..."
        
        show ka 002 with dis
        
        ka "「Well, the outside isn't that great,{w=.2}\n\ \ but the inside is pretty nice, you know? 」"
        fn "「Eh, really? 」"
        
        show ka 003 with dis
        
        ka "「Yep, you'll see when we go in.{p}\ \ In the summer it's nice and cool.{p}\ \ In winter, it kinda sucks, though. 」"
        fn "「Yeah, I guessed as much from looking at it. 」"
        "So it's drafty.{p}The wind probably whistles inside.{p}But he says it's pretty nice in there?"
        
        show ka 002 with dis
        
        ka "「That's enough standing around and talking,{w=.2}\n\ \ let's get in already. 」"
        fn "「Yeah. 」"
    
        hide ka with dis
        
        "I picked up my stuff,\nand Kouya and I walked over."
    
        scene bedroom with sdis
        
        fn "「Ah, the outside part of it...\n\ \ is really hanging in there. 」"
        "After opening the well-serviced door,\na one-room living area came into view."
        "And, just like the door,\nit seems like it's been around for a while."
        "The walls on all four sides\ngive off an atmosphere of a long time ago."
        "If it were in Minasato,\nthe interior wouldn't be out of place."
        "Since Kouya said it was pretty nice inside,\nI was expecting something like an apartment\nyou'd see in the city. I'm a little disappointed."
        "Aside from the kitchen visible around the corner,\nit doesn't look that new."
        fn "「So, this is how it is.{w=.2} In reality. 」"
        
        show ka 005 at center with dis
        
        ka "「You think so?\n\ \ I think that the outer wall\n\ \ has been doing pretty well. 」"
        "Kouya sounded a bit dejected."
        "I'm not saying it's sparkling like a new building,\nbut it's not like it's as ruined as it looks outside."
        "'It has its charm,' you could say."
        "As for the falling-apart bit,\nit's about the same as the rest of the village."
        "But because I've been living in the city\nso long, it doesn't meet my own standards."
        fn "「Hmm, maybe my senses are dulled down...\n\ \ Oh, but the kitchen itself looks kind of new.\n\ \ Why's that? 」"
        
        show ka 001 with dis
        
        ka "「I fixed it just after I came here.\n\ \ The kitchen, washroom, the bath, and the plumbing. 」"
        ka "「It was seriously coming apart, so it was\n\ \ going to be a real problem if it was left alone. 」"
        ka "「Thanks to that,\n\ \ it also became the bath area and toilet. 」"
        ka "「That seems to go against the floorplan, though. 」"
        fn "「Well, that's lucky then. 」"
        
        show ka 002 with dis
        
        ka "「Well, I thought if the outside\n\ \ looked good then whatever.{p}\ \ Still, wouldn't a complete remodeling be good? 」"
        fn "「But if that happened, wouldn't the rent go up? 」"
        
        show ka 013 with dis
        
        ka "「I guess. It's because it's so run down that I\nc\ \ an live here...{w} {nw}"
        show ka 001 with dis
        extend " Oh, you can put your stuff\n\ \ over there. I'll get you something to drink. 」"
        fn "「T-thanks. 」"
    
        hide ka with dis
        
        "After saying that, Kouya opened up the\nrefrigerator and began looking for something."
        "I put my luggage into a corner\nso as not to get in the way,\nthen looked over the room again."
        "It's a decidedly cramped one-roomer.\nThere were many things arranged along the walls."
        "From a component stereo to a guitar to magazines,\nand along with whatever's in Kouya's fridge,\nthere's really so much here."
        "But the most surprising part\nis that it's all neatly arranged."
        "None of the magazines are scattered around,\nand all the trash has been\ntaken care of in the kitchen."
        fn "「It really is surprising... 」"
        
        show ka 001 at center with dis
        
        ka "「What is? 」"
        "Kouya responded to my muttering\nas he closed the refrigerator door.\nIn his hand he held two cans of juice."
        ka "「Here. 」"
        "He threw one to me."
        fn "「Whoa-!{w} Thanks. 」"
        "Since he threw it all of a sudden,\nI accidentally dropped it."
        ka "「So, what was so surprising? 」"
        fn "「Oh, I was just thinking how cleaner\n\ \ the room was than I thought it'd be. 」"
        
        show ka 002 with dis
        
        ka "「Ahh, so that's what you mean.{p}\ \ Well, as you can see this room's not that big. 」"
        ka "「If everything were messy,\n\ \ I wouldn't be able to live normally. 」"
        fn "「Huh...{w=.2}\n\ \ so you usually clean up pretty nicely. 」"
        ka "「It's because I live alone, you know. 」"
        fn "「I see then. 」"
        
        show ka 001 with dis
        
        "As I spoke, I took another look around.{p}I noticed something right after that."
        
        play music oo39_cho_ys001 fadein 1.5
        
        fn "「...By the way, over in the stack of magazines,{w=.2}\n\ \ I see it's not sorted numerically. 」"
        fn "「If you look at February's issue,\n\ \ July's on top of it,{w=.2}\n\ \ and even higher up is January's. 」"
        fn "「Why's that? 」"
        
        show ka 005 with dis
        
        ka "「...Umm. 」"
        "Kouya started getting delicately confused."
        "Ooh, could it be 'that'?"
        fn "「If it were sorted normally,\n\ \ it'd generally be in sequential order. 」"
        fn "「Even if you do reread them occassionally,\n\ \ would you slip up like that? 」"
        ka "「...just drink your juice. 」"
        fn "「Hey Kouya...{p}\ \ Could it be that you cleaned up before I got here? 」"
        
        show ka 006 with dis
        
        ka "「It's better to drink it while it's cold.\n\ \ It gets really gross if it's warm. 」"
        fn "「Are you a surprisingly shy person? 」"
        ka "{size=+25}「JUST DRINK UP. 」"
        fn "「'Kay. 」"
        "Kouya waved his juice can in\nirritation from my pointing out."
        "Somehow, that gesture was quite cute.{p}It seems Kouya is more than just a cool surface."
        
        play music o97 fadein 1
        show ka 001 with dis
        
        ka "「...That reminds me, [fn],\n\ \ what's up with that sack? 」"
        "While feigning calmness, Kouya pointed out\nthe sack of vegetables I had brought along with me."
        fn "「Oh, I forgot about those.{p}\ \ Grandma had me bring them over,\n\ \ as a sort of gift.{w} It- 」"
        
        play sound bosu31    
        show ka 002 with dis
        
        ka "「Sorry, looks like I made you\n\ \ make a fuss about stuff. 」"
        "We pulled out the bag,\nthen checked through all the contents.\nI hadn't looked at them until then."
        fn "「Carrots,{w} onions,{w} potatoes... 」"
        "Huh?\nWhere have I heard of this combination before...?"
        
        show ka 005 with dis
        
        ka "「What, aren't these things for that? 」"
        "Seems like Kouya thought the same thing."
        fn "「Yeah,{w=.2} ingredients for curry,{w=.2}\n\ \ no matter how you slice it. 」"
        ka "「Is she saying to use these for curry tonight? 」"
        fn "「No, I don't think that was the idea...{p}\ \ Couldn't it be for meat and potato stew? 」"
        
        show ka 014 with dis
        
        ka "「That's not much of a difference... 」"
        
        show ka 002 with dis
        
        ka "「Whatever, it's all good.{p}\ \ I already have stock and meat,\n\ \ so today it'll be curry. 」"
        ka "「The time's about right too,\n\ \ so I'll start making it now. 」"
        fn "「Oh, I'll help too. 」"
        ka "「You sure?{w=.2} Sorry, I'm counting on you then. 」"
        "With the bag in hand,\nthe two of us went into the kitchen."
        ka "「I don't really need an apron.{p}\ \ You going to use it, [fn]? 」"
        fn "「It doesn't matter to me. 」"
        ka "「Hm, I'll wear it then. 」"
    
        hide ka with wipeleft
        
        "Kouya put the apron on.\nI went right up to his armpits."
        "T-{w=.2}this is-!"
        "I wonder if Kouya bought the green cloth apron\nto match himself?{w=.2}\nIt's a bit bigger than usual."
        "Because of that and with the tanktop he wore,\nthe apron completely hid his shirt,\nand it went down to his feet."
        "It looked like he was wearing a naked apron."
        "As least, that's how I see it.{p}I can totally see it."
        "Wait wait, if I start imagining it\nmy head's gonna get all funny."
        "I-is this how it usually is!?\nNo camera could do this justice!\nIt's for my eyes only!"
        "This is th-that!{p}P-PLEASE ENJOY WITH JUST THE SOUND...!"
        ka "「What's wrong, [fn]?{w=.2} You're spacing out. 」"
        fn "「Eh!?{w=.2}\n\ \ Uh, no, it's just... That's a nice apron... 」"
        ka "「Hm?{w=.2} How so? 」"
        fn "「No, just talking to myself... 」"
        "Unacceptable. Just what am I thinking?{p}Calm down. Calm down, damn it.{p}Get rid of your wicked thoughts."
        "...Right, I'm okay now."
        "But for you, camera,\nthings will stay the same for now."
        fn "「Okay,{w=.2} what should I do? 」"
        ka "「Let's see...{p}\ \ I leave the potato-peeling to you.{w=.2}\n\ \ I'll make a salad. 」"
        fn "「Okay,{w=.2} got it. 」"
        "Just as instructed, I pulled out\nthe potatoes scattered through the bag\nand started skinning."
        "Next to me, Kouya was using lettuce,\ntomatoes, canned tuna and other stuff\nto make a simple salad."
        "It looks like he's used to doing this."
        "...Ah, it's okay now camera.\nThe filter's done preparing."
        
        show ka 001 at center with dis
        
        fn "「Oh yeah,\n\ \ since you live alone you also cook by yourself? 」"
        ka "「Yeah.{w=.2} It's cheaper in the long run\n\ \ if I get better at it, so I make things a lot.{p}\ \ Still, I can only make the simple stuff. 」"
        fn "「Huh, that's also a surprise.{p}\ \ I thought you lived off instant stuff. 」"
        
        show ka 005 with dis
        
        ka "「...Just how do you see me in your mind? 」"
        fn "「If I had to say it...{w=.2} Hmm... 」"
        
        menu:
            "A. Kind of crude.":
                jump kouya20_crude
            "B. Kind of steady.":
                jump kouya20_steady
        
    
    ###################################################
    label kouya20_crude:
        
        $ event_name = "Wild Man"
        
        fn "「Well,{w=.2} I guess it'd be a crude,\n\ \ rough kind of lifestyle. 」"
        
        show ka 001 with dis
        
        ka "「Ahh, people say that to me a lot.{p}\ \ I'm bad at expressing things,\n\ \ so it probably looks that way. 」"
        ka "「I think I should be a bit careful though. 」"
        "As he kept working with his usual skill,\nKouya gave a bitter smile."
        fn "「But I think you're fine as you are right now.{p}\ \ It's just so you. 」"
        
        show ka 005 with dis
        
        ka "「You think?{w=.2} I don't think it's that good. 」"
        fn "「That's not true.{p}\ \ I think you're cool. 」"
        "...Wait, what am I saying all of a sudden?"
        "I got embarrassed after saying it.{p}My face got all hot,\nand I could tell I was blushing."
        
        show ka 006 with dis
        
        ka "「Ah,{w=.2} well...{w=.2} Thanks. 」"
        "Glancing at Kouya, I noticed that\nthe insides of his ears were red for some reason."
        fn "「A{w=.2}-anyway!{p}\ \ I think you're fine as you are right now! 」"
        
        show ka 001 with dis
        
        ka "「I-{w=.2}I see...{p}\ \ Well, I am myself. 」"
        fn "「Y-{w=.2}yeah! 」"
        ka "「Uh-huh... 」"
        fn "「... 」"
        "Needless to say, until the curry was done,\nthe conversation stalled awkwardly."
        
        scene black with sdis

        jump kouya20_dinner
    
    #################################################
    label kouya20_steady:
        
        $ event_name = "Gentleman"
      
        fn "「Hmm, I was thinking you were\n\ \ unexpectedly steady here. 」"
        
        show ka 001 with dis
        
        ka "「What do you mean by 'here'? 」"
        fn "「I mean, it's probably been said,{w=.2}\n\ \ when people describe you, they probably say wild,{w=.2}\n\ \ or a little rough-seeming. 」"
        
        show ka 002 with dis
        
        ka "「Well, that's been said to me a bit.\n\ \ That's the feeling you'd get from my looks, right? 」"
        fn "「But you also have kind points,\n\ \ and I think people around you can see it. 」"
        fn "「When you look at it that way,\n\ \ I thought you seemed steady. 」"
        
        show ka 005 with dis
        
        ka "「I think that'd be a different story though. 」"
        ka "「And saying that straight to my face like that,{w=.2}\n\ \ it's embarrassing. 」"
        "He really does seem embarrassed."
        "Maybe he's really shy?"
        fn "「It's true, though.{p}\ \ You're very kind, Kouya. 」"
        
        show ka 006 with dis
        
        ka "「And I'm saying stop saying that. 」"
        "Kouya's being as shy as can be.{p}That's so cute."
        "Unexpectedly, Kouya does have ways to be teased."
        
        show ka 001 with dis
        
        ka "「Hey, hurry up and get back to peeling.{p}\ \ You stopped moving your hands. 」"
        fn "「Right, right. 」"
        "From now on,\nit'd be fun to poke him once in a while."
        "That's what I was thinking\nin my innermost thoughts."
        
        scene black with sdis
    
    ###################################################
    label kouya20_dinner:
        
        $ event_name = "A Restful Night"
    
        scene bedroom red with sdis
        
        "Dinner preparations\nfinished earlier than I expected."
        "It's still light out, and the clock was barely\npointing at the hour for dinner time,\nbut Kouya and I sat at the dining table."
        fn "「Whew, thanks for the food. 」"
        "After the last mouthful,\nI put my hands together and spoke."
        "Kouya finished eating a moment before I did,\nand he came back from putting away the tableware."
        
        show ka 001 red with dis
        
        ka "「Yeah.{w=.2} Was it good? 」"
        fn "「Yep, very.{p}\ \ You're pretty good at cooking. 」"
        
        show ka 002 red with dis
        
        ka "「I wasn't doing anything complicated.{w=.2}\n\ \ Anyone could make the same thing,\n\ \ with ingredients like that. 」"
        fn "「You think so? 」"
        ka "「Of course. 」"
        fn "「Still, in any case, it was delicious. 」"
        
        show ka 003 red with dis
        
        ka "「That's the most important thing.{p}\ \ Oh,{w=.2} put that in the kitchen,\n\ \ I'll wash it later. 」"
        fn "「No, I can do the dish washing.{p}\ \ You made the curry, but I haven't\n\ \ done anything besides peel potatoes. 」"
        
        show ka 001 red with dis
        
        ka "「...You sure?{w} I'll leave it to you, then.{w=.2}\n\ \ I'll get the bath ready. 」"
        fn "「Oh, okay.{w=.2} We'll split it like that. 」"
        
        show ka 002 red with dis
        
        ka "「Wanna go in together? 」"
        fn "「Ye-{w=.2}...eEEH!? 」"
        "That was close! I almost said 'yeah' automatically!"
        "No, it's fine though!{w} Totally fine, right!?{p}But is that really the thing to do...?{w=.2}\nI mean, it's only a step away from that, right!?"
        fn "「Uh... Really? 」"
        
        show ka 001 red with dis
        
        ka "「Nope,{w=.2} kidding. 」"
        "...Of course it is."
        fn "「...Anyway, I'll go wash up. 」"
        
        show ka 002 red with dis
        
        ka "「Right, I'm counting on you. 」"
    
        hide ka with dis
        
        "I stood up, carried everything to the kitchen,\nand picked up a sponge."
    
        play sound shower
        
        fn "「Now,{w=.2} I'll clean ya right up. 」"
        "Usually, I don't do this at home.{p}I thought I was bad at this."
        "However, even a grade-schooler can wash dishes.{p}If I washed them, they'd definitely be clean."
        "After a few minutes, both our dishes were clean\nand sparkling, lined up in the dishrack."
        fn "「Whew,{w=.2} I can do it too, if I try. 」"
        
        show ka 001 red at center with dis
        
        ka "「Yeah, but even grade-schoolers can wash dishes. 」"
        "I jumped as Kouya whispered into my ear.\nWhen did he get behind me...?"
        fn "「...Hey, could you not bring me\n\ \ down to Earth so hard?{p}\ \ It hurts my mind. 」"
        ka "「My bad. 」"
        fn "「So, how's the bath? 」"
        ka "「The bathtub will be full in about 10 minutes. 」"
        ka "「It was being used for laundry earlier,{w=.2}\n\ \ since that's where the hot water's put. 」"
        fn "「I see. 」"
        
        show ka 002 red with dis
        
        ka "「Anyway, watch TV and make yourself at home.\n\ \ There's still plenty to talk about. 」"
        
        hide ka with dis
        
        "After saying that and ruffling my hair,\nKouya went back into the living room."
        "I left the kitchen a little after that."
        fn "「...I've been gone\n\ \ from Minasato for so many years. 」"
        "I can still remember the time when we moved."
        
        stop music fadeout 1.5
        scene white with sdis
        play music melodious05 fadein 1
        
        "I was in front of my house."
        "Everyone got together,\nand we said out last goodbyes."
        "Everyone was making sad and lonely looking faces,\nbut I still laughed in the midst of all that."
        fn "「It's okay,{w=.2} we'll meet again. 」"
        "I laughed loud and clear."
        "But really, I actually hated\nbeing separated from everyone."
        "I was always saying 'we'll meet again.'{p}Because if, just if,{p}we really couldn't meet, I'd be scared."
        "But, I still knew that if I cried\nI'd make them all even sadder."
        "So I held it in."
        "And then after I got in the car and we left..."
        fn "「U...waaah... 」"
        "I cried my heart out."
        
        scene bedroom red
        show ka 001 red at center 
        with sdis
        
        fn "「I saw it that time,{w=.2}\n\ \ the last time I saw the\n\ \ scenery of Minasato Village but... 」"
        fn "「When I came back and looked around,\n\ \ somehow, I can see a bunch of things have changed. 」"
        
        show ka 014 red with dis
        
        ka "「That so?{p}\ \ For me, I can't see anything\n\ \ but the countryside back then and now. 」"
        "Kouya raised an eyebrow in doubt.{p}Like he was saying\n'just what changed around here, then?'"
        fn "「There are still a lot of things\n\ \ around that haven't changed.{p}\ \ But there really has been change. 」"
        fn "「It's the same for the village's mood,{w=.2}\n\ \ but more than that... 」"
        fn "「More than that,{w=.2} it feels like everyone changed. 」"
        "I looked straight at Kouya and spoke."
        "It's an obvious thing,\nbut I still thought it was something important."
        "It's just disappointing that I wasn't here for it."
        
        show ka 001 red with dis
        
        ka "「[fn]... 」"
        "Kouya noticed my feelings,\nand spoke my name softly."
        fn "「But you changed the most.\n\ \ I was surprised to see you live alone. 」"
        
        show ka 002 red with dis
        
        ka "「I guess. 」"
        fn "「Oh, that reminds me,{w=.2} why did you start living\n\ \ alone?{w} Isn't it{w=.2} kind of far from home?{p}\ \ Or, did you move? 」"
        "My words disappeared into the air."
        "Kouya smiled bitterly at my questions."
        
        show ka 013 red with dis
        
        ka "「Ahh... No,{w=.2} I ran away from home.{p}\ \ I had a fight with my father,{w=.2}\n\ \ around the time I was going into high school. 」"
        ka "「Since we had a fight,{w=.2}\n\ \ I was thinking of living in Kazenari,{w=.2}\n\ \ but I could only afford the rent here. 」"
        ka "「Different people kept helping me out,\n\ \ and I somehow ended up here. 」"
        "Just like that,{w=.2} he told me the shocking truth."
        "I was so surprised,\nI couldn't get my voice to work."
        
        show ka 005 red with dis
        
        ka "「Hey, come on,{w=.2} you don't need to be\n\ \ that speechless. 」"
        fn "「No,{w=.2} but... 」"
        "I only recovered a little\nas those helpless words poked out of my mouth."
        "The inside of my head was all hazy,{w=.2}\nand I couldn't really put thoughts together."
        
        show ka 001 red with dis
        
        ka "「...Sorry for keeping quiet about it.{p}\ \ I was trying not to put you into a weird mood,{w=.2}\n\ \ but it looks like I got the opposite result. 」"
        fn "「Kouya... 」"
        "What should I say?{p}Should I call out to him?{p}I can't find any good words to use."
        "What can I say to him?"
        "I have no idea."
        
        show ka 003 red with dis
        
        ka "「Come on, let's stop with the gloomy talk.{p}\ \ You don't really like it,{w=.2} do you?{p}\ \ The bath should be ready, so you go in first. 」"
        "There were so many things I should have said,{p}but when the time came,"
        fn "「Okay... 」"
        "I couldn't do anything but bow my head."

        jump end20

    
#######################################################
label shin20:
    
    $ event_name = "Shin-kun and Amaki-san"
    
    play music piano3_015
    $ renpy.music.set_volume(0.8, 0.0, channel = "music")
    scene shin_house_front with dis
    pause 1
    
    play sound tm2_chime002
    pause 2
    play sound tm2_chair003
    pause 1
    
    show si 001 at center with dis
    
    si "「Hey, welcome. 」"
    fn "「Afternoon! 」"
    "I've gotten used to pressing the door bell,\nShin-kun showed up before long,\nwe exchanged greetings, and then we went in."
    "I've called up in advance,\nbut we've gotten used to this\ncountless back-and-forth."
    fn "「Alright, I'll be in your care today too. 」"
    
    stop music fadeout 1
    scene black with sdis
    
    if shin_lesson == True:
        jump shin20_baking
    else:
        jump shin20_homework

    ########################################################
    label shin20_baking:
        
        play music daily02
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
    
        scene shin_house_kitchen with dis    
        show si 001 at center with dis
        
        si "「I was thinking of teaching you\n\ \ how to make a pound cake today... 」"
        fn "「Yes chef. 」"
        
        show si 010 with dis
        
        si "「Don't confuse sugar with salt. 」"
        fn "「Understood, {w=.2}chef. 」"
        
        show si 003 with dis
        
        si "「Would you stop calling me chef? 」"
        fn "「Uu...{w} sorry Shin-kun. 」"
        "I guess last time's blunder still has an effect.{p}So I tried to smooth over the atmosphere\nby forcing a smile onto my face."
        "Last time we made cookies,{w=.2}\nbut I carelessly put in salt instead of sugar\nso when we tasted them after, it was a disaster."
        
        show si 010 with dis
        
        si "「Last time,{w=.2}\n\ \ I wasn't ever expecting to taste\n\ \ a cookie that salty. 」"
        fn "「But they were right next to each other! 」"
        
        show si 001 with dis
        
        si "「Shouldn't you be able to tell\n\ \ when you opened the lid? 」"
        si "「The granules are different,\n\ \ and salt smells differently. 」"
        "I'm so sorry. I understand now."
        fn "「I'm really sorry.{p}I'll check the label from now on. 」"
        
        show si 010 with dis
        
        si "「...I'm not that mad at you. 」"
        "So he says, but I can't forget\nShin-kun's cold look from then."
        "Whenever we're eating confections, Shin-kun\nusually is in a good mood,{w=.2} but last time,\nhe had the eyes of a predator catching its prey."
        "He was smiling though.{p}Not that any of it reached his eyes.{p}That day, I was constantly in a cold sweat."
        "Today, I can't make a mistake that big."
        
        show si 001 with dis
        
        si "「Now let's start with the ingredients and... 」"
        
        scene black with wipe_right
        scene shin_house_kitchen with wipe_right       
        show si 001 at center with dis
        
        si "「Now we just need to bake it in the oven.{p}\ \ Temperature should be 170-180 degrees\n\ \ for about 30 minutes. 」"
        
        show si 004 with dis
        
        si "「You should really keep watch as it bakes,\n\ \ but if you do it too much you'll lose everything. 」"
        si "「If you arrange things as the recipe says,\n\ \ it should be fine. 」"
        fn "「Okay, got it. 」"
        
        show si 001 with dis
        
        si "「There aren't any so-called tricks,\n\ \ but make sure you don't mix the dough too much\n\ \ or the texture goes bad. 」"
        si "「Same goes for the baking. 」"
        si "「If it's half-baked you can still fix it,\n\ \ but nothing can be done if it's burnt. 」"
        fn "「Mhmm, that's true. 」"
        
        show si 002 with dis
        show am 001 at offleft_far
        
        si "「Now then, what should we do until it's done? 」"
        "As he spoke, Shin-kun set\nthe timer on a stopwatch."
        "I can relax knowing\nwe can keep time away from the oven."
        "Let's see...{w} I still don't know the rules to chess,{w=.2}\n(and Shin-kun doesn't go easy on beginners)\nso cards might be safe."
    
        show am at move_farleft(1)
        
        am "「Shin-kun, a moment? 」"
        fn "「Wah-! 」"
        
        show si 001 with dis
        
        si "「Oh, Amaki. {w=.2}What is it? 」"
        "Amaki-san suddenly appeared behind me.{p}H-he's as undetectable as ever."
        "I'm not used to--{w=.2} wait I am,\nbut it's still a surprise."
        am "「I have some things to do,\n\ \ so can I ask you to watch the house?{p}\ \ Maybe I can ask you too [ln]-kun? 」"
        fn "「Oh, okay. 」"
        
        show si 010 with dis
        
        si "「I don't mind, but don't refer to it as\n\ \ 'watching the house.' 」"
        
        show am 002 with dis
        
        am "「Oh yes,{w} sorry about that.{w=.2}\n\ \ I won't. 」"
        
        show si 001 with dis
        
        si "「Geez... 」"
        "Shin-kun had a much gentler expression\non his face than usual when he said that.{p}I wonder.{w} It's such a strange feeling."
        "It's like there's a Shin-kun I don't know there,{w=.2}\nand somehow,{w=.2} I feel so sad."
        
        show am 001 with dis
        
        am "「Now then, I'll be going. 」"
        
        show si 004 with dis
        
        si "「Yes, yes. Take care. 」"
    
        hide am with dis
        play sound DoorCloseB
        pause 1
        
        "That person who has no reason to know my feelings\ninformed us of such with a smile, then left."
        fn "「I don't really get the feeling\n\ \ Amaki-san is a servant. 」"
        
        show si 001 with dis
        
        si "「Is that so? 」"
        fn "「I figure servants are supposed to be more humble,\n\ \ and that he'd be all {w=.2}'Young Master,\n\ \ I shall be leaving on business' and stuff. 」"
        "I pretended to be a servant, bowing my head\nin reverence and changing my voice."
        
        show si 003 with dis
        
        si "「Oh, Amaki does that too at times.{p}\ \ It always sounds like he's making fun of me,\n\ \ so I told him to stop. 」"
        fn "「Really? 」"
        
        show si 001 with dis
        
        si "「Up until now he's always felt like that.{p}\ \ Even now we look like master and servant,\n\ \ but it's actually kind of awkward,{w=.2} uncomfortable. 」"
        fn "「Huuuh. 」"
        "He can say {w=.2}'that's it,'\nbut I can see them as being something closer.{p}Is this a special 'bond'?"
        "It's kind of...{w} vexing."
    
        scene black with wipe_right    
        stop music fadeout 1
        pause 1
        scene shin_bedroom with wipeleft
        show si 001 at center with dis
        play music daily03
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        
        fn "「It's my turn now, right? 」"
        si "「Yes. {w=.2}Make whatever move you like. 」"
        fn "「I'll do just that then. 」"
        "I showed my hand, smiling self-confidently.{p}10 of Hearts, 10 of Spades,\nthen the Kings of Club, Diamond, and Hearts."
        fn "「Full House. 」"
        
        show si 004 with dis
        
        si "「Four of a Kind. 」"
        fn "「What!? 」"
        "I just declared victory,\nbut Shin-kun turned my confidence\nto shock with one quiet phrase."
        "Shin-kun's hand was the Ace of Spade, Diamond,\nClub, a Joker, and the Jack of Spade."
        fn "「I lost again! 」"
        
        show si 002 with dis
        
        si "「I picked up the Joker when I had Three of a Kind.{p}\ \ I thought that was enough,\n\ \ but I'm glad I got another Ace. 」"
        fn "「Seriously...?{p}\ \ I already had a pretty good hand. 」"
        "I thought I had won when I changed out\nand got the pair of kings."
        fn "「You're too good Shin-kun. 」"
        
        show si 001 with dis
        
        si "「It was just luck.{p}\ \ I'd have lost if I didn't get an ace. 」"
        fn "「But hasn't every session\n\ \ ended with more wins to you? 」"
        si "「Who can say?{p}\ \ I can't since I don't remember.{p}\ \ {nw}"
        show si 002 with dis
        extend "Another round? 」"
    
        play sound timer
        
        fn "「Of course. 」"    
        "The stop watch started beeping\nat the same time I answered.{p}It looks like the cake is done baking."
        
        show si 001 with dis
        
        si "「We'll continue after cutting the cake. 」"
        fn "「Okay. 」"
        
        show si 002 with dis
        
        si "「Today we're actually having something sweet.\n\ \ I'm looking forward to it. 」"
        fn "「Are you ever going to let that go? 」"
        si "「Hmhm. 」"
        "Shin-kun had a teasing smile on his face\nas he headed to the kitchen.{p}I ran after him a moment later."
    
        scene shin_house_kitchen with wipeleft
        
        "A few minutes later, there was a beautifully\ncut cake on a plate,{w} and a collapsed, uneven,\nbadly cut cake on another plate."
        "How could they be so different yet\ncut the exact same way...?"
        
        show si 001 at center with dis
        
        si "「Now then.{w=.2} Amaki, the tea...{p}\ \ {nw}"
        show si 003 with dis
        extend "Amaki went out didn't he?{p}\ \ {nw}"
        show si 001 with dis
        extend "Oh well. 」"
        "Shin-kun pulled out\nsome tea leaves from the shelves."
        fn "「Oh,{w=.2} is Amaki-san in charge of the tea? 」"
        si "「Somewhat.{p}\ \ I can brew it too, but the scent is\n\ \ different when Amaki brews it. 」"
        fn "「Huh. 」"
        si "「He used the cookies from before\n\ \ and some other ingredients for cooking. 」"
        si "「I'm the one saying it and all,{w=.2}\n\ \ but Amaki is amazing. 」"
        "For Shin-kun to be praising anyone like this,\nhe must be super amazing."
        
        show si 002 with dis
        
        si "「If it comes to sweets,\n\ \ I won't make anything that loses in taste though. 」"
        "Shin-kun seemed to be done making the tea,\nand now he was holding up the plate\nwith the cake I cut."
        fn "「Oh, that one's mine. 」"
        
        show si 001 with dis
        
        si "「Didn't you cut it just for me? 」"
        fn "「Eh? 」"
        
        show si 002 with dis
        
        si "「I'm kidding.{p}\ \ {nw}"
        show si 001 with dis
        extend "But if you were thinking of giving this to someone,\n\ \ don't you feel you should get better at making it? 」"
        fn "「I-I guess so. 」"
        
        show si 002 with dis
        
        si "「Well, I'm going to eat now then.{p}\ \ Next time you cut this cake,\n\ \ cut it with a bit more control, yes? 」"
        fn "「I was already trying so hard\n\ \ to cut it so delicately... 」"
        si "「Hmhmhm... 」"
        
        pause .5
        
        show si 001 with dis
        
        si "「... 」"
        
        show si 009 with dis
        
        si "(This isn't good.{p}\ \ Seems like I start acting spoiled when I'm with you.)"
        fn "「What's wrong? 」"
        
        show si 001 with dis
        
        si "「Oh, yes.{w=.2} Sorry.{p}\ \ I was just thinking about things. 」"
        "What was that?{p}For a second I thought I saw a really sad\nexpression on Shin-kun...{w=.2} did I see things?"
        
        show si 002 with dis
        
        si "「So then, how about we continue our game\n\ \ while eating the cake? 」"
        "Shin-kun was smiling in a good mood\nas he left the kitchen.{p}Maybe I really was just seeing things."
    
        jump end20
    
    #######################################################
    label shin20_homework:
        
        stop music fadeout 1
        play music free51
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
    
        scene shin_bedroom with wipeleft
        show si 001 at center with dis
        
        fn "「Uhh... 」"
        si "「Mark it over there,\n\ \ then translate just the earlier part. 」"
        fn "「Uh, 'I gave my special candy'? 」"
        si "「Now try translating up to the next point. 」"
        fn "「Umm, 'it was a very sweet cream'? 」"
        si "「That sentence is related to candy. 」"
        fn "「'A very sweet, creamy, special candy'? 」"
        si "「Correct.{p}\ \ Now, what's left is about the receiving party. 」"
        fn "「Because they were... my grandchild...\n\ \ oh, I see! 」"
        "Right, I feel like I got it."
        "The pronunciation and all...{p}I'm learning like a native speaker,\nso I feel like I can really study!"
        "...I was told almost all of it though."
        si "「Is English at about this level? 」"
        fn "「Yeah.{w} \ \ After is math and history and... 」"
        
        show si 010 with dis
        
        si "「...I said I'd teach you,\n\ \ but do you even intend to do anything yourself? 」"
        fn "「S-sorry. 」"
        "Shin-kun stared at me as\nI apologized reflexively again."
        
        show si 001 with dis
        
        si "「I don't mind,{w=.2}\n\ \ but you need to use your own ability\n\ \ and not always rely on others. 」"
        "Still, he really does properly teach me\nwith anything.{w=.2} Shin-kun's complained once,\nbut most of the time he was okay with things."
        "Maybe that's his kindness?{p}Isn't that what people call tsundere?{p}Is he a tsundere!?"
        
        show si 010 with dis
        
        si "「What are you smiling about? 」"
        fn "「Uweh? 」"
        
        show si 004 with dis
        
        si "「Oh please.{p}\ \ Your concentration seems to be going,\n\ \ so how about we take a break? 」"
        fn "「Oh, really?{w} Yay! 」"
        
        show si 010 with dis
        
        si "「Seriously now,\n\ \ you really haven't changed at all have you? 」"
        
        show si 001 with dis
        
        si "「You didn't really just come here hoping\n\ \ for confections and air conditioning, did you? 」"
        fn "「T-that isn't true. 」"
        
        show si 002 with dis
        
        si "「So it'd be fine if we skipped tea time today? 」"
        fn "「What!? 」"
        si "「I'm kidding.{p}\ \ {nw}"
        show si 001 with dis
        extend "For me, I'm grateful to hear\n\ \ people's thoughts about what I've made. 」"
        "Shin-kun's mouth moved\ninto the shape of a smile as he stood up."
        
        show si 002 with dis
        
        si "「Now would you mind waiting a bit?{p}\ \ Today I've made pudding. 」"
        fn "「Ooohh. 」"
        "So there's pudding today.{p}He really can make anything."
        "Every time I've come here, Shin-kun's now\ncustomary handmade confections\nall have been store-quality."
        "The deliciousness is a natural thing,{w=.2}\nthe presentation is good,{w=.2}\nand the repertoire seems to be fairly big."
        "He really could become a patissier."
        "But every time I suggest that,\nhe always tells me{w=.2}\n\"it's not something I can sell.\""
        "It's true that I think it'd be tough to turn\na hobby into a job, but I also think\nit'd be a waste of talent."
        
        play sound Door03Open
        pause 2
        show am 001 at farleft with dis
        
        am "「Oh. 」"
        
        show si 001 with dis
        
        si "「Ah, Amaki. What do you want? 」"
        fn "「P-please excuse the intrusion. 」"
        "As Shin-kun was leaving the room\nhe bumped into Amaki-san who was coming in."
        
        show am 002 with dis
        
        am "「Welcome.{p}\ \ How are things progressing? 」"
        fn "「Well, little by little. 」"
        am "「That's good then. 」"
        "Amaki-san kept speaking with that bright smile on his face."
        
        show am 001 with dis
        
        am "「I have to leave for a bit,\n\ \ but can I ask you to take care of things? 」"
        si "「Okay.{p}\ \ Will you be gone long? 」"
        am "「Who can say?{p}\ \ I'll try to get back as soon as I can.{p}\ \ {nw}"
        show am 002 with dis
        extend "Getting lonely? 」"
        
        show si 010 with dis
        
        si "「...{w} Amaki,{w=.2} you do know how old I am don't you? 」"
        am "「Sorry, sorry.{w} I know, and I'll be back, {w=.2}okay?{p}\ \ {nw}"
        show am 001 with dis
        extend "Well then, I'm going now. 」 "
        si "「Take care. 」"
        "..."
        
        scene black with sdis
        scene shin_bedroom with dis
        show si 001 at center with dis
        
        fn "「You know,\n\ \ I don't really get the feeling\n\ \ Amaki-san is a servant. 」"
        "I spoke as I brought\nShin-kun's handmade pudding to my mouth."
        "Mmmmmm,{w=.2}\nit tastes different from a supermarket's pudding,\na gentle, nostalgic sweetness that is unique."
        si "「Is that so? 」"
        fn "「Yeah.{p}\ \ More like,{w=.2} an older brother or something. 」"
        
        show si 004 with dis
        
        si "「I see. 」"
        "Then Shin-kun continued eating his pudding."
        
        show si 001 with dis
        
        si "「I really did refer to him as my brother\n\ \ a long time ago. 」"
        fn "「Eh? Really? 」"
        si "「I was still in kindergarten at the time.\n\ \ When he told me to call him by name,\n\ \ that was when I started calling him 'Amaki.' 」"
        fn "「I see then.{w=.2} Huh... 」"
        "A childhood Shin-kun being held by Amaki-san\nwhile calling him 'big brother'...{p}S-such destructive power!"
        
        show si 010 with dis
        
        si "「In any case I haven't\n\ \ lost my image from that time.{p}\ \ I was treated like a kid in every possible way. 」"
        
        show si 001 with dis
        
        si "「I'm this old already, so there's no need for\n\ \ 'getting lonely?', is there? 」"
        fn "「Haha, I suppose so. 」"
        "Amaki-san is probably the only one\nwho can say that to Shin-kun."
        "When I remembered Shin-kun's face earlier,\nhis mouth's corners relaxed a bit."
        
        show si 010 with dis
        
        si "「Although, {w=.2}you could say he's more like\n\ \ my family than my actual family... 」"
        
        stop music fadeout 1.5
        
        fn "「?{w=.2} What do you mean? 」"
        
        play music piano4_001
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        
        show si 001 with dis
        
        si "「Have you ever seen my parents? 」"
        "Now that he mentions it...{p}I have no memories of his mom or dad."
        fn "「...I don't think so. 」"
        si "「This village is inconveniently\n\ \ accessible after all. 」"
        si "「I hardly ever see them.{p}\ \ {nw}"
        show si 009 with dis
        extend "They're busy people. 」"
        
        show si 001 with dis
        
        si "「Because of that, I've spent more time\n\ \ with Amaki than I have with my own parents.{p}\ \ So now, Amaki is more like my real family. 」"
        
        show si 004 with dis
        
        si "「Oh, don't take it the wrong way.{p}\ \ It's just that my circumstances are different,\n\ \ {w=.2}that's all. 」"
        
        show si 001 with dis
        
        si "「Even after coming to live here,\n\ \ it's necessary for my health. 」"
        
        show si 009 with dis
        
        si "「And also,{w=.2} having more general contact\n\ \ with people makes me feel better than\n\ \ being looked at like I'm pitiable. 」"
        "Shin-kun's spoon hit down with a clatter.{p}Whatever feelings were on the other side\nof those quiet words, I couldn't tell."
        
        show si 002 with dis
        
        si "「That's why you, the people in this village,\n\ \ and the people who can talk to me calmly\n\ \ make me happy despite the annoying moments. 」"
        si "「Until I came to this village,\n\ \ I think I've hardly ever talked with{w=.2}\n\ \ anyone like this. 」"
        "The smile on his face was so gentle,\nso very transient."
        "If I had to say one thing about this decent speech\nit'd be cool, {w=.2}but all I could really do was stare\nat his face as it looked the same as ever."
        
        show si 001 with dis
        
        si "「What's wrong? 」"
        
        stop music fadeout 1
        pause 1
        play music piano3_015
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        
        "I spaced out for a moment,\nand Shin-kun asked me that."
        fn "「Oh, nothing. 」"
        
        show si 009 with dis
        
        si "「Does it not suit your tastes?{p}\ \ Maybe a little less sweetness? 」"
        fn "「Oh uh, I was just thinking about things.{p}\ \ This is really amazing,\n\ \ and I think the sweetness is just right. 」"
        
        show si 001 with dis
        
        si "「Is that so?{p}\ \ That's fine then if it is. 」"
        fn "「Yeah,{w} it's really good. 」"
        "As I took the last mouthful,\nI said it one more time.{p}Nothing better came to mind though."
        
        jump end20
    
#######################################################
label end20:
    stop music fadeout 3
    stop sound fadeout 3
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

    jump day21



