import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
artist_check = Transition(label='Artist Check')
provenance_scan = Transition(label='Provenance Scan')
document_review = Transition(label='Document Review')
material_test = Transition(label='Material Test')
pigment_analysis = Transition(label='Pigment Analysis')
pattern_detect = Transition(label='Pattern Detect')
fraud_screening = Transition(label='Fraud Screening')
legal_compliance = Transition(label='Legal Compliance')
customs_liaison = Transition(label='Customs Liaison')
transport_plan = Transition(label='Transport Plan')
condition_report = Transition(label='Condition Report')
insurance_setup = Transition(label='Insurance Setup')
exhibition_prep = Transition(label='Exhibition Prep')
final_certify = Transition(label='Final Certify')
stakeholder_notify = Transition(label='Stakeholder Notify')

# Define silent transitions
skip = SilentTransition()

# Define loop nodes for verification and authentication
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[artist_check, provenance_scan, document_review, material_test, pigment_analysis, pattern_detect, fraud_screening, legal_compliance, customs_liaison, transport_plan, condition_report, insurance_setup])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[exhibition_prep, final_certify, stakeholder_notify])

# Define exclusive choice for final certification and stakeholder notification
xor = OperatorPOWL(operator=Operator.XOR, children=[final_certify, stakeholder_notify])

# Define root of the POWL model
root = StrictPartialOrder(nodes=[loop1, loop2, xor])
root.order.add_edge(loop1, xor)

print(root)