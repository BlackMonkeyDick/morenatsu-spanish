###Day 27
label day27:
    
    $ renpy.music.set_volume(1.0, 0.0, channel = "music")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound2")
    
    $ day = 27
    $ the_date = "August 27"
    $ event_name = "８月27日"
    
    if favorite == "kouya" or favorite == "shin":
        window hide
        play music birds_chirping
            
        scene sky01 
        show text "{size=+130}August 27" at truecenter
        with Dissolve(.5)
        
        pause 3
        scene black with Dissolve(1)
        pause .4
        
    else:
        jump day28
        
    $ renpy.jump (favorite + "27")
    
    
#########################################################
label kouya27:
    
    $ event_name = "Your Equipment is a Towel Bedsheet"

    scene black with dis    
    
    who "「...Hey.{p}\ \ Hey, [fn].{p}\ \ It's time for breakfast, wake up already. 」"
    "The pleasant dream world shook.{p}A voice calling out to came at the same time."
    fn "「Uu-uuhm... 」"

    scene bedroom with wipe_corner
    
    "Half-awake, I partially opened my eyes,\nand the world in front of me grew lighter.{p}Still, I already knew who was there."
    "I pushed myself up, despite my body's protests.{p}Then, as I rubbed my eyes,\nI spoke, somewhat groggily."
    
    show ka 001 at center with dis
    
    fn "「...Morning,{w=.2} Kouya. 」"
    
    play music daily03
    show ka 002 with dis
    
    ka "「Yeah,{w=.2} morning. 」"
    "Before long I started noticing various things.{p}Today is kind of cold."
    ka "「Breakfast is ready.{p}\ \ You should wash up before that, though. 」"
    fn "「Yeah,{w=.2} I will. 」"
    ka "「You should probably put something on, too.{p}\ \ If you keep on like that you'll catch a cold,\n\ \ even if it is summer. 」"
    fn "「Eh? Wha-! 」"
    "I was so surprised I couldn't voice anything coherent."
    "When I looked down at myself,\nI found myself wrapped in a bedsheet."
    "I was naked from the waist up.{p}Totally, completely naked."
    "If my self-consciousness were to be graphed,\nit'd start off relaxed, then suddenly spike up.{p}I thought my heart stopped for a second."
    "With that,{w=.2} the memories of\nlast night came flooding back."
    fn "「Ah... 」"
    "It was...{w=.2} Really embarrassing."
    "...Wait, now that I think about it,\nI'm not that dirty."
    "My left hand should be pretty sticky,\nif I recall properly.{p}Did Kouya clean me up...?"
    "When I thought about that,{w=.2}\nI got even more embarrassed."
    
    show ka 001 with dis
    
    ka "「What's wrong?{w} Not feeling well? 」"
    "Kouya looked at me with worry\nas I groaned and held my head."
    ka "「And sorry about yesterday.{p}\ \ {nw}"
    show ka 006 with dis
    extend "I guess, I overdid it... a bit. 」"
    "His approaching face was fearless, like last night.{p}I was a bit startled, and I shook my head in a panic."
    fn "「No, that's not true at all!\n\ \ I'm totally fine! Completely okay!\n\ \ A-anyway, I'll go wash! 」"
    
    show ka 010 with dis
    
    ka "「O-okay... 」"

    hide ka with wipe_right
    
    "I rapidly jabbered in one breath.{p}Kouya seemed a bit overwhelmed,\nand simply gave a slight nod."
    
    play sound step03
    scene black with wipeleft
    scene kouya_bathroom with wipeleft
    
    "Without really taking time to check myself,\nI ran over to the washroom as fast as I could."
    fn "「...Sigh... 」"
    "For now I should wash my face and cool my head off."

    play sound shower
    
    "When I turned the faucet, water poured out.{p}The shock of the cold water shot through me."
    "When people say 'refreshing',{w=.2}\nI guess this is what they mean."
    fn "「...Whew. 」"
    "After washing my face, I felt a lot calmer.{p}When I looked in the mirror,\nI looked the same as ever.{w} Yep, no problems there."
    "Only my naked dash to the washroom was strange.{p}Not that it's anything to kick up a fuss about."

    scene black with wipeleft
    scene bedroom with wipeleft
    
    "I went back into the room and had some breakfast,{w=.2}\nconsisting of toast, eggs,\nand some fried sausage wieners."
    "It's pretty simple, but Kouya's cooking\nis as good as usual."
    
    show ka 001 at center with dis
    
    fn "「Thanks for the meal. 」"
    
    show ka 002 with dis
    
    ka "「Nah,{w=.2} it's nothing special. 」"
    fn "「Hey,{w=.2} when does practice start today? 」"
    "I asked Kouya as I sat down at the table.{p}When I looked at the clock, it just hit 7:43.{p}We woke up pretty early today."
    
    show ka 001 with dis
    
    ka "「Hm?{w} We'll be meeting up at 10.\n\ \ Same as usual. 」"
    fn "「Then we have plenty of time.{p}\ \ What should we do? 」"
    ka "「Let's see...{p}\ \ Maybe we'll just go early.{p}\ \ You okay with that? 」"
    fn "「Yeah,{w=.2} it's fine with me. 」"
    ka "「Well, that's decided.{p}\ \ {nw}"
    show ka 003 with dis
    extend "Let's get things back on track. 」"
    
    stop music fadeout 3
    scene black with sdis  
  
    $ event_name = "Hop, Step--"

    scene studio with sdis    
    play music free0211
    show ka 005 at midleft
    show ke 003 at midright
    with dis
    
    ke "「...I see. Man, it looks like\n\ \ everyone's on the same page today. 」"
    ke "「Too bad for you, Kouya-kun...{p}\ \ I didn't even need to say anything. 」"
    ka "「Guh...! 」"
    fn "「Ahahaha... 」"
    "We had left the house immediately.{p}We'd torn down the peaceful morning roads,\nprobably breaking some laws."
    "We got here easily enough,{w=.2}\nbut someone had beaten us to it..."
    "Just like Keisuke-san said,\nit looked like everyone was thinking the same thing.{p}So, in other words..."

    show yu 002 at farleft
    show jn 001 at farright
    with dis
    
    yk "「Well, looks like everyone is here,\n\ \ so we may as well start practice already. 」"
    jn "「... 」"
    "...We planned on being the first ones here,\nand we ended up the last ones to get here."
    fn "「Still,{w=.2} it's amazing that everyone\n\ \ thought the same thing and came here early.{p}\ \ It's like you're all on the same wavelength. 」"

    show ke 006 at jump_up
    
    ke "「You think so too, [fn]?{p}\ \ I think everyone here has\n\ \ the same sense of commitment. 」"
    
    show ke 008 with dis
    
    ke "「Like club members, or something?{p}\ \ Seems as if we're all tied together by destiny! 」"
    "Keisuke-san shook his fist for emphasis.{p}In contrast to that, everyone else looks composed."
    
    show ka 001 with dis
    
    ka "「Looking at you make that face\n\ \ and treating us like club members\n\ \ makes me kind of sick. 」"
    
    show yu 001 with dis
    
    yk "「No objections here. 」"
    ke "「You guys are cooold.\n\ \ But you two back me up, right?{w} Jun? [fn]? 」"
    
    show jn 006 with dis
    
    jn "「... 」"
    
    show ke 004 with dis
    
    ke "「Hey, aren't you even going to look at me?{p}\ \ {nw}"
    show ke 005 with dis
    extend "W-what now, [fn]?{w=.2}\n\ \ Looks like it's down to us two. 」"
    fn "「Since it's still early in the day,\n\ \ I'd like to say 'no comment'. 」"
    
    show ke 004 with dis
    
    ke "「Tch, I have to hurry and turn this around...!{p}\ \ {nw}"
    show ke 001 with dis
    extend "Fine, whatever!{p}\ \ Let's hurry up on start with practice, ya mooks! 」"
    
    play sound bosu10_a
    pause .2
    play sound bosu10_a
    
    "Keisuke-san bellowed out as he banged on his drums.{p}The other three responded appropriately\nas they picked up their instruments."
    
    stop music fadeout 3
    show ke 006 with dis
    
    ke "「Right, everyone, let's put everything we've\n\ \ got into this morning!{p}\ \ Now, continuing on from yesterday...! 」"

    scene studio with wipe_right
    pause .4
    play music melodious04
    
    "Keisuke-san set the rhythm,\nand Kouya and Jun-kun soon joined in.{p}Right afer that, Yuuki-san's voice rung out."
    "It came together as one beautiful melody."
    "Still, it feels like things today sound... Different.{p}I couldn't tell you how, though."
    "It's just that the mood has changed somehow.{p}At least, that's how I saw it."
    "...Could it be that everyone's\nhaving more fun than usual...?"
    "When I look at Keisuke-san,{w=.2} Yuuki-san,{w=.2} Jun-kun,{w=.2}\nand finally Kouya, I get that sort of impression."
    "Just maybe, it could be that everyone's\ntrying to move past yesterday's incident."
    "Everyone should be under a lot of pressure.{p}Normally, people would feel like they're cornered,{w=.2}\nbut did they manage to get past that?"
    "I'm not familiar with this, so I don't really know.{p}But everyone does seem to be enjoying the sounds:\nThey're making 'music'."
    "That's what I gather from their expressions."
    "But even with me just watching and listening,{w=.2}\nI was having a lot of fun,\nso it has its own special charm to it."
    "The song was resonating with my heart.{p}It was a strange sensation,\nlike the sound in the air was mixing in with me."
    "It gave me goosebumps."
    
    stop music fadeout 3
    
    "It's completely overwhelming.{p}After a moment I realized it was quiet."
    fn "「That was... awesome, wasn't it? 」"
    "Those were the words I eventually came up with.{p}Now that I've said them, I feel kind of stupid."
    
    play music melodious02
    show ka 002 at midleft
    show ke 002 at midright
    show yu 001 at farleft
    show jn 006 at farright
    with dis
    
    ke "「Yeah, seems like everyone's in a good mood today. 」"
    yk "「Yep. You can't even compare this to yesterday.{p}\ \ It feels like we've got our real style back.{p}\ \ I was feeling pretty good too while I was singing. 」"
    
    show jn 007 with dis
    
    jn "「...Kouya's back to his normal self. 」"
    
    show ke 006 with dis
    
    ke "「Oh yeah, that's true!{w} How do I say this?\n\ \ Yesterday, it was like you were someone else. 」"
    
    show ke 008 with dis
    
    ke "「But then today's performance happened.{p}\ \ It was scary, really scary I tell you.{p}\ \ Our Kouya's finally come back! 」"
    
    show yu 001 with dis
    
    yk "「Ah, I think I get what you're trying to say. 」"
    "Everybody was speaking excitedly.{p}Even the normally silent Jun-kun was in our circle,{w=.2}\nso all of them probably thought it was a good run."
    ke "「Anyway, I wanna ask about what happened.{p}\ \ It's weird for Kouya to be in a good mood.\n\ \ What's with this sudden shift? 」"
    
    show ke 003 with dis
    
    ke "「Something happened, didn't it, lover boy? 」"
    "Everyone's eyes shifted to Kouya.{p}As he was the center of attention,\nKouya opened his mouth slowly."
    
    show ka 003 with dis
    
    ka "「Didn't I say earlier?{w} I'll tell you later. 」"
    "Kouya was laughing like a kid\nwho'd just pulled off a prank,\nand it reminded me of the sun."
    "It was just so brilliant."
    "That smile made me feel quite happy myself.{p}Everyone laughed heartily."
    
    stop music fadeout 3
    scene black with sdis 
   
    $ event_name = "-Jump"

    play music free04

    scene studio with sdis
    
    "Practice today ended a bit early for two reasons."
    "First, due to tomorrow being the big day,\nan early leave would allow us to rest up for it."
    "The second reason is because we wanted to finish\non a high note, before anything went wrong."
    "From the beginning to the end,\ntoday's practice went really well.{p}Everyone was smiling the whole way through."
    "「If we keep at it like this,\nwe might even make the Grand Prix! 」{w=.2}\nor so Yuuki-san said during the day."
    "I thought so too after hearing them play.\nEveryone really is amazing."
    "The place they all had their eyes on.{p}It's not just a dream any more."
    "With all their work they've put in,\nif they reached out, they'd be able to get it.{w=.2}\nThe goal they've firmly believed in."
    "All that's left is to charge at full speed,\nstruggle our way through,{w=.2} and grab the goal."

    show ka 001 at midleft
    show ke 001 at midright
    with dis
    
    ke "「All right you two, don't be late tomorrow.{p}\ \ And don't oversleep like yesterday. 」"
    ka "「Those should be my lines. 」"
    
    show ke 003 with dis
    
    ke "「Hmhmhm, no problem. I'm going straight to\n\ \ bed when I get home.{w} And then, since I'm having\n\ \ Yuuki wake me in the morning, it's all okay. 」"
    
    show ka 005 with dis
    
    ka "「And which part of that is okay? 」"
    ke "「Hey, it's not like I've made any mistakes!{p}\ \ Anyway, I'm going home. I'll leave the\n\ \ locking up to you.{w} {nw}"
    show ke 006 with dis
    extend " Good job today! 」"
    
    show ka 001 with dis
    
    ka "「Yeah,{w=.2} good job. 」"
    fn "「Thanks for all your hard work. 」"

    scene studio with wipe_right
    show ka 001 at center with wipe_right
    
    "Keisuke-san left the studio,{w=.2}\nfollowing after Yuuki-san and Jun-kun,\nwho'd already left.{w} The only ones left were us."
    fn "「...Tomorrow's the big day. 」"
    "I talked to Kouya\nas he was adjusting his guitar."
    "When I spoke again,{w=.2}\nI felt a strange tension inside of me.{p}...At long last, the day has finally come."
    ka "「Yeah... 」"
    "In contrast to me,{w=.2} the one who's\nactually going to be on stage looks calm.{p}It's kinda of strange for me to be nervous then."
    fn "「You seem fine.{p}\ \ You look the same as usual,\n\ \ not nervous at all. 」"
    
    show ka 002 with dis
    
    ka "「No way.{w=.2} Of course I'm nervous.{p}\ \ Whatever happens tomorrow determines everything\n\ \ afterwards.{w} There's no way I wouldn't be nervous. 」"
    fn "「Well, I guess that's true.. 」"
    "I couldn't follow up on that.{p}Only the sounds of Kouya's work filled\nthis quiet studio."
    "My heart started pounding loudly in the silence.{p}I could calm down if I had something to talk about."
    "However, nothing came to mind."
    fn "「Uuu... 」"
    "Maybe I'll just groan for now."
    
    show ka 001 with dis
    
    ka "「What are you moaning about?{p}\ \ You aren't some animal. 」"
    "He cut into it so naturally."
    fn "「It's just that I can't really calm down\n\ \ if I'm not doing anything.{p}\ \ Man,{w=.2} I probably won't be able to sleep tonight... 」"
    
    show ka 005 with dis
    
    ka "「You aren't a kid, so just stop that.{p}\ \ I won't get to sleep either,\n\ \ if you're going to toss and turn next to me. 」"
    
    play sound tyakuO
    
    "Kouya kept working as he replied.{p}It seems as if the guitar is done with now.{p}...Hm?{w} Hey, wait a sec."
    fn "「Eh?{w=.2} I'm sleeping in the same bed as you tonight? 」"
    
    show ka 001 with dis
    
    ka "「You don't want to? 」"
    fn "「Actually,{w=.2} I've been hoping for that.{p}\ \ But now, I'm even less sure I'll be able\n\ \ to sleep tonight... 」"
    "My heart rate will be several times faster after all."
    ka "「Then tonight you'll sleep in the futon. 」"
    fn "「No, no, the bed is fine. 」"
    ka "「Then calm down, already.{p}\ \ It's not like we can help being restless. 」"
    
    play sound freeze04
    
    fn "「I-{w=.2}I'll do my best! 」"
    
    show ka 005 with dis
    
    ka "「...Whatever, it's about time we left.{p}\ \ Now hold onto this.\n\ \ I don't feel like carrying it today. 」"
    
    play sound bosu10_a
    
    "Kouya put the guitar he was tuning back\ninto its case, and handed it over to me."
    fn "「...S-since you're using it tomorrow,\n\ \ you're bringing it home? 」"
    ka "「Yeah.{w=.2} It's been working really well today.\n\ \ I think it's best not to change it. 」"
    fn "「I see. 」"
    "I put on the strap for the soft case,\nthen tightened it so it wouldn't swing around freely."
    
    show ka 001 with dis
    
    ka "「Mm,{w=.2} looks okay.{p}\ \ Come on, let's go. 」"
    "After checking on it, Kouya started walking.{p}I followed him out of the studio."
    
    stop music fadeout 3
    hide ka with wipe_right
    scene black with wipe_right
    scene kazenari01 red with wipe_right
    
    "When we got outside, the sun was already\nbeginning to set.{w} Over in the west,\nthe sky was streaked with red."

    scene black with wipe_right
    scene runway1 red with wipe_right
    play sound load_gun
    pause 1.5
    play sound motor_engine
    
    "I held onto Kouya's back, looking up at the sky\nas the bike moved down the roads."
    "The vermillion red of the setting\nsun soon gave way to a blueish black."
    "It felt kind of lonely.{p}Night would be arriving soon."

    scene black with wipe_right
    scene runway1 night with wipe_right
    
    "Even though the noises around us\ngradually faded into the peaceful darkness,{w=.2}\nmy heart was still thumping loudly in my chest."
    "Even when I took a deep breath,\nit didn't seem to help much."

    scene black with wipe_right
    scene shrine_stairs night with wipe_right
    
    "The bike stopped not long after\nmy failed attempts to calm myself."
    "However,{w=.2} we weren't at Kouya's apartment.{p}The engine stopped."

    play sound night_insects loop
    show ka 001 night at center with dis
    
    fn "「Kouya? 」"
    "I asked him as he faced forward.{p}Why were we here?"
    ka "「I was thinking it's a bit too early for dinner,\n\ \ so we're stopping by here. Come on, get off. 」"
    
    play sound2 bosu34
    
    "I stepped off the bike as Kouya urged me on.{p}The air here was quite still."
    "Looking forward, the stone\nsteps seemed to extend into the sky."
    
    play sound2 step01
    
    "Kouya ascended them one by one.{p}I followed along after him."

    scene black with wipe_right
    scene shrine_court night with wipe_right
    
    "At the top was Minasato Shrine.{p}Last time we were here, it was the Summer Festival."
    "Kouya briskly walked over to the smaller shrine."
    fn "「Praying? 」"
    
    show ka 001 night at center with dis
    
    ka "「Kind of. It's tradition.{p}\ \ The day before a contest, I always come here. 」"

    hide ka with dis
    play sound2 coin02
    
    "Kouya pulled out some coins,\nand tossed them into the offering box.{p}I followed his lead, confused."

    play sound2 shrine_bell
    
    "We both shook the cord hanging from the ceiling,\nand the sound of bells rung out.{p}{nw}"
    play sound2 explosive
    pause .5
    play sound2 explosive
    extend "Then came the customary two bows and two claps."
    "However, I haven't thought\nof the crucial part: My wish.{p}For now, I'll take whatever pops into my mind."
    "When I opened my eyes Kouya,\nseemed to be done with his prayer,{w=.2}\nso the two of us bowed together and left."
    
    show ka 002 night at center with dis
    
    ka "「...All right,{w=.2} ready to head back? 」"
    fn "「Yeah. 」"
    ka "「Hey,{w=.2} [fn]. 」"
    fn "「Hm? 」"
    
    play music free60
    show ka 001 night with dis
    
    ka "「Do you think we can win the Grand Prix tomorrow? 」"
    "Just after we'd started walking, Kouya spoke up.{p}I stopped moving without really thinking about it."
    ka "「Just so we're clear,\n\ \ it's not like I'm not confident.{p}\ \ I'm going in with my best shot, and I intend to win. 」"
    ka "「But I want to hear your thoughts on it.{p}\ \ Do you think we can win tomorrow? 」"
    "Kouya's eyes were fixed straight through me.{p}He didn't waver,{w=.2} and I could feel the\ndetermination pouring out of his eyes."
    "I looked back at him with the same expression.{p}Right now, I'm not hesistating.{p}So I made my declaration."
    fn "「Yes.{w} I was thinking that at practice today.{p}\ \ Everyone was having so much fun playing. 」"
    fn "「It's like everyone really loves doing it.{p}\ \ ...It's possible, if it's you guys.{p}\ \ If you love music, then they'll definitely respond. 」"
    "Those words came straight from my heart.{p}None of it was a lie, all of it was true."
    ka "「... 」"
    "Kouya said nothing.{p}{nw}"
    show ka 002 night with dis
    extend "He just laughed, as if satisfied by my answer."
    ka "「Yeah,{w=.2} that's it. 」"
    fn "「Kouya...? 」"
    "Since I didn't understand where\nhe was going with this, I was taken aback."
    "However, that only lasted a moment.{p}A moment later, Kouya answered my unvoiced question."
    
    show ka 001 night with dis
    
    ka "「I was thinking about things last night,\n\ \ before I went to sleep.{p}\ \ 'Why am I playing so badly?' and things like that. 」"
    ka "「It was simple.{w} I was rushing, plain and simple.{p}\ \ Until today, I kept going until it all fell apart. 」"
    ka "「I thought I had to do something about that.{p}\ \ I think that was the cause of it all. 」"
    ka "「I used to think the cause of it all was my promise.{p}\ \ But actually, it's a little different.{p}\ \ That was only part of it. 」"
    ka "「It's true, the promise is weighing heavily on me.\n\ \ But really,{w} it seemed as if I couldn't enjoy playing\n\ \ the guitar any more.{w} At least, it felt like that. 」"
    ka "「Even though it's something I like doing,{p}\ \ before I knew it I felt like I had to move on,{w=.2}\n\ \ that I was doing something I shouldn't be. 」"
    ka "「And then I got worse.{w=.2}\n\ \ I stopped doing something I wanted to do. 」"
    
    show ka 013 night with dis
    
    ka "「That's why today, I was only thinking\n\ \ about having fun like I used to.{p}\ \ I put aside everything else, like the contest. 」"
    
    show ka 001 night with dis
    
    ka "「Once I did that, I got better.\n\ \ I forgot something I knew from the very beginning.{p}\ \ I forgot that I just wanted to have fun. 」"
    
    show ka 002 night with dis
    
    ka "「It's just as you said, [fn].\n\ \ If I like it, then the music will respond.{p}\ \ I won't lose sight of that ever again. 」"
    "Kouya took a step forward towards me.{p}{nw}"
    scene black with sdis
    extend "And then, he slowly hugged me."
    ka "「So relax.{p}\ \ You don't need to be all panicky. Just take it easy.{p}\ \ Tomorrow, I'll win for sure. 」"
    ka "「I-{w} we can be counted on. Just you wait. 」"
    "He turned me around,{w=.2} and pulled me in close.\nI finally started to calm down a little."
    "It's just like Kouya said.{p}What am I nervous about?{w=.2}\nWhat am I worrying about?{w=.2} And why am I panicking?"
    "I don't need any of that."
    "I know everyone can play well if they enjoy it,{w=.2}\nand even though I said they could win,{w=.2}\nI didn't really have faith in my statement."
    "That's why I was getting all worked up.{w=.2}\nIt's so stupid."
    "I don't need to worry about anything.{p}Everyone will win.\nThey have all the ability they need."
    "If that's the case,{w=.2}\nall I need to do is watch."
    "That's why I couldn't see that Kouya was nervous.{p}He knew perfectly well what he should do,\nand he believed in that."
    "Kouya isn't at a loss.{p}That's why he seems to be the same as ever.{p}It was something plain and simple."
    "Now I have to follow his lead.{p}I came to see everyone, Kouya especially,\nso what'll I do if I don't believe in it?"
    fn "「Kouya... 」"
    "I put my own arm around Kouya,\nand held him close to me.\nThat was my own answer."
    ka "「Tomorrow, we'll win for sure. 」"
    fn "「Yeah... 」"
    "After that, we said nothing.{p}There was no need for words."
    "Everything will be decided tomorrow.{p}Of all the paths in front of us,\nthere's now only one road."
    "Right now, we just can't see that far ahead.{p}The path's obscured so we can't tell where it leads,\nand right now there's no one who can tell us."
    "But over there, I can hear the sound\nof tears from someone I know very well.{p}I'm sure that those would be tears of happiness."

    jump end27
    
#########################################################    
label shin27:
    
    $ event_name = "Onward to Shin's House"
    
    $ renpy.music.set_volume(0.8, 0.0, channel = "music")

    scene hbroom with dis
    
    "The next day, I was still in my room.{p}I remembered Amaki-san's words from yesterday.{p}What Shin-kun needed was a friend like me."
    
    if shin_normalend == True:
        jump shin27_normalend
    else:
        jump shin27_house

    #########################################################
    label shin27_normalend:
            
        $ event_name = "Shattered Determination"
        
        stop music fadeout 1.5
        
        "...{w} but...{p}The determination I had yesterday is faltering.{p}Will anything really happen if I go?"
        
        play music piano4_001
        
        si "「Don't make a promise you can't keep! 」"
        "What Shin-kun had shouted still rung in my ears.{p}Just what can I do with Shin-kun?"
        si "「Aren't you supposed to be going soon? 」"
        "Right, I have to leave Minasato soon.{p}Even if I go now,\nit just doesn't seem like enough time."
        si "「You just simply tell someone you love them,\n\ \ but do you understand\n\ \ how much that can hurt people!? 」"
        "Even if I do go, won't I just hurt him again?\nEven if I could keep that from happening,{p}what could I say...?"
        si "「{cps=5}I'm begging you,{w=.2} don't come here anymore. 」"
        "Just what am I to Shin-kun?{p}What is Shin-kun to me?{p}I don't know. {w=.2}I just don't know."
        "As I kept thinking about it,\nmy determination was replaced by anxiety."
        "But,{w=.2} at this rate I won't be able\nto see Shin-kun again in all likelihood."
        "Still,{w=.2} even if I see him what should I do...?{p}My thoughts kept cycling {w=.2}and cycling{w=.2} and cycling."
        "Even if we broke ties,\nthat had always stayed in my mind."
        
        scene black with sdis
        
        "That kept going, and I never came to a decision.{p}Time just passed, and another day ended,{w=.2}\nand when I noticed there was no time left."
        
        stop music fadeout 1.5
        pause 1.5
        
        $ event_name = "Farewell"
        
        scene bstop with dis
        play music melodious02
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        
        "The day summer vacation ends.{w} I went\nto the bus stop leaving behind unease and regret,\nand everyone was waiting there."
        "Shin-kun too...{w} As I exchanged awkward greetings,\neveryone's bright faces cheered me on\nand gave words of parting."
        "Torahiko grabbed me,\nTatsu-nii lifted me up,\nand just like that the bus had arrived."
        
        show su 004 at farleft
        show to 003 at center 
        show ko 001 at farright
        with wipe_right
        
        to "「It's just about time.{p}\ \ {nw}"
        show to 001 with dis
        extend "So once again,{w=.2} take care [fn]. 」"
    
        show ko 003 with dis
        
        ko "「Take care.{p}{nw}"
        show ko 002 at jump_up
        extend "Next time you come back,\n\ \ I'll be looking forward to the souvenir stories. 」"
        su "「[fn]-san...{nw}"
        show su 010 with dis
        extend " this really is lonely.{p}\ \ {nw}"
        show su 008 at jump_up
        extend "B-but I'm not crying!{w=.2}\n\ \ {nw}"
        show su 001 with dis
        extend "Please take care even when you're going home. 」"
        
        scene bstop with wipeleft
        show ta 002 at farright
        show ky 001 at center 
        show so 001 at farleft
        with wipeleft
        
        ta "「Don't cry just because we\n\ \ can't see each other anymore!{p}\ \ {nw}"
        show ta 006 with dis
        extend "Don't...{w=.2} even...{w=.2} cry... 」"
    
        show ky 003 with dis
        
        ky "「Come on, it means nothing if you cry too Tatsuki-san. 」"
    
        show ta 009 at jump_up
        
        ta "「S-shut up!{w} {nw}"
        show ta 006 with dis
        extend " Who's crying!? 」"
    
        show so 006 with dis
        
        so "「I wanted to talk more,\n\ \ but it's already time to go... 」"
    
        show so 003 with dis
        
        so "「I'm lookin' forward to the next time we meet!{w=.2}\n\ \ Stay healthy until then! 」"
    
        show ky 001 with dis
        
        ky "「See you. Take care of yourself. 」"
        
        scene bstop with wipeleft
        show si 001 at farright
        show ka 001 at center
        show ju 001 at farleft
        with wipeleft
        
        ka "「Be careful.{p}\ \ {nw}"
        show ka 003 with dis
        extend "Even if you're going back, stay happy. 」"
        ju "「Well, {w=.2}I can't say anything clever, so take care.{p}\ \ {nw}"
        show ju 004 with dis
        extend "Come back anytime. 」"
        si "「...{p}\ \ Take care,{w=.2} [fn]. 」"
    
        scene bstop with wipeleft
        
        fn "「Thanks guys.{p}\ \ Shin-kun, uh... 」"
    
        show si 001 at center with dis
        
        si "「Hm? 」"
        fn "「Good luck with {w=.2}the overseas school. 」"
        si "「...{p}\ \ {nw}"
        show si 002 with dis
        extend "Did you hear that from Amaki? 」"
        fn "「...yeah. 」"
        
        show si 001 with dis
        
        si "「I see.{p}Still, I haven't decided yet.{p}\ \ I'm deciding after this. 」"
        fn "「I-{w=.2}I see then. 」"
    
        show ko 006 at farright behind si with dis
        
        ko "「Huh?{w=.2} What's this about school? 」"
    
        show to 003 at farleft behind si with dis
        
        to "「I haven't heard anything like that. 」"
        
        show si 004 with dis
        
        si "「Hmph.{p}\ \ Look, isn't it because you're talking about\n\ \ that here that the peanut gallery is swelling? 」"
        fn "「S-sorry. 」"
    
        scene bstop with wipeleft
        
        "As Shin-kun was being asked by everyone around,\nhe looked a bit annoyed\nas he explained the situation."
        "That was unmistakably the Shin-kun\nI know so well."
    
        play sound honking
        
        "At that time, the bus finally came."
        fn "「Oh, well see you guys.{p}\ \ Later! 」"
    
        show to 001 at center with dis
        
        to "「Y-yeah.{w=.2}{nw}"
        show to 002 with dis
        extend " Come again sometime! 」"
        stop music fadeout 3
        play sound auto_door
        scene black with sdis
        play sound2 bus_idling
        pause 3
        play music melodious01
        scene bus with dis 
        
        "The bus started to move,\nand everyone out the window started chasing after.{p}Torahiko rapidly waved his right arm."
        "Kounosuke waved both of his arms.{p}Kouya waved moderately,{p}and Juuichi-san looked taciturn."
        "Tatsu-nii and Shun-kun cried together.{p}Kyouji-sempai was looking calm,\nSoutarou looked cheerful..."
        "Everyone was seeing me off.{p}Shin-kun too had a shocking smile on his face\nas he waved his little hand."
        "Shin-kun will be fine, {w=.2}right?{w} After\nasking that in my head, I kept waving my hand\nout the window until I couldn't see them anymore."
        "So much happened, but it's really good\nI'm going home.{w} I'm sure I'll never forget\nthe memories of this summer!"
        "So, I'll definitely come back again..."
        "Until then, everyone take care too!"
        "As I tried to hold onto the feelings\nboiling up, I ended up yelling as loud as I could.{p}Summer was soon meeting its end."
    
        stop music fadeout 1.5
        stop sound2 fadeout 1
        play sound truck
        scene black with sdis
        pause 6
    
        jump endings
    
    #####################################################
    label shin27_house:
        
        "...alright, let's go.{p}I reconfirmed my feelings,\nthen headed out to Shin-kun's house."
        
        stop music fadeout 1.5
        scene black with sdis
        play music cicada01
        scene shin_house_front with sdis
        
        "It's been a few days since I've seen it,\nand once again I was in front\nof the door I should be used to."
        "I don't know how things will go.{p}But I've come this far, so I have to keep going.{p}I steeled myself, and pressed the intercom."
        
        play sound tm2_chime002
        pause 2
        
        am "「Yes, who might this be? 」"
        fn "「This is [ln].{w} Is Shin-kun available? 」"
        am "「Oh, it's you.{w=.2} I'll open the door now 」"
        "..."
        
        play sound tm2_chair003
        pause 1
        show am 002 with dis
        
        am "「Good afternoon.{w} So you've come. 」"
        fn "「Yes. {p}\ \ ...where's Shin-kun? 」"
        
        show am 001 with dis
        
        am "「He's in his room.{p}\ \ I'll take you there, so please come along. 」"
        fn "「Pardon the intrusion. 」"
    
        stop music fadeout 1
        scene shin_house_den
        show am 001 at center
        with sdis
        show am 004 with dis
        
        am "「...thank you, {w=.2}for coming. 」"
        fn "「...yes. 」"
        
        scene black with wipeleft
        scene shin_bedroom
        show si 001 at midright
        with wipeleft
        play music free0211
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        play sound door_knock
        pause 2
        play sound Door03Open
        pause 1
        show am 001 at midleft with dis
        
        am "「Shin-kun, can I come in? 」"
        si "「...{w=.2}so am I just imagining you already in here? 」"
        
        show am 002 with dis
        
        am "「Haha, don't be so stuffy. 」"
        
        show si 004 with dis
        
        si "「... 」"
        
        show am 001 with dis
        
        am "「A friend came over. 」"
        
        show si 001 with dis
        
        si "「A friend? 」"
        
        show si 005 with dis
        
        fn "「H-hi. 」"
        
        show si 009 with dis
        
        si "「[fn]... 」"
        
        show am 002 with dis
        
        am "「Okay, I'll be going downstairs now. 」"
    
        hide am with wipe_right
        pause 2
        show am 001 at midleft with wipe_right
        
        am "「Oh yes.{p}\ \ I told him about the technical school. 」"
        
        show si 005 with dis
        pause .4
        show si 012 with dis
        
        si "「Amaki! 」"
        am "「Weren't you going to tell him anyway?{p}\ \ {nw}"
        show am 002 with dis
        extend "Oh, was it wrong for him to hear it from me first? 」"
        
        show si 009 with dis
        
        si "「... 」"
        
        show am 001 with dis
        
        am "「Now then, I'll be downstairs.{p}\ \ If you need anything, just call for me. 」"
    
        hide am with dis
        
        am "「(Hang in there.) 」"
        "On the way out, Amaki-san whispered\nthat into my ear."
        
        stop music fadeout 2
        play sound DoorCloseB 
        pause 2
        show si 009 at center with dis
        
        si "「... 」"
        "What should I say first?{p}As I smiled politely in the awkward mood,\nI broke the ice."
        
        play music free58
        
        fn "「...sorry.{w=.2}\n\ \ I came over again. 」"
        si "「... 」"
        fn "「Are you mad? 」"
        
        show si 001 with dis
        
        si "「...{w} {nw}"
        show si 009 with dis
        extend "not really. 」"
        "Shin-kun looked away as he said that."
        fn "「Is it true you're going to an overseas school? 」"
        si "「Not yet, I haven't decided. 」"
        fn "「... 」"
        "I was almost carelessly overwhelmed by\nthe increasingly cold attitude,\nbut I somehow managed to work up the next words."
        fn "「What do you want to do Shin-kun? 」"
        
        show si 001 with dis
        
        si "「Eh? 」"
        fn "「Didn't you say so before?{p}\ \ That you wanted to leave making sweets a hobby.{p}\ \ Unless, you seriously are aiming to be a patissier? 」"
        
        show si 009 with dis
        
        si "「That's... 」"
        fn "「I can't really say it all\n\ \ that well,{w=.2} but,{w=.2} I think it's\n\ \ wrong to lie to your own feelings. 」"
        si "「...{p}\ \ You...{p}\ \ {nw}"
        show si 012 with dis
        extend "Don't speak like you know anything about me! 」"
        fn "「But... 」"
        
        $ event_name = "The Word He Desires"
        
        show si 005 with dis
        
        si "「Ah... 」"
        "Even without saying anything, Shin-kun should\nknow best.{w} The moment he shouted, the\ntransparent falling drops made everything clear."
        
        show si 008 with dis
        
        si "「No.{w} This, {w=.2}I, {w=.2}no,{w} why...? 」"
        fn "「Shin-kun, won't you say it outright?{p}\ \ A little bit is fine, just tell me your feelings. 」"
        si "「This is... my problem.{p}\ \ You...{w=.2} aren't involved. 」"
        
        scene shin_bed
        show si 008 at center 
        with sdis
        
        "Like the tears he tried to wipe\nas he sat on the bed,\nShin-kun's words shot off bit by bit."
        fn "「I'm not uninvolved!{p}\ \ I've always worried about you----! 」"
        
        play sound bosu31
        show si 012 with dis
        
        si "「You're so shameless! 」"
        fn "「！！ 」"
        
        show si 008 with dis
        
        si "「So please, {w=.2}just leave me alone. 」"
        fn "「...{w} I can't leave you alone. 」"
        si "「Why...? 」"
        fn "「Because, {w=.2}isn't it obvious? 」"
        
        show si 009 with dis
        
        si "「Because we're friends? 」"
        fn "「There's that,{w=.2} but... 」"
        fn "「It's because you're important to me.{w=.2}\n\ \ Is that so wrong? 」"
        
        show si 006 with dis
        
        si "「！ 」"
        
        show si 012 with dis
        
        si "「Don't just...! 」"
        
        show si 008 with dis
        
        si "「Don't just...{w=.2} say things like that! 」"
        "And just like that, Shin-kun fell silent again."
        fn "「I can't stand watching you like this... 」"
        si "「... 」"
        fn "「If anyone tried holding up that much,\n\ \ won't they break?{p}\ \ If you don't have faith in me, that's fine. 」"
        fn "「At least speak properly to Amaki-san or someone else! 」"
        
        play sound bosu35
        show si 012 with dis
        
        si "「I can't do that!{p}\ \ {nw}"
        show si 009 with dis
        extend "I... 」"
        "After that I couldn't hear anything.{p}Shin-kun trembled as he took deep breaths,\nand I could see he was trying to soothe himself."
        "I waited until he said something again.{p}How long would I have to wait?{p}Bit by bit,{w=.2} Shin-kun started talking again."
        si "「I...{w=.2} I wanted to say I hate you. 」"
        fn "「Why...?{p}\ \ Because you hate me? 」"
        si "「...{w} it's the opposite. 」"
        fn "「The opposite? 」"
        si "「...{w=.2}I have always loved you.{p}\ \ Maybe, ever since we were little. 」"
        si "「I've been hanging onto yearning\n\ \ and liking for you. 」"
        fn "「Wha... 」"
        si "「Holding those kinds of feelings for someone of\n\ \ the same sex one-sidedly is disgusting, isn't it.{p}\ \ I didn't understand my own feelings either. 」"
        si "「But,{w=.2} after spending time with you this summer\n\ \ I realized that I liked you more than a friend,{w=.2}\n\ \ it was those kinds of feelings. 」"
        fn "「Then...{p}\ \ That's not disgusting at all!\n\ \ I mean I feel the same---- 」"
        
        show si 012 with dis
        pause .4
        play sound bosu31
        
        si "{size=+15}「THAT'S NOT TRUE! 」"
        fn "「！ 」"
        
        show si 007 with dis
        
        si "「No...{w=.2}you're wrong.{p}\ \ {nw}"
        show si 009 with dis
        extend "I'm...not like that. {w=.2}You're wrong. 」"
        fn "「Wrong...? 」"
        
        show si 007 with dis
        
        si "「I never wanted to love you.{p}\ \ So I decided to stop these feelings in me.{p}\ \ {nw}"
        show si 012 with dis
        extend "That would have been just fine! 」"
        
        show si 009 with dis
        
        si "「That would have...been fine.{p}\ \ If these feelings wouldn't be returned,{w=.2} at least\n\ \ if you came by,{w=.2} I thought it would be enough. 」"
        
        show si 007 with dis
        
        si "「Even if you didn't come around,\n\ \ it'd be fine if we just stayed friends.{p}\ \ Just that...{w=.2} would have been okay... 」"
        fn "「Shin-kun... 」"
        
        show si 009 with dis
        
        si "「This is your fault.{w} It's because you came\n\ \ close that I don't understand my feelings,{p}\ \ I don't understand at all... 」"
        si "「My feelings swelled up,\n\ \ and I can't stop them. 」"
        fn "「... 」"
        si "「...{w} {nw}"
        show si 010 with dis
        extend "At that time,\n\ \ Dad's letter came in.{w} As Amaki said,{w=.2}\n\ \ it's about an overseas technical school. 」"
        
        show si 009 with dis
        
        si "「I like making sweets, and I like eating them. 」"
        si "「If I could turn it into a job, {w=.2}\n\ \ I could surely become happy.{p}\ \ That's why I can understand my father's feelings. 」"
        
        show si 007 with dis
        
        si "「But I'm not like that.{p}\ \ I don't want to do that for work. 」"
        si "「If people just said what I made was good,\n\ \ that would be enough. 」"
        si "「Even if I could make better things if I studied,\n\ \ even then, I didn't want it.{p}\ \ I thought I didn't want to go. 」"
        si "「I thought,{w=.2} I want to stay here... 」"
        
        show si 009 with dis
        
        si "「...{w} it's like the selfishness of a child isn't it?{p}\ \ I know. I know,{w=.2} but I couldn't decide.{p}\ \ I don't know what's best, even if I know the answer. 」"
        fn "「... 」"
        si "「When I read the letter, I thought of you first.{p}\ \ {nw}"
        show si 012 with dis
        extend "And then, I hoped you'd might stop me!{p}\ \ {nw}"
        show si 009 with dis
        extend "When I noticed I hoped that, I knew. 」"
        si "「I noticed the me that'd run from the\n\ \ circumstances to you and explain your excuses. 」"
        si "「I wanted to fall in love with you, {w=.2}but I really\n\ \ just wanted to see you as a convenient human.{p}\ \ I was shocked, and I laughed. 」"
        fn "「... 」"
        si "「If I could push that selfishness onto you,\n\ \ I thought I could get rid of these feelings. 」"
        si "「If you clearly rejected me,\n\ \ I thought I could do it. 」"
        
        show si 012 with dis
        
        si "「And yet...!{w=.2}{nw} "
        show si 007 with dis
        extend "Why didn't you say that?{p}\ \ Why did you say you 'love' me?{p}\ \ Why...{w=.2} are you in front of me again? 」"
        si "「I wanted you to hate me.{p}\ \ Just say you hate me,{w=.2}\n\ \ that would have been fine. 」"
        
        show si 008 with dis
        
        si "「I wanted you to give up on me,\n\ \ I wanted you to draw a line,\n\ \ but why...{w=.2} am I hesitating? 」"
        "...{p}so those are Shin-kun's true feelings..."
        "I quietly got close\nto Shin-kun who was sobbing on the bed.{p}And then, I sat down next to him."
        si "「Don't fill me with any more doubts.{p}\ \ Even if you make me happy, it'd only be painful.{p}\ \ So, clearly,{w=.2} give up on me. 」"
        si "「I beg you, {w=.2}[fn] 」"
        fn "「... 」"
        "Shin-kun shrunk like a frightened child as I\nextended my hand, and for a moment he was perplexed.\nWhen I touched him, I thought he would break apart."
        
        stop music fadeout 1.5
        
        "I told myself it was an illusion,\nand held him by his shoulders.{p}And then, I firmly pulled him towards me."
        "The delicate black cat's body fell on top of my chest."
        
        show si 009 with dis
        
        si "「[fn]... 」"
        "As I held that slim body, I slowly\nspoke to him like I would a crying child."
        
        play music free60
        
        fn "「Hey, Shin-kun.\n\ \ What do you want to give up? 」"
        si "「Eh? 」"
        fn "「Because, Shin-kun,{w=.2} you seem to be in so much pain.{p}\ \ If it's like that, is it really so bad\n\ \ to give up something? 」"
        si "「But... 」"
        fn "「Aren't you the one to decide?{p}\ \ It's okay to be a little selfish. 」"
        
        show si 005 with dis
        
        si "「！ 」"
        
        show si 009 with dis
        
        si "「... 」"
        fn "「Don't get mad, and listen.{p}\ \ If what you say is true,\n\ \ I'll listen, and I was a bit happy. 」"
        fn "「You were relying on me that much. 」"
        si "「I didn't...{w=.2} say that... 」"
        fn "「You did.{p}\ \ I was the first thing you thought of.{p}\ \ Isn't that relying on me? 」"
        si "「{cps=5}N-no... 」"
        fn "「This might bother you, but I'll speak selfishly.{w=.2}\n\ \ I don't want you to go.{w} If you do go,\n\ \ I definitely want you to come back.{w} Because... 」"
        
        stop music fadeout 1.5
        
        "I once again gave him the words I decided on.{p}If it's now, I think they'll reach."
        fn "「I love you Shin-kun.{p}\ \ If I can't see you,{w=.2} I'll be sad. 」"
        si "「...! 」"
        
        play music piano3_014
        
        show si 007 with dis
        
        "Shin-kun shook his head in my chest.\nAs I tightly held him, he hugged back just as hard."
        si "「Terrible...{w} you're terrible, [fn].{p}\ \ And I said such cruel things to you... 」"
        "I held his sobbing form,\nthen patted his small back as he spoke."
        
        show si 008 with dis
        
        si "「I'm scared.{p}\ \ If I'm with you, I might depend on you.{p}\ \ I might get dependent on you,{w} so I'm scared. 」"
        fn "「That's no dependence.{p}\ \ When you're suffering by yourself,\n\ \ that's when it's okay to rely on someone. 」"
        si "「But, {w=.2}I'm bothering you... 」"
        fn "「You aren't bothering me at all.\n\ \ If you rely on me, {w=.2}if you trust me,{w=.2}\n\ \ don't you know that makes me happy? 」"
        si "「...{w} I'm not...{w=.2} bothering you...? 」"
        fn "「That's right. 」"
        si "「I can be... selfish...? 」"
        fn "「Yeah. 」"
        si "「I...{p}\ \ It's okay to...{w=.2}\n\ \ be in love with you? 」"
        fn "「...{w} yeah. 」"
        
        $ event_name = "Shattered Shell"

        show si 008 big at center_big with dis
        
        si "{size=+15}「AH! {w=.2}AAAAAAHH! 」"
        "The one crying loudly in my chest\nwasn't the unpleasable honors student,\nbut just a frightened child."
        "That's how it is, isn't it.{p}It was never something you could do yourself,{w=.2}\nit's just something you had to do that way."
        "You always tried so hard by yourself.\nDon't rely on anyone... you don't know how to."
        
        show si 006 big with dis
        
        si "「Ngh... 」"
        "I raised the head of the black cat in my arms,\nand I forcibly kissed those lips.{p}Just as Shin-kun did that day."
        "I love you.{p}Don't cry anymore.{p}I'm here with you now."
        
        show si 011 big with dis
        
        "It was awkward, but our tongues entwined deeply.{p}When I felt the characteristic rough catman tongue,\nexcitement welled up from within me."
        "When I realized that,\nI pushed Shin-kun down on the bed."
        "After our faces parted while breathing roughly,\nI began exposing the unguarded form of that\nblack cat whose cried out eyes look spellbound."
        "I unintentionally swallowed some saliva as I laid\nmy hands on his clothes,{w} when I was taken aback\nand backed off from Shin-kun in panic."
    
        hide si 
        show si 011 at center
        with dis
        
        si "「Ah... 」"
        fn "「S-sorry.{w=.2} Uh... 」"
        
        show si 013 with dis
        
        si "「...{w=.2}it's okay.{p}\ \ Do it how you want to. 」"
        fn "「Shin-kun... 」"
        si "「If it's you, it's okay. 」"
        fn "「...！ 」"
        "Shin-kun was calmly smiling,\nbut still shaking a little\nwhen I deeply kissed him one more time."
        
        stop music fadeout 1.5
        scene black with sdis
        
###############################################
    label shin27_sex:
        if persistent.replay == True:
            
            $ first = persistent.name_first
            $ last = persistent.name_last
            $ day = 27
            $ event_name = "I Love You"
            
            scene black with dis
            
        $ event_name = "I Love You"
    
        play music wind_noise
        $ renpy.music.set_volume(0.6, 0.0, channel = "music")
        pause 1.5
        scene shin_bed
        show si 111 at center
        with sdis
        
        fn "「You're sure, right? 」"
        si "「Yeah... 」"
        fn "「O-okay, here I go then. 」"
        si "「Okay{w} ...{nw}"
        show si 106 with qdis
        extend "nng. 」"
        "Foreplay went well enough,\nso Shin-kun let me in okay."
        "As I supported myself on my arms slowly\nmoved my hips, even with all the resistance,\nI could tell my tip was slowly going in."
        fn "「Does it hurt? 」"
    
        show si 111 with dis
        
        si "「Mm-mm... 」"
        fn "「S-sorry if I don't do well. 」"
        "Even as I was speaking to him\nI was moving into Shin-kun little by little,\nfar enough that the whole of my tip was inside."
        si "「I'm okay...{w} {nw}"
        show si 106 wuth dus
        extend " ah, whoa... 」"
        fn "「Huh? You feel something? 」"
        
        show si 111 with dis
        
        si "「I'm not...sure yet...{p}\ \ {nw}"
        show si 113 with dis
        extend "but I do know...{w=.2}it's very big. 」"
        fn "「Y-you think so? 」"
        
        show si 111 with dis
        
        "N-no way. Mine's not that big.{p}It's average.{w} I think."
        "As my face showed some embarrassment,\nI went in further."
        "Things went more smoothly than\nI thought after just getting in."
        "I thought I was pushing too much,\nbut Shin-kun seemed okay."
        
        show si 113 with dis
        
        si "「You're warm and big, [fn]. 」"
        fn "「S-Shin-kun, {w=.2}it's embarrassing\n\ \ when you stare at me like that. 」"
    
        show si 110 with dis
        
        si "「... 」"
        "Shin-kun suddenly frowned and\ntightly grabbed my shoulders.{p}Maybe it really is hurting him."
        fn "「Oh, sorry. Does it hurt? 」"
        si "「No...it doesn't. 」"
        "Shin-kun shook his head,\nbut his voice did get quieter.{p}He was grabbing tight, {w=.2}as if saying 'don't move.'"
        fn "「Should I pull out?{p}\ \ If we overdo it, it might hurt... 」"
        si "「[fn]. 」"
        fn "「Huh? 」"
        
        show si 111 with dis
        
        si "「The -kun.{w} I want you to stop adding it. 」"
    
        play sound heartbeat
        
        fn "「Ah... 」"
        "The black cat turned his face away,\nhis eyes flitting back towards me every so often.{p}I called out his name in bewilderment."
        fn "「T-then...{w} Shin. 」"
    
        show si 102 with dis
        
        si "「Mm. 」"
        "Shin-kun smiled, satisfied.{p}At the same time, the hands on my shoulders relaxed.{p}{nw}"
        play sound heartbeat
        extend "{w=.4}{nw}"
        play sound heartbeat
        extend "{w=.4}{nw}"
        play sound heartbeat
        extend "{w=.4}{nw}"
        play sound heartbeat
        extend "My heartbeats suddenly quickened."
        fn "「Sorry, I can't hold back anymore...! 」"
    
        show si 106 with qdis
        
        si "「Ah! Wa- 」"
        
        #!#hide window with dis
        stop music fadeout 1
        pause 1
        play music piano3_005
        scene ev_shin_1a with dis
        $ renpy.music.set_volume(0.7, 0.0, channel = "music")
        play sound humping loop        
        
        "When I suddenly began moving again,\nShin-kun tightened down hard in surprise."
        "However, with the tightening happening\non a lubed up area, all it really did\nwas drive my excitement up."
        si "「[fn],{w} haah,{w} urk,{p}\ \ s-slow down... 」"
        fn "「I can't Shin-kun,{w=.2} Shin! 」"
        si "「Ah,{w} w-wait,{w=.2} ahh 」"
        "As I somewhat forcefully wriggled my hips,\na sweet voice sometimes rose up."
        "It couldn't help but spur me on,\nand I thrust into Shin trying to figure things out."
        si "「N-no!{w=.2} If you... move there...!{p}\ \ Ngh! Aah! 」"
        "Every time I moved, I slowly better understood\nhow to keep going.{w} Just like that I was sliding\nin smoothly while Shin cried out sweetly."
        "The feelings running through my body, the voice in\nmy ear, and Shin's body jumping from beneath me...{p}All of it got my blood boiling."
        si "「Hya!{w} S- {w=.2}wait, this is...{w=.2} Nya! 」"
        "The black cat beneath me cried out as he shook,\ntightly shutting his eyes as if embarrassed."
        "But when I looked down, his member was bent back\nstiff, dribbling drops of delight.{w} Everytime\nit throbbed I swore I could hear heartbeats."
        "As I kept going I was getting close to the edge,\nand I let the pace fall out of confusion."
    
        stop sound fadeout 1
        
        si "「Ngah! {w=.2}　Hah...{w=.2}ngh!{p}\ \ I-it feels,{w=.2} ah!{w=.2} My stomach's tingling... 」"
        fn "「Does it feel good? 」"
        "I pulled one of Shin's hand, and as we entwined our\nfingers I held his light airy furred form close.{p}I could smell the scent of the sun on him."
        si "「Ah- It{w=.2} does 」"
        "As he twitched and trembled, Shin spoke in a\nfeeble voice.{w} His inner walls gripped so hard it\nwas almost unbearable, and I gave a little groan."
        si "「[fn]...I feel like...{w=.2}\n\ \ I'm losing my mind... 」"
        "Shin slightly opened his eyes as tears appeared.{p}I placed my lips atop his again."
        si "「Ng...u- n...ah-{w=.2} nya! Ha~ah! 」"
    
        play sound humping loop
        
        "I moved once again,\nand his voice rose more glossed over than before."
        "I felt a hot sigh on my face.{p}I tightly held onto Shin's body\nas my hips slapped into him countless times."
        "Things would end soon if I spaced out,\nbut as I felt Shin's impatience at not being close\nI let my body run on instinct and pleasure."
        si "「Ngh... nm... 」"
        "We exchanged countless kisses as our\ntongues wrestled.{w} I could almost feel\nhis breathy voice inside my mouth."
        "I combed the slightly rough fur and felt the heat\nwithin him.{w} When I pushed the little prick I saw,\nShin cried out sweetly yet again."
    
        scene white with qdis
        scene ev_shin_1a with qdis
        
        "I grabbed the towering hard malehood,\nand drew my hand through the spilling droplets.\nIn that instant, Shin's body notably flinched."
    
        stop sound fadeout 1
        scene white with qdis
        scene ev_shin_1a with qdis
        
        si "「[fn]！{w} {nw}"
        scene white with qdis
        scene ev_shin_1a with dis
        extend "Ah!{w} {nw}"
        scene white with qdis
        scene ev_shin_1b with dis
        extend "　Nyaahhh!！ 」"
        "My entire body stiffened and trembled convulsively,\nand I shot hard and hot into him\nwhile my right hand was gripped tightly."
        fn "「I-I'm cumming too! 」"
        "I couldn't stand the sudden pressure,\nand I reached my limit a moment later.{p}All the feelings I tried to endure flooded my mind."
        "I felt like I was going to collapse from it all\nas I marked out a bit of myself into\nthe deepest parts of Shin."
        "Maybe it was because of the pressure,\nbut the orgasm and the sensations{w=.2}\nflowing from my base continued for a little bit."
        
        scene white with sdis
        pause 1
        scene black with sdis
        stop music fadeout 1.5
        pause 3
        play music wind_noise
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        scene shin_bed
        show si 111 at center
        with sdis
        
        si "「... 」"
        fn "「Are you okay?{w} Do you feel pain anywhere? 」"
        si "「I'm okay... 」"
        si "「...{w} [fn] 」"
        fn "「Hm? 」"
        si "「Was it...{w=.2} good for you? 」"
        fn "「Y-{w=.2}yeah. 」"
        
        show si 113 with dis
        
        si "「Then, that's good. 」"
        "He's smiling bashfully even after we've done\nsomething like this, but the expression on his face\nwas much more innocent that I had ever seen it."
        "It wasn't false, {w=.2}it wasn't a decoy,{w=.2}\nit was very pure...{p}This was Shin-kun's true face."
        
        show si 111 with dis
        
        si "「My heart's still pounding. 」"
        fn "「Me too... 」"
    
        show si 109 with dis
        
        si "「[fn] 」"
        fn "「What? 」"
        
        show si 111 with dis
        
        si "「... 」"
        
        hide si with dis
        play sound standup
        
        "Shin clung tight to me."
        si "「...{w=.2}can I say something selfish? 」"
        fn "「Like what? 」"
        si "「Just, let me do this for a while.{p}\ \ I want to stay like this. 」"
        fn "「...{w} okay. 」"
        "Shin settled onto my chest, and I held him back\ngently.{w} I felt our body temperatures become one,\nand before I knew it, we fell asleep like that."
    
        stop music fadeout 1
        scene black with sdis
        pause 2
        
        if persistent.replay == True:
            $ renpy.end_replay()
            
        $ persistent.event_shin1 = True
        
        if shin_key3 == True:
            jump shin27_childhood_memory
        else:
            jump shin27_childhood_goodbye
    
    ###########################################################
    label shin27_childhood_memory:
            
        $ event_name = "Early Childhood"
        
        "My body is sinking.{p}I can't breathe.{p}Help me...{w} help me!"
    
        play music piano4_001
        
        scene school01 gray 
        show over red light 
        with sdis
        
        "I hear children's voices from far away.{p}In the excitement, I hear someone calling.{p}It's probably an adult calling them."
    
        scene black with sdis
        scene school hallway 1 gray
        show over red light 
        with sdis
        
        "A white ceiling.{p}My mother's crying face.{p}Did I have another fit?"
        si "「I'm... sorry... 」"
        "My mother's hand tightly holding mine{w=.2}\nwas so very warm."
    
        scene black with sdis
        scene school01 gray 
        show over red light
        with sdis
        
        "「Shin-kun's body is weak,\nso you can't push him into anything! 」"
        "No.{p}I asked for it.{p}I said I wanted us to run and play together."
        "But, I'm the child of a rich family.{p}The adults were always sensitive to\nthe possibility I might not get up."
        "「Won't you collapse soon? 」"
        "...{w=.2}that's why I was always told no.{p}Even so, when I was selfish, everyone got mad.{p}I'm sorry. I'm so sorry."
        "Even if you're with me, it's boring isn't it?"
    
        scene black with sdis
        scene shin_bedroom gray 
        show over red light
        with sdis
        
        "There wasn't anything I really liked.{p}Not art, {w=.2}not music,{w=.2} not literature.{w} I was\njust trying to find something I could do alone."
        "Once I could read, I was especially lost\nin my books.{w} Even with a body like this,{w=.2}\nif I was in a book, I was free."
    
        scene black with sdis
        scene school gym gray 
        show over red light
        with sdis
        
        "「You're amazing Shin-kun. 」"
        "...{w} no.{p}I'm not amazing at all.{p}I just haven't done anything else."
        "Since I was always alone, I did things people could\ndo alone.{w} That's all there is to it.{p}Even then, people still said that to me."
        "They said, \"it's amazing\nhow you can do anything by yourself.\""
    
        scene black with sdis
        
        "...but I was happy my parents just praised me.{p}Because I had always worried them.{p}When they smiled for me, I was so happy."
    
        scene bus gray 
        show over red light
        with sdis
        
        "「Minasato Village 」"
        "If I go there, my sickness could be healed.{p}The two of them told me I'd be living there from\nnow on.{w} I nodded to both of them in reply."
        "...{w} I never said it.{p}I knew, even without asking."
        "「What about you, Mom and Dad? 」"
    
        scene black with sdis
        
        "I never said it.{w} Because, I knew the answer.{p}Even if I asked that question,\nit'd only cause trouble for them."
        "I'll be okay by myself.{p}Besides, the one looking after me in their place\nis someone I know very well."
        "But..."
    
        scene shin_bed gray 
        show over red light
        with sdis
        
        "I was scared of that morning arriving."
        "Maybe all of this was a dream,\nand when I open my eyes I'll be with my parents,{p}and maybe that morning won't come."
        "But, it was all a fantasy.{w} An idle phantasm.{p}When I open my eyes it'd all disappear,\na stupid dream."
        "When morning came,{w=.2}\nI helplessly realized that."
        "That's why I was scared of that morning coming."
    
        scene black with sdis
        
        "I was always alone.{p}Nothing changed,{w=.2} nothing could change,{w=.2}\nI was shown that was the only truth..."
    
        scene black with sdis
        stop music fadeout 1    
        pause 1
        play sound bosu34
        scene shin_bed
        show si 105 at center
        with dis
        
        si "「...! 」"
        
        show si 101 with dis
        
        si "「{cps=10}A...{cps=40}{w=.2}dream? 」"
        
        show si 110 with dis
        
        "Why am I suddenly remembering that time...?"
        
        show si 109 with dis
        
        si "(Always alone...)"
        "Maybe I've always felt like that.{p}Ever since I came to this village."
        fn "「Nmm. 」"
        
        show si 105 with dis
        
        si "「！？ 」"
        
        show si 101 with dis
        
        si "「[fn]...？ 」"
        fn "「... 」"
        si "「Why are you in my bed...{w} {nw}"
        show si 106 with dis
        extend " ah! 」"
        
        show si 111 with dis
        
        si "(Oh right, up until a while ago we...)"
        fn "「... 」"
        
        show si 101 with dis
        
        si "「...{w} {nw}"
        show si 102 with dis
        extend "...hee hee.{p}\ \ You sleep so well. 」"
        "All alone?{p}What kind of stupid thing am I saying?"
        "This village allows me to be by myself,\nand I didn't have any good friends.{p}I really was alone."
        "Even if I did have friends who didn't treat me\nlike an untouchable swelling,{w=.2} who talked\nwith me normally, who were so impudent and nosy."
    
    #####################################################
    label shin27_childhood_goodbye:
            
        $ event_name = "This isn't a Dream, is it?"
        
        scene black with sdis
        scene bstop gray 
        show over red light
        with sdis
        
        si "「Transferring...? 」"
        fn "「Yep.{p}\ \ That's why I came to see you. 」"
        si "「Hmm.{w} I see... 」"
        fn "「Come on, say some more.{p}\ \ Well that is like you Shin-kun.{p}\ \ Later, take care of yourself even if I'm not here. 」"
        si "「You take care too, [fn]. 」"
        si "「...{w=.2}...{w=.2}. 」"
    
        scene black with sdis
        
        "I didn't say anything then either.{p}The day I knew the friend I loved would leave.{p}Since then, always up until now."
        "\"I'll be lonely if I can't see you.\"{p}I couldn't say I didn't want us to be seperated."
        "He was going to leave me behind too.\nI couldn't think of it any other way.{p}Are you okay with someone like me?"
    
        scene black with dis
        scene shin_bed
        show si 109 at center
        with dis
        
        si "「It's not a dream is it, {w=.2}[fn]? 」"
    
        play sound standup
        hide si with dis
        
        "I quietly whispered it inside my mouth,\nand I gently pressed my face against him.{p}I could smell his scent."
        "It's warm.{w} It's not a dream.{p}I'm here with you."
        "I love you.{p}I've always loved you,{w} [fn]."
        "I said it one more time in my head,\nand slowly closed my eyelids."
    
        scene black with sdis    
        
        $ event_name = "Because it's my own Decision"
    
        scene shin_bedroom red
        show si 001 red at center
        with sdis
        play music free0258
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        
        fn "「Alright, it's about time for me to go home. 」"
        
        show si 009 red with dis
        
        si "「Right.{p}\ \ Thanks, {w=.2}for everything today. 」"
        fn "「Um,{w=.2} hey.{p}\ \ I'm not trying to press you for an answer,\n\ \ but what are you going to do about the school? 」"
        
        show si 001 red with dis
        
        si "「...{p}\ \ {nw}"
        show si 002 red with dis
        extend "I'm going to think about it again my own way.{p}\ \ It's okay, {w=.2}I can decide by myself. 」"
        fn "「If you say so Shin-kun...{p}\ \ But, if you want my advice go ahead and ask.{p}\ \ I'll help you as much as I can. 」"
        
        show si 013 red with dis
        
        si "「Thank you. 」"
        
        show si 001 red with dis
        
        si "「By the way. 」"
        fn "「Hm? What? 」"
        si "「Try saying my name, one more time. 」"
        fn "「？{w} 　Shin-kun. 」"
        si "「{cps=10}... 」"
        fn "「{cps=10}...{cps=40}{w} ah. 」"
        "It was a little while after\nI realized what I said so casually."
        
        show si 002 red with dis
        
        fn "「I mean, Shin. 」"
        si "「It's okay, don't force yourself.{p}\ \ Everyone will think it's weird\n\ \ if you're suddenly addressing me differently. 」"
        fn "「Y-you think so?{w} I think I've fallen\n\ \ into the habit of using -kun...{w} sorry. 」"
        si "「I said it's okay.{p}\ \ {nw}"
        show si 011 red with dis
        extend "Though I suppose I'd be happy if\n\ \ you called me that when we're alone,{w=.2} I think. 」"
        "Shin looked away a little as his voice softened.{p}When I saw him obviously embarrassed,\nmy face relaxed instinctively."
        fn "「Got it. I'll do it whenever I can. 」"
        
        show si 002 red with dis
        
        si "「Okay. 」"
        "..."
        fn "「Hey, Shin. 」"
        
        show si 001 red with dis
        
        si "「What? 」"
        fn "「... 」"
        
        show si 013 red with dis
        scene black with sdis
        
        "After a little silence, we kissed each other\none more time before I would leave."
        "Even if I leave, I'm sure we'll meet again.\nThis is the promise we exchanged."
        
        if shin_true == True and shin_key2 == True and shin_key3 == True:
            jump shin27_number_promise
        else:
            jump end27
    
    ##########################################################
    label shin27_number_promise:
        
        $ event_name = "A Promise"
        
        $ shin_trueend = True
        scene shin_bedroom red
        show si 001 red at center
        with sdis
        
        si "「Oh, wait. 」"
        
        hide si with wipe_right
        
        fn "「Hm? 」"
        "Immediately after our faces parted, Shin-kun\nseemed to remember something and went for his desk."
        
        play sound tm2_slidedoor000
        pause 1
        
        "He pulled something out of the drawer\nand brought it back."
        
        show si 002 red at center with dis
        
        fn "「This is... 」"
        si "「It might not work here,\n\ \ but there may be a signal in Kazenari.{p}\ \ Is it okay if we exchange numbers and addresses? 」"
        fn "「Of course!{p}\ \ No wait, I left it back at my grandparents'. 」"
        
        show si 001 red with dis
        
        si "「Next time then.{p}\ \ {nw}"
        show si 009 red with dis
        extend "We'll be fine even if we're separated, won't we. 」"
        fn "「Yeah,{w=.2} definitely. 」"
        
        show si 002 red with dis
        
        "I gave a big nod to Shin-kun,\nwho seemed a bit anxious."
        
        jump end27
    
#########################################################
label end27:
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

    jump day28

