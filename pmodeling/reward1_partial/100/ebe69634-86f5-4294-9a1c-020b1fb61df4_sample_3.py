import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their names
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

# Define the silent transition
skip = SilentTransition()

# Define the loops and exclusive choices
loop_feedback = OperatorPOWL(operator=Operator.LOOP, children=[prototype_build, feedback_loop])
xor_deployment = OperatorPOWL(operator=Operator.XOR, children=[deployment_prep, support_handoff])

# Define the partial order
root = StrictPartialOrder(nodes=[client_intake, needs_analysis, developer_match, expert_vetting, loop_feedback, xor_deployment, license_draft, ip_negotiation, contract_sign, go_live, monitor_model, optimize_ai, support_handoff, compliance_check, final_review])

# Add dependencies
root.order.add_edge(client_intake, needs_analysis)
root.order.add_edge(needs_analysis, developer_match)
root.order.add_edge(developer_match, expert_vetting)
root.order.add_edge(expert_vetting, loop_feedback)
root.order.add_edge(prototype_build, feedback_loop)
root.order.add_edge(feedback_loop, prototype_build)
root.order.add_edge(loop_feedback, xor_deployment)
root.order.add_edge(xor_deployment, license_draft)
root.order.add_edge(license_draft, ip_negotiation)
root.order.add_edge(ip_negotiation, contract_sign)
root.order.add_edge(contract_sign, go_live)
root.order.add_edge(go_live, monitor_model)
root.order.add_edge(monitor_model, optimize_ai)
root.order.add_edge(optimize_ai, support_handoff)
root.order.add_edge(support_handoff, compliance_check)
root.order.add_edge(compliance_check, final_review)

# Print the final POWL model
print(root)