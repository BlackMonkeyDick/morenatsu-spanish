##########################################################
###Character Bios
#########################################################

image char_main_back = "images/image/char_main_back.png"
image char_sub_back = "images/image/char_sub_back.png"
image char_winow = "images/image/menu_window.png"
image char_main = "images/image/char_main_normal.png"
image char_sub = "images/image/char_sub_normal.png"
image char_return = "images/image/char_return_normal.png"

image char_next_normal = "images/image/char_page_next_normal.png"
image char_next_hover = "images/image/char_page_next_over.png"
image char_prev_normal = "images/image/char_page_previous_normal.png"
image char_prev_hover = "images/image/char_page_previous_over.png"

image char_00 = "images/image/char_00.png"
image char_01 = "images/image/char_01.png"
image char_02 = "images/image/char_02.png"
image char_03 = "images/image/char_03.png"
image char_04 = "images/image/char_04.png"
image char_05 = "images/image/char_05.png"
image char_06 = "images/image/char_06.png"
image char_07 = "images/image/char_07.png"
image char_08 = "images/image/char_08.png"
image char_09 = "images/image/char_09.png"

image char_10 = "images/image/char_10.png"
image char_11 = "images/image/char_11.png"
image char_12 = "images/image/char_12.png"
image char_13 = "images/image/char_13.png"
image char_14 = "images/image/char_14.png"
image char_15 = "images/image/char_15.png"
image char_16 = "images/image/char_16.png"
image char_17 = "images/image/char_17.png"
image char_21 = "images/image/char_21.png"
image char_22 = "images/image/char_22.png"
image char_23 = "images/image/char_23.png"
image char_24 = "images/image/char_24.png"
image char_31 = "images/image/char_31.png"
image char_32 = "images/image/char_32.png"
image char_41 = "images/image/char_41.png"
image char_42 = "images/image/char_42.png"
image char_43 = "images/image/char_43.png"
image char_44 = "images/image/char_44.png"
image char_45 = "images/image/char_45.png"
image char_51 = "images/image/char_51.png"
image char_61 = "images/image/char_61.png"

image char_m_0_back = "images/image/char_m_0_back.png"
image char_m_1_back = "images/image/char_m_1_back.png"
image char_m_2_back = "images/image/char_m_2_back.png"
image char_m_3_back = "images/image/char_m_3_back.png"
image char_m_4_back = "images/image/char_m_4_back.png"
image char_m_5_back = "images/image/char_m_5_back.png"
image char_m_6_back = "images/image/char_m_6_back.png"
image char_m_7_back = "images/image/char_m_7_back.png"
image char_m_8_back = "images/image/char_m_8_back.png"
image char_m_9_back = "images/image/char_m_9_back.png"

image char_s_11_back = "images/image/char_s_11_back.png"
image char_s_12_back = "images/image/char_s_12_back.png"
image char_s_13_back = "images/image/char_s_13_back.png"
image char_s_14_back = "images/image/char_s_14_back.png"
image char_s_15_back = "images/image/char_s_15_back.png"
image char_s_16_back = "images/image/char_s_16_back.png"
image char_s_17_back = "images/image/char_s_17_back.png"
image char_s_21_back = "images/image/char_s_21_back.png"
image char_s_22_back = "images/image/char_s_22_back.png"
image char_s_23_back = "images/image/char_s_23_back.png"
image char_s_24_back = "images/image/char_s_24_back.png"
image char_s_31_back = "images/image/char_s_31_back.png"
image char_s_32_back = "images/image/char_s_32_back.png"
image char_s_41_back = "images/image/char_s_41_back.png"
image char_s_42_back = "images/image/char_s_42_back.png"
image char_s_43_back = "images/image/char_s_43_back.png"
image char_s_44_back = "images/image/char_s_44_back.png"
image char_s_45_back = "images/image/char_s_45_back.png"
image char_s_51_back = "images/image/char_s_51_back.png"
image char_s_61_back = "images/image/char_s_61_back.png"


screen character_picture(z):
    if z == 0:
        add "char_m_0_back"  xpos 236 ypos 26 at fadein
    elif z == 1: #Kounosuke
        add "char_m_1_back" xpos 236 ypos 26 at fadein
    elif z == 2: #Tatsuki
        add "char_m_2_back" xpos 236 ypos 26 at fadein
    elif z == 3: #Kouya
        add "char_m_3_back" xpos 236 ypos 26 at fadein
    elif z == 4: #Torahiko
        add "char_m_4_back" xpos 236 ypos 26 at fadein
    elif z == 5: #Shin
        add "char_m_5_back" xpos 236 ypos 26 at fadein
    elif z == 6: #Shun
        add "char_m_6_back" xpos 236 ypos 26 at fadein
    elif z == 7: #Kyouji
        add "char_m_7_back" xpos 236 ypos 26 at fadein
    elif z == 8: #Soutarou
        add "char_m_8_back" xpos 236 ypos 26 at fadein
    elif z == 9: #Juuichi
        add "char_m_9_back" xpos 236 ypos 26 at fadein
        
    elif z == 11: #Tappei
        add "char_s_11_back" xpos 236 ypos 26 at fadein
    elif z ==12: #Yukino
        add "char_s_12_back" xpos 236 ypos 26 at fadein
    elif z == 13: #Akira
        add "char_s_13_back" xpos 236 ypos 26 at fadein
    elif z == 14: #Chuukichi
        add "char_s_14_back" xpos 236 ypos 26 at fadein
    elif z == 15: #Tetsuya
        add "char_s_15_back" xpos 236 ypos 26 at fadein
    elif z == 16: #Shigure
        add "char_s_16_back" xpos 236 ypos 26 at fadein
    elif z == 17: #Botan
        add "char_s_17_back" xpos 236 ypos 26 at fadein
    elif z == 21: #Yukiharu
        add "char_s_21_back" xpos 236 ypos 26 at fadein
    elif z == 22: #Harue
        add "char_m_0_back"  xpos 236 ypos 26 at fadein
        add "char_s_22_back" xpos 236 ypos 26 at fadein
    elif z == 23: #Nanafuse
        add "char_s_23_back" xpos 236 ypos 26 at fadein
    elif z == 24: #Botan #He appears in two routes, but takes up two different slots
        add "char_s_24_back" xpos 236 ypos 26 at fadein
    elif z == 31: #Gaku
        add "char_s_31_back" xpos 236 ypos 26 at fadein
    elif z == 32: #Iwao
        add "char_s_32_back" xpos 236 ypos 26 at fadein
    elif z == 41: #Mitsuhisa
        add "char_s_41_back" xpos 236 ypos 26 at fadein
    elif z == 42: #Kazumi
        add "char_s_42_back" xpos 236 ypos 26 at fadein
    elif z == 43: #Yuuki
        add "char_s_43_back" xpos 236 ypos 26 at fadein
    elif z == 44: #Jun
        add "char_s_44_back" xpos 236 ypos 26 at fadein
    elif z == 45: #Keisuke
        add "char_s_45_back" xpos 236 ypos 26 at fadein
    elif z == 51: #Ten
        add "char_s_51_back" xpos 236 ypos 26 at fadein
    elif z == 61: #Amaki
        add "char_s_61_back" xpos 236 ypos 26 at fadein        
        
        
screen character_m_profile(z, page):
    if z == 1: #Kounosuke
        if page == 1:
            vbox:
                textbutton (_("   Easily gets carried away with optimism.  He likes to live life")) text_size 15
                textbutton (_("a tempo out of step with everyone else.")) text_size 15
                textbutton (_("   Although the things he does might irritate those around him, he")) text_size 15
                textbutton (_("means no offense.  Thanks to his innocent appearance they just sigh")) text_size 15
                textbutton (_("and leave it there.")) text_size 15
                at fadein                    
                xpos 250 ypos 330
                spacing -10
                
            hbox:
                imagebutton xpos 735 ypos 555 idle 'char_next_normal' hover 'char_next_hover' action ShowMenu('characters_main', 1, 2, "no")
                at fadein
                
        elif page == 2:
            vbox:
                textbutton (_("   Loves \"new things\" and \"things he has never seen before\".")) text_size 15
                textbutton (_("He often returns from the city with lots of stuff he's interested in.")) text_size 15
                textbutton (_("He is thinking about living in the city in the future.")) text_size 15
                textbutton (_("   Also, his hobby is photography.  He neatly arranges his photographs,")) text_size 15
                textbutton (_("but rarely gets an opportunity to open his album and admire them.")) text_size 15
                textbutton (_("Even though he seems like a little brother, he is actually the older")) text_size 15
                textbutton (_("brother.")) text_size 15
                xpos 250 ypos 330
                spacing -10
                
            hbox:
                imagebutton xpos 245 ypos 555 idle 'char_prev_normal' hover 'char_prev_hover' action ShowMenu('characters_main', 1, 1, "no")
                
                
    elif z ==2: #Tatsuki
        if page == 1:
            vbox:
                textbutton (_("   A lively and cheerful dragon.  As a dragon, he has a vary large physique,")) text_size 15
                textbutton (_("though he's a little worried about how much his belly has grown lately.")) text_size 15
                textbutton (_("   His family's business is carpentry that specializes in shrines.  His")) text_size 15
                textbutton (_("father's the boss, but Tatsuki is working hard every day to become just")) text_size 15
                textbutton (_("as qualified.  He dreams of being Japan's best craftsman.")) text_size 15
                at fadein                
                xpos 250 ypos 330
                spacing -10
                
            hbox:
                imagebutton xpos 735 ypos 555 idle 'char_next_normal' hover 'char_next_hover' action ShowMenu('characters_main', 2, 2, "no")
                at fadein
                
        elif page ==2:
            vbox:
                textbutton (_("   Kind to everyboy, he is like a good big brother to everyone")) text_size 15
                textbutton (_("because he likes to help.  However, little often comes out of it and")) text_size 15
                textbutton (_("he usually fails at both his job and private matters.")) text_size 15
                textbutton (_("   He is the only member of the group who can drive, but a car is like a")) text_size 15
                textbutton (_("dangerous weapon when he drives."))  text_size 15                          
                xpos 250 ypos 330
                spacing -10
                
            hbox:
                imagebutton xpos 245 ypos 555 idle 'char_prev_normal' hover 'char_prev_hover' action ShowMenu('characters_main', 2, 1, "no")
                
    elif z == 3: #Kouya
        if page == 1:
            vbox:
                textbutton (_("   He is considerate of others, however this dog has a straightforward"))  text_size 15
                textbutton (_("and rebellious atmosphere to him.  Usually calm, he is the type who burns"))  text_size 15
                textbutton (_("quietly.  He has a bit of a stubborn side to him."))  text_size 15
                textbutton (_("   Cut off from his parents, he has been living alone since graduating"))  text_size 15
                textbutton (_("from junior high."))  text_size 15
                textbutton (_(""))
                textbutton (_("   He makes a living by working and plays with his band every day, aiming"))  text_size 15
                textbutton (_("to become a musician"))  text_size 15
                at fadein                
                xpos 250 ypos 330
                spacing -10
                
    elif z == 4: #Torahiko
        if page == 1:
            vbox:
                textbutton (_("   Only son of the Ooshima Inn."))  text_size 15
                textbutton (_("   Open and optimistic, \"Let nature take its course\" is the creed he"))  text_size 15
                textbutton (_("lives by when troubled.  Helps out at home by studying to become a"))  text_size 15
                textbutton (_("quality chef."))  text_size 15
                textbutton (_("   He's getting fired up for his clubs's activities because of the upcoming"))  text_size 15
                textbutton (_("swin meet."))  text_size 15
                at fadein                
                xpos 250 ypos 330
                spacing -10
                
    elif z == 5: #Shin
        if page == 1:
            vbox:
                textbutton (_("   A young black cat who lives in a western-style house on the"))  text_size 15
                textbutton (_("outskirts of the village.  He seems out of place in the small rural town."))  text_size 15
                textbutton (_(""))
                textbutton (_("   Has a slender and handsome figure, perfect reflexes, and gets good"))  text_size 15
                textbutton (_("grades.  However he has poor physical strength.  Even with his three"))  text_size 15
                textbutton (_("good qualities, he sees himself as incomplete no matter what he does."))  text_size 15
                textbutton (_(""))
                textbutton(_("Makes sweets to keep his mind off things whenever he feels down."))  text_size 15
                at fadein                
                xpos 250 ypos 330
                spacing -10
                
    elif z == 6: #Shun
        if page == 1:
            vbox:
                textbutton (_("   He is a kind boy who has a childish personality and an innocent heart."))  text_size 15
                textbutton (_("Master of video games, he had a friendly rivalry with the main character."))  text_size 15
                textbutton (_("His tears are his strongest weapon."))  text_size 15
                textbutton (_("   After 5 years, he reunites with his senpai.  Starting high school after"))  text_size 15
                textbutton (_("this eventful summer vacation."))  text_size 15
                textbutton (_("   He's not able to fully sort out things in his head."))  text_size 15
                at fadein                
                xpos 250 ypos 330
                spacing -10
                
    elif z == 7: #Kyouji
        if page == 1:
            vbox:
                textbutton (_("   Gentle with everyone, he always finds a way to help out in one way or"))  text_size 15
                textbutton (_("another."))  text_size 15
                textbutton (_("   Everybody relies on his calm personality.  Also serves as captain of"))  text_size 15
                textbutton (_("the soccer club.  He does nothing but practice every day in order to"))  text_size 15
                textbutton (_("dominate the tournament this summer."))  text_size 15
                textbutton (_("   He is known for his clever tactivs, however hs is not perfect.  He's"))  text_size 15
                textbutton (_("not good with thunder and ghosts."))  text_size 15
                textbutton (_("   Also, he is a little timid and doesn't always say his honest opinion."))  text_size 15
                at fadein                
                xpos 250 ypos 330
                spacing -10
                
    elif z == 8: #Soutarou
        if page == 1:
            vbox:
                textbutton (_("   A very hard working yet timid boy who loves soccer."))  text_size 15
                textbutton (_("Belongs to the local soccer club.  He and his senpai, Kyouji, work up a"))  text_size 15
                textbutton (_("sweat practicing every day."))  text_size 15
                textbutton (_("   Because he grew up without a father, he relies on and adores his"))  text_size 15
                textbutton (_("Takahara-senpai."))  text_size 15
                textbutton (_("   Sometimes shows a bright and impressive smile."))  text_size 15
                textbutton (_("   Moved to the village 3 years ago; this is the first time meeting the"))  text_size 15
                textbutton (_("main character."))  text_size 15
                at fadein                
                xpos 250 ypos 330
                spacing -10
   
    elif z == 9: #Juuichi
        if page == 1:
            vbox: 
                textbutton (_("   His body has reached maturity and his mind is more than"))  text_size 15
                textbutton (_("mature enough.  His younger twin brother, whose personality is the polar"))  text_size 15
                textbutton (_("opposite, says Juuichi has \"the mind and body of an old man\"."))  text_size 15
                textbutton (_("   Usually frowning, but that doesn't always mean he's in a bad mood."))  text_size 15
                textbutton (_("Achieved black belt status in Judo by using his full strength in a"))  text_size 15
                textbutton (_("tournament."))  text_size 15
                textbutton (_("   Recently he has been emonstrating his ability thoroughly whenever"))  text_size 15
                textbutton (_("Torahiko speaks with bad manners."))  text_size 15
                at fadein                
                xpos 250 ypos 330
                spacing -10                
                
                
screen character_s_profile(z, page):
    if z == 11: #Tappei
        if page == 1:
            vbox:
                textbutton (_("   Tatsuki's father and head of the Midoriya Group.  He is 43 years old.")) text_size 15
                textbutton (_("He is an obstinate and domineering husband.  A heavy drinker, like a true")) text_size 15
                textbutton (_("Tokyoite, who gives the impression of a true craftsman.")) text_size 15
                textbutton (_("While working outsidem he is a cheerful and playful old man.")) text_size 15
                textbutton (_("   At 232 cm (~ 7' 7\"), he is considerably taller than Tatsuki, so much so")) text_size 15
                textbutton (_("that even socks don't fit him.")) text_size 15
                textbutton (_("   He loves to smoke his pipe and is bad with machines.")) text_size 15
                textbutton (_("   His wife bosses him around -- he is truly no match for her.  He is a")) text_size 15
                textbutton (_("lover of both men and women, a bisexual DILF.")) text_size 15
                at fadein                    
                xpos 250 ypos 330
                spacing -10   
                
    elif z == 12: #Yukino
        if page == 1:
            vbox:
                textbutton (_("Tatsuki's mother.  She is 41 years old,")) text_size 15
                textbutton (_("and shorter than both Tatsuki and Tappei.")) text_size 15
                textbutton (_("Her gentle, big-hearted nature makes it clear that Tatsuki takes")) text_size 15
                textbutton (_("after his mother.")) text_size 15
                textbutton (_("As someone capable of skillfully handling Tappei,")) text_size 15
                textbutton (_("they make for a good marrie couple.")) text_size 15
                at fadein                    
                xpos 250 ypos 330
                spacing -10
                
            hbox:
                imagebutton xpos 735 ypos 555 idle 'char_next_normal' hover 'char_next_hover' action ShowMenu('characters_sub', 12, 2)
                at fadein
                
        elif page == 2:
            vbox:
                textbutton (_("While it seems like she lets Tappei act as he likes,")) text_size 15
                textbutton (_("she actually has a lot of control over him.")) text_size 15
                textbutton (_("Her role in the Midoriya Group is administrative:")) text_size 15
                textbutton (_("Yukino mostly manages the finances of the Group.")) text_size 15
                textbutton (_("With clothes that compliment her Japanese beauty,")) text_size 15
                textbutton (_("she has an elegant and mature character")) text_size 15
                textbutton (_("in contrast to Tappei's rowdiness.")) text_size 15
                at fadein                    
                xpos 250 ypos 330
                spacing -10
                
            hbox:
                imagebutton xpos 245 ypos 555 idle 'char_prev_normal' hover 'char_prev_hover' action ShowMenu('characters_sub', 12, 1)
                at fadein
                
    elif z == 13: #Akira
        if page == 1:
            vbox:
                textbutton (_("   A 20-year old horse.  Son of a famous architect.  When he was 17")) text_size 15
                textbutton (_("he rebelled against his father, left home, and joined the Midoriya Group.")) text_size 15
                textbutton (_("Because of this, he is trying to build a relationship with Tatsuki and")) text_size 15
                textbutton (_("Tappei.  Incidentally, he doesn't like talking to them about runninf away")) text_size 15
                textbutton (_("from home")) text_size 15
                at fadein                    
                xpos 250 ypos 330
                spacing -10
                    
            hbox:
                imagebutton xpos 735 ypos 555 idle 'char_next_normal' hover 'char_next_hover' action ShowMenu('characters_sub', 13, 2)
                at fadein
        
        elif page == 2:
            vbox:
                textbutton (_("   The other workers don't understand the theories behind his job the")) text_size 15
                textbutton (_("way he does, but when he talks about the data and mechanics of")) text_size 15
                textbutton (_("construction he gets Tappei's fist.")) text_size 15
                textbutton (_("   His frankness doesn't mean that he is conceitedm but it often leads to")) text_size 15
                textbutton (_("misunderstands,  His fellow workers think that he and Tatsuki make")) text_size 15
                textbutton (_("good rivals.")) text_size 15
                at fadein                    
                xpos 250 ypos 330
                spacing -10
                    
            hbox:
                imagebutton xpos 245 ypos 555 idle 'char_prev_normal' hover 'char_prev_hover' action ShowMenu('characters_sub', 13, 1)
                at fadein
                
    elif z == 14: #Chuukichi
        if page == 1:
            vbox:
                textbutton (_("   A 16-year old mouse.  He dove right into society when he graduated")) text_size 15
                textbutton (_("from junior high.  He has a juvenile habit of saying \"-ssu\".")) text_size 15
                textbutton (_("   He has a simple and friendly personality, and his job brings out his")) text_size 15
                textbutton (_("enthusiasm.  He loves the Midoriya Group, but has a bit of bad luck and")) text_size 15
                textbutton (_("somehow almost always ends up getting the short end of the stick.")) text_size 15
                textbutton (_("   Despite this, he doesn't let it get him down.  He is the mood maker of")) text_size 15
                textbutton (_("the group.  However, he used to be quite mean...")) text_size 15
                textbutton (_("   He has never seen a human up close before, and his inexperienced")) text_size 15
                textbutton (_("hands make his heart thump.")) text_size 15
                textbutton (_("   Number of times he has been beaten during the game: [chuu_beat].")) text_size 15
                at fadein                    
                xpos 250 ypos 310
                spacing -10
                
    elif z == 15: #Tetsuya
        if page == 1:
            vbox:
                textbutton (_("   He is a 36-year old fox.  He is a calm veteran carpenter who works for")) text_size 15
                textbutton (_("the Midoriya Group.  Definitely skilled, he is respected by those around")) text_size 15
                textbutton (_("him and serves as the senior apprentice.")) text_size 15
                textbutton (_("   His wife and son live at home while he stays with the Midoriya")) text_size 15
                textbutton (_("Group.  He returns home to visit them every day.")) text_size 15
                textbutton (_("   Because of his levelheadedness, competency and gentle nature,")) text_size 15
                textbutton (_("newer apprentices to the Midoriya Group are extremely dependent on")) text_size 15
                textbutton (_("him.  He is usually the one who calms Tappei's temper by using a")) text_size 15
                textbutton (_("carrot-and-the-stick routine.")) text_size 15
                textbutton (_("   To Chuukichi, he is \"Merciful Tetsu-san\".")) text_size 15
                at fadein                    
                xpos 250 ypos 320
                spacing -10
                
    elif z == 16: #Shigure
        if page == 1:
            vbox:
                textbutton (_("   He is a 68-year old dog.  He is a person who is aloof from the world.")) text_size 15
                textbutton (_("He and Tatsuki's grandfather - Tappei's father - were close friends.  Now")) text_size 15
                textbutton (_("he is friends with Tappei and Mr. Botan.  Tappei's robustness and")) text_size 15
                textbutton (_("Shigure's fraility make them completely opposites.")) text_size 15
                textbutton (_("   He likes new things, and his hobby is watching TV shopping programs.")) text_size 15
                textbutton (_("He is active in restoring the village and attracting new people, and the")) text_size 15
                textbutton (_("happiness of the villagers is his number one priority.")) text_size 15
                textbutton (_("   As the current mayor, he gently watches over the people of his")) text_size 15
                textbutton (_("village.")) text_size 15
                at fadein                    
                xpos 250 ypos 330
                spacing -10
                
    elif z == 17: #Botan
        if page == 1:
            vbox:
                textbutton (_("   He is a 42-year old boar.  Because he is the only teacher in the")) text_size 15
                textbutton (_("village, he was the main character's teacher.  He is a kind teacher, but")) text_size 15
                textbutton (_("fearsome when angered.")) text_size 15
                textbutton (_("   These days he has grown fat, but he used to be an active rugby")) text_size 15
                textbutton (_("player.  Although he does have a house in the village, he spends so much")) text_size 15
                textbutton (_("time keeping watch at the school that the janitor's closet has become")) text_size 15
                textbutton (_("his second home")) text_size 15
                textbutton (_("   He is Tappei's drinking budy, but their relationship swings back and")) text_size 15
                textbutton (_("forth between public and private.")) text_size 15
                at fadein                    
                xpos 250 ypos 330
                spacing -10
                
    elif z ==21: #Yukiharu
        if page == 1:
            vbox:
                textbutton (_("   He is Kounosuke's little brother.  They are a few years apart in age.")) text_size 15
                textbutton (_("Currently in his 5th year at Minasato Elementary School.")) text_size 15
                textbutton (_("   He used to be very shy and reserved, always hiding himself behind")) text_size 15
                textbutton (_("Kounosuke.  Now he isn't shy at all and is becoming a")) text_size 15
                textbutton (_("followup to his brother.  He has a cheerful personality because of his")) text_size 15
                textbutton (_("brother's influence.")) text_size 15
                textbutton (_("   Recently he has been becoming less dependent on his brother.  This")) text_size 15
                textbutton (_("seems to make Kounosuke feel a little lonely.")) text_size 15
                at fadein                    
                xpos 250 ypos 330
                spacing -10
                
    elif z == 22: #Harue
        if page == 1:
            vbox:
                textbutton (_("  She is Kounosuke an Yukiharu's mother.  Usually quiet, she")) text_size 15
                textbutton (_("has a habit of softly saying \"ara ara\" and is a rather easygoing")) text_size 15
                textbutton (_("person.  Because of this, it's hard to tell exactly what she's")) text_size 15
                textbutton (_("thinking...")) text_size 15
                textbutton (_("   However, her quietness is connected to her large capacity")) text_size 15
                textbutton (_("to tolerate as a mother.")) text_size 15
                textbutton (_("   When Kounosuke was little, she would lose him as soon as she took")) text_size 15
                textbutton (_("her eyes off him.  The sixth sense of a mother's love would lead her right")) text_size 15
                textbutton (_("to where he was.  Just like Kounosuke and his glasses, she is usually")) text_size 15
                textbutton (_("seen wearing an apron.")) text_size 15
                at fadein                    
                xpos 250 ypos 170
                spacing -10
                
    elif z == 23: #Nanafuse
        if page == 1:
            vbox:
                textbutton (_("   The personification of Minasato Elementary's Seventh")) text_size 15
                textbutton (_("Wonder.  The ghost of a practical joker who loves to play with children")) text_size 15
                textbutton (_("more than anything else.")) text_size 15
                textbutton (_("   In the past, his existence was more vague, but by discovering Shun's")) text_size 15
                textbutton (_("appearance and hearing the main character's name called out, he")) text_size 15
                textbutton (_("gained consciousness.")) text_size 15
                at fadein                    
                xpos 250 ypos 330
                spacing -10
                    
            hbox:
                imagebutton xpos 735 ypos 555 idle 'char_next_normal' hover 'char_next_hover' action ShowMenu('characters_sub', 23, 2)
                at fadein
                    
        elif page == 2:
            vbox:
                textbutton (_("   As the personification of gossip, it's not possible for him to show his")) text_size 15
                textbutton (_("appearance to those who think he doesn't exist.  When you become an")) text_size 15
                textbutton (_("adult you will realize no one is there because you are no longer")) text_size 15
                textbutton (_("influenced by the suggestion.")) text_size 15
                textbutton (_("   An adult that can see Nanafuse will just see him as something vague")) text_size 15
                textbutton (_("like \"one of the children\", but it's possible that Nanafuse is posing as")) text_size 15
                textbutton (_("the person who knows that.")) text_size 15
                at fadein                    
                xpos 250 ypos 330
                spacing -10
                    
            hbox:
                imagebutton xpos 245 ypos 555 idle 'char_prev_normal' hover 'char_prev_hover' action ShowMenu('characters_sub', 23, 1)
                at fadein
                    
    elif z == 31: #Gaku
        if page == 1:
            vbox:
                textbutton (_("An employee at Kazenari's game store.")) text_size 15
                textbutton (_("The grandchild of Shun's grandfather's oler brother,")) text_size 15
                textbutton (_("the equivalent of a so-called secon cousin, and oler brother.")) text_size 15
                textbutton (_("His love of games is also a common point, and is taken to well.")) text_size 15
                textbutton (_(""))
                textbutton (_("With game store abundant with new works and an assortment of")) text_size 15
                textbutton (_("products, this wolf beastman works comparatively sullenly.")) text_size 15
                textbutton (_("Has bad eyes, lacks sleep, and has an unhealthy thin body.")) text_size 15
                textbutton (_("His favorite things are alcohol and cotton swabs.  He doesn't blow.")) text_size 15
                textbutton (_("He doesn't like environments where Shun cannot find happiness.")) text_size 15
                textbutton (_(""))
                textbutton (_("The name of the main character who left the village 5 years ago,")) text_size 15
                textbutton (_("which is brought up by Shun with a smile at each and every opportunity,")) text_size 15
                textbutton (_("is troublesome and awfully worrying to him these days.")) text_size 15
                at fadein                    
                xpos 250 ypos 180
                spacing -10
                
    elif z == 32: #Iwao
        if page == 1:
            vbox:
                textbutton (_("   Shun's grandfather.  Old-fashioned and stubborn, values his family's")) text_size 15
                textbutton (_("social standing above all else, and current family head of the Minasato")) text_size 15
                textbutton (_("Kodori family.")) text_size 15
                at fadein                    
                xpos 250 ypos 470
                spacing -10
                
    elif z == 41: #Mitsuhisa
        if page == 1:
            vbox:
                textbutton (_("Kouya's father.")) text_size 15
                textbutton (_("In the old days he worked at a major company, what you'd call an elite.")) text_size 15
                textbutton (_("However, around the time Kouya was one year old, there was a")) text_size 15
                textbutton (_("restructuring.  Because of his own mistakes and hardships, he wanted")) text_size 15
                textbutton (_("Kouya to go to a good school, find a job at a good company,")) text_size 15
                textbutton (_("and live that kind of life.")) text_size 15
                at fadein                    
                xpos 250 ypos 330
                spacing -10
                
            hbox:
                imagebutton xpos 735 ypos 555 idle 'char_next_normal' hover 'char_next_hover' action ShowMenu('characters_sub', 41, 2)
                at fadein
                
        if page == 2:
            vbox:
                textbutton (_("His strictness was a warped expression of his love.")) text_size 15
                textbutton (_("He knew from the beginning that Kouya hated it, yet he still")) text_size 15
                textbutton (_("stayed strict for Kouya's sake.  As kouya kept showing his stubborness.")) text_size 15
                textbutton (_("Both parent and child greatly resemble each other in this difficulty with")) text_size 15
                textbutton (_("being straightforward.")) text_size 15
                at fadein                    
                xpos 250 ypos 330
                spacing -10
                
            hbox:
                imagebutton xpos 245 ypos 555 idle 'char_prev_normal' hover 'char_prev_hover' action ShowMenu('characters_sub', 41, 1)
                at fadein
                
    elif z == 42: #Kazumi
        if page == 1:
            vbox:
                textbutton (_("   A very calm and composed lady.")) text_size 15
                textbutton (_("   It seems she's visited Kouya's new place countless times after he left")) text_size 15
                textbutton (_("home.  She wants to support Kouya's dream, but it's not as if she")) text_size 15
                textbutton (_("doesn't understand Mitsuhisa's feelings... so as she gets anxious")) text_size 15
                textbutton (_("about their child, she also worries about the complex state of things.")) text_size 15
                at fadein                    
                xpos 250 ypos 330
                spacing -10
                
    elif z == 43: #Yuuki
        if page == 1:
            vbox:
                textbutton (_("   A canary birdman who is a part of Kouya's band and is the group")) text_size 15
                textbutton (_("vocalist.")) text_size 15
                textbutton (_("   His bright eyes give off a very young impression, but despite his")) text_size 15
                textbutton (_("appearance, he's level-headed, courteous, and proper.  When his")) text_size 15
                textbutton (_("bandmate Keisuke needs a straight man, it always comes down")) text_size 15
                textbutton (_("as his role.")) text_size 15
                at fadein                    
                xpos 250 ypos 330
                spacing -10
                    
            hbox:
                imagebutton xpos 735 ypos 555 idle 'char_next_normal' hover 'char_next_hover' action ShowMenu('characters_sub', 43, 2)
                at fadein
                
        elif page == 2:
            vbox:
                textbutton (_("   Since his height doesn't reach 170cm (almost 5' 7\"), he's a little")) text_size 15
                textbutton (_("worried about it.  But at the same time, he uses his physical appearance")) text_size 15
                textbutton (_("more often than his actual age, which a point of determination for him.")) text_size 15
                at fadein                    
                xpos 250 ypos 330
                spacing -10
                    
            hbox:
                imagebutton xpos 245 ypos 555 idle 'char_prev_normal' hover 'char_prev_hover' action ShowMenu('characters_sub', 43, 1)
                at fadein
                
    elif z == 44: #Jun
        if page == 1:
            vbox:
                textbutton (_("   A tortoise-shell catman who is a part of Kouya's band and is")) text_size 15
                textbutton (_("in charge of the bass.  The look in his eyes is just a bit intense,")) text_size 15
                textbutton (_("he's quiet and never speaks more the necessary.")) text_size 15
                textbutton (_("   In exchange, he has plenty of facial expressions that immediately")) text_size 15
                textbutton (_("show what he is thinking.  His stranger anxiety is quite intense, and it")) text_size 15
                textbutton (_("seems he's trying to correct it.")) text_size 15
                at fadein                    
                xpos 250 ypos 370
                spacing -10
                    
            hbox:
                imagebutton xpos 735 ypos 555 idle 'char_next_normal' hover 'char_next_hover' action ShowMenu('characters_sub', 44, 2)
                at fadein
                
        elif page == 2:
            vbox:
                textbutton (_("   When you came back home after so long, because your ages were")) text_size 15
                textbutton (_("so close, he immediately took a liking to you, which surprised even")) text_size 15
                textbutton (_("himself a bit.")) text_size 15
                at fadein                    
                xpos 250 ypos 370
                spacing -10
                    
            hbox:
                imagebutton xpos 245 ypos 555 idle 'char_prev_normal' hover 'char_prev_hover' action ShowMenu('characters_sub', 44, 1)
                at fadein
                
    elif z == 45: #Keisuke
        if page == 1:
            vbox:
                textbutton (_("   A horseman who is part of Kouya's band and is in charge of the")) text_size 15
                textbutton (_("drums.  As the oldest of the band members he is the leader.")) text_size 15
                textbutton (_("   With his cheer, he can make just about anyone open up to him quickly.")) text_size 15
                textbutton (_("A mood-maker.  But when he gets into the mood, he makes Kouya or")) text_size 15
                textbutton (_("the vocalist Yuuki into his strict straight man.")) text_size 15
                textbutton (_("   He often says \"I look carefree don't I?  But this is also an act.")) text_size 15
                textbutton (_("To be honest I also am thinking about a lot of things as I live,\"")) text_size 15
                textbutton (_("but the people around generally don't believe him.")) text_size 15
                at fadein                    
                xpos 250 ypos 330
                spacing -10
                
    elif z == 51: #Ten
        if page == 1:
            vbox:
                textbutton (_("   The captain of Kazenari High's judo club.")) text_size 15
                textbutton (_("His presence and abilities are the real deal.")) text_size 15
                textbutton (_("   A distant blood-relative of Shun.")) text_size 15
                textbutton (_("In accordance with his family's motto")) text_size 15
                textbutton (_("'Protect the head family from the shadows',")) text_size 15
                textbutton (_("he has learned a wide variety of martial arts.")) text_size 15
                textbutton (_("   Since Juuichi-san started judo, they have been friendly rivals.")) text_size 15
                textbutton (_("Though they usually only see each other in the judo hall,")) text_size 15
                textbutton (_("on rare occasions they go other places together.")) text_size 15
                textbutton (_("Witnesses say that they don't look honest at all when standing together.")) text_size 15
                textbutton (_(" "))
                textbutton (_(" "))
                textbutton (_("His tail saying more than his mouth has been troubling him recently.")) text_size 15
                at fadein                    
                xpos 250 ypos 310
                spacing -10
                
    elif z == 61: #Amaki
        if page == 1:
            vbox:
                textbutton (_("Caretaker of the Kuroi residence in Minasato, he acts as a guardian to Shin.")) text_size 15
                textbutton (_("Graceful and polite, but reserved, he can be hard to find sometimes.")) text_size 15
                textbutton (_("Though he is a servant of the Kuroi family, he has a deep connection with")) text_size 15
                textbutton (_("Shin's father since they were young.")) text_size 15                                  
                textbutton (_("He is held in high regard, like a relative or a member of the family.")) text_size 15
                textbutton (_("From cleaning the mansion to preparing the meals, he does it all")) text_size 15
                textbutton (_("by himself with the saying 'Just another day'.")) text_size 15
                textbutton (_("By the way, his name was orignally going to be 'Tsukuyo', with his parents")) text_size 15
                textbutton (_("intending to have a baby girl, but because he was born a boy the reading")) text_size 15
                textbutton (_("of the name was changed.")) text_size 15
                at fadein                    
                xpos 250 ypos 310
                spacing -10
                


                
screen characters_main(y, p, f):
    modal True
    if f == "yes":
        add "char_main_back" at fadein
        use character_picture(y)
        use character_m_profile(y, p)
    else:
        add "char_main_back"
        use character_picture(y)
        use character_m_profile(y, p)
    #add "char_window"   
    tag menu
    
    if f == "yes":
        hbox:
            imagebutton idle "char_main" at fadein
            imagebutton idle "char_sub" action [Hide('characters_main', Dissolve(0.2)), ShowMenu('characters_sub', 0, 1)] at fadein
            xpos 20 ypos 108
            spacing 55
            
        hbox:
            #imagebutton idle "char_return" action [Hide('characters_main', Dissolve(0.5)), Show("navigation")]
            imagebutton idle "char_return" action [Hide('characters_main', dis), Show("navigation")] at fadein
            xpos 133 ypos 467
                
    
        vbox:
            if encounter_kounosuke == True:
                imagebutton idle "char_01"  action [Hide('characters_main', Dissolve(0.5)), ShowMenu('characters_main', 1, 1, "no")] at fadein
            else:
                imagebutton idle "char_00" at fadein
            if encounter_tatsuki == True:
                imagebutton idle "char_02"  action [Hide('characters_main', Dissolve(0.5)), ShowMenu('characters_main', 2, 1, "no")] at fadein
            else:
                imagebutton idle "char_00" at fadein
            if encounter_kouya == True:
                imagebutton idle "char_03"  action [Hide('characters_main', Dissolve(0.5)), ShowMenu('characters_main', 3, 1, "no")] at fadein
            else:
                imagebutton idle "char_00" at fadein
            if encounter_torahiko == True:
                imagebutton idle "char_04"  action [Hide('characters_main', Dissolve(0.5)), ShowMenu('characters_main', 4, 1, "no")] at fadein
            else:
                imagebutton idle "char_00" at fadein
            if encounter_shin == True:
                imagebutton idle "char_05"  action [Hide('characters_main', Dissolve(0.5)), ShowMenu('characters_main', 5, 1, "no")] at fadein
            else:
                imagebutton idle "char_00" at fadein
            if encounter_shun == True:
                imagebutton idle "char_06"  action [Hide('characters_main', Dissolve(0.5)), ShowMenu('characters_main', 6, 1, "no")] at fadein
            else:
                imagebutton idle "char_00" at fadein
            if encounter_kyouji == True:
                imagebutton idle "char_07"  action [Hide('characters_main', Dissolve(0.5)), ShowMenu('characters_main', 7, 1, "no")] at fadein
            else:
                imagebutton idle "char_00" at fadein
            if encounter_soutarou == True:
                imagebutton idle "char_08"  action [Hide('characters_main', Dissolve(0.5)), ShowMenu('characters_main', 8, 1, "no")] at fadein
            else:
                imagebutton idle "char_00" at fadein
            if encounter_juuichi == True:
                imagebutton idle "char_09"  action [Hide('characters_main', Dissolve(0.5)), ShowMenu('characters_main', 9, 1, "no")] at fadein
            else:
                imagebutton idle "char_00" at fadein
                
            xpos 5 ypos 145
            
    else:
        hbox:
            imagebutton idle "char_main"
            imagebutton idle "char_sub" action [Hide('characters_main', Dissolve(0.2)), ShowMenu('characters_sub', 0, 1)]
            xpos 20 ypos 108
            spacing 55
        
        hbox:
            #imagebutton idle "char_return" action [Hide('characters_main', Dissolve(0.5)), Show("navigation")]
            imagebutton idle "char_return" action [Hide('characters_main', dis), Show("navigation")]
            xpos 133 ypos 467
                
    
        vbox:
            if encounter_kounosuke == True:
                imagebutton idle "char_01"  action [Hide('characters_main', Dissolve(0.5)), ShowMenu('characters_main', 1, 1, "no")]
            else:
                imagebutton idle "char_00"
            if encounter_tatsuki == True:
                imagebutton idle "char_02"  action [Hide('characters_main', Dissolve(0.5)), ShowMenu('characters_main', 2, 1, "no")]
            else:
                imagebutton idle "char_00"
            if encounter_kouya == True:
                imagebutton idle "char_03"  action [Hide('characters_main', Dissolve(0.5)), ShowMenu('characters_main', 3, 1, "no")]
            else:
                imagebutton idle "char_00"
            if encounter_torahiko == True:
                imagebutton idle "char_04"  action [Hide('characters_main', Dissolve(0.5)), ShowMenu('characters_main', 4, 1, "no")]
            else:
                imagebutton idle "char_00"
            if encounter_shin == True:
                imagebutton idle "char_05"  action [Hide('characters_main', Dissolve(0.5)), ShowMenu('characters_main', 5, 1, "no")]
            else:
                imagebutton idle "char_00"
            if encounter_shun == True:
                imagebutton idle "char_06"  action [Hide('characters_main', Dissolve(0.5)), ShowMenu('characters_main', 6, 1, "no")]
            else:
                imagebutton idle "char_00"
            if encounter_kyouji == True:
                imagebutton idle "char_07"  action [Hide('characters_main', Dissolve(0.5)), ShowMenu('characters_main', 7, 1, "no")]
            else:
                imagebutton idle "char_00"
            if encounter_soutarou == True:
                imagebutton idle "char_08"  action [Hide('characters_main', Dissolve(0.5)), ShowMenu('characters_main', 8, 1, "no")]
            else:
                imagebutton idle "char_00" 
            if encounter_juuichi == True:
                imagebutton idle "char_09"  action [Hide('characters_main', Dissolve(0.5)), ShowMenu('characters_main', 9, 1, "no")]
            else:
                imagebutton idle "char_00"
                
            xpos 5 ypos 145
        
   
screen characters_sub(y, p):
    modal True
    add "char_sub_back"
    use character_picture(y)
    use character_s_profile(y, p)
    #add "char_reg_back" xpos 236 ypos 26
    
    hbox:
        imagebutton idle "char_main"action [Hide('characters_sub', Dissolve(0.2)), ShowMenu('characters_main', 0, 1, "no")]
        imagebutton idle "char_sub" 
        xpos 20 ypos 108
        spacing 55
        
    hbox:
            imagebutton idle "char_return" action [Hide('characters_sub', Dissolve(0.5)), Show("navigation")]
            xpos 133 ypos 467
        
        
    vbox:
        if focus_character == "":
            imagebutton idle "char_10"
            imagebutton idle "char_10"
            imagebutton idle "char_10"
            imagebutton idle "char_10"
            imagebutton idle "char_10"
            imagebutton idle "char_10"
            imagebutton idle "char_10"
            imagebutton idle "char_10"
            imagebutton idle "char_10"
            
            ypos 145
        
        elif focus_character == "tatsuki":
            if encounter_tappei == True:
                imagebutton idle "char_11"  action [Hide('characters_sub', Dissolve(0.5)), ShowMenu('characters_sub', 11, 1)]
            else:
                imagebutton idle "char_10"
            if encounter_yukino == True:
                imagebutton idle "char_12"  action [Hide('characters_sub', Dissolve(0.5)), ShowMenu('characters_sub', 12, 1)]
            else:
                imagebutton idle "char_10"
            if encounter_akira == True:
                imagebutton idle "char_13"  action [Hide('characters_sub', Dissolve(0.5)), ShowMenu('characters_sub', 13, 1)]
            else:
                imagebutton idle "char_10"
            if encounter_chuukichi == True:
                imagebutton idle "char_14"  action [Hide('characters_sub', Dissolve(0.5)), ShowMenu('characters_sub', 14, 1)]
            else:
                imagebutton idle "char_10"
            if encounter_tetsuya == True:
                imagebutton idle "char_15"  action [Hide('characters_sub', Dissolve(0.5)), ShowMenu('characters_sub', 15, 1)]
            else:
                imagebutton idle "char_10"
            if encounter_shigure == True:
                imagebutton idle "char_16"  action [Hide('characters_sub', Dissolve(0.5)), ShowMenu('characters_sub', 16, 1)]
            else:
                imagebutton idle "char_10"
            if encounter_botan1 == True:
                imagebutton idle "char_17"  action [Hide('characters_sub', Dissolve(0.5)), ShowMenu('characters_sub', 17, 1)]
            else:
                imagebutton idle "char_10"
            imagebutton idle "char_10"
            imagebutton idle "char_10"
                
            ypos 145
            
        elif focus_character == "kounosuke":
            if encounter_yukiharu == True:
                imagebutton idle "char_21"  action [Hide('characters_sub', Dissolve(0.5)), ShowMenu('characters_sub', 21, 1)]
            else:
                imagebutton idle "char_10"
            if encounter_harue == True:
                imagebutton idle "char_22"  action [Hide('characters_sub', Dissolve(0.5)), ShowMenu('characters_sub', 22, 1)]
            else:
                imagebutton idle "char_10"
            if encounter_nanafuse == True:
                imagebutton idle "char_23"  action [Hide('characters_sub', Dissolve(0.5)), ShowMenu('characters_sub', 23, 1)]
            else:
                imagebutton idle "char_10"                 
            imagebutton idle "char_10"
            imagebutton idle "char_10"
            imagebutton idle "char_10"
            imagebutton idle "char_10"
            imagebutton idle "char_10"
            imagebutton idle "char_10"
            
            ypos 145
            
        elif focus_character == "shun":
            if encounter_gaku == True:
                imagebutton idle "char_31"  action [Hide('characters_sub', Dissolve(0.5)), ShowMenu('characters_sub', 31, 1)]
            else:
                imagebutton idle "char_10"
            if encounter_iwao == True:
                imagebutton idle "char_32"  action [Hide('characters_sub', Dissolve(0.5)), ShowMenu('characters_sub', 32, 1)]
            else:
                imagebutton idle "char_10"
            imagebutton idle "char_10"
            imagebutton idle "char_10"
            imagebutton idle "char_10"
            imagebutton idle "char_10"
            imagebutton idle "char_10"
            imagebutton idle "char_10"
            imagebutton idle "char_10"
            
            ypos 145
            
        elif focus_character == "kouya":
            if encounter_mitsuhisa == True:
                imagebutton idle "char_41"  action [Hide('characters_sub', Dissolve(0.5)), ShowMenu('characters_sub', 41, 1)]
            else:
                imagebutton idle "char_10"
            if encounter_kazumi == True:
                imagebutton idle "char_42"  action [Hide('characters_sub', Dissolve(0.5)), ShowMenu('characters_sub', 42, 1)]
            else:
                imagebutton idle "char_10"
            if encounter_yuuki == True:
                imagebutton idle "char_43"  action [Hide('characters_sub', Dissolve(0.5)), ShowMenu('characters_sub', 43, 1)]
            else:
                imagebutton idle "char_10"
            if encounter_jun == True:
                imagebutton idle "char_44"  action [Hide('characters_sub', Dissolve(0.5)), ShowMenu('characters_sub', 44, 1)]
            else:
                imagebutton idle "char_10"
            if encounter_keisuke == True:
                imagebutton idle "char_45"  action [Hide('characters_sub', Dissolve(0.5)), ShowMenu('characters_sub', 45, 1)]
            else:
                imagebutton idle "char_10"
            imagebutton idle "char_10"
            imagebutton idle "char_10"
            imagebutton idle "char_10"
            imagebutton idle "char_10"
            
            ypos 145
            
        elif focus_character == "juuichi":
            if encounter_ten == True:
                imagebutton idle "char_51"  action [Hide('characters_sub', Dissolve(0.5)), ShowMenu('characters_sub', 51, 1)]
            else:
                imagebutton idle "char_10"
            imagebutton idle "char_10"
            imagebutton idle "char_10"
            imagebutton idle "char_10"
            imagebutton idle "char_10"
            imagebutton idle "char_10"
            imagebutton idle "char_10"
            imagebutton idle "char_10"
            imagebutton idle "char_10"
            
            ypos 145
            
        elif focus_character == "shin":
            if encounter_amaki == True:
                imagebutton idle "char_61"  action [Hide('characters_sub', Dissolve(0.5)), ShowMenu('characters_sub', 61, 1)]
            else:
                imagebutton idle "char_10"
            imagebutton idle "char_10"
            imagebutton idle "char_10"
            imagebutton idle "char_10"
            imagebutton idle "char_10"
            imagebutton idle "char_10"
            imagebutton idle "char_10"
            imagebutton idle "char_10"
            imagebutton idle "char_10"
            
            ypos 145
        
        
    
        
        
        
style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text
            
    
