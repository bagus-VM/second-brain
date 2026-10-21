---
title: "Exercise 1 — Spam classification with Naive Bayes (Solutions)"
tags: [homework, ml-security, semester-2]
course: "Machine Learning for Cybersecurity"
source_count: 2
status: current
last_updated: 2026-10-19
---

# ML for Cybersecurity — Lecture 2 exercise: spam classification

Source: `02_Spam.pdf` (Reiser), Winter 2026/27.
Runnable code: `spam_classifier.py` in this folder. Every number below came from an actual run, not from the slides.

## The task (as printed)

1. Create a dictionary of words — drop non-words (punctuation, single characters) — keep the **2000 most frequent words of the training set**.
2. Transform each mail into a word-count vector over that dictionary.
3. Train a Bayes classifier (`MultinomialNB` from `sklearn.naive_bayes`).
4. Check the classifier with the test set.

Dataset: LingSpam. The lecture offers `lingspam_public.tar.gz` from AUEB or a pre-processed subset from Dropbox. The AUEB archive is the live one (11.5 MB, 2893 texts in each of four variants: `bare`, `lemm`, `lemm_stop`, `stop`).

## What I ran

```
python spam_classifier.py <path>/lingspam_public/lemm_stop
```

- **Variant:** `lemm_stop` — lemmatised and stop-word-removed, matching the "preprocessing done: removal of stop-words, lemmatization" note in the lecture.
- **Split:** parts 1–9 train, part 10 test (the standard LingSpam split). Labelling follows the dataset convention: `spmsg*.txt` is spam.
- **Tokenizer:** `[A-Za-z]+`, lower-cased, words of length ≥ 2. That satisfies "drop non-words and single characters" without a separate stop-word list (already applied in the dataset variant).
- **Model:** `MultinomialNB()` with default `alpha=1.0` — i.e. Laplace smoothing, exactly the lecture's slide 20.

## Results (actual run)

```
train: 2602 mails (432 spam)
test:   291 mails (49 spam)
vocabulary: 2000 words
test mails with no known word: 0

confusion matrix [[TN FP] [FN TP]]:
[[242   0]
 [  3  46]]

accuracy:  0.9897
precision: 1.0000
recall:    0.9388
F1:        0.9684

baseline (always ham) accuracy: 0.8316
```

Classification report:

| class | precision | recall | f1-score | support |
|-------|-----------|--------|----------|---------|
| ham | 0.9878 | 1.0000 | 0.9938 | 242 |
| spam | 1.0000 | 0.9388 | 0.9684 | 49 |
| accuracy | | | 0.9897 | 291 |

The most spam-indicative words the model learned: `ffa, capitalfm, floodgate, investment, stealth, millions, nbsp, offshore, mlm, orders, sales, invest`.
The most ham-indicative: `linguistic, workshop, abstract, theory, linguistics, grammar, linguist, discourse, syntax, semantic, pp, acquisition`.

## The two things this exercise is actually teaching

**1. Accuracy is the wrong headline number.** The baseline of always predicting "ham" scores 83.16% here. A model with 98.97% accuracy looks excellent until you notice recall on spam is 0.94 — 3 spam mails out of 49 slipped through, and the model has *never* flagged a ham mail as spam. In a real filter that asymmetry is deliberate (false positives annoy users), but you have to say so out loud instead of quoting accuracy.

**2. What the classifier learned is dataset-specific.** LingSpam's ham is a linguistics mailing list. The model learned "academic linguistics vocabulary" versus "commercial vocabulary", not "legitimate" versus "spam" in general. Swap the ham corpus and the vocabulary — and probably the decision boundary — changes. This is the same trap as the credit-card example from the lecture: the model fits the dataset's peculiarities, not the world.

## Reading assignment — answers

Paper: Kontsewaya, Antonov, Artamonov, *Evaluating the Effectiveness of Machine Learning Methods for Spam Detection*, Procedia Computer Science (BICA 2020 proceedings), 2021. I pulled the full text (EasyChair preprint 6074) to answer these; where the paper does not say something, I say so rather than guess.

**1. At least one alternative to naive Bayes for spam detection.**
The paper compares six: **Naive Bayes, K-nearest neighbours, SVM, logistic regression, decision tree, random forest**. Logistic regression and NB reach the highest accuracy (the paper reports up to 99%); KNN and random forest perform worst in its table. So: any of the other five is a valid answer, and the paper's own conclusion is that logistic regression is the strongest alternative to NB.

**2. Additional preprocessing methods not discussed in the lecture.**
The paper uses: removing undefined values, gaps and duplicates before anything else (it drops the dataset from 5728 to 5695 rows); lowercasing; removing numbers; removing punctuation and stop words with `string` and `nltk`; tokenisation; `CountVectorizer` to turn words into a numeric matrix; and an 80/20 train/test split. Hyperparameters are tuned with `GridSearchCV` for every algorithm except NB.
Methods the paper does *not* use but that are standard additions: stemming (Porter/Snowball) instead of or before lemmatisation, TF-IDF weighting instead of raw counts, n-grams (bigrams catch "free money" as one feature), character n-grams (robust to obfuscation like "v1agra"), and metadata features (sender domain, headers, HTML structure).

**3. Main differences between the credit-card fraud dataset and the spam dataset.**

| | Credit-card fraud (lecture) | Spam (paper) |
|---|---|---|
| Data type | tabular, 30 numeric features (28 anonymised via PCA, plus Time and Amount) | raw text — one message column plus a label |
| Size | 284,807 rows | 5,695 rows after dedup |
| Class balance | 492 frauds / 284,315 non-frauds — about **0.17%** positives | 1,368 spam / 4,360 ham — about **24%** positives |
| Preprocessing | scaling (StandardScaler), random undersampling of the majority class | text cleaning, tokenisation, CountVectorizer |
| Feature engineering | already done (PCA components) | the entire task (the vocabulary *is* the model input) |
| What "correct" means | missing a fraud is expensive; false alarms cost analyst time | misclassifying ham as spam is the worst outcome for the user |

The balance difference is the big one: 0.17% versus 24% positives is why the lecture needs undersampling and why accuracy is worthless on the credit-card data but merely misleading on LingSpam.

**4. What is the ROC curve used in the paper? How is it calculated?**
**The paper does not use a ROC curve.** I checked the full text: neither "ROC" nor "AUC" appears anywhere. It evaluates with accuracy, precision, recall and F-measure only, both in the method section and in the results table. If the exam or tutorial asks this, the honest answer is that the question does not match the paper.
For completeness, what ROC is: it plots the **true-positive rate** (recall = TP/(TP+FN)) against the **false-positive rate** (FP/(FP+TN)) while sweeping the classifier's decision threshold from 1 to 0. It is computed by sorting test samples by predicted score, then walking down that ranking and recording (FPR, TPR) after each sample — each point corresponds to "threshold at this score". The area under it (AUC) is the probability that a randomly chosen positive is ranked above a randomly chosen negative. ROC matters precisely where the paper is weakest: it is threshold-independent, so it exposes the trade-off that a single accuracy figure hides.

**5. Most interesting aspects (my judgement, not the paper's).**
The hyperparameter table is more useful than the results table: it shows KNN tuned over `n_neighbors ∈ 5..10`, SVM over `C ∈ {1,10,100,1000} × gamma × kernel`, random forest over `n_estimators ∈ {10,20,30}` and depth, logistic regression over `C = logspace(-3,3,7)` and l1/l2 — while Naive Bayes has **no hyperparameters at all**. That is the lecture's point made concrete: NB is a baseline you get for free, and everything else has to earn its complexity.

**6. Weaknesses (my judgement, labelled as such).**
- **Row-label misalignment in the results table.** The PDF's table extracts with labels offset by one row; the mapping has to be reconstructed from the conclusion (LR and NB at ~99% accuracy). Any conclusion drawn from that table should be checked against the original PDF.
- **Only one dataset, no cross-validation split reported.** A single 80/20 split on 5,695 rows makes the reported differences between algorithms unstable.
- **Naive Bayes gets no tuning and still competes.** Reporting "NB is as good as logistic regression" without noting that NB has zero hyperparameters and is a much simpler model oversells the comparison.
- **No threshold analysis** (which is what ROC/AUC would have provided), for a problem where the cost of errors is asymmetric.
- **CountVectorizer described as setting "a binary sign" per word**, while the model is a multinomial-style count approach elsewhere — the paper is loose about whether it is using presence/absence or counts.
- **The motivating statistic** ("more than half of the letters received by the user are spam") is not sourced.

## Implementation notes worth keeping

- **Vocabulary from the training set only.** Building the top-2000 list on the full corpus leaks test-set information into the model.
- **Laplace smoothing is not optional.** Without it, a word never seen in the spam training set makes `P(word|spam) = 0` and zeroes the whole product. `MultinomialNB`'s `alpha=1.0` is that +1 fix.
- **Work in log space.** Multiplying thousands of probabilities below 1.0 underflows to 0.0 in floating point; `MultinomialNB` adds log-probabilities for exactly this reason.
- **Impact of the variant:** `bare` keeps stop words and punctuation; `lemm_stop` (used here) removes both. If you rerun with `bare` and a longer vocabulary you will get different — usually slightly worse — results, which is the practical lesson about preprocessing.
