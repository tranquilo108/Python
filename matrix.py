import logging
import argparse


class Matrix:
    """
    Класс, представляющий матрицу.

    Атрибуты:
    - rows (int): количество строк в матрице
    - cols (int): количество столбцов в матрице
    - data (list): двумерный список, содержащий элементы матрицы

    Методы:
    - __str__(): возвращает строковое представление матрицы
    - __repr__(): возвращает строковое представление матрицы, которое может быть использовано для создания нового объекта
    - __eq__(other): определяет операцию "равно" для двух матриц
    - __add__(other): определяет операцию сложения двух матриц
    - __mul__(other): определяет операцию умножения двух матриц
    """

    def __init__(self, rows, cols, values=None):
        self.logger = logging.Logger('logger')
        self.rows = rows
        self.cols = cols
        if values is not None:
            if len(values) != rows or any(len(row) != cols for row in values):
                raise ValueError("Неправильные размеры данных для матрицы")
            self.data = values
        else:
            self.data = [[0 for j in range(cols)] for i in range(rows)]

    def __str__(self):
        """
        Возвращает строковое представление матрицы.

        Возвращает:
        - str: строковое представление матрицы
        """
        return '\n'.join([' '.join([str(self.data[i][j]) for j in range(self.cols)]) for i in range(self.rows)])

    def __repr__(self):
        """
        Возвращает строковое представление матрицы, которое может быть использовано для создания нового объекта.

        Возвращает:
        - str: строковое представление матрицы
        """
        return f"Matrix({self.rows}, {self.cols}, values={self.data})"

    def __eq__(self, other):
        """
        Определяет операцию "равно" для двух матриц.

        Аргументы:
        - other (Matrix): вторая матрица

        Возвращает:
        - bool: True, если матрицы равны, иначе False
        """
        if self.rows != other.rows or self.cols != other.cols:
            return False
        for i in range(self.rows):
            for j in range(self.cols):
                if self.data[i][j] != other.data[i][j]:
                    return False
        return True

    def __add__(self, other):
        """
        Определяет операцию сложения двух матриц.

        Аргументы:
        - other (Matrix): вторая матрица

        Возвращает:
        - Matrix: новая матрица, полученная путем сложения двух исходных матриц
        """
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы должны иметь одинаковые размеры")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result

    def __mul__(self, other):
        """
        Определяет операцию умножения двух матриц.

        Аргументы:
        - other (Matrix): вторая матрица

        Возвращает:
        - Matrix: новая матрица, полученная путем умножения двух исходных матриц
        """
        if self.cols != other.rows:
            raise ValueError("Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы")
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        return result


def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def main():
    parser = argparse.ArgumentParser(description="Matrix operations")
    parser.add_argument('--rows1', type=int, help='Number of rows in the first matrix')
    parser.add_argument('--cols1', type=int, help='Number of columns in the first matrix')
    parser.add_argument('--rows2', type=int, help='Number of rows in the second matrix')
    parser.add_argument('--cols2', type=int, help='Number of columns in the second matrix')
    parser.add_argument('--values1', type=int, nargs='+', help='Values of the first matrix (space-separated)')
    parser.add_argument('--values2', type=int, nargs='+', help='Values of the second matrix (space-separated)')

    args = parser.parse_args()

    setup_logging()

    try:
        matrix1 = Matrix(args.rows1, args.cols1,
                         [args.values1[i:i + args.cols1] for i in range(0, len(args.values1), args.cols1)])
        matrix2 = Matrix(args.rows2, args.cols2,
                         [args.values2[i:i + args.cols2] for i in range(0, len(args.values2), args.cols2)])

        print("Matrix 1:")
        print(matrix1)
        print("\nMatrix 2:")
        print(matrix2)
        print("\nMatrix 1 + Matrix 2:")
        print(matrix1 + matrix2)
        print("\nMatrix 1 * Matrix 2:")
        print(matrix1 * matrix2)

    except ValueError as e:
        logging.error(f"Error: {e}")


if __name__ == "__main__":
    main()
