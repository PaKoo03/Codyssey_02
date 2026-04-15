import sys

def main():
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
        
        choice = int(input("메뉴를 선택하세요 (0~5): ")) 
        
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

if __name__ == "__main__":
    main()