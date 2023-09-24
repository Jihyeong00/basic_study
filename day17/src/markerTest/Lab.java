package markerTest;

public class Lab {
	public void checkKind(Animal[] animals) {
		for (int i = 0; i < animals.length; i++) {
			if (animals[i] instanceof Carnivore) {
				System.out.println("육식 동물 입니다.");
			} else if (animals[i] instanceof Herbivore) {
				System.out.println("초식 동물 입니다.");
			} else {
				System.out.println("잡식 동물 입니다.");
			}
		}
	}

	public static void main(String[] args) {
		Lab lab = new Lab();
		Animal[] anmial = { new Cow(), new Dog(), new Tiger(), new Bear() };
		lab.checkKind(anmial);
	}
}
