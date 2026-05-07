
# paper-to-python
<img width="450" height="600" alt="paper-to-python" src="https://github.com/user-attachments/assets/a0bf93c2-0755-4ee5-ac48-5e7e7d2a1861" />

Reimplementing Python's core data structures from scratch — drawn on paper first,
then coded by hand.


## Why this exists

Reading about a data structure is not the same as building one. This repo is my
deliberate-practice log: each entry starts as a paper diagram, becomes a
from-scratch implementation, gets reviewed for correctness and idiom, and ends
with a comparison against CPython's actual source.

The goal isn't to write production replacements — CPython is already excellent.
The goal is to *understand* the trade-offs the standard library team made, and
to build the instinct for when each structure fits a problem.

## Method

Each entry follows the same loop:

1. **Draw it on paper.** Pointers, edge cases, invariants — sketched before any code.
2. **Implement without AI assistance.** Write it solo. Get stuck. Backtrack.
   The friction is the point.
3. **AI-reviewed iteration.** Once a method works, it gets reviewed for correctness,
   idiom, and edge-case coverage. Revise. Re-review.
4. **Read the real thing.** Compare my implementation against CPython's source.
   Note where I diverged and why.

~1 hour per day. Streaks beat perfection.

## Structure

Each data structure lives in its own folder:

```
linked-list/
├── README.md             # Concept + invariants
├── diagrams/             # Hand-drawn sketches
├── implementation.py
├── tests.py
├── notes.md              # What I got wrong, what surprised me
└── cpython-comparison.md
```

## Progress

- [x] Doubly Linked List
- [ ] Stack / Queue
- [ ] Deque
- [ ] HashMap (`dict`)
- [ ] LRU Cache
- [ ] HashSet (`set`)
- [ ] Heap / Priority Queue
- [ ] Trie
- [ ] Binary Search Tree
- [ ] Graph + BFS/DFS
- [ ] Merge / Quick Sort
- [ ] Bisect

## Why public

Two reasons. First, public commitment — a private folder is easy to abandon.
Second, this is exactly the kind of work that's hard to signal on a CV otherwise:
depth, curiosity, and willingness to slow down and understand.
