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

# Define exclusive choice for fraud screening and legal compliance
exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[fraud_screening, legal_compliance])

# Define loop for material test and pigment analysis
loop_material_test = OperatorPOWL(operator=Operator.LOOP, children=[material_test, pigment_analysis])

# Define partial order structure
root = StrictPartialOrder(nodes=[artist_check, provenance_scan, document_review, exclusive_choice, loop_material_test, customs_liaison, transport_plan, condition_report, insurance_setup, exhibition_prep, final_certify, stakeholder_notify])
root.order.add_edge(artist_check, provenance_scan)
root.order.add_edge(provenance_scan, document_review)
root.order.add_edge(document_review, exclusive_choice)
root.order.add_edge(exclusive_choice, loop_material_test)
root.order.add_edge(loop_material_test, customs_liaison)
root.order.add_edge(customs_liaison, transport_plan)
root.order.add_edge(transport_plan, condition_report)
root.order.add_edge(condition_report, insurance_setup)
root.order.add_edge(insurance_setup, exhibition_prep)
root.order.add_edge(exhibition_prep, final_certify)
root.order.add_edge(final_certify, stakeholder_notify)

print(root)