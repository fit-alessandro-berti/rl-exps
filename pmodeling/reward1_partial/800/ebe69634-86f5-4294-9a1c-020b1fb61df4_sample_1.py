import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the loop for the model refinement process
loop = OperatorPOWL(operator=Operator.LOOP, children=[model_refinement, feedback_loop])

# Define the exclusive choice for the license drafting and IP negotiation process
xor = OperatorPOWL(operator=Operator.XOR, children=[license_draft, ip_negotiation])

# Define the root POWL model
root = StrictPartialOrder(nodes=[client_intake, needs_analysis, developer_match, expert_vetting, prototype_build, loop, xor, contract_sign, deployment_prep, go_live, monitor_model, optimize_ai, support_handoff, compliance_check, final_review])
root.order.add_edge(client_intake, needs_analysis)
root.order.add_edge(needs_analysis, developer_match)
root.order.add_edge(developer_match, expert_vetting)
root.order.add_edge(expert_vetting, prototype_build)
root.order.add_edge(prototype_build, loop)
root.order.add_edge(loop, feedback_loop)
root.order.add_edge(feedback_loop, model_refinement)
root.order.add_edge(model_refinement, xor)
root.order.add_edge(xor, license_draft)
root.order.add_edge(xor, ip_negotiation)
root.order.add_edge(license_draft, contract_sign)
root.order.add_edge(ip_negotiation, contract_sign)
root.order.add_edge(contract_sign, deployment_prep)
root.order.add_edge(deployment_prep, go_live)
root.order.add_edge(go_live, monitor_model)
root.order.add_edge(monitor_model, optimize_ai)
root.order.add_edge(optimize_ai, support_handoff)
root.order.add_edge(support_handoff, compliance_check)
root.order.add_edge(compliance_check, final_review)

# Print the root POWL model
print(root)