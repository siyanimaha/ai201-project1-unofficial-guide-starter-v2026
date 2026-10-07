# The Unofficial Guide

Siyani Mahadevan — Corpus: campus_life

## What This Does

The Unofficial Guide is a RAG system that answers questions using student-written campus life documents. I used the campus_life corpus, which contains information about dining, housing, courses, and campus procedures. The system retrieves relevant documents and uses them to produce grounded answers. It also uses a relevance gate to avoid answering questions when the documents do not contain enough information.

## Chunking Strategy

The campus_life corpus contains 88 documents with 27,908 total characters. The starter produced 88 chunks with an average length of 317 characters, a shortest chunk of 178 characters, and a longest chunk of 549 characters.

I attempted to replace the starter chunker with my own strategy, but my implementation caused syntax and formatting errors. I restored the starter chunker so the pipeline would remain functional. The current function is `chunker.py::fallback_split`. For this corpus, keeping the short student posts together works reasonably well because most posts contain one focused topic and can stand on their own.

## Sample Chunks

### Chunk 1
Source: `admin_add_drop_deadline.txt#0`
Function: `chunker.py::fallback_split`

On the add/drop deadline

You can add a course through the end of the second week. Dropping is a longer window — through the end of week six — but a drop after week two shows as a W on your transcript. Nothing anywhere on the registrar's site says this plainly, and students find out from each other.

### Chunk 2
Source: `course_biol_160.txt#0`
Function: `chunker.py::fallback_split`

BIOL 160 Cell Biology

I lived here my sophomore year. Format is lecture three times a week with a weekly lab. Assessment: four unit tests and a cumulative final. Not curved.

Expect 9 to 11 hours a week, the heaviest first-year course by reputation.

The one piece of advice: the unit tests come fast, roughly every three weeks; falling behind once is very hard to recover from.

### Chunk 3
Source: `course_hist_118_workload.txt#0`
Function: `chunker.py::fallback_split`

Workload for HIST 118 Modern World History

People keep asking so: a lot of reading, about 120 pages a week, but no problem sets. That's real time, not optimistic time.

It's front-loaded — the first month is heavier than the rest, partly because you're learning the format.

### Chunk 4
Source: `dining_pellew_dining_hall_followup.txt#0`
Function: `chunker.py::fallback_split`

Re: Pellew Dining Hall

Adding to what people have said about Pellew Dining Hall. The wait figure of 12 to 18 minutes at peak matches what I've seen. If you're trying to eat between classes, go before 11:45 and it's a different building entirely.

Also worth saying: the furthest hall from anywhere, next to the athletics centre. Nobody tells you this at orientation.

### Chunk 5
Source: `housing_innisfree_hall.txt#0`
Function: `chunker.py::fallback_split`

Innisfree Hall — what it's actually like

Transferred in last year, so take this with a grain of salt. Built 1991, renovated 2022. Rooms are doubles arranged as pairs sharing one bathroom between two rooms.

The good: the shared-bathroom-between-two-rooms arrangement is the best compromise on campus.

The bad: no air conditioning, which matters for the first three weeks of September.

Laundry costs $1.75 wash, $1.75 dry, app-based. On noise: moderate; the building is L-shaped and the short wing is much quieter.

## Sample Answer

**Question:** What food is worth getting at Verrill Street Grill?

**Answer:** The food worth going for at Verrill Street Grill is the burger, which is the only late-night hot food on campus.

**Source:** `dining_verrill_street_grill.txt`

**Relevance cutoff:** 0.6

I kept the cutoff at 0.6 because the five in-corpus questions had best distances from 0.172 to 0.449, while the five out-of-scope questions had best distances from 0.807 to 0.899. There is a clear gap between the two groups, and 0.6 falls inside that gap.

| Question | In corpus? | Best distance |
|---|---|---:|
| What food is worth getting at Verrill Street Grill? | Yes | 0.449 |
| How long can the wait be at Verrill Street Grill on Friday evenings? | Yes | 0.172 |
| When is the best time to eat at North Kitchen between classes? | Yes | 0.267 |
| What food is worth getting at Halden Hall? | Yes | 0.391 |
| What time does Halden Hall close? | Yes | 0.323 |
| Who won the 2018 FIFA World Cup? | No | 0.879 |
| What is the boiling point of mercury? | No | 0.807 |
| How do I replace the alternator in a 2014 Honda Civic? | No | 0.899 |
| What is the capital of Burkina Faso? | No | 0.859 |
| How many moons does Neptune have? | No | 0.835 |

## How I Used AI

**1.** I used AI to help debug my project environment after the test showed that my Python version was too old. I installed Python 3.11, recreated the virtual environment, reinstalled the requirements, and reran the test until all 10 checks passed.

**2.** I used AI while attempting to replace the starter chunker. My first attempt caused indentation and triple-quoted-string syntax errors. I restored the starter implementation instead of leaving the project broken and documented why I kept `chunker.py::fallback_split`.

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->
| Criterion | Target | Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Verdict |
|---|---|---|---|---|---|---|---|
| 1. Retrieved chunks contain the answer | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 2. Every answer names a source | Every answer | 5 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 3. Out-of-scope questions are refused | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 4. Chunk sizes stay appropriate | At least 80% | 100% | 100% | 100% | 100% | 100% | MET |
| 5. Answers use retrieved information | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunks contain the answer | MET | All 5 test questions retrieved chunks containing the expected information. |
| 2 | Every answer names a source | MET | The generated answers named at least one source document. |
| 3 | Out-of-scope questions are refused | MET | The relevance gate refused all 5 out-of-scope questions. |
| 4 | Chunk sizes stay appropriate | MET | All 88 chunks were between 150 and 600 characters, which is 100%. |
| 5 | Answers use retrieved information | MET | All 5 test questions included the expected fact in the generated answers across the evaluation runs. |
## DiagnosesAll five criteria were met in the before evaluation, so I did not find a failed stage in the pipeline to diagnose. The results were consistent across the five runs, and all five test questions returned the expected information.

Since none of the criteria were missed, I would tighten Criterion 1. Instead of requiring the correct information to be retrieved for at least 4 of 5 questions, I would require 5 of 5. The system already reached 5 of 5 in this evaluation, so this would be a stronger target for future testing.

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

## The Improvement

**What I changed:** I added a 5-second delay between evaluation runs in run_eval.py. When I first tried to run five trials for each question, the evaluation hit the Gemini API rate limit and stopped with a 429 RESOURCE_EXHAUSTED error. Adding the delay allowed the full evaluation to finish without exceeding the request limit.

**Why I picked it:** All five of my quality criteria were already met, but the evaluation process itself was not reliable because it could stop before completing all five runs. I chose this improvement so the full evaluation could run successfully and produce complete evidence.

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Verdict |
|---|---|---|---|---|---|---|---|
| 1. Retrieved chunks contain the answer | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 2. Every answer names a source | Every answer | 5 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 3. Out-of-scope questions are refused | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 4. Chunk sizes stay appropriate | At least 80% | 100% | 100% | 100% | 100% | 100% | MET |
| 5. Answers use retrieved information | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |

**Did it help?**
Yes. The 5-second delay made the evaluation more reliable. Before adding the delay, the five-run evaluation stopped because the Gemini API returned a 429 RESOURCE_EXHAUSTED rate-limit error. After adding the delay, the evaluation completed all 25 model calls and produced the full after-run results. The quality results stayed consistent, with all five criteria still met.

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->
## MCP Tool

I moved the campus guide search capability into an MCP tool named `search_listings` in `mcp_server.py`. The tool accepts a question, top-k value, and optional corpus, then uses the existing search system and returns the matching text, source, label, and distance.

I tested the MCP connection with `mcp_client.py`. The client successfully discovered the `search_listings` tool and called it with the question "Where can I study on campus?" The tool returned structured search results without an error.

## Agent Loop Trace

I added tracing so I could see what happened during each step of the pipeline. For the question "How much does laundry cost in Aldridge Hall?" the trace showed:

- Search found 3 results.
- The relevance gate passed with a best distance of 0.247 and a cutoff of 0.6.
- The model was called using the 3 retrieved chunks.
- The final answer said that laundry costs $1.75 for a wash and $1.50 for a dry.

This trace helped me see the path from retrieval to the relevance gate and then to generation.

Actual trace output:

```text
[TRACE] MCP tool call: search_listings
[TRACE] gate
[TRACE] model
[TRACE] model_result
```

This trace was produced by `app.py::ask_pipeline` using the `--trace` option. It shows the MCP `search_listings` tool call followed by the relevance gate and model generation steps in order.
## What's Still Broken
All five criteria were still met after the improvement, so there were no failed criteria left to fix. One limitation is that the evaluation only uses five test questions from the campus_life corpus. A larger and more varied set of questions would provide stronger evidence that the system works consistently. I stopped here because the current evaluation met all five targets and completed successfully.
<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently
If I did this again, I would use a larger and more varied test set instead of only five questions. I would also make Criterion 1 stricter by requiring the correct information to be retrieved for 5 out of 5 questions instead of 4 out of 5. This would make the evaluation stronger and give me more confidence that the system works consistently.
<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
