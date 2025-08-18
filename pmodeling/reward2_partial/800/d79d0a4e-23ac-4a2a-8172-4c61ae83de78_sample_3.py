import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
Spec_Review = Transition(label='Spec Review')
Component_Pick = Transition(label='Component Pick')
Frame_Build = Transition(label='Frame Build')
Motor_Mount = Transition(label='Motor Mount')
Sensor_Fit = Transition(label='Sensor Fit')
Wiring_Setup = Transition(label='Wiring Setup')
Software_Load = Transition(label='Software Load')
Calibration_Test = Transition(label='Calibration Test')
Stress_Check = Transition(label='Stress Check')
Firmware_Flash = Transition(label='Firmware Flash')
Feedback_Loop = Transition(label='Feedback Loop')
Package_Prep = Transition(label='Package Prep')
Doc_Compile = Transition(label='Doc Compile')
Ship_Arrange = Transition(label='Ship Arrange')
Remote_Setup = Transition(label='Remote Setup')

# Define the partial order
root = StrictPartialOrder(nodes=[Spec_Review, Component_Pick, Frame_Build, Motor_Mount, Sensor_Fit, Wiring_Setup, Software_Load, Calibration_Test, Stress_Check, Firmware_Flash, Feedback_Loop, Package_Prep, Doc_Compile, Ship_Arrange, Remote_Setup])
root.order.add_edge(Spec_Review, Component_Pick)
root.order.add_edge(Component_Pick, Frame_Build)
root.order.add_edge(Frame_Build, Motor_Mount)
root.order.add_edge(Motor_Mount, Sensor_Fit)
root.order.add_edge(Sensor_Fit, Wiring_Setup)
root.order.add_edge(Wiring_Setup, Software_Load)
root.order.add_edge(Software_Load, Calibration_Test)
root.order.add_edge(Calibration_Test, Stress_Check)
root.order.add_edge(Stress_Check, Firmware_Flash)
root.order.add_edge(Firmware_Flash, Feedback_Loop)
root.order.add_edge(Feedback_Loop, Package_Prep)
root.order.add_edge(Package_Prep, Doc_Compile)
root.order.add_edge(Doc_Compile, Ship_Arrange)
root.order.add_edge(Ship_Arrange, Remote_Setup)