from datasets import Simple, Split, Xor
N = 100


def classify(pt):
    "Classify based on x position"
    if pt[0] < 0.5 and pt[1]<0.5 or pt[0] > 0.5 and pt[1] > 0.5:
        return 1.0
    else:
        return 0.0

Xor(N, vis=True).graph("initial", model=classify)