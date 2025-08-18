import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

provenance_check = Transition(label='Provenance Check')
sample_collection = Transition(label='Sample Collection')
spectroscopy_test = Transition(label='Spectroscopy Test')
carbon_dating = Transition(label='Carbon Dating')
expert_review = Transition(label='Expert Review')
legal_clearance = Transition(label='Legal Clearance')
cultural_assessment = Transition(label='Cultural Assessment')
digital_scan = Transition(label='Digital Scan')
report_draft = Transition(label='Report Draft')
stakeholder_meet = Transition(label='Stakeholder Meet')
acquisition_vote = Transition(label='Acquisition Vote')
restoration_plan = Transition(label='Restoration Plan')
condition_report = Transition(label='Condition Report')
archival_entry = Transition(label='Archival Entry')
final_approval = Transition(label='Final Approval')

skip = SilentTransition()

# Define the process tree structure
provenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check])
sample_loop = OperatorPOWL(operator=Operator.LOOP, children=[sample_collection])
spectroscopy_loop = OperatorPOWL(operator=Operator.LOOP, children=[spectroscopy_test])
carbon_dating_loop = OperatorPOWL(operator=Operator.LOOP, children=[carbon_dating])
expert_loop = OperatorPOWL(operator=Operator.LOOP, children=[expert_review])
legal_loop = OperatorPOWL(operator=Operator.LOOP, children=[legal_clearance])
cultural_loop = OperatorPOWL(operator=Operator.LOOP, children=[cultural_assessment])
digital_loop = OperatorPOWL(operator=Operator.LOOP, children=[digital_scan])
report_loop = OperatorPOWL(operator=Operator.LOOP, children=[report_draft])
stakeholder_loop = OperatorPOWL(operator=Operator.LOOP, children=[stakeholder_meet])
acquisition_loop = OperatorPOWL(operator=Operator.LOOP, children=[acquisition_vote])
restoration_loop = OperatorPOWL(operator=Operator.LOOP, children=[restoration_plan])
condition_loop = OperatorPOWL(operator=Operator.LOOP, children=[condition_report])
archival_loop = OperatorPOWL(operator=Operator.LOOP, children=[archival_entry])
final_loop = OperatorPOWL(operator=Operator.LOOP, children=[final_approval])

# Define the process tree
root = StrictPartialOrder(nodes=[provenance_loop, sample_loop, spectroscopy_loop, carbon_dating_loop, expert_loop, legal_loop, cultural_loop, digital_loop, report_loop, stakeholder_loop, acquisition_loop, restoration_loop, condition_loop, archival_loop, final_loop])
root.order.add_edge(provenance_loop, sample_loop)
root.order.add_edge(sample_loop, spectroscopy_loop)
root.order.add_edge(spectroscopy_loop, carbon_dating_loop)
root.order.add_edge(carbon_dating_loop, expert_loop)
root.order.add_edge(expert_loop, legal_loop)
root.order.add_edge(legal_loop, cultural_loop)
root.order.add_edge(cultural_loop, digital_loop)
root.order.add_edge(digital_loop, report_loop)
root.order.add_edge(report_loop, stakeholder_loop)
root.order.add_edge(stakeholder_loop, acquisition_loop)
root.order.add_edge(acquisition_loop, restoration_loop)
root.order.add_edge(restoration_loop, condition_loop)
root.order.add_edge(condition_loop, archival_loop)
root.order.add_edge(archival_loop, final_loop)

# Print the root of the POWL model
print(root)