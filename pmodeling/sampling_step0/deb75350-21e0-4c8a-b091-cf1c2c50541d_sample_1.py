import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
intake_review = Transition(label='Intake Review')
visual_inspect = Transition(label='Visual Inspect')
material_test = Transition(label='Material Test')
provenance_check = Transition(label='Provenance Check')
archival_search = Transition(label='Archival Search')
expert_consult = Transition(label='Expert Consult')
digital_scan = Transition(label='Digital Scan')
condition_report = Transition(label='Condition Report')
forgery_assess = Transition(label='Forgery Assess')
legal_review = Transition(label='Legal Review')
risk_analysis = Transition(label='Risk Analysis')
acquisition_vote = Transition(label='Acquisition Vote')
catalog_entry = Transition(label='Catalog Entry')
storage_prep = Transition(label='Storage Prep')
final_approval = Transition(label='Final Approval')

# Define the silent transitions (no action)
skip = SilentTransition()

# Define the exclusive choices (XOR)
intake_analysis_choice = OperatorPOWL(operator=Operator.XOR, children=[intake_review, visual_inspect])
material_analysis_choice = OperatorPOWL(operator=Operator.XOR, children=[material_test, provenance_check])
archival_search_choice = OperatorPOWL(operator=Operator.XOR, children=[archival_search, expert_consult])
digital_scan_choice = OperatorPOWL(operator=Operator.XOR, children=[digital_scan, condition_report])
forgery_assessment_choice = OperatorPOWL(operator=Operator.XOR, children=[forgery_assess, legal_review])
risk_analysis_choice = OperatorPOWL(operator=Operator.XOR, children=[risk_analysis, acquisition_vote])
cataloging_choice = OperatorPOWL(operator=Operator.XOR, children=[catalog_entry, storage_prep])
final_approval_choice = OperatorPOWL(operator=Operator.XOR, children=[final_approval, skip])

# Define the loops
intake_analysis_loop = OperatorPOWL(operator=Operator.LOOP, children=[intake_analysis_choice])
material_analysis_loop = OperatorPOWL(operator=Operator.LOOP, children=[material_analysis_choice])
archival_search_loop = OperatorPOWL(operator=Operator.LOOP, children=[archival_search_choice])
digital_scan_loop = OperatorPOWL(operator=Operator.LOOP, children=[digital_scan_choice])
forgery_assessment_loop = OperatorPOWL(operator=Operator.LOOP, children=[forgery_assessment_choice])
risk_analysis_loop = OperatorPOWL(operator=Operator.LOOP, children=[risk_analysis_choice])
cataloging_loop = OperatorPOWL(operator=Operator.LOOP, children=[cataloging_choice])

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    intake_analysis_loop,
    material_analysis_loop,
    archival_search_loop,
    digital_scan_loop,
    forgery_assessment_loop,
    risk_analysis_loop,
    cataloging_loop,
    final_approval_choice
])

# Define the dependencies between the nodes
root.order.add_edge(intake_analysis_loop, material_analysis_loop)
root.order.add_edge(material_analysis_loop, archival_search_loop)
root.order.add_edge(archival_search_loop, digital_scan_loop)
root.order.add_edge(digital_scan_loop, forgery_assessment_loop)
root.order.add_edge(forgery_assessment_loop, risk_analysis_loop)
root.order.add_edge(risk_analysis_loop, cataloging_loop)
root.order.add_edge(cataloging_loop, final_approval_choice)

# Print the root POWL model
print(root)