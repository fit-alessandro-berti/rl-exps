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

# Define the silent activities
skip = SilentTransition()

# Define the process tree operators
loop = OperatorPOWL(operator=Operator.LOOP, children=[visual_inspect, material_test, spectroscopy])
xor = OperatorPOWL(operator=Operator.XOR, children=[preservation_plan, legal_review, sale_prep])
xor_2 = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])

# Define the process tree
root = StrictPartialOrder(nodes=[loop, historical_check, provenance_trace, style_compare, three_d_scanning, condition_assess, xor, xor_2])
root.order.add_edge(loop, historical_check)
root.order.add_edge(loop, provenance_trace)
root.order.add_edge(loop, style_compare)
root.order.add_edge(loop, three_d_scanning)
root.order.add_edge(loop, condition_assess)
root.order.add_edge(historical_check, xor)
root.order.add_edge(provenance_trace, xor)
root.order.add_edge(style_compare, xor)
root.order.add_edge(three_d_scanning, xor)
root.order.add_edge(condition_assess, xor)
root.order.add_edge(xor, xor_2)
root.order.add_edge(xor, report_finalize)
root.order.add_edge(xor, archive_data)