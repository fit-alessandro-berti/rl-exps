import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

historical_research_loop = OperatorPOWL(operator=Operator.LOOP, children=[historical_research])
material_sampling_loop = OperatorPOWL(operator=Operator.LOOP, children=[material_sampling])
forensic_testing_loop = OperatorPOWL(operator=Operator.LOOP, children=[forensic_testing])
ownership_audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[ownership_audit])
legal_verification_loop = OperatorPOWL(operator=Operator.LOOP, children=[legal_verification])
ethical_screening_loop = OperatorPOWL(operator=Operator.LOOP, children=[ethical_screening])
expert_consultation_loop = OperatorPOWL(operator=Operator.LOOP, children=[expert_consultation])
cultural_assessment_loop = OperatorPOWL(operator=Operator.LOOP, children=[cultural_assessment])
condition_survey_loop = OperatorPOWL(operator=Operator.LOOP, children=[condition_survey])
provenance_mapping_loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_mapping])
risk_analysis_loop = OperatorPOWL(operator=Operator.LOOP, children=[risk_analysis])
report_compilation_loop = OperatorPOWL(operator=Operator.LOOP, children=[report_compilation])
acquisition_approval_loop = OperatorPOWL(operator=Operator.LOOP, children=[acquisition_approval])
repatriation_review_loop = OperatorPOWL(operator=Operator.LOOP, children=[repatriation_review])
archival_storage_loop = OperatorPOWL(operator=Operator.LOOP, children=[archival_storage])

root = StrictPartialOrder(nodes=[
    initial_inquiry,
    document_review,
    historical_research_loop,
    material_sampling_loop,
    forensic_testing_loop,
    ownership_audit_loop,
    legal_verification_loop,
    ethical_screening_loop,
    expert_consultation_loop,
    cultural_assessment_loop,
    condition_survey_loop,
    provenance_mapping_loop,
    risk_analysis_loop,
    report_compilation_loop,
    acquisition_approval_loop,
    repatriation_review_loop,
    archival_storage_loop
])
root.order.add_edge(initial_inquiry, document_review)
root.order.add_edge(document_review, historical_research_loop)
root.order.add_edge(historical_research_loop, material_sampling_loop)
root.order.add_edge(material_sampling_loop, forensic_testing_loop)
root.order.add_edge(forensic_testing_loop, ownership_audit_loop)
root.order.add_edge(ownership_audit_loop, legal_verification_loop)
root.order.add_edge(legal_verification_loop, ethical_screening_loop)
root.order.add_edge(ethical_screening_loop, expert_consultation_loop)
root.order.add_edge(expert_consultation_loop, cultural_assessment_loop)
root.order.add_edge(cultural_assessment_loop, condition_survey_loop)
root.order.add_edge(condition_survey_loop, provenance_mapping_loop)
root.order.add_edge(provenance_mapping_loop, risk_analysis_loop)
root.order.add_edge(risk_analysis_loop, report_compilation_loop)
root.order.add_edge(report_compilation_loop, acquisition_approval_loop)
root.order.add_edge(acquisition_approval_loop, repatriation_review_loop)
root.order.add_edge(repatriation_review_loop, archival_storage_loop)

print(root)