# 英语试卷分析 · Best Practice 复盘总结

> 基于10套英语模拟卷（沈阳7区+抚顺+营口+铁岭）的完整分析流程总结
> 目的：下次再做学科分析时少走弯路

---

## 一、整体流程回顾

### 实际执行顺序（10套卷 → 单卷页面 → 首页 → 横向对比）

```
Phase 1: 数据录入 + 单卷页面生成
  ├─ 写 SKILL_英语单卷分析.md（五维分析模板）
  ├─ OCR文本 → 逐卷分析 → 填入 gen_data.py / gen_data_extra.py
  ├─ gen.py 模板引擎 → 批量生成 10 个 .html 文件
  └─ git push 部署

Phase 2: 首页 index.html 丰富
  ├─ 从语文 index.html 对标质量水平
  ├─ 补充：板块权重分布 / 命题铁律 / 考点频次表 / 写作趋势
  └─ git push 部署

Phase 3: 横向对比 duibi.html
  ├─ 确定分析维度（最终7个，去掉听力）
  ├─ Python 脚本从 gen_data 提取跨卷统计数据
  ├─ 手写完整 HTML（~480行）
  └─ git push 部署
```

### 总耗时分布（估算）

| 阶段 | 占比 | 主要工作 |
|------|------|----------|
| 数据录入（10套卷的 gen_data） | ~45% | OCR→逐题分析→填字段（最耗时） |
| 模板/引擎调试（gen.py） | ~15% | CSS + 条件渲染(听力/无听力) |
| 首页丰富（index.html） | ~15% | 对标语文质量水平 |
| 横向对比（duibi.html） | ~20% | 数据提取+7维度HTML |
| 部署/修bug | ~5% | git push + 文件冲突 |

---

## 二、踩过的坑 & 解决方案

### 坑1: gen_data.py 文件过大，上下文溢出

**问题**: 前两套卷(和平/浑南)直接写在 gen_data.py 中，加上后面8套，单文件会超过3000行，AI上下文容易丢失前面的数据结构。

**解决**: 拆分为 `gen_data.py`（主文件，仅含和平+浑南） + `gen_data_extra.py`（8套卷，每套一个函数）。主文件底部 `from gen_data_extra import ...` 导入。

**Best Practice**:
- **数据文件超过500行就拆分**，每个函数返回一个 dict
- 主文件只做 `PAGES["key"] = func()` 的汇总
- 这样每次只需要看一个函数的上下文，不会丢失结构

### 坑2: 单卷数据字段不一致导致 gen.py 报错

**问题**: 前几套卷的字段名/结构和后几套不一致（比如 `has_listening` 有的写 True 有的漏了，`target_rows` 格式不统一），gen.py 渲染时报 KeyError。

**解决**: 在 gen.py 中加了条件判断 `d.get("has_listening", False)`，并在 gen_data 中统一所有卷的字段。

**Best Practice**:
- **先定义数据 schema，再开始填数据**。SKILL.md 中应包含一份完整的 `dict` 字段定义表
- gen.py 模板中所有字段都用 `.get()` + 默认值，防御性编程
- 每完成一套卷的数据，立即 `python gen.py` 验证能否生成，不要攒到最后

### 坑3: create_file 无法覆盖已有文件

**问题**: duibi.html 已存在旧版本，`create_file` 工具拒绝覆盖，返回 "File already exists"。多次尝试浪费时间。

**解决**: 先 `rm` 删除旧文件，再 `create_file` 创建新文件。

**Best Practice**:
- **大文件整体替换时**：`rm` + `create_file` 是最可靠的方式
- **小修改时**：`replace_string_in_file` 或 `multi_replace_string_in_file`
- 不要尝试用 `replace_string_in_file` 替换整个文件内容（oldString 太长会匹配失败）

### 坑4: 横向对比维度一开始定了8个（含听力），后来要去掉

**问题**: 最初按8个维度（含听力分析）规划了 duibi.html，写了一半才被告知听力不需要分析（因为听力各市单独考，模拟卷不统一）。推翻重来浪费了大量时间。

**解决**: 去掉听力维度，改为7个维度重写。

**Best Practice**:
- **动手前先确认分析维度**，尤其是"哪些板块在所有试卷中统一/不统一"
- 英语特殊性：听力30分各市单独组织，模拟卷中听力部分不统一，不适合做横向对比
- **维度确认 checklist**：
  - [ ] 该板块在所有试卷中都存在吗？
  - [ ] 数据结构一致吗？（题量/分值/题型）
  - [ ] 有足够的对比价值吗？（不是简单罗列而是能发现趋势）

### 坑5: 数据提取脚本与手动核实的矛盾

**问题**: 用 Python 脚本从 gen_data 自动提取统计数据（如阅读体裁分布、题型频次），但某些字段（如阅读还原的话题）在 gen_data 中没有单独字段，需要从 OCR 原文中人工补充。

**解决**: 分两阶段——先用脚本提取结构化数据（能自动化的部分），再人工补充非结构化数据。

**Best Practice**:
- **gen_data 的字段设计要为横向对比服务**。一开始就要想好"哪些字段将来要跨卷汇总"
- 建议在 SKILL 中列出"横向对比需要的字段清单"，确保单卷分析时把这些字段都填上
- 具体到英语，以下字段是横向对比必须的：
  ```
  passages[].genre     # 体裁（应用文/记叙文/说明文/议论文）
  passages[].topic     # 话题（一句话）
  passages[].theme     # 主题领域
  passages[].questions[].type  # 题型（细节理解/推理判断/...）
  cloze.genre          # 完形体裁
  cloze.topic          # 完形话题
  cloze.emotion_arc    # 情感弧线
  grammar.topic        # 语法填空话题
  grammar.theme        # 语法填空主题
  grammar.points[]     # 语法考点列表
  writing.genre        # 写作体裁
  writing.topic        # 写作话题
  reading_expression.topic   # 阅读表达话题
  restoration.topic    # 阅读还原话题
  ```

### 坑6: index.html 内容单薄，与语文差距大

**问题**: 英语 index.html 一开始只有简单的试卷列表（10个链接），而语文 index.html 已经做到了"板块权重 + 命题铁律 + 高频考点表 + 写作趋势"的丰富程度。被指出差距后需要大幅补充。

**解决**: 对标语文 index.html，补充了板块权重分布、4条命题铁律、11行必考考点频次表、书面表达趋势分析。

**Best Practice**:
- **index.html 不是简单的链接列表，是"学科分析入口页"**
- 标准内容清单：
  - [ ] 板块权重分布（柱状图/饼图）
  - [ ] 3-5条命题铁律（insight cards）
  - [ ] 高频考点频次表（从 duibi 数据反哺）
  - [ ] 写作/压轴趋势分析
  - [ ] 各单卷链接（含简短描述+话题关键词）
  - [ ] duibi.html 链接（置顶/featured）
- **执行顺序建议**：先做完 duibi 横向对比 → 再用对比结论反哺 index.html

---

## 三、与语文/数学对比的关键差异

| 维度 | 语文 | 数学 | 英语 |
|------|------|------|------|
| 单卷数据量 | 中等（22-24题） | 中等（23-25题） | **大**（45题+8篇文本+逐篇话题分析） |
| 数据结构复杂度 | 中等 | 简单 | **高**（嵌套：passages→questions→type/ability） |
| 横向对比维度 | 8个（结构/古诗/文言/现代文/名著/作文/考点/策略） | 8个（结构/领域/压轴/情境/新定义/...） | **7个**（阅读体裁/题型频次/语法/完形/写作/主题渗透/备考） |
| gen_data 拆分 | 未拆分（12套在一个文件） | 已拆分 | **必须拆分**（10套数据量太大） |
| 横向对比可自动化程度 | 低（大量文本分析） | 高（数字统计为主） | **中等**（结构化字段可自动提取，话题/情感弧线需人工） |
| 特殊处理 | 作文二选一 | 新定义题分类 | **听力有/无的条件渲染** |

---

## 四、英语分析的最佳执行流程（下次照做）

### Step 0: 准备阶段（做一次，后续复用）

- [ ] 确认 SKILL_英语单卷分析.md 是否需要更新
- [ ] 确认 gen.py 模板是否能处理所有情况（有听力/无听力/特殊结构）
- [ ] 确认 gen_data 的 schema（字段列表 + 类型 + 必填/可选）
- [ ] 确认横向对比需要的字段清单（Step 0 就定好，不要等到 Phase 3）

### Step 1: 单卷数据录入（最耗时，按流水线执行）

每套卷严格按以下顺序：

1. **读OCR** → 确认试卷结构（有无听力？题号范围？）
2. **读答案** → 对每道题标注正确答案
3. **填 passages[]** → 4篇阅读选择（体裁/话题/主题/题型分类）
4. **填 restoration** → 阅读还原（话题/结构/衔接手段）
5. **填 cloze** → 完形（体裁/话题/情感弧线/词类统计）
6. **填 grammar** → 语篇填空（话题/主题/语法点清单）
7. **填 reading_expression** → 阅读表达（话题/题型/开放性题分析）
8. **填 writing** → 书面表达（体裁/话题/要点）
9. **填 battle_plan** → 作战地图（P0/P1/P2策略）
10. **填 target_rows** → 目标分数表
11. **`python gen.py` 验证** → 确认HTML能正常生成
12. **git push** → 每2-3套卷推一次，不要攒到最后

**关键**: 不要跳着填。按 passages → cloze → grammar → writing 的顺序，跟试卷阅读顺序一致，不容易漏。

### Step 2: 首页 + 横向对比（数据录完后再做）

```
2a. Python脚本提取跨卷统计数据
    └─ 从 gen_data 自动提取：体裁计数/题型频次/语法矩阵/完形词类统计
    └─ 人工补充：情感弧线/阅读还原话题/主题渗透关系

2b. 写 duibi.html（7个维度，每个维度独立section）
    └─ 先写框架（7个空section）
    └─ 再逐维度填充数据+结论+insight

2c. 用 duibi 结论反哺 index.html
    └─ 命题铁律 ← duibi维度一的体裁锁定规律
    └─ 考点频次 ← duibi维度二/三的统计表
    └─ 写作趋势 ← duibi维度五的体裁/话题聚类
```

### Step 3: 部署验证

```
git add -A
git commit -m "英语: 完成全部10套卷+index+duibi"
git push origin main
# Vercel 自动部署，等2分钟后打开网页验证
```

---

## 五、gen_data Schema 定义（下次直接复用）

```python
{
    "district": str,          # "和平区"
    "exam_name": str,         # "2026年九年级学情调研问卷"
    "has_listening": bool,    # True/False — 控制总分显示120/90

    "skeleton_note": str,     # HTML字符串，结构解读说明

    # ---- 阅读选择 (4篇) ----
    "passages": [
        {
            "id": "A/B/C/D",
            "genre": str,     # 应用文/记叙文/说明文/议论文/新闻报道
            "topic": str,     # 一句话话题描述
            "theme": str,     # 主题领域标签
            "difficulty": str, # ★☆☆/★★☆/★★★
            "cls": str,       # card CSS class: info/success/warning/""
            "tags": [(label, color)],  # 标签列表
            "questions": [
                {
                    "no": str,       # "Q21"
                    "type": str,     # 细节理解/推理判断/标题选择/主旨大意/...
                    "ability": str,  # 考查能力简述
                    "location": str, # 答案定位说明
                }
            ]
        }
    ],

    # ---- 阅读还原 ----
    "restoration": {
        "topic": str,
        "structure": str,
        "items": [{"no":str, "position":str, "clue":str, "answer":str}]
    },

    # ---- 完形填空 ----
    "cloze": {
        "genre": str,         # 体裁
        "topic": str,         # 话题
        "emotion_arc": str,   # 情感弧线
        "theme": str,         # 主题/启示
        "items": [{"no":str, "type":str, "pos":str, "answer":str, "clue":str}]
    },

    # ---- 语篇填空 ----
    "grammar": {
        "topic": str,
        "theme": str,
        "items": [{"no":str, "fill_type":str, "point":str, "answer":str, "logic":str}]
    },

    # ---- 阅读与表达 ----
    "reading_expression": {
        "topic": str,
        "genre": str,
        "mood": str,
        "items": [{"no":str, "score":int, "type":str, "question_type":str, "source":str}]
    },

    # ---- 书面表达 ----
    "writing": {
        "type": str,          # 书信/新闻报道/发言稿/...
        "topic": str,
        "genre": str,
        "word_count": str,
        "points": [str],
        "difficulty": str
    },

    # ---- 命题DNA ----
    "dna_cards": [{"cls":str, "title":str, "body":str}],

    # ---- 作战地图 ----
    "battle_plan": [{"cls":str, "title":str, "body":str}],

    # ---- 目标分数 ----
    "target_rows": str,       # HTML <tr> 字符串
    "target_low": str,        # "61分(68%)"
    "target_high": str,       # "81分(90%)"
}
```

---

## 六、横向对比 duibi.html 的7个维度模板

| 维度 | 核心数据来源 | 可自动提取 | 需人工补充 |
|------|------------|-----------|-----------|
| 1. 阅读体裁×话题矩阵 | passages[].genre + topic | ✓ 体裁计数 | 话题分类标签 |
| 2. 阅读题型频次热力图 | passages[].questions[].type | ✓ 完全自动 | — |
| 3. 语法考点矩阵 | grammar.items[].point | ✓ 大部分 | 归类到12大考点 |
| 4. 完形选材与解题线索 | cloze.genre + emotion_arc | ✓ 体裁/词类 | 情感弧线描述 |
| 5. 书面表达体裁与话题 | writing.type + topic | ✓ 体裁计数 | 话题聚类标签 |
| 6. 跨板块主题渗透 | 所有板块的 theme/topic | ✗ | 需人工分析交叉关系 |
| 7. 备考优先级矩阵 | 各维度统计结论汇总 | ✗ | 需人工综合判断 |

**自动化建议**: 维度1-5写提取脚本(~50行Python)，维度6-7纯人工分析。

---

## 七、通用经验（适用于所有学科）

### 7.1 数据先行，HTML后行
- 先把所有卷的数据录完并验证，再写 index 和 duibi
- 不要"边录数据边写对比"，否则前面的结论可能被后面的数据推翻

### 7.2 拆文件是必需的
- 单文件超过500行 → 拆
- 10套卷以上 → 主文件 + extra文件 + 每套卷一个函数
- gen.py 模板单独一个文件，不要和数据混在一起

### 7.3 index.html 的质量标准
- 不是链接列表，是"学科分析入口页"
- 标配：板块权重 + 命题铁律 + 高频考点 + 趋势分析 + 单卷链接 + duibi链接
- 做完 duibi 后回头补充 index（用对比结论反哺）

### 7.4 duibi.html 的维度设计原则
- 每个维度必须有"数据表 + 结论 + 备考策略"三件套
- insight card 用 warn/info/ok 三色区分重要级别
- 最后一个维度必须是"备考优先级矩阵"（P0/P1/P2分级）

### 7.5 CSS 一致性
- 所有学科共用同一套配色(--bg/#f5f1e8, --primary/#8b2e2e)
- duibi.html 用自包含CSS（不依赖外部main.css）
- 单卷页面用 gen.py 内嵌CSS

### 7.6 部署流程
- 每完成一个阶段就 push（不要攒到最后）
- commit message 格式：`英语: 完成XX`
- Vercel 自动部署，push 后等2分钟即可

### 7.7 工具使用注意
- `create_file` 不能覆盖已有文件 → 先 `rm` 再 `create_file`
- 大文件(>200行)不要用 `replace_string_in_file` 全量替换
- Python验证脚本用 `run_in_terminal` 执行，看完整报错
- 数据提取脚本写成独立 .py 文件，方便反复运行调试

---

## 八、下次启动 Checklist

开始新学科分析前，按顺序核对：

- [ ] SKILL_XX单卷分析.md 是否就绪？
- [ ] gen_data schema 是否定义清楚？（含横向对比需要的字段）
- [ ] gen.py 模板是否能处理所有条件分支？
- [ ] 横向对比维度是否确认？（哪些板块统一/不统一？）
- [ ] index.html 内容清单是否明确？（不只是链接列表）
- [ ] 部署配置是否就绪？（Vercel/git remote）
- [ ] 文件拆分策略是否确定？（>500行必拆）
