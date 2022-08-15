def rotate_queue(queue, n):
    for _ in range(n):
        queue.enqueue(queue.dequeue())
