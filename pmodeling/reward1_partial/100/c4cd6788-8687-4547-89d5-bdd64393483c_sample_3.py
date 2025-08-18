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

# Define silent transitions
skip = SilentTransition()

# Define POWL operators
exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[legal_review, diplomatic_contact])
choice_with_loop = OperatorPOWL(operator=Operator.XOR, children=[transport_plan, exclusive_choice])
loop_for_shipping = OperatorPOWL(operator=Operator.LOOP, children=[shipping_monitor, community_brief])

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    artifact_research,
    ownership_verify,
    stakeholder_meet,
    choice_with_loop,
    loop_for_shipping,
    public_release
])

# Define the order between nodes
root.order.add_edge(artifact_research, ownership_verify)
root.order.add_edge(ownership_verify, stakeholder_meet)
root.order.add_edge(stakeholder_meet, choice_with_loop)
root.order.add_edge(choice_with_loop, loop_for_shipping)
root.order.add_edge(loop_for_shipping, public_release)

print(root)