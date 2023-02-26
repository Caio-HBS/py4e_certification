import copy
import random
# Consider using the modules imported above.


class Hat:
    hat_dict = {}
    contents = []

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            self.hat_dict[k] = v

        for ball in self.hat_dict.keys():
            for _ in range(self.hat_dict[ball]):
                self.contents.append(ball)

    def draw(self, number_to_draw):
        draw_list = []
        if number_to_draw > len(self.contents):
            return self.contents
        for i in range(number_to_draw):
            draw_list.append(random.choice(self.contents))
        return draw_list

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    correct = 0
    experiment_dict = {}
    g = 0
    for y in range(num_experiments * 2):
        x = hat.draw(num_balls_drawn)
        for _ in x:
            experiment_dict[x[g]] = experiment_dict.get(x[g], 0) + 1
            g += 1
            if g >= len(x):
                g = 0
            if experiment_dict == expected_balls:
                correct += 1
        experiment_dict = {}
        probability = correct / num_experiments
    return probability
