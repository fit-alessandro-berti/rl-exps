import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
intake_review = Transition(label='Intake Review')
visual_inspect = Transition(label='Visual Inspect')
material_test = Transition(label='Material Test')
provenance_check = Transition(label='Provenance Check')
archival_search = Transition(label='Archival Search')
expert_consult = Transition(label='Expert Consult')
digital_scan = Transition(label='Digital Scan')
condition_report = Transition(label='Condition Report')
forgeries_assess = Transition(label='Forgery Assess')
legal_review = Transition(label='Legal Review')
risk_analysis = Transition(label='Risk Analysis')
acquisition_vote = Transition(label='Acquisition Vote')
catalog_entry = Transition(label='Catalog Entry')
storage_prep = Transition(label='Storage Prep')
final_approval = Transition(label='Final Approval')

# Define the workflow
intake_review_to_visual_inspect = OperatorPOWL(operator=Operator.XOR, children=[intake_review, visual_inspect])
visual_inspect_to_material_test = OperatorPOWL(operator=Operator.XOR, children=[visual_inspect, material_test])
material_test_to_provenance_check = OperatorPOWL(operator=Operator.XOR, children=[material_test, provenance_check])
provenance_check_to_archival_search = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, archival_search])
archival_search_to_expert_consult = OperatorPOWL(operator=Operator.XOR, children=[archival_search, expert_consult])
expert_consult_to_digital_scan = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, digital_scan])
digital_scan_to_condition_report = OperatorPOWL(operator=Operator.XOR, children=[digital_scan, condition_report])
condition_report_to_forgeries_assess = OperatorPOWL(operator=Operator.XOR, children=[condition_report, forgeries_assess])
forgeries_assess_to_legal_review = OperatorPOWL(operator=Operator.XOR, children=[forgeries_assess, legal_review])
legal_review_to_risk_analysis = OperatorPOWL(operator=Operator.XOR, children=[legal_review, risk_analysis])
risk_analysis_to_acquisition_vote = OperatorPOWL(operator=Operator.XOR, children=[risk_analysis, acquisition_vote])
acquisition_vote_to_catalog_entry = OperatorPOWL(operator=Operator.XOR, children=[acquisition_vote, catalog_entry])
catalog_entry_to_storage_prep = OperatorPOWL(operator=Operator.XOR, children=[catalog_entry, storage_prep])
storage_prep_to_final_approval = OperatorPOWL(operator=Operator.XOR, children=[storage_prep, final_approval])

# Define the partial order
root = StrictPartialOrder(nodes=[
    intake_review_to_visual_inspect,
    visual_inspect_to_material_test,
    material_test_to_provenance_check,
    provenance_check_to_archival_search,
    archival_search_to_expert_consult,
    expert_consult_to_digital_scan,
    digital_scan_to_condition_report,
    condition_report_to_forgeries_assess,
    forgeries_assess_to_legal_review,
    legal_review_to_risk_analysis,
    risk_analysis_to_acquisition_vote,
    acquisition_vote_to_catalog_entry,
    catalog_entry_to_storage_prep,
    storage_prep_to_final_approval
])

# Define the dependencies
root.order.add_edge(intake_review_to_visual_inspect, visual_inspect_to_material_test)
root.order.add_edge(visual_inspect_to_material_test, material_test_to_provenance_check)
root.order.add_edge(material_test_to_provenance_check, provenance_check_to_archival_search)
root.order.add_edge(provenance_check_to_archival_search, archival_search_to_expert_consult)
root.order.add_edge(archival_search_to_expert_consult, expert_consult_to_digital_scan)
root.order.add_edge(expert_consult_to_digital_scan, digital_scan_to_condition_report)
root.order.add_edge(digital_scan_to_condition_report, condition_report_to_forgeries_assess)
root.order.add_edge(condition_report_to_forgeries_assess, forgeries_assess_to_legal_review)
root.order.add_edge(forgeries_assess_to_legal_review, legal_review_to_risk_analysis)
root.order.add_edge(legal_review_to_risk_analysis, risk_analysis_to_acquisition_vote)
root.order.add_edge(risk_analysis_to_acquisition_vote, acquisition_vote_to_catalog_entry)
root.order.add_edge(acquisition_vote_to_catalog_entry, catalog_entry_to_storage_prep)
root.order.add_edge(catalog_entry_to_storage_prep, storage_prep_to_final_approval)