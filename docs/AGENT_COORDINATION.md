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

## Event-based Grok notifications (requested, not yet confirmed)
- **Goal**: When ChatGPT posts a new comment in shared **Issue #1** addressed `TO: Grok Bot` with `FROM: ChatGPT`, Grok Bot should be notified, read that comment, and either acknowledge it or act if authorized.
- **Preferred setup**: In the owning Grok Bot's **Routines**, create an event-triggered routine using the **GitHub notification account integration**, restricted to this repository and Issue #1. xAI's Grok Bot documentation says GitHub notifications can trigger routines where supported; the integration may require an additional account connection. Filter by both FROM/TO markers to avoid unrelated activity, and deduplicate based on comment ID. Ignore Grok's own comments and avoid loops.
- **Verification**: After linking the integration, publish exactly one non-sensitive test comment using the defined header, check Grok's routine history, and respond with the result on Issue #1. Mere GitHub issue creation or comment posting does **not** prove the routine fired.
- **Fallback**: Enable GitHub issue notifications (including the owner's own updates where required) and configure an incoming-email trigger if available in the Grok environment, or set up a low-frequency routine to check Issue #1 for the last unseen comment. Note that fallback polling consumes Grok usage when run. Do not add GitHub webhooks or API secrets to a public issue.
- Grok's supported routines run when triggered, not necessarily for every page edit; use comments to Issue #1 for messages, other issues for substantial tasks. Keep the volume low to conserve credits.

## Current starting point — 2026-10-18
- GitHub project contains three static event guides and links to Printful Quick Stores, which remain transitional until Fourthwall migration is verified.
- Netlify is connected and has produced a ready production deploy at https://rally-rover-events.netlify.app/ ; GitHub Pages is the demo/test site. A commit marker `[publish-netlify]` gates intentional Netlify releases; verify skip behavior.
- Owner approved migration to Fourthwall; Grok's task list is in Issue #3 (https://github.com/exitramp505/rally-rover-events/issues/3). Account setup and product integration are not yet verified.
- Grok Bot should check `docs/STATUS.md` for current work and acknowledge this channel with a comment on this issue. No always-on notification is active until tested.
- ChatGPT can read and respond to the handoff issue during the user's conversations; no automatic unsolicited response is implied.
