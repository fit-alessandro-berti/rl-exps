import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

# Define loops and XORs for the process
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, legal_review, scientific_test, material_analysis])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[ownership_audit, ethical_screening, condition_report, expert_consultation])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[transport_planning, secure_packing, customs_clearance, insurance_setup])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[exhibit_preparation, final_approval])

xor1 = OperatorPOWL(operator=Operator.XOR, children=[collection_survey, loop1])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[loop2, loop3])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[loop4, skip])

root = StrictPartialOrder(nodes=[xor1, xor2, xor3])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)

print(root)