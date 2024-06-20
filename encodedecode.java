class Solution {

    public String encode(List<String> strs) {
        StringBuilder encodedString = new StringBuilder();
        for(String str : strs){
            encodedString.append(str.length()).append("#").apppend(str);
        }
        return encodedString.toString();
    }

    public List<String> decode(String str) {
        List<String> decodedString = new ArrayList<>();
        int i=0;
        while(i<str.length()){
            int sepIdx = str.indexof("#",i);
            int len = Integer.parseInt(str.subString(i,sepIdx));
            i = sepIdx+1;
            String decodedString = s.substring(i,i+length);
            decodedStrings.add(decodedString);
            i=i+length;
        }
    }
}
 