"""Spam classification with a Naive Bayes classifier (ML4CySec, Exercise 1).

Implements the lecture's programming exercise:
  1. Build a word dictionary: drop non-words and single characters, keep the
     2000 most frequent words of the *training* set.
  2. Turn every mail into a word-count vector over that dictionary.
  3. Train sklearn's MultinomialNB.
  4. Evaluate on the held-out test set.

Dataset: lingspam_public (AUEB), lemmatised + stop-word-removed variant.
Split: parts 1-9 train, part 10 test (the standard lingspam split).

Usage:
    python spam_classifier.py <path>/lingspam_public/lemm_stop

Pass one of the four variants (bare, lemm, lemm_stop, stop) - the parts live
inside the variant directory, not at the archive root.
"""
from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

import numpy as np
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.naive_bayes import MultinomialNB

TOKEN = re.compile(r"[A-Za-z]+")
VOCAB_SIZE = 2000


def read_split(root: Path):
    """Return (texts, labels) for parts 1-9 (train) and part 10 (test)."""
    train, test = [], []
    for part in sorted(root.glob("part*"), key=lambda p: int(p.name[4:])):
        bucket = test if part.name == "part10" else train
        for f in sorted(part.glob("*.txt")):
            # lingspam convention: spam files are named spmsg*.txt
            label = 1 if f.name.startswith("spmsg") else 0
            bucket.append((f.read_text(encoding="latin-1", errors="ignore"), label))
    return train, test


def tokenize(text: str):
    # non-words are dropped by the regex; single characters dropped by the length filter
    return [w.lower() for w in TOKEN.findall(text) if len(w) > 1]


def build_vocabulary(train, size=VOCAB_SIZE):
    counts = Counter()
    for text, _ in train:
        counts.update(tokenize(text))
    return [w for w, _ in counts.most_common(size)], counts


def vectorize(docs, index):
    X = np.zeros((len(docs), len(index)), dtype=np.int64)
    for i, text in enumerate(docs):
        for w in tokenize(text):
            j = index.get(w)
            if j is not None:
                X[i, j] += 1
    return X


def main():
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("lingspam_public")
    train, test = read_split(root)
    print(f"train: {len(train)} mails ({sum(y for _, y in train)} spam)")
    print(f"test:  {len(test)} mails ({sum(y for _, y in test)} spam)")

    vocab, counts = build_vocabulary(train)
    index = {w: i for i, w in enumerate(vocab)}
    print(f"vocabulary: {len(vocab)} words (most frequent: {vocab[:8]})")

    X_train = vectorize([t for t, _ in train], index)
    y_train = np.array([y for _, y in train])
    X_test = vectorize([t for t, _ in test], index)
    y_test = np.array([y for _, y in test])

    # how much of the test set is actually covered by the training vocabulary?
    unknown = int((X_test.sum(axis=1) == 0).sum())
    print(f"test mails with no known word: {unknown}")

    clf = MultinomialNB()
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    print("\nconfusion matrix [[TN FP] [FN TP]]:")
    print(confusion_matrix(y_test, y_pred))
    print(f"accuracy:  {accuracy_score(y_test, y_pred):.4f}")
    print(f"precision: {precision_score(y_test, y_pred):.4f}")
    print(f"recall:    {recall_score(y_test, y_pred):.4f}")
    print(f"F1:        {f1_score(y_test, y_pred):.4f}")

    # the honest baseline: always predict "ham"
    baseline = float((y_test == 0).mean())
    print(f"\nbaseline (always ham) accuracy: {baseline:.4f}")
    print("\nclassification report:")
    print(classification_report(y_test, y_pred, target_names=["ham", "spam"], digits=4))

    # the words the model finds most indicative, per class
    order = np.argsort(clf.feature_log_prob_[1] - clf.feature_log_prob_[0])
    print("most spam-indicative words:", [vocab[i] for i in order[-12:][::-1]])
    print("most ham-indicative words:  ", [vocab[i] for i in order[:12]])


if __name__ == "__main__":
    main()
