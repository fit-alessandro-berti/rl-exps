import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
analyze_performance = Transition(label='Analyze performance for future optimization')
campaign_ends = Transition(label='Campaign period ends')
collect_leads = Transition(label='Collect leads in CRM system')
create_content = Transition(label='Create content')
define_objectives = Transition(label='Define campaign objectives')
design_visuals = Transition(label='Design visuals')
launch_campaign = Transition(label='Launch campaign')
follow_up_leads = Transition(label='Sales teams follows up on leads')
select_channels = Transition(label='Select promotion channels')
track_performance = Transition(label='Track performance in real-time')

# Define silent transitions
skip = SilentTransition()

# Define the POWL model
loop = OperatorPOWL(operator=Operator.LOOP, children=[analyze_performance, campaign_ends])
xor = OperatorPOWL(operator=Operator.XOR, children=[collect_leads, skip])
root = StrictPartialOrder(nodes=[loop, xor])

# Define the partial order
root.order.add_edge(loop, xor)
root.order.add_edge(define_objectives, create_content)
root.order.add_edge(create_content, design_visuals)
root.order.add_edge(design_visuals, select_channels)
root.order.add_edge(select_channels, launch_campaign)
root.order.add_edge(launch_campaign, track_performance)
root.order.add_edge(track_performance, follow_up_leads)
root.order.add_edge(follow_up_leads, loop)