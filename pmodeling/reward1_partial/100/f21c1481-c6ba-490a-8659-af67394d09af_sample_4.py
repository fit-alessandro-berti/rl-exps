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

# Define the POWL model
xor1 = OperatorPOWL(operator=Operator.XOR, children=[legal_review, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[ethical_screening, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[condition_report, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[exhibit_preparation, skip])

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[collection_survey, provenance_check])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[scientific_test, material_analysis])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[ownership_audit, xor1])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[xor2, xor3])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[transport_planning, secure_packing])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[customs_clearance, insurance_setup])

root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5, loop6, final_approval])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, loop5)
root.order.add_edge(loop5, loop6)
root.order.add_edge(loop6, final_approval)

print(root)