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

# Define loop nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[artist_check, provenance_scan])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[document_review, material_test])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[pigment_analysis, pattern_detect])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[fraud_screening, legal_compliance])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[customs_liaison, transport_plan])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[condition_report, insurance_setup])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[exhibition_prep, final_certify])
loop8 = OperatorPOWL(operator=Operator.LOOP, children=[stakeholder_notify, skip])

# Define partial order
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5, loop6, loop7, loop8])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, loop5)
root.order.add_edge(loop5, loop6)
root.order.add_edge(loop6, loop7)
root.order.add_edge(loop7, loop8)
root.order.add_edge(loop8, loop1)