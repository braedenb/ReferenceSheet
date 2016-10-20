import java.util.*;

public class TreeNode {
    public static void main(String[] args) {
        TreeNode A = new TreeNode("A");
        TreeNode B = new TreeNode("B");
        TreeNode C = new TreeNode("C");
        TreeNode D = new TreeNode("D");
        TreeNode E = new TreeNode("E");
        TreeNode F = new TreeNode("F");

        A.addChild(B);
        A.addChild(C);
        B.addChild(D);
        B.addChild(E);
        C.addChild(F);

        TreeNode.traverse(A, new Doer() {
            public void doit(TreeNode node) {
                System.out.println(node.value);
            }
        });
    }

    public String value = ""; // can be any type (int, float, whatever)
    public TreeNode parent = null;
    public ArrayList<TreeNode> children = new ArrayList<TreeNode>();

    public TreeNode(String value) {
        this.value = value;
    }

    public void addChild(TreeNode child) {
        child.parent = this;
        children.add(child);
    }

    interface Doer {
        public void doit(TreeNode node);
    }

    public static void traverse(TreeNode node, Doer doer) {
        LinkedList<TreeNode> toVisit = new LinkedList<TreeNode>();
        toVisit.push(node);

        while(toVisit.size() > 0) {
            // get the next node to visit
            TreeNode next = toVisit.pop(); // DFS
            // TreeNode next = toVisit.poll(); // BFS

            toVisit.addAll(next.children);

            // run our "function"
            doer.doit(next);
        }
    }
}
