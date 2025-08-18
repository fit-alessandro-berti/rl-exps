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
artifact_intake_to_catalog_entry = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, catalog_entry])
visual_inspect_to_material_test = OperatorPOWL(operator=Operator.XOR, children=[visual_inspect, material_test])
material_test_to_spectroscopy = OperatorPOWL(operator=Operator.XOR, children=[material_test, spectroscopy])
historical_check_to_provenance_trace = OperatorPOWL(operator=Operator.XOR, children=[historical_check, provenance_trace])
provenance_trace_to_style_compare = OperatorPOWL(operator=Operator.XOR, children=[provenance_trace, style_compare])
style_compare_to_three_d_scanning = OperatorPOWL(operator=Operator.XOR, children=[style_compare, three_d_scanning])
three_d_scanning_to_condition_assess = OperatorPOWL(operator=Operator.XOR, children=[three_d_scanning, condition_assess])
condition_assess_to_preservation_plan = OperatorPOWL(operator=Operator.XOR, children=[condition_assess, preservation_plan])
preservation_plan_to_legal_review = OperatorPOWL(operator=Operator.XOR, children=[preservation_plan, legal_review])
legal_review_to_report_draft = OperatorPOWL(operator=Operator.XOR, children=[legal_review, report_draft])
report_draft_to_report_finalize = OperatorPOWL(operator=Operator.XOR, children=[report_draft, report_finalize])
report_finalize_to_archive_data = OperatorPOWL(operator=Operator.XOR, children=[report_finalize, archive_data])
archive_data_to_sale_prep = OperatorPOWL(operator=Operator.XOR, children=[archive_data, sale_prep])

# Create the root of the POWL model
root = StrictPartialOrder(nodes=[artifact_intake_to_catalog_entry,
                                  visual_inspect_to_material_test,
                                  material_test_to_spectroscopy,
                                  historical_check_to_provenance_trace,
                                  provenance_trace_to_style_compare,
                                  style_compare_to_three_d_scanning,
                                  three_d_scanning_to_condition_assess,
                                  condition_assess_to_preservation_plan,
                                  preservation_plan_to_legal_review,
                                  legal_review_to_report_draft,
                                  report_draft_to_report_finalize,
                                  report_finalize_to_archive_data,
                                  archive_data_to_sale_prep])

# Add edges to the root
root.order.add_edge(artifact_intake_to_catalog_entry, visual_inspect_to_material_test)
root.order.add_edge(visual_inspect_to_material_test, material_test_to_spectroscopy)
root.order.add_edge(material_test_to_spectroscopy, historical_check_to_provenance_trace)
root.order.add_edge(historical_check_to_provenance_trace, provenance_trace_to_style_compare)
root.order.add_edge(provenance_trace_to_style_compare, style_compare_to_three_d_scanning)
root.order.add_edge(style_compare_to_three_d_scanning, three_d_scanning_to_condition_assess)
root.order.add_edge(three_d_scanning_to_condition_assess, condition_assess_to_preservation_plan)
root.order.add_edge(condition_assess_to_preservation_plan, preservation_plan_to_legal_review)
root.order.add_edge(preservation_plan_to_legal_review, legal_review_to_report_draft)
root.order.add_edge(legal_review_to_report_draft, report_draft_to_report_finalize)
root.order.add_edge(report_draft_to_report_finalize, report_finalize_to_archive_data)
root.order.add_edge(report_finalize_to_archive_data, archive_data_to_sale_prep)