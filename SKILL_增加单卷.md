# 增加单卷分析 · 通用操作 Skill

> **适用于**: 任何学科新增1-2套模拟卷的完整流程
> **前提**: 该学科已有 index.html、duibi.html 和若干已完成的单卷分析页
> **输入**: 用户提供的 PDF 文件（试卷 + 答案），由 Agent 提取文本
> **输出**: 新单卷分析页 + 更新后的 duibi.html + 更新后的 index.html + 全站计数同步

---

## 〇、学科参数速查

执行前先确认目标学科的参数：

| 参数 | 查找方式 |
|------|----------|
| 学科文件夹 | `{subject}/`（yuwen/shuxue/wuli/huaxue/yingyu/lishi/daofa） |
| 分析工作目录 | `{学科中文}学科分析/`（语文学科分析/数学学科分析/...） |
| 单卷分析 SKILL | `{学科中文}学科分析/SKILL_{学科中文}单卷分析.md` |
| 生成模式 | 有 gen.py → 脚本模式；无 → 手写 HTML 模式 |
| 当前套数 | `ls {subject}/*.html` 减去 index.html 和 duibi.html |
| 满分/题量 | 查看 `{subject}/index.html` 的 hero 区 |

### 7 学科速查表

| 学科 | 文件夹 | 满分 | 生成模式 | 当前套数（截至初始部署） |
|------|--------|------|----------|------------------------|
| 语文 | yuwen/ | 120分 | 手写 HTML | 12 |
| 数学 | shuxue/ | 120分 | 手写 HTML | 11 |
| 英语 | yingyu/ | 120分(笔90+听30) | gen.py | 10 |
| 物理 | wuli/ | 80分 | 手写 HTML | 11 |
| 化学 | huaxue/ | 50分 | gen.py | 11 |
| 历史 | lishi/ | 70分 | 手写 HTML | 8 |
| 道法 | daofa/ | 70分 | 手写 HTML | 6 |

---

## 一、Phase A · 准备（开始前必做）

### A1. 确认 slug

新卷的 slug 必须在 MASTER_SKILL.md 的全局注册表中注册。

**已有 slug**:
```
heping shenhe hunnan yuhong huanggu tiexi sujiatun shenbei fushun yingkou tieling tieling-ermo
```

**新增城市/区**时，取拼音，加入注册表：
```bash
# 例如大连
dalian → 大连市
```

⚠️ **铁律**: 同一区/市在所有学科中必须使用**完全相同的 slug**。

### A2. 从 PDF 提取文本（最关键步骤）

用户提供的输入是 PDF 文件（试卷 + 答案），存放于 `{学科中文}学科分析/` 目录。
必须准确提取全部文字内容，**任何漏字、错字都会导致后续分析错误**。

#### 工具优先级

| 优先级 | 工具 | 适用场景 | 安装/依赖 |
|--------|------|----------|-----------|
| **首选** | pdfplumber (Python) | 文字型 PDF（Word/WPS 导出、电子排版） | `pip install --user --break-system-packages pdfplumber` |
| **备选** | Tesseract OCR | 扫描型 PDF（扫描全能王、照片扫描件、图片型） | 系统已装 `/usr/bin/tesseract`，需 `chi_sim` 语言包 |

#### 步骤 1：用 pdfplumber 尝试提取（首选）

```python
import pdfplumber

pdf = pdfplumber.open("试卷.pdf")
for i, page in enumerate(pdf.pages):
    text = page.extract_text()
    if text:
        print(f"--- 第{i+1}页 ---")
        print(text)
    else:
        print(f"⚠️ 第{i+1}页无文字（可能是扫描件）")
pdf.close()
```

**判断标准**：
- ✅ 每页都有文字输出 → **文字型 PDF**，提取成功，保存为 `{区名}_试卷_ocr.md`
- ⚠️ 部分或全部页面输出为空/乱码 → **扫描型 PDF**，转步骤 2

#### 步骤 2：Tesseract OCR 提取（扫描件备选）

当 pdfplumber 提取为空时，说明 PDF 是扫描图片。流程：

```bash
# 2a. 用 pdfplumber 将每页转为 300dpi PNG
python3 -c "
import pdfplumber
pdf = pdfplumber.open('试卷.pdf')
for i, page in enumerate(pdf.pages):
    img = page.to_image(resolution=300)
    img.save(f'/tmp/{slug}_page_{i+1}.png')
pdf.close()
print(f'共导出 {len(pdf.pages)} 页')
"

# 2b. Tesseract 逐页 OCR
cd /tmp
text=""
for i in $(seq 1 {总页数}); do
    page_text=$(tesseract ${slug}_page_${i}.png stdout -l chi_sim 2>/dev/null)
    text="$text\n--- 第${i}页 ---\n$page_text"
done
echo -e "$text" > {学科中文}学科分析/ocr_text/{区名}_试卷_ocr.md

# 2c. 检查输出质量
wc -l {学科中文}学科分析/ocr_text/{区名}_试卷_ocr.md
head -50 {学科中文}学科分析/ocr_text/{区名}_试卷_ocr.md
```

#### 步骤 3：答案 PDF 单独提取

答案 PDF 通常是文字型（排版清晰），优先用 pdfplumber：

```python
import pdfplumber
pdf = pdfplumber.open("答案.pdf")
text = "\n".join(page.extract_text() or "" for page in pdf.pages)
with open("{学科中文}学科分析/ocr_text/{区名}_答案.md", "w") as f:
    f.write(text)
pdf.close()
```

⚠️ **注意**：部分试卷 PDF 内同时包含试卷和答案（如鞍山卷，前9页试卷+后5页答案），此时只需提取一个 PDF，但需标注分界点。

#### OCR 质量校验（Gate A2）

| 检查项 | 方法 |
|--------|------|
| 题号连续完整 | grep 搜索 `1\. 2\. 3\.` 或 `一、二、三` |
| 分值标注可见 | grep `分` 确认各题分值可读 |
| 关键内容无乱码 | 人工抽查古诗文/人名/专有名词 |
| 答案与试卷可交叉验证 | 试卷题号数 = 答案题号数 |

⚠️ **扫描件 OCR 常见问题**：
- 繁体/异体字识别错误（如"闵萧著"→实为其他人名）→ 需结合答案 PDF 交叉验证
- 表格/图片区域丢失文字 → 需人工补充或结合答案推断
- 数学公式/化学方程式 OCR 不可靠 → 必须与答案 PDF 核对

### A3. 确认 OCR 文件就位

```bash
ls {学科中文}学科分析/ocr_text/
# 需要存在：
# {区名}_试卷_ocr.md  — 试卷文本（必须）
# {区名}_答案.md      — 参考答案（强烈建议，无则标注）
```

### A4. 读取学科 SKILL

```bash
cat {学科中文}学科分析/SKILL_{学科中文}单卷分析.md
```

这个文件定义了该学科五维（或六维）分析的完整框架、CSS 样式、输出格式。**必须读取后再开始分析**。

### A5. 读取一份已有单卷作为模板

```bash
# 选择该学科中最近完成的一份单卷分析页作为 HTML 结构参考
cat {subject}/{最近完成的slug}.html | head -50
```

目的：确认 CSS 变量、HTML 结构、导航栏格式与现有页面一致。

---

## 二、Phase B · 生成单卷分析页

### B1. 手写 HTML 模式（语文/数学/物理/历史/道法）

按学科 SKILL 的五维框架，读取 OCR 文本 + 答案，生成 `{subject}/{slug}.html`。

**关键约束**:
- 内嵌 CSS（不依赖 main.css），与同学科其他单卷页面使用相同 `:root` 变量
- 导航栏与 MASTER_SKILL §十 一致，当前学科设为 `class="active"`
- 分值合计 = 试卷满分（必须人工验证）
- 逐题映射表不允许跳过任何一道题
- footer 包含生成日期和数据来源

### B2. gen.py 模式（英语/化学）

1. 在对应的 `gen_data.py` 或 `gen_data_extra{N}.py` 中添加新卷数据函数
2. 在主文件底部注册：`PAGES["{slug}"] = {slug}()`
3. 运行 `python gen.py` 生成 HTML
4. 验证输出 HTML 无报错

**gen_data 文件拆分规则**（来自 MASTER_SKILL §1.3）:

| 条件 | 策略 |
|------|------|
| ≤3套卷 | 全部在 gen_data.py |
| 4-6套卷 | gen_data.py(前2) + gen_data_extra.py(其余) |
| 7-12套卷 | gen_data.py(前2) + gen_data_extra.py(3-7) + gen_data_extra2.py(8-12) |
| >12套卷 | 每3-4套一个文件 |

### B3. 单卷验证（Gate B）

| 检查项 | 方法 |
|--------|------|
| HTML 可正常渲染 | 浏览器打开 or 检查 HTML 结构完整性 |
| 题目数量匹配 | 逐题表行数 = 试卷实际题数 |
| 分值合计正确 | 各部分分值之和 = 满分 |
| 导航栏正确 | nav 顺序、active 状态、链接路径 |
| 五维/六维齐全 | 每个维度的 section 均存在 |

---

## 三、Phase C · 更新横向对比（duibi.html）⚠️ 不可跳过

**每次增加新卷，duibi.html 必须全面更新。** 这不是可选操作。

### C1. 读取现有 duibi.html

```bash
cat {subject}/duibi.html
```

理解当前的维度结构和数据内容。

### C2. 逐维度更新清单

duibi.html 的**每一个维度/section** 都需要检查并更新。以下是通用检查项：

| 更新点 | 操作 | 如何验证 |
|--------|------|----------|
| **header 标题** | N套 → N+1套 | 搜索 `{N}套` |
| **header 覆盖范围** | 添加新城市/区名 | chip 标签列表 |
| **维度一：结构对比表** | 新增一行（题量/分值/结构特征） | 表格行数 = 套数 |
| **维度二-六：各对比表** | 每个表格都新增新卷对应行 | 逐表检查 |
| **关键发现/结论** | 根据新数据**重新审视**结论 | 频次/占比是否变化 |
| **高频考点/热力图** | 重新统计频次（N→N+1基数） | 百分比是否需要更新 |
| **备考策略** | 如果新卷引入新趋势，需要更新 | 检查是否有新考点 |
| **footer** | 覆盖套数、城市列表、日期 | 搜索 `覆盖{N}套` |

#### ⚠️ 新增行显示规则（必须遵守）

**1. 置顶显示**：新增卷的数据行必须插入到**每个表格 `<tbody>` 之后的最前面**（紧跟表头），而不是追加到表格末尾。这样用户打开页面第一眼就能看到新增内容。

**2. 高亮样式**：新增行必须使用以下标记：

```html
<!-- 新增行模板 -->
<tr class="new-row"><td>{区名}一模 <span class="badge-new">新增</span></td><td>...</td></tr>
```

**3. CSS 定义**（duibi.html 内嵌 `<style>` 中需包含）：

```css
.new-row td{background:#f0faf3}
.badge-new{display:inline-block;font-size:.72rem;padding:1px 7px;border-radius:999px;background:#16a34a;color:#fff;font-weight:700;margin-left:4px;vertical-align:middle}
```

如果 duibi.html 的 `<style>` 中已有这两条规则则无需重复添加。

**4. 所有表格统一处理**：duibi.html 中的**每一个数据表**都要对新增卷做置顶+高亮，不可只改部分表格。

### C3. 语文 duibi 特有维度更新参考

语文 duibi.html 有 8 个维度，增加新卷时每个都要更新：

| 维度 | 需更新内容 |
|------|-----------|
| 一、试卷结构对比 | 新增行：题量/积累/古诗文/现代文/写作/情境整合 |
| 二、古诗文选篇对比 | 新增行：甲篇(课内)/乙篇(课外)/对比维度 |
| 三、文言文课内篇目频次 | 更新频次统计，新增出现的篇目 |
| 四、现代文阅读选材 | 三个子表各新增一行(非连/记叙/议论or说明) |
| 五、名著考查形式 | 新增行（如果该卷有名著考查） |
| 六、作文命题对比 | 新增行：两个选项+主题方向 |
| 七、高频考点热力图 | 重新统计 tag 出现频次，调整分类 |
| 八、备考策略总纲 | 根据新数据审视建议是否需要调整 |

### C4. 其他学科 duibi 维度更新参考

按 MASTER_SKILL §九中各学科的维度列表逐一更新。核心原则：**每个维度中的每个数据表都要新增对应行**。

### C5. duibi 验证（Gate C）

| 检查项 | 方法 |
|--------|------|
| 所有表格行数 = 新套数 | 逐表检查 |
| 新增行在每个表格顶部 | 新增行紧跟 `<tbody>` 之后 |
| 新增行有高亮样式 | `class="new-row"` + `badge-new` 标签 |
| CSS 规则存在 | `.new-row td` 和 `.badge-new` 在 `<style>` 中 |
| 结论/发现已更新 | 频次描述是否反映新数据 |
| header 套数正确 | `grep "{N+1}套" {subject}/duibi.html` |
| footer 套数+城市+日期 | 底部信息更新 |

---

## 四、Phase D · 更新学科首页（index.html）

### D1. hero 区更新

```html
<!-- 修改前 -->
<div class="sub">12套模拟卷深度分析 · 闭卷考试 · 150分钟 · 满分120分</div>
<!-- 修改后 -->
<div class="sub">13套模拟卷深度分析 · 闭卷考试 · 150分钟 · 满分120分</div>
```

### D2. 数据速览卡片更新

```html
<!-- 需要更新的 stat-box -->
<div class="stat-box"><div class="num">{N} → {N+1}</div><div class="label">模拟卷</div></div>
<div class="stat-box"><div class="num">{旧题目总量} → {旧+新卷题数}</div><div class="label">题目总量</div></div>
<div class="stat-box"><div class="num">{旧总分值} → {旧+满分}</div><div class="label">总分值</div></div>
```

### D3. 板块权重/铁律/趋势更新

index.html 中的统计数据（如"十二卷均值"）需要更新文字说明中的基数：
- 搜索 `{N}卷` / `{N}套` 的所有出现位置
- 更新百分比（如果新卷改变了均值分布）
- 更新"关键发现"文字（如果结论发生变化）

### D4. 报告列表新增条目

在 `<div class="report-list">` 中添加新卷链接，**插入到 featured（对比分析）之后、其他报告之前**（置顶显示）：

```html
<!-- 新增卷报告条目模板 — 插入到 featured 条目之后 -->
<a class="report-item" href="{slug}.html">
  <div class="title">{区名}一模 <span class="tag green">新增</span></div>
  <div class="info">{题数}题 · 五维深度分析 · {关键内容描述}</div>
</a>
```

**显示规则**：
- `<span class="tag green">新增</span>` 标签加在标题文字后面（`.tag.green` 已在 main.css 中定义）
- 新增卡片紧跟 featured 对比分析卡片之后，排在所有旧报告之前
- 多张新卷按地市重要性排列（如大连在鞍山前面）

### D5. duibi 条目更新

如果 duibi 的标题变了（如"十二套卷横向对比"→"十三套卷横向对比"），index.html 中 featured 链接的标题也要同步。

### D6. index 验证（Gate D）

| 检查项 | 方法 |
|--------|------|
| hero 套数正确 | `grep "套模拟卷" {subject}/index.html` |
| stat-box 数字正确 | 模拟卷数/题目总量/总分值 |
| 新卷链接存在且置顶 | 新卷在 featured 之后、旧报告之前 |
| 新卷有"新增"标签 | `<span class="tag green">新增</span>` |
| duibi featured 标题同步 | 与 duibi.html 标题一致 |

---

## 五、Phase E · 全站计数同步 ⚠️ 最容易遗漏

每增加一卷，以下文件中的计数**全部需要更新**。

### E1. 受影响文件清单

| 文件 | 需更新内容 | grep 关键词 |
|------|-----------|-------------|
| `index.html`（首页） | ① hero 区总套数（如 69→70）<br>② 语文卡片副标题（如 12→13） | `{总套数}套` + `{学科套数}套模拟卷` |
| `jijiu/index.html` | hero 区总套数 | `{总套数}套` |
| `jijiu/zuozhan.html` | 底部数据来源（总套数 + 各科分项） | `{总套数}套.*{学科}{N}套` |
| `jijiu/print.html` | 底部数据来源（同上） | `{总套数}套.*{学科}{N}套` |

### E2. 计数公式

```
总套数 = 语文 + 数学 + 英语 + 物理 + 化学 + 历史 + 道法
增加1卷 → 总套数 +1，对应学科分项 +1
```

### E3. 全站 grep 验证（Gate E）

```bash
# 1. 搜索旧的总套数（应该为0结果）
grep -rn "{旧总套数}套" *.html jijiu/*.html {subject}/*.html

# 2. 搜索旧的学科套数（应该为0结果，除了不涉及的页面）
grep -rn "{学科中文}{旧学科套数}套" jijiu/*.html

# 3. 搜索新的套数确认（应该出现在所有预期位置）
grep -rn "{新总套数}套" *.html jijiu/*.html
grep -rn "{新学科套数}套" {subject}/index.html

# 4. 如果有 site/ 镜像目录中的对应文件也引用了套数，同步更新
grep -rn "{旧总套数}套\|{旧学科套数}套" site/ 2>/dev/null
```

---

## 六、Phase F · 提交部署

### F1. Git 操作

```bash
cd /home/ekewang/projects/zhongkao
git add -A
git diff --cached --stat   # 确认变更范围
git commit -m "{学科}: 新增{区名}单卷分析 (N→N+1套)"
git push origin main
# Vercel 自动部署（约2分钟）
```

### F2. 部署后验证

- 新单卷页面可访问
- index.html 链接可点击
- duibi.html 数据正确
- 首页套数正确

---

## 七、完整执行检查清单（Checklist）

每次增加单卷时，按顺序打勾：

```
Phase A · 准备
  □ slug 已确认（全局一致）
  □ PDF 文本已提取（pdfplumber 首选 → Tesseract 备选）
  □ OCR 质量已校验（题号连续 + 分值可读 + 与答案交叉验证）
  □ OCR 文件已就位（试卷 + 答案）
  □ 学科 SKILL 已读取
  □ 已有单卷模板已读取

Phase B · 单卷分析
  □ {subject}/{slug}.html 已生成
  □ 题目数量 = 试卷实际题数
  □ 分值合计 = 满分
  □ 五维/六维齐全
  □ 导航栏正确

Phase C · 横向对比更新
  □ duibi.html header 套数已更新
  □ 每个维度的数据表已新增行（置顶 + new-row 高亮 + badge-new 标签）
  □ duibi.html <style> 中包含 .new-row 和 .badge-new CSS 规则
  □ 关键发现/结论已重新审视
  □ 高频考点频次已重新统计
  □ footer 套数+城市+日期已更新

Phase D · 学科首页更新
  □ {subject}/index.html hero 套数已更新
  □ stat-box 数字已更新（模拟卷/题目总量/总分值）
  □ 报告列表已新增条目（置顶 + tag green "新增"标签）
  □ duibi featured 标题已同步

Phase E · 全站计数同步
  □ index.html 首页总套数已更新（如 69→70）
  □ index.html 学科卡片副标题已更新（如 12→13）
  □ jijiu/index.html 总套数已更新
  □ jijiu/zuozhan.html 底部数据已更新（总套数+分项）
  □ jijiu/print.html 底部数据已更新（总套数+分项）
  □ grep 验证旧套数已无残留

Phase F · 提交部署
  □ git add && commit && push
  □ 部署后验证通过
```

---

## 八、经验教训库（持续补充）

### 教训1: 计数不一致是最高频 Bug
- **现象**: 改了 index.html 忘了 jijiu/print.html，或反过来
- **根因**: 同一个数据（套数）散布在 5+ 个文件中
- **对策**: Phase E 的全站 grep 验证是强制步骤，不可跳过

### 教训2: DOM 元素删除前必须检查 JS 引用
- **现象**: 删除/替换 HTML 中带 `id` 的元素 → JS 报 null 引用
- **对策**: 修改 index.html 等有 JS 的页面时，先搜索 JS 中的 `getElementById`

### 教训3: duibi 结论必须基于新数据重新审视
- **现象**: 只在表格中加了一行，但结论文字还是说"12套中有X套..."
- **根因**: 机械添加行而不更新文字
- **对策**: Phase C 要求逐维度检查结论文字中的数字和描述

### 教训4: 学科 SKILL 是分析质量的锚点
- **现象**: 不读 SKILL 直接分析 → 维度缺失、格式不一致
- **对策**: Phase A3 是强制步骤，SKILL 文件必须先读再做

### 教训5: 英语时长 120→90 的连锁修改教训
- **现象**: 一处数据错误散布到多个文件，漏改一个就不一致
- **对策**: 任何可能在多处出现的数据，都用 grep 全站搜索确认

### 教训6: duibi.html 不可跳过或延迟
- **现象**: "先加卷，duibi 下次再更新" → 永远不会更新 → 数据不一致
- **对策**: 本 SKILL 将 duibi 更新设为 Phase C（强制），排在 Phase D 之前

### 教训7: PDF 提取必须先判断类型再选工具
- **现象**: 直接用 pdfplumber 提取扫描件 PDF → 返回空字符串 → 浪费时间尝试其他参数
- **根因**: 扫描件 PDF（如"扫描全能王"生成）内容是图片而非文字层
- **判断方法**: pdfplumber 的 `page.extract_text()` 返回空或极短 → 扫描件
- **正确流程**: pdfplumber 试提取 → 空则 pdfplumber 转 PNG(300dpi) → Tesseract OCR(chi_sim)
- **关键**: 不要跳过 pdfplumber 首选步骤，文字型 PDF 提取质量远优于 OCR

### 教训8: 答案 PDF 可能与试卷合并在同一文件中
- **现象**: 鞍山卷 PDF 前9页是试卷、后5页是答案，分开处理会遗漏
- **对策**: 提取完文本后先通读，确认是否包含答案部分；如果包含，标注分界页码

---

## 九、同时增加多卷的处理

如果一次增加 2+ 套卷到同一学科：

1. Phase B: 逐卷生成（每完成一卷立即验证）
2. Phase C: 一次性更新 duibi（把所有新卷一起加入）
3. Phase D-E: 一次性更新计数（N→N+2 或 N+K）
4. Phase F: 一次性提交

如果同时增加多个学科各一卷：

1. 按学科依次完成 Phase A-D
2. Phase E 统一做全站计数（总套数一次性加到位）
3. Phase F 一次性提交

---

## 十、快速启动模板

当用户说"增加 XX 学科 YY 区一模"时，AI 按以下顺序执行：

```
1. 读取本文件（SKILL_增加单卷.md）          ← 你已经在这里了
2. 确认参数：
   - 学科 = ?，文件夹 = ?
   - slug = ?（查注册表或新建）
   - 当前套数 = ?（ls {subject}/*.html）
   - 生成模式 = ?（有无 gen.py）
3. 读取学科 SKILL：cat {学科中文}学科分析/SKILL_{学科中文}单卷分析.md
4. 读取 OCR：cat {学科中文}学科分析/ocr_text/{区名}_试卷_ocr.md
5. 读取答案：cat {学科中文}学科分析/ocr_text/{区名}_答案.md
6. 读取模板：cat {subject}/{最近的slug}.html | head -50
7. 执行 Phase B → C → D → E → F
```
