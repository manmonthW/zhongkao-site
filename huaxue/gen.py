#!/usr/bin/env python3
"""Generate 4 chemistry analysis HTML pages."""

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
<a href="index.html" class="active">化学</a>
<a href="../yingyu/index.html">英语</a>
<a href="../lishi/index.html">历史</a>
<a href="../daofa/index.html">道法</a>
</nav>"""

# Import data module
from gen_data import PAGES
import gen_data_extra  # adds dalian/anshan to PAGES

def bar(label, pct, cls="c1", val=""):
    return f'<div class="bar-row"><div class="bar-label">{label}</div><div class="bar-track"><div class="bar-fill {cls}" style="width:{pct}%">{val}</div></div></div>'

def tag(text, color="blue"):
    return f'<span class="tag {color}">{text}</span>'

def gen_page(d):
    city = d.get("city", "沈阳")
    exam_round = d.get("round", "一模")
    rows_q = ""
    for q in d["questions"]:
        tags = "".join(tag(t, c) for t, c in q.get("tags", []))
        rows_q += f'<tr><td>{q["no"]}</td><td>{q["type"]}</td><td>{q["content"]}</td><td>{q["score"]}</td><td>{tags}</td></tr>\n'

    rows_kp = ""
    for k in d["knowledge"]:
        rows_kp += f'<tr><td>{k[0]}</td><td>{k[1]}</td><td>{k[2]}</td><td>{k[3]}</td></tr>\n'

    dna_cards = ""
    for i, obs in enumerate(d["dna"]):
        cls = ["", "info", "success", "warning"][i % 4]
        dna_cards += f'<div class="card {cls}"><div class="card-title">{obs["title"]}</div><p>{obs["body"]}</p></div>\n'

    strategy_cards = ""
    for s in d["strategy"]:
        strategy_cards += f'<div class="card {s.get("cls","")}"><div class="card-title">{s["title"]}</div>{s["body"]}</div>\n'

    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{d["district"]}{exam_round}化学试卷深度分析</title>
{CSS}
</head>
<body>
<div class="container">
{NAV}
<div class="cover">
<h1>{city}{d["district"]}{exam_round}<br>化学试卷深度分析报告</h1>
<div class="subtitle">{d["exam_name"]} · 化学</div>
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
<tr><td>总分</td><td>50分</td><td>50分 ✓</td></tr>
<tr><td>总题量</td><td>14题</td><td>14题 ✓</td></tr>
<tr><td>考试形式</td><td>闭卷笔试，与物理合卷</td><td>闭卷笔试 ✓</td></tr>
<tr><td>合卷时长</td><td>150分钟（化学约55分钟）</td><td>150分钟 ✓</td></tr>
<tr><td>命题级别</td><td>区级一模（{d["district"]}）</td><td>省级统考卷</td></tr>
</table>
<h3>结构分布</h3>
<table>
<tr><th>部分</th><th>题型</th><th>题号</th><th>题量</th><th>分值</th><th>占比</th></tr>
<tr><td>第一部分</td><td>选择题</td><td>1-10</td><td>10题</td><td>10分(每题1分)</td><td>20%</td></tr>
{d["structure_rows"]}
<tr><td colspan="3"><strong>合计</strong></td><td><strong>14题</strong></td><td><strong>50分</strong></td><td><strong>100%</strong></td></tr>
</table>
<h3>客观题 vs 主观题</h3>
<div class="bar-chart">
{bar("选择题（客观）","20","c2","10分 / 20%")}
{bar("非选择题（主观）","80","c1","40分 / 80%")}
</div>
<div class="card info"><div class="card-title">骨架图解读</div><p>{d["skeleton_note"]}</p></div>

<h2 class="section-title" id="ch2">维度二 · 题型谱（逐题档案）</h2>
<table>
<tr><th>题号</th><th>题型</th><th>简要内容</th><th>分值</th><th>标记</th></tr>
{rows_q}
</table>
<div class="card warning"><div class="card-title">题型谱关键发现</div><ul>{"".join(f"<li>{x}</li>" for x in d["type_findings"])}</ul></div>

<h2 class="section-title" id="ch3">维度三 · 考点标签（知识定位）</h2>
<table>
<tr><th>题号</th><th>知识维度</th><th>能力维度</th><th>教材定位</th></tr>
{rows_kp}
</table>
<h3>知识板块分值占比</h3>
<div class="bar-chart">
{"".join(bar(b[0],b[1],b[2],b[3]) for b in d["knowledge_bars"])}
</div>

<h2 class="section-title" id="ch4">维度四 · 命题DNA（命题解码）</h2>
{dna_cards}

<h2 class="section-title" id="ch5">维度五 · 作战地图（行动转化）</h2>
{strategy_cards}

<h3>全卷目标分数规划</h3>
<table>
<tr><th>板块</th><th>满分</th><th>保底目标</th><th>冲刺目标</th></tr>
<tr><td>选择题1-10</td><td>10分</td><td>8分</td><td>10分</td></tr>
{d["target_rows"]}
<tr><td><strong>合计</strong></td><td><strong>50分</strong></td><td><strong>{d["target_low"]}</strong></td><td><strong>{d["target_high"]}</strong></td></tr>
</table>

<div class="footnote">
<p><strong>试卷来源：</strong>{city}{d["district"]}2026年九年级学情调研·化学（PDF扫描版）<br>
<strong>分析方法：</strong>五维解析法（骨架图/题型谱/考点标签/命题DNA/作战地图）<br>
<strong>生成日期：</strong>2026年4月25日</p>
</div>
</div>
</body>
</html>"""

if __name__ == "__main__":
    for key, d in PAGES.items():
        html = gen_page(d)
        with open(f"/home/ekewang/projects/zhongkao/huaxue/{key}.html", "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Generated {key}.html ({len(html)} bytes)")
