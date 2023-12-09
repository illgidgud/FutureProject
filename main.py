import numpy as np
from Grapher import Grapher, SpaceFillingCurve

class PredefinedCurves:
    class TextBookCurve(SpaceFillingCurve):
        def __init__(self):
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
            
            super().__init__(operation = operation, starting_seeds = [{"point": [np.array([0, 0]), np.array([0.5, 0.5]), np.array([1, 0])], "direction": "u"}])
            for _ in range(5):
                self._final_path_list.append(self.operation(self._final_path_list[-1]))
                self.points_list.append(SpaceFillingCurve.from_path_to_points(self._final_path_list[-1]))
                self.parametric_curve.append(Grapher.ParametricCurve.line_through_points(self.points_list[-1]))

        @property
        def final_path_list(self):
            return self._final_path_list
        
    class GeneralCurveSquareVersion(SpaceFillingCurve):
        def __init__(self):
            def operation(path_list):
                new_path_list = []
                a, b = path_list[0]["point"]
                inc = abs(sum(b - a)) / 2
                move_pattern = {
                    "u": {"add": [np.array([0, inc]), np.array([inc, 0])],
                        "directions": ["r", "u", "u", "l"]},
                    "r": {"add": [np.array([inc, 0]), np.array([0, inc])],
                        "directions": ["u", "r", "r", "d"]},
                    "d": {"add": [np.array([0, -inc]), np.array([-inc, 0])],
                        "directions": ["l", "d", "d", "r"]},
                    "l": {"add": [np.array([-inc, 0]), np.array([0, -inc])],
                        "directions": ["d", "l", "l", "u"]},
                }
                for path in path_list:
                    pattern = move_pattern[path["direction"]]
                    p1, p5 = path["point"]
                    p2 = p1 + pattern["add"][0]
                    p3 = p2 + pattern["add"][1]
                    p4 = p3 + pattern["add"][1]
                    end_points = [p1, p2, p3, p4, p5]
                    directions = pattern["directions"]
                    for i in range(4):
                        new_path_list.append({"point": [end_points[i], end_points[i + 1]], "direction": directions[i]})
                return new_path_list
            
            super().__init__(operation = operation, starting_seeds = [{"point": [np.array([0, 0]), np.array([1, 0])], "direction": "u"}])
            for _ in range(5):
                self._final_path_list.append(self.operation(self._final_path_list[-1]))
                self.points_list.append(SpaceFillingCurve.from_path_to_points(self._final_path_list[-1]))
                self.parametric_curve.append(Grapher.ParametricCurve.line_through_points(self.points_list[-1]))

# curve = PredefinedCurves.TextBookCurve()
# print(curve.final_path_list)
# print(type(curve.points_list[1][0]))
# print(curve.final_path_list[1])
# print(curve.parametric_curve[5].function(1))
# print(curve.points_list[0])

# print(type(funct_writer(10)))
# print(sum(np.array([1, 2])))
# p1 = np.array([0, 0])
# p2 = np.array([1, 1])
# p3 = np.array([2, 0])
# graph1 = Grapher.ParametricCurve.line_through_points([p1, p2, p3])
# graph2 = Grapher.ParametricCurve.line_through_two_points(p1, p2)
# print(graph2.function(0.5))
# print(graph1.domain)
# graph1 = Grapher.ParametricCurve(lambda t: np.array([t, t + 1]), domain = (0, 1))
# graph2 = Grapher.ParametricCurve(lambda t: np.array([t, t + 1]), domain = (1, 2))
# graph3 = Grapher.ParametricCurve.join_curves([graph1, graph2])
# print(graph3.function(2))