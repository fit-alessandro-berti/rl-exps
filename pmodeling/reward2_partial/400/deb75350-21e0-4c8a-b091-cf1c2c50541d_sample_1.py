import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
intake_review = Transition(label='Intake Review')
visual_inspect = Transition(label='Visual Inspect')
material_test = Transition(label='Material Test')
provenance_check = Transition(label='Provenance Check')
archival_search = Transition(label='Archival Search')
expert_consult = Transition(label='Expert Consult')
digital_scan = Transition(label='Digital Scan')
condition_report = Transition(label='Condition Report')
forger_assess = Transition(label='Forgery Assess')
legal_review = Transition(label='Legal Review')
risk_analysis = Transition(label='Risk Analysis')
acquisition_vote = Transition(label='Acquisition Vote')
catalog_entry = Transition(label='Catalog Entry')
storage_prep = Transition(label='Storage Prep')
final_approval = Transition(label='Final Approval')

# Define the POWL model
root = StrictPartialOrder(nodes=[
    intake_review,
    visual_inspect,
    material_test,
    provenance_check,
    archival_search,
    expert_consult,
    digital_scan,
    condition_report,
    forger_assess,
    legal_review,
    risk_analysis,
    acquisition_vote,
    catalog_entry,
    storage_prep,
    final_approval
])

# Define the order of execution
root.order.add_edge(intake_review, visual_inspect)
root.order.add_edge(intake_review, material_test)
root.order.add_edge(visual_inspect, provenance_check)
root.order.add_edge(visual_inspect, archival_search)
root.order.add_edge(material_test, provenance_check)
root.order.add_edge(material_test, archival_search)
root.order.add_edge(provenance_check, expert_consult)
root.order.add_edge(archival_search, expert_consult)
root.order.add_edge(expert_consult, digital_scan)
root.order.add_edge(digital_scan, condition_report)
root.order.add_edge(condition_report, forger_assess)
root.order.add_edge(forger_assess, legal_review)
root.order.add_edge(legal_review, risk_analysis)
root.order.add_edge(risk_analysis, acquisition_vote)
root.order.add_edge(acquisition_vote, catalog_entry)
root.order.add_edge(catalog_entry, storage_prep)
root.order.add_edge(storage_prep, final_approval)