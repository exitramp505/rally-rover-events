# Rally Rover — agent coordination protocol

**Purpose:** Shared, auditable, asynchronous work handoff between **Grok Bot** and **ChatGPT** through GitHub, without inventing a direct always-on chat connection.

## Communications channel
- **GitHub Issues** in `exitramp505/rally-rover-events` serve as the inbox and conversation log. Start with the issue titled **"Agent handoff: Grok Bot ↔ ChatGPT"**.
- Any agent that can read and comment on Issues can send a message by adding a comment to the handoff issue, or open a dedicated issue for a substantial task. Reference specific commit SHAs, pull requests, paths, or issue numbers.
- Each agent MUST explicitly check issues when instructed/configured to do so. **Posting a message does not automatically wake the other agent.** ChatGPT here does not independently monitor GitHub between conversations unless a separate scheduled workflow is configured.
- For ongoing technical work, use an individual issue per requested change. Use a pull request for code changes needing review; avoid two agents overwriting the same file at once.
- The files `docs/DECISIONS.md`, `docs/OPERATIONS.md`, `docs/STATUS.md`, and `docs/QC_LOG.md` remain the durable source of truth. Issues contain discussion/handoffs; accepted decisions belong in these files.

## Message template
```text
FROM: Grok Bot | ChatGPT
TO: ChatGPT | Grok Bot
TYPE: HANDOFF | QUESTION | REVIEW | UPDATE
STATUS: OPEN | BLOCKED | DONE
CONTEXT: <relevant issue/commit/path and verified facts>
REQUEST: <specific action or answer needed>
RESULT: <what has been done, where it can be verified>
```

## Scope and operating rules
1. The owner personally handles **all organizer contact, correspondence, relationships, and follow-ups**. Neither AI creates organizer reminders, outreach lists, drafts, messages, or tracking tasks. Do not ask the other agent to do so.
2. AI scope: event discovery from permitted public sources, fact-checking, independent fan guides, original merchandise content/design, site publishing, QC, monitoring technical functionality, and reporting.
3. Do not write credentials, private contacts, subscriber emails, purchase details, or other personal data into public GitHub issues or commits. Coordinate only with non-sensitive references.
4. Make no claim that an agent completed a task unless its result can be verified (repo commit, successful deployment, public page, or explicit tool response). Identify blockers and distinguish proposals from live changes.
5. Use the same base branch and check the newest status/commits before modifying files. GitHub code is the source of truth.
6. This site is independently produced; interest forms are **not official tickets or organizer registrations**.

## Current starting point — 2026-10-18
- GitHub project contains three static event guides and links to Printful Quick Stores.
- A Netlify project named `rally-rover-events` has been created. The GitHub connection and first production deployment require confirmation.
- Grok Bot should check `docs/STATUS.md` for current work and acknowledge this channel with a comment on the handoff issue once it has been instructed to monitor/use it.
- ChatGPT can read and respond to the handoff issue during the user's conversations; no automatic unsolicited response is implied.
