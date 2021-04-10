from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(self.read_file())
        self.goto(0, 270)
        self.color('white')
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, 'center', ('Courier', 12, 'bold'))
        self.penup()
        self.speed('fastest')
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, 'center', ('Courier', 12, 'bold'))

    def read_file(self):
        with open('highscore.txt') as file:
            contents = file.read()
            return contents

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def update_high_score(self):
        with open('highscore.txt', mode='w') as file:
            file.write(f'{self.high_score}')
