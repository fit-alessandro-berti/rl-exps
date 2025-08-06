import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

# Define exclusive choice for fraud screening and legal compliance
xor = OperatorPOWL(operator=Operator.XOR, children=[fraud_screening, legal_compliance])

# Define loop for material test and pigment analysis
loop = OperatorPOWL(operator=Operator.LOOP, children=[material_test, pigment_analysis])

# Define exclusive choice for transport plan and insurance setup
xor2 = OperatorPOWL(operator=Operator.XOR, children=[transport_plan, insurance_setup])

# Define exclusive choice for exhibition prep and final certify
xor3 = OperatorPOWL(operator=Operator.XOR, children=[exhibition_prep, final_certify])

# Define exclusive choice for stakeholder notify and final certify
xor4 = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_notify, final_certify])

# Define loop for custom liaison and document review
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[customs_liaison, document_review])

# Define loop for condition report and stakeholder notify
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[condition_report, stakeholder_notify])

# Define partial order for the entire process
root = StrictPartialOrder(nodes=[artist_check, provenance_scan, xor, loop, xor2, xor3, xor4, loop2, loop3])

# Add edges to the partial order
root.order.add_edge(artist_check, provenance_scan)
root.order.add_edge(provenance_scan, xor)
root.order.add_edge(xor, loop)
root.order.add_edge(loop, material_test)
root.order.add_edge(material_test, pigment_analysis)
root.order.add_edge(pigment_analysis, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, transport_plan)
root.order.add_edge(transport_plan, insurance_setup)
root.order.add_edge(insurance_setup, xor3)
root.order.add_edge(xor3, exhibition_prep)
root.order.add_edge(exhibition_prep, final_certify)
root.order.add_edge(final_certify, xor4)
root.order.add_edge(xor4, stakeholder_notify)
root.order.add_edge(stakeholder_notify, loop2)
root.order.add_edge(loop2, customs_liaison)
root.order.add_edge(customs_liaison, document_review)
root.order.add_edge(document_review, loop3)
root.order.add_edge(loop3, condition_report)
root.order.add_edge(condition_report, stakeholder_notify)