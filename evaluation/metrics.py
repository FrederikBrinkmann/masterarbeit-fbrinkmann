# evaluation/metrics.py
# Platzhalter für Metriken: Schema-Valid-Rate, Slot-F1, Exact-Match

def schema_valid_rate(preds, golds):
    # preds/golds: Liste von dicts
    valid = 0
    for p,g in zip(preds,golds):
        if p == g:
            valid += 1
    return valid/len(golds) if golds else 0


def exact_match(pred, gold):
    return pred == gold
