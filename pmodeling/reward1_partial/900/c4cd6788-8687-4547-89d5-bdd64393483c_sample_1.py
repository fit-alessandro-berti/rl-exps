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

# Create the root of the POWL model
root = StrictPartialOrder()

# Add the activities to the root
root.nodes.add(artifact_research)
root.nodes.add(ownership_verify)
root.nodes.add(stakeholder_meet)
root.nodes.add(legal_review)
root.nodes.add(diplomatic_contact)
root.nodes.add(condition_report)
root.nodes.add(transport_plan)
root.nodes.add(insurance_setup)
root.nodes.add(customs_clear)
root.nodes.add(secure_packaging)
root.nodes.add(shipping_monitor)
root.nodes.add(community_brief)
root.nodes.add(arrival_inspect)
root.nodes.add(exhibit_prepare)
root.nodes.add(public_release)

# Define the partial order structure
# Artifact Research -> Ownership Verify
root.order.add_edge(artifact_research, ownership_verify)

# Ownership Verify -> Stakeholder Meet
root.order.add_edge(ownership_verify, stakeholder_meet)

# Stakeholder Meet -> Legal Review
root.order.add_edge(stakeholder_meet, legal_review)

# Legal Review -> Diplomatic Contact
root.order.add_edge(legal_review, diplomatic_contact)

# Diplomatic Contact -> Condition Report
root.order.add_edge(diplomatic_contact, condition_report)

# Condition Report -> Transport Plan
root.order.add_edge(condition_report, transport_plan)

# Transport Plan -> Insurance Setup
root.order.add_edge(transport_plan, insurance_setup)

# Insurance Setup -> Customs Clear
root.order.add_edge(insurance_setup, customs_clear)

# Customs Clear -> Secure Packaging
root.order.add_edge(customs_clear, secure_packaging)

# Secure Packaging -> Shipping Monitor
root.order.add_edge(secure_packaging, shipping_monitor)

# Shipping Monitor -> Community Brief
root.order.add_edge(shipping_monitor, community_brief)

# Community Brief -> Arrival Inspect
root.order.add_edge(community_brief, arrival_inspect)

# Arrival Inspect -> Exhibit Prepare
root.order.add_edge(arrival_inspect, exhibit_prepare)

# Exhibit Prepare -> Public Release
root.order.add_edge(exhibit_prepare, public_release)

# Print the root of the POWL model
print(root)