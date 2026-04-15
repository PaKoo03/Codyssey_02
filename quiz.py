class Quiz:
    """
    개별 퀴즈의 상태와 동작을 관리하는 데이터 모델 클래스입니다.
    """

    def __init__(self, question: str, choices: list[str], answer: int, hint: str = ""):
        """
        퀴즈 객체를 초기화합니다.
        
        :param question: 퀴즈 문제 (문자열)
        :param choices: 4개의 선택지가 담긴 리스트
        :param answer: 정답 번호 (1 ~ 4 정수)
        :param hint: 문제 힌트
        """
        # 데이터 무결성을 위한 간단한 검증 로직
        if len(choices) != 4:
            raise ValueError("선택지는 반드시 4개여야 합니다.")
        if not (1 <= answer <= 4):
            raise ValueError("정답은 1에서 4 사이의 정수여야 합니다.")

        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint

    def check_answer(self, user_answer: int) -> bool:
        """
        사용자가 입력한 답이 정답인지 확인합니다.
        """
        return self.answer == user_answer

    def get_hint(self) -> str:
        """
        문제의 힌트를 반환합니다. 등록된 힌트가 없을 경우 안내 메시지를 반환합니다.
        """
        if self.hint:
            return f"💡 힌트: {self.hint}"
        return "💡 이 문제에는 등록된 힌트가 없습니다."

    def display(self):
        """
        퀴즈와 선택지를 화면에 깔끔하게 출력합니다.
        """
        print(f"\nQ. {self.question}")
        for i, choice in enumerate(self.choices, start=1):
            print(f"  {i}) {choice}")