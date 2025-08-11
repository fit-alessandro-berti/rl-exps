import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
AnalyzePerformance = Transition(label='Analyze performance for future optimization')
CampaignEnds = Transition(label='Campaign period ends')
CollectLeads = Transition(label='Collect leads in CRM system')
CreateContent = Transition(label='Create content')
DefineObjectives = Transition(label='Define campaign objectives')
DesignVisuals = Transition(label='Design visuals')
LaunchCampaign = Transition(label='Launch campaign')
SalesFollowUp = Transition(label='Sales teams follows up on leads')
SelectChannels = Transition(label='Select promotion channels')
TrackPerformance = Transition(label='Track performance in real-time')

# Define the partial order
root = StrictPartialOrder(nodes=[DefineObjectives, CreateContent, DesignVisuals, SelectChannels, LaunchCampaign, TrackPerformance, CollectLeads, SalesFollowUp, AnalyzePerformance, CampaignEnds])
root.order.add_edge(DefineObjectives, CreateContent)
root.order.add_edge(CreateContent, DesignVisuals)
root.order.add_edge(DesignVisuals, SelectChannels)
root.order.add_edge(SelectChannels, LaunchCampaign)
root.order.add_edge(LaunchCampaign, TrackPerformance)
root.order.add_edge(TrackPerformance, CollectLeads)
root.order.add_edge(CollectLeads, SalesFollowUp)
root.order.add_edge(SalesFollowUp, AnalyzePerformance)
root.order.add_edge(AnalyzePerformance, CampaignEnds)