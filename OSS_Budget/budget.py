import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, description, amount, filename="expenses.txt"):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        # 지출 추가 할때마다 expenses.txt 파일에도 추가
        # expenses.txt 파일이 존재하지 않으면 새로 생성함
        with open(filename, "a", encoding="utf-8") as f:
                f.write(f"{expense.date}, {expense.category}, {expense.description}, {expense.amount}\n") #쉼표로 구분하여 저장
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
    # 프로그램 실행 시 expenses.txt를 읽어오는 함수
    def file_read(self, filename="expenses.txt"):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                for line in f:
                    date, category, description, amount = line.strip().split(", ", 3)
                    expense = Expense(date, category, description, int(amount))
                    self.expenses.append(expense)
            print("지출 내역을 불러왔습니다.")
        except FileNotFoundError:
            print("저장된 지출 내역이 없습니다.")
