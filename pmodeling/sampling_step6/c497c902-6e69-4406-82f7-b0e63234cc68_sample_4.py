import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the partial order model
root = StrictPartialOrder(nodes=[
    artist_check, provenance_scan, document_review, material_test, pigment_analysis,
    pattern_detect, fraud_screening, legal_compliance, customs_liaison, transport_plan,
    condition_report, insurance_setup, exhibition_prep, final_certify, stakeholder_notify
])

# Define the dependencies between activities (POWL model)
root.order.add_edge(artist_check, provenance_scan)
root.order.add_edge(artist_check, document_review)
root.order.add_edge(artist_check, material_test)
root.order.add_edge(artist_check, pigment_analysis)
root.order.add_edge(artist_check, pattern_detect)
root.order.add_edge(artist_check, fraud_screening)
root.order.add_edge(artist_check, legal_compliance)
root.order.add_edge(artist_check, customs_liaison)
root.order.add_edge(artist_check, transport_plan)
root.order.add_edge(artist_check, condition_report)
root.order.add_edge(artist_check, insurance_setup)
root.order.add_edge(artist_check, exhibition_prep)
root.order.add_edge(artist_check, final_certify)
root.order.add_edge(artist_check, stakeholder_notify)

# Save the final result in the variable 'root'
print(root)