## Day 9

screen park09:
    hbox:
        add "arrow down"
        at parkbounce1
    hbox:
        add "icon_kouya"
        at parkbounce2
    hbox:
        text _("Park")
        xalign .49 yalign .55
screen shunhouse09:
    hbox:
        add "arrow down"
        at shunhousebounce1
    hbox:
        add "icon_shun"
        at shunhousebounce2
    hbox:
        text _("Shun's House")
        xalign .72 yalign .61
screen ricefield09:
    hbox:
        add "arrow down"
        at ricebounce1
    hbox:
        add "icon_juu"
        at ricebounce2
    hbox:
        text _("Rice Fields")
        xalign .245 yalign .66     
screen forest09:
    hbox:
        add "arrow down"
        at forestbounce1
    hbox:
        add "icon_shin"
        at forestbounce2
    hbox:
        text _("Forest")
        xalign .61 yalign .87
screen tatsukihouse09:
    hbox:
        add "arrow right"
        at tatsukibounce1
    hbox:
        add "icon_tatsu"
        at tatsukibounce2
    hbox: 
        text _("Tatsuki's House")
        xalign .85 yalign .88

screen minasatomap09a():
    add "map"
    add "mapdate"
    imagebutton idle "a icon" hover "icon loop" xpos 364 ypos 270  action Jump("kouya09") hovered Show("park09")  unhovered Hide("park09") hover_sound "av/audio/click_008.wav"
    imagebutton idle "a icon" hover "icon loop"  xpos 516 ypos 300  action Jump("shun09") hovered Show("shunhouse09")  unhovered Hide("shunhouse09") hover_sound "av/audio/click_008.wav"
    imagebutton idle "a icon" hover "icon loop"  xpos 453 ypos 447  action Jump("shin09") hovered Show("forest09")  unhovered Hide("forest09") hover_sound "av/audio/click_008.wav"
    imagebutton idle "a icon" hover "icon loop"  xpos 662 ypos 391  action Jump("tatsuki09") hovered Show("tatsukihouse09")  unhovered Hide("tatsukihouse09") hover_sound "av/audio/click_008.wav"
    imagebutton idle "a icon" hover "icon loop"  xpos 197 ypos 325  action Jump("juuichi09") hovered Show("ricefield09")  unhovered Hide("ricefield09") hover_sound "av/audio/click_008.wav"
    hbox:
        text _("{size=+30}August 9")
        at maptime
        
screen minasatomap09b():
    add "map"
    add "mapdate"
    imagebutton idle "a icon" hover "icon loop" xpos 364 ypos 270  action Jump("kouya09") hovered Show("park09")  unhovered Hide("park09") hover_sound "av/audio/click_008.wav"
    imagebutton idle "a icon" hover "icon loop"  xpos 516 ypos 300  action Jump("shun09") hovered Show("shunhouse09")  unhovered Hide("shunhouse09") hover_sound "av/audio/click_008.wav"
    imagebutton idle "a icon" hover "icon loop"  xpos 453 ypos 447  action Jump("shin09") hovered Show("forest09")  unhovered Hide("forest09") hover_sound "av/audio/click_008.wav"
    imagebutton idle "a icon" hover "icon loop"  xpos 662 ypos 391  action Jump("tatsuki09") hovered Show("tatsukihouse09")  unhovered Hide("tatsukihouse09") hover_sound "av/audio/click_008.wav"
    hbox:
        text _("{size=+30}August 9")
        at maptime
        
############################################
label day09:
    
    $ renpy.music.set_volume(1.0, 0.0, channel = "music")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound2")
    
    $ focus_character = ""
    $ event_name = _("８月9日")
    $ the_date = _("August 9")
    $ day = 9
    
    window hide
    play music birds_chirping
    
    scene sky01 
    show text "{size=+130}August 9" at truecenter
    with Dissolve(.5)

    pause 3
    scene black with Dissolve(1)
    pause .4
    
    scene hbroom with wipe_corner
    
    fn "「I wonder what I should do today. 」"
    
    if juuichi_hate == True:
        play music "<from 2.5>av/audio/free0422.ogg"
        call screen minasatomap09b
    
    play music "<from 2.5>av/audio/free0422.ogg"
    call screen minasatomap09a
    
###############################################    
label kouya09:
    
    $ focus_character = "kouya"
    $ event_name = _("Taking Shelter in the Park from Rain")
    $ love_kouya += 1
    
    scene map
    hide screen park09 
    pause .01
    
    call rain_set from _call_rain_set_6 
    scene market
    show over black 
    show raining
    with Dissolve(.5)
    play music rainfall
    pause .5

    fn "「Damn it!{p}\ \ Who missed something in the weather forecast!? 」"
    "I was running, screaming to no one in particular\nas the rain came pouring down."
    "If someone I knew saw me like this,\nI might die from embarrassment."
    "The T-shirt I was wearing was soaked through.{p}It felt awkward moving around\nwith the wetness clinging to my skin."
    "On a side note, the one who missed something\nin the forecast wasn't anyone, but me."
    fn "「Gaah, if I knew this was going to happen,\n\ \ I'd be sitting at home...! 」"
    "Lately, we've had nothing but summer-like weather."
    "Sunlight flaring across endless blue skies.{p}Cicadas singing all day.\nNo other weather to be seen."
    "However, today was different."
    "After so long there were clouds.{p}Comparing temperatures, it was much cooler.{p}It wasn't that humid, either."
    "So, I was happy to go out for a walk.{p}With weather like this,\nit's much easier to go outside."
    "Usually, I'd be shrivelling to a crisp,\ncomplaining about it being so hot.\nSo today I jumped at the chance to go out."
    "But that was all I took into account.{p}In my haste, I carelessly ignored the forecast."
    "If I think about it, this weather was suspicious.{p}When it rains, it isn't that weird."
    "If I'd listened in on the housewives I passed earlier:"
    hwa "「Oh my, it really is raining. 」"
    hwb "「Of course. The forecast\n\ \ said there was a 99\% chance of rain.{p}\ \ Wouldn't it be strange for it not to rain? 」" 
    "...Something like that.\nAnd boy, is it raining."
    "Still, what's this 「99\% chance of rainfall 」?{p}What the hell kind of odds are those?{p}A really old FebrXze commercial?"
    "Just put it at 100 already.{p}What is that last 1\% for anyway?{p}Adults' circumstances?"
    "Well in any case, it's my naivety\nthat brought me into this situation."
    "Is there anything to do but run with all I've got?"
    fn "「Man, give me a break... 」"
    "While I was cursing,\nI immediately turned around to go home."
    "With each step I took, the wet asphalt would\ngive back a bit of a strange sensation."
    "The smell of rain blended into the passing wind."
    fn "「Oh, I give up.\n\ \ At this rate, I really will be wet to the bone. 」"
    "It's too late to say that, but I tried anyway."
    "The rain has only just started falling.{p}When I was looking at the sky earlier,\nI thought it wasn't going to get darker."
    "I should have figured it would get worse."
    fn "「I have to get out of the rain...\n\ \ Otherwise I really will catch a cold. 」"
    "I pulled out all my oldest memories,\ntrying to remember if there\nwere any good places to shelter around here."
    fn "「...Ah! 」"
    "And then I did remember."
    "There should be a park, somewhere near here."
    fn "「There should be a square gazebo, I think... 」"
    "When I was still here, I'm sure there was one.{p}Then again, that was a long time ago.{p}I don't know if it's still there now."
    fn "「...Yeah. 」"
    "But, I thought I should go."
    "I don't really get why,\nbut I feel like there's\nsomething important to me there."
    "I changed course, and headed to the park."
    "The rain seemed to pour down even harder."
    
    scene black with Dissolve(1)
    pause .5
    call rain_set from _call_rain_set_7 
    scene park_rain 
    show raining 
    with wipe_right

    $ event_name = _("The Boy Taking Shelter from the Rain")
    
    "When I arrived at the park,\nI thought I was going back into the past.\nEverything was the same as it used to be."
    "Looking around at the entrance,\nI could almost see an overlay of\nmy memories on top of the scenery."
    "Out here, they're more attentive to maintenance,\nas I can tell from the neat-looking park."
    "Further on, there's a see-saw, a swing set,\na jungle gym that's now a bit too small for me,\nand a larger square gazebo."
    "The paint must've been put on so many times,\neven though it's starting to peel off again.\nI feel like it's the same as back when I played here."
    fn "「It really hasn't changed. 」"
    "I made my way through the empty park,\ntowards the gazebo."
    "Because I went into my nostalgic tangent,\nI got wetter than I needed to be."
    "That was idiotic of me, seriously."
    fn "「Whew... 」"
    "I sat on the bench to catch my breath,\nthen took another look around the park."
    "There's nothing special about the scenery,\nbut it's so nostalgic."
    "I don't understand why,\nbut just being here makes me a little happier."
    "Nothing unusual here.\nJust a park with no children around on a rainy day."
    fn "「...? 」"
    "As I look at it all, for some reason,\nI feel as though I've forgotten something important."
    "It's the same as when I decided\nto come here to get out of the rain.\nThe feeling that I'm missing something."
    fn "「Did I forget something, somehow...? 」"
    
    show black behind raining with split_close
    $ renpy.music.set_volume(0.15, 0.0, channel = "music")

    "I went into thinking, searching through my memories.{p}At the same time, on the other side of my eyelids,\nsomething seemed to be moving."
    "There's no doubt about it, I've forgotten something."
    "I tried focusing my closed eyes.{p}But I still couldn't get a clear glimpse at the image."
    "...Nothing really sticks out,\nin my memories of before."
    "I started getting irritated\nwith my elderly-seeming impression.\nI voiced this self-disgust publically."
    fn "「No good at all... 」"
    who "「Hey. 」"
    
    play sound bosu29
    hide black with split_open_fast
    
    fn "{size=+15}「WAH!? 」{nw}" #!#Speech box need to shake
    show park_rain at hshake
    extend ""
    "A voice came out of nowhere,\nand I looked up in alarm."
    "What entered my eyes\nwas a husky dogman from somewhere."
    
    play music shop01 fadein 3
    show ka 001 at center behind raining with dis

    ka "「What are you doing, way out here? 」"
    fn "「...You scared me.{p}\ \ Don't surprise me like that, Kouya. 」"

    show ka 005 with dis
    
    ka "「I wasn't trying to surprise you. 」"
    fn "「...Oh well, I won't get anywhere,\n\ \ sweating the small stuff like this. 」"

    show ka 001 with dis
    
    ka "「Saying that in advance for something, huh.{p}\ \ So,{w=.3} what was that about \"no good at all\" earlier? 」"
    "As he asked, he sat down beside me."
    fn "「Hmm?{p}\ \ I just can't remember something from a while back.{p}\ \ Have I really gotten so old? 」"

    show ka 005 with dis
    
    ka "「Yeah, you're old enough.{p}\ \ Thinking is what middle-aged people do. 」"
    fn "「...Can't you play along better than that?{p}\ \ I was waiting for a straight man just now, you know? 」"
    ka "「Sorry, I don't think I'd be a very good\n\ \ straight man. I'll pass. 」"
    fn "「You're so cold.{w} By the way,\n\ \ what were you doing out here in the rain? 」"

    show ka 002 with dis
    
    ka "「I was out doing some shopping.{p}\ \ When I came out of the store, it was raining,\n\ \ so I was running, when I passed by someone I knew. 」"

    show ka 003 with dis
    
    ka "「I wondered what you were doing, you know?{p}\ \ So I tried following you.{p}\ \ Then I noticed this place. 」"
    fn "「I-{w=.3}is that so... 」"
    "He saw everything, then.{p}I wanna die from embarrassment."

    show ka 001 with dis
    
    ka "「Hey, that's what I should be asking.{p}\ \ So what are you doing, out on this kind of day? 」"
    fn "「Hm? 」"

    show ka 005 with dis
    
    ka "「The forecast said there'd be rain today,\n\ \ so why would you go out loitering empty-handed?\n\ \ ...That's what I'm asking you. 」"
    fn "「Aah...{w} I missed out on the forecast.{p}\ \ If I hadn't I wouldn't be out here, pretty much. 」"
    ka "「Oh you...\n\ \ make sure of these things when you go out. 」"
    ka "「Give me a break. 」"
    "Kouya shook his head and took a deep sigh."
    fn "「I was thinking that too...\n\ \ But still, it was clear this morning.\n\ \ It *was* clear, wasn't it? 」"
    ka "「Yeah yeah, it was.{p}\ \ It was all clear, looking like good weather.{p}\ \ But that doesn't have an effect on weather later on. 」"
    fn "「Hahahah, I know right?\n\ \ But, if only it kept that way... 」"
    "After saying that, I got depressed.\nUnintentionally, I let out a sigh."
    ka "「Geez... 」"
    "When he saw me like that,\nit seemed as if he were surprised."
    "Wait, it's less \"seemed as\" and\nmore \"actually\" surprised."

    show ka 001 with dis
    
    ka "「...Hey. 」"
    fn "「Mm,{w=.3} what? 」"
    ka "「You doing anything after this? 」"
    fn "「No, I was out on a simple walk,\n\ \ then I was thinking it'd be nice to go home.{p}\ \ But there's the rain and all... 」"
    "While I was speaking, I looked up into the sky."
    "The sky was still shaded in lead.\nThough honestly, the color of lead\nalready looks like it wouldn't water down."
    "Without an umbrella,\nI can't think about going back in this."

    show ka 002 with dis
    
    ka "「I see, so if you had an umbrella you could go back. 」"
    fn "「That's how it is. 」"

    show ka 003 with dis
    
    ka "「Wanna go back, then? 」"
    fn "「Eh? 」"
    "Kouya stood up as if he hadn't heard a thing I said."
    fn "「Eh,{w=.3} but we'll get all soaked.{p}\ \ And what about an umbrella? 」"

    show ka 001 with dis
    
    ka "「What are you talking about?{p}\ \ I've got an umbrella. 」"
    fn "「Ah... 」"
    "I looked down,\nand there in Kouya's hand was a blue-green umbrella."
    "He passed by me in the rain in the first place,\nbut he isn't wet at all."
    fn "「Oh...{w} I see then. 」"
    "I was in a temper from being soaked in the rain,\nand I didn't notice until he pointed it out."
    "I really am feeling like I'll drop dead..."
    ka "「Your ability to notice things really is weak...{p}\ \ Oh well, shall we go? 」"
    
    stop music fadeout 1
    hide ka with wipe_right

    "With a *fwump*, the umbrella opened.{p}The beautiful hue reminded me\nof an illusionary flower blooming from somewhere."
    "A very mysterious flower,\nwith curled up leaves and no petals."

    play music rainfall fadein 1
    
    fn "「...? 」"
    "In the moment I saw that,\nsomething flickered in my field of vision."
    "Huh, where did I...?"
    "Somewhere in my head, I could hear a whisper."
    "Do I know this...?"

    show ka 002 with dis
    
    ka "「It's good that this umbrella is so big.{p}\ \ It should be fine for someone your size, [fn]. 」"
    fn "「... 」"
    "Just a casual word from Kouya.{p}It feel into my chest with a clink."
    "And then the blurred world\nbecame something else altogether."
    "That's it, I remember-"
    
    $ event_name = _("The Boy in the Memory")
    
    scene black with dis
    pause .3
    call rain_set from _call_rain_set_8 
    scene school01 gray 
    show over red light
    show raining
    with dis 

    "That day, coming home from school,\nit was rainy just like today."
    "In the morning, even though my mom had warned me,\nI went to school without bringing an umbrella."
    "I had thought that since the weather was so nice,\nthere wouldn't be any way there'd be rain."
    "However, when the school day was close to ending,\nthe sky quickly darkened.\nRain would start falling at any second."
    "So when class actually ended,\nthe sky was still just as dark,\nso I hurried and ran home."
    "Unfortunately, the forecast wasn't wrong."
    "「It may rain this afternoon.{p}Please do not forget your rain gear. 」"
    "So naturally, in the middle of the run home,\nthe rain came brutally pouring down."
    "Moreover, it was a downpour."
    "I panicked and sought out a\nplace to get out of the rain."
    "Then, just like today, I came to this park\nand stayed under this gazebo."
    "As I was looking at the lightless sky,\nMy way had come to an end."
    "It was then."
    who "「Hey. 」"

    $ event_name = _("The Boys Under the Umbrella")

    ka "「-ey,{w=.3} -h- 」"
    fn "「... 」"
    ka "「-he-,{w=.3}{w=.3} -Hey! 」"
    fn "「Eh...? 」"
    
    call rain_set from _call_rain_set_9 
    scene park_rain
    show ka 005 at center
    show raining 
    with Dissolve(.5)

    "When I came to, Kouya's worried face\nwas right in front of me."
    "The scene I was looking at changed,\nand before I knew it,\nI returned to the park I'm in presently."
    ka "「What's wrong, [fn]? You were spacing out.{p}\ \ Did you come down with a cold already? 」"
    fn "「...no,{w=.3} I was just\n\ \ remembering something from back then. 」"

    show ka 001 with dis
    
    ka "「Hm?{p}\ \ What did you remember? 」"
    fn "「Umm... It's a secret!{p}\ \ My memories will always stay inside of me. 」"

    show ka 005 with dis
    
    ka "「What's that about? 」"
    "Kouya made a puzzled face,\nas if to say 「I don't get you 」."
    fn "「Come on, come on already.{p}\ \ Now,{w=.3} shall we go?{w} You'll take me back right? 」"
    "I clapped Kouya on the shoulder, as if to deceive him.{p}For this memory, I can't really tell him.{p}Because maybe, if I told him, he might get mad."
    ka "「... 」"
    "As I got under the umbrella,\nhe made a face that said he wasn't satisfied\nwith that explanation."
    "Under this rainy sky,\nthere was only one blue-green flower."
    "Underneath that shared umbrella,\nI remembered that tiny husky beastman."
    
    jump end09

###############################################    
label shun09:

    $ focus_character = "shun"
    $ love_shun += 1
    $ event_name = _("3 Black Sets")

    scene map
    stop music fadeout 1
    hide screen shunhouse09
    scene black with wipe_dr
    pause .5
    scene shun_house_living with dis
    $ renpy.music.set_volume(0.7, 0.0, channel = "sound")
    play sound unari00
    pause 2.5
    $ renpy.music.set_volume(0.8, 0.0, channel = "sound")
    play sound rainfall loop
    
    "Gaah. {p}A game console roars."
    "The beginning of this occurrence\nwas a result of the unfortunate rain."
    
    scene black with wipe_dr
    pause 1
    
    call rain_set from _call_rain_set_10
    scene shun_house_door 
    show raining
    with wipeleft
    
    pause 1
    play sound2 doorbell1
    
    pause 3
    
    show shun_house_entry with blind_vert
    stop sound fadeout .5    
    $ renpy.music.set_volume(0.8, 0.0, channel = "music")
    play music daily02 fadein .5
    show su 002 at center with dis

    su "「Please come in♪ 」"
    fn "「Pardon me for barging in.{p}\ \ What a beautiful entranceway. 」"

    show su 001 with dis
    
    su "「You think so?{p}\ \ Ehehe, thank you very much. 」"
    "I wipe away the water on my umbrella\nand place it in his umbrella stand. {p}I have come to Shun-kun's house to play today."
    
    scene shun_house_living
    show su 001 at center
    with wipeleft
    
    "An extension cord is plugged into to 2 places\nin the living room wall."
    "A 6-hole outlet strip extends out from there,{p}with an on-off switch attached to each outlet."
    
    show su tailwag 01 at bobbing with dis

    su "「Now then, which one should we play!? 」"
    "He restlessly fidgets with a full smile\nand a burst of tail wagging."
    "His eyes speak more of his present excitement\nthan his words. {p}Fufufu, he's so cute. I feel happy as well."
    fn "「Hmm, there's plenty to choose from,\n\ \ isn't there. 」"
    "An imposing rack sits next to the TV\nwith a game console on every shelf."
    "They're white, black, and pink\nand assert themselves intensely."
    "On the shelves there's hardware, software,\nand other miscellaneous gaming products."
    "They are meticulously organized and arranged\nso that they can be taken out easily."
    "Huh? {p}A strange looking game console\nsits on the highest shelf."
    fn "「Shun-kun, are those game consoles stacked\n\ \ on top of each other? 」"
    "It seems to be a cluttered up black mass."
    "If they're valuable game consoles,\nI don't think he would be giving them\nsuch rough treatment, would he?"

    show su 015 at center with dis

    su "「? 」"
    "He bends his head slightly to the side.\nAfter following my line of sight,\nhe nods in comprehension."
    
    show su 001 at bowing 

    su "「That one is connected to all of them. 」"
    fn "「Connected? 」"
    su "「There are a lot of peripheral devices. 」"
    "According to him, the one in the center\nis the main console, on the bottom is a rough box,\nand the unsteady one on top seems to be optional."
    "It looks just like a {nw}"
    play sound metal38 
    extend "space ship.{w=1}\nI'm overpowered by the intensity of its gold logo." 
    fn "「When you said there were things connected to it,\n\ \ I imagined things like a gun controller or a mouse\n\ \ connected to a relatively smaller machine. 」"
    su "「Like this? 」"
    "Shun-kun takes out a mouse with blue buttons."
    fn "「Yeah, needed for something like drawing software,\n\ \ or a miniature garden simulator. 」"

    show su 002 with dis
    
    su "「It can also be used turned upside down. 」"
    fn "「!{w=.3} It, it changed into a trackball! 」"
    "Now then,{w} after thoroughly enjoying the\ngame space in Shun-kun's house for a while,\nI sit myself down."
    "Well, every little thing must be inserted\ninto the source of the electricity\njust so we can have fun."
    
    show su tailwag 01 with dis

    su "「[fn]-san, which game should we play? 」"
    menu:
        "A. A fighting game.":
            jump shun09_fighting
        "B. A puzzle game.":
            jump shun09_puzzle
        "C. An old game I used to play with Shun-kun.":
            jump shun09_oldgame
    
    ############################################
    label shun09_fighting:

        $ event_name = _("←↓→＋Ｐ")
        show su 001 with dis
        play music pops_001 fadein .5
    
        su "「Well then, I'll call Torahiko-san too. 」"
        fn "「Torahiko? He likes fighting games? 」"
    
        show su 002 with dis
        
        su "「Yeah. He wanted me to call him\n\ \ the next time I play one. 」"
        
        scene black with wipe_dr
        pause .3
        
        scene shun_house_living 
        show su 002 at center
        show to 010 at offright
        with wipe_dr
        
        pause .2
        
        show su at move_midleft(0.5)
        show to at move_midright(0.5)
        
        pause .5
    
        to "「Heheheh, I've come to get payback\n\ \ for the other day! 」"
    
        show su 005 at jump_up
        
        su "「I accept your challenge! 」"
        "Shun-kun must have done beyond repairable damage\nto him last time, so he's probably chomping\nat the bit for revenge."
        "With one phone call, a tiger dripping\nwith rain immediately appeared."
        
        show to 006 at stagger 
    
        "He wipes his head dry with a borrowed bath towel,{p}{nw}"
        show to 003 at still
        play sound bosu31
        extend "then sits with a thump on the 2nd player's side." 
        "There is a controller with 6 buttons and a stick,\nmodeled after the ones in arcades."
        "It seems to be Torahiko's favorite.\nShun-kun probably has it prepared\nwhenever he comes over."

        show to at shivering
        show su 001 with dis
        play music free0456 fadein .5
    
        to "「UOOOOOOH! 」"
        su "「... 」"
        "Torahiko's play style is to excitedly yell\nwhile mashing the buttons.{w} In stark contrast,\nShun-kun follows the screen in silence."
        "A military-style character with huge muscles, {p}and a petite, oriental martial artist.{p}Their selections are projections of their appearances."
        "The lever violently clatters in the yellow hand.{p}The brown fingers precisely trace the arrow buttons.{p}"
        "Brute force is just toyed around with\nby effective tight turns."
        
        show to 005 at hit_right 
        
        to "「Uoh!! 」"
    
        hide to with wipe_down_slow
        play sound bosu29
    
        "Just as I thought.{p}Torahiko leans back and yells simultaneously\nwith the loser on the screen."
    
        show to 008 at midright with wipe_up_slow
        
        to "「A-again! Again! 」"
    
        show su 002 with dis
        
        su "「Hehe, I'm looking forward to it♪ 」"
        "Then Torahiko continues to receive a beating,{p}which is expanded to 2 people whenever I rush in."
        "The result ended with a landslide victory\nfor Shun-kun today."
        
        jump end09

    #########################################    
    label shun09_puzzle:
        
        $ event_name = _("ＮＥＸＴ□□□□")

        fn "「This won't be too hard. I should be able\n\ \ to learn the rules fairly quickly. 」"
    
        show su 002 with dis
        
        su "「Well then, here. 」"
        fn "「Ooh! 」"
        "Make a nice gap, casually insert a stick,\nand clear a line.{w} Loved throughout the world,\nthis is Falling Mono Block Puzzle."
    
        show su 005 with dis
        
        su "「Let's battle! 」"
        fn "「Huh?{w=.3} You play against each other in this? 」"
        "I was under the impression that this was a game\nwhere you challenge your own limits alone."
    
        show su 002 with dis
        
        su "「Yeah!{w=.3} You send blocks into your\n\ \ opponent's field and use techniques.{p}\ \ Whoever's stack fills up first loses. 」"
        "Huh. {p}I didn't think that the era where you use\nspecial techniques in puzzle games had come."
        fn "「Alright. Now that I know the rules,\n\ \ I feel safe even if we're starting right away.{p}\ \ I won't lose! 」"
    
        show su 005 with dis
        
        su "「I won't lose either! 」"
        
        scene black with rotation
        stop music fadeout .5
        pause 1.5
        
        play music pops_004 fadein .5
        scene shun_house_living
        show su tailwag 01 at center 
        with wipe_up_slow
    
        "Utter defeat. {p}More blocks rose up and I had lost."
        
        show su at bowing
        
        su "「Victory! 」{nw}"
        "Some time ago, I took a quick side glance\nat Shun-kun's button handling. {p}It wasn't natural."
        "The moment he pushed the up button,\nthe blocks fell."
        fn "「Sh{w=.3}-Shun-kun, you're good at this, aren't you?{p}\ \ I didn't stand a chance... {p}\ \ Isn't there an opponent that can beat you? 」"
        "I think through all of my childhood friends.{p}Somebody better than Shun-kun... hmm. {p}Kounosuke might be unexpectedly strong."
        
        show su 004 with dis
        
        su "「Father is better than me. 」"
        "What!? A nearby ambush!"
        
        show su 016 with dis
        
        su "「He pretty much only plays this game though.\n\ \ I've never been able to beat him. 」"
        
        show su 001 with dis
        
        su "「I asked him about it.\n\ \ When the first machine was put in the arcade,\n\ \ he was really addicted to it 」"
        "Wow. {p}He was shown the experience of an old gamer?"
        "Shun-kun has inherited the spirit of the blocks.{p}It was a crappy day for me in the end,\nI couldn't compete with him at all."
        
        jump end09
    
    ###########################################
    label shun09_oldgame:

        $ event_name = _("Dungeon Mapping")
            
        fn "「Back then there was a game\n\ \ I'd come to your house to play,\n\ \ I want to see if it might be here. 」"
        su "「Alright.\n\ \ Please wait a minute♪ 」"
    
        hide su with wipeleft
        
        "He exits the living room,\nand seems to go to his room upstairs."
    
        show su 001 at center with wipeleft
        
        su "「Do you remember this? 」"
        "He shows me the thing he brought.{p}I think it's a retro paper box. There are characters\nlike medieval knights and wizards printed on it."
        "Hmm? {p}Although I do recall something like this\nin the corner of my head,{w} I can't remember."
        su "「Back then I couldn't find my way\n\ \ through the dungeons. 」"
    
        show su 002 with dis
        
        su "「When I asked you for help,\n\ \ you said 『Let's do it together!』\n\ \ and did the mapping for me. 」"
        "Oh yeah, if I'm not mistaken I'd sit next\nto Shun-kun and copy the way through the caves\nwith a pencil while watching the screen."
        su "「Here's this. 」"
        "A large, colorful insert that comes out\nof the box with the instructions.{p}If you gently open the folded up back side,"
        "there are poorly-written characters,\nand things like maps and charts with pictures."
        "After that, there are pictures\nof monsters where the layout collapsed."
        "I remember!"
        fn "「You kept that?{p}\ \ This is kind of embarrassing...\n\ \ Ah, I made a mistake with that character. 」"
    
        show su 001 with dis
        
        su "「[fn]-san... {p}\ \ {nw}"
        show su tailwag 01 with dis
        extend "You remembered this game for me, I'm so happy♪ 」"
    
        show su 004 with dis
        
        su "「We got lost in the end.\n\ \ When it was time to stop playing, we couldn't save. 」"
        "An hour a day game."
        "I look and see \"entrance\" there, but no \"exit\".{p}Looks like we got really confused."
        "The same path had been drawn 5 or 6 times\nin overlapping black lines."
        fn "「We did that? 」"
    
        show su 002 with dis
        
        su "「Yeah. Both of us got sad and cried. {p}\ \ When father came to see what happened,\n\ \ he asked us, 『Are you fighting?』 」"
        fn "「Hahaha, that's embarrassing too. 」"
    
        show su 001 with dis
        
        su "「After that I didn't play it for a while.{p}\ \ It stayed in the back of a drawer for a long time,{p}\ \ but after you left I started it again. 」"
    
        show su tailwag 01 with dis
        
        su "「I made it out of the dungeon and cleared it. 」"
        fn "「Really?{w} Didn't you want to throw away\n\ \ these sloppy notes that weren't helpful at all? 」"
        "These crude characters and lopsided pictures\nare evidence of myself in those days. {p}It feels half charming, half embarrassing."
        
        show su 005 at briefzoom
    
        su "「N-{w=.3}no way! 」"
    
        show su 002 with dis
        
        su "「It's a memory. Of you and me. 」"
        "He places it on his lap and lovingly gazes\nat the scrap of paper."
        "That scrap of paper distracts him for a short time\nwhenever he feels sad about me being gone."
        "Even those poor illustrations\nwere helpful to him..."
        fn "「Hey, do you want to play that game? 」"
        
        show su tailwag 01 at jump_up
    
        su "「Yes! 」"
        "A small cartridge connected us here on that day.{p}In the time we were separated,\nthe switch is turn on."
        
        stop music fadeout .5
        play sound button2_007
        pause 1
        play sound se_012 
        "{cps=15}Journal 1 has been lost {p}{nw}"
        play sound se_012
        extend "{cps=15}Journal 2 has been lost {p}{nw}"
        play sound se_012
        extend "{cps=15}Journal 3 has been lost"
        "{cps=15}Sorry."
        
        show su 001 with dis
    
        su "「... 」"
        fn "「... 」"
        
        jump end09
    
###############################################
label shin09:
    
    $ event_name = _("Who went into the forest...?")
    $ love_shin += 1
    $ focus_character = "shin"

    scene map
    stop music
    hide screen forest09
    scene path with dis
    play music cicada01

    "So I was out on another walk in the village\nwhen I noticed a figure entering into the forest."
    
    scene black with wipeleft
    pause .1
    
    scene forest enter
    show si 501 at center
    with wipeleft
    pause .2
    scene black with wipeleft
    pause .1
    scene path with dis

    "Shin-kun?{p}Well, I think so at least..."
    "I didn't even have time to call out\nas a backpack-carrying little figure\ndisappeared inside."

    scene forest enter with Dissolve(1)
    
    "What could there be to do in the woods?{p}Foraging for edibles...?{w} That can't be.{p}But still, is it okay for them to go in alone?"
    menu:
        "Go after them.":
            jump shin09_follow
        "Maybe I saw something wrong.":
            jump shin09_ignore

    ##########################################
    label shin09_follow:

        $ love_shin += 1
        
        "I guess I should go after them.{p}I don't know if it really was Shin-kun,\nbut if it is him, it's dangerous to go alone."
        
        scene black with Dissolve(1)
        stop music fadeout .75
        play sound step13b
        pause 1
        scene forest center with dis
        play music free22
    
        "At any rate, the weeds here are amazing."
        "There's probably enough to keep people out,\nbut I slowly pushed my way in through\nthe animal trail into the forest."
        "I never came in here back in the days,\nbut it still feels like I got lost in a new place."
        "No wait,{w=.3} I think I *am*\ncompletely lost in a new place."
        "When we played in the forest\nwe entered from somewhere else\nso I'm stuck relying on the animal trail alone."
        "...{w} even so, it's pretty hot.{p}The trees' foliage blocked some of the sunlight's\nwarmth, but on the other hand it's humid."
        "With that in the rustic air,\nthe moisture is killing me."
        "So far, I'm buried in the weeds,\ntripping on rocks, walking on an uneven path,\nand sometimes sliding in mud."
        "The merciless path and the heavy uncomfortable\natmosphere have steadily been cutting\naway at my stamina."
        "This is supposed to be a nostalgic scent for me,\nso maybe it's because of the fatigue I'm hating it,{w=.3}\nor maybe it's because I'm used to the city air now."
        fn "「{cps=10}*huff*... *huff*... 」"
        "I could feel how heavy each breath was.{p}Between the sweat and humidity my clothes\nwere so uncomfortable."
        "I'm fighting with the overgrown weeds in every way.\nI only remember the uneven ground\nas being a pain in the ass."
        "I grabbed the weeds trying to vent my anger out,\nand somehow it supported me as I tore off on ahead."
        "...I wonder if it really was Shin-kun?{p}He's not really the type to exercise much,\nand this isn't a path any normal person would take."
        "For starters, that gap in the grass isn't a real\nentrance, and no one who doesn't really know this\nforest in and out would really go in{w=.3}, right?"
        
        play sound bosu34
        show forest center at hshake
        
        fn "「Wah! 」"
        "It seems like I slipped on the ground."
        "Even though there was a tree to keep me\nfrom falling, I'm just about tapped out,\nand a break is sounding good."
        "What should I do?"
    
        if shin_step1 == True:
            jump shin09a
        else:
            jump shin09b
    
    ##########################################
    label shin09a:
        menu:
            "Can't go on, I should rest.":
                jump shin09_rest
            "Try calling his name.":
                jump shin09_call
            "Keep going until I fall over tired.":
                jump shin09_continue
    
    ##########################################
    label shin09b:
        menu:
            "Can't go on, I should rest.":
                jump shin09_rest
            "Try calling his name.":
                jump shin09_call
    
    ##########################################
    label shin09_rest:

        $ love_shin -= 1
        $ renpy.music.set_volume(0.5, 0.1, channel = "music")
        
        "W-well, it's useless to continue now.{p}I tried looking for a nice looking place\nand settled on the loose ground."
        
        play sound si_gasa03
        
        "T-there's no way Shin-kun could be here.{p}Since I'm almost at my limit,\nI don't know how he could ever go down this way."
        "In that case,\ndid I really mistake my eyes earlier?"
        "No,{w=.3} I can't think of any other possibility.\nBesides, if someone came here\nwouldn't they leave a better trail?"
        "If there was something like that,\nthis path couldn't even be an animal trail."
        "It's impossible no matter how I think about it.{p}Impossible, completely impossible."
        "If Shin-kun was lost in this forest,{w=.3}\nor so I reluctantly thought,\nI would constantly warn myself about it."
        
        stop music fadeout 1
        pause .5
        scene black with Dissolve(.5)
        pause .2
        play music free0428
    
        "The way back,{w} and the way I made by getting here,\nI've lost track of both. And when I was taken out\nof the forest I was completely exhausted."
        "I'll probably have terrible muscle aches tomorrow."
        "I will also definitely try calling\nShin-kun's house later, and I'm sure I'll\nget an answer saying he didn't go in."
        "...between all the mosquito bites, my muddy shoes,\nsoreness where the grass brushed against me,\nand all the soreness, today has been the worst!"
        
        jump end09
    
    ############################################
    label shin09_call:

        $ renpy.music.set_volume(0.5, 0.1, channel = "music")
        
        fn "「Shin-kuuun!{p}\ \ If you're here, answer me! 」"
        "I yelled out as loud as I could into the forest.{p}...however, there was no answer."
        "N-{w=.3}...no more...{p}{nw}"
        stop music fadeout 1
        extend "I dragged myself over."
        
        play music wind_noise 
        $ renpy.music.set_volume(0.5, 0.1, channel = "music")
    
        "The stirring of the trees, {p}the buzzing of the insects,{p}the cries of the birds and animals."
        "I could hear nothing else. {p}Suddenly, I felt so anxious."
        
        $ renpy.music.set_volume(0.6, 0.1, channel = "music")
    
        "I've always made light of the place\nI played in back then, but do I\nhave any memories of this place?"
        "Or maybe memories of coming in this deep?"
    
        $ renpy.music.set_volume(0.7, 0.1, channel = "music")
        
        "I followed this inscrutable path,\nbut could I have lost the way back...?{p}No wait, aren't I lost already?"
        
        show over black at fadein_slow
        $ renpy.music.set_volume(0.8, 0.1, channel = "music")
    
        "My agitation was worsening in this eerie forest."
        "I tried not to think about it\nas best I could, but whenever I strayed\nto the negative it got worse."
    
        $ renpy.music.set_volume(1.0, 0.1, channel = "music")
        
        "Since I went on a random walk,\nI have nothing on hand.{p}Food and water of course,"
        "but I need something I could wield.{p}{nw}"
        stop music fadeout 1
        extend "What should I do?{p}If I was attacked by a wild animal..."
        
        play sound don17_a
        hide over black
        show forest_center at hshake
        show over black at hshake
        pause .2
    
        "{size=+15}Hiee-!"
        "Suddenly I heard sounds from the side,\nand I felt completely afraid.{p}As I instinctually back away I saw..."
    
        show si 501 at center behind over with dis
        
        si "「...{p}\ \ [fn]? 」"
        "What...?"
        fn "「{cps=10}Shin...{cps=40}kun{cps=10}...? 」"
        
        show over black at fading(0, 1.5)
        play music daily05
        $ renpy.music.set_volume(0.7, 0.5, channel = "music") 
    
        $ event_name = _("One day in the woods, I met Shin-kun")
        
        si "「What are you doing in a place like this? 」"
        fn "{size=+15}「THAT'S WHAT I WANTED TO\n\ \ ASK！ 」" 
        "Out coming from the grass was the figure\nI saw earlier for a moment going into the forest,\nthe backpack-carrying Shin."
        "I-I was almost about to cry!{p}Stupid Shin-kun!"
        fn "「Even after I thought I saw and came after you,\n\ \ I couldn't find you, the path was rocky,\n\ \ and I got lost. 」"
    
        show si 510 with dis
        
        si "「You came after me?{w} Why? 」"
        fn "「Well, isn't it dangerous to go\n\ \ into the forest alone!? 」"
    
        show si 505 with dis
        
        si "「You... were worried about me? 」"
        fn "「Of course I was! 」"
    
        show si 501 with dis
        
        si "「... 」"
    
        show si 502 with dis
        
        si "「But if you get lost yourself,\n\ \ then what's the point? 」"
        fn "「Ugh...{w} no, that's... 」"
        "He's hitting where it hurts.{p}It's true, so I can't argue against that."
    
        show si 501 with dis
        
        si "「So I was right?{w} Anyway, from the look of things\n\ \ you didn't bring any insect spray?{p}\ \ They bite you know. 」"
        "Shin-kun pointed at his slim neck\nwith his finger as he said that.{p}When I touched the same area, it was true."
        "There was a bite.\nWait, it's not just there,\nit's all over."
    
        show si 504 with dis
        
        si "「Oh well then.{p}\ \ I have some ointment, so wait there. 」"
        
        hide si with wipe_right
        play sound tyakuO
        
        "As he talked, he put down his backpack\nand pulled it out."
        "He took off the cap,\nsqueezed some onto his fingertip,\nthen rubbed the back of my neck."
        fn "「T-thanks. 」"
        "My neck was rubbed by a soft paw pad.{p}That warm gentle feeling was\naccompanied by a ticklish feeling from the fur."
        "He was touching my neck,\nbut I got a shiver from just that,\nso if he keeps touching me like this..."
    
        show si 501 with dis
        
        si "「Would you mind standing for a bit? 」"
        fn "「Huh? O-okay. 」"
        
        play sound standup
    
        si "「Face that way. 」"
        
        play sound step13b
        
        fn "「Like this? 」"
    
        show si 504 with dis
        
        si "「Wow, they really did get your back too.{p}\ \ Pull up your shirt for me? 」"
        "No, you're so bold to do that here\nwhile we're alone Shin-kun..."
        
        play sound puu75
        "Ah, that's-{p}{nw}"
        play sound puu75
        pause .1
        play sound puu75
        extend "Aaaaaahh---"
        
        hide message box
        scene black with dis
        pause .3
        
        scene forest center
        show si 510 at center 
        with dis
    
        si "「Right, done. 」"
        fn "「Thanks. 」"
        si "「You're welcome.{p}\ \ {nw}"
        show si 503 with dis
        extend "It's just, couldn't you stop making\n\ \ weird noises when I was rubbing you? 」" 
        fn "「Hey, it was ticklish. 」"
        "Usually when I feel fingers on my back it's itchy,\nbut getting touched by a furry finger tickles me,\nand I tried so hard to keep my voice down."
        
        show si 505 with dis
        pause .5
        show si 501 with dis
    
        si "「I see.{w=.3} So human skin is sensitive when exposed? 」"
        fn "「Yeah, it is.{p}\ \ And with your fur so soft,\n\ \ it just makes things even more ticklish. 」"
    
        show si 510 with dis
        
        si "「Sorry, I didn't realize that. 」"
        fn "「Hahah,\n\ \ it didn't feel that bad, you know? 」"
    
        show si 511 with dis
        
        si "「Well... 」"
        "I was unintentionally smiling wide\nat the unusually meek Shin-kun.{p}He's so cute."
        
        play sound wind_noise
        pause 1.2
    
        fn "「Oh, uh...{w} what do we do after this? 」"
    
        show si 501 with dis
        
        si "「Well... let's see.{p}\ \ For now, how about we leave the forest? 」"
        fn "「I can agree to that. 」"
        
        stop music fadeout .75
        scene black with dis
        pause .3
        
        scene forest enter
        show si 510 at center
        with dis
        play music step13b
    
        si "「Be careful there.\n\ \ The grass hides it, but there's a hole. 」"
        fn "「Oh, okay. 」"
        "Amazing, Shin-kun.{p}He's gliding through all the points I had trouble with."
        "Additionally, since he told me about the\ndangerous parts, the same path I took earlier\nis a lot easier now."
        "Well even if I say that it's not like it's being\npaved, and with body differences there wasn't much\nelse I could do but push away the weeds in my way."
        "When did Shin-kun get so used to the wild...?{p}Or did living in the city rust my senses away?"
        si "「That reminds me. 」"
        fn "「What?{w} {nw}"
        stop music
        play sound hit78
        extend "Whoa!? {nw} 」{w=.1}"
        pause .1
        show si 505 with dis
    
        hide si with wipe_right
        
        "I was preoccupied with talking,\nand my feet promptly fell into the grass."
        "But the moment I tipped over,\nShin-kun grabbed me and somehow\nmanaged to keep me upright."
    
        show si 501 at center with dis
        
        fn "「T-thanks. 」"
        si "「Be careful.{w=.3} With how wet the grass is,\n\ \ it's easy to slip.{w} {nw}"
        play music step13b
        extend "And about today,\nwould you mind not telling anyone about it? 」"
        fn "「Sure, but why? 」"
    
        show si 509 with dis
        
        si "「You know.{p}\ \ {nw}"
        show si 501 with dis
        extend "I have a secret base over there,\n\ \ so I don't want anyone to know. 」"
    
        show si 510 with dis
        
        si "「Especially{w=.3} Kounosuke. 」"
        "Oh I see. {p}If Kounosuke ever finds out,\nthen soon everyone will know."
        fn "「Sure. I promise. 」"
    
        show si 501 with dis
        
        si "「Please do. 」"
        
        #!#Hide message box
        scene black with dis
        stop music fadeout .5
        pause .5
        scene path with dis
        play music tam_n06
        
        fn "「We're finally out! 」"
        "I wonder how much I've walked.{p}I totally lost my sense of time,\nso it felt both long and short."
        "If I consider the sun's position, no amount\nof time passed since I went in{w} ... I think.{p}I can't say since I don't have a watch."
    
        show si 501 at center with dis
        
        si "「You'll be fine at this point, right? 」"
        fn "「Yeah. Thanks Shin-kun. 」"
    
        show si 504 with dis
        
        si "「You're welcome. 」"
    
        show si 501 with dis
        
        si "「Well I'm going home. What are you going to do? 」"
    
        show si 502 with dis
        
        si "「If you like, I could give you some tea in apology? 」"
        fn "「Eh, really?{p}\ \ I guess I'll take up your offer then. 」"
        
        #!#Message box hide
        scene black with Dissolve(1)
    
        "That afternoon, I had a bit\nof a refined tea time at Shin-kun's house"
        "Still, what was Shin-kun doing in that forest?{p}Maybe I'll ask the next chance I get."
        
        jump end09

    #######################################    
    label shin09_continue:

        stop music fadeout .25
        play music free0470
        
        "N-no, there's no way I can rest here.\nWhat if Shin-kun collapsed up ahead!?{p}That's right, I have to go on!"
        "I mustered up my willpower, and charged madly in.{p}Shin-kun is waiting for me to save him up ahead!\nWho says I couldn't save him!?"
        "I don't even know what I'm thinking anymore.{p}I gave myself an indisctinct yell to cheer up,\nand I recklessly put myself another step forward."
        
        stop music
        play sound bosu31
        show forest_center at hshake
    
        "...{w} ow{w}{nw}"
        play music wind_noise
        $ renpy.music.set_volume(0.5, 0.1, channel = "music")
        "First I notice the pain,{w=.3}\nthen I remember leaning over,{w=.3} falling,{w=.3}\nand now I'm on top of the bushes."
    
        play sound bosu34
        
        fn "「... 」"
        "I got up in silence.{w} Yeah,\nI'm really reaching my limit.{w} As I stood up,\nI had to smile a bit when I looked at myself."
        "Why am I taking this so seriously?{p}I still don't know for sure if it was\nShin-kun I saw before."
        "I can't do it anymore.{p}I'm done.{w} I'm out."
        "...{w} hmm?{p}This is{cps=10}...{cps=40}{p}What I noticed then was a huge coincidence."
        "Over where I fell,\nthere was a side path in the grass."
        "Since I went in normally I probably overlooked it,\nbut it seems someone came by recently,\nand the grass has been trampled."
        "And of course, I didn't do that.{p}So could Shin-kun be up ahead?"
        "I'm not even thinking calmly now.{p}It was a belief based on instinct,\nand I whipped my body on to that path."
        
        stop music fadeout .75
        scene black with Dissolve(1)
        play music step13b
    
        "I went on as if lead to it,\nbut how much walking will it take?{p}It wasn't really that far."
        
        scene white with Dissolve(1)
        stop music fadeout .25
        pause .3
    
        fn "「Mn... 」"
        
        scene forest meadow with Dissolve(1)
        play music cicada01
        $ renpy.music.set_volume(0.5, 0.1, channel = "music")
    
        "Suddenly the high summer sunlight hit my eyes.{p}Looks like I came into some sort of clearing."
        "I suppose a forest\ncan have places like this occassionally."
        "No hands have touched this place,\nyet the trees have thinned\nfor a natural meadow like this..."
        
        stop music fadeout .75
    
        "{size=+15}!!!"
        
        play music free0531
    
        $ event_name = _("Is something wrong with Shin-kun?")
        
        "Shin-kun was over there.{w} Here where the forest\nopens inside, there was one large tree, and at its\nroots was a figure lying its head against it."
        "Below that happy head a backpack was set down,\nand while I don't see any wounds,\nI won't know unless I get closer to take a look."
        "I forgot about my fatigue, then ran on over."
        
        scene black with wipeleft
        
        scene forest tree
        show si 504 at center
        with wipeleft
        pause .15
    
        fn "「Shin-kun...?{w} Shin-kun? 」"
        "I wasn't mistaking anything, it was Shin-kun.{p}His eyes were closed like he was asleep\nand he didn't say a single thing."
        "I don't see him hurt anywhere,\nb-but w-what should I do?"
        menu:
            "F-first off, resuscitate him!":
                jump shin09_cpr
            "Calm down and call his name.":
                jump shin09_shout
    
    #########################################
    label shin09_cpr:

        $ event_name = _("Basking in the Sun")
        
        "A-anyway, I need to do artificial respiration!{p}Hee,{w=.3} hoo,{w=.3} hee, {w=.3}hoo,{w} okay then!"
    
        show si 510 with dis
        
        "I'm all ready, my lungs are filled to capacity,\nand now I just need to go to Shin-kun's lips...{w}{nw}"        
        show si 505 with dis
        stop music fadeout .25
        play sound hit_p09
        show forest tree at hshake
        extend "{w=.25}{nw}"
        show forest tree at hshake
        extend "{w=.25}{nw}"
        show forest tree at hshake
        extend "{w=.25}{nw}"
    
        "{size=+30}OOF"
    
        show si 512 with dis
        
        si "「W-what were you going to do\n\ \ to someone who was asleep!? 」"
        
        scene black with Dissolve(1)
        
        scene forest tree
        show si 511 at center
        with Dissolve(1)
        play music daily03
    
        fn "「S-so then, you didn't fall,\n\ \ and you don't feel ill or anything? 」"
        si "「Yes. {w=.3}I was just sleeping.{p}\ \ I dozed off after reading a little. 」"
        "Oh come on...{p}If that was the case,\nyou could have slept a bit longer."
        "No wait, that's not right."
        fn "「I was sure you fell and hit your head. 」"
    
        show si 509 with dis
        
        si "「...{w} sorry for worrying you.{p}\ \ {nw}"
        show si 512 with dis
        extend "Still, there's no need for artificial respiration! 」" 
        fn "「No, that was because I was in a hurry. 」"
    
        show si 510 with dis
        
        si "「... 」"
        fn "「Uhh,{w} I'm sorry. 」"
        si "「You don't have anything to apologize for. 」"
        fn "「No, but still... 」"
        si "「... 」"
        "Shin-kun suddenly looked away.{p}Now I've done it.\nLooks like I made him completely mad."
        fn "「A-anyways, what are you doing here? 」"
        fn "「You have air conditioning at home,\n\ \ so there's no need to come out\n\ \ where it's all humid. 」"
    
        show si 501 with dis
        
        si "「... 」"
        "Shin-kun's looking this way.{p}He's smiling politely for now, but how are things?{p}Are they going south?"
    
        show si 510 with dis
        
        si "「I don't like being alone in that house. 」"
        fn "「Huh?{w} Why? 」"
        si "「... 」"
    
        show si 509 with dis
        
        si "「... 」"
        si "「...because... 」"
        fn "「What? 」"
        "I couldn't hear what he whispered in such a\nlow voice.{w} But{w=.3} it did seem like he said\n\"because it's lonely\"..."
    
        show si 510 with dis
        
        si "「...that place is so pointlessly big,\n\ \ it's so peaceful,{w=.3} too peaceful\n\ \ that I can't calm down. 」"
        si "「There's air conditioning, but that's is. 」"
        fn "「Shin-kun...{w=.3} do you hate that mansion? 」"
    
        show si 501 with dis
        
        si "「Who can say?{w} 　I'm used to it...{p}\ \ {nw}"
        show si 510 with dis
        extend "It's just that it feels better outside.{p}\ \ Even on this humid day. 」"
        fn "「Still, you don't need to come\n\ \ in this deep, right? 」"
    
        show si 511 with dis
        
        si "「I tried to look for good places in the village.{p}\ \ {nw}"
        show si 501 with dis
        extend "Up until I ended up falling asleep on the village\n\ \ outskirts and Kounosuke took a picture. 」"
        "What!?{p}Pictures of Shin-kun's sleeping face!?"
    
        show si 503 with dis
        
        si "「Since then, it's been hard\n\ \ finding a place away from prying eyes. 」"
        fn "「By the way, what happened to that picture? 」"
    
        show si 501 with dis
        
        si "「I burned it in the oven at home.\n\ \ Along with the negatives. 」"
    
        show si 510 with dis
        
        si "「It was when Kounosuke brought it over\n\ \ to show it, laughing. 」"
        fn "「I-I see. 」"
        "Hmm, well that's a shame."
        "...but then,{w=.3} Shin-kun's eyes look so serious,\nso I shouldn't pursue it any further."
        
        play sound wind_noise
        pause 1
        show si 501 with dis
    
        fn "「...it's so peaceful. 」"
        si "「It's because the trees block out the noises\n\ \ from the village.{w} But you can still hear\n\ \ the wind in the trees and the insects, right? 」"
        fn "「Eh?{w} Yeah, that's true. 」"
    
        show si 510 with dis
        
        si "「That's why it's fine.{p}\ \ It's peaceful yet noisy,\n\ \ so I can really relax. 」"
    
        play sound wind_noise
        
        "It's peaceful,\nbut if you listen closely you can hear so much."
        "The wood shaking in the winds,{w} insect buzzing,{p}and then, that vaguely familiar, annoying tinnying."
        fn "「Ah! Dammit! 」"
    
        show si 501 with dis
        
        si "「What's wrong? 」"
        fn "「A bug bit me. 」"
        "When I checked myself again,\nI must have been bitten\nso many times on the way here."
        "My arms, my neck, my back,\n{w=.3}just about everywhere."
    
        show si 502 with dis
        
        si "「[fn], you didn't use any repellant,\n\ \ did you? 」"
        fn "「That's because I didn't think\n\ \ I'd be going into the forest. 」"
    
        show si 501 with dis
        
        si "「Oh whatever. {w=.3}I'll get you some medicine later. 」"
        fn "「Dammit, here too!? 」"
    
        show si 502 with dis
        
        "Shin-kun watched and laughed as I\nchecked myself over again."
    
        show si 501 with dis
        
        si "「Well then,{w=.3} I suppose it's time to go home. 」"
        fn "「Oh, sure. 」"
        si "「Sorry about today.{w=.3} It looks like\n\ \ it's my fault you're flapping like that.{p}\ \ {nw}"
        show si 502 with dis
        extend "Would you like to come over later? 」"
        fn "「Huh?{w=.3} Is that okay? 」"
        si "「Yeah.{p}\ \ I want to treat you to a lunch,{w=.3}\n\ \ {nw}"
        show si 501 with dis
        extend "but is that a bother for you? 」" 
        fn "「No, not at all! 」"
    
        show si 502 with dis
        
        si "「Then I suppose I will invite you over for a meal?{p}\ \ I probably can't compare well to Torahiko's,\n\ \ but I can definitely win with Western-style food. 」"
        fn "「Ooh, this is exciting. 」"
        si "「You're such a glutton, just like always. 」"
        fn "「N-no I'm not.{w} You just invited me over. 」"
        si "「Hmhm. 」"

        scene white with Dissolve(1)
    
        si "「Well thanks for your trouble up to this point.{p}\ \ And, thanks for worrying about me, {w=.3}[fn] 」"
        fn "「Wait, what? 」"
        si "「Nothing.{p}\ \ Never mind that, is there anything you can't eat?\nAnything you want to request? 」"
        
        $ shin_key1 = True 
       
        jump end09
    
    ########################################
    label shin09_shout:

        $ event_name = _("Secret Place")

        $ renpy.music.set_volume(0.5, 0.1, channel = "music")
    
        fn "「Shin-kun! Shin-kun! 」"
        "He might have fallen and hit his head.{p}I tried shaking him as best I could without\nmoving his head, and called out to Shin-kun."
        si "「Mm... 」"
        
        show si 510 with dis
        stop music fadeout .75
    
        si "「[fn]...? 」"
    
        play music cicada01
        
        fn "「Shin-kun!?{w} What a relief. 」"
        "After calling to him so many times,\nShin-kun's eyes were slowly opening.{p}Oh good, he seems to be waking up..."
    
        show si 505 with dis
        
        si "「[fn]!? 」"
        fn "「Oh, yeah. Are you okay? 」"
    
        show si 512 with dis
        
        si "「Why are you here!? 」"
        fn "「W-why? 」"
        "It looks like he's still upset.{p}He jumped to his feet away from me,\nand he's suddenly speaking so threateningly."
        fn "「I saw you enter the forest earlier,\n\ \ so I came after you after getting worried.{p}\ \ After that, I saw that you fainted. 」"
        fn "「But, you seem to be okay.{w} That's good.{w=.3}\n\ \ My heart was pounding when I found you. 」"
        si "{size=+15}「OF COURSE I'M ALRIGHT! 」"
        "Shin-kun raised his voice even further.{p}*sniff* {w=.3}I'm glad he's back to normal,\nbut I really was worried."
        fn "「B-but if you hit your head,\n\ \ you should go get that... 」"
    
        show si 501 with dis
        
        si "「... 」"
    
        show si 503 with dis
        
        si "「It seems like you misunderstood things\n\ \ from the very start. 」"

        stop music fadeout .75
        scene black with Dissolve(.5)
        pause .5
        
        scene forest tree
        show si 510 at center
        with dis
        play music daily04
        
        fn "「You were just sleeping!? 」"
        si "「...{w} {nw}"
        show si 511 with dis
        extend "yes. 」" 
        "Uh, then,{w=.3} so Shin-kun was napping?"
        fn "「Now that I think about it,\n\ \ you used the backpack as a pillow. 」"
        si "「I have stuff besides that,\n\ \ but it's mostly stuffed with towels. 」"
        fn "「...{w} why over there? 」"
    
        show si 510 with dis
        
        si "「... 」"
    
        show si 512 with dis
        
        si "「Where I sleep is none of your business! 」"
        fn "「Yes!{w=.3} That's true. I'm sorry. 」"
    
        show si 503 with dis
        
        si "「No, I'm sorry.{p}\ \ I know things won't change by yelling at you. 」"
        "Shin-kun calmed himself down\nby shaking his head back and forth,\nthen took a deep breath."
    
        show si 501 with dis
        
        si "「...{w} before,{w=.3} I've dozed off\n\ \ like that in other places. 」"
        "Dozing...{w=.3} wait,\nhe's all prepared and resolved to sleep..."
        "I was so flustered earlier I didn't notice,\nbut there was a vinyl sheet spread out.{p}Just enough space for one."
    
        show si 510 with dis
        
        si "「That time,\n\ \ Kounosuke walked up all of a sudden.{p}\ \ Seems like he took a picture of me sleeping. 」"
        fn "「Huh. 」"
    
        show si 502 with dis
        
        si "「Anyways, when he came by laughing\n\ \ wanting to show it off,\n\ \ I disposed of it and the negatives. 」"
    
        show si 512 with dis
        
        si "「Well if that happens,\n\ \ I have to be vigilant don't I? 」"
        fn "「Y-yeah... 」"
        "The negatives were disposed...{p}I know there are consequences,\nbut sucks for Kounosuke."
        fn "「Well if it was him, wasn't it just a joke? 」"
    
        show si at jump_up
        
        si "「Even if it was a joke, it was horrible!{p}\ \ Everyone at school who saw it talked about it! 」"
        fn "「Right! Sorry! 」"
        "The normally emotionally-controlled Shin-kun shouted,\nand my spine instinctively stiffened.{p}Hmm, I guess I did overdo it."
    
        show si 504 with dis
        
        si "「...{w} and that's how it is. 」"
        fn "「I see... 」"
        "To summarize,{w} he wanted to take a nap,\nbut he was afraid Kounosuke would take a picture."
        "So he chose to come here\ninto the forest away from people."
        "...{w=.3}did he really need to come\nall the way out here for a nap?{p}I'm probably the only one thinking that."
        
        show si 510 with dis
        $ renpy.music.set_volume(0.5, 0.1, channel = "music")
    
        si "「[fn]... 」"
        fn "「Yes?!!{w} W-what? 」"
        "I looked into the two eyes of the black cat,\nwho was unsmiling and held a gloomy aura."
        
        stop music fadeout .75
        show si 510 big at center_big with dis
    
        si "「{cps=10}If you blab about this to anyone,\n\ \ I won't ever forgive you for it -{p}\ \ {nw}"
        play sound metalhit001
        extend "even if we're childhood friends. Got it? 」"
        fn "「{cps=10}...{cps=40}{p}\ \ {cps=10}YES-MY-MASTER. 」"
        "Even if it was summer, I felt\na terrible chill down my back."
        
        jump end09
    
    ###########################################
    label shin09_ignore:

        $ love_shin -= 1
        
        "No way, even if it was Shin-kun\nhe wouldn't go into this place all alone."
        "I only saw for a second,\nso maybe I mistook who it was."
        "It was from far away too,\nso if I remembered as hard as I can,\nI'm still not confident it was him."
    
        scene forest center with dis
        
        "It looked like they went in only a little bit,\nbut it's an overgrown animal trail, so I can't\nbelieve any normal person would go in there."
        "So, did I see it wrong?{p}I'm still worried, but I went back\nto the village with that in my mind."
        
        scene black with dis
        stop music fadeout .75
        
        "By evening,\nI called Shin-kun's house for peace of mind."
        "And when I asked about the day,\nI was told Shin-kun did not go into the forest."
        "So then, I really was mistaken right?{p}I still have this feeling\nI saw him for a second though."
        
        jump end09
        
###############################################
label tatsuki09:

    $ love_tatsuki += 1
    $ focus_character = "tatsuki"

    scene map
    stop music
    hide screen tatsukihouse09
    $ renpy.music.set_volume(0.45, 0.0, channel = "music")
    play music cicada01
    scene tatsukihouse inside with Dissolve(1)
    pause 1.5
    
    fn "「Afternoon!{p}\ \ Is Tatsu-nii here? 」"
    
    show ta 001 at center with dis
    
    ta "「Yo, [fn].{p}\ \ You came at a good time. 」"
    fn "「What makes this a 'good time'? 」"
    
    play music daily02 fadein 1.5
    show ta 002 with dis

    ta "「Because Shun's free. 」"
    fn "「Ah. 」"
    
    show ta 001 with dis
    
    ta "「Shun probably spends all his time playing\n\ \ games and never going out, so I call him\n\ \ up sometimes to hang out. 」"
    fn "「Hmm, I see. 」"
    "Tatsu-nii always was popular with the\nyounger kids.{p}He gets along pretty well with Shun-kun."
    
    show ta 008 with dis

    ta "「Anyway,{w=.3} I thought about calling him over,\n\ \ but you try it this time. 」"
    fn "「Ehh,{w=.3} even if I were to do that all of a sudden,\n\ \ I don't know what to say... 」"
   
    show ta 002 with dis
    
    ta "「It'll be all right,{w=.3} don't worry.{p}\ \ C'mon, time's wasting. 」"
    hide ta with wipe_right
    play sound call02
    pause .5
    play sound call05
    pause .3

    who "「Yes, this is Kodori. 」"
    fn "「Ah- 」" 
    
    menu:
        "A. You wanna hang out together?":
            jump tatsuki09_hangout
        "B. Help me!":
            jump tatsuki09_help
        "C. Let's go out and hit on people.":
            jump tatsuki09_goout

    #######################################
    label tatsuki09_hangout:

        $ love_shun += 1
        $ love_tatsuki += 1
        
        su "「Oh, [fn]-san? 」"
        su "「Are you at Tatsuki-san's house?{p}\ \ Hang out together...{w=.3} Wow...{p}\ \ I'm looking forward to it!"
        su "I'll be right there, so please wait a bit. 」"
        
        play sound call05
        "*click*, {nw}"
        pause .1
        play sound call00
        extend "*boop*, {nw}"
        pause .1
        play sound call00
        extend "*boop*"
        
        fn "「Shun-kun is a good boy.{p}\ \ He said he'll be here soon. 」"
        
        show ta 001 with dis
        
        ta "「Well then, if Shun-kun's coming, what\n\ \ should we do? 」"
        
        show su 001 at farright with wipe_right 
        
        su "「Good afternoon!{p}\ \ {nw}"
        show su 002 with dis
        extend "Tatsuki-san, [fn]-san, I came over to\n\ \ play. 」"
        
        fn "「Whoa, that was fast! 」"
        
        jump end09

    ########################################    
    label tatsuki09_help:
        
        fn "「I-it's terrible! 」"
        fn "「I've been caught by a Green Giant Max\n\ \ Great Iguana Dragon,{w=.3} and it's a huge crisis! 」"
        fn "「You're the only one who can save me!{p}\ \ Come quickly! 」"
        su "「You were caught by bad guys, [fn]-san?{p}\ \ You'll be saved if I come, right? 」"
        fn "「Uh,{w=.3} yeah. 」"
        su "「Okay, I understand.{p}\ \ Once I prepare my equipment I'll be right over- 」"
    
        play sound call05
        "*click*, {nw}"
        pause .1
        play sound call00
        extend "*boop*, {nw}"
        pause .1
        play sound call00
        extend "*boop*"
        
        fn "「The Ultra Green Giant Max Great Dragon is in\n\ \ the Midoriya Group's building... 」"
        fn "「Wait,{w=.3} equipment?\ \ Wait, what?{p}\ \ Shun-kun??? 」"
        
        play sound call00
        "*boop*, {nw}"
        pause .1
        play sound call00
        extend "*boop*, {nw}"
        pause .1
        play sound call00
        extend "*boop*"
        
        fn "「No good,{w=.3} he already hung up. 」"
        
        show ta 004 with dis
    
        ta "「Who's a green iguana!? 」"
        fn "「Well, it'll be okay.{p}\ \ He said he'll be here soon. 」"
        
        show ta 008 with dis
    
        ta "「Really? I don't know about that. 」"
        "On that day, no matter how much time passed,\nShun-kun never showed up....."
        
        jump end09

    ####################################    
    label tatsuki09_goout:

        $ love_shun -= 1
        $ love_tatsuki -= 1
    
        fn "「Let's go out and hit on some people.{p}\ \ Our summer starts right here! 」"
        who "「Oh, [fn]-kun, is it?{p}\ \ Long time no see.{p}\ \ If you're looking for Shun, he already left. 」"
        "Huh?"
        "Shun-kun's voice is kind of deep...{p}His dad!?"
        ryo "「Want me to pass on the message? 」"
        "On the other end of the receiver, I could\nhear giggling."
        fn "「No,{w=.3} that won't be necessary.{p}\ \ Excuse me. 」"
        
        show ta 008 with dis
        
        "I was embarrassed as I quickly put the phone down.{p}I feel Tatsu-nii's cold stare behind me."
        "D-{w=.3}don't look..."
        fn "「Well, seems like Shun-kun went out.{p}\ \ Looks like you had nothing to worry about, and since\n\ \ there's no other way, how about just us two go out? 」"
        
        show ta 001 with dis
        
        ta "「...Yeah,{w=.3} maybe we can call over Tora.{p}\ \ Oh, I'll have to call his number, so you just\n\ \ make yourself at home. 」"
        "Uu,{w=.3} if there's a hole somewhere,\nI want to hide in it..."
        
        jump end09

###############################################
label juuichi09:

    $ love_juuichi += 1
    $ focus_character = "juuichi"
    $ event_name = _("Rain Poems")

    scene map
    stop music
    hide screen ricefield09
    pause .01
    play music free0258
    scene field2
    show over black 
    with dis
    

    "The once-sunny sky has been covered by clouds.{p}I only really noticed when the sunlight had\nstopped shining down on me."
    "There's a rumble of thunder in the distance."
    fn "「Uh-oh,{w=.3} looks like it's going to rain... 」"
    "I unintentionally mutter to myself at the sound.{p}It was sunny when I set out this morning,{w=.3}\nso I didn't think to bring an umbrella with me."
    "I look up at the sky,\nwondering whether I can get home before it\nstarts to rain."
    
    pause 1
    
    "A raindrop lands on my right hand."

    stop music fadeout 3
    call rain_set from _call_rain_set_11
    
    fn "「Damn it! 」"
    "As I start to run,{w=.3}\nthe rain strengthens,\nas though it were mocking me.{w}{nw}"    
    play sound2 rainfall loop fadein 10
    show raining at fading(0.0, 0.0)
    extend "{w=.01}{nw}"
    show raining at fading(1, 10)
    
    "My shoes make a wet squelching sound with each step,{w=.3}\nbut there's nothing I can do about it."
    "Earlier, I was thinking about\ngoing to the candy store,{w=.3}\nbut it would be a pain to go there now."
    "It seems the best course\nof action would be to go home."
    "...I'd like to think that this is giving\nme a break from the summer heat,\nbut I'm actually getting pretty cold."
    "As I think about that, I rub my arms."
    "I want to get home and take a nice, warm bath."
    "It'd be earlier than usual,\nbut given the pitiful state I'm in,\nI don't think Grandpa would mind."
    "While I'm walking along, thinking warm thoughts,{w=.3}\nthe bus stop suddenly enters my field of vision."
    "...Hm, the bus stop?{p}That means shelter, doesn't it?{p}I can get out of the rain!"
    "I remember a shelter being next to the bus stop,{w=.3}\ncausing my spirits to rise.\nUnable to help myself, I half-jog towards it."
    
    play sound step03
    scene black with wipe_right
    scene bstop 
    show over black 
    with wipe_right

    "Whew, saved.{w} Now I'll just wait out the rain."
    "Arriving at my destination,{w=.3}\nI put my hand on the steel door to enter."
    "It's then that I meet eyes with\nthe person who got here before me."
    fn "「Oh, Juuichi-san.{w} Hello. 」"
    
    play sound tm2_slidedoor000

    "I open the door and greet Juuichi-san,\nwho was already sitting inside."
    
    play sound free51
    show ju 001 at center with dis

    ju "「[ln]?{p}\ \ Seems like it's really coming down. 」"
    fn "「Yeah, it is.{p}\ \ It caught me by surprise.{w=.3}\n\ \ I know I'm human, but I feel like a drowned rat... 」"

    show ju 003 with dis
    
    ju "「... 」"
    "He doesn't say a word.{p}...Hmm,{w=.3} I did try to say something witty."
    "Unfortunately, it seems Juuichi-san is not amused."
    ju "「...Anyway, come in and dry yourself off. 」"
    fn "「If you insist.{p}\ \ Excuse the intrusion. 」"
    
    show ju 001 with dis
    
    ju "「It's not like this is my house.{p}\ \ There's no need to be so polite. 」"
    "He does have a point.{p}But, with the two of us in the shelter,{w=.3}\nit strangely seems like it's Juuichi-san's space."
    "I step inside, and decide to take off my wet shirt.{p}I don't have anything to dry off with,{w=.3}\nso should I just wring my shirt out and use that?"
    fn "「Excuse me for a second. 」"

    hide ju with wipe_right
    
    "I turn my back to him,\nand try to take off the shirt\nthat's stuck to my skin."
    "...I wonder why wet clothes\nare so difficult to get off."
    "I try lifting the hem of my shirt,{w=.3}\nbut it gets stuck on my shoulders."
    "Great, now I look like a criminal that's been\nput in a straightjacket. And my midriff's exposed.{p}...This is embarrassing beyond words."
    "But my shirt feels like it's\ngoing to tear if I force it further..."
    ju "「Hey,{w=.3} are you all right? 」"
    "Could he just not bear to watch my\ndesperate struggle against my shirt?{w=.3}\nHe spoke up."
    menu:
        "A. Could I get some help here?":
            jump juuichi09_help
        "B. It's ok, I got this.":
            jump juuichi09_nohelp

    #########################################
    label juuichi09_help:

        $ event_name = _("Once Past the Border, One May Do Anything")
        $ love_juuichi += 1
        
        "I don't think I've had help changing clothes\nsince elementary school, but these days it seems\nI need it more and more."
        "I hesitantly ask for his assistance."
        fn "「...Sorry,{w=.3} but can you please give me a hand? 」"
    
        show ju 001 at center with dis
        
        ju "「Sure.{w} [ln],{w=.3} lift up your arms. 」"
        "...Ah,{w=.3} that sounds like something a childcare\nworker would say.{p}While thinking that, I lift my arms as he asks."
        ju "「I'm taking it off now. 」"
        "He puts his fingers on my sides.{p}His slightly stiff fur tickles me."
        "Juuichi-san lifts my shirt up.{p}But, even with his help, my shirt sticks to me\nand refuses to come off."
    
        show ju 008 with dis
        
        ju "「...Hmm. 」"
        
        play sound pyoro45_a 
        show bstop at vshake
        
        fn "「Hyaah?! 」"
        "Suddenly,{w=.3} Juuichi-san shoves his hand up my shirt\nto try and get it off.{p}The sudden act makes me cry out in surprise."
    
        show ju 001 with dis
        
        ju "「This might tickle a bit,\n\ \ but you're going to have to put up with it.{p}\ \ Keep your arms raised. 」"
        "His hand wriggles around.{p}I desperately try to keep quiet."
        "It only lasts for a few seconds,{w=.3}\nbut it feels like an eternity."
        "Pulling his hand out,\nJuuichi-san lifts up the hem of my shirt,{w=.3}\nthis time easily removing it."
        "I say thank you as he hands me my shirt.{p}...I may be thankful,{w=.3}\nbut changing clothes like that is bad for my heart."
    
        play sound standup
    
        hide ju with wipe_right
        
        "Juuichi-san turns and rummages around in his bag.{p}While I'm trying to figure out what he's doing,{w=.3}\nhe stops, and turns to me."
    
        show ju 001 at center with wipe_right
        
        ju "「Here,{w=.3} dry yourself off with this.{p}\ \ Don't worry, it hasn't been used. 」"
        "He hands me a white towel."
        fn "「Oh, thanks.{w} You're a lifesaver. 」"
        "I take advantage of his kindness.{p}I feel like he's doing too much for me, though."
        "I wipe myself down with the fluffy, dry towel{p}My head,{w=.3} shoulders,{w=.3} arms,{w=.3} back,{w=.3} stomach... Wait."
        "I look down at my lower body.{p}Hmm,{w=.3} would it be rude of me to take off my jeans?{p}I hate the feel of wet denim..."
        "Well, since it's just the two of us here,\nit should be ok, right?"
        "With that decision, I wrestle with\nthe jeans clinging to me,\nand take them off."
        "Leaving my underwear on,\nI dry the exposed parts of my body."
        "Haah, that feels better.\nThey say being wet isn't\ngood for your mental health."
        fn "「Juuichi-san,{w=.3} thank you for the towel. 」"
        "After I finish drying myself off,\nI sit down next to Juuichi-san."
        "I might still be wet in some places,{w=.3}\nso I try to avoid contacting Juuichi-san\nas much as possible."
        ju "「...Don't worry about it.{p}\ \ Here, you should put this on. 」"
        
        play sound standup
        show ju 201 with dis
    
        "He takes off his blue jersey,{w=.3}\nand offers it to me."
        
        jump juuichi09_talk

    ###########################################    
    label juuichi09_nohelp:

        $ event_name = _("There's Nothing More Embarrassing than Asking")
        $ love_juuichi -= 1
        
        "It's too embarrassing to ask\nfor help getting undressed.{p}I'm not a kindergartener, after all."
        "I appreciate the offer, but politely decline."
        ju "「I see. 」"
        "Since I declined his offer,\nit'd look bad if I didn't get it off quickly.{p}I pull with a little more force than earlier."
        "My shirt makes protesting sounds as I pull.{p}I really start to get impatient at times like this,\nwhen things don't go my way."
        "Aaah, desperate times call for desperate measures!{p}I pull as hard as I can."
        
        play sound rip
        
        "Despite the protests coming from the stitching,{w=.3}\nI'm somehow successful in removing my shirt."
        "...I'm too scared to check whether it tore or not."
        "Why was that such a struggle?{p}I sigh to myself while wringing it out."
        "Maybe I should have asked\nJuuichi-san for help after all?"
        "While thinking that, I wipe myself off with\nmy semi-dry shirt. It doesn't do much,{w=.3}\nbut it's better than nothing."
        "Then, I hear a voice behind me."
    
        show ju 001 at center with dis
        
        ju "「[ln],{w=.3} use this. 」"
        "I turn around,{w=.3}\nand see a towel being presented to me."
        ju "「Don't worry, it's clean. 」"
        fn "「Oh, thanks, I needed that. 」"
        "Juuichi-san's nonchalant concern makes me feel cold.{p}Taking the offered towel,{w=.3}\nI quickly dry my head and upper body."
        "I take a look at my lower body.{p}Hmm, would it be rude to take off my jeans?"
        "Juuichi-san was kind enough to\nlet me borrow his towel, after all."
        "I take a glance outside.{p}Hm, looks like nobody's out there for now.{p}I ready myself, then start to remove my jeans."
        "Stripping down to underwear\nin front of somebody else,\nlet alone in a public place, is pretty pathetic."
        "...But this is all my fault\nfor not bringing an umbrella."
        ju "「Wear this so you don't catch a cold. 」"
    
        play sound standup
        show ju 201 with dis
    
        "While I wipe off the moisture on the bench,{w=.3}\nJuuichi-san takes off the jersey he was wearing,\nand hands it to me."

        jump juuichi09_talk
    
    ############################################
    label juuichi09_talk:

        $ event_name = _("In the Waiting Area")
        
        fn "「No,{w=.3} you don't have to do that... 」"
        ju "「Humans don't have fur, so it doesn't\n\ \ take much to change your body temperature. 」"
        ju "「I'd feel bad if you caught\n\ \ a cold right in front of me. 」"
        fn "「I'll be fine,{w=.3} I'm mostly dry.\n\ \ Besides, it's summer,\n\ \ I won't catch a cold that easily. 」"
    
        show ju 211 with dis
        
        ju "「...A while ago, there was a kid who kept playing\n\ \ Even though he was soaking wet.{w} The next day,{w=.3}\n\ \ he came down with a fever and had to stay in bed. 」"
        fn "「What?{w=.3} Nobody would do something that stupid. 」"
    
        show ju 201 with dis
        
        ju "「... 」"
        "He stares right at me, in silence.{p}Is there something on my face?{p}I try to say something, but my lips are sealed."
        "Come to think of it, when I was just out there\nwithout an umbrella, on a day it's meant to rain,{w=.3}\ndid I think about being close to death the next day?"
        "...{p}...{p}..."
        "A-ahaha.{w} There's nobody that stupid here, right?"
        "...Juuichi-san even remembers things like that.{p}I'd forgotten, until he pointed it out."
    
        show ju 201 big at center_big with dis
        
        ju "「... 」"
        "Once again, he pressures me with that silence.{p}I-I get it, don't give me that look!"
    
        hide ju
        show ju 201 at center
        with dis
        
        "I take the blue jersey from him,{w=.3}\n{nw}"
        play sound standup
        extend "and put it on over my naked torso." 
        "It's still warm from his body heat.{w=.3}\nIt's like he's hugging my whole body."
        "...That was a strange thought just now."
        "As for its size...\nI knew this before putting it on,\nbut it doesn't fit me at all."
        "My hands can't reach the cuffs,\neven if I fully extend my arms.\nIt also goes down to the lower half of my thighs."
        
        play sound tyakuO
        
        "I zip it up, so the heat can't escape.{w=.3}\nIt goes all the way up to my mouth, making it look\nlike I'm wearing a turtleneck sweater."
        "Realizing that it's hard to talk like this,{w=.3}\nI pull the zipper down a bit."
    
        show ju 203 with dis
        
        ju "「...does it? 」"
        fn "「What? 」"
        "Completely unlike his usual self,{w=.3}\nHe asks something in a small voice.{p}Without looking at me,{w=.3} he repeats himself."
    
        show ju 204 with dis
        
        ju "「I-{w=.3}it...{w} doesn't smell, does it? 」"
        "Why is he worried about something like that?{p}I bring the collar up to my nose and sniff it."
    
        show ju 207 with dis
        
        ju "「H-{w=.3}hey...! 」"
        "Judging by how flustered Juuichi-san looks,{w=.3}\nI overdid it.{w} I don't think he\nneeds to worry about it, though."
        "Is this something that beastmen\nare more conscious of than humans?"
        fn "「I don't think it smells. 」"
    
        show ju 212 with dis
        
        ju "「...Really? 」"
        "Juuichi-san shifts on the seat uncomfortably."
    
        show ju 201 with dis
        
        ju "「By the way...{p}\ \ I've been wondering since we went to the beach,{w=.3}\n\ \ do you exercise often? 」"
        fn "「Huh?{p}\ \ Let's see...{w} I do about an hour of exercise,{w=.3}\n\ \ three days out of the week. 」"
    
        show ju 203 with dis
        
        ju "「...And outside of gym class? 」"
        "He saw right through me.{p}I guess the classic way of\ndodging the question won't work."
        fn "「N-{w=.3}never. 」"
        "I reluctantly tell him the exact amount."
        "B-but members of the go-home\nclub don't like moving around that much.{w=.3}\nOf course I'm never going to exercise!"
    
        show ju 201 with dis
        
        ju "「...I thought as much.{p}\ \ If you don't find time to do some exercise,{w=.3}\n\ \ you'll have a body like Kuri's before you know it. 」"
        "He has a point, but...{p}I don't think my stomach has that much control over\nme. Nope,{w=.3} not at all." 
        "I take a glance at Juuichi's abdomen.{p}His shirt is stretched to its limit."
        "No matter how I look at it,\nhis seems bigger than even Kounosuke's."
        "Did he notice me looking?{w=.3}\nHe rubs his stomach while talking to me."
        
        show ju 203 with dis
        
        ju "「Just so you know,{w=.3} I do control my bodyweight,\n\ \ even if it doesn't look that way, okay? 」"
        
        play sound hit_p09
        show bstop at vshake
    
        fn "「Whaat?! 」"
    
        show ju 206 with dis
        
        ju "「What's with that surprised look on your face? 」"
        fn "「...Uhh,{w=.3} you eat a lot of sweets,\n\ \ so I thought... 」"
        ju "「... 」"
        "As I timidly press on,{w=.3} Juuichi-san falls silent.{p}Apparently I was wrong."
    
        show ju 201 with dis
        
        ju "「The heavier you are,\n\ \ the harder it is to get thrown,\n\ \ and your opponents have a harder time when pinned. 」"
        ju "「Being physically large\n\ \ also intimidates the opponent, too. 」"
        ju "「There are a surprising number of times where\n\ \ weight can be a weapon, [ln]. 」"
        fn "「...I'm sorry. 」"
        "It was inappropriate for me to\nassume he was eating too many sweets.{p}I meekly bow my head."
    
        show ju 203 with dis
        
        ju "「Don't worry about it.{p}\ \ I put on weight easily, anyway. 」"
        "He scratches his chin with a thumb."
        ju "「...Besides,{w=.3} you're not wrong\n\ \ about me liking sweets.{p}\ \ Kuroi often makes them for me. 」"
        fn "「Shin-kun? 」"
    
        show ju 201 with dis
        
        ju "「Yeah. 」"
        "I knew Torahiko cooks things for him,{w=.3}\nbut Shin-kun makes sweets for him, too...?{p}Wow, I had no idea."
        fn "「I'd like to try his sweets, sometime... 」"
        ju "「Why don't you ask him?{p}\ \ I'm sure he will, if he's in the right mood. 」"
        "Ah, that's the hard part, though.{p}I'll wait and see how things go,\nthe next time I see him."
        fn "「He makes awfully dainty sweets, doesn't he? 」"
        ju "「I wouldn't say that...{w=.3}\n\ \ {nw}"
        show ju 208 with dis
        extend "They have the impression of somebody who thinks\n\ \ carefully about what goes in them. 」"
        fn "「Huh, really?{p}\ \ I wasn't expecting that. 」"
        "I had the idea that he drew patterns on the plate,{w=.3}\nor maybe decorated his sweets...{p}I guess I was wrong."
    
        show ju 201 with dis
        
        ju "「If I'm with him,{w=.3} he usually\n\ \ mixes honey into his sweets. 」"
        ju "「He makes things sweeter than usual,\n\ \ after I mentioned I like them that way. 」"
        "Shin-kun will do things like that?{p}I wonder if he'd make my favorite sweets\nif I said something beforehand."
        "He loves sweet things... Rather, honey?{p}I wonder if all bears are like that."
        fn "「So who makes better sweets,\n\ \ Torahiko or Shin-kun? 」"
        "I was a bit hesitant to ask that question.{w=.3}\nJuuichi replies with a heavy growl."
        
        show ju 203 with dis
        $ renpy.music.set_volume(0.9, 1.0, channel = "sound2")
        
        ju "「I'd say...{w} Kuroi? 」"
        fn "「Really? I thought Torahiko was the best chef\n\ \ out of our group, though. 」"
    
        show ju 201 with dis
        
        ju "「That's just my opinion.{p}\ \ Tora is definitely an above-average chef.{p}\ \ It's rare that he makes something that I can't eat. 」"
        ju "「On the other hand, Kuroi precisely caters to\n\ \ personal tastes. Depending on the person, I think\n\ \ Kuroi would have a more professional evaluation. 」"
        fn "「Oh, I see.{w} That might be true. 」"
    
        show ju 201 with dis
        
        ju "「...Don't tell Tora I said that, okay? 」"
        fn "「I won't.{w} If I did,{w=.3}\n\ \ it'd probably make him depressed. 」"
        
        scene black with wipe_right
        
        scene bstop gray 
        show to 007 gray at center
        show over red light
        with wipe_right
    
        "It's not hard to imagine Torahiko looking at me\nwith his ears down, tail drooping, and sad eyes."
        "He's a feline, but for some reason\nhe looks more like an abandoned puppy."
        
        scene black with wipe_right
        
        scene bstop
        show over black
        show ju 201 at center
        with wipe_right
        
        $ renpy.music.set_volume(0.8, 1.0, channel = "sound2")
        
        fn "「Oh,{w=.3} sounds like the rain is letting up. 」"
        ju "「You're right. 」"
        "I stand up,{w=.3}\n{nw}"
        play sound tm2_slidedoor000
        extend "pull open the door,\nand reach out with my palm." 
        
        $ renpy.music.set_volume(0.8, 1.0, channel = "sound2")
        
        "It feels as if the rain from earlier never happened."
        "There are a few spots here and there,{w=.3}\nbut I think I can make it\nhome without getting soaked."
        "I poke my head through the door,\nand look up at the sky."
        "I can see a patch of blue through the clouds.\nIt's only a matter of time\nbefore the rain stops completely."
        "Juuichi-san gets up,{w=.3}\nand takes a look at the clouds, too."
        
        $ renpy.music.set_volume(0.5, 1.0, channel = "sound2")
        
        ju "「The rain will stop soon, at this rate. 」"
        fn "「You're right.{p}\ \ ...Man,{w=.3} I did not have a good time out there. 」"
        ju "「You've got some bad habits, don't you? 」"
        fn "「I'm not as bad as Torahiko or Kounosuke.{p}\ \ ...Wait, that wasn't very nice! 」"  
        
        stop sound2 fadeout 2 
        show ju 202 with dis
        pause .2
        show ju 201 with dis
        
        "When I raise my voice in protest,{w=.3}\nthe corners of Juuichi's mouth lift slightly."        
        ju "「...Sorry. 」"
        "He pats me on the head a few times.{p}His large hands are warm,{w=.3}\nalmost like a father's."
        "...When he does that,{w=.3}\nI lose the energy to complain."
        ju "「You can hold on to that jacket for now,\n\ \ so leave it on.{p}\ \ You don't want to wear wet clothes home, do you? 」"

        menu:
            "A. Borrow it.":
                jump juuichi09_borrow
            "B. Return it now.":
                jump juuichi09_return
    
    ########################################
    label juuichi09_borrow:

        $ event_name = _("I Would Also Like to Borrow the Bear's Hands")
        $ love_juuichi += 1
        $ borrow_jacket = True
    
        fn "「Thanks,{w=.3} I'll hold on to it. 」"
        "I decide to do as he says, and borrow his jersey.{p}Since he's letting me use it,{w=.3}\nI'll make sure to wash it and get it back to him."
        "...Besides, he's right.{p}I don't want to wear my soaking-wet shirt again."
        ju "「So your torso is covered,{w=.3}\n\ \ but are you going to put your pants on? 」"
        fn "「Of course I won't forget my pants! 」"
        "It's unpleasant, but I don't have a choice.{p}I don't want to get in trouble with the police,{w=.3}\nso I force myself to put my wet pants back on."
        "...Eugh, I need to take a bath when I get home."
    
        hide ju with dis
        
        "As I'm thinking about that,{w=.3}\nJuuichi-san and I both head home."
        
        jump end09
    
    ##########################################
    label juuichi09_return:

        $ event_name = _("Returning it now")
        
        fn "「Nah, I'll be fine.{p}\ \ Thanks for letting me borrow the jersey. 」"
        "I don't want to impose on him that much.{p}I take off the jacket, fold it up,{w=.3}\nand hand it back to him."
        ju "「...Hm,{w=.3} I see. 」"
        
        $ renpy.music.set_volume(1.0, 1.0, channel = "music")
        
        "Juuichi-san doesn't press the issue further.{p}{nw}"
        play sound standup
        show ju 001 with dis
        extend "He takes back the jersey, and puts it on."
        
        ju "「All right, let's head home. 」"
    
        hide ju with wipe_right
        
        "As he says that, he exits the waiting area.{p}I go to follow him,{w=.3}\nthen remember that I'm only wearing my underwear."
        fn "「Juuichi-saaan,{w=.3} please wait!\nI'm wearing clothes now! 」"
        
        jump end09
    
###############################################    
label end09:    
    stop sound2 fadeout 2
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
    jump day10
    
###############################################

    
