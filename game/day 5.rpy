###Day 5

screen tatsukimarket05:
    hbox:
        add "arrow down"
        at marketbounce11
    hbox:
        add "icon_tatsu"
        at marketbounce21
    hbox:
        text _("Marketplace")
        xalign .515 yalign .54
        
screen kouyacandy05:
    hbox:
        add "arrow down"
        at marketbounce12
    hbox:
        add "icon_kouya"
        at marketbounce22
    hbox:
        text _("Candy Store")
        xalign .47 yalign .53
        
screen juuichiriver05:
    hbox:
        add "arrow down"
        at riverbounce1
    hbox:
        add "icon_juu"
        at riverbounce2
    hbox: 
        text _("River")
        xalign .625 yalign .7
        
screen minasatomap05a():
    add "map"
    add "mapdate"
    imagebutton idle "a icon" hover "icon loop" xpos 458 ypos 351 action Jump("juuichi05") hovered Show("juuichiriver05")  unhovered Hide("juuichiriver05") hover_sound "av/audio/click_008.wav"
    imagebutton idle "a icon" hover "icon loop" xpos 382 ypos 259 action Jump("tatsuki05") hovered Show("tatsukimarket05")  unhovered Hide("tatsukimarket05") hover_sound "av/audio/click_008.wav"
    imagebutton idle "a icon" hover "icon loop" xpos 352 ypos 249 action Jump("kouya05") hovered Show("kouyacandy05")  unhovered Hide("kouyacandy05") hover_sound "av/audio/click_008.wav"
    hbox:
        text _("{size=+30}August 5")
        at maptime
    
screen minasatomap05b():
    add "map"
    add "mapdate"
    imagebutton idle "a icon" hover "icon loop" xpos 382 ypos 259 action Jump("tatsuki05") hovered Show("tatsukimarket05")  unhovered Hide("tatsukimarket05") hover_sound "av/audio/click_008.wav"
    imagebutton idle "a icon" hover "icon loop" xpos 352 ypos 249 action Jump("kouya05") hovered Show("kouyacandy05")  unhovered Hide("kouyacandy05") hover_sound "av/audio/click_008.wav"
    hbox:
        text _("{size=+30}August 5")
        at maptime
        
label day05:
    
    $ renpy.music.set_volume(1.0, 0.0, channel = "music")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound2")
    
    $ day = 5
    $ the_date = _("August 5")
    $ event_name = _("８月5日")
    $ focus_character = ""
    
    window hide
    play music birds_chirping
    
    scene sky01 
    show text "{size=+130}August 5" at truecenter
    with Dissolve(.5)

    pause 3
    scene black with Dissolve(1)
    pause .4
    
    scene hbroom with wipe_corner
    
    fn "「What to do today? 」"
    
    play music "<from 2.5>av/audio/free0422.ogg"
    
    if  juuichi_fireflies01 == True:
        call screen minasatomap05a
    else:
        call screen minasatomap05b
   
###############################################        
label kouya05:
    
    scene map
    hide screen kouyacandy05
    stop music
    
    $ event_name = _("Candy Wars")
    $ love_kouya += 1
    
    scene black with wipe_dr_slow
    scene candystorein with wipe_corner
    play music cicada01
    
    "If I remember right,{p}there's a candy shop here in Minasato."
    "An old-fashioned, nostalgic, charming,{p}dare I say \"retro\" candy shop."
    "It fits in perfectly with the village's rural image.{p}No matter how you look at it, it's retro.{p}If it were in the city, it'd be pretty popular."
    "Here, it's the local hangout for the little kids."
    "That hasn't changed at all..."
    
    scene candystoreout with wipe_right

    fn "「Hey guys. 」"
    
    play music daily01
    
    show ky 001 at farleft
    show ka 001 at center
    show ko 001 at farright
    with dis

    ky "「Oh, [fn]. 」"

    show ko 002 with dis
    
    ko "「Oh hey! 」"

    show ka 003 with dis
    
    ka "「Yo. 」"
    "On a whim my destination became the sweet shop.{p}Inside the store were the earlier visitors.{p}Each of them greeted me."
    fn "「Huh, so you all came. 」"

    show ko 003 with dis
    
    ko "「Well, this place has always been our hangout,{p}\ \ since way back then. 」"
    
    show ka 002 with dis
    
    ka "「Sometimes, if we come by here and meet up,{p}\ \ we hang around for a bit, you know? 」"

    show ky 002 with dis
    
    ky "「Anyway, all of us gathering here\n\ \ is something like a children's tradition. 」"
    fn "「Yeah, I guess so. 」"

    show ka 001 with dis
    
    ka "「But lately, there aren't that many kids around.{p}\ \ And the ones that usually do come here\n\ \ you don't see often anyway. 」"

    show ko 005 with dis
    
    ko "「Yeaaah. I came here all right,{p}\ \ but there aren't as many customers now\n\ \ than there were back then. 」"
    fn "「Still, isn't it thanks to that\n\ \ that we all met up together like this? 」"

    show ky 001 with dis
    
    ky "「True, but having high school students like us around\n\ \ makes it a little unapproachable for younger kids,{p}\ \ don't you think? 」"

    show ko 001 with dis
    
    ko "「Yeah, Kouya, control yourself! 」"

    show ka 005 with dis
    
    ka "「What the hell are you saying that to me for? 」"

    show ko 004 with dis
    
    ko "「Eh? That's 'cause you have bad eyes.{p}\ \ They're kinda scary. It always looks like\n\ \ you're gonna murder someone! Big bad wolf! 」"

    show ka 007 with dis
    
    ka "「First, I'm a husky. Get it right.{p}\ \ Second, watch your ass, Kuri,{p}\ \ or I'm gonna be shoving my foot up it. 」"

    show ko 005 with dis
    
    ko "「No, I really...{p}\ \ {nw}"
    show ko 006 at jump_up
    extend "Ow, owowowowow, Sorry, I-I'll shut up!{p}\ \ I-I apologized! Leggo of my head! 」"
    "As we all joked about,{p}our silly little talk opened up."
    "Things like this were also the same as back then."
    
    scene candystorein with wipe_right

    fn "「...Okay then, what should I get?{p}\ \ I'm feeling a bit hungry now. 」"
    "For a little while after that,{p}we all broke up and looked through the shelves."
    "From small snack bags,{p}to candy imitating pork cutlets,{p}the line-up is mostly the same as well."
    "Everything past here is probably like that too."
    fn "「So many choices, so little time... 」"
    "While I tried to decide,{p}I walked here and there through the shop."
    "And then I noticed that there was also\nmore stuff under the counter by the cash register."
    fn "「Woooaaah... that looks awesome... 」"
    "As I was muttering something meaningless to myself,{p}I picked one up in my hand."
    "Attached to a spherical head of a character,{p}there was a mighty color-changing bag.{p}Inside it, there were fried snacks."
    "It's called umaibou."
    "It's one my favorites, to be honest."
    "I haven't had any in a while, come to think of it.{p}In the city, I never really thought\nabout going out to buy some."
    "All right, I'll go with this then."
    
    scene candystoreout
    show ky 001 at farleft
    show ka 001 at center
    show ko 001 at farright
    with wipeleft

    fn "「Which flavor would be good...? 」"

    show ko 004 with dis
    
    ko "「It's gotta be salad. 」"

    show ky 003 with dis
    
    ky "「No, it should be cheese. 」"

    show ka 009 with dis
    
    ka "「What are you talking about? Gotta be takoyaki. 」"
    fn "「Thanks for the suggestions.{p}\ \ But if you want to surprise me,{p}\ \ try not to be so obvious about it. 」"
    "Noticing the three of them behind me,{p}I furrowed my brows into a wrinkle as I spoke."
    "Maybe I'm too used to the city,{p}but lately I'm having trouble\nnoticing anyone around me."

    show ky 001 with dis
    
    ky "「You've been tamed,\n\ \ by the concrete jungle, [fn]. 」"

    show ko 001 with dis
    
    ko "「And you used to be the champ at hide and seek, too. 」"

    show ka 001 with dis
    
    ka "「That's sad. You're not even a shadow\n\ \ of who you used to be, huh... 」"
    show candystoreout at vshake
    play sound shock1 
    fn "「Fine, that's enough!{p}\ \ Read my mind, why don't you!{p}\ \ What is this, a hazing!? 」" 

    show ky 002 with dis
    
    ky "「Well, let's set that aside.{p}\ \ Which one are you getting?{p}\ \ Is it going to be cheese, after all? 」"

    show ko 011 with dis
    
    ko "「Didn't we settle on salad? 」"

    show ka 007 with dis
    
    ka "「It can't be anything else but takoyaki, right? 」"
    fn "「Hmm, let me think... 」"
    "If I could say something in advance,{p}it feels like a lot of important things\nare being ignored right now."
    "But that's not true at all."
    "...Right, I haven't decided."
    "Still, this choice is pretty hard.{p}Honestly, I like them all.{p}It's hard to say which is better."
    "But, if I had to say something,{p}today I'm in the mood for..."
   
    $ renpy.music.set_volume(0.4, 0.0, channel = "music")
    
    menu:
        "A. Salad":
            jump kouya05_salad
        "B. Cheese":
            jump kouya05_cheese
        "C. Takoyaki":
            jump kouya05_takoyaki

######################################
label kouya05_salad:
    
    $ event_name = _("Unity is Strong")
    $ love_kounosuke += 1

    fn "「I feel like having salad today. 」"
    
    play music free0211
    
    show ko 002 at jump_up

    ko "「Of course, [fn]!{p}\ \ You totally get it. 」"

    show ky 003 with dis
    
    ky "「... 」"

    show ka 005 with dis
    
    ka "「... 」"
    "My agreement had Kounosuke in high spirits.{p}Behind him, Kouya's and Kyouji's shoulders,{p}were slumped and bumping into each other."
    "It's a bit of a weird scene."

    show ko 003 with dis
    
    ko "「Just as I thought, that refreshing feeling\n\ \ from salad is great! 」"
    fn "「Y-yeah... 」"
    "I do think the taste of salad,{p}doesn't warrant so many words."
    "My impression was that\nother tastes were pretty great, too."
    "Still, what's up with Kounosuke's cheering?{p}I don't think I'd like to get into the...{p}complexities of his salad fetishes."
    "If I think about it will I... lose?"

    show ko 002 big at center_big with wipe_right 
    ko "「Okay, I'm gonna buy one too.{p}\ \ Wanna eat it together? 」"
    fn "「Yeah, okay. Wait, hey, Kounosuke!{p}\ \ You don't need to... Uh... 」"
    
    hide ky
    hide ka
    hide ko
    with wipe_right

    "Kounosuke paid for both our pieces with 20 yen,{p}then grabbed my hand and walked quickly\nto a table on the oppposite side."
    "What... Just happened?"
    "Kouya and Kyouji were still bumping shoulders."
    "What happened to those two?"
    "In the end, the day finished\nwithout me really understanding anything."
    "Even when I knew the truth of the matter,{p}I was left in a difficult position."
    "According to the sweet shop owner,{p}after Kounosuke left the counter..."
    "It seemed the two left behind\nhad a conversation somthing like this."

    show ky 001 at midright
    show ka 005 at midleft
    with dis

    ky "「Kouya... 」"

    show ka 001 with dis
    
    ka "「...What? 」"

    show ky 002 with dis
    
    ky "「Want to eat together like the losers we are? 」"

    show ka 005 with dis
    
    ka "「...I guess. 」"
    "Back when we were browsing,{p}it seemed the three of them\nhad a bet on what I'd pick."
    "After that, the two who lost went up\nand gave Kounosuke two large bottles of soda."
    "It doesn't matter to me, but..."
    "I don't think it's good for people\nto gamble on something like that."
    "Absolutely. Bad."

    jump end05

#############################################
label kouya05_cheese:
    
    $ event_name = _("An Italian Feeling")
    $ love_kyouji += 1

    fn "「Hmm... I guess I'll go with cheese. 」"
    
    play music free0211
    show ky 001 with dis

    ky "「Oh, just as I thought [fn].{p}\ \ Just cheese is good, huh. 」"
    fn "「Yeah. The flavor of it is so delicious.{p}\ \ It's like the base for all snack foods. 」"
    ky "「Yeah, really.{p}\ \ It's simple, but that's good too. 」"
    fn "「Uh-huh, {nw}"
    show ka 005
    show ko 007
    with dis
    extend "that's rea- 」"
    
    "As the two of us discussed cheese,{p}I felt some icy looks on me."
    "I thought about it,{p}then timidly looked around..."
    ko "「... 」"
    ka "「... 」"
    "The two of them seemed to have trouble talking,{p}making lonely-looking faces at me."
    "Is that because I agreed with Kyouji?{p}Even so, it's still a lot of pressure..."
    "And thanks to that, I cut myself off,{p}before saying 「that's right. 」"
    
    show ky 001 big at border_left_big with wipe_right
    
    ky "「Okay, I'll treat you to it today.{p}\ \ How about we eat over there together? 」"
    fn "「O-okay... Thanks, let's do that. 」"
    "As Kouya and Kounosuke kept looking at us,{p}Kyouji and I walked over to the provided table."
    "The other two still kept standing by the counter."
    "What's up with them?"
    "It bothered me, but the day ended like that.{p}The truth became apparent on another day later on."
    "Back when we were browsing,{p}it seemed the three of them\nhad a bet on what I'd pick."
    "The prize was two bottles of soda."
    "After that, Kounosuke and Kouya were disappointed,{p}and with the looks on their faces,{p}it was clear that they felt defeated."
    "But even so..."
    "...I don't think it's good for people\nto gamble on something like that."
    "Absolutely. Bad."
    
    jump end05

###########################################
label kouya05_takoyaki:
    
    $ event_name = _("Just Eat")
    $ love_kouya += 1

    fn "「It's gonna be takoyaki, then. 」"
    
    play music free0211
    
    show ka 003 at jump_up    
    
    ka "「I know, right?{p}\ \ And it's only going to be takoyaki, right? 」"
    fn "「Yeah, the flavor is so dependable.{p}\ \ I like that strong feeling more than anything else. 」"

    show ka 002 with dis
    
    ka "「Yeah, it's pretty good.{p}\ \ Also, there's one more layer of seasoning,\n\ \ compared to other flavors. 」"
    fn "「Huh. I didn't know that. 」"

    hide ka
    show ka 003 big at center_big
    with wipe_right
    
    ka "「I'm a guy who likes some trivia.{p}\ \ Anyway, that aside, how about we eat one together?{p}\ \ I'll pay for yours. 」"
    fn "「Eh, is that okay?{p}\ \ I'll take you up on that then.{p}\ \ Do you two also want to... 」"
    "I looked towards Kyouji and Kounosuke as I said that,{p}and the two of them were making\ndisappointed faces for some reason."
    
    play music cicada01 fadein 4
    
    scene candystoreout
    show ky 003 at midleft
    show ko 007 at midright
    with dis

    ky "「... 」"
    ko "「... 」"
    "The looks in their eyes were so reproachful."
    "Huh? Did I do something?"
    fn "「W-what's wrong you two...? 」"

    show ky at jump_up
    
    ky "「...No, it's nothing.{p}\ \ Right, Kounosuke? 」"

    show ko 005 with dis
    
    ko "「Y-yeah. Nothing, nothing at all. 」"
    
    play music oo39_cho_ys001

    "No matter how I look at it,{p}no matter how I think about it,{p}there's something suspicious here."
    "All this talk about nothing feels so staged.{p}I should investigate this thoroughly."
    fn "「...Really?{p}\ \ You guys aren't hiding anything from me?{p}\ \ Well, Kounosuke? 」"

    show ko 004 with dis
    
    ko "「N-no, we aren't.{p}\ \ Nothing to hide... 」"
    
    play sound hit_p07
    show candystoreout at vshake
    "{size=+25}LIES."
    "Those eyes aren't focusing on me!{p}They're focusing anywhere but me!"
    fn "「Uh-huh...{p}\ \ Well, that's fine,{p}\ \ but don't overdo it, all right? 」"

    show ko 005 with dis
    
    ko "「W-what are you talking about...? 」"
    fn "「Ah, it's nothing to really hide.{p}\ \ I get it, seriously. I just overheard it.{p}\ \ But I still don't think this kind of thing is cool. 」"
    fn "「I mean, it's fine if it's me,{p}\ \ but for anyone else... You know? 」"

    show ko 011 at jump_up
    
    ko "「I-I said to stop, didn't I!?{p}\ \ But Kouya and Kyouji were into it... 」"
    
    show ky at jump_up
    
    ky "「No no. Kounosuke, you were into this from the start,{p}\ \ you wanted to make the bet. 」"

    show ko 012 at briefzoom
    
    ko "「T-that's not...{p}\ \ Weren't only you and Kouya\n\ \ getting all excited about this!? 」"

    show ka 005 at farright with wipeleft
    
    ka "「I'm not denying it, but isn't it bad,{p}\ \ for only one person to be saying that? 」"
    "The three suspects who started this fight.{p}Oh, what a dumb fight it is."
    "I don't care about it anymore.{p}The time for fessing up passed by already."
    fn "「A bet, eh? So that's what it was,{p}\ \ all of you getting worked up\n\ \ over what I would choose? 」"
    fn "「So, what prize was the winner going to get...? 」"

    show ka 010 with dis
    
    ka "「...Wait, you didn't hear us talking? 」"

    show ky 001 with dis
    
    ky "「Busted, huh. 」"

    show ko 006 with dis
    
    ko "「Eh, w-what? 」"
    fn "「Of course I didn't hear anything.{p}\ \ I figured if I shook hard enough,{p}\ \ it'd all come out. 」"
    
    scene candystoreout
    show ky 001 at farleft
    show ko 006 at center
    show ka 010 at farright
    with wipe_right

    "After I spoke, the three stood in mute amazement.{p}They all seemed to be thinking\n「what do we do now? 」"
    "Heh, this stuff is hilarious."

    play music cicada01 fadein 1.5
    
    fn "「Well, anyway, what am I supposed to think?{p}\ \ Using someone for a bet like that... 」"

    show ka 005 with dis
    
    ka "「Sorry... 」"

    show ky 003 with dis
    
    ky "「Our bad... 」"

    show ko 005 with dis
    
    ko "「We'll reflect on it... 」"
    fn "「How'd that happen anyway?{p}\ \ Were you asking the owner? 」"

    show ka 001 with dis
    
    ka "「No, thing is... 」"

    show ky 002 with dis
    
    ky "「This is... 」"

    show ko 004 with dis
    
    ko "「It's complicated. 」"
    "They opened their mouths,\nand the suspects began talking."
    
    stop music fadeout 2
    scene black with sdis
    
    $ event_name = "His Select Is...?"

    "It happened five minutes ago,{p}right after I'd gone off to go looking around."
    
    play music cicada01 fadein 3
    scene candystoreout
    show ky 001 at farleft    
    show ko 001 at farright
    show ka 001 at center
    with sdis

    ky "「Hey, I wonder what [fn]'s going to get. 」"

    show ko 005 with dis
    
    ko "「Hmm, what could it be?{p}\ \ Maybe he'll get everything here. 」"

    show ka 009 with dis
    
    ka "「...What about an umaibou?{p}\ \ He likes that stuff. 」"

    show ky 002 with dis
    
    ky "「Oh, that's possible. 」"

    show ko 006 at jump_up
    
    ko "「Oh, it is.{p}\ \ He's stopped in front of the Umaibou. 」"
    ky "「Hmm, then the next problem is...{p}\ \ Which flavor he's going to get. 」"

    show ka 002 with dis
    
    ka "「I don't think it's that much of a problem.{p}\ \ Won't it be takoyaki? 」"

    show ky 003 with dis
    
    ky "「What are you talking about?{p}\ \ Won't he get cheese? 」"

    show ka 009 with dis
    
    ka "「No way. That can't be. 」"

    show ky 001 with dis
    
    ky "「Want to bet on it, then?{p}\ \ Does two large sodas sound good? 」"

    show ka 005 with dis
    
    ka "「Where'd that weird prize choice come from? 」"

    show ky 003 with dis
    
    ky "「If you don't want to, then that's fine.{p}\ \ We'll just stop.{w} But if it were Torahiko,\n\ \ he'd be in on it... 」"

    show ka 007 with dis
    
    ka "「...Is that a challenge?{p}\ \ Fine then, I'm in. 」"

    show ko 004 with dis
    
    ko "「...You guys, you've been saying cheese or takoyaki,{p}\ \ but haven't you forgotten the most important one? 」"

    show ka 005 with dis
    
    ka "「Huh? 」"

    show ky 002 with dis
    
    ky "「Hm? 」"

    show ko 002 with dis
    
    ko "「If it's Umaibou then it has to be salad.{p}\ \ If it's not salad, it's pointless,{p}\ \ so of course he's going to pick that. 」"

    show ky 001 with dis
    
    ky "「I say cheese.{p}\ \ Kouya says takoyaki.{p}\ \ And Kounosuke says salad. All good? 」"

    show ko 001 with dis
    
    ko "「Ah, I hope I get two bottles of orange juice. 」"

    show ka 010 with dis
    
    ka "「You've think you've won!? 」"

    show ko 004 with dis
    
    ko "「Of course. 」"

    show ky 003 with dis
    
    ky "「Well, that doesn't really matter.{p}\ \ The rule says it can be anything.{p}\ \ The point is to encourage yourself to want to win. 」"

    show ky 001 with dis
    
    ky "「All right, go! 」"
    
    $ event_name = _("Things That Haven't Changed Between Then and Now")
    stop music fadeout 1
    
    scene candystoreout
    show ko 001 at farleft
    show ky 001 at farright
    show ka 001 at center
    with Dissolve(.5) #!#Need to change transition to the squigly-like one
    
    play music cicada01 fadein 4
    
    show ka 005 with dis

    ka "「...And that's what happened. 」"

    show ky 002 with dis
    
    ky "「I was thinking of just teasing Kouya at first,{p}\ \ but it went awry somewhere along the line... 」"

    show ko 004 with dis
    
    ko "「It's not like you had any ill will right? 」"
    fn "「Yeah, I get it, I get it. 」"
    "...It's a bit stupid."
    "It's that, what's the word I'm looking for?\nI forgot for a second, umm..."
    
    play sound freeze04
    pause .2
    
    "Ah,{w=.3} \"dumb.\"{p}Lately my vocabulary has been getting worse, damn." 
    "At any rate, what happened with these three?{p}They aren't blaming anyone,\nso this ending is a bit anticlimatic."
    "Should I demand an apology and compensation?"
    "...I know, I just thought up of a good game."
    fn "「For now, I'm really shocked,{p}\ \ but I haven't said just how shocked I am. 」"
    "From just one word from me,{p}the three of them hung their head in shame."
    "Geez, for keeping a secret from me\nI'm gonna say this."
    fn "「For now, you can make it up to me\n\ \ by getting me two large sodas. 」"
    
    show ko 006
    show ka 010
    with dis

    "All Three" "「Huh? 」"
    fn "「It was going to be the prize anyway, right?{p}\ \ As punishment for keeping a secret from me,{p}\ \ go get them for me. 」"
    "Everyone was surprised by the announcement."
    "But I'm not going to stop here.{p}There's still more."
    "And with a smile, I informed them of it."
    
    play music daily04 fadein 2

    fn "「Now, how about we all drink together? 」"
    "Since that was so tasty, it should be fun."
    "It'd be best for us to do something together."

    show ka 006 with dis
    
    ka "「[fn]... 」"
    fn "「Come on, I'm going to go buy them now.{p}\ \ Let's go already. 」"

    show ky at jump_up
    
    ky "「Whoa!? 」"

    hide ky with wipe_right
    show ko 001 with dis
    
    ko "「Hey, [fn], don't push! That's dangerous! 」"

    hide ko
    hide ka
    with wipe_right
   
    "I pushed everyone from behind,\nand we all left the shop."
    "The gloomy mood hanging over us was blown away.{p}With that, it was just like always."
    
    scene market
    show ko 001 at farleft
    show ky 001 at farright
    show ka 002 at center
    with wipeleft

    ky "「Seriously, we're no match for [fn]. 」"

    show ka 003 with dis
    
    ka "「If anyone's as crazy,{p}\ \ I'd think that Torahiko is the only one\n\ \ who could even compare to him. 」"

    show ko 004 with dis
    
    ko "「You said it. 」"
    fn "「What!?{p}\ \ And after I've shown you a bit of slack!? 」"
    "Here or there, it's the same as always.{p}We'd laugh over the simple things."
    "For the punishment games,{p}it always would be something fun."
    "That's because we'd all be laughing,{p}as we all walk alongside each other."
    
    jump end05

#############################################    
label tatsuki05:
    
    $ focus_character = "tatsuki"
    
    scene map
    hide screen tatsukimarket05
    stop music
    
    $ love_tatsuki += 1
    
    scene black with wipe_dr
    scene market red with sdis
    play music free0213

    who "「Yo, what are you up to? 」"
    fn "「Hey, Tatsu-nii. Done with work already? 」"
    "Looking back over my shoulder,\nTatsu-nii was leaning out the window of his run-down\nlight truck, waving at me."
    "The racket of the engine got louder as\nhe pulled the truck up alongside me."

    show ta 001 red with dis

    ta "「Yep, just finished now.{p}\ \ After this, I'm gonna take a bath and have a drink. 」"

    show ta 002 red with dis

    fn "「Just how old are you, again...? 」"
    ta "「Gahaha! Hell if I know. 」"

    show ta 001 red with dis

    ta "「I'm going home right now,\n\ \ do you want me to give you a lift to somewhere? 」"
    menu:
        "A. Sorry, I have stuff I need to do.":
            jump tatsuki05_busy
        "B. Uhh... Is your driving okay?":
            jump tatsuki05_avoid
        "C. Thanks, that'd be great!":
            jump tatsuki05_accept

#############################################
label tatsuki05_busy:

    fn "「Sorry, I have stuff I need to do. 」"

    show ta 008 red with dis

    ta "「Oh. I guess it can't be helped, then. 」"
    fn "「Instead of saying that,\n\ \ you could just wait until I was finished. 」"
    ta "「No way. I wanna go home already. 」"

    show ta 002 red with dis 
    
    fn "「You're so cold. 」"
    ta "「Don't say that so shamelessly. 」"
    fn "「Haha, well, I'm heading off then. Bye, Tatsu-nii. 」"
    ta "「Yeah. Take care, [fn]. 」"
    fn "「You too. 」"

    hide ta with dis
    
    play sound truck
    
    "No matter which way you look at it...{p}Tatsu-nii's the one who needs to take care."
    "He's kind of careless, and his driving's crazy.{p}But that's just like him."
    "I should finish up here and head home, too."
    
    jump end05


label tatsuki05_avoid:
    
    $ love_tatsuki -= 1

    fn "「Uhh... Is your driving okay? 」"
    "I think everyone has warned\nme about Tatsu-nii's driving,\nand it worries me a bit..."

    show ta 006 red with dis

    ta "「What, are you questioning my driving technique? 」"
    fn "「No, it's not that...{p}\ \ It's just you're super aggressive, Tatsu-nii. 」"

    show ta 004 red with dis

    ta "「If you've got something to say, then spit it out.\n\ \ Someone probably told you that my driving's scary.{p}\ \ And here I was looking forward to driving you, too... 」"
    fn "「Sorry, I've got errands to do.\n\ \ I need to do some shopping, too. 」"
    ta "「Okay, okay, I got it.\n\ \ If you've got errands, then there's no helping things.{p}\ \ I don't think you want a ride afterwards.{w=.3} Later. 」"

    hide ta with dis
    play sound truck

    "Aah, now I've done it. I wonder if he's mad?{p}But it really does seem scary, and I do have errands,\nso I can't really get around it.{w} {nw}"
    stop music fadeout .6
    extend "{w=.5}{nw}"
    play sound CarStopA
    extend "{w=1}{nw}"
    play sound crash20_b 
    show market red at hshake
    extend "{w=.5}{nw}"

    fn "「Eeeh??? 」"
    
    play music free0428 fadein 2

    "All of a sudden, there was a braking sound,\nand I turned my head in surprise.\nOn the other side of the road, smoke was billowing."
    fn "「That can't be Tatsu-nii.{p}\ \ But the light truck is the Midoriya Gro...{p}\ \ It flipped over... Tatsu-nii?{w} Tatsu-nii...? 」"
    
    jump end05

#########################################
label tatsuki05_accept:
    
    $ love_tatsuki += 1

    fn "「Thanks, that'd be great! 」"
    
    scene market red with Dissolve(1) 
    pause .3
    show ta 002 big red at center_big with dis 

    ta "「Oh, that's a special place. 」"

    show ta 010 big red with dis 

    ta "「I don't let just anyone sit next to me. 」"
    "Come to think of it..."
    "I think just about everyone has said something\nor other about riding in Tatsu-nii's car."
    fn "「It's just until I finish my errands.\n\ \ This is really good timing. 」"

    show ta 001 big red with dis 
    
    ta "「Yeah, it is. 」"
    fn "「So you did get your licence.\n\ \ Is your driving all right? 」"

    show ta 002 big red with dis 

    ta "「Of course. I use this car every day for work.{p}\ \ All right, let's head off. 」"

    play sound truck

    "As Tatsu-nii said that,\none of his tires gave a loud groan,\nand kicked up a large dust cloud.{w} {nw}"
    play sound BurstE
    extend "{w=.5}{nw}"
    play sound BurstE
    extend "{w=.5}{nw}"
    play sound BurstE
    extend "{w=.5}{nw}"

    fn "「Hey, Tatsu-nii, did you just hear something weird? 」"
    
    stop music fadeout .7
    play music free44

    ta "「Don't worry about it, the car's just old.{p}\ \ It's running fine.{p}\ \ ...Huh? 」{w} {nw}"
    show ta 008 big red at shivering with dis     
    play sound BurstE 
    show market red at vshake
    extend "{w=.5}{nw}"
    play sound BurstE
    show market red at vshake
    extend "{w=.8}{nw}"
    play sound BurstE
    show market red at vshake
    extend "{w=.5}{nw}"
    play sound BurstE
    show market red at vshake
    extend "{w=.8}{nw}"
    play sound don17_a
    show market red at hshake

    "The beaten-up frame gave a jolt\nas a weird noise came from the engine."
    "The needle in the speedometer dropped,\nand the truck stalled."
    "It rolled for a while,\nbut in the end, {w=.3}{nw}"
    show market red at hshake
    play sound don17_a 
    extend "it gave a hiss, {nw}"
    show ta at still
    extend "{w=.05}{nw}"
    show ta 008 big red at jump_up_big
    #extend "{w=.1}{nw}"
    pause .1
    show ta at center_big
    extend "and stopped."
    
    fn "「It stopped. 」"
    
    stop music fadeout .5
    pause .5
    play music free0211

    show ta 002 big red with dis 
    
    ta "「Whoops, it looks like it's out of gas.{p}\ \ No, wait, I forgot to put any in. Gahahaha! 」"
    fn "「What do we do? 」"

    show ta 004 big red with dis 

    ta "「Well, there's not much else we can do.{p}\ \ I'll get out and push, while you steer. 」"
    fn "「I don't have my licence.\n\ \ Even then, can you really push this thing? 」"

    show ta 002 big red with dis 
    
    ta "「You don't need a licence if I'm pushing it. 」"
    ta "「Occasionally, when I run out of gas,\n\ \ I just push this back home,\n\ \ which is what Pa told me to do. 」"
    "The crazy Midoriya father and son..."

    show ta 008 big red with dis

    ta "「I know I said I'd drive you,\n\ \ but can you come along with me? 」"
    fn "「Yeah, there's no helping it.{p}\ \ You messed up again, just like you always do. 」"

    show ta 004 big red with dis 

    ta "「What was that!? 」"

    show ta 005 big red with dis
    
    ta "「No... This is totally my fault.{p}\ \ Sorry about that, and thanks for helping, [fn]. 」"
    fn "「Hey, no problem. 」"

    show ta 002 big red with dis 

    ta "「Okay, let's hurry on home.{p}\ \ I'll push from behind, and we'll be back soon.{p}\ \ You take care of the steering. 」"
    
    jump end05

########################################################    
label juuichi05:
    
    scene map
    hide screen juuichiriver05
    stop music
    
    $ event_name = _("Pure, Ephemeral, Beautiful")
    $ focus_character = "juuichi"
    $ love_juuichi += 1
    $ juuichi_fireflies02 = True
    
    play music shop03
    scene riverbank night with dis 

    "Heading to where I was meeting Juuichi-san,{w=.3}\nI walk along the embankment in silence.{p}Catching fireflies. That's our plan for today."
    "After talking to him yesterday,{p}I immediately went looking in the\nshed for something we could use."
    "The bug net I found in the corner looked promising,\nuntil I saw the large hole in the net."
    "I even went out to get a brand new\ninsect-catching kit just for this outing,{w=.3}\nbut in the end, all I've got is this flashlight."
    "It's quite bright,{w=.3}\nand illuminates the surroundings\nmore than I thought it would."
    "The way the light cuts through the dark night\nhas a somewhat reliable feeling to it."
    "Although I felt lost in the dark yesterday,{p}I have a completely different impression of it\nnow that I have a light."
    "While I think about that,{w=.3}\nI take a look at my watch.{p}There are still...{w=.3} 15 minutes until the meeting."
    "Damn,{w=.3} seems I was a little too early.{p}I'm at a bit of a loss on how to kill time..."
    ju "「Hey,{w=.3} [ln]. 」"
    
    play sound bosu27
    show riverbank night at vshake

    "It's the owner of the physique that dwarfs me.{p}Needless to say, it's the person I'm here to meet?{w=.3}\nthat is, it's Juuichi-san."
    fn "「Oh, Juuichi-san!{w=.3} Good evening.{p}\ \ Please stop surprising me from behind...{w=.3}\n\ \ It's bad for my heart. 」"
    "As I greet him, I raise my voice in protest.{p}I guess I'm still twitchy from last night."

    show ju 003 night with dis

    ju "「Sorry,{w=.3} I didn't mean to scare you.{p}\ \ I forgot that humans don't have good night vision. 」"
    "I'm sure that even beastmen who can see fine\nat night would jump if their name was called out\nwhen they weren't expecting it."
    "...Actually,{w=.3} Juuichi-san would probably just say{w=.3}\n'What do you want, at a time like this?' as though\nnothing was out of the ordinary."
    "Hmm.{w=.3} I suppose it depends on who was calling."
    fn "「Juuichi-san,{w=.3} you got here pretty fast.{p}\ \ And here I was thinking I was too early. 」"

    show ju 008 night with dis
    
    ju "「...Really? 」"
    fn "「Yeah.{w} There are still about 15 minutes\n\ \ until the time we were going to meet. 」"

    show ju 001 night with dis

    ju "「15 minutes isn't really that early. 」"
    "Hmm,{w=.3} I don't know about that.{p}I'm the type who likes to\ndo things at the last minute."
    "...As expected, Juuichi-san's the leader again.{p}I consider apologising for being late,\nbut I was technically here early."

    show ju 003 night with dis

    ju "「...Well,{w=.3} it's better than always being late,\n\ \ like a certain someone, right? 」"
    "Juuichi-san speaks with a low growl.{p}...He must be talking about Kounosuke."
    "I suppose he does have a reputation for being late.{p}It's not easy to make Juuichi-san growl.{w=.3}\n...Well, in a bad way."
    fn "「...Ahem.{p}\ \ It's still a little early,{w=.3}\n\ \ but why don't we get going? 」"
    fn "「It's just the two of us today. 」"

    show ju 001 night with dis

    ju "「Yeah,{w=.3} you're right. 」"

    play sound step13b

    "We set out, with Juuichi-san in front.{p}I follow the beams of light\ncoming from our flashlights with my eyes."
    "The large flashlight he's holding looks like it\nwas built for emergency situations.{w=.3}\nIt has a whole bunch of knobs and switches on it."
    "From its appearance,{w=.3}\nit must have an inbuilt radio.{p}Curious, I ask him about it."
    fn "「Juuichi-san,{w=.3} do you usually listen to the radio\n\ \ when you're out walking? 」"

    show ju 003 night with dis

    ju "「No. 」"
    "He shakes his head."

    show ju 001 night with dis

    ju "「When I'm walking alone,{w=.3}\n\ \ I remember that day's practice,\n\ \ and try to figure out how to improve. 」"
    ju "「I rarely listen to the radio. 」"

    show ju 008 night with dis

    ju "「...Why,{w=.3} is there a program\n\ \ you wanted to listen to? 」"
    "I hastily shake my head in response to his question."
    fn "「Oh,{w=.3} that's not what I meant.{p}\ \ I noticed all those buttons and the tuner,\n\ \ and was just curious. 」"
    fn "「...But it looks like it's seen some use, doesn't it?{p}\ \ It seems like it's an old design, too. 」"
    
    play sound kachi09
    pause .2
    play sound kachi09

    "When I ask him about that,\nhe strikes the flashlight, hard.\nIt sounds much more solid than I thought it would."

    show ju 001 night with dis

    ju "「It used to be my father's.{p}\ \ It may look old-fashioned,{w=.3}\n\ \ but it's well-built, so it still works fine. 」"
    ju "「Besides,{w=.3} you grow attached to the things you\n\ \ use for a long time, even if it is just a tool. 」"
    fn "「It's a ten-year veteran! 」"

    show ju 002 night with dis

    ju "「...It might be even older than that. 」"
    "The rugged model and chipped paint\nmake it seem even more mysterious."
    fn "「It might even be older than us.{p}\ \ ...By the way, how long does it take\n\ \ to get to where the fireflies are? 」"

    show ju 001 night with dis

    ju "「...From here,{w=.3} about twenty minutes or so. 」"
    fn "「It's farther upstream, right? 」"
    ju "「Yeah. 」"
    fn "「I'm looking forward to it.{p}\ \ It's been a while since I've seen something magical. 」"

    show ju 003 night with dis
    
    ju "「...Magical? 」"
    fn "「You know the feeling where you've been overwhelmed\n\ \ by the beauty of nature?{p}\ \ That was the best way I could describe it. 」"
    "I guess it wasn't the best way to say it...?\nI start to worry about it."
    
    show ju 002 night with dis

    ju "「...I see.{p}\ \ {nw}"
    show ju 001 night with dis
    extend "Well,{w=.3} that's just like you to think that. 」"
    "Just for a moment,{w=.3} I caught a glimpse of a smile.{p}I couldn't tell in the dark,{w=.3}\nbut I don't think it was a malicious one."
    "That said...{p}I've thought it before,{w=.3}\nbut Juuichi-san is such a handsome guy."
    "I wish he'd smile more often."
    "If he did, I have a feeling\nthat he wouldn't be mistaken for a scary old man." 

    show ju 003 night with dis

    ju "「...[ln],{w=.3} why have you stopped? 」"
    fn "「Oh, sorry. 」"
    "I run to catch up to Juuichi-san."

    show ju 001 night with dis

    ju "「...Well,{w=.3} I don't often get the chance either.{p}\ \ What exactly do you see?{w=.3}\n\ \ I've heard it's a fun thing to do. 」"
    fn "「Wait,{w=.3} you don't go firefly catching that much?{p}\ \ Don't you like going for walks? 」"
    ju "「No.{w} If I wasn't with someone, like today,{w=.3}\n\ \ I probably wouldn't go. 」"
    fn "「That seems like a bit of a waste, though... 」"
    "I cock my head, confused.{p}I think I'd want to see beautiful things every day."

    show ju 003 night with dis

    ju "「I suppose,{w=.3} but wouldn't you tire of it,\n\ \ if you went and saw it every day?{p}\ \ It's better as a rare thing. 」"
    fn "「Hmm,{w=.3} I guess. 」"
    "Well,{w=.3} they say you get tired of\nseeing a beautiful person after 3 days."
    "I guess, if you kept looking at a beautiful scene,{w=.3}\nyou'd appreciate it less."

    $ event_name = _("Learning to Walk, Juuichi-Style")

    show ju 001 night with dis

    ju "「Like I said,{w=.3} I don't go on\n\ \ walks to admire the scenery. 」"
    ju "「It's rare to meet people at this hour.{p}\ \ I find that listening to my steps calms my mind.{w=.3}\n\ \ That's why it's perfect for thinking. 」"
    "Wow, really?{w} I decide to imitate him,{w=.3}\nand walk in silence for a bit."

    hide ju with Dissolve(.2)
    play sound step13b

    "I hear the sound of our footsteps,\nthe calls of insects,\nand the sounds of the river."
    "When I focus,{w=.3}\nI can tell the difference between our steps."
    "Is it because he has a larger stride?{w=.3}\nThere's a longer gap between his steps than mine."
    "It seems like the ground\ncrunches louder when he steps, too."
    "It's a really small thing,{w=.3}\nbut if Juuichi-san hadn't pointed it out,\nI never would have noticed..."
    "I usually only rely on my sight when walking.{p}When I pay attention to my sense of hearing, too...{w=.3}\nIt's very interesting."
    "I'm really not used to walking like this.{p}I need to watch my feet,\nor else I'm going to trip."
    "...Juuichi-san's trick gets pretty dangerous,{w=.3}\neven by talking about it."

    scene black with Dissolve(1)
    
    scene riverbank night
    show ju 001 night at center
    with dis

    $ event_name = _("Fireflies on an overcast night")

    ju "「...We're almost there. 」"
    fn "「Huh? 」"
    "As he says that, I shine my flashlight on my watch.{p}The long hand shows that 15 minutes have passed."
    fn "「It's been that long, huh?{p}\ \ Sorry for being so quiet the whole time. 」"
    ju "「Don't worry about it.{p}\ \ ...Besides,{w=.3} we're close enough friends that\n\ \ we don't need to talk all the time. 」"
    "He says that with a shrug of his shoulders.{p}Hmm, am I giving it too much thought...?{p}Juuichi-san doesn't seem to mind."
    ju "「Turn your flashlight off. 」"
    fn "「Oh,{w=.3} sure. 」"
    
    play music night_insects fadein 1.5
    play sound phone_pickup

    "Just as he asks, I turn it off.{p}Our surroundings are plunged into darkness,{w=.3}\nmore abruptly than I was expecting."
    ju "「[ln],{w=.3} can you walk? 」"
    fn "「Uhh,{w=.3} can you hold on a second?{p}\ \ My eyes need to adjust to the dark. 」"
    ju "「...I see. 」"
    "I try rubbing my eyes.{p}...Doing so doesn't really help,\nbut I guess it's just a habit."
    ju "「Would you like to walk while holding my hand? 」"
    "...Wha-?"
    "While I'm trying to think\nof an appropriate response,{w=.3}\nhe lets out a small snort."
    ju "「What's with that look on your face?{p}\ \ {nw}"
    show ju 002 night with dis 
    extend "It was a joke. 」"
    fn "「I didn't hear it as a joke... 」"

    show ju 001 night with dis

    ju "「...Did you say something? 」"
    fn "「No, nothing. 」"
    "While we talked,{w=.3}\nmy eyes adjusted to the darkness.{p}The adaptability of the body is truly amazing."
    "Asking Juuichi-san if he's ready to go,\nI get a nod of the head in response."
    "He leaves the path we were walking on,\nand heads down the slope beside it."

    hide ju with Dissolve(.2)

    "I go after him so I don't get left behind,\nbut I take care to watch my feet."
    "Don't they trim the plants around here?{w=.3}\nThe weeds reach up to my waist.{p}There are even some that are as tall as Juuichi-san."
    "If I'm not willing to get my hands dirty,\nthen I won't get to the fireflies.{w=.3}\nIt's still difficult to walk, though."
    "Thank goodness Juuichi-san's making a path in front.{p}If I came here alone,\nit would be quite the struggle."
    "Juuichi-san's back looks bigger than usual\nas he pushes through the reeds in silence.{p}Surely it can't be an optical illusion."

    $ event_name = _("Green Lights Under the Night Sky")

    "We continue through the weeds for about 20 meters.{p}As we get close to the river,{w=.3}\nthe number of green lights in the air increases."
    "As the number of them increases,{w=.3}\nI give up trying to count them.{p}There are more here than I imagined."
    "Finally, I push out of the tall weeds.{p}{nw}"
    scene white with dis
    pause .5
    scene river night with dis
    play music free31
    extend "In front of us,{w=.3} a spectacle of\ngreen, interweaving fireflies fills my vision."
    "It's as if the stars had changed color,\nand were dancing around."
    "The sight overwhelms me.\nMy mouth agape, I'm unable to move."
    "With each gust of wind,{w=.3}\nripples appear in the mass of light."
    "Earlier, I half-jokingly used the term 'magical',{p}but now, I don't think that was the wrong term."
    fn "「...Amazing... 」"

    show ju 001 night at center with dis
    ju "「It is.{p}\ \ ...It's beautiful. 」"
    fn "「I'm really glad I came out here. 」"

    show ju 002 night with dis

    ju "「...I see. 」"
    "Juuichi-san smiles, just slightly."
    ju "「I am, too- 」"

    play sound wind_noise

    "As he speaks, a strong gust of wind kicks up.{p}The rattling grass makes a loud sound,\nmaking me instinctively cover my face with my arm."
    "Juuichi-san's words become lost."
    fn "「Ah, sorry.{p}\ \ Could you repeat that? 」"

    show ju 001 night with dis

    ju "「...The lifespan of a firefly is about 2-3 weeks.{p}\ \ They live a hard, short life,\n\ \ literally spent glowing. 」"
    ju "「I guess that's why they look so beautiful. 」"
    fn "「Juuichi-san, isn't that a\n\ \ bit of an odd thing to say? 」"

    show ju 004 night with dis
    ju "「...Hm,{w=.3} you think so? 」"
    fn "「...But I agree with you.{p}\ \ This scenery is like a living creature.{p}\ \ It really is beautiful, isn't it? 」"

    show ju 001 night with dis

    ju "「Quite the poet, aren't you? 」"
    fn "「No way,{w=.3} I don't even come close to you. 」"
    "We both laugh at this.{p}Then, we shift our attention\nback to the scene in front of us."
    "Oh, I should have brought my phone.{p}I could have taken a photo of this sight...{p}I'd forgotten that it even existed."
    "But even a photograph of this\nstill wouldn't compare to the real thing..."
    "The green-colored waves are endless.{p}Juuichi-san and I say little,{w=.3}\nbut there's no need. Just sharing this is enough."
    "Instead of trying to hold inelegant conversation,\nthere's a strange feeling in the air."
    "We can get along and hang out together like this.{p}For however short the moment may be,\nI can feel truly relaxed."
    "Is this what I came back to my hometown for?{p}Juuichi-san stands beside me,\nhis eyes focused on the dazzling scene."
    "Suddenly, he turns his head to look at me.{p}As our eyes meet,{w=.3}\nI feel really embarrassed for some reason."
    ju "「[ln].{w} It's getting late... 」"
    fn "「...Huh?{w=.3} Oh,{w=.3} already? 」"
    "When I chack the time, it's just about 10.{p}It took about 30 minutes to get here,{w=.3}\nso is this about the time to leave?"
    "I'd like to forget about the time and keep watching,{w=.3}\nbut Grandpa will get worried if I'm too late."
    "I stare at the wonderful scene,\ntrying to etch it into my memory."
    ju "「...Would you like to come back here again,{w=.3}\n\ \ before you go home? 」"
    "I shake my head."
    fn "「No.{w=.3} By the time I come back,\n\ \ there won't be as many fireflies.{p}\ \ I want to keep this time as special as possible. 」"
    ju "「...I see. 」"
    "He says no more,{w=.3}\nand pats my shoulder a few times."
    
    hide ju with dis
    scene black with dis

    "I just gained another precious\nmemory of this summer."

    jump end05

################################################
label end05:

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
    
    jump day06
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
