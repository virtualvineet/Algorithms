import java.lang.*;
import java.util.*;
import java.util.Iterator;

class TimerThread extends Thread {
	pball p;
	final int SIMU = 600000;

	TimerThread(pball p) {
		this.p = p;
	}

	public void run() {
		System.out.println("Enter Timer thread ");
		try {
			Thread.sleep(SIMU);
			p.setflag();
		} catch (Exception e) {
		}
		System.out.println("Exit Timer thread ");
	}
}

class GenerateThread extends Thread {
	pball p;

	GenerateThread(pball p) {
		this.p = p;
	}

	public void run() {
		System.out.println("Enter pball thread ");
		p.simulatePowerball();
		p.printMetrics();
		System.out.println("Exit pball thread ");
	}

}

class presult {
	private final LinkedHashSet<Integer> val;
	private final int power;

	public presult(LinkedHashSet<Integer> val, int power) {
		this.val = val;
		this.power = power;
	}

	public LinkedHashSet<Integer> getSet() {
		return val;
	}

	public int getPower() {
		return power;
	}
}

class pball {

	private static boolean stop_flag;
	private static final Object flagLock = new Object();
	private int total_generation_count;
	private int success_count;

	// constructor
	public pball() {
		stop_flag = true;
		total_generation_count = 0;
		success_count = 0;
	}

	// function to print metrics
	public void printMetrics() {
		System.out.println("Total Generation Attempt:  "
				+ total_generation_count);
		System.out.println("No of Winning combination:  " + success_count);
	}

	public synchronized void setflag() {
		synchronized (flagLock) {
			stop_flag = false;
		}
	}

	public synchronized boolean getflag() {
		boolean flag;
		synchronized (flagLock) {
			flag = stop_flag;
		}
		return flag;
	}

	private Boolean compareSet(LinkedHashSet<Integer> G,
			LinkedHashSet<Integer> W) {
		Integer elem;
		if (G.size() != W.size()) {
			return false;
		}
		LinkedHashSet<Integer> Wcopy = new LinkedHashSet<Integer>(W);
		Iterator it = G.iterator();
		while (it.hasNext()) {
			elem = (Integer) it.next();
			if (Wcopy.contains(elem)) {
				Wcopy.remove(elem);
			} else {
				return false;
			}
		}
		return true;
	}

	// Geneate function to generate power sequence
	private presult generatePowerballOutcome(long seed) {
		Random rng = new Random(seed);
		int power, number;
		LinkedHashSet<Integer> RandomSet = new LinkedHashSet<>();
		while (RandomSet.size() < 5) {
			number = rng.nextInt(69) + 1;
			RandomSet.add(number);
		}
		power = rng.nextInt(26) + 1;
		presult result = new presult(RandomSet, power);
		System.out.println(" Random Set:  " + RandomSet + "  " + power);
		return result;
	}

	public void simulatePowerball() {
		presult result;
		Boolean ret;
		LinkedHashSet<Integer> W = new LinkedHashSet<Integer>(
				Arrays.asList(new Integer[] { 8, 27, 34, 4, 19 }));
		int win_powerball = 10;
		System.out.println("Winning Combination: " + W + " " + win_powerball);
		while (getflag()) {
			result = generatePowerballOutcome(System.nanoTime());
			if (result.getPower() == win_powerball) {
				ret = compareSet(result.getSet(), W);
				if (ret) {
					success_count++;
					total_generation_count++;
				} else {
					total_generation_count++;
				}
			} else {
				total_generation_count++;
			}

		}

	}
}

class powerball {
	public static void main(String args[]) {
		System.out.println("Welcome to Powerball");
		pball pinst = new pball();
		System.out.println("flag at instance: " + pinst.getflag());
		// Initialize the threads
		GenerateThread Gthread = new GenerateThread(pinst);
		TimerThread Tthread = new TimerThread(pinst);
		Gthread.start();
		Tthread.start();

	}

} // End PowerBall
