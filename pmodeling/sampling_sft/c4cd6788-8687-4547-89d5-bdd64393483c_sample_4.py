import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
artifact_research    = Transition(label='Artifact Research')
ownership_verify     = Transition(label='Ownership Verify')
stakeholder_meet     = Transition(label='Stakeholder Meet')
legal_review         = Transition(label='Legal Review')
diplomatic_contact   = Transition(label='Diplomatic Contact')
condition_report     = Transition(label='Condition Report')
transport_plan       = Transition(label='Transport Plan')
insurance_setup      = Transition(label='Insurance Setup')
customs_clear        = Transition(label='Customs Clear')
secure_packaging     = Transition(label='Secure Packaging')
shipping_monitor     = Transition(label='Shipping Monitor')
community_brief      = Transition(label='Community Brief')
arrival_inspect      = Transition(label='Arrival Inspect')
exhibit_prepare      = Transition(label='Exhibit Prepare')
public_release       = Transition(label='Public Release')

# Define the final loop body: Exhibit Prepare -> Public Release
body = StrictPartialOrder(nodes=[exhibit_prepare, public_release])
# No edges => they run in parallel

# Define the LOOP: Secure Packaging -> Shipping Monitor -> (Arrival Inspect -> body)
loop = OperatorPOWL(operator=Operator.LOOP, children=[secure_packaging, shipping_monitor])

# Assemble the overall partial order
root = StrictPartialOrder(nodes=[
    artifact_research, ownership_verify, stakeholder_meet, legal_review, diplomatic_contact,
    condition_report, transport_plan, insurance_setup, customs_clear, loop,
    community_brief, arrival_inspect, exhibit_prepare, public_release
])

# Define the control-flow dependencies
root.order.add_edge(artifact_research, ownership_verify)
root.order.add_edge(artifact_research, stakeholder_meet)
root.order.add_edge(stakeholder_meet, legal_review)
root.order.add_edge(stakeholder_meet, diplomatic_contact)
root.order.add_edge(ownership_verify, condition_report)
root.order.add_edge(ownership_verify, transport_plan)
root.order.add_edge(transport_plan, insurance_setup)
root.order.add_edge(transport_plan, customs_clear)
root.order.add_edge(insurance_setup, loop)
root.order.add_edge(customs_clear, loop)
root.order.add_edge(loop, community_brief)
root.order.add_edge(community_brief, arrival_inspect)
root.order.add_edge(arrival_inspect, exhibit_prepare)
root.order.add_edge(arrival_inspect, public_release)

# The final sequence of the loop body
root.order.add_edge(exhibit_prepare, public_release)

print(root)