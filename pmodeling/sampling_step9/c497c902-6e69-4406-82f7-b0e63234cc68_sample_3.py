import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the silent transition (skip)
skip = SilentTransition()

# Define the loop node for fraud screening
fraud_loop = OperatorPOWL(operator=Operator.LOOP, children=[pattern_detect, fraud_screening])

# Define the XOR node for legal compliance and insurance setup
legal_insurance_xor = OperatorPOWL(operator=Operator.XOR, children=[legal_compliance, insurance_setup])

# Define the root POWL model
root = StrictPartialOrder(nodes=[artist_check, provenance_scan, document_review, material_test, pigment_analysis, fraud_loop, transport_plan, condition_report, legal_insurance_xor, exhibition_prep, final_certify, stakeholder_notify])
root.order.add_edge(fraud_loop, legal_insurance_xor)
root.order.add_edge(legal_insurance_xor, exhibition_prep)
root.order.add_edge(exhibition_prep, final_certify)
root.order.add_edge(final_certify, stakeholder_notify)

# Print the root POWL model
print(root)