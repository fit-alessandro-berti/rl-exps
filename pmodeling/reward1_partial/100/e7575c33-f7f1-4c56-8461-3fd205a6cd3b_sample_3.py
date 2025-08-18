import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the process steps
loop_visual_inspect = OperatorPOWL(operator=Operator.LOOP, children=[visual_inspect, material_test, spectroscopy])
xor_historical_check_style_compare = OperatorPOWL(operator=Operator.XOR, children=[historical_check, style_compare])
xor_three_d_scanning_condition_assess = OperatorPOWL(operator=Operator.XOR, children=[three_d_scanning, condition_assess])
xor_legal_review_report_draft = OperatorPOWL(operator=Operator.XOR, children=[legal_review, report_draft])
xor_report_finalize_archive_data = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])
xor_sale_prep = OperatorPOWL(operator=Operator.XOR, children=[sale_prep])

# Define the partial order
root = StrictPartialOrder(nodes=[
    artifact_intake,
    catalog_entry,
    loop_visual_inspect,
    xor_historical_check_style_compare,
    xor_three_d_scanning_condition_assess,
    xor_legal_review_report_draft,
    xor_report_finalize_archive_data,
    xor_sale_prep
])

# Define the dependencies
root.order.add_edge(artifact_intake, catalog_entry)
root.order.add_edge(catalog_entry, loop_visual_inspect)
root.order.add_edge(loop_visual_inspect, xor_historical_check_style_compare)
root.order.add_edge(xor_historical_check_style_compare, xor_three_d_scanning_condition_assess)
root.order.add_edge(xor_three_d_scanning_condition_assess, xor_legal_review_report_draft)
root.order.add_edge(xor_legal_review_report_draft, xor_report_finalize_archive_data)
root.order.add_edge(xor_report_finalize_archive_data, xor_sale_prep)

print(root)