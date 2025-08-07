from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
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

# Define the partial order workflow
root = StrictPartialOrder(nodes=[
    intake_review, 
    visual_inspect, 
    material_test, 
    provenance_check, 
    archival_search, 
    expert_consult, 
    digital_scan, 
    condition_report, 
    forgeries_assess, 
    legal_review, 
    risk_analysis, 
    acquisition_vote, 
    catalog_entry, 
    storage_prep, 
    final_approval
])

# Add dependencies as per the process description
# Intake Review -> Visual Inspect, Material Test, Provenance Check
root.order.add_edge(intake_review, visual_inspect)
root.order.add_edge(intake_review, material_test)
root.order.add_edge(intake_review, provenance_check)

# Visual Inspect -> Provenance Check, Material Test, Digital Scan, Condition Report
root.order.add_edge(visual_inspect, provenance_check)
root.order.add_edge(visual_inspect, material_test)
root.order.add_edge(visual_inspect, digital_scan)
root.order.add_edge(visual_inspect, condition_report)

# Material Test -> Provenance Check, Digital Scan, Condition Report
root.order.add_edge(material_test, provenance_check)
root.order.add_edge(material_test, digital_scan)
root.order.add_edge(material_test, condition_report)

# Provenance Check -> Archival Search, Expert Consult, Forgeries Assess, Legal Review, Risk Analysis
root.order.add_edge(provenance_check, archival_search)
root.order.add_edge(provenance_check, expert_consult)
root.order.add_edge(provenance_check, forgeries_assess)
root.order.add_edge(provenance_check, legal_review)
root.order.add_edge(provenance_check, risk_analysis)

# Archival Search -> Expert Consult, Forgeries Assess, Legal Review, Risk Analysis
root.order.add_edge(archival_search, expert_consult)
root.order.add_edge(archival_search, forgeries_assess)
root.order.add_edge(archival_search, legal_review)
root.order.add_edge(archival_search, risk_analysis)

# Expert Consult -> Forgeries Assess, Legal Review, Risk Analysis
root.order.add_edge(expert_consult, forgeries_assess)
root.order.add_edge(expert_consult, legal_review)
root.order.add_edge(expert_consult, risk_analysis)

# Digital Scan -> Condition Report
root.order.add_edge(digital_scan, condition_report)

# Condition Report -> Acquisition Vote, Catalog Entry, Storage Prep
root.order.add_edge(condition_report, acquisition_vote)
root.order.add_edge(condition_report, catalog_entry)
root.order.add_edge(condition_report, storage_prep)

# Forgeries Assess -> Legal Review, Risk Analysis
root.order.add_edge(forgeries_assess, legal_review)
root.order.add_edge(forgeries_assess, risk_analysis)

# Legal Review -> Risk Analysis
root.order.add_edge(legal_review, risk_analysis)

# Risk Analysis -> Acquisition Vote
root.order.add_edge(risk_analysis, acquisition_vote)

# Acquisition Vote -> Catalog Entry, Storage Prep
root.order.add_edge(acquisition_vote, catalog_entry)
root.order.add_edge(acquisition_vote, storage_prep)

# Catalog Entry -> Storage Prep
root.order.add_edge(catalog_entry, storage_prep)

# Storage Prep -> Final Approval
root.order.add_edge(storage_prep, final_approval)

# The final result is stored in the 'root' variable