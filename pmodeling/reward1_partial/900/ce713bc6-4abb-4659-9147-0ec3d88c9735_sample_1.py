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

# Define the POWL model structure
xor1 = OperatorPOWL(operator=Operator.XOR, children=[legal_verification, ethical_screening])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[historical_research, condition_survey])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[material_sampling, forensic_testing])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[expert_consultation, cultural_assessment])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[provenance_mapping, risk_analysis])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[report_compilation, acquisition_approval])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[repatriation_review, archival_storage])

# Construct the partial order
root = StrictPartialOrder(nodes=[
    initial_inquiry,
    document_review,
    xor1,
    xor2,
    xor3,
    xor4,
    xor5,
    xor6,
    xor7
])

# Define dependencies
root.order.add_edge(initial_inquiry, document_review)
root.order.add_edge(document_review, xor1)
root.order.add_edge(xor1, legal_verification)
root.order.add_edge(xor1, ethical_screening)
root.order.add_edge(ethical_screening, xor2)
root.order.add_edge(xor2, historical_research)
root.order.add_edge(xor2, condition_survey)
root.order.add_edge(condition_survey, xor3)
root.order.add_edge(xor3, material_sampling)
root.order.add_edge(xor3, forensic_testing)
root.order.add_edge(forensic_testing, xor4)
root.order.add_edge(xor4, expert_consultation)
root.order.add_edge(xor4, cultural_assessment)
root.order.add_edge(cultural_assessment, xor5)
root.order.add_edge(xor5, provenance_mapping)
root.order.add_edge(xor5, risk_analysis)
root.order.add_edge(risk_analysis, xor6)
root.order.add_edge(xor6, report_compilation)
root.order.add_edge(xor6, acquisition_approval)
root.order.add_edge(acquisition_approval, xor7)
root.order.add_edge(xor7, repatriation_review)
root.order.add_edge(xor7, archival_storage)

print(root)