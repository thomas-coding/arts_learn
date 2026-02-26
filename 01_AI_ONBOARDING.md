# AI入场指引（v2，按需加载）

此文件是补充说明。默认每日启动流程以 `.opencode/PROJECT_BRIEF.md` 与 `.opencode/SESSION_STATE.md` 为准。

## 默认流程（新）
1. 仅用 `.opencode/PROJECT_BRIEF.md` + `.opencode/SESSION_STATE.md` 建立最小上下文。
2. 启动阶段不主动全量读取知识库；根据当前任务再读取必要文件。
3. 执行中持续遵守口令分支、60分钟SOP、闸门规则与库存规则。
4. 日终由用户命令触发更新：常规更新 `.opencode/SESSION_STATE.md`；长期规则变化才更新 `.opencode/PROJECT_BRIEF.md`。

## 按需读取建议
- 教师线（`你学习下*`）: 优先读 `knowledge_base/teacher/teacher_kb.md` 与相关 `knowledge_base/teacher/lesson_*.md`。
- 学员线（`我来学习`）: 优先读 `knowledge_base/student/student_kb.md`、`knowledge_base/student/class_C001_review.md` 与当次 `submissions/` 文件。
- 协议争议或规则变更: 再读 `00_PROJECT_CHARTER.md` 作为历史协商参考。

## 必守规则（简版）
- 不改为固定排课，保持口令驱动。
- 不跳过前置与闸门，未达标先补强。
- 教师线保持 `1 ready + 3 prepared` 库存。
- 学员线按60分钟SOP执行并记录评分结论。
