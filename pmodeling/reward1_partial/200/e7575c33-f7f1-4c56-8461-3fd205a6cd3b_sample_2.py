import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
artifact_intake = Transition(label='Artifact Intake')
catalog_entry = Transition(label='Catalog Entry')
visual_inspect = Transition(label='Visual Inspect')
material_test = Transition(label='Material Test')
spectroscopy = Transition(label='Spectroscopy')
historical_check = Transition(label='Historical Check')
provenance_trace = Transition(label='Provenance Trace')
style_compare = Transition(label='Style Compare')
three_d_scanning = Transition(label='3D Scanning')
condition_assess = Transition(label='Condition Assess')
preservation_plan = Transition(label='Preservation Plan')
legal_review = Transition(label='Legal Review')
report_draft = Transition(label='Report Draft')
report_finalize = Transition(label='Report Finalize')
archive_data = Transition(label='Archive Data')
sale_prep = Transition(label='Sale Prep')

# Define the POWL model
root = StrictPartialOrder(
    nodes=[
        artifact_intake,
        catalog_entry,
        visual_inspect,
        material_test,
        spectroscopy,
        historical_check,
        provenance_trace,
        style_compare,
        three_d_scanning,
        condition_assess,
        preservation_plan,
        legal_review,
        report_draft,
        report_finalize,
        archive_data,
        sale_prep
    ]
)

# Define dependencies
root.order.add_edge(artifact_intake, catalog_entry)
root.order.add_edge(catalog_entry, visual_inspect)
root.order.add_edge(visual_inspect, material_test)
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

# Print the root model
print(root)