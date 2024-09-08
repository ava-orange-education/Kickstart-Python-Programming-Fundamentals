import numpy as np

def basic_vector_operations():
    # Create two vectors
    vector1 = np.array([1, 2, 3])
    vector2 = np.array([4, 5, 6])
    
    # Calculate the dot product of the vectors
    dot_product = np.dot(vector1, vector2)
    print(f"Dot Product: {dot_product}")
    
    # Calculate the cross product of the vectors
    cross_product = np.cross(vector1, vector2)
    print(f"Cross Product: {cross_product}")

# Execute the function if the script is run directly
if __name__ == "__main__":
    basic_vector_operations()
