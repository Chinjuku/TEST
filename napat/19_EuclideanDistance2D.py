"""EuclideanDistance2D"""
def main():
    """EuclideanDistance2D"""
    pos_q1 = float(input())
    pos_q2 = float(input())
    pos_p1 = float(input())
    pos_p2 = float(input())
    diff_1 = pos_q1 - pos_p1
    diff_2 = pos_q2 - pos_p2
    print((diff_1**2 + diff_2**2)**0.5)
main()
