from datasets import Simple, Split, Xor
N = 100


def classify(pt):
    "Classify based on x position"
    if pt[0] > 0.8 or pt[0]<0.2:
        return 1.0
    else:
        return 0.0

Split(N, vis=True).graph("initial", model=classify)