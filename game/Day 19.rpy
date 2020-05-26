###Day 19
screen house19:
    hbox:
        add "arrow down"
        at housebounce1
    hbox:
        add "icon_kouya"
        at housebounce2
    hbox:
        text "[fn]'s House"
        xalign .58 yalign .42
        
screen minasatomap19():
    add "map"
    add "mapdate"
    if favorite == "kouya":
        imagebutton idle "a icon" hover "icon loop"  xpos 418 ypos 185  action Jump("kouya19") hovered Show("house19")  unhovered Hide("house19") hover_sound "av/audio/click_008.wav"    
    #elif favorite == "shun":    
    hbox:
        text _("{size=+30}August 19")
        at maptime

################################################
label day19:
    
    $ renpy.music.set_volume(1.0, 0.0, channel = "music")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound2")
    
    $ day = 19
    $ the_date = _("August 19")
    $ event_name = _("８月19日")
    
    if favorite == "kouya" or favorite == "juuichi":
        window hide
        play music birds_chirping
        
        scene sky01 
        show text _("{size=+130}August 19") at truecenter
        with Dissolve(.5)
    
        pause 3
        scene black with Dissolve(1)
        pause .4
        
        if favorite == "kouya":
            jump map19
        elif favorite == "juuichi":
            jump juuichi19
        
    else:
        jump day20    
        
#####################################################
label map19:
    scene hbroom with wipe_corner
    pause .2
    fn "「What should I do today? 」"

    play music "<from 2.5>av/audio/free0422.ogg"
    call screen minasatomap19
    
#####################################################
label kouya19:

    hide screen house19
    scene map
    pause .01
    $ event_name = _("Live Concert")
    scene hbroom with sdis
    play music daily01
    $ renpy.music.set_volume(0.7, 0.0, channel = "music")
    
    fn "「...Okay then. 」"
    "I have my wallet.{w} I've picked out my clothes.{p}After rechecking one more time, I nodded my head."
    "Yep,{w=.2} it's perfect."
    "Today's the day I've been waiting for,\nthe day of Kouya's concert."
    "I've been a little restless since yesterday,\nand so, a little sleep-deprived.\nMy eyes are blinking more often."
    "However,{w=.2} that wasn't a problem,\nand a sense of excitement filled me up.{p}Just like a little kid before a trip."
    "Of course, I really can't help but enjoy myself.{p}The corners of my mouth went up without realizing it.\nIf I do say so myself it's dangerous, seriously."
    "Now, it's almost time for the bus.{p}If I miss the bus, I sure as hell am going to be late."
    
    
    stop music fadeout 10
    scene black with wipe_right
    scene rice red with wipe_right
    pause 1
    scene black with wipe_right
    scene bstop red with wipe_right
    pause 1
    scene black with wipe_right
    scene bus red with wipe_right
    pause 1
    scene black with wipe_right
    scene kazenari01 night with wipe_right
    pause 1
    scene black with wipe_right
    scene concert with wipe_right
    play music shop02
    
    "After riding on the bus and walking for about\n10 minutes, I safely arrived at a club\nin a certain section of town."
    "It'd be awesome if we could all go at the same time,{w=.2}\nbut unfortunately it seemed as if everyone got hit\nwith last minute plans."
    "So now I'm at the local hangout."
    "Everyone should be here soon,{w=.2} but with the\nplace much more packed than I figured it'd be,{p}can we actually meet up in all this confusion...?"
    "Seriously, look at all these people.{p}The band Kouya and his friend put together,\nit must really be popular."
    "Now that I think about it,{w=.2} I'm not really\nfamiliar with the topic about having a band.{p}In reality, I know nothing about it."
    "...Oh well.{w=.2} I'll try asking about it later."
    "For now, I have to think about connecting\nwith everyone else.{w} My cellphone would be useful,{w=.2}\nexcept no one else actually has one..."
    "I left home by myself too,{w=.2}\nso what am I going to do..."
    "Since I didn't have any really good ideas,{w=.2}\nI weaved my way through the crowd\nas I looked restlessly around me."
    "But I couldn't find any of them.{p}Did they actually come? {w=.2}\nI was starting to doubt it."
    
    stop music fadeout 7.5
    scene concert night with sdis
    
    "Suddenly,{w=.2}\nthe dim lights darkened even further.{p}Looks like it's time for the curtains to rise."

    play sound cheering1 fadein 1
    
    "In contrast to the deepening darkness,{w=.2}\nthe air was filled with cheers."
    "As if answering them, the forms\nof four beastmen appeared on stage."
    
    stop sound fadeout 3
    scene black with sdis
    pause 3 
   
    $ event_name = _("After Everything")

    scene kazenari01 night with sdis
    play music shop03
    show to 007 night at farleft
    show ky 001 night at center
    show ko 001 night at farright
    with wipe_right
    
    to "「Geez,{w} we said we'd all go together,\n\ \ so don't walk in by yourself like that. 」"
    fn "「...Sorry. 」"
    "In the end, the concert went off well,{w=.2}\nand I was able to meet up with everyone afterwards."
    "I was pretty much pushed out of the club,{w=.2}\nwhere I met everyone outside along with Kouya\nseeing off all the customers."
    "When I asked where they were,\nTorahiko replied with an angry{w=.2} 'that's my line!'"
    "In any case, it looks like they all got together\noutside the entrance."
    "I got here a bit earlier than that,{w=.2}\nand then hurried on inside.{w} So I just didn't come\nacross them at any point until then, it seems."
    "But still.{p}If I am supposed to meet up with everyone, staying\nby the door would have been sensible..."
    "There must be something in the air.{w=.2} I mean, how\ncould I not notice something so simple...{w} I really\ndoubt I can get rid of this self-hate anytime soon."
    
    show ky 002 night with dis
    
    ky "「You didn't show up even though we waited\\ \ nuntil the last second.{w=.2} Everyone was thinking\n\ \ you got stuck in bed with a cold, or something. 」"
    ky "「But still,{w=.2} overanxiety is better though. 」"
    fn "「Yes,{w=.2} sorry for worrying you... 」"
    
    show ko 004 night with dis
    
    ko "「Good grief,{w=.2} get a hold of yourself.{p}\ \ Just think things through a bit more\n\ \ before going anywhere. 」"

    show to 003 night at jump_up
    
    to "「Nobody wants to hear that from you.{p}\ \ You need to think a lot more,{w=.2}\n\ \ and keep an eye on the time when you come. 」"
    to "「Just how many years are you planning to be late? 」"
    ky "「Don't say that, Torahiko,{w=.2}\n\ \ it couldn't be helped even if you did. 」"
    "Everyone nodded at that.{p}Kounosuke just looked a little offended."

    scene kazenari01 night with wipe_right
    show ka 002 night at center with dis
    
    ka "「But yeah,{w=.2} thank you guys for coming. 」"
    fn "「Oh, Kouya.{w} All done with seeing everyone off? 」"
    ka "「Yep, they all went home.{p}\ \ About the only ones left are you guys. 」"
    fn "「Good work out there, then.{p}\ \ And that reminds me.{w} That show you put on,{w=.2}\n\ \ it was awesome!{w} I was a bit touched by it. 」"
    "It was the first time I saw Kouya's concert.{p}Well I have seen one alone,{w=.2}\nbut this was different."
    "Maybe it was the same for the other guys,{w=.2}\nas they enjoyed the show with great enthusiasm."
    "Even with the scheduled performance over,\nthere were calls for an encore."

    hide ka with wipe_right
    show su 002 night at farleft
    show ta 002 night at center
    show si 002 night at farright
    with wipe_right
    
    ta "「This year was especially exciting! 」"

    show su tailwag 01 night with dis
    
    su "「Yes,{w=.2} and Kouya-san was so coool! 」"
    si "「I'm not good with crowds like that,{w=.2}\n\ \ but I still had fun. 」"

    scene kazenari01 night with wipe_right
    show ju 002 night at midleft
    show so 003 night at midright
    with wipe_right
    
    ju "「As always,{w=.2} I thought it was a nice performance. 」"
    so "「Aotsuki-senpai,{w=.2} you were shinin' awesomely! 」"

    scene kazenari01 night with wipe_right
    show to 001 night at farleft
    show ko 001 night at farright
    show ky 001 night at center
    with wipe_right
    
    ky "「That's because you guys looked like you were having\n\ \ fun,{w=.2} and that makes it fun for us, too. 」"

    show ko at jump_up
    
    ko "「Yeah, yeah!{p}\ \ That was really amazing.{w=.2}\n\ \ I honestly respect you for that! 」"

    show to 003 night with dis
    
    to "「Huh,{w=.2} I guess you guys did good out there? 」"
    
    show ko 004 night with dis
    
    ko "「And you were so into it earlier.{w=.2}\n\ \ You're not being honest, Torahiko. 」"
     
    play sound bom35
    show to 005 night at briefzoom
    
    to "「Bwuh!?{p}\ \ {nw}"
    show to 013 night with dis
    extend "Stop saying stuff about things that didn't happen! 」"
    ko "「Right, right, my bad. 」"

    scene kazenari01 night with wipe_right
    show ka 003 night with wipe_right
    
    ka "「Thanks, you guys.{p}\ \ This concert has been the best one ever.{w=.2}\n\ \ Even the other guys in the band said so. 」"
    fn "「Then I guess I really did\n\ \ take part in something cool.{p}\ \ It feels pretty lucky. 」"
    ka "「I'm glad I gave you guys the best performance too.{p}\ \ Really,{w=.2} thanks for coming. 」"
    fn "「Nah, we should be saying that. 」"
    "With an unusually cheerful Kouya,{w=.2} my cheeks felt\nso slack.{w} It really is great I came to the concert."
    "If I came back much earlier,\nI think I could have seen this every year,{w=.2}\nthough I don't think I especially deserve it."
    "I wonder if they'll do it next year?{p}If they do,{w=.2} I definitely want to come see it\nagain..."

    hide ka with wipe_right
    show ta 001 night with wipe_right
    
    ta "「Oh yeah, what's everyone doing afterwards?{p}If you're all free, how about we all eat somewhere? 」"

    hide ta with wipe_right
    show to 001 night at farleft
    show ko 001 night at farright
    show ky 001 night at center
    with wipe_right
    
    to "「That doesn't sound bad to me. 」"

    show ky 003 night with dis
    
    ky "「Oh,{w=.2} sorry.{p}\ \ I was asked to do some shopping for the club today.{p}\ \ I had to come here with Sou. 」"
    ko "「Ah, is that so.{p}\ \ That seems like a lot of work.{w=.2}\n\ \ Should we all just stop for today? 」"
    
    show ky 001 night with dis
    
    ky "「No,{w=.2} you don't have to worry about us.{p}\ \ You guys can go on ahead. 」"

    scene kazenari01 night with wipe_right
    show ju 001 night at midleft
    show so 001 night at midright
    with wipe_right
    
    ju "「No, it's more fun when we're all together.{p}\ \ Besides, it doesn't have to be today. 」"
    ju "「It'd be better if it was when\n\ \ we all had some free time again. 」"

    show so 005 night with dis
    
    so "「Guess so,{w=.2} I'm real sorry 'bout the timin'... 」"

    scene kazenari01 night with wipe_right
    show su 001 night at farleft
    show si 001 night at farright
    show ta 001 night at center
    with wipe_right
    
    ta "「How about we split things off here then?{p}\ \ It's probably not so good for so many\n\ \ people to gather around here. 」"
    ta "「Hmm,{w=.2} if anyone wants to go by car I can take along\n\ \ one person.{w} {nw}"
    show ta 002 night  with dis
    extend " Anyone want on? 」"
    si "「No, I'm going to pass on that.{p}\ \ And it's been so long since I've come to Kazenari.{w=.2}\n\ \ I think I'll do some shopping, first. 」"
    su "「Oh, maybe I'll do that too.{p}\ \ I'm going to go say hi to Gaku-san. 」"

    scene kazenari01 night with wipe_right
    show ju 001 night at midleft
    show so 001 night at midright
    with wipe_right
    
    ju "「It's been a while for me too,{w=.2} so maybe I'll go\n\ \ to the sportswares shops with Takahara and Touno.{p}\ \ If they have a lot of luggage, I'll help them. 」"

    show so 003 night with dis
    
    so "「F'real!?{p}\ \ That'd be great! 」"

    scene kazenari01 night with wipe_right
    show to 001 night at farleft
    show ko 001 night at farright
    show ky 001 night at center
    with wipe_right
    
    ky "「Sorry about that Mikazuki.{p}\ \ If you mean that, I'll accept your offer this time. 」"
    ko "「I think I'll take a peek at the electronics store.{p}\ \ It's in the same direction, so I'll go\n\ \ with Shun-kun and Shin-kun. 」"
    to "「What, where are all you guys going?{p}\ \ Then I guess I'm riding with Tatsu-nii...{p}\ \ {nw}"
    show to 006 night with dis
    extend "Uh, wait, what do I do... 」"
    "「About Tatsu-nii's driving... 」 Torahiko mouthed.{p}Tatsu-nii didn't seem to notice."

    scene kazenari01 night with wipe_right
    show ta 002 night at midleft
    show ka 001 night at midright
    with wipe_right
    
    ta "「What, are you gonna bow out too, Torahiko?{p}\ \ {nw}"
    show ta 001 night with dis
    extend "Oh,{w=.2} but if we do that,\n\ \ we'll be leaving [fn] alone... 」"    
    fn "「Ah. 」"
    "I didn't notice that until just then myself.{p}It's true,{w=.2} I've carelessly been left behind!{p}W-what do I do?"
    ka "「It's okay,{w=.2} I'll take [fn] back home.{p}\ \ That is, if you're fine with the back of my\n\ \ motorbike, [fn]? 」"
    fn "「Eh, is that okay!?{p}\ \ I've always wanted to ride on one at least once!{p}\ \ Please! 」"
    
    show ka 002 night with dis
    
    ka "「Okay,{w=.2} that settles it. 」"

    show ta 002 night at briefzoom
    
    ta "「Right, then we take off here! 」"
    
    stop music fadeout 3
    scene black with sdis  
  
    $ event_name = _("A Trivial Question")

    scene market night
    show ka 002 night at center
    with sdis
    play music free58
    
    fn "「Thanks for inviting me to the concert\n\ \ and then taking me back,{w=.2} Kouya. 」"
    "As I gave back his helmet,{w=.2}\nI thanked Kouya for everything today.{p}I had a really good time."
    ka "「Don't worry about it.{p}\ \ I wanted to thank you too. 」"
    fn "「I see.{w=.2} I guess it evens things out. 」"
    
    show ka 001 night with dis
    
    ka "「But is it okay for me to take you this far?{p}\ \ Shouldn't I take you all the way home? 」"
    fn "「It's fine,{w=.2} it's not far from here.{p}\ \ Besides, isn't it easier for you\n\ \ to go back yourself like this? 」"
    "My house (more accurately, my grandparents' house){w=.2}\nis mostly in the residential area but slightly off,\nas it's elevated."
    "That's why I figured being a little way\nfrom it would be better for Kouya."
    ka "「Well,{w=.2} if you say so... 」"
    fn "「Mhmm.{w=.2} You don't need to worry about it too much. 」"
    ka "「Just be careful going back.{p}\ \ It's not like the city, there isn't\n\ \ much lighting outside. 」"
    fn "「I said I'm fine. You worry too much. 」"
    ka "「I see. Sorry then.{p}\ \ {nw}"
    show ka 002 night with dis
    extend "...Well then,{w=.2} later, [fn]. 」"
    fn "「Yeah, see you later Kouya.\n\ \ Good night. 」"
    ka "「Ah,{w=.2} good night. 」"

    hide ka with dis
    
    "And that was the end of the parting words.{p}{nw}"
    play sound load_gun
    pause 1.5
    play sound motor_engine
    extend "As the engine revved up,{w=.2} the bike Kouya rode on\ndrove off into Minasato's night."
    "After I saw off that back,{w=.2}\nI walked the path back up to the house."
    fn "「...Hm? 」"
    "In the distance,\nI saw Kouya turn left at an intersection."
    "However,{w=.2} in my memories Kouya's home\nshould be closer and to the right."
    "...What's going on?{p}Maybe he has to park the bike somewhere?"
    "Still, it's a trivial question.{w} But in that question,\nI think I felt something important,{w=.2} and that night,\nI couldn't help but keep thinking about it."
    
    jump end19
    
    
#####################################################
label juuichi19:
    
    $ event_name = _("A Midsummer Day's Dream")

    play music cicada01
    scene hbroom with dis
    
    "It's early afternoon, and my stomach is full."
    "I don't have anything in particular to do,\nso I'm daydreaming while watching tv\nin the lukewarm breeze of the fan."
    "Onscreen, a newscaster\nreads a report on minerals."
    "I change the channel,{p}but it's just a mushy soap opera\nand I have no idea what's going on."
    "I can't watch any of the usual lunchtime programs\nbecause of one lethal flaw:{p}State-managed channels don't reach here."
    "This is the time when it's hottest outside, too..."
    "Well, I've been going out a lot since I got here.{p}It's okay to take it easy once in a while, right?"
    
    play sound phone_ring loop
    pause 1.5
    
    "Suddenly, I hear the phone ringing mixed with the\ncries of the cicadas."
    "Thinking my grandma will answer it,{w=.2}\nI continue to watch tv."
    "...{p}...{p}..."
    "...Hm?{w} 　Come to think of it,{w=.2}\nGrandma and Grandpa went out,\nasking me to watch the house."
    "Crap, it keeps ringing!{p}I stand up, rush to the hallway,{w=.2}\nand leap for the receiver."
    
    scene black with wipe_right
    scene hentry with wipe_right
    play sound phone_pickup
    
    fn "「Hello,{w=.2} [ln] speaking!! 」"
    "Whew,{w=.2} I got to it before they hung up...{p}I sigh with relief in my head,\nso the person on the other end doesn't hear it."
    who "「...Jeez...{p}\ \ [fn],{w=.2} don't yell so loud.{p}\ \ My ears are ringing now. 」"
    
    stop music fadeout 5
    
    fn "「Oh,{w=.2} is that you, Torahiko?{p}Sorry, I forgot I was the only one home right now. 」"
    
    play music pops_001
    to "「Come on now,{w=.2}\n\ \ get your head in the game. 」"
    fn "「I said I was sorry.{p}\ \ ...So, what do you want? 」"
    to "「Well,{w=.2} I wasn't calling for anything in particular.{p}\ \ [fn], are you busy right now? 」"
    fn "「Yeah.{w=.2} I was just watching tv. 」"
    to "「Just like a student on summer vacation should be. 」"
    fn "「I know, right? 」"
    to "「So,{w=.2} you're not busy.{p}\ \ Want to go do something?{p}\ \ I'm finally done with all my chores for today. 」"
    "I'm on the verge of agreeing to his proposal,\nbut then I remember that I'm the only one here."
    "I was asked to house sit,{w=.2}\nwhich means I shouldn't be going out..."
    fn "「...Oh, sorry.{w} Thanks for the offer,{w=.2}\n\ \ but I can't go out until my grandparents get back. 」"
    to "「I see...{w} Well, I guess your hands are tied... 」"
    "He sounds disappointed.{p}I can picture him standing in front of the phone\nwith his shoulders handing low."
    fn "「Yeah,{w=.2} I can't come out, but...{p}\ \ There's no reason you can't come over and hang out. 」"

    play sound dream
    
    to "「Really?{w=.2} That'll work!{p}\ \ You're really on the ball now, [fn]! 」"
    "His tone instantly becomes cheerful.{p}...He really hasn't changed.{p}I can't help but smile."
    to "「So it's ok if I come over right now? 」"
    fn "「Of course. 」"
    to "「All right.{w=.2}\n\ \ I'll be at your place by 3 o'clock! 」"
    
    stop music fadeout 5
    play sound phone_end
    
    "I hear him hang up the phone at the same\ntime he says goodbye."
    "I didn't get the chance to reply...{p}He really hasn't grown up since I left."
    "Looking at the clock, I see it's 2:30.{p}There's still some time before he gets here,{w=.2}\nso I'll tidy the room a bit before he arrives."
    "I hang up the phone, and start organizing my room."
    
    scene black with sdis
    scene hbroom with sdis
    play music tam_n06
    
    to "「Heey! You there, [fn]? 」"
    
    play sound tm2_slidedoor000
    
    "I hear the sound of the door opening.{p}At the same time, I hear him call from the hallway.\nIt sounds like he's here."
    fn "「Torahiko,{w=.2} come in. 」"
    "I lean over, stick my head into the hallway,{w=.2}\nand beckon him in."
    to "「Thanks for having me over! 」"
    fn "「This way. 」"
    to "「Sure. 」"
    "I hear the floor squeak in the hallway{w=.2}\nas he approaches.{w} Stopping in front of my room,{w=.2}\nI see him gingerly standing at the door."
    
    show to 007 at center with dis
    
    to "「...Sorry,{w=.2} did I make you wait? 」"
    fn "「Yeah,{w=.2} it's way past 3.{p}\ \ ...Did something happen to you on the way over? 」"
    to "「Well, I thought it'd be rude for me to show up\n\ \ empty-handed, so I stopped and got this. 」"
    "Torahiko pulls his hand out from behind his back.{p}In it is a plastic bag.{w} On closer inspection,{w=.2}\nI can make out the contents."
    "...Mmm, is that what I think it is?"
    fn "「You stopped and got ice cream for me? 」"
    
    show to 013 with dis
    
    to "「...Heh heh. 」"
    "He rubs his lip in embarrassment."
    fn "「Thank you, Torahiko. 」"

    show to 002 at jump_up
    
    to "「N-{w=.2}no problem!{p}\ \ Now, let's eat it before it melts!{p}\ \ Which one do you want? 」"
    fn "「Either one's fine with me.{p}\ \ You choose first. 」"
    
    show to 010 with dis
    
    to "「Don't be so polite, we're friends! 」"

    show hbroom at hshake
    play sound hit_p07
    pause .4
    play sound hit_p07
    
    "He comes up to me and smacks me on the back.{p}...Hmm, but he's the one who bought it,{w=.2}\nso it'd be rude for me to choose first..."
    
    show to 001 with dis
    
    to "「Come on, hurry up and pick one! 」"
    
    play sound puu75
    
    "He forces the bag into my hands.{p}Well,{w=.2} it's okay if he tells me to, right?{p}I'll be grateful that he's letting me choose first."
    "I take a look inside the bag.{p}There's one cup and one soft serve.\nBoth of them are vanilla-flavored."
    "...Uhh, Torahiko.{p}As grateful as I am that you got me this,{w=.2}\nyou could at least have gotten different flavors."
    "I won't tell him that.{p}So,{w=.2} which one?"
    
    menu:
        "A. Choose the cup":
            jump juuichi19_cup
        "B. Choose the soft serve":
            jump juuichi19_softserve

    #######################################################
    label juuichi19_cup:
            
        $ event_name = _("In the Mood for a Cup")
        
        fn "「Hm, I guess I'll take this one then. 」"
        "I rummage around in the bag, take out my ice cream,\nand set it on the table.{p}I hand Torahiko the other one."
        to "「Hm,{w=.2} you like the cup kind? 」"
        fn "「Well, either one is fine.{p}\ \ Soft serve tends to melt and get all over your\n\ \ hands, though. 」"
        "I sit down as I give him my answer.{p}I pass a cushion to Torahiko, too."
        
        show to 010 at center with dis
        
        to "「...Oh, thanks.{p}\ \ {nw}"
        show to 001 with dis
        extend "I like soft serve because you can eat a lot of\n\ \ it at once. 」"
        "He puts a cover on the cushion\nto protect it from his ice cream."
        "...Wow, he's already eaten a third of it.\nI wonder if he's going to get\nbrainfreeze from eating it so quickly?"
        fn "「Well, it makes no difference\n\ \ which you choose in the end.{p}\ \ ...Ah! 」"
        "The moment I open the lid,{w=.2}\ndrops of molten ice cream fly onto my face.\n...This is worse than getting it on my hands."
        
        show to 007 with dis
        
        to "「Aw, what a waste.{w} {nw}"
        show to 001 with dis
        extend "...Here. 」"
    
        hide to with dis
        
        "As he says that, Torahiko leans over the table,{w=.2}\nand wipes the ice cream off my face with his finger.{p}Then, he sticks out his tongue and licks it off."
        
        show to 006 with dis
        
        to "「Mm, it's kind of salty.{p}\ \ It had some of your sweat in it too,{w=.2} didn't it? 」"
        fn "「Stop talking like that.{p}\ \ I don't need to be flirted with, okay? 」"
        
        show to 007 with dis
        
        to "「Yeah, yeah,{w=.2} I know. 」"
        "Our eyes meet.{p}{nw}"
        show to 002 with dis
        extend "Neither of us can stand the silence,{w=.2}\nso we laugh at each other."
        
        jump juuichi19_talk
    
    #########################################################
    label juuichi19_softserve:
            
        $ event_name = _("The Age of Softness")
        
        fn "「Hm, I guess I'll take this one then. 」"
        "I rummage around in the bag, take out my ice cream,\nand set it on the table.{p}I hand Torahiko the other one."
        
        show to 002 with dis
        
        to "「Thanks. 」"
        "Beastmen nails are sharp compared to a human's.{p}If he's not paying attention,\nhis nails could catch and tear something."
        "...Although it probably hasn't melted that much,{w=.2}\nit's tragic when ice cream is spilt."
        "I sit on the floor and offer Torahiko a cushion.{p}Thanking me, he sits down,\ncareful not to sit on his tail."
        
        show to 001 with dis
        
        to "「Hm,{w=.2} you like soft serve? 」"
        fn "「Well,{w=.2} either one is okay.{p}\ \ It's just that you can eat soft\n\ \ serve all the way down to the cone. 」"
        fn "「I think that's the main advantage it\n\ \ has over cups. 」"
        "I take off the cover from my ice cream,{w=.2}\ntaking care not to destroy the shape."
        to "「Oh,{w=.2} I see.{p}\ \ Well,{w=.2} I like the cup kind\n\ \ because you can eat it one bite at a time. 」"
        fn "「...That's unlike you. 」"
    
        show to 003 at jump_up
        
        to "「Be quiet. 」"
        "He manages to answer with the spoon in his mouth."
        "After making sure that his ice cream actually\nmakes the journey to his mouth,{w=.2}\nI start on mine."
        "Ahh, this is good.{p}Ice cream is best during summer."
    
    ###########################################################
    label juuichi19_talk:
            
        $ event_name = _("Something that Will Never Come True")
        
        stop music fadeout 5
        scene black with sdis
        scene hbroom
        show to 006 at center 
        with sdis
        play music free02
        
        to "「Haah,{w=.2} summer break is already halfway over. 」"
        fn "「...Well- 」"
        "I suddenly stop speaking,{w=.2}\nas a strange feeling of sadness hits me.{p}The month really is half gone, isn't it..."
        to "「Ah,{w=.2} I need to get to work on my homework.{p}\ \ I've just been slacking off so far. 」"
        fn "「You have to do your homework.{p}\ \ It's a student's duty. 」"
        "I try saying something out of character.{p}Well, honestly, I probably couldn't do it either."
        "Torahiko makes a weary face at my statement."
        
        show to 007 with dis
        
        to "「Yeah, yeah,{w=.2} thanks for the model student reply.{p}\ \ {nw}"
        show to 001 with dis
        extend "...You've gotten a bit stiff, haven't you?{p}\ \ You used to put fun before everything else. 」"
        fn "「That was then,{w=.2} this is now.{p}\ \ ...Torahiko, I'm guessing you haven't changed\n\ \ much since I left, right? 」"
    
        show to 003 at jump_up
        
        to "「What?! 」"
    
        play sound book_close
        
        "He slams his ice cream on the table,{w=.2}\nand stands up without making a sound."
        "Then he lunges towards me,{w=.2}\nand puts me in a headlock."
        "I can't help but laugh.{p}Torahiko's acting like he always does."
        "Unfortunately, he takes the\nchance to tighten his grip."
        
        show to 003 at jump_up
        play sound hit_p07
        
        to "「I've grown up! 」"
        fn "「Owowow,{w=.2} I'm sorry, I'm sorry! 」"
        to "「No,{w=.2} I won't forgive you! 」"
        "Augh, give me a break!"
        to "「My body has grown too,{w=.2}\n\ \ enough that the person I love- 」"
        
        stop music fadeout 5
        
        fn "「Wait, what did you just say? 」"
        "I can't let something like that slip by.{p}{nw}"
        show to 005 at jump_up
        extend "When I ask,{w=.2} he lets go, and moves back from me."
        "Torahiko's expression is as easy to read as ever.{p}Embarrassment is written all over his face."
        
        play music free0428
        
        fn "「Wow,{w=.2} you're in love with somebody? 」"
        
        show to 006 with dis
        
        to "「Uh,{w=.2} Th-{w=.2}that was... 」"
        "Rubbing my sore head,\nI ask him a blunt question.{p}His face is getting more red by the second."
        "I feel slightly sorry for him, but...{p}I did ask something similar while we were camping.{p}...All right, I'll prod a little more."
        "Justice will prevail!"
        fn "「So,{w=.2} who is it?{p}\ \ As your childhood friend,\n\ \ I have a right to know. 」"
        "I try asking in my best coaxing voice.{p}Torahiko moans, but doesn't say anything."
        
        show to 008 with dis
        
        to "「Ooh... 」"
        fn "「You gave me an answer when we were camping,{p}\ \ but now you're just staying quiet?{w=.2}\n\ \ Don't you think that's kind of pathetic as a man? 」"
        
        show to 006 with dis
        
        to "「... 」"
        "His ears droop.{p}It seems that 'as a man' was a critical hit."
        "It's only a matter of time until he cracks.{p}Hmph, Torahiko is mere child's play\nfor [fn]-sama."
        "I'll get him in one fell swoop!{p}The key is to speak softly."
        fn "「Why don't you go right out and say it?{p}\ \ I'm sure it'll be easy. 」"
        
        show to 007 with dis
        
        to "「...Why are you doing this? 」"
        "He mutters at me, tears in his eyes.{p}Looking at me like that won't get you any sympathy,{w=.2}\nI can promise you that."
        "Even so, Torahiko loves somebody?{p}He seems to be the type of guy to go for looks,{w=.2}\nso it must be the prettiest girl in his class."
        "No, the bookish girl who looks good in glasses.\nThat could be it, too."
        "Come to think of it, he loves these subjects.{w=.2}\nHe never seems to talk about himself, though.{p}...Hm, I think that's unfair."
        
        show to 003 at jump_up
        play sound bom19_b
        
        to "「F-fine, I'll tell you!{p}\ \ Is that what you want? 」"
        "...Ah, the offender becomes the offended.{p}However, I've pushed him far enough.{w=.2}\nI wait for him to say it."
        "...{p}...{p}..."
        fn "「Well,{w=.2} Torahiko? 」"
        to "「I need to prepare myself! 」"
        "He grumbles to himself so I can't hear him.{p}Hm, it's odd for a guy like him to hesitate."
        "This goes on for about 5 minutes.{p}Just as I'm getting bored,{w=.2}\nTorahiko opens his mouth to speak."
        "Is he really that worried about telling me?{p}It's not like we go to the same school,{w=.2}\nso I can't spread it around or anything."
        
        show to 013 with dis
        stop music fadeout 5
        
        to "「I-I'm gonna say it... 」"
        fn "「...Go on. 」"
        "He uses his long tongue to moisten his lips.{p}In order to push him along, I swallow some saliva."
        
        show to 003 with dis
        
        to "「The person I love is- 」"
        "He stops speaking, and looks me in the eye.{p}His nervous expression has changed,{w=.2}\nand now he looks completely serious."
        "For some reason, he's starting to scare me.{p}It feels like he's hunting me with his eyes."
        to "「It's you,{w} [fn]. 」"
        fn "「...{w=.2}Huh? 」"
        "Of all the things he could have said,{w=.2}\nI was never expecting that."
        "If I didn't just mishear him...{p}Torahiko just said he loves me, didn't he?"
        fn "「...{w=.2}Me? 」"
        
        show to 013 with dis
        
        to "「... 」"
        "He sheepishly nods.{p}Even though his face is red,{w=.2}\nhe doesn't take his eyes off me."
        
        play music daily02 fadein 1.5
        
        "...Oh.{p}I get it.{p}This is just another one of his jokes, isn't it?"
        "There's probably some lame punchline coming up.{p}...Jeez, he really had me going, didn't he?"
        fn "「...J-{w=.2}just say you're joking already. 」"
        
        stop music
        show to 003 at jump_up
        play sound bom26_b
        show hbroom at vshake
        
        to "「This isn't a joke! 」"
        "He practically yells his reply at me."
        to "「Would I joke about something like this...? 」"
        fn "「... 」"
        
        play music melodious02
        
        to "「Even back then...{w=.2} Before you changed schools...{p}\ \ I've always loved you. 」"
        fn "「Torahiko... 」"
        
        show to 007 with dis
        
        to "「...Ha ha, I knew saying it so suddenly\n\ \ would make things awkward. 」"
        fn "「...No, it didn't. 」"
        "I shake my head.{p}A confession from him certainly\ndid come out of nowhere, but..."
        "Now that I think about it,\nI feel like I should have seen it coming."
        "He's awfully fond of physical contact,{w=.2}\nand he tends to go overboard when he's around me."
        "...Is it normal to want to tease the one you love?"
        fn "「I'd be lying if I said I wasn't surprised... 」"
        to "「... 」"
        fn "「... 」"
    
        show to 013 at jump_up
        
        to "「...So,{w=.2} um,{w=.2} [fn]... If it's okay with you,{p}\ \ will you go out with me? 」"
    
        hide to with dis
        
        "Torahiko thrust his hand face-down towards me.{p}It's shaking a bit."
        "What has Torahiko been to me?{p}A good friend?{w} 　...Or something more than that?"
        "My memories of him this summer float across my mind,{w=.2}\nthen disappear."
        "Fighting Kouya constantly,{p}getting thrown by Juuichi-san,{p}and playing with Shun-kun."
        
        #;Since I've come back,
        #;I've seen him almost every day.
        #;What no you haven't
        #;This line's too contradictory later
        
        "To me, Torahiko is..."
        
        menu:
            "A. More than a friend":
                jump juuichi19_lover
            "B. Just a good friend":
                jump juuichi19_friend
    
    
    #####################################################
    label juuichi19_lover:
            
        $ event_name = _("A Happy Ending")
        
        "He's always been at my side,{w=.2}\nand he's always cherished me."
        "I always took that for granted,\nbut those are irreplaceable things."
        "Yeah, that's what he is to me..."
        "I take his outstreched hand, and pull.{p}Caught by surprise, Torahiko falls towards me."
        "I try to catch him...{w=.2}\nBut I can't support his weight,{w=.2}\nand we fall to the floor."
        
        play sound bosu35
        
        to "「Wah!{w} 　What're you... 」"
        "He realizes what's going on,\nand his sentence trails off."
        "Depending on how you look at it...{p}No, this would be obvious to anybody.{w=.2}\nTorahiko crouches over me as I lay on my back."
        to "「H-{w=.2}hey, [fn]?{w} 　What was that for? 」"
        "I sit up a bit, and kiss him on the mouth."
        "In an instant, his whole body freezes.\nI can plainly see all his fur standing on end."
        "His tail springs up,\nbut then relaxes and droops down."
        "I can smell the scent of vanilla and sunflowers\ncoming from him."
        "Eventually, our lips part.{p}Torahiko's eyes are still wide in confusion."
        "As I look into them,{w=.2}\nI speak the words I've been keeping down."
        fn "「I love you too, Torahiko. 」"
        to "「...Really? 」"
        "After a long silence,\nTorahiko is finally able to speak."
        fn "「Well,{w=.2} there's no sense in lying to you now.{p}\ \ I... I couldn't do that to you. 」"
        "Becoming awfully embarrassd myself,{w=.2}\nI quickly look away from him."
        "My cheeks are getting really hot.{p}I'm sure they're quite red at the moment..."
        to "「Well, you wouldn't have done all that\n\ \ if you didn't feel like that. 」"
        "When I glance at him,\nI see him staring at me\nwith a dazed look on his face."
        to "「Hey,{w=.2} [fn]. 」"
        fn "「Hm?{w=.2} What is it? 」"
        to "「Say it again. 」"
        fn "「...Again?!{p}\ \ It's so embarrassing, though...{p}\ \ Fine, just for today. 」"
        "I take a deep breath."
        fn "「Torahiko,{w=.2} I love you. 」"
        
        show hbroom at vshake
        
        to "「[fn]!!! 」"
        "He picks me up, and gives me a\nhug so tight it hurts."
        "I wrap my arms around his back\nand give him the biggest hug I can in return."
        
        stop music fadeout 5
        scene black with sdis
        pause 2
        scene ooshima_inn_out with sdis
        play music cicada01
        
        to "「Hey,{w=.2} [fn]!{p}\ \ The new guests are here! 」"
        fn "「Oh,{w=.2} I'll just be a minute! 」"
        "Once again, summer has arrived.{p}It's a season I'll never forget."
        "I graduated from school, and,\ndespite the objections from my parents,\nmoved back to Minasato."
        "I couldn't imagine living away from\nTorahiko any longer."
        "Thanks to him pulling some strings,{w=.2}\nI was able to live and work at the Ooshima Inn."
        "I've always been on good terms with his uncles.{p}They were happy to add another son to the family."
        "I live in my hometown to this day,\nsavoring the happiness of living\nunder the same roof as Torahiko."
        to "「Hey!{w=.2} You're going to be the bottom tonight\n\ \ if you don't get down here soon! 」"
        fn "「Gah...{w} Your uncles can hear us, can't they?! 」"
        to "「The longer you take,{w=.2}\n\ \ the more embarrassing stories I'll tell them! 」"
        fn "「...Ah!{w} 　I'm coming! 」"
        "I hurry down to the person I love.{p}I hope this happiness lasts forever..."
        
        stop music fadeout 5
        scene black with sdis
        pause 2
        
        $ renpy.full_restart()
    
    #######################################################
    label juuichi19_friend:
            
        $ event_name = _("The Cost of a Confession.")
        
        "I repeat his confession to myself.{p}Do I love Torahiko?"
        "If I loved him,{w=.2} and accepted him as my boyfriend,{p}I should be full of happiness right now.{p}I don't feel that way."
        "This breaks my heart.{p}It painfully stabs my chest."
        "Images start to build up in my mind."
        "Torahiko's smiling face is covered\nby that person's awkward smile."
        "Torahiko's embarrassed face is buried\nby that person shyly turning his face away."
        
        stop music fadeout 4
        
        "...Yes,{w=.2} that's right.{p}The person I really love is-"
        
        play music free58
        
        fn "「...Torahiko. 」"
        
        show to 006 with dis
        
        "When I speak,\nhe jumps in surprise."
        fn "「I'm really happy you feel that way. 」"
    
        show to 011 at jump_up
        
        to "「S-{w=.2}so that means...! 」"
        fn "「But...{w=.2}\n\ \ I'm not going to go out with you.{p}\ \ I'm sorry. 」"
        
        show to 005 with dis
        
        "His face falls.{nw}"
        show to 007 with dis
        extend "{p}His tail, betraying his emotions,{w=.2}\nfalls to the floor."
        to "「...Ha ha,{w=.2} I got rejected, huh?{p}\ \ Somehow I knew this was going to happen. 」"
        "The voice he manages to sqeak out is something\nI never imagined coming from him.{w=.2}\nIt hurts me to hear him like this."
        fn "「I really am sorry. 」"
        
        show to 006 with dis
        
        to "「...Haah,{w=.2} I've wanted to do this since we were kids,\n\ \ so it's been about 10 years. 」"
        to "「Is it rare these days?{p}\ \ To fall in love with a guy who moved to the city? 」"
        "I can do nothing but nod."
        to "「Hey,{w=.2} [fn]. 」"
        fn "「What? 」"
        to "「Is there someone else you love? 」"
        fn "「...Yeah. 」"
        to "「I see...{w} Back when you lived here,\n\ \ we used to see each other every day. 」"
        to "「Since you've been back,\n\ \ I can count the number of\n\ \ times I've seen you on one hand. 」"
        
        show to 007 with dis
        
        to "「...And now you're at the age where you do things{w=.2}\n\ \ like fall in love with somebody. 」"
        "He speaks in a lonely-sounding voice,\nthen sighs."
        fn "「Well yeah,{w=.2} we're the same age. 」"
        to "「When we were little, you said\n\ \ 'I'm going to marry you when we grow up!' 」"
        fn "「... 」"
        
        show to 006 with dis
        
        to "「[fn]...{w} I hope things go\n\ \ well for you and that person. 」"
        fn "「...Thanks. 」"
        to "「...Well.{w} I should get back home. 」"
        fn "「...All right. 」"
    
        hide to with sdis
        
        "As he turns his back to leave,\nI see his shoulders shake slightly."
        "When I see that, I go to approach him.{p}...Then I stop myself."
        "What I was about to do would have been selfish.{p}He probably wouldn't be able to stand being being\ncomforted by the person who just turned him down."
        "I don't want to hurt him more than I already have.{p}It's best to do nothing right now.{p}That's what I tell myself."
        "Torahiko seems smaller than his usual self.\nI just stand there and stare silently at his back."
        to "「It's probably gonna take some\n\ \ time for me to get over this. 」"
        fn "「...Yeah. 」"
        to "「But even so,{w=.2} we're still friends...{w} Right? 」"
        fn "「Of course we are! 」"
        to "「...{w=.2}Thanks. 」"
        "He rubs his eyes with the back of his hand."
        to "「All right then,{w=.2} I'm leaving. 」"
        fn "「...Yeah.{w} See you later. 」"
        "Torahiko walks out of the room in silence.{p}Usually I'd see him off at the door,\nbut today I can't."
        
        play sound tm2_slidedoor000
        
        "The sound of the door opening and closing\nechoes through the house."
    
        stop music fadeout 5
        play music cicada01 fadein 5
        
        "I sit down with a thump and sigh.{p}I didn't think that it would be\nso painful to reject somebody."
        "I was just watching documentaries and soap operas,{w=.2}\nbut what happened just now... That was really tough."
        "If I'd known I was going to feel so guilty,{p}maybe I should have lied about my feelings,{w=.2}\nand gone out with Torahiko."
        "I shake my head.{p}I shouldn't have carelessly become his boyfriend.{p}I couldn't do that."
        "I'd just be making things easy for myself,{w=.2}\nwithout thinking about how others feel.{p}I'd end up hurting him some day."
        "This... This was the right thing to do."
        "..."
        "I sigh again.{p}That's right, Juuichi-san is the one I...{w=.2} love."
        "It feels like I've been spending more time with him\nthan I used to, but I never thought about why."
        "...No, that thought has been in my heart since the\nbeginning. I must have been denying it."
        "It's no use, though.{p}Once I start thinking about him,\nI can't get him out of my head."
        "When I close my eyes, all I can see is Juuichi-san."
        "Looking sullen when he's actually in a good mood.{p}Scratching his chin when he's troubled.{p}Getting seriously mad when provoked."
        "...I want to see Juuichi-san.{p}I want to see him and talk to him.{p}And I want him to smile, just for me."
        "As I think about things that are sappy,{w=.2}\neven for me."
        "I look up at the calendar on the wall.{p}It's already past the halfway point of my vacation."
        "I have limited days, limited hours.{p}How do I see him more, so that I have no regrets?{p}From now on, I need to act carefully."
        "I slap my face with my hands to\nget myself pumped up."
        
        scene black with dis 
   
        jump end19

#####################################################    
label end19:
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

    jump day20
    
    
    


