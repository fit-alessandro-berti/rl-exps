import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL nodes
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

# Define the POWL operators
xor = OperatorPOWL(operator=Operator.XOR, children=[community_brief, shipping_monitor])
loop = OperatorPOWL(operator=Operator.LOOP, children=[secure_packaging, shipping_monitor])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[condition_report, insurance_setup])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[diplomatic_contact, legal_review])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[public_release, exhibit_prepare])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[arrival_inspect, custom_clear])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[transport_plan, stakeholder_meet])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[ownership_verify, artifact_research])

# Define the root POWL model
root = StrictPartialOrder(nodes=[xor, loop, xor2, xor3, xor4, xor5, xor6, xor7])
root.order.add_edge(xor, loop)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor, xor3)
root.order.add_edge(xor, xor4)
root.order.add_edge(xor, xor5)
root.order.add_edge(xor, xor6)
root.order.add_edge(xor, xor7)