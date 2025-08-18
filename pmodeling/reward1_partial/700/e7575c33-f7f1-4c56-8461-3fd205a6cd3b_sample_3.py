import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities) for the process
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

# Define silent transitions
skip = SilentTransition()

# Define the process flow
visual_inspect_and_test = OperatorPOWL(operator=Operator.XOR, children=[visual_inspect, material_test])
spectroscopy_and_compare = OperatorPOWL(operator=Operator.XOR, children=[spectroscopy, style_compare])
historical_check_and_trace = OperatorPOWL(operator=Operator.XOR, children=[historical_check, provenance_trace])
three_d_scanning_and_assess = OperatorPOWL(operator=Operator.XOR, children=[three_d_scanning, condition_assess])
legal_review_and_plan = OperatorPOWL(operator=Operator.XOR, children=[legal_review, preservation_plan])

root = StrictPartialOrder(nodes=[artifact_intake, catalog_entry, visual_inspect_and_test, spectroscopy_and_compare, historical_check_and_trace, three_d_scanning_and_assess, legal_review_and_plan, report_draft, report_finalize, archive_data, sale_prep])

# Define dependencies
root.order.add_edge(artifact_intake, catalog_entry)
root.order.add_edge(catalog_entry, visual_inspect_and_test)
root.order.add_edge(visual_inspect_and_test, spectroscopy_and_compare)
root.order.add_edge(spectroscopy_and_compare, historical_check_and_trace)
root.order.add_edge(historical_check_and_trace, three_d_scanning_and_assess)
root.order.add_edge(three_d_scanning_and_assess, legal_review_and_plan)
root.order.add_edge(legal_review_and_plan, report_draft)
root.order.add_edge(report_draft, report_finalize)
root.order.add_edge(report_finalize, archive_data)
root.order.add_edge(archive_data, sale_prep)