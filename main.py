import sys
from game import QuizGame

def get_valid_int(prompt: str, min_val: int = None, max_val: int = None) -> int:
    while True:
        user_input = input(prompt).strip()
        
        if not user_input:
            print("[안내] 입력값이 없습니다. 다시 입력해주세요.")
            continue
            
        try:
            value = int(user_input)
            
            if min_val is not None and value < min_val:
                print(f"[안내] {min_val} 이상의 숫자를 입력해주세요.")
                continue
            if max_val is not None and value > max_val:
                print(f"[안내] {max_val} 이하의 숫자를 입력해주세요.")
                continue
                
            return value
            
        except ValueError:
            print("[안내] 숫자로만 입력해주세요.")

def main():
    game = QuizGame()
    
    try:
        while True:
            print("\n" + "="*30)
            print(" 파이썬 & Git 퀴즈 게임 ")
            print("="*30)
            print("1. 퀴즈 풀기")
            print("2. 새로운 퀴즈 추가")
            print("3. 퀴즈 목록 보기")
            print("4. 퀴즈 삭제 (보너스)")
            print("5. 점수 및 기록 확인")
            print("0. 종료")
            print("="*30)
            
            choice = get_valid_int("메뉴를 선택하세요 (0~5): ", 0, 5)
            
            if choice == 1:
                if not game.quizzes:
                    print("\n[안내] 등록된 퀴즈가 없습니다.")
                    continue
                max_q = len(game.quizzes)
                num_q = get_valid_int(f"\n몇 문제를 푸시겠습니까? (1~{max_q}): ", 1, max_q)
                game.play_game(num_q)
                
            elif choice == 2:
                print("\n--- 새로운 퀴즈 추가 ---")
                question = input("문제를 입력하세요: ").strip()
                if not question:
                    print("[안내] 문제가 비어있어 추가를 취소합니다.")
                    continue
                
                choices = []
                for i in range(1, 5):
                    choice_text = input(f"선택지 {i}을(를) 입력하세요: ").strip()
                    choices.append(choice_text if choice_text else f"선택지 {i}")
                
                answer = get_valid_int("정답 번호를 입력하세요 (1~4): ", 1, 4)
                hint = input("힌트를 입력하세요 (없으면 그냥 Enter): ").strip()
                
                game.add_quiz(question, choices, answer, hint)
                
            elif choice == 3:
                pass
            elif choice == 4:
                pass
            elif choice == 5:
                pass
                
            elif choice == 0:
                print("\n게임을 종료합니다. 플레이해주셔서 감사합니다!")
                sys.exit(0)

    except (KeyboardInterrupt, EOFError):
        print("\n\n[안내] 프로그램이 강제 종료 신호를 받았습니다.")
        print("안전하게 종료합니다...")
        sys.exit(1)

if __name__ == "__main__":
    main()