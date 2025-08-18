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

# Define the control-flow operators
xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, archival_search])
xor_expert = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, digital_scan])
xor_forger = OperatorPOWL(operator=Operator.XOR, children=[forger_assess, legal_review])
xor_legal = OperatorPOWL(operator=Operator.XOR, children=[legal_review, risk_analysis])
xor_risk = OperatorPOWL(operator=Operator.XOR, children=[risk_analysis, acquisition_vote])
xor_acquisition = OperatorPOWL(operator=Operator.XOR, children=[acquisition_vote, catalog_entry])
xor_catalog = OperatorPOWL(operator=Operator.XOR, children=[catalog_entry, storage_prep])
xor_storage = OperatorPOWL(operator=Operator.XOR, children=[storage_prep, final_approval])

# Construct the POWL model
root = StrictPartialOrder(nodes=[
    intake_review,
    visual_inspect,
    material_test,
    xor_provenance,
    xor_expert,
    xor_forger,
    xor_legal,
    xor_risk,
    xor_acquisition,
    xor_catalog,
    xor_storage
])

# Add edges based on the process flow
root.order.add_edge(intake_review, visual_inspect)
root.order.add_edge(visual_inspect, material_test)
root.order.add_edge(material_test, xor_provenance)
root.order.add_edge(xor_provenance, xor_expert)
root.order.add_edge(xor_expert, xor_forger)
root.order.add_edge(xor_forger, xor_legal)
root.order.add_edge(xor_legal, xor_risk)
root.order.add_edge(xor_risk, xor_acquisition)
root.order.add_edge(xor_acquisition, xor_catalog)
root.order.add_edge(xor_catalog, xor_storage)
root.order.add_edge(xor_storage, final_approval)

# Print the POWL model (optional)
print(root)