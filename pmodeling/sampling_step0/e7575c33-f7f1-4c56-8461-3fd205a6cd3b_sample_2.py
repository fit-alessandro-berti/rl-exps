from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

loop_artifact_intake = OperatorPOWL(operator=Operator.LOOP, children=[artifact_intake, catalog_entry])
xor_visual_inspect = OperatorPOWL(operator=Operator.XOR, children=[visual_inspect, skip])
xor_material_test = OperatorPOWL(operator=Operator.XOR, children=[material_test, skip])
xor_spectroscopy = OperatorPOWL(operator=Operator.XOR, children=[spectroscopy, skip])
xor_historical_check = OperatorPOWL(operator=Operator.XOR, children=[historical_check, skip])
xor_provenance_trace = OperatorPOWL(operator=Operator.XOR, children=[provenance_trace, skip])
xor_style_compare = OperatorPOWL(operator=Operator.XOR, children=[style_compare, skip])
xor_3d_scanning = OperatorPOWL(operator=Operator.XOR, children=[three_d_scanning, skip])
xor_condition_assess = OperatorPOWL(operator=Operator.XOR, children=[condition_assess, skip])
xor_preservation_plan = OperatorPOWL(operator=Operator.XOR, children=[preservation_plan, skip])
xor_legal_review = OperatorPOWL(operator=Operator.XOR, children=[legal_review, skip])
xor_report_draft = OperatorPOWL(operator=Operator.XOR, children=[report_draft, skip])
xor_report_finalize = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, skip])
xor_archive_data = OperatorPOWL(operator=Operator.XOR, children=[archive_data, skip])
xor_sale_prep = OperatorPOWL(operator=Operator.XOR, children=[sale_prep, skip])

root = StrictPartialOrder(nodes=[
    loop_artifact_intake,
    xor_visual_inspect,
    xor_material_test,
    xor_spectroscopy,
    xor_historical_check,
    xor_provenance_trace,
    xor_style_compare,
    xor_3d_scanning,
    xor_condition_assess,
    xor_preservation_plan,
    xor_legal_review,
    xor_report_draft,
    xor_report_finalize,
    xor_archive_data,
    xor_sale_prep
])

root.order.add_edge(loop_artifact_intake, xor_visual_inspect)
root.order.add_edge(loop_artifact_intake, xor_material_test)
root.order.add_edge(loop_artifact_intake, xor_spectroscopy)
root.order.add_edge(loop_artifact_intake, xor_historical_check)
root.order.add_edge(loop_artifact_intake, xor_provenance_trace)
root.order.add_edge(loop_artifact_intake, xor_style_compare)
root.order.add_edge(loop_artifact_intake, xor_3d_scanning)
root.order.add_edge(loop_artifact_intake, xor_condition_assess)
root.order.add_edge(loop_artifact_intake, xor_preservation_plan)
root.order.add_edge(loop_artifact_intake, xor_legal_review)
root.order.add_edge(loop_artifact_intake, xor_report_draft)
root.order.add_edge(loop_artifact_intake, xor_report_finalize)
root.order.add_edge(loop_artifact_intake, xor_archive_data)
root.order.add_edge(loop_artifact_intake, xor_sale_prep)