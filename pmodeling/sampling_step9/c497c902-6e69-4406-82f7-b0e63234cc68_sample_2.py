import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define loops and choices
loop_artist_check = OperatorPOWL(operator=Operator.LOOP, children=[artist_check, provenance_scan])
loop_document_review = OperatorPOWL(operator=Operator.LOOP, children=[document_review, material_test])
loop_pigment_analysis = OperatorPOWL(operator=Operator.LOOP, children=[pigment_analysis, pattern_detect])
loop_fraud_screening = OperatorPOWL(operator=Operator.LOOP, children=[fraud_screening, legal_compliance])
loop_customs_liaison = OperatorPOWL(operator=Operator.LOOP, children=[customs_liaison, transport_plan])
loop_condition_report = OperatorPOWL(operator=Operator.LOOP, children=[condition_report, insurance_setup])
loop_exhibition_prep = OperatorPOWL(operator=Operator.LOOP, children=[exhibition_prep, final_certify])
loop_stakeholder_notify = OperatorPOWL(operator=Operator.LOOP, children=[stakeholder_notify, skip])

# Define root POWL model
root = StrictPartialOrder(nodes=[loop_artist_check, loop_document_review, loop_pigment_analysis, loop_fraud_screening, loop_customs_liaison, loop_condition_report, loop_exhibition_prep, loop_stakeholder_notify])
root.order.add_edge(loop_artist_check, loop_document_review)
root.order.add_edge(loop_document_review, loop_pigment_analysis)
root.order.add_edge(loop_pigment_analysis, loop_fraud_screening)
root.order.add_edge(loop_fraud_screening, loop_customs_liaison)
root.order.add_edge(loop_customs_liaison, loop_condition_report)
root.order.add_edge(loop_condition_report, loop_exhibition_prep)
root.order.add_edge(loop_exhibition_prep, loop_stakeholder_notify)

# Print the root POWL model
print(root)