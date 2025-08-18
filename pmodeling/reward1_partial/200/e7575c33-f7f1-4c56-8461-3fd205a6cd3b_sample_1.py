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

visual_inspect_loop = OperatorPOWL(operator=Operator.LOOP, children=[visual_inspect, material_test])
spectroscopy_loop = OperatorPOWL(operator=Operator.LOOP, children=[spectroscopy, historical_check])
style_compare_loop = OperatorPOWL(operator=Operator.LOOP, children=[style_compare, provenance_trace])
three_d_scanning_loop = OperatorPOWL(operator=Operator.LOOP, children=[three_d_scanning, condition_assess])
preservation_plan_loop = OperatorPOWL(operator=Operator.LOOP, children=[preservation_plan, legal_review])

root = StrictPartialOrder(nodes=[
    artifact_intake,
    catalog_entry,
    visual_inspect_loop,
    spectroscopy_loop,
    style_compare_loop,
    three_d_scanning_loop,
    preservation_plan_loop,
    report_draft,
    report_finalize,
    archive_data,
    sale_prep
])

root.order.add_edge(visual_inspect_loop, spectroscopy_loop)
root.order.add_edge(spectroscopy_loop, style_compare_loop)
root.order.add_edge(style_compare_loop, three_d_scanning_loop)
root.order.add_edge(three_d_scanning_loop, preservation_plan_loop)
root.order.add_edge(preservation_plan_loop, report_draft)
root.order.add_edge(report_draft, report_finalize)
root.order.add_edge(report_finalize, archive_data)
root.order.add_edge(archive_data, sale_prep)