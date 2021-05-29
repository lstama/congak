from problem_generator import generate_sum_problem, generate_substract_problem
from docx_exporter import export_problem_to_docx, export_solution_to_docx
import itertools

easy = generate_sum_problem('x+x', 20)
medium_1 = generate_sum_problem('x+1y', 7)
medium_2 = generate_substract_problem('1y-x', 8)
hard_1 = generate_substract_problem('2y-x', 2)
hard_2 = generate_sum_problem('x+2y', 2)
hard_3 = generate_sum_problem('1y+2y', 2)
hard_4 = generate_substract_problem('2y-1y', 2)
hard_5 = generate_sum_problem('xy+xy', 1)

all_problem = list(itertools.chain(
    easy,
    medium_1,
    medium_2,
    hard_1,
    hard_2,
    hard_3,
    hard_4,
    hard_5
    ))

export_problem_to_docx(all_problem, name='problems_example')
export_solution_to_docx(all_problem, name='solutions_example')
