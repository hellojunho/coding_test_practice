package bubble;
import java.util.Arrays;

public class Bubble {
	static int[] nums;

	public static void main(String[] args) {
		nums = new int[10];
		for (int i = 0; i < 10; i++) {
			nums[i] = (int) (Math.random() * 10);
		}
		System.out.println("before");
		System.out.println(Arrays.toString(nums));
		
		// 한 번의 반복이 완료될 때 마다 가장 큰 수는 배열의 가장 마지막 부분으로 밀리는 것이 보장된다.
		for(int i = nums.length - 1; i > 0; i--) {
			// 따라서, 한 번의 반복마다 가장 뒤의 인덱스는 비교하지 않도록 반복문을 설계할 수 있다.
			for(int j = 0; j < i; j++) {
				// 만일, 앞의 수가 뒤의 수보다 더 크다면 swap 연산을 진행해준다.
				if(nums[j] > nums[j + 1]) {
					int temp = nums[j];
					nums[j] = nums[j + 1];
					nums[j + 1] = temp;
				}
			}
		}
		
		System.out.println("after");
		System.out.println(Arrays.toString(nums));
	}
}