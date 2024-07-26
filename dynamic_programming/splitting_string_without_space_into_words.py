import collections
class SplittingString:
    def split_sentence(self, dic, sentence):

        memo = {}
        
        def helper(dic, sentence):
            # Base case is if no more sentences 
            if not sentence:
                return []
            
            # Base case if found in memo for dynamic programming approach
            if sentence in memo:
                return memo[sentence]
            
            for word in dic:
                if sentence.startswith(word):
                    split_word_prefix = sentence[len(word):]
                    returned_list = helper(dic, split_word_prefix)
                    
                    if returned_list is not None:
                        memo[sentence] = returned_list +[word]
                        return memo[sentence]
            # Found no word that matches in the dic
            return None
        
        result = helper(dic, sentence)
        print(memo)
        return result
    
    def bottom_up_bfs_split_sentence(self, dic, sentence):
        
        # Split[prefix ] = list of words that form the prefix 
        splits = {"":[]}
        # Prefixes of the sentence that we have not processed yet
        prefixes_to_process = collections.deque([""])
        while prefixes_to_process:
            prefix = prefixes_to_process.popleft()
            if prefix == sentence:
                # Any split works. Return the first round 
                return splits[prefix]
            for word in dic:
                # Prefix matches the word  
                if sentence[len(prefix):].startswith(word):
                    next_prefix = prefix + word
                    if next_prefix not in splits:
                        splits[next_prefix] = splits[prefix] + [word]
                        prefixes_to_process.append(next_prefix)
        return None
                    
ss = SplittingString()
# print(ss.split_sentence(["cat", "cats", "eat", "mice"], "catseatmice"))
print(ss.bottom_up_bfs_split_sentence(["cat", "cats", "eat", "mice"], "catseatmice"))