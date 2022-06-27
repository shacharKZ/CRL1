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


def generate_plan(n_entities, path_out=None):
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
        with open(path_out, 'w') as f:
            for robot_name in entities_map:
                robot_plan = entities_map[robot_name]
                # print(robot_plan)
                for task in robot_plan:
                    # print(task)
                    f.write(f'{robot_name} {task[0]} {task[1]}\n')
    return entities_map


def main():
    print(generate_plan(n_entities=10, path_out='../../../plans_to_run/plan2.txt'))
    # print('plan0 is:')
    # print(parse_txt_to_plan('../../../plans_to_run/plan0.txt'))


if __name__ == '__main__':
    main()
