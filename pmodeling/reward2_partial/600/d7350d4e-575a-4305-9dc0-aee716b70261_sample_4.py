from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the POWL nodes
provenance_check = Transition(label='Provenance Check')
sample_collection = Transition(label='Sample Collection')
spectroscopy_test = Transition(label='Spectroscopy Test')
carbon_dating = Transition(label='Carbon Dating')
expert_review = Transition(label='Expert Review')
legal_clearance = Transition(label='Legal Clearance')
cultural_assessment = Transition(label='Cultural Assessment')
digital_scan = Transition(label='Digital Scan')
report_draft = Transition(label='Report Draft')
stakeholder_meet = Transition(label='Stakeholder Meet')
acquisition_vote = Transition(label='Acquisition Vote')
restoration_plan = Transition(label='Restoration Plan')
condition_report = Transition(label='Condition Report')
archival_entry = Transition(label='Archival Entry')
final_approval = Transition(label='Final Approval')

# Define the POWL model
root = StrictPartialOrder(nodes=[provenance_check, sample_collection, spectroscopy_test, carbon_dating, expert_review, legal_clearance, cultural_assessment, digital_scan, report_draft, stakeholder_meet, acquisition_vote, restoration_plan, condition_report, archival_entry, final_approval])

# Define the POWL order
root.order.add_edge(provenance_check, sample_collection)
root.order.add_edge(sample_collection, spectroscopy_test)
root.order.add_edge(spectroscopy_test, carbon_dating)
root.order.add_edge(carbon_dating, expert_review)
root.order.add_edge(expert_review, legal_clearance)
root.order.add_edge(legal_clearance, cultural_assessment)
root.order.add_edge(cultural_assessment, digital_scan)
root.order.add_edge(digital_scan, report_draft)
root.order.add_edge(report_draft, stakeholder_meet)
root.order.add_edge(stakeholder_meet, acquisition_vote)
root.order.add_edge(acquisition_vote, restoration_plan)
root.order.add_edge(restoration_plan, condition_report)
root.order.add_edge(condition_report, archival_entry)
root.order.add_edge(archival_entry, final_approval)

print(root)