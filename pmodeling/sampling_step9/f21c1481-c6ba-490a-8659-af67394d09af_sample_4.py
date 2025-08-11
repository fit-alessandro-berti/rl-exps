import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define the loop and choice nodes
loop = OperatorPOWL(operator=Operator.LOOP, children=[collection_survey, provenance_check, legal_review])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[scientific_test, material_analysis])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[ownership_audit, ethical_screening])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[condition_report, expert_consultation])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[transport_planning, secure_packing])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[customs_clearance, insurance_setup])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[exhibit_preparation, final_approval])

# Define the root POWL model
root = StrictPartialOrder(nodes=[loop, xor1, xor2, xor3, xor4, xor5, xor6])
root.order.add_edge(loop, xor1)
root.order.add_edge(loop, xor2)
root.order.add_edge(loop, xor3)
root.order.add_edge(loop, xor4)
root.order.add_edge(loop, xor5)
root.order.add_edge(loop, xor6)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor1, xor3)
root.order.add_edge(xor2, xor4)
root.order.add_edge(xor2, xor5)
root.order.add_edge(xor3, xor6)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, skip)