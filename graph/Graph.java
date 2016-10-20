import java.util.*;

public class Graph {
    // Test code
    public static void main(String[] args) {
        Graph G = new Graph();
        G.connect("A", "B");
        G.connect("A", "C");
        G.connect("B", "C");
        G.connect("C", "D");

        System.out.println(G.isVertex("E"));
        System.out.println(G.isVertex("D"));
        System.out.println(G.neighbors("A"));
    }

    public HashMap<String, HashMap<String, Integer>> edges;

    public Graph() {
        edges = new HashMap<String, HashMap<String, Integer>>();
    }

    public void connect(String node1, String node2) {
        connect(node1, node2, 0);
    }

    public void connect(String node1, String node2, int weight) {
        if(!edges.containsKey(node1)) {
            edges.put(node1, new HashMap<String, Integer>());
        }
        if(!edges.containsKey(node2)) {
            edges.put(node2, new HashMap<String, Integer>());
        }

        edges.get(node1).put(node2, new Integer(weight));
        edges.get(node2).put(node1, new Integer(weight));
    }

    public boolean isVertex(String node) {
        return edges.containsKey(node);
    }

    public boolean areConnected(String node1, String node2) {
        return isVertex(node1) && edges.get(node1).containsKey(node2);
    }

    public int weight(String node1, String node2) {
        return edges.get(node1).get(node2).intValue();
    }

    public Set<String> neighbors(String node1) {
        return edges.get(node1).keySet();
    }
}
