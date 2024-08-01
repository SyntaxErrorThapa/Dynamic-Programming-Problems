class Paging:
    
    
    def convert_address_sequence_to_page_reference(self, references, bytes_per_page):
        
        sequence = []
        # Using two pointer 
        l = 0
        r = 1
        sequence.append(references[l] // bytes_per_page)
        while r < len(references):
            reference_number_r = references[r] // bytes_per_page
            reference_number_l = references[l] // bytes_per_page
            if reference_number_l != reference_number_r:
                sequence.append(reference_number_r)
            r += 1
            l += 1
        return sequence
p = Paging()

print(p.convert_address_sequence_to_page_reference([100,432,101,612,102,504,101,611,803,104,101,610,
702,103,1004,101,609,102,105], 200))