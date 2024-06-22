def parse_matrix(matrix_str):
    """Parse the input string into a matrix."""
    matrix = []
    rows = matrix_str.strip().split('|')
    for row in rows:
        matrix.append([int(x) for x in row.split(',')])
    return matrix

def matrix_to_dict(matrix):
    """Convert a matrix (list of lists) to a dictionary."""
    return {i: matrix[i] for i in range(len(matrix))}

def dict_to_matrix(matrix_dict):
    """Convert a dictionary back to a matrix (list of lists)."""
    return [matrix_dict[i] for i in range(len(matrix_dict))]

def matrix_multiplication(U_dict, V_dict):
    """Multiply two matrices U and V given as dictionaries."""
    n = len(U_dict)
    M_dict = {i: [0] * n for i in range(n)}
    for i in range(n):
        for j in range(n):
            M_dict[i][j] = sum(U_dict[i][k] * V_dict[k][j] for k in range(n))
    return M_dict

def main():
    # Input matrices U and V
    U_str = input("Enter matrix U : ")
    V_str = input("Enter matrix V : ")

    # Parse the input strings into matrices
    U = parse_matrix(U_str)
    V = parse_matrix(V_str)

    # Convert matrices to dictionaries
    U_dict = matrix_to_dict(U)
    V_dict = matrix_to_dict(V)

    # Compute the resulting matrix M as a dictionary
    M_dict = matrix_multiplication(U_dict, V_dict)

    # Convert the resulting dictionary back to a matrix
    M = dict_to_matrix(M_dict)

    # Print the resulting matrix
    print("M = U x V")
    for row in M:
        print(row)

if __name__ == "__main__":
    main()
