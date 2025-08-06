from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
Assess_Structure = Transition(label='Assess Structure')
Analyze_Environment = Transition(label='Analyze Environment')
Design_Modules = Transition(label='Design Modules')
Procure_Materials = Transition(label='Procure Materials')
Install_Irrigation = Transition(label='Install Irrigation')
Set_Sensors = Transition(label='Set Sensors')
Select_Seeds = Transition(label='Select Seeds')
Schedule_Planting = Transition(label='Schedule Planting')
Monitor_Growth = Transition(label='Monitor Growth')
Collect_Data = Transition(label='Collect Data')
Manage_Pests = Transition(label='Manage Pests')
Harvest_Crops = Transition(label='Harvest Crops')
Coordinate_Sales = Transition(label='Coordinate Sales')
Compost_Waste = Transition(label='Compost Waste')
Review_Feedback = Transition(label='Review Feedback')

# Define the POWL model
root = StrictPartialOrder(
    nodes=[
        Assess_Structure,
        Analyze_Environment,
        Design_Modules,
        Procure_Materials,
        Install_Irrigation,
        Set_Sensors,
        Select_Seeds,
        Schedule_Planting,
        Monitor_Growth,
        Collect_Data,
        Manage_Pests,
        Harvest_Crops,
        Coordinate_Sales,
        Compost_Waste,
        Review_Feedback
    ],
    order={
        Assess_Structure: Analyze_Environment,
        Analyze_Environment: Design_Modules,
        Design_Modules: Procure_Materials,
        Procure_Materials: Install_Irrigation,
        Install_Irrigation: Set_Sensors,
        Set_Sensors: Select_Seeds,
        Select_Seeds: Schedule_Planting,
        Schedule_Planting: Monitor_Growth,
        Monitor_Growth: Collect_Data,
        Collect_Data: Manage_Pests,
        Manage_Pests: Harvest_Crops,
        Harvest_Crops: Coordinate_Sales,
        Coordinate_Sales: Compost_Waste,
        Compost_Waste: Review_Feedback
    }
)

# Add dependencies between activities
root.order.add_edge(Analyze_Environment, Design_Modules)
root.order.add_edge(Design_Modules, Procure_Materials)
root.order.add_edge(Procure_Materials, Install_Irrigation)
root.order.add_edge(Install_Irrigation, Set_Sensors)
root.order.add_edge(Set_Sensors, Select_Seeds)
root.order.add_edge(Select_Seeds, Schedule_Planting)
root.order.add_edge(Schedule_Planting, Monitor_Growth)
root.order.add_edge(Monitor_Growth, Collect_Data)
root.order.add_edge(Collect_Data, Manage_Pests)
root.order.add_edge(Manage_Pests, Harvest_Crops)
root.order.add_edge(Harvest_Crops, Coordinate_Sales)
root.order.add_edge(Coordinate_Sales, Compost_Waste)
root.order.add_edge(Compost_Waste, Review_Feedback)