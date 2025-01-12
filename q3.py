import numpy as np

def reconstruct_matrix(U, S, V):
    
    S_matrix = np.diag(S)
    
   
    reconstructed_matrix = np.dot(U, np.dot(S_matrix, V))
    
    return reconstructed_matrix


U = np.array([[0.58, -0.58, 0.58], 
              [0.58, 0.81, -0.11], 
              [0.58, -0.05, -0.81]])

S = np.array([17.0, 6.0, 4.0])  

V = np.array([[0.58, 0.58, 0.58], 
              [-0.58, 0.81, -0.05], 
              [0.58, -0.11, -0.81]])

reconstructed = reconstruct_matrix(U, S, V)
print("Reconstructed Matrix:")
print(reconstructed)
