import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
collection_survey      = Transition(label='Collection Survey')
provenance_check       = Transition(label='Provenance Check')
legal_review           = Transition(label='Legal Review')
scientific_test        = Transition(label='Scientific Test')
material_analysis      = Transition(label='Material Analysis')
ownership_audit        = Transition(label='Ownership Audit')
ethical_screening      = Transition(label='Ethical Screening')
condition_report       = Transition(label='Condition Report')
expert_consultation    = Transition(label='Expert Consultation')
transport_planning     = Transition(label='Transport Planning')
secure_packing         = Transition(label='Secure Packing')
customs_clearance      = Transition(label='Customs Clearance')
insurance_setup        = Transition(label='Insurance Setup')
exhibit_preparation    = Transition(label='Exhibit Preparation')
final_approval         = Transition(label='Final Approval')

# Build the loop for scientific testing and material analysis
# Loop: do scientific_test, then optionally do material_analysis and repeat
loop_science = OperatorPOWL(
    operator=Operator.LOOP,
    children=[scientific_test, material_analysis]
)

# Build the choice for ethical screening (either pass or fail)
# XOR: either Ethical Screening or skip (silent transition)
skip = Transition(label='')
xor_ethics = OperatorPOWL(
    operator=Operator.XOR,
    children=[ethical_screening, skip]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    collection_survey,
    provenance_check,
    legal_review,
    loop_science,
    condition_report,
    expert_consultation,
    transport_planning,
    secure_packing,
    customs_clearance,
    insurance_setup,
    exhibit_preparation,
    final_approval
])

# Define the control-flow dependencies
root.order.add_edge(collection_survey, provenance_check)
root.order.add_edge(provenance_check, legal_review)
root.order.add_edge(legal_review, loop_science)
root.order.add_edge(loop_science, condition_report)
root.order.add_edge(condition_report, expert_consultation)
root.order.add_edge(expert_consultation, transport_planning)
root.order.add_edge(transport_planning, secure_packing)
root.order.add_edge(secure_packing, customs_clearance)
root.order.add_edge(customs_clearance, insurance_setup)
root.order.add_edge(insurance_setup, exhibit_preparation)
root.order.add_edge(exhibit_preparation, final_approval)

# Final XOR for ethical screening
root.order.add_edge(loop_science, xor_ethics)
root.order.add_edge(xor_ethics, final_approval)

# Final loop for transport and packing
root.order.add_edge(secure_packing, customs_clearance)
root.order.add_edge(customs_clearance, insurance_setup)
root.order.add_edge(insurance_setup, exhibit_preparation)
root.order.add_edge(exhibit_preparation, final_approval)