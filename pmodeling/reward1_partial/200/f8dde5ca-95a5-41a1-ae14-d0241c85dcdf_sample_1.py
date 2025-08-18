from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions (activities) for the POWL model
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

# Define the silent transition (skip)
skip = SilentTransition()

# Define the partial order
root = StrictPartialOrder(
    nodes=[
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
    ],
    order=[
        (provenance_check, material_scan),
        (provenance_check, radiocarbon_test),
        (provenance_check, style_compare),
        (provenance_check, database_query),
        (provenance_check, blockchain_prep),
        (provenance_check, legal_review),
        (provenance_check, ownership_audit),
        (provenance_check, conservation_plan),
        (provenance_check, expert_panel),
        (provenance_check, report_draft),
        (provenance_check, client_review),
        (provenance_check, authority_submit),
        (provenance_check, exhibit_setup),
        (provenance_check, final_approval),
        (material_scan, radiocarbon_test),
        (material_scan, style_compare),
        (material_scan, database_query),
        (material_scan, blockchain_prep),
        (material_scan, legal_review),
        (material_scan, ownership_audit),
        (material_scan, conservation_plan),
        (material_scan, expert_panel),
        (material_scan, report_draft),
        (material_scan, client_review),
        (material_scan, authority_submit),
        (material_scan, exhibit_setup),
        (material_scan, final_approval),
        (radiocarbon_test, style_compare),
        (radiocarbon_test, database_query),
        (radiocarbon_test, blockchain_prep),
        (radiocarbon_test, legal_review),
        (radiocarbon_test, ownership_audit),
        (radiocarbon_test, conservation_plan),
        (radiocarbon_test, expert_panel),
        (radiocarbon_test, report_draft),
        (radiocarbon_test, client_review),
        (radiocarbon_test, authority_submit),
        (radiocarbon_test, exhibit_setup),
        (radiocarbon_test, final_approval),
        (style_compare, database_query),
        (style_compare, blockchain_prep),
        (style_compare, legal_review),
        (style_compare, ownership_audit),
        (style_compare, conservation_plan),
        (style_compare, expert_panel),
        (style_compare, report_draft),
        (style_compare, client_review),
        (style_compare, authority_submit),
        (style_compare, exhibit_setup),
        (style_compare, final_approval),
        (database_query, blockchain_prep),
        (database_query, legal_review),
        (database_query, ownership_audit),
        (database_query, conservation_plan),
        (database_query, expert_panel),
        (database_query, report_draft),
        (database_query, client_review),
        (database_query, authority_submit),
        (database_query, exhibit_setup),
        (database_query, final_approval),
        (blockchain_prep, legal_review),
        (blockchain_prep, ownership_audit),
        (blockchain_prep, conservation_plan),
        (blockchain_prep, expert_panel),
        (blockchain_prep, report_draft),
        (blockchain_prep, client_review),
        (blockchain_prep, authority_submit),
        (blockchain_prep, exhibit_setup),
        (blockchain_prep, final_approval),
        (legal_review, ownership_audit),
        (legal_review, conservation_plan),
        (legal_review, expert_panel),
        (legal_review, report_draft),
        (legal_review, client_review),
        (legal_review, authority_submit),
        (legal_review, exhibit_setup),
        (legal_review, final_approval),
        (ownership_audit, conservation_plan),
        (ownership_audit, expert_panel),
        (ownership_audit, report_draft),
        (ownership_audit, client_review),
        (ownership_audit, authority_submit),
        (ownership_audit, exhibit_setup),
        (ownership_audit, final_approval),
        (conservation_plan, expert_panel),
        (conservation_plan, report_draft),
        (conservation_plan, client_review),
        (conservation_plan, authority_submit),
        (conservation_plan, exhibit_setup),
        (conservation_plan, final_approval),
        (expert_panel, report_draft),
        (expert_panel, client_review),
        (expert_panel, authority_submit),
        (expert_panel, exhibit_setup),
        (expert_panel, final_approval),
        (report_draft, client_review),
        (report_draft, authority_submit),
        (report_draft, exhibit_setup),
        (report_draft, final_approval),
        (client_review, authority_submit),
        (client_review, exhibit_setup),
        (client_review, final_approval),
        (authority_submit, exhibit_setup),
        (authority_submit, final_approval),
        (exhibit_setup, final_approval)
    ]
)