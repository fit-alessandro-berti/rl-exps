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

# Define silent transitions (if any)
skip = SilentTransition()

# Define the POWL model structure
loop_artifact = OperatorPOWL(operator=Operator.LOOP, children=[receive_artifact, condition_log, radiocarbon_test, spectroscopy_scan, expert_consult, provenance_check, archive_search, risk_assess, three_d_scan, legal_review, insurance_setup, certificate_draft, certificate_approve, climate_pack, conservation_plan, monitoring_schedule])

xor_legal_review = OperatorPOWL(operator=Operator.XOR, children=[legal_review, skip])

root = StrictPartialOrder(nodes=[loop_artifact, xor_legal_review])
root.order.add_edge(loop_artifact, xor_legal_review)