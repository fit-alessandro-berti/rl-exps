import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define dependencies between activities
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

root.order.add_edge(initial_inquiry, document_review)
root.order.add_edge(initial_inquiry, historical_research)
root.order.add_edge(initial_inquiry, material_sampling)
root.order.add_edge(initial_inquiry, forensic_testing)
root.order.add_edge(initial_inquiry, ownership_audit)
root.order.add_edge(initial_inquiry, legal_verification)
root.order.add_edge(initial_inquiry, ethical_screening)
root.order.add_edge(initial_inquiry, expert_consultation)
root.order.add_edge(initial_inquiry, cultural_assessment)
root.order.add_edge(initial_inquiry, condition_survey)
root.order.add_edge(initial_inquiry, provenance_mapping)
root.order.add_edge(initial_inquiry, risk_analysis)
root.order.add_edge(initial_inquiry, report_compilation)
root.order.add_edge(initial_inquiry, acquisition_approval)
root.order.add_edge(initial_inquiry, repatriation_review)
root.order.add_edge(initial_inquiry, archival_storage)