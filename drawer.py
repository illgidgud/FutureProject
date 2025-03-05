# This is where I do all the "drawings", so things are a bit disorganized. Feel free to make use of the resources here!

from manim import *
import json
import sys
# If importing doesn't work, add manually add search path into python's path (refer online to 'pathlib' package)
from ConstantCurves import TextBookCurve
from ConstantCurves import TriangleCurveOne
from ConstantCurves import TriangleCurveTwo
from ConstantCurves import TriangleCurveForPentagon
from ConstantCurves import CircleCurve
from Grapher import Grapher

# config.disable_caching = True

class DrawTriangle(Scene):
    def construct(self):
        triangle_curve = TriangleCurveTwo()
        curve_list = []
        # Curves 1-3
        # param_list = []
        # for i in range(1, 4):
        #     param_list.append(Grapher.ParametricCurve.to3D(triangle_curve.get_curve_normal(i).function))
        # for index in range(3):
        #     curve_drawer = ParametricFunction(
        #         function=param_list[index],
        #         t_range=[0, 1, 0.001],
        #         stroke_width=1.5,
        #         use_smoothing=False
        #     )
        #     curve_drawer = CurvesAsSubmobjects(curve_drawer)
        #     curve_drawer.set_color_by_gradient(GREEN, BLUE, PURPLE)
        #     curve_list.append(curve_drawer)

        # Curve 4
        # curve_drawer = ParametricFunction(
        #         function=Grapher.ParametricCurve.to3D(triangle_curve.get_curve_normal(4).function),
        #         t_range=[0, 1, 0.0001],
        #         stroke_width=1.5,
        #         use_smoothing=False
        #     )
        # curve_drawer = CurvesAsSubmobjects(curve_drawer)
        # curve_drawer.set_color_by_gradient(GREEN, BLUE, PURPLE)
        # curve_list.append(curve_drawer)

        # Curve 5
        # curve_drawer = ParametricFunction(
        #         function=Grapher.ParametricCurve.to3D(triangle_curve.get_curve_normal(5).function),
        #         t_range=[0, 1, 0.0001],
        #         stroke_width=1.5,
        #         use_smoothing=False
        #     )
        # curve_drawer = CurvesAsSubmobjects(curve_drawer)
        # curve_drawer.set_color_by_gradient(GREEN, BLUE, PURPLE)
        # curve_list.append(curve_drawer)

        # Curves 6
        # parameter = Grapher.ParametricCurve.to3D(triangle_curve.get_curve_point_wise(6))
        # const = triangle_curve.const(6)
        # curve_drawer = ParametricFunction(
        #     function=parameter,
        #     t_range=[0, const, 1],
        #     stroke_width=1.5,
        #     use_smoothing=False
        # )
        # curve_drawer = CurvesAsSubmobjects(curve_drawer)
        # curve_drawer.set_color_by_gradient(GREEN, BLUE, PURPLE)
        # curve_list.append(curve_drawer)

        # Curve 7
        parameter = Grapher.ParametricCurve.to3D(triangle_curve.get_curve_point_wise(7))
        const = triangle_curve.const(7)
        curve_drawer = ParametricFunction(
            function=parameter,
            t_range=[0, const, 1],
            stroke_width=1.5,
            use_smoothing=False
        )
        curve_drawer = CurvesAsSubmobjects(curve_drawer)
        curve_drawer.set_color_by_gradient(GREEN, BLUE, PURPLE)
        curve_list.append(curve_drawer)

        # Curve 8
        parameter = Grapher.ParametricCurve.to3D(triangle_curve.get_curve_point_wise(8))
        const = triangle_curve.const(8)
        curve_drawer = ParametricFunction(
            function=parameter,
            t_range=[0, const, 1],
            stroke_width=3.0,
            use_smoothing=False
        )
        curve_drawer = CurvesAsSubmobjects(curve_drawer)
        curve_drawer.set_color_by_gradient(GREEN, BLUE, PURPLE)
        curve_list.append(curve_drawer)

        # Draw transfromation
        self.add(curve_list[0])
        self.wait(1)
        self.play(FadeIn(curve_list[1]))
        self.wait(1)
        # for index in range(6):
        #     self.play(ReplacementTransform(curve_list[index], curve_list[index + 1]))
        #     self.wait(1)

class DrawSquare(Scene):
    def construct(self):
        curve = TextBookCurve()
        param_list = []
        for i in range(1, 6):
            param_list.append(Grapher.ParametricCurve.to3D(curve.get_curve_normal(i).function))
        curve_list = []
        for index in range(5):
            curve_drawer = ParametricFunction(
                function=param_list[index],
                t_range=[0, 1, 0.001],
                stroke_width=1.5
            )
            curve_drawer = CurvesAsSubmobjects(curve_drawer)
            curve_drawer.set_color_by_gradient(RED, GREEN, BLUE)
            curve_list.append(curve_drawer)

        # Curves 6, 7
        for index in range(6, 8):
            parameter = Grapher.ParametricCurve.to3D(curve.get_curve_point_wise(index))
            const = curve.const(index)
            curve_drawer = ParametricFunction(
                function=parameter,
                t_range=[0, const, 1],
                stroke_width=1.5,
                use_smoothing=False
            )
            curve_drawer = CurvesAsSubmobjects(curve_drawer)
            curve_drawer.set_color_by_gradient(RED, GREEN, BLUE)
            curve_list.append(curve_drawer)

        # Curve 8
        # parameter8 = Grapher.ParametricCurve.to3D(curve.get_curve_point_wise(8))
        # const8 = curve.const(8)
        # curve_drawer8 = ParametricFunction(
        #         function=parameter8,
        #         t_range=[0, const8, 1],
        #         stroke_width=1.7,
        #         use_smoothing=False
        #     )
        # curve_drawer8 = CurvesAsSubmobjects(curve_drawer8)
        # curve_drawer8.set_color_by_gradient(RED, GREEN, BLUE)
        # curve_list.append(curve_drawer8)

        # Curve 9
        # parameter9 = Grapher.ParametricCurve.to3D(curve.get_curve_point_wise(9))
        # const9 = curve.const(9)
        # curve_drawer9 = ParametricFunction(
        #         function=parameter9,
        #         t_range=[0, const9, 1],
        #         stroke_width=3.5,
        #         use_smoothing=False
        #     )
        # curve_drawer9 = CurvesAsSubmobjects(curve_drawer9)
        # curve_drawer9.set_color_by_gradient(RED, GREEN, BLUE)

        # Draw transition 8, 9
        # self.add(curve_drawer8)
        # self.wait(1)
        # self.play(FadeIn(curve_drawer9))
        # self.wait(1)

        # Draw transfromation
        self.add(curve_list[0])
        self.wait(1)
        for index in range(2):
            self.play(ReplacementTransform(curve_list[index], curve_list[index + 1]))
            self.wait(1)

class IntroducePentagon(Scene):
    def construct(self):
        isosceles = Polygon(
            [0, 0, 0],
            [2*-5.87785252e-01, 2*-8.09016994e-01,  0.00000000e+00,],
            [2*5.87785252e-01, 2*-8.09016994e-01,  0.00000000e+00,],
            stroke_width=1.0,
            fill_opacity=1.0,
            color=BLUE_C,
        )
        copy = isosceles.copy()
        self.add(copy)
        self.wait(1)
        for i in range(4):
            self.play(
                isosceles.animate.rotate(
                    angle=2*PI/5, 
                    about_point=ORIGIN,
                ),
                run_time=0.8,
            )
            copy = isosceles.copy()
            self.add(copy)
        self.wait(1)

def N_folds(obj: Mobject, n):
    """
    Tao ra n-1 ban sao de lap thanh mot n-giac deu
    """
    obj_list = [obj]
    for i in range(n - 1):
        new_obj = obj.copy().rotate_about_origin(angle=2*(i + 1)*PI/n)
        obj_list.append(new_obj)
    return Group(*obj_list)

class GroupMobject(Scene):
    def construct(self):
        isosceles = Polygon(
            [0, 0, 0],
            [2*-5.87785252e-01, 2*-8.09016994e-01,  0.00000000e+00,],
            [2*5.87785252e-01, 2*-8.09016994e-01,  0.00000000e+00,],
            stroke_width=1.0,
            fill_opacity=1.0,
            color=BLUE_C,
        )
        grp_obj = N_folds(isosceles, 5)
        self.add(grp_obj)
        # obj_list = [isosceles]
        # self.play(Create(isosceles))
        # isosceles.rotate(
        #     angle=2*PI/5,
        #     about_point=ORIGIN,
        # )
        # self.add(isosceles)
        # self.wait(1)
        # for i in range(4):
        #     obj = isosceles.copy().rotate_about_origin(2*PI*(i + 1)/5)
        #     obj_list.append(obj)
        # grouped_mobject = Group(*obj_list)

class DrawPentagon(Scene):
    def construct(self):
        triangle_curve = TriangleCurveForPentagon()
        curve_list = []

        # Curve 0
        line = Line(
            [2*-5.87785252e-01, 2*-8.09016994e-01,  0.00000000e+00],
            [2*5.87785252e-01, 2*-8.09016994e-01,  0.00000000e+00],
            stroke_width=1.0,
            fill_opacity=1.0,
            color=BLUE_C,
        )
        curve_list.append(N_folds(line, 5))
        
        # Curves 1-3
        param_list = []
        for i in range(1, 4):
            param_list.append(Grapher.ParametricCurve.to3D(triangle_curve.get_curve_normal(i).function))
        for index in range(3):
            curve_drawer = ParametricFunction(
                function=param_list[index],
                t_range=[0, 1, 0.001],
                stroke_width=1.5,
                use_smoothing=False
            )
            curve_drawer = CurvesAsSubmobjects(curve_drawer)
            curve_drawer.set_color_by_gradient(GREEN, BLUE, PURPLE)
            curve_list.append(N_folds(curve_drawer, 5))

        # Curves 4-7
        for index in [4, 5, 6, 7]:
            parameter = Grapher.ParametricCurve.to3D(triangle_curve.get_curve_point_wise(index))
            const = triangle_curve.const(index)
            curve_drawer = ParametricFunction(
                function=parameter,
                t_range=[0, const, 1],
                stroke_width=1.5,
                use_smoothing=False
            )
            curve_drawer = CurvesAsSubmobjects(curve_drawer)
            curve_drawer.set_color_by_gradient(GREEN, BLUE, PURPLE)
            curve_list.append(N_folds(curve_drawer, 5))

        # Curve 8
        # parameter = Grapher.ParametricCurve.to3D(triangle_curve.get_curve_point_wise(8))
        # const = triangle_curve.const(8)
        # curve_drawer = ParametricFunction(
        #     function=parameter,
        #     t_range=[0, const, 1],
        #     stroke_width=3.0,
        #     use_smoothing=False
        # )
        # curve_drawer = CurvesAsSubmobjects(curve_drawer)
        # curve_drawer.set_color_by_gradient(GREEN, BLUE, PURPLE)
        # curve_list.append(N_folds(curve_drawer, 5))

        # Draw transfromation
        self.add(curve_list[0])
        # self.wait(1)
        # self.play(FadeIn(curve_list[1]))
        # self.wait(1)
        for index in range(7):
            self.play(ReplacementTransform(curve_list[index], curve_list[index + 1]))
            self.wait(1)

class DrawCircle(Scene):
    def construct(self):
        circle_curve = CircleCurve()
        curve_list = []

        # Curve 0
        line = Line(
            [-2, 0, 0], [2, 0, 0],
            stroke_width=1.0,
            fill_opacity=1.0,
            color = RED,    
        )
        curve_list.append(line)

        # Curves 1-3
        param_list = []
        for i in range(1, 4):
            param_list.append(Grapher.ParametricCurve.to3D(circle_curve.get_curve_normal(i).function))
        for index in range(3):
            curve_drawer = ParametricFunction(
                function=param_list[index],
                t_range=[0, 1, 0.001],
                stroke_width=1.5,
                use_smoothing=False
            )
            curve_drawer = CurvesAsSubmobjects(curve_drawer)
            curve_drawer.set_color_by_gradient(RED, ORANGE, YELLOW)
            if index == 2:
                curve_list.append(curve_drawer)
                curve_list.append(N_folds(curve_drawer, 5))
            else: curve_list.append(curve_drawer)

        # Draw transfromation
        self.add(curve_list[0])
        # self.wait(1)
        # self.play(FadeIn(curve_list[1]))
        # self.wait(1)
        for index in range(3):
            if index == 2:
                self.play(
                    ReplacementTransform(curve_list[index], curve_list[index + 1]),
                    FadeIn(curve_list[4])
                )
            else:
                self.play(ReplacementTransform(curve_list[index], curve_list[index + 1]))
            self.wait(1)

# Pentagon points - 3rd list
"""
[2*-5.87785252e-01, 2*-8.09016994e-01,  0]
[2*5.87785252e-01, 2*-8.09016994e-01,  0]
"""

# Octagon points - 4th list
"""
[-0.76536686, -1.84775907,  0]
[ 0.76536686, -1.84775907,  0]
"""

# 12-gon points - 5th list
"""
[-0.51763809, -1.93185165,  0]
[ 0.51763809, -1.93185165,  0]
"""

# 20-gon points - 6th list
"""
[-0.31286893, -1.97537668,  0]
[ 0.31286893, -1.97537668,  0]
"""

# 32-gon points - 7th list
"""
[-0.19603428, -1.99036945,  0]
[ 0.19603428, -1.99036945,  0]
"""

class DrawCharactersIntro(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()
        # I the stick.
        eye_ball = Circle(radius=0.5, color=WHITE, fill_opacity=1).shift([0, 1, 0])
        eye_balls = Group(eye_ball, eye_ball.copy().shift([-1, 0, 0])).scale(0.2)

        pupil = Circle(0.15, color=BLACK, fill_opacity=1).shift([0, 1, 0])
        pupils = Group(pupil, pupil.copy().shift([-1, 0, 0])).scale(0.2)

        body = Line([-0.5, -1.5, 0], [-0.5, 1.5, 0], stroke_width=3, color=BLUE)

        # Big square
        square_eye_ball = Circle(radius=0.25, color=WHITE, fill_opacity=1)
        square_pupil = Circle(0.1, color=BLACK, fill_opacity=1).shift([-0.1, 0, 0])
        square_eye = Group(square_eye_ball, square_pupil).scale(0.8)
        square_eyes = Group(square_eye.copy().shift([0.5, 0.8, 0]), square_eye.copy().shift([-0.5, 0.8, 0]))
        square = Square(3, color=RED, stroke_width=0, fill_opacity=1)
        big_square = Group(square, square_eyes).shift([9, 0, 0])

        self.play(FadeIn(body, eye_balls, pupils))
        self.play(
            pupils.animate.shift([0.07, 0, 0]),
            rate_func=rate_functions.ease_in_out_back,
            run_time=0.5,
        )
        self.wait(0.5)
        self.add(big_square)
        self.play(self.camera.frame.animate.shift([4.5, 0, 0]))
        self.wait(0.5)

        self.play(self.camera.frame.animate.shift([-4.5, 0, 0]))
        self.play(
            pupils.animate.shift([-0.07, 0, 0]),
            rate_func=rate_functions.ease_in_out_back,
            run_time=0.5,
        )
        self.wait(0.5)

class ICoilingAndJumping(Scene):
    def construct(self):
        # I the stick.
        eye_ball = Circle(radius=0.5, color=WHITE, fill_opacity=1).shift([0, 1, 0])
        eye_balls = Group(eye_ball, eye_ball.copy().shift([-1, 0, 0])).scale(0.2)

        pupil = Circle(0.15, color=BLACK, fill_opacity=1).shift([0, 1, 0])
        pupils = Group(pupil, pupil.copy().shift([-1, 0, 0])).scale(0.2)

        body = Line([-0.5, -1.5, 0], [-0.5, 1.5, 0], stroke_width=3, color=BLUE)

        ax = Axes()
        sine_body = ax.plot(
            lambda x: 0.3*np.sin(8*x/3), x_range=[-1.5, 1.2],
            color=BLUE,
        ).rotate_about_origin(PI/2).shift([-0.5, 0, 0])

        copy_body = body.copy()
        self.play(FadeIn(copy_body, eye_balls, pupils))
        self.play(
            Transform(copy_body, sine_body),
            rate_func=rate_functions.ease_in_out_elastic,
            run_time=1.5
        )

        self.play(
            Transform(copy_body, body.move_to([5, 6, 0])),
            pupils.animate.move_to([5, 7.5, 0]),
            eye_balls.animate.move_to([5, 7.5, 0]),
            rate_func=rate_functions.ease_in_expo,
            run_time=0.5,
        )
        self.wait(0.5)

class IFillingSquare(Scene):
    def construct(self):
        path = 'C:\\Users\\Admin\\HieuProject\\FutureProject\\ConstantCurves\\ICurve\\data.json'
        with open(path, "r") as f:
            points = json.load(f)

        square = Square(4, color=RED, fill_opacity=1, stroke_width=0)
        
        eye_ball = Circle(radius=0.5, color=WHITE, fill_opacity=1).shift([0, 1, 0])
        eye_balls = Group(eye_ball, eye_ball.copy().shift([-1, 0, 0])).scale(0.2)

        pupil = Circle(0.15, color=BLACK, fill_opacity=1).shift([0, 1, 0])
        pupils = Group(pupil, pupil.copy().shift([-1, 0, 0])).scale(0.2)

        curve_function = Grapher.ParametricCurve.line_through_points(points)
        curve_function = Grapher.ParametricCurve.to3D(curve_function.function)

        mobject_curve = ParametricFunction(
            function=curve_function,
            t_range=[0, 1, 0.001],
            stroke_width=1.5,
        )

        eyes = Group(eye_balls, pupils)

        self.add(square)
        trace = TracedPath(eyes.get_center, stroke_width=2, stroke_color=BLUE)
        self.add(trace)
       
        self.play(
            MoveAlongPath(eyes, mobject_curve),
            rate_func=linear,
            run_time=30,
        )
        self.wait(1)

class DrawIntro(Scene):
    def construct(self):
        ax = Axes()
        sine = ax.plot(
            lambda x: 0.3*np.sin(3*x/2), x_range=[-2, 2],
            color=BLUE,
        ).rotate_about_origin(PI/3).shift(3 * LEFT)

        square = Square(side_length=4, fill_opacity=1, color=BLUE).shift(3 * RIGHT)

        self.play(FadeIn(sine, square))
        self.play(Wiggle(sine))
        self.wait(0.8)
        self.play(Indicate(square, 1.2, color=BLUE))

class Illustration(MovingCameraScene):
    def construct(self):
        square = Square(4, stroke_width=1.5)
        line1 = Line([0, -2, 0], [0, 2, 0], stroke_width=1.5)
        line2 = Line([-2, 0, 0], [2, 0, 0], stroke_width=1.5)
        dots1 = Group(Dot([-2, -2, 0], color=GREEN), Dot([2, -2, 0], color=GREEN)).shift(4 * LEFT)
        dots2 = dots1.copy().shift(8 * RIGHT)
        arrow = Arrow().scale(0.8)
        curve = TextBookCurve()
        param_list = []
        for i in range(1, 3):
            param_list.append(Grapher.ParametricCurve.to3D(curve.get_curve_normal(i).function))
        curve_list = []
        for index in range(2):
            curve_drawer = ParametricFunction(
                function=param_list[index],
                t_range=[0, 1, 0.001],
                stroke_width=1.5
            )
            curve_list.append(curve_drawer)
        mini_curve1 = curve_list[0].copy().scale(0.5).rotate_about_origin(3*PI/2).shift([-0.5, -1, 0] + 4 * RIGHT)
        mini_curve2 = curve_list[0].copy().scale(0.5).rotate_about_origin(PI/2).shift([0.5, -1, 0] + 4 * RIGHT)

        # First scene
        self.play(FadeIn(square))
        self.play(Create(curve_list[0]), rate_func=rate_functions.lingering)
        self.play(FadeOut(square))
        self.play(
            curve_list[0].animate.shift([4 * LEFT]),
            FadeIn(arrow)
        )
        grp = Group(square, line1, line2)
        self.play(FadeIn(grp.shift(4 * RIGHT)))
        self.play(Create(curve_list[1].shift(4 * RIGHT)), run_time=1.5)
        self.play(FadeOut(grp))
        self.play(FadeIn(dots1, dots2))
        self.play(FadeOut(dots1, dots2))

        
        # Second scene
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.move_to(curve_list[1]).set(width=curve_list[1].width * 1.5))
        self.wait(0.3)
        for _ in range(2):
            self.play(
                ShowPassingFlash(
                    mini_curve1.set_color(RED),
                    time_width=0.8,
                    run_time=2,
                ),
                ShowPassingFlash(
                    mini_curve2.set_color(YELLOW ),
                    time_width=0.8,
                    run_time=2,
                )
            )
        self.play(Restore(self.camera.frame))

        for _ in range(1, 5):
            self.play(
                curve_list[0].animate.rotate(PI/2),
                curve_list[1].animate.rotate(PI/2),
            )
            self.wait(0.8)

        # Third scene
        group0 = Group(curve_list[0], arrow, curve_list[1])
        small_curve = {i: curve_list[0].copy().rotate(about_point=[-4, 0, 0], angle=i*PI/2) for i in [1, 2, 3]}
        big_curve = {i: curve_list[1].copy().rotate(about_point=[4, 0, 0], angle=i*PI/2) for i in [1, 2, 3]}
        arrows = {i: arrow.copy() for i in [1, 2, 3]}
        
        groups = {i: Group(small_curve[i], big_curve[i], arrows[i]) for i in [1, 2, 3]}

        groups[1].shift(20 * RIGHT)
        groups[2].shift(8 * DOWN + 20 * RIGHT)
        groups[3].shift(8 * DOWN)

        group = Group(group0, groups[1], groups[2], groups[3])
        self.add(groups[1], groups[2], groups[3])
        self.play(self.camera.frame.animate.move_to(group.get_center()).set(width=50))
        self.wait(1)

class ClosingScene(MovingCameraScene):
    def construct(self):
        square = Square(4, color=RED, fill_opacity=1, stroke_width=0)
        eye_ball = Circle(radius=0.5, color=WHITE, fill_opacity=1).shift([0, 1, 0])
        eye_balls = Group(eye_ball, eye_ball.copy().shift([-1, 0, 0])).scale(0.2)
        pupil = Circle(0.15, color=BLACK, fill_opacity=1).shift([0, 1, 0])
        pupils = Group(pupil, pupil.copy().shift([-1, 0, 0])).scale(0.2)
        eyes = Group(eye_balls, pupils)

        path = 'C:\\Users\\Admin\\HieuProject\\FutureProject\\ConstantCurves\\ICurve\\data.json'
        with open(path, "r") as f:
            points = json.load(f)

        fixed_curve_function = Grapher.ParametricCurve.line_through_points(points)
        fixed_curve_function = Grapher.ParametricCurve.to3D(fixed_curve_function.function)

        mobject_curve_const = ParametricFunction(
            function=fixed_curve_function,
            t_range=[0, 1, 0.001],
            stroke_width=1.5,
            stroke_color=BLUE
        )
        group = Group(square, mobject_curve_const).shift(15 * RIGHT)

        new_points = np.random.uniform(-2, 2, (200, 2))
        new_points = [point + np.array([15, 0]) for point in new_points]

        curve_function = Grapher.ParametricCurve.line_through_points(new_points)
        curve_function = Grapher.ParametricCurve.to3D(curve_function.function)

        mobject_curve = ParametricFunction(
            function=curve_function,
            t_range=[0, 1, 0.001],
            stroke_width=1.5,
        )

        self.add(group)
        self.play(self.camera.frame.animate.shift(15 * RIGHT), run_time = 0.8)

        trace = TracedPath(eyes.get_center, stroke_width=2, stroke_color=BLUE)
        self.add(trace)
       
        self.play(
            MoveAlongPath(eyes, mobject_curve),
            rate_func=linear,
            run_time=60,
        )
        
class FurtherSuggestionScene(Scene):
    def construct(self):
        a = Polygon(
            [0, -2, 0], [0, 2, 0], [3, 2.5, 0], [3, -1.5, 0],
            fill_opacity=0.7,
            color=BLUE_C, 
            stroke_width=0,  
        )
        b = Polygon(
            [0, -2, 0], [0, 2, 0], [-3, 2.5, 0], [-3, -1.5, 0],
            fill_opacity=1,
            color=BLUE,
            stroke_width=0,  
        )
        c = Polygon(
            [0, 2, 0], [3, 2.5, 0], [0, 3, 0], [-3, 2.5, 0],
            fill_opacity=1,
            color=BLUE,
            stroke_width=0,
        )

        cube2D = Group(a, b, c).scale(0.5).shift(4*RIGHT + 1.5*DOWN)

        circle = Circle(radius=2.8, color=GREEN, fill_opacity=1).scale(0.5).shift(4*LEFT + 0.5*DOWN)

        self.play(Create(circle))
        self.wait(0.5)
        self.play(FadeIn(cube2D))
        self.wait(0.5)

