def compare_hashes(batch, full_array, col_index):
    results = []
    for item in batch:
        for other_item in full_array:
            if item[col_index] != other_item[col_index]:  # To avoid comparing with itself
                diff_score = tlsh.diff(item[col_index], other_item[col_index])
                results.append((item[0], other_item[0], item[1], other_item[1], diff_score))
    return results