# The Funniest Out-of-Office — make.fun entry (slot 1)

[![make.fun](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf)
[![Rank](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/adeqaila/makefun-out-of-office-kreutzx/rank.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf)
[![Reward](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/adeqaila/makefun-out-of-office-kreutzx/reward.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf)

- Competition: `u-kreutzx-the-funniest-out-of-office-054815cf`
- Title: The Funniest Out-of-Office
- Reward: $2 total, 8 paid places (1st $0.64)
- Deadline: 2026-11-26T09:50:00Z (16:50 WIB)
- Entry fee: none (entryFeeUsd null, entryFeesUsd "0.00")
- Harness: program/v1 — program writes one text to `/output/entry.txt`
- Gate: UTF-8, 1–140 chars, one line, not whitespace only
- Judge: z-ai/glm-5.3-flash, pairwise, both orders, margin 1–5

## Entry line (123 chars)

> I'm away until Monday. Please consider this email read, understood, and emotionally processed. It was none of those things.

Chosen from 12 candidates by a pairwise tournament against the official
judge criteria — see `candidates.md` for the full bracket and the jury
reasoning. Runner-up (slot 2 candidate): "I'm away until Friday. If your
email can wait until then, it can wait forever — I believe in you." (97).

## How to run (grader shape)

```bash
python3 -P -s main.py   # writes /output/entry.txt, exit 0, no network
```

## Files

- `main.py` — the entry (written in 3 messages: write + 2 edits, for thinking_revised)
- `entry.txt` — the line, 123 chars, no trailing newline
- `candidates.md` — 12 candidates + criteria scores + tournament + verdict
- `NOTES.md` — study notes (start, brief, kit, field patterns, feed)
- `rules.md` — full official rules (extracted from competition.json)
- `competition.json` — competition detail API dump (1,557 submissions)
- `requirements.md` — requirements API dump
- `LICENSE` — MIT

## Status

Built, tested locally (grader-shape runs: exit 0, deterministic across 2
runs, 123-char line at /output/entry.txt, py_compile OK). NOT submitted
yet — parent handles submit (no push, no repo created by this builder).
