class Student:
    _first_name: str
    _last_name: str
    _quizz_score: int | float
    _quizz_count: int

    def __init__(self, first_name: str, last_name: str) -> None:
        self._first_name = first_name
        self._last_name = last_name
        self._quizz_score = 0
        self._quizz_count = 0

    def get_name(self) -> str:
        return f'{self._first_name} {self._last_name}'

    def add_quizz(self, score: int | float) -> None:
        self._quizz_score += score
        self._quizz_count += 1

    def get_total_score(self) -> int | float:
        return self._quizz_score

    def get_average_score(self) -> float:
        return self._quizz_score / self._quizz_count
