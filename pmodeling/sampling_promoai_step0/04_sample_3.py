import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
analyze_performance = Transition(label='Analyze performance for future optimization')
campaign_ends = Transition(label='Campaign period ends')
collect_leads = Transition(label='Collect leads in CRM system')
create_content = Transition(label='Create content')
define_objectives = Transition(label='Define campaign objectives')
design_visuals = Transition(label='Design visuals')
launch_campaign = Transition(label='Launch campaign')
sales_follow_up = Transition(label='Sales teams follows up on leads')
select_channels = Transition(label='Select promotion channels')
track_performance = Transition(label='Track performance in real-time')

# Define silent transitions
skip_define_objectives = SilentTransition()
skip_design_visuals = SilentTransition()
skip_select_channels = SilentTransition()
skip_track_performance = SilentTransition()

# Define the process tree structure
loop = OperatorPOWL(operator=Operator.LOOP, children=[define_objectives, design_visuals, select_channels, track_performance])
xor = OperatorPOWL(operator=Operator.XOR, children=[collect_leads, sales_follow_up])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

# Print the root model
print(root)