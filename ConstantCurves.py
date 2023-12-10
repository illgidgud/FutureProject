from Grapher import Grapher
from pathlib import Path
import json
import os

class ConstantCurves:
    def __init__(self, name):
        self.path = Path(__file__).parent / f"ConstantCurves/{name}"
        self.length = len(os.listdir(self.path)) + 4

    def get_curve_normal(self, n, domain: tuple = (0, 1)):
        """
        Trả về phương trình tham số cho đường cong thứ n. 
        Miền xác định mặc định là đoạn [0, 1]
        """
        assert n >= 1, "Đường cong phải có thứ tự nguyên dương."
        if self.length < n: 
            raise ValueError(f"Chưa có đường cong thứ {n}")
        else:
            if 1 <= n <= 5:
                path = self.path / "Curves1-5.json"
                with open(path, "r") as f:
                    points = json.load(f)
                return Grapher.ParametricCurve.line_through_points(points[str(n)])
            else:
                path = self.path / f"Curve{n}.json"
                with open(path, "r") as f:
                    points = json.load(f)
                return Grapher.ParametricCurve.line_through_points(points)

    def get_curve_point_wise(self, n):
        """
        Trả về hàm nhận các giá trị rời rạc, cho tương ứng số nguyên
        không âm t với phần tử có chỉ số t trong list đường cong thứ n, 
        trong đó 0 <= t <= len(đường cong thứ n).
        """
        assert n >= 1, "Đường cong phải có thứ tự nguyên dương."
        if self.length < n: 
            raise ValueError(f"Chưa có đường cong thứ {n}")
        else:
            if 1 <= n <= 5:
                path = self.path / "Curves1-5.json"
                with open(path, "r") as f:
                    points = json.load(f)[str(n)]
            else:
                path = self.path / f"Curve{n}.json"
                with open(path, "r") as f:
                    points = json.load(f)
        def funct(t):
            return points[int(t)]
        return funct
    
class TextBookCurve(ConstantCurves):
    def __init__(self):
        super().__init__("TextBookCurve")

    def const(self, n):
        """
        Số đoạn thẳng trong đường cong thứ n. Khi đó, số điểm là
        số đoạn cộng 1.
        """
        assert 1 <= n <= self.length, "Giá trị không hợp lệ."
        return 2 * 4 ** (n - 1)