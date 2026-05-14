import sys
import os
from pathlib import Path


EXPLANATION_TEMPLATE = '''# Explanation

## Pattern


## Idea


## Complexity
- Time: O()
- Space: O()
'''


def create_problem(main_dir: Path, topic: str, problem_id: str, problem_name: str):
    problem_name = '_'.join(map(str.lower, problem_name.split(' ')))
    problem_name = f"{problem_id:0>3}_{problem_name}"

    problem_dir = main_dir / topic / problem_name

    if not os.path.exists(problem_dir):
        problem_dir.mkdir(parents=True)
        for file_name in ('solution_1.py', 'explanation.md', 'notes.md'):
            (problem_dir / file_name).touch()

        with open(problem_dir / 'explanation.md', 'w') as f:
            f.write(EXPLANATION_TEMPLATE)

        print("Files were created successfully")
    
    else:
        solutions_num = len([file_name for file_name in os.listdir(problem_dir) if file_name.startswith('solution')]) + 1
        (problem_dir / f'solution_{solutions_num}.py').touch()
        print(f"File for solution no. {solutions_num} was created")



if __name__=='__main__':
    if len(sys.argv) != 4:
        raise ValueError('The function requires 3 arguments: <topic> <id> <name>')

    cur_dir = Path() / 'problems'
    if not os.path.exists(cur_dir):
        raise FileNotFoundError("Folder \'problems\' doesn't exist")


    topic = sys.argv[1]
    problem_id = sys.argv[2]
    problem_name = sys.argv[3]
    create_problem(cur_dir, topic, problem_id, problem_name)