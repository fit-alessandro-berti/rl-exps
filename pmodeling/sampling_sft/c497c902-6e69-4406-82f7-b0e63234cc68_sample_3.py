import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
artist_check      = Transition(label='Artist Check')
provenance_scan   = Transition(label='Provenance Scan')
document_review   = Transition(label='Document Review')
material_test     = Transition(label='Material Test')
pigment_analysis  = Transition(label='Pigment Analysis')
pattern_detect    = Transition(label='Pattern Detect')
fraud_screening   = Transition(label='Fraud Screening')
legal_compliance  = Transition(label='Legal Compliance')
customs_liaison   = Transition(label='Customs Liaison')
transport_plan    = Transition(label='Transport Plan')
condition_report  = Transition(label='Condition Report')
insurance_setup   = Transition(label='Insurance Setup')
exhibition_prep   = Transition(label='Exhibition Prep')
final_certify     = Transition(label='Final Certify')
stakeholder_notify= Transition(label='Stakeholder Notify')

# Build the loop body (all activities after initial checks)
body = StrictPartialOrder(nodes=[
    material_test, pigment_analysis, pattern_detect,
    fraud_screening, legal_compliance, customs_liaison,
    transport_plan, condition_report, insurance_setup,
    exhibition_prep, final_certify, stakeholder_notify
])
# Define the loop: do initial checks, then repeatedly do body until exit
loop = OperatorPOWL(operator=Operator.LOOP, children=[artist_check, provenance_scan, document_review, body])

# Assemble the top‐level partial order
root = StrictPartialOrder(nodes=[loop])
# Add the control‐flow edges: loop body after initial checks
root.order.add_edge(loop, material_test)
root.order.add_edge(material_test, pigment_analysis)
root.order.add_edge(pigment_analysis, pattern_detect)
root.order.add_edge(pattern_detect, fraud_screening)
root.order.add_edge(fraud_screening, legal_compliance)
root.order.add_edge(legal_compliance, customs_liaison)
root.order.add_edge(customs_liaison, transport_plan)
root.order.add_edge(transport_plan, condition_report)
root.order.add_edge(condition_report, insurance_setup)
root.order.add_edge(insurance_setup, exhibition_prep)
root.order.add_edge(exhibition_prep, final_certify)
root.order.add_edge(final_certify, stakeholder_notify)