###Replay
##Will show all images for the Gallery

screen cg_tatsuki1():
    imagebutton idle "ev_tatsuki_1" action Hide('cg_tatsuki1', Dissolve(0.5))
    
screen cg_tatsuki2():
    imagebutton idle "ev_tatsuki_2" action Hide('cg_tatsuki2', Dissolve(0.5))
    
screen cg_kounosuke1():
    imagebutton idle "ev_kounosuke_1" action Hide('cg_kounosuke1', Dissolve(0.5))
    
screen cg_kounosuke2():
    imagebutton idle "ev_kounosuke_2" action Hide('cg_kounosuke2', Dissolve(0.5))
    
screen cg_ghost1():
    imagebutton idle "ghostpic clear" action [Hide('cg_ghost1', Dissolve(0.5)), Show('cg_ghost2')]
    
screen cg_ghost2():
    imagebutton idle "ghostpic blur1" action [Hide('cg_ghost2', Dissolve(0.5)), Show('cg_ghost3')]
    
screen cg_ghost3():
    imagebutton idle "ghostpic blur2" action Hide('cg_ghost3', Dissolve(0.5))
    
screen cg_shun1a():
    imagebutton idle "ev_shun_1a" action [Hide('cg_shun1a', Dissolve(0.5)), Show('cg_shun1b')]
    
screen cg_shun1b():
    imagebutton idle "ev_shun_1b" action Hide('cg_shun1b', Dissolve(0.5))
    
screen cg_shun2a():
    imagebutton idle "ev_shun_2a" action [Hide('cg_shun2a', Dissolve(0.5)), Show('cg_shun2b')]
    
screen cg_shun2b():
    imagebutton idle "ev_shun_2b" action Hide('cg_shun2b', Dissolve(0.5))
    
screen cg_kouya1a():
    imagebutton idle "ev_kouya_1a" action [Hide('cg_kouya1a', Dissolve(0.5)), Show('cg_kouya1b')]
    
screen cg_kouya1b():
    imagebutton idle "ev_kouya_1b" action Hide('cg_kouya1b', Dissolve(0.5))
    
screen cg_kouya2a():
    imagebutton idle "ev_kouya_2a" action [Hide('cg_kouya2a', Dissolve(0.5)), Show('cg_kouya2b')]
    
screen cg_kouya2b():
    imagebutton idle "ev_kouya_2b" action Hide('cg_kouya2b', Dissolve(0.5))
    
screen cg_juuichi1a():
    imagebutton idle "ev_juuichi_1a" action [Hide('cg_juuichi1a', Dissolve(0.5)), Show('cg_juuichi1b')]
    
screen cg_juuichi1b():
    imagebutton idle "ev_juuichi_1b" action Hide('cg_juuichi1b', Dissolve(0.5))
    
screen cg_juuichi2a():
    imagebutton idle "ev_juuichi_2a" action [Hide('cg_juuichi2a', Dissolve(0.5)), Show('cg_juuichi2b')]
    
screen cg_juuichi2b():
    imagebutton idle "ev_juuichi_2b" action [Hide('cg_juuichi2b', Dissolve(0.5)), Show('cg_juuichi2c')]
    
screen cg_juuichi2c():
    imagebutton idle "ev_juuichi_2c" action Hide('cg_juuichi2c', Dissolve(0.5))
    
screen cg_shin1a():
    imagebutton idle "ev_shin_1a" action [Hide('cg_shin1a', Dissolve(0.5)), Show('cg_shin1b')]
    
screen cg_shin1b():
    imagebutton idle "ev_shin_1b" action Hide('cg_shin1b', Dissolve(0.5))
    
screen cg_shin2a():
    imagebutton idle "ev_shin_2a" action [Hide('cg_shin2a', Dissolve(0.5)), Show('cg_shin2b')]
    
screen cg_shin2b():
    imagebutton idle "ev_shin_2b" action Hide('cg_shin2b', Dissolve(0.5))
    
screen cg_afterword0():
    imagebutton idle "afterword0" action Hide('cg_afterword0', Dissolve(0.5))
    
screen cg_afterword1a():
    imagebutton idle "afterword1a" action [Hide('cg_afterword1a', Dissolve(0.5)), Show('cg_afterword1b')]
    
screen cg_afterword1b():
    imagebutton idle "afterword1b" action [Hide('cg_afterword1b', Dissolve(0.5)), Show('cg_afterword1c')]
    
screen cg_afterword1c():
    imagebutton idle "afterword1c" action [Hide('cg_afterword1c', Dissolve(0.5)), Show('cg_afterword1d')]
    
screen cg_afterword1d():
    imagebutton idle "afterword1d" action Hide('cg_afterword1d', Dissolve(0.5))
    
screen cg_afterword2a():
    imagebutton idle "afterword2a" action [Hide('cg_afterword2a', Dissolve(0.5)), Show('cg_afterword2b')]
    
screen cg_afterword2b():
    imagebutton idle "afterword2b" action [Hide('cg_afterword2b', Dissolve(0.5)), Show('cg_afterword2c')]
    
screen cg_afterword2c():
    imagebutton idle "afterword2c" action Hide('cg_afterword2c', Dissolve(0.5))
    
screen cg_afterword3a():
    imagebutton idle "afterword3a" action [Hide('cg_afterword3a', Dissolve(0.5)), Show('cg_afterword3b')]
    
screen cg_afterword3b():
    imagebutton idle "afterword3b" action [Hide('cg_afterword3b', Dissolve(0.5)), Show('cg_afterword3c')]
    
screen cg_afterword3c():
    imagebutton idle "afterword3c" action Hide('cg_afterword3c', Dissolve(0.5))
    
##Leads to replaying scenes from Game

label rp_tatsuki1():
    $ persistent.replay = True
    $ renpy.call_replay('tatsuki22_sex')
    $ persistent.replay = False
    scene replaymode
    call screen gallery('rp', 1)
    
label rp_tatsuki2():
    $ persistent.replay = True
    $ renpy.call_replay('tatsuki30_sex')
    $ persistent.replay = False
    scene replaymode
    call screen gallery('rp', 1)
    
label rp_kounosuke1():
    $ persistent.replay = True
    $ renpy.call_replay('kounosuke29_sex')
    $ persistent.replay = False
    scene replaymode
    call screen gallery('rp', 1)
    
label rp_nanafuse():
    $ persistent.replay = True
    $ renpy.call_replay('nanafuse00')
    $ persistent.replay = False
    stop sound
    scene replaymode
    call screen gallery('rp', 1)
    
label rp_shun1():
    $ persistent.replay = True
    $ renpy.call_replay('shun16_sex')
    $ persistent.replay = False
    scene replaymode
    call screen gallery('rp', 2)
    
label rp_shun2():
    $ persistent.replay = True
    $ renpy.call_replay('shun26_sex')
    $ persistent.replay = False
    scene replaymode
    call screen gallery('rp', 2)
    
label rp_kouya1():
    $ persistent.replay = True
    $ renpy.call_replay('kouya26_sex')
    $ persistent.replay = False
    scene replaymode
    call screen gallery('rp', 2)
    
label rp_kouya2():
    $ persistent.replay = True
    $ renpy.call_replay('kouya29_sex')
    $ persistent.replay = False
    scene replaymode
    call screen gallery('rp', 2)
    
label rp_juuichi1():
    $ persistent.replay = True
    $ renpy.call_replay('juuichi29_sex')
    $ persistent.replay = False
    scene replaymode
    call screen gallery('rp', 3)
    
label rp_juuichi2():
    $ persistent.replay = True
    $ renpy.call_replay('juuichi30_sex')
    $ persistent.replay = False
    scene replaymode
    call screen gallery('rp', 3)
    
label rp_shin1():
    $ persistent.replay = True
    $ renpy.call_replay('shin27_sex')
    $ persistent.replay = False
    scene replaymode
    call screen gallery('rp', 3)
    
###############################################################
##This scene can only be viewed in the gallery if you discover the truth about Nanafuse 
label nanafuse00:
    
    $ day = "?"
    $ event_name = _("A Lie")
    
    scene black with dis
    
    "Does everybody know about it?{p}At this school, there is a strange,{p}slightly scary story called \"The Seven Wonders\"..."
    
    scene black with dis
    $ renpy.music.set_volume(0.7, 0.0, channel = "music")
    play music free60 fadein 1
    pause 1
    
    scene library
    show na 001 at midright
    show yk 001 at midleft
    with sdis

    na "「The Seven Wonders? 」"
    ko "「Yep. 」"
    na "「If it's a scary book, they're over there. 」"
    
    show yk 003 with dis
    
    ko "「No, no. 」"
    
    show yk 002 with dis
    ko "「The Seven Wonders of Minasato's school! 」"
    
    show yk at jump_up
    ko "「This school has seven wonders.{p}\ \ That's why I'm interviewing different people,{p}\ \ but nobody ever knows anything about the last one. 」"

    show yk at move_center(.25)
    
    ko "「Do you know about the 7th?{p}\ \ The last of the Seven Wonders. 」{w}{nw}"
    show na at shake_side
    extend "{w=.5}{nw}"
    hide na
    show na 001 at midright behind yk 
    with dis
    
    na "「Err... 」"
    
    show na at move_farright(.25)
    
    na "「Why are you asking me? 」"
    
    show yk 002 with dis
    
    ko "「You like books, don't you?{p}\ \ I thought you would know a lot about it. 」"
    na "「I don't particularly like them... 」"
    
    show yk 001 with dis
    
    ko "「Huh?{w=.2} Really? 」"
    
    show na 002 with dis
    
    na "「Yeah. I like how it feels in here,{p}\ \ rather than the books. 」"
    ko "「Hmmm. 」"
    
    scene library
    show na 002 at farright
    show yk 001 at center
    with dis
    $ renpy.music.set_volume(0.8, 0.0, channel = "sound")
    play sound clock_tick loop
    pause 3
    stop sound 
    pause .2
    
    ko "「Oh, um, so, do you know anything? 」"
    
    show na 001 with dis
    
    na "「I do know about it, but... 」"
    
    show yk 002 with dis
    
    ko "「Really!? 」"
    na "「Yeah. 」{w}{nw}"
    show yk at jump_up
    extend "{w=.2}{nw}"
    show yk at move_midright(.25)
    
    ko "「Yes! Tell me, tell me. 」{w}{nw}"
    show na 002 at shake_side
    extend "{w=.5}{nw}"
    hide na
    show na 002 at farright behind yk 
    with dis
    
    na "「O,okay. 」"
    
    show yk 001 with dis
    
    ko "「Ah, wait a minute. Let me prepare. 」"
    
    scene library with sdis
    show na 002 at midright
    show yk 001 at midleft
    with sdis
    
    ko "「Now then, let's start the interview. 」"
    na "「Umm...{p}\ \ {nw}"
    show na 001 with dis
    extend "You want me to talk about the 7th wonder, right? 」"
    ko "「Yes. 」"
    na "「If you know about the 7th wonder,{p}\ \ bad things happen to you. 」"
    na "「Even if you do know about it,{p}\ \ you're not supposed to tell anybody.{p}\ \ That's why nobody knows about it. 」"
    
    show yk 002 at jump_up
    
    ko "「Mmhm.{w=.2} What else? 」"
    na "「That's it. 」"
    
    show yk 001 with dis
    
    ko "「...{w=1}Huh? 」"
    na "「That's the 7th wonder. 」"
    
    show yk 003 with dis
    
    ko "「Eh?{w} ...what? 」"
    
    show na 002 with dis
    
    na "「That's why the last wonder is {w=.2}{cps=10}\"The Secret You Must not\n\ \ Know\".{w=.2}{w} {cps=40}The secret, or the rumors, are really the 7th wonder."
    na "That's the trick of the Seven Wonders. 」"
    
    pause 1
    
    show yk 003 at jump_up
    
    ko "「...Huuuuuh!? 」"
    
    show yk at briefzoom
    
    ko "「{w=.2}What!?{p}\ \ That's boring! {nw} 」"
    show yk at bobbing
    extend "{w}{nw}"    
    hide yk with wipe_down_slow
    extend "{w=.3}{nw}"
    show library at vshake
    $ renpy.music.set_volume(0.6, 0.0, channel = "sound")
    play sound bosu31
    extend "{w=.3}{nw}"
    
    ko "「O,ow. 」"
    
    hide na with dis
    
    na "「Are you okay? 」"
    ko "「I,I'm fine.{w=.3} Ouch. 」"
    
    scene library with sdis
    show na 001 at midright
    show yk 003 at midleft
    with sdis
    
    ko "「I see... So that's why{p}\ \ nobody would tell me anything about it. 」"
    
    show na 002 with dis
    
    na "「It's not that they didn't know,{p}\ \ there was just nothing to begin with.{p}\ \ There's nothing for anybody to tell you. 」"    
    ko "「Oooh. But the interview... 」"
    
    pause 2    
    show na 001 with dis
    
    na "「...But there's actually more to the{p}\ \ rumors of the Seven Wonders. 」"
    
    show yk 001 with dis
    
    ko "「Huh...? 」{w}{nw}"    
    $ renpy.music.set_volume(0.2, 1.0, channel = "music")
    $ renpy.music.set_volume(0.2, 0.0, channel = "sound")
    play sound clock_tick
    $ renpy.music.set_volume(0.8, 1.0, channel = "sound")

    na "「{cps=20}A kid who heard about them{p}\ \ and became fixated on the 7th. 」"
    na "「{cps=20}Anyone he asked would just say that \"Something strange\n\ \ happens\", and nobody would tell him anything.\n\ \ That's why it's all rumors. 」"
    na "「{cps=20}\"What kind of story is the 7th wonder?\" they asked.\n\ \ In that way, the rumors of the Seven Wonders spread{p}\ \ and eventually a new rumor was born. 」"
    na "「{cps=20}The story of the {cps=10}\"True Seven Wonders\"{w=.2}{cps=20}{p}\ \ came from everybody's gossiping. 」"
    
    show na 002 with dis

    na "「Even though there's really nothing,{p}\ \ there are the \"True Seven Wonders\".{p}\ \ It's funny, isn't it?. 」"
    ko "「... 」"
    
    show na 001 with dis
    na "「{cps=20}But everybody believed it.\n\ \ That there is a 7th wonder. 」"
    na "{cps=20}「So before too long, the 7th wonder became\n\ \ {w=.2}{cps=10}\"It's there and yet it isn't\". 」"
    
    show na 002 with dis
    
    na "「{cps=20}In time, something strange happened{p}\ \ among the children investigating the Seven wonders. 」"
    
    show na 001 with dis
    
    na "「{cps=20}While they were investigating,{p}\ \ their number of friends increased{p}\ \ by one without them noticing. 」"
    na "「{cps=20}Even though everybody should know{p}\ \ who their friends are. 」"
    na "「{cps=20}But when they went home,{p}\ \ the number would decrease by one person. 」"
    na "「{cps=20}Isn't that strange?{p}\ \ So everybody was clamoring about{p}\ \ \"The Appearance of the Ghost of the Seven Wonders\". 」"
    
    show na 002 with dis
    
    na "「{cps=20}Surely somebody just made a simple mistake when counting,\n\ \ right?{nw}"
    show na 001 with dis
    extend ""
    na "{cps=20}But nobody thought that. 」"
    na "「{cps=20}\"When you try to investigate the Seven Wonders, a ghost\n\ \ appears.{w} It pretends to be somebody everybody knows!\"{p}\ \ they fussed about. 」"
    
    show na 002 with dis
    
    na "{cps=20}「In addition to that, \"That ghost is really always near\n\ \ everybody, but nobody realizes it\", the children gossiped. 」"
    
    show na 001 with dis
    
    na "{cps=20}「In doing so, the 7th wonder that should have been nothing\n\ \ unkowingly became another rumor. 」"
    na "{cps=20}「A known, yet unknown person who lives in Minasato's school.\n\ \ A rumored {w=.2}{cps=10}\"known, but unkown person\"{w=.2}{cps=20} who plays with the\n\ \ children. 」"
    na "{cps=20}「That's the story of the last of the Seven Wonders. 」"
    ko "{cps=20}「... 」"
    
    pause 1
    $ renpy.music.set_volume(1.0, 1.0, channel = "sound")    
    show na 002 with dis
    
    na "「How was that?{w=.2} Was that a good interview? 」"
    
    stop sound fadeout 1
    $ renpy.music.set_volume(0.8, 1.0, channel = "music") 
    
    ko "「Oh...{cps=10}{p}\ \ {nw}"
    show yk 003 with dis
    extend "Aah!{w=.2} I forgot! 」"
    ko "「Err, {w=.2}\n\ \ {cps=10}\"The 7th wonder, a known but unknown person\". 」"
    
    scene black with sdis
    scene school hallway 1 red with sdis
    show na 001 red at midright
    show yk 002 red at midleft
    with sdis
    
    ko "「Thanks. I'm glad I asked you about it.{p}\ \ {nw}"
    show yk 001 red with dis
    extend "I need to tell everybody about this rumor. 」"
    
    show na 002 red with dis
    
    na "「Sure.{w=.2} Go ahead. 」"
    ko "「Alright, see you tomorrow, Nanacchi. 」"
    na "「See you later~ 」"
    
    show yk at move_offleft_far(.5)    
    show na 001 red with dis

    na "「Oh!{w=.25} Wait! 」"
    
    show yk at move_midleft(.75)
    
    ko "「What? 」"
    na "「Kounosuke, I just have one thing to ask of you. 」"
    
    show yk 002 red with dis

    ko "「And what is that? 」"
    na "「Um... 」"
    
    show na 101  red with sdis
    show na 001 red with sdis
    
    na "「{cps=20}Don't forget about me. 」"
    
    show yk 001 red with dis
    
    ko "「?{p}\ \ I wouldn't forget about you. 」"
    
    show na 002 red with dis
    
    na "「But you do have a pretty bad memory. 」"
    
    show yk 003 red with dis
    
    ko "「That's mean! Even though it doesn't seem like it,{p}\ \ I do have a good memory. 」"
    
    show na 001 red with dis
    
    na "「Okay.{w}{w=.2} Sorry. 」"
    
    show yk 001 red with dis
    
    ko "「Nanacchi,{w=.2} what's wrong? 」"

    show na 002 red with dis
    
    na "「It's nothing.{p}\ \ Anyways, won't Botan-sensei get angry if he catches you{p}\ \ being in the school at a time like this? 」"

    show yk 003 red with dis

    ko "「Oh crap!{w=.2} You're right.{p}\ \ S,see you later Nanacchi! 」"
    
    show yk at move_offleft_far(.5)
    show na 001 red with dis
    
    na "「{w=.2}{cps=30}... 」"
    
    stop music fadeout 1
    scene black with sdis
    pause .5
    $ renpy.music.set_volume(0.7, 0.0, channel = "music") 
    play music melodious05
    scene school01 red with sdis
    show na 101 at center with sdis
    
    "{cps=20}I know it's impossible,{p}but why do I always try?{p}I am real, and yet {w=.2}{cps=10}\"not real\"{w=.2}."
    "{cps=20}Will Kounosuke remember me with those notes?{p}He'll forget... even my rumors."
    
    show na 102 with dis
    
    "{cps=20}But I'll remember.{p}Everybody made me, the 7 that was empty."
    "{cps=20}The children made the rumor of {w=.2}{cps=10}\"The Ghost of the Seven Wonders\"{w=.2}."
    "{cps=20}A lot of children believed in the rumor.{p}People who were children."
    "{cps=20}A friend who found me as a faint ghost{p}gave me my form."
    "{cps=20}My form was given a name when his was called out.{p}That friend created {w=.2}{cps=10}\"me\"."
    "{cps=20}I played with a lot of friends,{p}and there were so many memories.{p}I'm sure everybody has forgotten,{w=.2}{cps=30} but I haven't."
    
    scene white with sdis
    pause .5
    
    "{cps=20}My memories of playing with everybody under the{p}sunlight shining through the trees,\n{w=.2}{cps=30}I'll aways have them,{w=.2} forever..."
    
    scene white with dis
    $ renpy.music.set_volume(0.4, 1.0, channel = "music") 
    $ renpy.music.set_volume(0.4, 1.0, channel = "sound") 
    play sound wind_noise
    stop music fadeout 3
    pause 3
    scene black with sdis
    pause 3

    $ renpy.end_replay()
    
    pause

        

    
    

