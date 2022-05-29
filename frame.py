MAX_PINS = 10


class Frame(object):

    def __init__(self, frame_number, previous_frame):
        self.first_shot = -1
        self.second_shot = -1
        self.bonus = 0
        self.frame_number = frame_number
        self.previous_frame = previous_frame

    def first_shot_empty(self):
        return self.first_shot == -1

    def second_shot_empty(self):
        return self.second_shot == -1

    def first_shot_score(self):
        if self.first_shot_empty():
            return 0
        return self.first_shot

    def second_shot_score(self):
        if self.second_shot_empty():
            return 0
        return self.second_shot

    def get_frame_number(self):
        return self.frame_number

    def frame_empty(self):
        return self.first_shot_empty()

    def frame_max_pins_cleared(self):
        return self.frame_score() >= MAX_PINS

    def frame_finished(self):
        return not self.second_shot_empty() or self.frame_max_pins_cleared()

    def is_spare(self):
        return self.frame_max_pins_cleared() and not self.second_shot_empty()

    def is_strike(self):
        return self.frame_max_pins_cleared() and self.second_shot_empty()

    def frame_score(self):
        if self.first_shot_empty():
            return 0
        elif self.second_shot_empty():
            return self.first_shot + self.bonus
        else:
            return self.first_shot + self.second_shot + self.bonus

    def game_score(self):
        if not self.previous_frame:
            return self.frame_score()
        return self.frame_score() + self.previous_frame.game_score()

    def shot(self, pins):
        if self.first_shot_empty():
            self.first_shot = pins
            return True
        elif self.second_shot_empty():
            self.second_shot = pins
            return True
        return False

    def add_bonus(self, score):
        self.bonus += score
        if self.bonus > MAX_PINS * 2:
            raise ValueError

    def add_bonus_to_previous_frames(self):
        if not self.previous_frame:
            return
        if self.previous_frame.frame_max_pins_cleared():
            self.previous_frame.add_bonus(self.first_shot_score())
            if self.previous_frame.is_strike():
                self.add_bonus_to_previous_previous_frame(self.first_shot_score())
        if self.previous_frame.is_strike():
            self.previous_frame.add_bonus(self.second_shot_score())

    def add_bonus_to_previous_previous_frame(self, pins):
        prev_previous_frame = self.previous_frame.previous_frame
        if prev_previous_frame and prev_previous_frame.is_strike():
            self.previous_frame.previous_frame.add_bonus(pins)

    def log_to_console(self):
        print("\n\n      <==========>\n\n")
        print("      Frame:", self.frame_number)
        print("      First shot:", self.first_shot_score())
        print("      Second shot:", self.second_shot_score())
        print("      Bonus:", self.bonus)
        print("      Frame-Score:", self.frame_score())
        print("      Game-Score:", self.game_score())
