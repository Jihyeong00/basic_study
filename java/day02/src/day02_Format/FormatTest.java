package day02_Format;

public class FormatTest {
	public static void main(String[] args) {
//		이름, 나이, 몸무게 변수 선언
		String name = "이지형";
		int age = 13;
		double weight = 76.4;
		
		System.out.printf("이름 : %s\n", name);
		System.out.printf("나이 : %3d살\n", age);
		System.out.printf("몸무게 : %.2f\n", weight);
	}
}
