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

# Define a loop for each activity
loop_collection_survey = OperatorPOWL(operator=Operator.LOOP, children=[collection_survey])
loop_provenance_check = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check])
loop_legal_review = OperatorPOWL(operator=Operator.LOOP, children=[legal_review])
loop_scientific_test = OperatorPOWL(operator=Operator.LOOP, children=[scientific_test])
loop_material_analysis = OperatorPOWL(operator=Operator.LOOP, children=[material_analysis])
loop_ownership_audit = OperatorPOWL(operator=Operator.LOOP, children=[ownership_audit])
loop_ethical_screening = OperatorPOWL(operator=Operator.LOOP, children=[ethical_screening])
loop_condition_report = OperatorPOWL(operator=Operator.LOOP, children=[condition_report])
loop_expert_consultation = OperatorPOWL(operator=Operator.LOOP, children=[expert_consultation])
loop_transport_planning = OperatorPOWL(operator=Operator.LOOP, children=[transport_planning])
loop_secure_packing = OperatorPOWL(operator=Operator.LOOP, children=[secure_packing])
loop_customs_clearance = OperatorPOWL(operator=Operator.LOOP, children=[customs_clearance])
loop_insurance_setup = OperatorPOWL(operator=Operator.LOOP, children=[insurance_setup])
loop_exhibit_preparation = OperatorPOWL(operator=Operator.LOOP, children=[exhibit_preparation])
loop_final_approval = OperatorPOWL(operator=Operator.LOOP, children=[final_approval])

# Define the POWL model as a partial order
root = StrictPartialOrder(nodes=[
    loop_collection_survey,
    loop_provenance_check,
    loop_legal_review,
    loop_scientific_test,
    loop_material_analysis,
    loop_ownership_audit,
    loop_ethical_screening,
    loop_condition_report,
    loop_expert_consultation,
    loop_transport_planning,
    loop_secure_packing,
    loop_customs_clearance,
    loop_insurance_setup,
    loop_exhibit_preparation,
    loop_final_approval
])

# Define the partial order structure
root.order.add_edge(loop_collection_survey, loop_provenance_check)
root.order.add_edge(loop_provenance_check, loop_legal_review)
root.order.add_edge(loop_legal_review, loop_scientific_test)
root.order.add_edge(loop_scientific_test, loop_material_analysis)
root.order.add_edge(loop_material_analysis, loop_ownership_audit)
root.order.add_edge(loop_ownership_audit, loop_ethical_screening)
root.order.add_edge(loop_ethical_screening, loop_condition_report)
root.order.add_edge(loop_condition_report, loop_expert_consultation)
root.order.add_edge(loop_expert_consultation, loop_transport_planning)
root.order.add_edge(loop_transport_planning, loop_secure_packing)
root.order.add_edge(loop_secure_packing, loop_customs_clearance)
root.order.add_edge(loop_customs_clearance, loop_insurance_setup)
root.order.add_edge(loop_insurance_setup, loop_exhibit_preparation)
root.order.add_edge(loop_exhibit_preparation, loop_final_approval)

print(root)