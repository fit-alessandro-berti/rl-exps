from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the POWL model for the process
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

# Define the POWL operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, archival_search])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, digital_scan])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[condition_report, forgeries_assess])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[legal_review, risk_analysis])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[acquisition_vote, catalog_entry])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[storage_prep, final_approval])

# Define the POWL model
root = StrictPartialOrder(nodes=[
    intake_review, visual_inspect, material_test, xor1, xor2, xor3, xor4, xor5, xor6
])
root.order.add_edge(intake_review, visual_inspect)
root.order.add_edge(intake_review, material_test)
root.order.add_edge(visual_inspect, xor1)
root.order.add_edge(material_test, xor2)
root.order.add_edge(xor1, xor3)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, final_approval)