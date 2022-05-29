import random

from frame import Frame, MAX_PINS


class Game:

    def __init__(self):
        self.frames = []
        self.current_frame = None

    def next_frame(self):
        if not self.frames:
            self.frames.append(Frame(1, None))
        else:
            previous_frame = self.get_previous_frame()
            previous_frame_number = previous_frame.frame_number
            self.frames.append(
                    Frame(previous_frame_number + 1, previous_frame))

        return self.frames[-1]

    def log_to_console(self):
        self.frames = self.frames[:10]
        print("\n\t\t\t---Bowling Game")
        for frame in self.frames:
            frame.log_to_console()

    def get_previous_frame(self):
        if not self.frames or len(self.frames) < 1:
            return None

        return self.frames[-1]

    def check_create_or_not_next_frame(self):
        if not self.current_frame or self.current_frame.frame_finished():
            self.current_frame = self.next_frame()

    def play_frame_shots(self, pins):
        shot = random.randint(0, 10) if pins < 0 else pins

        self.shot(shot)
        if shot < MAX_PINS:
            shot2 = random.randint(0, 10 - shot)
            self.shot(shot2)
            # in case if current shot ended up in a spare we need another 1 shot for bonus
            if self.current_frame.is_spare():
                return 1
            return 0
        # if its a strike we need to return 2 since bonus depends on next 2 shots
        return 2 

    def shot(self, pins):
        self.check_create_or_not_next_frame()
        self.current_frame.shot(pins)
        if self.current_frame.frame_finished():
            self.current_frame.add_bonus_to_previous_frames()

    def shot_many(self, shots, pins):
        self.run(frames=shots, pins=pins)
        
    def score(self):
        self.log_to_console()
        game_score = 0
        for frame in self.frames:
            game_score += frame.frame_score()
        return game_score

    def run(self, frames=10, pins=-1):
        extra_frames = 0
        for frame in range(frames):
            bonus_shots = self.play_frame_shots(pins)
            if extra_frames > 0:
                extra_frames -= 1
            extra_frames = max(bonus_shots, extra_frames)
        
        if extra_frames > 0:
            for frame in range(extra_frames):
                self.play_frame_shots(pins)