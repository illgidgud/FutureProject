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
            
            super().__init__(operation=operation, starting_seeds=[{"point": [np.array([-2, -2]), np.array([0, 0]), np.array([2, -2])], "direction": "u"}])
            for index in range(1, 9):
                self._final_path_dict[index + 1] = self.operation(self._final_path_dict[index])
                self.points_dict[index + 1] = SpaceFillingCurve.from_path_to_points(self._final_path_dict[index + 1])

        @property
        def final_path_dict(self):
            return self._final_path_dict
        
    class TriangleCurve(SpaceFillingCurve):
        def __init__(self, begin_point: np.array, side_vectors: list):
            increment = [np.round(vector / 2, 7) for vector in side_vectors]
            point2 = np.round(begin_point - increment[2], 7)
            point3 = np.round(point2 - increment[1], 7)
            point4 = np.round(point3 - increment[2], 7)
            point5 = np.round(point4 + increment[1], 7)
            starting_seed = [{
                "point": [begin_point, point2, point3, point4, point5],
                "type": "type1", 
            }]
            def operation(path_list, side_vectors):
                # side_vectors = [AB, BC, CA]; A bottom left; B top
                # Create functions to generate points for four types of paths
                def gen_type1(point1: np.ndarray):
                    """
                             *  *  *
                               *     *
                    start: *  *  *     *
                    """
                    point2 = np.round(point1 - side_vectors[2], 7)
                    point3 = np.round(point2 - side_vectors[1], 7)
                    point4 = np.round(point3 - side_vectors[2], 7)
                    point5 = np.round(point4 + side_vectors[1], 7)
                    return [point1, point2, point3, point4, point5]
                
                def gen_type2(point1: np.ndarray):
                    """
                    *       *
                      *   *   *
                        *       *
                              *
                    start:  *   
                    """
                    point2 = np.round(point1 + side_vectors[0], 7)
                    point3 = np.round(point2 - side_vectors[1], 7)
                    point4 = np.round(point3 - side_vectors[0], 7)
                    point5 = np.round(point4 - side_vectors[1], 7)
                    return [point1, point2, point3, point4, point5]
                
                def gen_type3(point1: np.ndarray):
                    """
                    start:  *
                              *
                         *  *   *
                           *    
                             *  *  *
                    """
                    point2 = np.round(point1 + side_vectors[1], 7)
                    point3 = np.round(point2 + side_vectors[2], 7)
                    point4 = np.round(point3 + side_vectors[1], 7)
                    point5 = np.round(point4 - side_vectors[2], 7)
                    return [point1, point2, point3, point4, point5]
                
                def gen_type4(point1: np.ndarray):
                    """
                    *  *  *     * start:
                        *     *
                      *  *  *   
                    """
                    point2 = np.round(point1 - side_vectors[0], 7)
                    point3 = np.round(point2 + side_vectors[2], 7)
                    point4 = np.round(point3 + side_vectors[0], 7)
                    point5 = np.round(point4 + side_vectors[2], 7)
                    return [point1, point2, point3, point4, point5]
                
                generators = {"type1": gen_type1, "type2": gen_type2, 
                                 "type3": gen_type3, "type4": gen_type4,}
                
                pattern = {
                    "type1": {
                        "type": ["type1", "type2", "type1", "type3"],
                        "point_type": [0, 1, 2, 3]
                        },
                    "type2": {
                        "type": ["type2", "type1", "type2", "type4"],
                        "point_type": [0, 3, 1, 2]
                        },
                    "type3": {
                        "type": ["type3", "type4", "type3", "type1"],
                        "point_type": [0, 1, 2, 3]
                        },
                    "type4": {
                        "type": ["type4", "type3", "type4", "type2"],
                        "point_type": [0, 3, 1, 2]
                        },
                    }
                # browse path_list and implement operation
                new_path_list = []
                for path in path_list:
                    type_list = pattern[path["type"]]["type"]
                    point_list = pattern[path["type"]]["point_type"]
                    for index in range(4):
                        path_type = type_list[index]
                        new_path_list.append(
                            {
                                "point": generators[path_type](path["point"][point_list[index]]),
                                "type": path_type
                            }
                        )
                return new_path_list

            super().__init__(operation, starting_seed)
            for index in range(1, 9):
                increment = [np.round(vector / 2, 7) for vector in increment]
                self._final_path_dict[index + 1] = self.operation(self._final_path_dict[index], increment)
                self.points_dict[index + 1] = SpaceFillingCurve.from_path_to_points(self._final_path_dict[index + 1])

"""
[0, 0, 0],
[2*-5.87785252e-01, 2*-8.09016994e-01,  0.00000000e+00,],
[2*5.87785252e-01, 2*-8.09016994e-01,  0.00000000e+00,]
"""

A = np.array([2*-5.87785252e-01, 2*-8.09016994e-01])
B = np.array([0, 0])
C = np.array([2*5.87785252e-01, 2*-8.09016994e-01])
AB = B - A
BC = C - B
CA = A - C

triangle_curve = PredefinedCurves.TriangleCurve(
    A,
    [AB, BC, CA],
)

triangle_curve.export_points_as_text("TriangleCurveForPentagon")