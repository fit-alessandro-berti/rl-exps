import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
DefineCampaignObjectives = Transition(label='Define campaign objectives')
CreateContent = Transition(label='Create content')
DesignVisuals = Transition(label='Design visuals')
SelectPromotionChannels = Transition(label='Select promotion channels')
LaunchCampaign = Transition(label='Launch campaign')
TrackPerformance = Transition(label='Track performance in real-time')
CollectLeads = Transition(label='Collect leads in CRM system')
SalesFollowUp = Transition(label='Sales teams follows up on leads')
CampaignEnds = Transition(label='Campaign period ends')
AnalyzePerformance = Transition(label='Analyze performance for future optimization')

# Define the partial order
root = StrictPartialOrder(nodes=[DefineCampaignObjectives, CreateContent, DesignVisuals, SelectPromotionChannels, LaunchCampaign, TrackPerformance, CollectLeads, SalesFollowUp, CampaignEnds, AnalyzePerformance])

# Define the order (dependencies)
root.order.add_edge(DefineCampaignObjectives, CreateContent)
root.order.add_edge(DefineCampaignObjectives, DesignVisuals)
root.order.add_edge(DefineCampaignObjectives, SelectPromotionChannels)
root.order.add_edge(CreateContent, LaunchCampaign)
root.order.add_edge(DesignVisuals, LaunchCampaign)
root.order.add_edge(SelectPromotionChannels, LaunchCampaign)
root.order.add_edge(LaunchCampaign, TrackPerformance)
root.order.add_edge(TrackPerformance, CollectLeads)
root.order.add_edge(CollectLeads, SalesFollowUp)
root.order.add_edge(SalesFollowUp, CampaignEnds)
root.order.add_edge(CampaignEnds, AnalyzePerformance)

# The final POWL model is now stored in the variable 'root'