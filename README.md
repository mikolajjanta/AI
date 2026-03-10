# AI
ai tasks from labs


Fuzzy Systems
Lander control
A fuzzy lander controller should be designed to select force F value depending on the amount of fuel,
height and speed of the lander. Show the simulation on the charts. For initial assessment of the lander
behavior you can use the manual control option using script landster_by_hand.m. Using this script, you
can also generate examples for learning an ANFIS fuzzy system (see example scripts sug1.m and AN.m).
After starting the fuzzy system editor in Matlab with the fuzzy command, create a system that calculates
the force based on 3 input variables. For this purpose, fuzzy sets should be proposed for each variable (3
input and 1 output) and a set of control rules. After saving the system to disk (File/Export/To disk),
modify the landsym.m script by entering the fuzzy system file name in the line fis=readfis(...).
The fuzzy system must contain at least one rule. If you haven't any, you can comment lines 10, 25 and
uncomment line 26 then run the landsym script in the Matlab dialog box. If After the script has finished
running, the results of 5 simulations appear on the screen for 5 different initial states. Operation of the
fuzzy controller can be considered correct if the absolute value of the lander end speed does not exceed 5
m/s in any simulation. Running the additional landsym2.m script allows you to observe the fuzzy
inference process.

<img width="669" height="498" alt="image" src="https://github.com/user-attachments/assets/431dee62-44f6-4006-bc43-65319e4e4de7" />
