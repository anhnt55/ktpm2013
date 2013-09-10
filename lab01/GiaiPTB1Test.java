import static org.junit.Assert.*;
import org.junit.Test;

public class GiaiPTB1Test {
	//Ham test1 voi gia tri dau vao la 1 va 1
	@Test
	public void Test1() {
		GiaiPT pt = new GiaiPT();
		int kq = pt.giaiPTB1(1, 1);
		assertEquals(kq, -1);
	}

	//Ham test2 voi gia tri dau vao la 10 va -90
	@Test
	public void Test2() {
		GiaiPT pt = new GiaiPT();
		int kq = pt.giaiPTB1(10, -90);
		assertEquals(kq, 9);
	}
}
