from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
client_intake = Transition(label='Client Intake')
needs_analysis = Transition(label='Needs Analysis')
developer_match = Transition(label='Developer Match')
expert_vetting = Transition(label='Expert Vetting')
prototype_build = Transition(label='Prototype Build')
feedback_loop = Transition(label='Feedback Loop')
model_refinement = Transition(label='Model Refinement')
license_draft = Transition(label='License Draft')
ip_negotiation = Transition(label='IP Negotiation')
contract_sign = Transition(label='Contract Sign')
deployment_prep = Transition(label='Deployment Prep')
go_live = Transition(label='Go Live')
monitor_model = Transition(label='Monitor Model')
optimize_ai = Transition(label='Optimize AI')
support_handoff = Transition(label='Support Handoff')
compliance_check = Transition(label='Compliance Check')
final_review = Transition(label='Final Review')

# Define the POWL model
xor = OperatorPOWL(operator=Operator.XOR, children=[client_intake, needs_analysis])
exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[developer_match, expert_vetting, prototype_build])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[feedback_loop, model_refinement])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[license_draft, ip_negotiation])
exclusive_choice2 = OperatorPOWL(operator=Operator.XOR, children=[contract_sign, deployment_prep])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[go_live, monitor_model, optimize_ai])
exclusive_choice3 = OperatorPOWL(operator=Operator.XOR, children=[support_handoff, compliance_check])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[final_review])

# Define the partial order
root = StrictPartialOrder(nodes=[xor, exclusive_choice, xor2, xor3, exclusive_choice2, xor4, exclusive_choice3, xor5])
root.order.add_edge(xor, exclusive_choice)
root.order.add_edge(exclusive_choice, xor2)
root.order.add_edge(exclusive_choice, xor3)
root.order.add_edge(xor2, exclusive_choice2)
root.order.add_edge(xor3, exclusive_choice2)
root.order.add_edge(exclusive_choice2, xor4)
root.order.add_edge(exclusive_choice2, exclusive_choice3)
root.order.add_edge(xor4, xor5)
root.order.add_edge(exclusive_choice3, xor5)

# Print the result
print(root)