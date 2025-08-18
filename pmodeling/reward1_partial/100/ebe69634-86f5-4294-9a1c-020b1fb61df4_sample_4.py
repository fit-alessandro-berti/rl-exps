import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define the partial order structure
loop_feedback = OperatorPOWL(operator=Operator.LOOP, children=[feedback_loop, model_refinement])
xor_prototype = OperatorPOWL(operator=Operator.XOR, children=[prototype_build, SilentTransition()])
xor_refinement = OperatorPOWL(operator=Operator.XOR, children=[model_refinement, SilentTransition()])
xor_optimize = OperatorPOWL(operator=Operator.XOR, children=[optimize_ai, SilentTransition()])
xor_support = OperatorPOWL(operator=Operator.XOR, children=[support_handoff, SilentTransition()])
xor_compliance = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, SilentTransition()])
xor_final = OperatorPOWL(operator=Operator.XOR, children=[final_review, SilentTransition()])

root = StrictPartialOrder(nodes=[client_intake, needs_analysis, developer_match, expert_vetting,
                                 xor_prototype, loop_feedback, xor_refinement, xor_optimize,
                                 xor_support, xor_compliance, xor_final, contract_sign, deployment_prep, go_live])
root.order.add_edge(client_intake, needs_analysis)
root.order.add_edge(needs_analysis, developer_match)
root.order.add_edge(developer_match, expert_vetting)
root.order.add_edge(expert_vetting, xor_prototype)
root.order.add_edge(xor_prototype, loop_feedback)
root.order.add_edge(loop_feedback, xor_refinement)
root.order.add_edge(xor_refinement, xor_optimize)
root.order.add_edge(xor_optimize, xor_support)
root.order.add_edge(xor_support, xor_compliance)
root.order.add_edge(xor_compliance, xor_final)
root.order.add_edge(xor_final, contract_sign)
root.order.add_edge(contract_sign, deployment_prep)
root.order.add_edge(deployment_prep, go_live)

# Print the root for verification
print(root)