import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the partial order
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

# Since there are no dependencies specified in the problem description, the partial order is already complete.
# If there were dependencies, they would be added here.

# Now, 'root' contains the POWL model for the described process.