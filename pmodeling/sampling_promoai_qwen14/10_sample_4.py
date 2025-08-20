import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
submit_request = Transition(label='Submit IT solution request')
assess_compatibility = Transition(label='Assess compatibility')
evaluate_cost = Transition(label='Evaluate cost and resource needs')
procure_tools = Transition(label='Procure necessary tools or licenses')
install_solution = Transition(label='Install the solution')
test_solution = Transition(label='Test solution')
roll_out = Transition(label='Roll out solution to requesting department')
provide_training = Transition(label='Provide training')
provide_support = Transition(label='Provide support for troubleshooting')

# Define choices
assess_or_skip = OperatorPOWL(operator=Operator.XOR, children=[assess_compatibility, SilentTransition()])
evaluate_or_skip = OperatorPOWL(operator=Operator.XOR, children=[evaluate_cost, SilentTransition()])
install_or_skip = OperatorPOWL(operator=Operator.XOR, children=[install_solution, SilentTransition()])
test_or_skip = OperatorPOWL(operator=Operator.XOR, children=[test_solution, SilentTransition()])
roll_out_or_skip = OperatorPOWL(operator=Operator.XOR, children=[roll_out, SilentTransition()])
provide_training_or_skip = OperatorPOWL(operator=Operator.XOR, children=[provide_training, SilentTransition()])

# Define loop
install_and_test_loop = OperatorPOWL(operator=Operator.LOOP, children=[install_or_skip, test_or_skip])

# Define root node
root = StrictPartialOrder(nodes=[submit_request, assess_or_skip, evaluate_or_skip, procure_tools, install_and_test_loop, roll_out_or_skip, provide_training_or_skip, provide_support])

# Define dependencies
root.order.add_edge(submit_request, assess_or_skip)
root.order.add_edge(assess_or_skip, evaluate_or_skip)
root.order.add_edge(evaluate_or_skip, procure_tools)
root.order.add_edge(procure_tools, install_and_test_loop)
root.order.add_edge(install_and_test_loop, roll_out_or_skip)
root.order.add_edge(roll_out_or_skip, provide_training_or_skip)
root.order.add_edge(provide_training_or_skip, provide_support)