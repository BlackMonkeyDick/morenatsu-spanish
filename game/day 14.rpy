##Day 14 / Camping Trip Part 1
#################################################
label day14:
    
    $ renpy.music.set_volume(1.0, 0.0, channel = "music")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound")
    $ renpy.music.set_volume(1.0, 0.0, channel = "sound2")
    
    $ day = 14
    $ the_date = _("August 14")
    $ event_name = _("How about tomorrow")
    $ focus_character = ""
    
    scene hbroom with Dissolve(1)
    play music cicada01
    $ renpy.music.set_volume(0.7, 0.0, channel = "music")

    "Ah,{w=.3} the Bon Festival will be here soon.{p}My stay at Minasato Village is about half over."
    "But there have been a few things in the\nfirst half of the month since I got here."
    "First there was the welcoming party.\nAfter that, we split up again, but then everybody\nwent to the beach and had a good time."
    "That was fun, I'd like to go on another trip with\neverybody."
    "They'll probably be busy by the end of the\nmonth, though, so I better take action ahead of time."
    "That's right!{p}This time I should be the one to invite everybody."
    "It seems like they have a contact network,\nso I'll try calling somebody."
    "However, if I'm planning it,\nI'll have to set everything up.{p}Maybe I should search for something to do first."
    "What day would be convenient for everybody?{p}Hmm, maybe I should call them first.{p}After that..."
    
    scene black with Dissolve(1)
    $ event_name = _("Meeting time")
    play music birds_chirping
    scene sky01 
    show text _("{size=+130}August 14") at truecenter
    with Dissolve(.5)
    pause 3
    scene black with Dissolve(1)
    pause .5
    scene path with wipe_right
    play music free44
    $ renpy.music.set_volume(0.7, 0.0, channel = "music")

    fn "「Awawawawawa, this is bad.{p}\ \ This is...{w=.3} really bad. 」"
    "Why do I have to sprint as\nfast as I can this morning..."
    "That's right, this is all my fault.{p}Why could it only be today."
    
    scene market with wipe_right
    
    "Ah, there they are."
    
    scene street_corner
    show ju 001 at midright
    show to 001 at farright
    show su 001 at center
    show si 001 at farleft
    with wipe_right
    
    show su tailwag 01 with dis
    pause .2
    
    su "「Ahh,{w=.3} [fn]-san, you're late. 」"
    "I meet Shun-kun at the park,\nhis swishing tail greeting me."
    to "「Oh,{w=.3} you finally showed up.{p}\ \ I was getting tired of waiting. 」"
    ju "「[ln], it's unusual for you\n\ \ to be late on a day like today. 」"
    si "「Are you not the one who organised this? 」"
    "Just as I expected, everybody's already here.{p}I talked to them all on the phone, but..."
    "I never would have thought that we\nwere going to go the very next day..."
    fn "「Sorry, I overslept. 」"
    
    scene street_corner
    show ky 001 at midleft
    show ka 001 at farright
    show so 001 at farleft
    show ko 001 at midright
    with wipe_right
    show ko 004 with dis
    pause .2
    
    ko "「You weren't prepared to get up early?{p}\ \ That's not good if you're not staying alert\n\ \ on a day like this. 」"

    show ka 005 with dis
    
    ka "「Wait,{w=.3} you shouldn't be the one saying that... 」"
    fn "「That's right,{w=.3} you have no right to talk.{p}\ \ I should be the one saying something about\n\ \ you getting here on time. 」"

    show ko 001 with dis
    
    ko "「That's very true.{p}\ \ I did get here earlier than usual today. 」"
    
    play sound puu79_a
    show street_corner at hshake

    fn "{size=+15}「THAT'S A LIE!! 」"
    ky "「...In order to get here ahead of time,\n\ \ you would have to slow down time. 」"
    fn "「That's being late isn't it!? 」"
    
    show ko 004 with dis
    
    ko "「I was a little late, but there's\n\ \ no reason to complain.{w} The important thing\n\ \ is that I got here earlier, right? 」"
    fn "「That's still the same as being late... 」"
    
    scene street_corner
    show ju 001 at midright
    show to 001 at farright
    show su 001 at center
    show si 001 at farleft
    with wipeleft
    show to 010 with dis
    pause .2

    to "「What's strange about that?{p}\ \ Who was it that was late when he finally got here? 」"
    fn "「Well... that's- 」"
    
    show si 004 with dis
    
    si "「Even though you're about to say something,\n\ \ I want you to be level-headed.{p}\ \ {nw}"
    show si 001 with dis
    extend "How are you going to take responsibility for this? 」"
    "Aah, Shin-kun, don't look at me like that.{p}How would I take responsibility for this?"
    to "「I know how you'll take responsibility.{p}\ \ A punishment game. 」"
    fn "「But why only me this time?{p}\ \ Isn't this bullying? 」"

    show su 004 with dis
    
    su "「What will the punishment game be?{p}\ \ I feel sorry for [fn]-san. 」"
    "Shun-kun... you're so kind."

    show ju 002 with dis
    
    ju "「It's okay, Kodori.{p}\ \ It will be something everybody can\n\ \ enjoy, so don't worry. 」"
    su "「Really? 」"
    ju "「It will certainly also meet [ln]'s\n\ \ expectations. 」"
    
    show si 004 with dis
    show su 002 with dis

    su "「Okay, I undertand.{p}\ \ Please do your best, [fn]-san. 」"
    "Shun-kun was easily convinced.{p}He's even backing them up with a smiling face..."
    "I should be more concerned about why\nJuuichi-san is so interested."
    "He's usually the one who puts a stop to this.{p}Oh, I see..."
    fn "「Is that the kind of thing Juuichi-san is\n\ \ expecting of me?{p}\ \ Then I'll do my best for him! 」"
    
    hide ju
    show ju 006 at midright
    pause .01
    show ju at briefzoom

    ju "「Nobody's talking about that!! 」"
    
    scene street_corner
    show ky 001 at midleft
    show ka 001 at farright
    show so 001 at farleft
    show ko 001 at midright
    with wipe_right
    pause .2

    
    so "「[ln]-senpai... fight! 」"
    "Everybody's in a pretty good mood,\neven the members who are usually quiet are active.{p}This is an odd atmosphere for departing."
    "It seems like everybody's looking forward to this.{p}We're going to be staying overnight this time."

    scene street_corner
    show ka 002 at farleft
    show to 001 at farright
    with wipe_right
    pause .2

    to "「So, what kind of punishment game is it going to be? 」"
    ka "「We might as well do something flashy. 」"
    fn "「Oooh, that's mean... 」"
    
    play music free53 fadein .8
    scene street_corner
    show ky 001 at farright
    show so 001 at midright
    show ta 001 at farleft
    with wipeleft

    ta "「Hey, hey, let's not pester [fn] that much.\n\ \ If we're all here, it'll be a waste of time\n\ \ if we don't get started soon. 」"
    fn "「Whew, I've been saved.{p}\ \ ...Wait.{w=.3} What are we doing with the luggage? 」"
    ta "「I borrowed the truck from home, so it'll\n\ \ be riding in the back. 」"
    ta "「I packed all the stuff we might need yesterday,\n\ \ so there's no problem. 」"
    ky "「I looked it over to make sure Tatsuki-san\n\ \ didn't forget anything. 」"

    show ta 008 with dis
    
    ta "「You're terrible. I doubt I did. 」"
    fn "「Ahaha, Tatsu-nii missed something, didn't he? 」"

    show so 003 with dis
    
    so "「Um, will we be safe ridin' in the back? 」"

    show ta 002 with dis
    
    ta "「Gahaha! We're in the country, you'll be fine.{p}\ \ Satsuki and May also rode in the back when they\n\ \ moved. 」"
    
    scene street_corner
    show ju 001 at farright
    show su 001 at midright
    show ka 002 at farleft
    with wipeleft

    su "「It's like the opening of that movie.{p}\ \ My Neighbor Toto...{nw}"
    show su 005 at shivering 
    extend " mfphmfph. 」"
    ju "「Kodori, you don't need to say any more. 」"
    ka "「Guys usually go out into the country on their\n\ \ motorbikes without a helmet.{p}\ \ You'll be fine on the way to the campsite. 」"
    
    scene street_corner
    show ta 002 
    show ko 001 at midleft
    with wipe_right

    ta "「You don't need to think about a thing, just\n\ \ leave it to me, we don't have time to wait.{p}\ \ If you get it,{w=.3} then let's go, let's go! 」"
    ko "「Aand we're off! 」"
    
    scene black with wipe_up_fast
    scene street_corner
    show to 001 at midright
    show ky 001 at midleft
    show su 002
    show ko 001 at farright
    with wipe_up_fast

    su "「Waah, it's high up here... 」"
    ky "「Shun, it's dangerous to stand.{w=.3} Sit down, okay? 」"
    
    scene black with wipe_down
    scene street_corner
    show si 004
    with wipe_down

    si "「Sorry, but I'm going to take the passenger seat. 」"

    show si at move_offleft(1.5)
    show ta 001 at offright
    
    
    "Because Shin-kun has asthma, of course getting\nin the back of the truck would be too physically\ndemanding."
    "Wait, Shin-kun in the back of the truck..."
    "He'd hate that. Such a low-class thing to do\ndoesn't suit Shin-kun at all.\nIf Shin-kun had something more glamorous..."
    "A-a limousine!{p}If he had a limousine, then we could be going\nin style!!"

    show ta at move_farright(0.5)

    ta "「Hey, [fn], what are you just standing there for?{p}\ \ Are you going to be late again?Let's leave already. 」"
    fn "「Oh wait, I'm getting in. 」"
    "Oops. Recently, I haven't been able \nto stop daydreaming."
    
    scene black with wipe_up
    scene street_corner
    show to 001 at center
    with wipe_up

    to "「Is everybody in?{p}\ \ All right, Tatsu-nii, let's go.{p}\ \ I'm sincerely begging you, drive safely. 」"
    to "「Go slow and carefully, there are a lot of\n\ \ people back here... 」"
    ta "「I know, I won't drive fast.{p}\ \ You don't need to keep telling me. 」"
    fn "「I wonder if we'll be all right if he's driving... 」"
    to "「Ah, you probably shouldn't worry.{p}\ \ He's dangerous at full speed,\n\ \ but he's not a bad driver. 」"
    to "「He's actually pretty good. 」"
    fn "「He should be a racer, not a carpenter... 」"

    show to 002 with dis
    
    to "「Yeah.{w=.3} If his family business was racing,\n\ \ I think he'd become a street racer. 」"
    ta "「I can hear you from the driver's seat!{p}\ \ Are you always doing that on purpose?! 」"

    show to ray 01 with dis
    
    to "「Oh, Tatsu-nii's mad!{w=.3} Run away! 」"
    fn "「We can't run, we're on the back of a truck. 」"
    si "「It doesn't matter, are we leaving soon? 」"

    show to 007 with dis
    
    "「Okay... 」"
    
    hide to with wipe_right

    "From now on, we're camping.\nI wonder what's waiting for us.{p}Well, let's enjoy it."
    
    scene black with dis
    stop music fadeout .2
    $ event_name = _("Let's start camping")
    scene camp_site with sdis
    play music free0258

    fn "「Wow,{w=.3} this is a nice place.{p}\ \ It's like we're really out in nature. 」"
    "The campground is 30 minutes away from Minasato\nVillage, there's a nice view of the area.{p}Or should I say most of the field."
    "It looks like there's a restroom,{w=.3} but the rest of\nplace feels like it's untouched.{p}I wonder if it's being maintained."
    
    show ky 001 at midleft
    show so 001 at center
    show ta 001 at farright
    with wipe_right

    ta "「Really?{w=.3} It's not that much different\n\ \ from Minasato, even though we're so far away. 」"
    fn "「Ehh,{w=.3} I've never seen such beautiful scenery in the\n\ \ village.{w} It's like it's become a deeper green... 」"
    ky "「It's because the mountains are at a higher elevation\n\ \ than the village. 」"
    ky "「We don't really notice since we're used to this,\n\ \ but it might be different to you,\n\ \ since you've been in the city. 」"

    show so 003 with dis
    
    so "「But it does feel better than usual.{p}\ \ It changes when the mood is different, doesn't it? 」"
    ky "「Ah, that's right.{p}\ \ Besides, you grew up in the city. 」"
    so "「Yeah.{w} The air here is delicious. 」"

    scene camp_site
    show ka 002 at farleft
    show to 001 at midright
    show su 001 at center
    with wipe_right
    pause  .5

    ka "「We're camping in a different spot.{p}\ \ I wonder if sleeping in a tent is any fun. 」"
    to "「Yeah, we're so far from the village\n\ \ that it doesn't matter.{p}\ \ Let's hurry up and start. 」"

    show su 002 at jump_up
    
    su "「Woof,{w=.3} let's begin! 」"

    show su 004 with dis
    
    su "「But is the manager not here?{p}\ \ There aren't any other people staying here either. 」"

    scene camp_site with wipeleft
    
    "He's right, there's nobody else here."
    "That doesn't mean we have everything at our\ndisposal, but it's nice to have the whole\ncampground to ourselves."

    show ky 001 at midleft
    show ka 001 at farright
    show ko 001 at center
    with wipe_right

    ka "「Minasato itself is a hard-to-reach place.{p}\ \ People like to camp in the mountains over there.{p}\ \ I don't think they come here. 」"
    ky "「We should be grateful for this simplicity.{p}\ \ We have water and other minimum facilities,\n\ \ and we don't have to worry about anybody around us. 」"
    ka "「And there's also a noisy guy.{p}\ \ Look over there. 」"
    
    scene camp_site
    show to 002 at offleft
    with wipe_right
    show to at move_offright(1)
    
    to "「Hey hey hey,{w=.3} let's unload the luggage! 」"

    show si 001 at farright
    show to 002 at offleft behind si
    with wipeleft

    si "「Fu,{w=.3} I envy your abundant energy. 」"
    
    show to at move_farleft(0.5)
    show ju 001 at offleft

    to "「You wanna help? 」"
    si "「No, I'll pass.{p}\ \ I wouldn't be able to keep up. 」"
    to "「If you're jealous,{w=.3} don't be so reserved.{p}\ \ It's unexpected of you to say something nice to me. 」"
    
    show to at move_center(0.5)
    show ju at move_midleft(0.5)

    ju "「I don't think it would be praise if he wasn't\n\ \ being reserved... 」"

    show si 003 with dis

    si "「Wouldn't there be nothing to worry about if those\n\ \ muscles were in your head? 」"

    show to 006 with dis

    to "「Y-{w=.3}you don't need to go that far... 」"
    ju "「Tora... Kuroi doesn't mean any harm. 」"

    show ju 002 with dis
    
    ju "「It is a very rare occurrence,{w=.3}\n\ \ but this is a good time for you to be a noisy guy. 」"

    show to 001 with dis
    
    to "「Juuichi-senpai! 」"

    show ju 001 with dis
    
    ju "「Don't hug me, get off.{p}\ \ Hey, don't rub my belly!{p}\ \ {nw}"
    show ju 006 with dis
    show si at move_offright(1)
    extend "...Tora,{w=.3} it seems like you want me to be angry! 」"
    ju "「Humph! 」{nw}"
    
    show ju at briefzoom
    play sound bosu35
    show to 008 at move_offright_far(.7)
    extend "{w=.3}"
    
    scene camp_site
    show ky 001 at midleft
    show ta 001 at midright
    show to 006 at offright
    with wipeleft
    
    fn "「Why won't Torahiko stay quiet if he knows he's\n\ \ going to get thrown... 」"
    ky "「Who knows.{w=.3} Maybe he doesn't think about it if\n\ \ he doesn't know... 」"
    ta "「All right,{w=.3} leave the guy doing the control\n\ \ alone and I'll assign roles.{p}\ \ Let's get this set up before sunset. 」"
    fn "「Something like a cooking team,{w=.3} a campfire team,{w=.3}\n\ \ and a tent team? 」"
    ta "「I'll put up the tent.{p}\ \ This thing is mine. 」"
    fn "「Cooking is something that never did suit you. 」"

    show ta 008 with dis
    
    ta "「Well,{w=.3} I can make stuff like drinking snacks,\n\ \ so I can do a little.{p}\ \ I'm pretty good at it. 」"
    
    show to 006 at move_farright(.5)

    to "「All right then,{w=.3} I'll take control of the cooking\n\ \ team, even though I already decided that from \n\ \ the beginning. 」"
    to "「I brought the ingredients, too. 」"
    ky "「Should I prepare the campfire? 」"
    
    scene camp_site
    show ka 001 at farleft
    show su 001 at center
    with wipe_right

    ka "「We need to get firewood.{p}\ \ Should I do that? 」"

    show su 002 with dis
    
    su "「I'll help too. 」"
    
    scene camp_site
    show ta 001 at offleft
    show ko 001 at farright
    with wipe_right
    show ta at move_farleft(0.5)

    ta "「Hey, handyman,{w=.3} help me out here.{p}\ \ You work with this kind of stuff. 」"

    show ko 005 with dis
    
    ko "「My house is a hardware store, not a general store,\n\ \ we do things like machine repair and replacement.{w=.3}\n\ \ I've never touched a tent. 」"
    ta "「You've never done this?{p}\ \ If that's the case, I'll have to try to teach you. 」"
    ko "「Oh,{w=.3} all right then... 」"
    
    scene camp_site with wipeleft

    "Somehow I didn't get assigned a role.{p}I wonder what I should try."

    $ event_name = _("Curry and Rice")
    scene black with wipe_down_slow
    scene camp_site
    show ta 001 at midright
    show ko 001 at center
    with wipe_down_slow

    ko "「Aah, I'm tired.{p}\ \ And really hungry. 」"

    show ta 002 with dis
    
    ta "「What?{w=.3} Aren't you always hungry? 」"
    
    scene camp_site
    show ky 001 at farright
    show ka 001 at midleft
    show su 001 at farleft
    with wipe_right

    ky "「That took longer than I expected. 」"
    ka "「I didn't expect it to be that tough to gather\n\ \ firewood...{p}\ \ Are you all right, Shun? 」"

    show su 002 with dis
    
    su "「We survived since Kouya-san brought so much.{p}\ \ Thank you very much. 」"
    ka "「It's nothing... I just got as much as I could. 」"
    
    scene camp_site
    show to 001 at center
    show so 001 at farright
    show ko 001 at offright
    show si 001 at midleft
    with wipe_right
    show to 010 with dis

    to "「All right then,{w=.3} the curry is done. 」"
    
    show to at move_midleft(0.5)
    show so at move_center(0.5)
    show si at move_farleft(0.5)
    show ko at move_farright(0.5)

    ko "「Wow, it looks delicious.{w} You made all this? 」"
    to "「Well,{w=.3} I had a few helpers. 」"
    so "「I helped out too! 」"

    show si 002 with dis

    si "「I don't know what everybody's tastes are,\n\ \ but I think this should be good enough. 」"
    "The cooking team is a surprising combination.{p}It's a mix of those who cook and one who doesn't.{p}It just happened to be their hobby."
    to "「Anyway, let's try it. 」"
    
    scene camp_site
    show ta 001 at farleft
    show ka 001 at midright
    show ky 001 at midleft
    show su 001 at farright
    with wipeleft

    ky "「Let's sit down, everybody. 」"
    "Hmm, I wonder what this will taste like."
    ka "「...This is pretty good. 」"
    ta "「It's sweet but it tastes good.{w=.3} It's rich. 」"
    su "「It's delicious! 」"
    ky "「There's a good depth of flavor...{w=.3}\n\ \ What did you put in it?{p}\ \ It's a little sweet. 」"
    
    scene camp_site
    show to 001 at midright
    show ju 001 at midleft
    with wipe_right

    to "「Heh heh heh.{p}\ \ We had a bit of trouble,{w=.3} Juuichi-senpai\n\ \ just happened to bring his honey and he put in a lot. 」"

    show to 002 at briefzoom
    
    to "「Right,{w=.3} Senpai? 」"

    show ju 007 with dis
    
    ju "「Tora,{w=.3} that's enough of you! 」"
    su "「Juuichi-san's face is bright red. 」"
    ju "「Prepare yourself! 」"
    to "「Hehe,{w=.3} this place is so spacious that\n\ \ I've got plenty of room to run away. 」{w} {nw}"    
    hide to
    show to 002 at midright
    extend "{w=.01}{nw}"
    show to at jump_up
    extend "{w=.1}{nw}"
    show to at move_farright(0.25)
    show ju at move_midright(0.25)
    extend "{w=.25}{nw}"
    show ju at move_offleft(0.8)
    show to at move_offleft(0.4)

    "Juuichi-san tries to grab Torahiko, but he\nnimbly dodges and runs away."
    "Juuichi-san chases after him.{p}I guess Torahiko is quicker on his feet."

    scene camp_site
    show ky 001 at farright
    show si 010 at midright
    show ka 001 at farleft
    show su 001 at center
    with wipeleft

    
    si "「Can't they be quiet while we're eating? 」"
    ky "「It looks like he knew he was going to be thrown\n\ \ this time. 」"
    su "「They look like they're having fun. 」"
    ka "「This is what usually happens when we eat... 」"
    "I'm somewhat getting used to seeing this.{p}Still, this is nice.{p}Just as I thought,{w=.3} curry tastes delicious outdoors."
    
    scene camp_site
    show ju 006_run
    show to 002_run
    with wipe_right

    ju "「I won't forgive you today! 」"
    to "「Heh!{w=.3} Catch me, catch me if you can! 」"
    
    scene black with sdis
    pause .5
    $ event_name = _("Camp Fire")
    scene camp_site red
    show ta 001 red at offright
    show to 001 red at midright
    show ka 001 red at farleft
    with sdis

    ka "「Why are we also having curry for dinner? 」"
    to "「You eat curry when you go camping.{p}\ \ There's still some left. 」"
    ka "「Don't tell me we're eating curry tomorrow too... 」"

    show to 002 red with dis
    
    to "「You don't know?{p}\ \ Curry tastes even better when it sits overnight. 」"

    show ka 005 red with dis
    
    ka "「I'm going to kill you... 」"

    show to at move_center(0.5)
    show ta at move_farright(0.5)

    ta "「Well,{w=.3} I already ate everything up.{p}\ \ I'm eating to charge myself up for later. 」"
    fn "「That's right. 」"
    
    scene camp_site red with wipe_right

    fn "「Then let's start the campfire. 」"
    "I light the prepared firewood."
    "Since it was set up so that it'll easily burn,{w=.3}\nthe small flame grows into a great fire in the\nblink of an eye."
    "The lively party begins."
    
    show ky 001 red at center
    show so 001 red at midright
    with wipe_right

    ky "「Today went by so quickly.{p}\ \ It got dark before we were able to do anything. 」"
    so "「You're right.{p}\ \ But the day still hasn't ended yet. 」"
    
    scene camp_site red
    show ju 001 red at farleft
    show ta 001 red at farright
    with wipe_right
    show ta 002 red with dis

    ta "「Yep, it's going to be night.{p}\ \ Well, let's start off with a toast. 」"
    fn "「...Tatsu-nii,{w=.3} did you bring alcohol? 」"
    ta "「Isn't that natural?{w=.3} Of course I'm going to\n\ \ drink when I'm here. 」"
    ta "「I let it chill in the river water.{p}\ \ Bwah- it's delicious! 」"
    ju "「Tatsu-san, are you sure that's all right?{p}\ \ You should restrain yourself, since we're in the\n\ \ mountains... 」"
    ta "「Why? I've been waiting patiently up until now.{p}\ \ This is a campfire,{w=.3} let's rile things up. 」"
    "There's nothing we can do about this,\nwe can't even confiscate it."

    scene camp_site red
    show ka 001 red at farleft
    show to 001 red at farright
    show ta 301 red at offright
    with wipe_right
    pause .3
    show ka 002 red with dis

    ka "「You're right.{p}\ \ Even though we have a campfire, it is pretty dull\n\ \ and quiet. 」"
    "Realizing this, Kouya suddenly pulls out a guitar,{w=.3}\ncloses his eyes, and begins to play a rhythm."
    
    stop music fadeout 2

    show to 002 red with dis
    
    to "「Good, sing, sing. 」"
    
    play music free31

    ka "「Si tu esperes, je dedierai tout... 」"
    "Still playing his guitar,\nKouya begins to sing in French."
    "The way the fire illuminates the area makes the feel\nsomewhat exotic.{w} {nw}"
    
    show ka at move_offleft(0.5)
    show to at move_midleft(0.5)
    show ta at move_farright(0.5)
    extend "{w=.5}{nw}"
    show to 001 red with dis

    to "「Psh, way to sing such a stuffy song. 」"

    show ta 302 red with dis
    
    ta "「Let's do a campfire song,\n\ \ we'll have to dance later!! 」{nw}"
    show ta 202 red with wipe_down_slow
    extend ""
    
    scene camp_site red
    show ko 001 red at midright
    show ky 001 red at farleft
    show su 004 red at center
    with wipeleft

    su "「Wah,{w=.3} Tatsuki-san is naked. 」"
    ky "「Tatsuki-san, what are you taking your\n\ \ clothes off for? 」"
    
    show ko 004 red with dis

    ko "「Ah, it's no use.{p}\ \ It looks like he's totally drunk. 」"
    
    scene camp_site red
    show ta 402 red at offright_far
    with wipe_right

    ta "「Aso-re, {nw}"
    show ta at move_farright(0.5)
    extend "{w=.5}{nw}"
    show ta 402 red at jump_up
    extend "aso-re, {nw}"
    show ta at move_midright(0.5)
    extend "{w=.5}{nw}"
    show ta at jump_up
    extend "yotto...! {nw}"
    show ta at move_center(0.5)
    extend "{w=.5}{nw}"
    show ta at jump_up
    extend " 」"
    
    show ta at briefzoom
    
    ta "「C'mon, you guys, don't hold back! 」"
    "Tatsu-nii dances back and forth around the fire, naked.{p}I can't think of anything flattering to say..."

    scene camp_site red
    show ky 001 red at center
    show to 001 red at farleft
    show si 010 red at midright
    with wipe_right

    si "「It's a dancing octopus... 」"

    show to 002 red with dis
    
    to "「If Tatsu-nii's getting undressed, then I have\n\ \ no choice but to pitch in and help! 」"
    ky "「Ooshima too...? 」"
    si "「We've increased to two buffoons. 」"
    
    scene camp_site red
    show ju 001 red at center
    show ta 401 red at offleft
    show to 201 red at offright
    with wipeleft

    ju "「Tora,{w=.3} you shouldn't take off{nw}"
    show ta at move_midleft(0.5)
    show to at move_midright(0.5)
    extend "{w=.5} ... Hm? 」"

    "Uh-oh, {w=.3} when those two have that face,\nit definitely means they're scheming something..."
    
    show ta 402 red with dis

    ta "「Hee hee! 」"
    to "「Hehehe! 」"
    ju "「...What do you think you're doing? 」" 
    tato "「Now!! 」"
    
    play sound swing40_a
    hide ju
    show ju 101 red at center

    ju "「... 」{w} {nw}"
    
    show ju 107 red at briefzoom    
    show ta at move_offleft_far(0.4)
    show to at move_offleft_far(0.4)
    extend "{nw}"

    ju "「You bastards...!!{nw}"
    show ju at move_offleft_far(0.4)
    extend "{w=.3}　Give me back my clothes!!! 」"
    "Then the dragon, tiger, and bear\nstart to spin around the fire."
    
    scene black with wipe_right
    scene camp_site red
    show ta 401_run 
    show to 201_run 
    show ju 107_run 
    with wipe_right

    ju "「Tora,{w=.3} stop...!! 」"
    to "「No way... 」"
    ta "「Run, run,{w=.3} don't get caught.{p}\ \ If you get caught, you'll be killed! 」"
    
    scene black with wipeleft
    scene camp_site red
    show ta 402 red at offleft
    show si 001 red at center
    with wipeleft

    fn "「Jeez, those two... 」"
    si "「Three buffoons... 」"
    
    show ta at move_midleft(0.5)

    ta "「Oh,{w=.3} don't be afraid to dance, Shin! 」"
    
    show si 005 red with qdis

    si "「Uh, no, not me- 」"
    
    show ta at move_offleft(0.5)
    show si at move_offleft(0.5)

    "Tatsu-nii grabs on to Shin-kun,\nwho is reluctantly pulled into the middle."
    "...A kidnapper appears!"
    
    scene black with wipe_right
    scene camp_site red
    show ky 001 red at midleft
    show so 001 red at midright
    with wipe_right

    ky "「Shall we dance,{w=.3} Taro? 」"
    so "「Together!? 」"
    ky "「If you don't want to, are you going to have to\n\ \ be forced out there? 」"

    show so 003 red with dis
    
    so "「Oh, I'm not against it!{w=.3} I'd be happy to! 」"
    ky "「Really?{w=.3} Well then, let's go. 」"
    so "「Y-{w=.3}yeah! 」"
    
    scene black with wipe_right
    scene camp_site red
    show ko 001 red at midright
    show su 001 red at midleft
    with wipe_right

    ko "「Shun-kun, dance with me! 」"

    show su 202 red at jump_up
    
    su "「Okay,{w=.3} let's do it 」"
    "Shun-kun... you don't need to take off your clothes."
    
    scene black with wipe_right
    scene camp_site red 
    show to 201_stagger at offright
    show ju 107_stagger at offright_far
    with wipe_right
    
    show to at move_offleft_far(2.5)
    show ju at move_offleft_far(2.75)
    
    show ta 402_stagger at offright_far
    show si 006_stagger at offright_far

    ju "「I'm telling you to wait! 」"
    to "「Hehe,{w=.3} and I'm telling you I'm not going to 」"
    
    show ta at move_offleft_far(2.5)
    show si at move_offleft_far(2.5)
    
    show ko 001 red at offright
    show su 002 red at offright_far
    
    ta "「What's wrong? Let's enjoy ourselves! 」"
    si "「W-w-w-wait,{w=.3} Tatsuki-san!{w} I- 」"
    
    show ko 001_stagger at move_offleft_far(3.2)
    show su 002_stagger at move_offleft_far(3)
   
    show ky 001 at offright
    show so 003 at offright_far

    ko "「Ahaha!{w=.3} Spin, spin! 」"
    su "「Woof!{w=.3} We're spinning so much...! 」"
    
    show ky 001_stagger at move_offleft_far(3)
    show so 003_stagger at move_offleft_far(3.2)

    ky "「Isn't this better than you thought,{w=.3} Taro? 」"
    so "「It's because you're such a good lead, Senpai. 」"
    
    scene camp_site red
    show ta 401 red at offright
    show to 201 red at offleft
    "All around the campfire,\neverybody is dancing merrily."
    fn "「I'm too slow, I'm the only person left. 」"
    
    show to at move_midleft(0.5)
    show ta at move_midright(0.5)

    ta "「... 」"
    to "「... 」"
    
    show ta 402 red with qdis

    fn "「Hm? 」"
    "I've got a bad feeling about this..."
    to "「What person here has a gloomy face? 」"
    ta "「Were you just pretending to play\n\ \ around with me before?{p}\ \ Well then, prepare yourself! 」"
    fn "「Wait a minute... 」"
    "Uh-oh... I was careless."
    tato "「Now! 」"
    
    play sound swing40_a

    fn "「Stop...!{w=.3} Give me my clothes back! 」"
    
    stop music fadeout 1
    scene black with sdis
    play music free60 fadein 1
    scene camp_site night
    show ta 001 night at center
    with sdis
    pause .2
    show ta 002 night with dis
    $ event_name = _("Perverted Conversation")

    ta "「All right, I finished cleaning everything up.{p}\ \ I also took care of the fire. 」"
    fn "「So now we just go to sleep?{p}\ \ There's nothing to do after it gets dark. 」"
    
    scene camp_site night
    show ko 001 night at midright
    show ka 001 night at farright
    show si 001 night at farleft
    with wipe_right

    ko "「But even though it's dark, isn't it too early\n\ \ to lie down?{p}\ \ I don't think I'll be able to sleep. 」"
    ka "「Same here... 」"
    si "「Then what should we do?{p}\ \ We don't even have a single light. 」"
    "Without any kind of artificial light, the camp\nis completely dark."
    "You can only tell where you are by the moonlight,\nI don't think there's anything we can do."
    
    scene camp_site night
    show ky 001 night at farleft
    show ju 001 night at farright
    show to 001 night at center
    show so 001 night at midleft
    with wipe_right
    pause .2
    show to 010 night with dis

    to "「We're going to be packed together overnight,{w=.3}\n\ \ so we should do something before lying down 」"
    ju "「A pillow fight? 」"
    
    show to 002 night with dis
    
    to "「Maybe... 」"
    fn "「I would like to, but these are pillows for camping,\n\ \ and it's too dark for a pillow fight. 」"
    ju "「You're right...{w=.3} I guess we can't do that.{p}\ \ Besides, it would be bad if we got mud on the pillows. 」"
    "It seemed like Juuichi-san really wanted to do that..."
    to "「Hey, there's other stuff we could do. 」"
    ky "「A test of courage? 」"
    so "「That could get pretty scary here. 」"
    
    show to 005 night at briefzoom
    show su 001 night at offright
    
    to "「A-{w=.3}a test of courage!?{p}\ \ {nw}"
    show to 006 night with dis
    extend "Nonono,{w=.3} let's not do somthing so boring! 」"
    fn "「Hmm, what should we do? 」"
    
    show to at move_offleft_far(0.5)
    show ky at move_offleft_far(0.5)
    show so at move_offleft_far(0.5)
    show ju at move_farleft(0.7)
    show su at move_farright(0.7)

    su "「Ooh,{w=.3} I don't know... 」"
    ju "「Don't be afraid to say something. 」"
    
    scene camp_site night
    show to 001 night at center
    with wipeleft
    pause .3
    show to 002 night with dis

    to "「I decided on something earlier.{p}\ \ Why don't we talk about who we like? 」"
    
    scene camp_site night
    show ky 001 night at farleft
    show ju 001 night at farright
    show si 001 night at center
    with wipeleft

    ju "「... 」"
    ky "「... 」"
    si "「... 」"
    
    scene camp_site night
    show ta 008 night at farleft
    show ka 005 night at farright
    with wipeleft

    ka "「...Are you a middle-schooler? 」"
    ta "「You want to talk about the person you like...? 」"
    fn "「Well, we did go through all this trouble,\n\ \ why don't we talk about that? 」"
    fn "「Everybody here goes to high school,\n\ \ so is there somebody you like or love there? 」"

    $ renpy.music.set_volume(0.0, 1.5, channel = "music")
    scene black with wipeleft
    scene camp_site night
    show ky 002 night at farleft
    show ju 004 night at farright
    show to 011 night at center 
    with wipeleft
    pause 1.5
    scene black with wipeleft
    scene camp_site night
    show ta 007 night at farright
    show so 006 night at center 
    show ko 008 night at farleft
    with wipeleft
    pause 1.5
    scene black with wipeleft
    scene camp_site night
    show si 011 night at farright
    show su 004 night at center
    show ka 006 night at farleft
    with wipeleft
    pause 1.5
    scene camp_site night with wipeleft
    pause 1
    $ renpy.music.set_volume(0.7, 1.5, channel = "music")

    "...Huh, no response.{p}Did I say something strange?"
    fn "「Your favorite type?{p}\ \ Or somebody you have in mind? 」"
    
    show ta 007 night at center with wipe_right

    ta "「What about you, [fn]? 」"
    fn "「Eeh, me?{w=.3} Let's see...{p}\ \ I guess I like furry guys. 」"
    "I never said I like beastmen.{p}Everybody of that type is here."
    
    show ta 008 night with dis
    
    ta "「... 」"
    
    show ta 006 night with dis
    show to 001 night at offright

    ta "「I don't grow any fur!\n\ \ You don't like smooth and silky...? 」"
    fn "「Oh,{w=.3} that's not it! 」{w} {nw}"    
    show ta at move_farleft(0.5)
    show to at move_farright(0.5)
    extend "{w=.6}{nw}"
    show to 002 night with dis

    to "「I like smooth and silky too.{p}\ \ A furless guy is better than a furry guy. 」"
    
    show ta 301 night with dis

    ta "「Yeah,{w=.3} I also prefer guys who don't grow\n\ \ fur. A tiny, down-to-earth guy...{p}\ \ {nw}"
    show ta 302 night with dis
    extend "So,{w=.3} that just leaves [fn]! 」"
    fn "「What!? 」"
    ta "「You're my type.{w=.3} Gahaha! 」"
    
    scene camp_site night
    show ko 001 night at farleft
    show ju 003 night at midright
    with wipe_right

    ju "「Tatsu-san... That's... 」"
    ko "「But look at at that thing he just dropped! 」"
    "Kounosuke points at a bottle that's lying\non the ground.{p}Beast Man Mountain is written on the label."
    
    scene camp_site night
    show ky 001 night at farright
    show ka 005 night at center
    show ta 302 night at offleft_far
    with wipe_right

    ka "「It's already empty... 」"
    ky "「I thought he sobered up a while ago. 」"
    
    show ka at move_midright(0.5)
    show ta at move_farleft(0.75)

    ta "「Gahahahaha!{w=.3} [fn], get over here!{p}\ \ If you don't, I'll come to you! 」"
    
    show ka 001 night with dis

    ka "「[fn], run for it! 」"
    ky "「You'd better run all the way to Kyoto. 」"
    fn "「Okay,{w=.3} see you later. 」"
    
    scene camp_site night with wipeleft
    show ta 302 night at offright

    "I'm going to Kyoto, huh?"
    "I face that direction and start running."
    "But I wouldn't even see it by tomorrow.\nThe stars are shining in the sky."
    "I just recklessly kick at the ground,\ntake a deep breath, and run through."
    "Summer is forever in the wind."
    
    show ta at move_center(0.4)

    ta "「Guhehehe, you're not getting away! 」"
    "I'm caught."
    ta "「[fn], I've got you now...!{p}\ \ Should I give you a kiss? 」"
    fn "「Stop it, Tatsu-nii, this joke has gone far enough.{p}\ \ I smell alcohol. 」"
    "He reeks of it."
    ta "「You really are cute.{w=.3} Kiss...! 」"
    "Bleh."
    
    scene camp_site night
    show ju 001 night at farright
    show ko 001 night at midright
    show ky 001 night at midleft
    with wipe_right

    ju "「There's nothing you can do when Tatsu-san is like\n\ \ this.{w=.3} Give up. 」"
    fn "「Nooo! 」"
    
    scene camp_site night
    show ta 302 night at center
    with wipeleft

    ta "「[fn], I'm not letting you go...! 」"
    "He smells!{p}And below that smell is the smell of vomit...!!"
    "I've never been around\nsomebody so drunk..."
    "Has he been drinking a ton of alcohol?{p}No!!{w=.3} He was born a drunk!"
    ta "「Ueh- *hic*{w=.3} It's going to be nighttime...! 」"
    "He stinks!{w=.3}\nHe stinks so much...!!"
    "This such a horrible smell..."
    "Is he smelly because he smells?"
    "Rancid!!{w=.3} He's so putrid!!{w=.3} Foul!"
    "This place stinks, it stinks!"
    
    scene camp_site night
    show ju 001 night at center
    show to 001 night at farright
    with wipe_right

    to "「Did you know?{p}\ \ If you add five to his shoe size, then divide it\n\ \ by two, you'll know the size of his dick. 」"
    ju "「That's ridiculous. 」"
    
    scene camp_site night
    show ko 001 night at midleft
    show ky 001 night at farright
    show si 001 night at center
    with wipe_right

    ky "「Well, we shouldn't make light of something so\n\ \ wonderful... 」"
    ko "「Ah,{w=.3} terrible would be more or less correct. 」"
    
    show si 004 night with dis

    si "「With a body that big it'll get pretty large,\n\ \ won't it?{p}\ \ It's only natural. 」"

    show si 001 night with dis
    
    si "「Of course. 」"
    ky "「Then that means Tatsuki-san's is... 」"
    
    scene camp_site night
    show ta 302 night at center
    with wipeleft

    ta "「I'd like to have nine children.{w=.3} I'll\n\ \ give birth to them. 」"
    "He stiiinks."
    "(Note, he can't do that)"

    scene black with wipe_down_slow
    scene camp_site night
    show to 001 night at center
    show ky 001 night at farleft
    show ta 001 night at farright
    show so 001 night at midleft
    with wipe_down_slow

    ky "「Now then,{w=.3} let's get to sleep.{p}\ \ It's already a good time for that. 」"
    to "「Today you're going to have to endure not doing\n\ \ that thing you do before going to bed.{p}\ \ Even if it's an everyday thing. 」"
    
    show ta 002 night with dis

    ta "「I made sure to do that everyday thing\n\ \ before we got here. 」"
    ky "「I did it this morning, but I also I\n\ \ like to do it at night. 」"
    so "「Yeah, I also like doin' it at night. 」"
    
    scene camp_site night
    show ko 001 night at center
    show ka 001 night at farleft
    show si 001 night at midright
    with wipe_right

    ka "「Either time is good for me.{p}\ \ I do it fairly often. 」"    
    
    show ko 008 night with dis
    
    ko "「I wonder if I also do it enough... 」"
    
    show si 010 night with dis

    si "「I'm fine with doing it any time. 」"
    
    scene camp_site night
    show ju 003 night at farright
    show su 004 night at midleft
    with wipe_right

    ju "「Hey, isn't this embarrassing...?{p}\ \ Or is this just the way the conversation's gone... 」"
    ju "「I do it every morning before going\n\ \ to school... 」"
    
    show ju 004 night with dis
    
    to "「What kind do you use, everybody?{p}\ \ I use the thick kind, myself. 」"
    ju "「Tora...{w=.3} You use tools? 」"
    ky "「I use an extra-fine one. 」"
    so "「Same here. 」"
    ta "「Gahaha!{w=.3} I use a big one. 」"
    ka "「The one I use has a rounded tip. 」"

    show su 002 night at jump_up
    show to 001 night at offright behind ju

    su "「Woof!{w=.3} I get it.{p}\ \ I use the rounded bristles too. 」"
    ju "「Everybody's being so open...{p}\ \ I just use my right hand... 」"
    
    show su at move_farleft(0.4)
    show ju at move_center(0.5)
    show to at move_farright(0.55)

    to "「Eh,{w=.3} you use your right hand? 」"
    ju "「...That's right, {w=.3}my right hand 」"
    to "「For what? 」"
    ju "「You know, that healthy thing that young\n\ \ men do...{w=.3} That. 」"
    to "「What's 'that'? 」"
    ju "「You know...{w=.3} jerking off...{p}\ \ I mean, isn't that what we're talking about? 」"
    to "「'Jerk-off'? 」"
    
    show su 004 night with dis

    su "「Who's this 'jerk-off'? Is someone stopping\n\ \ you from brushing your teeth? 」"
    ju "「... 」"
    
    show to 002 night with dis
    
    ju "「... 」"
    
    show ju 007 night at briefzoom

    ju "「...Toraaa!!!{p}\ \ Bastard, you planned thiiis!{w} {nw} 」"    
    show to at move_offright_far(0.5)
    show ju at move_offright_far(0.5)
    extend "{w=.8}{nw}"
    play sound swing40_a
    extend "{w=.4}{nw}"
    play sound bosu27

    to "「Oof- 」"
    "Juuichi-san throws Torahiko with all his\npower, so that the upper half of his body\nsticks up out of the ground."
    
    scene camp_site night
    show to 008_shivering night at midleft_down
    show ju 006 night at farright
    show su 004 night at offleft
    show ka 005 night at offright
    with wipe_right

    ju "「That should cool you down.{p}\ \ Stay there and think about what you did! 」"
    
    show su at move_farleft(0.7)

    su "「What were you talking about? 」"
    ju "「Kodori, I'll tell you some other time.{w=.3}\n\ \ Just go to bed already. 」"
    
    show su at move_offleft(0.5)
    show to at move_offleft(0.5)
    show ju at move_midleft(0.6)
    show ka at move_farright(0.7)

    ka "「Are you going to teach him...? 」"
    fn "「If so, then please teach me right now. 」"
    ju "「Stop talking about that nonsense and go to sleep. 」"

    $ event_name = _("Bedtime")
    
    scene camp_site night
    show ko 001 night at center
    show su 001 night at farright
    show ta 002 night at farleft
    with wipeleft

    ta "「G'night! 」"
    
    show su 002 night with dis

    su "「Good night. 」"
    ko "「Good night! 」"
    fn "「Good night, everybody. 」"
    "This was a very busy day.{p}I'm going to enjoy tomorrow as much as I can."

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
    
    jump day15
    #jump day14

