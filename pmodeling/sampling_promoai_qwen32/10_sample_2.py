import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
submit_request = Transition(label='Submit IT solution request')
assess_compatibility = Transition(label='Assess compatibility')
evaluate_cost = Transition(label='Evaluate cost and resource needs')
procure_tools = Transition(label='Procure necessary tools or licenses')
install_solution = Transition(label='Install the solution')
test_solution = Transition(label='Test solution')
roll_out = Transition(label='Roll out solution to requesting department')
provide_training = Transition(label='Provide training')
provide_support = Transition(label='Provide support for troubleshooting')

# Define the POWL model
root = StrictPartialOrder(nodes=[submit_request, assess_compatibility, evaluate_cost, procure_tools, install_solution, test_solution, roll_out, provide_training, provide_support])
root.order.add_edge(submit_request, assess_compatibility)
root.order.add_edge(assess_compatibility, evaluate_cost)
root.order.add_edge(evaluate_cost, procure_tools)
root.order.add_edge(procure_tools, install_solution)
root.order.add_edge(install_solution, test_solution)
root.order.add_edge(test_solution, roll_out)
root.order.add_edge(roll_out, provide_training)
root.order.add_edge(roll_out, provide_support)
root.order.add_edge(provide_training, provide_support)

# The final result is saved in the variable 'root'