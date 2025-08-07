import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) in the POWL model
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

# Define the partial order (POWL model)
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

# Since there are no dependencies specified in the problem, the partial order is already complete
# If dependencies were specified, they would be added here, e.g.:
# root.order.add_edge(artifact_research, ownership_verify)
# ...

# Save the final result in the variable 'root'