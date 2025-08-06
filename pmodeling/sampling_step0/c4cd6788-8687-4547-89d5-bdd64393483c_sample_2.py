import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
artifact_research = Transition(label='Artifact Research')
ownership_verify = Transition(label='Ownership Verify')
stakeholder_meet = Transition(label='Stakeholder Meet')
legal_review = Transition(label='Legal Review')
diplomatic_contact = Transition(label='Diplomatic Contact')
condition_report = Transition(label='Condition Report')
transport_plan = Transition(label='Transport Plan')
insurance_setup = Transition(label='Insurance Setup')
customs_clear = Transition(label='Customs Clear')
secure_packaging = Transition(label='Secure Packaging')
shipping_monitor = Transition(label='Shipping Monitor')
community_brief = Transition(label='Community Brief')
arrival_inspect = Transition(label='Arrival Inspect')
exhibit_prepare = Transition(label='Exhibit Prepare')
public_release = Transition(label='Public Release')

# Define the loop for transportation and verification
transport_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    transport_plan,
    condition_report,
    customs_clear,
    secure_packaging,
    shipping_monitor
])

# Define the choice for legal review and diplomatic contact
legal_diplomatic_choice = OperatorPOWL(operator=Operator.XOR, children=[
    legal_review,
    diplomatic_contact
])

# Define the main root
root = StrictPartialOrder(nodes=[
    artifact_research,
    stakeholder_meet,
    legal_diplomatic_choice,
    transport_loop,
    community_brief,
    arrival_inspect,
    exhibit_prepare,
    public_release
])

# Add the dependencies
root.order.add_edge(artifact_research, stakeholder_meet)
root.order.add_edge(stakeholder_meet, legal_diplomatic_choice)
root.order.add_edge(legal_diplomatic_choice, transport_loop)
root.order.add_edge(transport_loop, community_brief)
root.order.add_edge(community_brief, arrival_inspect)
root.order.add_edge(arrival_inspect, exhibit_prepare)
root.order.add_edge(exhibit_prepare, public_release)

# Print the root model
print(root)