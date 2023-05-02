# ScaleConverter 상속받는 클래스
# 화씨온도(F) = 섭씨온도(C) * 1.8 + 32
# from 패키지이름.모듈이름 import 클래스
import classfication.scale_converter
from classfication.scale_converter import ScaleConverter

class Converter(ScaleConverter):
    def __init__(self, units_from, units_to, factor, offset):
        super().__init__(units_from, units_to, factor)
        self.offset = offset

    def convert(self, value):  # 함수 이름은 같으나 내용을 재정의
        #return self.factor * value + self.offset
        return super().convert(value) + self.offset

if __name__=="__main__":
    conv = Converter('C', 'F', 1.8, 32)
    print("converting 21C")
    print(f'{conv.convert(21):.2f}{conv.units_to}') # :.2f 소수 2자리까지 표시


"""
con = ScaleConverter("KB", "B", 1024)
print("Converting 1 KB")
print(str(con.convert(1)) + con.units_to)
"""


