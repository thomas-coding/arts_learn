# AI入场指引（防漂移）

此文件用于新AI在context缺失时快速恢复项目上下文。

## 入场步骤
1. 先读取 `00_PROJECT_CHARTER.md`（最高优先级）。
2. 再读取教师知识库 `knowledge_base/teacher/teacher_kb.md`。
3. 再读取学员知识库 `knowledge_base/student/student_kb.md`。
4. 再读取术语卡 `knowledge_base/shared/beginner_terms_card.md`（用于0基础解释一致）。
5. 根据用户当前口令决定运行分支:
   - "你学习下" -> 教师线。
   - "我来学习" -> 学员线。

## 必守规则
- 不要强行改成固定排课周期。
- 学员线开课前，教师线准备必须已完成。
- 教师线每次要有"1节可上 + 额外3节预备"库存。
- 每次执行后同步更新双知识库。

## 响应准则
- 若用户发"你学习下": 输出教师线学习与备课成果，并更新知识库。
- 若用户发"我来学习": 直接开1节60分钟课（step-by-step），课后给练习和验收。
- 若用户提出改协议: 先确认变更点，再更新 `00_PROJECT_CHARTER.md` 的版本记录。
