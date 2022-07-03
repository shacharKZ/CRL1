import warnings
import random


'''
This function receives the path to a plan file, in the file every line is in the following format:
<robot ID (int)> <x position> <y position> <goal message>
goal message can either be: finish or goal-<id>, where the id is a number representing the goal, regardless of the id of the robot that is set to handle it

This function outputs a dictionary where every key represents a robot and the value is a list of (x,y,goal_message)
'''
def parse_txt_to_plan(plan_path):
    entities_map = {}
    with open(plan_path) as f:
        for line in f:
            line = line.split()
            if len(line) == 0:
                continue
            if len(line) < 3:
                warnings.warn(f'skip un-parseable line: {line}')
            try:
                robot_num = int(line[0])
            except:
                raise "plan did not provide robot ID as Int"
            try:
                x = float(line[1])
                y = float(line[2])
            except:
                raise "plan did not provide position x or y as numeric coordinates"
            goal_message = "" if len(line) < 4 else line[3]
            if robot_num in entities_map:
                entities_map[robot_num].append([x, y, goal_message])
            else:
                entities_map[robot_num] = [[x, y, goal_message]]
    return entities_map


'''
Generate a text file from a dictionary of robot plans (performs the opposite of the parse_txt_to_plan function)
'''
def dict_plan_to_txt(entities_map, path_out):
    if path_out is None or path_out == '':
        return
    with open(path_out, 'w') as f:
        for robot_name in entities_map:
            robot_plan = entities_map[robot_name]
            for task in robot_plan:
                f.write(f'{robot_name} {task[0]} {task[1]}\n')


'''
return a list for commanding a robot to move in a square
'''
def move_square(x, y, leg_len, clockwise=True, delta=0.0):
    plan = [[x+delta, y, '']]
    if delta != 0:
        plan.append([x+delta, y, ''])
    plan.append([x+leg_len, y+delta, ''])
    plan.append([x+leg_len-delta, y+leg_len, ''])
    plan.append([x, y+leg_len-delta, ''])
    if delta != 0:
        plan.append([x, y-delta, ''])
    plan.append([x, y, ''])

    if clockwise:
        plan.reverse()

    return plan

'''
create a mocked plan for the executer
'''
def generate_plan1(path_out=None):
    entities_map = {}
    entities_map[0] = move_square(-0.5, -0.5, 1) + \
                      move_square(-0.5, -1.5, 2, clockwise=False) + \
                      move_square(-0.5, -0.5, -1)
    entities_map[1] = move_square(0.5, 0.5, -1) + \
                      move_square(0.5, 1.5, -2, clockwise=False) + \
                      move_square(0.5, 0.5, 1)

    dict_plan_to_txt(entities_map, path_out)
    return entities_map


'''
create a mocked plan for the executer
'''
def generate_plan2(n_2=3, path_out=None):
    entities_map = {}
    for i in range(n_2):
        for j in range(n_2):
            x = i
            y = j
            if j % 2 == 0:
                entities_map[i*10 + j] = [[x, y, '']] + move_square(x+1, y+0.5, 1)
            else:
                entities_map[i * 10 + j] = [[x, y, '']] + move_square(x+1, y + 0.5, 1)

    dict_plan_to_txt(entities_map, path_out)
    return entities_map


'''
create a mocked (and random) plan for the executer
'''
def generate_random_plan(n_entities, path_out=None):
    entities_map = {}
    for i in range(n_entities):
        x = float(random.randint(-3, 3))
        y = float(random.randint(-3, 3))
        plan = [[x, y, ""]]
        task_number = random.randint(1, 20)
        for j in range(task_number):
            x = x + random.randint(-3, 3)
            y = y + random.randint(-3, 3)
            plan.append([x, y, ""])
        entities_map[i] = plan
    if path_out is not None and path_out != "":
        dict_plan_to_txt(entities_map, path_out)
    return entities_map


def main():
    generate_plan2(path_out='../../../plans_to_run/plan_example1.txt')


if __name__ == '__main__':
    main()
