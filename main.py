import numpy as np

# EMRAX 228 Motor
motor_peak_power = 124000  # Peak power in Watts
motor_continuous_power = 75000  # Continuous power in Watts
motor_efficiency = 0.96  # Motor efficiency
motor_coolant_flow_rate = 6 / 60  # Coolant flow rate in kg/s (from 6 L/min to kg/s)

# Rinehart PM100DZ Motor Controller
controller_continuous_power = motor_continuous_power  # Assuming the controller's power is the same as motor's continuous power for this calculation
controller_efficiency = 0.97  # Controller efficiency
controller_coolant_flow_rate = 10 / 60  # Coolant flow rate in kg/s (from 10 L/min to kg/s)

# Combined cooling requirements
combined_coolant_flow_rate = motor_coolant_flow_rate + controller_coolant_flow_rate  # Combined flow rate for coolant

# Specific heat capacity of coolant - Assuming 50/50 Ethylene Glycol and Water mixture
Cp_coolant = 3680  # Specific heat capacity in J/(kg*K) for 50/50 EGW mix

# Heat dissipation calculations
heat_dissipated_motor = (1 - motor_efficiency) * motor_peak_power  # Heat to be dissipated by motor
heat_dissipated_controller = (1 - controller_efficiency) * controller_continuous_power  # Heat to be dissipated by controller

# Total heat to be dissipated by the cooling system
total_heat_dissipation = heat_dissipated_motor + heat_dissipated_controller

# Print the results
print(f"Heat to be dissipated by the motor: {heat_dissipated_motor:.2f} W")
print(f"Heat to be dissipated by the controller: {heat_dissipated_controller:.2f} W")
print(f"Total heat to be dissipated by the cooling system: {total_heat_dissipation:.2f} W")

# Assuming an ambient temperature of 30 degrees Celsius for the cooling system design
T_ambient = 30  # Ambient temperature in degrees Celsius

# Assuming inlet temperature for coolant is the max coolant temperature for both motor and controller
T_motor_inlet = 50  # Inlet coolant temperature for the motor in degrees Celsius
T_controller_inlet = 80  # Inlet coolant temperature for the controller in degrees Celsius

# Assuming the cooling system can maintain the inlet temperature at the maximum temperature specs
T_motor_outlet = T_ambient  # Outlet coolant temperature for the motor in degrees Celsius
T_controller_outlet = T_ambient  # Outlet coolant temperature for the controller in degrees Celsius

# Calculate the thermal capacity rates for coolant in the motor and controller
C_motor_coolant = motor_coolant_flow_rate * Cp_coolant
C_controller_coolant = controller_coolant_flow_rate * Cp_coolant

# Total thermal capacity rate for the combined coolant
C_total_coolant = combined_coolant_flow_rate * Cp_coolant

# Assuming an overall heat transfer coefficient (U) and heat transfer surface area (A)
U = 300  # Overall heat transfer coefficient in W/(m^2*K)
A = 1  # Heat transfer surface area in m^2

# Calculate the NTU (Number of Transfer Units)
NTU = U * A / C_total_coolant

# Calculate the heat capacity ratio
Cr = C_total_coolant / max(C_motor_coolant, C_controller_coolant)

# Estimate the effectiveness based on the NTU and Cr for a parallel flow heat exchanger
effectiveness = 1 - np.exp(-NTU * (1 + Cr)) / (1 + Cr)

# Calculate the maximum possible heat transfer rate
Q_max = C_total_coolant * (max(T_motor_inlet, T_controller_inlet) - T_ambient)

# Calculate the actual heat transfer rate using the effectiveness
Q_actual = effectiveness * Q_max

# Display results
print(f'Effectiveness: {effectiveness:.2f}')
print(f'Maximum possible heat transfer rate: {Q_max:.2f} W')
print(f'Actual heat transfer rate: {Q_actual:.2f} W')

# Check if the cooling system meets the requirements
if Q_actual >= total_heat_dissipation:
    print('The cooling system is sufficient.')
else:
    print('The cooling system is NOT sufficient.')