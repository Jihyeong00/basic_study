package lambdaTest;

public class PrintNameTest {
	public static void printFullName(PrintName printName) {
		System.out.println(printName.getName("이", "지형"));
	}

	public static void main(String[] args) {
		printFullName((l, f) -> l + f);
	}
}
