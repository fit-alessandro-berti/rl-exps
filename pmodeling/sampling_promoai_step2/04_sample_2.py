import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
analyze_performance = Transition(label='Analyze performance for future optimization')
campaign_period_ends = Transition(label='Campaign period ends')
collect_leads_in_crm = Transition(label='Collect leads in CRM system')
create_content = Transition(label='Create content')
define_campaign_objectives = Transition(label='Define campaign objectives')
design_visuals = Transition(label='Design visuals')
launch_campaign = Transition(label='Launch campaign')
sales_teams_follows_up_on_leads = Transition(label='Sales teams follows up on leads')
select_promotion_channels = Transition(label='Select promotion channels')
track_performance_in_real_time = Transition(label='Track performance in real-time')

# Create the partial order
root = StrictPartialOrder(nodes=[
    analyze_performance, 
    campaign_period_ends, 
    collect_leads_in_crm, 
    create_content, 
    define_campaign_objectives, 
    design_visuals, 
    launch_campaign, 
    sales_teams_follows_up_on_leads, 
    select_promotion_channels, 
    track_performance_in_real_time
])

# Define the dependencies
root.order.add_edge(define_campaign_objectives, create_content)
root.order.add_edge(create_content, design_visuals)
root.order.add_edge(design_visuals, select_promotion_channels)
root.order.add_edge(select_promotion_channels, launch_campaign)
root.order.add_edge(launch_campaign, track_performance_in_real_time)
root.order.add_edge(track_performance_in_real_time, collect_leads_in_crm)
root.order.add_edge(collect_leads_in_crm, sales_teams_follows_up_on_leads)
root.order.add_edge(sales_teams_follows_up_on_leads, analyze_performance)
root.order.add_edge(analyze_performance, campaign_period_ends)

print(root)