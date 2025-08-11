import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
collection_survey = Transition(label='Collection Survey')
provenance_check = Transition(label='Provenance Check')
legal_review = Transition(label='Legal Review')
scientific_test = Transition(label='Scientific Test')
material_analysis = Transition(label='Material Analysis')
ownership_audit = Transition(label='Ownership Audit')
ethical_screening = Transition(label='Ethical Screening')
condition_report = Transition(label='Condition Report')
expert_consultation = Transition(label='Expert Consultation')
transport_planning = Transition(label='Transport Planning')
secure_packing = Transition(label='Secure Packing')
customs_clearance = Transition(label='Customs Clearance')
insurance_setup = Transition(label='Insurance Setup')
exhibit_preparation = Transition(label='Exhibit Preparation')
final_approval = Transition(label='Final Approval')

# Define silent transitions
skip = SilentTransition()

# Define loop nodes
loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[legal_review, customs_clearance])
loop_2 = OperatorPOWL(operator=Operator.LOOP, children=[material_analysis, ethical_screening])
loop_3 = OperatorPOWL(operator=Operator.LOOP, children=[transport_planning, secure_packing])
loop_4 = OperatorPOWL(operator=Operator.LOOP, children=[condition_report, expert_consultation])

# Define exclusive choices
xor_1 = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, skip])
xor_2 = OperatorPOWL(operator=Operator.XOR, children=[scientific_test, skip])
xor_3 = OperatorPOWL(operator=Operator.XOR, children=[ownership_audit, skip])
xor_4 = OperatorPOWL(operator=Operator.XOR, children=[insurance_setup, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[loop_1, loop_2, loop_3, loop_4, xor_1, xor_2, xor_3, xor_4, final_approval])
root.order.add_edge(loop_1, xor_1)
root.order.add_edge(loop_2, xor_2)
root.order.add_edge(loop_3, xor_3)
root.order.add_edge(loop_4, xor_4)
root.order.add_edge(xor_1, final_approval)
root.order.add_edge(xor_2, final_approval)
root.order.add_edge(xor_3, final_approval)
root.order.add_edge(xor_4, final_approval)

# Print the root POWL model
print(root)