import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) for the POWL model
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

# Define the silent transitions (no label)
skip = SilentTransition()

# Define the loop nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[artifact_research, ownership_verify, stakeholder_meet, legal_review, diplomatic_contact, condition_report, transport_plan, insurance_setup])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[customs_clear, secure_packaging, shipping_monitor, community_brief, arrival_inspect])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[exhibit_prepare, public_release])

# Define the partial order
root = StrictPartialOrder(nodes=[loop1, loop2, loop3])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)

# Print the root of the POWL model
print(root)