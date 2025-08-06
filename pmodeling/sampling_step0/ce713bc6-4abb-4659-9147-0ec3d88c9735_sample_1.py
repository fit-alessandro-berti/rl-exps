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

# Define exclusive choice nodes
xor1 = OperatorPOWL(operator=Operator.XOR, children=[ownership_audit, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[legal_verification, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[ethical_screening, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[expert_consultation, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[cultural_assessment, skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[condition_survey, skip])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[provenance_mapping, skip])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[risk_analysis, skip])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[report_compilation, skip])

# Define loop nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[historical_research, xor1])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[material_sampling, xor2])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[forensic_testing, xor3])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[xor4, xor5])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[xor6, xor7])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[xor8, xor9])

# Define the root POWL model
root = StrictPartialOrder(nodes=[initial_inquiry, loop1, loop2, loop3, loop4, loop5, loop6, xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8, xor9, acquisition_approval, repatriation_review, archival_storage])
root.order.add_edge(initial_inquiry, loop1)
root.order.add_edge(initial_inquiry, loop2)
root.order.add_edge(initial_inquiry, loop3)
root.order.add_edge(initial_inquiry, loop4)
root.order.add_edge(initial_inquiry, loop5)
root.order.add_edge(initial_inquiry, loop6)
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop2, xor2)
root.order.add_edge(loop3, xor3)
root.order.add_edge(loop4, xor4)
root.order.add_edge(loop4, xor5)
root.order.add_edge(loop5, xor6)
root.order.add_edge(loop5, xor7)
root.order.add_edge(loop6, xor8)
root.order.add_edge(loop6, xor9)
root.order.add_edge(xor1, acquisition_approval)
root.order.add_edge(xor2, acquisition_approval)
root.order.add_edge(xor3, acquisition_approval)
root.order.add_edge(xor4, repatriation_review)
root.order.add_edge(xor5, repatriation_review)
root.order.add_edge(xor6, repatriation_review)
root.order.add_edge(xor7, repatriation_review)
root.order.add_edge(xor8, archival_storage)
root.order.add_edge(xor9, archival_storage)

# Save the final result in the variable 'root'