import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator
from pm4py.objects.petri.obj import Marking

# Define the POWL model
provenance_check = Transition(label='Provenance Check')
material_scan = Transition(label='Material Scan')
expert_review = Transition(label='Expert Review')
legal_audit = Transition(label='Legal Audit')
condition_report = Transition(label='Condition Report')
carbon_dating = Transition(label='Carbon Dating')
ownership_verify = Transition(label='Ownership Verify')
historical_match = Transition(label='Historical Match')
customs_clearance = Transition(label='Customs Clearance')
risk_assessment = Transition(label='Risk Assessment')
ethics_approval = Transition(label='Ethics Approval')
restoration_plan = Transition(label='Restoration Plan')
final_approval = Transition(label='Final Approval')
catalog_entry = Transition(label='Catalog Entry')
exhibit_prep = Transition(label='Exhibit Prep')
skip = SilentTransition()

# Define the partial order
loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, material_scan])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[expert_review, legal_audit])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[condition_report, carbon_dating])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[ownership_verify, historical_match])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[customs_clearance, risk_assessment])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[ethics_approval, restoration_plan])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[final_approval, catalog_entry])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[exhibit_prep, skip])

# Define the order
root = StrictPartialOrder(nodes=[loop, xor1, xor2, xor3, xor4, xor5, xor6, xor7])
root.order.add_edge(loop, xor1)
root.order.add_edge(loop, xor2)
root.order.add_edge(loop, xor3)
root.order.add_edge(loop, xor4)
root.order.add_edge(loop, xor5)
root.order.add_edge(loop, xor6)
root.order.add_edge(loop, xor7)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)

# Print the POWL model
print(root)