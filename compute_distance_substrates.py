import pandas as pd


file_path = '/home/sal/hsesol_nodisp/pery_on_graph/pery_foranalysis.xyz'


df = pd.read_csv(file_path, sep='\s+', header = None, skiprows= 1)

#df = df.drop(df[df.iloc[:, 0] == 'X'].index) #drops dummy atom
#df = df.drop(df[df.iloc[:, 0] == '1465'].index) #drops atom count line at every new step

df = df.reset_index(drop = True)
#print(df)

def process_step(step): 
    step_surface = step.iloc[:111, 3] #defining subchunk for surface and substrate, 3 for z axis
    step_substrate= step.iloc[112:151]
    step_substrate_carbon = step_substrate[step_substrate.iloc[:, 0] == 'C']
    step_substrate_nitrogen = step_substrate[step_substrate.iloc[:, 0] == 'N']
    step_substrate_oxygen = step_substrate[step_substrate.iloc[:, 0] == 'O']
    step_substrate_hydrogen = step_substrate[step_substrate.iloc[:, 0] == 'H']
    return step_surface.mean(), step_substrate.iloc[:, 3].mean(), step_substrate_carbon.iloc[:, 3].mean(), step_substrate_nitrogen.iloc[:, 3].mean(), step_substrate_oxygen.iloc[:, 3].mean(), step_substrate_hydrogen.iloc[:, 3].mean()

step_size = 152 # needs to be adjusted for atom count 

results = []

for step in range(0, len(df), step_size):
    end = step + step_size 
    frame = df.iloc[step:end]
    result = process_step(frame)
    results.append(result)

results_simulation = pd.DataFrame(results)
#print(results_simulation)

overall_average = results_simulation.mean()
print(overall_average)
