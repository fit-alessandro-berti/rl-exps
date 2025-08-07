import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
receive_artifact = Transition(label='Receive Artifact')
condition_log = Transition(label='Condition Log')
radiocarbon_test = Transition(label='Radiocarbon Test')
spectroscopy_scan = Transition(label='Spectroscopy Scan')
expert_consult = Transition(label='Expert Consult')
provenance_check = Transition(label='Provenance Check')
archive_search = Transition(label='Archive Search')
risk_assess = Transition(label='Risk Assess')
three_d_scan = Transition(label='3D Scan')
legal_review = Transition(label='Legal Review')
insurance_setup = Transition(label='Insurance Setup')
certificate_draft = Transition(label='Certificate Draft')
certificate_approve = Transition(label='Certificate Approve')
climate_pack = Transition(label='Climate Pack')
conservation_plan = Transition(label='Conservation Plan')
monitoring_schedule = Transition(label='Monitoring Schedule')

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[
    receive_artifact,
    condition_log,
    radiocarbon_test,
    spectroscopy_scan,
    expert_consult,
    provenance_check,
    archive_search,
    risk_assess,
    three_d_scan,
    legal_review,
    insurance_setup,
    certificate_draft,
    certificate_approve,
    climate_pack,
    conservation_plan,
    monitoring_schedule
])

# Add dependencies between activities if any are required (not specified in the problem statement)
# For example, if there is a dependency between 'Receive Artifact' and 'Condition Log', you would add:
# root.order.add_edge(receive_artifact, condition_log)

# If you need to add more dependencies, you can do so by calling add_edge() method on the order attribute of the root.

# Now, 'root' contains the POWL model for the process described.