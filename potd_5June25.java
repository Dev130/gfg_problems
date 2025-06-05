import java.util.*;

class Solution {
    public int countPaths(int[][] edges, int V, int src, int dest) {
        // Step 1: Build adjacency list
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < V; i++) {
            graph.add(new ArrayList<>());
        }
        for (int[] edge : edges) {
            graph.get(edge[0]).add(edge[1]);
        }

        // Step 2: Initialize memoization array with -1
        int[] dp = new int[V];
        Arrays.fill(dp, -1);

        // Step 3: Call DFS + memoization
        return dfs(graph, src, dest, dp);
    }

    private int dfs(List<List<Integer>> graph, int current, int dest, int[] dp) {
        if (current == dest) return 1;
        if (dp[current] != -1) return dp[current];

        int totalPaths = 0;
        for (int neighbor : graph.get(current)) {
            totalPaths += dfs(graph, neighbor, dest, dp);
        }

        dp[current] = totalPaths;
        return totalPaths;
    }
}
