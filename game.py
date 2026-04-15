import json
import random
from datetime import datetime
from quiz import Quiz

class QuizGame:
    """
    퀴즈 게임의 전체 상태(퀴즈 목록, 최고 점수, 기록)를 관리하고
    비즈니스 로직 및 파일 입출력을 담당하는 클래스입니다.
    """

    def __init__(self, data_file: str = "state.json"):
        self.data_file = data_file
        self.quizzes: list[Quiz] = []
        self.best_score: int = 0
        self.history: list[dict] = []
        
        # 인스턴스 생성 시 자동으로 데이터를 불러오거나 초기화합니다.
        self.load_data()

    def load_data(self):
        """
        state.json 파일에서 데이터를 읽어와 속성에 할당합니다.
        파일이 없거나 손상된 경우 예외 처리 후 기본 데이터로 복구합니다.
        """
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.best_score = data.get("best_score", 0)
                self.history = data.get("history", [])
                
                # 딕셔너리 리스트를 Quiz 객체 리스트로 역직렬화
                quiz_list = data.get("quizzes", [])
                self.quizzes = [Quiz.from_dict(q) for q in quiz_list]
                
                # 퀴즈가 비어있으면 기본 데이터 로드
                if not self.quizzes:
                    self._init_default_data()

        except FileNotFoundError:
            print("\n[안내] 데이터 파일이 존재하지 않아 기본 퀴즈 데이터를 생성합니다.")
            self._init_default_data()
        except json.JSONDecodeError:
            print("\n[경고] 데이터 파일이 손상되었습니다. 기본 데이터로 복구합니다.")
            self._init_default_data()
        except Exception as e:
            print(f"\n[오류] 데이터를 불러오는 중 알 수 없는 오류가 발생했습니다: {e}")
            self._init_default_data()

    def save_data(self):
        """
        현재의 퀴즈 목록, 최고 점수, 히스토리를 state.json에 안전하게 저장합니다.
        """
        data = {
            "best_score": self.best_score,
            "history": self.history,
            "quizzes": [quiz.to_dict() for quiz in self.quizzes] # 직렬화
        }
        
        try:
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"\n[오류] 데이터를 저장하는 중 문제가 발생했습니다: {e}")

    def _init_default_data(self):
        """
        파일이 없거나 손상되었을 때 사용할 파이썬/Git 기초 기본 퀴즈 5개입니다.
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
        self.save_data() # 생성 후 바로 파일로 저장

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
            
        # 보너스: 히스토리 저장
        record = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "played": len(play_list),
            "score": score
        }
        self.history.append(record)
        self.save_data()

    def add_quiz(self, question: str, choices: list[str], answer: int, hint: str):
        """
        새로운 퀴즈를 목록에 추가하고 저장합니다.
        """
        new_quiz = Quiz(question, choices, answer, hint)
        self.quizzes.append(new_quiz)
        self.save_data()
        print("\n✅ 퀴즈가 성공적으로 추가되었습니다!")

    """
    def delete_quiz(self, index: int):

        if 0 <= index < len(self.quizzes):
            deleted = self.quizzes.pop(index)
            self.save_data()
            print(f"\n✅ 퀴즈 '{deleted.question}'가 삭제되었습니다.")
        else:
            print("\n❌ 잘못된 번호입니다.")
    """
    def delete_quiz(self, index: int):
        deleted = self.quizzes.pop(index)
        self.save_data()
        print(f"\n✅ 퀴즈 '{deleted.question}'가 삭제되었습니다.")

    def get_score_info(self) -> str:
        """
        최고 점수와 최근 플레이 기록을 포맷팅하여 문자열로 반환합니다.
        """
        info = f"\n🏆 최고 점수: {self.best_score}점\n"
        info += "-" * 30 + "\n"
        if not self.history:
            info += "아직 플레이 기록이 없습니다."
        else:
            info += "📜 최근 플레이 기록 (최대 5개)\n"
            # 최신 기록부터 5개만 보여줌
            for record in reversed(self.history[-5:]):
                info += f"[{record['date']}] {record['played']}문제 풀이 / 점수: {record['score']}점\n"
        return info

    def get_quiz_list(self) -> str:
        """
        현재 등록된 모든 퀴즈의 목록을 반환합니다.
        """
        if not self.quizzes:
            return "등록된 퀴즈가 없습니다."
        
        result = "\n=== 등록된 퀴즈 목록 ===\n"
        for i, quiz in enumerate(self.quizzes):
            result += f"{i + 1}. {quiz.question} (정답: {quiz.answer}번)\n"
        return result