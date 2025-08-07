import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities
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

# Build the partial order
root = StrictPartialOrder(nodes=[
    artist_check,
    provenance_scan,
    document_review,
    material_test,
    pigment_analysis,
    pattern_detect,
    fraud_screening,
    legal_compliance,
    customs_liaison,
    transport_plan,
    condition_report,
    insurance_setup,
    exhibition_prep,
    final_certify,
    stakeholder_notify
])

# Define the control-flow dependencies
# 1. Artist Check -> Provenance Scan
root.order.add_edge(artist_check, provenance_scan)

# 2. Provenance Scan -> Document Review
root.order.add_edge(provenance_scan, document_review)

# 3. Document Review -> Material Test
root.order.add_edge(document_review, material_test)

# 4. Material Test -> Pigment Analysis
root.order.add_edge(material_test, pigment_analysis)

# 5. Pigment Analysis -> Pattern Detect
root.order.add_edge(pigment_analysis, pattern_detect)

# 6. Pattern Detect -> Fraud Screening
root.order.add_edge(pattern_detect, fraud_screening)

# 7. Fraud Screening -> Legal Compliance
root.order.add_edge(fraud_screening, legal_compliance)

# 8. Legal Compliance -> Customs Liaison
root.order.add_edge(legal_compliance, customs_liaison)

# 9. Customs Liaison -> Transport Plan
root.order.add_edge(customs_liaison, transport_plan)

# 10. Transport Plan -> Condition Report
root.order.add_edge(transport_plan, condition_report)

# 11. Condition Report -> Insurance Setup
root.order.add_edge(condition_report, insurance_setup)

# 12. Insurance Setup -> Exhibition Prep
root.order.add_edge(insurance_setup, exhibition_prep)

# 13. Exhibition Prep -> Final Certify
root.order.add_edge(exhibition_prep, final_certify)

# 14. Final Certify -> Stakeholder Notify
root.order.add_edge(final_certify, stakeholder_notify)

# Final dependencies (optional: all after Final Certify)
for target in [stakeholder_notify]:
    root.order.add_edge(final_certify, target)