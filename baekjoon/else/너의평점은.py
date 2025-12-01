import sys
def solve():
    grade_map = {
        'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0,
        'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0
    }
    total_score = 0.0  # (학점 * 과목 평점)의 총합
    total_credits = 0.0 # 학점 총합
    for _ in range(20):
        subject, credit, grade = input().split()
        if grade == 'P':
            continue
        credit = float(credit)
        total_score += credit * grade_map[grade]
        total_credits += credit
    if total_credits == 0:
        gpa = 0.0
    else:
        gpa = total_score / total_credits
    print(f"{gpa:.6f}")

solve()