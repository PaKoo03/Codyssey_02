import sys
from game import QuizGame

def get_valid_int(prompt: str, min_val: int = None, max_val: int = None) -> int:
    """
    사용자로부터 안전하게 정수를 입력받는 함수입니다.
    과제 요구사항인 빈 입력, 공백 제거, 형변환 실패, 허용 범위 검사를 모두 수행합니다.
    """
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
    # 게임 인스턴스 생성
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
                # 풀이할 문제 수 선택
                max_q = len(game.quizzes)
                num_q = get_valid_int(f"\n몇 문제를 푸시겠습니까? (1~{max_q}): ", 1, max_q)
                game.play_game(num_q)
                
            elif choice == 2:
                print("\n[안내] 아직 구현되지 않은 기능입니다.")
            elif choice == 3:
                print("\n[안내] 아직 구현되지 않은 기능입니다.")
            elif choice == 4:
                print("\n[안내] 아직 구현되지 않은 기능입니다.")
            elif choice == 5:
                print("\n[안내] 아직 구현되지 않은 기능입니다.")
                
            elif choice == 0:
                print("\n게임을 종료합니다. 플레이해주셔서 감사합니다!")
                return 0 

    except (KeyboardInterrupt, EOFError):
        print("\n\n[안내] 프로그램이 강제 종료 신호를 받았습니다.")
        print("안전하게 종료합니다...")
        sys.exit(1)

if __name__ == "__main__":
    main()