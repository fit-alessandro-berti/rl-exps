import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities as transitions
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

# Define loop and exclusive choice nodes
loop_collection_survey = OperatorPOWL(operator=Operator.LOOP, children=[collection_survey])
xor_provenance_check = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, skip])
xor_legal_review = OperatorPOWL(operator=Operator.XOR, children=[legal_review, skip])
xor_scientific_test = OperatorPOWL(operator=Operator.XOR, children=[scientific_test, skip])
xor_material_analysis = OperatorPOWL(operator=Operator.XOR, children=[material_analysis, skip])
xor_ownership_audit = OperatorPOWL(operator=Operator.XOR, children=[ownership_audit, skip])
xor_ethical_screening = OperatorPOWL(operator=Operator.XOR, children=[ethical_screening, skip])
xor_condition_report = OperatorPOWL(operator=Operator.XOR, children=[condition_report, skip])
xor_expert_consultation = OperatorPOWL(operator=Operator.XOR, children=[expert_consultation, skip])
xor_transport_planning = OperatorPOWL(operator=Operator.XOR, children=[transport_planning, skip])
xor_secure_packing = OperatorPOWL(operator=Operator.XOR, children=[secure_packing, skip])
xor_customs_clearance = OperatorPOWL(operator=Operator.XOR, children=[customs_clearance, skip])
xor_insurance_setup = OperatorPOWL(operator=Operator.XOR, children=[insurance_setup, skip])
xor_exhibit_preparation = OperatorPOWL(operator=Operator.XOR, children=[exhibit_preparation, skip])
xor_final_approval = OperatorPOWL(operator=Operator.XOR, children=[final_approval, skip])

# Create the root node and define the partial order
root = StrictPartialOrder(nodes=[
    loop_collection_survey,
    xor_provenance_check,
    xor_legal_review,
    xor_scientific_test,
    xor_material_analysis,
    xor_ownership_audit,
    xor_ethical_screening,
    xor_condition_report,
    xor_expert_consultation,
    xor_transport_planning,
    xor_secure_packing,
    xor_customs_clearance,
    xor_insurance_setup,
    xor_exhibit_preparation,
    xor_final_approval
])

# Add dependencies between nodes
root.order.add_edge(loop_collection_survey, xor_provenance_check)
root.order.add_edge(xor_provenance_check, xor_legal_review)
root.order.add_edge(xor_legal_review, xor_scientific_test)
root.order.add_edge(xor_scientific_test, xor_material_analysis)
root.order.add_edge(xor_material_analysis, xor_ownership_audit)
root.order.add_edge(xor_ownership_audit, xor_ethical_screening)
root.order.add_edge(xor_ethical_screening, xor_condition_report)
root.order.add_edge(xor_condition_report, xor_expert_consultation)
root.order.add_edge(xor_expert_consultation, xor_transport_planning)
root.order.add_edge(xor_transport_planning, xor_secure_packing)
root.order.add_edge(xor_secure_packing, xor_customs_clearance)
root.order.add_edge(xor_customs_clearance, xor_insurance_setup)
root.order.add_edge(xor_insurance_setup, xor_exhibit_preparation)
root.order.add_edge(xor_exhibit_preparation, xor_final_approval)