import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

artifact_intake = Transition(label='Artifact Intake')
condition_check = Transition(label='Condition Check')
material_test = Transition(label='Material Test')
archival_search = Transition(label='Archival Search')
style_compare = Transition(label='Style Compare')
expert_review = Transition(label='Expert Review')
restoration_check = Transition(label='Restoration Check')
provenance_trace = Transition(label='Provenance Trace')
legal_verify = Transition(label='Legal Verify')
value_appraise = Transition(label='Value Appraise')
catalog_entry = Transition(label='Catalog Entry')
marketing_plan = Transition(label='Marketing Plan')
auction_setup = Transition(label='Auction Setup')
certify_final = Transition(label='Certify Final')
sales_report = Transition(label='Sales Report')

skip = SilentTransition()

# Loop for material test and archival search
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[material_test, archival_search])

# Choice for style compare and expert review
xor1 = OperatorPOWL(operator=Operator.XOR, children=[style_compare, expert_review])

# Loop for restoration check
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[restoration_check])

# Choice for provenance trace and legal verify
xor2 = OperatorPOWL(operator=Operator.XOR, children=[provenance_trace, legal_verify])

# Choice for value appraise and catalog entry
xor3 = OperatorPOWL(operator=Operator.XOR, children=[value_appraise, catalog_entry])

# Loop for marketing plan
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[marketing_plan])

# Choice for auction setup and certify final
xor4 = OperatorPOWL(operator=Operator.XOR, children=[auction_setup, certify_final])

# Loop for sales report
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[sales_report])

root = StrictPartialOrder(nodes=[artifact_intake, condition_check, loop1, xor1, loop2, xor2, xor3, loop3, xor4, loop4])
root.order.add_edge(artifact_intake, condition_check)
root.order.add_edge(condition_check, loop1)
root.order.add_edge(loop1, xor1)
root.order.add_edge(xor1, loop2)
root.order.add_edge(loop2, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, loop3)
root.order.add_edge(loop3, xor4)
root.order.add_edge(xor4, loop4)
root.order.add_edge(loop4, artifact_intake)