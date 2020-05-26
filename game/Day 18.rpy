###Day 18
screen shrine18:
    hbox:
        add "arrow up"
        at shrinebounce1
    hbox:
        add "icon_shun"
        at shrinebounce2
    hbox:
        text _("Minasato Shrine")
        xalign .16 yalign .12

screen minasatomap18:
    add "map"
    add "mapdate"
    imagebutton idle "a icon" hover "icon loop" xpos 164 ypos 104 action Jump("shun18") hovered Show("shrine18")  unhovered Hide("shrine18") hover_sound "av/audio/click_008.wav" 
    hbox:
        text _("{size=+30}August 18")
        at maptime

################################################
label day18:
    
    $ renpy.music.set_volume(1.0, 0.0, channel = "music")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound2")
    
    $ day = 18
    $ the_date = _("August 18")
    $ event_name = _("８月18日")
    
    if favorite == "shun":        
        window hide
        play music birds_chirping
        
        scene sky01 
        show text "{size=+130}August 18" at truecenter
        with Dissolve(.5)
    
        pause 3
        scene black with Dissolve(1)
        pause .4
    else:
        jump day19
        
    if favorite == "shun":
        jump map18
    else:
        $ renpy.jump (favorite + "18")
    
#################################################
label map18:
    scene hbroom with wipe_corner
    pause .2
    fn "「What should I do today? 」"
    play music "<from 2.5>av/audio/free0422.ogg"
    call screen minasatomap18
#################################################
label shun18:
    
    $ event_name = _("The Strongest Weapon and Shin")

    scene map
    hide screen shrine18
    stop music fadeout 1.5
    scene black with sdis  
    scene shrine 
    show over black 
    with sdis
    $ renpy.music.set_volume(0.7, 0.0, channel = "sound")
    play sound kara00
    pause 2
    show su 010 at center with dis    
    play music free58
    $ renpy.music.set_volume(0.8, 0.0, channel = "music")
    
    su "「Uu...Unyuu... 」"
    "Aah.{p}It feels like this happened just the other day.{p}The only thing different from that time,{w} {nw}"    
    show su at move_midleft(0.5)
    extend "{w=.5}{nw}"
    show si 001 at midright with sdis
    
    "is that there are two people in front of me.{p}It wasn't me that made Shun-kun cry, but Shin-kun?"
    
    stop music fadeout 1
    pause 1
    scene black with sdis
    
    $ event_name = _("Legend of the Sky Dragon King")

    scene path 
    show over black 
    with sdis
    play music daily05 fadein 1
    $ renpy.music.set_volume(0.8, 0.0, channel = "music")
    
    "For the first time in a while, the cloudy sky,\ncombined with a pleasant and gentle breeze,\ndrives away the usually feverish atmosphere."
    "To be honest, I have been wanting a break from\nthe summer template of a blue sky and shining sun."
    "My shirt isn't sticking to my skin this morning!{p}That's great!"
    "And in my field of vision is..."

    show su tailwag 01 at midleft with dis
    
    su "「Yaay, yaay, yaay. 」"
    "Boing boing boing, Shun-kun\nhops on the ground with both feet, and,"

    show si 002 at midright with dis
    
    si "「Hey, you're going to fall over\n\ \ frolicking around like that. 」"
    "Judging from his tone of voice,\nhe's not intending on strongly chiding him.{p}Shin-kun calmly laughs."
    "It's a charming scene of summer vacation.{p}Today I'm being escorted to Minasato's shrine\nby Shun-kun."
    "We happened to meet Shin-kun along the way,{p}and he joined us."
    "At first I was worried whether or not\nhe would be interested, but he unexpectedly\ncame along when I invited him."
    "According to Shin-kun, it's because he doesn't{p}have to worry about getting sunburned."
    su "「Dragon God, prepare your moustache♪ 」"
    "The happy wolf wags his tail and sings a song."
    su "「Before he goes out, he gets dressed♪ 」"
    fn "「Moustache? 」"
    
    show su 001 with dis
    
    su "「Yes, he can't fly very well if his moustache\n\ \ is bent because it doesn't look good. 」"
    
    show su 002 with dis
    
    su "「That's why it's cloudy today. 」"
    fn "「??? 」"
    "I-It's no good. I can't understand\na word he's saying."
    "I sheepishly turn to my side\nto get help from Shin-kun."
    
    show si 004 with dis
    
    "He probably guessed why I'm confused.{p}After blinking with surprise for a moment,{p}Shin-kun slowly explains."
    
    show si 001 with dis
    
    si "「It's because it's standard for gods\n\ \ to be above the sky. 」"
    su "「That's right! So when they get dressed\n\ \ or take a bath, they make a curtain of\n\ \ clouds because they're embarrassed. 」"
    "Oh, I see."
    "When you open the lid, it's like a phrase\nfrom a picture book or children's song.{p}Shun-kun happily talks with big, round eyes."
    "Is Shun-kun really around the same age as us?{p}I'm starting to worry about him a little."
    
    show si 002 with dis
    
    si "「Shun-kun's songs always have profound meanings,\n\ \ don't they? 」"
    
    show su 004 with dis
    
    su "「Really? Funyuu. 」"
    "It's simple and pure when you say it like that.{p}Take it the wrong way, and it's an old-fashioned\ncountry thing."
    "The legends of Minasato have taken root in Shun-kun\nwhile I have been stained by urban living.{p}It's a soft, heartwarming fantasy."
    
    scene black with wipeleft

    $ event_name = _("Legend of the River Dragon King")

    scene rice 
    show over black 
    with wipeleft
    
    "We trudge along the riverside."
    "Fresh water from the mountains flows into this\nvillage, branches as it goes downstream, and\ndelivers moisture to all corners of the land."
    "Nevertheless, the water here is amazingly clear.\nIf I look closely I can see fish swimming around."
    
    show si 001 at center with dis
    
    si "「What's the matter?\n\ \ Why are you staring like that? 」"
    fn "「Oh, uh, I was thinking\n\ \ about how clear the river water is. 」"
    
    show si 002 with dis
    
    si "「Is that strange? 」"
    fn "「Really, it's so clean I could swim in it. 」"
    
    show si 004 with dis
    
    si "「...I see. 」"
    "He looks away in disintrest.{p}Ah, was this not a good topic?{w} {nw}"    
    show si 001 with dis
    show si at move_midright(0.5)
    extend "{w=.5}{nw}"    
    show su 001 at midleft with dis
    
    su "「This whole river is the Dragon King's pathway. 」"
    fn "「Huh? 」"
    "Once again, Shun-kun teaches us\nabout Minasato's legends."
    su "「He swims in the river and always patrols\n\ \ the fields and rice paddies. 」"
    fn "「Hmm. 」"
    
    show su 002 with dis
    
    su "「That's why there was a good harvest last year. 」"
    fn "「I see, the Dragon King sure is great,\n\ \ isn't he? 」"

    show su tailwag 01 with dis
    
    su "「Yep!\n\ \ Ehehe. 」"
    
    "Shun-kun is quite pleased\nat being praised for what he said."
    "On the other hand, next to me\n{nw}"
    show si 004 with dis
    extend "Shin-kun opens his mouth to speak{p}about what doesn't make sense."
    
    show si 001 with dis

    si "「Even on a cloudy day like today? 」"
    
    show su 001 with dis
    
    su "「What? 」"
    si "「Doesn't he get dressed on cloudy days? 」"
    su "「Yes! 」"
    si "「If that's the case, to say he is\n\"always\" patrolling is wrong. 」"
    
    show su 003 at shivering with dis
    pause .2
    
    su "「W-woof. 」"
    "Shun-kun is bewildered by what Shin-kun\naccurately pointed out.{w} A pushyuu sound\ncomes from his head out of confusion."
    "His head is likely to overheat if this continues.\nShin-kun does have a valid point, but it's just\na simple legend. He should let it slide."
    fn "「H-Hey Shun-kun and Shin-kun!{p}\ \ We're almost there, so shouldn't we get going? 」"
    "I press both of them on."
    
    show si 004 with dis
    
    si "「...I see.{p}\ \ You're siding with Shun-kun, aren't you? 」"
    fn "「Huh? 」"
    "Shin-kun mutters in a delicate voice,\nI can barely hear him from where I'm standing."
    
    show si 001 with dis
    
    si "「Alright then, shall we go?{p}\ \ Watch your step, Shun-kun. 」"
    
    show su 004 at still with dis
    
    su "「O-okay... 」"
    scene black with wipeleft 
  
    $ event_name = _("Which One is an Ally?")

    scene shrine 
    show over black
    with wipeleft
    show su 001 at midleft
    show si 001 at midright
    with wipe_up
    
    "After climbing the stone stairs, the three of us\nline up and put our hands together."
    "The god of dragons is revered at Minasato's shrine.\nThe dragon king Shun-kun spoke of earlier."
    fn "「By the way, what are you praying for? 」"
    
    show su 002 with dis
    
    su "「Hehee, it's a secret. 」"
    fn "「Oh, well I'll pray that you'll tell me\n\ \ what you're praying for. 」"

    show su 005 at jump_up
    pause .2
    
    su "「Ah, that's cheating! 」"
    
    show su 003 at bobbing
    pause .2
    
    su "「The dragon king is very powerful.{p}\ \ If you do that, I definitely won't be able\n\ \ to keep it a secret... 」"
    "He seems really impatient.{p}Back when I was a kid in Minasato,\nwas the dragon king's power this great?"
    fn "「Alright then, I'll stop.{p}\ \ I guess I'll pray for your healthy growth. 」"
    
    show su 002 at midleft with dis
    
    su "「Okay! Thank you very much! 」"
    fn "「What about you, Shin-kun?{p}\ \ What are you praying for? 」"
    
    show si 001 with dis
    
    si "「\"If he lives in this shrine, will he show\n\ \ himself to us?\",{w} is what I'm praying for. 」"
    
    show su 004 with dis
    
    su "「What? 」"
    
    show si 004 with dis
    
    si "「And the dragon king hasn't appeared.{p}\ \ This proves that he, in fact, does not live here. 」"
    "I-Is Shin-kun some kind of malicious character?"
    
    stop music fadeout 1
    play music free27 fadein 1
    $ renpy.music.set_volume(0.8, 0.0, channel = "music")
    pause 2
    
    su "「... 」"
    
    show si 001 with dis
    
    si "「For example, 」"
    "Shin-kun continues talking.{p}Ooh, it's gotten somewhat aggressive, or rather\nthe peaceful atmosphere has drifted away..."
    si "「Shun-kun.{p}\ \ The dragon king is above the sky,\n\ \ and also in the river. 」"
    si "「After that, he watches us on the shrine grounds,\n\ \ right? 」"
    su "「Yes. 」"
    si "「Because there is only one dragon king,\n\ \ I don't think that is a very convenient story. 」"
    
    show su 003 with dis
    
    su "「Fueh. 」"
    si "「Earlier you said he is always patrolling the river,\n\ \ so he can't be up in the sky or at the shrine\n\ \ for very long. 」"
    si "「There's been a curtain of clouds since morning,\n\ \ and he's listening to shrine visitors.{p}\ \ There isn't an adequate explanation for this. 」"
    
    show su 004 with dis
    
    su "「B-but. 」"
    si "「But? 」"
    
    show su 010 with dis
    
    su "「I hear from my family all the time that\n\ \ the dragon god is protecting the village. 」"
    
    show si 003 with dis
    
    si "「It doesn't matter what kind of stories you hear.{p}\ \ The inconsistencies are a problem. 」"
    "Shin-kun is only questioning things\nthat don't make sense."
    "However, his sharp tone\nhas unfortunately frightened Shun-kun."
    su "「W-woof. 」"
    
    show si 001 with dis
    
    si "「If you can come up with an explanation,\n\ \ I'd like to hear it. 」"
    "Although I think it's a little childish,\nwas this what I was worried about from before?"
    "He focuses his gaze directly at Shun-kun,\nlooking as if he's going to take a bite out of him."
    
    show su 003 at shivering with dis
    pause .2
    
    su "「Woof... 」"
    si "「Crying to get out of trouble\n\ \ isn't very admirable. 」"
    "Part of this seems to be Shun-kun's fault.{p}Should I give a little response?"
    fn "「H-hey, it probably depends\n\ \ on the dragon king's mood. 」"
    fn "「Sometimes he wants to be in the sky,\n\ \ and sometimes he wants to be in the river. 」"
    si "「Then, \"always\" is incorrect. 」"
    
    show su 005 at still with dis
    
    su "「No!{p}\ \ The dragon king is protecting us! 」"
    fn "「Y-you hear that Shin-kun?{p}\ \ The legend says so. 」"
    
    show si 004 with dis
    
    si "「And you completely believe\n\ \ what Shun-kun is saying? 」"
    fn "「Huh? 」"
    "He changes his aim of attack\nin this conversation."
    
    show si 001 with dis
    
    si "「What Shun-kun and I are talking about,\n\ \ or rather, feeling doubt about\n\ \ Minasato's legends. 」"
    si "「Do you think there aren't any contradictions,\n\ \ or are you thinking logically? 」"
    
    show si 004 with dis
    
    si "「Do you agree with me?{p}\ \ At the very least the stories don't match up,\n\ \ do they not? 」"
    "Wah, why is he snapping at me like that?"
    
    show si 001 with dis
    
    si "「It's natural that it's\n\ \ unnatural because it's a legend.{p}\ \ I'd like to hear [fn]'s opinion. 」"
    
    show su 004 with dis
    
    su "「[fn]-san... 」"
    "The issue of the current situation has changed\nto whether I agree with Shun-kun or Shin-kun.\nB-both of you don't need to get so serious!"
    "C-crap."
    "If I don't come up with a proper explanation\nfor the dragon king, It's only a matter of time\nbefore Shun-kun starts to fighting with me."
    "On the other hand, I also want to avoid\noffending Shin-kun. His tail is swinging around\nwith displeasure, it's kind of scary."
    "What should I do?"
    
    menu:
        "A. Support Shun-kun.":
            jump shun18_support_shun
        "B. Shin-kun's opinion is reasonable too.":
            jump shun18_support_shin
        "C. Dodge the question.":
            jump shun18_support_neither
    
    #####################################################
    label shun18_support_shun:

        $ event_name = _("Which Side...?")
            
        stop music fadeout 1
        pause 1
        play music pops_003 fadein 1
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        
        fn "「I agree with Shun-kun. 」"
    
        show su tailwag 01 with dis
        
        su "「[fn]-san! 」"
        "Shun-kun immediately regains his smile.{p}His tail is wagging as if it's going to break off."
        fn "「Maybe he forgot to open the curtains\n\ \ after getting dressed. 」"
        fn "「So that doesn't necessarily mean he's always\n\ \ in the sky when it's cloudy. 」"
        
        show si 003 with dis
        
        si "「Then can you explain how he is swimming\n\ \ in the river, protecting the village,\n\ \ and also living at the shrine? 」"
        
        show su 003 at shivering with qdis
        pause .2
        
        fn "「He's a god, so he has the great ability\n\ \ to see faraway places. 」"
        fn "「He can foresee the movement\n\ \ of tiny creatures like us. 」"
        fn "「So even if he's in the sky, in the river,{p}\ \ or at the shrine,{w} he is able to\n\ \ \"always\"  watch over us. 」"
    
        show su tailwag 01 at still with qdis
        pause .2
        
        si "「I see. 」"
        si "「However, if he can foresee what goes on\n\ \ in the village, then there's no need for him\n\ \ to go out of his way to patrol. 」"
        
        show su 003 at shivering with qdis
        pause .2
        
        fn "「He wants everybody to see himself dressed up. 」"
        
        show su tailwag 01 at still with qdis
        pause .2
        
        si "「Why didn't he appear at the shrine\n\ \ when I prayed for him to do so? 」"
        
        show su 003 at shivering with qdis
        pause .2
        
        fn "「Err, he would appear, but he doesn't want\n\ \ to be embarrassed so he went back to the sky\n\ \ to prepare his moustache. 」"
        fn "「I think he'll show up at your house sometime tonight. 」"
        
        show su tailwag 01 at still
        show si 001 
        with dis
        
        si "「... 」"
        fn "「... 」"
        
        show su 004 with dis
        
        su "「... 」"
    
        show su tailwag 01
        
        su "「Woof. 」"
        "D-did I get through that somehow?{p}Shun-kun smiling in consent is proof\nof that more than anything else."
        "On the other hand,{p}{nw}"
        show si 004 with dis
        extend "Shin-kun lets out a single sigh."
        si "「Forget it.{p}\ \ I understand [fn]'s opinion. 」"
        si "「Even though I thought he was my friend. 」"
        fn "「What? 」"
        "He faintly murmured,\nso I still couldn't hear him very well."
        
        show si 001 with dis
        
        si "「Nothing.{p}\ \ And Shun-kun. 」"
        
        show su 004 with dis
        
        su "「Y-yes...? 」"
        "Shin-kun's nomination scares Shun-kun."
        si "「Don't just accept what you hear\n\ \ from others without question,\n\ \ you should learn to doubt its authenticity. 」"
        su "「But- 」"
        si "「No buts.{p}\ \ You should know when things don't make sense. 」"
        si "「Even things you believe\n\ \ from the bottom of your heart. 」"
        si "「You didn't answer my questions earlier,\n\ \ that should be more convincing than anything else.{p}\ \ [fn]'s answers were less than credible. 」"
        
        show su 010 with dis
        
        su "「Okay... 」"
        fn "「You're right about that. 」"
        si "「And so there's no need to pick\n\ \ a quarrel over something so childish. 」"
        
        show su 003 with dis
        
        su "「I'm sorry. 」"
        fn "「Okay! That's enough! 」"
        "Not being able to stand his cutting tone,\nI step between them."
        fn "「Shun-kun, are you alright? 」"
        su "「Yeah, *sniffle*, I'm okay. 」"
        si "「... 」"
        fn "「Shun-kun's dragon god is still great. 」"
        
        show su 013 with dis
        
        su "「Y-yeah, that's right.{p}\ \ The dragon god is watching over us, so... 」"
        "In order to convince himself,\nShun-kun continues to mutter."
        "Even so, what Shin-kun said\nseems to have stuck to him."
        "His unclouded faith from earlier\nis no longer reflected in his eyes."
        "It looks like he's completely discouraged.{p}Hmm, he really did believe in the legend\nof the dragon god."
        "Maybe it's my fault for saying too much."
    
        jump end18
        
        
    ##################################################
    label shun18_support_shin:

        $ event_name = _("Which Side...?")

        stop music fadeout 1
        pause 1
        play music piano3_015
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        
        fn "「Shin-kun does have a point. 」"
        
        show su 003 with dis
        
        su "「[fn]-san... 」"
        fn "「It's impossible if Shun-kun is wrong,\n\ \ isn't it? 」"
        fn "「It's an old legend,\n\ \ so it's not strange for things to change\n\ \ when it's told for a long time. 」"
        si "「That's right. 」"
        fn "「For example, people who noticed the dragon king\n\ \ watching from the river were so happy,"
        fn "「That they were unintentionally put under\n\ \ the impression that he's \"always\" watching. 」"
        fn "「When other people came to visit the shrine,\n\ \ the dragon king was away, but makes a show\n\ \ of saying things like \"I'm always listening.\" 」"
        fn "「Things like that overlapping each other\n\ \ are the reason why the god's legend changes. 」"
        fn "「Therefore, I think that's a reason\n\ \ why the stories Shun-kun heard are wrong. 」"
        fn "「But if there's something that doesn't make sense,\n\ \ it's just from misunderstandings and assumptions,"
        fn "「so I don't think one bit of the dragon king's\n\ \ greatness has been lost. 」"
        si "「I'm surprised. 」"
        si "「I didn't think that you were\n\ \ able to perceive all of that. 」"
        "Ah.{p}That's what Shin-kun has been\nthinking of me up until now."    
        si "「For the people of this village, are the way\n\ \ the contents of the legend told important? 」"
        si "「Because it doesn't seem particularly interesting. 」"    
        si "「I'm relieved that [fn] has a\n\ \ different way of thinking. 」"
        
        show su 004 with dis
        
        su "「Uu, I don't get it. 」"
        fn "「Shun-kun? 」"
        
        show su 003 at shivering with dis
        
        su "「The dragon king is a great god.{p}\ \ It all has to be true. 」"
        fn "「Shun-kun... 」"
        "It's rare to see him perplexed like this."
        "Until we returned in the evening,\nShun-kun grumbled with a troubled expression."
    
        jump end18        
        
    #################################################
    label shun18_support_neither:

        $ event_name = _("Which Side...?")
        
        stop music fadeout 1
        pause 1
        play music free0630 fadein 1
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        
        fn "「I don't mean to put emphasis on Trinitarianism,{p}\ \ but unity in the actual existence of gods\n\ \ should always be doubted,"
        fn "「So it's not necessary to be subjected\n\ \ to the limits of time and space, is it? 」"
        
        show su 015 with dis
        
        su "「? 」"
        si "「? 」"
        fn "「In other words, for the conclusive evidence\n\ \ of the ontology in the God Hypothesis, 」"
        fn "「There's whether or not Pascal's Wager gives\n\ \ meaning to Agnostics, as well as Atheists,\n\ \ and causes about the same amount of ruin to them. 」"
        su "「??? 」"
        si "「!? 」"
        fn "「As for me,{w}  I love Shun-kun, Shin-kun,\n\ \ and the dragon king. 」"
        
        show su 004 with dis
        
        su "「! 」"    
        si "「...[fn], I would like you\n\ \ to give a conclusion, 」"
        si "「but because you turned\n\ \ your forced theory into a mess,\n\ \ I think you've given up on maintaining context. 」"
        "Yeah.{p}I also understand that I have failed.{p}I tried with a possibility of 1/10,000."
        "I thought of as many words\nabout god to put together."
        "I wondered if it would settle this\nsituation peacefully."
        "As a result,\nShun-kun was bewildered,\nand Shin-kun was left speechless."
        "Ahaha."
        fn "「As for me,{p}\ \ I love Shun-kun, Shin-kun, and the dragon king! 」"
        
        show su 016 with dis
        
        su "「M-me too!! 」"
        "Although confused, Shun-kun agrees with me.{p}Shin-kun, who is already beyond fed-up,\nbitterly smiles."
        "Was that alright?"
        
        jump end18

#################################################        
label end18:
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

    jump day19

