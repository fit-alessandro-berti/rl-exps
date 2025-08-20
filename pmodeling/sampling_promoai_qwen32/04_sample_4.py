import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
define_objectives = Transition(label='Define campaign objectives')
create_content = Transition(label='Create content')
design_visuals = Transition(label='Design visuals')
select_channels = Transition(label='Select promotion channels')
launch_campaign = Transition(label='Launch campaign')
track_performance = Transition(label='Track performance in real-time')
collect_leads = Transition(label='Collect leads in CRM system')
follow_up = Transition(label='Sales teams follows up on leads')
end_campaign = Transition(label='Campaign period ends')
analyze_performance = Transition(label='Analyze performance for future optimization')

# Create a loop for the campaign execution
campaign_execution = OperatorPOWL(operator=Operator.LOOP, children=[launch_campaign, track_performance, collect_leads, follow_up])

# Create a choice for whether to continue the campaign or end it
campaign_choice = OperatorPOWL(operator=Operator.XOR, children=[campaign_execution, end_campaign])

# Define the order of activities
root = StrictPartialOrder(nodes=[define_objectives, create_content, design_visuals, select_channels, campaign_choice, analyze_performance])
root.order.add_edge(define_objectives, create_content)
root.order.add_edge(create_content, design_visuals)
root.order.add_edge(design_visuals, select_channels)
root.order.add_edge(select_channels, campaign_choice)
root.order.add_edge(campaign_choice, analyze_performance)