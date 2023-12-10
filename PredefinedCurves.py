import numpy as np
from Grapher import SpaceFillingCurve
from pathlib import Path
import json
import os

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

class PredefinedCurves:
    class TextBookCurve(SpaceFillingCurve):
        def __init__(self):
            # path = self.__class__.__name__
            def operation(path_list):
                new_path_list = []
                a, b = path_list[0]["point"][0], path_list[0]["point"][1]
                inc = abs(b[0] - a[0]) 
                move_pattern = {
                    "u": {"add": [np.array([0, inc]), np.array([inc, 0]), np.array([inc/2, inc/2])],
                        "directions": ["r", "u", "u", "l"]},
                    "r": {"add": [np.array([inc, 0]), np.array([0, inc]), np.array([inc/2, inc/2])],
                        "directions": ["u", "r", "r", "d"]},
                    "d": {"add": [np.array([0, -inc]), np.array([-inc, 0]), np.array([-inc/2, -inc/2])],
                        "directions": ["l", "d", "d", "r"]},
                    "l": {"add": [np.array([-inc, 0]), np.array([0, -inc]), np.array([-inc/2, -inc/2])],
                        "directions": ["d", "l", "l", "u"]},
                }
                for path in path_list:
                    pattern = move_pattern[path["direction"]]
                    p1, p5, p9 = path["point"]
                    p2 = p1 + pattern["add"][2]
                    p3 = p1 + pattern["add"][0]
                    p4 = p2 + pattern["add"][0]
                    p6 = p4 + pattern["add"][1]
                    p7 = p5 + pattern["add"][1]
                    p8 = p6 - pattern["add"][0]
                    end_points = [p1, p2, p3, p4, p5, p6, p7, p8, p9]
                    directions = pattern["directions"]
                    for i in range(4):
                        new_path_list.append({"point": [end_points[2 * i], end_points[2 * i + 1], end_points[2 * i + 2]], "direction": directions[i]})
                return new_path_list
            
            super().__init__(operation = operation, starting_seeds = [{"point": [np.array([-2, -2]), np.array([0, 0]), np.array([2, -2])], "direction": "u"}])
            for index in range(1, 9):
                self._final_path_dict[index + 1] = self.operation(self._final_path_dict[index])
                self.points_dict[index + 1] = SpaceFillingCurve.from_path_to_points(self._final_path_dict[index + 1])

        @property
        def final_path_dict(self):
            return self._final_path_dict
        
        def export_points_as_text(self):
            """
            Xuất points_dict ra file text, các điểm chuyển định dạng
            từ nd.array thành iterable.
            """
            path = Path(__file__).parent / f"ConstantCurves/{self.__class__.__name__}/Curves1-5.json"
            new_points_dict = {k:[point.tolist() for point in self.points_dict[k]] for k in range(1, 6)}
            with open(path, "w") as f:
                json.dump(new_points_dict, f, indent=2)
            for index in [6, 7, 8, 9]:
                path = Path(__file__).parent / f"ConstantCurves/{self.__class__.__name__}/Curve{index}.json"
                data = [point.tolist() for point in self.points_dict[index]]
                with open(path, "w") as f:
                    json.dump(data, f)

        def gen_next_point_list(self):
            """
            Tạo danh sách điểm tiếp theo của points_dict, lưu trực tiếp ra file text.
            """
            path = Path(__file__).parent / f"ConstantCurves/{self.__class__.__name__}"
            target_length = len(os.listdir(path)) + 4 + 1
            new_path = path / f"Curve{target_length}.json"
            current_length = len(self._final_path_dict)
            if current_length >= target_length:
                points = [point.tolist() for point in self.points_dict[target_length]]
                with open(new_path, "w") as f:
                    json.dump(points, f)
            else:
                times_to_append = target_length - current_length
                for index in range(times_to_append):
                    self._final_path_dict[current_length + index + 1] = self.operation(self._final_path_dict[current_length + index])
                points = [point.tolist() for point in SpaceFillingCurve.from_path_to_points(self._final_path_dict[target_length])]
                with open(new_path, "w") as f:
                    json.dump(points, f)
        
    # class GeneralCurveSquareVersion(SpaceFillingCurve):
    #     def __init__(self):
    #         def operation(path_list):
    #             new_path_list = []
    #             a, b = path_list[0]["point"]
    #             inc = abs(sum(b - a)) / 2
    #             move_pattern = {
    #                 "u": {"add": [np.array([0, inc]), np.array([inc, 0])],
    #                     "directions": ["r", "u", "u", "l"]},
    #                 "r": {"add": [np.array([inc, 0]), np.array([0, inc])],
    #                     "directions": ["u", "r", "r", "d"]},
    #                 "d": {"add": [np.array([0, -inc]), np.array([-inc, 0])],
    #                     "directions": ["l", "d", "d", "r"]},
    #                 "l": {"add": [np.array([-inc, 0]), np.array([0, -inc])],
    #                     "directions": ["d", "l", "l", "u"]},
    #             }
    #             for path in path_list:
    #                 pattern = move_pattern[path["direction"]]
    #                 p1, p5 = path["point"]
    #                 p2 = p1 + pattern["add"][0]
    #                 p3 = p2 + pattern["add"][1]
    #                 p4 = p3 + pattern["add"][1]
    #                 end_points = [p1, p2, p3, p4, p5]
    #                 directions = pattern["directions"]
    #                 for i in range(4):
    #                     new_path_list.append({"point": [end_points[i], end_points[i + 1]], "direction": directions[i]})
    #             return new_path_list
            
    #         super().__init__(operation = operation, starting_seeds = [{"point": [np.array([0, 0]), np.array([1, 0])], "direction": "u"}])
    #         for _ in range(5):
    #             self._final_path_list.append(self.operation(self._final_path_list[-1]))
    #             self.points_list.append(SpaceFillingCurve.from_path_to_points(self._final_path_list[-1]))
    #             self.parametric_curve.append(Grapher.ParametricCurve.line_through_points(self.points_list[-1]))

curve = PredefinedCurves.TextBookCurve()
curve.export_points_as_text()