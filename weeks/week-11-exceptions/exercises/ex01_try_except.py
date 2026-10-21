"""Exercise 01: expected bad input."""
raw_turn = "not-a-number"

try:
    turn=int(raw_turn)
except ValueError:
    print("Loi: Khong phai so nguyen")