import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Define_campaign_objectives = Transition(label='Define campaign objectives')
Create_content = Transition(label='Create content')
Design_visuals = Transition(label='Design visuals')
Select_promotion_channels = Transition(label='Select promotion channels')
Launch_campaign = Transition(label='Launch campaign')
Track_performance_in_real_time = Transition(label='Track performance in real-time')
Collect_leads_in_CRM_system = Transition(label='Collect leads in CRM system')
Sales_teams_follows_up_on_leads = Transition(label='Sales teams follows up on leads')
Campaign_period_ends = Transition(label='Campaign period ends')
Analyze_performance_for_future_optimization = Transition(label='Analyze performance for future optimization')

# Define the loop structure
loop = OperatorPOWL(operator=Operator.LOOP, children=[Track_performance_in_real_time, Collect_leads_in_CRM_system, Sales_teams_follows_up_on_leads])

# Define the exclusive choice structure
xor = OperatorPOWL(operator=Operator.XOR, children=[Campaign_period_ends, Analyze_performance_for_future_optimization])

# Define the partial order structure
root = StrictPartialOrder(nodes=[Define_campaign_objectives, Create_content, Design_visuals, Select_promotion_channels, Launch_campaign, loop, xor])

# Define the order of transitions
root.order.add_edge(Define_campaign_objectives, Create_content)
root.order.add_edge(Create_content, Design_visuals)
root.order.add_edge(Design_visuals, Select_promotion_channels)
root.order.add_edge(Select_promotion_channels, Launch_campaign)
root.order.add_edge(Launch_campaign, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(Campaign_period_ends, Analyze_performance_for_future_optimization)

print(root)