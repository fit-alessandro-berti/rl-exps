import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

artifact_intake = Transition(label='Artifact Intake')
condition_check = Transition(label='Condition Check')
material_test = Transition(label='Material Test')
style_compare = Transition(label='Style Compare')
carbon_dating = Transition(label='Carbon Dating')
document_review = Transition(label='Document Review')
provenance_check = Transition(label='Provenance Check')
digital_imaging = Transition(label='Digital Imaging')
forgery_scan = Transition(label='Forgery Scan')
expert_consult = Transition(label='Expert Consult')
historical_research = Transition(label='Historical Research')
panel_review = Transition(label='Panel Review')
report_draft = Transition(label='Report Draft')
final_approval = Transition(label='Final Approval')
catalog_entry = Transition(label='Catalog Entry')

skip = SilentTransition()
parallel_choices = OperatorPOWL(operator=Operator.XOR, children=[
    OperatorPOWL(operator=Operator.LOOP, children=[condition_check, material_test, style_compare, carbon_dating]),
    OperatorPOWL(operator=Operator.LOOP, children=[document_review, provenance_check, digital_imaging, forgery_scan, expert_consult, historical_research, panel_review])
])
root = StrictPartialOrder(nodes=[artifact_intake, parallel_choices, report_draft, final_approval, catalog_entry])
root.order.add_edge(artifact_intake, parallel_choices)
root.order.add_edge(parallel_choices, report_draft)
root.order.add_edge(report_draft, final_approval)
root.order.add_edge(final_approval, catalog_entry)