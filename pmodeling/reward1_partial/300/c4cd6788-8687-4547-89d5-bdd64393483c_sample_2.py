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

xor1 = OperatorPOWL(operator=Operator.XOR, children=[legal_review, stakeholder_meet])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[diplomatic_contact, condition_report])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[transport_plan, insurance_setup])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[customs_clear, secure_packaging])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[shipping_monitor, community_brief])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[arrival_inspect, exhibit_prepare])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[public_release, skip])

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[xor1, xor2])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[xor3, xor4])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[xor5, xor6])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[xor7, skip])

root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, artifact_research])
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop1, xor2)
root.order.add_edge(loop2, xor3)
root.order.add_edge(loop2, xor4)
root.order.add_edge(loop3, xor5)
root.order.add_edge(loop3, xor6)
root.order.add_edge(loop4, xor7)