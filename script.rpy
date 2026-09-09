image cha1 = "images/characters/A1.png"
image chb1 = "images/characters/B1.png"
image chb2 = "images/characters/B2.png"
image desk = "images/bg/desk.png"
image chcup = "images/characters/cup.png"
image chletter = "images/characters/letter.png"
image rain = "images/bg/rain.png"

init python:
    # 1. 宣告訪客類別：封裝訪客的狀態與行為資料
    class Visitor:
        def __init__(self, name):
            self.name = name
            self.attitude = 0       # 玩家互動分數（影響後續對話微調）
            self.has_tea = False    
            self.letters = [
                "十年前離家出走時寫的抱怨信",
                "父親留下的關心字條",
                "當年揉爛又被父親撿起的道歉信"
            ]

        def update_attitude(self, value):
            self.attitude += value
            if self.attitude > 2:
                self.attitude = 2
            elif self.attitude < -2:
                self.attitude = -2

    # 2. 宣告劇情主軸管理器類別：將遊戲進度與流程控制物件化
    class StoryManager:
        def __init__(self):
            self.current_act = 1
            self.unlocked_ending = None
            self.plot_nodes = {
                1: "雨夜來訪與第一階段抉擇",
                2: "三封信的重量與核心對話",
                3: "結局分歧與收尾"
            }

        def advance_act(self, next_act):
            self.current_act = next_act

        def set_ending(self, ending_name):
            self.unlocked_ending = ending_name

# 宣告角色與顯示設定
define p = Character("男主", color="#5c93c4")      # 男主
define v = Character("女孩", color="#d4738b")      # 女孩
define narrator = Character(None, what_italic=True) # 旁白

label start:
    $ visitor = Visitor("深夜訪客")
    $ game_manager = StoryManager()
    
    scene black with fade

    # -------------------------------------------------------------------------
    # 【 第一幕：雨夜來訪 】
    # -------------------------------------------------------------------------
    play sound "hearing_rain1.mp3"
    play music "piano.mp3" loop
    narrator "深夜十一點。窗外的雨勢沒有停歇的意思，反而把整個老舊街區包裹得更加寂靜。"
    narrator "木質櫃檯上的綠罩檯燈發出昏黃的光，我正收拾著桌上的郵戳，準備結束這一天的營業。"
    scene black with fade
    scene desk with fade
    play sound "being_knocked3.mp3"
    narrator "突地，門口傳來了急促而沉悶的敲門聲。"

    show cha1 at center with dissolve

    p "在這個時間點，還會有人在雨夜裡來到這間偏遠的小郵局？"
    p "……請進，門沒鎖。"

    show chb1 at center with dissolve

    v "（聲音有些沙啞，帶著明顯的疲憊）"
    v "抱歉……這麼晚了還來打擾。請問……這裡還收件嗎？但我沒有地址，也沒有郵票。"

    # 第一個重要選擇點
    menu:
        "遞上一杯剛泡好的熱茶，示意對方坐下。":
            $ visitor.update_attitude(1)
            $ visitor.has_tea = True
            jump choice_tea

        "冷淡地看著對方，指了指牆上的時鐘。":
            $ visitor.update_attitude(-1)
            $ visitor.has_tea = False
            jump choice_cold


# -----------------------------------------------------------------------------
# 分支 A：choice_tea
# -----------------------------------------------------------------------------
label choice_tea:
    p "外面的雨很大，先進來把雨擦乾吧。這裡剛好有熱茶。"
    show chcup at center with dissolve
    narrator "我將剛倒好的熱茶推了過去。對方有些驚訝地接過，指尖在溫熱的陶杯上微微發抖。"
    scene black with fade
    scene desk with fade 
    show cha1 at center with dissolve
    show chb1 at center with dissolve
    v "謝謝你……我以為這個時間，這裡已經不會有人理我了。"
    hide chcup with dissolve
    v "我只是……在整理一間老房子時，找到了一些很久以前的東西。"
    v "三封沒有寄出去的信。收件人是我父親，但寄信的人……是我自己。十年前的我。"

    narrator "訪客從外套裡掏出三封泛黃的信紙，輕輕放在木質櫃檯上。"
    show chletter at center with dissolve


    p "（看著那些信）……你希望我幫你做什麼？"

    v "我不知道。我只是覺得，如果今晚再不這件事做個了結，我大概一輩子走不出這個雨夜了。"

    hide chletter with dissolve

    jump second_act


# -----------------------------------------------------------------------------
# 分支 B：choice_cold
# -----------------------------------------------------------------------------
label choice_cold:
    scene black with fade
    scene desk with fade
    show cha1 at center with dissolve
    show chb1 at center with dissolve
    p "郵局已經準備打烊了。如果寄信，請明天早上再來。"

    narrator "我沒有多說什麼，空氣中只剩下窗外的雨聲和檯燈的微光。"

    v "（苦笑了一下）也是……像我這樣連地址都沒有的人，怎麼會有人想收留呢？"
    v "不過……我只是想把這個留下。這是老房子裡找到的信。"

    narrator "女孩默默將三封泛黃的信紙放在櫃檯邊，轉身就準備拉開門走進雨中。"

    menu:
        "叫住對方，問清楚是怎麼回事。":
            p "等等……把話說清楚再走。"
            v "（回過頭，眼裡閃過一絲光芒）"
            jump second_act

        "看著對方走入雨中，收下信件。":
            jump ending_quiet


# -----------------------------------------------------------------------------
# 【第二幕：三封信的重量】
# -----------------------------------------------------------------------------
label second_act:
    scene black with fade
    scene desk with fade
    show cha1 at center with dissolve
    show chb1 at center with dissolve
    # 透過劇情主軸管理器物件推進至第二幕
    $ game_manager.advance_act(2)
    
    # 透過 Python 串列安全取得信件資料
    python:
        let_1 = visitor.letters[0]
        let_2 = visitor.letters[1]
        let_3 = visitor.letters[2]

    # 根據先前累積的互動分數（attitude）動態改變訪客的反應
    if visitor.attitude > 0:
        v "（她微微點了點頭，神情比剛進門時放鬆了許多，眼神裡帶有一絲感激）"
        v "其實……剛剛喝了你那杯熱茶後，我心裡安穩多了。有些話，我本來一輩子都不打算說出口的……"
    else:
        v "（她冷笑了一聲，目光有些閃躲，雙手緊緊抓著風衣的衣角）"
        v "我知道你覺得我很煩，也沒耐心聽我囉嗦。但沒關係，反正這是我自己的事……"

    v "第一封信，是十年前我準備離家去外地念書的那天晚上寫的。"
    v "當時我爸嫌我選的科系沒有前途，我們在飯桌上大吵了一架。我摔門就走，背包裡塞了這封寫好卻沒寄出的信——信裡寫滿了抱怨，說我再也不想回這個家了。"

    p "但你十年後才把它拿出來。"

    v "因為我爸在上個月過世了。我回去整理他的遺物時，在抽屜深處看到了這第二封信。"
    v "這是他寫給我的。"

    p "（拿起泛黃的信紙，念出上面的字）"
    p "『孩子：今天巷口那家你最愛吃的麵攤收攤了，老闆說要搬去外縣市。我本想買一碗給你，才想起你已經去外地了。桌上留了兩百塊零用錢，自己在外地別省過頭。那天晚上的話……爸也有點急了，別往心裡去。』"

    hide chb1 with dissolve
    show chb2 at center with dissolve
    v "（聲音哽咽，肩膀微微顫抖）"
    v "我離家十年，電話打回去不超過十通。每次他問我過得好不好，我都嫌他囉嗦，急著掛電話。"
    v "我以為我恨他，以為是他把我綁得太緊。直到他走了我才發現……原來他一直在原地等我回頭，而我連一封像樣的道歉信都沒寄給他。"

    # 選擇結局並記錄到遊戲主軸物件中
    menu:
        "「你還有第三封信沒看。那是你自己寫給未來的信嗎？」":
            $ game_manager.set_ending("Dawn")
            jump ending_dawn

        "「過去的事已經回不去了，但至少你現在懂了。」":
            $ game_manager.set_ending("Regret")
            jump ending_regret

        "（保持沉默，靜靜遞上一張乾淨的紙和筆）":
            $ game_manager.set_ending("Echo")
            jump ending_echo


# -----------------------------------------------------------------------------
# 結局 A：晨光微熹（溫暖釋懷，推薦的主線結局）
# -----------------------------------------------------------------------------
label ending_dawn:
    scene black with fade
    scene desk with fade
    show cha1 at center with dissolve
    show chb1 at center with dissolve
    p "你還有第三封信沒看。那是……你自己寫給未來的信嗎？"

    hide chb2 with dissolve
    show chb1 at center with dissolve

    narrator "女孩愣了一下，目光緩緩移向桌上那封壓在最底下的泛黃信封。"
    narrator "她的手指顫抖著將它抽出來，信封口早就已經被拆開了，上面甚至有被揉爛又重新撫平的痕跡。"

    v "這封信……我記得。"
    v "那是離開家後的第三年，某個同樣下著雨的深夜。我當時在外地工作受挫，覺得自己一事無成，心裡對我爸充滿了愧疚與思念。"
    v "我寫了這封信，想跟他道歉，想告訴他我其實過得很辛苦……"

    p "但你沒有寄出去？"

    v "嗯。寫完之後，我覺得自己太軟弱了，覺得『像我這樣的人怎麼有臉低頭』，於是氣得把它揉爛，丟進了房間的垃圾桶。"
    v "我以為它早就被當作垃圾處理掉了……"

    hide chb1 with dissolve
    show chb2 at center with dissolve

    v "（淚水終於潰堤，聲音哽咽得幾乎說不出話）"
    v "笨蛋……他到底是什麼時候撿起來的？他明明那麼愛面子，為什麼要把這種東西留下來……"

    narrator "郵局裡一片寂靜，只有訪客壓抑許久的哭聲，伴隨著窗外漸漸變小的雨滴聲。"
    narrator "這一刻，十年來堆積在心頭的防備、憤怒與自責，終於在泛黃的紙張間找到了出口。"
    narrator "時間一分一秒過去。窗外的黑夜褪去，天際邊緣透出了一抹淡淡的魚肚白。"
    narrator "雨停了。清晨微涼而清新的空氣，順著微微推開的木門縫隙溜進了郵局。"
    narrator "女孩用袖子擦乾了眼淚，深深吸了一口氣。雖然眼睛紅腫，但她的眼神裡那種揮之不去的陰霾，已經悄然消散。"

    v "謝謝你……"
    v "這個雨夜，我好像終於……找到回家的路了。"

    scene desk with fade

    narrator "女孩站起身，將那三封信整齊地留在櫃檯上，轉身走入清晨微亮的街道中。"
    narrator "我站在櫃檯後方，看著她的背影漸漸消失在轉角，然後伸出手，輕輕熄滅了桌上那盞亮了一整夜的綠罩檯燈。"
    scene black with fade
    narrator "有些話永遠不嫌遲，只要心還在聽"
    scene black with fade
    return


# -----------------------------------------------------------------------------
# 結局 B：平靜的雨夜 (淡淡遺憾)
# -----------------------------------------------------------------------------
label ending_regret:
    scene black with fade
    scene desk with fade
    show cha1 at center with dissolve
    show chb1 at center with dissolve
    p "過去的事已經回不去了，但至少你現在懂了。"

    narrator "女孩聽完，苦笑了一下。她拿起桌上的信紙，手指輕輕摩挲著上頭父親熟悉的字跡。"

    v "是啊，回不去了。"
    v "我以前總覺得，『時間還很多』是一件理所當然的事。每次他打電話來，我都嫌他囉嗦，總說『我現在很忙，下次再聊』。"
    v "我一直以為『下次』還有很多次，直到他走了我才發現……『下次』這個詞，原來這麼奢侈。"

    p "人都是在失去之後，才學會怎麼去凝視那些曾經擁有過的日常。"

    v "你說得對。"
    v "雖然心裡還是很遺憾，也有很多來不及說出口的話……但奇怪的是，把這些信讀完之後，我心裡那塊大石好像稍微放下了。"

    narrator "女孩將三封信小心翼翼地摺好，收回風衣的內袋裡，動作輕柔得像是在捧著什麼珍貴的寶物。"

    v "雨好像變小了。"
    p "嗯，快停了。"
    v "我要走了。明天……我得回老家一趟，把他的房間好好打掃乾淨，把那些他來不及丟的老東西都理一理。"
    v "至少，這次換我來等他了。"

    p "一路順風。"

    scene desk with fade
    play sound "hearing_rain1.mp3"

    narrator "女孩點了點頭，推開門走進雨後的街道。空氣裡瀰漫著泥土與青草的香氣。"
    narrator "郵局恢復了原本的安靜。我坐回木椅上，拿起桌上的筆記本，寫下了今天的最後一個郵戳。"
    narrator "雖然帶著遺憾，但生活總得繼續，雨後終會天晴。"
    scene black with fade
    return


# -----------------------------------------------------------------------------
# 結局 C：未竟的迴音 (留白共鳴)
# -----------------------------------------------------------------------------
label ending_echo:
    scene black with fade
    scene desk with fade
    show cha1 at center with dissolve
    show chb1 at center with dissolve
    narrator "我沒有多說什麼，只是默默拉開抽屜，拿出一張乾淨潔白的信紙，以及一支黑色的鋼筆，輕輕推到了訪客面前。"
    narrator "女孩愣了一下，低頭看著那張白紙，又抬頭看了看我。"

    v "這是……給我的？"

    p "如果你有些話，現在不寫下來，以後可能就沒有機會了。"

    narrator "空氣安靜了許久。窗外的雨聲沙沙作響，彷彿在催促著時間的流逝。"
    narrator "女孩沒有說話。她伸出微微顫抖的手，拿起那支筆.筆尖落在紙上，發出沙沙的輕響。"
    narrator "她沒有寫給過世的父親，也沒有寫給任何人。"
    narrator "她在紙上寫下的是給十年後、終於學會放過自己的那個自己的話。"
    narrator "大約過了一刻鐘，訪客停下了筆。她將信紙工整地對折，放進一個空白的信封裡，親手封上口。"
    narrator "她轉過頭，看向櫃檯旁那個造型古老、貼著『未寄出信箱』木牌的小箱子。"

    v "如果把它投在這裡……這樣，就算寄到了吧？"

    p "嗯。只要你心裡送出去了，它就一定會抵達。"

    narrator "女孩微微一笑。那是一個極其輕淺、卻無比真實的笑容。"
    narrator "她站起身，將信封投入箱子裡，發出了一聲輕輕的悶響。"

    v "謝謝你，這夜真的很長，但幸好這裡有燈光。"

    scene desk with fade
    play sound "hearing_rain1.mp3"
    narrator "女孩轉身推門離去。雨夜的街道空無一人，但路燈的倒影在水窪裡閃爍著溫柔的光。"
    narrator "我沒有去追，也沒有說再見。只是靜靜地看著那個信箱，知道有些靈魂在這一刻，終於找到了停泊的港灣。"
    scene black with fade
    return


# -----------------------------------------------------------------------------
# 額外收尾：分支 B 冷淡走法
# -----------------------------------------------------------------------------
label ending_quiet:
    scene black with fade
    scene rain with fade
    play sound "hearing_rain1.mp3"
    narrator "看著女孩孤獨的背影消失在雨幕中，我默默收下了桌上那三封信。"
    narrator "有些故事註定沒有解答，而有些緣分，僅僅只是在雨夜裡擦身而過。"
    scene black with fade
    return