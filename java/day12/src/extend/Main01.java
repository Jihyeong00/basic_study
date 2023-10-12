package extend;

public class Main01 {
public static void main(String[] args) {
	FileArticle file = new FileArticle();
	file.setNum(1);
	file.setTitle("첫 번째 자료입니다.");
	file.setFileName("java.ppt");
	System.out.println(file.toString());
}
}
