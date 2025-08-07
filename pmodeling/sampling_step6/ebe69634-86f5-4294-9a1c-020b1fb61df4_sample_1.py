import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define the partial order
root = StrictPartialOrder(nodes=[
    client_intake,
    needs_analysis,
    developer_match,
    expert_vetting,
    prototype_build,
    feedback_loop,
    model_refinement,
    license_draft,
    ip_negotiation,
    contract_sign,
    deployment_prep,
    go_live,
    monitor_model,
    optimize_ai,
    support_handoff,
    compliance_check,
    final_review
])

# Define dependencies (if any)
# In this case, there are no explicit dependencies defined in the description, so we leave the order empty.
# If there were dependencies, they would be added here, e.g., root.order.add_edge(client_intake, needs_analysis)

# Print the root to verify the model
print(root)