import random

hands = ["ぐー","ちょき","ぱー"]

def judge(ene_hand, usr_hand):
    diff = usr_hand - ene_hand if (usr_hand - ene_hand) >= 0 else (usr_hand - ene_hand) + 3
    if   diff == 0: return "draw"
    elif diff == 1: return "lose"
    elif diff == 2: return "win"

if __name__ == "__main__":
    ene_hand = random.randint(0,2)
    usr_hand = int(input("your hand: 0(ぐー), 1(ちょき), 2(ぱー)"))
    print(f"ene_hand:{hands[ene_hand]} usr_hand:{hands[usr_hand]}")
    res = judge(ene_hand, usr_hand)
    print(res)
