import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
initial_inquiry      = Transition(label='Initial Inquiry')
document_review      = Transition(label='Document Review')
historical_research  = Transition(label='Historical Research')
material_sampling    = Transition(label='Material Sampling')
forensic_testing     = Transition(label='Forensic Testing')
ownership_audit      = Transition(label='Ownership Audit')
legal_verification   = Transition(label='Legal Verification')
ethical_screening    = Transition(label='Ethical Screening')
expert_consultation  = Transition(label='Expert Consultation')
cultural_assessment  = Transition(label='Cultural Assessment')
condition_survey     = Transition(label='Condition Survey')
provenance_mapping   = Transition(label='Provenance Mapping')
risk_analysis        = Transition(label='Risk Analysis')
report_compilation   = Transition(label='Report Compilation')
acquisition_approval = Transition(label='Acquisition Approval')
repatriation_review  = Transition(label='Repatriation Review')
archival_storage     = Transition(label='Archival Storage')

# Define the choice for either Acquisition Approval or Repatriation Review
approval_choice = OperatorPOWL(operator=Operator.XOR, children=[acquisition_approval, repatriation_review])

# Build the partial order for the acquisition path
acquisition_po = StrictPartialOrder(nodes=[
    initial_inquiry,
    document_review,
    historical_research,
    material_sampling,
    forensic_testing,
    ownership_audit,
    legal_verification,
    ethical_screening,
    expert_consultation,
    cultural_assessment,
    condition_survey,
    provenance_mapping,
    risk_analysis,
    report_compilation,
    approval_choice
])
# Define the order dependencies for the acquisition path
acquisition_po.order.add_edge(initial_inquiry, document_review)
acquisition_po.order.add_edge(document_review, historical_research)
acquisition_po.order.add_edge(document_review, material_sampling)
acquisition_po.order.add_edge(historical_research, forensic_testing)
acquisition_po.order.add_edge(material_sampling, forensic_testing)
acquisition_po.order.add_edge(forensic_testing, ownership_audit)
acquisition_po.order.add_edge(ownership_audit, legal_verification)
acquisition_po.order.add_edge(legal_verification, ethical_screening)
acquisition_po.order.add_edge(ethical_screening, expert_consultation)
acquisition_po.order.add_edge(expert_consultation, cultural_assessment)
acquisition_po.order.add_edge(cultural_assessment, condition_survey)
acquisition_po.order.add_edge(condition_survey, provenance_mapping)
acquisition_po.order.add_edge(provenance_mapping, risk_analysis)
acquisition_po.order.add_edge(risk_analysis, report_compilation)
acquisition_po.order.add_edge(report_compilation, approval_choice)

# Build the partial order for the repatriation path
repatriation_po = StrictPartialOrder(nodes=[
    initial_inquiry,
    document_review,
    historical_research,
    material_sampling,
    forensic_testing,
    ownership_audit,
    legal_verification,
    ethical_screening,
    expert_consultation,
    cultural_assessment,
    condition_survey,
    provenance_mapping,
    risk_analysis,
    report_compilation,
    repatriation_review
])
# Define the order dependencies for the repatriation path
repatriation_po.order.add_edge(initial_inquiry, document_review)
repatriation_po.order.add_edge(document_review, historical_research)
repatriation_po.order.add_edge(document_review, material_sampling)
repatriation_po.order.add_edge(historical_research, forensic_testing)
repatriation_po.order.add_edge(material_sampling, forensic_testing)
repatriation_po.order.add_edge(forensic_testing, ownership_audit)
repatriation_po.order.add_edge(ownership_audit, legal_verification)
repatriation_po.order.add_edge(legal_verification, ethical_screening)
repatriation_po.order.add_edge(ethical_screening, expert_consultation)
repatriation_po.order.add_edge(expert_consultation, cultural_assessment)
repatriation_po.order.add_edge(cultural_assessment, condition_survey)
repatriation_po.order.add_edge(condition_survey, provenance_mapping)
repatriation_po.order.add_edge(provenance_mapping, risk_analysis)
repatriation_po.order.add_edge(risk_analysis, report_compilation)
repatriation_po.order.add_edge(report_compilation, repatriation_review)

# Final choice between acquisition and repatriation
root = OperatorPOWL(operator=Operator.XOR, children=[acquisition_po, repatriation_po])

# Add archival storage as a post‐process step for both paths
root.order.add_edge(acquisition_po, archival_storage)
root.order.add_edge(repatriation_po, archival_storage)

print(root)