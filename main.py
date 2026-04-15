import sys

def get_valid_int(prompt: str, min_val: int = None, max_val: int = None) -> int:
    """
    사용자로부터 안전하게 정수를 입력받는 공통 헬퍼 함수입니다.
    과제 요구사항인 빈 입력, 공백 제거, 형변환 실패, 허용 범위 검사를 모두 수행합니다.
    """
    while True:
        # 입력 앞뒤 공백 제거
        user_input = input(prompt).strip()
        
        # 빈 입력 처리
        if not user_input:
            print("[안내] 입력값이 없습니다. 다시 입력해주세요.")
            continue
            
        try:
            # 숫자 변환 시도
            value = int(user_input)
            
            # 허용 범위 밖 숫자 검사
            if min_val is not None and value < min_val:
                print(f"[안내] {min_val} 이상의 숫자를 입력해주세요.")
                continue
            if max_val is not None and value > max_val:
                print(f"[안내] {max_val} 이하의 숫자를 입력해주세요.")
                continue
                
            return value
            
        except ValueError:
            # 숫자 변환 실패 (예: abc)
            print("[안내] 숫자로만 입력해주세요.")

def main():
    # 프로그램 강제 종료(Ctrl+C 등)를 대비한 예외 처리
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
            
            # 기존 int(input())을 만든 함수로 교체
            choice = get_valid_int("메뉴를 선택하세요 (0~5): ", 0, 5)
            
            if choice == 1:
                print("\n[안내] 아직 구현되지 않은 기능입니다.")
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

    # KeyboardInterrupt (Ctrl+C) 또는 EOFError (Ctrl+D / Ctrl+Z) 발생 시 안전하게 종료
    except (KeyboardInterrupt, EOFError):
        print("\n\n[안내] 프로그램이 강제 종료 신호를 받았습니다.")
        print("안전하게 종료합니다...")
        sys.exit(1) # 비정상 상황에서의 종료이므로 상태 코드 1 반환

if __name__ == "__main__":
    main()