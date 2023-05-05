class Solution {
    public int solution(int[][] board) {
        int answer = 0;
        int[][] cp = new int[board.length][board[0].length];

        for(int i=0; i<board.length; i++){
            for(int j=0; j<board[i].length; j++){
                if(board[i][j] == 1) boom(cp, i, j);
            }
        }

        // System.out.println(Arrays.deepToString(cp));
        for(int i=0; i<board.length; i++){
            for(int j=0; j<board[i].length; j++){
                if(cp[i][j] == 0) answer++;
            }
        }
        return answer;
    }

    private void boom(int[][] cp_board, int x, int y){
        for(int i=-1; i<=1; i++){
            for(int j=-1; j<=1; j++){
                int dx = x+i, dy = y+j;
                if(dx < 0 || dx > cp_board.length-1 || dy < 0 || dy > cp_board.length-1 ) continue;
                cp_board[dx][dy] = 1;
            }
        }
    }

}