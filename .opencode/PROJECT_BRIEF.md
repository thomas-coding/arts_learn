# Project Brief - arts

## Purpose
- Maintain a measurable, command-driven art training workflow for zero-foundation learner `C001`, from Stage 1 fundamentals to project-ready baseline over the 24-month roadmap.

## Session Model (v2, token-optimized)
- Daily run mode is `new session`.
- Startup context uses only `.opencode/PROJECT_BRIEF.md` (long-term rules) and `.opencode/SESSION_STATE.md` (daily state).
- Startup read/intro is user-triggered; AI does not self-init full onboarding scans.
- Any other file is loaded only when the active task needs it.
- End-of-day updates are done by user command: always refresh `.opencode/SESSION_STATE.md`; update `.opencode/PROJECT_BRIEF.md` only when long-term rules change.

## Always-On Rules (must know every day)
- Command branch: `你学习下*` -> teacher line; `我来学习` -> student line.
- Lesson rhythm: 60-minute SOP (`demonstration -> guided practice -> timed independent task -> rubric feedback`).
- Gate rule: if total score or key dimension floor is unmet, do reinforcement first and do not advance.
- Inventory rule: keep `1 ready + 3 prepared`.
- Teacher line must pre-prepare scripts, sample outputs, and common fixes before student class to avoid in-class waiting.
- For zero-foundation learner, explain each new concept first (`what -> why -> how -> pass/fail check`) before practice starts.
- Student guidance must be step-by-step with explicit action order, time boxes, and quick checkpoints.
- Provide samples by default for new tasks; keep independent transfer checks free from sample-image dependency.
- Tooling blockers must be cleared quickly before core practice.

## Scope
- In scope: maintain teacher SOP/rubric/error library/run logs and student delivery/review/scoring/progression decisions.
- In scope: keep `knowledge_base/`, `homework/`, and `submissions/` synchronized with real teaching progress.
- Out of scope: non-SOP free-drawing coaching, skipping gates, unrelated non-art content, and AI replacing student final practice.

## Key Paths
- `.opencode/PROJECT_BRIEF.md`
- `.opencode/SESSION_STATE.md`
- `knowledge_base/teacher/`
- `knowledge_base/student/`
- `submissions/`
- `homework/`

## Done Criteria
- Teacher line done: notes updated, at least one lesson immediately teachable, inventory still `1 ready + 3 prepared`.
- Student class done: score recorded, pass/fail explicit, key errors mapped to executable fixes, next lesson condition clear.
- Daily ops done: related knowledge files synced and `.opencode/SESSION_STATE.md` updated with focus/progress/blockers/next first action.

## Response Rule
- Keep responses concise and actionable.
