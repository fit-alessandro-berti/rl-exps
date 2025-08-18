import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
artifact_intake = Transition(label='Artifact Intake')
provenance_check = Transition(label='Provenance Check')
archive_search = Transition(label='Archive Search')
expert_consult = Transition(label='Expert Consult')
material_scan = Transition(label='Material Scan')
three_d_imaging = Transition(label='3D Imaging')
stylistic_match = Transition(label='Stylistic Match')
database_query = Transition(label='Database Query')
panel_review = Transition(label='Panel Review')
certify_report = Transition(label='Certify Report')
condition_assess = Transition(label='Condition Assess')
storage_plan = Transition(label='Storage Plan')
catalog_entry = Transition(label='Catalog Entry')
display_prep = Transition(label='Display Prep')
loan_arrange = Transition(label='Loan Arrange')
monitor_setup = Transition(label='Monitor Setup')

# Define parallel nodes
parallel_node = OperatorPOWL(operator=Operator.XOR, children=[archive_search, expert_consult])
parallel_node2 = OperatorPOWL(operator=Operator.XOR, children=[material_scan, three_d_imaging])
parallel_node3 = OperatorPOWL(operator=Operator.XOR, children=[stylistic_match, database_query])

# Define loop node
loop_node = OperatorPOWL(operator=Operator.LOOP, children=[panel_review, certify_report, condition_assess, storage_plan, catalog_entry, display_prep, loan_arrange, monitor_setup])

# Define the root
root = StrictPartialOrder(nodes=[artifact_intake, provenance_check, parallel_node, parallel_node2, parallel_node3, loop_node])
root.order.add_edge(artifact_intake, provenance_check)
root.order.add_edge(provenance_check, parallel_node)
root.order.add_edge(parallel_node, parallel_node2)
root.order.add_edge(parallel_node2, parallel_node3)
root.order.add_edge(parallel_node3, loop_node)