import warnings
import random


def parse_txt_to_plan(plan_path):
    entities_map = {}
    with open(plan_path) as f:
        for line in f:
            line = line.split()
            if len(line) == 0:
                continue
            if len(line) < 3:
                warnings.warn(f'skip un-parseable line: {line}')
            # print(line)
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


def dict_plan_to_txt(entities_map, path_out):
    if path_out is None or path_out == '':
        return
    with open(path_out, 'w') as f:
        for robot_name in entities_map:
            robot_plan = entities_map[robot_name]
            for task in robot_plan:
                f.write(f'{robot_name} {task[0]} {task[1]}\n')


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


def generate_dance0(path_out=None):
    entities_map = {}
    for i in range(10):
        x = 0
        y = i/2.0 - 7.0
        flag_clockwise = i % 2 == 0
        plan = move_square(x, y, i+0.5, flag_clockwise)
        entities_map[i] = plan
    if path_out is not None and path_out != "":
        with open(path_out, 'w') as f:
            for robot_name in entities_map:
                robot_plan = entities_map[robot_name]
                for task in robot_plan:
                    f.write(f'{robot_name} {task[0]} {task[1]}\n')
    return entities_map


def generate_race_condition_test(n=3, path_out=None):
    entities_map = {}
    for i in range(n):
        plan = [[i, 0, ''], [i+1, 0, ''], [i-1, 0, '']]
        entities_map[i] = plan

    if path_out is not None:
        dict_plan_to_txt(entities_map, path_out)


def generate_dance2(n=2, path_out=None):
    entities_map = {}
    for i in range(n):
        for j in range(n):
            x = i
            y = j
            plan = move_square(x, y, 1, delta=0.5)
            # plan = move_square(x, y, 1, delta=0.5) + move_square(x, y, -1)
            entities_map[i * 10 + j] = plan
    entities_map[1000] = [[0.5, 0.5, '']]
    # for i in range(n):
    #     for j in range(n):
    #         x = i+2
    #         y = j+2
    #         plan = move_square(x, y, 1)
    #         entities_map[i*10+j+100] = plan

    if path_out is not None:
        dict_plan_to_txt(entities_map, path_out)


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


def generate_plan2(n_2=2, path_out=None):
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
    # generate_race_condition_test(n=5, path_out='../../../plans_to_run/test2.txt')
    # generate_dance2(path_out='../../../plans_to_run/plan4.txt')
    # generate_plan1(path_out='../../../plans_to_run/turtlebot3_world_s1.txt')
    generate_plan2(path_out='../../../plans_to_run/plan6.txt')
    # generate_dance(path_out='../../../plans_to_run/dance1.txt')
    # print(generate_plan(n_entities=10, path_out='../../../plans_to_run/plan2.txt'))
    # print('plan0 is:')
    # print(parse_txt_to_plan('../../../plans_to_run/plan0.txt'))


if __name__ == '__main__':
    main()
