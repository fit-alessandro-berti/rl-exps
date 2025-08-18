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

# Define silent transitions
skip = SilentTransition()

# Define partial order nodes and their dependencies
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[historical_research, material_sampling])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[forensic_testing, ownership_audit])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[legal_verification, ethical_screening])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[expert_consultation, cultural_assessment])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[condition_survey, provenance_mapping])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[risk_analysis, report_compilation])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[acquisition_approval, repatriation_review])
loop8 = OperatorPOWL(operator=Operator.LOOP, children=[archival_storage, skip])

# Construct the root partial order
root = StrictPartialOrder(nodes=[initial_inquiry, loop1, loop2, loop3, loop4, loop5, loop6, loop7, loop8])

# Define dependencies between nodes
root.order.add_edge(initial_inquiry, loop1)
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, loop5)
root.order.add_edge(loop5, loop6)
root.order.add_edge(loop6, loop7)
root.order.add_edge(loop7, loop8)
root.order.add_edge(loop8, archival_storage)

print(root)