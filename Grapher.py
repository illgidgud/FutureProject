import numpy as np

class Grapher:
    class ParametricCurve:
        """
        Một đường cong tham số hoá trong R^2, gồm phương trình tham số
        và miền xác định.
        """
        def __init__(self, funct, domain):
            self.function = funct
            self.domain = domain

        @staticmethod
        def line_through_two_points(a, b, domain: tuple = (0, 1)):
            """
            Nhận vào hai điểm trong R^2, trả về đường thẳng nối a với b,
            với miền xác định trong khoảng domain.
            """
            t1, t2 = domain
            a, b = np.asarray(a), np.asarray(b)
            def funct(t):
                if t1 <= t <= t2:
                    return (t - t2)/(t1 - t2) * a + (t - t1)/(t2 - t1) * b
                else: return None
            return Grapher.ParametricCurve(funct, domain)
            
        @staticmethod
        def join_curves(curve_list: list):
            """
            Nối một dãy các đường cong tham số. 
            Miền giá trị của các đường cong phải nối tiếp nhau.
            """
            length = len(curve_list)
            if length == 0:
                raise ValueError("Không chấp nhận danh sách rỗng")
            elif length == 1: return curve_list[0]
            else:
                for index in range(length - 1):
                    if curve_list[index].domain[1] != curve_list[index + 1].domain[0]:
                        raise ValueError("Miền giá trị của các đường cong tham số phải nối tiếp nhau.")                
            domain_list = [curve_list[index].domain[0] for index in range(length)] + [curve_list[length - 1].domain[1]]
            def funct(t):
                if t < domain_list[0]: return None
                for index in range(length):
                    if domain_list[index] <= t < domain_list[index + 1]:
                        return curve_list[index].function(t)
                if t == domain_list[length]: return curve_list[length - 1].function(t)
                else: return None
            return Grapher.ParametricCurve(funct = funct, domain = (domain_list[0], domain_list[length]))

        
        @staticmethod
        def line_through_points(point_list: list, domain: tuple = (0, 1)):
            """
            Trả về một đường gấp khúc đi qua các điểm trong danh sách
            điểm đã cho, theo thứ tự đó. Miền xác định mặc định là [0, 1].
            """
            t1, t2 = domain
            number_of_points = len(point_list)
            assert number_of_points >= 2, "Không chấp nhận số điểm nhỏ hơn 2."
            intervals = np.linspace(t1, t2, number_of_points)
            curve_list = []
            for index in range(number_of_points - 1):
                curve = Grapher.ParametricCurve.line_through_two_points(
                    point_list[index], 
                    point_list[index + 1], 
                    (intervals[index], intervals[index + 1]),
                )
                curve_list.append(curve)
            return Grapher.ParametricCurve.join_curves(curve_list)
        
        @classmethod
        def normalize(cls):
            """
            Chuẩn hoá phương trình tham số: đưa miền xác định về [0, 1].
            """
            t1, t2 = cls.domain
            def funct(t):
                if 0 <= t <= 1:
                    return cls.function((1 - t) * t1 + t * t2)
                else: return None
            return Grapher.ParametricCurve(funct, (0, 1))
        
        @staticmethod
        def to3D(function):
            """
            Chuyển tham số từ R^2 sang R^3, với tọa độ thứ ba đồng nhất bằng 0.
            """
            def funct(t):
                return np.append(function(t), 0)
            return funct
        
class SpaceFillingCurve:
    def __init__(self, operation, starting_seeds, *args):
        self.starting_seeds = starting_seeds
        self.operation = operation
        self._final_path_dict = {1: self.starting_seeds}
        self.points_dict = {1: self.starting_seeds[0]["point"]}
    
    @staticmethod
    def from_path_to_points(path: list):
        """
        Chỉ dùng cho path có dạng một danh sách các đối tượng, trong
        đó mỗi đối tượng là một dict với value ứng với key ["point"] chứa
        thông tin về các điểm của đối tượng. Lưu ý: Điểm đầu của đối tượng
        sau phải trùng với điểm cuối của đối tượng trước.
        """
        points_list = []
        for obj in path:
            for elem in obj["point"][:-1]:
                points_list.append(elem)
        points_list.append(path[-1]["point"][-1])
        return points_list

    @property
    def final_path_dict(self):
        return self._final_path_dict
    
    @final_path_dict.setter
    def final_path_dict(self, n: int):
        """
        Đặt lại _final_path_list sao cho nó chứa đúng n bước.
        Điều chỉnh points_list tương ứng chứa n bước.
        """
        assert n >= 1, "Số bước phải ít nhất bằng 1."
        current_length = len(self._final_path_dict)
        if current_length < n:
            times_to_append = n - current_length
            for i in range(times_to_append):
                self._final_path_dict[current_length + i + 1] = self.operation(self._final_path_dict[current_length + i])
                self.points_dict[current_length + i + 1] = SpaceFillingCurve.from_path_to_points(self._final_path_dict[current_length + i + 1])
        else:
            self._final_path_dict = {k:self._final_path_list[k] for k in range(1, n + 1)}
            self.points_dict = {k:self.points_dict[k] for k in range(1, n + 1)}

    def reset_path(self):
        self._final_path_dict = {1: self.starting_seeds}
        self.points_dict = {1: self.starting_seeds[0]["point"]}