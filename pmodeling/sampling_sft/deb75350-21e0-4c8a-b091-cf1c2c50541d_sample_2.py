import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
intake_review     = Transition(label='Intake Review')
visual_inspect    = Transition(label='Visual Inspect')
material_test     = Transition(label='Material Test')
provenance_check  = Transition(label='Provenance Check')
archival_search   = Transition(label='Archival Search')
expert_consult    = Transition(label='Expert Consult')
digital_scan      = Transition(label='Digital Scan')
condition_report  = Transition(label='Condition Report')
forgery_assess    = Transition(label='Forgery Assess')
legal_review      = Transition(label='Legal Review')
risk_analysis     = Transition(label='Risk Analysis')
acquisition_vote  = Transition(label='Acquisition Vote')
catalog_entry     = Transition(label='Catalog Entry')
storage_prep      = Transition(label='Storage Prep')
final_approval    = Transition(label='Final Approval')

# Build the choice for final approval: either Acquisition Vote or Final Approval
final_choice = OperatorPOWL(operator=Operator.XOR, children=[acquisition_vote, final_approval])

# Build the loop for risk analysis: do Risk Analysis, then either exit or do Forgery Assess then Risk Analysis again
loop_analysis = OperatorPOWL(operator=Operator.LOOP, children=[risk_analysis, forgery_assess])

# Assemble the overall partial order
root = StrictPartialOrder(nodes=[
    intake_review,
    visual_inspect,
    material_test,
    provenance_check,
    archival_search,
    expert_consult,
    digital_scan,
    condition_report,
    legal_review,
    loop_analysis,
    final_choice
])

# Define the control-flow dependencies
root.order.add_edge(intake_review, visual_inspect)
root.order.add_edge(intake_review, material_test)
root.order.add_edge(visual_inspect, provenance_check)
root.order.add_edge(material_test, provenance_check)
root.order.add_edge(provenance_check, archival_search)
root.order.add_edge(provenance_check, expert_consult)
root.order.add_edge(archival_search, digital_scan)
root.order.add_edge(expert_consult, digital_scan)
root.order.add_edge(digital_scan, condition_report)
root.order.add_edge(condition_report, legal_review)
root.order.add_edge(legal_review, loop_analysis)
root.order.add_edge(loop_analysis, final_choice)