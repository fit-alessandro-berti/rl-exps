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

# Define silent transitions
skip = SilentTransition()

# Define the workflow model
loop_model = OperatorPOWL(operator=Operator.LOOP, children=[prototype_build, feedback_loop, model_refinement])
xor_model = OperatorPOWL(operator=Operator.XOR, children=[contract_sign, skip])
xor_model2 = OperatorPOWL(operator=Operator.XOR, children=[go_live, monitor_model])
xor_model3 = OperatorPOWL(operator=Operator.XOR, children=[optimize_ai, support_handoff])
xor_model4 = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, final_review])
root = StrictPartialOrder(nodes=[loop_model, xor_model, xor_model2, xor_model3, xor_model4])
root.order.add_edge(loop_model, xor_model)
root.order.add_edge(loop_model, xor_model2)
root.order.add_edge(loop_model, xor_model3)
root.order.add_edge(loop_model, xor_model4)