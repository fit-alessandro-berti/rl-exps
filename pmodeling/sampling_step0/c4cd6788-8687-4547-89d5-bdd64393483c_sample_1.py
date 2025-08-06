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

# Define silent activities
skip = SilentTransition()

# Define the loop for the transportation phase
transport_loop = OperatorPOWL(operator=Operator.LOOP, children=[secure_packaging, shipping_monitor, arrival_inspect, exhibit_prepare])

# Define the exclusive choice for the legal review phase
legal_exclusive = OperatorPOWL(operator=Operator.XOR, children=[public_release, diplomatic_contact])

# Define the partial order for the entire process
root = StrictPartialOrder(nodes=[transport_loop, legal_exclusive])
root.order.add_edge(transport_loop, legal_exclusive)

# Add edges to connect the activities to the partial order
root.order.add_edge(artifact_research, transport_loop)
root.order.add_edge(ownership_verify, transport_loop)
root.order.add_edge(stakeholder_meet, transport_loop)
root.order.add_edge(legal_review, legal_exclusive)
root.order.add_edge(diplomatic_contact, legal_exclusive)
root.order.add_edge(condition_report, transport_loop)
root.order.add_edge(transport_plan, transport_loop)
root.order.add_edge(insurance_setup, transport_loop)
root.order.add_edge(customs_clear, transport_loop)
root.order.add_edge(secure_packaging, transport_loop)
root.order.add_edge(shipping_monitor, transport_loop)
root.order.add_edge(community_brief, transport_loop)
root.order.add_edge(arrival_inspect, transport_loop)
root.order.add_edge(exhibit_prepare, transport_loop)
root.order.add_edge(public_release, legal_exclusive)

# Print the root POWL model
print(root)