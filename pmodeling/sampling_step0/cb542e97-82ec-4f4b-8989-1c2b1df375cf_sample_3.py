import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the silent transitions
skip = SilentTransition()

# Define the exclusive choice for expert review and restoration check
xor_expert_restoration = OperatorPOWL(operator=Operator.XOR, children=[expert_review, restoration_check])

# Define the loop for archival search and style compare
loop_archival_style = OperatorPOWL(operator=Operator.LOOP, children=[archival_search, style_compare])

# Define the partial order for the entire process
root = StrictPartialOrder(nodes=[artifact_intake, condition_check, material_test, loop_archival_style, xor_expert_restoration, legal_verify, value_appraise, catalog_entry, marketing_plan, auction_setup, certify_final, sales_report])

# Define the order dependencies
root.order.add_edge(artifact_intake, condition_check)
root.order.add_edge(artifact_intake, material_test)
root.order.add_edge(condition_check, material_test)
root.order.add_edge(material_test, loop_archival_style)
root.order.add_edge(loop_archival_style, xor_expert_restoration)
root.order.add_edge(xor_expert_restoration, legal_verify)
root.order.add_edge(legal_verify, value_appraise)
root.order.add_edge(value_appraise, catalog_entry)
root.order.add_edge(catalog_entry, marketing_plan)
root.order.add_edge(marketing_plan, auction_setup)
root.order.add_edge(auction_setup, certify_final)
root.order.add_edge(certify_final, sales_report)

# Print the root of the POWL model
print(root)