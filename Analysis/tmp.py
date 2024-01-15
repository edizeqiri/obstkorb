import tlsh
def subresult(frame):
    existing_shm = shared_memory.SharedMemory(name=shm_name)
#   numi = np.ndarray(shape, dtype=dtype, buffer=existing_shm.buf)
    local_result = []
    for i in range(len(frame)):
        min_score = 10000
        winner = []
        score = 100000
        for j in range(len(numi)):
            if frame[i][3] == numi[j][3]:
                continue
            try:
                score = tlsh.diff(frame[i][0], numi[j][0])
            except:
                print(f"Error in tlsh: {frame[i][1]} and {numi[j][1]}, {frame[i][2]} and {numi[j][2]}, ")
            if score < min_score:
                min_score = score
                winner = [frame[i][1], numi[j][1], frame[i][2], numi[j][2], score]
        local_result.append(winner)
    return local_result