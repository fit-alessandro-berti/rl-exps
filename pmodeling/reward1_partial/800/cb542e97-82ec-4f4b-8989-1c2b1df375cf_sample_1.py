import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL nodes
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

# Define the POWL operators
xor = OperatorPOWL(operator=Operator.XOR, children=[provenance_trace, legal_verify])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[restoration_check, material_test])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[value_appraise, catalog_entry])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[marketing_plan, auction_setup])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[certify_final, sales_report])

# Define the POWL partial order
root = StrictPartialOrder(nodes=[artifact_intake, condition_check, material_test, archival_search, style_compare, expert_review, restoration_check, provenance_trace, legal_verify, value_appraise, catalog_entry, marketing_plan, auction_setup, certify_final, sales_report])
root.order.add_edge(artifact_intake, condition_check)
root.order.add_edge(condition_check, material_test)
root.order.add_edge(material_test, archival_search)
root.order.add_edge(archival_search, style_compare)
root.order.add_edge(style_compare, expert_review)
root.order.add_edge(expert_review, restoration_check)
root.order.add_edge(restoration_check, xor)
root.order.add_edge(provenance_trace, xor2)
root.order.add_edge(legal_verify, xor2)
root.order.add_edge(xor2, value_appraise)
root.order.add_edge(value_appraise, xor3)
root.order.add_edge(catalog_entry, xor3)
root.order.add_edge(xor3, marketing_plan)
root.order.add_edge(marketing_plan, xor4)
root.order.add_edge(auction_setup, xor4)
root.order.add_edge(xor4, certify_final)
root.order.add_edge(certify_final, sales_report)