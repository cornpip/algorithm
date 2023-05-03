class Solution {
    int flag = 0;
    String ret = "";

    private void mode0(char c, int idx){
        if( c == '1' ) this.flag = 1;
        else if( idx % 2 == 0 ) ret += c;
    }
    
    private void mode1(char c, int idx){
        if ( c == '1' ) this.flag = 0;
        else if( idx % 2 == 1 ) ret += c;
    }

    public String solution(String code) {
        for(int i=0; i < code.length(); i++) {
            char c = code.charAt(i);
            if(this.flag == 0) mode0(c, i);
            else mode1(c, i);
        }
        if (ret.equals("")) return "EMPTY";
        return this.ret;
    }
}