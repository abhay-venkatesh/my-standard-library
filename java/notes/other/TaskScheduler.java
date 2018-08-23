public class TaskScheduler {
    /*
    tasks = {'A', 'B', 'C', 'A', 'A', 'B', 'A'}
    n = 2
    c = {..., (23 x 0), ..., 1, 2, 4}
    i = 24

    tasks.length = 7, 10
    A, B, C, A, B, _, A, _, _, A
    
    --- The Frame Business ---
    Basically, the idea is to use the most frequent task as the delimiter
    for the frames, and then since all the other tasks are at least as
    frequent as the most frequent task, then there will be at most
    only one instance of them occuring.
    */
    public int leastInterval(char[] tasks, int n) {

        int[] c = new int[26];
        for(char t : tasks) {
            c[t - 'A']++;
        }
        Arrays.sort(c);
        int i = 25;
        while(i >= 0 && c[i] == c[25]) i--;

        return Math.max(tasks.length, (c[25] - 1) * (n + 1) + 25 - i);
    }
}