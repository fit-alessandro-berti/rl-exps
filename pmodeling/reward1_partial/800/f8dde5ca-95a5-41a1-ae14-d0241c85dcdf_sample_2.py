from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
provenance_check = Transition(label='Provenance Check')
material_scan = Transition(label='Material Scan')
radiocarbon_test = Transition(label='Radiocarbon Test')
style_compare = Transition(label='Style Compare')
database_query = Transition(label='Database Query')
blockchain_prep = Transition(label='Blockchain Prep')
legal_review = Transition(label='Legal Review')
ownership_audit = Transition(label='Ownership Audit')
conservation_plan = Transition(label='Conservation Plan')
expert_panel = Transition(label='Expert Panel')
report_draft = Transition(label='Report Draft')
client_review = Transition(label='Client Review')
authority_submit = Transition(label='Authority Submit')
exhibit_setup = Transition(label='Exhibit Setup')
final_approval = Transition(label='Final Approval')

# Define silent transitions for concurrency
skip = SilentTransition()

# Define the process model
root = StrictPartialOrder(nodes=[
    provenance_check,
    material_scan,
    radiocarbon_test,
    style_compare,
    database_query,
    blockchain_prep,
    legal_review,
    ownership_audit,
    conservation_plan,
    expert_panel,
    report_draft,
    client_review,
    authority_submit,
    exhibit_setup,
    final_approval
])

# Define the control flow
root.order.add_edge(provenance_check, material_scan)
root.order.add_edge(provenance_check, radiocarbon_test)
root.order.add_edge(provenance_check, style_compare)
root.order.add_edge(provenance_check, database_query)
root.order.add_edge(provenance_check, blockchain_prep)
root.order.add_edge(provenance_check, legal_review)
root.order.add_edge(provenance_check, ownership_audit)
root.order.add_edge(provenance_check, conservation_plan)
root.order.add_edge(provenance_check, expert_panel)
root.order.add_edge(provenance_check, report_draft)
root.order.add_edge(provenance_check, client_review)
root.order.add_edge(provenance_check, authority_submit)
root.order.add_edge(provenance_check, exhibit_setup)
root.order.add_edge(provenance_check, final_approval)

root.order.add_edge(material_scan, radiocarbon_test)
root.order.add_edge(material_scan, style_compare)
root.order.add_edge(material_scan, database_query)
root.order.add_edge(material_scan, blockchain_prep)
root.order.add_edge(material_scan, legal_review)
root.order.add_edge(material_scan, ownership_audit)
root.order.add_edge(material_scan, conservation_plan)
root.order.add_edge(material_scan, expert_panel)
root.order.add_edge(material_scan, report_draft)
root.order.add_edge(material_scan, client_review)
root.order.add_edge(material_scan, authority_submit)
root.order.add_edge(material_scan, exhibit_setup)
root.order.add_edge(material_scan, final_approval)

root.order.add_edge(radiocarbon_test, style_compare)
root.order.add_edge(radiocarbon_test, database_query)
root.order.add_edge(radiocarbon_test, blockchain_prep)
root.order.add_edge(radiocarbon_test, legal_review)
root.order.add_edge(radiocarbon_test, ownership_audit)
root.order.add_edge(radiocarbon_test, conservation_plan)
root.order.add_edge(radiocarbon_test, expert_panel)
root.order.add_edge(radiocarbon_test, report_draft)
root.order.add_edge(radiocarbon_test, client_review)
root.order.add_edge(radiocarbon_test, authority_submit)
root.order.add_edge(radiocarbon_test, exhibit_setup)
root.order.add_edge(radiocarbon_test, final_approval)

root.order.add_edge(style_compare, database_query)
root.order.add_edge(style_compare, blockchain_prep)
root.order.add_edge(style_compare, legal_review)
root.order.add_edge(style_compare, ownership_audit)
root.order.add_edge(style_compare, conservation_plan)
root.order.add_edge(style_compare, expert_panel)
root.order.add_edge(style_compare, report_draft)
root.order.add_edge(style_compare, client_review)
root.order.add_edge(style_compare, authority_submit)
root.order.add_edge(style_compare, exhibit_setup)
root.order.add_edge(style_compare, final_approval)

root.order.add_edge(database_query, blockchain_prep)
root.order.add_edge(database_query, legal_review)
root.order.add_edge(database_query, ownership_audit)
root.order.add_edge(database_query, conservation_plan)
root.order.add_edge(database_query, expert_panel)
root.order.add_edge(database_query, report_draft)
root.order.add_edge(database_query, client_review)
root.order.add_edge(database_query, authority_submit)
root.order.add_edge(database_query, exhibit_setup)
root.order.add_edge(database_query, final_approval)

root.order.add_edge(blockchain_prep, legal_review)
root.order.add_edge(blockchain_prep, ownership_audit)
root.order.add_edge(blockchain_prep, conservation_plan)
root.order.add_edge(blockchain_prep, expert_panel)
root.order.add_edge(blockchain_prep, report_draft)
root.order.add_edge(blockchain_prep, client_review)
root.order.add_edge(blockchain_prep, authority_submit)
root.order.add_edge(blockchain_prep, exhibit_setup)
root.order.add_edge(blockchain_prep, final_approval)

root.order.add_edge(legal_review, ownership_audit)
root.order.add_edge(legal_review, conservation_plan)
root.order.add_edge(legal_review, expert_panel)
root.order.add_edge(legal_review, report_draft)
root.order.add_edge(legal_review, client_review)
root.order.add_edge(legal_review, authority_submit)
root.order.add_edge(legal_review, exhibit_setup)
root.order.add_edge(legal_review, final_approval)

root.order.add_edge(ownership_audit, conservation_plan)
root.order.add_edge(ownership_audit, expert_panel)
root.order.add_edge(ownership_audit, report_draft)
root.order.add_edge(ownership_audit, client_review)
root.order.add_edge(ownership_audit, authority_submit)
root.order.add_edge(ownership_audit, exhibit_setup)
root.order.add_edge(ownership_audit, final_approval)

root.order.add_edge(conservation_plan, expert_panel)
root.order.add_edge(conservation_plan, report_draft)
root.order.add_edge(conservation_plan, client_review)
root.order.add_edge(conservation_plan, authority_submit)
root.order.add_edge(conservation_plan, exhibit_setup)
root.order.add_edge(conservation_plan, final_approval)

root.order.add_edge(expert_panel, report_draft)
root.order.add_edge(expert_panel, client_review)
root.order.add_edge(expert_panel, authority_submit)
root.order.add_edge(expert_panel, exhibit_setup)
root.order.add_edge(expert_panel, final_approval)

root.order.add_edge(report_draft, client_review)
root.order.add_edge(report_draft, authority_submit)
root.order.add_edge(report_draft, exhibit_setup)
root.order.add_edge(report_draft, final_approval)

root.order.add_edge(client_review, authority_submit)
root.order.add_edge(client_review, exhibit_setup)
root.order.add_edge(client_review, final_approval)

root.order.add_edge(authority_submit, exhibit_setup)
root.order.add_edge(authority_submit, final_approval)

root.order.add_edge(exhibit_setup, final_approval)