from manim import *
from ConstantCurves import TextBookCurve
from Grapher import Grapher

config.disable_caching = True

curve = TextBookCurve()
param_list = []
for i in range(1, 6):
    param_list.append(Grapher.ParametricCurve.to3D(curve.get_curve_normal(i).function))

class Draw(Scene):
    def construct(self):
        # curve_list = []
        # for index in range(5):
        #     curve_drawer = ParametricFunction(
        #         function=param_list[index],
        #         t_range=[0, 1, 0.001],
        #         stroke_width=1.5
        #     )
        #     curve_drawer = CurvesAsSubmobjects(curve_drawer)
        #     curve_drawer.set_color_by_gradient(RED, GREEN, BLUE)
        #     curve_list.append(curve_drawer)

        # Curves 6, 7
        # for index in range(6, 8):
        #     parameter = Grapher.ParametricCurve.to3D(curve.get_curve_point_wise(index))
        #     const = curve.const(index)
        #     curve_drawer = ParametricFunction(
        #         function=parameter,
        #         t_range=[0, const, 1],
        #         stroke_width=1.5,
        #         use_smoothing=False
        #     )
        #     curve_drawer = CurvesAsSubmobjects(curve_drawer)
        #     curve_drawer.set_color_by_gradient(RED, GREEN, BLUE)
        #     curve_list.append(curve_drawer)

        # Curve 8
        parameter8 = Grapher.ParametricCurve.to3D(curve.get_curve_point_wise(8))
        const8 = curve.const(8)
        curve_drawer8 = ParametricFunction(
                function=parameter8,
                t_range=[0, const8, 1],
                stroke_width=1.7,
                use_smoothing=False
            )
        curve_drawer8 = CurvesAsSubmobjects(curve_drawer8)
        curve_drawer8.set_color_by_gradient(RED, GREEN, BLUE)
        # curve_list.append(curve_drawer8)

        # Curve 9
        parameter9 = Grapher.ParametricCurve.to3D(curve.get_curve_point_wise(9))
        const9 = curve.const(9)
        curve_drawer9 = ParametricFunction(
                function=parameter9,
                t_range=[0, const9, 1],
                stroke_width=2,
                # use_smoothing=False
            )
        curve_drawer9 = CurvesAsSubmobjects(curve_drawer9)
        curve_drawer9.set_color_by_gradient(RED, GREEN, BLUE)

        # Draw
        self.add(curve_drawer8)
        self.wait(1)
        # self.play(ReplacementTransform(curve_drawer8, curve_drawer9))
        self.play(FadeIn(curve_drawer9))
        self.wait(1)
        # Draw transfromation
        # self.add(curve_list[0])
        # for index in range(7):
        #     self.play(ReplacementTransform(curve_list[index], curve_list[index + 1]))
        #     self.wait(1)
        
# class PredefinedCurves:
#     class TextBookCurve(SpaceFillingCurve):
#         def __init__(self):
#             def operation(path_list):
#                 new_path_list = []
#                 a, b = path_list[0]["point"][0], path_list[0]["point"][1]
#                 inc = abs(b[0] - a[0]) 
#                 move_pattern = {
#                     "u": {"add": [np.array([0, inc]), np.array([inc, 0]), np.array([inc/2, inc/2])],
#                         "directions": ["r", "u", "u", "l"]},
#                     "r": {"add": [np.array([inc, 0]), np.array([0, inc]), np.array([inc/2, inc/2])],
#                         "directions": ["u", "r", "r", "d"]},
#                     "d": {"add": [np.array([0, -inc]), np.array([-inc, 0]), np.array([-inc/2, -inc/2])],
#                         "directions": ["l", "d", "d", "r"]},
#                     "l": {"add": [np.array([-inc, 0]), np.array([0, -inc]), np.array([-inc/2, -inc/2])],
#                         "directions": ["d", "l", "l", "u"]},
#                 }
#                 for path in path_list:
#                     pattern = move_pattern[path["direction"]]
#                     p1, p5, p9 = path["point"]
#                     p2 = p1 + pattern["add"][2]
#                     p3 = p1 + pattern["add"][0]
#                     p4 = p2 + pattern["add"][0]
#                     p6 = p4 + pattern["add"][1]
#                     p7 = p5 + pattern["add"][1]
#                     p8 = p6 - pattern["add"][0]
#                     end_points = [p1, p2, p3, p4, p5, p6, p7, p8, p9]
#                     directions = pattern["directions"]
#                     for i in range(4):
#                         new_path_list.append({"point": [end_points[2 * i], end_points[2 * i + 1], end_points[2 * i + 2]], "direction": directions[i]})
#                 return new_path_list
            
#             super().__init__(operation = operation, starting_seeds = [{"point": [np.array([0, 0]), np.array([2, 2]), np.array([4, 0])], "direction": "u"}])
#             for _ in range(8):
#                 self._final_path_list.append(self.operation(self._final_path_list[-1]))
#                 self.points_list.append(SpaceFillingCurve.from_path_to_points(self._final_path_list[-1]))
#                 # self.parametric_curve.append(Grapher.ParametricCurve.line_through_points(self.points_list[-1]))

#         @property
#         def final_path_list(self):
#             return self._final_path_list

# curves = PredefinedCurves.TextBookCurve()

# def curve6_funct(t):
#     point_list = curves.points_list[6]
#     const = 0.0001220703125
#     index = int(t/const)
#     return np.append(point_list[index], 0)

# def curve7_funct(t):
#     point_list = curves.points_list[7]
#     const = 0.000030517578125
#     index = int(t/const)
#     return np.append(point_list[index], 0)

# def curve8_funct(t):
#     point_list = curves.points_list[8]
#     const = 7.62939453125e-6
#     index = int(t/const)
#     return np.append(point_list[index], 0)

# class Curve(Scene):
#     def construct(self):
#         curve6 = ParametricFunction(function = curve6_funct, 
#                                     t_range = [0, 1, 0.0001220703125],
#                                     stroke_width = 1.5)
#         curve6 = CurvesAsSubmobjects(curve6)
#         # curve6.set_color_by_gradient(RED, GREEN, BLUE)

#         curve7 = ParametricFunction(function = curve7_funct, 
#                                     t_range = [0, 1, 0.000030517578125],
#                                     stroke_width = 1.5)
#         curve7 = CurvesAsSubmobjects(curve7)
#         # curve7.set_color_by_gradient(RED, GREEN, BLUE)

#         # curve8 = ParametricFunction(function = curve8_funct, 
#         #                             t_range = [0, 1, 7.62939453125e-6],
#         #                             stroke_width = 1.5)
#         # curve8 = CurvesAsSubmobjects(curve8)
#         # curve8.set_color_by_gradient(RED, GREEN, BLUE)
#         self.add(curve6)
#         self.play(ReplacementTransform(curve6, curve7))
#         self.wait(1)
#         # self.play(ReplacementTransform(curve7, curve8))
#         # self.wait(1)sadasd