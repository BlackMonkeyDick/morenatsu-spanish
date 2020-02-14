###Day 30

label day30:
    
    $ renpy.music.set_volume(1.0, 0.0, channel = "music")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound2")
    
    $ day = 30
    $ the_date = "August 30"
    $ event_name = "８月30日"
    
    window hide
    play music birds_chirping                
    scene sky01 
    show text "{size=+130}August 30" at truecenter
    with Dissolve(.5)            
    pause 3
    scene black with Dissolve(1)
    pause .4    
    $ renpy.jump (favorite + "30")
    
#######################################################
label kounosuke30:

    scene hbroom with wipe_corner
    play music cicada01 fadein 2.5
    $ renpy.music.set_volume(0.4, 0.0, channel = "music")

    "August 30th."
    "Another summer vacation ends tomorrow.{p}I'm returning home then,{p}so today is the last real day I can play."
    "Somehow, this long month has passed,{p}in the blink of an eye."    
    "Well, what should I do today.{p}I would gather all of my stuff,{p}but I didn't bring that much luggage."    
    "I decide to go visit Kounosuke's place."
    
    scene black with wipe_right
    scene kouno_house_in with sdis
    $ renpy.music.set_volume(0.7, 0.0, channel = "music")
    play sound door_slide
    
    fn "「Hello... 」"
    
    if kouno_badend == True:
        jump kounosuke30_badend
    else:
        jump kounosuke30_goodend
    
    ######################################################
    label kounosuke30_goodend:
        
        $ event_name = "Once again, A Tanuki in the Forest"
    
        show yk 001 at center with dis
        
        yk "「Oh, welcome. 」"
        "When I enter the store,{p}Yukiharu-kun greets me."
        fn "「Good afternoon. Is Kounosuke here? 」"
        yk "「Oh, Kounosuke went out somewhere. 」"
        "Damn it. He's not home."
        fn "「Do you know where he went? 」"
        
        show yk 003 with dis
        
        yk "「Sorry, I have no idea.{p}\ \ He always leaves before I notice. 」"
        fn "「Hmm, I see... 」"
        
        show yk 001 with dis
        
        yk "「He always comes back for lunch,{p}\ \ so you can wait here until then to see him. 」"
        fn "「Hmm, no, I'll go look for him in the village.{p}\ \ I might come back at noon though. 」"
        yk "「Is that so? 」"
        fn "「See you later, Yukiharu-kun. 」"
        
        show yk 002 with dis
        
        yk "「Please come back again! 」"
        
        stop music fadeout 3
        play sound door_slide
        scene black with sdis
        scene path with wipe_right
        play music free60
        $ renpy.music.set_volume(0.7, 0.0, channel = "music")
        
        "With that said, where should I look?{p}Where would he likely go...{p}He could be anywhere."
    
        show na 002 at center with dis
        
        who "「Ah, hello... 」"
        fn "「Huh? Oh, hello. 」"
        "I wasn't aware at first,{p}that somebody was calling out to me.{p}Err, who is this kid?"
        "He seems very familiar, but...{p}Hmm... it's no use.{p}I just can't remember."
        who "「Onii-san, are you walking alone? 」"
        fn "「No, I'm looking for someone. 」"
    
        show na 001 with dis
        
        who "「Someone? Oh, perhaps Yuki's big brother? 」"
        "Oh, now I remember.{p}This kid is Yukiharu-kun's friend."
        fn "「That's right, do you know,{p}\ \ where he is by any chance? 」"
    
        show na 002 with dis
    
        ykfr "「Yeah. I saw him going to the forest earlier. 」"
        fn "「Oh, really? 」"
    
        show na 001 with dis
        
        "What good timing.{p}It seems looking in the village,{p}would have been a waste of time."
        fn "「Thank you, err... 」"
        ykfr "「Nanafuse. [fn] Nanafuse. 」"
        fn "「Wow, that's the same first name as mine.{p}\ \ Oh, I'm [fn] [ln].{p}\ \ Thank you, Nana-kun. See ya! 」"
    
        show na 002 with dis
        
        na "「See you later! 」"
        
        stop music fadeout 2
        play music higurasi fadein 2
        scene rice with wipeleft
        
        "Just as I'm about to continue down the road,{p}I suddenly turn back."
        fn "「You know, before... 」{nw}"
        play sound wind_noise
        scene path with qdis
        extend ""
        "I feel like I was about to talk to somebody,{p}but when I turned my head there was no one there."
        "A slightly cold wind blows,{p}and the grass on the side of the road rustles."
        
        $ renpy.music.set_volume(0.5, 0.0, channel = "music")
        play music cicada01 fadein 2
        
        fn "「...Huh? 」"
        "Umm, what was I doing?{p}Oh, that's right."
        "I'm going to the forest,{p}to search for Kounosuke."
        "The dazzling sunlight sparkles through the trees.{p}However, it feels like I'm somewhere desolate.{p}I wonder if that's because of the weakened sunlight."
    
        scene forest01 with sdis
        
        "But it still is Summer weather,{p}even after the festival.{p}The lukewarm humid air coils around my body."
        fn "「Ah, crap. 」"
        "While halfheartedly talking,{p}about the closeness of Autumn..."
        "Those things are still shooting,{p}an unpleasantly high frequency into my ear.{p}I scratch the back of my neck after I'm bitten."
        "Damn, those guys work just as fast as ever.{p}Someday I'll invent something,{p}to annihilate all of them."
        "A super-strong insecticide,{p}that's harmless to other organisms."
        "Oh?"
        "Is that Kounosuke?"
    
        show ko 001 at center with dis
        
        "Ah, it is him.{p}Good. I found him surprisingly fast.{p}I won't have to scour the village for him."
        fn "「Heey, Kounosuke! 」"
        "......{p}No response."
        "He's pointing his camera at something again.{p}I wonder what he's taking a picture of?"
        fn "「Kounosuke? 」"
    
        show ko 006 at jump_up
        stop music fadeout 5
        play sound bosu34
        pause .2
        
        ko "{size=+15}「UWAAAA!? 」"
        "I used a soft voice so I wouldn't startle him,{p}but that seems to have had the opposite effect.{p}He was completely surprised."
    
        play music daily02
        show ko 005 with dis
        
        ko "「Wh-what, [fn]? 」"
        fn "「Don't get so surprised like that... 」"
    
        show ko 001 with dis
        
        ko "「In the forest it's normal to be surprised,{p}\ \ when your name is suddenly called out,{p}\ \ from behind you like that. 」"
        "Hmm, he does have point."
        fn "「Sorry... 」"
        
        show ko 005 with dis
        
        ko "「Jeez...{nw}"
        show ko 006 with qdis
        extend " Ah! 」"   
        "Kounosuke remembers what he was doing,{p}and turns his camera back,{p}to what he was pointing it at before."
    
        show ko 007 with dis
        
        ko "「Aaawww... 」"
        fn "「What were you taking a picture of? 」"
        
        show ko 005 with dis
        
        ko "「A grasshopper. It was just a normal one,{p}\ \ so it should be okay... 」"
        "Kounosuke looks bitterly at my direction."
        fn "「S-sorry. But why a grasshopper? 」"
    
        show ko 001 with dis
        
        ko "「It's because of my ambition. 」"
        fn "「Your ambition? 」"
    
        show ko 003 with dis
        
        ko "「Yep. A sweet home for just us two lovers. 」"
        fn "「H-huh... What does a grasshopper,{p}\ \ have to do with that? 」"
        
        show ko 001 with dis
        
        ko "「Around here in the country,{p}\ \ there might be a rare creature,{p}\ \ a new species yet to be discovered. 」"
        ko "「If I send in a picture of it,{p}\ \ I think I could get some kind of cash reward. 」"
        "So that's what he's up to this time...{p}Well, I don't expect it to turn out well,{p}but this is Kounosuke after all."
    
        show ko 003 with dis
        
        ko "「Oh, did you need me for something? 」"
        fn "「Not particularly, I just wanted to see you. 」"
        
        show ko 001 with dis
        
        ko "「Hmm. 」"
        "......"
    
        show ko 002 with dis
        
        ko "「Let's take a little walk in the village! 」"
    
        jump kounosuke30_meteor
        
    ##################################################
    label kounosuke30_badend:

        $ event_name = "Kounosuke"
    
        show ko 001 at center with dis
        
        ko "「Welco... 」"
    
        show ko 002 with dis
        
        ko "「Oh, come on in [fn]. 」"
        "I enter, and Kounosuke is the one watching the store."
        fn "「Hey. I've come to visit. 」"
    
        show ko 001 with dis
        
        ko "「Sorry, I'm watching the store.{p}\ \ Wait a second... 」"
    
        hide ko with wipe_right
        
        ko "「Yukiharu, can you take over for bit? 」"
        yk "「Eh, again? 」"
        ko "「Please, [fn]'s here. 」"
        yk "「You're always doing this... 」"
        ko "「I'll buy you a present as an apology! 」"
        yk "「It'll just be candy. 」"
        ko "「Oh... th-that's not good enough? 」"
        yk "「I might do it if you get me two ice creams. 」"
        ko "「Okay. I'll buy them on my way back. 」"
        yk "「See you later! 」"
    
        show ko 001 with dis
        
        ko "「Sorry to keep you waiting.{p}\ \ Well then, let's go! 」"
    
    
    #######################################################
    label kounosuke30_meteor:
        
        stop music fadeout 3
        scene black with sdis
        scene path with sdis
        show ko 001 at center with dis
        play music melodious01
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        
        ko "「Your Summer vacation is already over. 」"
        fn "「Yeah. 」"
        
        show ko 007 with dis
        
        ko "「And you're going to be going back home tomorrow? 」"
        fn "「Yeah... 」"
        
        show ko 005 with dis
        
        ko "「Man, time sure does fly. 」"
        
        hide ko with wipe_down_slow
        play sound bosu34
    
        "Kounosuke looks up at the sky as he says that."
        fn "「You're right. 」"
        "I look up at the blue sky too."
    
        scene sky with sdis
        
        "That clear sky stretches everywhere I look.{p}This vast, endless blue expanse,{p}can't be seen in the city as well."
        "When I was young, and even now,{p}everybody I ran around with,{p}I'll be saying good-bye to them and Kounosuke."
        "When I think about that,{p}I feel a sudden sadness rise up within me."
        ko "「Oh, that's right. 」"
    
        scene path
        show ko 001 at center 
        with dis
        
        ko "「[fn], I'll take you,{p}\ \ to a really special spot this evening. 」"
        fn "「Tonight? 」"
        
        show ko 002 with dis
        
        ko "「Yeah. If I remember correctly,{p}\ \ there's a meteor shower today."
        ko "I know of a good spot.{p}Since you're special, I'll show it to you! 」"
        fn "「Really? 」"
        
        show ko 001 with dis
        
        ko "「Would, say, eight o' clock be a good time?{p}\ \ To meet up, that is... 」"
        fn "「Sure, I'm looking forward to it! 」"
    
        stop music fadeout 3
        scene black with sdis
        play sound night_insects
        $ renpy.music.set_volume(0.6, 0.0, channel = "music")
        
        "Night.{p}As I thought, Kounosuke didn't come,{p}until 8:30 to get me."
        "The flashlight I got from home is broken,{p}so Kounosuke is the only one with light."
        "There are almost no street lights,{p}or passing cars in the country at night.{p}It's dark, quiet, and eerie."
        "The crying in insects in the darkness,{p}and the lush, thick forest,{p}makes the whole place... "
        "Seem like a giant living entity itself.{p}It seems to be breathing with life."
        
        scene forest01 night with sdis
        
        fn "「We're going into the forest? 」"
    
        show ko 001 night at center with dis
        
        ko "「Yep. It'd be horrible if we got separated,{p}\ \ so give me your hand 」"
        "I don't think many people go through here,{p}so we're pushing our way down an animal trail."
        "We advance with just the thin beam,{p}of Kounosuke's flashlight."
        "I tightly grasp his hand,{p}to keep myself from getting lost."
        "Then, I see a clearing in the forest up ahead.{p}When we get to it,{p}my field of vision suddenly opens."
    
        play music melodious03
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        scene starry_sky with sdis
        call set_star_stats from _call_set_star_stats 
        show shooting_star
        
        "There's stardust as far as the eye can see."
        "In the star-filled sky,{p}they become falling grains of light,{p}as if it's all spilling over."
        "What can I say, It's amazing.{p}Amazing is the only word,{p}for this indescribable view."
        
        hide shooting_star
        scene forest01 night
        show ko 001 night at center
        with wipe_right
        
        ko "「So....? 」"
        fn "「It's amazing... 」"
        ko "「It is, isn't it? 」"
        fn "「Wait. Where are your glasses? 」"
    
        show ko 003 night with dis
        
        ko "「It looks even more beautiful without lenses.{p}\ \ Although it is a little blurry... 」"
        fn "「Hmm...{p}\ \ Ah, I see. 」"
    
        scene starry_sky with sdis
        call set_star_stats from _call_set_star_stats_1 
        show shooting_star
        
        "For a slight moment,{p}both of us gaze at the falling stars."
        "I can even almost hear a twinkling noise,{p}of the stars falling without any regrets."
        ko "「[fn]. 」"
        fn "「Hm?{w=.5} Mm... 」"
    
        hide shooting_star
        scene ev_kounosuke_2 
        with dis
        pause 1.5
        
        "In the moment he calls my name,{p}and I try to turn around..."
        "My body is wrapped in warm fur,{p}and my mouth is closed up."
        "It was after he let go of me,{p}that I realized we kissed."
        ko "「Again, we might not be able...{p}\ \ to see each other anymore. 」"
        fn "「Yeah, you're right... 」"
        "My mouth is closed up again.{p}This time I'm given plenty of time to accept it."
        
        if kouno_badend == True:
            jump kounosuke30_confession
        else:
            jump kounosuke30_promise
            
    ##################################################
    label kounosuke30_promise:

        $ event_name = "Recalled Promise"

        play music night_insects fadein 2.5
        
        ko "「[fn]. 」"
        fn "「Hm? 」"
        ko "「Let's try having sex out here. 」"
        fn "「Huh? 」"
        ko "「Have you already forgotten your promise?{p}\ \ I get to be the top this time! 」"
        fn "「H-here? 」"
        ko "「It's alright, nobody comes here... 」"
        fn "「…… 」"
        "At Kounosuke's proposal,{p}my body goes against my head,{p}and begins to throb violently."
        "I'm embarrassed and afraid to do it,{p}where there isn't a roof,{p}but it's also for that reason that I'm excited."
        fn "「Okay. 」"
        "When I tried to say that..."
    
        jump kounosuke30_gathering
        
    #####################################################
    label kounosuke30_confession:
        
        $ event_name = "Confession"
            
        ko "「[fn], I love you.{p}\ \ I've always felt this way... and...{p}\ \ ...am I making you uncomfortable? 」"
        "Kounosuke's grip on my hand gets stronger.{p}It's like he'll never let go again.{p}Or like the clinging of a child. It's powerful."
        fn "「N-no, you're not.{p}\ \ I also... 」"
    
        play music night_insects fadein 2.5
    
    ####################################################
    label kounosuke30_gathering:
        
        $ persistent.event_kounosuke2 = True
        
        scene starry_sky with qdis
        play sound si_gasa03
        pause 1.5
        scene forest01 night with qdis
    
        "At the sudden noise,{p}we both jump away from each other."
        
        scene white with qdis
        scene forest01 night
        show ka 001 night at center
        with qdis
    
        ka "「Huh? [fn]? 」"
    
        show si 001 night at farright with dis
        
        si "「What are you doing here at a time like this? 」"
    
        show ko 006 night at farleft behind ka with dis
        
        ko "「Wh-why are you two here? 」"
    
        show si 004 night with dis
        
        si "「Because the stars around here are beautiful. 」"
    
        show ka 003 night with dis
        
        ka "「Amaki-san asked me to keep an eye on Shin. 」"
    
        show si 003 night with dis
        
        si "「I said I would be fine on my own,{p}\ \ but Amaki would not allow it... 」"
    
        show ka 002 night with dis
        
        ka "「He won't.{p}\ \ Isn't that because he cares for you so much? 」"
    
        show si 001 night with dis
        
        si "「I know, but is he going to treat me,{p}\ \ like a child forever?"
        si "Anyways, because you got here before me,{p}I won't be able to quietly watch the stars. 」"
    
        play sound si_gasa03
        scene forest01 night with wipe_right
        show ky 001 night at center with wipeleft
        
        ky "「Look over here... Hm? 」"
        
        show so 003 night at midright with dis
        
        so "「Wow, it's amazing!{nw}"
        show so 001 night with dis
        extend " Wait, huh? 」"
    
        show ky 002 night with dis
        
        ky "「It looks like they got here before us. 」"
        fn "「H-hello... 」"
    
        show ka 001 night at farleft behind ky with wipe_right
        
        ka "「Are you both stargazing too? 」"
    
        show ky 001 night with dis
        
        ky "「Well, yes. 」"
    
        show so 005 night with dis
        
        so "「(It's really supposed to be a date night,{p}\ \ for just senpai and me...) 」"
    
        show ka 005 night with dis
        
        ka "「Hm? What was that? 」"
    
        show so 006 night at jump_up
        pause .2
        
        so "「N-nothin'! 」"
        "Somehow, it has become noisy."
    
        play sound si_gasa03
        scene forest01 night
        show ju 006 night at midright
        show ta 002 night at midleft
        with wipe_right
    
        ju "「Tatsu-san, I'm not old enough to drink! 」"
        ta "「You'll be fine.{p}\ \ I've been drinking since I was a kid! 」"
    
        show ju 003 night with dis
        
        ju "「That's not the problem... 」"
    
        scene forest01 night with wipe_right
        show su 004 night at center with wipeleft
        
        su "「I want to try some! 」"
    
        show to 007 night at midright behind su with wipe_right
        
        to "「Stop, stop. It doesn't even taste that good. 」"
        
        scene forest01 night
        show ko 005 night at center
        with sdis
        
        fn "「...Those voices. 」"
        ko "「...... 」"
        
        scene forest01 night
        show to 001 night at center
        show su 001 night at farleft
        show ta 001 night at farright
        with wipe_right
    
        su "「Really? 」"
    
        show to 003 night with dis
        
        to "「Yeah, the reason you drink,{p}\ \ is because it feels good when you're drunk! 」"
    
        show ta at briefzoom
        
        ta "「That's not wrong, is it?{p}\ \ in the world that doesn't taste good.{p}\ \ Gahahahahaha! 」"
    
        show su 004 night with dis
        
        su "「Huh? So which is it after all? 」"
        fn "「G-good evening... 」"
        
        scene forest01 night with wipe_right
        show ju 001 night at center with wipeleft
        
        ju "「It seems they got here before us. 」"
    
        show su 002 night at midright with dis
        
        su "「Oh, it's [fn]-san. Good evening! 」"
    
        show to 001 night at farleft behind ju with dis
        
        to "「What are you guys doing in a place like this? 」"    
        fn "「Um, well... Shouldn't I...{p}\ \ be asking what you are doing? 」"
    
        show to 002 night with dis
        
        to "「Tatsu-nii wanted to throw one last party,{p}\ \ but we could only contact four people."
        to "I couldn't even get in contact with you,{p}and you're the most important part! 」"
    
        show to 001 night with dis
        
        to "「There wasn't anything we could do,{p}\ \ so it's just the four of us.{p}\ \ Tatsu-nii's taking us to a special spot. 」"
        
        hide su with wipe_right
        show ta 002 night at farright with wipe_right
    
        ta "「Now everybody's here... 」"
        "......"
    
        scene forest01 night with wipe_right
        show ko 005 night at center with wipeleft
        
        "I look over at Kounosuke.{p}I can't describe the look on his face."
        ko "「I've been waiting so long for this moment... 」"
    
        hide ko with wipe_right
        show ta 001 night at center with wipeleft
        
        ta "「Everybody has unexpectedly gathered.{p}\ \ Looks like tonight's a party.{p}\ \ {nw}"
        show ta 002 night at jump_up
        extend "{w=.2}Look, here's some alcohol too! 」"
    
        show ju 003 night at farleft behind ta with wipe_right
        
        ju "「I'm telling you, this is underage drinking... 」"
        
        scene forest01 night
        show si 004 night at midleft with wipeleft
        show ka 001 night at midright with wipeleft
        
        si "「It really has become quite noisy... 」"
        ka "「Well, this is alright, isn't it? 」"
    
        scene forest01 night with dis
        show ky 001 night at midright
        show so 005 night at midleft
        with wipe_right
        
        so "「It was supposed to be just me n' senpai... 」"
        ky "「Now, now. How about we save it for another day? 」"
    
        show so 003 night with dis
        
        so "「O-okay! 」"
    
        scene forest01 night with wipe_right
        show to 001 night at midright
        show su 001 night at midleft
        with wipeleft
        
        to "「Shun, give everybody a paper cup. 」"
        su "「Alright. 」"
    
        scene forest01 night
        show ko 005 night at midleft
        show su 002 night at midright
        with wipeleft
        
        su "「Here, Kounosuke-san. 」"
        ko "「Th-thanks. 」"
        su "「You too, [fn]-san. 」"
        fn "「Thank you, Shun-kun... 」"
    
        scene forest01 night with wipe_right
        show ju 001 night at midleft
        show ta 001 night at midright
        with wipeleft
        
        ju "「Pour everyone the juice they'd like.{p}\ \ {nw}"
        show ju 006 night at jump_up
        extend "...Tatsu-san! What are you trying to mix in!? 」"
    
        show ta 008 night with dis
        
        ta "「Tch. You got me... 」"
    
        show ju 003 night with dis
        
        ju "「You weren't caught. Please stop trying\n\ \ to get everybody to drink,{p}\ \ when they're all underaged! 」"
    
        scene forest01 night with wipe_right
        show ko 005 night at center with dis
        
        fn "「Somehow... it has gotten really noisy. 」"
        ko "「Yeah... 」"
        fn "「That's surprising, wasn't this...{p}\ \ place supposed to be unknown? 」"
        ko "「It was my little secret... 」"
        "I force a smile while a depressed Kounosuke,{p}sits down next to me."
        "Why is it that when I'm with Kounouske,{p}things like this usually happen?{p}Whenever we do something, it falls apart."
        fn "「Well, I guess there's nothing...{p}\ \ we can do about it, right? 」"
        
        show ko 007 night with dis
        
        ko "「Yeah... 」"
        "I slap Kounosuke's back for encouragement,{p}and call over Shun, who has become our waiter."
        fn "「Shun-kuuun, I'll take some orange juice,{p}\ \ over here please! 」"
        su "「Oh, okay. 」"
        fn "「Well, let's just enjoy tonight.{p}\ \ It may not be just the two of us,{p}\ \ but having fun like this is good too, isn't it? 」"
    
        show ko 001 night with dis
        
        ko "「Yeah. You're right... 」"
    
        stop music fadeout 2
        scene black with sdis
        window hide
        play music birds_chirping
        
        $ day = 31
        $ the_date = "August 31"
        
        scene sky01 
        show text "{size=+130}August 31" at truecenter 
        with Dissolve(.5)            
        pause 3
        scene black with Dissolve(1)
        pause .4
        scene hbroom with wipe_corner
        
        "My Summer vacation has come to an end at last.{p}I lightly sigh when I see the calendar,{p}and once again check my luggage."
        "Have I left anything behind... No."
        gm "「You haven't forgotten anything? 」"
        fn "「Nope. Everything's fine. 」"
        gp "「It's going to be quiet around here again. 」"
        gm "「You're welcome back any time. 」"
        fn "「Yeah. I'll come back and visit some time. 」"
        gp "「We'll be looking forward to it! 」"
        
        play sound ChimeA
        pause 1
        
        gm "「Oh my? A guest at this time in the morning? 」"
        fn "「Oh, that's okay. I'll get it,{p}\ \ I'm just about to leave anyways 」"
    
        scene hentry with wipeleft
        
        fn "「Coming, who is it? 」"
    
        show ko 001 at center with dis
        
        ko "「Good morning! 」"
        fn "「Good morning. This is rare for you,{p}\ \ coming out this early in the morning. 」"
    
        show ko 005 with dis
        
        ko "「Well, I didn't want to be late today.{p}\ \ If I was, you might have been gone already. 」"
        fn "「If only you always had this enthusiasm... 」"
    
        show ko 001 with dis
        
        ko "「You're mean. Even if this is the last time. 」"
        fn "「Ahaha, sorry, sorry! 」"
        "Kounosuke and I go to the bus stop together."
    
        scene path with sdis
        play music daily03
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        
        "Along the way, while talking about small things,{p}different memories came to mind.{p}Old things, new things, everybody, and Kounosuke..."
        "I'm too old to cry, but even now...{p}thinking about sad thoughts tempted me.{p}I tried my best to hold them back."
        "I guess I was looking for a suitable topic,{p}to hide my feelings."
        
        scene bstop with wipeleft
        show to 001 at midleft
        show ju 001 at midright
        with wipe_right
    
        to "「Hey! 」"
        ju "「You're here. 」"
        "When we got to the bus stop,{p}everybody was waiting there."
        fn "「So everyone came... 」"
    
        show to 002 with dis
        
        to "「Well, duh! 」"
        ju "「Saying farewell to a friend like you is important.{p}\ \ It's only appropriate that we have a good one. 」"
        fn "「Th-thanks... 」"
    
        show to 010 with dis
        
        to "「Have a safe trip, man. 」"
        ju "「Take care of yourself. 」"
    
        scene bstop with wipe_right
        show ta 002 at midleft
        show su 001 at midright
        with wipe_right
           
        ta "「Come back again! 」"
        su "「I'll be waiting! 」"
    
        scene bstop with wipe_right
        show ky 001 at midleft
        show so 001 at midright
        with wipe_right
        
        ky "「Take care, and work hard. 」"
        so "「Our time was short, but it was nice meetin' ya! 」"
    
        scene bstop with wipe_right
        show ka 003 at midleft
        show si 001 at midright
        with wipe_right
        
        ka "「Take care. Don't kill yourself out there. 」"
        
        show si 010 with dis
        
        si "「...... 」"
    
        show ka 001 with dis
        
        ka "「Hey, you say something too, Shin. 」"
    
        show si 011 with dis
        
        si "「B-be quiet. I don't need...{p}\ \ {nw}"
        show si 003 with dis
        extend "to tell you anything, but...{p}\ \ {nw}"
        show si 001 with dis
        extend "Umm, be safe...... [fn]. 」"
        fn "「Yeah. You guys take care of yourselves too. 」"
    
        scene bstop with wipe_right
        show to 007 at farleft
        show ju 001 at center
        show su 004 at farright
        with wipe_right
        
        to "「Haah, he's going to be late even on today? 」"
        ju "「He really is beyond helping... 」"
        su "「He's terrible... 」"
        fn "「Who? 」"
    
        show to 006 with dis
        
        to "「Kounosuke, of course! Jeez... 」"
        fn "「Huh? Kounosuke was with me... 」"
    
        scene bstop with wipe_right
        
        "I look next to me as I say that,{p}but nobody's there. Wh-what?"
    
        show ju 003 at center with dis
        
        ju "「What are you talking about? 」"
    
        show su 004 at midright with dis
        
        su "「Weren't you alone the whole time? 」"
        "Huh? No, that can't be.{p}This is weird..."
        ko "「Heeey, [fn]! 」"
        
        scene bstop
        show ko 005 at offright_far
        with wipe_right
        play sound step03
        show ko 005 at move_center(0.5)
        
        ko "「Y-you're terrible.{p}\ \ I went out of my way to go pick you up earlier! 」"
        fn "「Huh? 」"
        "Kounosuke comes sprinting as fast as he can,{p}breathing heavily... I guess I just...{p}left him behind while absorbed in conversation?"
        ko "「You just went to the bathroom for a bit.{p}\ \ You didn't come out and I got impatient. 」"
        fn "「Oh, s-sorry. 」"
    
        show to 005 at farright behind ko with wipeleft
        
        to "「Heh, heh, heh... that's rare.{p}\ \ You weren't late today after all. 」"
    
        show ko 001 with dis
        
        ko "「Well, I couldn't be late today! 」"
    
        show to 001 with dis
        
        to "「You're right about that.{p}\ \ Right for once, at least... 」"
    
        show ju 003 at farleft behind ko with wipe_right
        
        ju "「You should always be this enthusiastic. 」"
    
        show ko 004 with dis
        
        ko "「Huh? That's overdoing it.{p}\ \ I'd get worn out if I was always like this! 」"
    
        show to 007 with dis
        
        to "「Well, no shit, you would! 」"
        
        show na 101 at center
        show ju 001 at farleft
        show to 002 at farright
        show ko 002 at center
        show ky 001 at midleft
        show si 002 at midright
        show ta 002 at midleft
        show su 002 at midright
        with dis
        
        "「Ahahahaha! 」"
        "In Kounosuke's exchange,{p}everybody laughed, not just me."
        "Really, even if he died,{p}his habit wouldn't get any better."
        
        play sound honking
        pause 2.5
        scene bstop with wipe_right
        
        "Oh, it looks like the bus is here."
    
        play sound auto_door
        
        fn "「Good bye, everybody.{p}\ \ I had a really good time.{p}\ \ I'm definitely coming back again! 」"
    
        show ko 001 at center with dis
        
        ko "「Oh, [fn], wait! 」"
        "As I was giving my parting words to everybody,{p}Kounosuke stops me as I'm getting on the bus."
        
        show ko 007 with dis
        
        ko "「Err, t-take this... 」"
        fn "「Heh? 」"
        "He presents to me a single photograph.{p}A snapshot of everybody when we were camping."
        
        show ko 001 with dis
        
        ko "「So you'll never forget about us,{p}\ \ and this village... 」"
        fn "「I won't forget.\n\ \ Thank you, Kounosuke. 」"
    
        show ko 002 with dis
        
        ko "「Hehehe. See you later. Come back again! 」"
        fn "「I will! 」"
        
        play sound auto_door
        hide window with dis
        stop music fadeout 5
        pause 2
        
        if kouno_badend == True:
            jump kounosuke_ending #!#May need to change to just endings
    
        if ghost_encounter == 3:
            jump kounosuke30_farewell_nana
        
    
    #######################################################
    label kounosuke30_farewell_nana:
    
        $ event_name = "Bye Bye"
    
        play music cicada01 fadein 5
        $ renpy.music.set_volume(0.5, 0.0, channel = "music")
        scene black with sdis
        scene path with sdis
        show na 101 at center with dis
        
        na "「Farewell, [fn]. 」"
    
        show na 102 with dis
        
        na "「Still, Kounosuke can be quite troublesome. 」"
    
        show na 101 with dis
        
        na "「You won't be a child forever,{p}\ \ so can't you straighten up a little? 」"
        
        stop music fadeout 3
        hide na with sdis
        scene black with sdis
        pause 2
        
        jump endings

#######################################################
label tatsuki30:
    
    $ event_name = "Every Day is my Favorite Day"

    play music cicada01 fadein 1.5
    $ renpy.music.set_volume(0.4, 0.0, channel = "music")
    scene tatsukihouse_inside with wipe_corner
    
    fn "「Thank you for the work. 」"

    show tp 401 at center with dis
    
    tp "「Good work. 」"

    show tp 409 with dis
    
    tp "「But is this really okay?\n\ \ You go back tomorrow, don't you?{p}\ \ And here you are, working on your last day... 」"
    fn "「Working here has become one of my best memories.{p}\ \ It's been a lot of fun. 」"
    
    show tp 406 with dis
    
    tp "「I see... 」"
    "Tappei-san's face relaxed, and looked a bit happy."

    show tp at jump_up
    pause .2
    
    tp "「Here, today's pay.{w} Take it. 」"
    fn "「Eeh!?{w} 　Is it really okay for me to accept this? 」"
    "The envolope he was giving me\nwas heavier than usual, and inside there\nwas at least twice the usual amount of money."
    
    show tp 402 with dis
    
    tp "「It'll be a special travel allowance,\n\ \ for your last day.{p}\ \ You better thank me. 」"
    fn "「Thank you very much! 」"
    fn "「I haven't been at this job very long,\n\ \ and for me to receive this much...{p}\ \ I'll use it very carefully. 」"
    
    play music piano2_015 fadein 5
    $ renpy.music.set_volume(0.8, 0.0, channel = "music")
    show tp 406 with dis
    
    tp "「It's fine, don't mind it.{p}\ \ That should be enough to cover\n\ \ the travel costs of coming to work. 」"
    fn "「Huh? 」"
    
    show tp 401 with dis
    
    tp "「Of course you'll be coming\n\ \ back on your next vacation. 」"
    tp "「It's not like you can't afford the fare,\n\ \ and since you'll be working at home,\n\ \ it won't matter if you're broke. 」"
    fn "「Eeh,{w=.2} no way!? 」"
    
    show tp 403 
    
    tp "「What, don't like it? 」"
    fn "「No, it's not that... 」"
    
    show tp 402 with dis
    
    tp "「If you use that money\n\ \ I gave you for anything else, I'll crush you.\n\ \ Be ready for that. 」"
    fn "「Yes sir... 」"
    
    show cu 008 at midright with wipeleft
    
    cu "「Not having Aniki around'll make things lonely.{p}\ \ Let's work together again. 」"
    
    show te 001 at farleft behind tp with wipeleft
    
    te "「Everyone here cares about you very much.{p}\ \ We will be awaiting your return. 」"
    
    show ni 002 at midleft with wipeleft
    
    ni "「Good grief, wouldn't that make his next visit less\n\ \ of a homecoming and more a manual labour contract\n\ \ with the Midoriya Group? 」"
    
    show ta 002 at farright behind tp with wipeleft
    
    ta "「Isn't that okay?{p}\ \ Come back, we'll be waiting for you. 」"
    "Minasato isn't the home of my parents anymore,\njust the home of my grandparents."
    "Looks like the number of places\nI can come back to has gone up."
    
    $ renpy.music.set_volume(0.5, 1.0, channel = "music")
    scene tatsukihouse_inside
    show ta 007 at center 
    with wipe_right
    
    ta "「*mumble mumble*...{w} {size=-10} A-{w=.2}and,\n\ \ if you're working from home,{p}\ \ we could have sex every day. 」{nw}"
    $ renpy.music.set_volume(0.7, 0.0, channel = "music")
    extend ""
    "Tatsu-nii blushed furiously,\nas he whispered so that only I could hear."
    fn "「Hmm, even if we did that,\n\ \ I can't do it both morning and night,\n\ \ so you'd have to pick one. 」"

    show cu 002 big at midleft_big with dis 
    
    cu "「What're you two talkin' about by yourselves?{p}\ \ Let me in on it, too? 」"

    show ta 003 at jump_up
    pause .2
    
    ta "「N-{w=.2}nothing, we weren't talking\n\ \ about anything indecent. 」"
    "Tatsu-nii turned away in embarrassment."
    "As he turned, he swung his tail around,\nscoring a direct hit on Chuukichi-kun."
    
    play sound hit_p00
    show tatsukihouse_inside at hshake
    show cu at move_offleft_far(0.25)
    $ chuu_beat += 1
    
    cu " {size=+15}「Bwaaah!! 」"
    "Chuukichi-kun was blown away,\noff into the horizon,\nuntil he disappeared with a twinkle..."

    play music cicada01 fadein 8
    scene sky with sdis
    
    "The sky was a gentle ephemeral blue."
    
    $ renpy.music.set_volume(0.4, 1.0, channel = "music")
    
    "The loud buzzing of cicadas\ndied down before I knew it."
    "The red dragonflies that swarmed over the village\nduring the change in season were nowhere to be seen."
    "Summer...{w} is already over."
    
    scene sky with sdis
    
    yukino "「Everyone,{w} if you're all done,\n\ \ come inside and get something to eat. 」"
    fn "「Okaaay. 」"
    
    play music daily02 fadein 5
    $ renpy.music.set_volume(0.7, 0.0, channel = "music")
    scene tatsukihouse_inside with wipe_right
    show ni 001 at center with dis
    
    ni "「Doesn't dinner feel earlier than usual? 」"
    yukino "「Isn't today the day of the meteor showers?{p}\ \ I thought everyone would go, so I'd have you\n\ \ all eat something before going. 」"

    show te 001 at farright with dis
    
    te "「So today was the day of the meteor showers.{p}\ \ I completely forgot. 」"

    show tp 402 at farleft behind ni with dis
    
    tp "「In that case, it should be okay to knock back a\n\ \ drink or two while stargazing. 」"
    yukino "「Oh dear.{w} Did everyone forget? 」"
    
    show ni 005 with dis
    
    ni "「It's probable. 」"
    
    scene tatsukihouse_inside
    show ta 002 at center 
    with wipeleft
    
    ta "「Oh yeah, was that today?{p}\ \ [fn], want to go with everyone later on? 」"
    fn "「Oh, okay... 」"
    
    show ta 001 with dis
    
    ta "「Something up? 」"
    fn "「I was thinking it'd be nice\n\ \ if it were just the two of us. 」"
    
    show ta 007 with dis
    
    ta "「Oh... Well, there's no helping it, then.{p}\ \ It'll be just the two of us,\n\ \ having a special time together. 」"
    "I get the feeling he only wanted to make it sound\nlike it couldn't be helped,\nsince his tail was thumping happily on the ground."

    show cu 004 at farright with wipe_right
    
    cu "「Ah, Aniki's havin' secret talks again!\n\ \ Lemme in on the talks too, please! 」"
    yukino "「Chuu-chan, welcome back.{w} That was fast.{p}\ \ The chilled noodles are ready, so it's dinner now. 」"
    
    show cu 006 with dis
    
    cu "「F'real!?{w} 　I love chilled noodles!! 」"
    
    show ta 009 with dis
    
    ta "「Hey, wait a minute. Why is it chilled noodles?{p}\ \ Shouldn't we be having a huge feast,\n\ \ since [fn]'s leaving? 」"
    yukino "「They were a gift,\n\ \ and I didn't want to eat inside the hot house. 」"

    show ta at jump_up
    pause .2
    
    ta "「Don't put out soggy food on a day like this.\n\ \ We should be having sekihan, at least. 」"

    show ni 002 at farleft with wipeleft
    
    ni "「You want celebratory red rice for a parting meal? 」"
    yukino "「You don't have to eat, if you don't like it. 」"

    show ta at jump_up
    pause .2
    
    ta "「Totally, something like that should be here.{p}\ \ Why aren't we having something huge? 」"
    
    show ni 005 with dis
    
    ni "「Sekihan doesn't constitute a feast by itself. 」"
    
    play sound bosu27
    scene tatsukihouse_inside
    show tp 403 at center
    with explosion
    show tatsukihouse_inside at vshake
    
    tp "「You whelp!! What are you saying to your Ma?{p}\ \ {nw}"
    show tp 409 with dis
    extend "Chilled noodles... {nw}"
    show tp 403 at jump_up
    pause .2
    extend "Why haven't you made a feast yourself!? 」"

    show tp at jump_up
    
    tp "「In the old days, having sekihan was like a dream.{p}\ \ You don't need to eat something like that today.{p}\ \ Don't you place any value on rice??? 」"

    show te 003 at midright with wipeleft
    
    te "「Chief.{w} Who's side are you on?{p}\ \ I cannot tell who you are angry at any more. 」"
    
    play sound bosu35
    show te behind tp
    show tp at jump_up
    pause .2
    
    tp "{size=+15}「SOMEONE LIKE YOU SHOULD GET\n\ \ OUT!! 」"
    "I don't mind at all...{p}If I'm eating with everyone,\nthen anything tastes great."

    stop music fadeout .5
    scene tatsukihouse_inside with dis
    
    "Hm? What's that?"
    
    play sound fuurin
    play sound cicada01 fadein 4
    $ renpy.music.set_volume(0.4, 0.0, channel = "music")
    show cu 002 at center with sdis
    
    cu "「Chilled noodles are so good.{w} The best! 」"
    
    show cu 001 with dis
    
    cu "「Whatcha guys doin'?\n\ \ I'm gonna eat everyone's,\n\ \ if you guys don't come soon. 」"
    "On the other side of the verandah,\nChuukichi-san and Yukino-san had already started."
    
    play music free44 fadein 2.5
    $ renpy.music.set_volume(0.9, 0.0, channel = "music")
    play sound bom35
    show tatsukihouse_inside at vshake
    show tp 403 at midright behind cu with wipe_right
    
    tp "「Little braaat!!{p}\ \ Who said you could eat before me?\n\ \ Shyaaaaaahhh!! 」{w} {nw}"
    scene white with qdis
    play sound hit_p07
    #Shake the textbox horizontally
    extend "{w=.3}{nw}"
    play sound hit_p09
    #Shake the textbox horizontally
    extend "{w=.5}{nw}"
    play sound hit81_echo
    #Shake the textbox horizontally
    show cu 009 big at center_big with explosion 
    
    $ chuu_beat += 1
   
    cu "{size=+15}「Bububwaaa! 」{w} {nw}"   
    hide cu with wipe_down
    extend "{w=.3}{nw}"
    play sound bosu31
    
    yukino "「How long have you all been out there?{p}\ \ Hurry now, wash your hands and eat. 」"
    fn "「Okaaay. 」"
    
    stop music fadeout 3
    scene white with dis
    scene black with sdis
    play music night_insects
    pause 2.5
    scene starry_sky  with sdis    
    
    #############################################
    label tatsuki30_sex:  
      
        if persistent.replay == True:
            $ first = persistent.name_first
            $ last = persistent.name_last
            $ day = 30
            $ event_name = "Night of the Meteor Shower"
            
            scene starry_sky with sdis 
            
        $ event_name = "Night of the Meteor Shower"
            
        play music melodious09
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        
        fn "「Whoa, the stars are so bright.{p}\ \ You can't see them this well in the city. 」"
        "We went around the back of the school,\nwhere we climbed a hill that gave us\nan excellent view of the whole village."
        
        scene hill night
        show ta 001 night at center
        with dis
        
        ta "「We came this far, and there's no one here.{p}\ \ This place is so pretty, it's almost a bit sad. 」"
        fn "「It's so dark, I can't see much.\n\ \ There might be other people around. 」"
        
        show ta 008 night with dis
        
        ta "「It'd be nice if someone else were here. 」"
        fn "「That aside, look.{p}\ \ The stars are shining so brightly,\n\ \ like they might fall. 」"
        fn "「Which one would I take back with me? 」"
        
        show ta 002 night with dis
        
        ta "「Gahaha! You wanna bring one home?{p}\ \ It'd be a problem if they did start falling. 」"
        fn "「Hm, that sucks.{p}\ \ It looks like the meteor shower hasn't started yet.{p}\ \ The peak is supposed to be at about 11 PM. 」"
        
        show ta 001 night with dis
        
        ta "「That's true.{p}\ \ Still, I've seen a few already. 」"
        fn "「Eh,{w=.2} really? 」"
        ta "「Yeah, a few.{p}\ \ Still, it'll be better when the peak comes.\n\ \ Let's just wait until then. 」"
        fn "「Yeah, okay. 」"
    
        scene starry_sky with sdis
        
        "Tatsu-nii and I lay down on the grass,\ngazing up at the night sky."
        "All we could see was the depths of the night,\nalong with the stars, more radiant than ever,\nas if a box of jewellery had been knocked over."
        ta "「It's amazingly beautiful. 」"
        fn "「Yeah. 」"
        "..."
        ta "「You have to go back tomorrow... 」"
        fn "「Yeah. 」"
        fn "「But I got given the money for travel expenses,\n\ \ so I have to come back. 」"
        ta "「... 」"
        ta "「It's not about the money, [fn].{p}\ \ What about your feelings?{p}\ \ Do you want to come back? 」"
        ta "「If it's always the same job, won't you hate it?{p}\ \ How about I give the travel money back to Pa? 」"
        "..."
        "It might be because it's night,\nor maybe because we're in the mountain's shadow,\nbut the breeze is a little cold,"
        "and the grass is starting to cool off."
        
        scene hill night
        show ta 001 night at center
        with dis
        
        fn "「Hey, Tatsu-nii, your dream is to\n\ \ become Japan's best craftsman, right? 」"
        
        show ta 002 night with dis
        
        ta "「Yeah, it is. 」"
        fn "「There's nothing I want to be,\n\ \ so I don't know much about the near future.{p}\ \ That's why I haven't thought about it before. 」"
        
        show ta 008 night with dis
        
        ta "「... 」"
        
        scene tatsuki_house_front gray
        show tp 403 gray at center
        show ni 002 gray at farleft
        show te 001 gray at midright
        show cu 009 big gray at farright_big
        show over red light
        with dis
        
        fn "「But you, and everyone else in the Midoriya Group,\n\ \ are different.{p}\ \ Every day you all live life to the fullest. 」"
        fn "「It has nothing to do with reason,\n\ \ and it's not about showing off your talent,\n\ \ it's about committing yourself fully to work. 」"
        fn "「Normal time doesn't apply.\n\ \ A different time flows in that workplace... 」"
    
        hide window
        pause 1.5
        
        fn "「Some answer I've been giving you, huh. 」"
    
        scene starry_sky with dis 
        
        fn "「I want to try living in a house you made.{p}\ \ It'll be my dream to live with you, Tatsu-nii. 」"
        fn "「If I'm with people who need me,\n\ \ I think I can be certain about my answer. 」"
        
        stop music fadeout 2.5
        
        fn "「I want to support the dream\n\ \ of the family that loves me.{p}\ \ That's the kind of person I want to be. 」"
        fn "「That's my dream. 」"
        "I ended it there,\nthen kissed Tatsu-nii."
        "My tongue hit his fangs,\nand slid inside his mouth."
        
        play music night_insects fadein 6
        $ renpy.music.set_volume(0.5, 0.0, channel = "music")
        scene hill night
        show ta 308 big night at center_big
        with dis
        
        ta "「Ng... 」"
        "Tatsu-nii's tongue pushed back at me,\nand soon it was filling up my mouth."
        ta "「[fn]... 」"
        fn "「Tatsu-nii. 」"
        fn "「That was fast, you're already up. 」"
        "Tatsu-nii's pants had tented up,\nand it was pressing into my body."
    
        show ta 301 big night with dis
        
        ta "「What do you expect? We're in a romantic spot,\n\ \ and then you kiss me all of a sudden... 」"
        fn "「You perv. 」"
        
        show ta 302 big night with dis
        
        ta "「Hehehe... I'm romantic.{p}\ \ Let's do it here, [fn]! 」"
        fn "「Eeeh, here? 」"
    
        show ta at jump_up_big
        pause .2
        
        ta "「Gahaha, yeah.{w} It's too dark for anyone to see us.{p}\ \ Come on, take off your clothes. 」"
    
        hide ta with dis
        show ta 101 big night at center_big with dis
        
        "Tatsu-nii took off his work uniform and fundoshi,\nexposing his scaly body to the night air."
        "Beneath the round stomach of that muscular body\nwas a gigantic penis protruding from his sheath."
        fn "「Tatsu-nii, have you been drinking? 」"
        
        show ta 108 big night with dis
        
        ta "「No, I'm sober.{p}\ \ Never mind that, get started already. 」"
        fn "「Y-{w=.2}yeah.{w} Okay. 」"
    
        play sound clink
        
        "I was a bit wary of my surroundings,\nbut I took off my clothes just the same."
        
        show ta 107 big night with dis
        
        ta "「Good, come on then. 」"
        fn "「Yeah... 」"
        "I'm still worried that I might be seen by someone,\nso I'm hiding, out of embarrassment."
    
        show ta 104 big night with explosion
        
        ta "「Hey hey hey, what's wrong.{p}\ \ You aren't full of energy like normal. 」"
        
        show ta 107 big night with dis
        
        ta "「Looks like I have to train your dick to harden\n\ \ when you see my body.{w} C'mon, let's go. 」"
        "Tatsu-nii grabbed my flaccid penis with his hand,\nthen gently began massaging it."
        fn "「Nn- 」"
    
        show ta 110 big night with dis
        
        ta "「Maybe this will help.{w} Or maybe even better? 」"
        
        hide ta with dis
        
        "My dick slid into Tatsu-nii's mouth,\nand was completely engulfed.{p}He handled it in a tender, adorable-looking way."
        fn "「Whoa... amazing. 」"
        "A long tongue coiled around my erection,\nmaking wet slurping sounds\nthat added to the stimulation."
        "The inside of Tatsu-nii's mouth was hot,\nand made me feel like I was melting."
        ta "「Mm,{w=.2} *suck*{w=.2} *slurp* 」"
        "I've never felt this much pleasure before...\nGrabbing on to Tatsu-nii's horn's,\nI began thrusting my hips."
        "Watching my shaft go in and out of Tatsu-nii's\nmouth drove me to further heights of pleasure."
        ta "「Ngg, na... 」"
        "While I was thrusting into his muzzle,\none of his hands reached down to pay attention\nto his unattended cock."
        ta "「Mng,{w=.2} *urk*,{w=.2} mmm,{w=.2} *cough* 」"
        "Despite the occasional choke from my thrusts,\nTatsu-nii didn't let go. He kept suckling me,\ncontinuing his passionate fellatio."
        fn "「Tatsu-nii... You're amazing...{p}\ \ This is... 」"
        ta "「Nnng! 」"
        "Tatsu-nii kept going as his body tensed up,\nreleasing the first climax of the night."
        "Thick white ropes of semen spilled out from his\ncock, making puddles on the ground."
        fn "「You came a lot... 」"
        ta "「Haah, haah,{w=.2} how's that?{p}\ \ It's my first time,\n\ \ but I did all right. 」"
        fn "「And yet, you still came first. 」"
        ta "「You aren't the only one who enjoyed that. 」"
        fn "「It felt good, but you're done already... 」"
        ta "「No helping it, then.\n\ \ I'll make you feel good. 」"
        "As he said that, Tatsu-nii laid down on his back,\ntook a good look at me as he spread his legs open,\nand invited me over for the second round."
        "During his orgasm, Tatsu-nii had managed to\ncover some of his belly and chest with cum.\nHis body glistened under the light of the moon."
        ta "「What is it? Come over here already. 」"
        "Tatsu-nii pulled me into the missionary position."
        "Since I'm lying in a way that faces him head on,\nthe shape of his round stomach\nsticks out to me much more than usual."
        "Urged on by lust, I pushed into Tatsu-nii."
        "No matter how deeply I thrust,\nhe easily took my entire length,\nhis inner walls gripping me tightly."
        ta "「Kuh... I'm so close... 」"
        "I hardly had any time to prepare before he came,\na torrent of seed squirting from his cock."
        "It arced back onto Tatsu-nii's chest,\ncoating his body with sticky white lines."
        fn "「Heh, there you go again.{p}\ \ Did you always have such a hair-trigger, Tatsu-nii? 」"
        ta "「My bad.{w} I was getting sad about thinking how\n\ \ we won't be seeing each other for a while,\n\ \ and forgot to keep control. 」"
        "I'm glad I could give Tatsu-nii pleasure like that,\nbut I'm still aching for release."
        fn "「Tatsu-nii, it's okay if I keep going, right? 」"
        "Tatsu-nii thought about my question for a bit,\nthen answered."
    
        show ta 107 big night at center_big with dis
        
        ta "「I want to try it on top, next... 」"
        fn "「Huh? No way. I mean, look at how big you are. 」"
        "Tatsu-nii's thick shaft still protruded from\nhis sheath.{w} It was about as thick as my wrist,\nand looked as long as my forearm."
        
        show ta 110 big night with dis
        
        ta "「B-{w=.2}but, but.{w} I don't have to go all the way in.{p}\ \ Your first time, you got all the way into me.{p}\ \ It should be okay if I top, once in a while. 」"
        ta "「Let me take your virginity, too! 」"
        fn "「No, absolutely not.{p}\ \ You'll tear me up trying to get it in. 」"
        
        show ta 109 big night with dis
        
        ta "「Don't worry about it, you'll be fine.{p}\ \ You should be able to stretch.{p}\ \ {nw}"
        show ta 107 big night with dis
        extend "If it gets too bad, I'll stop. 」"
        fn "「Geez, I can't get out of it, can I?{p}\ \ Only if you stop if I can't take it. 」"
        "I gave in to the request,\nand tried to get ready to take him."
        "Besides, I've been cumming in him all this time,\nso I can't really say no to him."
        
        show ta 102 big night with dis
        
        ta "「Hehe, {w=.2}that won't happen.{p}\ \ We have to loosen you up a bit first,\n\ \ so move over here. 」"
        
        scene hill night with dis
        scene ev_tatsuki_2 with sdis
        pause 2.5
        
        "I moved myself over to the spot he gestured to."
        ta "「Well, isn't this a nice view. Get ready... 」"
        fn "「Hwaa-! 」"
        "I could feel something warm pressing into my hole."
        "It began by gently caressing the outside,\nthen it slipped inside,\nand began to wriggle deeper inside me."
        ta "「Just bear with it for now,\n\ \ otherwise it'll hurt later. 」"
        "Tatsu-nii's long tongue steadily slipped into me,\nlicking at the sensitive spots inside my ass."
        fn "「Hey, don't lick so much. It feels kinda weird... 」"
        ta "「You've loosened up quite a bit.{p}\ \ That ought to be enough. 」"
        "The long tongue slid out of my body,\nand was then replaced by a finger about as thick\nas the average manhood."
        fn "「Ngaaah...{w=.2} it's... 」"
        ta "「Okay, let's do it. 」"
        ta "「It might be a bit hard since\n\ \ our body sizes are so different,\n\ \ so try sitting on top of me for support. 」"
        fn "「So...{w=.2}　Like this...? 」"
        "I rested my hips on his,\nas though going to hug him."
        "Without missing a beat,\nTatsu-nii held me against him,\npropping me against his body."
        "I moved my hips down, pressing his stiff,\ncurved length into my entrance."
        ta "「[fn], let's do this... 」"
        "I pushed down further,\nand Tatsu-nii's shaft spread my hole firmly open."
        fn "「Aaah-{w} It's too big. It won't fit...{w} Augh! 」"
        "The top of his shaft was inside me,\nand the rest was gently pressing in."
        "My insides felt like they were going to split\nfrom the pressure."
        ta "「Now, we wait.{p}\ \ We can try going deeper in a little bit. 」"
        "Slowly, bit by bit, the burning hot shaft\npushed into me.{w} Slowly, my hole stretched\nto compensate, allowing more inside."
        fn "「O-oww... Ah-! 」"
        "*Grind*"
        "What meager resistance my body offered faded away,\nletting even more of Tatsu-nii's shaft into me."
        ta "「Looks like I'm mostly in.{p}\ \ At this rate, I'll be boning you to the hilt. 」"
        fn "「Gaah, oww... Tatsu-nii, be more gentle. 」"
        fn "「O-{w=.2}ouch... I'm about to tear apart.{p}\ \ Uwaaagh,{w=.2} it can't go any further-! 」"
        "Tatsu-nii stopped moving into me,\nand simply held me to his chest."
        ta "「Hey,{w=.2} take a look.{w} I'm almost all the way in.{p}\ \ My bad, did I hurt you?{p}\ \ There's no blood though, so nothing's damaged. 」"
        "The feeling of the hot shaft buried inside me\nresounded through my body.{p}I could feel evey inch and curve of it."
        ta "「Well, at this rate, we won't get any further.\n\ \ I'm gonna try moving in again. 」"
        fn "「Hey, wai-{w=.2}uhn,{w=.2} hnn! 」"
        "Tatsu-nii pushed further into my\nstretched-to-the-limit hole,\nrubbing against my inner walls."
        ta "「You all right? We can stop, if this is it. 」"
        "Tatsu-nii paused in concern for me,\nbut that large body, and cock to match,\nwas making me shudder in pleasure."
        fn "「Aaah...{w=.2} It still hurts a litte...{p}\ \ But it feels good, so don't stop. 」"
        "I was held against that burly chest,\nand Tatsu-nii's cock began to slide in and out."
        "When his member was pulling out,\nmy stretched hole sucked onto it."
        ta "「Looks like you're getting used to it.\n\ \ Feels really good, doesn't it?\n\ \ You look like you're about to come from this. 」"
        "My cock wasn't getting touched at all,\nyet it was leaking precum all over the place."
        fn "「Hnng,{w=.2} so good... 」"
        ta "「Yep, you're definitely used to it.{p}\ \ Time to step up the pace. 」"
        "He thrust in, hard, and my body was wracked with\nwaves of pleasure."
        fn "「Hyaa!{w} 　I'm gonna burst! 」"
        "The hot, almost boiling rod thrust deep into my\nbody, causing huge waves of pleasure that were\nalmost intolerable."
        ta "「Guh,{w=.2} you're tightening up. 」"
        "The member inside me swelled up,\ncoating my insides with sticky seed,\nand filling me to the brim."
        fn "「I-I'm about to c-{w=.2}cum, too-! 」"
        "..."
        
        scene hill night with dis
        show ta 408 big night at center_big with dis   
        play music night_insects fadein 5
        
        ta "「Whew,{w=.2} that was good. 」"
        fn "「Tatsu-nii... 」"
    
        show ta 410 big night with dis
        
        ta "「It's nice to be the one on top.\n\ \ Now, time to pull out. 」"
        "His now-flaccid penis slid out of me,\nand his cum began leaking out."
        fn "「You came so much inside me... 」"
        "My hole remained open, even after his cock was out,\nand his thick white semen dripped out of it."
        
        show ta 402 big night with dis
        
        ta "「Gahahaha.{w=.2} There's plenty left, if you want some.{p}\ \ {nw}"
        show ta 105 big night with dis
        extend "But this is it for the day. Lame. 」"
        fn "「I'll come back to Minasato,\n\ \ and we can do it again then.{p}\ \ Or do you mean I'm only good for one round? 」"
        
        show ta 107 big night with dis
        
        ta "「No, you moron.{p}\ \ It's awesome just having you here, next to me. 」"
        fn "「I wish I could stay... 」"
        
        show ta 102 big night with dis
        
        ta "「I have no complaints about us being together.{p}\ \ Basically, you're the most important thing to me. 」"
        ta "「I'll make you the happiest guy in Japan.\n\ \ No, the world! 」"
        fn "「I'm looking forward to that.{p}\ \ You better come through with it soon! 」"
        
        show ta 109 big night with dis
        
        ta "「Yeah, you should look forward to it.{p}\ \ I promise I will. 」"
    
        hide ta with dis
        
        fn "「It's a promise. 」"
        "If it's Tatsu-nii, it'll be fine."
        "After all, he kept that\nlittle promise from so long ago."
        "So I'll wait and look forward to that day,"
        "by his side, supporting him as the\nWorld's Happiest Guy,"
        "for our promise, and for our dream."
        
        scene hill night with dis
        scene starry_sky with sdis
        call set_star_stats from _call_set_star_stats_2 
        show shooting_star
        
        ta "「Hey, look.{w} It looks like it's started. 」"
        fn "「Oh, wow.{w} They're so beautiful. 」"
        "The meteors streaked across the night sky."
        "Countless bright stars streamed by,\nlike a shower of sparks."
        
        hide shooting_star
        call set_star_stats from _call_set_star_stats_3 
        show shooting_star
        
        "It doesn't look like I'll be able to take one,\nbut no matter how bright they are,\nthey're nothing to what I have in my hands now."
        fn "「They're so beautiful. 」"
        ta "「Yeah, so pretty... 」"
        "We stayed there, watching the night sky,\nuntil we lost all track of time."
        
        stop music fadeout 5
        hide shooting_star
        scene black 
        with sdis
        
        if persistent.replay == True:
            pause 1
            $ renpy.end_replay()
            
        $ persistent.event_tatsuki2 = True
        
        $ event_name = "The Last Morning"
        
        window hide
        
        $ day = 31
        $ the_date = "August 31"
        
        scene sky01 
        play music birds_chirping
        show text "{size=+130}August 31" at truecenter
        with Dissolve(.5)            
        pause 3
        scene black with Dissolve(1)
        pause .4
        scene hbroom with wipe_corner
        
        "The last morning of Summer vacation had arrived."
        fn "「Hwaaah... is it time to go already? 」"
        "Today's the day I have to leave Minasato,\nand head back into the city."
        fn "「Hmm, here's all my luggage.{p}\ \ I never did change my clothes, did I...?\n\ \ Well, better get onto that. 」"
        gp "「Good morning, [fn]. 」"
        gm "「Morning, [fn]-chan. 」"
        fn "「Morning. 」"
        gm "「Breakfast is ready. 」"
        fn "「Okay, thank you. 」"
        gp "「Hey, go clean up first. 」"
        fn "「Oh, right. 」"
        gm "「Oh, silly.{w} Fufufufu... 」"
        "Will this be the last time I have breakfast with\nGrandpa and Grandma?"
        fn "「Thank you for the food. 」"
        gp "「The bus will be arriving soon, eh? 」"
        gm "「It's sad, knowing you go home today.\n\ \ It'd be great if you stay here some more. 」"
        gp "「It can't be helped, he has school.{p}\ \ Not just school, but high school.{p}\ \ He must have a lot of things to do. 」"
        "Somehow, I've spent half the month at Tatsu-nii's,\nand I'm spending the last bit of it back here.{p}I wonder if I did something bad."
        
        play sound ChimeA
        pause 1
        
        gm "「Just a moment, I'll be right there. 」"
        gp "「Strange for someone to come by this early. 」"
        gm "「[fn]-chan, it's for you. 」"
        fn "「Eh? Me?{w} 　Okay, I'm coming. 」"
        "Huh, I wonder who it is...?"
    
    menu:
        "A. Maybe it's Tatsu-nii":
            jump tatsuki30_tatsuki
        "B. The one I want to see before the end.":
            jump tatsuki30_tappei
        "C. Whut?":
            jump tatsuki30_chuukichi

    ##########################################
    label tatsuki30_tatsuki:
            
        $ event_name = "Tatsuki"

        scene hbroom with dis
        scene hentry with wipeleft
        show ta 001 at center with dis
        
        ta "「Yo, [fn]. 」"
        fn "「Morning, Tatsu-nii. 」"
    
        jump tatsuki30_walk
    
    ###########################################
    label tatsuki30_tappei:
        
        $ event_name = "Tappei..."

        scene hbroom with dis
        scene hentry with wipeleft
        show tp 001 at center with dis
        
        tp "「Yo, [fn]. 」"
        fn "「Good morning, Tappei-san. 」"
        "Why is Tappei-san here???"
        
        hide tp with qdis
        show ta 008 at center with qdis
        
        ta "「What?{w} 　Do I have something on my face? 」"
        fn "「Ah,{w=.2} no.{w} Nope, nothing. 」"
        "What's wrong with me?{p}How could I mistake Tatsu-nii for Tappei-san?"
        
        jump tatsuki30_walk
        
    ############################################
    label tatsuki30_chuukichi:

        $ event_name = "Chuukichi..."

        scene hbroom with dis
        scene hentry with wipeleft
        show cu 013 at center with dis
        
        cu "「Yo, [fn]. 」"
        fn "「M-{w=.2}morning... Chuukichi-kun. 」"
        "{size=+15}???"
    
        show cu 011 with dis
        
        cu "「You're going back today, right?{p}\ \ I came to meet'cha. 」"
        fn "「Y-{w=.2}yeah,{w} thanks... 」"
    
        show cu 005 with dis
        
        cu "「What's up, not feeling well?{w} {nw}"
        show cu 004 with dis
        extend "　...aha.\n\ \ You don't want to go back,\n\ \ and now you're feeling all sentimental, huh? 」"
        fn "「Eh?{w} 　Now that you mention it... 」"
    
        show cu 002 with dis
        
        cu "「Don't worry about school,\n\ \ 'll do something about it for you.{p}\ \ If you're okay with it, you can live with me. 」"
        fn "「U-{w=.2}umm...{w} Chuukichi-kun? 」"
        
        stop music fadeout .1     
        play music free44
        
        who "{size=+15}「What the hell are you doing!? 」"
        
        play sound crash21
        show ta 004 at midright behind cu with explosion
        show hentry at vshake
        
        ta "「You don't say 'yo', dumbass!!{p}\ \ What kind of character are you? 」"
        
        play sound hit_p07
        show cu 009 at hit_right
        $ chuu_beat += 1
        show hentry at hshake
        pause .2
        
        $ chuu_beat += 1
        
        cu "「Guooohhh-!!! 」{nw}"
        hide cu with wipe_down
        play sound bosu31
        extend ""    
        ta "「Phew, couldn't let that happen. 」"
        
        stop music fadeout 1.5    
        play sound birds_chirping loop  
  
        jump tatsuki30_walk
    
    #################################################
    label tatsuki30_walk:
    
        $ event_name = "At Summer's Conclusion"
    
        show ta 002 with dis
        
        ta "「You're going back today, right?{p}\ \ I came to meet you. 」"
        "But I never said when would be a good time..."
        
        show ta 008 with dis
        
        ta "「Hey, hurry up and get ready.{p}\ \ Don't tell me you aren't packed yet. 」"
        fn "「That's not...{p}\ \ Wait a minute. I'll be out soon. 」"
    
        stop sound fadeout .5
        play music cicada01 fadein 4
        $ renpy.music.set_volume(0.5, 0.0, channel = "music")
        scene path with wipeleft
        
        "Tatsu-nii and I walked side-by-side,\nalong that familiar country road."
        "At the beginning of August, I was walking down\nto stay over here.\nNow I'm walking the other way, leaving this place."
    
        show ta 001 at center with dis
        
        ta "「The rice plants are growing well this year...{p}\ \ Looks like harvest is gonna be a pain, again. 」"
        fn "「Oh yeah, in the fall, all the adults get together\n\ \ to harvest the rice.{w} I remember them asking us\n\ \ to go look for some of the older boys to help. 」"
        
        show ta 008 with dis
        
        ta "「It wasn't all the time,\n\ \ but when we had a day off at home,\n\ \ we'd be made to help... 」"
        fn "「Still, I don't think it's all that bad.{p}\ \ There's nothing like that in the city. 」"
        
        show ta 010 with dis
        
        ta "「You say that since you've never done it,\n\ \ but trust me, it's really tiring.{p}\ \ Just try it, and you'll see what I mean. 」"
        "I wonder if it really is that intense..."
        
        show ta 001 with dis
        
        ta "「But when the seasons change,\n\ \ it's very easy to see.{p}\ \ That's where the city's different. 」"
        fn "「I know, right? It's not that the village is\n\ \ surrounded by nature, it's that the village is\n\ \ one with nature. 」"
        ta "「Yeah.{w} There's nothing here, though,\n\ \ but I think that's the best thing about Minasato.{p}\ \ {nw}"
        show ta 007 with dis
        extend "Well, nothing except my handsome self. 」"
        
        show ta 002 with dis
        
        ta "「Don't you cry when you go back to the\n\ \ city and I'm not there. Just man up and\n\ \ deal with it until you come back. 」"
        fn "「Will you be all right when I'm not around, Tatsu-nii?{p}\ \ I won't be able to follow you around,\n\ \ and take care of you. 」"
        
        show ta 007 with dis
        
        ta "「Dumbass, who wants someone to take care of them?{p}\ \ I'm the one taking care of you.{p}\ \ Don't go mixing that up. 」"
        "..."
    
        play music piano3_014 fadein 12
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        
        fn "「I want to keep staying here\n\ \ in Minasato with you, Tatsu-nii.{p}\ \ I want Summer to keep on going like this... 」"
    
        show ta 006 with dis
        
        ta "「That's no good, then you\n\ \ have nothing to look forward to. 」"
        fn "「I like things as they are.\n\ \ I don't want to be separated from everyone. 」"
        fn "「If I grow up, we might lose touch,\n\ \ and if that happens, I feel like I might not\n\ \ be able to meet with everyone... 」"
        fn "「That's why I don't want to become an adult. 」"
        fn "「It's bad enough that Summer vacation is ending,\n\ \ but I live away from everyone, and now that we're\n\ \ growing up, it's painful not to see anyone. 」"
    
        scene sky with sdis
        
        ta "「...When we were kids, it was tough when Summer\n\ \ vacation ended, huh?{w} 　We thought 'why does it have\n\ \ to end?', and we'd be all depressed about it. 」"
        fn "「Yeah... 」"
        ta "「Every day, we'd play from dawn 'til dusk.\n\ \ We'd try to go somewhere far away,\n\ \ and plan to do something totally different. 」"
        ta "「We'd swim in the river, and go camping,\n\ \ and there'd be heaps of bugs. 」"
        ta "「Even thinking about it makes\n\ \ it seem like a lot of fun. 」"
        fn "「Yeah, that's true.{p}\ \ Every day, it was never enough.\n\ \ It was exciting all the time. 」"
        ta "「For me, this Summer was just like those times,\n\ \ and I had the time of my life. 」"
        fn "「I had a lot of fun, too.{w} This Summer has been the\n\ \ most fun of all, even more than the ones\n\ \ we used to have when we were kids. 」"
        ta "「Right?{w} 　But I think the reason this one's the\n\ \ most fun is because it's the first. 」"
        ta "「Summer comes every year.{p}\ \ But the same Summer won't come again. 」"
        ta "「There's only one Summer a year, and it passes,\n\ \ leaving the way for the next one. 」"
        ta "「It can't come back, even if it wanted to.\n\ \ That's why memories are so special. 」"
        ta "「But still, there's always the next one, right?{p}\ \ Fall, then Winter, then Spring, and then back to\n\ \ Summer. Can't you look forward to the next one? 」"
        ta "「Can't you make the next one even better? 」"
        ta "「So come on, let's get excited about next Summer.{p}\ \ We'll look forward to it until the day it arrives. 」"
        
        scene path
        show ta 001 at center 
        with sdis
        
        fn "「Oh yeah... yeah.{p}\ \ We're going to make more fun memories after this,\n\ \ and from now on, we'll always... 」"
        
        show ta 008 with dis
        
        ta "「Oh, of course.{p}\ \ So stop saying stuff like\n\ \ a sulky grade schooler. 」"
        fn "「You're mean.\n\ \ And I was taking you seriously, too... 」"
        
        show ta 002 with dis
        
        ta "「That's because I'm an adult.{p}\ \ You hurry up and grow up, too. 」"
        fn "「But I'm still a grade schooler. 」"
    
        show ta at jump_up
        
        ta "「Gahaha! Still, I promised.\n\ \ I said I'd make you happy.{w} If you're with me,\n\ \ you won't need anything else. 」"
        ta "「I'll wait until you get into college,\n\ \ so deal with it until then. 」"
        fn "「I wonder what course I should take.\n\ \ But first, I need to aim\n\ \ for a higher-level school. 」"
        
        show ta 001 with dis
        
        ta "「Well, just think about it when you get home.{p}\ \ You'll always be welcome at mine. 」"
        fn "「Yeah.{w} No need to get impatient. 」"
        "I wonder what I should do. Accounting, maybe,\nor something like architecture...?"
        
        show ta 002 with dis
        
        ta "「Come on, let's go. 」"
        ta "「If you keep lagging behind like this,\n\ \ you really won't be going back.{p}\ \ {nw}"
        show ta at jump_up
        extend "{w=.2}Gahahahaha! 」"
        fn "「Hey, waaaiiit. 」"
    
        stop music fadeout 2.5
        scene black with sdis
        pause 2
        play music free51
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        scene bstop with wipe_corner
        show to 006 at center with dis
        
        to "「Yer' late. What were you doing? 」"
        "Everyone was already gathered at the bus stop\nto see me off."
    
        show to 003 with dis
        
        to "「How long did you take to get ready,\n\ \ even after having someone pick you up?{p}\ \ Did you two need some alone time, or something? 」"
    
        show ta 010 at midleft behind to with wipeleft
        
        ta "「Nah, my bad.{w} He said he didn't want to go back,\n\ \ Then got upset like a grade schooler.{p}\ \ Sorry we're late. 」"
        fn "「Hey!{w} 　Tatsu-nii-!{w} 　That's... 」"
    
        show to 006 with dis
        
        to "「What?{w} id you say something like 'it'd be great\n\ \ if Summer vacation never ended'?{p}\ \ Not even gradeschoolers say that, any more. 」"
        
        show ta 008 with dis
        
        ta "「No, that's not true. Don't grade schoolers say\n\ \ that all the time?{w} Summer vacation is super\n\ \ important, as far as they're concerned. 」"
    
        show ky 001 at farright with wipe_right
        
        ky "「Tatsuki-san, that wasn't what he meant... 」"
        
        show ta 001 with dis
        
        ta "「Oh, really? 」"
        
        show ta 002 with dis
        
        ta "「Anyway, he said he didn't want to be away from me,\n\ \ and he kept talking and talking without listening.{p}\ \ And then we were late. Gahahahaha! 」"
    
        show ko 003 at farleft with wipeleft
        
        ko "「Still, Torahiko seems more the type for\n\ \ saying that sort of thing. 」"
    
        show to 002 with dis
        
        to "「Shut it, moron, I love school.{p}\ \ I can meet my friends, there's always something\n\ \ interesting, plus there's club stuff. 」"
    
        scene bstop with wipe_right
        show su 004 at center with wipeleft
        
        su "「Fweh? 」"    
        su "「If I remember right, weren't you just saying\n\ \ it'd be great if Summer vacation kept on going?{p}\ \ You said something about lessons being dull... 」"
    
        show to 005 at midright behind su with wipe_right
            
        to "「Tha-!{w} 　There's no way anything like that happened,\n\ \ I totally love school.{w} Shun, you're a good kid,\n\ \ can you go over there for a minute? 」"
    
        show su 005 with dis
        
        su "「Mgmg- 」"
        
        scene bstop with wipe_right
        show ky 001 at midright
        show ka 007 at midleft
        with wipe_right
        
        ky "「Ooshima... 」"
    
        show ka at jump_up
        pause .2
        
        ka "「You bastard, what are you doing to Shun? 」"
        ka "「What's this bull about liking school?{p}\ \ I see an even bigger brat over here,\n\ \ and you're usually the irresponsible one. 」"
        
        show to 003 at farleft behind ka with wipe_right
        
        to "「Wuzzat? 」"
    
        show ju 003 at farright with wipe_right
        
        ju "「You guys... Can't you be decent at the very end? 」"
    
        show to at hit_right
        pause .2
        show ka at hit_left
        show to 010 with qdis
        pause .25
        show to at hit_right
        pause .2
        show to at hit_right
        pause .2
        show ka at hit_left
        show to 005 with qdis
        pause .45
        show ju 006 at briefzoom
        show to 006
        show ka 005
        with dis
        scene bstop with sdis
        
        show so 005 at center with dis
        
        so "「Feels the same as usual... 」"
    
        show si 001 at midright with dis
        
        si "「That's the usual amount of noise,\n\ \ but it looks like the bus is here.{p}\ \ It'd be bad if you were late for this... 」"
        "In the distance, just as Shin-kun said,\nan old-fashioned looking bus\nwas approaching the bus stop."
        
        scene bstop
        show ta 001 at center 
        with wipeleft
        
        fn "「Well, bye guys. I gotta go...{p}\ \ I won't forget this month I spent with you all.\n\ \ This year's Summer has been awesome. 」"
        ta "「... 」"
        
        show ta 002 with dis
        
        ta "「Today isn't the last time we'll see you.\n\ \ Just come back. 」"
        
        show ta 001 with dis
        
        ta "「No matter how far apart you are from us,\n\ \ this place is your hometown.\n\ \ No matter what happens, that won't change. 」"
        
        show ta 002 with dis
        
        ta "「So come back...{p}\ \ We'll be waiting, until the day we meet again.{p}\ \ Gahahaha! 」"
        
        play sound bosu32
        
        "As he was laughing,\nTatsu-nii forcefully patted my back."
        
        show ta 008 with dis
        
        ta "「Come on, you gotta go.{p}\ \ I hate long goodbyes. 」"
        "Tatsu-nii pushed me onto the bus."
        fn "「Wai-{w=.2}wait, {w=.2}Tatsu-nii. 」"
        fn "「I don't need to hurry that much. 」"
        ta "「Oh, stuff it. Hurry on back. 」"
        
        hide ta
        show to 002 at center 
        with wipeleft
        
        to "「Well then, later.{w} Next time you're here,\n\ \ come and stay over at my place.\n\ \ I'll treat you to so much food you'll burst. 」"
    
        show su 001 at midright with dis
        
        su "「Bye-bye, [fn]-san! See you next time!{p}\ \ Let's play again! 」"
        fn "「Mm... yeah. 」"
    
        show so 005 at midleft behind su with wipeleft
        
        so "「Later, [ln]-san, let's meet again.{p}\ \ Ya didn't forget anything? 」"
        
        scene bstop with wipe_right
        show ka 002 at midright with wipe_right
        
        ka "「No way, he's not Kounosuke. 」"
        
        show to 002 at midleft behind ka with wipe_right
        
        to "「Hahaha, you said it. 」"
        
        show ko 005 at center with explosion
        
        ko "「Hey!{p}\ \ Don't talk about me like some helpless human.{p}\ \ Anyway, the time's just a bit more lax than usual. 」"
        
        scene bstop with wipe_right
        show ju 003 at center with wipe_right
        
        ju "「You do have time awareness problems, after all... 」"
    
        show so 001 at midright with wipe_right
        
        so "「Shocker... 」"
    
        show ko 006 at farleft with wipe_right
        
        ko "「What's that mean!?{p}\ \ I'm perfectly on time right now.{p}\ \ I just took a little time to get ready. 」"
        
        scene bstop with wipe_right
        show ky 001 at farright with wipeleft
        
        ky "「...So in the end, you haven't changed at all? 」"
    
        show ka 003 at center with wipe_right
        
        ka "「Honestly, you were late again today. 」"
    
        show su 002 at midleft with wipe_right
        
        su "「Ahahahaha! 」"
        
        scene bstop with wipe_right
        show ko 005 at center with wipe_right
        
        ko "「Uu... 」"
        
        stop music fadeout 2
        hide ko with dis
        play music cicada01 fadein 4
        $ renpy.music.set_volume(0.4, 0.0, channel = "music")
        
        driver "「Um, excuse me... 」"
        fn "「Yes, what is it? 」"
        driver  "「I'm sorry to interrupt the farewell,\n\ \ but can we leave?{p}\ \ It would be a huge problem if we were late. 」"
        fn "「Oh, I'm sorry.{w} Please, go ahead. 」"
        "I waved to everyone from the steps."
        
        stop music
        play sound auto_door
        
        fn "「Thanks, I'll co- 」{nw}"
        play music bus_idling
        $ renpy.music.set_volume(1.0, 0.0, channel = "music")
        scene bus with wipe_right
        extend ""
        
        driver "「Next stop, Kazenari.{w} Next stop is Kazenari.{p}\ \ Please remain seated, as the vehicle may jolt\n\ \ during transit. 」"
        fn "「Ow- 」"
        "There was a jolt as the bus started forward,\nmaking me lose my balance and\nknock my head into something."
        fn "「Ouch, this looks like something Tatsu-nii'd do. 」"
        to "「Hey, what are you talking about.\n\ \ Get a grip, already. 」"
        si "「Good grief. You don't stop until the end, do you? 」"
        "Everyone was looking at me,\nlaughing from outside the bus."
        
        stop music fadeout 1.5
        
        "I ran over to the seat and opened the window,\nand shouted through it."
        
        scene bus with dis
        play music piano3_001 
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        scene sky with sdis
        
        fn "「Bye, I'll see you later, I'll come back!{p}\ \ We'll meet again,{w} it's a promise! 」"
        "Because Minasato Village is my hometown..."
        "There's a place here for me to return to."
        ta "「Later, I'll be waiting!{w} 　It's a promise!{p}\ \ This time, I'll protect you!! 」"
        "At the end, Tatsu-nii was shouting and waving."
        "However, the scenery outside was flowing past."
        "Before long, everyone disappeared from sight."
        
        $ renpy.music.set_volume(0.9, 9.0, channel = "music")
        
        fn "「Bye, everyone.{w} I promise,{w} I'll be back. 」"
        "We don't need to be children forever."
        "We'll each be walking our own path."
        "There will be times when we need to say goodbye."
        "But our old home will always be here."
        "The bright and precious memories\nwill always be in my heart, like a gem."
        "I have a place to go home to."
        "I have people who are waiting for me."
        fn "「I... will be back. Definitely. 」"
        "I'll always come back to that Summer."
        "I'll always come back to\nmake that unbeatable Summer."
        "Because that is what I treasure."
        
        play music cicada01 fadein 3.5
        $ renpy.music.set_volume(0.4, 1.0, channel = "music")
        scene sky01 with sdis
        
        "A warm breeze blew in from the window,\nwarming the chilly interior of the bus."
        "Outside the bus, the clear blue sky spread out,\nand far away, thunderclouds were building."
        "I looked out the window, and up into the sky."
        
        stop music fadeout 1.5

        "\n\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ My summer...{w=.2} Is already over."
        
        jump endings

#######################################################
label shun30:
    
    $ event_name = "Wishing Stars Flowing Through the Night"
    
    "Before going to watch the meteor shower."
    
    play music festa01 fadein 1
    $ renpy.music.set_volume(0.8, 0.0, channel = "music")
    scene kodori_house with wipeleft
    show su 401 at center with dis
    
    "I was invited to the old Kodori family's house,\nin other words his grandfather's house,\nand have gone over to visit them."
    "There's Shun-kun in a yukata!"
    "The reason is that it's because he wasn't able\nto wear one at the Bon Festival, but he says\nhe just wants me to see him looking his best."
    "Ooh, I've been waiting a long time for this,\nI wanted to see it from the place where he put it on!"

    show su 402 with dis
    
    "Butterfly-like wings extend from the back of the obi.{p}He spins around to display it to me.{p}Oh, it's kind of short, isn't it?"
    "The hem above his knees lightly sways.{p}Perhaps if he sits down,\nhis underwear will definitely show."
    "How shameless!{w=.2} Whose tastes are these?!"

    show su 401 big at center_big with dis
    
    "I must burn this into my memory!{p}In order to get the full experience, \nI intently watch Shun-kun run around."
    "He has a quiet, refined elegance. Yes, yes."
    
    stop music fadeout 1
    pause 1
    scene hill night with wipeleft
    play sound night_insects loop fadein 1
    
    "He must not take it off!{w=.2} No!{w=.2}"
    "My fervent speech is ignored,\nand he changes into his everyday clothes.\nThen we go to the hill together."

    show su 005 night at center with dis
    
    su "「It's for the ceremony.{p}\ \ So it would be a huge problem\n\ \ if I got it dirty. 」"
    "...I wanted to dirty it just a little.\nWith various fluids.\nIt has a quiet,{w=.2} refined elegance.{w=.2} Ahaha."
    
    show su 001 night with dis
    
    su "「I'm glad the sky is clear. 」"
    fn "「Yeah. I was kind of worried about the weather. 」"
    "The meteor shower is tonight.{p}It's a phenomenon that decorates the night sky with\nthousands of shooting stars once every few years."
    "At least until tomorrow,\nthat is, the time when I leave,\nthere's no rain to worry about."
    "While waiting for the stars,\nI try asking Shun-kun\nhow things are going for him."
    
    $ event_name = "Kodori Family Afterword"
    
    "After the disappearance incident,\nhis disposition is considerably different\nwhen he talks about the Kodori family."
    "Above all else, I'm relieved that\nhis expression doesn't get clouded."
    
    show su 002 night with dis
    
    "As for the strained relationship\nbetween Gaku-san and his grandfather,"
    "although they are being unsociable towards\n each other, things seemed to have calmed down."
    "I was surprised to hear that Gaku-san\nhas been coming out here from Kazenari."
    su "「Now Gaku-san comes to the game store\nin Minasato's shopping district♪ 」"
    "Now the store merged and was renovated.{p}In the form of an expanding chain store, it seems\nGaku-san is responsible for their management."
    fn "「I see, that sounds like fun. 」"
    
    show su tailwag 01 night with dis
    
    su "「Hehe, I can tell you more about it. 」"
    "However, there's obviously a small gaming\npopulation in Minasato.{p}Will it be able to hold as a business?"
    "But if Shun-kun is the only customer,{w=.2}\nit should be alright."
    
    show su 001 night with dis
    
    su "「But after he graduates from school... 」"
    fn "「Wait, what?{w=.2} Gaku-san is a student? 」"
    "I thought that he was in the store\npretty much all day long..."
    "Hmm, but he is more or less\na blood relative to diligent Shun-kun.{p}I'm sure he wouldn't throw out school for work."
    fn "「But I really am glad for that.{p}\ \ He can also live in Minasato and maybe\n\ \ reconcile with your grandfather. 」"
    
    show su 002 night with dis
    
    su "「Yes!{w} They don't argue anymore.{p}\ \ But they aren't good at having\n\ \ conversations sometimes. 」"
    fn "「They've been away from each other for so long,\n\ \ of course things are going\n\ \ to be awkward between them... Oh! 」"
    
    $ event_name = "Wishes Come True"
    
    scene starry_sky with wipe_down_slow    
    call set_star_stats from _call_set_star_stats_4 
    show shooting_star
    
    "With one long, straight shooting star\nthe air is split and the curtain rises.{p}A meteor shower."
    "It's similar to that,\nbut it's more like perfect shooting stars."
    "Like rainfall,\nthe only thing I feel is awe\nat the night sky full of divinity."
    fn "「Wow... 」"
    su "「... 」"
    "I take it all in.{p}The scenery around us completely changes, and\nI'm overwhelmed by the otherworldly beams of light."
    "I think it would ruin the moment to say something,\nso I look next to me silently."
    "There, Shun-kun's eyes are wide open\nwith surprise, but the more I think about it,\nit's a little different than that."
    "He's definitely fascinated by the spectacle in front\nof him, but in the depths of his eyes it looks as\nif he's given up on something he was pondering."

    show su 004 big night at center_big with dis
    
    hide shooting_star
    call set_star_stats from _call_set_star_stats_5 
    show shooting_star behind su
    
    su "「When you make a wish on a shooting star\n\ \ ...it comes true, right? 」"
    "Huh?{p}He's not talking to anyone and muttering to himself.\nThen he continues in detail."
    
    show su 002 big night with dis
    
    su "「I got to see [fn]-san this summer\n\ \ and we did so much together.\n\ \ I wasn't lonely anymore. 」"
    
    show su 004 big night with dis
    
    su "「But if wishes do come true... 」"
    su "「I want to see him again. 」"
    
    show su 010 big night with dis
    
    su "「I want us to always be together. 」"
    
    show su 003 big night with dis
    
    su "「I don't want us to be separated... 」"
    "For a moment, there's a pause in the flow of stars.{p}A single flash of light is left behind,\nand the wishing star disappears far away."
    
    hide shooting_star
    hide su 
    with wipeleft
    
    "Shun-kun turns his back to me."
    su "「U,um. 」"
    fn "「Hm...? 」"
    su "「I don't want you to look at me. 」"
    su "「Because I've decided\n\ \ {cps=10}I'm{size=-10} not going {cps=5}to cry anymore... 」"
    "Shun-kun's words get smaller and smaller.{p}His shoulders tremble with his back turned to me.{p}The night sky regains its brightness once again."

    call set_star_stats from _call_set_star_stats_6
    show shooting_star 
    
    su "「There's nothing to be sad about.{p}\ \ That's why it's weird for me to cry. 」"
    su "「It's not like I'll never be able to see you.{p}\ \ You're just going far away.{w} ...you'll come back\n\ \ just like you did the other day. 」"
    fn "「Shun-kun... 」"
    "He wipes his tears on the edge\nof his sleeve and turns to me.{p}As hard as possible."
    "Then he looks at me painfully,{p}and tries his hardest to smile."
    
    show su 007 big night at center_big with dis
    
    su "「...please come back here again. 」"
    fn "「Shun-kun... 」"
    su "「I'll be waiting. 」"
    
    $ event_name = "The Distance of Two People"
    
    "It's not like I won't be able to see him.{p}But it's not easy either. The distance between us\nwill return to the way it was a month ago."
    "Those 5 years when Shun-kun couldn't smile\nfrom the bottom of his heart.{p}The same time is beginning again."
    "It's only for today and tomorrow we can be close."
    "What can I do?"
    
    hide shooting_star
    call set_star_stats from _call_set_star_stats_7 
    show shooting_star behind su
    show su 019 big night with dis
    
    su "「...wah. 」"
    "I hug him close to me.{p}This close contact is to make\nmy heart and body be known."
    "It's an expression of love, not haughtiness.\nI breathe in his scent, and share my warmth.\nThis awkward gesture was like an instinct."
    "I don't want to leave him."
    fn "「I don't want to leave you. 」"
    fn "「I want to be with you longer. 」"
    fn "「I want to hold and feel you. 」"
    
    show su 022 big night with dis
    
    su "「Nn...Nn. 」"
    fn "「I love you. 」"
    
    show su 007 big night with dis
    
    su "「Yes... I... 」"
    su "「I love you too. 」"
    
    $ event_name = "It Won't Be the Same"
    
    fn "「It won't be the same. {w=.2}\n\ \ It'll be different than that time.{p}\ \ And I'll come back, too. 」"
    fn "「Because I know of a way of understanding\n\ \ each other that's even deeper than hugging. 」"
    
    show su 015 big night with dis
    
    "After looking puzzled for a second,\n{nw}"
    show su 022 big night with dis
    extend "he remembers various things, and his cheeks redden."
    su "「[fn]-san... that's embarrassing. 」"
    fn "「What? 」"
    
    hide shooting_star
    call set_star_stats from _call_set_star_stats_8
    show shooting_star behind su
    show su 011 big night with dis
    
    su "「...Y-you know. 」"
    fn "「Shun-kun, are you possibly getting excited? 」"
    
    show su 017 big night with dis
    
    su "「I-it's because you're saying dirty things. 」"
    fn "「I'm just talking about the \"method\".{p}\ \ You're the one imagining dirty things, aren't you? 」"
    
    show su 020 big night with dis
    
    su "「Uu... aah, you're mean. 」"
    fn "「Heheh, sorry.{p}\ \ I'm just messing with you because you're so cute. 」"
    
    show su 019 big night with dis
    
    su "「[fn]-san... 」"
    su "「You're not going to do dirty things\n\ \ with somebody other than me, are you...? 」"
    "Uwaah, that's a bold statement.{p}Is that a subtle way of giving me a warning?"
    "Guh, this cute-faced wolf\ndoesn't miss the important things!"
    fn "「Only with you, Shun-kun.{p}\ \ Because no one else uses a voice like that. 」"
    
    show su 018 big night with dis
    
    su "「Hya...{w=.2} that's embarrassing. 」"
    
    show su 011 big night with dis
    hide shooting_star
    call set_star_stats from _call_set_star_stats_9 
    show shooting_star behind su
    
    "He turns bright red down\nto his neck and hangs his head.\nThen, he looks at me with upturned eyes."
    
    show su 020 big night with dis
    
    su "「Only with me...? 」"
    "Guh. I-I'll be okay."
    "When I get back to the city,\nI'll remember that seductive expression."
    "It'll be devoted to enjoying{w=.2} \"single player\"{w=.2}...\nThere won't be anything left in the afterglow."
    "I can only be intoxicated like this now\nwith Shun-kun's pheromones."
    "Under the eerily bright summer night sky,{p}we touch each other."
    "Until the moment we separate,{p}I spare the sadness of parting."
    
    hide shooting_star
    scene black 
    with sdis
    stop sound fadeout 1
    pause 1 
   
    $ event_name = "Good Morning"

    window hide
    play music birds_chirping    
    
    $ day = 31
    $ the_date = "August 31"
    
    scene sky01 
    show text "{size=+130}August 31" at truecenter
    with Dissolve(.5)            
    pause 3
    scene black with Dissolve(1)
    pause .4
    scene shun_house_living with sdis
    play music free0213 fadein 1
    $ renpy.music.set_volume(0.8, 0.0, channel = "music")
    
    "I make the light sound of footsteps\nas I descend from the 2nd floor.{p}A kettle of hot water whistles in the kitchen."
    "Piiii."
    su "「Good morning.\n\ \ [fn]-san,{w=.2} how do you like your eggs? 」"
    fn "「Oh, that's right... Hm. 」"
    "Why did I sleep at Shun-kun's house?"
    "Standing in the kitchen,\nShun-kun turns around to face me\nwhile holding an egg and spatula."
    "Cooking isn't something he's good at, is it?"

    show su 002 at center with dis
    
    su "「Hehee, Kouya-san and Torahiko-san taught me. 」"
    "I see."
    
    show su 005 with dis
    
    su "「Ah, but we're taking turns, aren't we?{p}\ \ You're doing the laundry today. 」"
    "We're rotating chores, huh."
    "I check the calendar.{p}There's a blue magic marker circle on yesterday,\nand a red magic marker circle on today."
    "August 31st."
    
    stop music fadeout 1
    pause 1
    scene black with dis #!#Replace with transition うねうね 

    $ event_name = "I Had a Dream"

    play sound birds_chirping loop
    scene hbroom with sdis
    
    "...{p}A dream?"
    "Even though it didn't feel all that real,\nI woke up when I realized it wasn't.{w=.2}\nIs that a phenomenon you can't do anything about?"
    "Today is the day I return from Minasato.{p}Goodbye, the familiar room I see from the futon.{p}My one month homecoming went by in an instant."
    "Is Shun-kun already awake?"

    scene black with wipeleft  
     
    $ event_name = "The Beginning of the Last Day of August"

    scene hentry with wipeleft
    play sound2 ChimeA 
    pause 3.5    
    show su 002 at center with dis
    
    su "「Good morning!{w=.2} [fn]-san! 」"
    fn "「Good morning, Shun-kun.{p}\ \ Did you sleep well yesterday? 」"
    su "「Yes!{p}\ \ Thank you very much for going with me\n\ \ late last night {nw}"
    show su at bowing
    extend "{w=.2}and taking me home. 」"
    "He dutifully bows."
    fn "「No, no, I don't mind. 」"
    "「Take care of [fn] 」{p}is called out by my grandparents,\nand Shun-kun dutifully {nw}"
    show su at bowing
    extend "{w=.2}bows again."
    fn "「Well, it's about time.{p}\ \ Thank you very much. 」"
    "I thank both of them and say goodbye,\nthen grab my luggage in the entranceway."
    "My grandma says I can come back any time.{p}My grandpa says he hopes I come back again."
    "With a nod, I say got it, and leave the roost\nthat took care of me ...although there was\na day where I didn't sleep here."

    stop sound fadeout .5
    pause .5   
 
    $ event_name = "To Meet"

    scene path
    show su 001 at center
    with wipeleft    
    play music melodious06
    $ renpy.music.set_volume(0.8, 0.0, channel = "music")
    
    "Even though August is almost over,\nthe sun in Minasato is the same as ever."
    "It is relatively comfortable compared\nto when it was at its peak,\nbut this heat doesn't weaken easily."
    su "「... 」"
    fn "「... 」"
    "And there hasn't been much conversation.{p}No, there doesn't need to be one."
    "At least the last one I'll remember\nwill be a normal one..."
    "Aah, the more I think about it,\nthe less I'm able to speak."
    "Was my enthusiasm from last night\njust carried away with the stars?"
    "I don't know when the next time\nI'll be able to come back.\nWinter break?{w=.2} Spring break?"
    "I can't promise anything.{w} Not 100\%.{p}I can't predict what's ahead.{w} I can't find\n a way for Shun-kun and I to be together."
    "Still, if I don't tell him..."
    
    show su 004 with dis
    
    su "「U-um. 」"
    fn "「Shun-ku-... 」"
    "I talked over him."
    
    show su 003 with dis
    
    su "「W-woof, you go first. 」"
    fn "「N-no, you go... 」"
    
    show su 005 with dis
    
    su "「Um, [fn]-san. 」"
    
    show su 004 with dis
    
    "Shun-kun stops as he says that."
    "He cuts away the hesitant atmosphere,\nputs on a brave expression,\nand starts talking to me."
    
    show su 001 with dis
    
    su "「Can I come to see you during winter break...? 」"
    fn "「What!? 」"
    "Shun-kun!?{p}Leaving Minasato to see me!!?"
    
    show su 010 with dis
    
    su "「It's okay if it's too much trouble. 」"
    "He looks at me while I'm terribly surprised,\nand seems to think that I don't like that idea."
    "Hanging his head,\nhe withdraws his request in a low voice."
    fn "「That's not any trouble at all!{p}\ \ I was just a little surprised,{w=.2}\n\ \ really,{w=.2} that's right,{w=.2} yeah. 」"
    
    show su 015 with dis
    
    su "「? 」"
    "Since a little while ago,\nI've been searching for a way for\nShun-kun and I to be together."
    "But I had only been saying\nit had to be in Minasato."
    "I had not thought of Shun-kun\nleaving Minasato at all."
    fn "「Of course you're welcome to, Shun-kun! 」"
    
    show su 002 with dis
    
    su "「Yaay!{w=.2} Thank you! 」"
    "When it comes to that, the conversation is different.{p}When it's one way, I'm not any good.{p}When it's two ways, I get even closer!"
    fn "「Winter break, that's December, right?{p}\ \ There's Christmas and New Year's day... 」"
    
    show su 004 with dis
    
    su "「Oh, but on New Year's Day... 」"
    fn "「Hm? 」"
    
    show su 002 with dis
    
    su "「On New Year's Day, all of my relatives\n\ \ visit the shrine.{w} But that's okay.{p}\ \ I'll make sure to ask to go to your place. 」"
    "Going with Shun-kun,{w=.2} that means {w=.2}undermining\nthe Kodori family's traditional values.{p}Hmmm.{w=.2} That's a serious responsibility,{w=.2} maybe."
    
    show su tailwag 01 with dis
    
    su "「Hehe, I'm looking forward to it.{p}\ \ I'll get to be with you again. 」"
    "Shun-kun's steps get lighter.{p}In my head, all sorts of fun things\nare swirling around."
    "Playing in the snow, the staples of the first\nthree days of the year, and everything else.\nI can be even closer this time."
    "Things I want to do continuously come to mind.{p}While I talk excitedly about this and that,\nbefore I realize it, we're at the bus stop."
    
    $ event_name = "Words of Farewell"
    
    scene bstop with wipeleft
    
    "...Five years ago.{p}If I'm not mistaken, didn't everybody\nsend me off like this?"
    "That memory has become quite vague.{p}But I'm sure this painful feeling\nis the same as that time."
    
    show ju 001 at midright with wipe_right
    pause .2
    
    ju "「...take care of yourself. 」"
    "Juuichi-san is blunt,\nbut there is warmth in his words."
    
    show si 001 at midleft with wipe_right
    pause .2
    
    si "「See you, take care of your body. 」"
    "I can sense kindness in Shin-kun's awkward behavior."
    "It's the same as that time."

    scene bstop with wipe_right
    show ky 001 at midleft with wipe_right
    
    ky "「I'm looking forward to you coming back again. 」"

    show so 003 at midright with wipe_right
    
    so "「I'll be waitin'! 」"
    fn "「Yeah... thanks Kyouji and Soutarou-kun. 」"
    "I sincerely hope for both of your progress!"

    scene bstop with wipe_right
    show ka 006 at farright with wipe_right
    pause .2
    
    ka "「You are coming back again, right? 」"
    "Kouya's tone makes it seem like\nhe's reluctant to part with me."
    "I think his voice is usually like this,\neven though I don't readily hear it..."
    
    show to 002 at center with wipe_right
    pause .2
    
    to "「That's right, come back soon!{w=.2} I'll be waiting! 」"
    "Even he says \"soon\".{p}No, if it's the way things usually are,\nhe just making fun of the way Kouya is acting."

    show to ray 01 with dis
    
    "It's sadder that the words are dependent\non Torahiko's energy.{w} Ah, owowow,{p}don't slap me on the back like that..."

    show ta 002 at farleft with wipe_right
    pause .2
    
    ta "「It'd be nice if you even moved back here! 」"
    "Slap, slap, slap, slap. Instead of a farewell gift,\nI receive the blows of 2 too painful palms.{p}...were Tatsu-nii's palms always this big?"

    show ko 002 at midright with wipe_right
    
    ko "「That's right! You living in Minasato again...  」"
    
    show ko 005 with qdis
    
    ko "「Ah, well, if you come back and\n\ \ forth in about 2 months,\n\ \ {nw}"
    show ko 002 with qdis
    extend "we can exchange information! 」"
    "Kounosuke shakes in his feelings towards me\nand his admiration of the city.{p}Yeah, I'll write. And talk on the phone."
    "I have to keep in touch with them,\nso from now on I'll be doing that a lot."
    
    scene black with sdis    
    stop music fadeout 1
    pause 1  
  
    $ event_name = "The Future Ahead of the Bus Stop"

    play sound car000 loop
    scene bus with sdis
    
    "Like at the beginning of summer,\nwhen I came back to Minasato, I'm surrounded\nby my childhood friends, exchanging words."
    "Then I'm seen off by everybody,\nand get on the bus leaving the village."
    "Among the usual members,\nShun-kun is laughing as always."
    "If I said I wasn't sad, I'd be lying.{p}I also wanted this summer vacation to last longer.\nSeveral lines symbolize our separation. "
    "「I'll see you again 」{w=.2}\n「Take care of yourself 」{w=.2}\n「Stay in touch 」{w=.2}"
    "But none of them keep this summer away from me."
    "However,"
    
    stop sound fadeout 1
    pause 1
    scene bstop
    show su 002 at center
    with sdis    
    play music pops_003
    $ renpy.music.set_volume(0.8, 0.0, channel = "music")
    
    su "「I'm definitely going to go see you! 」"

    scene bus with sdis
    
    "Just a short while ago, his words might\nhave been 「Please come see me 」.{p}He has become even closer to me now."
    "Of course, I have too.\nI want to be with him even more."
    "Our separation 5 years ago was too long in\ncomparison, but this summer was too short too."
    "I was able to regain something irreplaceable.\nAt that time, the palm of his hand\nis beyond his control."
    "He waves as hard as he can.{p}From the window of the bus, I do the same."

    $ renpy.music.set_volume(0.4, 1.5, channel = "music")
    scene sky with sdis
    
    "{cps=10}It doesn't feel like we're far from each other.{w=.2}\nThat sky is.{w=.2}\n{cps=5}Far away."
    
    stop music fadeout 5
    scene black with sdis
    pause 5

    jump endings

    
#######################################################
label kouya30:
    
    $ event_name = "The Summer that Passed By"

    scene hbroom with dis
    play music free10
    
    fn "「Haaah... 」"
    "I let out a sigh."
    "I'm back on August 30th, at 1:18.{p}I'd gone back to my grandparents' house,\nas Kouya he had to go back to his part time job."
    "It's already been four hours.{p}I just had lunch, and now I'm pretty much free.{p}But I had no idea what I should do."
    "I just had too much time on my hands."
    "For a little more than a week, I've been with Kouya.{p}There were fun times, and a few painful times,{w=.2}\nbut I think it's been very fulfilling."
    "That might be the reason it feels like\nthere's nothing to do since I'm alone."
    "I've even been keeping up to date with homework."
    "Yep, over this past month..."
    fn "「Haah... 」"
    "I sighed,{w=.2} one more time."
    "One month."
    "When I thought about that, it's been a while,\nbut a certain melancholy rolled around in my heart."
    "Tommorow will be the last day of August.{p}Then, I'll have to go back to the city.{p}I'm getting on the early-morning bus."
    "Since time passed by so quickly,\nI've forgotten something.{p}My true feelings never came forth."
    "Originally, my coming here was only\nfor the August of summer vacation.{p}And now my time was drawing to a close."
    "With such a gloomy state of affairs,\nmy motivation to do anything tanked."
    "Kouya invited me to go out with him somewhere\nonce he finishes for the day,{w=.2} so I guess\nit's all right to just lie about until then."
    "...Well, that'd probably be around sunset."
    fn "「Man, that is kind of a waste... 」"
    "Guess it can't be helped.{w=.2}\nI'll go take a walk or something..."
    "After thinking that, I spurred myself into action.{p}I put on my sandals, and staggered outside."

    scene black with wipe_right
    scene path with wipe_right
    
    "The weather's good again today, here in Minasato.{p}The sun was shining brilliantly in the deep blue sky."
    fn "「...Now then. 」"
    "In any case this is an aimless way to kill time.{p}I guess I'll be wandering around town."
    "I made up my mind as I squinted\nagainst the reflected light,{w=.2} then stepped\ninto the heat hazes hanging in the summer air."
    
    stop music fadeout 3
    scene black with sdis 
   
    $ event_name = "Shooting Star"
  
    play music free31
    scene hentry night with sdis
    show ka 002 night at center with dis
    
    ka "「Sorry,{w=.2} this is really late of me. 」"
    "When Kouya came over to meet me,\nthe sun had already set."
    "The moment after I heard the bell ring,\nI ran out to the entryway."
    "Kouya probably hurried over since he was late.{p}I could tell from his faint but audible panting.{p}It's kind of cute."
    fn "「No, it's not like that.{p}\ \ I was out until just a while ago.{w=.2}\n\ \ This is good timing. 」"
    ka "「Hm, I see.{w} Well, in that case,{w=.2}\n\ \ want to go out and see the stars?{p}\ \ The time's about right for it. 」"
    fn "「The stars? 」"
    
    show ka 003 night with dis
    
    ka "「What, you forgot about it?{p}\ \ Today's the day you can see the meteor shower.\n\ \ I thought I told you about it. 」"
    ka "「Even if I didn't,{w=.2}\n\ \ wasn't it on the news today? 」"
    fn "「Now that you mention it... 」"
    "Vague memories ran through my head as I said that.{p}I'm sure I'd heard about it, but when?"
    "I also got the feeling that\nI heard it announced on the news\nwhen I was in the living room."
    "Oh yeah,{w=.2} that was today."
    "The meteor shower would be on my\nlast night here in Minasato Village."
    "Since the location felt so perfect,{w=.2}\nmy heart had skipped a beat."
    
    show ka 002 night with dis
    
    fn "「Where should we go watch?{p}\ \ We could probably see it pretty\n\ \ well at a dark place, huh? 」"
    ka "「That's true.{p}\ \ The location's already been decided though. 」"
    fn "「Eh?{w=.2} Where? 」"
    ka "「That'll be a secret until you get there.{p}\ \ Come on,{w=.2} let's go. 」"

    scene black with wipe_right
    scene rice night with wipe_right
    
    "I followed along behind Kouya,\nas he urged me on down the road."
    "It seemed as if the whole town was looking forward\nto the meteor shower, as there were many people\nsitting outside the houses we passed by."
    "My gaze was drawn upwards,{w=.2}\nand I saw the vastness of space, along with the\nfading, glittering lines left by the stars."
    
    stop music fadeout 5
    
    "We made our way through the village,\nand for a while we went on.{p}Eventually, we reached the place Kouya had picked."    
    
    scene black with wipe_right
    scene river night with wipe_right
    show ka 002 night at center with dis
    play sound river_flow loop
    
    fn "「...here? 」"
    ka "「Yeah.{w=.2} Right here. 」"
    "We were at the usual spot at the river."
    "It's a bit of a special place for Kouya and me.{w=.2}\nOr, at least, I think it is."
    "Kouya walked down to the river bank,{w=.2}\nand sat down in a suitable place.{p}Then, he looked up to the sky."
    "I took a spot next to him and\nalso looked up at the night sky."
    "The time between the shooting stars\nappearing grew shorter and shorter."
    fn "「What time was it supposed to be at its best? 」"
    ka "「About 9 or so.{p}\ \ Right now it's about... 8:40,{w=.2}\n\ \ so we're a little early. 」"
    "And suddenly, the conversation stopped there."
    "I'm pretty sure that for the both of us,\nwe both had a lot on our minds,{w=.2}\nwhich made it hard to talk."
    "But, after hesitating, Kouya spoke up."
    
    show ka 001 night with dis
    
    ka "「...Tomorrow,{w=.2} you're going back. 」"
    fn "「Yeah... 」"
    "I confirmed it,{w=.2}\nspeaking so softly my voice\nsounded like it might go out."
    ka "「Right here.{w} For you and me,{w=.2}\n\ \ I get the feeling so much started up in this place. 」"
    ka "「So I was thinking earlier,{w=.2}\n\ \ that I wanted to be with you right here. 」"
    "Since today's the last day I'm here,{w=.2}\nI think he's saying he wanted to come to where\nit all began so we could look back at it all."
    "I didn't really understand."
    
    show ka 013 night with dis
    
    ka "「Sorry about today.{p}\ \ I wanted to spend all day with you... 」"
    fn "「You couldn't help it, it was your job.{p}\ \ If I kept intruding on your work,\n\ \ it'd probably cause problems with your manager. 」"
    fn "「I had to get ready, too. 」"
    "「I see, 」{w=.2} Kouya lightly grumbled.\nThen he continued on."
    
    show ka 001 night with dis
    
    ka "「You said you went out before I showed up,{w=.2}\n\ \ but where did you go? 」"
    fn "「Hmm,{w=.2} a bunch of places around the village.{p}\ \ ...Since I'll be going back pretty soon,{w=.2}\n\ \ I figured I'd take a long walk around. 」"
    fn "「I went to the school,{w=.2} the park, and the shrine.{p}\ \ When I went out, everything felt so nostalgic. 」"
    fn "「There's already so many things I can't remember,{w=.2}\n\ \ about a lot of different stuff... 」"
    "I only talked about it, but it felt like\nthe scenes of distant summer days\nspread out before my eyes."
    
    play music melodious01
    
    "The bustling schoolyard afternoons.{p}The see-saw bouncing back and forth until nightfall.{p}The shrine grounds that always felt a bit scary."
    "The memories floated and popped like soap bubbles,{w=.2}\ndisappearing as quickly as they came."
    "It all felt so dear to me,\nbut at the same time, it felt lonely."
    "But I put all that aside.{p}If I had to describe it, it felt kind of uncool."
    fn "「Besides,{w=.2} it's nice to look back\n\ \ on what happened this summer.{p}\ \ I'm sure-{w} no, I'm positive I won't forget this one. 」"
    "I tried bluffing with that and laughing a little.{p}Did I hide it well enough?{w=.2} I wasn't sure."
    ka "「...Don't look so sad when you laugh like that.{p}\ \ You'll make me sad too that way. 」"
    fn "「... 」"
    "Just as I worried about, it wasn't any good.{p}If I were any better at faking laughter,{w=.2}\nI probably wouldn't have thought about it so much."
    fn "「I get so lonely when I think\n\ \ about us not meeting anymore... 」"
    "I stopped looking at the sky,\nand started complaining to myself."
    "I'm only going back to my life from a month ago.{p}I knew that,{w=.2} but I loved this one month."
    "I also knew about my selfishness,\nand about things that couldn't be changed.{p}But,{w=.2} if it were possible, I wouldn't want to leave."
    
    show ka 002 night with dis
    
    ka "「Man, there's no helping you, is there...{p}\ \ You were always smiling and laughing back when\n\ \ you changed schools,{w=.2} so you can't say all that now. 」"
    fn "「But...! 」"
    "My eyes were growing hotter.{p}I'm sure if I were to look into the water's surface,{w=.2}\nit'd show my face on the verge of tears."
    
    show ka 001 night with dis
    
    ka "「I'm feeling just as sad about it as you are.{p}\ \ If we could, I wouldn't want us to part ways.{p}\ \ That's why, I plan on understanding your feelings. 」"
    ka "「However,{w=.2} this time-{p}\ \ I was thinking about what my dad talked about. 」"
    ka "「He said,{w=.2} \"Don't you have friends and family,{w=.2}\n\ \ people important to you?\" 」"
    ka "「...To be honest, I never thought what my dad\n\ \ talked about would be so appropriate here. 」"
    ka "「I thought we'd end up fighting again. 」"
    ka "「I went in thinking I'd try my best to understand.{p}\ \ But somewhere along the way,{w=.2} I gave up. 」"
    ka "「I never thought or saw that my dad\n\ \ was worried about me that much. 」"
    ka "「But, I was wrong about everything,{w=.2}\n\ \ I could speak about it properly,\n\ \ and we could come to an understanding. 」"
    ka "「That's something I can say now.{p}\ \ A year ago, we couldn't have. 」"
    ka "「I was thinking,{w=.2}\n\ \ wouldn't that be a kind of connection? 」"
    ka "「Physical distance doesn't matter,{w=.2}\n\ \ it's an unbreakable 'link' and 'bond' kind of thing. 」"
    ka "「Thanks to that being around,{w=.2}\n\ \ that might be why things could turn like this. 」"
    
    show ka 002 night with dis
    
    ka "「So, for you and me,{w=.2}\n\ \ we're definitely connected. 」"
    fn "「Kouya... 」"
    "From the side, Kouya's dignified face grew hazy.{p}His words sunk into my ears one by one."
    
    show ka 001 night with dis
    
    ka "「...Earlier,{w=.2} I said I thought\n\ \ about picking this place\n\ \ because it was where it all began. 」"
    ka "「Since today would be the last day,\n\ \ I didn't pick this place. 」"
    ka "「Here, there would always be something starting.{p}\ \ Something would change. 」"
    ka "「This summer,{w=.2} you and I changed so much.{p}\ \ That's why something can begin again here. 」"
    ka "「You have to keep going forward.{p}\ \ I'm sure that if you do,{w=.2}\nwe'll cross paths again somewhere. 」"
    "Kouya slowly turned around to look at me.\nOur eyes met."
    ka "「This is something I've asked for earlier for you.{p}\ \ I thought it might not get here in time,\n\ \ but it managed to get here today. 」"
    "He pulled out something from the pocket in his jeans."
    "As I looked at him with teary eyes,\nI could barely tell there was something there."
    "Kouya hung it around my neck.{p}...The thing he got me was...{w=.2}\na matching dog tag."
    ka "「'We are forever with.'{p}\ \ Even if we're apart, we'll always be connected. 」"
    "I quickly nodded at those words.{p}A gentle warmth wrapped around my body."

    scene starry_sky with wipe_up
    call set_star_stats from _call_set_star_stats_10 
    show shooting_star
    
    "When I looked up, Kouya had disappeared,\nand the whole night sky opened up.{p}There, the starts started falling in earnest."
    "The night sky was filled with silvery light.{p}After watching it for a while, I closed my eyes."

    hide shooting_star    
    scene black 
    with sdis
    stop music fadeout 5
    stop sound fadeout 5
    
    "Something else also slowly streamed from my eyes.{p}And just like the shooting stars,{p}they kept flowing,{w} and flowing."
    
    scene black with dis
    pause 3  
  
    $ event_name = "Running Steps"

    window hide
    play music birds_chirping  
    
    $ day = 31
    $ the_date = "August 31"
    
    scene sky01 
    show text "{size=+130}August 31" at truecenter
    with Dissolve(.5)
    pause 3
    scene black with Dissolve(1)
    pause .4
    scene hentry with dis
    
    "The night passed, and morning came.{p}Today's the day I leave Minasato Village."
    "My packing was all finished yesterday.{p}Absolutely nothing was forgotten."
    "All right then."
    "After tightly tying my shoelaces,{nw}"
    play sound standup
    extend "{p}I stood and picked up my stuff."
    "My grandparents were seeing me off,\nspeaking to me in their always-kind voices."
    "It seems they honestly wanted to come along with\nme to the bus stop,{w=.2} but they kept saying that\nwalking me up to the front door was enough."
    gm "「Well then,{w=.2} be careful on your way home, okay? 」"
    gp "「Come back again sometime.{p}\ \ We'll be waiting. 」"
    fn "「Okay, thanks.{p}\ \ And sorry for not being around\n\ \ much for the last few days. 」"
    gm "「It's okay, it's been so long since you've seen\n\ \ your friend.{w} And since you talked so much with us,{w=.2}\n\ \ you don't need to worry about it. 」"
    gp "「Yes, that's right.{p}\ \ At around your age,{w=.2}\n\ \ it'll be fine if you go out and play that much. 」"
    "The three of us laughed.{p}{nw}"
    play sound ChimeA
    extend "Then the doorbell rung out,{w=.2} right at that moment."
    gm "「Oh,{w=.2} we have a guest at this hour? 」"
    gp "「Could it be one of your\n\ \ friends coming to meet you? 」"
    "When he said that, the face of one particular\nperson leapt to my mind.{p}That really does seem possible."
    fn "「Haha, maybe so.{p}\ \ Well then,{w=.2} thanks for keeping me under your care.{p}\ \ I have to get going! 」"
    gp "「Right.{w} Tell your parents we said hi. 」"
    "I gave a small bow,{nw}"
    play sound tm2_slidedoor000
    extend "{p}then opened the door in the entryway."
    
    stop music fadeout .5
    pause .5
    scene black with dis
    scene rice_paddy with dis
    show ka 002 at center with dis
    play music o97
    
    ka "「Hey, morning, [fn]. 」"
    fn "「Morning, Kouya.{p}\ \ Did you come all this way to meet me? 」"
    "Sure enough, it was Kouya who had come over."
    "All my other friends were meeting at the bus stop,\nso for him to come out here for me made me happy."
    ka "「Yeah.{w} I was thinking I wanted to spend\n\ \ just a bit more time with you, however possible.{p}\ \ {nw}"
    show ka 006 with dis
    extend "...It's not a problem, is it? 」"
    fn "「\"Course not\"{p}\ \ Let's go.{p}\ \ Everyone will be waiting for us. 」"
    
    show ka 003 with dis
    
    ka "「Yeah.{w} Here, I'll carry your stuff.\n\ \ Let me hold that. 」"
    fn "「Eh, really?{w} Thanks, Kouya. 」"
    "I walked alongside Kouya happily,{p}in the clean morning air.{p}A smile formed on my face."
    
    show ka 002 with dis
    
    ka "「Seems like you've loosened up a lot. 」"
    fn "「Eh? 」"
    ka "「Nothing,{w=.2} I was just thinking\n\ \ about how much you cried last night. 」"
    fn "「Oh,{w=.2} yeah,{w=.2} that's true...{p}\ \ But, like you said last night,{p}\ \ we'll be connected even if we're apart. 」"
    fn "「When I can think that way,{w=.2}\n\ \ I get the feeling that things will work out fine. 」"
    fn "「I still feel kind of sad,{w=.2}\n\ \ but now, I can relax a bit. 」"
    ka "「I see. 」"
    "When I said that,{w=.2}\nKouya gave a gentle laugh.{p}Because of that, I smiled for a bit longer."
    fn "「Oh,{w=.2} I think the next time\n\ \ I can come back is winter vacation. 」"
    fn "「But I guess it really does kind of break\n\ \ my heart, if I think about us not being able\n\ \ to meet until then. 」"
    
    show ka 003 with dis
    
    ka "「Well, which is it? 」"
    fn "「Hahaha, I'm kidding.{p}\ \ I'll be okay,{w=.2} totally okay. 」"
    
    show ka 002 with dis
    
    ka "「Sheesh. 」"
    ka "「Well,{w=.2} I'll come visit you next time.{p}\ \ For winter vacation, along with\n\ \ any unexpected holidays. 」"
    
    show ka 003 with dis
    
    ka "「For our happiness, plus I don't have school. 」"
    fn "「Eh,{w=.2} you'll really come visit me? 」"
    
    show ka 005 with dis
    
    ka "「What,{w=.2} you don't want that? 」"
    fn "「No no,{w=.2} I'll have a big welcome for you.{p}\ \ ...Oh yeah, I'll have to really\n\ \ clean my room up for that. 」"
    fn "「If you could, would you mind calling in advance? 」"
    ka "「What?{w} You trying to tell me something? 」"
    fn "「No no no.{w} Of course not,{w=.2} you know? 」"
    
    show ka 003 with dis
    
    ka "「Oho!{w=.2} I won't call you at all, then.{p}\ \ I'll just ring the doorbell, out of the blue. 」"
    ka "「You better be ready for that!{p}\ \ Because maybe,{w=.2} I'll just go around and\n\ \ clean up your room or something. 」"
    fn "「Gyaaah!{w} Stop with that part at the very least!{p}\ \ There are so many things in there\n\ \ I can't let you see! 」"

    scene black with wipe_right
    scene bstop with wipe_right
    
    "As we were nearing the end of this exchange,\nwe also got steadily closer to the bus stop."
    "Everyone else was already gathered over there,{w=.2}\nand someone was waving a big hand at us.{p}It's probably Torahiko."
    "Kouya and I exchanged a glance,\nand the two of us quickened our pace."

    show to 001 at midleft
    show ky 001 at midright
    with dis
    
    to "「You're finally here, [fn].{p}\ \ {nw}"
    show to 006 with dis
    extend "I was getting worried you'd be late. 」"
    fn "「No way.{p}\ \ It would be impossible for me to be late today.{w=.2}\n\ \ I'm not Kounosuke. 」"
    
    show ky 002 with dis
    
    ky "「No, since Kounosuke wasn't late for once,{w=.2}\n\ \ we were just talking about whether or not\n\ \ his tardiness had transferred over to you. 」"

    scene bstop with dis
    
    "I looked around after he said that."
    
    pause 2
    show ko 002 at center with dis
    
    "Oh my God, it's true!{w} Kounosuke really is here!"
    fn "「Uueeehhh!?{w} No way, why!? 」"
    "I was thinking I sounded\nridiculous even to myself,{w=.2}\nbut I was that surprised."
    "In all honesty,{w=.2} I wouldn't have thought it was\nstrange if he was so late I didn't see him today."

    show ko 011 with dis
    
    ko "「What's with that response!?\n\ \ Isn't that an overreaction!?{p}\ \ I can do it if I put my mind to it, you know! 」"

    show ko 012 with dis
    
    ko "「On a day this important,{w=.2}\n\ \ I couldn't possibly be late! 」"

    hide ko with wipe_right
    show to 006 at midright with wipe_right
    show ko 012 at midleft with wipe_right
    
    to "「But you were totally late\n\ \ on the day [fn] actually\n\ \ came back,{w=.2} y'know. 」"
    
    show ko 001 with dis
    
    ko "「That's that,{w=.2} and this is this.{w} Besides,\n\ \ being late today would be the nail in the coffin.{p}\ \ There's still time to help out from it though. 」"

    scene bstop with dis
    show su 001 at farright
    show so 001 at farleft
    show si 001 at center
    with dis
    
    su "「Ohh,{w=.2} when you put it like that... 」"

    show so 005 with dis
    
    so "「Sh-{w=.2}Shun-kun.{w=.2}\n\ \ I don't think we're supposed to agree here... 」"

    show si 004 with dis
    
    si "「...In any case,{w=.2} isn't it fine\n\ \ if everyone could get here on time? 」"

    scene bstop with dis
    show ju 001 at midright
    show ta 001 at midleft
    with dis
    
    ju "「Well, either way,{w=.2}\n\ \ it looks like things'll get a little lonelier here. 」"
    
    show ta 006 with dis
    
    ta "「Yeah...{p}\ \ {nw}"
    show ta 002 with dis
    extend "But we can still meet again.{p}\ \ We can all come over to visit you next time. 」"
    fn "「Okay, come whenever you like. I'll be waiting. 」"

    scene bstop with dis
    show ko 002 at center with dis
    
    ko "「Yeah,{w=.2} even if you didn't say that,\n\ \ I'd come over, so be happy! 」"
    fn "「Heh,{w=.2} I figured you'd say that. 」"

    hide ko with dis
    
    "Everyone laughed a bit at that."
    
    play sound car000 loop
    $ renpy.music.set_volume(0.75, 0.0, channel = "sound")
    
    "It was at that time, the moment\nwe heard the unique sound of the bus' engine."
    
    show ta 001 at farleft
    show su 001 at farright
    show ta 001 at center 
    with dis
    
    to "「Oh, it's already time...{p}\ \ {nw}"
    show to 002 with dis
    extend "Later then, [fn]. Come back again sometime!{p}\ \ Next time, I'll have a room for you! 」"
    
    show su 004 with dis
    
    su "「Uuu, please come see us again?{p}\ \ {nw}"
    show su 002 with dis
    extend "I will also be waiting for you! 」"
    
    show ta 002 with dis
    
    ta "「Yeah, this is your home town,{w=.2}\n\ \ so come back whenever! 」"
    fn "「It'll be okay, I'm sure I'll see you all again soon.{p}\ \ So just keep waiting for me,{w=.2} okay you three? 」"

    scene bstop with dis
    show ju 001 at farleft
    show ko 001 at farright
    show si 001 at center
    with dis
    
    ju "「Take care of yourself,{w=.2} got it? 」"
    si "「Well, keep it up over there.{p}\ \ Don't go catching a cold. 」"

    show ko 002 with dis
    
    ko "「Yeah yeah! Health is the most important thing!{p}\ \ Ah,{w=.2} oh yeah, next time you come back,\n\ \ bring us a lot of souvenirs! 」"
    fn "「Okay,{w=.2} thanks.{p}\ \ And yeah, I'll bring a lot next time! 」"

    scene bstop with dis
    show ky 001 at midright
    show so 001 at midleft
    with dis
    
    ky "「I'll write to you.{p}\ \ Write back a reply if you can find the time. 」"
    so "「Oh, I'll write too!{p}\ \ {nw}"
    show so 006 with dis
    extend "...but writin' a letter is kinda embarrassin'. 」"
    fn "「Haha, I guess that's true.{p}\ \ Yeah, I'll definitely write back.{p}\ \ I'll keep in touch on my end too. 」"

    scene bstop with dis
    
    "I exchanged parting words with everyone.{p}It felt the same as it did five years ago."
    "Feelings of happiness and\nloneliness filled up my chest."
    "Well, there's still the most important one here,{w=.2}\nand I haven't finished talking with him yet."
    
    show ka 001 at center with dis
    
    ka "「[fn]. 」"
    fn "「Yeah? 」"
    ka "「I've really,{w=.2} really been in your care a lot.{p}\ \ --thanks. 」"
    fn "「Ahaha, you don't need to worry about that.{p}\ \ I've been taught a lot too.{w} We're even. 」"
    ka "「I see.{w=.2} Then we'll leave it at that. 」"
    fn "「Yeah,{w=.2} just like that. 」"
    
    show ka 003 with dis
    
    ka "「Right.{p}\ \ See you, [fn].{p}\ \ I'll be waiting for next time. Take care. 」"
    fn "「You too, Kouya.{p}\ \ Tell me if your band ever comes over my way.{p}\ \ I'll definitely go see. 」"
    ka "「Of course.{w} It's a promise. 」"

    hide ka with dis
    pause .4
    play sound2 honking
    
    "Suddenly, the bus' horn blasted.{p}I guess our talk got a little too long."
    fn "「Oh crap.{p}\ \ See you guys later!{p}\ \ I'll come back again, for sure! 」"
    "I took my luggage from Kouya and hurried on-board."
    "Then I immediately ran to a window,\nwhere I looked out at everyone,\ncarving their images into my memory."

    stop music fadeout 7.5
    stop sound fadeout 7.5
    
    "The bus slowly started to move.{p}Everyone was waving their hands,{w=.2}\nas they slowly disappeared behind me."
    "And then, no matter where,{w=.2}\nno matter how far,{w=.2} they kept chasing\nuntil we could no longer see each other."
    "Before long, I lost sight of them.{p}Inside the quiet bus, I was all alone."

    scene black with wipe_right
    scene bus with wipe_right
    play sound traffic01 loop
    $ renpy.music.set_volume(0.8, 0.0, channel = "sound")
    
    "I sat up in my seat, and let out a sigh.{p}Then, it started to hit me,{w=.2}\nsummer was now officially over."
    "Still, this summer may be already over,{w=.2}\nit's not like it disappeared.{p}My memories would always be with me."
    fn "「Isn't that right,{w=.2} Kouya? 」"
    "I quietly mumbled to myself as I grasped my shirt,\njust above my heart.{p}In my hand,{w=.2} I felt something firm."
    "The next time we meet, I have to really think about\nmyself without laughing about it."
    "What did I do now,\nand what do I want to do after this?"
    "The sky spread out to forever outside the window.{p}Just like my future,\nmy options are as vast as that."
    "I still don't know where I'm going to end up.{p}I just know that I always want to\nkeep what he taught me close to my heart."
    "Therefore, I want to walk with my head held high.{p}The next time we meet,\nI want to be able to stick out my chest."

    stop sound fadeout 7.5
    scene black with sdis
    
    "...Oh,{w=.2} but I might be a little bit off."
    "I thought about it, and let\nmy hand fall from my clothes."
    "The words of bonding carved in\nthe metal reflected back in my eyes."
    "'We are forever with.'"
    "It's not about next time.{p}Even though we're separated, right at this moment."
    "We'll always be together."
    
    scene black with sdis
    
    jump endings

#######################################################
label shin30:
    
    $ event_name = "Farewell Party"
    
    scene hbroom with sdis
    
    "Is this it?\nI didn't bring that much here.{p}My toothbrush...{w=.2} eh, it's fine."
    "I have my change of clothes for tomorrow and, oh,{p}I can't forget about what's in the laundry now.{p}...okay, that's everything."
    "Tomorrow's the summer vacation ends.{p}I was putting my luggage together in my room.{p}There shouldn't be anything I've forgotten."
    "Oh, I should bring my cell phone.{p}I pulled it out from within my stuff,\nthen looked at the time."

    play sound open_cell
    pause 1
    
    "Is this a good a time as any?{p}{nw}"
    play sound door_close
    extend "I should probably get going then."
    
    stop music fadeout 1.5
    scene black with dis
    pause 1.5
    
    scene shin_house_front
    show to 001 at center
    show ko 001 at farright
    with sdis
    play music daily01
    
    show to 002 with dis
    
    to "「Hey, you're here! 」"
    
    show ko 003 with dis
    show si 003 at offleft_far
    
    ko "「Welcome [fn]! 」"

    show si at move_farleft(1)
    
    si "「Why are you guys greeting him? 」"
    
    show ko 002 at jump_up
    
    ko "「Don't sweat the small stuff. 」"
    
    show to 010 with dis
    
    to "「Aren't you busy with the prep, Shin? 」"
    si "「Can't you help more if you think so?{p}\ \ {nw}"
    show si 001 with dis
    extend "Especially you Kounosuke. 」"
    
    show ko 004 with dis
    
    ko "「What?{w} But we're guests. 」"
    
    show si 003 with dis
    
    si "「Fine words from someone who's late. 」"
    
    show to 001 with dis
    
    to "「I get what you mean,\n\ \ but only Kounosuke was late. 」"
    fn "「I can believe that. 」"
    
    scene black with wipeleft
    $ renpy.music.set_volume(0.7, 0.0, channel = "music")
    scene shin_house_back
    show ju 001 at midright
    with wipeleft
    
    ju "「Kuroi, is it alright to put the chair here? 」"

    show si 001 at midleft behind ju with dis
    
    si "「Yes. Line them up circing the table,\n\ \ each will be done later. 」"
    ju "「Mmph. 」"
    
    scene shin_house_back with wipe_right
    
    "Maybe I'm a bit early.{w} We were having\n\ \ a goodbye party for me at Shin-kun's house,\n\ \ but it looks like they're still preparing it."
    
    show si 001 at center with dis
    
    si "「Sorry it isn't ready yet. 」"
    fn "「It's okay. {w=.2}I got here earlier than I said anyways.{p}\ \ That aside, how about I help out too? 」"
    
    show si 002 with dis
    
    si "「That's okay.{p}\ \ You're the guest of honor, and we're almost done,\n\ \ so just make yourself at home and wait. 」"

    hide si with wipe_right
    
    "Hmm, so I'll be looked after instead helping out?{p}When I thought that I took up Shin-kun's offer,\npulled up a chair, and watched everyone else. "
    "The setting up was mostly done,\nand all that was left was waiting for the\ntableware and cooking."

    show ta 001 at midleft
    show am 002 at midright
    with wipeleft
    
    ta "「Heeey, got the food here. 」"
    am "「Wow, it's such a big help!\n You're so strong Midoriya-kun. 」"
    
    show ta 002 with dis
    
    ta "「This is nothing.{p}\ \ {nw}"
    show ta 003 at jump_up
    extend "Whoa!? 」"
    
    show ta 006 with dis
    
    "..."
    
    show am 006 with dis
    
    am "「I can't really overlook that many upsets though,\n\ \ alright? 」"
    ta "「Y-yeah. 」"
    
    scene shin_house_back with wipe_right
    show am 001 at midleft
    show so 001 at midright
    with wipeleft
    
    so "「Do the decorations go like this? 」"
    
    show am 002 with dis
    
    am "「Yep, that's good.{p}\ \ You can take a break now Touno-kun.{p}\ \ Thank you for all your help. 」"
    
    show so 006 with dis
    
    so "「This ain't much really. 」"
    hide so with wipe_right
    show ka 001 at midright with dis
    
    ka "「Amaki-san, where should I put the drinks? 」"
    
    show am 001 with dis
    
    am "「Hmm, things might get crowded like this\n\ \ won't they?{w} Just a moment. 」"

    hide am with wipe_right
    
    am "「Takahara-kun! Takahara-kun! 」"
    ky "「Yes, what is it? 」"
    am "「I'm sorry,\n\ \ but would you help me carry in one more table? 」"
    ky "「Oh, I understand. 」"

    hide window
    hide ka with wipe_right
    show ko 001 at offleft_far
    
    "As I watched everyone,\nI suddenly realized someone was nearby..."

    show ko at move_midleft(2.5)
    
    "That tanuki was creeping up towards the food\nrestlessly peering around looking so shady."
    ko "「... 」"
    fn "「...Kounosuke? 」"
    
    show ko 002 with dis
    
    ko "「Shh! 」"

    show si 001 at midright with dis
    
    si "「...did you really think I wouldn't notice? 」"

    show ko 006 at jump_up
    
    ko "「Nwoh!? 」"
    
    show si 003 with dis
    
    si "「Oh come on, {w=.2}I don't care if you won't help,\n\ \ but can't you at least not sneak food? 」"
    
    show ko 005 with dis
    
    ko "「Tsk. 」"
    
    show si 001 with dis
    
    si "「...{w} {nw}"
    show si 004 with dis
    extend "how about you get a table out by yourself? 」"
    
    show ko 006 with dis
    
    ko "「What!?{w=.2}　You're so mean! 」"
    
    show si 003 with dis
    
    si "「Then help out a bit,\n\ \ or at least behave. 」"
    
    show ko 007 with dis
    
    ko "「Okay... 」"
    
    show ko at move_offleft_far(2.5)
    
    "Kounosuke left, dejected.{p}I involuntarily laughed after\nwatching their little back and forth."
    fn "「Pffft. 」"
    
    show si 001 with dis
    
    si "「? 」"
    fn "「Oh, sorry.{p}\ \ I was thinking, you looked just like always. 」"
    
    show si 011 with dis
    
    si "「R-really? 」"
    fn "「Yeah.{w} It's good you're in such high spirits. 」"
    
    show si 002 with dis
    
    si "「It's because you're here.{p}\ \ Thank you, [fn]. 」"
    fn "「Nah.{w} I didn't really do much.{p}\ \ That aside, {w=.2}how did that other thing turn out? 」"
    
    show si 001 with dis
    
    si "「I gave my dad a proper answer. 」"
    fn "「What'd you say? 」"
    si "「...{p}\ \ I wrote down\n\ \ {nw}"
    show si 002 with dis
    extend "'Stop sticking your nose into things, idiot.'{w=.2} 」"
    fn "{size=+25}「-PFT 」"
    "Well that's... something.{p}I-is that okay?"
    
    show si 001 with dis
    
    si "「If he complains about it,\n\ \ he can tell me the next time he sees me. 」"
    fn "「Is that okay? 」"
    si "「...{p}\ \ {nw}"
    show si 002 with dis
    extend "This is fine. 」"
    "Seeing Shin-kun smiling like that\nwas so refreshing."
    
    show si 009 with dis
    
    si "「If there's anything I want to say,\n\ \ I want to say it face to face.{p}\ \ {nw}"
    show si 001 with dis
    extend "Not by letters, {w=.2}email, {w=.2}or phone calls. 」"
    
    show si 002 with dis
    
    si "「I can be that much selfish{w=.2} can't I? 」"
    fn "「I see...{w} yeah. {w=.2}That's true. 」"

    scene black with sdis
    $ renpy.music.set_volume(0.8, 0.0, channel = "music")
    scene shin_house_back with sdis
    
    show ta 002 at center with dis
    
    ta "「Okay then, today's [fn]'s goodbye party.\n\ \ Guys, let's see him off with a bang.\n\ \ Cheers! 」"
    
    play sound glass1
    pause .1
    play sound glass1
     
    "{size=+15}「Cheers! 」"

    hide ta with dis
    
    "That's what Tatsu-nii said in the end.{p}Just as he raised his glass, so did everyone else,\nthen everyone started reaching for their food."
    "The food was placed on a different table,\nand there was salad, chicken, sandwiches.{w=.2}\nThings turned out to be a smorgasbord."
    "For now, I picked up Chicken Neapolitan\nand then some corn soup."

    show to 001 at center with dis
    
    to "「But wow man, that went by fast. 」"
    fn "「Yeah.{p}\ \ I wanted to stay here a while longer. 」"

    show to 010 big at center_big with dis
    
    to "「Right?{p}\ \ You should totally move back here. 」"
    "Torahiko held my shoulder as he said that.{p}I was firmly grabbed, and I gave a vague\nanswer to the childhood friend smiling next to me."
    fn "「H-huh?{p}\ \ Who knows? 」"

    show ka 005 at farright behind to with dis
    
    ka "「Come on, he can't decide just like that.{p}\ \ You'll bother him by being unreasonable. 」{w} {nw}"    
    hide to
    show to 003 at center
    extend "{w=.01}{nw}"
    show to at jump_up
    
    to "「What!?{p}\ \ Aren't you being cold? 」"
    
    show ka 001 with dis
    
    ka "「It's just common sense.{p}\ \ It's hard to move around here, and higher ed\n\ \ and finding employment is hard. 」"
    
    show to 002 with dis
    
    to "「Then I'll find a job for you. 」"
    
    show ka 005 with dis
    
    ka "「The sun will blow up by then. 」"
    
    show to 003 with dis
    
    to "「What was that?! 」"
    
    show ka 007 with dis
    
    ka "「What? Got a problem? 」"
    fn "「C-come on you guys. 」"

    show ko 005 at farleft behind to with dis
    
    ko "「Break it up now.\n\ \ Just take the flirting elsewhere. 」"
    
    show to at jump_up
    show ka at jump_up
    
    kato "{size=+15}「SHUT IT YOU! 」"  
    
    show ko 004 with dis
    
    "These guys haven't changed at all."
    "The way their aggressiveness turned to Kounosuke,\nmaybe if they'll be tamed sticking\nwith a certain human."
    "I left those two to Kounosuke\nand went back to my own meal."
    
    scene shin_house_back with wipe_right
    show ju 001 at center 
    show su 001 at farright
    with dis
    
    ju "「... 」"
    
    show su 004 with dis
    
    su "「Huh? You're not eating Juuichi-san? 」"
    
    show ju 003 with dis
    
    ju "「Y-yeah. 」"
    su "「What's wrong?{p}\ \ {nw}"
    show su 005 with dis
    extend "Ah, {w=.2}could it be that your stomach hurts? 」"
    ju "「Ah, no I'm fine, Kodori.{p}\ \ Don't worry about me. 」"
    
    show su 004 with dis
    
    su "「But... 」"

    show si 002 at farleft with dis
    
    si "「Yes, it's alright Shun-kun.{p}\ \ Juuichi-san's just getting ready\n\ \ for what's after this. 」"
    
    show su 015 with dis
    
    su "「After this? 」"
    si "「There's a big honey cake made.{p}\ \ I'll have to wrap up any leftovers too. 」"
    
    show ju 004 with dis
    
    ju "「Y-{w=.2}yeah. 」"

    show su 002 at jump_up
    
    su "「Woof! {w=.2}I understand!{p}\ \ Juuichi-san is a glutton. 」"
    
    play sound puu46
    show ju at shrink(.8, 1)
    
    ju "「Y-{w=.2}yeah... 」"
    "Shin-kun, your attitude's softened a bit.{p}As I saw the soft natural smile on his face,\nI suddenly felt warm fuzzy feelings myself."

    scene shin_house_back with wipe_right
    
    "Out of nowhere I felt this strange presence,{w=.2}\nthis aura, and I looked up.{p}What I saw was..."

    show so 001 at midright
    show ky 001 at midleft    
    with dis
    
    ky "「Sou, this one's good too. 」"
    so "「...(munch munch){p}\ \ {nw}"
    show so 003 at jump_up
    extend "Yeah it is!{p}\ \ {nw}"
    show so 006 with dis
    extend "Oh Sempai, I also like this one. 」"
    
    show ky 002 with dis
    
    ky "「Let me see...{w} {nw}"
    show ky 001 with dis
    extend "yep, that tastes good. 」"
    so "「Ehehe. 」"
    "I wonder what that is...{p}Doesn't it feel like\nthey have their own little world?"
    "I knew they were close when I first saw them,\nbut was it to that extent?{p}Could those two possibly be...?"
    "No wait, {w=.2}I shouldn't pry that much into things."
    
    scene shin_house_back with wipe_right
    scene black with wipeleft
    scene shin_house_back
    show ta 008 at center
    with wipeleft
    
    ta "「Hm? What the... 」"
    fn "「?{w} What's wrong Tatsu-nii? 」"
    "I was getting up from my seat to get seconds\nwhen I noticed Tatsu-nii wandering\naround looking for something."
    
    show ta 006 with dis
    
    ta "「Oh uh, I just can't find something I brought. 」"
    fn "「Something you brought?{w} Is it important? 」"
    
    show ta 008 with dis
    
    ta "「Yeah. {w=.2}I splurged on it just for today. 」"

    show am 002 at farright with dis
    
    am "「Are you talking about this? 」"

    show ta 003 at jump_up
    
    ta "「Ahh, that!? 」"
    "What the smiling Amaki-san was holding was\nwhat could be easily seen as a bottle of sake."
    "The words {w=.2}\n\"Junmai Daiginjou Refined Sake Dragon Slayer\"\nwas written on it."
    
    show am 001 with dis
    
    am "「This may be a relaxed party,\n\ \ but we can't be having this. 」"
    
    show ta 006 with dis
    
    ta "「Uugh. 」"
    
    show am 003 with dis
    
    ta "「But maybe we can\n\ \ call your father and make a big uproar of things.{p}\ \ You'll all have to take things elsewhere though. 」"

    show ta 003 at jump_up
    
    ta "「P-please forgive me! 」"
    
    show am 002 with dis
    
    am "「I'll hang onto this then. 」"
    
    show ta 005 with dis
    
    ta "「Okay... 」"

    hide am with wipe_right
    
    fn "「You really do like sake don't you Tatsu-nii. 」"
    
    show ta 009 with dis
    
    ta "「Of course I do!\n\ \ Real men drink! 」"
    fn "「But isn't this a beer gut? 」"
    
    play sound puu75
    
    "Ooh?{p}These scales feel squishy...{p}I kinda like it."
    
    show ta 002 with dis
    
    ta "「Gahahah, stop that, [fn]! It tickles! 」"
    
    play sound puu75
    pause .5
    play sound puu75
    
    fn "「It's amazing how squishy these scales are.{w=.2}\n\ \ Shouldn't you diet? 」"
    
    play sound puu75
    pause .5
    play sound puu75
    
    show ta 007 with dis
    
    ta "「That's not how it is.{p}\ \ All dragonfolk have stomachs like this. 」"
    
    play sound puu75
    pause .5
    play sound puu75
    pause .5
    play sound puu75
    scene black with sdis
    stop music fadeout 1.5
    pause 1
    scene shin_house_back with sdis
    play music daily02
    
    "By the time we were almost full,{w=.2}\nall the food was gone.{p}After that was the long awaited dessert time!"
    "The tableware the food was\nbrought in on was cleared away,\nand what was brought in its place was..."
    "How I've waited for this!{p}It was Shin-kun's handmade cake."
    "Usually it's shortcake, pie, Mont Blanc,{w=.2}\npudding and mousse,{w=.2} cupcakes,{w=.2} and other things."
    "Of course the taste is guaranteed to be good.{p}But with just this, the set would be complete\nand it feels like the big highlight of things."
    
    show si 002 at center with dis
    
    si "「I'm not sure it will be palatable though. 」"
    fn "「Of course it will! {w=.2}You always make great stuff. 」"
    
    hide si with wipe_right
    show ko 001 at farleft
    show to 001 at center 
    with dis
    
    to "「...{w} {nw}"
    show to 003 with dis
    extend "this is seriously good.{w} The taste is so smooth. 」"
    
    show ko 002 with dis
    
    ko "「Oh, does that make your blood run as a cook? 」"
    
    show to 006 with dis
    
    to "「Stop making fun of me you idiot.{w=.2}\n\ \ This really is that amazing. 」"

    show si 013 at farright with dis
    
    si "「Thank you. 」"
    fn "「...Kounosuke,\n\ \ you have pie falling out of your mouth. 」"
    
    show ko 003 with dis
    
    ko "「Fhmph?{w} Woo ai shee. 」"
    "Come on, don't speak with your mouth full."
    
    scene shin_house_back with wipe_right
    show ta 008 at farleft
    show ju 002 at center 
    show su 001 at farright
    with dis
    show su 002 at jump_up
    
    su "This is delicious!{p}\ \ {nw}"
    show su tailwag 01 with dis
    extend "Shin-san you're amazing\n\ \ for making something like this. 」"
    ju "「...mmph. 」"
    ta "「Sure, it's good. But Juuichi,{w=.2}\n\ \ aren't you eating too much? 」"
    
    show ta 006 with dis
    
    ta "「I'm getting a stomach ache\n\ \ just from looking at you. 」"
    
    show ju 003 with dis
    
    ju "「? 」"
    "Next to the weary looking Tatsu-nii,\nthere was a mountain of cake set aside..."
    "From the smell it was like a\nbig cupcake rolled in honey."
    "Seeing Juuichi-san eating just that\nreally does make my own stomach ache a little."
    
    show shin_house_front with wipe_right
    show so 003 at farleft
    show ka 003 at farright
    show ky 002 at center
    with dis
    
    ka "「I've had cake Shin made before,\n\ \ but I really do think you've got talent. 」"
    ky "「Definitely,\n\ \ it's better than a low end shop's stuff. 」"
    so "「It's amazin'! 」"
    "The moment everyone put the cake in their mouths,\nthey had nothing but praise for it.{p}I guess everyone does agree on that."
    
    scene shin_house_back with wipe_right
    show si 013 at center with dis
    
    si "「Could you all not pile on the flattery like that? 」"
    "Shin-kun smiled as if embarrassed\nwhen everyone spoke out.{w} But it's natural\nfor everyone to say it's good if it is."
    fn "「Joking aside,\n\ \ you seriously can have confidence in this. 」"
    si "「You don't need to make that big a deal of it. 」"
    fn "「You're too modest. 」"
    "Shin-kun was simply accepting everyone's comments\nwhile smiling in embarrassement.{w} Right.{w=.2}\nIt's best for people to be honest like that, {w=.2}Shin."
    
    scene black with sdis
    stop music fadeout 1.5
    pause 1.5
    scene shin_house_back red with sdis
    play music daily03
    
    "And just like that the fun times were over. I ate,{w=.2}\ntalked with,{w=.2} and helped clean up with everyone,\nlong past the point the shadows grew deeper."
    "It's this time already...{p}time for things to break up."
    "No wait,{w=.2} today's the last time I can make\nthis much noise with everyone."
    "The second I thought that,\nthis lonely feeling filled me up.{p}It'd be nice if this summer didn't end..."

    show ko 001 red at farright with dis
    
    ko "「What should be do after this? 」"

    show ta 002 red at center behind ko with dis
    
    ta "「How about another party at Raimon? 」"

    show ka 005 red at farleft with dis
    
    ka "「You just want to drink sake don't you,\n\ \ Tatsuki-san? 」"
    
    show ta 009 red with dis
    
    ta "「Yes! Is that so wrong!? 」"
    
    show ka 014 red with dis
    
    ka "「... 」"
    fn "「Hmm, I... 」"
    "Well huh.{p}It doesn't seem like\nthey'll let today end like this."

    scene shin_house_back red with wipe_right
    show to 003 red at center with dis
    
    to "「... 」"
    
    show to 002 red with dis
    
    to "「Well it'd suck if we made so much noise\n\ \ that we'd still hear it tomorrow. 」"

    show ju 001 red at farleft behind to with dis
    
    ju "「Maybe so.{w} [fn] might be tired too. 」"
    fn "「Eh? 」"

    show su 004 red at farright with dis
    
    su "「You do seem a little tired [fn]-san. 」"

    show ta 008 red at midright behind to with dis
    
    ta "「Is that true? 」"
    fn "「Y-yeah.{w=.2} Sorry.{p}\ \ I want to hang around with you guys more,\n\ \ but I might oversleep tomorrow if I do. 」"

    hide su with wipe_right
    show ko 002 red at farright with wipe_right
    
    ko "「Guess so. It'd be a huge problem if you were late\n\ \ to the bus because we drank with Tatsu-nii. 」"
    
    show ta 009 red at jump_up
    show ju 006 red at jump_up
    play sound don08
    show to 006 red with dis
    
    "{size=+15}「「「YOU DON'T GET TO SAY\n\ \ \ \ \ \ THAT! 」 」 」"
    "Whether Kounosuke was joking or being serious,{w=.2}\npretty much everyone around me\nhad the same thoughts I did."
    
    show ko 007 red with dis
    
    ko "「...{w=.2}you people are mean. 」"
    
    scene shin_house_back red with dis
    show so 001 red at farleft
    show ky 001 red at center 
    show ka 001 red at farright
    with dis
    
    ka "「But still, this is probably\n\ \ a good place to end things.{p}\ \ You probably have to stuff left pack up. 」"
    so "「That's true. 」"
    ky "「Well then, shall we part here? 」"

    scene shin_house_back red with wipe_right
    
    "And so, we all left Shin-kun's house.{p}Shin-kun has to deal with the rest\nof the clean-up, so we have to go first."
    "Earlier in the party, 'I want you\nto come back at night,'{w=.2} was whispered to me\nin a way so that no one would notice."
    "I didn't know why, but I already planned\non coming back in secret afterwards,\nso I gave a little nod then."
    "We exchanged our secret promise,\nand as everyone watched me off\nI headed back to my grandparents' house."

    scene black with sdis
    
    if shin_trueend == True:
        jump shin30_number_swap
    else:
        jump shin30_lastnight

    
    ##################################################
    label shin30_number_swap:
            
        $ event_name = "Number Exchange"

        scene rice red with dis
            
        "It was then that I realized\nI had forgotten something."
        fn "「Oh, crap. 」"
    
        show ka 001 red at center with dis
        
        ka "「What's wrong? 」"
        fn "「I forgot my cell phone. 」"
    
        show ko 006 red at farright with dis
        
        ko "「What!?{w=.2}\n\ \ That's really bad! 」"
        "The city- and appliance-obsessed Kounosuke\ngave a bit of exaggerated surprise.{p}Well I guess it is an everyday tool."
        fn "「Yeah. {w=.2}I'll go get it back. 」"
    
        show to 001 red at farleft with dis
        
        to "「Want us to come along? 」"
        fn "「I'll just be grabbing something so I'll be okay.{p}\ \ I think, {w=.2}I dropped it around that time. 」"
    
        scene rice red with wipe_right
        
        "I returned to Shin-kun's mansion\nonce I told them so.{w} I could come back later,\nbut it's better I do it sooner."
    
        scene black with sdis
        stop music fadeout 1.5
        pause 1.5
        scene shin_house_den red with sdis
        play music free51    
        show si 001 red at center with dis
        
        si "「Did you forget something? 」"
        fn "「Yeah.{w} I could have left it for later though. 」"
        "I don't think anyone could hear,\nbut my voice lowered all of a sudden either way."
        
        show si 004 red with dis
        
        si "「Oh please, what did you forget now? 」"
        fn "「This, {w=.2}this right here. 」"
        
        show si 005 red with dis
        
        si "「Ah... 」"
        "I pulled my cellphone\nout of my pocket and showed it to Shin."
        
        show si 002 red with dis
        
        si "「...you{w=.2} ...remembered. 」"
        fn "「Of course.{w} Wait, what?{p}\ \ You had that litte faith in me? 」"
        
        show si 011 red with dis
        
        si "「I-it's not like that.{p}\ \ It's just...{p}\ \ {nw}"
        show si 013 red with dis
        extend "I was just happy. 」"
        fn "「That's a relief then. 」"
    
        hide si with wipe_right
        pause .2
        play sound step03
        
        "Shin went back to his room to get his cell phone,\nthen came back.{p}And then, we exchanged our numbers and addresses."
        "When we parted, we had a secret goodbye kiss\naway from Amaki-san's eyes.{p}A kiss like a soft, gentle brushing."
        
        show si 002 red  at center with dis
        
        fn "「See you later.{p}\ \ I'll come back tomorrow night. 」"
        si "「Okay, {w=.2}I'll be waiting. 」"
        "I'm really looking forward to when night comes."
    
        scene black with sdis
    
    #####################################################
    label shin30_lastnight:
            
        $ event_name = "Two People Watching the Stars, Wishing"
        
        stop music fadeout 1.5
        pause 2
        play music night_insects
        scene path night with sdis
        
        "When the day ended, I told my grandparents\nI'd be going out, secretly snuck out,\nand headed for Shin-kun's house."
        "He had something he wanted to show me before I leave.{p}At night,{w} in secret,{w} and this reminded\nme of something I felt a litte guilty about."
        "But I can't believe Shin\nwould do something that bold.{p}What could he want to show me anyway?"
        "I took out a light from my pocket for the dark\nroad, and hurried on over to Shin-kun's mansion,\na little excited."
        
        scene shin_house_front night with wipeleft    
        play sound tm2_chime002
        pause 1.2
        play sound tm2_chair003
        pause .2
        show si 002 night at center with dis
        
        si "「Welcome.{p}\ \ You came at the perfect time. 」"
        fn "「Good evening.{p}\ \ What did you want to show me? 」"
        si "「It'll be time in a little bit,\n\ \ so go on ahead to my room. 」"
        
        stop music fadeout 1.5
        scene black with wipeleft
        scene shin_house_kitchen
        show si 001 at midleft
        show am 001 at midright
        with wipeleft    
        play music free10
        
        si "「Ah, Amaki.{w=.2}\n\ \ Could you make some tea? 」"
        
        show am 003 with dis
        
        am "「Is Darjeeling okay? 」"
        si "「What about the Assam? 」"
        am "「Sorry, we ran out of that earlier today.{p}\ \ {nw}"
        show am 001 with dis
        extend "It should be here tomorrow though. 」"
        
        show si 010 with dis
        
        si "「I see.{w=.2} I'll leave it to you then. 」"
        
        scene black with wipeleft
        scene shin_bed with wipeleft    
        pause 1.5
        play sound Door03Open
        pause .5
        show si 002 at center with dis
        
        si "「Sorry to keep you waiting. 」"
        "I was waiting in the room for a moment,\nand Shin-kun came in bringing tea and snacks."
        "Today we have cookies,{w} no wait, it looks\nlike a crispy bread,{w=.2} but what was it called?{p}Uhh...{w} -oh,{w=.2} it was rusk.{w=.2} I think."
        si "「There's still some time,{w=.2}\n\ \ so why don't we have some tea until then? 」"
        fn "「Okay.{w} That's fine,\n\ \ but what did you want to show me? 」"
        si "「Not telling yet. 」"
        
        hide si with wipe_right
        scene shin_bed night with dis
        
        "The tray was placed on a side table,\nand then Shin-kun turned off the lights.{p}Hey,{w} that's not really an invitation is it?"
        fn "「Eh?{w=.2} H-hey? 」"
    
        play sound curtain
        pause .5
        scene shin_bedroom night with sdis
        
        "The room was plunged into pitch blackness, but as\nI heard the sound of a curtain pale light came in,\nwhich was enough for me to see what was around me."
        
        show si 002 night at center with dis
        
        si "「Now then, how about some tea? 」"
        fn "「O-okay. 」"
        "I felt a bit like a little devil\nwhen I saw that moonlit smile,\nbut maybe that's because of my own impurity."
        
        scene black with sdis
        scene shin_bedroom night with sdis
        
        "For a little while I enjoyed the moonlit tea\nwith Shin-kun next to me when I suddenly felt\nas if something moved outside the window."
        
        stop music fadeout 1.5
        show si 001 night at center with dis
        
        si "「What is it? 」" 
        fn "「I just thought...{w=.2}\n\ \ something was moving outside. 」"
        si "「?{p}\ \ {nw}"
        show si 002 night with dis
        extend "...aahh. 」"
        fn "「Ah- 」"
        
        play music piano3_005
        scene black with sdis
        scene starry_sky with sdis
        call set_star_stats from _call_set_star_stats_11
        show shooting_star
        
        "When I stared out of the window this time,\nI didn't miss what it was."
        fn "「A shooting star... 」"
        si "「Looks like it's started. 」"
        "In the beginning it started with one,{w=.2}\nbut one after another, here,{w=.2} there,{w=.2}\nstars were falling through the night sky."
    
        hide shooting_star
        scene black 
        with sdis
        scene shin_bedroom night
        show si 002 night at center
        with sdis
        
        si "「They said you could see the meteor shower tonight.{p}\ \ I wanted to see it to the end with you. 」"
        
        play sound tm2_tea000
        
        "The sound of the teacup being set echoed\nin the silence.{w} Even now the number\nof shooting stars increased."
    
        play sound standup
        hide si with dis
        
        "Gently,\nI felt a warm body nestle up to me."
        si "「I've always watched by myself, but I've\n\ \ always thought, {w=.2}'I want to see it with someone.'{p}\ \ ...{w=.2}I never thought I could actually do it though. 」"
        fn "「It's beautiful. 」"
        "As my heart pounded next to the warmth cuddling\nup to me, I held the soft fur-covered hand.{p}As I did, Shin held my hand back."
        fn "「How about we wish for something? 」"
        
        show si 002 night at center with dis
        
        si "「We shouldn't.{p}\ \ It won't be granted either way. 」"
        fn "「So, {w=.2}you've got proof of that? 」"
        
        show si 010 night with dis
        
        si "「... 」"
        "Shin-kun didn't answer,\nbut I could tell he was looking away, blushing."
        fn "「Ah, thought so. 」"
        
        show si 011 night with dis
        
        si "「A-are you laughing at me? 」"
        fn "「I'm not.{p}\ \ Still, {w=.2}why don't we make a wish anyway?{p}\ \ Who knows, it might actually get granted. 」"
        
        show si 001 night with dis
        
        si "「...{w} maybe. 」"
        
        show si 002 night with dis
        
        si "「Well then, I'll make a wish too. 」"
    
        hide si with dis
        
        "In the darkness Shin closed his eyes\nand put his hands together.{w} I did the same,\nthen voiced my wish three times in my heart."
        "After making our wish we exchanged glances,\nand silently we kissed.{p}I could taste the sweetness of the rusk."
        
        if shin_trueend == True:
            jump shin30_bakery
        else:
            jump shin30_goodbye
    
    ####################################################    
    label shin30_bakery:
            
        $ event_name = "My Dream"
        
        show si 001 night at center with dis
        
        si "「...{w=.2}hey, [fn] 」"
        fn "「Hm? 」"
        si "「I've decided. 」"
        fn "「About what? 」"
        
        show si 010 night with dis
        
        si "「My dream of the future. 」"
        fn "「Dream? 」"
        si "「Yeah.{p}\ \ {nw}"
        show si 001 night with dis
        extend "I really do like to make confections. 」"
        
        show si 002 night with dis
        
        si "「Today everyone ate what I made,{p}\ \ they told me it was good,{p}\ \ and {w=.2}it made me feel so happy. 」"
        
        show si 009 night with dis
        
        si "「I tore up my father's letter of introduction,{w=.2}\n\ \ {nw}"
        show si 001 night with dis
        extend "but I think it really will be great if I made it\n\ \ as a job.{w} So I guess... 」"
        fn "「I think that's good.{p}\ \ The stuff you make is delicious. 」"
        
        show si 013 night with dis
        
        si "「Thank you.{w} I'm glad. 」"
        
        show si 001 night with dis
        
        si "「In the corner of some town somewhere,\n\ \ a small but warm store, 」"
        
        show si 005 night with dis
        
        si "「Ah,{w} {nw}"
        show si 002 night with dis
        extend " wait, {w=.2}I should be calling it a cafe.{p}\ \ {nw}"
        show si 001 night with dis
        extend "It doesn't have to be famous,\n\ \ just have enough people coming. 」"
        
        show si 002 night with dis
        
        si "「With the smell of sweets and black tea,\n\ \ time could pass by leisurely.{p}\ \ {nw}"
        show si 009 night with dis
        extend "But if I could, it wouldn't be just any town... 」"
        
        show si 001 night with dis
        
        si "「Here, this village is where I'd want\n\ \ to open that store.{w} {nw}"
        show si 002 night with dis
        extend "Doesn't it sound childish?{p}\ \ Talking about a dream like that... 」"
        
        show si 001 night with dis
        
        si "「Sorry for talking about something weird.{p}\ \ {nw}"
        show si 010 night with dis
        extend "I just wanted to tell someone,{p}\ \ {nw}"
        show si 001 night with dis 
        extend "to tell you about it. 」"
        fn "「No, I think it's a wonderful dream.{p}\ \ If that happens, maybe I can get a job there. 」"
        
        show si 002 night with dis
        
        si "「Just don't confuse salt and sugar okay? 」"
        fn "「I-I won't.{w=.2} Come on now... 」"
        si "「Hmhmhm. 」"
        fn "「Ah, {w=.2}won't your wish not come\n\ \ true anymore if you tell someone? 」"
        
        show si 001 night with dis
        
        si "「It's fine.{w} It's my dream, so I'll make it\n\ \ happen myself.{w} Besides, I wished\n\ \ for something different on the shooting star. 」"
        fn "「What's that? 」"
        
        show si 002 night with dis
        
        si "「It's a secret.{p}\ \ It won't come true if I tell you. 」"
        fn "「Whaaat?{w} Then give me a hint. 」"
        si "「You're hopeless.{p}\ \ {nw}"
        show si 001 night with dis
        extend "But only because it's you. 」"
    
        scene black with sdis
        
        si "「I'll be very happy\n\ \ if you wished for the same thing. 」"
    
    ##################################################
    label shin30_goodbye:
        
        scene black with sdis
        
        "In that peaceful night, the two of us\nenjoyed ourselves like that as much as we liked.{p}As much as time would allow..."
        
        stop music fadeout 2
        scene black with dis
        pause 3
        
        $ event_name = "The Last Day"
        $ day = 31
        $ the_date = "August 31"
        
        play music birds_chirping
        scene hbroom with sdis
        
        "Aw man, summer vacation's pretty much over.{p}My bags shouldn't be any different than when I\ncame here, but somehow it looks terribly small."
        "After I had a light breakfast,\nI made sure I didn't miss anything,\nthen carried my bags as I headed for the door."
    
        scene hentry with wipeleft
        
        gp "「Take care of yourself. 」"
        gm "「Don't get sick. 」"
        fn "「Yeah.{p}\ \ You two should stay healthy too.{p}\ \ Live long. 」"
        gp "「Hahahah, of course. 」"
        
        stop music fadeout 1
        scene path with sdis
        play music free21
        
        "Once I parted with my grandparents,{p}I headed for the bus stop."
        "So much really has happened this summer.{p}I wish things would keep going like this though."
        "As I thought of that grade school-like thought,\nI kept thinking of all the times I've\nspent with everyone as I passed the scenery."
        "...{p}I really don't want to go back."
        "I'm not at the age to throw tantrums anymore,\nbut partings really can be so bitter.{p}I wonder how Shin-kun is doing right now?"
        
        scene black with wipeleft
        scene bstop
        show si 001 at center 
        with wipeleft
        
        fn "「Ah- 」"
    
        show si 005 with dis
        
        si "「Ah... 」"
    
        show to 002 at farright with dis
        
        to "「Hey,{w=.2} you're finally here. 」"
    
        show su 002 at farleft with dis
        
        su "「Oh, [fn]-san is here. 」"
        
        show si 010 with dis
        
        "Once I could see the bus stop,\neveryone was waiting over there."
        fn "「You guys came. 」"
        
        show to 010 with dis
        
        to "「Of course.\n\ \ Aren't we your friends? 」"
        fn "「Thank you, everyone. 」"
        
        show to 002 with dis
        
        to "「You don't need to act like that. 」"
        si "「... 」"
        
        scene bstop with wipe_right
        show ju 001 at farright
        show ka 003 at center
        show ko 003 at farleft
        with dis
        
        ko "「Later [fn].{p}\ \ Next time you come we'll have\n\ \ so much more to talk about. 」"
        ka "「It's been fun seeing you again.{p}\ \ Take care when you get back. 」"
        ju "「Don't catch a cold when the seasons change. 」"
    
        scene bstop with wipe_right
        show ky 001 at midright
        show ta 002 at farleft
        show so 003 at farright
        show su 004 at center
        with dis
        
        ta "「Come back whenever you feel like it. 」"
        su "「[fn]-san...{p}\ \ Please, you must, must come back. 」"
        so "「I'm lookin' forward to the next time we meet. 」"
        ky "「See you. Good luck on the other side. 」"
    
        scene bstop with wipe_right
        
        "Everyone circled around me\nand gave me words of encouragement.{p}Among them, the one who walked past the circle was"
    
        show si 010 at center with dis
        
        si "「... 」"
    
        show to 002 at farleft with dis
        
        to "「Come on, you say something too. 」"
        
        show si 011 with dis
        
        si "「I-I know... 」"
        
        show to 006 with dis
        
        to "「Man you're as vague as ever.{p}\ \ {nw}"
        show to 002 with dis
        extend "You got here first and everything. 」"
        fn "「Really? 」"
        si "「Well, that's... 」"
    
        show to ray 01 with dis
        
        to "「You were standing here at the bus stop\n\ \ while there still wasn't anyone around. 」"
        to "「If you were that hyped up about it,\n\ \ you coulda just gone straight to his house. 」"
    
        show ko 003 at farright with dis
        
        ko "「Oh wow, he said it. 」"
        
        show to 006 with dis
        
        to "「Even if you weren't going to meet him,\n\ \ you shouldn't be late. 」"
    
        show ko 011 with dis
        
        ko "「But I wasn't late today! 」"
        to "「You barely got here before [fn] did... 」"
        
        show ko 004 with dis
        
        ko "「If I got here in time, I'm not late. 」"
    
        hide si
        show si 012 at center
        with dis
        
        si "「S-shut up! 」"
        
        show si 010 with dis
        show to 001
        show ko 001
        with dis
        
        si "「Well, {w=.2}that's not the type of person I am. 」"
    
        show ka 001 at midright behind ko with dis
        
        ka "「Oh, you have a reputation now? 」"
        
        show si 011 with dis
        
        si "「Not like that.{p}\ \ It's just,{w=.2} if I act out of character\n\ \ I thought people would see me funny. 」"
        
        show to 006 with dis
        
        to "「You pay too much attention to that sorta thing. 」"
    
        show ka 009 with dis
        
        ka "「Sounds like you've got a reputation\n\ \ to think of to me. 」"
        
        show si 005 with dis
        
        si "「R-{w=.2}really? 」"
        fn "「Ahaha.{p}\ \ I think it'd be great if\n\ \ you could be more honest with yourself Shin-kun. 」"
        
        show si 009 with dis
        
        si "「Even you, [fn]... 」"
    
        show ko 002 at jump_up
        
        ko "「Ahahah. It's just as [fn] says. 」"
        
        show to 002 with dis
        
        "Suddenly everyone was laughing."
        
        show si 002 with dis
        
        si "「Come on,{w=.2} don't you all make fun of me. 」"
        "Even Shin-kun was laughing.{p}If it were the Shin-kun from a little while before,\nhe'd probably frown and be all mad."
        
        scene bstop with wipe_right
        pause .4
        play sound honking
        
        "At that time, the bus arrived."
        fn "「Okay,{w} you guys take care too!{p}\ \ I'll definitely come back! 」"
        
        if shin_trueend == True:
            jump shin30_goodbye_kiss
        else:
            jump shin30_goodbye_normal
    
    #############################################################
    label shin30_goodbye_normal:
            
        $ event_name = "Don't Cry"

        scene bus with wipeleft
        play sound bus_idling loop
        
        "And so, I got onto the bus.{w} I could see everyone\nwaving their hands through the window.{p}Of course, Shin-kun too."
        "He was somewhat hidden by everyone,\nsmiling earnestly as if trying a bit to hide tears,\nand I smiled as hard as I could and waved back."
        "It's okay, I'll definitely come back.{p}As I held that thought in my mind,\nthe bus started moving."
        
        stop sound fadeout 1
        play sound2 truck
        stop music fadeout 1.5
        scene black with sdis
        pause 5
        
        jump endings
    
    
    #######################################################
    label shin30_goodbye_kiss:
            
        $ event_name = "A Kiss Goodbye, and for a New Beginning"
        
        si "「[fn], wait a moment. 」"
        fn "「? 」"
        "When I was about to board the bus,\nShin-kun stopped me.{p}When I turned around..."
        
        stop music fadeout 1    
        scene ev_shin_2a with dis
        
        fn "「!? 」"
        "My lips felt something warm and soft.{p}Both my cheeks felt something on them,\nwhich I'm pretty sure was Shin-kun's palms."
        
        scene ev_shin_2b with sdis
        
        si "「A goodbye kiss.{p}\ \ I haven't actually done that did I? 」"
        "My eyes widened at the sudden occurence\nas Shin-kun smiled sweetly while speaking."
        
        $ persistent.event_shin2 = True
        
        scene bstop
        show ka 010 at midright
        show to 005 at farleft
        show ko 006 at farright
        show si 002 at center
        with sdis
        
        play music free0551
        
        fn "「{cps=10}Uh, ah, um? 」"
        "I was too surprised to articulate anything.{p}I fell back on the bus steps,\nand looked up at Shin-kun's eyes."
        fn "「S-{w=.2}Shin{cps=5}...{cps=40}kun? 」"
        "Behind the mischieviously smiling Shin-kun,\nI could see everyone looking shocked."
        si "「Huh?{p}\ \ Was that so surprising? 」"
        fn "「W-well... 」"
        
        show si 001 with dis
        
        si "「Isn't it normal to at least kiss at partings?{p}\ \ {nw}"
        show si 002 with dis
        extend "So this is how people react to it in Japan. 」"
        "As Shin-kun smiled,\nhe gave me a secret wink.{p}O-{w=.2}oh,{w=.2} so that was a trick?"
        si "「You don't mean to say, that was your first kiss? 」"
        fn "「O-ohh. Yeah.{p}\ \ I {w=.2}guess. 」"
        "Well, {w=.2}it wasn't just now though."
        
        play sound auto_door
        scene black with wipeleft
        scene bus with wipeleft
        play sound bus_idling loop
        
        "As I sat in a daze, the bus doors closed\nin front of my eyes."
        "On the other side,\nthere was a black cat smiling and waving."
        "The next moment everyone regained their senses,\nthen jostled around Shin as they grabbed his head."
        "There,{w=.2} he didn't revert back\nto the unpleasable classmate."
        "But, {w=.2}it's true isn't it?"
        "I'm sure the face I see now is\nShin-kun's honest face.{w} I'm sure he wants\nto always smile with everyone like that."
        "It'll be okay.{w} I won't be late ever again.{p}Seeing him having fun with everyone\nbrought a smile to my own face."
        "As I waved back to everyone's shrinking\nfigures past the window,\nI returned their smiles in my heart."
        "Ah, cheating is wrong though isn't it,{w=.2} Shin?"
    
        play sound2 truck
        scene black with sdis
        stop sound fadeout 1        
        stop music fadeout 1.5
        stop sound2 fadeout 3
        pause 3
        
        jump endings
    
#######################################################
label juuichi30:
    
    $ event_name = "Our First and Last Village Date"
    
    play music tam_n06
    scene rice_paddy with dis
    
    "How many times have I met Juuichi-san like this?{p}I ponder that as I head to the candy store."
    "I've had numerous encounters with him,{w=.2}\nbut meetings we arranged beforehand...?{p}I could count those with both of my hands."
    "We've ran into each other by chance so many times.{p}That really is something that only happens in small,{w=.2}\nremote villages."
    "This is our first date where we mutualy love each\nother.{w} ...But these are my last days here too."
    "No, {w=.2}don't start getting depressed.{p}That would make Juuichi-san worry.{p}Just concentrate on our date right now."
    "...Yes, {w=.2}a date.{w} With Juuichi-san.{p}My expression relaxes as soon as I become aware of\nthat."
    "Thankfully there's nobody around at times like\nthese...{w} I think."
    "But I'm going on a date with my boyfriend, {w=.2}I can't\nhelp but smile, {w=.2}right?{w} Emotions aren't things that\ncan be shut away so easily."
    ju "「...Hey. 」"
    "We already planned a time to meet in advance,{w=.2}\nthere's no way we'd run into each other--"
    ju "「Hey, [fn]. 」"
    "--that is, {w=.2}unless the dragon god watching over\nMinasato really loves chance encounters."
    "While I'm thinking that, {w=.2}I turn around to see\nthe person calling out to me.{w} Juuichi-san's sullen\nface enters my field of vision."
    
    show ju 001 at center with dis
    
    fn "「Hello, {w=.2}Juuichi-san. 」"
    ju "「Hello.{p}\ \ You're kind of early. 」"
    fn "「Are you disappointed? 」"
    
    show ju 003 with dis
    
    ju "「Nobody said anything about that. 」"
    "His frown makes me smile."
    fn "「...I'm kidding.{p}\ \ I'm glad I get to spend even more time with you. 」"
    ju "「I see. 」"
    "After giving me the same reply he always does,{w=.2}\nhe turns his face away from me and murmurs"
    
    show ju 004 with dis
    
    ju "「I am too. 」"
    "...Apparently he's looking away to hide his\nembarrassment.{w} His cheeks are slightly red though,{w=.2}\nso I've already found him out."
    "I gently overlap the palm of his hand with my own.{p}There doesn't seem to be any people around,{w=.2}\nso even this much won't attract negative attention."
    "Although he looks towards me,{w=.2}\nhe quickly turns away right when our eyes meet."
    "He doesn't let go of my hand though,{w=.2}\nthat's just how he is."
    fn "「Juuichi-san, {w=.2}what should we do today? 」"
    "Now that I think about it,{w=.2} we arranged when to meet,{w=.2}\nbut we never decided on what to do for our date.{p}I missed something halfway."
    "Relaxing at the candy store or taking a walk in\nKazenari would both be nice.{w} How about a one-night\nstay at Ooshima Inn...{w} wait, {w=.2}what am I thinking?"
    
    show ju 001 with dis
    
    ju "「Is there somewhere you'd like to go? 」"
    fn "「Anywhere, {w=.2}as long as it's with you. 」"
    "In the end, {w=.2}I went with my true feelings."
    
    show ju 003 with dis
    
    ju "「I see.{p}\ \ {nw}"
    show ju 001 with dis
    extend "...Then, {w=.2}do you want to go to the mountains? 」"
    fn "「The mountains? 」"
    "That's an unexpected choice.{p}Sure I just told him that anywhere is fine,{w=.2}\nbut is there something he wants to see there?"
    
    show ju 003 with dis
    
    ju "「Yes. {w=.2}...You don't seem like you want to though.{p}\ \ I don't mean that we're going hiking. 」"
    "Apparently my face lets various things be known to\nhim."
    fn "「Huh? {w=.2}You mean something different? 」"
    
    show ju 001 with dis
    
    ju "「There's a relatively large lake there, {w=.2}don't you\n\ \ remember?{w} It's cool near the water, {w=.2}and I think the\n\ \ scenery is like this village's. 」"
    fn "「I see... 」"
    "Being cool is definitely a plus.{w} We're approaching\nthe end of August and the daytime temperatures have\ndropped, {w=.2}but that still doesn't change that it's hot."
    "It's best to stay comfortable, {w=.2}right?"
    fn "「Alright then, {w=.2}let's go there. 」"
    "Like that, {w=.2}we settled on our date spot for today."
    
    $ event_name = "What did We See at the Lake?!"

    stop music fadeout 3
    scene black with sdis
    scene lake with sdis
    play music free10
    
    "With Juuichi-san guiding me,{w=.2}\nwe arrive at the lake halfway up the mountain."
    "I expected it to be difficult walk since Juuichi-san\nsaid \"mountains\", {w=.2}but I realized that wasn't the case\nonce we started.{w} It's very close to Minasato Shrine."
    "The clear sky, {w=.2}blue lake, and then nothing but\ngreen trees comes into view.{w} It's a freshness that\nfeels different from when I went to the beach."
    "When I look up, {w=.2}I see what appears to be a pair of\nbirds, {w=.2}slowly flying in an arc."
    fn "「Mmm, {w=.2}this feels great! 」"
    "I speak to Juuichi-san while stretching out wide."
    
    show ju 002 at center with dis
    
    ju "「It sure does. 」"
    fn "「I was afraid you meant rock climbing when you said\n\ \ mountains, {w=.2}but this place is really close to the\n\ \ shrine. 」"
    fn "「Even so, {w=.2}if you had mentioned this first,{w=.2}\n\ \ I wouldn't have been so against it. 」"
    
    show ju 003 with dis
    
    ju "「...Hm.{w} You're right, {w=.2}sorry. 」"
    "Then, {w=.2}his mouth curves upwards."
    
    show ju 002 with dis
    
    ju "「...Well, {w=.2}you did seem to be panting as we went up\n\ \ the shrine stairs. 」"
    "...I tried to suppress the sound of my breathing as\nmuch as possible so he wouldn't find out,{w=.2}\nbut he completely saw through me."
    "It was quite a number of steps though,{w=.2}\nI have a feeling there's few who can get to the top\nwithout a change in their breathing."
    
    show ju 001 with dis
    
    ju "「That's a learning experience if you don't get much\n\ \ exercise. 」"
    "He once again tells me something I've heard before\nfrom him.{w} You could exercise as long as you want if\nyou never got tired..."
    "That's the thought of a completely hopeless case,{w=.2}\nisn't it?"
    fn "「I'll keep that in mind... 」"
    
    show ju 002 with dis
    
    ju "「... 」"
    "Juuichi-san lightly pats my head three times\nwithout saying anything.{w} That feels good,{w=.2}\nand makes me close my eyes."
    "If I were a cat, {w=.2}I'd probably\nbe purring right now..."
    fn "「Oh that reminds me, you retired from club\n\ \ activities yesterday, {w=.2}didn't you? 」"
    fn "「You took me home after that,{w=.2}\n\ \ did you not need to do the handing down of\n\ \ resposibilities or something? 」"
    
    show ju 001 with dis
    
    ju "「Yesterday was just for the matches.{p}\ \ Things like that are taken care of early in the\n\ \ morning, {w=.2}there aren't any particular problems. 」"
    "Oh, {w=.2}so that's why he decided to meet in the late\n\ \ morning."
    
    show ju 003 with dis
    
    ju "「...However, {w=.2}there has never been a day I regreted\n\ \ becoming the assistant captain until today.{p}\ \ That has made my time with you even shorter. 」"
    "He covers his muzzle with his right hand and says no\nmore."
    "Even though he does that,{w=.2}\nI think it's too round for to put his hand on."
    
    show ju 004 with dis
    
    ju "「So, {w=.2}uh, {w=.2}yeah.{p}\ \ Forget about what I said just now. 」"
    fn "「Hmm, {w=.2}I wonder if I should~? 」"

    show ju 007 at briefzoom
    
    ju "「JUST {w=.2}FOR-{w=.2}GET {w=.2}IT. 」"
    
    play sound attack00
    
    "He lowers the tone of his voice and strengthens the\npush of his hand that's on my head."
    fn "「I'll forget, {w=.2}I'll forget! 」"
    "I hurry to gloss over it from the tightening pain.{p}Juuichi-san sighs very deeply,{w=.2}\nand stares intently at my face."
    
    show ju 003 with dis
    
    ju "「...Why do you say that?{p}\ \ You've been getting too much of Tora's bad influence\n\ \ lately, {w=.2}haven't you? 」"
    fn "「What? {w=.2}That's not true. 」"
    ju "「Really?{p}\ \ Not too long ago, {w=.2}I don't think you would've\n\ \ ever said that. 」"
    "...Recently my use of the line \"Is it okay to say\nthat?\" has certainly gone down."
    "But that's because I've gotten better at reading\nhis facial expressions, {w=.2}right?{w} ...Torahiko might have\na little bit to do with it too, {w=.2}though."
    "Until just now,{w=.2}\nI never really thought about it or understood it that\nmuch."
    fn "「Well, that might be true.{p}\ \ But that's a good thing, {w=.2}isn't it? That just means\n\ \ that our relationship has deepened, {w=.2}right? 」"
    
    show ju 004 with dis
    
    ju "「...Hm. 」"
    
    play sound swing40_a
    hide ju with wipe_right
    
    "The moment I say that, {w=.2}he turns his back to me so\nquickly that I can feel the small gust it creates.{p}...I wish he wouldn't get so embarrassed."
    "I approach his back,{w=.2}\nand gently hug him from behind."
    "His body is much larger than mine, {w=.2}and a bit warmer\ntoo.{w} There's some unexpected muscle on his fat-\nlooking belly."
    "When I touch it,{w=.2}\nam I the only one that knows about this soft feeling?"
    "I put the side of my face against his back.{p}His scent tickles my nose."
    fn "「Hey, {w=.2}Juuichi-san. 」"
    ju "「...What? 」"
    fn "「I love you. 」"
    ju "「...I know. 」"
    "Feeling happy that he muttered those words,{w=.2}\nI tightly squeeze him agian."
    "Simply by touching our bodies like this,{w=.2}\nI feel an unbelievable happiness.{w} Even if we don't\ntalk, {w=.2}it's still not uncomfortable at all."
    "The sound of the waves on the lake's surface,{w=.2}\nthe greatly reduced cries of the cicadas,{w=.2}\nand the sound of our breathing.{w} I hear all of them."
    
    stop music fadeout 10
    
    ####################################################
    label juuichi30_sex:
        if persistent.replay == True:            
            $ first = persistent.name_first
            $ last = persistent.name_last
            $ day = 30
            $ event_name = "Mixed Heartbeats"
            
            scene lake with dis
            
        $ event_name = "Mixed Heartbeats"
        
        "I also know it's extravagant to want more than this.{p}But I still want to feel more off him.{p}I want to touch him."
        "I relax my arms just a bit, {w=.2}and insert my right hand\nunder the hem of his shirt.{w} He jumps in surprise,{w=.2}\nand his body trembles for a moment."
        "But he doesn't stop me either.{p}With his unspoken consent,{w=.2}\nI move my arm up higher."
        "I find a small protrusion among his fur,{w=.2}\nand start relentlessly playing with it."
        "Although he twists his body like it tickles at first,{w=.2}\nhe gradually starts breathing heavier and heavier\nin pleasure."
        ju "「Hah, {w=.2}kuh, {w=.2}Nngh. 」"
        fn "「Juuichi-san, {w=.2}do you like it here? 」"
        ju "「I-I'm just ticklish. 」"
        fn "「You're making pervy noises though. 」"
        ju "「...Nn. 」"
        "I didn't mean to inflame his shyness, {w=.2}but it seems to\nhave been more effective than I expected.{w} He's\nlooking down and his face is completely red."
        "That tells me now's my chance,{w=.2}\nso I bring my other hand to his crotch."
        "He his pants are already tented up in anticipation\njust from being felt up, {w=.2}strongly asserting itself.{p}I thought this yesterday too, {w=.2}but he's still big."
        "I continue to tease his nipple with my left hand, {w=.2}and\nstimulate his glans through his pants with my right.{p}Did that work?{w} Juuichi-san just took a deep breath."
        ju "「Nn, {w=.2}Kuh, {w=.2}Haah! 」"
        "I got a reaction from doing that to his nipple,{w=.2}\nbut I wonder if he'll like being played with down\nthere."
        "Alright then, {w=.2}let's focus on teasing that part now."
        
        play sound standup
        
        "I grab the top of his pants, {w=.2}and pull them down\nall at once.{w} On the lower half of his body, {w=.2}there's\na constricting-looking white tented fundoshi."
        "I stop teasing him for a moment and stand in front of\nhim.{w} Then I kneel in place, {w=.2}Juuichi-san's thing is in\ncondition in front of my very eyes."
    
        play sound sex1
        
        "I start licking him through his fundoshi."
        ju "「Guh...{w} Haah. 」"
        "Even though it's through the cloth, {w=.2}the warmth feels\ngood on my tongue.{w} Juuichi-san makes muffled noises."
        "With plenty of spit saved up,{w=.2}\nI go for the part where I think the glans is.{p}I stick to the top, {w=.2}and move my tongue around."
        "To keep licking it like this...{p}that'd probably be good, {w=.2}but I wonder if that'd\ntrouble him when it's time to leave."
        "I pull his fundoshi to the side with my hand,{w=.2}\nand grasp his exposed, {w=.2}throbbing warmth."
        "Even though it has just been set free,{w=.2}\nprecum has already started appearing from the tip.{p}I stretch my tongue out without hesitation."
        "It's just a little salty.{p}But when I consider that it belongs to Juuichi-san,{w=.2}\nI don't think it's weird or gross."
        "I stuff my mouth with his glans that stretches out my\ncheeks, {w=.2}and caress my popsicle with my tongue.{p}Is he particularly sensitive at the tip?"
        "He pants loudly every time I stimulate it."
        "While rubbing his balls,{w=.2}\nI caress the central part of his glans again."
        "Because of Juuichi-san's immodest silliness,{w=.2}\nMy strained crotch has been aching for a while now."
        "I part myself from his lower body,{w=.2}\nand look up at his face."
        "He seems to have regained some of his normal\ncomposure back from the look of ecstasy he had until\nthe stimulation stopped."
        
        show ju 004 at center with dis
        
        ju "「[fn]...? 」"
        fn "「Juuichi-san, {w=.2}can I be the one that puts it in this\ntime? 」"
        
        show ju 003 with dis
        
        ju "「Uh... 」"
        "Juuichi-san lowers his eyes in worry.{p}He's still reluctant to try it.{p}I know because I felt the same way yesterday."
        "But that's why I'm able to predict the next thing he\nsays."
        
        show ju 001 with dis
        
        ju "「...Fine.{w} I went crazy on you yesterday,{w=.2}\n\ \ so now it's my turn to take you. 」"
        fn "「Juuichi-san... {w=.2}thank you. 」"
        "I stand up and kiss him.{w} I didn't think he'd like it\nsince I just gave him a BJ, {w=.2}but he doesn't care and\nassertively gets his tongue involved."
        
        play sound standup
        
        "I release my body from Juuichi-san, {w=.2}and quickly\nget undressed.{w} He does too, {w=.2}and kicks away the\npants around his ankles."
    
        show ju 401 with dis
        
        "After he takes off his jacket and shirt,{w=.2}\nI stop him.{w} As I block his hand that was about to\nundo his fundoshi, {w=.2}he looks at me in confusion."
        
        show ju 403 with dis
        
        ju "「...Is there a reason for me to keep it on? 」"
        fn "「Nah, {w=.2}I just think you look hotter that way. 」"
        "It already accentuates his bulge nicely.{p}His lower body is exposed even though he's wearing\nunderwear. ...Mm, {w=.2}that's nice.{w} Very nice!"
        
        show ju 404 with dis
        
        ju "「...I really don't get your tastes. 」"
        "He sighs while holding his temple.{p}I choose not to say that he's going along\nwith it while he says that."
        "Anyways, {w=.2}in front of my eyes with cheeks dyed red\nis Juuichi-san with his erection exposed."
        "Telling me to not be aroused by this would be an\nimpossible proposition."
        "I instruct him to sit down with his legs spread.{p}{nw}"
        hide ju with wipe_down_slow
        extend "Although he sits for me without any objections,{w=.2}\nhis embarrassment causes him to keep his legs closed."
        "I squat down, put my hands on his knees,{w=.2}\nand put effort into pushing them aside.\nThere, {w=.2}this is perfect."
        ju "「...[fn]. 」"
        "I'm ignoring his protests now.{p}I once again run my tongue along him,{w=.2}\ngradually going lower and lower."
    
        play sound sex1
        
        "His shaft, {w=.2}balls, {w=.2}and taint.\nThen, {w=.2}I reach the innermost part of him.{p}In order to relax him, {w=.2}I lick it carefully."
        "I guess he can feel something playing with him,{w=.2}\noccasionally I hear the sweet sounds of his breath."
        "Yeah, that certainly was a complex, {w=.2}yet pleasant\nfeeling.{w} I duplicate what he did with me yesterday."
        "Meanwhile, {w=.2}his erection continues to stay strong,{w=.2}\nand is forming a pool of precum at his bellybutton."
        "When I try stimulating his glans with the palm of my\nhand,"
        ju "「Haaah! 」"
        "His back arches,{w=.2}\ngiving me the best reaction from him so far."
        "I wonder if he likes being stimulated this way.{p}When I stop loosening him and look up,{w=.2}\nthen rotate my palm one time again on his glans."
        "He looks away from me, {w=.2}a dirty look is on his face,{w=.2}\nhis eyebrows wrinkled together while he looks like\nhe's desperately trying to endure something."
        "As I trace around the area of the opening with my\nthumb, {w=.2}he groans and wrinkles his eyebrows even\ndeeper."
        fn "「Don't hold back, {w=.2}you can make the noises you were\n\ \ earlier. 」"
        ju "「Ooh, {w=.2}Kuaah! 」"
        "I don't know if my words triggered it,{w=.2}\nor else the stimulation just happened to be strong\nenough, {w=.2}but Juuichi-san responds by yelling."
        "I wet my index finger with spit,{w=.2}\nand slowly press it in while continuing to\nstroke him with my other hand."
        "His body stiffens slightly.{p}I try as much as possible to not make it painful,{w=.2}\nand slowly push harder over time."
        "I stimulate his nipples with my mouth,{w=.2}\ncausing his body to relax enough that\nI can get my finger in up to the second joint."
        ju "「Guh... 」"
        "It's hard for him to do something so unfamiliar too,{w=.2}\nisn't it?{w} A cold sweat is slowly appearing on his\nforehead."
        fn "「Juuichi-san, {w=.2}does it hurt? 」"
        ju "「No, {w=.2}not as much as I imagined.{p}\ \ ...But please don't go too fast. 」"
        fn "「Understood. 」"
        "After a few minutes I can tell by his breathing that\nhe's ready, and slowly begin to move my index finger."
        "Easily at first, {w=.2}then faster.{p}I continue the stimulation while checking on him."
        "Has the pain faded from when I first put it in?{p}His breathing has gradually turned more lustful."
        "I notice that it increases when I touch certain parts\ninside him, {w=.2}and the entrance has loosened up a lot\nfrom my finger."
        "I move my finger to massage that spot carefully."
        ju "「Uaaah! 」"
        fn "「Juuichi-san, {w=.2}do you like it here? 」"
        "He looks away while giving a tiny nod to my question.{p}I see, I'll need to intensify it then, {w=.2}won't I?{p}I rub it over and over again."
        "Is it impossible for him to endure it?\nHe's making remarkably lovely sounds."
        "...I wonder if this is enough.{w} Even though mine\nhasn't been getting any stimulation, {w=.2}the sight of\nJuuichi-san like this is plenty to keep me going."
        "I slowly pull out my index finger,{w=.2}\nand lift his ass up, {w=.2}exposing his anus to the air.{p}Then, {w=.2}I push my tip against it."
        fn "「Juuichi-san, {w=.2}are you ready? 」"
        ju "「...Yes 」"
        "When I shift the center of gravity,{w=.2}\nJuuichi-san's insides take me in, {w=.2}bit by bit."
        ju "「Guuh... 」"
        "Although his low growl makes me pull my hips back,{w=.2}\nJuuichi-san grabs me by the wrist to stop me."
        ju "「Don't pull out, {w=.2}keep going... 」"
        fn "「But are you okay?{p}\ \ You look like you're in a lot of pain... 」"
        ju "「I can put up with this much,{w=.2}\n\ \ I don't intend on being that weak, {w=.2}okay? 」"
        "..."
        "For him to say that much, {w=.2}I can't help but continue."
        "I push deep inside the thing that I had once\ntried to pull out.{w} His face distorts again,{w=.2}\nbut I don't stop halfway this time."
        "I put more weight into my hips.{w} A sliding sensation\ncan be felt on myself.{w} After I get my glans all the\nway in, {w=.2}the rest is smooth."
        
        scene ev_juuichi_2a with sdis
        
        "My hips are stuck close to his buttocks.{p}Then, {w=.2}Juuichi-san tightens up so much\nthat it almost hurts."
        "To be honest, {w=.2}I could probably cum without much work\nlike this.{w} It's a little tight, {w=.2}but I still feel like\nI could melt away just by being connected to him."
        "With my right hand, {w=.2}I grab the part of him that has\nstarted to lose firmness, {w=.2}and squeeze it up and down\nas hard as I can to distract his attention."
        "The sensation of being attacked from behind and in\nfront causes his brow to wrinkle even more."
        
        scene ev_juuichi_2b with sdis
        
        "With direct the stimulation, {w=.2}Juuichi-san regains his\nstrength.{w} To be proportional with that, {w=.2}I loosen my\ngrip on him bit by bit."
        fn "「Juuichi-san, {w=.2}I'm going to start thrusting. 」"
        ju "「... 」"
        "Before he replies, {w=.2}I start moving."
        
        play sound sex2 loop 
        $ renpy.music.set_volume(0.6, 0.0, channel = "sound")
        
        "Since there's no lube, {w=.2}I go slowly, but that doesn't\nseem to matter because I already feel like I'm on the\nbrink of an accidental discharge."
        "If I continue to thrust my hips like I am now,{w=.2}\nI don't think I'd last even a minute."
        "I want to cum at the same time as Juuichi-san,{w=.2}\nI want us to feel good together."
        "I blame focusing on the part of me that's thinking\nabout how he feels.{w} Of course I won't rest my hand\nthat's squeezing him either."
        "My glans rubs against his sensitive areas,{w=.2}\nand I can hear obscene sloppy sounds coming \nfrom down there."
        ju "「Guh, {w=.2}ah, {w=.2}oooh... 」"
        "With the simultaneous attack on two spots,{w=.2}\nJuuichi-san frantically covers his mouth with his\nright hand to stifle his voice."
        "I remove that hand, {w=.2}and lean forward\nto kiss him.{w} His rough breathing\ngoes directly in me."
        "So that I swallow it all,{w=.2}\nI suck in to take every single\nbreath from him."
        fn "「Juuichi-san, {w=.2}I'm getting close... 」"
        ju "「I-{w=.2}I am too... {w=.2}Kuh! 」"
        "With those words, {w=.2}I quicken the movement of my hips\nand hands.{w} His brow tightens.{w} It feels like\nI'm holding down an overflowing feeling of pleasure."
        "And then, {w=.2}I reach my limit all too soon."
        fn "「Juuichi-san, {w=.2}sorry but I'm cumming already! 」"
    
        stop sound
        play sound heartbeat
        scene white with qdis
        scene ev_juuichi_2b with qdis
        
        "As soon as I finish speaking,{w=.2}\nI pump plenty of the results of my lust inside him."
        ju "「Me too...{w} Ah! 」"
        
        play sound heartbeat
        scene white with qdis
        scene  ev_juuichi_2c with qdis
        
        "Was my bursting the final push for him?{p}A large quantity of semen gushes out from his lower\nbody."
        "While white liquid comes out of him,{w=.2}\nhis insides tighten up at the same time."
        "It's a little ticklish,{w=.2}\nbut it still feels strangely good."
        "While I'm immersed in the afterglow, {w=.2}I want to hold\nJuuichi-san close to me, {w=.2}but...{w} getting the mess he\nmade off of the front of me would probably be a pain."
        "Instead, I gently kiss him.{p}Taking his raised breathing into consideration,{w=.2}\nI make it a light one."
        "I start going soft, {w=.2}and pull myself out of Juuichi-\nsan.{w} Mm... {w=.2}the sound that comes out of his mouth is\nso seductive."
        
        $ event_name = "Toward Each of Our Futures"

        scene black with sdis
        
        if persistent.replay == True:
            pause .5
            $ renpy.end_replay() 
            
        $ persistent.event_juuichi2 = True
            
        scene lake with sdis
        play music daily03
        
        "We quickly jump in the water to get the sweat and\nsticky mess off our bodies."
        "When we're done with that, {w=.2}the effect of the\nmoderately cold lake has cooled my flushed body\nconsiderably."
        "I dry myself off with a towel I brought for wiping\noff sweat, {w=.2}put my clothes back on, {w=.2}and sit down."
        "Juuichi-san seems to be struggling with getting the\nmess out of his fur, {w=.2}but even though I offered to\nhelp since it was partially my fault."
        "He says it's unnecessary and refuses."
        "He gets out of the lake and walks towards me in the\nnude.{w} Then he gets a towel out of his stuffed\nknapsack, {w=.2}and begins to dry himself."
        "For some reason I get embarrassed,{w=.2}\nand look at the skunk cabbage on the other side of\nthe lake instead of Juuichi-san."
        
        play sound standup
        
        "I hear his clothes rustle as he puts them on."
    
        show ju 004 at center with dis
        
        ju "「...This might become a habit. 」"
        fn "「...Huh? 」"
        "His words that he muttered dissipate into the air.{p}I turn my head towards him."
    
        show ju 007 with dis
        
        ju "「No, {w=.2}it's nothing. 」"
        "He seems to be slightly flustered as he shakes his\nhead side-to-side.{w} Is there something I should be\nworried about when he speaks to me like that?"
        "...But I don't like the idea of him grinding on my\nhead again, {w=.2}so I decide to drop it."
        
        show ju 001 with dis
        
        ju "「...[fn],\n\ \ what do you want to do in the future? 」"
        "With a clearing of his throat,{w=.2}\nJuuichi-san asks a question to change the subject."
        fn "「Hmm, {w=.2}I haven't really thought about it that much.{p}\ \ I mean there's not much I want to do...{p}\ \ For now I guess I should go to college. 」"
        fn "「Well, I wonder if I could take it easy doing\n\ \ something related to that afterwords. 」"
        fn "「That doesn't mean I'm following the \"finding\n\ \ yourself\" fad though. 」"
        fn "「...Ah, {w=.2}you probably thought I'd say \"I'm not coming\n\ \ back here after graduating from high school\" or\n\ \ something like that, {w=.2}didn't you? 」"
        ju "「No. 」"
        "...There's something kind of sad about his quick\nreply.{w} It probably showed on my face,{w=.2}\nso Juuichi-san continues to speak."
        
        show ju 003 with dis
        
        ju "「Of course I'd be glad if you came back,{w=.2}\n\ \ but I meant that if there's something you want to do,{w=.2}\n\ \ you should give priority to it. 」"
        
        show ju 001 with dis
        
        ju "「I don't want your future to be limited because of\n\ \ me. 」"
        fn "「...Of the things I want to do,{w=.2}\n\ \ is seeing you as soon as possible not one of the\n\ \ options? 」"
        "When I ask him that, {w=.2}he begins to quietly ponder.\nAfter a short while of silence,{w=.2}\nhe exhales and speaks."
        
        show ju 008 with dis
        
        ju "「...I won't say anything if that's your answer.{p}\ \ However, {w=.2}a lot of that has to do with the emotions\n\ \ you're feeling now. 」"
        ju "「That's why I want you to think about your future\n\ \ once you've calmed down. 」"
        "His fatherly way of speaking makes me smile bitterly.{p}But that's easy to imagine when he's thinking of and\ntalking to me like that."
        fn "「...Yes, {w=.2}I will. 」"
        "That's why I'm able to obediently nod."
        "My future, {w=.2}huh...?{p}I've been putting it off for some reason,{w=.2}\nbut I need to start seriously thinking about it soon."
        fn "「What about you?{p}\ \ What are you going to do after you graduate from\n\ \ high school?{w} Go to college? 」"
        
        show ju 001 with dis
        
        ju "「No, {w=.2}I'm planning on finding a job here. 」"
        "...Since I was thinking about whether or not he would\ncome to where I live, {w=.2}his choice of not leaving\nMinasato makes me feel a bit lonely."
        "Well, {w=.2}we're just talking about me coming here when\nit's necessary though.{w} Still, {w=.2}does that mean we'll be\napart for one and half years...?"
        
        show ju 003 with dis
        
        ju "「However, {w=.2}I can't get a job until I pass the civil\n\ \ service exam next month. 」"
        "He rubs his thumb under his muzzle.{p}A civil servant?{w} That's a Juuichi-san kind of steady\nchoice."
        fn "「I can't really imagine you doing desk work\n\ \ though... 」"
        "He sighs,{w=.2}\nand raises the corner of his mouth in a wry smile."
        
        show ju 011 with dis
        
        ju "「Not all civil servants are office workers.{p}\ \ My first goal is to be a firefighter. 」"
        fn "「Oh, {w=.2}really? {p}\ \ I like that answer. 」"
        
        show ju 001 with dis
        
        ju "「...{p}\ \ I knew you'd respond that way. 」"
        "The troubled look on his face shows that he has given\nup.{w} I can't help but laugh."
        "Seeing me do that coaxes Juuichi-san into\nlaughing a bit as well."
        
        $ event_name = "Falling Stars and True Feelings"

        stop music fadeout 3
        scene black with sdis
        scene hill night with sdis
        play music free58
        
        "Our time of happiness passes in the blink of an eye.{p}I lay down next to Juuichi-san,{w=.2}\nlook up at the night sky."
        "I think that in our very limited time,{w=.2}\nwe were able to do all we can.{w} I've been with\nJuuichi-san ever since I left the house today."
        "We had a date in the village, {w=.2}played in the water,{w=.2}\ntook an afternoon nap, {w=.2}kissed, {w=.2}and then had sex."
        "I don't think about the time with have left,{w=.2}\nI devote myself to just living in the moment.{p}...It's like I'm making memories with expediency."
        "No.{w} Once I'm conscious, {w=.2}I won't let myself be stuck\nin my head anymore.{w} That would be less time spent\nwith Juuichi-san."
        "That fact makes my chest tighten.{p}I just got here, {w=.2}I can't imagine saying good-bye\nalready."
        "I glance over at his profile.{p}With his arms are crossed behind his neck,{w=.2}\nhe just stares up at the stars."
        "...I want a better view of him though,{w=.2}\nso I grab the hem of his blue jacket."
        "Juuichi-san finally turns his head towards me.{p}He has the same expression as usual.{p}Is he going to be sad to say good-bye...?"
        "He stretches out an arm, {w=.2}and slowly pulls me closer.{p}I cling to him like a baby."
        "At times like this, {w=.2}he's warm, {w=.2}big,{w=.2}\nand smells good.{w} When I hear the sound of his\nregular heart rhythm, {w=.2}I feel my mind settle down."
        "I look up, and see a meteor streak cut across the\nnight sky."
        "I try to wish that Juuichi-san and I can always\nbe like this... {w=.2}but it disappears from my sight all\ntoo soon."
        "Making a wish on a star has a strong image in\nanybody's mind precisely because it's absolutely\nimpossible."
        "If I could do this summer vacation again...{p}The thought of that suddenly crosses my mind, {w=.2}but I\nknow there's no point in thinking that'll come true."
        "This summer only happens once,{w=.2}\nand it's already almost over."
        "Once again, {w=.2}a star falls.{p}This time I don't make a wish."
        ju "「Hm, {w=.2}it's getting late. 」"
        fn "「...Yeah, {w=.2}you're right. 」"
        "I saw two in such a short period of time, {w=.2}perhaps\nit's certain.{w} A meteor shower.{w} I've never seen one\nbefore, {w=.2}but I'm sure it's a beautiful sight."
    
        scene starry_sky with wipe_up
        call set_star_stats from _call_set_star_stats_12
        show shooting_star
        
        "Twinkle.{w} Twinkle.{p}The stars burning out as soon as they fall from the\nheavens makes me wonder what they're thinking."
        "...I'm an idiot.{w} There's no way inorganic things have\nthoughts, {w=.2}right?{w} I deny the sentimental feelings\nwelling up inside me."
        "I was thinking that they're pouring like a shower,{w=.2}\nbut...{w} They are called meteor showers for a reason."
        "It's definitely pretty.{p}But... {w=.2}watching this spectacle makes me feel\nlonely in some respects."
        "Suddenly, {w=.2}Juuichi-san squeezes my shoulder with\nhis hand that's been resting on it."
        fn "「Juuichi-san...? 」"
        
        hide shooting_star
        call set_star_stats from _call_set_star_stats_13
        show shooting_star
        
        "He doesn't reply, {w=.2}he just squeezes me tighter\nwith the arm he's holding me with."
        "I don't say anything anymore either,{w=.2}\nand quietly wrap my arms around his."
        "...I see, {w=.2}Juuichi-san can be lonely too.{p}I should know that within that expressionless look,{w=.2}\nthere are a lot of emotions."
        "Why didn't I notice something so obvious until now?\nI'm an idiot. A huge idiot."
        "A noticeably large meteor flickers, {w=.2}then disappears\nfrom the night sky.{w} It's like a tear that's been held\nback finally rolling down."
        "Twinkle, {w=.2}twinkle.{p}Over time, {w=.2}many, {w=.2}many more fall.{w} That scene is\noverlapped with the side of Juuichi-san's face."
        "Maybe what Juuichi-san really wants to show me is\nthe scene reflected in his heart, {w=.2}not the meteors."
        "I open my mouth to say that, then close it and let it\nbe.{w} I'm sure he'd tell me that's not it and deny it."
        
        hide shooting_star
        call set_star_stats from _call_set_star_stats_14
        show shooting_star
        
        "There is something I can do now.{p}I can cuddle with Juuichi-san."
        
        hide shooting_star
        
        "We continue to watch the night sky,{w=.2}\nuntil we don't see any more shooting stars."
        
        $ event_name = "The Final Morning, A Morning of Good-Byes"

        stop music fadeout 5
        scene black with sdis
        pause 3
        window hide
        play music birds_chirping  
        
        $ day = 31
        $ the_date = "August 31"
    
        scene sky01 
        show text "{size=+130}August 31" at truecenter
        with Dissolve(.5)
        pause 3
        scene black with Dissolve(1)
        pause .4
        scene hbroom with sdis
        play music free60
        
        "I have many thoughts that are uncharacteristic of me.{p}By the time I got to bed, {w=.2}the sky was beginning to\nbrighten a little."
        "The voice calling my name slowly awakens my dozing\nsenses.{w} The light slipping through a gap in the door\nmakes me squint."
        "Today...{w} No, {w=.2}in a matter of hours I'll have to leave\nthis village.{w} With that though, {w=.2}I start feeling\nhelpless."
        "I'll get up, eat breakfast, {w=.2}and take a short break.{p}Then, {w=.2}I'll head towards the bus stop.{p}Even if I scream and cry, {w=.2}it won't wait for me."
        "I'm a tiny leaf floating down a river.{p}Unable to go against the flow of time,{w=.2}\nI can only let it wash me away to my destination."
        "I take off my pajamas, {w=.2}put on my clothes,{w=.2}\nand put away the futon."
        "I almost take my dirty clothes to the washing machine\nout of habit, {w=.2}but then I snap back to reality."
        "If I put them in now, {w=.2}they wouldn't be clean when\nit's time to leave, {w=.2}would they?"
        "I turn around, {w=.2}and stuff them into my travelling bag\nwith the rest of my clothes."
        "At my final meal, {w=.2}I wasn't able to eat that much."
        "My grandparents worry about my health,{w=.2}\nbut I just laugh it off and say\nthat I don't have much of an appetite."
        "With less than the usual amount of food in my\nstomach, {w=.2}I say thanks and stand up."
        "Then I take my dishes to the kitchen and put them in\na tub filled with water."
        "I wash my hands lightly with water, {w=.2}dry them with a\ntowel, {w=.2}then go back through the hallway to the room\nthat I have been sleeping in until now."
        "It's time to say good-bye to this place too...{p}Feeling sentimental, {w=.2}I look around the room."
        "I'll never forget this scene that was here when\nI arrived... {w=.2}not, {w=.2}that hasn't changed since I moved\naway."
        "I packed last night, {w=.2}but I still do a final\ncheck just in case.{w} I've forgotten...{w} Yep, {w=.2}nothing.{p}Not even the souvenirs my grandpa gave me."
        "I take a breath."
        "There's nothing in particular to do until the bus\ncomes.{w} I've never thought about how being idle can be\nso difficult."
        "I won't be able to come here for a while,{w=.2}\nshould I go chat with my grandparents...?"
        
        play sound ChimeA
        
        "While I'm idly thinking,{w=.2}\nthe sound of the doorbell interrupts my thoughts."
        "Hm, {w=.2}who could it be this early?"
        
        scene hentry
        show ju 001 at center
        with wipe_right
        
        "I quizzically go to the front door,{w=.2}\nand see a big, {w=.2}familiar figure dressed in a blue\njacket."
        fn "「Juuichi-san! 」"
        
        show ju 003 with dis
        
        ju "「...Sorry, {w=.2}but I came here early. 」"
        fn "「No, {w=.2}that's fine... {w=.2}but what's wrong?{p}\ \ There's still a lot of time before the bus gets\n\ \ here. 」"
        "When I tilt my head in confusion, {w=.2}Juuichi-san looks\nover at the wooden bear carving on the front porch as\nhe speaks."
        
        show ju 004 with dis
        
        ju "「...Well, {w=.2}you know.{p}\ \ I, {w=.2}uh, {w=.2}wanted to be with you for a little longer. 」"
        fn "「Juuichi-san... 」"
        ju "「...Am I bothering you? 」"
        fn "「No way, {w=.2}I'm really happy!{p}\ \ Wait a minute, {w=.2}I'll go get my luggage. 」"
    
        scene hbroom with wipe_right
        
        "I return to my room to get my bag,{w=.2}\nthen go to the living room where my grandparents are."
        "Their faces show that they're suprised that a friend\ncame to pick me up, {w=.2}they soon smile."
        "I tell them I'm really thankful for letting me stay,{w=.2}\nand give them a deep bow."
        "Both of them say there's no need to say thanks,{w=.2}\nyou're always welcome, {w=.2}and our house is your house\nrespectively."
        "Before leaving the room, {w=.2}I give another small bow\nand say good-bye to them with a smile.{p}Then I walk to the front door with my bag."
        
        scene hentry
        show ju 001 at center
        with wipe_right
        
        fn "「Sorry to keep you waiting. 」"
        ju "「Alright, {w=.2}let's get going. 」"
        "I nod, {w=.2}put on my shoes, {w=.2}and step outside."
        
        $ event_name = "The Faraway Hometown"

        stop music fadeout 3
        scene black  with sdis
        scene rice_paddy with sdis
        play music piano3_014
        
        "Even though I think that Minasato never changes,{w=.2}\nsigns of Autumn are starting to appear."
        "There are dragon flies early in the morning,{w=.2}\nand the ears of rice have grown in the paddies,{w=.2}\nwaiting to be harvested."
        "Nothing stays the same.{p}Me, {w=.2}Juuichi-san, {w=.2}or this village."
        "Juuichi-san usually leads diagonally in front of me,{w=.2}\nbut today I walk while snuggling up close to him.{p}Our pace seems to be somewhat slower too."
        "I look left and right, {w=.2}making sure nobody sees us.{p}Then I change my bag over to my right hand,{w=.2}\nthen place my left on Juuichi-san's hand."
        "I thought he'd say something,{w=.2}\nbut Juuichi-san only looked at me for a moment."
        "I tightly squeeze it, {w=.2}and he grasps back gently,{w=.2}\nso he doesn't stab me with his claws."
        "We walk while holding hands for a while.{p}It feels like his body temperature is being\ncompletely given to me through my left hand."
        "...It's really warm."
        
        show ju 001 at center with dis
        
        ju "「When you think about it,{w=.2}\n\ \ this month went by in the blink of an eye. 」"
        "It's rare for him to be the one that breaks the\nsilence.{w} I nod my head."
        fn "「Yeah, {w=.2}it did.{w} It feels like we just had my\n\ \ welcoming party.{w} Why does time have to fly\n\ \ when you're having fun? 」"
        ju "「...Because you're not paying attention to the time.\n\ \ On the other hand, don't you wish tough times would\n\ \ be over quickly? 」"
        ju "「That's why I think progressing too much feels\n\ \ slow. 」"
        fn "「Yeah, {w=.2}that's right. 」"
        "When it's stated so logically, {w=.2}it feels like\nI've been persuaded to think that way too.{p}...It's all thanks to Juuichi-san though."
        ju "「...[fn], {w=.2}did you enjoy your summer vacation? 」"
        fn "「Of course I did!{w} I reunited with everybody,{w=.2}\n\ \ and played until dark like when we were kids. 」"
        fn "「...And more importantly, {w=.2}I fell in love with you,{w=.2}\n\ \ and got to walk and hold hands like this. 」"
        fn "「If I didn't say I had fun and I'm happy,{w=.2}\n\ \ I'd be lying. 」"
        ju "「I see.{w} {nw}"
        show ju 002 with dis
        extend "...I feel the same way. 」"
        fn "「Juuichi-san... 」"
        ju "「If you get lonely, {w=.2}you can come back here anytime.{p}\ \ I'll always be here, {w=.2}thinking about you all the\n\ \ time. 」"
        "Juuichi-san gently smiles."
        
        $ event_name = "Smiling as I say Good-Bye"

        stop music fadeout 3
        scene black with sdis
        scene bstop with sdis
        play music free04
        
        "I see the bus stop in the distance.{w} Right away I\nnotice Torahiko waving his arms.{w} Is it called having\nreally good eyes,{w} or being sharp sighted...?"
        "I lightly sigh, {w=.2}and engrave the feeling of Juuichi-\nsan's warm hand into my memory.{p}Then, {w=.2}I slowly let go."
        "I look over at Juuichi-san to ask\n\"Was that enough?\"{p}He smiles and gives a small nod."
        "The flow of time does not stop.{p}Children become adults sooner or later.{p}I can't be spoiled forever either."
        "I won't lie and say that I'm not sad and don't wish\nthings could be like this forever.{w} But I'd become\na nuisance to Juuichi-san."
        "Therefore, {w=.2}I'll be patient.{p}If it's for Juuichi-san, {w=.2}I can do it."
        "When we get to the bus stop,{w=.2}\nit goes without saying that Torahiko is the first to\nspeak."
        
        show to 003 at center with dis
        
        to "「[fn], {w=.2}you're late! 」"
        fn "「The bus isn't going to be here for another ten\n\ \ minutes, {w=.2}right?{w} You always act like I'm doing\n\ \ things at the last minute. 」"
        "Torahiko scratches his head roughly."
        
        show to 007 with dis
        
        to "「Uh... {w=.2}Didn't you know you're having a farewell\n\ \ party?{w} If you say things like that,{w=.2}\n\ \ you'll end up like Kounosuke someday! 」"
        
        hide to with wipe_right
        show to 007 at midleft
        show ko 005 at midright
        with wipe_right
        
        ko "「Oh shut up, {w=.2}Torahiko.{p}\ \ When do I ever do that? 」"
        to "「Jeez, {w=.2}he's gonna be late today too, {w=.2}isn't he?{p}\ \ {nw}"
        show to 005 with dis
        extend "...Whaaa? 」"
        "Torahiko freezes up with a goofy look on his face.{p}I can't hide that I'm a little suprised as well."
        "I never thought Kounosuke would ever be somewhere\nearlier than me..."
        fn "「...Kounosuke, {w=.2}did you eat something weird? 」"
    
        show ko 011 with dis
        
        ko "「I made sure I'd be here to see off my friend! 」"
        "Juuichi-san delivers a finishing blow to the offended\nKounosuke."
        
        scene bstop with wipe_right
        show to 006 at farleft
        show ju 001 at farright
        show ko 011 at center
        with wipe_right
        
        ju "「...That's the face of somebody who has had their\n\ \ bad habits exposed. 」"
        
        show ko 006 with dis
        
        ko "「You too!? 」"
        "His shoulders droop in defeat.{p}Seeing that, {w=.2}everybody laughs."
        "During that, {w=.2}Kyouji whispers to me softly."
        
        scene bstop with wipe_right
        show ky 001 at center with wipe_right
        
        ky "「...From the look of things,{w=.2}\n\ \ I'm guessing everything went well? 」"
        fn "「Yeah.{w} Sorry, {w=.2}I wasn't able to tell you about it. 」"
        ky "「No, {w=.2}that's fine.{p}\ \ When I saw you two so happy together,{w=.2}\n\ \ it made giving the both of you a pep talk worth it. 」"
        fn "「Kyouji... 」"
        
        show ky 002 with dis
        
        ky "「But by the way things are going,{w=.2}\n\ \ you're still in for a lengthy long-distance\n\ \ relationship. 」"
        ky "「Make sure you stay in contact with each other. 」"
        ky "「He may not seem like it, {w=.2}but he's a popular guy.\n\ \ ...Keep a good hold on him, {w=.2}okay? 」"
        fn "「I will.{w} Thank you, {w=.2}Kyouji. 」"
        
        show ky 001 with dis
        
        ky "「Don't mention it. 」"
        "He smiles gently.{p}Then, {w=.2}Soutarou-kun suddenly shows up from behind."
        
        hide ky with wipe_right
        show ky 001 at midleft
        show so 001 at midright
        with wipe_right
        
        so "「Senpais, {w=.2}what are you talking about?{p}\ \ Let me in on it too! 」"
        ky "「I'm just giving him a little relationship advice.{p}\ \ It's nothing you need to worry about, {w=.2}Sou. 」"
        fn "「That's right.{w} I've got someone else I love,{w=.2}\n\ \ so don't worry about me snatching Kyouji away from\n\ \ you. 」"
        
        show so 005 with dis
        
        so "「Wha,{w} ...Whaaat?! 」"
        "Soutarou-kun face instantly turns red."
        "Oh, {w=.2}I see.{w} I was a special case when Kyouji\ntold me at that time, {w=.2}but Soutarou-kun\nthought nobody knew."
        "...Maybe I shouldn't have said that.{p}When I look over at Kyouji for help,{w=.2}\nhe shrugs his shoulders."
        ky "「Sorry, {w=.2}Sou.{w} One thing led to another,{w=.2}\n\ \ and I ended up telling [fn] about us. 」"
        so "「R-{w=.2}Really...? 」"
        fn "「Sorry.{p}\ \ I never planned on telling anybody else though. 」"
        so "「...I think my lifespan just got a little shorter. 」"
        "He pouts just a bit.{w} He looks strangely more\nchildlike than his usual peppy self,{w=.2}\nmaking me laugh a little."
        "...Aah, {w=.2}now I understand why Kyouji likes teasing him\nso much."
        fn "「I know, {w=.2}the four of us should go on a date the next\n\ \ time I'm here. 」"
        ky "「Oh, {w=.2}that would be nice. 」"
        so "「Wait, {w=.2}the four of us? A double date?{p}\ \ {nw}"
        show so 003 with dis
        extend "Senpai, {w=.2}you're going out with somebody? 」"
        fn "「Yep. {w=.2}Just recently. 」"
        so "「Can you tell me who it is? 」"
        fn "「Of course I can. {w=.2}It's Juuichi-san 」"
        
        show so 005 with dis
        
        so "「Wha,{w} ...Whaaat?! 」"
        "When he yells hysterically, {w=.2}this time he freezes up\nso much it looks like he turned to stone.{w} Hmm,{w=.2}\nI don't think it's fair that only I know."
        "...That might have backfired.{p}Kyouji taps my shoulder with a bitter smile."
        ky "「...It looks like I owe Sou an explaination later. 」"
        fn "「Yeah, {w=.2}please do. 」"
        "I quickly bow my head to Kyouji.{p}Then, {w=.2}Kouya speaks to me in a troubled sounding\nvoice."
        
        scene bstop with wipe_right
        show ka 005 at center with wipe_right
        
        ka "「Sorry, {w=.2}[fn]. {p}\ \ Can you help me out here? 」"
        fn "「Huh? {w=.2}Help with...? 」"
        "I stop speaking there.{w} Next to Kouya,{w=.2}\nI see Shun-kun standing there looking like he\ncould burst into tears at any moment."
        "Uh-oh, {w=.2}this is definitely a state of emergency."
        "Kouya tries to find the right words to appease him,{w=.2}\nbut they don't seem to be working."
        
        hide ka with wipe_right
        show su 010 at midleft
        show ka 005 at midright
        with wipe_right
        
        "I stand in front of Shun-kun, {w=.2}and bend down so\nI'm on the same level as him.{w} Then I slowly\nand deliberately talk to him to get him to calm down."
        fn "「Shun-kun, {w=.2}this doesn't mean I'm going away forever.{p}\ \ I can come back to see you anytime.{p}\ \ So don't make such a sad-looking face, {w=.2}okay? 」"
        su "「B-{w=.2}But {w=.2}I... 」"
        
        show ka 001 with dis
        
        ka "「Hey, {w=.2}you decided to send him of with a smile\n\ \ earlier, {w=.2}didn't you?{w} When you make a face like that,{w=.2}\n\ \ [fn] will worry and not be able to leave. 」"
        fn "「...When you put it that way,{w=.2}\n\ \ it sounds like I died and went to heaven. 」"
        
        show su 011 with dis
        
        su "「Woof, {w=.2}I-{w=.2}I did, {w=.2}didn't I... 」"
        "He wipes his eyes on his sleeve, {w=.2}looks at me with\nteary eyes, {w=.2}and attempts a smile.{p}{nw}"
        show ka 003 with dis
        extend "Seeing him like that, {w=.2}Kouya winks at me."
        "...Hmm, {w=.2}that was awfully quick-witted of Kouya to\nthink of using me to calm Shun-kun down."
        "I don't quite get it,{w=.2}\nbut it's still much better than a tearful good-bye."
        
        show su 008 with dis
        
        su "「Please, {w=.2}please come back! 」"
        fn "「I definitely will. {w=.2}I promise. 」"
        "I hold out my pinky finger towards him.{p}He does the same with his pinky.{w} Then we do a pinky\npromise."
        
        show su 005 with dis
        
        su "「We made a pinky promise!{p}\ \ You'll get a thousand needles if you break it! 」"
        fn "「Haha, {w=.2}how scary.{w} Now I have to come back. 」"
        
        show su 002 with dis
        
        su "「Yep! 」"
        "This time, Shun-kun's smile is as bright as the sun."
        
        if meet_ten == True: 
            
            show su 001 with dis
            
            su "「Oh, [fn]-san.{p}\ \ This was given to me. 」"
            "Shun-kun hands me a piece of paper.{p}Hm...? {w=.2}This feels like Japanese paper..."
            "And I've seen this way of folding before.{p}It's usually used in things like period dramas.{p}...For letters challenging you to a duel."
            "I timidly unfold it.{w} To overwhelm the person who\nsees it, {w=.2}the brushwork is powerful.{w} Just from that\nalone, {w=.2}I know this is from Ten-san."
            "\"Best regards.{p}Take care of youself\""
            "The simple words contrast the brushwork.{p}This really is a letter from Ten-san."    
        
        "Seeing that, a smile appears on my face.{p}Then I speak to Kouya, {w=.2}who's standing next to Shun-\nkun."
        fn "「Kouya, {w=.2}take care of yourself. 」"
        
        show ka 002 with dis
        
        ka "「I will. {w=.2}You do the same. 」"
        "We don't say much to each other,{w=.2}\nbut our exchange still feels like we care for each\nother.{w} When I look at Kouya's eyes, {w=.2}he nods once."
        
        scene bstop with wipe_right
        show to 001 at center with wipe_right
        
        to "「[fn], {w=.2}everything went well with you and\n\ \ senpai? 」"
        fn "「...Torahiko.{w} Yeah, {w=.2}a lot happened along the way,{w=.2}\n\ \ but Juuichi-san and I are now openly in love. 」"
        
        show to 007 with dis
        
        to "「...I see.{p}\ \ I guess it's really time for me to give up on going\n\ \ after you. 」"
        fn "「...Sorry. 」"
        
        show to 002 with dis
        
        to "「There's nothin' for you to apologize for,{w=.2}\n\ \ don't worry about it! 」"
        
        show to 001 with dis
        
        to "「If Juuichi-senpai gives you any trouble, {w=.2}come\n\ \ right to me!{w} I'll beat the crap out of him for\n\ \ you. 」"
        "...{p}I can only imagine Torahiko being thrown by Juuichi-\nsan, {w=.2}but that should be okay."
        
        show to 013 with dis
        
        to "「You turned me down,{w=.2}\n\ \ so now you have to be happy no matter what!{p}\ \ {nw}"
        show to at jump_up
        extend "Got it!? 」"
        fn "「Yep, I will.{w} Thank you, Torahiko. 」"
        
        hide to with wipe_right
        show si 004 at midleft
        show ta 005 at midright
        with wipe_right
        
        si "「...Playing around is nice and all,{w=.2}\n\ \ but the bus will be arriving soon. 」"
        ta "「Aww, {w=.2}already...? 」"
        "When I look, {w=.2}I see the bus approaching from the\nhorizon.{w} Just a bit longer and it'll be here.{p}I turn towards everybody again and bow my head."
        fn "「Everybody, {w=.2}I'm really thankful for everything you\ndid.{w} I was able to make some great memories.{p}\ \ I definitely won't forget about this summer. 」"
    
        show ta 010 with dis
        
        ta "「Hey, {w=.2}don't just make nice memories of us as you\n\ \ please. 」"
        fn "「Haha, {w=.2}sorry Tatsu-nii.{p}\ \ I just wanted to tell you that this was the best\n\ \ summer vacation I've ever had. 」"
        
        scene bstop with wipe_right
        show to 007 at midleft
        show ko 004 at midright
        with wipe_right
        
        ko "「I want to hear more stories about the city from\n\ \ you.{w} The next time you come here, {w=.2}I'm sticking to\n\ \ you like glue! 」"
        "An assult of questions from Kounosuke...{w=.2}\nI'm sure that'd last all day.{p}He doesn't care at all if I know or don't know."
    
        show to 003 at jump_up
        
        to "「Hey, {w=.2}he won't ever come back again if you tell him\n\ \ that! 」"
    
        show ko 001 with dis
        
        ko "「Really?{p}\ \ {nw}"
        show ko 002 with dis
        extend "Then I'll just stick to you in moderation! 」"
        "...There's something to be envied about Kounosuke's\nattitude of doing things at his own pace at times\nlike these."
    
        play sound car000 loop fadein 3
        
        "The old-fashioned bus pulls up--\ngets right beside me-- and stops.{p}It seems the time to depart has come."
        
        if meet_ten == True:
            jump juuichi30_goodbye_album
        else:
            jump juuichi30_goodbye_jacket

    #################################################
    label juuichi30_goodbye_album:
            
        $ event_name = "A Gift to Remember"
        
        scene bstop with wipe_right
        show ko 001 at center with wipe_right
        
        ko "「Oh yeah, here, [fn]. 」"
        "Hm, what's this?{p}I look at the blue-striped notebook he hands to me,{w=.2}\nand tilt my head to the side."
        ko "「I thought it'd be sad if you left without any\n\ \ souvenirs.{w} It's a collection of pictures of stuff\n\ \ like the village and everybody. 」"
        
        play sound2 paper00
        pause .5
        play sound2 paper00
        
        "I flip through the notebook."
        "Minasato's rice paddies.{p}A close-up of a bird.{p}The shrine's grounds."
        "The uncrowded park.{p}Lovely flowers."
        "With no permutations of relevance, {w=.2}photos of various\nplaces in Minasato are collected in the first half."
        "Photos of the welcoming party, {w=.2}the beach, {w=.2}and our\ncamping trip are lined up in the second half."
        "Each and every one of them feel like they're packed\nfull of memories of this summer."
        fn "「Kounosuke... 」"
        
        show ko 004 with dis
        
        ko "「Man, {w=.2}this was tough to put together, {w=.2}you know?\n\ \ I made this album just yesterday, {w=.2}and Juuichi-san\n\ \ treats his workers like crap...{w} {nw}"
        show ko 006 with dis
        extend "Ah. 」"
        
        show ko 005 with dis
        
        ko "「Um, {w=.2}well, {w=.2}yeah.{p}\ \ {nw}"
        show ko 002 with dis
        extend "Juuichi-san, {w=.2}I didn't mean it~ 」"
        "...{w} Kounosuke really is a \"do things at the last\nminute\" kind of guy.{w} Oh well, {w=.2}that's to be expected\nof him though."
    
        hide ko with wipe_right
        show ju 012 at center with wipe_right
        
        ju "「Kuri... I warned him not to say that. 」"
        fn "「Juuichi-san... 」"
        
        show ju 009 with dis
        
        ju "「I really should have made something myself,{w=.2}\n\ \ but so much was going on these last few days.{p}\ \ Besides, 」"
        
        show ju 004 with dis
        
        ju "「I said before that I was giving all my time to\n\ \ you, {w=.2}I'd never think of leaving you. 」"
        "Juuichi-san looks the other way in embarressment."
        fn "「Juuichi-san, {w=.2}just the thought is enough for me.{p}\ \ Thank you so much, {w=.2}I'll treasure it for the rest of\n\ \ my life. 」"
        ju "「...You're welcome. 」"
        "Then, {w=.2}an idea strikes him?{p}Juuichi-san walks up to me,{w=.2}takes off his jacket, {w=.2}and puts it on my shoulders."
    
        show ju 201 with dis
        
        fn "「...Juuichi-{w=.2}san?{p}\ \ What's this for? 」"
        ju "「It's going to get cold soon.{p}\ \ That's why I'm letting you borrow this.{p}\ \ ...Be sure to come back and return it. 」"
        fn "「...I will. 」"
        "Then he brings his face close to my ear,{w=.2}\nand whispers."
        
        show ju 209 with dis
        
        ju "「[fn]...{w} I love you. 」"
        fn "「I love you too.{p}\ \ More than anybody else in the world. 」"
        
        show ju 201 with dis
        
        "We stare at each other.{w} I reach out my hand to\nhis face, {w=.2}but stop myself at the last second.{p}We can't kiss in a place like this."
    
        play sound2 honking
        
        "The awfully high-pitched horn beeps at me.{p}I suddenly regain my senses,{w=.2}\nquickly pick up my bag, {w=.2}and board the bus."
        "Saying good-bye isn't necessary.{p}I show myself clutching his jacket tightly,{w=.2}\nand smile to him through the glass door."
        
        show ju 202 with dis
        
        "Juuichi-san smiles back at me.{p}It's the kind of gentle look that reassures me."
        
        hide ju with wipe_right
        stop sound fadeout 7.5
        
        "The bus slowly starts moving.{w} I hurry to the\nback seat, {w=.2}and wave through the window."
        "Everybody gradually gets smaller and smaller.{p}They get harder to see.{p}I still continue to wave though."
        
        scene black with wipe_right
        scene bus with wipe_right
        play sound traffic01 loop
        
        "Once everybody has disappeared,{w=.2}\nI finally face forward and sit down."
        "As if I'm hugging him,{w=.2}\nI squeeze his jacket that still has some of his\nwarmth on it."
        "As usual, {w=.2}it's well air-conditioned inside the bus.{p}In no time at all, {w=.2}the warm feeling is lost."
        "I'd be lying if I said that doesn't make me feel\nsad.{w} It's impossible for me to say I'm not lonely."
        "...However,{p}This summer I spent with everybody.{w} My memories of\nspending this summer with Juuichi-san."
        "Those won't disappear from me,{w=.2}\nnot in a million years."
        "I take the handmade album back of of my bag,{w=.2}\nand go through each photo one-by-one,{w=.2}\nso that they're burned into my eyes."
        
        play sound2 paper00
        pause .5
        play sound2 paper00
        pause .5
        play sound2 paper00
        
        "...Hm?"
        "My hand stops at the last page."
        "This must have been taken without me knowing about\nit.{w} In the picture, {w=.2}Juuichi-san and I are holding\nhands and talking with the lake in the background."
        "The photo is surrounded by a heart, {w=.2}and \"BE HAPPY!\"\nis written, {w=.2}emphasized with a double underline."
        "Kounosuke.{p}I'll lodge a complaint as soon as I go back there."
        "...\"Thank goodness I have such a bad friend\",{w=.2}\nI'll say."
        "I look down at the last photo.{p}In it, {w=.2}Juuichi-san and I are gazing at each other,{w=.2}\nwith smilies full of happiness."
        
        scene black with vsdis
        stop sound fadeout 2.5
        pause .5
        
        jump endings
    
    #######################################################
    label juuichi30_goodbye_jacket:      
        
        scene bstop with wipe_right
        show ju 001 at center with wipe_right
        
        ju "「...[fn]. 」"
        "Juuichi-san walks up to me,{w=.2}\ntakes off his jacket, {w=.2}and puts it on my shoulders."
    
        show ju 201 with dis
        
        fn "「...Juuichi-san? 」"
        ju "「It's going to get cold soon.{p}\ \ That's why I'm letting you borrow this.{p}\ \ ...Be sure to come back and return it. 」"
        fn "「...I will. 」"
        "Then he brings his face close to my ear,{w=.2}\nand whispers."
        
        show ju 204 with dis
        
        ju "「[fn]...{w} I love you. 」"
        fn "「I love you too.{p}\ \ More than anybody else in the world. 」"
        
        show ju 201 with dis
        
        "We stare at each other.{w} I reach out my hand to\nhis face, {w=.2}but stop myself at the last second.{p}We can't kiss in a place like this."
    
        play sound honking
        
        "The awfully high-pitched horn beeps at me.{p}I suddenly regain my senses,{w=.2}\nquickly pick up my bag, and board the bus."
        "Saying good-bye isn't necessary.{p}I show myself clutching his jacket tightly,{w=.2}\nand smile to him through the glass door."
        
        show ju 202 with dis
        
        "Juuichi-san smiles back at me.{p}It's the kind of gentle look that reassures me."
        
        hide ju with wipe_right
        stop sound fadeout 7.5
        stop music fadeout 7.5
        
        "The bus slowly starts moving.{w} I hurry to the\nback seat, {w=.2}and wave through the window."
        "Everybody gradually gets smaller and smaller.{p}They get harder to see.{p}I still continue to wave though."
        
        scene black with wipe_right
        scene bus with wipe_right
        play sound traffic01 loop
        
        "Once everybody has disappeared,{w=.2}\nI finally face forward and sit down."
        "As if I'm hugging him, {w=.2}I squeeze his jacket that\nstill has some of his warmth on it."
        "As usual, {w=.2}it's well air-conditioned inside the bus.{p}In no time at all, {w=.2}the warm feeling is lost."
        "I'd be lying if I said that doesn't make me feel sad.{p}It's impossible for me to say I'm not lonely."
        "...However, {w=.2}when I remember the three words Juuichi-\nsan told me with a bright red face, {w=.2}\"I love you\",{w=.2}\nit feels like I regain some of that warmth.."
        "Juuichi-san.{p}I voicelessly say the name of the person I love."
        "I take off his jacket, {w=.2}neatly fold it,{w=.2}\nand put it in my bag."
        "I look outside through my window.{w} Golden rice spreads\nfar and wide.{w} I'll probably never forget this scenery\nfor the rest of my life."
        "Juuichi-san.{p}My tiny, {w=.2}tiny whisper disappears into\nthe noise of the bus taking me back to ordinary life."
        
        scene black with sdis
        stop sound fadeout 1.5
        pause .5
        
        jump endings
    
#######################################################
