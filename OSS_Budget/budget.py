import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []
        self.goal_expense = 0

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()
    # 목표 최대 지출액 설정 함수
    def set_goal_expense(self, goal):
        self.goal_expense = goal
        print("목표 최대 지출액이 설정되었습니다.\n")
    # 목표 최대 지출액 달성도에 따른 문구 출력
    def percent_phrase(self):
        # 목표 최대 지출 설정 안했을 시 return
        if self.goal_expense <= 0:
            print("목표 최대 지출액을 설정해보는게 어떨까요?\n")
            return
        
        print(f"목표 최대 지출액: {self.goal_expense}원\n")
        
        total = sum(e.amount for e in self.expenses)
        percent = total / self.goal_expense * 100
        if percent <= 10:
            print(f"목표 최대 지출액의 {percent:.1f}% 사용! 최대한 아껴봐요!\n")
        elif 10 < percent <= 25:
            print(f"목표 최대 지출액의 {percent:.1f}% 사용! 아직은 여유로워요!\n")
        elif 25 < percent <= 50:
            print(f"목표 최대 지출액의 {percent:.1f}% 사용! 음 아직은 괜찮나..?\n")
        elif 50 < percent <= 75:
            print(f"목표 최대 지출액의 {percent:.1f}% 사용! 어라.. 벌써 절반 넘게 썼어요\n")
        elif 75 < percent <= 90:
            print(f"목표 최대 지출액의 {percent:.1f}% 사용! 목표 달성하려면 이제 허리띠 꽉 졸라매야겠는데요?\n")
        elif 90 < percent < 100:
            print(f"목표 최대 지출액의 {percent:.1f}% 사용! 이젠 정말 아껴야 해요!\n")
        elif percent == 100:
            print("목표 최대 지출액에 도달했어요! 되도록이면 더 쓰지 않는게 어떨까요?\n")
        else:
            print("목표 최대 지출액을 초과했어요... 다음엔 지켜봐요!\n")

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")


