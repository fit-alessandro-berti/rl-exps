from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

artifact_research_to_ownership_verify = OperatorPOWL(operator=Operator.XOR, children=[ownership_verify, skip])
ownership_verify_to_stakeholder_meet = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_meet, skip])
stakeholder_meet_to_legal_review = OperatorPOWL(operator=Operator.XOR, children=[legal_review, skip])
legal_review_to_diplomatic_contact = OperatorPOWL(operator=Operator.XOR, children=[diplomatic_contact, skip])
diplomatic_contact_to_condition_report = OperatorPOWL(operator=Operator.XOR, children=[condition_report, skip])
condition_report_to_transport_plan = OperatorPOWL(operator=Operator.XOR, children=[transport_plan, skip])
transport_plan_to_insurance_setup = OperatorPOWL(operator=Operator.XOR, children=[insurance_setup, skip])
insurance_setup_to_customs_clear = OperatorPOWL(operator=Operator.XOR, children=[customs_clear, skip])
customs_clear_to_secure_packaging = OperatorPOWL(operator=Operator.XOR, children=[secure_packaging, skip])
secure_packaging_to_shipping_monitor = OperatorPOWL(operator=Operator.XOR, children=[shipping_monitor, skip])
shipping_monitor_to_community_brief = OperatorPOWL(operator=Operator.XOR, children=[community_brief, skip])
community_brief_to_arrival_inspect = OperatorPOWL(operator=Operator.XOR, children=[arrival_inspect, skip])
arrival_inspect_to_exhibit_prepare = OperatorPOWL(operator=Operator.XOR, children=[exhibit_prepare, skip])
exhibit_prepare_to_public_release = OperatorPOWL(operator=Operator.XOR, children=[public_release, skip])

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

root.order.add_edge(artifact_research, ownership_verify)
root.order.add_edge(ownership_verify, stakeholder_meet)
root.order.add_edge(stakeholder_meet, legal_review)
root.order.add_edge(legal_review, diplomatic_contact)
root.order.add_edge(diplomatic_contact, condition_report)
root.order.add_edge(condition_report, transport_plan)
root.order.add_edge(transport_plan, insurance_setup)
root.order.add_edge(insurance_setup, customs_clear)
root.order.add_edge(customs_clear, secure_packaging)
root.order.add_edge(secure_packaging, shipping_monitor)
root.order.add_edge(shipping_monitor, community_brief)
root.order.add_edge(community_brief, arrival_inspect)
root.order.add_edge(arrival_inspect, exhibit_prepare)
root.order.add_edge(exhibit_prepare, public_release)