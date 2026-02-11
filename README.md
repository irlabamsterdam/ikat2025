# IKAT 2025 Repository

This repository contains the resources for **TREC iKAT 2025**:

> **TREC iKAT 2025: A Test Collection for the Offline and Interactive Evaluation of Conversational Search**  
> Abbasiantaeb*, Lupart*, Gohsen, Mirzakhmedova, Kiesel, Dalton, Aliannejadi

The collection supports both **offline (Cranfield-style)** and **interactive (user simulation-based)** evaluation of personalized conversational search systems.

## Overview

TREC iKAT focuses on **personalized conversational search**, where systems must:

1. Identify relevant persona knowledge (PTKB statements).
2. Retrieve relevant passages from a large web corpus.
3. Generate grounded, personalized responses.

The 2025 edition extends previous collections (2023–2024) with:

- Multi-session conversations
- Dynamically evolving user profiles
- Interactive system evaluation

## Repository Structure

### 1. `offline/`

Resources for **offline (Cranfield-style) test collection evaluation**.

#### Topics and Gold Data

- `2025_test_topics.json`: Official test topics.

- `gold-response-nist.json`: Human-written gold responses from NIST assessors.

#### Nuggets

- `nuggets/nuggets-nist.json`: 2,241 human-extracted gold nuggets.

- `nuggets/nuggets-LLM.json`: 8,607 LLM-extracted nuggets.


#### PTKB (Persona) Relevance

- `ptkb/qrels-ptkb-nist.trec`: PTKB relevance labels in TREC format from NIST assessors.

#### Passage Relevance (Qrels)

- `qrel/qrels-nist.trec`: 5,650 NIST-judged query-passage pairs (scale 0–4).

- `qrel/qrels-llm.txt`: 38,809 LLM-based passage relevance judgments.

Relevance scale (TREC style):
- 0: Fails to meet
- 1: Slightly meets
- 2: Moderately meets
- 3: Highly meets
- 4: Fully meets


#### `offline/runs/`

Contains baseline and participant runs for both the automatic submission and the generation-only runs.

Baselines include:
- BM25 (lexical)
- SPLADE (learned sparse retrieval)
- ANCE (dense)
- With and without PTKB personalization

To reproduce offline baselines:
👉 https://github.com/SimonLupart/ikat-baseline

---

### 2. `interactive/`

Resources for **interactive evaluation** (user simulation-based).

#### `interactive/assessments/`

Final assessments for the interactive task, both from human NIST assessors and from LLM-based judgement.

- `assess-llm.ipynb`  
- `prompts.py`  
- `LLM/`
  - `assessments-gpt4.json`
  - `assessments-gpt5.json`  
- `NIST/`
  - `topic*-*.final`  


#### `interactive/human evaluation guidelines/`

Human judging instructions used by NIST assessors:

- `ikat-dialog-v1.json`: Dialogue-level evaluation guidelines.

- `ikat-fragment-v1.json`: Rubric-level (turn-fragment) evaluation guidelines.

Evaluation dimensions include:

**Rubric-level (1–3 turns):**
- Engagement
- Relevance
- Overall Quality

**Dialogue-level:**
- Mixed-initiative strategies
- Personalization
- Information flow
- Trustworthiness
- User satisfaction

Each scored on a 1–5 scale, plus confidence ratings.

#### `interactive/rubrics/`

- `rubrics.json`: Manually derived grading rubric questions (92 total).

Rubrics decompose complex information needs into atomic evaluation questions.


#### `interactive/runs/trec-ikat25-runs/`

Submitted interactive system runs (`*.jsonl`):

## Acknowledgements

## Citation

## License

