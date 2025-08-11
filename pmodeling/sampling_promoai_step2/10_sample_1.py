import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
submit_request = Transition(label='Submit IT solution request')
assess_compatibility = Transition(label='Assess compatibility')
evaluate_cost_and_resource_needs = Transition(label='Evaluate cost and resource needs')
procure_tools_or_licenses = Transition(label='Procure necessary tools or licenses')
install_solution = Transition(label='Install the solution')
test_solution = Transition(label='Test solution')
roll_out_solution = Transition(label='Roll out solution to requesting department')
provide_training = Transition(label='Provide training')
provide_support = Transition(label='Provide support for troubleshooting')

# Define the partial order
root = StrictPartialOrder(nodes=[
    submit_request, assess_compatibility, evaluate_cost_and_resource_needs,
    procure_tools_or_licenses, install_solution, test_solution, roll_out_solution,
    provide_training, provide_support
])

# Define the dependencies
root.order.add_edge(submit_request, assess_compatibility)
root.order.add_edge(assess_compatibility, evaluate_cost_and_resource_needs)
root.order.add_edge(evaluate_cost_and_resource_needs, procure_tools_or_licenses)
root.order.add_edge(procure_tools_or_licenses, install_solution)
root.order.add_edge(install_solution, test_solution)
root.order.add_edge(test_solution, roll_out_solution)
root.order.add_edge(roll_out_solution, provide_training)
root.order.add_edge(roll_out_solution, provide_support)

print(root)