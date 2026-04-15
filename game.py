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
        
        # 인스턴스 생성 시 기본 데이터를 바로 세팅합니다.
        self._init_default_data()

    def _init_default_data(self):
        """
        기본으로 제공할 파이썬/Git 기초 퀴즈 5개입니다.
        (추후 파일이 없거나 손상되었을 때 사용하는 용도로 생성.)
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
        # 아직 JSON 파일 저장(save_data) 로직은 없습니다.