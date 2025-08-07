import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
initial = Transition(label='Initial Review')
provenance = Transition(label='Provenance Check')
material_scan = Transition(label='Material Scan')
chemical_test = Transition(label='Chemical Test')
imaging_capture = Transition(label='Imaging Capture')
expert_consult = Transition(label='Expert Consult')
historical_match = Transition(label='Historical Match')
forgery_detect = Transition(label='Forgery Detect')
documentation_verify = Transition(label='Documentation Verify')
cross_border = Transition(label='Cross-Border Check')
condition_assess = Transition(label='Condition Assess')
value_estimate = Transition(label='Value Estimate')
report_draft = Transition(label='Report Draft')
report_review = Transition(label='Report Review')
client_approval = Transition(label='Client Approval')
certification_issue = Transition(label='Certification Issue')
archive_record = Transition(label='Archive Record')

# Build the loop for iterative verification and detection
# A: Initial Review -> Provenance Check -> Material Scan -> Chemical Test -> Imaging Capture
A = StrictPartialOrder(nodes=[initial, provenance, material_scan, chemical_test, imaging_capture])
A.order.add_edge(initial, provenance)
A.order.add_edge(provenance, material_scan)
A.order.add_edge(material_scan, chemical_test)
A.order.add_edge(chemical_test, imaging_capture)

# B: Forgery Detect -> Historical Match -> Documentation Verify -> Cross-Border Check
B = StrictPartialOrder(nodes=[forgery_detect, historical_match, documentation_verify, cross_border])
B.order.add_edge(forgery_detect, historical_match)
B.order.add_edge(historical_match, documentation_verify)
B.order.add_edge(documentation_verify, cross_border)

# LOOP: execute A, then either exit or execute B then A again
loop = OperatorPOWL(operator=Operator.LOOP, children=[A, B])

# C: Condition Assess -> Value Estimate -> Report Draft
C = StrictPartialOrder(nodes=[condition_assess, value_estimate, report_draft])
C.order.add_edge(condition_assess, value_estimate)
C.order.add_edge(value_estimate, report_draft)

# D: Report Review -> Client Approval
D = StrictPartialOrder(nodes=[report_review, client_approval])
D.order.add_edge(report_review, client_approval)

# E: Certification Issue -> Archive Record
E = StrictPartialOrder(nodes=[certification_issue, archive_record])
E.order.add_edge(certification_issue, archive_record)

# Final concurrent sequence: Report Review -> Client Approval -> Certification Issue -> Archive Record
concurrent = StrictPartialOrder(nodes=[D, E])
# No edges means they are concurrent

# Build the top-level partial order
root = StrictPartialOrder(nodes=[loop, C, concurrent])
root.order.add_edge(loop, C)
root.order.add_edge(loop, concurrent)