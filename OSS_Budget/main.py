from budget import Budget


def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 목표 최대 지출액 입력")
        print("5. 종료")
        choice = input("선택 > ")

        if choice == "1":
            category = input("카테고리 (예: 식비, 교통 등): ")
            description = input("설명: ")
            try:
                amount = int(input("금액(원): "))
            except ValueError:
                print("잘못된 금액입니다.\n")
                continue
            budget.add_expense(category, description, amount)

        elif choice == "2":
            budget.list_expenses()
        
        # 총 지출 보기 선택 시 
        # 목표 최대 지출 설정X -> 총지출만 출력
        # 목표 최대 지출 설정O -> 총지출, 목표 최대 지출 및 문구 출력력
        elif choice == "3":
            budget.total_spent()
            budget.percent_phrase()
        
        # 목표 최대 지출액 설정
        elif choice == "4":
            try:
                goal = int(input("목표 최대 지출액(원): "))
                if goal <= 0:
                    print("0보다 큰 값을 입력하세요\n")
                    continue
                budget.set_goal_expense(goal)
            except ValueError:
                print("잘못된 금액입니다.\n")
                continue


        elif choice == "5":
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()
