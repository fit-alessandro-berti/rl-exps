import pm4py
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

artifact_research_xor = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_meet, legal_review])
diplomatic_contact_xor = OperatorPOWL(operator=Operator.XOR, children=[diplomatic_contact, condition_report])
transport_plan_xor = OperatorPOWL(operator=Operator.XOR, children=[transport_plan, insurance_setup])
customs_clear_xor = OperatorPOWL(operator=Operator.XOR, children=[customs_clear, secure_packaging])
shipping_monitor_xor = OperatorPOWL(operator=Operator.XOR, children=[shipping_monitor, community_brief])
arrival_inspect_xor = OperatorPOWL(operator=Operator.XOR, children=[arrival_inspect, exhibit_prepare])
public_release_xor = OperatorPOWL(operator=Operator.XOR, children=[public_release, skip])

root = StrictPartialOrder(nodes=[
    artifact_research, ownership_verify, artifact_research_xor, diplomatic_contact_xor, transport_plan_xor, customs_clear_xor, shipping_monitor_xor, arrival_inspect_xor, public_release_xor
])
root.order.add_edge(artifact_research, artifact_research_xor)
root.order.add_edge(ownership_verify, artifact_research_xor)
root.order.add_edge(artifact_research_xor, diplomatic_contact_xor)
root.order.add_edge(diplomatic_contact_xor, transport_plan_xor)
root.order.add_edge(transport_plan_xor, customs_clear_xor)
root.order.add_edge(customs_clear_xor, shipping_monitor_xor)
root.order.add_edge(shipping_monitor_xor, arrival_inspect_xor)
root.order.add_edge(arrival_inspect_xor, public_release_xor)