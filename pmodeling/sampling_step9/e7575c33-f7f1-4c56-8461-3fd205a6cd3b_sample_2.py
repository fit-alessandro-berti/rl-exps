import pm4py
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

# Add the POWL model for the process
xor1 = OperatorPOWL(operator=Operator.XOR, children=[provenance_trace, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[style_compare, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[legal_review, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[sale_prep, skip])

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[three_d_scanning, condition_assess])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[preservation_plan, archive_data])

xor5 = OperatorPOWL(operator=Operator.XOR, children=[loop1, loop2])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, skip])

root = StrictPartialOrder(nodes=[artifact_intake, catalog_entry, visual_inspect, material_test, spectroscopy, historical_check, xor1, xor2, xor3, xor4, xor5, xor6])
root.order.add_edge(artifact_intake, catalog_entry)
root.order.add_edge(catalog_entry, visual_inspect)
root.order.add_edge(visual_inspect, material_test)
root.order.add_edge(material_test, spectroscopy)
root.order.add_edge(spectroscopy, historical_check)
root.order.add_edge(historical_check, xor1)
root.order.add_edge(historical_check, xor2)
root.order.add_edge(historical_check, xor3)
root.order.add_edge(historical_check, xor4)
root.order.add_edge(xor1, xor5)
root.order.add_edge(xor2, xor5)
root.order.add_edge(xor3, xor5)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, report_finalize)