import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
receive = Transition(label='Receive Artifact')
condition_log = Transition(label='Condition Log')
radiocarbon = Transition(label='Radiocarbon Test')
spectroscopy = Transition(label='Spectroscopy Scan')
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

# Build the analysis phase (A)
A = StrictPartialOrder(nodes=[
    radiocarbon, spectroscopy,
    expert_consult, provenance_check,
    archive_search, risk_assess,
    three_d_scan
])
A.order.add_edge(radiocarbon, expert_consult)
A.order.add_edge(spectroscopy, expert_consult)
A.order.add_edge(expert_consult, provenance_check)
A.order.add_edge(provenance_check, archive_search)
A.order.add_edge(provenance_check, risk_assess)
A.order.add_edge(archive_search, three_d_scan)
A.order.add_edge(risk_assess, three_d_scan)

# Build the compliance phase (B)
B = StrictPartialOrder(nodes=[
    legal_review, insurance_setup,
    certificate_draft, certificate_approve
])
B.order.add_edge(legal_review, insurance_setup)
B.order.add_edge(insurance_setup, certificate_draft)
B.order.add_edge(certificate_draft, certificate_approve)

# Build the packaging phase (C)
C = StrictPartialOrder(nodes=[
    climate_pack, conservation_plan,
    monitoring_schedule
])
C.order.add_edge(climate_pack, conservation_plan)
C.order.add_edge(conservation_plan, monitoring_schedule)

# Build the overall process as a loop: receive -> analysis -> compliance -> packaging
root = StrictPartialOrder(nodes=[receive, A, B, C])
root.order.add_edge(receive, A)
root.order.add_edge(receive, B)
root.order.add_edge(receive, C)
root.order.add_edge(A, B)
root.order.add_edge(A, C)
root.order.add_edge(B, C)

# Loop operator: do A, then either exit or do B then A again
loop = OperatorPOWL(operator=Operator.LOOP, children=[A, B])

# Finalize the root partial order with the loop
root.order.add_edge(receive, loop)