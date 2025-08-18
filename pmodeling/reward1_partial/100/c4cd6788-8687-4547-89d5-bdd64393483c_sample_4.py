import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the partial order
root = StrictPartialOrder(nodes=[
    artifact_research,
    ownership_verify,
    stakeholder_meet,
    legal_review,
    diplomatic_contact,
    condition_report,
    transport_plan,
    insurance_setup,
    customs_clear,
    secure_packaging,
    shipping_monitor,
    community_brief,
    arrival_inspect,
    exhibit_prepare,
    public_release
])

# Define the dependencies between activities
root.order.add_edge(artifact_research, ownership_verify)
root.order.add_edge(artifact_research, stakeholder_meet)
root.order.add_edge(artifact_research, legal_review)
root.order.add_edge(artifact_research, diplomatic_contact)
root.order.add_edge(artifact_research, condition_report)
root.order.add_edge(artifact_research, transport_plan)
root.order.add_edge(artifact_research, insurance_setup)
root.order.add_edge(artifact_research, customs_clear)
root.order.add_edge(artifact_research, secure_packaging)
root.order.add_edge(artifact_research, shipping_monitor)
root.order.add_edge(artifact_research, community_brief)
root.order.add_edge(artifact_research, arrival_inspect)
root.order.add_edge(artifact_research, exhibit_prepare)
root.order.add_edge(artifact_research, public_release)

root.order.add_edge(ownership_verify, stakeholder_meet)
root.order.add_edge(ownership_verify, legal_review)
root.order.add_edge(ownership_verify, diplomatic_contact)
root.order.add_edge(ownership_verify, condition_report)
root.order.add_edge(ownership_verify, transport_plan)
root.order.add_edge(ownership_verify, insurance_setup)
root.order.add_edge(ownership_verify, customs_clear)
root.order.add_edge(ownership_verify, secure_packaging)
root.order.add_edge(ownership_verify, shipping_monitor)
root.order.add_edge(ownership_verify, community_brief)
root.order.add_edge(ownership_verify, arrival_inspect)
root.order.add_edge(ownership_verify, exhibit_prepare)
root.order.add_edge(ownership_verify, public_release)

root.order.add_edge(stakeholder_meet, legal_review)
root.order.add_edge(stakeholder_meet, diplomatic_contact)
root.order.add_edge(stakeholder_meet, condition_report)
root.order.add_edge(stakeholder_meet, transport_plan)
root.order.add_edge(stakeholder_meet, insurance_setup)
root.order.add_edge(stakeholder_meet, customs_clear)
root.order.add_edge(stakeholder_meet, secure_packaging)
root.order.add_edge(stakeholder_meet, shipping_monitor)
root.order.add_edge(stakeholder_meet, community_brief)
root.order.add_edge(stakeholder_meet, arrival_inspect)
root.order.add_edge(stakeholder_meet, exhibit_prepare)
root.order.add_edge(stakeholder_meet, public_release)

root.order.add_edge(legal_review, diplomatic_contact)
root.order.add_edge(legal_review, condition_report)
root.order.add_edge(legal_review, transport_plan)
root.order.add_edge(legal_review, insurance_setup)
root.order.add_edge(legal_review, customs_clear)
root.order.add_edge(legal_review, secure_packaging)
root.order.add_edge(legal_review, shipping_monitor)
root.order.add_edge(legal_review, community_brief)
root.order.add_edge(legal_review, arrival_inspect)
root.order.add_edge(legal_review, exhibit_prepare)
root.order.add_edge(legal_review, public_release)

root.order.add_edge(diplomatic_contact, condition_report)
root.order.add_edge(diplomatic_contact, transport_plan)
root.order.add_edge(diplomatic_contact, insurance_setup)
root.order.add_edge(diplomatic_contact, customs_clear)
root.order.add_edge(diplomatic_contact, secure_packaging)
root.order.add_edge(diplomatic_contact, shipping_monitor)
root.order.add_edge(diplomatic_contact, community_brief)
root.order.add_edge(diplomatic_contact, arrival_inspect)
root.order.add_edge(diplomatic_contact, exhibit_prepare)
root.order.add_edge(diplomatic_contact, public_release)

root.order.add_edge(condition_report, transport_plan)
root.order.add_edge(condition_report, insurance_setup)
root.order.add_edge(condition_report, customs_clear)
root.order.add_edge(condition_report, secure_packaging)
root.order.add_edge(condition_report, shipping_monitor)
root.order.add_edge(condition_report, community_brief)
root.order.add_edge(condition_report, arrival_inspect)
root.order.add_edge(condition_report, exhibit_prepare)
root.order.add_edge(condition_report, public_release)

root.order.add_edge(transport_plan, insurance_setup)
root.order.add_edge(transport_plan, customs_clear)
root.order.add_edge(transport_plan, secure_packaging)
root.order.add_edge(transport_plan, shipping_monitor)
root.order.add_edge(transport_plan, community_brief)
root.order.add_edge(transport_plan, arrival_inspect)
root.order.add_edge(transport_plan, exhibit_prepare)
root.order.add_edge(transport_plan, public_release)

root.order.add_edge(insurance_setup, customs_clear)
root.order.add_edge(insurance_setup, secure_packaging)
root.order.add_edge(insurance_setup, shipping_monitor)
root.order.add_edge(insurance_setup, community_brief)
root.order.add_edge(insurance_setup, arrival_inspect)
root.order.add_edge(insurance_setup, exhibit_prepare)
root.order.add_edge(insurance_setup, public_release)

root.order.add_edge(customs_clear, secure_packaging)
root.order.add_edge(customs_clear, shipping_monitor)
root.order.add_edge(customs_clear, community_brief)
root.order.add_edge(customs_clear, arrival_inspect)
root.order.add_edge(customs_clear, exhibit_prepare)
root.order.add_edge(customs_clear, public_release)

root.order.add_edge(secure_packaging, shipping_monitor)
root.order.add_edge(secure_packaging, community_brief)
root.order.add_edge(secure_packaging, arrival_inspect)
root.order.add_edge(secure_packaging, exhibit_prepare)
root.order.add_edge(secure_packaging, public_release)

root.order.add_edge(shipping_monitor, community_brief)
root.order.add_edge(shipping_monitor, arrival_inspect)
root.order.add_edge(shipping_monitor, exhibit_prepare)
root.order.add_edge(shipping_monitor, public_release)

root.order.add_edge(community_brief, arrival_inspect)
root.order.add_edge(community_brief, exhibit_prepare)
root.order.add_edge(community_brief, public_release)

root.order.add_edge(arrival_inspect, exhibit_prepare)
root.order.add_edge(arrival_inspect, public_release)

root.order.add_edge(exhibit_prepare, public_release)

print(root)