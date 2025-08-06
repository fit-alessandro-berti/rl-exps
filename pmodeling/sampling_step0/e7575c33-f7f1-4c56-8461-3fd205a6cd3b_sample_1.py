from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the POWL model
root = StrictPartialOrder()

# Define the transitions
artifact_intake = Transition('Artifact Intake')
catalog_entry = Transition('Catalog Entry')
visual_inspect = Transition('Visual Inspect')
material_test = Transition('Material Test')
spectroscopy = Transition('Spectroscopy')
historical_check = Transition('Historical Check')
provenance_trace = Transition('Provenance Trace')
style_compare = Transition('Style Compare')
three_d_scanning = Transition('3D Scanning')
condition_assess = Transition('Condition Assess')
preservation_plan = Transition('Preservation Plan')
legal_review = Transition('Legal Review')
report_draft = Transition('Report Draft')
report_finalize = Transition('Report Finalize')
archive_data = Transition('Archive Data')
sale_prep = Transition('Sale Prep')

# Define the partial order
root.nodes = [artifact_intake, catalog_entry, visual_inspect, material_test, spectroscopy, historical_check, provenance_trace, style_compare, three_d_scanning, condition_assess, preservation_plan, legal_review, report_draft, report_finalize, archive_data, sale_prep]
root.order.add_edge(artifact_intake, catalog_entry)
root.order.add_edge(artifact_intake, visual_inspect)
root.order.add_edge(catalog_entry, material_test)
root.order.add_edge(material_test, spectroscopy)
root.order.add_edge(spectroscopy, historical_check)
root.order.add_edge(historical_check, provenance_trace)
root.order.add_edge(provenance_trace, style_compare)
root.order.add_edge(style_compare, three_d_scanning)
root.order.add_edge(three_d_scanning, condition_assess)
root.order.add_edge(condition_assess, preservation_plan)
root.order.add_edge(preservation_plan, legal_review)
root.order.add_edge(legal_review, report_draft)
root.order.add_edge(report_draft, report_finalize)
root.order.add_edge(report_finalize, archive_data)
root.order.add_edge(archive_data, sale_prep)

# Print the POWL model
print(root)