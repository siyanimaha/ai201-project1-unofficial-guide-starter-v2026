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

## Run Log — Before

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | N/A | N/A | N/A | Not evaluated |
| 2. Every answer names a source | 5 of 5 | N/A | N/A | N/A | Not evaluated |
| 3. Gate stops out-of-corpus questions | 4 of 5 | N/A | N/A | N/A | Not evaluated |
| 4. Chunks are between 150 and 600 characters | 80% | 100% | 100% | 100% | MET |
| 5. Answers use retrieved information | 4 of 5 | N/A | N/A | N/A | Not evaluated |

The corpus loaded 88 documents and produced 88 chunks using
`chunker.py::fallback_split`. The shortest chunk was 178 characters and the
longest was 549 characters. Therefore, all 88 chunks were within my target
range of 150 to 600 characters.

I attempted to run `python run_eval.py --label before`, but the generation
stage repeatedly returned `503 UNAVAILABLE` from the Gemini API because the
model was experiencing high demand. I also tried an available Gemini model.
It worked for a simple API request, but the evaluation later returned
`429 RESOURCE_EXHAUSTED` after the free-tier request quota was reached.

Because the evaluation stopped before completing, no evaluation files were
written to `results/`. I marked the criteria that require completed generated
answers as not evaluated instead of inventing results.

## Verdicts

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunk contains the answer | Not evaluated | The generation-dependent evaluation did not complete, so I did not have three real runs to compare with the 4-of-5 target. |
| 2 | Every answer names a source | Not evaluated | The API failure prevented the required answer runs from completing. |
| 3 | Gate stops out-of-corpus questions | Not evaluated | I did not receive a completed evaluation file containing the required gate results. |
| 4 | Chunks are between 150 and 600 characters | MET | All 88 chunks were between 178 and 549 characters, so 100% met the 150–600 character requirement, exceeding my 80% target. |
| 5 | Answers use retrieved information | Not evaluated | The generated-answer evaluation did not complete, so I could not honestly compare the answers with the expected facts. |

## Diagnoses

The loading, chunking, embedding, and vector-store stages completed
successfully. The corpus loaded 88 documents and produced 88 chunks, and the
embedding model and vector store passed their setup checks.

The blocker occurred at the generation stage. Gemini repeatedly returned
`503 UNAVAILABLE` because of high demand. After I found a model that could
successfully answer a simple request, repeated evaluation attempts eventually
returned `429 RESOURCE_EXHAUSTED` because the free-tier request quota was
reached.

This means I do not have enough completed evaluation output to claim that a
specific question failed because of chunking, embedding, or retrieval. The
chunk-size criterion is the one criterion I could verify independently: all
88 chunks were between 178 and 549 characters.

## The Improvement

**What I changed:**

I tested another Gemini model available to my API key after the original
model repeatedly returned 503 errors. I kept the corpus, chunking strategy,
embeddings, and retrieval pipeline unchanged because I did not have a
completed baseline evaluation showing that one of those stages was causing
the problem.

**Why I picked it:**

My diagnosis showed that the immediate failure occurred during generation,
not during loading, chunking, or embedding. Changing the model configuration
was therefore the most directly related troubleshooting step I could test
without making an unsupported change to the RAG pipeline.

### Run Log — After

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | N/A | N/A | N/A | Not evaluated |
| 2. Every answer names a source | 5 of 5 | N/A | N/A | N/A | Not evaluated |
| 3. Gate stops out-of-corpus questions | 4 of 5 | N/A | N/A | N/A | Not evaluated |
| 4. Chunks are between 150 and 600 characters | 80% | 100% | 100% | 100% | MET |
| 5. Answers use retrieved information | 4 of 5 | N/A | N/A | N/A | Not evaluated |

**Did it help?**

The model change helped partially because I was able to successfully make a
simple generation request with the alternate model. However, I cannot claim
that it improved the RAG system because the complete before and after
evaluations did not finish. The API later reached its free-tier quota before
I could collect the required runs.

## What's Still Broken

Criteria 1, 2, 3, and 5 still need complete evaluation runs. The system
successfully loads and chunks the corpus, creates embeddings, and uses the
vector store, but I could not collect the required generation results because
of API availability and quota limits.

If I had additional API availability, I would first complete the three
baseline runs. I would then use the actual misses to identify whether the
problem was retrieval or generation, make one evidence-based change, and run
the three after evaluations using the same criteria.

I stopped at this point because I ran out of available free-tier API requests
and submission time. I chose to report the incomplete evaluation rather than
fill the tables with results my system did not actually produce.

## What I'd Do Differently

I would make criterion 4 more demanding. My original target required 80% of
chunks to be between 150 and 600 characters, but all 88 chunks already met
that target. Knowing this now, I would use a narrower range or a criterion
that measures whether each chunk preserves enough context for retrieval,
rather than relying mainly on character length.

I would also begin the repeated evaluation runs earlier. The assignment
requires multiple model calls, so leaving the evaluation close to the
submission deadline made temporary API availability and free-tier quota
limits much more significant.