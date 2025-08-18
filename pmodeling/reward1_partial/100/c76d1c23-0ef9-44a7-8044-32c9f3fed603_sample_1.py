import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Site_Survey = Transition(label='Site Survey')
Zoning_Check = Transition(label='Zoning Check')
Design_Layout = Transition(label='Design Layout')
System_Order = Transition(label='System Order')
Structure_Build = Transition(label='Structure Build')
Install_Hydroponics = Transition(label='Install Hydroponics')
Calibrate_Sensors = Transition(label='Calibrate Sensors')
Select_Crops = Transition(label='Select Crops')
Plant_Seeding = Transition(label='Plant Seeding')
Monitor_Growth = Transition(label='Monitor Growth')
Manage_Pests = Transition(label='Manage Pests')
Schedule_Harvest = Transition(label='Schedule Harvest')
Package_Produce = Transition(label='Package Produce')
Local_Delivery = Transition(label='Local Delivery')
Analyze_Data = Transition(label='Analyze Data')

# Define silent transitions
skip = SilentTransition()

# Define exclusive choices
Calibration = OperatorPOWL(operator=Operator.XOR, children=[Calibrate_Sensors, skip])
Crops = OperatorPOWL(operator=Operator.XOR, children=[Select_Crops, skip])
Pests = OperatorPOWL(operator=Operator.XOR, children=[Manage_Pests, skip])

# Define loops
Structure_Building = OperatorPOWL(operator=Operator.LOOP, children=[Structure_Build, Install_Hydroponics])
Planting = OperatorPOWL(operator=Operator.LOOP, children=[Plant_Seeding, Monitor_Growth, Pests])
Harvesting = OperatorPOWL(operator=Operator.LOOP, children=[Schedule_Harvest, Package_Produce, Local_Delivery])

# Define root partial order
root = StrictPartialOrder(nodes=[Site_Survey, Zoning_Check, Design_Layout, System_Order, Structure_Building, Calibration, Crops, Harvesting, Analyze_Data])
root.order.add_edge(Site_Survey, Zoning_Check)
root.order.add_edge(Zoning_Check, Design_Layout)
root.order.add_edge(Design_Layout, System_Order)
root.order.add_edge(System_Order, Structure_Building)
root.order.add_edge(Structure_Building, Install_Hydroponics)
root.order.add_edge(Install_Hydroponics, Calibration)
root.order.add_edge(Calibration, Crops)
root.order.add_edge(Crops, Harvesting)
root.order.add_edge(Harvesting, Analyze_Data)