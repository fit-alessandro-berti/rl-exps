import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
artifact_intake      = Transition(label='Artifact Intake')
provenance_check     = Transition(label='Provenance Check')
archive_research     = Transition(label='Archive Research')
expert_interview     = Transition(label='Expert Interview')
material_analysis    = Transition(label='Material Analysis')
spectroscopy_test    = Transition(label='Spectroscopy Test')
carbon_dating        = Transition(label='Carbon Dating')
digital_imaging      = Transition(label='Digital Imaging')
three_d_modeling     = Transition(label='3D Modeling')
data_review          = Transition(label='Data Review')
consensus_meeting    = Transition(label='Consensus Meeting')
conservation_plan    = Transition(label='Conservation Plan')
preservation_setup   = Transition(label='Preservation Setup')
documentation        = Transition(label='Documentation')
exhibition_prep      = Transition(label='Exhibition Prep')

# Build the loop for repeated data collection
loop_body = StrictPartialOrder(nodes=[material_analysis, spectroscopy_test, carbon_dating, digital_imaging, three_d_modeling])
loop_body.order.add_edge(material_analysis, spectroscopy_test)
loop_body.order.add_edge(material_analysis, carbon_dating)
loop_body.order.add_edge(spectroscopy_test, digital_imaging)
loop_body.order.add_edge(carbon_dating, digital_imaging)
loop_body.order.add_edge(digital_imaging, three_d_modeling)

loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, data_review])

# Assemble the overall partial order
root = StrictPartialOrder(nodes=[
    artifact_intake,
    provenance_check,
    archive_research,
    expert_interview,
    loop,
    consensus_meeting,
    conservation_plan,
    preservation_setup,
    documentation,
    exhibition_prep
])

# Define the control-flow dependencies
root.order.add_edge(artifact_intake, provenance_check)
root.order.add_edge(provenance_check, archive_research)
root.order.add_edge(provenance_check, expert_interview)
root.order.add_edge(archive_research, loop)
root.order.add_edge(expert_interview, loop)
root.order.add_edge(loop, consensus_meeting)
root.order.add_edge(consensus_meeting, conservation_plan)
root.order.add_edge(consensus_meeting, preservation_setup)
root.order.add_edge(consensus_meeting, documentation)
root.order.add_edge(consensus_meeting, exhibition_prep)