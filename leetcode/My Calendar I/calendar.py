class MyCalendar:

    def __init__(self):
        self.state = []

    def book(self, start: int, end: int) -> bool:
        for state_start, state_end in self.state:
            if start < state_end and end > state_start:
                return False
        else:
            self.state.append([start, end])
            return True
