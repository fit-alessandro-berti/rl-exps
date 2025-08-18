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

# Define loops and exclusive choices
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, legal_review])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[ethical_screening, material_analysis])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[scientific_test, condition_report])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[expert_consultation, transport_planning])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[secure_packing, customs_clearance])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[insurance_setup, exhibit_preparation])
xor = OperatorPOWL(operator=Operator.XOR, children=[final_approval, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[collection_survey, loop1, loop2, loop3, loop4, loop5, loop6, xor])
root.order.add_edge(collection_survey, loop1)
root.order.add_edge(collection_survey, loop2)
root.order.add_edge(collection_survey, loop3)
root.order.add_edge(collection_survey, loop4)
root.order.add_edge(collection_survey, loop5)
root.order.add_edge(collection_survey, loop6)
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop1, loop3)
root.order.add_edge(loop1, loop4)
root.order.add_edge(loop1, loop5)
root.order.add_edge(loop1, loop6)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop2, loop4)
root.order.add_edge(loop2, loop5)
root.order.add_edge(loop2, loop6)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop3, loop5)
root.order.add_edge(loop3, loop6)
root.order.add_edge(loop4, loop5)
root.order.add_edge(loop4, loop6)
root.order.add_edge(loop5, loop6)
root.order.add_edge(loop6, xor)

# Print the root POWL model
print(root)