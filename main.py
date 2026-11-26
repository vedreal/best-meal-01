#!/usr/bin/env python3
"""The Best Meal You Ever Had - make.fun bounty entry.

One sentence, at most 200 characters, about the best meal ever had.
No title, no explanation, no list of courses - just one sentence that
has to stand alone. The program scores ten fresh candidates against
the judge's criteria and writes the winner to /output/entry.txt.
"""

# ---------------------------------------------------------------------------
# Candidates (all single sentences, all at most 200 characters).
# ---------------------------------------------------------------------------

CANDIDATES = [
    "The best meal I ever had was a bowl of noodles at a night market "
    "in Jakarta, eaten standing up in the rain, and I have chased that "
    "exact bowl for ten years without ever finding it again.",
    "My grandmother's rendang, slow-cooked for six hours until the beef "
    "fell apart, taught me that patience is an ingredient you cannot "
    "buy in any shop.",
    "It was just rice, a fried egg, and sambal on a plastic plate at "
    "2 a.m., but after the longest day of my life, that plate tasted "
    "like someone finally saying welcome home.",
    "The best meal I ever had cost less than a dollar: satay from a "
    "street cart, smoke in my eyes, and the vendor remembering my "
    "order after only one visit.",
    "I ate grilled fish on a beach in Lombok with sand in my shoes and "
    "salt on my lips, and no restaurant since has ever come close to "
    "that plastic table.",
    "The soup arrived in a chipped bowl at a roadside warung, and one "
    "spoonful made the whole noisy street go quiet in my head.",
    "It was my mother's fried chicken, eaten with my hands on the "
    "kitchen floor as a kid, and I have spent twenty years trying to "
    "taste it exactly the same way.",
    "The best meal I ever had was a bowl of ramen in a tiny shop where "
    "the chef bowed, the steam fogged my glasses, and the broth "
    "tasted like someone had been perfecting it for decades.",
    "A stranger shared his lunch with me on a train - cold rice, "
    "salted fish, and a smile - and it was the kindest and tastiest "
    "meal I have ever eaten.",
    "The best meal I ever had was not on a menu: it was the first "
    "mango of the season, eaten over the sink, juice running down my "
    "arms, with nowhere to be.",
]

# ---------------------------------------------------------------------------
# Rubric: the judge reads sentences two at a time, so each one must
# stand alone. Criteria in order, weights 5/4/3/2/1, each scored 0-15.
# ---------------------------------------------------------------------------

CRITERIA = [
    ("specific_meal", 5),   # a concrete meal, not a vague memory
    ("sensory_detail", 4),  # you can taste, smell, or feel it
    ("emotional_turn", 3),  # a sting or turn in the last few words
    ("freshness", 2),       # not the obvious restaurant answer
    ("reads_aloud", 1),     # rhythm carries the sentence in one breath
]

# Scores per candidate, in the order of CRITERIA above.
SCORES = [
    [13, 13, 12, 12, 12],  # 1. night-market noodles in the rain
    [12, 12, 12, 11, 13],  # 2. grandmother's rendang
    [13, 13, 14, 13, 13],  # 3. rice, egg, sambal at 2 a.m.
    [12, 12, 11, 12, 12],  # 4. satay for less than a dollar
    [12, 13, 11, 11, 12],  # 5. grilled fish on a Lombok beach
    [13, 13, 12, 12, 12],  # 6. soup in a chipped bowl
    [11, 12, 13, 10, 13],  # 7. mother's fried chicken
    [12, 13, 11, 10, 12],  # 8. ramen in a tiny shop
    [12, 12, 14, 13, 12],  # 9. a stranger's lunch on a train
    [13, 13, 13, 13, 14],  # 10. first mango of the season
]


def total_score(index):
    """Weighted total for candidate `index` (0-based)."""
    return sum(
        score * weight
        for score, (_, weight) in zip(SCORES[index], CRITERIA)
    )


def ranked():
    """Candidates sorted by score (highest first); ties broken by
    shorter sentence, so the tighter line wins."""
    order = sorted(
        range(len(CANDIDATES)),
        key=lambda i: (-total_score(i), len(CANDIDATES[i])),
    )
    return [(CANDIDATES[i], total_score(i)) for i in order]


def pick_winner():
    """Highest score wins; ties break to the shorter sentence."""
    return ranked()[0]


def validate(sentence):
    """Gate: one sentence, at most 200 characters, no newline. A
    sentence ends with one terminal period and has no period followed
    by a space inside it (abbreviations such as "a.m." are fine)."""
    assert "\n" not in sentence, "entry must be a single line"
    assert len(sentence) <= 200, f"entry is {len(sentence)} chars, max 200"
    assert sentence.endswith("."), "entry must end with a period"
    assert ". " not in sentence, "entry must be a single sentence"
    assert sentence.strip() == sentence, "entry must not have edge spaces"
    return True


def main():
    winner, score = pick_winner()
    validate(winner)
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(winner)
    print(f"winner ({score} pts, {len(winner)} chars): {winner}")


if __name__ == "__main__":
    main()
