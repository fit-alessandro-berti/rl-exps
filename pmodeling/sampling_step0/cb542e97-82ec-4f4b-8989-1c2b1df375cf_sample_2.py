import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions
skip = SilentTransition()

# Define the loop for material test and archival search
loop_material = OperatorPOWL(operator=Operator.LOOP, children=[material_test, archival_search])

# Define the exclusive choice for style compare and expert review
xor_style_expert = OperatorPOWL(operator=Operator.XOR, children=[style_compare, expert_review])

# Define the exclusive choice for restoration check and provenance trace
xor_restore_prove = OperatorPOWL(operator=Operator.XOR, children=[restoration_check, provenance_trace])

# Define the exclusive choice for legal verify and value appraise
xor_legal_value = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, value_appraise])

# Define the exclusive choice for catalog entry and marketing plan
xor_catalog_marketing = OperatorPOWL(operator=Operator.XOR, children=[catalog_entry, marketing_plan])

# Define the exclusive choice for auction setup and certify final
xor_auction_certify = OperatorPOWL(operator=Operator.XOR, children=[auction_setup, certify_final])

# Define the exclusive choice for sales report and final
xor_sales_final = OperatorPOWL(operator=Operator.XOR, children=[sales_report, certify_final])

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    loop_material, xor_style_expert, xor_restore_prove, xor_legal_value,
    xor_catalog_marketing, xor_auction_certify, xor_sales_final
])

# Define the order dependencies
root.order.add_edge(loop_material, xor_style_expert)
root.order.add_edge(xor_style_expert, xor_restore_prove)
root.order.add_edge(xor_restore_prove, xor_legal_value)
root.order.add_edge(xor_legal_value, xor_catalog_marketing)
root.order.add_edge(xor_catalog_marketing, xor_auction_certify)
root.order.add_edge(xor_auction_certify, xor_sales_final)
root.order.add_edge(xor_sales_final, certify_final)

# Print the root POWL model
print(root)