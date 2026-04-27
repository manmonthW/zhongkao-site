#!/usr/bin/env python3
"""Generate English analysis HTML pages."""

CSS = """<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;600;700;900&display=swap');
:root{--bg:#f5f1e8;--text:#1a1815;--accent:#8b2e2e;--border:#d4cfc4;--card-bg:#faf8f3;--tag-bg:#e8e2d6;--success:#2e6b3e;--warning:#b8860b;--info:#2e4a8b;}
*{margin:0;padding:0;box-sizing:border-box;}body{font-family:'Noto Serif SC',serif;background:var(--bg);color:var(--text);line-height:1.8;font-size:16px;}
.container{max-width:960px;margin:0 auto;padding:20px;}
.cover{text-align:center;padding:60px 40px;border-bottom:3px double var(--accent);margin-bottom:50px;}
.cover h1{font-size:2.2em;font-weight:900;color:var(--accent);letter-spacing:.08em;margin-bottom:12px;}
.cover .subtitle{font-size:1.1em;color:#666;margin-bottom:6px;}.cover .meta{font-size:.9em;color:#999;margin-top:20px;}
.toc{background:var(--card-bg);border:1px solid var(--border);padding:24px 36px;margin-bottom:40px;}
.toc h2{font-size:1.2em;color:var(--accent);border-bottom:1px solid var(--border);padding-bottom:8px;margin-bottom:12px;}
.toc ol{padding-left:20px;}.toc li{margin-bottom:4px;}.toc a{color:var(--text);text-decoration:none;border-bottom:1px dotted var(--border);}
h2.section-title{font-size:1.5em;color:var(--accent);border-left:5px solid var(--accent);padding-left:14px;margin:45px 0 20px;}
h3{font-size:1.15em;color:var(--text);margin:26px 0 12px;padding-bottom:5px;border-bottom:1px solid var(--border);}
h4{font-size:1em;color:var(--accent);margin:16px 0 8px;}
table{width:100%;border-collapse:collapse;margin:14px 0 20px;font-size:.9em;}
th{background:var(--accent);color:#fff;padding:8px 10px;text-align:left;font-weight:600;}
td{padding:7px 10px;border-bottom:1px solid var(--border);vertical-align:top;}tr:nth-child(even){background:var(--card-bg);}
.bar-chart{margin:14px 0 20px;}.bar-row{display:flex;align-items:center;margin-bottom:6px;}
.bar-label{width:140px;font-size:.88em;text-align:right;padding-right:10px;flex-shrink:0;}
.bar-track{flex:1;background:var(--tag-bg);height:22px;border-radius:3px;overflow:hidden;}
.bar-fill{height:100%;border-radius:3px;display:flex;align-items:center;padding-left:8px;font-size:.78em;color:#fff;font-weight:600;min-width:28px;}
.bar-fill.c1{background:var(--accent);}.bar-fill.c2{background:var(--info);}.bar-fill.c3{background:var(--success);}.bar-fill.c4{background:var(--warning);}
.card{background:var(--card-bg);border:1px solid var(--border);padding:16px 20px;margin:14px 0;border-left:4px solid var(--accent);}
.card.info{border-left-color:var(--info);}.card.success{border-left-color:var(--success);}.card.warning{border-left-color:var(--warning);}
.card-title{font-weight:700;color:var(--accent);margin-bottom:6px;font-size:1.02em;}
.card.info .card-title{color:var(--info);}.card.success .card-title{color:var(--success);}.card.warning .card-title{color:var(--warning);}
.tag{display:inline-block;padding:1px 8px;border-radius:3px;font-size:.78em;margin:2px 3px 2px 0;}
.tag.red{background:#f5d5d5;color:var(--accent);}.tag.blue{background:#d5dff5;color:var(--info);}
.tag.green{background:#d5f5df;color:var(--success);}.tag.orange{background:#f5eed5;color:var(--warning);}.tag.purple{background:#e8d5f5;color:#6b2e8b;}
ul,ol{padding-left:22px;margin:6px 0;}li{margin-bottom:3px;}p{margin:8px 0;}strong{color:var(--accent);}
.highlight{background:#fff3cd;padding:1px 5px;border-radius:2px;}
.footnote{font-size:.85em;color:#888;border-top:1px solid var(--border);padding-top:16px;margin-top:50px;}
nav{margin:0 0 30px;display:flex;flex-wrap:wrap;gap:8px;justify-content:center;}
nav a{padding:6px 16px;border-radius:20px;font-size:.9em;color:var(--text);text-decoration:none;background:var(--card-bg);border:1px solid var(--border);}
nav a.active{background:var(--accent);color:#fff;border-color:var(--accent);}
nav a:hover{background:var(--tag-bg);}nav a.active:hover{background:var(--accent);}
@media(max-width:700px){.cover h1{font-size:1.5em;}.bar-label{width:100px;}}
</style>"""

NAV = """<nav>
<a href="../jijiu/index.html">冲刺加油站</a>
<a href="../yuwen/index.html">语文</a>
<a href="../shuxue/index.html">数学</a>
<a href="../wuli/index.html">物理</a>
<a href="../huaxue/index.html">化学</a>
<a href="index.html" class="active">英语</a>
<a href="../lishi/index.html">历史</a>
<a href="../daofa/index.html">道法</a>
</nav>"""

from gen_data import PAGES

def bar(label, pct, cls="c1", val=""):
    return f'<div class="bar-row"><div class="bar-label">{label}</div><div class="bar-track"><div class="bar-fill {cls}" style="width:{pct}%">{val}</div></div></div>'

def tag(text, color="blue"):
    return f'<span class="tag {color}">{text}</span>'

def gen_page(d):
    city = d.get("city", "沈阳")
    exam_round = d.get("round", "一模")
    has_listening = d.get("has_listening", True)

    # --- 阅读篇章分析 ---
    passages_html = ""
    for p in d["passages"]:
        tags_str = "".join(tag(t, c) for t, c in p.get("tags", []))
        passages_html += f"""<div class="card {p.get('cls','info')}">
<div class="card-title">{p['id']}篇 · {p['genre']} · {p['topic']}</div>
<p><strong>主题领域：</strong>{p['theme']}　<strong>难度：</strong>{p['difficulty']}　{tags_str}</p>
<table><tr><th>题号</th><th>设题类型</th><th>考查能力</th><th>正确选项定位</th></tr>
"""
        for q in p["questions"]:
            passages_html += f'<tr><td>{q["no"]}</td><td>{q["type"]}</td><td>{q["ability"]}</td><td>{q["location"]}</td></tr>\n'
        passages_html += "</table></div>\n"

    # --- 阅读还原 ---
    restore_html = ""
    if "restore" in d:
        r = d["restore"]
        restore_html = f"""<h4>阅读还原（五选四，8分）</h4>
<div class="card info"><div class="card-title">{r['topic']}</div>
<p><strong>文章结构：</strong>{r['structure']}</p>
<table><tr><th>空格</th><th>位置</th><th>衔接线索</th><th>正确答案</th></tr>
"""
        for slot in r["slots"]:
            restore_html += f'<tr><td>{slot[0]}</td><td>{slot[1]}</td><td>{slot[2]}</td><td>{slot[3]}</td></tr>\n'
        restore_html += "</table></div>\n"

    # --- 完形填空 ---
    cloze = d["cloze"]
    cloze_rows = ""
    for q in cloze["questions"]:
        cloze_rows += f'<tr><td>{q["no"]}</td><td>{q["type"]}</td><td>{q["pos"]}</td><td>{q["answer"]}</td><td>{q["clue"]}</td></tr>\n'
    cloze_stats = ""
    for wt in cloze["word_types"]:
        cloze_stats += f'<tr><td>{wt[0]}</td><td>{wt[1]}</td><td>{wt[2]}</td></tr>\n'

    # --- 语篇填空 ---
    grammar_rows = ""
    for g in d["grammar"]:
        grammar_rows += f'<tr><td>{g["no"]}</td><td>{g["type"]}</td><td>{g["point"]}</td><td>{g["answer"]}</td><td>{g["clue"]}</td></tr>\n'
    grammar_stats = ""
    for gs in d["grammar_stats"]:
        grammar_stats += f'<tr><td>{gs[0]}</td><td>{gs[1]}</td><td>{gs[2]}</td></tr>\n'

    # --- 阅读与表达 ---
    reading_expr_rows = ""
    for q in d["reading_expression"]:
        reading_expr_rows += f'<tr><td>{q["no"]}</td><td>{q["score"]}</td><td>{q["type"]}</td><td>{q["question"]}</td><td>{q["answer"]}</td></tr>\n'

    # --- 书面表达 ---
    w = d["writing"]

    # --- 阅读微技能统计 ---
    skill_rows = ""
    for s in d["reading_skills"]:
        skill_rows += f'<tr><td>{s[0]}</td><td>{s[1]}</td><td>{s[2]}</td><td>{s[3]}</td></tr>\n'

    # --- 话题分布 ---
    topic_rows = ""
    for t in d["topics"]:
        topic_rows += f'<tr><td>{t[0]}</td><td>{t[1]}</td><td>{t[2]}</td></tr>\n'

    # --- 命题DNA ---
    dna_cards = ""
    for i, obs in enumerate(d["dna"]):
        cls = ["", "info", "success", "warning"][i % 4]
        dna_cards += f'<div class="card {cls}"><div class="card-title">{obs["title"]}</div><p>{obs["body"]}</p></div>\n'

    # --- 作战地图 ---
    strategy_cards = ""
    for s in d["strategy"]:
        strategy_cards += f'<div class="card {s.get("cls","")}"><div class="card-title">{s["title"]}</div>{s["body"]}</div>\n'

    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{d["district"]}{exam_round}英语试卷深度分析</title>
{CSS}
</head>
<body>
<div class="container">
{NAV}
<div class="cover">
<h1>{city}{d["district"]}{exam_round}<br>英语试卷深度分析报告</h1>
<div class="subtitle">{d["exam_name"]} · 英语</div>
<div class="subtitle" style="font-size:.95em;color:#999;">骨架图 · 题型谱 · 考点标签 · 命题DNA · 作战地图</div>
<div class="meta">数据来源：原始试卷PDF + OCR提取 + 原图校核<br>分析日期：2026年4月25日</div>
</div>

<div class="toc"><h2>目 录</h2><ol>
<li><a href="#ch1">维度一 · 骨架图（结构解剖）</a></li>
<li><a href="#ch2">维度二 · 题型谱（逐题档案）</a></li>
<li><a href="#ch3">维度三 · 考点标签（知识定位）</a></li>
<li><a href="#ch4">维度四 · 命题DNA（命题解码）</a></li>
<li><a href="#ch5">维度五 · 作战地图（行动转化）</a></li>
</ol></div>

<h2 class="section-title" id="ch1">维度一 · 骨架图（结构解剖）</h2>
<h3>基本参数</h3>
<table>
<tr><th>参数</th><th>本卷</th><th>辽宁省卷对标</th></tr>
<tr><td>总分</td><td>{"120分（笔试90分+听力30分）" if has_listening else "90分（笔试卷·听力口语单独考试30分）"}</td><td>120分 ✓</td></tr>
<tr><td>笔试题量</td><td>45题</td><td>45题 ✓</td></tr>
<tr><td>含听力</td><td>{"是（20题30分）" if has_listening else "否（听力单独考试）"}</td><td>听力30分</td></tr>
<tr><td>考试形式</td><td>闭卷笔试</td><td>闭卷笔试 ✓</td></tr>
<tr><td>笔试时长</td><td>90分钟</td><td>90分钟 ✓</td></tr>
<tr><td>命题级别</td><td>{"区级" if city == "沈阳" else "市级"}{exam_round}（{d["district"]}）</td><td>省级统考卷</td></tr>
</table>

<h3>笔试结构分布</h3>
<table>
<tr><th>大题</th><th>题型</th><th>题号</th><th>题量</th><th>每题分值</th><th>小计</th><th>占笔试%</th></tr>
<tr><td rowspan="2">一</td><td>阅读选择（4篇）</td><td>Q21-Q36</td><td>16题</td><td>2分</td><td>32分</td><td>35.6%</td></tr>
<tr><td>阅读还原（五选四）</td><td>Q37-Q40</td><td>4题</td><td>2分</td><td>8分</td><td>8.9%</td></tr>
<tr><td>二</td><td>完形填空</td><td>Q41-Q50</td><td>10题</td><td>1分</td><td>10分</td><td>11.1%</td></tr>
<tr><td>三</td><td>语篇填空</td><td>Q51-Q60</td><td>10题</td><td>1分</td><td>10分</td><td>11.1%</td></tr>
<tr><td>四</td><td>阅读与表达</td><td>Q61-Q64</td><td>4题</td><td>2+2+2+4</td><td>10分</td><td>11.1%</td></tr>
<tr><td>五</td><td>书面表达</td><td>Q65</td><td>1题</td><td>20分</td><td>20分</td><td>22.2%</td></tr>
<tr><td colspan="3"><strong>笔试合计</strong></td><td><strong>45题</strong></td><td></td><td><strong>90分</strong></td><td><strong>100%</strong></td></tr>
</table>
{('<div class="card info"><div class="card-title">📋 本卷说明</div><p>' + d["skeleton_note"] + '</p></div>') if d.get("skeleton_note") else ''}

<h3>选择题 vs 非选择题</h3>
<div class="bar-chart">
{bar("选择题","56","c2","50分 / 55.6%")}
{bar("非选择题","44","c1","40分 / 44.4%")}
</div>

<h3>能力维度分值分布</h3>
<div class="bar-chart">
{bar("阅读理解","56","c1","50分 / 55.6%")}
{bar("书面表达","22","c4","20分 / 22.2%")}
{bar("语言知识运用","22","c2","20分 / 22.2%")}
</div>

<div class="card info"><div class="card-title">骨架图解读</div><p>{d["skeleton_note"]}</p></div>

<h2 class="section-title" id="ch2">维度二 · 题型谱（逐题档案）</h2>

<h3>阅读选择（4篇 × 4题 = 32分）</h3>
{passages_html}

{restore_html}

<h3>完形填空（10题 × 1分 = 10分）</h3>
<div class="card">
<div class="card-title">{cloze['genre']} · {cloze['topic']}</div>
<p><strong>情感线索：</strong>{cloze['emotion_line']}</p>
<p><strong>主题启示：</strong>{cloze['theme']}</p>
</div>
<table><tr><th>题号</th><th>考查类型</th><th>词性</th><th>正确答案</th><th>解题线索</th></tr>
{cloze_rows}
</table>
<h4>完形填空词性分布</h4>
<table><tr><th>词性</th><th>题数</th><th>占比</th></tr>
{cloze_stats}
</table>

<h3>语篇填空（10题 × 1分 = 10分）</h3>
<div class="card info">
<div class="card-title">{d['grammar_topic']}</div>
<p><strong>话题类型：</strong>{d['grammar_theme']}</p>
</div>
<table><tr><th>题号</th><th>填空类型</th><th>语法点</th><th>正确答案</th><th>解题思路</th></tr>
{grammar_rows}
</table>
<h4>语法点分布统计</h4>
<table><tr><th>语法点</th><th>题数</th><th>频次评级</th></tr>
{grammar_stats}
</table>

<h3>阅读与表达（10分）</h3>
<div class="card success">
<div class="card-title">{d['reading_expr_topic']}</div>
<p><strong>体裁：</strong>{d['reading_expr_genre']}　<strong>情感基调：</strong>{d['reading_expr_tone']}</p>
</div>
<table><tr><th>题号</th><th>分值</th><th>题型</th><th>问题</th><th>参考答案</th></tr>
{reading_expr_rows}
</table>

<h3>书面表达（20分）</h3>
<div class="card warning">
<div class="card-title">{w['type']} · {w['topic']}</div>
<p><strong>字数要求：</strong>{w['word_count']}词　<strong>体裁：</strong>{w['genre']}</p>
<p><strong>写作要点：</strong></p>
<ol>{"".join(f"<li>{r}</li>" for r in w['requirements'])}</ol>
<p><strong>难度评估：</strong>{w['difficulty']}</p>
</div>

<h2 class="section-title" id="ch3">维度三 · 考点标签（知识定位）</h2>

<h3>阅读微技能分布</h3>
<table><tr><th>阅读微技能</th><th>涉及题号</th><th>题数</th><th>分值</th></tr>
{skill_rows}
</table>

<h3>话题与主题分布</h3>
<table><tr><th>篇章/题目</th><th>话题</th><th>主题领域</th></tr>
{topic_rows}
</table>

<h2 class="section-title" id="ch4">维度四 · 命题DNA（命题解码）</h2>
{dna_cards}

<h2 class="section-title" id="ch5">维度五 · 作战地图（行动转化）</h2>
{strategy_cards}

<h3>全卷目标分数规划</h3>
<table>
<tr><th>板块</th><th>满分</th><th>保底目标</th><th>冲刺目标</th></tr>
{d["target_rows"]}
<tr><td><strong>合计</strong></td><td><strong>{"120分" if has_listening else "90分"}</strong></td><td><strong>{d["target_low"]}</strong></td><td><strong>{d["target_high"]}</strong></td></tr>
</table>

<div class="footnote">
<p><strong>试卷来源：</strong>{city}{d["district"]}2026年九年级学情调研·英语（PDF扫描版）<br>
<strong>分析方法：</strong>五维解析法（骨架图/题型谱/考点标签/命题DNA/作战地图）<br>
<strong>生成日期：</strong>2026年4月25日</p>
</div>
</div>
</body>
</html>"""

if __name__ == "__main__":
    for key, d in PAGES.items():
        html = gen_page(d)
        with open(f"/home/ekewang/projects/zhongkao/yingyu/{key}.html", "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Generated {key}.html ({len(html)} bytes)")
