---
name: tonghua-skill
description: 童话短篇小说创作技能包。执行大纲、人物、目录、章节的专业创作，基于童话创作法则和诗意优美的写作风格生成高质量小说内容。
---

# 童话小说创作 Skill

[技能说明]
    专业的童话短篇小说创作技能包，覆盖故事构思、人物塑造、章节规划、正文写作全流程。根据不同创作阶段，读取对应的创作资源并生成符合童话规范的小说内容。

[文件结构]
    .claude/skills/tonghua-skill/
    ├── SKILL.md                        # 本文件（技能包核心配置）
    ├── outline-method.md               # 大纲创作方法论（含人物塑造指导）
    ├── output-style.md                # 写作风格（含章节创作方法）
    ├── examples/
    │   ├── outline-example.md          # 大纲示例
    │   ├── character-example.md        # 人物示例
    │   └── chapter-example.md          # 章节示例
    └── templates/                      # 文档结构模板（通用）
        ├── outline-template.md         # 大纲文档格式模板
        ├── character-template.md       # 人物小传格式模板
        ├── chapter-index-template.md   # 章节目录格式模板
        └── chapter-template.md         # 章节正文格式模板

[核心能力]
    - **创作阶段理解**：识别当前处于大纲、人物、目录还是章节创作阶段
    - **资源整合**：读取模板、方法论、风格、示例等多维度资源
    - **专业创作**：基于资源和上下文创作符合童话规范的小说内容
    - **风格把控**：确保创作内容符合童话的诗意优美写作风格
    - **模板遵循**：严格按照模板格式生成文档结构
    - **上下文理解**：理解已有文档内容，确保创作连贯性

[执行流程]
    第一步：理解创作需求
        识别当前创作阶段：
        - 如果在讨论故事大纲或outline.md不存在 → 大纲创作阶段
        - 如果在讨论人物或刚执行/character → 人物创作阶段
        - 如果在讨论章节规划或刚执行/catalog → 目录创作阶段
        - 如果在创作章节正文或刚执行/write → 章节创作阶段

    第二步：读取创作资源
        **大纲创作阶段**：
            1. 读取 templates/outline-template.md（文档格式模板）
            2. 读取 outline-method.md（童话大纲创作方法论，含人物塑造指导）
            3. 读取 output-style.md（童话写作风格）
            4. 读取 examples/outline-example.md（童话大纲示例）
            5. 从对话历史获取用户回答的Q1-Q3（核心创意、核心冲突、故事调性）

        **人物创作阶段**：
            1. 读取 outline.md（了解故事背景和设定）
            2. 读取 templates/character-template.md（文档格式模板）
            3. 读取 outline-method.md（童话人物塑造指导部分）
            4. 读取 output-style.md（童话写作风格）
            5. 读取 examples/character-example.md（童话人物示例）

        **目录创作阶段**：
            1. 读取 outline.md 和 character.md（了解故事和人物）
            2. 读取 templates/chapter-index-template.md（文档格式模板）
            3. 读取 outline-method.md（童话章节规划方法）
            4. 读取 output-style.md（童话写作风格）

        **章节创作阶段**：
            1. 读取 outline.md、character.md、chapter_index.md（全部上下文）
            2. 读取 templates/chapter-template.md（文档格式模板）
            3. 读取 output-style.md（童话写作风格和章节创作方法，最重要）
            4. 读取 examples/chapter-example.md（童话章节示例）
            5. 从chapter_index.md获取当前章节的规划内容

    第三步：执行专业创作
        **大纲创作**：
            基于用户提供的信息（核心创意、核心冲突、故事调性）和读取的资源：
            - 严格按照 templates/outline-template.md 的格式结构
            - 遵循 outline-method.md 的童话创作方法论
            - 应用 output-style.md 的诗意优美写作风格
            - 参考 examples/outline-example.md 的示例
            - 生成包含以下内容的完整大纲：
                • 小说信息（书名、类型：童话、故事调性）
                • 核心梗概（一句话）
                • 导语（150-200字，包含奇幻元素和情感钩子）
                • 故事大纲（采用起承转合结构，2000-3000字）
                • 主要人物（简要列出3-5个核心人物）

        **人物创作**：
            基于outline.md的故事设定和读取的资源：
            - 严格按照 templates/character-template.md 的格式结构
            - 遵循 outline-method.md 中的童话人物塑造指导
            - 应用 output-style.md 的诗意优美写作风格
            - 参考 examples/character-example.md 的示例
            - 生成包含以下内容的人物小传：
                • 主要角色（3-5个，详细描述，强调性格特点和成长轨迹）
                • 反派角色（如有）
                • 重要配角（如有）
                • 其他角色（如有）
            - 确保人物形象鲜明，具有童话特质

        **目录创作**：
            基于outline.md和character.md的设定和读取的资源：
            - 严格按照 templates/chapter-index-template.md 的格式结构
            - 遵循 outline-method.md 的童话章节规划方法
            - 应用 output-style.md 的写作风格
            - 生成固定5章的章节目录，与大纲的起承转合结构对应
            - 每章包含：章节标题 + 一句话剧情简介（体现奇幻元素和成长主题）
            - 确保起承转合布局合理，故事节奏流畅

        **章节创作**：
            基于全部上下文文档和读取的资源：
            - 严格按照 templates/chapter-template.md 的格式结构
            - 严格遵循 output-style.md 的诗意优美写作风格和章节创作方法（最重要）
            - 参考 examples/chapter-example.md 的示例
            - 基于 chapter_index.md 中该章节的规划进行创作
            - 生成2000-3000字的章节正文

    第四步：返回创作成果
        **大纲创作阶段**：
            返回符合templates/outline-template.md格式的完整大纲内容

        **人物创作阶段**：
            返回符合templates/character-template.md格式的完整人物小传

        **目录创作阶段**：
            返回符合templates/chapter-index-template.md格式的完整章节目录

        **章节创作阶段**：
            返回符合templates/chapter-template.md格式的完整章节正文

[创作原则]
    - **模板遵循原则**：
        • 创作的所有文档必须严格遵循templates/中定义的格式
        • 不能遗漏模板中的必要标题和段落
        • 不能改变模板定义的层级结构
        • 可以根据实际需要调整内容的详略

    - **风格一致性原则**：
        • 所有创作必须保持童话的诗意优美风格统一
        • 严格遵循output-style.md中定义的写作风格
        • 参考examples/中的示例风格
        • 确保大纲、人物、章节的风格协调

    - **上下文连贯性原则**：
        • character创作必须基于outline
        • catalog创作必须基于outline + character
        • chapter创作必须基于outline + character + catalog
        • 确保前后内容不矛盾，逻辑连贯

    - **质量标准原则**：
        • 大纲：奇幻元素丰富，主题积极向上，故事结构完整，固定起承转合结构，2000-3000字
        • 人物：形象鲜明，具有童话特质，与故事匹配
        • 目录：固定5章，与大纲的起承转合结构对应，布局合理，节奏流畅
        • 章节：2000-3000字，风格统一，富有诗意，推进剧情

[注意事项]
    - 确保每个阶段的必需资源都已读取完整
    - 不仅读取文档内容，还要深入理解其含义
    - output-style.md中的诗意优美风格要求是强约束，必须严格遵守
    - templates/中的格式是必须遵循的，任何偏离都可能导致问题
    - 短篇小说固定为5章结构，采用起承转合布局
    - 创作内容必须完整、连贯、符合童话特点
    - 始终使用中文创作
