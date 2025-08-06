import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL nodes
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

# Define the POWL operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[legal_compliance, pattern_detect])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[transport_plan, insurance_setup])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_notify, exhibition_prep])

# Define the POWL model
root = StrictPartialOrder(nodes=[artist_check, provenance_scan, document_review, material_test, pigment_analysis, fraud_screening, xor1, xor2, xor3, final_certify])
root.order.add_edge(artist_check, provenance_scan)
root.order.add_edge(provenance_scan, document_review)
root.order.add_edge(document_review, material_test)
root.order.add_edge(material_test, pigment_analysis)
root.order.add_edge(pigment_analysis, fraud_screening)
root.order.add_edge(fraud_screening, xor1)
root.order.add_edge(legal_compliance, xor1)
root.order.add_edge(pattern_detect, xor1)
root.order.add_edge(transport_plan, xor2)
root.order.add_edge(insurance_setup, xor2)
root.order.add_edge(stakeholder_notify, xor3)
root.order.add_edge(exhibition_prep, xor3)
root.order.add_edge(xor1, final_certify)
root.order.add_edge(xor2, final_certify)
root.order.add_edge(xor3, final_certify)