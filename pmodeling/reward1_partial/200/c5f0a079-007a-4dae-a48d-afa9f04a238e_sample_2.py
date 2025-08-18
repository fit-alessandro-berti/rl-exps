import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

provenance_check = Transition(label='Provenance Check')
material_scan = Transition(label='Material Scan')
wear_analysis = Transition(label='Wear Analysis')
image_capture = Transition(label='Image Capture')
pattern_match = Transition(label='Pattern Match')
ownership_verify = Transition(label='Ownership Verify')
ethics_review = Transition(label='Ethics Review')
carbon_dating = Transition(label='Carbon Dating')
restoration_eval = Transition(label='Restoration Eval')
report_draft = Transition(label='Report Draft')
stakeholder_review = Transition(label='Stakeholder Review')
archive_data = Transition(label='Archive Data')
exhibit_approve = Transition(label='Exhibit Approve')
condition_monitor = Transition(label='Condition Monitor')
final_certification = Transition(label='Final Certification')

skip = SilentTransition()

provenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check])
material_loop = OperatorPOWL(operator=Operator.LOOP, children=[material_scan])
wear_loop = OperatorPOWL(operator=Operator.LOOP, children=[wear_analysis])
image_loop = OperatorPOWL(operator=Operator.LOOP, children=[image_capture])
pattern_loop = OperatorPOWL(operator=Operator.LOOP, children=[pattern_match])
ownership_loop = OperatorPOWL(operator=Operator.LOOP, children=[ownership_verify])
ethics_loop = OperatorPOWL(operator=Operator.LOOP, children=[ethics_review])
carbon_loop = OperatorPOWL(operator=Operator.LOOP, children=[carbon_dating])
restoration_loop = OperatorPOWL(operator=Operator.LOOP, children=[restoration_eval])
report_loop = OperatorPOWL(operator=Operator.LOOP, children=[report_draft])
stakeholder_loop = OperatorPOWL(operator=Operator.LOOP, children=[stakeholder_review])
archive_loop = OperatorPOWL(operator=Operator.LOOP, children=[archive_data])
exhibit_loop = OperatorPOWL(operator=Operator.LOOP, children=[exhibit_approve])
condition_loop = OperatorPOWL(operator=Operator.LOOP, children=[condition_monitor])
final_loop = OperatorPOWL(operator=Operator.LOOP, children=[final_certification])

root = StrictPartialOrder(nodes=[
    provenance_loop, material_loop, wear_loop, image_loop, pattern_loop,
    ownership_loop, ethics_loop, carbon_loop, restoration_loop, report_loop,
    stakeholder_loop, archive_loop, exhibit_loop, condition_loop, final_loop
])

root.order.add_edge(provenance_loop, material_loop)
root.order.add_edge(material_loop, wear_loop)
root.order.add_edge(wear_loop, image_loop)
root.order.add_edge(image_loop, pattern_loop)
root.order.add_edge(pattern_loop, ownership_loop)
root.order.add_edge(ownership_loop, ethics_loop)
root.order.add_edge(ethics_loop, carbon_loop)
root.order.add_edge(carbon_loop, restoration_loop)
root.order.add_edge(restoration_loop, report_loop)
root.order.add_edge(report_loop, stakeholder_loop)
root.order.add_edge(stakeholder_loop, archive_loop)
root.order.add_edge(archive_loop, exhibit_loop)
root.order.add_edge(exhibit_loop, condition_loop)
root.order.add_edge(condition_loop, final_loop)

print(root)