#!/bin/bash
# 批量复制物理模拟卷到工作区
SRC="/mnt/c/Users/ekewang/OneDrive - Ericsson/B-Work/AI/中考模拟"
DST="/home/ekewang/projects/zhongkao/物理学科分析/模拟卷"
OK=0; FAIL=0; TOTAL=17

copy_one() {
    local src="$1" dst="$2" n="$3"
    cp -f "$src" "$dst" 2>/dev/null
    if [[ $? -eq 0 ]] && [[ -s "$dst" ]]; then
        echo "[$n/$TOTAL OK] $(basename "$dst") ($(stat -c%s "$dst") bytes)"
        ((OK++))
    else
        echo "[$n/$TOTAL FAIL] $(basename "$dst")"
        rm -f "$dst"  # 删除 0 字节文件
        ((FAIL++))
    fi
}

copy_one "$SRC/2026年4月于洪区区模/2026辽宁沈阳于洪区九下一模物理试卷.pdf" "$DST/于洪区_物理试卷.pdf" 1
copy_one "$SRC/2026年4月于洪区区模/2026辽宁沈阳于洪区九下一模物理试卷答案.pdf" "$DST/于洪区_物理答案.pdf" 2
copy_one "$SRC/2026年沈阳沈河区一模/2026.4沈阳沈河区九下一模-物理.pdf" "$DST/沈河区_物理试卷.pdf" 3
copy_one "$SRC/沈阳和平区/26沈阳和平一模物理试卷.pdf" "$DST/和平区_物理试卷.pdf" 4
copy_one "$SRC/沈阳和平区/26沈阳和平一模物理试卷答案.pdf" "$DST/和平区_物理答案.pdf" 5
copy_one "$SRC/沈阳浑南区/2026年4月沈阳浑南物理一模_.pdf" "$DST/浑南区_物理试卷.pdf" 6
copy_one "$SRC/沈阳浑南区/2026年4月沈阳浑南物理一模试卷及答案.pdf" "$DST/浑南区_物理答案.pdf" 7
copy_one "$SRC/沈阳皇姑区/2026年皇姑区一模物理.pdf" "$DST/皇姑区_物理试卷.pdf" 8
copy_one "$SRC/沈阳沈北新区/2026年4月沈阳沈北新区一模物理试卷.pdf" "$DST/沈北新区_物理试卷.pdf" 9
copy_one "$SRC/沈阳铁西区/2026铁西区一模物理试卷.pdf" "$DST/铁西区_物理试卷.pdf" 10
copy_one "$SRC/沈阳铁西区/沈阳铁西区2025-2026学年九年级中考一模物理试卷含答案.pdf" "$DST/铁西区_物理含答案.pdf" 11
copy_one "$SRC/沈阳苏家屯区/2025-2026辽宁沈阳苏家屯区九下中考一模物理含答案.pdf" "$DST/苏家屯区_物理含答案.pdf" 12
copy_one "$SRC/抚顺一模/2026.4.20辽宁抚顺市统考物理试卷.pdf" "$DST/抚顺市_物理试卷.pdf" 13
copy_one "$SRC/抚顺一模/2026.4.20辽宁抚顺市统考物理试卷答案.pdf" "$DST/抚顺市_物理答案.pdf" 14
copy_one "$SRC/营口市一模/2026年4月营口市市一模物理试卷.pdf" "$DST/营口市_物理试卷.pdf" 15
copy_one "$SRC/营口市一模/2026年4月营口市市一模物理试卷答案.pdf" "$DST/营口市_物理答案.pdf" 16
copy_one "$SRC/铁岭二模/2026.4铁岭九年物理二模试卷+答案.pdf" "$DST/铁岭市_物理试卷含答案.pdf" 17

echo ""
echo "========== 汇总 =========="
echo "成功: $OK / $TOTAL"
echo "失败: $FAIL / $TOTAL"
ls -1 "$DST"/*.pdf 2>/dev/null | wc -l
