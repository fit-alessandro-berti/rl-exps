import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
initial_inquiry = Transition(label='Initial Inquiry')
document_review = Transition(label='Document Review')
historical_research = Transition(label='Historical Research')
material_sampling = Transition(label='Material Sampling')
forensic_testing = Transition(label='Forensic Testing')
ownership_audit = Transition(label='Ownership Audit')
legal_verification = Transition(label='Legal Verification')
ethical_screening = Transition(label='Ethical Screening')
expert_consultation = Transition(label='Expert Consultation')
cultural_assessment = Transition(label='Cultural Assessment')
condition_survey = Transition(label='Condition Survey')
provenance_mapping = Transition(label='Provenance Mapping')
risk_analysis = Transition(label='Risk Analysis')
report_compilation = Transition(label='Report Compilation')
acquisition_approval = Transition(label='Acquisition Approval')
repatriation_review = Transition(label='Repatriation Review')
archival_storage = Transition(label='Archival Storage')

# Define the partial order
root = StrictPartialOrder(nodes=[
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
    acquisition_approval,
    repatriation_review,
    archival_storage
])

# Define the dependencies
root.order.add_edge(initial_inquiry, document_review)
root.order.add_edge(document_review, historical_research)
root.order.add_edge(historical_research, material_sampling)
root.order.add_edge(material_sampling, forensic_testing)
root.order.add_edge(forensic_testing, ownership_audit)
root.order.add_edge(ownership_audit, legal_verification)
root.order.add_edge(legal_verification, ethical_screening)
root.order.add_edge(ethical_screening, expert_consultation)
root.order.add_edge(expert_consultation, cultural_assessment)
root.order.add_edge(cultural_assessment, condition_survey)
root.order.add_edge(condition_survey, provenance_mapping)
root.order.add_edge(provenance_mapping, risk_analysis)
root.order.add_edge(risk_analysis, report_compilation)
root.order.add_edge(report_compilation, acquisition_approval)
root.order.add_edge(acquisition_approval, repatriation_review)
root.order.add_edge(repatriation_review, archival_storage)