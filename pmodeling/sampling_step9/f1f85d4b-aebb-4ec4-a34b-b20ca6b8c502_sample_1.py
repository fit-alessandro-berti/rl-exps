import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
initial_review = Transition(label='Initial Review')
provenance_check = Transition(label='Provenance Check')
material_testing = Transition(label='Material Testing')
expert_survey = Transition(label='Expert Survey')
digital_scan = Transition(label='Digital Scan')
condition_report = Transition(label='Condition Report')
legal_review = Transition(label='Legal Review')
risk_analysis = Transition(label='Risk Analysis')
seller_negotiation = Transition(label='Seller Negotiation')
documentation = Transition(label='Documentation')
archival_entry = Transition(label='Archival Entry')
committee_review = Transition(label='Committee Review')
final_approval = Transition(label='Final Approval')
acquisition_setup = Transition(label='Acquisition Setup')
exhibit_planning = Transition(label='Exhibit Planning')

# Define silent transitions
skip = SilentTransition()

# Define the workflow
loop_provenance = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, skip])
loop_material = OperatorPOWL(operator=Operator.LOOP, children=[material_testing, skip])
loop_expert = OperatorPOWL(operator=Operator.LOOP, children=[expert_survey, skip])
loop_documentation = OperatorPOWL(operator=Operator.LOOP, children=[documentation, skip])
loop_archival = OperatorPOWL(operator=Operator.LOOP, children=[archival_entry, skip])
loop_committee = OperatorPOWL(operator=Operator.LOOP, children=[committee_review, skip])
loop_final = OperatorPOWL(operator=Operator.LOOP, children=[final_approval, skip])
loop_acquisition = OperatorPOWL(operator=Operator.LOOP, children=[acquisition_setup, skip])
loop_exhibit = OperatorPOWL(operator=Operator.LOOP, children=[exhibit_planning, skip])

xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[risk_analysis, skip])
xor_material = OperatorPOWL(operator=Operator.XOR, children=[seller_negotiation, skip])
xor_expert = OperatorPOWL(operator=Operator.XOR, children=[condition_report, skip])
xor_documentation = OperatorPOWL(operator=Operator.XOR, children=[legal_review, skip])

root = StrictPartialOrder(nodes=[
    loop_provenance, loop_material, loop_expert, loop_documentation, loop_archival, loop_committee, loop_final, loop_acquisition, loop_exhibit,
    xor_provenance, xor_material, xor_expert, xor_documentation
])
root.order.add_edge(loop_provenance, xor_provenance)
root.order.add_edge(loop_material, xor_material)
root.order.add_edge(loop_expert, xor_expert)
root.order.add_edge(loop_documentation, xor_documentation)