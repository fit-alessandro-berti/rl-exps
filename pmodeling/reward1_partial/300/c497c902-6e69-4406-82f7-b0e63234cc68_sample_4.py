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

skip = SilentTransition()

# Define the POWL model
xor1 = OperatorPOWL(operator=Operator.XOR, children=[legal_compliance, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[customs_liaison, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[transport_plan, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[condition_report, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[insurance_setup, skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[exhibition_prep, skip])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_notify, skip])

root = StrictPartialOrder(nodes=[
    artist_check,
    provenance_scan,
    document_review,
    material_test,
    pigment_analysis,
    pattern_detect,
    fraud_screening,
    xor1,
    xor2,
    xor3,
    xor4,
    xor5,
    xor6,
    xor7
])

root.order.add_edge(artist_check, provenance_scan)
root.order.add_edge(provenance_scan, document_review)
root.order.add_edge(document_review, material_test)
root.order.add_edge(material_test, pigment_analysis)
root.order.add_edge(pigment_analysis, pattern_detect)
root.order.add_edge(pattern_detect, fraud_screening)
root.order.add_edge(fraud_screening, xor1)
root.order.add_edge(xor1, legal_compliance)
root.order.add_edge(legal_compliance, xor2)
root.order.add_edge(xor2, customs_liaison)
root.order.add_edge(customs_liaison, xor3)
root.order.add_edge(xor3, transport_plan)
root.order.add_edge(transport_plan, xor4)
root.order.add_edge(xor4, condition_report)
root.order.add_edge(condition_report, xor5)
root.order.add_edge(xor5, insurance_setup)
root.order.add_edge(insurance_setup, xor6)
root.order.add_edge(xor6, exhibition_prep)
root.order.add_edge(exhibition_prep, xor7)
root.order.add_edge(xor7, stakeholder_notify)

print(root)