package bbq;

public class BBQ {

	public String branchName;

	BBQ(String name) {
		this.branchName = name;
	}

	public void register(Form form) {
		String[] menus = form.getMenu();
		System.out.println("===================== " + branchName + "치킨 메뉴 =====================");

		for (int i = 0; i < menus.length; i++) {
			System.out.println(i + 1 + ". " + menus[i]);
		}

		if (form instanceof FormAdaptor) {
			System.out.println("무료 나눔 행사중");
		} else {
			form.sell("황금 올리브 치킨");
		}
	}
}
