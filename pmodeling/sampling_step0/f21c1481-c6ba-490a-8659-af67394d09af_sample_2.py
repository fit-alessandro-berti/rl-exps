from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the silent transitions
skip = SilentTransition()

# Define the POWL model
loop_collection_survey = OperatorPOWL(operator=Operator.LOOP, children=[collection_survey, provenance_check])
loop_legal_review = OperatorPOWL(operator=Operator.LOOP, children=[legal_review, scientific_test])
loop_material_analysis = OperatorPOWL(operator=Operator.LOOP, children=[material_analysis, ownership_audit])
loop_ethical_screening = OperatorPOWL(operator=Operator.LOOP, children=[ethical_screening, condition_report])
loop_expert_consultation = OperatorPOWL(operator=Operator.LOOP, children=[expert_consultation, transport_planning])
loop_transport_planning = OperatorPOWL(operator=Operator.LOOP, children=[transport_planning, secure_packing])
loop_secure_packing = OperatorPOWL(operator=Operator.LOOP, children=[secure_packing, customs_clearance])
loop_customs_clearance = OperatorPOWL(operator=Operator.LOOP, children=[customs_clearance, insurance_setup])
loop_insurance_setup = OperatorPOWL(operator=Operator.LOOP, children=[insurance_setup, exhibit_preparation])
loop_exhibit_preparation = OperatorPOWL(operator=Operator.LOOP, children=[exhibit_preparation, final_approval])

root = StrictPartialOrder(nodes=[loop_collection_survey, loop_legal_review, loop_material_analysis, loop_ethical_screening, loop_expert_consultation, loop_transport_planning, loop_secure_packing, loop_customs_clearance, loop_insurance_setup, loop_exhibit_preparation])
root.order.add_edge(loop_collection_survey, loop_legal_review)
root.order.add_edge(loop_legal_review, loop_material_analysis)
root.order.add_edge(loop_material_analysis, loop_ethical_screening)
root.order.add_edge(loop_ethical_screening, loop_expert_consultation)
root.order.add_edge(loop_expert_consultation, loop_transport_planning)
root.order.add_edge(loop_transport_planning, loop_secure_packing)
root.order.add_edge(loop_secure_packing, loop_customs_clearance)
root.order.add_edge(loop_customs_clearance, loop_insurance_setup)
root.order.add_edge(loop_insurance_setup, loop_exhibit_preparation)
root.order.add_edge(loop_exhibit_preparation, final_approval)