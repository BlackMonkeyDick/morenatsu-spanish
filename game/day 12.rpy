## Day 12

screen shrine12:
    hbox:
        add "arrow up"
        at shrinebounce1
    hbox:
        add "icon_kouya"
        at shrinebounce2
    hbox:
        text "Minasato Shrine"
        xalign .16 yalign .12
screen tatsukihouse12:
    hbox:
        add "arrow right"
        at tatsukibounce1
    hbox:
        add "icon_tatsu"
        at tatsukibounce2
    hbox: 
        text "Tatsuki's House"
        xalign .85 yalign .88
screen riverbed12:
    hbox:
        add "arrow down"
        at riverbounce1
    hbox:
        add "icon_juu"
        at riverbounce2
    hbox: 
        text "River"
        xalign .625 yalign .7
        
screen minasatomap12a():
    add "map"
    add "mapdate"
    imagebutton idle "a icon" hover "icon loop" xpos 164 ypos 104 action Jump("kouya12") hovered Show("shrine12")  unhovered Hide("shrine12") hover_sound "av/audio/click_008.wav"
    hbox:
        text "{size=+30}August 12"
        at maptime
        
screen minasatomap12b():
    add "map"
    add "mapdate"
    imagebutton idle "a icon" hover "icon loop" xpos 164 ypos 104 action Jump("kouya12") hovered Show("shrine12")  unhovered Hide("shrine12") hover_sound "av/audio/click_008.wav"
    imagebutton idle "a icon" hover "icon loop"  xpos 458 ypos 351  action Jump("juuichi12") hovered Show("riverbed12")  unhovered Hide("riverbed12") hover_sound "av/audio/click_008.wav"
    hbox:
        text "{size=+30}August 12"
        at maptime  
        
screen minasatomap12c():
    add "map"
    add "mapdate"
    imagebutton idle "a icon" hover "icon loop" xpos 164 ypos 104 action Jump("kouya12") hovered Show("shrine12")  unhovered Hide("shrine12") hover_sound "av/audio/click_008.wav"
    imagebutton idle "a icon" hover "icon loop"  xpos 662 ypos 391  action Jump("tatsuki12") hovered Show("tatsukihouse12")  unhovered Hide("tatsukihouse12") hover_sound "av/audio/click_008.wav"
    hbox:
        text "{size=+30}August 12"
        at maptime            
        
screen minasatomap12d():
    add "map"
    add "mapdate"
    imagebutton idle "a icon" hover "icon loop" xpos 164 ypos 104 action Jump("kouya12") hovered Show("shrine12")  unhovered Hide("shrine12") hover_sound "av/audio/click_008.wav"
    imagebutton idle "a icon" hover "icon loop"  xpos 458 ypos 351  action Jump("juuichi12") hovered Show("riverbed12")  unhovered Hide("riverbed12") hover_sound "av/audio/click_008.wav"
    imagebutton idle "a icon" hover "icon loop"  xpos 662 ypos 391  action Jump("tatsuki12") hovered Show("tatsukihouse12")  unhovered Hide("tatsukihouse12") hover_sound "av/audio/click_008.wav"
    hbox:
        text "{size=+30}August 12"
        at maptime
        
#########################################
label day12:
    
    $ renpy.music.set_volume(1.0, 0.0, channel = "music")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound2")
    
    $ day = 12
    $ event_name = "８月12日"
    $ the_date = "August 12"
    $ focus_character = ""
    
    window hide
    play music birds_chirping
    
    scene sky01 
    show text "{size=+130}August 12" at truecenter
    with Dissolve(.5)

    pause 3
    scene black with Dissolve(1)
    pause .4
    
    scene hbroom with wipe_corner
    
    fn "「I wonder what I should do today. 」"
    
    play music "<from 2.5>av/audio/free0422.ogg"
    
    if part_time == True:
        if juuichi_hate == False:
            call screen minasatomap12d
        else:
            call screen minasatomap12c
    elif juuichi_hate == False:
        call screen minasatomap12b
    else:
        call screen minasatomap12a
  
##################################################        
label juuichi12:

    $ event_name = "Soutarou's Worries"
    $ love_juuichi += 1
    $ focus_character = "juuichi"

    scene map
    hide screen riverbed12    
    scene riverbank with dis
    play music cicada01

    "In the midst of a chorus of cicadas,{w=.2}\nI steadily walk along the river bank."
    "Clear water flows beside me.{p}Man, it'd feel good to jump into that."
    "I'm thinking like an elementary school kid."
    "...Hell, there are so few people out\nhere in the countryside,{w=.2}\nI probably could go skinny-dipping if I wanted."
    "...Of course any person would think that."
    "It'll be okay if I cool off a little, right?{p}My feet are tired from walking too,\nso this is a good time."
    "I place my feet in the river,\n{w=.2}{nw}"
    play sound step13b
    extend "And push my way through the reeds."
    
    scene black with wipe_right
    scene river with wipe_right
    play music water03

    fn "「Whew,{w=.2} I needed this... 」"
    "A few minutes later,{p}I'm soaking in the clear water up to my shins,{w=.2}\nand I sigh with satisfaction."
    "Being warmed by the sun and cooled by the water\nat the same time is conflicting."
    "It's probably natural to feel this way during\nsummer, but it feels somewhat fresh."
    "Maybe it's simply because the water is so nice,{w=.2}\nand I'm in this peaceful village\ninstead of the hectic city."
    "...Is it like me to think of things like that?"
    "I try kicking one of my legs.{p}{nw}"
    play sound water01
    pause .3
    play sound water01
    extend "The sound of splashing is mixed with the cicadas.{p}I get cooler from the splash getting me more wet."
    "Ah, did I get my clothes wet?{p}...Oh well, I'm sure they'll dry in the sun.{p}I keep doing it."
    "I try kicking my leg as hard as I can.{p}{nw}"
    play sound water01
    pause .3
    play sound water01
    pause .5
    play sound water01
    extend "The droplets of flying water glitter in the sun.{p}I keep splashing, not caring how wet I get."
    "For a short while, I play in the water like that."
    fn "「...? 」"
    "I could swear I just heard a voice.{p}There shouldn't be anyone nearby, though..."
    
    pause 1

    "Oh.{p}There is somebody.{p}And it's people that I know."
    "A short way down the river,{w=.2}\nJuuichi-san is walking with Soutarou-kun."
    "They're deep in discussion,{w=.2}\nand don't seem to notice me."
    "With a bit of trouble, {nw}"
    play sound mizu07
    extend "I step out of the water.{p}After all, 2 people are more than 1,\nand 3 people is more than 2!"
    "I didn't bring a towel with me.{w=.2}\nI guess I can just use my socks to dry off.{p}I'll stick my wet socks in my pockets for now."
    
    stop music fadeout 5
    
    "...Okay. I'm done putting my shoes on.{p}{nw}"
    play sound step03
    extend "I run along the gravel, taking care not to trip.{p}I greet them as I approach."
    fn "「Hey!{w=.2} Juuichi-san,{w=.2} Soutarou-kun! 」"
    
    play music daily03
    show ju 001 at midright
    show so 001 at midleft
    with wipe_right

    ju "「...[ln]? 」"
    so "「Oh, good afternoon, Senpai! 」"
    "There's quite a contrast in their greetings.{p}I guess Soutarou-kun is yang,{w=.2}\nand Juuichi-san is ying?"
    "...No, while Juuichi-san certainly is surly,\nI don't think that's true."
    ju "「...Why are you here? 」"
    fn "「I was just cooling off a bit. 」"
    "I look behind me as I say that.{p}Juuichi-san gets my meaning."
    fn "「So,{w=.2} what are you two up to? 」"
    ju "「Well,{w=.2} Touno called me up.{p}\ \ There's something he wanted to talk to me about. 」"
    "Upon hearing what he says,{w=.2}\nI tilt my head in confusion."
    fn "「Huh? He didn't call Kyouji? 」"
    "I'm sure Soutarou-kun has\nquite a lot of respect for Kyouji."
    "I don't know him very well,\nbut even I can tell that when I see him."
    "That's why it seems out of place for him\nto call Juuichi-san instead of Kyouji."

    show ju 003 with dis

    ju "「That's what I thought, too.{p}\ \ I asked him why he didn't talk to Takahara. 」"
    
    play sound bom35
    show so 005 at briefzoom

    so "「No,{w=.2} Takahara-senpai can't know about this! 」"
    
    show ju 001 with dis

    ju "「...So,{w=.2} here we are. 」"
    fn "「I see...{p}\ \ Something he can't talk to Kyouji about, huh? 」"
    ju "「Correct. 」"
    "Juuichi-san glances over at Soutarou-kun.{p}I guess he's saying I should decide whether\nor not to talk to him myself."
    "When I take a closer look at him,{w=.2}\nSoutarou-kun's face doesn't have its usual cheer.{p}It's kind of... Gloomy, I guess?"
    "He looks troubled for quite a long time,\nbut eventually looks towards me with resolve."
    
    show so at jump_up

    so "「Um,{w=.2} Senpai,{w=.2}\n\ \ how do I get bigger? 」"
    "I think I'm missing something here.{w=.2}\nHe wants to get... Bigger?"
    "What does he mean?{p}What's bothering Soutarou-kun is..."
    
    menu:
        "A. His body?":
            jump juuichi12_body
        "B. What?":
            jump juuichi12_stick

    ###############################################
    label juuichi12_body:

        $ event_name = "Sleep Brings Up a Child Well"
        $ love_juuichi += 1
        $ love_soutarou += 1
    
        "Hmm, I wonder...{p}Do soccer players body-build too?"
        fn "「I see,{w=.2} you want a better physique? 」"
    
        show so 003 with dis
    
        so "「Yeah!{w} 　That's right! 」"
        "He nods vigorously.{p}I can't help but laugh at the honest\nway he expresses himself."
        
        show so 005 with dis
    
        so "「...Senpai,{w=.2} did I say somethin' weird? 」"
        fn "「No,{w=.2} it's nothing.{p}\ \ I just remembered something funny. 」"
        so "「...Huh,{w=.2} really? 」"
        "He tilts his head, confused.\nI clear my throat to try and\nworm my way out of this situation."
        ju "「Just having a good physique is\n\ \ often an advantage in sports. 」"
        
        show so 001 with dis
        
        "Hearing what Juuichi-san says,{w=.2}\nSoutarou-kun voices his agreement."
        "...There's still something he's not telling us.{p}I can tell, just by looking at him."
        so "「I really want a slim, athletic body.{w=.2}\n\ \ Just like Takahara-senpai! 」"
        fn "「Ah,{w=.2} Kyouji definitely is the slim type. 」"
        "Juuichi-san nods in confirmation."
        "...Hm? Wait."
        "Juuichi-san isn't in the same club as Kyouji.\nHow often does he see him naked?{w=.2}\nThat's going to bother me for a while."
        "...Now that I think about it,{w=.2}\nI'm pretty sure they're in the same class.{p}I'm sure there would be plenty of chances, right?"
    
        show ju 008 with dis
        
        ju "「...I doubt you've finished growing yet.{w=.2}\nYou shouldn't push yourself too hard, you know? 」"
        
        show so 005 at jump_up
    
        so "「Huh?{w=.2} Really? 」"
        "Soutarou-kun's voice rises in surprise."
        fn "「Oh, I think I've heard about that.{p}\ \ If you train too hard,{w=.2}\n\ \ you can't support the weight of your muscles. 」"
        fn "「In the worst case, you actually shrink, right? 」"
        "It may seem like I'm making that up,\nbut I did actually see that on television."
        
        show so at shivering
    
        so "「Shrink...?! 」"
        "Soutarou-kun shudders in shock at what I said.{p}...That was more of a reaction that I expected."
        
        show ju 001 with dis
        show so at still
    
        ju "「Well, it's best to be careful.{p}\ \ Don't use weights that are too heavy,{w=.2}\n\ \ stick to push-ups and squats. 」"
        ju "「Don't forget to eat well and sleep well, too.{p}\ \ They're just as important as exercise. 」"
        "Juuichi-san gently pats Soutarou-kun's shoulder.{p}When a big person like Juuichi-san tells you that,\nit really does seem true."
        
        stop music fadeout 2
        
        "...Wait.{p}Soutarou-kun sighs and says something more."
        
        play music free58
        
        so "「...I'm tired of waiting.{p}\ \ I want to be a regular on the team soon,{w=.2}\n\ \ to be an important player like Takahara-senpai. 」"
        so "「So you can tell me to stop weight training,{w=.2}\n\ \ but I can't. 」"
        "His expression gets more cloudy as he speaks."
        so "「...But that actually isn't good for me, huh... 」"
        "He looks down.{p}I can hear him sniffling."
        "I should say something...{w=.2}\nBut I can't think of any words to comfort him with."
        
        show ju 003 with dis
        
        ju "「Hey, Touno, I like your proactive way of thinking. 」"
        "Juuichi-san places his hands on Soutarou-kun's\nshoulders, and looks into his face."
        so "「...*sniff* 」"
        ju "「You just happened to go the wrong way this time,\n\ \ okay? All you need to do is take a slightly\n\ \ different course of action. 」"
        so "「...*sniff* 」"
        
        stop music fadeout 3
        
        "He makes small sobbing sounds.{p}Over time, they disappear,\nand the sounds of the cicadas are all that's left."
        "...I think that went on for about 5 minutes."
        
        play music daily03
        
        "Soutarou-kun regains his composure,{w=.2}\nthen says something quietly into Juuichi-san's ears.{p}He nods, several times."
        "Juuichi-san takes his hands\noff Soutarou-kun's shoulders."
        
        show so 001 with dis
    
        "Although his eyes are still slightly red,{w=.2}\nSoutarou-kun rubs his face with his arm,\nbringing back his usual bright smile."
        "Hm, it seems he's all better now.{p}...I didn't do anything, though."
    
        show ju 001 with dis
        
        ju "「...Even so,{w=.2}\n\ \ it seems I've become Takahara by acting like this. 」"
        "Did Juuichi-san just lighten the mood?{w=.2}\nIt's rare for him to joke around.{p}Soutarou-kun and I both laugh."
        fn "「Certainly! 」"
        so "「Haha,{w=.2} that's right! 」"
        "Then, Soutarou-kun bows his head."
        
        show so at bowing
    
        so "「...Mikazuki-senpai,{w=.2} [ln]-senpai.{p}\ \ I'm sorry you had to see me so pitiful! 」"
        so "「So,{w=.2} thank you very much! 」"
        
        show ju 008 with dis
    
        ju "「You don't need to be so formal. 」"
        fn "「Yeah.{w=.2} I was just a bystander, really.{p}\ \ Juuichi-san is the only one you should be thanking. 」"
    
        show ju 004 with dis
    
        ju "「Hey, [ln].{w} You're saying too much. 」"
        "He sounds slightly flustered.{p}Did I embarrass him?"
        
        show so 005 at jump_up
    
        so "「Well, you gave me advice,{w=.2}\n\ \ so of course I have to thank you! 」"
        "...I think he might be overdoing it,{w=.2}\nbut I suppose he is the kind\nof guy to be so sportsmanlike."
    
        show ju 001 with dis
    
        ju "「...Touno,{w=.2} may I have a word? 」"
        "Did he just think of something?{w=.2}\nJuuichi-san whispers to Soutarou-kun with a grimace."
    
        so "「I-I understand. 」"
        "Soutarou-kun stiffens at the pressure coming\nfrom Juuichi-san."
        
        "I'd turn and run if he showed me a face like that.{p}Soutarou-kun must be amazing to stand his\nground against a look like that."
        ju "「Now, let's go to the candy store.{p}\ \ {nw}"
        show ju 002 with dis
        extend "...We'll get some ice cream,{w=.2} okay? 」"
        
        show so 003 with dis
    
        so "「Sure! 」"
        "Soutarou-kun's relief shows on his face.{p}I wonder what Juuichi-san told him?{w=.2}\nIt'd be rude of me to ask, though."
        ju "「Good answer.{p}\ \ ...Get whatever you like,{w=.2}\n\ \ it's my treat today. 」"
    
        show so 005 at jump_up
    
        so "「No, you don't need to do that!{p}\ \ I've got enough money! 」"
    
        show ju 001 with dis
        
        "Juuichi-san gives him a stern glare.{p}Once again, Soutarou-kun cringes."
        ju "「Are you crushing your senpai's honour? 」"
        so "「No,{w=.2} that's not what I meant... 」"
        ju "「{cps=10}Then take it, it's my treat. 」"
        "He speaks in a low, forceful tone.{p}I don't think anyone would disobey that.{p}...Except Torahiko."
        
        show so 001 with dis
    
        so "「...Got it!{w} 　I'll take it! 」"
        "Soutarou-kun seems to have understood the point."
        ju "「Now then,{w=.2} let's go, Touno, [ln]. 」"
        fn "「Me too? 」"
        "I reflexively ask.{p}Juuichi's voice somehow manages to go even lower\nas he replies:"
        ju "「...Are you coming or not? 」"
        fn "「Th-th-there's no reason for me not to!{p}\ \ Of course I'll come! 」"
        "Is he satisfied with my response?{w=.2}\nHe nods, and turns to head towards the candy store."
        
        play sound step01
        hide ju with wipe_right
        
        "At least Soutarou-kun's worries have been solved.{p}Looking over at him, he has a cheerful face,\nlike his gloomy one before never even happened."
        "Yeah, now that's the Soutarou-kun I know."
        
        play sound step01
        hide so with wipe_right
    
        ju "「[ln],{w=.2} you're paying for your own. 」"
        fn "「What?{w=.2} That's not fair! 」"
        ju "「That was a joke. 」"
        fn "「... 」"
        "Please stop joking with a straight face."
        
        jump end12
    
    ############################################
    label juuichi12_stick:

        $ event_name = "Lament of the Burning Match"
        $ love_juuichi -= 1
        $ love_soutarou -= 1
        play music free22
        
        "There's only one thing a boy would want bigger!{p}His crotch match...\nI'm sure it's his magic wand!"
        "Wow, Soutarou-kun,\nI wasn't expecting that from\nsomeone as innocent-looking as you."
        "But how should I answer?{p}While I'm weighing up my options,\nJuuichi-san speaks first."
        ju "「I think daily training is important. 」"
        
        show so 001 with dis
    
        so "「Training? 」"
        ju "「Yes.{w=.2} Moderate training promotes growth. 」"
        fn "「...Ju-Ju-Juuichi-san!{p}\ \ You got to the point so suddenly! 」"
        "I can't help but comment.{p}He's being a little too hasty, isn't he?!{p}Some things have to be set up first!"
    
        show ju 003 with dis
    
        ju "「...? 」"
        "He looks at me, confused."
        "But I'm the one that's confused here!{p}I take my eyes off Juuichi-san,\nand look back over to Soutarou-kun."
        
        show ju 001 with dis
    
        ju "「Be careful not to overdo it.{p}\ \ Excessive training will hinder your growth. 」"
        so "「Got it... 」"
        
        play sound hit_p09
        show riverbank at vshake
    
        fn "「No, no, it doesn't get bigger from muscle training!{p}\ \ Don't you mean blood? 」"
        "I interrupt Soutarou-kun without meaning to."
    
        show ju 003
        show so 005
        with dis
        
        "Maybe Juuichi-san is uninformed about these things?{p}I thought he'd be a more knowledgeable about this,\nso I'm kind of surprised."
        "...Should I lend a hand?{p}I decide to so."
        "How to start...?{p}First, I'll ask him what his type is...{w=.2} No!"
        "Theories as to why ejaculation occurs?{w=.2}\nAll right, [fn]-sensei's impromptu\nhealth lesson begins now!"
    
        play sound iron_pipe
        
        "...The two of them have been giving me\na strange look this whole time.{w=.2}\nMaybe I didn't phrase it right?"
        ju "「[ln],{w=.2} what are you talking about? 」"
        fn "「You know...{w} We're talking about 'that', right? 」"
        so "「What do you mean, 'that'? 」"
        "I'm on the verge of tears.{p}Soutarou-kun, your big brother\ndoesn't like it when you play dumb."
        "...What is this?{w} 　Are they teasing me?{p}Did I become a joke character without realizing?"
        fn "「{size=-10}You know,{w=.2} that thing. {size=+10} 」"
        "I look down,{w=.2}\ntowards the area of Juuichi-san's\nand Soutarou-kun's"
        "...But they still don't get it?{p}They ask again."
        
        show so 001 with dis
    
        so "「[ln]-senpai,{w=.2} I don't understand. 」"
    
        show ju 001 with dis
    
        ju "「You're a man, say what's on your mind. 」"
       
        "...{p}...{p}..."
        
        play sound hit82
        
        "Pop.{p}I'm pretty sure something just burst inside me."
        
        play sound hit_p09
        show riverbank at vshake
        
        fn "{size=+15}「You know,{w=.2} that thing all men have\n\ \ dangling from their crotches! 」"
        
        play music unari00
        stop music fadeout 3
        
        " I say it all at once.{p}{nw}"
        play sound dream
        extend "Wow, that was a liberating feeling...!"
        "It was like...{p}Leaving footprints on fresh snow.{p}I said it.{w=.2} I said it!!"
        "I get the urge to cry out in joy,{w=.2}\nbut I suppress the feeling."
        "...Then,{w=.2} I take a look the two of them."
        
        show ju 011
        show so 005
        with dis
    
        "Soutarou-kun looks completely bewildered,{w=.2}\nand Juuichi-san looks flabbergasted.{p}Huh? This isn't the reaction I was expecting..."
        ju "「I was talking about weight training... 」"
        so "「Uh, me too... 」"
        fn "「... 」"
        ju "「... 」"
        so "「... 」"
        
        play sound metalhit001
        
        "A terrible silence falls upon us.{p}Even the cicadas pick up on the mood,{w=.2}\nand stop their incessant noise."
        "In an instant, all my blood rushes to my face.{p}You could fry an egg on it at the moment."
        so "「...S-senpai... 」"
        fn "「...Hm?{w=.2} What is it, Soutarou-kun? 」"
        "Is he trying to cover for me or something?"
        "When he sees my face, though,{w=.2}\nhe groans and says no more."
        "I guess I've made quite the facial expression.{p}I suppose it doesn't matter any more."
        
        scene river with wipe_right
    
        "I slowly step backwards, heading towards home."
        
        scene black with Dissolve(1)
        
        "Then I turn around and run.{p}Like the wind."
    
        jump end12

##################################################
label kouya12:

    $ focus_character = "kouya"
    $ event_name = "Unexpected Encounter"
    $ love_kouya += 1
    scene map
    hide screen shrine12    
    scene sky with sdis
    $ renpy.music.set_volume(0.4, 0.0, channel = "music")
    play music cicada01 fadein 3

    fn "「White clouds, blue sky,\n\ \ and cicada noises, way off in the distance.{p}\ \ Today is another peaceful day in Minasato Village. 」"
    "Alone at the grounds, I monologued to myself."
    "No reason in particular.{p}Not even a tiny bit of purpose."
    "There are some things that I feel like doing,\nso I just do them."
    "Nevertheless, my words themselves are true.{p}Today, Minasato is the same as it always was.{p}The breeze in my face felt so refreshing."
    "Yep,{w=.2} very elegant."
    ka "「Well, if it isn't [fn]. 」"
    
    scene shrine_court with dis
    
    "While looking at the dreamily swinging branches,\na voice reached my ears."
    
    play sound step01
    
    "When I looked over, Kouya's form coming up\nthe stone steps reflected in my eyes."
    fn "「Huh, what's going on, Kouya?\nDidn't expect to see you here. 」"
    
    show ka 002 at center with dis

    ka "「I could ask you the same thing.{p}\ \ What are you doing, here at a Shinto shrine? 」"
    fn "「...Nothing much, just killing time.{p}\ \ I don't have anything to do, really. 」"
    "Ever since I got back to Minasato,\nI've been getting the feeling\nthat most days are like this."
    "Everyone else is also on vacation,\nbut it's not like their days are free.{p}They might have clubs, work, or household helping."
    "Therefore, they don't have much time to be alone."
    "When that itself becomes a way of having leisure,\nI don't really hate it,{p}but I can't help but feel a bit sad."
    "And this method of killing time\nwas just a spontaneous attempt at something,\nso maybe something new might happen."
    
    show ka 005 with dis

    ka "「Ahh...{w} sorry.{p}\ \ You just came back, but I haven't had much time. 」"
    fn "「Nah, don't apologize.{p}\ \ You didn't do anything wrong, Kouya. 」"
    fn "「Besides, something like this is a bit nostalgic,\n\ \ so I don't mind.{w} Anyway, what brings you here? 」"

    show ka 001 with dis
    
    ka "「Hmm, if I had to sum it up, I'm here to guide. 」"
    fn "「Guide? 」"
    "I don't really get that."
    "「What do you mean? 」 I was about to ask.{p}But before it could get out, the words\nwere erased by another voice calling out."
    who "「Heeey, Kouyaa~.{w} Big Brother is kinda old here,\n\ \ so ease up on the heavy exercise.{p}\ \ Anyway, wait a sec,{nw}"
    play sound bosu35
    show shrine_court at vshake
    extend " damn it. 」"
    "The words being spoken didn't seem that tired,\nbut rather bright.{w} From the stone steps\nwere three people that I'd never seen before."
    
    scene shrine
    show ke 001 at center
    show yu 001 at farleft
    show jn 001 at farright
    with wipeleft

    "A light brown-haired horseman,{p}a clear-eyed birdman,{p}and a short-statured tricolored catman."
    "Are they friends of Kouya's?"
    
    show ke 004 with dis
    
    horse "「Good grief, what's this about leaving me behind?{p}\ \ Don't you trust me? 」"
    
    show yu 003 with dis
    
    bird "「Isn't that because you're making things difficult,\n\ \ Keisuke?{w} You were all, {nw}"
    show yu 001 at briefzoom
    extend "『Show me around!』{w=.5}\n\ \ {nw}"
    show yu 003 with dis
    extend " and then you go, 『We're seriously going up?』 」"
    bird "「As for the 『left behind』 thing,{w} it wasn't that far. 」"
    
    cat "「... 」"
    "From the voices, it seems all the complaining\ncame from the horse.{w} How do I put this...\nhe seems like a unique kind of guy."
    
    show ke 008 with dis

    horse "「I dunno about that.{p}\ \ You need a bigger heart to accept me.{p}\ \ Things won't work if you can't,{w=.2} seriously. 」"
    
    show yu 001 with dis

    bird "「So,{w=.2} Kouya.\n\ \ Who is the person next to you? 」"
    
    scene shrine with wipe_right
    
    show ka 001 at midleft
    show yu 001 at farleft
    show ke 001 at midright
    show jn 001 at farright
    with wipe_right

    ka "「He's a childhood friend.{p}\ \ He changed schools a while back,\n\ \ but he's come back to hang out,{w=.2} for now. 」"
    
    show yu 006 with dis

    bird "「Ahh,{w=.2} did you mention him the other day?{p}\ \ Hmm,{w=.2} what was that name...?{w=.2}\n\ \ I remember asking about it... 」"
    
    show jn 006 with dis
    
    cat "「...[fn], [ln]. 」"
    
    show yu 002 with dis

    bird "「Yes yes, that's it.{p}\ \ So you're [fn] [ln]-kun then... 」"
    
    show ke 004 with dis

    horse "「Seriously!?{p}\ \ The rumored [fn] [ln]!?{p}That's like the biggest scoop ever! 」"
    fn "「No, well, I am [fn] [ln]... 」"
    "All of their eyes were on me,\nfilled with immense interest or curiosity."
    "It's a little... Actually, it's really embarrassing.{p}The way things are, that is."
    "When he noticed my discomfort,\nthe birdman looked taken aback, and said,"
    
    show yu 007 with dis

    bird "「...Oh, sorry. Didn't mean to stare like that. 」"

    show yu 001 with dis

    bird "「Just a while ago, Kouya was talking about you for\n\ \ a bit, and when he was talking he seemed happy. 」"
    bird "「I got interested,\n\ \ wondering what kind of person you were. 」"
    fn "「Hwuh? Is that true? 」"
    "I blurted out in a shaky voice, surprised.{p}Even for me, I thought I sounded weird."
    
    show ka 013 with dis

    ka "「...Hey, Yuuki, don't go on so much about it. 」"
    
    show ke 003 with dis

    horse "「What are you saying?{w} Your tail was wagging\n\ \ when you were talking earlier. 」"
    
    show ka 010 at briefzoom

    ka "「Wha-!?{p}\ \ There's no way that's- 」"
    
    show yu 003 with dis

    bird "「No no, he's for real this time.{p}\ \ For Keisuke, that's pretty serious.{p}\ \ Wait, you weren't self-aware at the time? 」"
    
    show ke 008 with dis

    horse "「Yeah yeah.{p}\ \ It really is serious.{p}\ \ Right, Jun!? 」"
    cat "「... 」"
    "The birdman added in his agreement, double checking\nthat the catman nodded at the horseman's words."
    "For his part, Kouya looked away from my eyes\nand hung his head in silence.{w} Well actually,\nit's more like there's nothing else he could do."
    "I'm really happy about it,\nbut being blabbed about like this makes me\nfeel bad for him. I'm feeling awkward myself."
    fn "「B-{w=.2}by the way, Kouya.{p}\ \ Would you mind introducing everyone...? 」"
    "Because I felt so bad for him, I tried changing\nthe subject.{w} Yes, that's nice, me.{p}Keep it up, me."
    
    show ka 005 with dis

    ka "「Y-{w=.2}yeah...{p}\ \ All these guys are my true friends and bandmates. 」"
    
    scene shrine with wipe_right
    show ke 006 at center with wipeleft
    
    $ encounter_keisuke = True

    ka "「The horseman is the drummer, Keisuke. 」"
    ke "「Nice to meet ya! 」"

    hide ke with wipe_right
    show yu 001 at farleft with wipeleft

    $ encounter_yuuki = True 

    ka "「The birdman over there is the vocalist, Yuuki. 」"
    yu "「Nice to meet you.{w} I hope we get along. 」"

    hide yu with wipe_right
    show jn 001 at farright with wipeleft
    
    $ encounter_jun = True
    
    ka "And, the quiet catman over there\n\ \ is the bassist, Jun. 」"
    
    show jn at bowing
    
    jn "「... 」"

    hide jn with wipe_right
    show ka 005 at center with wipeleft

    ka "「Well, anyway,{w} we normally borrow a studio in Kazenari\n\ \ and practice there,{w} but there's some construction\n\ \ going on, so we can't use it for the time being. 」"
    
    show ka 001 with dis
    
    ka "「We tried looking for a new place,\n\ \ but there isn't any place as good in Kazenari. 」"
    
    show ka 014 with dis

    ka "「So now we're looking around here,\n\ \ and these guys said they wanted to look around\n\ \ the village, so I'm showing them around. 」"
    "Kouya was talking a lot faster than usual.{p}Moreover, his cheeks have slackened a bit.{p}He must really be in a hurry."
    fn "「Huh, I see then.{p}\ \ Is there a place where you can\n\ \ practice here in Minasato Village? 」"
    
    show ka 001 with dis

    ka "「I was thinking of borrowing the school gym. 」"
    "I see, I get it now.{p}The gym should be fine for their equipment."

    show ka 002 with dis

    ka "「We went and talked with Botan-sensei about it,\n\ \ and he said he was fine with it,{p}\ \ but he also told us to check with Uncle Shigure. 」"
    ka "「Visiting him is fine and all, but he's out.{p}\ \ It doesn't seem like he'll be back until tonight,\n\ \ so we just packed up and went around sightseeing. 」"
    fn "「I see.{w} So that's what you meant by \"guide\". 」"
    
    show ka 003 with dis

    ka "「That's how it is.{p}\ \ But there's not much special about the village,\n\ \ and with nowhere to go, I'm a bit stumped. 」"
    
    show ka 005 with dis

    ka "「On top of that, the one who suggested the\n\ \ sightseeing is spazzing out about it. 」"
    
    hide ka with wipe_right
    
    show ka 005 at midleft
    show yu 001 at farleft
    show ke 004 at midright
    show jn 001 at farright
    with wipe_right

    ke "「Hey, I wasn't spazzing out about it.{p}\ \ I just said that climbing stairs is a pain. 」"
    yu "「Wouldn't the world in general refer to that as\n\ \ 'spazzing out'? 」"
    jn "「... 」"
    
    show ke 008 at briefzoom
    
    ke "「No it's not.{w} It's totally not.{p}\ \ {nw}"
    show ke 004 with dis
    extend "I don't really get it, but it shouldn't be.\n\ \ It's not.{w} Yeah.{w} If it's not, it's not. 」"
    
    show yu 003 with dis

    yu "「Ahh, yes yes,{w=.2} we get it,{w=.2} we get it. 」"
    "Yuuki-san spoke in exasperation."
    "Somehow, this seems like a small-time comedy act,\nbut this back and forth is pretty fun.{p}These two make such a good team."
    
    show ke 001 with dis

    ke "「If you get it, then that's fine.{p}\ \ {nw}"
    show ke 006 with dis
    extend "Now, we've been here for ages,\n\ \ so let's go to the next place. 」"
    
    show ke 002 with dis

    ke "「Oh,{w=.2} yeah.{w} If you want, [fn] do y-\n\ \ {nw}"
    show ke 001 with dis
    extend "...Wait,{w=.2} is it okay if I call you by first name? 」"
    fn "「Eh?{w} Oh, yes.{w} I don't mind at all. 」"

    show ke 006 with dis
    
    ke "「Thanks.{w} So, you wanna tag along?{p}\ \ Might be saying too much,\n\ \ but you look like you're free. 」"
    
    show yu 002 with dis

    yu "「Oh,{w=.2} that's a nice idea, Keisuke. 」"
    
    show ke 003 with dis

    ke "「I know, right?{w} It's cool if you want\n\ \ to really pile on the praise. 」"

    show yu 003 with dis

    yu "「Even if it was a joke,\n\ \ it was a bit cool even if you got all excited. 」"
    
    show ke 004 with dis

    ke "「Leave it!{w} Leave it there!{p}\ \ {nw}"
    show ke 002 with dis
    extend "...And [fn], you don't need to be polite with\n\ \ us.{w} It sucks when everyone's all formal. 」"
    ke "「Just go with whatever works. 」"
    fn "「Yes...{w=.2}I mean, yeah.{p}\ \ Okay. I'll do that. 」"
    
    show ke 001 with dis

    ke "「Yeah, just like that. 」"

    show yu 001 with dis

    yu "「...So, back on topic, what will you do,\n\ \ [fn]-kun?{w} Just like Keisuke said earlier,\n\ \ do you want to come with us? 」"
    yu "「Kouya would probably be happy if you did. 」"
    
    show ka 006 with dis

    ka "「Why you... 」"
    "Glancing at Kouya, that didn't seem likely.\nHe looked liked he'd get mad.{p}Since my heart's beating so fast, it's troubling."
    
    show yu 002 with dis

    yu "「Well,{w=.2} shall we? 」"
    fn "「U-{w=.2}uhh... 」"
    "Well, I am free, and I don't have a reason to refuse,\nbut what should I do?"
    
    menu:
        "A. I'll go.":
            jump kouya12_go
        "B. I'll pass.":
            jump kouya12_pass

    #############################################
    label kouya12_go:

        $ event_name = "Let's Go Right Now"
        $ love_kouya += 1
        
        fn "「...Sure, I'll come. 」"
        
        hide ke
        show ke 006 big at center_big
        with explosion
    
        ke "「Ohh, you said it, [fn]! 」"
        
        play sound bosu29
        pause .2
        play sound bosu29
        
        "Keisuke slapped me on the back\nwith a smile across his whole face."
        "He's probably holding back,\nbut it still hurt a bit.{p}Actually, it seems to be getting worse!"
        
        show shrine at vshake
        play sound hit_p07
        pause .2
        #Shake vertically
        play sound hit_p07
        pause .2
        
        "Crap,{w=.2} ow!?{p}Where'd the gentleness from earlier go!?"
        
        hide ke
        show ka 005
        show ke 001 at midright behind ka 
        with dis
    
        ka "「Hey, Keisuke, you're hitting him too hard. 」"
        "Maybe he could tell, as Kouya chided\nKeisuke-san before he hit hard enough to kill.\nSeriously nice save there, Kouya."
        
        show ke 004 at jump_up
        
        ke "「Oh, for real?{w} Whoops.{p}\ \ Sorry about that [fn]. 」"
        "Keisuke-san stopped that movement, saving me\nfrom being beaten on like a drum.\nI dug out a deep relieving sigh."
        "It was dangerous for a minute there.\nAll the way to my bones."
        fn "「No, I'm all right.{p}\ \ Though I'd be happy if you treated me\n\ \ more gently from now on... 」"
        
        show ke 006 with dis
        
        ke "「Roger!{p}\ \ I'll keep that in mah mind! 」"
        "...Somehow, I'm not reassured."
        
        show ke 001 with dis
    
        ke "「That aside, we should celebrate the\n\ \ addition to our little travel pack,\n\ \ maybe with an offering, but... 」"
        
        show ke 004 with dis
    
        ke "As he pulled out his wallet, Keisuke-san's\n\ \ expression hardened a bit. And with a quiet *clink*,\n\ \ he put it back in his pocket."
        
        show ke 008 with dis
    
        ke "「...I only have a 500 yen coin, so we'll\n\ \ have to pass. 」"
        
        show ka 014 with dis
    
        ka "「...Keisuke, you really do muck up everything. 」"
        "No objections there.{p}I'm sure everyone else there thought the same thing."
        
        stop music fadeout 2
        scene black with sdis
        
        jump kouya12_continue
    
    #########################################
    label kouya12_pass:

        $ event_name = "I'll Go on Ahead."
    
        fn "「...it's been a while, but I'll pass this time.{p}\ \ It's for the band members and no one else,\n\ \ so I figure it'd be weird for me to come along. 」"
        "Also, being here together with Kouya is giving me\na bad feeling in my heart.{w} I might end up blowing\nmyself up in a weird state of mind."
    
        show yu 001 with dis
        
        yu "「Hmm... Is that so?{w} Well, if [fn]-kun\n\ \ says so, then it can't be helped. 」"
        
        show ke 004 with dis
        
        ke "「Eh?{w} Why aren't you coming [fn]?{p}\ \ Is it Kouya?{w} Is this Kouya's fault? 」"
        
        show ka 005 with dis
    
        ka "「Why are you suddenly calling me out? 」"
        
        show ke at jump_up
    
        ke "「Shut it, lover-boy! 」"
        
        show yu 003 with dis
    
        yu "「Yes, yes, enough with the meaningless accusations,\n\ \ Keisuke.{w} ...Now then,{w} see you next time,\n\ \ if there's a chance, [fn]-kun. 」"
        ke "「You're breaking my heart here.{w} {nw}"
        show ke 006 with dis
        extend "Oh yeah, we got a\n\ \ live concert coming up, so come see us if you can.{p}\ \ Kouya can probably get you the tickets. 」"
        fn "「Yeah, sorry.{p}I'll definitely be there. 」"
        
        show ke 001 with dis
    
        ke "「You promise?{w} Well, later then, [fn].{p}\ \ ...Come on, don't just stand there.\n\ \ Say something, Jun. 」"
        
        show jn 006 with dis
    
        jn "「...Later. 」"
        fn "「Yeah, see you next time, Jun-kun. 」"
        
        scene shrine with wipe_right
        show ka 001 with wipeleft
    
        "Briefly after all the goodbyes were said,\nthe three of them waved their hands\nas they went back the way they came."
        "Kouya was the only one left in front of me."
        
        show ka 013 with dis
    
        ka "「...Sorry, did we disturb you? 」"
        fn "「Nope, not at all.{p}\ \ They seem like nice people, so I don't mind it. 」"
    
        show ka 002 with dis
        
        ka "「That so...{w} Well, next time\n\ \ let's get together and go somewhere. 」"
        fn "「Yep, I'm looking forward to it.{p}\ \ Anytime, right? 」"
        
        show ka 003 with dis
    
        ka "「Yeah. Time for me to get moving.{p}\ \ Later. 」"
        
        hide ka with wipe_right
    
        "He ran off to catch up with the others,\nwaving behind his back to me.{p}Once again, I'm hanging around alone on the grounds."
        "...「Let's get together and go somewhere, 」{w=.2} huh?"
        "It's a casual promise, but it'd be\ngreat if it came true sometime."
        
        jump end12
    
    ############################################
    label kouya12_continue:

        $ event_name = "Continuing On."

        play music daily02
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
        scene mountain_path with Dissolve(.5)
        
        show ke 001 at midright
        show jn 001 at farright
        show ka 001 at midleft
        show yu 001 at farleft
        with wipe_right
    
        ke "「So, where we headed off to next? 」"
        "After finishing a short prayer at the shrine,{w=.2}\nwe went down the steps, walking along the road."
        "On a side note, Keisuke-san threw in\na 10 yen coin from Yuuki-san."
        "I'm guessing he just didn't want\nto use his 500 yen coin at all.{p}Then again, I would've done the same thing."
        
        show ka 005 with dis
    
        ka "「Where else is there...{p}\ \ After that,{w=.2} the only thing left\nw\ \ ould be Lake Shiratsuyu. 」"
    
        show ke 004 with dis
    
        ke "「I guess that's where the name- 」"
    
        show ka 001 with dis
    
        ka "「It's just a normal lake. 」"
        "Kouya cut him off abruptly,{w=.2} and Keisuke-san\ncould do nothing but give a big laugh.{p}I think I know what he was going to say next."
        ke "「...Minasato Village{w=.2} really is an empty place. 」"
        
        show ka 005 with dis
    
        ka "「I've been saying that from the start.{w} What were\n\ \ you expecting from an ordinary \"village\"?{p}\ \ {nw}"
        show ka 001 with dis
        extend "It's not like it's a famous tourist site. 」"
        ka "「Oh, but there are some weird\n\ \ souvenirs here.{w=.2} Gonna buy some? 」"
        ke "「Hmm,{w=.2} well, maybe...{w} I'll think about it...{p}\ \ Oh,{w=.2} hey, [fn], do you know anything?{w=.2}\n\ \ Any hidden cool places? 」"
        fn "「Even if you ask me,{w=.2} I haven't been back\n\ \ here in Minasato for five years... 」"
        
        show ke 006 with dis
    
        ke "「It's all cool!{w} Anyway, all feelings up 'til now\n\ \ shouldn't have changed!{w} Reach into your memories,\n\ \ even all the way to when you were in diapers! 」"
        fn "「Hmm... 」"
        "Crazy, unreasonable behavior.{p}Shoves everything onto others.{p}Above all, an amazing way of speaking."
        "...But still,{w=.2} just like Keisuke-san said,\nthe Minasato Village I knew and the Minasato Village\nof now aren't entirely different."
        "I'll try thinking about it."
        "When I think of myself from five years ago,{w=.2}\nI was a tireless kid that ran around everywhere\nwith everyone until the day ended."
        "Around then, I think I knew everything\nin the village,{w=.2} from one end to the other."
        "But even that memory has faded a bit, sadly.{p}In those dim and hazy images,{w=.2}\nif I had to pick something I could still see..."
        fn "「I guess we should go to Lake Shiratsuyu after all. 」"
        
        show ka 003 with dis 
    
        ka "「What, you remember something? 」"
        fn "「No,{w=.2} it's all fuzzy to me.{p}\ \ I'm a little worried about it. 」"
        
        show ka 001 with dis
    
        ka "「Huh.{w=.2} It's strange to hear that coming from you. 」"
        ka "「Time to go to Lake Shiratsuyu then.{w=.2}\n\ \ It's a request, after all.{p}\ \ You guys okay with it too? 」"
        yu "「That should be fun, I haven't been to many lakes.{p}\ \ I might want to take a walk around it. 」"
        jn "「...Yeah,{w=.2} I'm fine with it.{w=.2} 」"
        
        show ke 004 with dis
    
        ke "「Whoa,{w=.2} we settled that in just one round... 」"
        ka "「Well that's a shame,{w=.2} since it looks like Keisuke\n\ \ will drop out here for business, so the four of us- 」"
        
        show ke 001 with dis
    
        ke "「No I'll go, I'm going.{w} {nw}"
        show ka at move_offleft(1)
        extend "Who said anything\n\ \ about not going? What, is this bullying?{p}\ \ {nw}"
        show yu at move_offleft(1)
        extend "Just stop it.{w} How old are you?{nw}"
        show jn at move_offright(1)
        extend " Bullying's-- 」{w} {nw}"        
        show ke 004 at jump_up
        extend "{w=.15}{nw}"
        show ke at jump_up
    
        ke "「Hey wait, don't leave me behind! 」"
        
        play sound step03
        show ke at move_offright(0.5)
    
        "「He's at it again, 」{w=.2} the three of them thought\nas they quickly walked away and ignored him."
        "I also followed them right as they left,{w=.2}\nand the voice behind me grew louder.{p}My cheeks were unexpectedly loose."
        "Lake Shiratsuyu is pretty close to the shrine.{p}If you follow the road in front of you\nthen cross the river,{w=.2} you should be pretty close."
        "It should take about five minutes.{p}Maybe I should bring up a topic in here.{p}So, what should I talk about?"
        
        menu:
            "A. How did everyone meet?":
                jump kouya12_you
            "B. What did Kouya say about me?":
                jump kouya12_me
    
    #######################################
    label kouya12_you:

        $ event_name = "Old Talk"
        
        show ke 001 at midright
        show ka 001 at midleft
        show jn 001 at farright
        show yu 001 at farleft
        with wipe_right
    
        fn "「Say, how did everyone come to meet each other? 」"
        "I wanted to know a bit more about everyone,{w=.2}\nso I began with that."
        "I'm sure they aren't from Minasato, and I was\nthinking that they were from neighboring towns,{w} but\nI was a bit interested in how Kouya got to know them."
        "...No,{w=.2} no matter which way I put it,\nwhat Kouya did in the time I've been gone\nis what I'm really interested in."
        
        show ke 004 with dis
    
        ke "「Ah,{w=.2} that's right...{p}\ \ {nw}"
        show ke 001 with dis
        extend "In the beginning, wasn't it just me and Kouya?{p}\ \ We met at that pops's place. 」"
        ka "Yep.{w} Jun and Yuuki joined in sometime later on. 」"
        fn "「Who's 'Pops'? 」"
        yu "「The manager of the musical instruments store\n\ \ Kouya works at.{w} Even now he takes care of us\n\ \ in a lot of ways. He's a really nice person. 」"
        ke "「It was a long time ago,{w=.2} but when I first thought\n\ \ of starting up a band and looking for members,\n\ \ Kouya was the one he introduced me to first. 」"
        
        show ke 006 with dis
    
        ke "「Then after that, we talked about random crap\n\ \ until we clicked with one another,{w=.2}\n\ \ then started out as a team. 」"
        ke "「...Or something like that. 」"
        
        show ka 005 with dis
    
        ka "「That sounds wrong in all sorts of ways,\n\ \ but that's basically how it went. 」"
        
        show ka 001 with dis
    
        ka "「Well, I thought he was amusing,{w=.2}\n\ \ and he seemed to be legit.\n\ \ I was also looking for people to team up with. 」"
        
        show ke 007 with dis
    
        ke "「Honestly, it's all right to say 'it turned to love,'{w=.2}\n\ \ you know? 」"
        ka "「And,{w=.2} since just a guitar and drums wasn't going\n\ \ to cut it, and because I wanted to make a band,{w=.2}\n\ \ I went looking for other members. 」"
        
        show ke 005 with dis
        
        ke "「...You tsundere.{w=.2} I understand. 」"
        ka "「I thought about taking an ad out in a magazine,{w=.2}\n\ \ but the manager went and did the work for us."
        ka "「Jun and Yuuki were amongst the regulars\n\ \ he introduced to us. 」"
        fn "「Huh.{w=.2} So everyone is a regular at the same shop. 」"
        ka "「Yeah,{w=.2} so from the beginning I could\n\ \ at least remember everyone's faces. 」"
        ka "「Because of that, things went quickly,{w=.2}\n\ \ and about two weeks later,\n\ \ Yuuki was the last one to join up. 」"
        
        show ke 001 with dis
    
        ke "「Yeah,{w=.2} that was pretty fast, wasn't it?{w=.2} 」"
        yu "「Yep,{w=.2} I decided to join almost right away.{p}\ \ {nw}"
        show yu 002 with dis
        extend "I felt that if he was a member, then he could do so\n\ \ many things. It was like instinct. 」"
        
        show jn 006 with dis
    
        jn "「I thought so too. 」"
        fn "「Were you surprised? 」"
        
        show yu 006 with dis 
    
        yu "「That might be a bit too long ago, you know? 」"
        "Yuuki-san became a bit embarrassed\nfrom being put into the spotlight."
        "He laughed like he was trying to hide it,{w=.2}\nand we laughed along with him."
        
        show yu 001 with dis
        
        yu "「But I think it was like that.{p}\ \ Something like a seed of fate. 」"
        fn "「So from a bunch of friends from a store,{w=.2}\n\ \ you all came together as a group, huh. 」"
        
        show ka 003 with dis
    
        ka "「That's right.{p}\ \ Someway or another we settled into things. 」"
        fn "「I see then. 」"
        "I see,{w=.2} so Kouya works part-time at a music store.{p}There's probably no better place for him,\nsince he likes music so much."
        "On top of that, he's made real friends like this.{p}There doesn't seem to be room for any more,{w=.2}\nbut even I could tell they were all nice people."
        "As I thought,{w=.2} everyone's changed a lot\nsince I've been gone."
        ke "「Oh, is that it?{w} Lake Shiratsuyu? 」"
        "I was being caught up in my own world,{w=.2}\nuntil Keisuke-san's words brought me back to Earth."
        "Looking at where he was pointing,{w=.2}\nI saw the shining surface of the water\nreflecting the summer sunlight."
        
        stop music fadeout 2

        jump kouya12_lake
    
    ################################################
    label kouya12_me:

        $ event_name = "He said..."
        
        "Hmm,{w=.2} I'm a little stumped for things to talk about."
        "...Well, there was that one thing from earlier."
        
        show ke 001 at midright
        show ka 001 at midleft
        show jn 001 at farright
        show yu 001 at farleft
        with wipe_right
    
        fn "「By the way,{w=.2} you guys said that Kouya\n\ \ was talking about me to you all,\n\ \ but what did he talk about? 」"
        "Yes, I'll be honest.{p}I'm totally interested in that!"
        "After all, \"that\" Kouya was\nwagging his tail as he was talking about me.{p}I'd have to be crazy to not be intrigued by it!"
        
        show ka 005 with dis
    
        ka "「Hey, [fn] that's- 」"
        
        play sound tsuzumi
        play music free44
        $ renpy.music.set_volume(1.0, 0.0, channel = "music")
        
        hide ke
        show ke 003 big at center_big
        with explosion
    
        ke "「You wanna hear?{p}\ \ You do, dontcha!? 」"
        fn "「Y-{w=.2}yeah... 」"
        "While cutting across Kouya's protests,{w=.2}\nKeisuke-san walked up close to me."
        "Wow, he's seriously close...{p}I can feel him breathing through his nose."
        
        show ke 006 big with dis
    
        ke "「Yeah yeah!{w} Let's talk about everything then!{p}\ \ {nw}"
        show ke 007 big with dis
        extend "Stuff that's there{w=.2} and stuff that's not, any-{p}\ \ {nw}"
        show ke 004 big at jump_up_big
        pause .1
        show ke at center_big
        extend "Gaaah!? 」"
        
        show yu 003 with dis
    
        yu "「Your face is too close, can you back off a little?{p}\ \ No one wants to see your face from that close.{p}\ \ Sorry, [fn]-kun.{w} I'll get rid of this ass. 」"
        
        show ke at jump_up_big
        pause .1
        show ke at center_big
        pause .05
        show ke at jump_up_big
        pause .1
        show ke at center_big
    
        ke "「Hey, ow!{w} I get it,{w=.2}\n\ \ I get it, so stop pulling my tail, will ya!? 」"
        
        hide ke
        show ke 004 at midright behind jn
        with dis
        
        "As if being dragged along (I think he is, actually){w=.2}\nKeisuke-san moved back{w=.2}\nto a more normal distance away."
        "His eyes have some tears in them,\nand it's a little pitiful to see."
        
        stop music fadeout 6
    
        yu "「Good grief,{w=.2} you get so excited sometimes,\n\ \ Keisuke... 」"
        ke "「Whaaaat?{p}\ \ Don't get all jealous of me getting close\n\ \ to [fn] so fast. 」"
        yu "「Yes yes, whatever you say.{p}\ \ {nw}"
        show yu 001 with dis
        extend "Keep talking already. 」"
        
        show ke 006 with dis
        play music daily02
        $ renpy.music.set_volume(0.8, 0.0, channel = "music")
    
        ke "「Aye aye, sir!{p}\ \ {nw}"
        show ke 008 with dis
        extend "Now then,{w=.2} you were asking about\n\ \ what Kouya was talking about? 」"
        "Putting on a smile that said\n「doesn't matter to me, if we keep talking, 」\nKeisuke-san double checked with me."
        "I nodded immediately in response."
        "I knew Kouya was making a face as if he wanted\nto say something,{w=.2} but for now I chose to not\nlook at him.{w} I'll apologize now.{w=.2} Sorry Kouya."
        
        show ke 001 with dis
     
        ke "「Uh-huh...{p}\ \ How do I put this...{p}\ \ He was in a super good mood. 」"
        ke "「I don't know the right expression for it,\n\ \ but it's something like that. 」"
        fn "「A super good mood? 」"
        ke "「Yeah.{w} I've seen him every day these few years,\n\ \ but I've never seen him like that before.{p}\ \ Right,{w=.2} Yuuki? Jun? 」"
        yu "「Yep.{w} He'd been cheerful since that morning.\n\ \ When I asked him about it,{w=.2}\n\ \ he said a friend from grade school came back. 」"
        yu "「He was putting out this happy aura for a while. 」"
        
        show jn 006 with dis
    
        jn "「His tail wagged a lot, too. 」"
        
        show yu 002 with dis
    
        yu "「Yeah, that's right.{w=.2} Always swishing back and forth,\n\ \ left and right.{w} If I had to compare the atmosphere\n\ \ around him to something... 」"
        yu "「I'd say he was about five times\n\ \ happier than Jun. Yeah, five times. 」"
        "Keisuke-san and Jun-kun both nodded at this."
        "I wonder what's up with that method of comparison.{p}Well, I do kinda get it,{w=.2}\nbut I feel like it's some kind of in-joke."
        "As for that five times thing,{w=.2} it sounds like\nsomething relatively impossible between them.{p}The way they nod their heads gives that impression."
        
        show ka 014 with dis
        
        "From a quick glance at Kouya,{w=.2}\nhis brow was wrinkled into a sullen expression\nthat screamed \"I don't want to hear any more.\""
        "I'll apologize again.{w=.2} Sorry, Kouya."
        
        show ke 004 with dis
    
        ke "「It's kinda scary.{p}\ \ I was afraid that someone messed with him{w=.2}\n\ \ and left him for dead that day. 」"
        ke "「I'm so glad you're alive. 」"
    
        show yu 001 with dis
    
        yu "「Was it just for August?{w} Ever since you came back\n\ \ [fn]-kun, it feels like every day is different.{p}\ \ It calms down for several minutes though. 」"
        fn "「Ehh?{w} No, I suspect it's more of the opposite.{p}\ \ You're not making that up, are you? 」"
        
        stop music
        
        "「Nope, not at all. 」"
        
        play music daily02 fadein 2
        
        "I was denied in complete synchronity.{p}I think I noticed Jun-kun's voice in there too,{w=.2}\nso he must think so too."
        
        show ka 001 with dis
    
        "I looked aside at Kouya again,{w=.2}\nhe's gone straight past sullenness\nand gradually into complete emptiness."
        "For Kouya, there probably isn't anything\neven more embarrassing.{w} I wouldn't ever want\nto be stuck in the same situation."
        "Then again,{w=.2} I was the one who started this..."
        "But I think I understand Kouya a bit better.{p}He looked forward to meeting with me again.{p}And he was honestly happy."
        "So this time I'll use different words.{p}And this time it won't be in my head,\nI'll give them to him with my voice."
        fn "「Thanks, Kouya. 」"
        
        show ka 012 at briefzoom
        
        "Kouya's eyes opened in confusion at my words,{p}{nw}"
        show ka 001 with dis
        extend "but they quickly returned to normal."
        ka "「Nah,{w=.2} it's nothing you need to thank me for.{w=.2} 」"
        fn "「Huh?{w=.2} But it really fits in this case. 」"
        ka "「Really? 」"
        fn "「Yeah.{p}\ \ I'm so glad, so just accept it. 」"
        
        show ka 006 with dis
    
        ka "「...You sure? 」"
        fn "「Yeah. 」"
        
        show ke 004 with dis
    
        ke "「Umm... Sorry to intrude while you two\n\ \ are in your own little world, but... 」"
        
        show ka 001 with dis
    
        "Our two-man loop came to a sudden stop.{p}To be honest,{w=.2} I'm a little glad it did."
        
        show ke 001 with dis
    
        ke "「Is that Lake Shiratsuyu? 」"
        "Looking at where he was pointing,{w=.2}\nI saw the shining surface of the water\nreflecting the summer sunlight."
        
        stop music fadeout 2

        jump kouya12_lake
        
    #########################################
    label kouya12_lake:

        $ event_name = "Memory of the Lake"
    
        scene black with Dissolve(.5)
        pause .1
        scene lake with Dissolve(.5)
        
        show ke 001 at midright
        show ka 001 at midleft
        show jn 001 at farright
        show yu 001 at farleft
        with wipe_right
        play music free0258
    
        "If you look after getting close to the water,{w=.2}\nyou'd notice that the water's perfectly clear\nand that you could see all the way to the bottom."
        "Lake Shiratsuyu,{w=.2} located in Minasato Village.\nOne of the most important places."
        "A dragon god that lived here from ancient times,{w=.2}\nseems to be the reason why it's so important,{p}Kouya explained."
        ke "「Ahh, when you put it like that...{p}\ \ {nw}"
        show ke 006 with dis
        extend "I-{w=.2}it has such an awesome mood here! 」"
        
        show yu 003 with dis
    
        yu "「I don't really feel like\n\ \ coming up with some sort of punchline...{p}\ \ I won't force myself if I can't think of anything. 」"
        
        show ke 004 with dis
    
        ke "「Well, that can't be helped.{p}\ \ I don't see it as a normal lake,{w=.2}\n\ \ but I think it's best that way. 」"
        ke "「That's how it feels,{w=.2} to me anyway. 」"
        yu "「Ah, I see... 」"
        
        show jn 002 with dis
    
        jn "「But,{w=.2} it's a beautiful place. 」"
        
        show yu 002 with dis
    
        yu "「Yep, sure is.{w} A place that a god lives in,{w=.2}\n\ \ and a place treasured by the villagers.\n\ \ I think I can understand that. 」"
        ka "「Well, when we were kids this was a place\n\ \ we might have damned ourselves while playing around.{p}\ \ I think we liked it here.{w} Right, [fn]? 」"
        fn "「Uh-huh.{w} Now that you mention it,{w=.2}\n\ \ we probably did defile the place,\n\ \ when I think about it... 」"
        
        show ke 001 with dis
    
        ke "「Won't the god forgive them as mistakes\n\ \ of little kids?{w} He lives in a lake this huge,\n\ \ so his heart must be just as big, right? 」"
    
        show ka 005 with dis
        
        ka "「...Maybe. 」"
        "He probably has so many things he wants to say,{w=.2}\nbut Kouya swallowed them all up and kept them inside.{p}I mean,{w=.2} he's making such a cool face right now."
        "But that lasted for only a moment,\nafter which he went back to his usual look."
        "I feel like I can hear him switching over to\n\"Well, whatever then\" mode."
        
        show ka 001 with dis
    
        ka "「Oh yeah, [fn].{w=.2}\n\ \ You said that there was something here\n\ \ that worried you, but what exactly is it? 」"
        fn "「Hm... How do I put this, it feels like a curse...{p}\ \ ...Back then, I have a memory of making a secret\n\ \ base somewhere here. 」"
        fn "「I was thinking about what happened to it. 」"
        "It's possible that it might still be around,\njust where I left it.\nI had that hope within my chest."
        "It doesn't matter much to me what state it's in,{w=.2}\nbut since we're here, I wanted to check up on it."
        
        show yu 001 with dis
    
        yu "「Ohoh, a secret base.{p}\ \ Niiice, I wanted to make one too.{p}\ \ It seemed like so much fun. 」"
        
        show ke 006 with dis
    
        ke "「A secret base is a man's passion. 」"
        ke "「I used to think, 'I wanna make one, too'{w=.2}\n\ \ but in the end I got too old for it.{p}\ \ So, where did you make this base? 」"
        fn "「In a thicket over there.{w=.2} It's pretty complex\n\ \ and it took me half of a summer to build,{p}\ \ but it should be around here, I think... 」"
        
        show ka 003 with dis
    
        ka "「That's right, you did make one.{p}\ \ ...Yeah,{w=.2} it was around here.{p}\ \ You really remembered, [fn]. 」"
        "「Seriously, 」 I thought to myself.{w} That said,\nmost of my memories have faded since I left,{w=.2}\nso why do I remember this?"
        fn "「Yeah...{w} Just like you said, it was fun, Yuuki-san.{p}\ \ That part of my memory was probably strong. 」"
        "For now, I should complete it myself."
        ka "「Huuuh.{p}\ \ Well, how about we go take a look at it? 」"
        
        scene lake with wipe_right
        play sound step13b
    
        "With that,{w=.2} everyone paired off\nand went into the grove of trees.{p}I'm sure it would look strange to most others."
        "Based on my memories and Kouya's,{w=.2} we made our way\nthrough the filtered sunlight beneath the leaves,{w=.2}\nand before long we reached our destination."
        "A small, shoddy secret base,{w=.2}\ncobbled together with scraps\nfrom Tatsu-nii's place and a towering tree."
        "Our base that could deal with the rain fairly well,{w=.2}\nusing torn blue sheets that we got from\nhere and there and fixed together for a roof."
        "When we finished at the time it looked relatively\nsteady,{w=.2} but it's very worn-out from years of neglect."
        "The scrap wood parts are rotting,{w=.2} and the blue\nsheets could no longer function as before,{w=.2} so I could\ntell that the inside was a huge mess from outside."
        
        show ke 001 at midright
        show ka 001 at midleft
        show jn 001 at farright
        show yu 001 at farleft
        with wipe_right
    
        ka "「There was a base here,{w=.2} once. 」"
        fn "「Yeah,{w=.2} it looks terrible now... 」"
        "When looking at it all ruined like this,{w=.2}\nthe conversation also felt that way."
        ke "「But, since you said you made it as a kid,{w=.2}\n\ \ it held up surprisingly okay.{p}\ \ I still see it now, since it left its form behind. 」"
        ka "「Probably because the materials weren't that bad.{p}\ \ The leftover wood at Tatsuki-san's place, remember.{w=.2}\n\ \ he let us use it for this. 」"
        fn "「Tatsu-nii's place was always a carpenter's home. 」"
        ka "「Weren't they temple builders?{p}\ \ Well,{w=.2} leaving the materials alone\n\ \ for a few years turns it into this. 」"
        yu "「But someone left it here without taking it down.{p}\ \ Is this an okay place to put it?{w} For a secret base. 」"
        ka "「Still, I wonder who it was.{w=.2}\n\ \ The one who decided to make the secret base here. 」"
        fn "「Huh, wasn't it you? 」"
        
        show ka 005 with dis
    
        ka "「...You kidding? 」"
        "「Stop playing around, 」 his rising brow seemed to say.{p}Sorry,{w=.2} but I'm not playing around here..."
        fn "「No, I'm serious.{p}\ \ When we were all deciding where to build it,{w=.2}\n\ \ you were the one who said to make it here. 」"
        ka "「Seriously?{p}\ \ ...No,{w=.2} I don't remember that at all. 」"
        fn "「I'm sure of it.{w=.2} I got the feeling\n\ \ you said something amazingly original. 」"
        fn "「It's good to have it near water,\n\ \ and it's a good place to hide it, since\n\ \ people from the village don't come here often. 」"
        ka "「...Even for me,{w=.2} how do I say it, I'm amazed. 」"
        "As he briskly scratched his head,{w=.2} Kouya faced\nthe base and looked at it one more time."
    
        show ka 001 with dis
        
        "In those eyes,{w=.2} I'm sure he's\nseeing a lot of his old memories.{p}...Because lately, that's the way it is for me."
        ka "「...Should we make one? 」"
        
        stop music fadeout 6
    
        fn "「Eh? 」"
        "I wonder when Kouya did that.{w} It's a distant\nfeeling, but I think it was after several blinks.{p}All of a sudden, Kouya opened his mouth."
        "It was too sudden,{w=.2} as I couldn't grasp\nthe meaning of his words."
        
        play music piano3_001
    
        ka "「I said 'should we make one.'{w} A secret base. 」"
        fn "「...Eh,{w=.2} right now? 」"
        "When I finally got it,{w=.2} I was so\ntaken aback by it that I didn't hear anything else."
        
        show ka 002 with dis
    
        ka "「No,{w=.2} it'd be impossible right now, but sometime.{p}\ \ This summer, next year, or maybe sometime after that. 」"
        ka "「I thought maybe it'd be fun,\n\ \ to make one again someday. 」"
        
        show ke 006 at jump_up
    
        ke "「Really!?{w} Me too!{w} I wanna do it too! 」"
        
        show yu 002 with dis
    
        yu "「Ah,{w=.2} I want to do it too then! 」"
        
        show jn 002 with dis
    
        jn "「Me three.{w=.2} I want to try. 」"
    
        show ka 003 with dis
        
        ka "「Yeah,{w=.2} let's invite all the guys\n\ \ from the village, and make a huge one.{p}\ \ It's like we're joining a secret society. 」"
        "Oh, as I thought-"
        ka "「Hey, {w=.2}[fn].{p}\ \ You're in too, aren't you? 」"
        fn "「...Of course I am.{p}\ \ There's no way I won't! 」"
        "Just as I thought, Kouya will always be Kouya."
        "For a second I saw Kouya laughing like he did\nas a kid,{w=.2} and it felt so nostalgic."
        "But now, I feel a fresh new feeling,{p}a feeling that's embarrassing,{p}but also very happy."
        
        $ meet_band = True
        
        jump end12

##################################################
label tatsuki12:

    $ event_name = "A secret shared between us"
    $ love_tatsuki += 1
    $ focus_character = "tatsuki"

    scene map
    hide screen tatsukihouse12    
    play music cicada01 fadein 7
    scene workplace2 with dis
    show tp 401 at center with dis

    tp "「[fn], you can put that here.{p}\ \ You don't haveta use the tools, so it's okay to\n\ \ drop 'em. 」"
    fn "「Yes, sir. ｣"
    
    hide tp with dis

    tp "「Now then, it's time we finish up here.{p}\ \ It's all wood shavings, so burning it will be fine.{p}\ \ Let's burn the office trash, while we're at it. 」"
    fn "「Well, that's easy enough.{p}\ \ After this... there's nothing left, right? 」"
    
    show ta 002 at center with wipe_right

    ta "「Yo, [fn]. What'cha you doing over here? 」"
    "Tatsu-nii came in, shaking his tail\nin a good mood.{w} Spotting me from\nacross the room, he came over."
    fn "「Cleaning up, as you can see.{p}\ \ You just don't learn, do you?\n\ \ You'll make him mad again. 」"
    
    show ta 008 with dis

    ta "「Heh, it's not like I came over to play.{p}\ \ Just picking up some tools, is all. 」"
    ta "「After this I'll be cleaning some wood,\n\ \ so I'll need the butterfly plane. 」"
    fn "「That one, huh? Your toolbox is over... there,\n\ \ Tatsu-nii.{w} Here, I'll get it for you.{p}\ \ This is for unrefined lumber, right? 」"
    "I took out the small tool from the bag,\nand gave it to Tatsu-nii."
    
    show ta 002 with dis

    ta "「Thanks. You know a lot now, huh?{p}\ \ Someone must have taught you without telling me. 」"
    fn "「I've been working here for how long, now?\n\ \ I should at least know this much. 」"
    
    show ta at jump_up

    ta "「Gahaha, for a guy who's never worked in carpentry,\n\ \ you sure are talking big.{p}\ \ Anyway, Tetsu-san taught you that, didn't he? 」"
    fn "「Yep, that's right. 」"
    fn "「He politely explained a bunch of stuff to me, like\n\ \ what the tools are called, how the artisans have\n\ \ their own tools, and who puts what where. 」"

    show ta 001 with dis

    ta "「I thought as much. 」"
    fn "「I remember all of it, perfectly. 」"
    
    show ta 008 with dis

    ta "「Is that so?{w} 　What's this one, then? 」"
    "As he said that, Tatsu-nii picked up a\ncarpentry tool.{w} Blackened with dirt,\nit looked like a miniature wooden cart."
    "Let's see, that one is..."
    fn "「That one's easy enough. An inking device, right?{p}\ \ It's used for drawing lines on lumber. 」"

    show ta 002 with dis
    
    ta "「Right.{w} The ink is pitch black,\n\ \ so that one was easy.{p}\ \ {nw}"
    show ta 001 with dis
    extend "What about this one? 」"
    "Tatsu-nii picked up an L-shaped tool.{p}I've seen these at school."
    fn "「That's a carpenter's square.\n\ \ I remember because of the ruler. 」"
    
    show ta 002 with dis

    ta "「You got it again.{p}\ \ It's mostly used for dimensioning, but lately\n\ \ a bunch of carpenters don't know how to use them. 」"
    fn "「Huh? It's not just some bent ruler? 」"

    show ta 008 with dis
    
    ta "「Nope.{w} Using it is an art,\n\ \ it's not just a simple measuring tool. 」"
    ta "「The carpenter's square, butterfly plane, and\n\ \ the inking device.{p}\ \ You could say those are the three key tools. 」"
    fn "「Oh, I see, then.{p}\ \ To be able to use them makes you amazing,\n\ \ Tatsu-nii. 」"
    
    show ta 001 with dis
    
    ta "「Well... I'm not that good, yet. 」"
    "Oh yeah, he's still an apprentice.{p}Always getting scolded every day.{p}Hang in there, Tatsu-nii."
    
    play music piano2_015 fadein 1.5
    show ta 004 with dis
    
    ta "「Okay, for getting everything right I'll give you\n\ \ an awesome prize.{p}\ \ {nw}"
    show ta 007 with dis
    extend "Here, I'll kiss you. 」"
    "Saying that, Tatsu-nii pushed out his hands and\nmouth and came close to me."
    fn "「Wait, what? 」"
    
    hide ta
    show ta 007 big at center_big
    with explosion

    ta "「I'll kiss yooouuu. 」"
    "Whoa, this is bad. I'm cornered.{p}Tatsu-nii's face is approaching, fast.{p}He's grabbed my shoulders firmly, so I can't run..."
    "But if it's Tatsu-nii...{w} it's okay..."
    ta "「Kiii...{w} {nw}"
    show ta 001 big with dis
    extend "Ha, just kidding.{p}\ \ Wait, why did you close your eyes?{p}\ \ You took me seriously? 」"
    fn "「That's because you seemed serious about it.{p}\ \ Besides, it's a little intimidating,\n\ \ being approached by such a big guy. 」"
    "By intimidating I mean it was exciting."
    
    hide ta
    show ta 002 at center
    with dis

    ta "「Gahaha, my bad.{w} I thought it'd be a cute prank.{p}\ \ I'd be careful if Pa said that, though.\n\ \ He might be serious about it. 」"
    
    show ta 008 with dis

    ta "「Seems like he'd do that with anyone. 」"
    "Tappei-san..."
    
    show ta 007 with dis

    ta "「Maybe I should be serious about it, too... 」"
    fn "「Wait, you mean... 」"
    
    hide ta
    show ta 007 big at center_big
    with explosion

    ta "「I'll kiss yooouuu. 」"
    "Once again, Tatsu-nii comes close to me.{p}Somehow, he's always chasing after me."
    ta "「I'm gonna kisschuuuu... 」"

    show cu 005 at farright behind ta with wipe_right

    cu "「Someone call me? 」"
    
    show ta 004 big with dis

    ta "「NO!!! 」"
    
    show ni 005 at farleft behind ta with wipeleft

    ni "「What were you two doing just now? 」"
    
    hide ta
    show ta 004 at center
    with wipe_right

    "Tatsu-nii's fellow apprentice Nikaidou-kun was\nstanding in the doorway, looking coldly at us."
    ta "「Nikaidou, stop bothering us. 」"
    
    show ni 002 with dis

    ni "「Bothering you?{w} 　Don't you have that\n\ \ the wrong way around? 」"
    ni "「I only saw a little,\n\ \ but didn't you two have a little quiz,\n\ \ start kissing, and not do one bit of work? 」"
    
    show ta 008 with dis

    ta "「As far as I'm concerned,\n\ \ talking with [fn] is an\n\ \ important bit of work. 」"
    "Tatsu-nii, don't say that.{p}Let's just get back to work..."
    
    show ni 003 with dis

    ni "「What would the boss say if he saw that? 」"
    
    show ni 001 with dis

    ni "「Anyway, [fn]-kun. 」"
    ni "「Before you got here,\n\ \ Things weren't this disordered. 」"
    ni "「The boss seems to favor you, for some reason,\n\ \ but if he saw this,\n\ \ wouldn't he pin you as the source of it all? 」"
    "That's possible...{p}I started talking without thinking,\nbecause I really wanted to talk to Tatsu-nii."
    
    show ta 005 with dis

    ta "「No, it's my fault.{p}\ \ If [fn]'s here, things are fun, and I get\n\ \ excited.{w} I just started talking, suddenly. 」"
    "Tatsu-nii hung his head and dropped his shoulders.{p}Maybe I was imagining things,\nbut he seemed more apologetic than normal."
    
    show ni 002 with dis

    ni "「I don't care what you do,\n\ \ but I don't want it to get in the way of work. 」"
    ni "「There's time after work for that sort of thing,\n\ \ so leave it until then, yeah? 」"
    
    show ta 007 with dis

    ta "「No, it's... 」"
    
    play music cicada01 fadein .7
    scene workplace2
    show tp 401 at midleft
    show ni 001 at midright
    with wipe_right

    tp "「Hey, who was the guy who planed this wood? 」"
    "Looking over to the source of the commotion,\nI see Tappei-san storming in with a daemon face on."
    ni "「I did that. 」"
    
    show tp 403 with dis

    tp "「Dumbass!! 」"

    play sound tm2_hit002
    show tp at hit_right

    tp "「The bark's rough, and uneven.\n\ \ You did it without looking again, didn't you? 」"
    tp "「I'm always telling you to watch your work!\n\ \ How many times do I need to say it,\n\ \ before it sinks in?! 」"
    
    show ni 005 with dis

    ni "「I'm sorry.{w} How can I remember to do it? 」"
    
    show ni 004 with dis

    ni "「You tell me to 'see the trees',\n\ \ But I can't understand without better explanation.{p}\ \ Can you explain it more clearly? 」"
    tp "「Shut up. This aint a theory. 」"
    ni "「But if you don't explain, then I can't understand. 」"
    tp "「Stop arguing about every little thing\n\ \ and put a sock in it.{p}\ \ If you hate this that much, quit. 」"
    ni "「I won't quit. 」"
    
    show cu 002 at farright with wipe_right

    cu "「Can't see the forest for the trees, eh? 」"
    tp "「Wrong. 」"
    
    show tp at hit_right
    play sound tm2_hit002
    show cu 009

    $ chuu_beat += 1

    "{size=+20}Wham!"
    
    hide cu with wipe_down
    play sound bosu35
    show workplace2 at vshake

    "Whoa, that looked like it hurt...{p}He'd be better off keeping his mouth shut..."
    
    show te 003 at farleft with wipeleft

    te "「There is...{w} something about a craftsman's work.\n\ \ It is not something that can be easily explained,{p}\ \ and there are parts that can't be told with words. 」"
    te "「I think the boss wants to say that.{p}\ \ The trees remember their feelings over the years. 」"
    te "「No one can teach you this.\n\ \ You must ask the tree itself, and it will tell you.{p}\ \ Only then can craftsmen learn, by experience. 」"
    
    show te 001 with dis

    te "「That's what it means to 'see the trees'.\n\ \ Right, boss? 」"
    
    show tp 406 with dis

    tp "「Tch,{w=.2} you smooth-talking...{p}\ \ Okay, but I'm not putting up with it next time.{p}\ \ I'm not saying this again. 」"
    te "「Next time, we will place the planes better.{p}\ \ Let's do our best. 」"
    
    show tp at hit_right

    tp "「Keh,{w=.2} have it your way. 」"
    "Tappei-san had an angry look as he turned away,\nbut his tail was twitching from side to side."
    "Could Tappei-san be a tsundere at work!?"
    
    play music pops_004 fadein 2
    hide tp with wipe_right
    show ta 002 at midleft behind te with wipeleft

    ta "「Good luck with that.{w} I'm pretty skilled,\n\ \ so there's nothing for me to learn.\n\ \ I know all about trees' feelings by now. 」"

    show ni 002 with dis

    ni "「What...? Don't you people get angry every day?{p}\ \ As for what just happened, you do exactly the same. 」"
    
    show ta 004 at jump_up

    ta "「What?! Say that again! 」"
    "This is not good, both of them are getting mad.{p}They take each other too seriously..."
    
    hide te with wipe_right

    ta "「...You're a guy who remembers work easily,\n\ \ but you fail because you get bored too easily. 」"
    ta "「All because you don't see the wood.\n\ \ That's your problem. 」"

    show ni 003 with dis
    
    ni"「Look, you've forgotten what\n\ \ you just said about work 」"

    show ta 008 with dis
    
    ta "「Ha, I don't want to hear that from such a klutz.{p}\ \ Though, despite that, you fold the toilet paper into\n\ \ triangles and get methodical in the weirdest of places. 」"
    ta "「It creeps me out. 」"
    
    show ni 004 with dis

    ni "「Hmph... While you're so skilled with your hands,\n\ \ you just shovel food into your mouth at meals.{p}\ \ Food always ends up all over you. Disgusting. 」"
    
    show ta 004 at hit_right

    ta "「What was that...!? 」"
    
    show ni 002 with dis

    ni "「You can't let things go,\n\ \ can you? You started this... 」"
    
    show ta 003 at jump_up

    ta "{cps=0}(This has been abbreviated.)"
    
    show ta 004 with dis

    ni "「○▲□×◇ 」"
    
    show cu 009 big with explosion

    cu "「くぁｗせｄｒｆｔｇｙふじこｌｐ；＠： 」"
    "What should I do...{w} Those two aren't\nholding back.{w} Chuukichi-kun's panicking,\neven though he's not involved..."
    "I have to get Tetsuya-san to stop this,\nbefore it goes too far."
    
    scene workplace2
    show te 003 at center
    with wipe_right

    "I look over to Tetsuya-san,\nand make an anxious face at him."
    "Oh... I see why he's staying quiet."
    "As the two keep fighting,\na giant shadow comes over them."
    
    scene workplace2
    show tp 403 at center
    show ta 004 at midleft
    show ni 004 at midright
    with wipe_right

    tp "「Start learning about the trees' feelings,\n\ \ and cool your dumbass heads off, already!! 」"
    
    scene white with qdis
    play sound tm2_hit002
    pause .25
    play sound tm2_hit002
    pause .25
    scene workplace2
    show tp 403 at center
    with qdis

    "Well, that's settled...{p}Those fists seem bigger than normal right now.{p}Both Tatsu-nii and Nikaidou-kun are on the floor."
    "I should probably go over there."
    
    hide tp with wipe_right
    
    $ event_name = "After Work"
    
    play music free0213 fadein 3
    
    scene black with Dissolve(.5)
    pause .1
    scene tatsukihouse_inside with Dissolve(1)
    show ta 005 at center with dis

    ta "「Guh, ow...{w=.2} those were some terrible eyes. 」"
    "There's a large bump on Tatsu-nii's head,\nAnd it looks like it really hurts...\nis he all right?"
    fn "「Are you okay, Tatsu-nii?{p}\ \ Anything broken from getting hit so hard? 」"
    
    show ta 006 with dis

    ta "「No, it's no worse than usual.{p}\ \ Seems like Pa held back a bit. 」"
    "It didn't look that way to me..."
    
    show ta 001 with dis

    ta "「Haah, the day's finally over.{p}\ \ So, how was it? You tired? 」"
    fn "「Yeah, completely exhausted.{p}\ \ It's better than when I started, though.\n\ \ I think I could do a bit more. 」"
    
    show ta 002 with dis

    ta "「Hey hey hey, getting attached to your work, huh?{p}\ \ Hey, Pa! [fn] said he wants overtime! 」"
    fn "「Hold on, I never said that. 」"
    
    show ta 001 with dis

    ta "「What? You're still able to do work.{p}\ \ Aren't you going to put in some overtime? 」"
    ta "「Pa always closes up at five,\n\ \ but it's normal for overtime in this kind of work. 」"
    fn "「That's surprising.{p}\ \ I wonder why he doesn't do overtime? 」"
    
    show ta 008 with dis

    ta "「What could it be? 」"
    ta "「Does he just not want to do it? 」"
    "Is that the true Tappei-san...?"
    
    show ta 001 with dis

    ta "「Well then, I've got some personal stuff to do,\n\ \ so just stay here, and make yourself at home. 」"
    "Hmm, personal stuff...{p}wait, what?!{p}Tatsu-nii's not even inviting me along."
    "It's impossible for Tatsu-nii to just want\nto do errands by himself.{p}So why???"
    
    show ta 002 with dis

    ta "「Catch you later.{w} See you at work. 」"
    
    hide ta with wipe_right

    ta "Tatsu-nii said that as he left me there,\n\ \ and went off by himself."
    fn "「Wait, Tatsu-nii.{w} Where are you going? 」"
    "I stopped him, in a panic, and it was effective...\nbut I asked him directly...{p}Maybe a little too directly."

    show ta 002 with wipe_right
    
    ta "「Oh, I'm headed off to work on that airplane from\n\ \ before.{w} There aren't enough parts for it,\n\ \ So I'm going to buy them from town. 」"
    fn "「You're going to get them from the\n\ \ mayor on the way, right? 」"
    
    show ta 001 with dis

    ta "「Yeah, that's right.{p}\ \ I have to get them now,\n\ \ since I'm all dirty from work. 」"
    
    show ta 005 with dis

    ta "「Anyway, if Uncle Shigure has got working parts,\n\ \ It won't matter how old the plane is.\n\ \ It should fly with no problems. 」"
    fn "「But if the mayor catches on,\n\ \ He might take the plane off you.{p}\ \ So all your hard work would come to nothing. 」"
    
    show ta 006 with dis

    ta "「Still. If the blueprints are lost, and the body stays\n\ \ all worn out, then I can't do anything on it. 」"
    
    show ta 005 with dis

    ta "「There's also the engine that needs repairing,\n\ \ so that'll keep me busy. 」"
    fn "「\"There's nothing more rewarding than working for\n\ \ free,\"{p}\ \ Or something like that, huh? 」"
    
    show ta 004 with dis

    ta "「I've salvaged a lot of stuff,\n\ \ and I've got some money saved up for this.\n\ \ It's just a matter of doing it, now. 」"
    
    show ta 008 with dis

    ta "「I'm really lucky. Because it's got a lot of\n\ \ wooden parts, I can make those sections myself. 」"
    fn "「Oh, you're able to do that?{p}\ \ It's awesome that you can\n\ \ fix up a plane like this. 」"
    
    show ta 007 with dis

    ta "「You reckon? I'm not going too far off the plans.{p}\ \ I'm just going to fix it back to the way it was. 」"

    show ta 002 with dis
    
    ta "「Well, if I'm doing it all myself,\n\ \ there's no reason I can't tweak the plans a bit. 」"
    ta "「The working parts I have are pretty modern,\n\ \ and I think they'll fit in the design properly.\n\ \ Plus, I can be picky about wood quality. 」"
    "Tatsu-nii combined a bunch of\nsweeping hand gestures\nas he talked to me about the plane."
    "When he puts his mind to something,\nit's like he never stopped being a kid."
    fn "「Right. I don't really get it, but it sounds\n\ \ like you're doing a lot of remodeling.{p}\ \ When it finally flies, you won't be afraid? 」"
    
    show ta 001 with dis

    ta "「I think I'll be too excited to be afraid.{p}\ \ Besides, this feeling of wanting to fly\n\ \ seems kinda instinctual, you know? 」"
    ta "「In ancient times, dragonmen flying seems...\n\ \ Right. 」"
    fn "「Instinctual...{p}\ \ I think I know what you mean,\n\ \ about wanting to fly. 」"

    show ta 002 with dis
    
    ta "「I know, right? Flying is a man's dream!{p}\ \ People have always wanted to soar, high in the air.{p}\ \ Even you get that feeling. 」"
    "As Tatsu-nii was saying all that,\nhe put his arm around my shoulder\nand drew me closer."
    "He didn't bend down, though,\nso he just ended up holding me under his arm."
    "Tatsu-nii kept talking as though in a trance.\nSitting down to match my height like old times,\nhe pulled me in and started ruffling my hair."
    "I love him when he's like this."
    ta "「I wonder what it feels like to fly.{p}\ \ It's probably an awesome feeling. 」"
    fn "「The feeling of freedom,\n\ \ with nothing like traffic jams to get in the way. 」"
    ta "「[fn], you don't need to worry about a thing.{p}\ \ I'll make sure I finish it soon. 」"
    "My hair was starting to get very disheveled as\nTatsu-nii kept talking."
    "I could smell the bittersweet scent of\ndragonman sweat on him."
    fn "「Okay, I'm looking forward to it. 」"
    "Going into the sky with Tatsu-nii...{p}What kind of things would we see?"
    
    show ta 004 with dis

    ta "「That's good, I'm glad you are. 」"
    ta "「When you're working on a hobby, you need to take\n\ \ time out, but I'll get it done for you, [fn]. 」"
    fn "「Are you going to do the whole thing by yourself? 」"
    
    show ta 001 with dis

    ta "「Yeah. That way, I won't bother anyone around me. 」"
    fn "「In that case, I'll help too! 」"
    
    show ta 008 with dis

    ta "「Come on, I'll be fine by myself.{p}\ \ You've already done enough, by coming back and\n\ \ working at my place. I can't let you do more... 」"
    fn "「Shouldn't you be a bit more careful?{p}\ \ If it's only for a short time, I think the guys\n\ \ at the Midoriya group would help you out. 」"
    fn "「Besides, you said you'd take me on the flight,\n\ \ so that means it's my hobby, too.{p}\ \ At least let me help. It should be fine. 」"
    
    show ta 005 with dis

    ta "「Maybe... 」"
    fn "「No go? 」"
    
    show ta 002 with dis

    ta "「You're the best, you know.{p}\ \ There's no way I could refuse. Gahahahaha!{p}\ \ I'm counting on you, partner! 」"
    
    play sound hit_p07

    "Tatsu-nii laughed, his mouth open wider than\nusual.{w} He was almost exploding with happiness, as\nhe clapped me on the back with an open hand."
    "Ouch..."
    "I was blown easily off my feet,\nand rolled across the ground like\nleaves in the wind."
    
    show ta 001 with dis

    ta "「Oh. {w=.2}Whoops... 」"
    
    show ta 002 with dis

    ta "「My bad.\n\ \ I only meant to give you a light pat.{p}\ \ I guess I overdid it, huh?{w} 　Gahaha! 」"
    fn "「'Gahaha' my ass, this isn't funny.{p}\ \ How'd I go that far with just a pat?{p}\ \ I can't be that light. 」"
    ta "「Hey, maybe you are.{p}\ \ Just eat more meat. 」"
    fn "「Tatsu-nii, you're probably the\n\ \ only one who'd say that... 」"
    
    show ta 008 with dis

    ta "「Heh, that's because I'm already big enough. 」"
    "His excuses are so childish.\nThey really haven't changed at all."
    "I always knew he'd grow up to be a craftsman,\nBut I never thought he'd want to fly.{p}I wonder how long he's been thinking about it."
    fn "「Hey, Tatsu-nii.{w} When did you start thinking\n\ \ about flying?{p}\ \ Was it a dream that just got bigger, over time? 」"
    
    show ta 001 with dis

    ta "「Yeah, there's that.{p}\ \ But the biggest reason is... 」"
    ta "「[fn]. 」"
    "Tatsu-nii looked serious as he turned to face me."
    ta "「Don't you remember? 」"
    "This wasn't the usual Tatsu-nii,\nthe one who'd always joke around,\nmake clumsy mistakes, or laugh too much."
    "As I look at the new Tatsu-nii,\nit feels like I'm being suffocated."
    "Why is that?"
    
    show ta 004 with dis

    ta "「The 29th of each month is Meat Day!{p}\ \ Meat's on sale at supermarkets,\n\ \ So we can eat a whole bunch!! 」"
    ta "「Gah!{w} But not at Minasato's market!!! 」"
    fn "「Huh!? 」"
    "Before I could even ask that,\nTatsu-nii punched his hand and cried out.{p}What is this?"
    
    show ta 001 with dis

    ta "「Oh, it's nothing.{p}\ \ Just that you should eat more. 」"
    "Oh, really..."
    "Could it be that you're changing the subject...?"
    
    show ta 002 with dis

    ta "「All right, from today on you'll be helping me,\n\ \ partner.{w} The only thing I need to do today is a\n\ \ bit of shopping, so you can just take it easy. 」"
    "Aren't you going to take me with you?{p}Maybe it really is nothing..."
    
    menu:
        "A. Force yourself along":
            jump tatsuki12_force
        "B. Stay quiet":
            jump tatsuki12_quiet
            
    ###########################################        
    label tatsuki12_force:

        $ event_name = "Changing Clothes"

        play music free53 fadein 3
    
        fn "「Hey, I'll come with you. 」"
        
        show ta 008 with dis
    
        ta "「You'll be bored if you come.\n\ \ Shopping isn't anything exciting. 」"
        fn "「No way, I wanna come with you.{p}\ \ I don't wanna be left here by myself. 」"
        
        show ta 010 with dis
    
        ta "「C'mon, don't whine like that... 」"
        fn "「I'll keep it up until you let me come.{p}\ \ Take me!{w=.2}　Take me!{w=.2} Take me!{w=.2} Take me!{w=.2}　C'mon!{w=.2} Take me!{w=.2}\n\ \ Take me!{w=.2} Take me!{w=.2} Take me!{w=.2} 」"
    
        show ta 004 with qdis
    
        ta "「Gah, shut up already! 」"
        
        show ta 008 with dis
    
        ta "「Okay, okay, you can come. 」"
        fn "「Hooray! 」"
    
        show ta 007 with dis
        
        ta "「There's really no other way, is there.{p}\ \ I already said this won't be anything special... 」"
        fn "「Ehehe. 」"
    
        show ta 001 with dis
        
        ta "「Let's get going, then. 」"
        fn "「Oh, hold up.\n\ \ I need to change after sweating so much. 」"
        "Whew, it feels good to\nchange out of sweaty clothes."
        ta "「Now that you mention it,\n\ \ I guess I'll change, too. 」"
        
        show ta 202 with dis
    
        fn "「...Why are you stripping from the bottom up? 」"
    
        show ta 210 with dis
        
        ta "「Oh, I was thinking of changing, too. 」"
        
        scene tatsukihouse_inside
        show ta 201 at midright
        show ni 001 at midleft
        with wipe_right
    
        ni "「Why are you two stripping...? 」"
    
        show ta 204 with dis
        
        ta "「We're in the middle of changing. Don't look. 」"
        
        show ni 002 with dis
    
        ni "「I don't really get why, but if you don't want to\n\ \ be seen, shouldn't you be changing in your room,\n\ \ and not out here? 」"
        
        show ta at jump_up
        
        ta "「Hey, stop staring at [fn] like that. 」"
        
        show ni 005 with dis
    
        ni "「As I said, changing elsewhere would be better.{p}\ \ You have your own room, after all. 」"
        ni "「Besides, it's not like I'm making\n\ \ eyes at your precious [fn]-kun. 」"
        
        show ta 208 with dis
    
        ta "「So you ARE looking!{p}\ \ [fn], we don't know what he's gonna do.\n\ \ You'd better get behind me. 」"
        
        show ni 004 with dis
    
        ni "「I just said I wasn't looking at him! 」"
        
        show cu 002 at farright with wipe_right
    
        cu "「...The two of 'em get along so well. 」"
        
        show ta 204 with dis
    
        ta "「What.{w} No one could ever get along with this guy. 」"
        
        show ni 001 with dis
    
        ni "「Give me a break.{p}\ \ How can you possibly see things like that? 」"
        
        show ta 208 with dis
    
        ta "「If we didn't have to work together, I'd probably\n\ \ never remember your name. 」"
        
        show ni 002 with dis
    
        ni "「If we didn't have to work together, I'd probably\n\ \ never speak to you in the first place. 」"
    
        show ta 204 with dis
        
        ta "「Totally.{w} I hate argumentative know-it-alls. 」"
        
        show ni 001 with dis
    
        ni "「Right. I could never accept people who are\n\ \ so rude and unrefined. 」"
        ta "「So we agree. 」"
        ni "「Indeed. 」"
        "Looks like you two are getting on well enough..."
        
        show cu 007 with dis
     
        cu "「Anyway, Aniki's body is so smooth. No fur at all!{p}\ \ This is th' first time I've seen a human's body.{p}\ \ Nikaidou-san, you had a good look, didn't ya? 」"
        
        show ta 201 with dis
    
        ta "「Hey, I'm smooth, too. 」"
        
        show ni 004 with dis
    
        ni "「I wasn't looking. 」"
        
        show cu 011 with dis
    
        cu "「(Humans 've got such strange bodies.\n\ \ 'S kinda exciting.) 」"
        fn "「Come to mention it, I don't remember\n\ \ seeing many humans around Minasato.{p}\ \ Am I that unusual? 」"
        ta "「Well, there's the old man at Raimon... 」"
        
        show cu 001 with dis
    
        cu "「Ya see one around now and then, but you haveta\n\ \ imagine what they look like wit' no clothes.{p}\ \ Furless bodies look pretty. 」"
        fn "「Is that so?{p}\ \ I'm used to seeing it,\n\ \ so I wouldn't really know. 」"
        
        show ta 204 with dis
    
        ta "「Hey!{w} 　Touch [fn],\n\ \ and I'll make you regret it! 」"
        
        show cu 007 with dis
    
        cu "「(Still, 'm not supposed to get\n\ \ all excited over another dude...) 」"
        
        show ni 003 with dis
    
        ni "「If you want beauty, look at me.{p}\ \ I'm descended from a long line of some\n\ \ of the most striking horses. 」"
        ni "「[fn]-kun's not that bad,\n\ \ but he just can't compare to me. 」"
        
        show ta 210 with dis
    
        ta "「Ha! You mean that spongy body of yours?{p}\ \ Hey, Chuu, {w=.2}show us yours. 」"
        cu "「（'S weird for this to be between guys...{w} {nw}"
        show cu 006 with dis
        extend "Huh?) 」"
        
        show cu 007 with dis
    
        cu "「Uhh, I can't do that.{p}\ \ I can't strip naked and show myself ta other guys.{p}\ \ I just can't... 」"
        
        show ta 208 with dis
    
        ta "「Hey, what's up with you? 」"
        "Does Chuukichi-kun have something to hide...?"
        
        show ta 201 with dis
    
        ta "「Now's not the time for this.{p}\ \ I've got to hurry up and finish my stuff. 」"
        
        hide ta with wipe_right
        show ta 001 at midright behind ni with wipe_right
    
        fn "「Whoa, Tatsu-nii, that's the first time I've seen\n\ \ you in plain clothes.{p}\ \ Wait, why are you wearing the work uniform? 」"
        
        show ta 008 with dis
    
        ta "「I don't have any others. 」"
        fn "「That reminds me, you hung out in\n\ \ those same clothes, too... 」"
        
        show ta 002 with dis
    
        ta "「Well, I've got a custom one with the dragon kanji\n\ \ on the back.{p}\ \ It's easy to wash it, too. 」"
        "Next payday I've got to\nget him some more clothes..."
        
        show ni 002 with dis
        
        ni "「I can't come... I made a promise to Tetsu-san,\n\ \ so you'll have to excuse me. 」"
        
        hide ni with wipe_right
        show ta 001 with dis
    
        ta "「Nuts, we'd better get going, too. 」"
        fn "「Yeah, okay.{w} Bye, Chuukichi-kun. 」"
        ta "「Later, Chuu.{w} We'll be back by dinner. 」"
        
        hide ta with wipe_right
        show cu 001 with dis
    
        cu "「Take care. 」"
        
        show cu 013 with dis
    
        cu "「Man, everyone left... 」"
        
        show cu 005 with dis
    
        cu "「(Maybe Aniki and Young Master are together,\n\ \ after all?) 」"
        
        show cu 007 with dis
    
        cu "「(They're both dudes, so no way.{p}\ \ If I tried somethin'...) 」"
    
        show cu 004 with dis
    
        cu "「(Man, 's so lonely here...) 」"
        cu "「(Looks like Nikaidou-san and Tetsuya-san 've both\n\ \ gone out. Just me, then...) 」"
        
        show tp 401 at farleft with wipeleft
    
        tp "「Chuu, you free right now? 」"
    
        show cu 005 with dis
        
        cu "「Yep, I am. 」"
        tp "「I see... 」"
        
        show cu 011 with dis
    
        cu "「(Could dis be...) 」"
    
        show cu 007 with dis
        
        cu "「(N-no way.{w} Not even if Master was th'\n\ \ Emperor of the Night.{p}\ \ I'm totally gonna be made into a toy.) 」"
        
        show cu 006 with dis
    
        cu "「There's no way, it's impossible.{p}\ \ Look at the difference in body size!{p}\ \ 'll be torn apart!) 」"
        
        show cu 007 with dis
     
        cu "「(B-but maybe I should try it...{w} Right?) 」"
    
        show tp 403 with dis
    
        tp "「Dumbass, don't think an apprentice like you\n\ \ can have time to spare!!{p}\ \ Go polish the blade of the wood plane! 」"
        tp "「Apprentices are always working, at meals, in the\n\ \ bath, right up until bedtime!{p}\ \ Don't you act all spoiled on me!!! 」"
        
        show cu 006 with dis
      
        cu "「Y-y-yes, of course!{w} I'm going right now! 」"
        
        show tp 406 with dis
    
        tp "「Keh, idjit.{w} {nw}"
        show tp at jump_up
        extend " Hic! 」"
        
        hide tp with wipe_right
        show cu 013 with dis
    
        cu "「Haah, he's in a bad mood... 」"
        cu "「Now I think about it, he's not normally like that. 」"
        
        show cu 007 with dis
    
        cu "「{nw}"
        play sound puu79_b
        extend "That's for jumping t' conclusions,\n\ \ m'boy☆ 」"
    
        scene black with sdis

        jump tatsuki12_shigure
        
    ################################################
    label tatsuki12_quiet:

        $ event_name = "Changing"
    
        show ta 001 with dis
    
        ta "「Catch you later. 」"
    
        hide ta with wipe_right
        
        "Man, there he goes.{p}Ah well, I'd better get changed."
        
        play music cicada01 fadein 1
    
        fn "「Whew. Today was hot, too. 」"
    
        show tp 401 at center with dis
        
        tp "「Hey [fn]. 」"
        fn "「Thanks for the work today, Tappei-san. 」"
        tp "「Just you here? 」"
        fn "「Yeah.{w} I was all sweaty from work,\n\ \ So I thought I'd change clothes... 」"
        tp "「Is that so. 」"
        "Somehow, it's embarrassing changing in front of\nTappei-san.{w} I wouldn't mind if everyone else were\nhere, but if it's just the two of us..."
        "Maybe I shouldn't be getting changed around here."
        
        show tp 402 with dis
    
        tp "「Well, [fn].{p}\ \ You've certainly put on a bit more meat\n\ \ since you started work here, haven't you? 」"
        "Suddenly, there was the feeling of smooth scales\nagainst my back, and a pair of hands started\npatting me all over the place."
        fn "「You think so...? 」"
        
        play music free0428 fadein 1
        show tp 407 with dis
    
        tp "「You're looking pretty good there.{p}\ \ I almost wanna just eat you up... 」"
        "I'm getting a bad feeling about this."
        fn "「Uhh, excuse me... 」"
        
        show tp 406 with dis
        
        tp "「And how are things going down below?{p}\ \ Let me just check if you've grown into a man. 」"
        "Tappei-san's hand moved up my inner thigh..."
        fn "「T-{w=.2}Tappei-san,{w} please stop. 」"
        
        show tp 402 with dis
    
        tp "「Gahahaha, you can't take a joke, can you? 」"
        "With you, I don't think it would be a joke..."
        
        show tp 401 with dis
    
        tp "「[fn], you've got some free time, right? 」"
        fn "「Uhh, yes. 」"
        tp "「Come out with me, then. 」"
        fn "「Huh? With you, Tappei-san? 」"
        
        show tp 406 with dis
    
        tp "「What is it?{p}\ \ You don't want to come with me...? 」"
        "Maybe it's reluctance, maybe it's anxiety...{p}I'm happy to go, but also a little bit scared."
        
        show tp 401 with dis
    
        tp "「I'm not going to eat you, or anything.{p}\ \ I just wanna drink at Raimon, but it looks like\n\ \ no one else is here, and drinking alone sucks. 」"
        fn "「Huh? But I can't drink...{p}\ \ And what about dinner? 」"
        tp "「You're free, right?\n\ \ Stop making excuses and come with me. 」"
        "So, I was strong-armed into going along...\nWell, more like physically dragged along."
        
        jump tatsuki12_tappei

    ##############################################    
    label tatsuki12_shigure:

        $ event_name = "Uncle Shigure"

        scene path with dis
        play music free51 fadein 1
        show ta 001 at center with wipe_right
    
        ta "「There, what'd I say?{w} 　No big deal. 」"
        fn "「You don't get it, do you Tatsu-nii?{p}\ \ Going out like this is fun, too. 」"
    
        show ta 007 with dis
        
        ta "「Oh, okay then. 」"
        
        show ta 001 with dis
    
        ta "「Oh yeah, want to go visit Uncle Shigure?{p}\ \ There's a bunch of interesting stuff at his place. 」"
        fn "「The mayor's house, huh?{p}\ \ He's the one that gave us the plane, after all. 」"
        
        show ta 002 with dis
        
        ta "「Yep.{p}\ \ His taste in antiques usually\n\ \ leans towards smaller things, "
        ta "but somehow he got the plane cheap, \nalong with the airfield. 」"
        ta "「Seems like he gave up on fixing it about\n\ \ halfway through,\n\ \ so I took the old thing off his hands. 」"
        fn "「I see, so that's how you got it.{p}\ \ and about buying the airfield...{p}\ \ So that rumour was true, then? 」"
        
        show ta 001 with dis
    
        ta "「Which rumour? 」"
        fn "「This is back when I was still living here... 」"
        fn "「I heard that the mayor's hobby of buying antiques\n\ \ grew to the point where he had too much stuff,{p}\ \ and he buried an entire cellar-full of junk. 」"
        
        show ta 008 with dis
    
        ta "「Oh, that... yeah, that's true.{p}\ \ It's an old story, though. 」"
        ta "「Lately, he's been getting even more stuff,\n\ \ so he's started renting a storehouse from Kazenari. 」"
        fn "「So the rumour was true... wow, that's awesome. 」"
        
        show ta 001 with dis
    
        ta "「No, Uncle Shigure's a fad junkie.\n\ \ Always getting into the latest thing. 」"
        ta "「Still, he gets a lot of stuff through\n\ \ mail order.{w} It's interesting to see the\n\ \ variety of stuff in his house. 」"
        fn "「What? So did he get the\n\ \ airplane by mail-order, too!? 」"
        
        show ta 008 with dis
     
        ta "「Moron. There's no way it is.{p}\ \ When it broke, the original owner\n\ \ just abandoned it. 」"
        ta "「So, when Uncle Shigure bought the plot of land,\n\ \ he got the plane with it. 」"
        
        show ta 001 with dis
      
        ta "「Once he saw the thing,\n\ \ he somehow got the idea inside his head\n\ \ to fix the thing so that it could fly again. 」"
        fn "「But he gave up,\n\ \ and decided to give it to you? 」"
        
        show ta 002 with dis
    
        ta "「That's right. It's mine, now. 」"
        "I never knew the mayor was that kind of person.{p}I only ever saw him as a guy who smiled\nand laughed."
    
        show ta 001 with dis
        
        ta "「What's up, you daydreaming again?{w} 　We're here. 」"
        fn "「Wha, huh? Oh, right. 」"
        
        hide ta with wipe_right
        scene old_house1 with Dissolve(.5)
    
        "The mayor's house is in the middle of Minasato,\na fancy place for the countryside."
        "It looks ancient. I wonder if the Midoriya group\nhas anything to do with it?"
        
        show ta 001 at midright with wipe_right
    
        ta "「Hey, Uncle, you home?{w} 　We came over to say hi. 」"
        
        play sound bosu31
        pause .25
        play sound bosu31
        pause .25
        
        "While Tatsu-nii called out in his loud voice,\nhe pounded hard on the gate."
        "A normal person would probably knock,\nbut the gate looks like it can take a beating."
        
        show sg 001 at midleft with dis
        
        $ encounter_shigure = True
    
        sg "「What a racket.{p}\ \ Are you trying to break our gate or something? 」"
        "The door opened, and the\nmayor's aged figure came into view."
        
        show ta 002 with dis
    
        ta "「Yo, we came over to play! 」"
        fn "「Good afternoon. 」"
        
        show sg 002 with dis
        
        sg "「Hohoho, good afternoon to you, too.{p}\ \ Coming over to play is fine,{p}\ \ but could you at least take pity on the gate? 」"
        ta "「Well, since you have such a huge house,\n\ \ I thought you wouldn't hear me.{w} Anyway, if I\n\ \ broke the gate, I'd fix it.{w} Gahaha! 」"
        sg "「That would be great,{p}\ \ but since you'd probably make it with a raw plank,{p}\ \ could you exercise some restraint? 」"
        
        show sg 001 with dis
    
        sg "「Besides, if you did break it, I'd still end up\n\ \ with the repair bill. Isn't that right? 」"
        ta "「Gahahaha...haha, ha. 」"
        
        show ta 001 with dis
        
        "Don't laugh, Tatsu-nii..."
        sg "「As expected.\nIt's always when I'm doing moxibustion. 」"
    
        show ta 010 with dis
        
        ta "「Hey, be careful.{p}\ \ Shigure's a martial arts expert. Even when Pa was\n\ \ younger, he'd get tossed around all the time. 」"
        "So like Juuichi-san and Torahiko, or something."
        
        scene tatsukihouse_inside
        show tp 401 at center
        with wipe_right
        pause .1
        show tp 403 at hit_right
    
        tp "「Aaa-choo!!{p}\ \ Must be getting a summer cold... 」"
        
        scene old_house1 red
        show ta 001 red at midright
        show sg 001 red at midleft
        with wipe_right
        show sg 002 red with dis
     
        sg "「Well, don't just stand there,\n\ \ come on in and we'll have\n\ \ some cold barley tea. 」"
        sg "「Would you like to\n\ \ hear about the master carpenter\n\ \ when he was young, [fn]-kun? 」"
        fn "「Wait, you know me? 」"
        
        show sg 001 red with dis
        
        sg "「Of course! You're quite the celebrity.{p}\ \ I can remember like it was yesterday,\n\ \ all of the mischief you and Torahiko got up to. 」"
        fn "「I'm very sorry.\n\ \ I was such a troublemaker back then. 」"
        
        show sg 002 red with dis
    
        sg "「Hohoho, boys will be boys.{p}\ \ No need to worry about all of that. 」"
    
        show sg 001 red with dis
    
        sg "「Hurry up and come out of the heat.{p}\ \ I don't have that much junk lying around,\n\ \ so you can relax. 」"
        fn "「Eh!?{w} Ah,{w=.2} no,{w=.2} that doesn't matter... 」"
        sg "「I like to keep stuff around my house,\n\ \ so I can have interesting things to talk to people\n\ \ about.{w} I'm renting a storehouse, too. 」"
        
        show ta 008 red with dis
        
        ta "「Wait, what!?{p}\ \ What the hell, Uncle. Seriously. 」"
        sg "「Well, it's true that the storehouse is already\n\ \ half full of things that I've bought. 」"
    
        show ta 001 red with dis
    
        ta "「Last I checked, it looked more than half full... 」"
        sg "「Is that so?{w} 　Take another look later, then.{p}\ \ Aah, I can't bear this heat.{p}\ \ Hurry up and come in, already. 」"
        fn "「Excuse us for intruding. 」"
        ta "「I love Uncle Shigure's stories.\nThey give me so much to tease Pa with. 」"
        "...Making fun of Tappei-san would be suicide..."
        
        show sg 002 red with dis
    
        sg "「Today is another scorcher...{p}\ \ It's so much nicer inside, you'll see. 」"
        sg "「While we're having tea,\n\ \ do this old man a favor\n\ \ and chat for a while. 」"
        
        show ta 002 red with dis
    
        ta "「Sure thing. 」"
        fn "「Of course. 」"
        sg "「Hmm, I think I have some candy somewhere.\nLet me go get it. 」"
        
        jump end12

    ###############################################    
    label tatsuki12_tappei:

        $ event_name = "Tappei Midoriya"

        play music daily02 fadein 3
        scene raimon1 with dis
    
        "It's still evening,\nbut since there aren't any restaurants in the\nvillage besides Raimon,"
        "there are already customers sitting\naround the place, and a busy atmosphere\nis in the air."
        
        play sound door_slide
        pause .5
        
        om "「Welcome back! 」"
        "Tappei-san and I take seats by the counter."
    
        show tp 401 at center with dis
        
        tp "「Go order whatever you like. 」"
        fn "「Okay. 」"
        "What am I going to get...?"
        "This is Raimon, so there's only so much on the\nmenu. With drinks, there's the daily special, side\ndishes, okonomiyaki, BBQ, and that's about it."
        "Hmm...{w} actually, that's plenty of variety."
        fn "「What should I get? 」"
        "We're at the counter,\nso it's probably not the best idea to get a BBQ."
        "I think I'll go for something easy to eat,\nso the okonomiyaki should be good."
        
        show tp 402 with dis
    
        tp "「I'll have the usual, overnight salted squid.{p}\ \ And then whatever goes good with that. 」"
        fn "「Well then, I'll have some oolong tea, and\n\ \ whatever goes well with that, please. 」"
        "It's been a long time, so it's a good plan\nto be trying different things.{p}I'm being treated, too."
    
        show tp 401 with dis
        
        tp "「Eh? You're not drinking? 」"
        fn "「Yes, I'm fine with tea. 」"
        
        show tp 402 with dis
    
        tp "「Don't hold back, drink all you want. 」"
        fn "「Okay. 」"
        tp "「Well, aren't you a good boy.{p}\ \ Not exactly the bottom, {w=.2}eh? 」"
        "Tappei-san gets into a very good mood after work's\nover and he comes here to drink."
        "Still,\nsince I've seen him be so scary at work,\nI'm still a little nervous of him."
        
        show tp 401 with dis
    
        tp "「Hey, [fn].{p}\ \ How've things been since you got back?\n\ \ You having fun? 」"
        fn "「Yeah, it's fun.{w} I'm back in my childhood town,\n\ \ so I can catch up with everyone.{p}\ \ I'm also helping with the Midoriya Group. 」"
    
        show tp 402 with dis
        
        tp "「That so... I'm glad you're assisting us.{p}\ \ You've been a great help. 」"
        fn "「Oh, I should be thanking you.{p}\ \ You've given me fun experiences,\n\ \ plus I'm getting part-time wages. 」"
        
        show tp 401 with dis
    
        tp "「Still, you live in the city.\n\ \ Why'd you come back to the crappy country?{p}\ \ There's nothing here, compared to the city. 」"
        fn "「That's not true.{w} There are more people and\n\ \ buildings in the city, but that's it.{p}\ \ Here, there's always something fun going on. 」"
        fn "「Also... everyone else is here.{p}\ \ I guess the hometown is the best, after all. 」"
        tp "「Maybe... 」"
        fn "「Yeah, it is. 」"
        "This is so different from the Tappei-san at work.{p}I'm sure alcohol is a part of it,\nbut maybe this is the real personality."
        
        play music free0421 fadein 3
        $ renpy.music.set_volume(0.7, 0.0, channel = "music")
        show tp 406 with dis
    
        tp "「By the way...{w} you got anyone you like? 」"
        fn "「!?{w} 　*cough, cough* I'm sorry, what? 」"
        "The question was so out of the blue that I\nalmost knocked my tea over."
        
        show tp 407 with dis
    
        tp "「At your age, it's normal to feel these things.{p}\ \ Now, how many people have you done it with? 」"
        fn "「What do you mean, 'it'!? 」"
        
        show tp 406 with dis
    
        tp "「So, ya never done it before?{p}\ \ When I was your age,\n\ \ I did it with just about anyone around. 」"
        fn "「Just about anyone...? 」"
        "Even though he's dropping a bombshell like this,\nhe's speaking like it's just a trivial memory."
        "Well, maybe it is a trivial memory, to him..."
        
        show tp 401 with dis
    
        fn "「So, how many of your friends have you slept with? 」"
        fn "「Tappei-san, you know we're both guys, right!? 」"
        tp "「'Course I know.{w} Friends your own age are fine\n\ \ and all, but how 'bout someone my age? {p}\ \ I could teach you so many things... 」"
        "He leaned towards me,\nputting his face close to mine."
        fn "「Tappei-san... I- 」"
        "He's so much bigger than Tatsu-nii..."
        "His hair's also getting a bit thinner,\nand there are wrinkles\nstarting to show in his face."
        "His scales aren't young and smooth anymore,\nthey're dry and rough."
        "Those eyes are staring hotly at me."
        fn "「I can't.{w} You have a wife,\n\ \ and Tatsu-nii... 」"
        
        show tp at jump_up
    
        tp "「Gaahahaha! You really can't take a joke, can you?{p}\ \ That's good. Means you're innocent. 」"
        fn "「Please stop.{p}\ \ If you say it, I can't hear it as a joke. 」"
        tp "「Then how about I stop joking, and get serious?{p}\ \ After this,\nI can take you somewhere where adults have fun... 」"
        fn "「I respectfully decline. 」"
        tp "「Hey, what was that for?{nw}"
        show tp at jump_up
        extend "{w=.2} Gahahaha! 」"
        "Maybe I really am the biggest sucker for jokes...{p}Why he pranks his son's friend, I'll never know."
        "Still, I saw some real seriousness in his eyes."
        
        show tp 406 with dis
    
        tp "「Old man, I want seconds! 」"
        "Maybe I was imagining it..."
        
        jump end12
    
##################################################
    
label end12:

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
    
    jump day13

