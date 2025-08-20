import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
define_campaign_objectives = Transition(label='Define campaign objectives')
create_content = Transition(label='Create content')
design_visuals = Transition(label='Design visuals')
select_promotion_channels = Transition(label='Select promotion channels')
launch_campaign = Transition(label='Launch campaign')
track_performance_in_real_time = Transition(label='Track performance in real-time')
collect_leads_in_crm_system = Transition(label='Collect leads in CRM system')
sales_teams_follow_up_on_leads = Transition(label='Sales teams follows up on leads')
analyze_performance_for_future_optimization = Transition(label='Analyze performance for future optimization')
campaign_period_ends = Transition(label='Campaign period ends')

# Define silent transition
skip = SilentTransition()

# Define operator POWLs
launch_campaign_loop = OperatorPOWL(operator=Operator.LOOP, children=[launch_campaign, track_performance_in_real_time])
collect_leads_in_crm_system_xor = OperatorPOWL(operator=Operator.XOR, children=[collect_leads_in_crm_system, skip])
sales_teams_follow_up_on_leads_xor = OperatorPOWL(operator=Operator.XOR, children=[sales_teams_follow_up_on_leads, skip])
analyze_performance_for_future_optimization_xor = OperatorPOWL(operator=Operator.XOR, children=[analyze_performance_for_future_optimization, skip])

# Define partial order
root = StrictPartialOrder(nodes=[
    define_campaign_objectives,
    create_content,
    design_visuals,
    select_promotion_channels,
    launch_campaign_loop,
    collect_leads_in_crm_system_xor,
    sales_teams_follow_up_on_leads_xor,
    analyze_performance_for_future_optimization_xor,
    campaign_period_ends
])

# Define dependencies
root.order.add_edge(define_campaign_objectives, create_content)
root.order.add_edge(create_content, design_visuals)
root.order.add_edge(design_visuals, select_promotion_channels)
root.order.add_edge(select_promotion_channels, launch_campaign_loop)
root.order.add_edge(launch_campaign_loop, collect_leads_in_crm_system_xor)
root.order.add_edge(collect_leads_in_crm_system_xor, sales_teams_follow_up_on_leads_xor)
root.order.add_edge(sales_teams_follow_up_on_leads_xor, analyze_performance_for_future_optimization_xor)
root.order.add_edge(analyze_performance_for_future_optimization_xor, campaign_period_ends)