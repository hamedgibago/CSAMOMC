from pymoo.factory import get_problem
from pymoo.util.plotting import plot

from pymoo.visualization.fitness_landscape import FitnessLandscape



#problem = get_problem("zdt6",n_var=2)
#plot(problem.pareto_front(), no_fill=True)
#FitnessLandscape(problem, angle=(45, 45), _type="surface").show()


from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.optimize import minimize
from pymoo.visualization.scatter import Scatter

problem = get_problem("zdt6")

algorithm = NSGA2(pop_size=5)

res = minimize(problem,
               algorithm,
               ('n_gen', 500),
               seed=1,
               verbose=True)

plot = Scatter()
plot.add(problem.pareto_front(), plot_type="line", color="black", alpha=0.7)
plot.add(res.F, facecolor="none", edgecolor="red")
plot.show()

