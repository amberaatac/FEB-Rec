Progress log 
- [x] Heat Load Calculations: 
    - Calculated the heat that needs to be dissipated by the EMRAX 228 motor and the Rinehart PM100DZ motor controller.
    - Used the peak power output and continuous power output specifications, along with assumed efficiencies, to estimate the heat generated by the motor and controller.  
    - Summed the heat generated by both components to estimate the total heat load that the cooling system must dissipate.

- [x] Initial Assumptions for Cooling System Design:
    - Identified the specific heat capacity of the coolant mixture (50/50 Ethylene Glycol and Water).
    - Established coolant flow rates based on the datasheet recommendations for both the motor and the controller.
    - Assumed overall heat transfer coefficient (U) and heat transfer surface area (A) for the cooling system's radiator.
    - Effectiveness Calculation for Hypothetical Heat Exchanger:

- [x] Calculated the Number of Transfer Units (NTU) based on the overall heat transfer coefficient and minimum thermal capacity rate.
    - Estimated the heat exchanger effectiveness for a parallel flow heat exchanger using the NTU method.
    - Determined the maximum possible heat transfer rate and the actual heat transfer rate for the cooling system based on the calculated effectiveness.
    - Verification Against Required Heat Dissipation:

- [x]Compared the calculated actual heat transfer rate to the total heat load required to be dissipated to determine if the hypothetical cooling system is sufficient.


TODO: 
- [ ] Detailed Component Selection:
    - Selection of the 
        - radiator
        - pump

- [ ] Simulation Modeling:
    - A detailed simulation model of the radiator's thermal dissipation characteristics, which could influence the final component selection.

- [ ] Testing and Validation:
    - Development of a testing protocol to validate the cooling system's performance.
    Incorporation of necessary sensors and monitoring equipment to measure system effectiveness in real-world conditions.

- [ ] System Integration and Documentation:
    - Detailed planning of how the system components will be integrated into the vehicle.
    Thorough documentation of the design process, simulation outcomes, testing protocols, and final results.

- [ ] Iterative Design Improvements:
    - Analysis of initial test results to improve and optimize the cooling system design.
    - Iteration of the design based on findings to ensure reliability and compliance with FSAE rules.