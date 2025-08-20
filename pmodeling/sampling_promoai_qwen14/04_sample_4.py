import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
define_campaign_objectives = Transition(label='Define campaign objectives')
create_content = Transition(label='Create content')
design_visuals = Transition(label='Design visuals')
select_promotion_channels = Transition(label='Select promotion channels')
launch_campaign = Transition(label='Launch campaign')
track_performance = Transition(label='Track performance in real-time')
collect_leads = Transition(label='Collect leads in CRM system')
sales_follow_up = Transition(label='Sales teams follows up on leads')
analyze_performance = Transition(label='Analyze performance for future optimization')
campaign_ends = Transition(label='Campaign period ends')

# Create the partial order for the process
root = StrictPartialOrder(nodes=[define_campaign_objectives, create_content, design_visuals, select_promotion_channels, launch_campaign, track_performance, collect_leads, sales_follow_up, analyze_performance, campaign_ends])
root.order.add_edge(define_campaign_objectives, create_content)
root.order.add_edge(create_content, design_visuals)
root.order.add_edge(design_visuals, select_promotion_channels)
root.order.add_edge(select_promotion_channels, launch_campaign)
root.order.add_edge(launch_campaign, track_performance)
root.order.add_edge(track_performance, collect_leads)
root.order.add_edge(collect_leads, sales_follow_up)
root.order.add_edge(sales_follow_up, analyze_performance)
root.order.add_edge(analyze_performance, campaign_ends)