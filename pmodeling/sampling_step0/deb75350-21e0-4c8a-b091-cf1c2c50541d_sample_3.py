import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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
skip = SilentTransition()

# Define the loops and choices
intake_loop = OperatorPOWL(operator=Operator.LOOP, children=[intake_review, visual_inspect])
analysis_loop = OperatorPOWL(operator=Operator.LOOP, children=[material_test, provenance_check, archival_search, expert_consult, digital_scan])
condition_loop = OperatorPOWL(operator=Operator.LOOP, children=[condition_report, forger_assess])
legal_loop = OperatorPOWL(operator=Operator.LOOP, children=[legal_review, risk_analysis])
acquisition_loop = OperatorPOWL(operator=Operator.LOOP, children=[acquisition_vote, catalog_entry, storage_prep])

# Define the exclusive choices
analysis_choice = OperatorPOWL(operator=Operator.XOR, children=[analysis_loop, condition_loop])
legal_choice = OperatorPOWL(operator=Operator.XOR, children=[legal_loop, acquisition_loop])

# Define the main partial order
root = StrictPartialOrder(nodes=[intake_loop, analysis_choice, legal_choice, final_approval])
root.order.add_edge(intake_loop, analysis_choice)
root.order.add_edge(analysis_choice, legal_choice)
root.order.add_edge(legal_choice, final_approval)

# Print the root node
print(root)