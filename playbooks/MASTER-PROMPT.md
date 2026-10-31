# MASTER PROMPT · 通用主提示词

> 用法：把本文件 + 一个领域模板（`01`–`10`）+ 填好的 Brief 一起发给 AI。
>
> 建议分阶段：先让它做 Phase 0–2，验收后再继续。

---

## 1. 完整版（推荐）

```text
你是一名资深数据工程师 + 前端工程师 + 技术编辑。请为我从零复现一个「策展型目录站点」。

【输入】
1. 我已提供通用骨架：playbooks/00-universal-skeleton.md
2. 我已提供领域模板：playbooks/<编号>-<名称>.md
3. 我已提供项目 Brief（见最后）
4. 请严格遵守模板中的数据契约、页面结构、设计 tokens、验收标准。

【目标】
在一台干净机器上建立：
- data/catalog.json          机械抓取的原始目录
- data/items/*.json          策展后的条目（按分类分文件）
- data/relations.json        关系边表
- data/aliases.json          搜索别名
- scripts/fetch_catalog.py   抓取
- scripts/build.py           生成 Markdown / README 表格 / items.json
- scripts/build_site.py      生成 docs/ 静态站点
- scripts/check.py           数量 / 链接 / 字段 / 关系校验
- docs/                      可直接部署的静态站点
- .github/workflows/build.yml
- README.md                  线上地址、预览图、构建命令

【硬性规则】
1. 不要手写几十上百个 HTML 页面；所有详情页必须由数据生成。
2. 不要伪造任何 URL。找不到官方资源就留官方入口，并写「以官网为准」。
3. 第三方资源必须标注来源类型、访问方式、最后核验日期。
4. 目录（catalog）与策展（items）必须分离；抓取不能覆盖人工内容。
5. 每条 relation 必须有 source 或 note，否则不要画。
6. 时间敏感字段必须带 checked_at。
7. 所有相对链接必须能通过 check.py。
8. 移动端 390px 不得横向滚动。
9. 任何数量变化，同步更新 check.py 的预期值。
10. 不确定的字段写 null 并注明「待核验」，不要猜。

【执行阶段与验收门】
Phase 0：输出 BRIEF 确认、分类表、收录/排除标准。等我确认。
Phase 1：实现抓取脚本，产出 catalog.json；报告条目数、字段完整率、重复率。
Phase 2：先做 20–30 个条目的垂直切片（items + 详情页 + index），等我 review 文风与字段。
Phase 3：扩展到目标规模；生成 Markdown / README 表格。
Phase 4：实现关系图 / 时间线 / 对比页（按模板要求）。
Phase 5：补外部资源、搜索别名、第三方链接与失效报告。
Phase 6：实现 check.py 与 CI；确保 errors: 0。
Phase 7：部署说明 + 线上冒烟清单。

【每阶段输出格式】
- 改了哪些文件（路径列表）
- 运行了哪些命令
- 验收数字（条目数、页面数、errors、缺失字段数）
- 已知问题 / 待确认的 1–3 个问题
- 下一阶段计划（一句话）

【开始前】
先问我最多 5 个必要问题。如果 Brief 信息足够，直接开始 Phase 0。

【项目 Brief】
<在这里粘贴填好的 YAML>
```

---

## 2. 精简版（适合 Cursor / Claude Code 快速开工）

```text
读 playbooks/00-universal-skeleton.md 和 playbooks/<编号>-<名称>.md，
按其中的数据契约与页面结构，为我实现一个「<项目名>」静态站点。

Brief:
<粘贴 YAML>

要求：
- 先做 20 个条目的垂直切片，不要一次做完。
- 所有页面由 data/items/*.json 生成，不手写 HTML。
- 不伪造链接；不确定字段写 null + 「待核验」。
- 先给我：文件树 + 数据 schema + 3 个示例条目，等我确认后再写代码。
```

---

## 3. 领域模板追加指令

在完整版后面追加对应模板末尾的「给 AI 的增量指令」。例如：

- 课程：`playbooks/01-course-map.md`
- 论文：`playbooks/02-paper-map.md`
- 工具：`playbooks/03-tool-map.md`
- 会议：`playbooks/04-conference-map.md`
- 数据集：`playbooks/05-dataset-map.md`
- 学者：`playbooks/06-people-lab-map.md`
- 书单：`playbooks/07-book-map.md`
- 产业：`playbooks/08-industry-map.md`
- 法规：`playbooks/09-policy-map.md`
- 城市：`playbooks/10-local-guide.md`

---

## 4. 组合模板的提示词

```text
这是一个组合项目：
- 主模板：<02-paper-map>
- 叠加模板：<06-people-lab-map>、<04-conference-map>

请先合并三者的 Item schema：
- 以论文为主键
- 人物、会议作为独立 Item 类型
- 用 relations 连接（authored_by / published_at / cites）
- 页面保留：paper detail、person detail、conference detail、graph、timeline

合并后先输出统一 schema 和 5 个示例条目，等我确认再实现。
```

---

## 5. MVP 模式提示词

```text
先不要做完整站。只做 MVP：
- 20 个条目
- 1 个 index + 20 个详情页 + 404
- 无关系图、无时间线、无对比
- check.py 只校验：条目数、slug 唯一、站内链接
目标：2 小时内能在本地 python -m http.server 看到效果。
完成后再问我是否扩展。
```

---

## 6. 代码审查提示词（让第二个 AI 检查）

```text
你是代码审查者。请检查这个策展站项目是否满足：
1. 所有详情页由数据生成，没有手写 HTML。
2. catalog 与 items 分离，抓取不会覆盖人工内容。
3. check.py 是否真的能发现：缺页、坏链、缺字段、悬空 relation。
4. 时间敏感字段是否有 checked_at。
5. 是否有伪造/未标注的第三方链接。
6. 移动端是否可能横向溢出。

只报告问题，不要改代码。按严重程度排序，每条给出文件与行号。
```

---

## 7. 常见失败模式（写进提示词里预防）

| 失败 | 预防指令 |
|---|---|
| 一次性生成 200 个页面，质量崩 | 「先做 20 个垂直切片」 |
| 伪造 PDF/视频链接 | 「不确定就留官方入口」 |
| 把抓取结果和人工内容混在一起 | 「catalog 与 items 分离」 |
| 页面数量对不上 | 「check.py 硬校验数量」 |
| 排序靠感觉 | 「写 rubric 与锚点」 |
| 时间敏感信息过期 | 「checked_at + volatile」 |
| 关系图乱连 | 「每条边有 source/note」 |
| 移动端溢出 | 「390px 冒烟测试」 |
| 第三方资源当官方 | 「access/risk 标记」 |
| AI 只报告「完成了」 | 「每阶段报告数字」 |
