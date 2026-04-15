import random
from datetime import datetime
from quiz import Quiz

class QuizGame:
    """
    퀴즈 게임의 전체 상태(퀴즈 목록, 최고 점수, 기록)를 관리하고
    비즈니스 로직을 담당하는 클래스입니다.
    """

    def __init__(self):
        self.quizzes: list[Quiz] = []
        self.best_score: int = 0
        self.history: list[dict] = []
        
        # 파일 로드 기능이 아직 없으므로, 인스턴스 생성 시 기본 데이터를 바로 세팅합니다.
        self._init_default_data()

    def _init_default_data(self):
        """
        기본으로 제공할 파이썬/Git 기초 퀴즈 5개입니다.
        """
        self.best_score = 0
        self.history = []
        self.quizzes = [
            Quiz("파이썬에서 변수의 타입을 확인하는 내장 함수는 무엇인가요?", 
                 ["type()", "print()", "len()", "id()"], 1, "자료형(type)을 알아내는 함수입니다."),
            Quiz("다음 중 파이썬의 변경 불가능한(immutable) 자료형은 무엇인가요?", 
                 ["list", "dict", "set", "tuple"], 4, "괄호 () 를 사용하여 만드는 자료형입니다."),
            Quiz("Git에서 로컬 저장소의 변경 사항을 원격 저장소로 올리는 명령어는 무엇인가요?", 
                 ["git pull", "git push", "git commit", "git clone"], 2, "밀어넣는다(push)는 의미를 가집니다."),
            Quiz("for문과 while문의 차이점으로 올바르지 않은 것은?", 
                 ["for문은 반복 횟수가 명확할 때 주로 쓴다.", "while문은 조건이 참인 동안 계속 반복한다.", 
                  "for문은 리스트 등 순회 가능한 객체와 함께 쓴다.", "while문은 무한 루프를 만들 수 없다."], 4, "while True: 를 생각해보세요."),
            Quiz("JSON 파일을 파이썬 딕셔너리로 읽어올 때 사용하는 json 모듈의 함수는?", 
                 ["json.dump()", "json.dumps()", "json.load()", "json.loads()"], 3, "파일 객체에서 데이터를 '불러오는(load)' 함수입니다.")
        ]

    def play_game(self, num_questions: int):
        """
        지정된 문제 수만큼 퀴즈를 출제하고 점수를 계산합니다. (보너스: 랜덤 출제, 힌트 감점)
        """
        if not self.quizzes:
            print("\n[안내] 등록된 퀴즈가 없습니다. 퀴즈를 먼저 추가해주세요.")
            return

        # 보너스: 퀴즈 랜덤 섞기
        play_list = random.sample(self.quizzes, min(num_questions, len(self.quizzes)))
        
        score = 0
        total_possible_score = len(play_list) * 10 # 문제당 10점

        print(f"\n=== 퀴즈 게임 시작! (총 {len(play_list)}문제) ===")
        print("💡 힌트를 보려면 'h'를 입력하세요. (힌트 사용 시 해당 문제 점수 반감)")
        
        for i, quiz in enumerate(play_list, start=1):
            quiz.display()
            earned_points = 10
            
            while True:
                user_input = input("\n정답을 입력하세요 (1~4, 힌트: h): ").strip().lower()
                
                # 빈 입력 처리
                if not user_input:
                    print("입력값이 없습니다. 다시 입력해주세요.")
                    continue

                # 힌트 처리
                if user_input == 'h':
                    print(quiz.get_hint())
                    earned_points = 5 # 힌트 사용 시 점수 반감
                    continue
                
                # 정답 확인
                try:
                    user_ans = int(user_input)
                    if not (1 <= user_ans <= 4):
                        print("1에서 4 사이의 번호를 입력해주세요.")
                        continue
                    
                    if quiz.check_answer(user_ans):
                        print("✅ 정답입니다!")
                        score += earned_points
                    else:
                        print(f"❌ 오답입니다. 정답은 {quiz.answer}번입니다.")
                    break # 문제 넘어가기
                    
                except ValueError:
                    print("숫자 또는 'h'만 입력해주세요.")

        # 결과 처리 및 저장
        print(f"\n=== 게임 종료 ===")
        print(f"최종 점수: {score} / {total_possible_score}")
        
        if score > self.best_score:
            print(f"🎉 신기록 달성! (기존 최고 점수: {self.best_score})")
            self.best_score = score
            
        # 기록저장.
        record = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "played": len(play_list),
            "score": score
        }
        self.history.append(record)