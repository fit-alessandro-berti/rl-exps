import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
define_objectives = Transition(label='Define campaign objectives')
create_content = Transition(label='Create content')
design_visuals = Transition(label='Design visuals')
select_channels = Transition(label='Select promotion channels')
launch_campaign = Transition(label='Launch campaign')
track_performance = Transition(label='Track performance in real-time')
collect_leads = Transition(label='Collect leads in CRM system')
follow_up_leads = Transition(label='Sales teams follows up on leads')
analyze_performance = Transition(label='Analyze performance for future optimization')
end_period = Transition(label='Campaign period ends')

# Create a choice for selecting promotion channels
select_channels_xor = OperatorPOWL(operator=Operator.XOR, children=[select_channels])

# Create a loop for tracking performance and collecting leads
track_and_collect_loop = OperatorPOWL(operator=Operator.LOOP, children=[track_performance, collect_leads])

# Create a choice for following up on leads or ending the campaign period
follow_up_or_end_xor = OperatorPOWL(operator=Operator.XOR, children=[follow_up_leads, end_period])

# Create the root of the POWL model
root = StrictPartialOrder(nodes=[
    define_objectives,
    create_content,
    design_visuals,
    select_channels_xor,
    launch_campaign,
    track_and_collect_loop,
    follow_up_or_end_xor,
    analyze_performance
])

# Define the partial order
root.order.add_edge(define_objectives, create_content)
root.order.add_edge(create_content, design_visuals)
root.order.add_edge(design_visuals, select_channels_xor)
root.order.add_edge(select_channels_xor, launch_campaign)
root.order.add_edge(launch_campaign, track_and_collect_loop)
root.order.add_edge(track_and_collect_loop, follow_up_or_end_xor)
root.order.add_edge(follow_up_or_end_xor, analyze_performance)

root