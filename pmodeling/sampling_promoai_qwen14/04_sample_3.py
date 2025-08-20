import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
Define_campaign_objectives = Transition(label='Define campaign objectives')
Create_content = Transition(label='Create content')
Design_visuals = Transition(label='Design visuals')
Select_promotion_channels = Transition(label='Select promotion channels')
Launch_campaign = Transition(label='Launch campaign')
Track_performance_in_real_time = Transition(label='Track performance in real-time')
Collect_leads_in_CRM_system = Transition(label='Collect leads in CRM system')
Sales_teams_follows_up_on_leads = Transition(label='Sales teams follows up on leads')
Analyze_performance_for_future_optimization = Transition(label='Analyze performance for future optimization')
Campaign_period_ends = Transition(label='Campaign period ends')

# Define silent transition
skip = SilentTransition()

# Define loops
Track_performance_loop = OperatorPOWL(operator=Operator.LOOP, children=[Track_performance_in_real_time, skip])

# Define choices
Sales_team_choice = OperatorPOWL(operator=Operator.XOR, children=[Sales_teams_follows_up_on_leads, skip])
Analyze_performance_choice = OperatorPOWL(operator=Operator.XOR, children=[Analyze_performance_for_future_optimization, skip])

# Define partial orders
pre_campaign_order = StrictPartialOrder(nodes=[Define_campaign_objectives, Create_content, Design_visuals, Select_promotion_channels])
campaign_order = StrictPartialOrder(nodes=[Launch_campaign, Track_performance_loop])
post_campaign_order = StrictPartialOrder(nodes=[Collect_leads_in_CRM_system, Sales_team_choice, Analyze_performance_choice])

# Connect partial orders
root = StrictPartialOrder(nodes=[pre_campaign_order, campaign_order, post_campaign_order])
root.order.add_edge(pre_campaign_order, campaign_order)
root.order.add_edge(campaign_order, post_campaign_order)