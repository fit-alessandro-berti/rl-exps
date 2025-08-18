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

initial_inquiry_node = OperatorPOWL(operator=Operator.AND, children=[initial_inquiry, document_review])
historical_research_node = OperatorPOWL(operator=Operator.AND, children=[historical_research, material_sampling, forensic_testing, ownership_audit, legal_verification, ethical_screening, expert_consultation, cultural_assessment, condition_survey, provenance_mapping, risk_analysis, report_compilation, acquisition_approval, repatriation_review, archival_storage])

root = StrictPartialOrder(nodes=[initial_inquiry_node, historical_research_node])
root.order.add_edge(initial_inquiry_node, historical_research_node)