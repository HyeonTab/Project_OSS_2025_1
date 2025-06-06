import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []

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

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")

    # 전체 지출에 대한 카테고리별 지출액 및 비율을 보여주는 함수
    def category_total_chart(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        # 카테고리별 지출액 저장
        summary = {}
        for e in self.expenses:
            # summary에 해당 카테고리가 있으면 그 지출액에 더함
            if e.category in summary:
                summary[e.category] += e.amount
            # summary에 해당 카테고리가 없으면 새로 만듬
            else:
                summary[e.category] = e.amount
        
        bar_width = 20
        total = sum(e.amount for e in self.expenses)

        print("[카테고리별 지출액 및 비율]")
        for category, amount in summary.items():
            bar_len = int((amount / total) * bar_width)
            expense_rate = amount / total * 100
            bar = "█" * bar_len
            print(f"{category}\t: {bar.ljust(bar_width)}{expense_rate:.1f}%\t{amount}원")
        print()