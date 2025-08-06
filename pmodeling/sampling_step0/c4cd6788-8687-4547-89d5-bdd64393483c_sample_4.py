import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions for none activities
none_transitions = [SilentTransition()] * 3

# Define exclusive choice between none and the following activities
xor = OperatorPOWL(operator=Operator.XOR, children=none_transitions + [artifact_research, ownership_verify, stakeholder_meet])

# Define loop for legal review and diplomatic contact
loop = OperatorPOWL(operator=Operator.LOOP, children=[legal_review, diplomatic_contact])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)