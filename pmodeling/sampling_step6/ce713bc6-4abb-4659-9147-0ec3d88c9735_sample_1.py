from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities as transitions
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

# Add dependencies between activities if any are needed (not specified in the problem statement)
# For example, if historical research must be completed before material sampling:
# root.order.add_edge(document_review, material_sampling)

# If any additional dependencies are needed, add them here.

# Print the root to verify the model
print(root)