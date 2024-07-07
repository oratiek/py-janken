import random

hands = ["ぐー","ちょき","ぱー"]

def judge(ene_hand, usr_hand):
    diff = usr_hand - ene_hand
    diff = usr_hand - ene_hand if diff >= 0 else diff + 3
    if diff == 0:
        return "draw"
    elif diff in [-1,2] :
        return "win"
    else:
        return "lose"

if __name__ == "__main__":
    ene_hand = random.randint(0,2)
    usr_hand = int(input("your hand: 0(ぐー), 1(ちょき), 2(ぱー)"))
    print(f"ene_hand:{hands[ene_hand]} usr_hand:{hands[usr_hand]}")
    res = judge(ene_hand, usr_hand)
    print(res)
