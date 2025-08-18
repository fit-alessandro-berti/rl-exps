import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

# Define the POWL model
xor1 = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, archive_search, expert_consult])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[material_scan, three_d_imaging, stylistic_match])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[database_query, panel_review])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[certify_report, condition_assess])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[storage_plan, catalog_entry])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[display_prep, loan_arrange])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[monitor_setup])

# Define the partial order
root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5, xor6, xor7])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor1, xor3)
root.order.add_edge(xor2, xor4)
root.order.add_edge(xor2, xor5)
root.order.add_edge(xor3, xor6)
root.order.add_edge(xor3, xor7)
root.order.add_edge(xor4, xor7)
root.order.add_edge(xor5, xor7)
root.order.add_edge(xor6, xor7)

# Print the root node
print(root)