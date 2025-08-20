import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
define_objectives = Transition(label='Define campaign objectives')
create_content = Transition(label='Create content')
design_visuals = Transition(label='Design visuals')
select_channels = Transition(label='Select promotion channels')
launch_campaign = Transition(label='Launch campaign')
track_performance = Transition(label='Track performance in real-time')
collect_leads = Transition(label='Collect leads in CRM system')
follow_up = Transition(label='Sales teams follows up on leads')
analyze_performance = Transition(label='Analyze performance for future optimization')
campaign_ends = Transition(label='Campaign period ends')

# Create the POWL model
root = StrictPartialOrder(nodes=[define_objectives, create_content, design_visuals, select_channels, launch_campaign, track_performance, collect_leads, follow_up, analyze_performance, campaign_ends])
root.order.add_edge(define_objectives, create_content)
root.order.add_edge(define_objectives, design_visuals)
root.order.add_edge(define_objectives, select_channels)
root.order.add_edge(create_content, launch_campaign)
root.order.add_edge(design_visuals, launch_campaign)
root.order.add_edge(select_channels, launch_campaign)
root.order.add_edge(launch_campaign, track_performance)
root.order.add_edge(track_performance, collect_leads)
root.order.add_edge(collect_leads, follow_up)
root.order.add_edge(follow_up, analyze_performance)
root.order.add_edge(analyze_performance, campaign_ends)