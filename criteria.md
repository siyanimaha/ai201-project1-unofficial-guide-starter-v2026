# Acceptance criteria — The Unofficial Guide

## 1. Retrieved chunks contain the answer

For at least 4 of my 5 test questions, the retrieved chunks include one that contains the answer.

**Why this target:**
I chose 4 out of 5 because some information in the campus life corpus may be harder to retrieve, but the system should still retrieve the correct information for most questions.

---

## 2. Every answer names a source

Every answer the system produces names at least one source document.

**Why this target:**
I chose every answer because the system uses retrieved documents to answer questions, so each generated answer should identify where its information came from.

---

## 3. Out-of-scope questions are refused

When I ask a question my documents clearly do not cover, the relevance gate stops it and the system returns "I don't have enough information about that" in at least 4 of 5 tries.

**Why this target:**
I chose 4 out of 5 because the relevance gate should reject almost all unrelated questions, while allowing for one borderline retrieval result.

---

## 4. Chunk sizes stay appropriate

At least 80% of the chunks are between 150 and 600 characters long.

**Why this target:**
The campus life corpus contains short posts, so chunks in this range should preserve useful information without combining too much unrelated material.

---

## 5. Answers use retrieved information

For at least 4 of my 5 test questions, the final answer includes the expected fact or phrase listed in questions.py.

**Why this target:**
I chose 4 out of 5 because the system should correctly use retrieved information for most questions, while allowing one difficult question to miss the target.
