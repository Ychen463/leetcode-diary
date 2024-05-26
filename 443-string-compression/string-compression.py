class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        
        read = write = 0
        while read < len(chars):
            char = chars[read]
            counter = 0
            while read < len(chars) and char == chars[read]:
                counter +=1
                read +=1
            # 以write写入chars
            chars[write] = char
            write +=1

            # 写入counter
            if counter >1:
                for c in str(counter):
                    chars[write] = c
                    print(c,counter, write)
                    write +=1
                    
        return write

            