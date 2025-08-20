import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
submit_request = Transition(label='Submit IT solution request')
assess_compatibility = Transition(label='Assess compatibility')
evaluate_cost_and_resource_needs = Transition(label='Evaluate cost and resource needs')
procure_tools_or_licenses = Transition(label='Procure necessary tools or licenses')
install_solution = Transition(label='Install the solution')
test_solution = Transition(label='Test solution')
roll_out_solution = Transition(label='Roll out solution to requesting department')
provide_training = Transition(label='Provide training')
provide_support = Transition(label='Provide support for troubleshooting')

# Define the POWL model
xor1 = OperatorPOWL(operator=Operator.XOR, children=[procure_tools_or_licenses, assess_compatibility])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[evaluate_cost_and_resource_needs, install_solution])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[test_solution, xor2])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[xor3, roll_out_solution])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[xor4, provide_training])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[xor5, provide_support])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[xor6, submit_request])

root = StrictPartialOrder(nodes=[xor7])
root.order.add_edge(xor7, xor6)
root.order.add_edge(xor6, xor5)
root.order.add_edge(xor5, xor4)
root.order.add_edge(xor4, xor3)
root.order.add_edge(xor3, xor2)
root.order.add_edge(xor2, xor1)
root.order.add_edge(xor1, submit_request)

print(root)