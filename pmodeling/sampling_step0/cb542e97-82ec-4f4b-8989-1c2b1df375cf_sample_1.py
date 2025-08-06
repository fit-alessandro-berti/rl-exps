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

# Loops and XORs
artifact_intake_loop = OperatorPOWL(operator=Operator.LOOP, children=[artifact_intake, condition_check])
condition_check_loop = OperatorPOWL(operator=Operator.LOOP, children=[condition_check, material_test])
material_test_loop = OperatorPOWL(operator=Operator.LOOP, children=[material_test, archival_search])
archival_search_loop = OperatorPOWL(operator=Operator.LOOP, children=[archival_search, style_compare])
style_compare_loop = OperatorPOWL(operator=Operator.LOOP, children=[style_compare, expert_review])
expert_review_loop = OperatorPOWL(operator=Operator.LOOP, children=[expert_review, restoration_check])
restoration_check_loop = OperatorPOWL(operator=Operator.LOOP, children=[restoration_check, provenance_trace])
provenance_trace_loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_trace, legal_verify])
legal_verify_loop = OperatorPOWL(operator=Operator.LOOP, children=[legal_verify, value_appraise])
value_appraise_loop = OperatorPOWL(operator=Operator.LOOP, children=[value_appraise, catalog_entry])
catalog_entry_loop = OperatorPOWL(operator=Operator.LOOP, children=[catalog_entry, marketing_plan])
marketing_plan_loop = OperatorPOWL(operator=Operator.LOOP, children=[marketing_plan, auction_setup])
auction_setup_loop = OperatorPOWL(operator=Operator.LOOP, children=[auction_setup, certify_final])
certify_final_loop = OperatorPOWL(operator=Operator.LOOP, children=[certify_final, sales_report])

# Exclusive choices
artifact_intake_xor = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, skip])
condition_check_xor = OperatorPOWL(operator=Operator.XOR, children=[condition_check, skip])
material_test_xor = OperatorPOWL(operator=Operator.XOR, children=[material_test, skip])
archival_search_xor = OperatorPOWL(operator=Operator.XOR, children=[archival_search, skip])
style_compare_xor = OperatorPOWL(operator=Operator.XOR, children=[style_compare, skip])
expert_review_xor = OperatorPOWL(operator=Operator.XOR, children=[expert_review, skip])
restoration_check_xor = OperatorPOWL(operator=Operator.XOR, children=[restoration_check, skip])
provenance_trace_xor = OperatorPOWL(operator=Operator.XOR, children=[provenance_trace, skip])
legal_verify_xor = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, skip])
value_appraise_xor = OperatorPOWL(operator=Operator.XOR, children=[value_appraise, skip])
catalog_entry_xor = OperatorPOWL(operator=Operator.XOR, children=[catalog_entry, skip])
marketing_plan_xor = OperatorPOWL(operator=Operator.XOR, children=[marketing_plan, skip])
auction_setup_xor = OperatorPOWL(operator=Operator.XOR, children=[auction_setup, skip])
certify_final_xor = OperatorPOWL(operator=Operator.XOR, children=[certify_final, skip])
sales_report_xor = OperatorPOWL(operator=Operator.XOR, children=[sales_report, skip])

# Construct the POWL model
root = StrictPartialOrder(nodes=[
    artifact_intake_loop,
    condition_check_loop,
    material_test_loop,
    archival_search_loop,
    style_compare_loop,
    expert_review_loop,
    restoration_check_loop,
    provenance_trace_loop,
    legal_verify_loop,
    value_appraise_loop,
    catalog_entry_loop,
    marketing_plan_loop,
    auction_setup_loop,
    certify_final_loop,
    sales_report_loop
])
root.order.add_edge(artifact_intake_loop, condition_check_loop)
root.order.add_edge(condition_check_loop, material_test_loop)
root.order.add_edge(material_test_loop, archival_search_loop)
root.order.add_edge(archival_search_loop, style_compare_loop)
root.order.add_edge(style_compare_loop, expert_review_loop)
root.order.add_edge(expert_review_loop, restoration_check_loop)
root.order.add_edge(restoration_check_loop, provenance_trace_loop)
root.order.add_edge(provenance_trace_loop, legal_verify_loop)
root.order.add_edge(legal_verify_loop, value_appraise_loop)
root.order.add_edge(value_appraise_loop, catalog_entry_loop)
root.order.add_edge(catalog_entry_loop, marketing_plan_loop)
root.order.add_edge(marketing_plan_loop, auction_setup_loop)
root.order.add_edge(auction_setup_loop, certify_final_loop)
root.order.add_edge(certify_final_loop, sales_report_loop)