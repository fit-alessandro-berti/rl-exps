import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
intake_review = Transition(label='Intake Review')
visual_inspect = Transition(label='Visual Inspect')
material_test = Transition(label='Material Test')
provenance_check = Transition(label='Provenance Check')
archival_search = Transition(label='Archival Search')
expert_consult = Transition(label='Expert Consult')
digital_scan = Transition(label='Digital Scan')
condition_report = Transition(label='Condition Report')
forger_assess = Transition(label='Forgery Assess')
legal_review = Transition(label='Legal Review')
risk_analysis = Transition(label='Risk Analysis')
acquisition_vote = Transition(label='Acquisition Vote')
catalog_entry = Transition(label='Catalog Entry')
storage_prep = Transition(label='Storage Prep')
final_approval = Transition(label='Final Approval')

# Define the control-flow operators for the workflow
xor1 = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, archival_search])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, material_test])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[digital_scan, condition_report])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[forger_assess, legal_review])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[risk_analysis, acquisition_vote])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[catalog_entry, storage_prep])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[final_approval, silent_transition])

# Define the partial order
root = StrictPartialOrder(nodes=[intake_review, visual_inspect, xor1, xor2, xor3, xor4, xor5, xor6, xor7])

# Define the dependencies between the nodes
root.order.add_edge(intake_review, visual_inspect)
root.order.add_edge(visual_inspect, xor1)
root.order.add_edge(xor1, provenance_check)
root.order.add_edge(xor1, archival_search)
root.order.add_edge(provenance_check, xor2)
root.order.add_edge(archival_search, xor2)
root.order.add_edge(xor2, expert_consult)
root.order.add_edge(xor2, material_test)
root.order.add_edge(expert_consult, xor3)
root.order.add_edge(material_test, xor3)
root.order.add_edge(xor3, digital_scan)
root.order.add_edge(xor3, condition_report)
root.order.add_edge(digital_scan, xor4)
root.order.add_edge(condition_report, xor4)
root.order.add_edge(xor4, forger_assess)
root.order.add_edge(xor4, legal_review)
root.order.add_edge(forger_assess, xor5)
root.order.add_edge(legal_review, xor5)
root.order.add_edge(xor5, risk_analysis)
root.order.add_edge(risk_analysis, acquisition_vote)
root.order.add_edge(acquisition_vote, xor6)
root.order.add_edge(xor6, catalog_entry)
root.order.add_edge(catalog_entry, xor7)
root.order.add_edge(xor7, storage_prep)
root.order.add_edge(storage_prep, final_approval)

# Define the silent transition
silent_transition = SilentTransition()

# Add the silent transition to the partial order
root.order.add_edge(xor7, silent_transition)
root.order.add_edge(silent_transition, final_approval)

# Print the root
print(root)