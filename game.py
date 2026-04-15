import random
from datetime import datetime
from quiz import Quiz

class QuizGame:
    def __init__(self):
        self.quizzes: list[Quiz] = []
        self.best_score: int = 0
        self.history: list[dict] = []
        self._init_default_data()

    def _init_default_data(self):
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
        if not self.quizzes:
            print("\n[안내] 등록된 퀴즈가 없습니다. 퀴즈를 먼저 추가해주세요.")
            return

        play_list = random.sample(self.quizzes, min(num_questions, len(self.quizzes)))
        
        score = 0
        total_possible_score = len(play_list) * 10

        print(f"\n=== 퀴즈 게임 시작! (총 {len(play_list)}문제) ===")
        print("💡 힌트를 보려면 'h'를 입력하세요. (힌트 사용 시 해당 문제 점수 반감)")
        
        for i, quiz in enumerate(play_list, start=1):
            quiz.display()
            earned_points = 10
            
            while True:
                user_input = input("\n정답을 입력하세요 (1~4, 힌트: h): ").strip().lower()
                
                if not user_input:
                    print("입력값이 없습니다. 다시 입력해주세요.")
                    continue

                if user_input == 'h':
                    print(quiz.get_hint())
                    earned_points = 5
                    continue
                
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
                    break
                    
                except ValueError:
                    print("숫자 또는 'h'만 입력해주세요.")

        print(f"\n=== 게임 종료 ===")
        print(f"최종 점수: {score} / {total_possible_score}")
        
        if score > self.best_score:
            print(f"🎉 신기록 달성! (기존 최고 점수: {self.best_score})")
            self.best_score = score
            
        record = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "played": len(play_list),
            "score": score
        }
        self.history.append(record)

    def add_quiz(self, question: str, choices: list[str], answer: int, hint: str):
        new_quiz = Quiz(question, choices, answer, hint)
        self.quizzes.append(new_quiz)
        print("\n✅ 퀴즈가 성공적으로 추가되었습니다!")

    def delete_quiz(self, index: int):
        deleted = self.quizzes.pop(index)
        print(f"\n✅ 퀴즈 '{deleted.question}'가 삭제되었습니다.")

    def get_score_info(self) -> str:
        info = f"\n🏆 최고 점수: {self.best_score}점\n"
        info += "-" * 30 + "\n"
        if not self.history:
            info += "아직 플레이 기록이 없습니다."
        else:
            info += "📜 최근 플레이 기록 (최대 5개)\n"
            for record in reversed(self.history[-5:]):
                info += f"[{record['date']}] {record['played']}문제 풀이 / 점수: {record['score']}점\n"
        return info

    def get_quiz_list(self) -> str:
        if not self.quizzes:
            return "등록된 퀴즈가 없습니다."
        
        result = "\n=== 등록된 퀴즈 목록 ===\n"
        for i, quiz in enumerate(self.quizzes):
            result += f"{i + 1}. {quiz.question} (정답: {quiz.answer}번)\n"
        return result