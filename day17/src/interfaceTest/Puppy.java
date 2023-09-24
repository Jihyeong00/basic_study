package interfaceTest;

public class Puppy implements Pet {

	@Override
	public void sitDown() {
		// TODO Auto-generated method stub
		System.out.println("앉는다.");
	}

	@Override
	public void stop() {
		// TODO Auto-generated method stub
		System.out.println("기다린다.");
	}

	@Override
	public void poop() {
		// TODO Auto-generated method stub
		System.out.println("맨날 싸는 곳에 싼다.");
	}

	@Override
	public void bang() {
		// TODO Auto-generated method stub
		System.out.println("눕는다.");
	}
}
