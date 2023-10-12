// 넷플릭스
// 애니메이션, 영화, 드라마 클래스
// 사용자가 선택한 영상이 애니메이션이라면 "자막 지원" 기능을 사용하고
// 영화라면 "4D" 기능을 사용하고
// 드라마라면 "굿즈" 기능을 사용합니다.
class Film extends Video {
    public void print4D() {
        System.out.println("4D");
    }
}

class Drama extends Video {
    public void printGoods() {
        System.out.println("굿즈판매");
    }
}

class Animation extends Video {
    public void printSubtitle() {
        System.out.println("자막지원");
    }
}

class Video {
}


public class CastingTest {

    public void check(Video video) {
        if (video instanceof Film) {
            ((Film) video).print4D();
            return;
        }
        if (video instanceof Drama) {
            ((Drama) video).printGoods();
            return;
        }
        if (video instanceof Animation) {
            ((Animation) video).printSubtitle();
        }
    }
    public static void main(String[] args) {
        CastingTest ct = new CastingTest();

        ct.check(new Film());
        ct.check(new Drama());
        ct.check(new Animation());
    }
}
