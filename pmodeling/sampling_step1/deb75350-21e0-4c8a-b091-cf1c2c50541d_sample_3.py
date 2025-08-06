import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
intake_review = Transition(label='Intake Review')
visual_inspect = Transition(label='Visual Inspect')
material_test = Transition(label='Material Test')
provenance_check = Transition(label='Provenance Check')
archival_search = Transition(label='Archival Search')
expert_consult = Transition(label='Expert Consult')
digital_scan = Transition(label='Digital Scan')
condition_report = Transition(label='Condition Report')
forgeries_assess = Transition(label='Forgery Assess')
legal_review = Transition(label='Legal Review')
risk_analysis = Transition(label='Risk Analysis')
acquisition_vote = Transition(label='Acquisition Vote')
catalog_entry = Transition(label='Catalog Entry')
storage_prep = Transition(label='Storage Prep')
final_approval = Transition(label='Final Approval')

# Define silent transitions
skip = SilentTransition()

# Define partial order nodes
intake_and_analysis = OperatorPOWL(operator=Operator.XOR, children=[intake_review, visual_inspect, material_test])
provenance_and_search = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, archival_search])
expert_and_assessment = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, forgeries_assess])
digital_and_condition = OperatorPOWL(operator=Operator.XOR, children=[digital_scan, condition_report])
legal_and_risk = OperatorPOWL(operator=Operator.XOR, children=[legal_review, risk_analysis])
acquisition_and_catalog = OperatorPOWL(operator=Operator.XOR, children=[acquisition_vote, catalog_entry])
storage_and_final = OperatorPOWL(operator=Operator.XOR, children=[storage_prep, final_approval])

# Define the root partial order
root = StrictPartialOrder(nodes=[intake_and_analysis, provenance_and_search, expert_and_assessment, digital_and_condition, legal_and_risk, acquisition_and_catalog, storage_and_final])
root.order.add_edge(intake_and_analysis, provenance_and_search)
root.order.add_edge(provenance_and_search, expert_and_assessment)
root.order.add_edge(expert_and_assessment, digital_and_condition)
root.order.add_edge(digital_and_condition, legal_and_risk)
root.order.add_edge(legal_and_risk, acquisition_and_catalog)
root.order.add_edge(acquisition_and_catalog, storage_and_final)