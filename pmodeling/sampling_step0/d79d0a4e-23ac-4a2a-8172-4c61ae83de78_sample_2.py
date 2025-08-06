import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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
Skip = SilentTransition()

# Define loops
Component_Pick_Frame_Build = OperatorPOWL(operator=Operator.LOOP, children=[Component_Pick, Frame_Build])
Motor_Mount_Sensor_Fit = OperatorPOWL(operator=Operator.LOOP, children=[Motor_Mount, Sensor_Fit])
Wiring_Setup_Software_Load = OperatorPOWL(operator=Operator.LOOP, children=[Wiring_Setup, Software_Load])
Calibration_Test_Stress_Check = OperatorPOWL(operator=Operator.LOOP, children=[Calibration_Test, Stress_Check])
Firmware_Flash_Feedback_Loop = OperatorPOWL(operator=Operator.LOOP, children=[Firmware_Flash, Feedback_Loop])

# Define XORs
XOR_1 = OperatorPOWL(operator=Operator.XOR, children=[Package_Prep, Skip])
XOR_2 = OperatorPOWL(operator=Operator.XOR, children=[Doc_Compile, Skip])
XOR_3 = OperatorPOWL(operator=Operator.XOR, children=[Ship_Arrange, Skip])
XOR_4 = OperatorPOWL(operator=Operator.XOR, children=[Remote_Setup, Skip])

# Define root POWL model
root = StrictPartialOrder(nodes=[
    Spec_Review,
    Component_Pick_Frame_Build,
    Motor_Mount_Sensor_Fit,
    Wiring_Setup_Software_Load,
    Calibration_Test_Stress_Check,
    Firmware_Flash_Feedback_Loop,
    XOR_1,
    XOR_2,
    XOR_3,
    XOR_4
])

# Define dependencies
root.order.add_edge(Spec_Review, Component_Pick_Frame_Build)
root.order.add_edge(Component_Pick_Frame_Build, Motor_Mount_Sensor_Fit)
root.order.add_edge(Motor_Mount_Sensor_Fit, Wiring_Setup_Software_Load)
root.order.add_edge(Wiring_Setup_Software_Load, Calibration_Test_Stress_Check)
root.order.add_edge(Calibration_Test_Stress_Check, Firmware_Flash_Feedback_Loop)
root.order.add_edge(Firmware_Flash_Feedback_Loop, XOR_1)
root.order.add_edge(XOR_1, Package_Prep)
root.order.add_edge(XOR_1, Doc_Compile)
root.order.add_edge(XOR_1, Ship_Arrange)
root.order.add_edge(XOR_1, Remote_Setup)
root.order.add_edge(XOR_2, Package_Prep)
root.order.add_edge(XOR_2, Doc_Compile)
root.order.add_edge(XOR_2, Ship_Arrange)
root.order.add_edge(XOR_2, Remote_Setup)
root.order.add_edge(XOR_3, Package_Prep)
root.order.add_edge(XOR_3, Doc_Compile)
root.order.add_edge(XOR_3, Ship_Arrange)
root.order.add_edge(XOR_3, Remote_Setup)
root.order.add_edge(XOR_4, Package_Prep)
root.order.add_edge(XOR_4, Doc_Compile)
root.order.add_edge(XOR_4, Ship_Arrange)
root.order.add_edge(XOR_4, Remote_Setup)