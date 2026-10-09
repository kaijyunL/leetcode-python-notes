# Agent / LLM 面经项目候选清单

> **用途**：为“主面 Agent 岗位、次面 LLM 岗位”筛选公开的面经项目和面试资料库。
>
> **数据快照**：2026-10-08。Star、创建时间和最近更新时间来自 GitHub 公开仓库元数据；它们会变化，仅用于辅助判断项目成熟度和社区验证程度。
>
> **重要说明**：下面的项目性质不同，不能把真实面经、二次整理的题库、教程和抓取工具混为一谈。Star 不能替代面经真实性，但完全忽略创建时间、更新时间和 Star 也不严谨。

## 一、候选项目总览

| 项目 | 创建时间 | 最近更新 | Star | 类型 | Agent/LLM 匹配度 | 判断 |
|---|---:|---:|---:|---|---|---|
| [AIGC-Interview-Book](https://github.com/WeThinkIn/AIGC-Interview-Book) | 2023-10 | 2026-10 | 4,908 | AI 面试书/知识库 | Agent 强，LLM 很强 | 成熟度最高的综合资料库之一，但不是纯真实面经库 |
| [AgentGuide](https://github.com/adongwanai/AgentGuide) | 2025-11 | 2026-09 | 10,507 | Agent 求职知识库 | Agent 很强，LLM 强 | Star 和岗位导向突出，但内容混合了教程、题库和项目 |
| [kaomian](https://github.com/smile-struggler/kaomian) | 2026-04 | 2026-10 | 96 | 面经数据化聚合 | Agent 很强，LLM 强 | 项目很新且 Star 很低；目前只能确认有 README 和 `题库/` 目录，实质内容和来源仍待核验 |
| [面试鸭](https://github.com/liyupi/mianshiya) | 未核实 | 2026-02 | 5,939 | 大型面试题库网站 | Agent/LLM 中等 | 社区验证和题库规模较好，但不能当作纯面经库 |
| [AI-Job-Notes](https://github.com/amusi/AI-Job-Notes) | 未核实 | 2025-06 | 6,170 | AI 算法求职资料库 | Agent 弱，LLM 强 | 成熟的 AI 算法补充资料，Agent 工程相关性不足 |
| [AI Engineering Interview Questions](https://github.com/amitshekhariitbhu/ai-engineering-interview-questions) | 2026-03 | 2026-10 | 3,316 | 英文 AI 工程题库 | Agent 强，LLM 强 | 社区增长快，适合补英文 AI Engineering，但不是国内面经 |
| [agent-interview-hub](https://github.com/Zchary1106/agent-interview-hub) | 2026 | 2026 | 未核实 | Agent 面试题库 | Agent 强，LLM 强 | 结构清晰，但项目较新，成熟度和原始面经比例需要继续核验 |
| [AIGC_Interview](https://github.com/EmbraceAGI/AIGC_Interview) | 未核实 | 2026-08 | 824 | AIGC 面经链接整理 | Agent 中等，LLM 强 | 原始面经外链价值较高，但内容分散且部分资料偏旧 |
| [ai-agents-from-zero](https://github.com/didilili/ai-agents-from-zero) | 未核实 | 2026-09 | 5,094 | Agent 教程 + 题库 | Agent 强，LLM 强 | 适合系统学习，但主体不是面经数据库 |
| [面灵面经](https://github.com/wearzdk/interview-experience) | 2026-03 | 2026-10 | 11 | 自动采集面经平台 | Agent/LLM 中等 | 更新很新，但样本规模和长期质量尚未验证 |
| [interview_experience](https://github.com/0voice/interview_experience) | 2021-06 | 2024-05 | 434 | 传统互联网面经合集 | Agent/LLM 弱 | 真实面经属性较强，但对当前方向较旧 |
| [Daily-Question](https://github.com/shfshanyue/Daily-Question) | 2019-11 | 2026-06 | 5,146 | 通用面试题和面经资源 | Agent/LLM 弱 | 社区成熟、资料广，但不是专项资料库 |
| [interview-experience-spider](https://github.com/bcefghj/interview-experience-spider) | 2026-05 | 2026-05 | 44 | 面经抓取工具 | 取决于自己抓取 | 可抓最新数据，但需要自己部署和清洗 |

## 二、按“真实面经程度”分类

### 1. 更接近真实面经的项目

- [kaomian](https://github.com/smile-struggler/kaomian)
- [面灵面经](https://github.com/wearzdk/interview-experience)
- [AIGC_Interview](https://github.com/EmbraceAGI/AIGC_Interview)
- [interview_experience](https://github.com/0voice/interview_experience)

`kaomian` 的 README 声称包含公司、岗位和题型线索，也列出了类似下面的记录：

- 京东 AI Agent 实习：二叉树层序遍历
- 快手 AI Agent 研发实习：岛屿数量
- 字节大模型 Agent：三数之和、连续子数组最大和
- 阿里淘天 AI 搜：树的最大路径和
- 腾讯大模型算法：第 K 大、数组找重复
- 抖音推荐算法：多头注意力、交叉熵

但这些内容目前不能仅凭 README 视为已验证的真实面经。需要继续检查 `题库/` 下是否有可直接阅读的原始内容、来源链接、面试时间和去重规则。因此，`kaomian` 暂时只能作为待核验候选，不能因为题目数量多就排在成熟项目之前。

### 2. 面经与高频题结合的结构化知识库

- [AgentGuide](https://github.com/adongwanai/AgentGuide)
- [AIGC-Interview-Book](https://github.com/WeThinkIn/AIGC-Interview-Book)
- [agent-interview-hub](https://github.com/Zchary1106/agent-interview-hub)

这类项目适合建立知识框架和查漏补缺，但不能把其中的所有题目都理解为某次真实面试中出现过的问题。

### 3. 大型通用面试题库

- [面试鸭](https://github.com/liyupi/mianshiya)
- [Daily-Question](https://github.com/shfshanyue/Daily-Question)
- [AI-Job-Notes](https://github.com/amusi/AI-Job-Notes)
- [AI Engineering Interview Questions](https://github.com/amitshekhariitbhu/ai-engineering-interview-questions)

这类项目适合补算法、基础知识、LLM 原理和通用 AI Engineering 内容，但不适合作为唯一的真实面经来源。

### 4. 面经抓取工具

- [interview-experience-spider](https://github.com/bcefghj/interview-experience-spider)

它更适合希望自己抓取最新牛客、小红书资料的人。使用成本更高，抓到内容之后仍然需要自己做清洗、去重和真实性判断。

## 三、按准备目标筛选

### 主攻 Agent 岗位

1. [AgentGuide](https://github.com/adongwanai/AgentGuide)：用来建立 Agent 岗位的完整准备框架，Star、Fork 和持续更新都提供了较强社区信号。
2. [AIGC-Interview-Book](https://github.com/WeThinkIn/AIGC-Interview-Book)：补齐 Agent、LLM、深度学习和求职知识体系，项目创建早且持续更新。
3. [agent-interview-hub](https://github.com/Zchary1106/agent-interview-hub)：按 Agent、RAG、MCP、Tool Calling 和系统设计查漏补缺，但先核验内容来源。
4. [kaomian](https://github.com/smile-struggler/kaomian)：只作为近期面经线索候选，先检查 `题库/` 的实质内容，再决定是否纳入主资料库。

### 次攻 LLM 岗位

1. [AIGC-Interview-Book](https://github.com/WeThinkIn/AIGC-Interview-Book)：创建早、持续更新，Agent 和 LLM 覆盖最均衡。
2. [AI-Job-Notes](https://github.com/amusi/AI-Job-Notes)：补深度学习、NLP、AIGC 和模型算法基础。
3. [AI Engineering Interview Questions](https://github.com/amitshekhariitbhu/ai-engineering-interview-questions)：补 RAG、Agent、LLMOps、评估和 Safety，注意它是英文资料。
4. [AIGC_Interview](https://github.com/EmbraceAGI/AIGC_Interview)：回看大模型岗位面经原文或外链。

### 补通用算法和基础

- [面试鸭](https://github.com/liyupi/mianshiya)
- [Daily-Question](https://github.com/shfshanyue/Daily-Question)
- [interview_experience](https://github.com/0voice/interview_experience)

## 四、重新排序后的结论

按“内容是否实质、项目成熟度、社区验证和岗位匹配度”排序，而不是只按 README 宣称的题目数量，建议优先比较下面五个：

1. `AgentGuide`：Agent 岗位准备价值第一，且 Star、Fork 和持续更新都提供了较强社区信号。
2. `AIGC-Interview-Book`：综合成熟度和 LLM 覆盖第一，适合作为系统知识库。
3. `面试鸭`：社区验证和题库规模较好，作为通用算法、基础和大厂高频题补充。
4. `agent-interview-hub`：方向匹配，但项目较新，需先核验面经来源和实际内容。
5. `kaomian`：只保留为待核验候选，不能根据 README 的统计数字直接排高。

如果按不同用途各选一个：

1. 看真实面试：先比较 `AIGC_Interview` 的原始面经外链和 `kaomian` 的实际题库内容。
2. 准备 Agent 岗位：选 `AgentGuide`。
3. 兼顾 Agent 和 LLM：选 `AIGC-Interview-Book`。

如果必须只选一个作为主资料库，我会选 `AgentGuide`，再用 `AIGC-Interview-Book` 补 LLM，用经过核验的原始面经校准真实问题。`kaomian` 在实际内容核验完成前，不应作为主资料库，也不应排在高 Star、长期维护的项目之前。

## 五、选择时的检查标准

打开项目后，重点检查以下内容：

- 是否标注真实公司和具体岗位，而不是只写“高频题”。
- 是否注明面试时间，能否反映当前招聘要求。
- 是否保留原始帖子或文章链接，内容能否回溯。
- 是否区分 Agent 工程岗、LLM 应用岗和 LLM 算法岗。
- 是否包含项目深挖、系统设计、RAG、Tool Calling、MCP、评估和部署问题。
- 是否区分真实面经、作者整理题和教程内容。
- 是否有明显重复、营销性描述或无法验证的题目数量。

最终判断时，不要只看 GitHub Star。对当前目标来说，公司/岗位线索、资料时效性、原始来源和 Agent/LLM 的岗位匹配度更重要。
