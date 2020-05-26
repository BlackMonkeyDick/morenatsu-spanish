##Day 3

screen park03:
    hbox:
        add "arrow down"
        at parkbounce1
    hbox:
        add "icon_shun"
        at parkbounce2
    hbox:
        text _("Park")
        xalign .49 yalign .55
screen arcade03:
    hbox:
        add "arrow down"
        at marketbounce1
    hbox:
        add "icon_shin"
        at marketbounce2
    hbox:
        text _("Candy Store")
        xalign .5 yalign .51
        
screen minasatomap03():
    add "map"
    add "mapdate"
    imagebutton idle "a icon" hover "icon loop" xpos 364 ypos 270  action Jump("shun03") hovered Show("park03") unhovered Hide("park03") hover_sound "av/audio/click_008.wav" 
    imagebutton idle "a icon" hover "icon loop" xpos 372 ypos 249  action Jump("candy03") hovered Show("arcade03")  unhovered Hide("arcade03") hover_sound "av/audio/click_008.wav"
    hbox:
        text _("{size=+30}August 3")
        at maptime
    
###########################################
label day03:
    
    $ renpy.music.set_volume(1.0, 0.0, channel = "music")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound2")
    
    $ the_date = _("August 3")
    $ focus_character = ""
    $ event_name = _("８月3日")
    
    window hide
    play music birds_chirping
    
    scene sky01 
    show text "{size=+130}August 3" at truecenter
    with Dissolve(.5)

    pause 3
    scene black with Dissolve(1)
    pause .4
    
    scene hbroom with wipe_corner
    fn "「Hmm, what to do today... 」"
    
    play music "<from 2.5>av/audio/free0422.ogg"
    call screen minasatomap03

###########################################    
label candy03:

    $ event_name = _("An Incompatible Person")
    $ focus_character = "shin"    
    
    scene map
    stop music
    hide screen arcade03
    scene black with Dissolve(1)
    scene candystoreout with Dissolve(1)
    play music daily04
    pause .5
    $ love_shin += 1
    
    "Whoa, this thing is still here."
    "In a fit of nostalgia,\nmy feet brought me here to this old-fashioned building,"
    "and you can just feel where the workmanship was done."
    "I'd always try to resist coming here on the way home,{w=.3}\nfail to do so, then get found out by the teacher\nwho would then get mad. Along with everyone else."
    "Hm? Looks like someone's here already."
    
    scene candystorein
    show si 001 at midright
    show ta 001 at midleft
    with dis

    "Isn't that Tatsu-nii and Shin-kun?{p}That's a strange pairing."
    ta "「... 」"
    si "「... 」"
    
    show si 009
    show ta 006
    with dis
    
    "I wonder what's up?{p}I'm too far away to hear what they're saying,\nbut there does seem to be some strange mood there."
    
    show ta 002 with dis

    ta "「O-oh yeah, I met Amaki-san the other day. 」"
    
    show si 001 with dis
    
    si "「Oh, I see.{w=.3}\n\ \ ...And? 」"
    
    show ta 008 with dis

    ta "「Uh, no, that was it. 」"
    
    show si 010 with dis

    si "「Did Amaki do something? 」"
    ta "「Well, it wasn't anything like that. 」"
    si "「... 」"
    
    show ta 005 with dis
    
    ta "「... 」"

    show si 009 with dis

    "W-what is this feeling?\nWhatever it is, it's swirling in the silence\nin front of the candy shop."
    fn "「H-hey. 」"
    "Even as the atmosphere overpowered me,\nI tried to greet them cheerfully."

    show si 001
    show ta 002
    with dis

    ta "「Oh, well if it isn't [fn]. 」"
    si "「Good day. 」"
    fn "「Afternoon you two.\n\ \ Strange how we're meeting like this, here. 」"
    
    show ta 001 with dis
    
    ta "「Really? I come here often enough. 」"
    si "「I come sometimes myself. 」"
    fn "「Huh. Is that so? 」"
    "Tatsu-nii I can see, but Shin and these sweets...?{p}No wait, I shouldn't be so prejudiced."
    
    show ta 002 with dis
    stop music fadeout 1

    ta "「Isn't that a surprise? 」"
    
    show si 010 with dis

    si "「Is that so strange? 」"
    
    show ta 006 with dis
    play music oo39_cho_ys001

    ta "「No, that's not what I meant.. 」"
    si "「Even I eat cheap candies. 」"
    ta "「Sorry. 」"
    
    show si 009 with dis
    
    si "「No, I wasn't getting at... 」"
    ta "「... 」"
    si "「... 」"
    "A-are these two...{w=.3}\nHolding a conversation!?\nIs it because of that strange atmosphere before?"
    "What should I do?"

    menu:
        "A. Talk to Tatsuki":
                jump candy03_tatsuki
        "B. Talk to Shin":
                jump candy03_shin

######################################
label candy03_tatsuki:

    $ event_name = _("Do you come here a lot, Tatsu-nii?")
    $ love_tatsuki += 1

    play music daily04

    fn "「You come here often, Tatsu-nii? 」"
    
    show ta 002 with dis

    ta "「Sure do.{w} I missed those old familiar tastes. 」"
    
    show si 001 with dis

    fn "「Yeah, I get that.\n\ \ I sometimes have this weird craving for them. 」"
    ta "「I know, right? 」"
    si "「Because it's a simple taste, right? 」"
    fn "「Yeah, yeah.\n\ \ It's just so good! Well, not always,\n\ \ but I miss it for some reason. 」"
    
    show ta 001 with dis

    ta "「Probably because you're Japanese. 」"
    si "「... 」"
    fn "「It must be carved into my DNA. 」"
    
    show si 009 with dis

    si "「I... 」"
    
    show ta 002 at hit_right
    play sound bosu32
    show si 005 at jump_up
    
    ta "「Japanese, right?\n\ \ You've lived here for so long after all. 」"

    si "「Eh? 」"
    
    show si 011 with dis

    si "「T-thank you very much... 」"
    fn "「? ...Oh, right.\n\ \ That reminds me,{w=.3} isn't Shin-kun...? 」"
    
    show si 001 with dis
    
    si "「... 」"
    
    show si 010 with dis
    pause 1
    hide si with dis
    
    si "「This one, please. 」"
    shopkeep "「Thank you, come again. 」"
    
    show si 001 at midright behind ta with dis
    
    si "「Uh, see you Tatsuki-san, [fn].\n\ \ Later. 」"
    
    show ta 001 with dis

    ta "「See you later! 」"
    fn "「Oh, yeah.{w=.3} See you. 」"
    
    hide si with wipe_right

    "Shin-kun quickly bought something,\nthen left the building just as quickly.\nI guess he doesn't really want to touch this subject."
    "I've never really understood the differences\nsince back then..."
    "As I saw off that small retreating back,\nI started talking to Tatsu-nii again."
    fn "「...Say, Tatsu-nii,\n\ \ I don't really know myself, but does it\n\ \ look like Shin-kun's changed all that much? 」"

    show ta 008 with dis

    ta "「Yeah, I guess his face is like a foreigner's. 」"
    ta "「After that, I don't really get it,\n\ \ but you can apparently see the difference\n\ \ in the way his hair looks and feels. 」"
    fn "「I see... I can't tell at all. 」"
    
    show ta 010 with dis

    ta "「His clumsiness is probably because\n\ \ of the distance between him and other people.{p}\ \ Well,{w=.3} that probably isn't everything. 」"
    fn "「Huh. 」"
    "So he's of mixed heritage."
    "I guess if it were a human analog,\nand I suddenly saw a transfer student\nwith different hair and skin color..."
    "I think I'd... most likely be staring in curiousity.{p}Is that what Shin-kun's been feeling all this time?"

    show ta 008 with dis
    
    ta "「It's probably gotten even more intense than before,{w=.03}\n\ \ but I can't really get on well with him.{p}\ \ I always try talking to him, but it ends up that way. 」"
    fn "「So... You two don't get along? 」"
    
    show ta 010 with dis

    ta "「Well I wouldn't go that far.{w=.3}\n\ \ I just can't carry on a conversation with him.{p}\ \ For me, if he were more gracious it'd be easier. 」"
    fn "「Is that so. 」"
    "Shin-kun and Tatsu-nii...{w=.3}\nI guess they don't really have much in common.{p}Is that how that mood came about?"
    
    show ta 002 with dis

    ta "「But never mind that, [fn].\n\ \ Since you're here, wanna buy something?\n\ \ I'll treat you. 」"
    fn "「Huh? Is that okay? 」"
    ta "「Sure. {w=.3}Pick whatever you want. 」"
    fn "「Yay!\n\ \ In that case this, this, and this... 」"
    ta "「Hey, hey.\n\ \ You won't be able to eat dinner\n\ \ if you eat that much candy. 」"
    fn "「It's fine. Sweet stuff goes into a different stomach. 」"
    ta "「Gahaha.\n\ \ It's almost like you're Kounosuke. 」"
    "Well if you're saying that,{w=.3}\nthen I'm gonna buy even more,{w=.3} so I added more\nthings to the basket for Tatsu-nii to pay for."
    "Thanks to that, the stuff I had to pay\nfor was pretty light."
    
    jump end03

#####################################
label candy03_shin:
    
    $ event_name = _("What's Shin-kun's favorite?")
    $ love_shin += 1
    
    play music daily04
    
    fn "「What do you like, Shin-kun? 」"
    
    show si 001 with dis
    
    si "「Eh? 」"
    
    show ta 001 with dis
    
    fn "「From the sweets. 」"
    
    show si 010 with dis

    si "「...This, I guess. 」"
    "A f-five yen chocolate?{p}That's surprisingly..."
    
    show si 009 with dis

    si "「Weird, isn't it? 」"
    fn "「No, I don't think so at all. 」"
    si "「... 」"
    fn "「How about you Tatsu-nii? 」"
    
    show ta 002 with dis

    ta "「Me? I like this one. 」"
    
    show si at move_offleft(2)
    
    "Ikataro snacks in miso cuts, and with plum.\nThat somehow fits my image of him."
    fn "「Oh, I like those too. 」"
    
    show ta 001 with dis
    
    ta "「Oh, you get it don't you?\n\ \ And if you fry them in direct heat,\n\ \ they taste even better. 」"
    fn "「Wow. 」"
    si "「Excuse me. Could you ring this up? 」"
    
    shopkeep "Of course. Thank you, come again."
    
    show si 001 at midright behind ta with dis
    
    si "「Well then Tatsuki-san, [fn], later. 」"
    
    show ta 006 with dis

    ta "「O-okay then. 」"
    fn "「Oh, uh, all right. 」"
    
    hide si with wipe_right
    
    "Before we noticed it, Shin-kun made\nhis purchase,{w=.3} then gave us a little\nwave as he left."
    "I wanted to talk with him a little more...{w=.3}\nMy eyes kept watching that little back\nuntil it went around the corner."
    
    show ta 008 with dis

    ta "「...[fn]. 」"
    fn "「Eh? What? 」"
    
    show ta 010 with dis

    ta "「You should go after him if it bothers you. 」"
    fn "「Huh? 」"
    ta "「You probably have an easier time talking to him\n\ \ than I do.{w} Just go talk to him. 」"
    fn "「...All right, I got it.\n\ \ Sorry Tatsu-nii. 」"
    
    show ta 002 with dis

    ta "「Don't worry about it. 」"
    "As he urged me on,\nI left Tatsuki at the shop while chasing after Shin. "
    
    scene black with Dissolve(1)
    stop music fadeout 1
    pause .3
    
    scene path
    show si 001 at center
    with Dissolve(1)
    
    fn "「Shin-kuuun! 」"
    
    play music piano3_015

    si "「[fn]? 」"
    "Since I went after him right away,\nit didn't take much time to catch up."
    si "「Is something the matter? 」"
    fn "「It's not that,{w=.3}\n\ \ it's just we just met up and you're already gone! 」"
    
    show si 010 with dis
    
    si "「Sorry. 」"
    fn "「It's nothing. 」"
    
    show si 009 with dis
    
    si "「...Tatsuki-san is... Not very good at things. 」"
    fn "「Eh? H-how so? 」"
    "When we were alone, Shin-kun suddenly spoke up.{p}Based on the mood earlier,\ndid something happen between them?"
    
    show si 001 with dis

    si "「Nice people take the time to understand me.{p}\ \ {nw}"
    show si 009 with dis
    extend "But Tatsuki-san didn't even keep a little distance. 」"
    fn "「Some distance? 」"
    si "「Yeah...{w} {nw}"
    show si 001 with dis
    extend "It's strangely childish, but he's older.\n\ \ If there was someone else, it might work,\n\ \ but if it's just us, the conversation just dies. 」"
    
    show si 010 with dis
    
    si "「It'd be nice if I were\n\ \ a little better at talking though. 」"
    si "「Or possibly if Tatsuki-san were the type\n\ \ to keep people further at range. 」"
    "I see then.\nSo that's how that mood came about."
    fn "「You two are incompatible. 」"
    
    show si 001 with dis
    
    si "「{cps=10}I... {cps=40}Guess.{w} That could be true. 」"
    "How was it back then?{p}No wait, back then,\nShin-kun was even more reserved."
    "And he probably never had many settings\nwhere he talked with people."
    
    show si 003 with dis

    si "「I probably should have had a bit more grace. 」"
    fn "「No I think you're good there. 」"
    "I thought Shin-kun was the type to not consider others,\nbut he's surprisingly bothered by it."
    fn "「Oh, that aside, what did you buy? 」"
    
    show si 001 with dis

    si "「This. 」"
    "5 yen chocolate, cotton candy, starch syrup...\nIt really clashes with his stylish dress,\nhe has a bag stuffed full of cheap candies."
    
    show si 002 with dis

    si "「Want to have some while we walk? 」"
    fn "「Huh? Is that okay? 」"
    si "「Go ahead. 」"
    fn "「Thanks. Then I'll pick... 」"
    "Oh,{w=.3} yeah,{w=.3} huh,{w=.3} often times when we were all heading\nback, we'd share candy while walking like this.\nEven if we knew we'd get yelled at if found out."
    "...{p}Wait, what?{p}But Shin-kun..."
    si "「... 」"
    "I looked at the profile of the one\nwalking along licking at the syrup.\nShin-kun didn't even do this back then though..."
    si "「This is nice... 」"
    fn "「Y-yeah. 」"
    "Could it be that he's always wanted to do this?"
    "As I saw that wide natural smile coming on that face,\nI felt like I glimpsed at the feelings\nof my moody childhood friend."
    
    jump end03

#########################################    
label shun03:
    
    $ event_name = _("His Strongest Weapon, Once Again")
    $ focus_character = "shun"
    $ love_shun += 1
    
    scene map
    stop music
    hide screen park03
    scene black with Dissolve(1)
    scene park red with Dissolve(2)
    play sound kara00
    pause 1.2
    show su 010 red with sdis
    play music free58
    
    su "「Uu......Unyu...... 」"
    
    "N-no!{p}I didn't mean to make you cry!{p}Aaah, if this keeps up I'll definitely..."
    
    scene black with Dissolve(1)
    stop music fadeout .5

    "This story goes back to around noon."
    
    scene path with Dissolve(1)
    play music cicada01
    
    fn "「Ugh... 」"
    "On the unpaved road, waves of heat rise up."
    "I haven't been to my hometown for so long,\nI didn't take this into consideration\nfrom being so used to living in the city."
    "I'm only here for a month.\nUnlike my usual summer vacations,\nI won't waste it lying around!"
    "So I gathered my strength,{p}and used up my luck to head out just past noon."
    "The endless blue sky.{p}From the thunderheads to the sunflowers,\nand the voices of the cicadas."
    "Even though I'm receiving this warm reception\nfrom the sun in the height of summer,\nmy awareness is only half there."
    fn "「It's so hot... 」"
    "Not only is my shirt soaking with sweat,{p}even down to my socks are too."
    "I didn't bring a hat and a towel.{p}I already want to go back."
    "Huh? Somebody's running up from over there? {p}In this heat?"
    
    show su 002 big at center_big with dis
    
    su "「[fn]-saaan♪ 」"
    fn "「Aah. Shun-ku-, oof. 」"
    
    hide su with dis
    play sound puu75
    
    su "「Hehee♪{w=.3} [fn]-san. 」"
    "It's hot."
    "With an appearance that could be mistaken\nfor a child, my childhood friend,{w} tail wagging\nback and forth,{w} mercilessly clings to me."
    
    show su tailwag 01 at center with dis
    
    su "「Good afternoon♪ 」"
    "Yeah, good afternoon.{w} I can't return his greeting\nas a higher body temperature is being transmitted\nfrom his tiny body, and is gradually heating me up."
    "I-{w=.3}I'm being embraced by a beastman!{p}Except my patience to itch is unbearable."
    "I come to understand that this is limited to\na well air-conditioned environment."
    "Fuaah, my brain seems to have become shoronpo.{p}His arms and muzzle are concealed in fur,{p}now I'm thinking of other cute things..."

    show su 015 with dis
    
    su "「?{w=.3} [fn]-san? 」"
    fn "「Oh, uhh, good afternoon. 」"
    "...But he is cute.{p}He anxiously looks up at me with his acorn eyes."
    "When my moderately steamed brain\nis about to state its cheap thoughts,{p}Shun-kun releases me."
    
    stop music fadeout 1
    play music pops_003
    show su 001 with dis
    
    su "「[fn]-san, are you out for a walk? 」"
    fn "「Yeah, I ended up here.{p}\ \ I'm going back soon though. 」"
    
    show su 005 with dis
    
    su "「What!? Let's go play together! 」"
    "My arm is being pulled."
    "This cute, one-year-below-me wolf\nis getting all fired up,\ndespite the direct rays of the sun."
    
    show su 002 with dis
    
    su "「So, [fn]-san? 」"
    "Guh, his whole face dazzles greater than the sun."
    "From the bottom of his heart,\nhe seems to be happy that he ran into me.{p}Shun-kun repeatedly invites me to go somewhere."

    show su tailwag 01 with dis
    
    "The antenna above his head, possibly a feeler,{p}nowadays called an ahoge, shakes."
    "Is that him expressing his joy\nof picking up my signal?"
    "Or is it just blowing in the wind?{p}Maybe it was a hallucination."
    "If I were ever to take him to an amusement park he\nwould have to promise to shake his ahoge and tail."

    show su 004 with dis
    
    "Besides that, he's short too.{p}He hasn't stopped growing,{w=.3} has he?"
    "Is he eating right?"
    "Isn't it bad for him if he's just\neating things like noodles?{p}Properly adding blanched meat and sashimi..."
    su "「[fn]-san? 」"
    "Delirious with heat,{w=.3}\nmy thoughts completely change to the trip scene."
    "Around the time I'm about to check his\neating habits, {w=.3}he calls out my name a second time."
    su "「Is it cooler out here than it is at home? 」"
    "Dazedly ignoring him,\nI think about the wind of the air conditioner.{p}Anyways, rather than having gone out..."
    
    show su 002 with dis
    
    su "「I know! {w=.3} How about we go to the river? 」"
    "River?{p}He said the river... oh, that's right."
    
    stop music fadeout .5
    play music water03
    
    "There's one here in Minasato.{p}Suddenly, memories from my childhood come to mind."
    "The nostalgic, light sound of the stream."
    "I know what he means now,\nnot the stagnated water of the city."
    
    stop music fadeout .5
    
    fn "「Shun-kun! 」"
    
    show su 004 with dis
    
    su "「Wah, wawah? Yes? 」"
    fn "「Take me there. 」"
    "As if my consciousness was suddenly awoken,{p}I snap out of it."
    "That would be a way for us to drive away\nas much of this heat as we want, wouldn't it?"
    
    play music pops_003
    show su 002 at jump_up
    
    su "「Yaay! Let's go! 」"
    "Shun-kun leads me while skipping and jumping.\nI follow behind him.{p}Even though sweat runs down me, I feel refreshed."
    
    $ event_name = _("Let's go play")
    
    stop music fadeout 1
    scene black with Dissolve(1)
    pause .4
    scene river with Dissolve(1)
    play music water03
    show su 201 at center with dis
    
    su "「Hanyaa, it's cold♪♪ 」"
    fn "「Haah... haah... haah... 」"
    
    show su 202 with dis
    
    su "「Hehe, this feels nice. 」"
    "Water trickles down Shun-kun's small body.{p}He suddenly undressed and started\nswimming in only his underwear."
    "A perfect score in the true spirit of summer."
    su "「[fn]-san, you come too please! 」"
    "My cooled-down brain begins to operate{p}in full swing."
    "The nostalgia from earlier{p}is lightly overwritten by lust."
    fn "「Umm, I'm cool enough right here. 」"
    
    show su 201 with dis
    
    "While enjoying the cool air at the river's edge,{p}I delightfully enjoy the view of my childhood\nfriend playing by himself."
    "Add in that splashing around\nand I won't be able to endure it."
    "He'll do that one thing where he'll take off his\nunderwear after swimming when he takes a break."
    "He'll wring out the water, hang them to dry on a\ntree around here, but forget to take them home.{p}Then I hope he'll say a clichéd line."
    "But Shun-kun is diligent, he probably brought{p}1 or 2 changes of underwear in a bag."
    "So {w=.5}that means it shouldn't be a problem even {p}if I take home a half-dried one."
    
    show su 204 with dis
    
    su "「...[fn]-san? Are you okay?{p}\ \ You're spacing out. 」"
    
    play sound bosu29
    
    fn "「!{w}  {nw}"
    play sound bosu32
    extend "I'm fine!\n\ \ {w=.3}{nw}"
    play sound bosu35
    extend "I wasn't thinking about wanting underwear! 」"
    
    su "「...? 」"
    
    stop music 
    scene black with dis
    pause .2
    
    scene shrine red
    show su 001 red at center
    with dis
    play music free51
    pause .1
    show su at jump_up
    
    su "「You're going to this year's Bon Festival too,{p}\ \ aren't you?♪ 」"
    fn "「That's right, it's been five years\n\ \ since the last time... 」"
    "Speaking of the festival,\nthat means yukata and fundoshi.\nUfufu, I'm looking forward to it ehehehehe."
    
    show su tailwag 01 red with dis
    
    "Shun-kun sits on the shrine grounds\nand swings his legs."
    "If I can expect to catch intermittent views of his\nbutt at the edge of his happi coat, then I'm not\ngoing to be carrying around the portable shrine."

    show su 004 red with dis
    
    "From a formal and hypothetical scientific\nperspective, {w=.3}this place is absorbed\nin the ordinary to the extraordinary."
    "I'll take on things I normally can't do!"
    su "「...[fn]-san? Are you okay?{p}\ \ You're spacing out. 」"
    
    play sound bosu29
    
    fn "「!{w}  {nw}"
    play sound bosu32
    extend "I'm fine!{p}\ \ {nw}"
    play sound bosu35
    extend "I wasn't thinking of wanting\n\ \ to carry you on my shoulders! 」"
    
    su "「...?? 」"
    
    stop music fadeout 1.5
    scene black with Dissolve(1)
    
    $ event_name = _("Although I was Spacing Out")
    
    "We walk around Minasato Village.{p}As one would expect, I'm a little tired."
    "I suggest to Shun-kun, who's still energetic,{p}that we take a break in the park."
    
    scene park red with sdis
    play sound kara00
    pause 1.2
    
    "Then he asked me\nwhy I didn't come back for 5 years."
    
    play music free58
    show su 002 red with dis
    
    "「I'm glad you came back 」, and{p}「Why did you come back? 」.{p}「I got a letter from Torahiko 」, I explained."
    
    show su 001 red with dis
    
    "「Funyuu, You came back to meet Torahiko-san 」,{p}he says."
    "「No, well, I was anticipating\nto see how much Torahiko has grown,\nbut I came back to meet everybody 」,{w} I tell him."
    
    show su 004 red with dis
    
    "H-huh?{p}His ears and tail have dropped."
    "「Then I should have written a letter too,\nfunyuun 」,{w} he says."
    "Shun-kun thinks that I\nonly came back for Torahiko.{p}...What?"
    "「It's not easy to come back, isn't Minasato far? 」{p}I continue the conversation, but when I look over,\nShun-kun begins to tremble sadly."
    
    show su 003 red with dis
    
    "His eyes break into tears mode.{p}N-no!{p}Aaah, if this keeps up I'll definitely..."
    
    show su 012 red at shivering with dis 
    
    su "「Uu, fuku, eku...... 」"
    "This is bad.{p}If a third party happens to pass by,\n{w=.3}they'll think I made this little wolf cry."
    "And I'll be suspected of abuse{p}or kidnapping or other unspeakable things."
    "I'll be taken directly to the village's only\npolice station for execution, {w=.3}no doubt about it."
    "I once again learn the destructive power{p}of Shun-kun's tearful face."
    "Just by doing this in front of me, {p}I'm seized by all these feelings of guilt."
    "...I wonder,{w=.3} has it been this long?"
    "Anyways, how do I get Shun-kun to stop\ncrying in this situation?"
    "There's almost nothing to do but cry myself.{p}A. Stop Shun's crying{p}B. Cry myself"
    "There's no need to choose.{p}I extend a finger to wipe away\nthe tears on Shun-kun's cheek."
    
    show su 016 red at still with dis 
    
    su "「Hyan... 」"
    fn "「Don't cry, Shun-kun. 」"
    su "「...Uku 」"
    fn "「I didn't come back just for Torahiko...? 」"
    
    show su 003 red with dis
    
    su "「Th-that's not it...{w} Hafu 」"
    "Huh?"
    
    show su 004 red with dis
    
    su "「I've been thinking about the reason\n\ \ why you didn't come back. 」"
    su "「At Kazenari School,\n\ \ I've studied things about the city... 」"
    su "「I also talked with\n\ \ Kounosuke-san and heard about it. 」"
    su "「Then, I realized there are no\n\ \ {w=.3}{cps=10}convenience stores{cps=40}, or {cps=10}amusement parks,{cps=40} or\n\ \ {cps=10}E-se-ho-so{cps=40} in {w=.3} Minasato... 」"
    "Not used to pronouncing those words,{p}Shun-kun awkwardly mumbles."
    
    show su 016 red with dis
    
    su "「So you...{p}\ \ didn't come back... *sniffle* 」"
    su "「That's what I've been thinking about. 」"
    "Hii~ii~ii.{p}Minasato certainly is rural to the max,{p}but it seems that I'd come close to crushing him."
    
    show su 010 red with dis
    
    su "「When I was playing earlier, you were spacing out{p}\ \ because the village is boring to you, isn't it... 」"
    "「That was in response to my uncontrollable lust\nfor underwear and bare legs."
    fn "「I-I was spacing out because I wanted to burn\n\ \ every one of your actions into my retinas!{p}\ \ ...wait, no! 」"
    
    scene park red
    show su 010 red
    with Dissolve(.5)
    
    $ event_name = _("Hugging Tightly")
    
    "I gave up all the adventures I could have\nduring summer vacation in the city,\n{w=.3}and decided to spend August here."
    "That doesn't mean I don't have regrets though."
    "But that's......"
    fn "「That's not it! 」"
    
    hide su with qdis
    
    su "「Fu, fueh!? 」"
    "Squeeze.{p}I hold him close, and feel a different smallness."
    "I try to wipe away his tears again\nwith my wrist and he pushes into my chest."
    su "「[fn]{w=.3}-san... 」"
    "Thump,{w=.3} thump.\nI can definitely hear his heart beating."
    "With his whole tiny body as a sound board,{p}his heartbeat resounds."
    fn "「There are a lot of things in Minasato\n\ \ that aren't in the city, right?! 」"
    su "「... 」"
    fn "「...Shun-kun? 」"
    su "「...yeah. 」"
    
    show su 004 big red at center_big with dis
    
    "I focus on Shun-kun's clouded eyes."
    fn "「Can't I only see you here in Minasato? 」"
    fn "「So don't cry. I didn't come back\n\ \ to see that kind of face. 」"
    su "「B-{w=.3}but... 」"
    "I put both my hands on his shoulders,\nget to his eye-level, and continue."
    fn "「I reeeally wanted to see everybody,{p}\ \ isn't that true? 」"
    su "「Uu... 」"
    fn "「Shun-kun, Torahiko, Tatsu-nii, Kounosuke,\n\ \ {w=.3}Kyouji, Shin-kun, Juuichi-san, Kouya,\n\ \ {w=.3}and now Soutarou-kun too, right? 」"
    "I didn't put any thought\ninto the order of their names."
    "Or maybe I should say that\nit wouldn't surprise me later."
    fn "「All of my friends are important to me. 」"
    
    show su 003 big red with dis
    
    su "「[fn]-san... 」"
    fn "「I love you, and everybody else too. 」"
    "I say with a wink."
    "Between the coolness of the city\n+ it's comforts + microwave oven meals\nor the full course of Minasato's beastmen,"
    "Of course I'd always choose the latter,\nwouldn't I?{w} Yeah!"
    
    show su 002 big red with dis
    
    su "「...Okay. 」"
    
    hide su with qdis
    play sound puu75
    
    su "「Hehee♪{w=.3} [fn]-san. 」"
    "It's hot."
    "When I see that Shun-kun is in an\nadhesive state again, I'm relieved.{p}\"Love\" seems to have been effective, that's good."
    "At last his mood has recovered."
    "With this, I'll be able to spend my summer vacation\nwithout the finger of scorn being pointed at me\nbehind my back..."
    
    show su 004 red at center with Dissolve(1)
    
    su "「B-but... 」"
    fn "「Wha- whawha-{w=.3} What? 」"
    "H-have I still not been able\nto smash that element of anxiety?!"
    
    show su 010 red with dis
    
    su "「[fn]-san,{p}\ \ You're going back once your summer vacation\n\ \ is over,{w} aren't you...? 」"
    "Shun-kun stares up at me with big round eyes.{p}I feel like I've done\nsomething extremely terrible."
    "I can't stand those cute and sad eyes any longer,{p}{nw}"
    hide su with qdis
    extend "I squeeze him, and push his head\ninto my chest once again."
    
    fn "「Let's get plenty of play time! 」"
    su "「Mmf, mmmf, [fn]-sa- mmmfmmf 」"
    fn "「This summer has only just begun! 」"
    
    stop music fadeout 1
    play music pops_003
    show su 002 red at center with dis
    
    su "「Y-you're right! 」"
    "He releases from my hugging arms,\nlooks at me, then smiles again.\nThat went well, I skillfully avoided... Huh?"
    
    show su at jump_up
    
    su "「The beach!{w=.3} Let's go to the beach! 」"
    fn "「Oh yeah, we were talking about\n\ \ that the other day 」"
    su "「And then the Bon Festival,{p}\ \ {nw}"
    show su 001 red with dis
    extend "and the mountains over there,{nw}"
    hide su
    show su tailwag 01 red with dis
    extend "{p}\ \ and umm, ummm... 」"
    
    scene black with sdis
    
    "I've come back to my valuable hometown,\nfull of distant memories."
    "I'll have lots of fun.{p}My summer vacation has just begun."

    jump end03

#######################################
label end03:
    
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
    
    jump day04


    
    
    
