# congak
Math worksheet generator for first grader. Create addition and/or subtraction worksheet with you own defined pattern, and then generate the .docx files of both the worksheet and the solution. Because this is for first grader, the first number will always bigger than or equal to the second number for subtraction problem.

## Pattern

For each number, you can define the number pattern for the digit.

- Maximum 4 digits per number
- First digit needs to be in range 1 - 9
- x is for 1 - 9 wildcard, can be used for any digit
- y is for 0 - 9 wildcard, can be used at any digit except the first digit)

and then join it with '+' (for addition) or '-' (for substraction).

`x1x+5y` `x+x` `xyy-xy`

## Functions
Then, you can use the pattern for generating problem set by using `problem_generator.generate_<sum/subtract>_problem(pattern, problem_count)`. You can also combine multiple problem set with `list(itertool.chain())`.

After that, you can export the generated worksheet (and solution) to .docx with `docx_exporter.export_<problem/solution>_to_docx(problem_set, filename)`.

## Example:
### Code:
``` python
from problem_generator import generate_sum_problem, generate_substract_problem
from docx_exporter import export_problem_to_docx, export_solution_to_docx
import itertools

easy = generate_sum_problem('x+x', 20)
medium_1 = generate_sum_problem('x+1y', 7)
medium_2 = generate_substract_problem('1y-x', 8)
hard_1 = generate_substract_problem('2y-x', 2)
hard_2 = generate_sum_problem('x+2y', 2)
hard_3 = generate_sum_problem('1y+2y', 1)

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
```

### problems_example.docx
![image](https://user-images.githubusercontent.com/20131054/120083240-7e16b200-c0f1-11eb-9388-5350dc1a4e3d.png)
### solutions_example.docx
![image](https://user-images.githubusercontent.com/20131054/120083262-a7374280-c0f1-11eb-90cf-c8286bbfdd65.png)
