import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
discover_item = Transition(label='Discover Item')
document_find = Transition(label='Document Find')
initial_survey = Transition(label='Initial Survey')
image_capture = Transition(label='Image Capture')
material_testing = Transition(label='Material Testing')
style_compare = Transition(label='Style Compare')
expert_consult = Transition(label='Expert Consult')
provenance_check = Transition(label='Provenance Check')
ownership_verify = Transition(label='Ownership Verify')
legal_review = Transition(label='Legal Review')
risk_assess = Transition(label='Risk Assess')
conservation_plan = Transition(label='Conservation Plan')
certification = Transition(label='Certification')
secure_transfer = Transition(label='Secure Transfer')
dispute_resolve = Transition(label='Dispute Resolve')
final_archive = Transition(label='Final Archive')

# Define silent transitions
skip = SilentTransition()

# Define POWL models for each activity
discover_item_model = StrictPartialOrder(nodes=[discover_item], order=set())
document_find_model = StrictPartialOrder(nodes=[document_find], order=set())
initial_survey_model = StrictPartialOrder(nodes=[initial_survey], order=set())
image_capture_model = StrictPartialOrder(nodes=[image_capture], order=set())
material_testing_model = StrictPartialOrder(nodes=[material_testing], order=set())
style_compare_model = StrictPartialOrder(nodes=[style_compare], order=set())
expert_consult_model = StrictPartialOrder(nodes=[expert_consult], order=set())
provenance_check_model = StrictPartialOrder(nodes=[provenance_check], order=set())
ownership_verify_model = StrictPartialOrder(nodes=[ownership_verify], order=set())
legal_review_model = StrictPartialOrder(nodes=[legal_review], order=set())
risk_assess_model = StrictPartialOrder(nodes=[risk_assess], order=set())
conservation_plan_model = StrictPartialOrder(nodes=[conservation_plan], order=set())
certification_model = StrictPartialOrder(nodes=[certification], order=set())
secure_transfer_model = StrictPartialOrder(nodes=[secure_transfer], order=set())
dispute_resolve_model = StrictPartialOrder(nodes=[dispute_resolve], order=set())
final_archive_model = StrictPartialOrder(nodes=[final_archive], order=set())

# Define exclusive choice nodes
xor1 = OperatorPOWL(operator=Operator.XOR, children=[image_capture_model, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[style_compare_model, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[expert_consult_model, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[provenance_check_model, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[ownership_verify_model, skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[legal_review_model, skip])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess_model, skip])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[conservation_plan_model, skip])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[certification_model, skip])
xor10 = OperatorPOWL(operator=Operator.XOR, children=[secure_transfer_model, skip])
xor11 = OperatorPOWL(operator=Operator.XOR, children=[dispute_resolve_model, skip])
xor12 = OperatorPOWL(operator=Operator.XOR, children=[final_archive_model, skip])

# Define loop nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[xor1, xor2])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[xor3, xor4])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[xor5, xor6])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[xor7, xor8])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[xor9, xor10])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[xor11, xor12])

# Define root POWL model
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5, loop6])
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop1, xor2)
root.order.add_edge(loop2, xor3)
root.order.add_edge(loop2, xor4)
root.order.add_edge(loop3, xor5)
root.order.add_edge(loop3, xor6)
root.order.add_edge(loop4, xor7)
root.order.add_edge(loop4, xor8)
root.order.add_edge(loop5, xor9)
root.order.add_edge(loop5, xor10)
root.order.add_edge(loop6, xor11)
root.order.add_edge(loop6, xor12)