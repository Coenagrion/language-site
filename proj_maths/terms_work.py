def get_terms_for_table():
    terms = []
    with open("./data/terms.csv", "r", encoding="utf-8") as f:
        cnt = 1
        for line in f.readlines()[1:]:
            term, definition, source = line.split(";")
            terms.append([cnt, term, definition])
            cnt += 1
    return terms

def get_rules_for_table():
    rules = []
    with open("./data/rules.csv", "r", encoding="utf-8") as f:
        cnt = 1
        for line in f.readlines()[1:]:
            rule, exceptions, source = line.split(";")
            rules.append([cnt, rule, exceptions])
            cnt += 1
    return rules


def write_term(new_term, new_definition):
    new_term_line = f"{new_term};{new_definition};user"
    with open("./data/terms.csv", "r", encoding="utf-8") as f:
        existing_terms = [l.strip("\n") for l in f.readlines()]
        title = existing_terms[0]
        old_terms = existing_terms[1:]
    terms_sorted = old_terms + [new_term_line]
    terms_sorted.sort()
    new_terms = [title] + terms_sorted
    with open("./data/terms.csv", "w", encoding="utf-8") as f:
        f.write("\n".join(new_terms))

def write_rule(new_rule, new_exception):
    new_rule_line = f"{new_rule};{new_exception};user"
    with open("./data/rules.csv", "r", encoding="utf-8") as f:
        existing_rules = [l.strip("\n") for l in f.readlines()]
        title = existing_rules[0]
        old_terms = existing_rules[1:]
    terms_sorted = old_terms + [new_rule_line]
    terms_sorted.sort()
    new_rules = [title] + terms_sorted
    with open("./data/rules.csv", "w", encoding="utf-8") as f:
        f.write("\n".join(new_rules))

def get_terms_stats():
    db_terms = 0
    user_terms = 0
    defin_len = []
    with open("./data/terms.csv", "r", encoding="utf-8") as f:
        for line in f.readlines()[1:]:
            term, defin, added_by = line.split(";")
            words = defin.split()
            defin_len.append(len(words))
            if "user" in added_by:
                user_terms += 1
            elif "db" in added_by:
                db_terms += 1
    stats = {
        "terms_all": db_terms + user_terms,
        "terms_own": db_terms,
        "terms_added": user_terms,
        "words_avg": sum(defin_len)/len(defin_len),
        "words_max": max(defin_len),
        "words_min": min(defin_len)
    }
    return stats
