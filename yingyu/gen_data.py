"""Data for English analysis pages (10 exams)."""

PAGES = {}


# ============ 和平区 ============
PAGES["heping"] = {
    "district": "和平区",
    "exam_name": "2026年九年级学情调研问卷",
    "has_listening": True,

    "skeleton_note": "本卷与辽宁省卷结构<strong>完全对齐</strong>（笔试45题90分+听力20题30分=120分）。阅读理解总计50分占笔试55.6%，是绝对主战场。书面表达20分为单题最高分值。语篇填空10分全部嵌入语篇考查语法，无传统单选题。阅读还原（五选四）对标高考新题型。",

    # ---- 阅读篇章 ----
    "passages": [
        {
            "id": "A", "genre": "应用文", "topic": "Summer Holiday Day Camp 2025夏令营广告",
            "theme": "日常生活·活动", "difficulty": "★☆☆", "cls": "info",
            "tags": [("应用文","green"),("广告","blue")],
            "questions": [
                {"no":"Q21","type":"写作目的","ability":"判断目标读者","location":"全文→for parents(需带孩子参加)"},
                {"no":"Q22","type":"细节理解","ability":"时间信息定位","location":"Program information: May 1—May 7"},
                {"no":"Q23","type":"细节理解","ability":"信息筛选","location":"活动列表: sports/movies/books ✓, maths/exams ✗"},
                {"no":"Q24","type":"文体判断","ability":"文本类型识别","location":"全文→广告(ad)"},
            ],
        },
        {
            "id": "B", "genre": "记叙文", "topic": "攀岩运动中的成长与人生启示",
            "theme": "个人成长·品质", "difficulty": "★★☆", "cls": "",
            "tags": [("记叙文","orange"),("运动","green"),("成长","purple")],
            "questions": [
                {"no":"Q25","type":"细节理解","ability":"因果关系","location":"第1段: lived in the flat city→few chances to climb"},
                {"no":"Q26","type":"细节理解","ability":"方法归纳","location":"第2段: picture the problem→plan moves step by step"},
                {"no":"Q27","type":"推理判断","ability":"信息推断","location":"第2段: communicated better with others→C社交技能"},
                {"no":"Q28","type":"主旨大意","ability":"写作目的","location":"全文: 通过攀岩分享人生经验→D分享攀岩中的人生启示"},
            ],
        },
        {
            "id": "C", "genre": "说明文", "topic": "爱好是否应该变成职业——Tracy和Jack的故事",
            "theme": "生活哲理·职业", "difficulty": "★★☆", "cls": "success",
            "tags": [("说明文","blue"),("职业","green"),("哲理","purple")],
            "questions": [
                {"no":"Q29","type":"细节理解","ability":"因果关系","location":"第2段: loved cycling→learned to fix bikes→got a job"},
                {"no":"Q30","type":"推理判断","ability":"情感变化","location":"第2段: 从翻译厌倦→骑车热爱→开店高兴→发现真爱不是修车"},
                {"no":"Q31","type":"推理判断","ability":"信息推断","location":"第3段: showed in shows/exchanged→cared more about sharing"},
                {"no":"Q32","type":"写作手法","ability":"论证方式","location":"全文通过Tracy和Jack两个例子论证→C举例论证"},
            ],
        },
        {
            "id": "D", "genre": "说明文", "topic": "中国商业太空旅行——明星科学家购票上太空",
            "theme": "科技创新·太空", "difficulty": "★★★", "cls": "warning",
            "tags": [("说明文","blue"),("科技","orange"),("太空","green")],
            "questions": [
                {"no":"Q33","type":"细节理解","ability":"数字计算","location":"第2段: $50 million×10%=$5 million→C"},
                {"no":"Q34","type":"细节理解","ability":"事件顺序","location":"第3段: separate→cross Kármán Line→return(先过卡门线)"},
                {"no":"Q35","type":"词义猜测","ability":"上下文推断","location":"第5段: backing=Supporting(给予更多机会)"},
                {"no":"Q36","type":"标题选择","ability":"主旨概括","location":"全文: 中国太空旅行梦想→D Space Travel: A Dream Coming True in China"},
            ],
        },
    ],

    # ---- 阅读还原 ----
    "restore": {
        "topic": "沙漠变电站——中国光伏治沙工程",
        "structure": "总分结构（问题提出→原因分析→解决方案→成果展望）",
        "slots": [
            ("37","段尾","词汇复现: power stations+amazing→B引出how achieved","B"),
            ("38","段中","逻辑连词: 前文little rain→A种田困难(farming hard)","A"),
            ("39","段尾","递进: Besides+solar-powered→E能源输送远方","E"),
            ("40","段首","总结: brings three good things→D专家总结三重效益","D"),
        ],
    },

    # ---- 完形填空 ----
    "cloze": {
        "genre": "记叙文",
        "topic": "爷爷的礼物——从摩托车事故到直面恐惧",
        "emotion_line": "回忆美好→事故阴影→爷爷卧病→意外惊喜→直面恐惧→感悟爱与勇气",
        "theme": "面对恐惧是困难的但有意义的，最好的礼物是爱与勇气的传递",
        "questions": [
            {"no":"Q41","type":"语境推理","pos":"形容词","answer":"B. ill","clue":"卧床+想去cheeer him up→生病"},
            {"no":"Q42","type":"语境推理","pos":"名词","answer":"C. picture","clue":"下文It showed him and friends on motorcycles→照片"},
            {"no":"Q43","type":"情感态度","pos":"形容词","answer":"A. sweet","clue":"那些是美好的回忆(正面情感)"},
            {"no":"Q44","type":"语境推理","pos":"副词","answer":"B. Suddenly","clue":"猫突然跑过→意外事件"},
            {"no":"Q45","type":"词义辨析","pos":"动词短语","answer":"D. fell over","clue":"摩托车翻倒(避让猫急转弯)"},
            {"no":"Q46","type":"语境推理","pos":"动词","answer":"C. allow","clue":"不允许我考摩托车驾照(因事故留下阴影)"},
            {"no":"Q47","type":"语境推理","pos":"名词","answer":"D. key","clue":"打开箱子→发现钥匙→下文看到新摩托车"},
            {"no":"Q48","type":"固定搭配","pos":"动词","answer":"B. stop","clue":"won't let my fear stop you(不让恐惧阻止你)"},
            {"no":"Q49","type":"语境推理","pos":"形容词","answer":"C. meaningful","clue":"hard but meaningful(困难但有意义)"},
            {"no":"Q50","type":"情感态度","pos":"动词","answer":"A. touch","clue":"touch our hearts(触动心灵的礼物最伟大)"},
        ],
        "word_types": [
            ("形容词", "4", "40%"),
            ("名词", "2", "20%"),
            ("动词/动词短语", "3", "30%"),
            ("副词", "1", "10%"),
        ],
    },

    # ---- 语篇填空 ----
    "grammar_topic": "围炉煮茶——从唐朝到当代年轻人的新时尚",
    "grammar_theme": "文化传承·传统",
    "grammar": [
        {"no":"Q51","type":"有提示·词形变化","point":"名词→专有名词(国名)","answer":"China","clue":"Chinese→China，介词in后需名词"},
        {"no":"Q52","type":"有提示·词形变化","point":"最高级","answer":"oldest","clue":"one of the+最高级+复数名词"},
        {"no":"Q53","type":"有提示·词形变化","point":"一般过去时","answer":"added","clue":"At that time(过去时间标志)"},
        {"no":"Q54","type":"有提示·词形变化","point":"被动语态","answer":"is called","clue":"It(围炉煮茶)被称为→一般现在时被动"},
        {"no":"Q55","type":"有提示·词形变化","point":"词性转换(名→形)","answer":"careful","clue":"修饰名词attention需形容词"},
        {"no":"Q56","type":"无提示·虚词","point":"冠词","answer":"A","clue":"The number of固定搭配(大量的)"},
        {"no":"Q57","type":"有提示·词形变化","point":"代词变格(主→宾)","answer":"them","clue":"makes them feel→宾格"},
        {"no":"Q58","type":"有提示·词形变化","point":"非谓语(to do)","answer":"to get","clue":"want to do固定搭配"},
        {"no":"Q59","type":"无提示·虚词","point":"连词","answer":"and","clue":"both...and...固定搭配"},
        {"no":"Q60","type":"无提示·虚词","point":"介词","answer":"in","clue":"live in a modern society"},
    ],
    "grammar_stats": [
        ("动词时态(过去时)", "1", "高"),
        ("被动语态", "1", "高"),
        ("最高级", "1", "高"),
        ("词性转换", "1", "高"),
        ("非谓语(to do)", "1", "高"),
        ("代词变格", "1", "中"),
        ("冠词", "1", "中"),
        ("连词", "1", "中"),
        ("介词", "1", "中"),
        ("名词(国名)", "1", "中"),
    ],

    # ---- 阅读与表达 ----
    "reading_expr_topic": "周坚的长发——为癌症儿童捐发的感人故事",
    "reading_expr_genre": "记叙文",
    "reading_expr_tone": "温暖·励志",
    "reading_expression": [
        {"no":"Q61","score":"2分","type":"细节提取","question":"What does Zhou Jian do when people laugh at him?","answer":"He just smiles and walks away."},
        {"no":"Q62","score":"2分","type":"细节提取","question":"How long has Zhou Jian kept his hair?","answer":"For over two years."},
        {"no":"Q63","score":"2分","type":"推理归纳","question":"Where does Zhou Jian probably send his hair?","answer":"To the City Children's Hospital."},
        {"no":"Q64","score":"4分","type":"开放性表达","question":"Tell us your opinion about what Zhou Jian has done. (≥30词)","answer":"言之有理即可。示例：I think Zhou Jian is a very kind and brave person. He kept his long hair for over two years even though people laughed at him. He did it to help children with cancer. His action shows that true kindness means giving without expecting anything in return."},
    ],

    # ---- 书面表达 ----
    "writing": {
        "type": "书信",
        "topic": "给即将回美国的Mike写告别信",
        "genre": "书信/邮件",
        "word_count": "80-100",
        "requirements": [
            "回忆美好时光（你们一起做过什么）",
            "表达感受（对Mike离开的感受）",
            "你的希望（对未来的期望/祝福）",
        ],
        "difficulty": "★★☆",
    },

    # ---- 阅读微技能统计 ----
    "reading_skills": [
        ("细节理解(Detail)", "Q21,Q22,Q23,Q25,Q26,Q29,Q33,Q34", "8", "16分"),
        ("推理判断(Inference)", "Q27,Q30,Q31", "3", "6分"),
        ("主旨大意/写作目的", "Q28", "1", "2分"),
        ("词义猜测(Word Meaning)", "Q35", "1", "2分"),
        ("标题选择(Best Title)", "Q36", "1", "2分"),
        ("文体判断(Text Type)", "Q24", "1", "2分"),
        ("写作手法(Method)", "Q32", "1", "2分"),
        ("逻辑衔接(Cohesion)", "Q37-Q40", "4", "8分(还原)"),
    ],

    # ---- 话题分布 ----
    "topics": [
        ("A篇·阅读选择", "夏令营活动广告", "日常生活·活动"),
        ("B篇·阅读选择", "攀岩运动的人生启示", "个人成长·运动"),
        ("C篇·阅读选择", "爱好与职业的抉择", "生活哲理·职业"),
        ("D篇·阅读选择", "中国商业太空旅行", "科技创新·太空"),
        ("阅读还原", "沙漠光伏治沙工程", "环保·新能源"),
        ("完形填空", "爷爷的摩托车与直面恐惧", "家庭亲情·勇气"),
        ("语篇填空", "围炉煮茶的文化复兴", "传统文化·茶文化"),
        ("阅读与表达", "为癌症儿童捐发", "社会责任·善良"),
        ("书面表达", "给外国朋友的告别信", "跨文化交际·友谊"),
    ],

    # ---- 命题DNA ----
    "dna": [
        {"title":"观察一 · 阅读选材紧扣社会热点+中国元素——D篇太空旅行+还原篇光伏治沙",
         "body":"D篇以中国商业太空旅行为题材(CYZ1飞船/卡门线/五年计划)，阅读还原篇以沙漠光伏为情境。两篇均涉及中国科技前沿和国家战略，体现<strong>\"中国故事+科技创新\"</strong>选材趋势。<strong>备考启示→</strong>关注中国科技进展(太空/新能源/AI)的英文报道，积累相关词汇。"},
        {"title":"观察二 · 细节理解题占50%——但设题方式已升级",
         "body":"16道阅读选择题中8道为细节理解，但不再是简单的原文照搬。Q33需计算($50M×10%=$5M)，Q34需排列事件顺序，Q23需排除干扰项。<strong>\"看似简单，实则需要精确定位+逻辑判断\"</strong>。<strong>备考启示→</strong>训练带着问题读文、关键词定位+同义替换识别能力。"},
        {"title":"观察三 · 语篇填空全面覆盖核心语法——围炉煮茶为载体",
         "body":"10空涵盖：过去时(added)、被动语态(is called)、最高级(oldest)、词性转换(careful)、非谓语(to get)、代词(them)、冠词(A)、连词(and)、介词(in)、专有名词(China)。<strong>以文化话题为语篇载体，语法考查全面且高频</strong>。<strong>备考启示→</strong>系统复习8大语法点，每个点准备3-5个典型例句。"},
        {"title":"观察四 · 完形填空记叙文为主+情感线索解题是关键",
         "body":"完形以\"爷爷的礼物\"为故事，情感线从回忆美好→事故阴影→卧病→惊喜→领悟。形容词占40%(ill/sweet/meaningful/careful)，需通过<strong>情感线索推断词义</strong>。<strong>备考启示→</strong>完形先通读把握情感基调，再逐空根据上下文语境选择。"},
        {"title":"观察五 · 阅读与表达Q64开放性试题4分——高考衔接特征明显",
         "body":"Q64要求对周坚捐发行为表达个人观点(≥30词)，考查<strong>英语思维表达能力</strong>。这与高考读后续写/概要写作的理念一脉相承。<strong>备考启示→</strong>准备\"人物评价+行为评价+个人感想\"三段式模板。"},
    ],

    # ---- 作战地图 ----
    "strategy": [
        {"cls":"","title":"🎯 P0 · 阅读选择拿下24-28分（满分32分）","body":"<ul><li><strong>限时训练</strong>：4篇阅读控制在35分钟内完成</li><li><strong>A篇(应用文)</strong>：3分钟速读，关键词定位表格/列表中的信息</li><li><strong>B篇(记叙文)</strong>：把握故事主线+情感变化，推理题回到原文找证据</li><li><strong>C/D篇(说明文)</strong>：首段+末段抓主旨，每段首句找分论点</li><li><strong>干扰项识别</strong>：原文出现≠正确答案，必须回到题目问的是什么</li></ul>"},
        {"cls":"warning","title":"⚡ P1 · 书面表达冲刺15-18分（满分20分）","body":"<ul><li><strong>审题三步</strong>：①确定体裁(书信) ②圈出写作要点(通常3个) ③确定时态(回忆用过去时/感受用现在时)</li><li><strong>本卷话题</strong>：给Mike写告别信→回忆/感受/希望，难度适中</li><li><strong>高分策略</strong>：每个要点展开2-3句，使用1-2个从句/高级表达</li><li><strong>必备句型</strong>：I still remember the day when... / Not only...but also... / I hope that...</li></ul>"},
        {"cls":"success","title":"📌 P2 · 语篇填空稳拿7-9分（满分10分）","body":"<ul><li><strong>有提示(7题)</strong>：看括号词→判断变什么→检查主谓一致</li><li><strong>无提示(3题)</strong>：判断缺什么词性→冠词/介词/连词/代词四选一</li><li><strong>必背规律</strong>：one of the+最高级+复数 / want/enjoy/finish+to do/doing / both...and...</li><li><strong>检查清单</strong>：时态标志词→第三人称单数→被动语态be→比较级最高级</li></ul>"},
        {"cls":"info","title":"🧩 P3 · 完形填空+阅读还原拿下13-16分（满分18分）","body":"<ul><li><strong>完形三步法</strong>：①通读全文(不看选项) ②逐空填写(根据情感线索) ③代入检查</li><li><strong>还原解题</strong>：先分析空格位置(段首/中/尾)→找衔接线索(代词/连词/词汇复现)→先做有明确线索的空</li><li><strong>本卷完形</strong>：记叙文+情感变化，形容词题占40%→需要把握情感基调</li><li><strong>本卷还原</strong>：说明文+总分结构，注意Besides/However等逻辑连词</li></ul>"},
    ],

    # ---- 目标分数 ----
    "target_rows": """<tr><td>听力(Q1-Q20)</td><td>30分</td><td>22分</td><td>27分</td></tr>
<tr><td>阅读选择(Q21-Q36)</td><td>32分</td><td>22分</td><td>28分</td></tr>
<tr><td>阅读还原(Q37-Q40)</td><td>8分</td><td>4分</td><td>8分</td></tr>
<tr><td>完形填空(Q41-Q50)</td><td>10分</td><td>7分</td><td>9分</td></tr>
<tr><td>语篇填空(Q51-Q60)</td><td>10分</td><td>7分</td><td>9分</td></tr>
<tr><td>阅读与表达(Q61-Q64)</td><td>10分</td><td>7分</td><td>9分</td></tr>
<tr><td>书面表达(Q65)</td><td>20分</td><td>14分</td><td>18分</td></tr>""",
    "target_low": "83分(69%)",
    "target_high": "108分(90%)",
}


# ============ 浑南区 ============
PAGES["hunnan"] = {
    "district": "浑南区",
    "exam_name": "2026年4月调研测试",
    "has_listening": False,

    "skeleton_note": "本卷笔试结构与辽宁省卷标准<strong>完全对齐</strong>（45题90分），听力口语单独考试不含在本卷中。笔试时长标注100分钟，比省卷标准90分钟略长10分钟。阅读理解总计50分占笔试55.6%，是绝对主战场。试卷共8页，卷面题号从Q1起编（不含听力偏移）。",

    # ---- 阅读篇章 ----
    "passages": [
        {
            "id": "A", "genre": "说明文", "topic": "中国首批国家公园介绍",
            "theme": "自然保护·地理", "difficulty": "★☆☆", "cls": "info",
            "tags": [("说明文","green"),("图文并茂","blue"),("国家公园","purple")],
            "questions": [
                {"no":"Q21","type":"细节理解","ability":"关键信息提取","location":"A—三江源以三条大河（长江/黄河/澜沧江）发源地闻名"},
                {"no":"Q22","type":"细节理解+计算","ability":"数据推算","location":"B(16%)—约210.7/1280km²≈16%覆盖原始森林"},
                {"no":"Q23","type":"细节理解","ability":"信息匹配","location":"D—东北虎豹国家公园在吉林和黑龙江"},
                {"no":"Q24","type":"文体判断","ability":"文本类型识别","location":"C—旅游指南(travel guidebook)"},
            ],
        },
        {
            "id": "B", "genre": "说明文", "topic": "中国粮食生产成就与世界影响",
            "theme": "社会发展·农业", "difficulty": "★★☆", "cls": "",
            "tags": [("说明文","blue"),("时事热点","green"),("粮食安全","orange")],
            "questions": [
                {"no":"Q25","type":"细节理解","ability":"段落归纳","location":"B—中国能自给自足养活国民（人均500kg+）"},
                {"no":"Q26","type":"细节理解","ability":"方式方法","location":"D—通过分享杂交水稻技术帮助他国"},
                {"no":"Q27","type":"推理判断","ability":"作者态度","location":"C(Positive)—全文正面评价，\"responsible world leader\""},
                {"no":"Q28","type":"主旨大意","ability":"文章主旨","location":"D—中国粮食成就及其全球影响"},
            ],
        },
        {
            "id": "C", "genre": "议论文", "topic": "什么是尊重？如何展示和获得尊重",
            "theme": "品德修养·人际关系", "difficulty": "★★☆", "cls": "success",
            "tags": [("议论文","orange"),("尊重","purple"),("Golden Rule","green")],
            "questions": [
                {"no":"Q29","type":"写作手法","ability":"引用目的","location":"A—提及Aretha Franklin歌曲是为了引入\"respect\"话题"},
                {"no":"Q30","type":"词义猜测","ability":"上下文推断","location":"D(Follow)—observe the Golden Rule=遵守黄金法则"},
                {"no":"Q31","type":"细节理解","ability":"应对策略","location":"B—面对不礼貌行为应保持礼貌、以身作则"},
                {"no":"Q32","type":"写作目的","ability":"全文目的","location":"A—提醒读者重视尊重(value respect)"},
            ],
        },
        {
            "id": "D", "genre": "新闻报道", "topic": "上海老年人专用商店——科技助老",
            "theme": "社会关怀·老龄化", "difficulty": "★★☆", "cls": "warning",
            "tags": [("新闻报道","blue"),("老龄化","orange"),("科技助老","green")],
            "questions": [
                {"no":"Q33","type":"细节理解","ability":"数字提取","location":"B(1,200m²)—首段明确\"1,200-square-meter shop\""},
                {"no":"Q34","type":"推理判断","ability":"特点归纳","location":"C—专为老年人服务且提供实际帮助"},
                {"no":"Q35","type":"细节理解","ability":"功能描述","location":"C—外骨骼机器人帮助老人更轻松行走"},
                {"no":"Q36","type":"推理判断","ability":"核心目的","location":"A—帮助老人过上更好的生活"},
            ],
        },
    ],

    # ---- 阅读还原 ----
    "restore": {
        "topic": "教育部保护学生体育锻炼时间的新政策",
        "structure": "政策背景→措施细则→原因分析→未来展望",
        "slots": [
            ("37","段中","后文\"They also keep students in...\"→前句应说明学校占用体育课","D"),
            ("38","段中","后文\"One is real...the other is fake\"→前句引出\"两套课表\"","E"),
            ("39","段中","前文\"paid much attention to exam scores\"→因果关系：所以缺运动","B"),
            ("40","段中","后文\"They will make sure the plan is used\"→前句引出更多政策","A"),
        ],
    },

    # ---- 完形填空 ----
    "cloze": {
        "genre": "记叙文",
        "topic": "13岁澳大利亚男孩Austin勇救家人",
        "emotion_line": "海滩度假(enjoying)→大风突袭(suddenly)→漂离海岸→勇敢游泳→筋疲力尽(tired)→呼救成功→全家获救",
        "theme": "勇气与果断行动在危急时刻可以拯救生命",
        "questions": [
            {"no":"Q41","type":"语境推理","pos":"动词","answer":"D. enjoying","clue":"a beach holiday→享受假期(正面语境)"},
            {"no":"Q42","type":"语境推理","pos":"副词","answer":"B. suddenly","clue":"strong winds突然将他们推远(意外转折)"},
            {"no":"Q43","type":"词义辨析","pos":"动词","answer":"C. reach","clue":"tried to reach the beach→试图到达海滩求救"},
            {"no":"Q44","type":"固定搭配","pos":"名词","answer":"A. choice","clue":"had no choice but to swim→别无选择只能游泳"},
            {"no":"Q45","type":"词义辨析","pos":"动词短语","answer":"C. called for","clue":"reached the beach and called for help→呼救"},
            {"no":"Q46","type":"语境推理","pos":"形容词","answer":"B. tired","clue":"so tired that he fell down→累到倒地"},
            {"no":"Q47","type":"语境推理","pos":"名词","answer":"A. chance","clue":"gave his family the chance to be saved→获救机会"},
            {"no":"Q48","type":"语境推理","pos":"动词","answer":"D. praised","clue":"actions should be highly praised→高度赞扬"},
            {"no":"Q49","type":"语境推理","pos":"动词","answer":"B. told","clue":"told reporters→告诉记者"},
            {"no":"Q50","type":"语境推理","pos":"名词","answer":"C. experience","clue":"a terrible and dangerous experience→可怕经历"},
        ],
        "word_types": [
            ("动词/动词短语", "5", "50%"),
            ("名词", "3", "30%"),
            ("形容词", "1", "10%"),
            ("副词", "1", "10%"),
        ],
    },

    # ---- 语篇填空 ----
    "grammar_topic": "元宵节——汤圆与元宵的文化对话",
    "grammar_theme": "传统文化·节日",
    "grammar": [
        {"no":"Q51","type":"有提示·词形变化","point":"最高级","answer":"most important","clue":"The (most important) part→多音节形容词最高级"},
        {"no":"Q52","type":"无提示·虚词","point":"冠词","answer":"the","clue":"look almost the same→固定搭配the same"},
        {"no":"Q53","type":"无提示·虚词","point":"连词","answer":"or","clue":"sweet sesame or salty meat→选择关系"},
        {"no":"Q54","type":"有提示·词形变化","point":"被动语态","answer":"are made","clue":"how they are made→主语they+被动"},
        {"no":"Q55","type":"无提示·虚词","point":"介词","answer":"by","clue":"make tangyuan by putting→方式介词"},
        {"no":"Q56","type":"有提示·词形变化","point":"不定式","answer":"to eat","clue":"difficult to eat→\"adj.+to do\"结构"},
        {"no":"Q57","type":"有提示·词形变化","point":"主谓一致","answer":"agrees","clue":"everyone agrees→不定代词+第三人称单数"},
        {"no":"Q58","type":"有提示·词形变化","point":"词性转换(形→副)","answer":"simply","clue":"were simply called→副词修饰动词"},
        {"no":"Q59","type":"有提示·词形变化","point":"名词复数","answer":"lines","clue":"wait in long lines→可数名词复数"},
        {"no":"Q60","type":"有提示·词形变化","point":"反身代词","answer":"themselves","clue":"These foods themselves→强调\"本身\""},
    ],
    "grammar_stats": [
        ("最高级", "1", "高"),
        ("被动语态", "1", "高"),
        ("不定式(to do)", "1", "高"),
        ("主谓一致", "1", "高"),
        ("词性转换(形→副)", "1", "高"),
        ("名词复数", "1", "中"),
        ("反身代词", "1", "中"),
        ("冠词", "1", "中"),
        ("连词", "1", "中"),
        ("介词", "1", "中"),
    ],

    # ---- 阅读与表达 ----
    "reading_expr_topic": "广州近零能耗摩天大楼——绿色建筑的未来",
    "reading_expr_genre": "说明文",
    "reading_expr_tone": "客观·科技自豪",
    "reading_expression": [
        {"no":"Q61","score":"2分","type":"细节提取","question":"What is special about this skyscraper in Guangzhou?","answer":"It is China's first \"near-zero-energy\" building."},
        {"no":"Q62","score":"2分","type":"细节提取","question":"How much of the building's electricity comes from its solar panels?","answer":"25 percent (of its electricity)."},
        {"no":"Q63","score":"2分","type":"细节提取","question":"How long did it take to build one floor with the \"cloud factory\" and robots?","answer":"Four days."},
        {"no":"Q64","score":"4分","type":"开放性表达","question":"What can we do to live a green life in our daily life? (≥30词)","answer":"言之有理即可。示例：We can live a green life by saving water and electricity, using reusable bags instead of plastic ones, planting more trees, and choosing public transport or cycling instead of driving."},
    ],

    # ---- 书面表达 ----
    "writing": {
        "type": "邮件回复",
        "topic": "分享自己的\"small victory\"",
        "genre": "应用文（邮件回复）",
        "word_count": "80-100",
        "requirements": [
            "祝贺David赢得英语演讲比赛",
            "分享你自己类似的\"small victory\"经历",
            "适当增加细节，文从字顺连贯",
        ],
        "difficulty": "★★☆",
    },

    # ---- 阅读微技能统计 ----
    "reading_skills": [
        ("细节理解(Detail)", "Q21,Q22,Q23,Q25,Q26,Q31,Q33,Q35", "8", "16分"),
        ("推理判断(Inference)", "Q27,Q34,Q36", "3", "6分"),
        ("主旨大意(Main Idea)", "Q28", "1", "2分"),
        ("词义猜测(Word Meaning)", "Q30", "1", "2分"),
        ("文体判断(Text Type)", "Q24", "1", "2分"),
        ("写作手法(Method)", "Q29", "1", "2分"),
        ("写作目的(Purpose)", "Q32", "1", "2分"),
        ("逻辑衔接(Cohesion)", "Q37-Q40", "4", "8分(还原)"),
    ],

    # ---- 话题分布 ----
    "topics": [
        ("A篇·阅读选择", "中国首批国家公园", "自然保护·地理"),
        ("B篇·阅读选择", "中国粮食安全与全球影响", "社会发展·农业"),
        ("C篇·阅读选择", "尊重的含义与实践", "品德修养·人际关系"),
        ("D篇·阅读选择", "上海老年人专用商店", "社会关怀·老龄化"),
        ("阅读还原", "教育部保护学生体育锻炼时间", "教育政策·体育健康"),
        ("完形填空", "13岁男孩勇敢游泳救家人", "勇敢·家庭·救援"),
        ("语篇填空", "元宵节汤圆与元宵的文化对话", "传统文化·节日"),
        ("阅读与表达", "广州近零能耗摩天大楼", "科技创新·绿色建筑"),
        ("书面表达", "分享自己的\"small victory\"", "个人成长·跨文化交际"),
    ],

    # ---- 命题DNA ----
    "dna": [
        {"title":"观察一 · 选材高度聚焦\"中国故事\"——6/9篇涉及中国题材",
         "body":"国家公园(A篇)、粮食安全(B篇)、教育部体育政策(还原)、上海老年商店(D篇)、广州近零能耗大楼(阅读与表达)、元宵节(语篇填空)。体现<strong>\"用英语讲中国故事\"</strong>的命题导向。<strong>备考启示→</strong>重点积累中国科技/政策/文化/社会话题的英文表达，如national park、grain production、solar panel、exoskeleton等。"},
        {"title":"观察二 · 细节理解占半壁江山但设题方式多样化",
         "body":"16道阅读选择中细节理解8题(50%)，但设题方式不再是简单原文定位：Q22需通过面积数据计算百分比(210.7/1280≈16%)，Q26需归纳\"sharing technology\"方式，Q31需理解\"反面应对→正面建议\"的逻辑。<strong>表面考细节，实则考信息加工能力</strong>。<strong>备考启示→</strong>训练\"带着问题精读+同义替换识别+数据推算\"三合一能力。"},
        {"title":"观察三 · 语篇填空\"有提示7+无提示3\"黄金比例——语法覆盖全面",
         "body":"有提示7题覆盖：最高级(most important)、被动语态(are made)、不定式(to eat)、主谓一致(agrees)、词性转换(simply)、名词复数(lines)、反身代词(themselves)。无提示3题：冠词(the)、连词(or)、介词(by)。<strong>语法点分布均匀，无偏难怪题</strong>。<strong>备考启示→</strong>重点攻克\"被动语态+主谓一致+不定式\"三大高频考点。"},
        {"title":"观察四 · 完形填空动词占50%——与和平区形容词主导形成差异",
         "body":"本卷完形10题中动词/动词短语5题(enjoying/reach/called for/praised/told)，名词3题，形容词和副词各1题。动词题需根据<strong>动作逻辑链</strong>（度假→遇险→游泳→求救→获救→讲述）选择。<strong>备考启示→</strong>完形记叙文要抓住\"事件发展顺序\"，动词短语(call for/prepare for/wait for/pay for)是必考点。"},
    ],

    # ---- 作战地图 ----
    "strategy": [
        {"cls":"","title":"🎯 P0 · 阅读选择拿下24-28分（满分32分）","body":"<ul><li><strong>A篇(说明文·图文)</strong>：3分钟速读，重点关注数字(面积/比例)和地理信息，注意计算题</li><li><strong>B篇(说明文·时事)</strong>：抓住每段首句(achievement→help→technology)，态度题全文定基调</li><li><strong>C篇(议论文)</strong>：先读题干关键词，回原文段落精确定位；词义猜测题看前后文逻辑</li><li><strong>D篇(新闻报道)</strong>：who/what/where/why四要素快速抓取，推理题需归纳而非原文照搬</li><li><strong>时间分配</strong>：A篇5分钟 + B篇7分钟 + C篇8分钟 + D篇8分钟 = 28分钟内完成</li></ul>"},
        {"cls":"warning","title":"⚡ P1 · 书面表达冲刺15-18分（满分20分）","body":"<ul><li><strong>审题三步</strong>：①体裁=邮件回复 ②要点=祝贺+分享经历 ③时态=回忆用过去时/感受用现在时</li><li><strong>本卷难度适中</strong>：\"small victory\"话题贴近学生生活，演讲比赛/考试进步/学会技能均可写</li><li><strong>高分模板</strong>：第1段祝贺(2-3句) → 第2段自己的经历(4-5句，有细节) → 第3段鼓励+期望(2句)</li><li><strong>必备句型</strong>：Congratulations on... / I still remember when... / I was so...that... / Keep up the great work!</li></ul>"},
        {"cls":"success","title":"📌 P2 · 语篇填空稳拿7-9分（满分10分）","body":"<ul><li><strong>有提示(7题)</strong>：看括号词→判断变什么(时态/语态/词性/级别)→检查主谓一致</li><li><strong>无提示(3题)</strong>：判断缺什么成分→冠词(the/a)/介词(by/in/of)/连词(or/and/but)三选一</li><li><strong>必背规律</strong>：the same(固定搭配) / difficult to do(adj.+to do) / everyone+单三 / by doing(方式)</li><li><strong>检查清单</strong>：①是否需要最高级 ②是否被动语态 ③第三人称单数-s ④名词是否需要复数</li></ul>"},
        {"cls":"info","title":"🧩 P3 · 完形填空+阅读还原拿下13-16分（满分18分）","body":"<ul><li><strong>完形(记叙文)</strong>：①通读把握\"海滩遇险→勇敢自救→全家获救\"主线 ②动词题按时间顺序选 ③名词题看搭配(have no choice but to / called for help)</li><li><strong>还原(政策说明)</strong>：先做线索最明确的空(Q38\"两套课表\"→E最确定)，再用排除法做其他空</li><li><strong>还原核心技巧</strong>：代词指代(They→前文谁) / 因果连词(So→前因后果) / 时间推进(later→展望)</li><li><strong>本卷还原难度</strong>：★★☆ 逻辑线索清晰，多余项C(安全担忧)与政策方向不匹配易排除</li></ul>"},
    ],

    # ---- 目标分数 ----
    "target_rows": """<tr><td>听力(单独考)</td><td>30分</td><td>22分</td><td>27分</td></tr>
<tr><td>阅读选择(Q21-Q36)</td><td>32分</td><td>22分</td><td>28分</td></tr>
<tr><td>阅读还原(Q37-Q40)</td><td>8分</td><td>4分</td><td>8分</td></tr>
<tr><td>完形填空(Q41-Q50)</td><td>10分</td><td>7分</td><td>9分</td></tr>
<tr><td>语篇填空(Q51-Q60)</td><td>10分</td><td>7分</td><td>9分</td></tr>
<tr><td>阅读与表达(Q61-Q64)</td><td>10分</td><td>7分</td><td>9分</td></tr>
<tr><td>书面表达(Q65)</td><td>20分</td><td>14分</td><td>18分</td></tr>""",
    "target_low": "83分(69%)",
    "target_high": "108分(90%)",
}

# remaining entries loaded from gen_data_extra.py
from gen_data_extra import shenhe, yuhong, huanggu, tiexi, sujiatun, fushun, yingkou, tieling
PAGES["shenhe"] = shenhe()
PAGES["yuhong"] = yuhong()
PAGES["huanggu"] = huanggu()
PAGES["tiexi"] = tiexi()
PAGES["sujiatun"] = sujiatun()
PAGES["fushun"] = fushun()
PAGES["yingkou"] = yingkou()
PAGES["tieling"] = tieling()

from gen_data_cities import dalian, anshan
PAGES["dalian"] = dalian()
PAGES["anshan"] = anshan()

