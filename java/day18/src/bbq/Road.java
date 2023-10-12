package bbq;

public class Road {
	public static void main(String[] args) {
		BBQ jamsil = new BBQ("잠실점");
		jamsil.register(new Form() {
			@Override
			public void sell(String order) {
				String[] menus = getMenu();
				for (int i = 0; i < menus.length; i++) {
					if (menus[i].equals(order)) {
						System.out.println(menus[i] + "주문 성공");
					}
				}

			}

			@Override
			public String[] getMenu() {
				String[] menus = { "후라이드 치킨", "양념 치킨", "황금 올리브 치킨" };
				return menus;
			}
		});
		
		BBQ gangnam = new BBQ("강남점");
		gangnam.register(new FormAdaptor() {
			@Override
			public String[] getMenu() {
				String[] menus = { "후라이드 치킨", "양념 치킨", "황금 올리브 치킨" };
				return menus;
			}
		});
	}
}
